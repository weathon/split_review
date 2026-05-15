Now I have all the information I need. Let me compile the final review.

---

## Summary

This paper identifies trace-induced gradient variance as a key bottleneck in aligning Large Reasoning Models (LRMs) with human preferences, and proposes BVPO — a method that combines a high-variance trace-based gradient estimator with a low-variance empty-trace gradient estimator via convex combination. The authors provide a theoretical analysis showing variance reduction (Theorem 1), MSE-optimal mixing (Theorem 2), and connection to SGD convergence (Theorems 3–4). Empirically, BVPO improves over DPO and SimPO on AlpacaEval 2 and Arena-Hard across three LRM scales, while also improving math reasoning performance despite training only on conversational data.

## Strengths

- **Well-motivated problem identification.** The paper clearly articulates why trace sampling creates high gradient variance in LRM alignment — a genuinely underexplored issue. The connection between stochastic trace length/log-probability fluctuations and optimization instability is intuitively and concretely motivated (§3.2, with empirical evidence referenced in Appendix B).

- **Sound and well-structured theoretical framework.** Theorems 1–4 build a coherent narrative: variance reduction from mixing (Thm 1) → MSE-optimal α with domination guarantees (Thm 2, Corollary 1) → convergence bound tightening under standard SGD assumptions (Thms 3–4). The mathematics is correct under the stated assumptions, and the progression from statistical to algorithmic optimality is cleanly argued.

- **Consistent empirical gains across scale and benchmarks.** BVPO outperforms DPO and SimPO on every (model, benchmark, mode) combination tested — three LRMs (1.5B, 7B, 8B), two alignment benchmarks (Arena-Hard, AlpacaEval 2), in both Thinking and NoThinking modes. Gains reach +7.8 LC win rate on AlpacaEval 2 for the 7B model.

- **Reasoning ability preserved and improved.** Despite using only general conversational preference data, BVPO not only avoids degrading math reasoning (a known risk during alignment) but improves average performance across six math benchmarks by up to 4.0 points. This is a practically important and non-obvious result.

- **Simple, drop-in method.** BVPO requires no architectural changes, no reward model training, and is formulated as a convex combination of existing gradient estimators, making it easy to adopt (§3.3).

## Weaknesses

### Fatal

None.

### Major

- **Theory–practice gap in the optimal mixing coefficient.** Theorem 2 derives a closed-form α\* in terms of unknown bias vectors, covariance matrices, and cross-covariance between g\_t and g\_e. The paper provides no method to estimate these quantities, uses a fixed α in experiments, and does not report what α value was used. The optimality guarantees therefore do not directly inform practice — the theory shows that an optimal α *exists* and what form it takes, but the experiments do not demonstrate that the chosen α approximates α\*. This weakens the claimed "principled link between statistical optimality and training stability."

- **No direct evidence for the claimed variance-reduction mechanism.** The central claim is that BVPO reduces trace-induced gradient variance, which in turn improves training stability. However, the paper provides no measurement of gradient variance for g\_t, g\_e, or g\_c during training. The only variance-related evidence referenced is log-probability and response-length variance (Appendix B, stripped), which is a proxy for gradient variance but not a direct measurement. Without training curves showing reduced gradient norm fluctuation or an α-sweep demonstrating the bias-variance trade-off in practice, the observed alignment improvements are consistent with BVPO's mechanism but not uniquely attributed to it.

### Minor

- **Asymmetric comparison with baselines.** BVPO's combined loss ℒ\_c = αℒ\_t + (1−α)ℒ\_e effectively trains on both trace-based and empty-trace data in each step, while DPO and SimPO baselines train only on trace-based data. The paper does not include a control that matches total gradient steps or effective data volume (e.g., DPO trained on a 50/50 mix of trace-based and empty-trace samples with double the updates). This makes it difficult to isolate whether the gains come from the mixed-gradient *operator* or simply from additional training signal diversity.

- **No error bars or seed variation.** The benchmark results in Tables 1–2 are reported as point estimates without confidence intervals or multiple-seed averages. Given that some improvements are modest (e.g., +1.8 average points for the 7B model on math benchmarks), the statistical significance of these gains is unclear.

- **Limited discussion of the empty-trace estimator's bias.** While the theory accounts for arbitrary bias in g\_e, the paper provides no empirical characterization of its magnitude or direction relative to μ. Theorem 2's MSE-optimal α\* depends critically on ‖b\_e‖² and b\_t^⊤b\_e, yet neither is estimated. An analysis of gradient alignment between g\_t and g\_e on even a small subset would substantially strengthen the bias-variance narrative.

### Trivial

- Key training hyperparameters (α, learning rate, β, batch size, number of epochs) are not reported in the main text. These are essential for reproducibility and evaluating the fairness of baseline comparisons.

## Nice-to-Haves

- An α-sweep experiment (α ∈ {0, 0.25, 0.5, 0.75, 1.0}) reporting both alignment performance and training dynamics would directly validate the bias-variance trade-off the paper builds its narrative around.

- Training curves (loss, gradient norm, evaluation metrics over steps) for BVPO vs. DPO would visually substantiate the stability claims.

- A comparison against a simple multi-trace averaging baseline (e.g., DPO with 2–4 traces averaged per preference pair) would help distinguish BVPO's mixing approach from other variance-reduction strategies.

