Now I have all the information needed to produce the final consolidated review.

---

## Summary

This paper proposes two algorithms for exact Geodesic PCA (GPCA) in the 2-Wasserstein space: one for centered Gaussian distributions (lifting to GL_d using the Bures-Wasserstein geometry), and one for general absolutely continuous measures (GPCAGEN, using neural network parametrizations of Otto's Riemannian structure). The goal is to solve the exact GPCA minimization problem — sum of squared Wasserstein projection residuals onto geodesic curves — without relying on the tangent linearization that underlies Tangent PCA (TPCA). The paper provides theoretical results including a lift to GL_d for the Gaussian case (Proposition 3) and a quantification of TPCA distortion (Proposition 4), and illustrates both methods on synthetic and real datasets.

## Strengths

- **Addresses a genuine gap in the literature.** Prior work on Wasserstein GPCA was limited to univariate measures (Bigot et al., 2017) or used generalized geodesics (Seguy & Cuturi, 2015). This paper is the first to propose algorithms for solving the *exact* GPCA problem (Equation 1) for multivariate absolutely continuous measures, using true Wasserstein geodesics rather than linearized approximations.

- **Theoretically grounded framing.** The lifting of GPCA to GL_d for centered Gaussians (Proposition 3) is mathematically sound and provides a clear connection between the Bures-Wasserstein geometry and a tractable optimization problem over invertible matrices and rotation variables. The analysis of when GPCA and TPCA differ (Proposition 4, the same-eigenvalue pathological case in Figure 4) is insightful and well-illustrated.

- **Novel parametrization for GPCAGEN.** Using Otto's parametrization (Equation 9) with MLPs to represent geodesics is a principled alternative to the more common McCann parametrization (which requires convex functions, typically enforced via ICNNs). The approach enables sampling along geodesic components and avoids hard architectural convexity constraints, which the paper correctly identifies as a trade-off rather than a free lunch.

- **Code provided.** Both the Gaussian GPCA code and GPCAGEN code are publicly available via GitHub repositories, which aids reproducibility.

## Weaknesses

### Fatal

None.

### Major

1. **GPCAGEN's experimental evaluation is almost entirely qualitative, and the paper does not provide the evidence needed to support the claim that it solves the exact GPCA problem.** There is no quantitative evaluation of the GPCA objective (Equation 1: sum of squared Wasserstein residuals) for GPCAGEN on any experiment — no values reported, no comparison against any baseline (TPCA, random geodesics, or even the training loss after convergence). The paper states that "a direct numerical comparison between the two methods is therefore not meaningful" (Section 5.2, Baselines) because TPCA acts on discrete measures while GPCAGEN learns continuous geodesics. However, this justification is unconvincing: one can compute the sum of squared Wasserstein projection residuals (Equation 1) *for any candidate geodesic, regardless of how it was produced*, by projecting empirical measures onto the geodesic and measuring the W₂ residuals. Even if the representations differ, the *objective function that defines the problem* can be evaluated uniformly. Without such a comparison, the reader cannot assess whether GPCAGEN improves on the simpler TPCA baseline, or whether it finds better geodesics than a random initialization. The claim that GPCAGEN solves the *exact* GPCA problem is not substantiated by the experiments as presented.

2. **No empirical verification that the learned curves are true geodesics.** GPCAGEN parametrizes curves as `μ(t) = (id + t∇f_ψ)_#(φ_θ_# ρ)`, which is a geodesic only if `id + t∇f_ψ` is a diffeomorphism for all `t` in the interval — equivalently, if the eigenvalues of `I_d + tH_{f_ψ}(x)` are positive for all `x`. The paper enforces this by monitoring eigenvalues over a finite set of samples and clipping `t_i` accordingly. This is a reasonable heuristic, but (a) the condition is only checked on sampled points, not in the continuous sense, and (b) gradient updates can violate it in unsampled regions. The paper provides no empirical check — e.g., verifying that `W₂²(μ(0), μ(t))` is proportional to `t²` along the learned curve — to confirm that the learned paths are length-minimizing. Without such verification, the curves optimized by GPCAGEN may not be geodesics, and the interpretation as a solution to Equation 1 is undermined.

3. **Missing implementation details that affect reproducibility.** The Gaussian GPCA optimization over `(Q_i) ∈ SO_d` and the horizontal constraint on X (Equation 12–13) is non-convex, but the paper does not specify how it is solved in practice (e.g., gradient-based optimization with manifold constraints, alternating minimization, initialization strategy). The Sinkhorn divergence `S_ε` is used as the loss for GPCAGEN, but the value of `ε` (and how it was chosen) is not reported. The batch size `m` (number of samples from ρ and ν_i per iteration) is not specified. These details matter: Sinkhorn bias depends on `ε`, and the quality of eigenvalue estimates for the geodesic constraint depends on `m`.

### Minor

1. **The "MNIST known geodesics" experiment (Section 5.2) does not serve as a ground-truth validation.** The paper constructs two geodesics by hand and shows that GPCAGEN can fit them. This demonstrates that the parametrization is expressive enough to recover given curves, but it does not test whether GPCAGEN finds the *correct* GPCA solution (minimizer of Equation 1) for an unseen dataset. This is analogous to verifying that a neural network can overfit a specific function, not that it generalizes or solves the intended optimization problem.

2. **No sensitivity analysis for the regularization coefficients.** The paper fixes `λ_I = λ_O = 1.0` for all experiments, stating this "ensures the algorithm works as expected," but does not report the actual values of the intersection and orthogonality losses after training, nor show what happens when these coefficients are varied. Since the second component's definition depends on satisfying these constraints, the reader cannot assess how well they are enforced in practice.

3. **The Gaussian GPCA experiments show that GPCA and TPCA are "generically" very similar** (<1% improvement on average), and the paper candidly notes that in the pathological case GPCA "may be seen as worse-behaved as TPCA" (Section 5.1). This raises the question of how often the harder GPCA problem is worth solving over the simpler TPCA — the paper does not provide practical guidance for when GPCA's extra complexity is justified.

### Trivial

- Figure 6 and several other figures are described with text that could be clearer about what exactly is being plotted.

## Nice-to-Haves

- A quantitative verification on a synthetic dataset with known ground-truth geodesics (e.g., interpolating between Gaussians, where the geodesic is a known Wasserstein barycenter path) to confirm that GPCAGEN recovers the correct GPCA solution and that the curves are length-minimizing.
- An ablation showing the effect of the Sinkhorn regularization parameter `ε` on the learned components.
- Reporting the actual optimized values of the intersection and orthogonality regularization losses after training.

## Removed Points

- **Criticism that the eigenvalue-based geodesic enforcement is fundamentally unsound / fatal**: The paper does provide a practical heuristic (eigenvalue monitoring + clipping), which is a reasonable engineering approximation given the continuous formulation. The criticism that it "does not guarantee the condition holds for the continuous function" is technically true but describes a standard limitation of any sample-based method. Demoted from Fatal to Major.
- **Criticism about ICNN vs. Otto's parametrization being a disadvantage**: The paper explicitly discusses this trade-off (Section 6). Both approaches have pros and cons; this is correctly framed as a design choice, not a weakness.
- **Criticism about missing related works**: The paper's related work section is appropriately scoped. Not included.
- **Reproducibility nitpicks about training logs, complete hyperparameter sweeps**: Standard for workshop/paper submissions. The paper provides architecture details (4 hidden layers of 128) and refers to Appendix E for more details (which was stripped by the parser, but exists in the original submission).
- **Strength about "avoiding ICNNs" being a clear advantage**: This is a trade-off (Hessian estimation cost vs. ICNN complexity), not a unqualified strength. Demoted to a neutral observation.
- **Strength about "continuous-distribution representation avoids discretization artifacts"**: Overclaimed — in practice, the method uses minibatch samples of ρ and ν_i, so it operates on discrete approximations. The advantage exists in principle but the paper's implementation does not fully realize it.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a genuine tension: the paper's core novel contribution (GPCAGEN for general measures) is the one with the weakest experimental support, while the better-supported contribution (Gaussian GPCA) is shown to be generically close to the simpler TPCA. This is not a contradiction — it is typical for first algorithms in a new space to need more thorough validation — but it means the paper claims more than the experiments currently justify.

## Suggestions

1. **Provide a quantitative comparison on the GPCA objective** (Equation 1). Evaluate `∑ᵢ W₂²(μ(tᵢ), νᵢ)` for both GPCAGEN and TPCA (and ideally a random geodesic baseline) on the same empirical distributions. Even if the representations differ, the residuals can be uniformly computed. This single comparison would substantially strengthen the paper.

2. **Verify the geodesic property empirically.** For a learned GPCAGEN curve, compute `W₂²(μ(0), μ(t))` at several `t` values and confirm it is linear in `t` (for the Otto parametrization of Equation 9, the squared distance should be `t²‖∇f‖²`). Report this for at least one experiment.

3. **Report essential missing details** in the main text: the Sinkhorn `ε` value, the batch size `m`, and how the `SO_d` optimization in the Gaussian case is solved.

## Score and Decision

### Calibration

**Round 1 — Bracketing:**
- Weak band (avg < 3.5): Anchors like *Fusion over the Grassmannian* (3.00), *Solving Schrodinger Bridge* (3.40) — these papers had fundamental flaws or very thin contributions. This paper is clearly above these.
- Middle band (avg 3.5–7.5): Anchors like *Wasserstein Flow Matching* (6.33, Reject), *Convergence Analysis of Wasserstein Proximal* (6.00, Reject), *Intrinsic Riemannian Classifiers* (5.00, Reject).
- Strong band (avg > 7.5): Anchors like *Comparing noisy neural population dynamics* (8.00, Accept), *DRO with Bias and Variance Reduction* (8.00, Accept). This paper is clearly below these.

**Initial bracket:** between 4 and 7.

**Round 2 — Narrowing:**
- *Wasserstein Flow Matching* (6.33, Reject): Similar setting (Wasserstein geometry + neural nets for distributions), more thorough experiments with quantitative comparisons, but the contribution was seen as more incremental. This paper has a stronger theoretical gap-filling aspect but weaker experiments. Comparable or slightly below.
- *Neural Sampling from Boltzmann Densities* (6.40, Accept): Stronger theoretical results, similarly limited experiments (2D only). This paper has less striking theoretical novelty but addresses a more direct problem.
- *Matrix Manifold Neural Networks++* (5.67, Accept): Mixed reviews, limited experiments on small datasets.
- *Disentangled Rep Learning / GMG* (5.50, Accept): Solid theory with limited experiments, accepted.
- *Intrinsic Riemannian Classifiers* (5.00, Reject): Incremental contribution with limited evaluation.

**Final bracket:** 5.0 to 6.0. This paper is most comparable to the 5.0–5.5 anchors. It has genuine theoretical merit and addresses a real gap, but the experimental validation of its main contribution (GPCAGEN) is substantially below the bar for acceptance.

### Calibration Anchors

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| Fusion over the Grassmannian | F5UgXkPgSn | 3.00 | R1 | Weaker: less coherent contribution |
| Solving Schrodinger Bridge | FjifPJV2Ol | 3.40 | R1 | Weaker: incremental |
| Wasserstein Flow Matching | HB4lr0ykTi | 6.33 | R1/R2 | Similar setting, more experiments, comparable overall quality |
| Convergence Analysis Wasserstein Proximal | WPz5e5V85k | 6.00 | R1 | Theory-heavy, limited experiments |
| Intrinsic Riemannian Classifiers | EyWKb7Ltcx | 5.00 | R1/R2 | Similar tier: limited evaluation, incremental |
| Probabilistic Geometric PCA | mkDam1xIzW | 7.33 | R1/R2 | Stronger: well-rounded methodology + experiments |
| Neural Sampling from Boltzmann | TUvg5uwdeG | 6.40 | R2 | Stronger theory, similarly limited experiments |
| Matrix Manifold Neural Networks++ | 30aSE3FB3L | 5.67 | R2 | Similar tier: mixed reviews, limited evaluation |
| Disentangled Rep Learning / GMG | ehr4oTe6XI | 5.50 | R2 | Similar tier: accepted with limited experiments |
| Compressed Online Sinkhorn | vA5Rs9mu97 | 5.50 | R2 | Similar tier, rejected |
| Geometry-aware Distance in Hyperbolic | IUmDBY4NOQ | 4.75 | R2 | Below: weaker contribution |

**Final score: 5.0.** The paper's theoretical contributions are real and the gap it addresses is genuine, but the experimental validation — especially for GPCAGEN, the more novel of the two proposed methods — is insufficient to support the central claim that the method "solves the exact GPCA problem." The quantitative evaluation gap (no objective values, no meaningful baseline comparison, no geodesic verification) is a major weakness that prevents acceptance in the current form. The paper would need substantial additional experiments before it could be accepted.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>