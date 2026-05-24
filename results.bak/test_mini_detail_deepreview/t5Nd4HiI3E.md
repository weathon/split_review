## Summary

This paper identifies and addresses a real bottleneck in aligning Large Reasoning Models (LRMs) with human preferences: the high gradient variance induced by stochastic trace sampling when the intractable marginal preference loss is replaced with a single-trace surrogate. The authors propose BVPO, which mixes the standard trace-based gradient estimator with a low-variance "empty-trace" gradient (obtained by disabling reasoning) via convex combination. Theoretically, they prove variance reduction, MSE optimality of the mixing weight, and connect these to tighter SGD convergence bounds. Empirically, BVPO shows consistent gains over DPO and SimPO on AlpacaEval 2 (up to +7.8 points) and Arena-Hard (up to +6.8 points) across three model sizes, while also improving math reasoning performance.

---

## Strengths

1. **Identifies a genuinely novel and practically important problem.** The paper is the first systematic treatment of trace-induced gradient variance as a bottleneck for LRM preference alignment. Prior work (DPO, SimPO, KTO) was developed for conventional LLMs without reasoning traces and does not address this issue. The paper supports this motivation with empirical evidence in Appendix B showing substantially higher log-probability variance when trace generation is enabled versus disabled.

2. **Principled theoretical framework with guarantees.** Theorem 2 provides a closed-form MSE-optimal mixing coefficient and shows that the combined estimator dominates both individual estimators in MSE. Theorem 4 connects MSE minimization to per-step SGD convergence error, establishing a direct link between statistical optimality and algorithmic performance. This goes beyond the heuristic application of DPO/SimPO to LRMs.

3. **Consistent and practically meaningful empirical gains.** Table 1 shows BVPO outperforms DPO and SimPO on both Arena-Hard and AlpacaEval 2 across all three model sizes (1.5B, 7B, 8B) and in both Thinking and NoThinking modes. The gains are substantial (up to 7.8 points on AlpacaEval 2 win rate). Table 2 shows that alignment on general conversational data does not degrade — and in fact improves — math reasoning performance (up to +4.0 points average), addressing a practical deployment concern.

4. **Simple, drop-in method.** BVPO modifies only the loss function (a convex combination of two DPO-style losses) and is agnostic to the underlying preference optimization algorithm. This makes it practical and easy to adopt.

---

## Weaknesses

### Fatal
None.

### Major

1. **Uncontrolled comparison: BVPO trains on more data than baselines.** BVPO uses two datasets: the trace-based dataset $\mathcal{D}_t$ (original prompts with traces) and the empty-trace dataset $\mathcal{D}_e$ (prompts with " thinking response" appended, responses without traces). The baselines (DPO, SimPO) are trained only on $\mathcal{D}_t$. This means BVPO sees approximately twice as many training examples per source prompt. The reported gains could partially reflect this data augmentation advantage rather than the variance-reduction mechanism that the paper claims. A controlled ablation — training DPO on the combined dataset $\mathcal{D}_t \cup \mathcal{D}_e$, or training BVPO variants that isolate the effect of the mixing — is needed to attribute the improvement to gradient variance reduction. This is the most significant weakness in the paper.

2. **Missing key experimental details.** The mixing weight $\alpha$ used in the main experiments is not reported anywhere in the paper. Since the method is called "Bias–Variance Optimized" and Theorem 2 provides a closed-form optimal $\alpha$, the reader needs to know whether $\alpha$ was computed from the formula, tuned on a validation set, or set to a fixed value. This is essential for reproducibility and for understanding whether the claimed optimality is actually realized in practice.

### Minor

3. **No statistical significance or variance reporting.** The paper reports single numbers without confidence intervals, standard errors, or multiple-seed results. Given that some reasoning improvements are modest (e.g., BVPO at 83.0 vs. DPO at 84.0 on MATH-500 for R1-Qwen-1.5B), it is unclear whether these differences are within noise. This is especially important for the "avg@32" metric on small test sets.

4. **Theoretical analysis is partially standard.** Theorem 1 (variance reduction) is structurally trivial: $\text{Var}(\alpha g_t + (1-\alpha)g_e) = \alpha^2 \text{Var}(g_t)$ when $g_e$ is deterministic w.r.t. trace sampling, so the reduction is simply $\alpha^2$. The MSE optimality of convex combinations (Theorem 2) is a classic result. The theoretical novelty lies more in the *application* of these standard tools to the novel LRM alignment setting and the connection to SGD convergence, rather than in the results themselves. The paper would benefit from making this clearer.

5. **Empty-trace implementation is heuristic.** The method appends " thinking response" to the prompt to disable reasoning. The paper does not discuss whether this truly produces an empty-trace distribution — the model may still generate some reasoning. The quality of the empty-trace approximation and its impact on the bias $b_e$ is not examined.

### Trivial
None.

---

## Nice-to-Haves

- An ablation showing how performance varies with $\alpha$ on a validation set, which would also aid reproducibility.
- Direct measurement of gradient variance during training for $g_t$, $g_e$, and $g_c$, to empirically confirm the variance-reduction mechanism.
- A discussion of the empty-trace implementation's fidelity: does appending " thinking response" reliably disable reasoning, or could the model still generate internal reasoning?

---

## Removed Points

These points from the input reviews are removed or demoted with justification:

