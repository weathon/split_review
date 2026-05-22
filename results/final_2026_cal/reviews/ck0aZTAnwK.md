Now I have all the calibration data I need. Let me produce the final consolidated review.

## Summary

This paper studies data-constrained pre-training under the premise of unlimited compute. It shows that standard recipes (increasing epoch count or parameter count) overfit. By tuning weight decay 30× above the standard practice of 0.1, the authors recover monotonic power-law scaling in parameter count. They propose evaluating recipes via their asymptote (loss as N→∞ or K→∞) rather than at a fixed compute budget. The key findings are that ensembling independently trained small models achieves a lower loss asymptote than scaling a single model, and that composing both (joint scaling) yields an estimated 5.17× data efficiency improvement at 200M tokens. Distillation preserves most ensemble gains in a smaller model. The paper is well-motivated, clearly written, and its qualitative findings are practically useful.

## Strengths

- **Identifies and quantifies overfitting in data-constrained recipes**: Shows convincingly that increasing epoch count or parameter count under fixed data eventually increases validation loss (Figure 2). This contradicts the monotonic improvement assumed by prior data-constrained scaling laws (Muennighoff et al., 2023) and is clearly demonstrated across multiple configurations.

- **Discovers that 30× larger weight decay than standard practice is necessary for monotone scaling**: By jointly tuning weight decay, learning rate, and epochs via coordinate descent, the paper shows that over-parameterized models require weight decay up to 3.2 (vs. the standard 0.1 from Brown et al., 2020). With this tuning, loss monotonically decreases following a power law for models up to 140× larger than Chinchilla proportions (Figure 3). This is a concrete, actionable finding likely to influence practice.

- **Introduces asymptote-based evaluation for data-constrained pre-training**: Rather than comparing models at a fixed compute budget, the paper proposes evaluating scaling recipes by their loss asymptote (lim_{N→∞} or lim_{K→∞}). This is a principled framing for the infinite-compute, finite-data regime and enables clean comparison of fundamentally different approaches (parameter scaling vs. ensemble scaling).

- **Demonstrates that ensembling achieves a lower asymptote than parameter scaling**: Averaging logits of independently trained 300M models yields a loss asymptote of 3.34, lower than the regularized single-model asymptote of 3.43 (Figure 4). Even a K=3 ensemble outperforms the entire regularized parameter-scaling limit. This is a non-obvious and practically relevant finding.

- **Shows distillation retains most ensemble gains without increasing inference parameter count**: Distilling an 8-ensemble of 300M models into a 300M student preserves 83% of the ensemble's loss improvement over the best regularized 300M model (Section 6.1). The student (loss 3.36) outperforms the regularized recipe's asymptote (3.43) while being 8× smaller. Self-distillation (same-size teacher and student) also improves over the teacher (Figure 8), suggesting data efficiency gains without large-parameter training.

## Weaknesses

### Major

- **Power-law fits use only 4 data points per curve, making quantitative claims (exponents, data efficiency multiples) more precise than the evidence warrants**. The regularized parameter scaling law (L(N) = A/N^α + E) and ensemble scaling law (L(K) = A/K^α + E) are each fit to only 4 data points (150M, 300M, 600M, 1.4B parameters or K=1,2,3,5 ensemble members) with 3 free parameters — leaving 1 degree of freedom per curve. The exponents (≈1.02 for both parameter and ensemble scaling) are suspiciously identical, suggesting the fitting procedure may be producing artifacts or that the functional form is underdetermined. The 5.17× data efficiency number at 200M tokens involves three layers of curve fitting (K→∞, then N→∞, then D-scaling), each on 4 points, amplifying uncertainty. While the paper notes asymptote variance of 0.02 across seeds (Appendix I), this does not account for exponent uncertainty. The paper should provide uncertainty intervals on fitted parameters and present the 5.17× figure as a rough estimate (e.g., "roughly 4–6×") rather than a precise number. The qualitative findings (regularization helps, ensembling helps more) are independently robust, but the quantitative precision is overstated.

