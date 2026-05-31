Now let me do the calibration search.Now I have enough information to write the final review.

---

## Summary

This paper proposes two algorithms for Geodesic PCA (GPCA) in Wasserstein space: one for centered Gaussian distributions leveraging the Bures-Wasserstein geometry via a lift to the space of invertible matrices GL_d, and one for general absolutely continuous measures using Otto's fiber bundle parametrization with neural networks (GPCAGEN). Both methods operate directly on Wasserstein geodesics rather than linearized (tangent space) approximations. The paper fills a genuine gap — prior work either used linearization (TPCA), restricted to 1D, or used generalized (not true) geodesics — and validates the approach through controlled synthetic experiments and qualitative real-world demonstrations on 3D point clouds and image color distributions.

---

## Strengths

- **Proposition 3 provides a provably exact lift of Gaussian GPCA to GL_d**: The reformulation of the BW₂ geodesic minimization as a Euclidean optimization over invertible matrices and rotations (eq. 12) is mathematically clean and fully justified, replacing a curved-space optimization with a flat-space one. The equivalence is proven, not approximated.

- **Quantitative characterization of TPCA distortion via Proposition 4**: The paper demonstrates via eq. (14) that TPCA distortion is governed by the ratio |a−b|/(a+b), and Figure 4 (right) shows empirically that GPCA achieves up to ~35% cost reduction over TPCA when this ratio exceeds ~0.4. This directly motivates the need for exact GPCA over linearized methods.

- **Honest and practical treatment of the geodesic validity interval**: The paper carefully explains how t_min and t_max are monitored through Hessian eigenvalue estimation (Section 4, Algorithm 1, line 5) and explicitly acknowledges the approximate nature of this finite-sample check. The connection between Otto's parametrization and the McCann convex formulation (eq. 9 vs eq. 10) is clearly explained.

- **Controlled MNIST recovery experiment**: The MNIST experiment (Section 5.2, Figures 5 and 9) constructs ground-truth orthogonal intersecting geodesics and demonstrates that GPCAGEN recovers them accurately, providing a meaningful falsifiable sanity check.

- **Advantage of continuous geodesic parametrization**: As highlighted in the Discussion, the Otto parametrization enables sampling along the geodesic at arbitrary t values and avoids discretization artifacts that appear in TPCA on discrete point clouds (Figure 16, Appendix A.2). This is a genuine practical advantage over TPCA.

---

## Weaknesses

### Fatal
None.

### Major

- **"Exactness" claim is overstated for GPCAGEN**: The paper's central positioning is that it solves the *exact* GPCA problem (equation 1), explicitly contrasting itself with "approximate" methods. For GPCAGEN, however, three simultaneous approximations are introduced: (a) W₂² is replaced by the Sinkhorn divergence S_ε; (b) the Hessian eigenvalue check that ensures the parametrized curve is a geodesic is evaluated only on a finite minibatch; and (c) the intersection and orthogonality constraints for the second component are enforced via soft regularization (eq. after eq. 15 in Section 4), not as hard constraints. The paper acknowledges (b) and (c) but frames them as implementation details rather than approximations that undercut the exactness claim. Since the regularization weights λ_I and λ_O are fixed at 1.0 with a single-line justification ("we found that setting the regularization coefficients λ_I and λ_O to 1.0 ensures the algorithm works as expected in all experiments"), the degree to which the structural constraints are actually satisfied is never quantified. The distinction from Seguy & Cuturi (2015)'s "approximate" GPCA is therefore one of degree, not kind. The authors should either qualify the exactness claim or measure constraint satisfaction empirically.

- **Real-data experiments are entirely qualitative with no quantitative comparison against TPCA**: For the ModelNet40 chair, lamp, and landscape image experiments, no residual loss value (eq. 1, approximated via Sinkhorn) is reported for either GPCAGEN or TPCA. The paper deflects by claiming "a direct numerical comparison between the two methods is therefore not meaningful" because TPCA acts on discrete measures — but the Sinkhorn divergence used in GPCAGEN is directly evaluable on both methods' outputs. The absence of quantitative comparison means the claim that GPCAGEN provides more meaningful components than TPCA (Section 5, Baselines) rests entirely on visual inspection of Figure 6 and Figure 16.

### Minor

- **No sensitivity analysis for λ_I and λ_O**: These parameters fundamentally govern whether the second (and higher) GPCAGEN components satisfy the intersection and orthogonality constraints. The paper states all experiments use λ_I = λ_O = 1.0, but provides no ablation or sensitivity table. The Appendix E discussion ("details on the architecture and hyperparameters") is deferred and we cannot assess how much the qualitative results would change under different regularization weights.

- **Landscape image experiment is underpowered (n = 39)**: With only 39 images, the result (PC1 = brightness, PC2 = blue vs. green) is visually plausible but provides weak evidence. It is difficult to distinguish geometric structure from initialization bias or network inductive bias at this scale.

- **Scalability of GPCAGEN not discussed**: The method requires optimizing two MLPs plus n scalar variables, iterating over all n distributions per epoch. There is no discussion of how runtime scales with n or the dimensionality d of the support. The experiments use n = 100 (point clouds) and n = 39 (images), which is small; it is unclear whether GPCAGEN scales to the hundreds or thousands of distributions typical in practice.

### Trivial

- The R* = id simplification for GPCAGEN (enforcing intersection in Diff(Ω) rather than a fiber-rotated version) is acknowledged but its effect on orthogonality quality is not analyzed. This is a deliberate and reasonable design choice but merits a sentence on the potential error it introduces.

---

## Nice-to-Haves

