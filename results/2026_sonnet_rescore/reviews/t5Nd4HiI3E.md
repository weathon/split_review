## Summary

BVPO proposes to address high gradient variance in preference-aligning Large Reasoning Models (LRMs) by mixing a high-variance trace-based gradient estimator $g_t$ with a low-variance empty-trace gradient estimator $g_e$: $g_c = \alpha g_t + (1-\alpha)g_e$. The paper provides a theoretical justification (variance reduction, MSE-optimal mixing weight, tighter SGD convergence) and demonstrates consistent empirical gains over DPO and SimPO on alignment benchmarks (AlpacaEval 2, Arena-Hard) as well as on six math reasoning benchmarks, across three LRMs at different scales.

---

## Strengths

- **Coherent theoretical framework directly supporting the method**: The paper provides a logically ordered sequence of formal results — Theorem 1 (variance reduction for any α ∈ (0,1)), Theorem 2 (closed-form MSE-optimal α* dominating both individual estimators), and Theorems 3–4 (convergence bounds governed by the bias-variance trade-off) — that together justify the design of $g_c$ and connect statistical optimality to algorithmic performance.

- **Consistent and substantial empirical alignment improvements across three model scales**: Table 1 shows BVPO outperforming the best baseline across all three models (1.5B, 7B, 8B), in both Thinking and NoThinking modes. In Thinking mode, BVPO gains up to 7.8 pts on AlpacaEval 2 win rate and 5.1 pts on Arena-Hard. In NoThinking mode, gains reach 6.8 pts on Arena-Hard and 6.9 pts on AlpacaEval 2 LC win rate. The breadth of models and evaluation modes makes this difficult to attribute to a single lucky configuration.

- **Preservation and enhancement of math reasoning despite training on non-math data**: Table 2 shows BVPO raising average math scores across six benchmarks (AIME24/25, AMC, Minerva, OlympiadBench, MATH-500) by up to 4.0 pts over the base model and exceeding DPO in most cases — a nontrivial and somewhat surprising finding that broadens the paper's significance.

- **Algorithm-agnostic, drop-in design**: The combined loss $\mathcal{L}_c = \alpha\mathcal{L}_t + (1-\alpha)\mathcal{L}_e$ is described as independent of the specific preference optimization algorithm (Section 3.3), making it easy to adopt in existing pipelines without architectural changes.

---

## Weaknesses

### Fatal
None.

### Major

- **Missing α=0 (empty-trace-only) ablation undermines the central claim**: The paper's core contribution is the *principled mixture* of $g_t$ and $g_e$, not simply replacing trace-inclusive training with trace-suppressed training. Yet Table 1 never evaluates $\mathcal{L}_e$ alone ($\alpha = 0$) — standard DPO applied to (prompt, answer) pairs with traces disabled. Without this, there is no way to determine whether the gains stem from the theoretically motivated convex combination or from simply avoiding the noisy trace-based gradient component. This alternative explanation is especially plausible given that BVPO's NoThinking-mode improvements (Table 1, last three columns) are consistently comparable to or exceed its Thinking-mode improvements, suggesting that the empty-trace component may be carrying much of the weight. Adding the $\alpha=0$ control is the minimum evidence required to support the paper's stated contribution; if BVPO beats $\mathcal{L}_e$ alone, the combination claim is validated cleanly.

### Minor

- **Theorem 4's ηL=1 condition sits at the boundary of the stability regime**: Theorem 3 establishes convergence for $\eta \leq 1/L$, while Theorem 4—the result formally linking MSE-optimality to SGD-optimality—requires exactly $\eta L = 1$. At this boundary, the convergence bound is the weakest within the admissible range. The paper acknowledges this as a "standard choice of learning rate," but practical implementations typically use considerably smaller step sizes. The claim that "minimizing MSE is equivalent to minimizing convergence error" strictly holds only at this corner case; the paper should acknowledge this limitation rather than presenting it as a general alignment of statistical and algorithmic optimality.

- **Reasoning improvement mechanism left unexplained**: Table 2 shows that training exclusively on UltraFeedback conversational data improves math reasoning performance (up to 4.0 pts average). The paper notes this finding but offers no mechanistic explanation — whether it arises from trace-length regularization, improved instruction-following, or other factors. While a full investigation is beyond the paper's scope, at least a brief discussion would strengthen the paper.

### Trivial

