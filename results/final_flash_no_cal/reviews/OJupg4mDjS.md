Now I have a thorough understanding of the paper. Let me compile the final consolidated review.

## Summary

This paper addresses Geodesic Principal Component Analysis (GPCA) in the Wasserstein space of probability measures. It proposes two algorithms: (1) a method for centered Gaussian distributions that lifts the GPCA problem to the space of invertible matrices (GL_d) via the Bures-Wasserstein geometry, yielding a tractable optimization over matrices and rotations; and (2) GPCAGEN, a neural-network-based method for general absolutely continuous measures that parametrizes Wasserstein geodesics using Otto's fibration with MLPs, avoiding input-convex neural networks. The Gaussian method is evaluated quantitatively with comparisons to tangent PCA (TPCA), while GPCAGEN is demonstrated qualitatively on MNIST, 3D point clouds (ModelNet40), and landscape image color distributions.

## Strengths

- **Gaussian GPCA via Bures-Wasserstein lifting (Proposition 3, Eq. 12):** The paper cleanly reformulates GPCA for centered Gaussians as a constrained optimization over GL_d and rotation variables, replacing the non-linear Bures-Wasserstein distance with the Frobenius norm. This yields a principled algorithm that directly targets the exact GPCA objective without linearizing the manifold.

- **Analytical quantification of TPCA distortion (Proposition 4, Fig. 4):** The paper derives a closed-form expression showing when the linearized Bures-Wasserstein distance deviates from the true distance (covariances near the boundary of the SPD cone) and demonstrates up to ~35% cost improvement of GPCA over TPCA in such regimes. This provides concrete insight into when the exact method matters.

- **Neural parametrization of Wasserstein geodesics without ICNNs (Section 4, Algorithm 1):** Using Otto's formulation, GPCAGEN parametrizes principal geodesics via unconstrained MLPs (f and φ) rather than requiring input-convex networks. This is a clever architectural choice that makes the optimization more tractable, with the trade-off of needing Hessian eigenvalue estimation — an approach that may be of independent methodological interest.

- **Controlled recovery of known geodesics (MNIST experiment, Fig. 5):** The MNIST experiment demonstrates that GPCAGEN can recover two known orthogonal geodesics in a constructed setting, providing evidence that the optimization does find the intended structure when the ground truth is known.

## Weaknesses

### Fatal
None.

### Major

1. **Lack of quantitative evaluation for GPCAGEN on real-world data.** The experiments for the general method (Section 5.2) are almost entirely qualitative. The paper shows interpolations along learned geodesics and describes components as capturing intuitive variation (brightness, chair vs. armchair, etc.), but reports no objective value (Eq. 1), reconstruction error, variance explained, or any other numerical metric on any real dataset. The MNIST experiment is a helpful sanity check on constructed data, but for ModelNet40 and landscape images the reader cannot verify whether the optimization actually drives the intended cost to a reasonable value. Without this evidence, it is unclear whether GPCAGEN truly solves the posed GPCA problem or merely produces plausible-looking interpolations. The paper itself describes these as "preliminary experiment" and "illustrations," which is honest, but the central claim of providing an exact GPCA method for general measures requires stronger validation.

2. **Restrictive orthogonality constraint for higher components with unmeasured impact.** The second principal geodesic is constrained to intersect the first in the *top space* Diff(Ω) (i.e., ξ₁ = ξ₂ at intersection), which is a stronger condition than intersecting in the base probability space. The paper acknowledges this and mentions a more flexible alternative (using R*), but dismisses it as computationally expensive without quantifying how severely this restriction affects the result. It remains unclear whether the resulting second component can be considered the true second principal geodesic under the Wasserstein metric, or whether the restriction biases the solution in an uncontrolled way. The paper does not measure this gap.

3. **Gap between the theoretical geodesic parametrization and practical implementation is under-discussed.** The theory (Proposition 2, Eq. 9) requires φ to be a diffeomorphism and id + t∇f to be a diffeomorphism for all t. In practice, φ_θ is an unconstrained MLP with no invertibility guarantee, the eigenvalue bounds for t_min/t_max are estimated from a finite batch rather than the full domain, and the exact Wasserstein distance is replaced by the Sinkhorn divergence. The paper mentions these choices but does not critically discuss how they affect the guarantee that the learned curve is exactly a Wasserstein geodesic or that the method truly solves the "exact" GPCA problem it claims to address. While "exact" is defined relative to linearization (not numerical precision), the accumulation of approximations deserves a more systematic discussion.

### Minor