- **"Fundamental misalignment between theory and algorithm" (Critic Issue 1):** REMOVED. The critic claims the theory treats $g_c$ as an estimator of $\nabla \mathcal{L}_m$ while the algorithm optimizes $\mathcal{L}_c$, making the analysis "vacuous." This is a misunderstanding. The paper explicitly defines bias vectors $b_t = \mathbb{E}[g_t] - \mu$ and $b_e = \mathbb{E}[g_e] - \mu$, and the entire MSE analysis is built around the bias-variance trade-off. The SGD convergence analysis (Theorem 3) is the standard biased SGD framework (Ghadimi & Lan, 2013; Ajallocian & Stich, 2020; Karimireddy et al., 2022), which is correct: it bounds the gradient norm of $\mathcal{L}_m$ when using a biased estimator $g_c$. The bias is explicitly accounted for in the error floor. The theory is sound.

- **"The trace-based gradient is not an unbiased estimator of the marginal gradient" (Critic Issue 3):** REMOVED. The paper never claims it is unbiased. The bias $b_t$ is defined precisely as $\mathbb{E}[g_t] - \mu$. The critic's claim that "the paper never derives the actual bias" is true but irrelevant — the paper's framework is general and applies to any two estimators with well-defined bias vectors, regardless of the source of the bias.

- **"The theoretical results are standard" (Critic, Strengthening section):** DEMOTED to Minor. The paper explicitly credits prior work (Karimireddy et al., 2022; Ghadimi & Lan, 2013) for the SGD convergence analysis, so there is no misrepresentation. The novelty is in the application to LRM alignment and the MSE-optimal mixing framework.

- **"The paper's theoretical results are standard... the experimental evidence is undermined by the confound" (Critic, Overall):** The first part is correct but the paper does not overclaim theoretical novelty. The second part is addressed in the Major weaknesses above.

---

## Novel Insights

The harsh critic's most useful observation is the data augmentation confound, which is a genuine and important experimental gap. Conversely, the critic's claim that the theory is "fundamentally misaligned" with the algorithm reflects a misunderstanding of biased SGD analysis — the paper's theoretical framework is sound, and the bias-variance decomposition is correctly applied. The real tension in the paper is between the theoretical elegance of the MSE-optimal estimator and the practical difficulty of isolating its effect from the side-effect of training on more data. A strength-finder observation that the paper "links statistical optimality to SGD convergence" is accurate and captures the paper's most distinctive contribution.

---

## Suggestions

1. **Control for the data confound in the revision.** The cleanest fix: train DPO and SimPO on the *same combined dataset* ($\mathcal{D}_t \cup \mathcal{D}_e$) that BVPO uses, and report whether the gains persist. If they shrink, the variance-reduction story is weakened; if they persist, it is strongly supported. This single experiment would substantially strengthen the paper.

2. **Report the mixing weight $\alpha$.** State whether $\alpha$ was computed from the closed-form formula in Theorem 2 (and if so, what plug-in estimates were used for the bias and covariance terms), tuned on a validation set, or set heuristically. Include a sensitivity analysis.

3. **Add confidence intervals or multiple-seed runs.** At minimum, report standard errors for the main results (Table 1 and Table 2) to clarify whether the improvements are statistically significant.

4. **Measure and report gradient variance directly.** An empirical plot of $\text{Var}(g_t)$, $\text{Var}(g_e)$, and $\text{Var}(g_c)$ during training would directly validate the claimed mechanism.

---

## Score and Decision

**Calibration anchors used across all rounds:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| CVX-DPO (EVZnnhtMNX) | 3.00 | R1 | Much weaker: serious experimental flaws, unclear method. BVPO is significantly stronger. |
| Soft Alignment (28TLorTMnP) | 2.50 | R1 | Much weaker. |
| MODPO (2BfZMh9td4) | 4.25 | R1 | Weaker: limited contribution, direct extension of existing method. BVPO is more novel. |
| 3D-Properties DPO (9Hxdixed7p) | 6.25 | R1 | Comparable: thorough analysis but limited novelty of observations. BVPO is similar in quality. |
| DRPO (Lz5lOSC0zg) | 5.25 | R1 | Comparable: good experiments, rejected. BVPO has stronger theory. |
| DPO Generalization (bGkPZtisSm) | 5.25 | R1 | Weaker: pure theory paper, limited experiments. |
| Samplers in Online DPO (F6z3utfcYw) | 6.00 | R2 | **Most comparable anchor.** Both have solid theory + experiments with addressable weaknesses. Similar score justified. |
| TIS-DPO (oF6e2WwxX0) | 7.00 | R2 | Stronger: cleaner experiments, more novel method. BVPO is slightly below. |
| VPO (SQnitDuow6) | 5.50 | R2 | Weaker: serious experimental validity concerns (ARC-Challenge). |
| SPO (oK1zJCWBqf) | 5.80 | R2 | Comparable: rejected partly due to ablation concerns. BVPO is slightly stronger. |
| Learning Loss Landscapes (TU5ApbbeDZ) | 5.00 | R2 | Weaker: limited novelty, MuJoCo focus. |

**Round 1 bracket:** 5.0–7.0. **Round 2 narrowing:** After comparing against the Samplers in Online DPO (6.00, Accept) as the most similar anchor and noting that BVPO has a stronger problem motivation but a more significant experimental confound, I place the paper at 6.0.

The paper identifies a genuine problem, proposes a principled solution, and provides consistent empirical support. The main weakness — the uncontrolled data confound — is addressable in revision and does not invalidate the contribution. The theoretical framework is sound (the critic's "fundamental misalignment" claim is incorrect). The paper is a solid contribution to the emerging area of LRM alignment.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>