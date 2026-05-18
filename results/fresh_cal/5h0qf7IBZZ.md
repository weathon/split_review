Now I have all the information needed. Let me write the consolidated review.

## Summary

This paper proposes MiniLLM, a white-box knowledge distillation method for large language models that replaces the standard forward KL divergence objective with reverse KL divergence. The authors derive a policy-gradient optimization for this objective and introduce three stabilization strategies: single-step decomposition, teacher-mixed sampling with importance weighting, and length normalization. Experiments across three model families (GPT-2, OPT, LLaMA) with sizes from 120M to 13B on five instruction-following datasets show consistent improvements over SFT, word-level KD, and SeqKD baselines in terms of Rouge-L, GPT-4 feedback, and human evaluation.

## Strengths

1. **Well-motivated and novel formulation of KD for generative LLMs.** The paper clearly identifies a genuine problem: forward KL forces a low-capacity student to overestimate void regions of a teacher's complex generative distribution. The toy Gaussian mixture experiment (Figure 1) cleanly illustrates this, and connecting it to reverse KL's known mode-seeking behavior is a principled framing that distinguishes MiniLLM from prior KD approaches.

2. **Consistent and substantial improvements across diverse settings.** Table 1 shows MiniLLM outperforming all baselines on nearly every configuration — 3 model families, sizes from 120M to 13B, and 5 datasets — using both automatic and GPT-4 metrics. The improvements are not marginal (e.g., GPT-4 scores improve by 3-10+ points over the best baseline in many cells), and MiniLLM students sometimes exceed the teacher, which directly supports the claim that on-policy training alleviates exposure bias.

3. **Three practical optimization strategies with clean ablations.** The single-step decomposition, teacher-mixed sampling, and length normalization are well-motivated and their individual contributions are clearly ablated (Table 6/Figure 6). Removing length normalization drops validation Rouge-L from 27.4 to 17.4, and removing teacher-mixed sampling drops it to 22.3, demonstrating these are not superficial additions but essential components.

4. **Complementary analyses strengthen the core claims beyond raw scores.** The exposure bias analysis (Figure 5), calibration evaluation (Table 3), and length-based analysis (Figure 6) provide mechanistic evidence for *why* MiniLLM works — not just that it works — which is a hallmark of a well-rounded empirical paper.

## Weaknesses

### Major

- **The reverse-KL objective is not isolated from the policy-gradient optimization framework.** The paper's central scientific claim is that reverse KL is superior to forward KL for generative LLM distillation (Section 2.1). However, MiniLLM optimizes reverse KL via policy gradient (on-policy sampling, reward shaping, importance-weight clipping), while the baselines (SFT, KD, SeqKD) optimize forward KL via teacher-forcing maximum likelihood. These differ in *both* the objective and the entire optimization paradigm. Without a forward-KL variant trained under the same PG framework (e.g., replacing the reward $r_t = \log(p/q)$ with $-\log(p/q)$ and keeping the three strategies identical), we cannot attribute the gains to the objective rather than the optimization machinery. The ablation study tests the three strategies on reverse KL only and does not control for this confound. This does not invalidate MiniLLM as a working method — it works clearly — but it weakens the attribution of *why*.