- A table reporting the GPCA residual loss (eq. 1 via Sinkhorn) for GPCAGEN vs. TPCA on at least one real dataset (e.g., ModelNet40 chairs) would transform a qualitative comparison into a quantitative one at modest extra cost.
- A brief sketch of how higher-order components (beyond the second) handle the nested orthogonality structure would help readers assess correctness without relying on Appendix D.2 alone.
- Reporting constraint satisfaction values I and O at convergence for the MNIST experiment would empirically validate the structural constraints.

---

## Removed Points

*These points are flagged to be removed, treat them with caution.*

- **Intersection-in-Diff(Ω) vs. Prob(Ω) discrepancy as a weakness**: The harsh critic notes that the R* = id simplification affects orthogonality quality. The paper explicitly acknowledges this on p. 6: "An alternative implementation would be to enforce the intersection of the geodesics in Prob(Ω) and to impose the orthogonality of ∇f_ψ(φ_θ) ∘ R* ... However, computing R* is computationally expensive, and we therefore preferred to impose ξ_1(t¹_inter) = ξ_2(t²_inter)." This is a stated design trade-off, not an error. Demoted to Trivial.

- **Characterization of latent-PCA baseline as insufficient**: The harsh critic argues the comparison to latent PCA "deserves more than a dismissal." However, the paper includes the comparison in Appendix A.2 and the primary contribution is the Wasserstein geodesic methodology — evaluating it in depth against a latent-space PCA is outside scope. Removed.

- **Missing appendix criticisms**: Any criticism grounded in the absence of appendix content (proofs, sensitivity tables, figures) is removed per policy, as the parser strips appendix sections.

- **Higher-order components not described in main text**: The harsh critic argues that the description of higher components in Appendix D.2 without a main-text sketch is insufficient. Since appendix content exists in the submission but was stripped, this is removed.

---

## Novel Insights

The paper's most conceptually novel contribution is the observation that Otto's fiber bundle construction — originally a theoretical tool for understanding the Wasserstein geodesic structure — can be operationalized computationally using unconstrained neural networks for the potential function f (avoiding the convexity constraints of McCann's parametrization), with the geodesic validity interval tracked dynamically via Hessian eigenvalue monitoring. This decouples "parametrize a geodesic" from "parametrize an optimal transport map," enabling a class of algorithms that learns geodesic components directly from samples of distributions. The Gaussian lift (Proposition 3) additionally shows that the gauge ambiguity in GL_d can be exploited to make multi-component GPCA tractable, offering a template for other quotient-space geometries.

---

## Suggestions

1. Reframe GPCAGEN's claims: replace "exact GPCA" with "geodesic PCA without linearization, using Sinkhorn approximation and soft constraint enforcement," and add a sentence quantifying how closely the structural constraints are satisfied in the MNIST experiment.
2. Add a quantitative GPCA residual comparison (Sinkhorn cost) between GPCAGEN and TPCA on one real dataset.
3. Provide a one-row sensitivity table for λ_I and λ_O (e.g., varying in {0.1, 1.0, 10.0}) to justify the fixed-at-1.0 choice.
4. Include a brief runtime table or discussion for GPCAGEN as a function of n and d.

---

## Score and Decision

**Originality**: High — the combination of Otto's fiber bundle with neural networks for GPCA is novel, and the Gaussian lift is clean and original.

**Importance of research question**: Moderate-high — GPCA in Wasserstein space is a well-motivated problem, and filling the gap for exact (non-linearized) methods in R^d is a meaningful contribution.

**Claims vs. support**: Moderate — the Gaussian case is fully supported; GPCAGEN's "exact" claims are overstated relative to the approximations used.

**Soundness of experiments**: Moderate — MNIST recovery is convincing; real-data experiments are qualitative with no quantitative baseline comparison.

**Clarity**: Good — background, propositions, and algorithms are clearly presented.

**Value to research community**: Moderate-high — opens a direction for neural parametrization of Riemannian statistics on Wasserstein spaces.

### Calibration anchors

| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| HB4lr0ykTi (Wasserstein Flow Matching) | 6.33 | R1 | Similar OT geometry + neural nets; weaker theory than ours (Gaussian case) but stronger experiments |
| rY8xdjrANt (WDHA Barycenter) | 6.20 | R1 | Similar gap between theory and practice; rejected despite good algo |
| cNmu0hZ4CL (Noisy Neural OT) | 8.00 | R1 | Much stronger empirical validation; not directly comparable |
| bwOndfohRK (NNs on Symmetric Spaces) | 6.00 | R2 | Similar Riemannian manifold ML; accepted; our paper comparable |
| rsg1mvUahT (Federated Wasserstein) | 6.50 | R2 | Accepted; sound theory + experiments; our paper slightly weaker experimentally |
| Kuj5gVp5GQ (Sinkhorn-Newton-Sparse) | 7.00 | R2 | Accepted; focused problem with strong theory + experiments; our paper broader but weaker on experiments |
| WPz5e5V85k (Wasserstein Proximal) | 6.00 | R2 | Rejected; similar theory-practice gap issue |

**Round 1 bracket**: 5.5 – 7.5

**Round 2 narrowing**: Compared to accepted papers at 6.0–6.5 (Neural Networks on Symmetric Spaces; Federated Wasserstein), this paper's Gaussian contribution is comparable, but GPCAGEN's real-data validation is weaker than those papers' empirical sections. The overstated exactness claim and lack of quantitative real-data comparison keep it from the 7.0 range. The paper is above the rejected WFM (6.33) and WDHA (6.2) because the Gaussian case is theoretically clean and the gap being filled is clearer.

**Final score**: 6.0 — Weak Accept / Borderline Accept.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>