- Decision: Accept
- Avg Score: 7.33
- Scores: 6, 8, 8
Now I have all the information needed to produce the final consolidated review.

---

## Summary

This paper proposes SAFER, a scalable algorithm for conditional value at risk (CVaR) minimization in collaborative filtering. The core contribution is using convolution-type smoothing — borrowed from smoothed quantile regression — to make the non-smooth CVaR objective differentiable and separable, enabling a primal-dual splitting that recovers an ALS-like block coordinate solver with per-epoch complexity matching iALS. Experiments on MovieLens 1M, MovieLens 10M, and Million Song Dataset show that SAFER improves tail performance (at α=0.3) while maintaining iALS-level computational efficiency.

## Strengths

- **SAFER achieves superior tail performance while retaining iALS-level computational efficiency.** Table 1 shows SAFER's runtime per epoch is within ~7% of iALS (3.45s vs 3.16s on ML-10M; 57.0s vs 53.5s on MSD). Figure 1 (quantile-vs-quality) confirms clear improvements over iALS and other baselines for small α (tail users) on both ML-10M and MSD, directly supporting the paper's central claim.

- **Convolution-type smoothing resolves the non-separability that blocks scalable CVaR optimization.** Section 3.1 shows that after smoothing, the objective Ψ_{1-α} becomes block multi-convex in U, V, ξ. Section 3.3 then derives a primal-dual splitting that decomposes the U,V subproblem into re-weighted ALS problems with the same separable structure as iALS. This is a genuine structural advance over prior CVaR approaches (subgradient methods, piecewise-quadratic smoothing) that lack such separability.

- **Closed-form dual variable update avoids iterative inner optimization.** Section 3.3 derives z_i^{(t+1)} = 1 - K_h(-r_i^{(t)}), a simple evaluation of the kernel CDF, removing the need for iterative inner maximization per user and directly contributing to the algorithm's efficiency.

- **Robustness analysis with 50 independent data splits on ML-1M.** Figure 2 shows that SAFER consistently outperforms iALS and ERM-MF for both average-case (α=1.0) and tail performance (α=0.3) across 50 splits, demonstrating robustness beyond a single split.

## Weaknesses

### Fatal

None.

### Major

- **Main empirical results on the larger datasets lack variance estimates.** The headline results for ML-10M and MSD (Table 1, Figure 1) are reported as point estimates from a single train/test split. Only the smaller ML-1M dataset receives repeated evaluation (50 splits). Recommendation data splits have substantial variance, and without confidence intervals, error bars, or at minimum results across multiple random seeds, the reader cannot assess whether SAFER's improvements on the larger datasets are systematic or noise. The paper's claim that SAFER "shows excellent quality in most cases" is weakened by this evidential gap for the datasets where scalability matters most.

### Minor

- **Metric mismatch between the optimized objective and the evaluation metric.** SAFER optimizes CVaR of a *pointwise* loss (which is a convex separable upper bound on the pairwise ranking loss), but evaluates on Recall@K, a ranking metric. While the paper correctly notes the pointwise loss is an upper bound on pairwise loss (Section 2), there is no empirical verification that optimizing the CVaR of the pointwise objective actually translates to better tail Recall@K. The connection is plausible and theoretically motivated, but some analysis (e.g., plotting the CVaR objective value against tail Recall during training) would strengthen the causal chain from optimization to evaluation.

- **The algorithm lacks convergence guarantees, and the paper is transparent about this.** Section 5 notes "Lacking a theoretical convergence guarantee" and Section 3.3 says "Through numerical experiments, we will show this algorithm converges in practice." For a paper proposing a new optimization algorithm with multiple interacting components (smoothing, Newton-Raphson for ξ, primal-dual splitting, Tikhonov regularization), this is a meaningful gap. The empirical convergence analysis (Figure 6) only examines bandwidth — it does not verify convergence to a stationary point of the smoothed CVaR objective. This limits the paper's status as a complete algorithmic contribution.

- **The Tikhonov regularization strategy is under-justified and not ablated from the CVaR contribution.** Section 3.3 proposes specific Tikhonov weight formulas "based on condition numbers" but provides no derivation of these formulas or analysis of their effect. Since the paper notes regularization is "critical for ranking quality," and SAFER combines a new CVaR-aware objective with a new regularization scheme, readers cannot disentangle whether tail-performance gains come from the CVaR optimization, the new regularization, or both. An ablation running SAFER with standard iALS Tikhonov weights would clarify this.

### Trivial

- Hyperparameter search ranges (especially for bandwidth h) and the grid-search budget are not reported, which matters for reproducibility given the paper's own analysis shows h is critical for convergence (Section 5).
- The derivation of the closed-form dual update (Section 3.3, Eq. 244→245) uses the relationship ∇(ρ₁ * k_h)(x) = 1 - K_h(-x) as a step without deriving it; the paper could cite the specific lemma from Fernandes et al. (2021) to improve clarity.

## Nice-to-Haves

- A sensitivity analysis for the Newton-Raphson iteration count L (fixed to 5) and the user sampling ratio |U_b|/|U| (fixed to 0.1) would strengthen the empirical characterization of the algorithm.
- A heuristic or guideline for choosing the bandwidth h based on the scale of loss values would be practically useful, since the paper shows h strongly affects convergence and tail performance.

## Removed Points

These points were raised in the reviews but are removed after verification:

- *"Unfair comparison with CVaR-MF; using Adam stacks the deck against it"* — REMOVED. The paper uses Adam as a preconditioner for the batch subgradient baseline, which is a reasonable and standard choice. Adam is a strong optimizer, not a weak one; this criticism is speculative and factually questionable.
- *"Missing related works"* — REMOVED per guidelines (cannot verify external completeness).
- *"Table 1 is not visible in the extract"* — REMOVED. This is a parser artifact, not a paper weakness.
- *"Tikhonov regularization as a strength"* (from Strength Finder) — REMOVED. Conflicts with the verified weakness that the regularization is under-justified and not ablated from the core contribution.
- *"Generic strengths about importance of the problem"* (from Strength Finder) — REMOVED. These are superficial and conflict with the verification discipline.

## Novel Insights

The harsh critic and strength finder together surface a pattern that is not fully articulated in the paper itself: the paper's strongest empirical evidence is *runtime efficiency* (the per-epoch complexity within 7% of iALS, and wall-time convergence plots), while the weakest evidence is *tail performance generalization* (single-trial results on large datasets). This asymmetry is important — the efficiency claim is robust because it depends only on algorithm structure and measured FLOP-equivalent operations, while the performance claim requires statistical evidence that is only provided for the smallest dataset. The paper's framing emphasizes the performance result, but the more reliable contribution is the algorithmic efficiency. Separately, both reviews independently flagged the under-justified Tikhonov regularization as a confound — the paper would benefit from acknowledging this asymmetry explicitly and prioritizing the efficiency result.

## Suggestions

1. **Report variance on the main results**: Add results from 5+ random seeds (or independent train/test splits) for ML-10M and MSD with standard error bars or confidence intervals in Table 1 and Figure 1. Even a small number of repeats would significantly strengthen the empirical claims.
2. **Ablate the Tikhonov regularization**: Run SAFER with standard iALS Tikhonov weights and report whether the tail-performance gains persist. This would isolate the CVaR smoothing contribution from the regularization contribution.
3. **Add objective-vs-metric correlation**: Plot the training CVaR objective value against tail Recall@K during training for one dataset to empirically bridge the gap between the pointwise objective and the ranking evaluation.
4. **Report hyperparameter search ranges**: Include the grid or search ranges for h, λ, β₀, and the number of NR iterations L to aid reproducibility.