- **No quantitative baseline comparison for GPCAGEN.** The paper dismisses a direct numerical comparison with TPCA as "not meaningful" but does not attempt any approximate quantitative bridge (e.g., discretizing GPCAGEN geodesics into point clouds and comparing Wasserstein reconstruction error). The qualitative TPCA comparison (showing discretization artifacts) is suggestive but does not substitute for a numeric assessment.

- **Optimization challenges not discussed.** The Gaussian GPCA involves non-convex optimization over SO_d rotation variables; the paper does not discuss initialization strategies, risk of local minima, or solution stability across random seeds.

- **Sinkhorn hyperparameters undefined in main text.** The entropy regularization parameter ε and number of Sinkhorn iterations — which control the quality of the W₂² approximation — are not stated in the main paper (deferred to the appendix). These should be at least summarized.

- **No runtime or complexity analysis.** The method trains multiple neural networks; some discussion of computational cost would help potential users assess practicality.

### Trivial
None.

## Nice-to-Haves

- A dedicated limitations paragraph in the Discussion section, covering the orthogonality restriction, dependence on the reference measure ρ, the diffeomorphism requirement in practice, and computational overhead.
- Reporting the optimized value of the GPCA objective (Eq. 1) for at least one real dataset, alongside a baseline objective from TPCA on a common discretization.
- Measuring the practical effect of the strong orthogonality constraint by comparing the cost achieved under the current implementation vs. a relaxed version that allows the more general R* formulation (at least on a small-scale problem).
- Run-to-run variability statistics for GPCAGEN, given the non-convex neural network optimization.

## Removed Points

- **"The experimental motivation for GPCA over TPCA is weakened by the paper's own results":** Removed. The paper honestly reports that GPCA and TPCA are similar for Gaussians, which is a genuine finding, not a weakness. It also clearly identifies regimes where they differ and discusses cases where GPCA is worse (a useful negative result). Honest reporting of limitations strengthens rather than weakens a paper.
- **"Exact claim is misleading":** Weakened and absorbed into Major Weakness #3 (theory-practice gap) rather than treated as a standalone fatal issue, because the paper does define "exact" as not relying on linearization, which is a reasonable framing. The real issue is the accumulation of unquantified approximations in the general case.
- **"Non-convex optimization over rotations not discussed":** Moved from Major to Minor. While this is a real omission, the rotation variables are low-dimensional (d=2 in experiments) and the optimization is standard; this does not threaten the paper's core claims.
- **"Formatting/typo/style nitpicks" and missing appendix content:** Removed per instructions (parser strips appendices, these are not author errors).
- **Reproducibility concerns about undisclosed hyperparameters:** The paper references Appendix E for architecture and hyperparameter details; since appendices are stripped by the parser, these concerns are not verifiable from the available text and are removed.
- **Strength Finder's generic strengths (e.g., "this paper addressed an important problem"):** Removed.

## Novel Insights

The paper's own honest finding that GPCA and TPCA are generically very similar for Gaussian distributions (<1% cost difference on average) and that the main counterexample is a "pathological" case where GPCA produces components that do not pass through the barycenter (yielding clipping artifacts) is a noteworthy meta-observation. It suggests that, for the Gaussian submanifold, the extra complexity of GPCA over the widely-used TPCA may seldom be warranted in practice — a useful calibration for practitioners. However, for non-Gaussian, absolutely continuous measures, GPCAGEN's ability to operate directly on continuous distributions (avoiding discretization artifacts that plague TPCA on point clouds) and to sample from any point along the geodesic components provides a genuine advantage that the qualitative results support, even if quantitative validation remains incomplete. The paper's framing of the orthogonality issue for higher components — requiring intersection in the top space rather than the base space — is a subtle structural observation that future work will need to address.

## Suggestions

1. Report the value of the GPCA objective (Eq. 1) achieved by GPCAGEN on at least one dataset (e.g., the MNIST controlled experiment, plus one real dataset via a discretized approximation), and compare it against a TPCA baseline's objective on a discretized common representation.
2. Quantify the impact of the restrictive orthogonality constraint by comparing the second-component cost under the current method vs. a more flexible search (even on a small-scale or 1D problem).
3. Add a concise limitations paragraph discussing: (a) the diffeomorphism requirement vs. unconstrained MLPs, (b) the effect of Sinkhorn approximation on the GPCA objective, (c) the orthogonality restriction for higher components, and (d) computational complexity.
4. Include a summary of Sinkhorn parameters (ε, iterations) and training hyperparameters in the main text, not only the appendix.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>