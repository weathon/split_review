Now I'll write the final consolidated review.

## Summary

This paper tackles Geodesic Principal Component Analysis (GPCA) in Wasserstein space — identifying geodesic curves that best capture variation in a dataset of probability distributions. It provides two contributions: (1) an exact GPCA formulation for centered Gaussian distributions via a lift to GL_d using Bures-Wasserstein geometry, and (2) GPCAGEN, a neural-network-based algorithm for general absolutely continuous measures using Otto's fiber bundle parametrization. Theoretical results include a closed-form quantification of TPCA distortion (Proposition 4) and a consistency result for univariate Gaussians (Proposition 5).

## Strengths

- **Proposition 4 provides a closed-form quantification of TPCA distortion**: Equation 14 gives an explicit formula showing how the ratio of TPCA-distorted distance to true BW₂ distance depends on the eigenvalue ratio (a−b)/(a+b) and orientation angle θ. This is the first analytic characterization of when linearization fails in this setting, and it directly supports the paper's framing of why GPCA can differ from TPCA.

- **Using Otto's parametrization avoids ICNNs**: Section 4 parametrizes geodesics via φ_(θ) and a smooth function f_(ψ) where f need not be convex, unlike the McCann parametrization that requires convex u. This removes the architectural constraint of input-convex neural networks while still enforcing geodesic validity via eigenvalue monitoring — a genuine methodological advance over prior work.

- **Principled handling of geodesic incompleteness**: The paper explicitly accounts for the fact that Wasserstein geodesics cannot be extended for all t ∈ ℝ. For Gaussians it clips projection times (Proposition 3), and for general measures it monitors Hessian eigenvalues (Algorithm 1). This practical innovation, essential for any exact GPCA method, was absent in prior work.

- **Honest discussion of limitations**: The paper transparently acknowledges that GPCA can produce "undesirable effects" (data projecting to geodesic boundaries, components not through the barycenter) and that "GPCA may be seen as worse-behaved as TPCA" in certain regimes. It also discusses the trade-off of the simplified intersection constraint in GPCAGEN.

## Weaknesses

### Major

1. **GPCAGEN evaluation is entirely qualitative, with no quantitative validation.** The MNIST, 3D point cloud, and landscape image experiments show plausible interpolations and projection plots, but there are no reconstruction error metrics, no variance-explained numbers, no correlation of projection times with known ground-truth labels, and no quantitative comparison against any baseline. For a method paper proposing a new algorithm, this level of validation is insufficient to establish that GPCAGEN actually minimizes the GPCA objective or produces useful components. The synthetic MNIST experiment (Figure 5) with known ground-truth geodesics is a natural place for error metrics (e.g., Wasserstein distance between recovered and true geodesics as a function of sample size m or iterations), but none are reported.

2. **No quantitative comparison against baselines for GPCAGEN.** The paper states that "a direct numerical comparison between [GPCAGEN and TPCA] is therefore not meaningful" because GPCAGEN operates on continuous distributions and TPCA on discrete measures (line 285). However, this sidesteps the need for any validation at all. The alternative of embedding into a latent space and performing PCA is shown in the appendix but dismissed without quantitative comparison. Given that a central motivation is that TPCA "fails to capture intrinsic structure," the paper must demonstrate — with concrete metrics — that GPCAGEN succeeds where TPCA fails. Without this, the reader cannot evaluate whether GPCAGEN is actually useful.

3. **The Gaussian experiments reveal a tension the paper does not resolve.** Figure 4 shows that when GPCA and TPCA differ most (same eigenvalues, near the cone boundary), GPCA's first component may not pass through the Wasserstein barycenter and data points can project to the geodesic boundaries ("undesirable effects"). The cost improvement reported is a *minimization* improvement — it shows GPCA fits its objective better — but does not indicate whether the resulting components are more meaningful or useful. The paper acknowledges this but does not argue why GPCA's output is nonetheless the "correct" geometric object, nor does it propose criteria beyond objective value for preferring GPCA over TPCA. This is a conceptual gap for the approach.

### Minor

4. **Missing optimization details for the Gaussian algorithm.** Proposition 3 formulates the GPCA problem as optimization over (A₁, X₁, {Qᵢ}) with Qᵢ ∈ SO_d, but the paper never describes how the Qᵢ are optimized (e.g., Riemannian gradient descent on SO_d, alternating minimization, closed-form updates). Without this, the Gaussian algorithm is not reproducible from the main text alone. The claim that "GPCA reduces the objective by less than 1% on average" is reported without standard deviations.

