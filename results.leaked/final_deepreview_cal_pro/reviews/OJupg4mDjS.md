Now I have all the information needed. Let me produce the final consolidated review.

---

## Summary

This paper introduces two algorithms for exact Geodesic PCA (GPCA) in Wasserstein space: one for centered Gaussian distributions using the Bures-Wasserstein geometry and a lifting to the general linear group, and one for general absolutely continuous probability measures (GPCAGEN) using a neural-network parametrization of Otto's geodesics. The lifting framework converts the geodesic search into a Euclidean optimization with orthogonal constraints. The method offers a principled alternative to tangent PCA that avoids linearization, and the paper provides theoretical analysis quantifying when the two differ.

## Strengths

- **Elegant fiber-bundle lifting framework.** The Gaussian GPCA algorithm lifts the problem from the curved Bures-Wasserstein manifold to the flat space of invertible matrices (Proposition 3), converting geodesic search into a tractable Euclidean optimization with orthogonal-group constraints. This yields an exact method that circumvents linearization without approximation.

- **Novel neural parametrization of Wasserstein geodesics for GPCA (GPCAGEN).** For general absolutely continuous measures, the paper leverages Otto's fiber-bundle parametrization (Proposition 2) to represent geodesics as pushforwards of a reference measure by MLP-parameterized maps, trained end-to-end with Sinkhorn divergence. This avoids the need for input-convex neural networks and enables continuous sampling along geodesic components.

- **Useful theoretical analysis.** Proposition 4 provides a closed-form quantification of the distortion incurred by tangent PCA for covariance matrices with identical eigenvalues, explaining when linearization breaks down and corroborated by experiments (Figure 4). Proposition 5 proves that for univariate Gaussians, GPCA in the full space of absolutely continuous measures coincides with GPCA restricted to the Gaussian submanifold, confirming internal theoretical coherence.

- **Convincing synthetic validation.** The MNIST experiment (Figure 5) demonstrates that GPCAGEN successfully recovers two pre-constructed orthogonal geodesics, providing evidence that the optimization captures the underlying Wasserstein geometry when ground truth is known.

## Weaknesses

### Fatal

None.

### Major

- **Orthogonality condition in GPCAGEN is an approximation, not fully justified.** The orthogonality regularizer \(\mathcal{O}\) for the second component computes the \(L^2(\rho)\) inner product between the horizontal velocities \(\nabla f_\psi \circ \varphi_\theta\) and \(\nabla f_{\psi_2} \circ \varphi_{\theta_2}\) evaluated at the *base maps* of each geodesic. Since both line segments in \(\text{Diff}(\Omega)\) have constant velocity, the paper argues this is equivalent to comparing velocities at the intersection point when \(\xi_1 = \xi_2\) (i.e., \(R^* = \text{id}\)). However, a velocity that is horizontal at the base point \(\varphi_\theta\) is not necessarily horizontal at the intersection point \(\varphi_\theta + t_{\text{inter}}^1\nabla f_\psi \circ \varphi_\theta\) — it may acquire a vertical (fiber) component. The Wasserstein inner product depends only on the horizontal components of these velocities at the intersection, while the paper's \(\mathcal{O}\) term includes both horizontal and vertical contributions. The paper acknowledges an alternative, more principled approach (the rotation \(R^*\) formulation used in the Gaussian case) but dismisses it as computationally expensive. This gap means the orthogonality constraint is approximate and the second component may not be strictly orthogonal in the Wasserstein metric. While the MNIST experiment suggests the approximation works in practice, the theoretical mismatch should be characterized more carefully.

- **Evaluation of GPCAGEN is predominantly qualitative with no quantitative metrics.** The experiments on 3D point clouds (chairs, lamps) and landscape images (Section 5.2) present only visualizations of geodesic traversals and scatter plots of projection times. No quantitative metrics are reported: no explained variance, no reconstruction error, no orthogonality error between components, no comparison of the GPCA objective value against any baseline, and no ablation of hyperparameters (\(\varepsilon\) for Sinkhorn, \(\lambda_I, \lambda_O\), network architecture). The MNIST experiment, while convincing qualitatively, also lacks quantitative recovery metrics. For a method that claims to solve "exact" GPCA, the evidence that it reliably produces better components than alternatives is incomplete.

### Minor

- **No diffeomorphism guarantee for unconstrained MLPs.** GPCAGEN's derivation requires \(\varphi \in \text{Diff}(\Omega)\) and \(\text{id} + t\nabla f_\psi \in \text{Diff}(\Omega)\). The paper uses standard MLPs and enforces the constraint heuristically by monitoring Hessian eigenvalues and clipping \(t\). This is a reasonable practical workaround, but it means the resulting curve is only approximately a Wasserstein geodesic, and the approximation error is not characterized.

- **Sinkhorn divergence introduces unanalyzed approximation.** The paper replaces \(W_2^2\) with the entropic Sinkhorn divergence \(S_\varepsilon\) for differentiability. The effect of this regularization on the quality of the learned geodesics is not examined, and no sensitivity analysis on \(\varepsilon\) is provided. This is another layer of approximation that sits uneasily with the "exact" framing.

