- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 5, 5, 5
Now I have all the information I need. Let me produce the consolidated review.

## Summary

This paper proposes Scaff-PD, an accelerated primal-dual algorithm for distributionally robust federated learning (DRO in FL). The method combines Nesterov-style extrapolation on the dual variable with Scaffold-style control variates to correct client drift from local steps. Theoretically, it achieves an accelerated O(1/T²) rate for strongly-convex-concave problems and linear convergence exp(-O(T)) for strongly-convex-strongly-concave problems — the first such rates for federated DRO. Experiments on synthetic data show linear convergence, and on CIFAR-100 / TinyImageNet (using linear classifiers on pretrained ResNet-18 features) the method improves worst-20% accuracy over baselines.

## Strengths

1. **First accelerated and linear convergence rates for federated DRO.** Theorem 1 establishes O(1/T²) in the strongly-convex-concave setting; Theorem 2 establishes exp(-O(T)) linear convergence in the strongly-convex-strongly-concave setting. This is explicitly stated as "the first federated approach for the DRO problem that achieves linear convergence, let alone an accelerated rate" (Section 1, Contributions). If the proofs are correct (they reside in the appendix), this is a genuine theoretical advance over prior sub-linear rates.

2. **Well-motivated algorithm design combining APD and Scaffold control variates.** The algorithm is clearly described: the dual update uses Nesterov extrapolation for acceleration, while the primal update uses bias-corrected local steps (Algorithm 2) to handle data heterogeneity. The design choice to *not* perform local dual updates is justified by the practical constraint that clients lack cross-client loss information. The algorithm is compatible with secure aggregation.

3. **Improved worst-20% accuracy on real-world benchmarks.** Table 1 shows consistent improvements in worst-20% accuracy — e.g., CIFAR-100, α=0.01: Scaff-PD achieves 29.30% vs. next-best DRFA at 26.77%; TinyImageNet, α=0.01: 25.32% vs. 22.32%. The improvements are modest (2–3 pp) but directionally consistent with the DRO objective.

4. **Synthetic experiments directly validate linear convergence.** Figure 1 plots ‖x^R − x*‖² on a log scale; Scaff-PD curves are straight lines while the baseline DRFA flattens. This provides clean empirical support for the theoretical rate.

5. **Unified framework covering multiple fairness objectives.** Equation (1) and Section 3 show that varying ψ, Λ recovers agnostic FL (AFL), CVaR, Q-FFL, and game-theoretic solutions (Nash bargaining). This generality is a conceptual strength.

6. **Stochastic setting matches optimal rates.** Corollary 1 yields O(1/T) in the stochastic case, improving over the previous O(1/√T) rate for federated DRO.

## Weaknesses

### Major

1. **Real-world evaluation is restricted to linear models on frozen features, not end-to-end deep learning.** The experiments train only a *linear classifier* on top of a frozen, pretrained ResNet-18 feature extractor (Section 6.2, "Model setup"). This reduces the problem to a convex one, consistent with the strong-convexity assumption in the theory, but it means the paper's practical claims are validated only in a simplified regime. The conclusion states "strong empirical performance… improving upon existing approaches in both communication efficiency and model performance," yet no end-to-end deep network training is conducted. The paper does mention a "Train-Convexify-Train" approach (line 48), but this is not evaluated — the authors simply start from frozen pretrained features. This disconnect between the general framing (hospital networks, autonomous driving, medical imaging) and the evidence (convex classifier on fixed features) is significant.

2. **No statistical uncertainty quantification in any real-world result.** Table 1 reports single numbers for each method/metric/setting, with no standard deviations, confidence intervals, or multiple seeds. The data partitioning uses random Dirichlet allocation and client subsampling, both of which introduce stochasticity. Without variance estimates, it is impossible to assess whether the reported improvements (often 1–3 pp in worst-20% accuracy) are statistically meaningful or noise.

3. **Communication efficiency claim is not directly validated on real-world data.** The title and abstract foreground communication efficiency. The synthetic experiments do show per-round convergence, but the real-world experiments report only *final accuracy* after training. No training curves (accuracy vs. communication rounds) are provided for Scaff-PD vs. baselines on real data. Figure 2 shows curves but only for different ρ values of Scaff-PD (plus SCAFFOLD as a dashed line), not a full baseline comparison. The conclusion claims improvement "in both communication efficiency and model performance" on real-world datasets, but the evidence for the former on real data is absent.

### Minor

4. **Hyperparameter selection for real-world experiments is underspecified.** The paper describes grid search for synthetic data parameters (line 337) but provides no tuning procedure for the real-world experiments. Key choices (local steps J, learning rates, dual step sizes, regularization ρ) are not discussed for CIFAR-100 / TinyImageNet. This makes the results harder to reproduce and raises concerns about whether baselines were equally tuned.

5. **Only the χ² penalty variant of DRO is tested on real data.** The paper presents a unified framework covering CVaR and Q-FL objectives (Section 3) but only evaluates the χ² penalty on real benchmarks. Testing at least one additional variant would strengthen the generality claim.

### Trivial

6. Minor typo: "Supppose" → "Suppose" (line 239).

## Nice-to-Haves

- An ablation study isolating the contribution of the Scaffold-style control variates (i.e., Scaff-PD without bias correction, using FedAvg-style local steps within the APD framework).
- Communication cost comparison in bits/round, since Scaff-PD additionally communicates N scalars (losses) per round compared to pure gradient-based baselines.
- Explicitly stating the linear-model limitation in a dedicated limitations section, rather than embedding it in the model setup paragraph.

## Removed Points

These points are flagged to be removed; treat them with caution:

- *"Assumption 1 is technically redundant"* — This is a formality observation, not a weakness or error in the paper. The assumption is standard and harms nothing.
- *"No comparison of communication cost in bits/round"* — Moved to Nice-to-Haves; it is a suggestion, not a weakness.
- *"No ablation of bias correction"* — Moved to Nice-to-Haves.
- *"Did not test CVaR/Q-FL variants"* — Kept as minor weakness #5 above, which is appropriate.
- *"Limitations section is absent"* — The paper embeds its limitations in the model setup section (line 376–378), which is an acceptable format choice. The criticism is a formatting nitpick.
- *Criticism about proofs being in the appendix* — Per instructions, the parser strips appendix content; this is not an author error.
- *"Assuming correctness, the theoretical claims are credible"* — This hedging is the reviewer's uncertainty, not a flaw in the paper.

## Novel Insights

None beyond the paper's own contributions. The two reviews largely converge on the key trade-off: the theoretical contribution (first accelerated/linear rates for federated DRO) is genuinely novel and well-motivated, but the experimental section has material gaps that leave the practical claims under-supported.

## Suggestions

1. **Add training curves (accuracy vs. communication rounds) for real-world experiments.** This would directly validate the communication efficiency claim and is the single highest-impact addition.
2. **Re-run all real-world experiments with at least 3 random seeds** (different Dirichlet partitions and initializations) and report means ± std in Table 1.
3. **Either run a small-scale end-to-end non-convex experiment** (e.g., a 2-layer MLP on a simpler dataset) or **explicitly scope the claims** to the convex setting. The current framing oversells the practical evaluation.
4. **Document the hyperparameter selection procedure for real-world experiments** (grid ranges, validation metric, whether baselines were similarly optimized).
