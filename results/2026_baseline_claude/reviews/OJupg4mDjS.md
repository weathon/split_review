## Summary

This paper proposes two algorithms for exact Geodesic Principal Component Analysis (GPCA) on probability distributions under the Wasserstein metric: (1) a method for centered Gaussian distributions that lifts the Bures-Wasserstein GPCA problem to the flat space of invertible matrices (GL_d) via the quotient fiber bundle structure, and (2) a neural network-based method (GPCAGEN) for general absolutely continuous probability measures using Otto's fiber bundle formulation to parameterize geodesics with MLPs. The paper identifies a genuine gap in the literature—prior work either relied on linearization (TPCA) or addressed approximate/one-dimensional cases—and aims to fill it with exact GPCA methods.

---

## Strengths

- **Mathematically rigorous Gaussian case**: Proposition 3 cleanly reduces the GPCA problem over SPD matrices to a Euclidean optimization in GL_d with explicit projection times t_i. The lifting is elegant and principled, rooted in Proposition 1 (Takatsu/Malagò/Bhatia).

- **Quantified gap between GPCA and TPCA**: Proposition 4 analytically characterizes when TPCA distorts relative to GPCA, linking distortion to proximity of covariance matrices to the SPD cone boundary and the ratio |a−b|/(a+b). Figure 4 (right) corroborates this quantitatively with percentage improvement curves and standard deviation bands.

- **Novel geodesic parameterization avoiding ICNNs**: Using Otto's formulation, the authors parameterize geodesics through a general MLP f_ψ (whose gradient, not the function itself, needs to be computed) and a diffeomorphism φ_θ. This circumvents the architectural constraints of input-convex neural networks and is a non-trivial conceptual contribution.

- **Theoretical completeness for 1D Gaussians**: Proposition 5 proves that GPCA in the full a.c. space restricted to univariate Gaussians remains Gaussian, which is a clean theoretical result connecting the two algorithms.

- **Addresses a recognized open problem**: The paper explicitly identifies the gap—no exact GPCA method existed for R^d-valued a.c. measures—and its related work section honestly characterizes the state of prior art.

---

## Weaknesses

### Fatal
None.

### Major

1. **No quantitative evaluation of GPCAGEN**: For the general case, all evaluations are purely qualitative (visual inspection of point clouds and images). There is no measurement of reconstruction error, explained variance ratio, or objective value (Eq. 1) for GPCAGEN versus TPCA. Even for the synthetic MNIST geodesic verification experiment—where ground truth geodesics are known—no quantitative accuracy metric is provided. For an ML conference, qualitative-only results for the core novel algorithm are a significant gap.

2. **Scalability and computational cost absent**: No wall-clock time, memory usage, or scaling analysis is provided. GPCAGEN requires iterating over all n distributions, computing Hessians of f_ψ (which scale as O(d²) per sample), and running Sinkhorn divergences. For the 3D point cloud experiment (n=100 point clouds), users have no guidance on feasibility for larger datasets or higher-dimensional settings.

3. **"Exactness" claim is misleading as stated**: The paper repeatedly emphasizes that its methods are "exact" (in contrast to linearized TPCA). However, GPCAGEN uses finite-capacity MLPs, ε-regularized Sinkhorn divergences, minibatch stochastic optimization, empirically estimated Hessian eigenvalues, and a simplification R* = id for the orthogonality constraint. The "exactness" refers only to avoiding tangent-space linearization. This distinction should be clearly stated up front to avoid overclaiming.

4. **Optimization analysis absent for GPCAGEN**: The joint optimization over φ_θ, f_ψ, and (t_i) is highly non-convex. The paper provides no convergence analysis, no sensitivity study to initialization, and no ablation on the regularization coefficients λ_I and λ_O (only asserting "setting both to 1.0 works"). For a method claiming exact optimization of Eq. 1, the lack of any guarantee or empirical evidence of reaching good local optima is a weakness.

### Minor

1. The approximation of replacing the true rotation R* = ξ_{θ₂,ψ₂}(t²_inter) ∘ ξ_{θ₁,ψ₁}(t¹_inter)⁻¹ with R* = id (line 186) to enforce the orthogonality constraint is stated as a computational convenience, but its effect on the quality of the recovered components is not analyzed.

2. In the Gaussian near-boundary case (Figure 4), the authors note that GPCA can exhibit "undesirable effects" where some distributions project onto component boundaries, yielding poor separation. The paper does not provide guidance on when practitioners should prefer TPCA over GPCA in this regime.

3. The weather dataset experiment is described in terms of "two histograms for each state" and "empirical covariances"—it is unclear how a 2×2 covariance is computed from two separate 1D histograms for precipitation and wind speed, rather than joint 2D data.

### Trivial

- A code repository URL appears as a blank placeholder ("available at .") at the end of Section 5.2.

---

## Nice-to-Haves

- An ablation on λ_I and λ_O would clarify robustness of GPCAGEN to its main hyperparameters.
- Reporting the objective value of Eq. 1 for both GPCA and TPCA on real datasets would provide the quantitative backbone the empirical section currently lacks.
- A brief scalability analysis (training time as a function of n and d) would help practitioners assess feasibility.

---

## Novel Insights

The most genuinely novel insight is the use of Otto's fiber bundle formulation—where geodesics in Wasserstein space are projected from straight lines in Diff(Ω)—to parameterize geodesics via unconstrained MLPs rather than convex architectures. This decouples the parameterization of the transport map (φ_θ) from the geodesic velocity (∇f_ψ), avoids hard architectural constraints on convexity, and yields a differentiable loss amenable to stochastic gradient descent. The observation that orthogonality of geodesic components can be enforced as an L²(ρ) inner product condition on horizontal vector fields (following Proposition 2) is an elegant bridge between the abstract Riemannian structure and practical optimization.

---

## Suggestions

- Report the objective value of Eq. 1 for both methods on the 3D point cloud and image experiments, to substantiate the advantage of exact GPCA over TPCA numerically.
- Add training time and memory measurements for GPCAGEN across the experiments to ground the practical utility claims.
- State clearly in the abstract/introduction that "exact" refers to the avoidance of tangent-space linearization, not to the optimization being solved globally or the loss being exactly W₂² rather than S_ε.
- Consider adding a reconstruction experiment on the synthetic MNIST setting, reporting a pixel-level or Wasserstein-level distance between recovered geodesic samples and ground truth.

---

## Score and Decision

The paper addresses a well-recognized open problem with principled mathematical machinery, provides a complete and rigorous treatment for the Gaussian case, and proposes a creative neural-network approach for the general case using Otto's geometry. The theoretical contributions are solid and the paper is well-written. The main weaknesses are (1) the lack of any quantitative evaluation for GPCAGEN, (2) missing computational analysis, (3) insufficient optimization robustness evidence, and (4) the "exactness" framing needs qualification. These gaps are significant for an ML venue but do not undermine the core theoretical contributions.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>