- A compute-matched DPO baseline (equal total gradient steps, or equal wall-clock time) would strengthen the causal attribution of gains to BVPO's gradient mixing rather than increased data diversity.

## Removed Points

These points were flagged from reviewer input but removed from the main review for the reasons given. Treat them with caution.

1. **"g\_e is not an estimator of the same marginal gradient μ"** — REMOVED. The paper explicitly frames g\_e as a biased estimator of μ = ∇ℒ\_m, and Theorem 2 handles arbitrary bias vectors b\_t, b\_e. This is mathematically coherent: any function can serve as an estimator, and the theory accounts for its bias. Whether the bias is acceptably small is an empirical question the paper addresses through results, if not through direct measurement. The harsh critic's claim that this disconnect "invalidates the central narrative" is incorrect — the theoretical framework explicitly accommodates biased estimators.

2. **"PPO with reward on the final answer (DeepSeek-AI et al., 2025) is the most directly relevant prior approach and is omitted"** — REMOVED. The paper's scope is explicitly preference optimization methods (DPO and its variants), and it compares against the two most prominent representatives (DPO, SimPO). PPO belongs to a different family (RLHF with explicit reward models) and the paper acknowledges DeepSeek-AI et al.'s use of PPO. Adding PPO would be a nice-to-have but its absence is not a weakness.

3. **"The statement that the mixed gradient is agnostic to the preference optimization algorithm is misleading"** — REMOVED. The paper states this in §3.3 to mean that BVPO's gradient mixing can be applied to any preference optimization objective (DPO, SimPO, etc.), which is a reasonable and accurate claim. The harsh critic's interpretation that it "changes the training objective" misses the point — the mixing is at the gradient level and is indeed algorithm-agnostic.

4. **"The paper does not report whether baselines were tuned with the same search budget"** — PARTIALLY REMOVED / REFRAMED. This is folded into the more precise concern about data/compute asymmetry in the Minor weaknesses section above, rather than treated as a standalone omission.

5. **"The link to SGD convergence (Theorems 3, 4) is standard; the only novelty is the substitution"** — REMOVED. Theorems 3–4 adapt a known bound to the BVPO setting and establish that MSE-optimal α\* also minimizes the per-step SGD convergence error when ηL = 1. This is a valid synthesis connecting statistical and algorithmic optimality, not claimed as a fundamental advance in SGD theory. The paper is upfront that Theorem 3 is adapted from prior work.

6. **Formatting/style nitpicks** — REMOVED per instructions (parser artifacts, not author errors).

7. **"Missing appendix, absent references"** — REMOVED per instructions. The parser strips these sections; they exist in the original submission.

## Novel Insights

The key conceptual advance is reframing LRM preference optimization as a bias-variance trade-off over gradient estimators rather than as a loss-function design problem. Prior work on LRM alignment (including DeepSeek-AI et al.'s PPO approach) treats trace sampling as an unavoidable practical compromise; BVPO identifies the empty-trace gradient as a complementary low-variance signal and shows that convex combination yields provably better MSE. The result that alignment training on general conversational data can *improve* math reasoning (rather than merely preserving it) is an empirical finding with practical implications, though the paper does not deeply analyze the mechanism behind this transfer.

## Suggestions

- Report the value of α used in experiments and provide a brief α-sweep (even on a single model/benchmark) to demonstrate that performance is reasonably robust to this choice — this would partially close the theory-practice gap without requiring full bias/covariance estimation.
- Add gradient variance measurements (trace of empirical covariance of g\_t, g\_e, g\_c over a fixed batch) to directly validate the variance-reduction claim.
- Include at least one compute-matched or data-volume-matched DPO baseline to strengthen the causal attribution.
- Report key hyperparameters (α, learning rate, β, batch size) in the main text.

## Score and Decision

**Calibration anchors consulted:**

| Path | Avg Score | Decision | Comparison to paper under review |
|------|-----------|----------|----------------------------------|
| `btEiAfnLsX.md` | 6.67 | Oral | Stronger: tighter theory-practice connection, more rigorous proofs, clearer mechanism validation |
| `IobTEbQ3vt.md` | 6.00 | Poster | Stronger: more thorough variance decomposition, direct variance measurements, more extensive ablations |
| `8xSU8Oscvg.md` | 5.00 | Poster | Comparable: similar topic (LRM + preference optimization), similar empirical breadth, accepted as poster |
| `2uTxLC4LmC.md` | 5.00 | Poster | Comparable: similar topic (LRM alignment), some theory-practice gaps, accepted as poster |
| `axQgyubT4X.md` | 4.00 | Reject | Weaker: less substantive theory, narrower experiments, overclaimed contributions |
| `qgyDao3n8E.md` | 3.50 | Reject | Weaker: trivial/incorrect theory, limited experiments, marginal improvements |
| `0MUrJkJYnP.md` | 3.00 | Withdrawn/Reject | Weaker: narrow idealized setting, limited practical contribution |

The paper under review sits at the same quality level as the two accepted posters on LRM alignment (`8xSU8Oscvg` at 5.00 and `2uTxLC4LmC` at 5.00). It has more theoretical content than either, a well-motivated problem, and consistent empirical gains. Its main weaknesses — the theory-practice gap in α selection, missing direct variance evidence, asymmetric baseline comparison — are addressable and do not undermine the core contribution. It falls clearly above the rejected papers and below the oral-accept level.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>