- **Downstream validation is limited to 3 small-scale accuracy benchmarks (PIQA, SciQ, ARC Easy) without confidence intervals or per-benchmark breakdowns in the main text**. The paper reports 9% average improvement for the best ensemble, but absolute accuracy numbers and per-benchmark breakdowns are deferred to Appendix G. At 200M tokens and ~300M parameters, these benchmarks have high variance. The paper would benefit from reporting a held-out validation loss from a distribution-shifted corpus (beyond i.i.d. DCLM) to test whether the data efficiency gains generalize across distribution shifts.

### Minor

- **The self-distillation result is presented as a single data point (green star in Figure 8) with no sensitivity analysis.** The finding that a same-size student outperforms its teacher is interesting and consistent with theory (Allen-Zhu & Li, 2023), but the paper does not report the synthetic data amount D' used, the data mixing ratio, whether any filtering was applied, or how sensitive the outcome is to these choices. Given the literature on model collapse from training on synthetic data, this experiment deserves more careful documentation.

- **The asymptote comparison between parameter scaling (N→∞, K=1, asymptote 3.43) and ensemble scaling (N=300M, K→∞, asymptote 3.34) conflates two fundamentally different regimes.** The gap is only 0.09 loss, and with the noise in the fits (0.02 from Appendix I), this gap is small enough that better tuning of the parameter-scaling law could close or reverse it. The paper appropriately addresses this by then studying joint scaling (N,K→∞), but the individual comparison in Section 4 should be more measured.

- **The joint scaling hyperparameter tuning uses a heuristic (2× epochs, 0.5× weight decay from the regularized recipe) rather than a full search**, as acknowledged in Section 4.3. This is a practical concession, but it means the joint scaling asymptote (and hence the 5.17× number) may not reflect the true optimum of the combined recipe.

### Trivial

- The 9% improvement figure should clarify whether this is relative or absolute improvement. The paper says "over 9% on average" (Section 7) without specifying which baseline, or whether the comparison is relative to the best unregularized model's error rate or accuracy.

## Nice-to-Haves

- A comparison or discussion of how the reported 5.17× data efficiency gain from regularization + ensembling compares conceptually to alternative data-constrained approaches such as synthetic data rephrasing (Maini et al., 2024) or diffusion LMs (Prabhudesai et al., 2025). The paper mentions these in related work but does not discuss how they relate to the reported efficiency multiples.
- A cross-distribution validation loss (e.g., on a different data source than DCLM) would strengthen the claim that validation loss improvements generalize beyond the training data distribution.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Standard recipe baseline doesn't tune weight decay"** (from Harsh Critic): This is the paper's central point — standard practice uses weight decay 0.1 from Brown et al. (2020), and the paper shows that tuning it to 30× larger recovers monotone scaling. The framing is accurate: standard practice *does* neglect weight decay tuning under data constraints. This is a valid finding, not a weakness.
- **"Coordinate descent details in appendix"**: The paper references Appendix C.1 for details. The appendix is stripped by the PDF parser; this is not an author omission.
- **"Free lunch ignores computational cost"**: The paper's premise is explicitly unlimited compute. Criticizing within-scope assumptions is not a valid weakness.
- **"Contradiction with Muennighoff partially explained by regime"**: The paper itself acknowledges the regime difference. This is a discussion point, not a weakness.
- **"Pure formatting nitpicks" and "typos"**: These are parser artifacts, not author errors.

## Novel Insights

Beyond the paper's own contributions, the most striking emergent observation is the *symmetry* of the two scaling exponents (≈1.02 for both parameter scaling and ensemble member scaling under regularization). If this symmetry holds with tighter experimental controls, it would suggest a deeper invariance: the excess loss under data-constrained, optimally-regularized pre-training decays as roughly 1/(total independent optimization trajectories) regardless of whether those trajectories are concatenated into a larger model or averaged across separate models. This would imply a unification of parameter scaling and ensemble scaling under a single "independent learned components" count, with implications for architecture design in data-constrained regimes.

