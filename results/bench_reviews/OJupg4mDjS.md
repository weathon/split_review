Now I have all the information I need. Let me write the consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses

### Fatal
None

### Major
- weakness 1 — why it matters

### Minor
- weakness 1 — why it matters

### Trivial
- weakness 1

## Nice-to-Haves
- suggestion that would improve but is not a core flaw

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision

Let me now write the full review.

---

## Summary

This paper tackles Geodesic PCA (GPCA) in the Wasserstein space of probability measures. It provides two algorithms: (1) for centered Gaussian distributions, lifting the problem to the space of invertible matrices via Bures-Wasserstein geometry, and (2) for general absolutely continuous measures (GPCAGEN), parameterizing geodesics through Otto's construction using MLPs. The Gaussian case is theoretically well-grounded with a clean formulation and distortion analysis; the a.c. case introduces a novel neural parametrization that avoids input-convex neural networks.

## Strengths

1. **Rigorous geometric lifting for Gaussian GPCA.** The paper formulates GPCA on centered Gaussians by lifting from the SPD manifold to GL_d using the horizontal line parametrization (Proposition 3). This makes the geodesic optimization tractable and geometrically principled, with explicit projection times and a clean optimization problem over invertible matrices and rotations.

2. **Theoretical characterization of the GPCA/TPCA gap.** Proposition 4 derives a closed-form expression for the distortion between the true Bures-Wasserstein distance and its linearized approximation at the barycenter. The result shows that distortion depends on (a−b)²/(a+b)², and Figure 4 validates that GPCA improves cost by up to ~35% when this ratio is large (near the cone boundary). This provides a measurable justification for preferring exact GPCA over TPCA in high-curvature regimes.

3. **Novel neural parametrization of Wasserstein geodesics avoiding ICNNs.** The paper parameterizes geodesics as μ_{θ,ψ}(t) = (id + t∇f_ψ)_#(φ_θ_#ρ) using standard MLPs for both φ_θ and f_ψ, bypassing the need for input-convex neural networks required by McCann's convex parametrization. This is a genuinely novel technical contribution that opens a new direction for neural Wasserstein geometry.

4. **Provable submanifold consistency for univariate Gaussian GPCA.** Proposition 5 proves that for univariate Gaussian distributions, the first principal geodesic component stays within the Gaussian submanifold, establishing that the restriction to Gaussians is lossless in 1D. The paper honestly notes the higher-dimensional case remains open.

## Weaknesses

### Major

1. **Insufficient experimental validation of GPCAGEN for the a.c. case.** The paper claims GPCAGEN "solves the exact GPCA problem" and that the components "minimize the cost in equation 1," but the experiments for the a.c. case do not quantitatively demonstrate this. The evidence consists of: (a) an MNIST experiment where the ground-truth geodesics are known by construction (a sanity check that the optimization can recover known structure), and (b) purely qualitative visualizations on 3D point clouds and landscape images showing interpretable components. There is no quantitative evaluation of the objective value in equation 1, no comparison to any baseline on the same cost, no measurement of whether the orthogonality constraint is satisfied within tolerance, and no ablation of the regularization terms λ_I, λ_O. The Gaussian experiments are well-validated, but GPCAGEN — the paper's main novel contribution for a.c. measures — lacks the experimental rigor needed to support the central claim.

2. **No quantitative comparison to TPCA on the a.c. experiments.** The paper states that "a direct numerical comparison between the two methods is therefore not meaningful" because GPCAGEN works on continuous distributions while TPCA acts on discrete measures. While this is a legitimate concern for a direct objective-value comparison, the paper could still compare on synthetic benchmarks where ground truth is known, or evaluate downstream metrics (e.g., reconstruction quality, clustering purity). The Gaussian experiments show GPCA improves the objective by <1% on average over TPCA, which undercuts the practical motivation for GPCA; without any quantitative evidence that GPCAGEN outperforms TPCA in the a.c. setting, the value proposition of the method remains unclear.

3. **The intersection constraint over-constrains the second component.** The paper enforces ξ₁(t¹_inter) = ξ₂(t²_inter) in Diff(Ω) (equality of the diffeomorphisms themselves) rather than merely requiring the projected measures to intersect. The paper acknowledges that the geometrically correct approach would use a rotation R* and that "computing R* is computationally expensive, and we therefore preferred to impose ξ₁ = ξ₂ which directly yields R* = id." This is a strictly stronger condition — two geodesics representing the same probability measure at the intersection point but through different diffeomorphisms would be penalized. The paper does not analyze the effect of this discrepancy on the recovered components.

### Minor