- **Gaussian GPCA shows limited practical advantage over TPCA.** The paper's own experiments report that GPCA improves over TPCA by less than 1% on average for random covariance matrices, and the one case where they differ drastically (matrices with identical eigenvalues on a circle, Figure 4) is described as exhibiting "undesirable effects" with "poor separation." This undercuts the practical motivation for the Gaussian method, though the theoretical analysis (Proposition 4) remains valuable for understanding *when* TPCA breaks down.

### Trivial

None.

## Nice-to-Haves

- A synthetic benchmark for GPCAGEN with known ground-truth geodesic components and quantitative recovery metrics (e.g., MSE of learned vs. true geodesics, orthogonality error, projection variance explained) would substantially strengthen the empirical case.
- Runtime measurements or complexity analysis for both algorithms would help practitioners assess scalability.
- Sensitivity analysis of the Sinkhorn regularization parameter \(\varepsilon\) and the orthogonality/intersection weights \(\lambda_O, \lambda_I\) would clarify practical tuning.

## Removed Points

These points from the harsh critic review are flagged to be removed; treat them with caution:

- **Claim that the orthogonality condition is "structurally wrong" and a "fatal error."** The paper explicitly discusses the correct alternative (the \(R^*\) rotation approach) and explains that its simplification makes \(R^* = \text{id}\) by enforcing intersection in \(\text{Diff}(\Omega)\). While the approximation deserves more analysis (retained as Major), the critic's assertion that "the algorithm does not reliably produce orthogonal geodesic components" and that this "undermines a central claim" is overstated — the MNIST experiment shows the method recovering orthogonal components, and the paper is transparent about the simplification.

- **Criticism that the weather dataset example "lacks any comparison to TPCA."** The weather experiment (Section 5.1) is presented as an illustration of GPCA applied to empirical covariances, not as a comparative benchmark. The paper's main comparison with TPCA is in the controlled synthetic experiments (Figure 4, Proposition 4), where quantitative differences are analyzed.

- **Criticism that TPCA comparison for GPCAGEN is dismissed "without rigorous justification."** The paper states that "A direct numerical comparison between the two methods is therefore not meaningful" because TPCA acts on discrete measures while GPCAGEN operates on continuous distributions. This is a substantive distinction — the methods operate on different representations — and the paper includes a TPCA visualization in the appendix (Figure 16) to illustrate the difference qualitatively.

- **Assertion that "the method is therefore not 'exact' as claimed."** The paper defines "exact" explicitly as "not relying on a linearization of the Wasserstein space" (line 49), not as "free of all numerical approximation." This is a reasonable usage in the context of GPCA vs. TPCA, which is the central distinction the paper draws.

- **Criticism about "missing proofs in appendix" and "proofs deferred to appendices."** The appendix is stripped by the parser; the original submission includes full proofs. These cannot be evaluated here and should not be held against the paper.

- **Request for invertible architectures (coupling layers).** This is a nice-to-have but not standard practice in the optimal transport / neural Wasserstein literature, where unconstrained networks with monitoring heuristics are common.

- **Criticism about empirical covariances in the weather dataset possibly being rank-deficient.** This is speculative — the paper computes empirical covariances from histograms, and there is no evidence they are rank-deficient.

## Novel Insights

The paper's key insight is that GPCA in Wasserstein space can be solved exactly by lifting to a fiber bundle where geodesics become straight lines, avoiding the linearization inherent in tangent PCA. The theoretical analysis reveals that GPCA and TPCA differ most when data lie near the boundary of the SPD cone (high curvature), and that this difference can be either beneficial or pathological depending on the data geometry — an honest assessment that is more informative than claiming universal superiority.

## Suggestions

- Add a quantitative evaluation for GPCAGEN: measure orthogonality error between learned components, report the GPCA objective value (equation 1) achieved, and compare against a TPCA baseline on the same sample-based representations even if the comparison is imperfect.
- Either provide a more rigorous analysis of when the simplified orthogonality condition \(\mathcal{O}\) accurately captures Wasserstein orthogonality, or implement the \(R^*\)-based alternative and compare the two approaches experimentally.
- Discuss the cumulative effect of approximations (unconstrained MLPs, Sinkhorn divergence, eigenvalue clipping, simplified orthogonality) on the "exactness" claim, to set appropriate expectations.

## Score and Decision

**Calibration summary:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| EyWKb7Ltcx | 5.00 | R1 | Weaker — incremental, overclaiming, presentation issues |
| HB4lr0ykTi | 6.33 | R2 | Most comparable — similar domain (Wasserstein + NNs), similar strengths/weaknesses |
| TUvg5uwdeG | 6.40 | R2 | Comparable — theoretical novelty, limited empirical validation |
| mkDam1xIzW | 7.33 | R1 | Stronger — more rigorous experiments, cleaner theory |
| g7ohDlTITL | 8.00 | R1 | Much stronger — comprehensive experiments, clean framework |

**Bracket:** Round 1 placed the paper between 5.0 and 7.5. Round 2 narrowed to 6.0–6.5 via HB4lr0ykTi (6.33) and TUvg5uwdeG (6.40), both of which share this paper's profile of genuine theoretical novelty combined with empirical limitations and some theoretical approximations. This paper is slightly below those anchors due to the orthogonality simplification concern and the more qualitative evaluation.

**Final placement:** 6.0. The paper makes a genuine contribution — the first exact GPCA algorithm for Wasserstein space — with an elegant theoretical framework. The empirical validation and some theoretical justifications need strengthening, but the core approach is sound and the weaknesses are addressable.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>