- **"Up to 4.0 points" framing in abstract favors the best-case model**: The 4.0-pt reasoning gain comes from the smallest (1.5B) model. For 7B it is 1.8 pts and for 8B it is 1.4 pts (Table 2). The framing "up to 4.0 points" in the abstract implies this is representative when it is the maximum; a balanced statement of the typical range would be more accurate.

---

## Nice-to-Haves

- **Sensitivity analysis over α**: Even a simple empirical curve showing performance as α varies across the three models would (i) confirm robustness around the chosen value, (ii) empirically support the theoretical claim that there exists an interior optimum, and (iii) give practitioners guidance. This is especially valuable given that the theoretically optimal α* is not directly computable from the quantities available during training.

- **Discussion of the ArmoRM–GPT-4 alignment assumption**: Preference data is scored using ArmoRM (Section 5.1) while alignment evaluation uses GPT-4-based judges (Arena-Hard, AlpacaEval 2). A brief note on ArmoRM–GPT-4 preference correlation and its potential effect on reported gains would strengthen rigor.

- **Scope note on the `<think></think>` convention**: The empty-trace mechanism (Section 3.3) depends on the model treating `<think></think>` as a signal to suppress reasoning. This is specific to DeepSeek R1 / Qwen-based LRMs and may not generalize to other architectures. Stating this scope explicitly would set appropriate expectations.

---

## Removed Points

*These points were flagged for removal. Treat with caution if revisiting.*

- **Practical α value unspecified (reproducibility concern)**: The harsh critic raised this as a failure. However, Section 5.1 explicitly states "Additional experimental details are provided in Appendix C," which is stripped from this extraction but is assumed to exist in the original submission per the review guidelines. This concern is likely addressed in Appendix C and cannot be confirmed as absent.

- **Abstract and introduction framing about "no systematic treatment"**: The critic noted that the claim ignores related discussion in technical reports. However, the authors explicitly reference DeepSeek-AI et al. (2025) and acknowledge that existing discussions are "sparse and limited to brief remarks in technical reports." This is a reasonable and accurate characterization, not an oversight.

- **ArmoRM scoring as a "mild concern"**: Removed from weaknesses because it is a standard practice in the field and the critic acknowledges ArmoRM correlates reasonably with human judgments. Retained only as a Nice-to-Have.

---

## Novel Insights

The paper's most noteworthy observation is that aligning LRMs with human preference using general conversational data (UltraFeedback), despite having no math content, measurably improves math reasoning performance across all three models. This is counterintuitive and suggests that some fraction of reasoning capability in current LRMs is bottlenecked not by mathematical knowledge but by alignment-adjacent properties such as instruction-following discipline or output regularity—properties that preference training on general data can improve. Understanding this transfer mechanism could have broad implications for training pipelines that typically treat alignment and capability tuning as separate phases.

---

## Suggestions

1. **Add the α=0 ablation**: Run all three models with $\mathcal{L}_e$ alone on AlpacaEval 2 and Arena-Hard and include in Table 1. This single addition either validates the mixture claim or productively reframes the contribution.
2. **Add an α sensitivity experiment**: Plot alignment performance against α ∈ {0.1, 0.2, …, 0.9, 1.0} for at least one model; show empirically where the optimum lies and how flat the curve is around it.
3. **Add a brief mechanistic discussion** of the UltraFeedback → math reasoning transfer finding, even if speculative, to help readers understand what alignment is doing to reasoning capability.
4. **State the exact α value used** in the main body (not only Appendix C) for reproducibility transparency.

---

## Score and Decision

**Originality**: The problem framing (bias-variance analysis of trace-induced gradient variance in LRM alignment) is novel and well-motivated. The solution is conceptually clean. **4/5**

**Importance**: LRM alignment is an underexplored but practically critical problem. The paper directly addresses it and provides both a method and a theoretical diagnosis. **4/5**

**Claims supported**: The alignment gains are well-supported across three models and two benchmarks. The reasoning improvement finding is reproducible. The theory is mostly correct with a minor boundary-condition caveat (Theorem 4). The core "mixture > either component" claim, however, is not fully supported due to the missing α=0 ablation. **3/5**

**Soundness**: Theory is generally sound. Experiments are well-conducted on appropriate models and benchmarks. The α=0 gap is the primary soundness concern. **3/5**

**Clarity**: Paper is clearly written, notation is consistent, and the method is easy to understand and implement. **4/5**

**Community value**: The paper addresses a real gap in LRM alignment, provides a practical drop-in method, and surfaces insights about trace variance as a bottleneck. **4/5**

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>