## Suggestions

- Provide uncertainty intervals (confidence regions) on all fitted power-law exponents and asymptotes. Even bootstrapped intervals from the existing 4-point fits would be informative.
- Present the 5.17× figure as a range (e.g., 4–6×) to better reflect the underlying uncertainty from multiple layers of curve fitting.
- Add per-benchmark accuracy breakdowns and confidence intervals to the main text for the downstream evaluation.
- Report the synthetic data amount, mixing ratio, and any filtering used in the self-distillation experiments.

## Score and Decision

**Round 1 — Bracketing**: The paper sits between the weak anchors (avg scores 1.0–3.33, all Reject/Withdrawn) and the strong anchors (avg scores 8.0 on different topics). The middle-band anchors on relevant topics score 4.40–6.80. Initial bracket: 5–7.

**Round 2 — Narrowing**: Compared to "How to train data-efficient LLMs" (avg 6.80, Poster), the paper under review has more novel methodological contributions (asymptote framework, ensemble-vs-parameter comparison) but weaker quantitative precision and narrower downstream evaluation — slightly below this anchor. Compared to "Scaling Laws Revisited" (avg 6.0, Poster), the paper has stronger qualitative findings but similar issues with quantitative fragility — comparable or slightly above. Compared to "Revisiting Scaling Properties of Downstream Metrics" (avg 6.0, Poster), the paper is more original and has richer experiments — slightly above this anchor.

**Final score: 6.0** — The paper makes solid, practically-relevant contributions (the importance of aggressive weight decay under data constraints, the advantage of ensembling over parameter scaling, the asymptote evaluation framework). Its main quantitative claims (the 5.17× figure, exponents ≈1) are overstated relative to the evidential base of 4-point power law fits, and the downstream evaluation is thin. These limitations are real but not fatal — the core qualitative findings are well-supported and likely to influence practice.

**Calibration anchors consulted** (all rounds):
| Anchor ID | Avg Score | Round | Comparison |
|-----------|-----------|-------|------------|
| jYrdhGvjVY | 3.33 | 1 | Weak — Reject, clearly below this paper |
| zCpVdWaIEp | 1.00 | 1 | Weak — Reject, clearly below this paper |
| 1m4cKCr0vx | 2.50 | 1 | Withdrawn/Reject, clearly below this paper |
| anAHXnrTVW | 3.00 | 1 | Withdrawn/Reject, clearly below this paper |
| x54wwB6QvL | 6.00 | 1 | Comparable quality, slightly narrower scope |
| 0BkvUY61MX | 5.33 | 1 | Larger scope but weaker execution, comparable |
| Ym33xJYINV | 6.00 | 1 | Comparable quality and limitations |
| v3mJ4f4Mnc | 4.40 | 1 | Weaker — Reject, paper is stronger |
| VKGTGGcwl6 | 8.00 | 1 | Different topic (multi-turn conversation), stronger paper |
| qOyF214xmg | 8.00 | 1 | Different topic (transducing LMs), stronger paper |
| oBXfPyi47m | 8.00 | 1 | Different topic (RL), stronger paper |
| kkBOIsrCXh | 8.00 | 1 | Different topic (embodied navigation), stronger paper |
| qPKTDOJ5Xs | 6.00 | 2 | Less directly comparable (theoretical), comparable |
| qBAV2DEvAC | 5.50 | 2 | Theoretical scaling laws, comparable quality |
| dSdLqg02tx | 6.00 | 2 | Different focus (convexity), comparable quality |
| YnJ2s4WeNF | 6.00 | 2 | Similar scaling-law/downstream topic, paper is more original |
| yKUbw7q1IA | 6.80 | 2 | Richer empirical study but less novel findings — slightly above this paper |
| T5wkZJqzkz | 6.00 | 2 | Different focus (LR decay), comparable quality |
| jpz7e3jhRq | 6.50 | 2 | Different focus (MLM vs CLM), comparable |
| 2FZC0c06jP | 6.50 | 2 | Different focus (proxy models), comparable |

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>