1. **Optimization dynamics of the t_i clipping are not analyzed.** In Algorithm 1, the projection times t_i are clipped to [t_min, t_max] using min/max operations. When t_i falls outside this interval, the gradient of the clipped value w.r.t. t_i is zero, meaning gradient descent cannot "pull" t_i back into the valid range through gradient information — t_i can only re-enter through changes in t_min, t_max (i.e., changes in f_ψ's Hessian eigenvalues). The paper does not analyze whether this optimization converges reliably or whether t_i values become stuck at boundaries. While the experiments appear to work, this is a potentially fragile mechanism that deserves discussion.

2. **No sensitivity analysis for regularization hyperparameters.** The second component objective has three terms (data fit + intersection + orthogonality) with coefficients λ_I and λ_O, both set to 1.0 in all experiments. No ablation study is provided showing how results change when these coefficients vary, or what the final orthogonality/intersection violations are after training. This makes it difficult to assess whether the constraints are actually satisfied or whether the method is sensitive to these hyperparameters.

3. **Gaussian experiments show GPCA and TPCA are nearly equivalent in typical cases.** The paper honestly reports that GPCA reduces the objective by <1% on average over TPCA for randomly generated covariance matrices. The "pathological" same-eigenvalue example where GPCA differs significantly is acknowledged to potentially yield "undesirable effects" and "poor separation." This raises the question of whether the practical benefit of exact GPCA over the simpler TPCA is marginal in most realistic settings.

### Trivial

1. The paper uses Sinkhorn divergence as a differentiable approximation of W₂² but does not discuss the effect of the entropy regularization parameter ε on the recovered geodesics.

## Nice-to-Haves

- A synthetic benchmark for the a.c. case where the true first GPCA component is known analytically (beyond the MNIST construction), with quantitative recovery error measured.
- Convergence trajectories of the t_i variables during training to demonstrate that the clipping mechanism does not cause optimization issues.
- Reporting of final orthogonality violation and intersection violation after training for the second component experiments.
- Computational cost analysis (training time, number of iterations) for the reported experiments.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"The paper's central claim is unsupported"** (from Harsh Critic Point 1): The critic conflates "solves the exact problem" (meaning the algorithm optimizes the exact objective without linearization) with "proves global optimality." The paper's claim is that the method optimizes the exact GPCA objective, which is what the algorithm does. The MNIST experiment provides meaningful validation that the optimization recovers known ground-truth geodesics. The criticism is overstated in severity, though the underlying concern about insufficient quantitative validation is valid and retained above.

- **"Comparison to TPCA is evaded"** (from Harsh Critic Point 2): The paper provides a principled justification for why a direct numerical comparison is not meaningful (continuous vs. discrete representations). The paper also provides qualitative TPCA comparisons in the appendix showing discretization artifacts. The critic's framing as "evasion" is too harsh; the retained weakness above captures the legitimate concern about missing quantitative evidence.

- **"Proposition 5 significance is unclear"** (from Harsh Critic): This is a clean theoretical result that establishes submanifold consistency. Its significance is clearly stated — it shows the restriction to Gaussians is lossless in 1D. The critic's dismissal is unwarranted.

- **"The algorithm description is vague"** (from Harsh Critic Section 4 notes): The paper describes how t_min, t_max are estimated from Hessian eigenvalues over a minibatch. This is a standard practical approximation. The critic's demand for analysis over all ℝ^d is unrealistic for a practical algorithm.

- **Strength Finder's "Empirical validation on diverse real-world datasets"**: This claimed strength conflicts with the verified weakness about insufficient quantitative validation. The qualitative demonstrations show interpretable components but do not constitute rigorous empirical validation. Moved here per the rule that when a strength and weakness disagree, the weakness wins.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add quantitative validation for GPCAGEN.** Construct a synthetic benchmark of a.c. measures where the true first GPCA component is known analytically (e.g., measures constructed via a known diffeomorphism from ρ), and measure GPCAGEN's recovery error. Report the final objective value (equation 1) and compare against a simple baseline (e.g., the mean measure as a trivial geodesic).

2. **Report constraint satisfaction.** For the second component experiments, report the final orthogonality violation ⟨∇f_ψ(φ_θ), ∇f_{ψ₂}(φ_{θ₂})⟩_{L²(ρ)} and the intersection error after training. This would validate that the regularization terms actually enforce the intended constraints.

3. **Ablate λ_I and λ_O.** Show how varying these coefficients affects the trade-off between data fit and constraint satisfaction. This would help readers understand the sensitivity and guide hyperparameter choice.

4. **Analyze the t_i clipping dynamics.** Show convergence trajectories of the t_i variables during training to demonstrate that the clipping mechanism does not cause optimization pathologies.

## Score and Decision

**Calibration anchors** (all from the human review corpus):

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `/home/wg25r/review_agent/human_reviews_2026/l3KtyVZde3.md` | 7.00 (Accept) | Stronger paper: solid theory AND well-executed experiments with baselines across multiple domains. The current paper has weaker experimental validation. |
| `/home/wg25r/review_agent/human_reviews_2026/xZNoeX0z9f.md` | 6.50 (Accept) | Similar in having strong theory but experiments limited to synthetic/low-dimensional settings. The current paper's a.c. experiments are more qualitative. |
| `/home/wg25r/review_agent/human_reviews_2026/e439wJl5sT.md` | 6.00 (Accept) | Had some experimental gaps (no approximation error evaluation) but still had quantitative results. The current paper's a.c. validation is weaker. |
| `/home/wg25r/review_agent/human_reviews_2026/JQ0SIA2IA1.md` | 5.33 (Reject) | Had mixed scores with some experimental limitations. The current paper has stronger theory but similar experimental gaps. |
| `/home/wg25r/review_agent/human_reviews_2026/e1JW30momq.md` | 3.50 (Reject) | Weaker paper: scalability issues, unclear relevance to ML. The current paper is substantially stronger in theory and relevance. |
| `/home/wg25r/review_agent/human_reviews_2026/L0DTflYss0.md` | 1.50 (Withdrawn) | Essentially an unfinished draft. Not comparable. |

The paper has genuine theoretical contributions (Gaussian GPCA lifting, distortion analysis, novel neural parametrization) and the approach is principled. However, the experimental validation of GPCAGEN — the paper's main novel contribution for a.c. measures — is insufficient to support the central claims. The experiments are almost entirely qualitative, with no quantitative evidence that the method minimizes equation 1 better than alternatives, no ablation studies, and no analysis of optimization dynamics. The Gaussian experiments, while well-executed, show that GPCA and TPCA are nearly equivalent in typical cases, which undercuts the practical motivation. Relative to the anchors, the paper sits below the acceptance threshold set by papers like l3KtyVZde3 (avg 7.00) and xZNoeX0z9f (avg 6.50), which had stronger experimental validation for their core claims.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>