- **The importance-weight approximation introduces unanalyzed bias.** In Eq. 8–9, the full importance weight $w_t = \prod_{t'=1}^t \frac{q_\theta(y_{t'}|\dots)}{\tilde{p}(y_{t'}|\dots)}$ is replaced with $w_t \approx \frac{q_\theta(y_t|\dots)}{\tilde{p}(y_t|\dots)}$ to reduce variance. The paper acknowledges the variance motivation but does not analyze the *bias* this introduces. Since both single-step and long-term gradient terms use this approximation, the estimated gradient no longer corresponds exactly to $\nabla\mathcal{L}(\theta)$. How large this bias is, and whether it varies by model size, training stage, or the mixing coefficient $\alpha$, is unknown. This is a methodological gap that warrants either formal analysis or an empirical comparison on a small scale.

### Minor

- **The language modeling preservation loss $\mathcal{L}_{\text{PT}}$ has no reported weighting hyperparameter.** The paper states the final update uses $(\nabla \mathcal{L})_{\text{Single}} + (\nabla \mathcal{L})_{\text{Long}}^{\text{Norm}} + \nabla \mathcal{L}_\text{PT}$ (line 126, Algorithm 1), but does not specify any loss weight or coefficient. If the gradients are simply summed without tuning, the PT gradient may dominate or be dominated by the KD gradients. The paper should report whether a weight was used and how it was selected.

- **No factuality or hallucination evaluation despite the paper's emphasis on "correctness and faithfulness" (Section 1).** The paper evaluates calibration on classification tasks (SST-2, BoolQ), which is informative but does not directly measure factual accuracy or hallucination rates in free-form generation. For a method whose narrative emphasizes truthful generation, this is a notable gap.

- **The exposure bias analysis (Figure 5) uses only one teacher–student pair (GPT-2 125M/1.5B).** While the result is convincing, generalizability across model families and sizes is not demonstrated for this specific analysis.

- **The human evaluation (Figure 3) reports aggregate win/tie/loss without annotator count, inter-annotator agreement, or the exact instructions given to annotators.** These details are important for assessing reliability.

- **The length normalization formula $R^{\text{Norm}}_{t+1} = \frac{1}{T-t-1}\sum_{t'=t+1}^T \log\frac{p}{q}$ has an edge case when $t = T-1$:** the denominator becomes zero. This edge case is not discussed, though it may not arise in practice if generation stops at EOS.

- **Only one value of the teacher-mix strength $\alpha=0.2$ is used throughout.** A sensitivity analysis over $\alpha$ would strengthen the robustness claims, especially since the teacher-mixed sampling is one of the core three strategies.

### Trivial

- The claim that "white-box KD for LLMs is yet to be explored" (p. 2) is slightly overstated given prior work like DistilBERT and the paper's own citation of concurrent GKD/f-div-KD. "Under-explored for generative LLMs at scale" would be more precise.

## Nice-to-Haves

- A forward-KL variant of MiniLLM (same PG framework, negated reward) to isolate the role of the objective — this is the single highest-leverage additional experiment
- Computational cost / training time comparison with baselines, since PG-based training is likely more expensive than teacher-forcing
- Generative calibration metrics (e.g., ECE on token-level probabilities during generation) instead of only classification ECE
- A formal limitations section discussing sensitivity to teacher quality, mode-collapse risk, and the requirement of a white-box teacher

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"The paper does not state whether code or model checkpoints will be released"** — Removed per hard rules: reproducibility concern about release status is not a valid criticism of the paper's scientific content.
- **"R_t notation inconsistency"** — The paper uses $(R_t-1)$ in Eq. 4 and $R_{t+1}$ in Eq. 5. These arise from different algebraic forms of the same REINFORCE gradient derivation (one expanded, one not). This is a standard algebraic manipulation, not an inconsistency.
- **"The gradient decomposition (Eq. 5) is not fully spelled out"** — Not a weakness per se; the decomposition is described and notation is defined. The derivation follows standard policy gradient and the paper's citations cover the omitted steps.
- **"Rouge-L 'aligns better with human preference' claim is not justified"** — The paper directly cites Super-NaturalInstructions for this claim. It is a standard citation, not an unjustified assertion.
- **"The teacher may overfit the training distribution"** — This is speculative and applies equally to all baselines; the paper's design is standard practice in the distillation literature.
- **"KD baseline implementation details not given"** — Sufficient detail is provided for reproduction; the level of detail is standard for this venue.

## Novel Insights

The most interesting observation from the reviews is that MiniLLM's success may be at least partially attributable to the *on-policy sampling* enabled by the policy-gradient framework rather than exclusively to the reverse-KL objective. This suggests a deeper insight: the key benefit of distillation methods for generative LLMs may be how they bridge the train-test discrepancy (exposure bias), with the choice of divergence measure being a secondary factor. The paper's own exposure bias analysis (Figure 5) supports this interpretation — MiniLLM's error accumulation flattens after ~150 tokens while baselines keep rising. This points toward a unified view where on-policy training dynamics matter as much as, if not more than, the particular f-divergence being minimized.

## Suggestions

1. **Add a forward-KL control experiment.** Implement a forward-KL variant of MiniLLM by replacing the reward $r_t = \log(p/q)$ with $-\log(p/q)$ (or equivalently $\log(q/p)$) and training under the same PG framework with the three strategies. If MiniLLM outperforms this variant, the case for reverse KL is substantially strengthened. If not, the paper should reframe its contribution as "policy-gradient-based on-policy distillation" rather than "reverse-KL distillation."

2. **Analyze the bias from the importance-weight approximation** either through a formal bound or a small-scale empirical comparison of the full-importance-weight version (even if high-variance) against the approximate version.

3. **Report a sensitivity analysis** for the teacher-mix strength $\alpha$ and the (currently unspecified) weighting of $\mathcal{L}_{\text{PT}}$.

4. **Add a generative factuality evaluation**, such as TruthfulQA or a human-annotated hallucination rate on model generations.

## Score and Decision

**Calibration anchors** (all from the human-review corpus):

| Path | Avg Score | Comparison to MiniLLM |
|------|-----------|----------------------|
| Wv9Gl1bFbc (Dynamic Self-Distillation) | 3.00 | Much weaker: incremental idea (CVPR paper applied to NLP), poor presentation, weak experiments. MiniLLM is substantially more novel and thorough. |
| 1TJSnL3ywS (LLM Distillation for MCQA) | 4.00 | Weaker: narrow scope (MCQA only), simple data-generation approach. MiniLLM tackles the harder problem of generative distillation with broader evaluation. |
| IcVSKhVpKu (Hidden State Matching via CKA) | 5.67 | Weaker in scope: focuses on encoder/encoder-decoder models at smaller scales; experimental setup is acknowledged as "outdated." MiniLLM works with modern decoder-only LLMs at scale. |
| 8wjWm5jr1w (Multi-Granularity Semantic Revision) | 6.00 | Comparable topic but weaker empirical results: improvements are mostly marginal (<1 Rouge-L) except for OPT; methods are complex with unclear intuition. MiniLLM has cleaner motivation and larger gains. |
| cqsw28DuMW (TAID) | 7.33 | Comparable quality: both have strong motivation and comprehensive experiments. TAID has theoretical analysis; MiniLLM has broader model coverage (120M-13B across 3 families) and more detailed mechanistic analyses (exposure bias, calibration). MiniLLM's key weakness (objective confounded with optimization) is somewhat analogous to TAID's heuristic interpolation mechanism. |
| xsx3Fpo3UD (ADPA) | 7.50 | Slightly stronger: cleaner motivation for preference alignment, very strong empirical results. MiniLLM has broader evaluation (more models, datasets, analyses) but a more significant methodological confound. |

MiniLLM is clearly above the 5-6 range papers. It is roughly comparable to TAID (7.33) — both have strong motivations, clean ablations, and broad experiments, with different trade-offs in their main weaknesses. The reverse-KL isolation concern is real but does not undermine the paper's practical contribution as a working method. **Score: 7.0**

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>