5. **Second GPCAGEN component uses a simplification that may bias the solution.** The intersection regularization ℐ forces the *representatives* in Diff(Ω) to coincide (ξ₁ = ξ₂ at intersection), not just the projected distributions. The paper notes this is a simplification because computing the correct R^* is "computationally expensive" (line 217). This imposes a specific choice of representative (from the first geodesic) that may not be optimal for the second, potentially constraining the solution space. The Gaussian case correctly handles this by rotating the representative; GPCAGEN avoids it for computational reasons without analyzing the bias this introduces.

6. **Sinkhorn divergence used without discussion of bias or parameter choice.** The GPCAGEN algorithm replaces W₂² with Sinkhorn divergence S_ε (line 189), which is biased (does not recover W₂² even asymptotically) and depends on a regularization parameter ε. The paper states ε is in Appendix E (stripped by the parser) but does not discuss the impact of Sinkhorn bias on the recovered geodesics in the main text.

### Trivial

7. **Proposition 5 (univariate Gaussian consistency) reads as an extra result not leveraged elsewhere.** It does not inform the algorithm design or experiments. It is a nice theoretical observation but is disconnected from the rest of the paper.

## Nice-to-Haves

- On the synthetic MNIST experiment where ground truth is known, report quantitative error (e.g., Wasserstein-2 distance between the true and recovered geodesic) as a function of sample size m, number of iterations, or Sinkhorn regularization ε. This would provide the minimal validation that GPCAGEN solves the stated problem.
- Show that on a dataset with known deformation parameters (e.g., shapes with known rotation/scaling), GPCAGEN's projection times correlate better with the true parameters than TPCA's projection coordinates.
- Add standard deviations to the Gaussian cost-improvement numbers (currently "average for 100 trials" with no spread reported).

## Removed Points

These points from the harsh critic review are removed with justification:

- **"The paper's central claim—solving *exact* GPCA—is undermined by approximations."** Partially removed. The paper defines "exact" as "do not rely on a linearization of the Wasserstein space" (line 49), which is a clear, defensible definition. The Gaussian algorithm genuinely solves the exact objective (modulo numerical optimization). For GPCAGEN, the Sinkhorn approximation is a real concern but is standard practice in neural OT; it is discussed in Appendix E. I retain a softened version as Minor weakness 6.
- **Reproducibility concerns about missing appendix content (hyperparameters, proofs).** Removed per instructions: the parser strips appendices from all papers; these exist in the original submission.
- **"The 'same orientation' experiment is not insightful."** Removed. It is useful validation that the algorithm behaves correctly in the zero-curvature limit.
- **Formatting, typo, and presentation nitpicks.** Removed per instructions — these are parser artifacts, not paper errors.
- **Demands for runtime comparisons, training times, scalability data.** Removed. These are nice-to-haves, not weaknesses, and the paper does not claim computational efficiency as a contribution.
- **Criticism that Proposition 5 is "not used anywhere."** Weakened to Trivial weakness 7. It is a theoretical consistency result; not every theorem must drive an experiment.

## Novel Insights

None beyond the paper's own contributions. The harsh critic's observation about the GPCA-vs-TPCA tension is a genuine insight that the paper partially surfaces but does not fully address: GPCA minimizes a geometrically coherent objective, yet in the "same eigenvalues" regime the resulting components can be less useful (boundary projections, no barycenter) than the linearized approximation. This raises the question of whether the GPCA objective is always the right one for data close to the boundary of the SPD cone — a question worth exploring beyond this paper.

## Suggestions

1. Add a quantitative evaluation for GPCAGEN on at least one synthetic benchmark where the true GPCA solution is known (e.g., mixtures of Gaussians along a known geodesic). Report reconstruction error as a function of sample size.
2. Either describe the optimization over SO_d in the Gaussian algorithm (even briefly: e.g., "using Riemannian gradient descent on SO_d with retractions") or cite standard approaches from the literature.
3. Acknowledge the Sinkhorn bias explicitly and either bound its effect or present a sensitivity analysis over ε.
4. Address the GPCA-vs-TPCA tension head-on: either argue why GPCA's output is the correct geometric object even when it yields "undesirable" properties, or propose a regularized objective that preserves the benefits of GPCA while avoiding boundary pathologies.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>