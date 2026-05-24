Now I have all the information needed. Let me compile the final review.

---

## Summary

This paper proposes two methods for exact Geodesic PCA in the Otto-Wasserstein space. For centered Gaussians, the authors lift the problem from the SPD cone to GL_d using the Bures-Wasserstein geometry, yielding a tractable optimization and a precise theoretical quantification (Proposition 4) of when GPCA diverges from tangent PCA. For general absolutely continuous measures, they introduce GPCAGEN, which parametrizes Otto's fiber-bundle geodesics with MLPs, avoiding input-convex networks. The Gaussian part is theoretically sound with controlled experiments; the GPCAGEN method is novel but its empirical evaluation is qualitative and incomplete.

## Strengths

- **Gaussian GPCA formulation is rigorous and insightful.** Lifting GPCA to GL_d via Proposition 3 transforms geodesic search into a constrained Frobenius-norm minimization over horizontal lines and rotations. Proposition 4 provides a clean, quantitative account of TPCA distortion as a function of eigenvalue spread (equation 14 and Figure 4, right), showing cost improvements up to ~35% when eigenvalue ratios are extreme.

- **GPCAGEN's Otto-bundle parametrization is genuinely novel.** Using ordinary MLPs to parametrize the diffeomorphism φ and scalar potential f — without requiring input-convex neural networks — is an elegant design choice grounded in Otto's geometry. The method can sample from geodesics at arbitrary continuous t, which discrete TPCA cannot do.

- **Proposition 5** proves that for univariate Gaussians, GPCA in the full Wasserstein space remains on the Gaussian submanifold, providing theoretical justification for the restriction made in Section 3.

- **Qualitative results show semantically meaningful structure.** On ModelNet40 lamps (Figure 6, middle row), Component 1 cleanly separates chandeliers from floor lamps while Component 2 captures structural thickness. On landscape images, Component 1 captures brightness and Component 2 separates color hue. These are interpretable and non-trivial.

## Weaknesses

### Fatal
None. The paper's core theoretical contributions are sound, and the GPCAGEN method is conceptually well-motivated. The weaknesses below are matters of incomplete empirical support rather than fundamental error.

### Major

- **GPCAGEN lacks any quantitative evaluation.** The paper reports no numerical metrics for the general method — no variance explained, no reconstruction error, no comparison of the GPCA objective value against any baseline. The experiments (MNIST, 3D point clouds, landscape images) consist entirely of qualitative visualizations of sampled densities along geodesics. While these are illustrative, a methods paper claiming to solve exact GPCA must demonstrate that the method actually optimizes the objective better than alternatives. The paper acknowledges that a direct numerical comparison with TPCA is "not meaningful" because the methods act on different representations, but even a self-contained metric such as the proportion of variance explained by the first k components (relative to the Fréchet mean) is absent. The claim in Section 6 that GPCA "enables downstream tasks such as classification, clustering, and outlier detection" is unsupported by any experiment in the main text. This is the most significant gap in the paper and the primary reason the evidence for GPCAGEN's practical value is incomplete.

### Minor

- **Sinkhorn approximation is used without discussion.** GPCAGEN optimizes the Sinkhorn divergence S_ε rather than the true W_2². While the paper's "exact" claim refers to the geodesic being a true geodesic (not linearized), the loss function itself is approximate, and no ablation on the regularization parameter ε is provided. The reader cannot assess whether the recovered geodesics are sensitive to this approximation. A brief discussion of ε's effect or a small empirical study would address this.

- **The "continuous distributions" advantage is overstated.** The paper states (Section 6) that GPCAGEN "operates directly on continuous distributions, avoiding the need for empirical approximations" and "discretization artifacts." In practice, the method still uses finite batches of i.i.d. samples to estimate the Sinkhorn divergence and to monitor Hessian eigenvalues. The genuine advantage — the ability to sample from the geodesic at any continuous t — is real but should be stated more precisely without overclaiming about the elimination of discretization.

- **No convergence or failure analysis for GPCAGEN.** The objective is non-convex and involves monitoring Hessian eigenvalues for validity of the geodesic parametrization. The paper does not discuss whether the optimizer reliably converges to meaningful solutions, how sensitive results are to initialization, or whether the Hessian eigenvalue monitoring remains reliable in higher dimensions (e.g., for images).

- **Comparison with latent-space PCA baseline is deferred to appendix.** The main text mentions that latent PCA "does not produce meaningful modes of variation" but shows no results (deferred to Appendix A.2, which is stripped). While appendix stripping is a parser artifact, a methods paper should at minimum summarize the key comparison result in the main text.

### Trivial
None significant.

## Nice-to-Haves

- Report the proportion of variance explained by the first few GPCAGEN components and compare with the variance explained by TPCA and by a trivial baseline (the Fréchet mean).
- Provide an ablation on the Sinkhorn parameter ε, showing that the learned geodesics stabilize for small ε.
- Include the outlier detection experiment (Appendix A.3) or at minimum a summary of it in the main text with a quantitative metric.
- Discuss the practical reliability of Hessian eigenvalue monitoring in higher dimensions, with empirical eigenvalue estimates from training.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"No baselines at all"* — REMOVED. The paper does discuss TPCA and latent PCA as baselines (Section 5.2, "Baselines" paragraph), even though the comparison is qualitative and partially deferred to the appendix. The claim of zero baselines is factually incorrect.
- *"Sinkhorn approximation makes the exact claim false"* — DEMOTED to Minor. The paper's "exact" refers to the geodesic being a true geodesic (not linearized), not to the distance computation being exact. This is a legitimate distinction. However, the lack of discussion of the Sinkhorn approximation remains a valid concern.
- *"The experiments are purely qualitative visualizations" criticism about the Gaussian experiments* — REMOVED for the Gaussian section. The Gaussian experiments (Section 5.1) do contain quantitative metrics: cost improvement percentages (Figure 4, right), Proposition 4's distortion quantification, and controlled comparisons showing when TPCA and GPCA coincide or diverge. The criticism applies only to GPCAGEN (Section 5.2).

## Novel Insights

The Gaussian GPCA analysis yields a concrete, verifiable insight: GPCA and TPCA coincide on zero-curvature submanifolds of S_d^{++} (matrices with constant orientation) but diverge substantially when data lies near the cone boundary with varying orientations — and counterintuitively, GPCA can behave *worse* than TPCA in those regimes, with the first component failing to pass through the barycenter and yielding poor separation (Figure 4). This is a genuinely non-obvious finding that qualifies the value of exact GPCA over the simpler TPCA approximation.

## Suggestions

- The single most impactful improvement would be adding even one quantitative metric for GPCAGEN — e.g., the GPCA objective value compared to TPCA's objective on the same data, or variance explained — and reporting it in a table alongside the qualitative figures. This would transform the evaluation from illustrative to evidential.
- Qualify the "continuous distributions" claim in the discussion to acknowledge that finite samples are still used for loss estimation while emphasizing the genuine advantage of continuous-time sampling along the geodesic.

---

**Calibration summary:**

| Anchor | Avg Score | Round | Comparison to this paper |
|--------|-----------|-------|--------------------------|
| F5UgXkPgSn (Fusion over Grassmannian) | 3.00 | R1 | Much weaker — limited theory and experiments |
| RmOXAa5H5Y (Simplicial Wasserstein) | 3.00 | R1 | Much weaker — empirical study, narrow scope |
| FjifPJV2Ol (Schrödinger Bridge) | 3.40 | R1 | Weaker — methodological gaps, rejected |
| 4mqt6QxSUO (Riemannian COVID detection) | 3.25 | R1 | Much weaker — incoherent |
| nS2DBNydCC (VQ by Distribution Matching) | 4.75 | R1 | Weaker — incremental, questionable assumptions |
| SkF7NZGVr5 (Curvature Loss of Plasticity) | 5.50 | R1 | Comparable score range, different domain |
| kvByNnMERu (Shape Distances, Limited Samples) | 5.25 | R2 | Weaker — narrower scope |
| WRLj18zwz6 (Manifold GNN Generalization) | 5.40 | R2 | Similar score range, different domain |
| 4IRYGvyevW (Lazy vs Rich Dichotomy) | 5.60 | R2 | Similar score, different domain |
| bwOndfohRK (NN on Symmetric Spaces) | 6.00 | R2 | Slightly stronger — similar theoretical depth but more comprehensive experimental validation |
| sRaAt9OOnW (Continuous GWOT) | 6.20 | R1 | Comparable — identifies gap, proposes method, but experiments limited; rejected |
| wpXGPCBOTX (Sparsistency for iOT) | 6.75 | R2 | Stronger — deeper theory |
| 62Ff8LDAJZ (OT Flows for 3D Point Clouds) | 6.80 | R2 | Stronger — better experimental validation on point clouds |
| aJ3tiX1Tu4 (Wasserstein Conformal) | 6.67 | R1 | Stronger — complete theory + experiments |
| P7O1Vt1BdU (Expected Sliced Transport) | 6.67 | R2 | Stronger — more mature method |
| mkDam1xIzW (Probabilistic Geometric PCA) | 7.33 | R2 | Stronger — more complete evaluation and EM algorithm |
| JWtrk7mprJ (Residual Deep GPs on Manifolds) | 7.60 | R1 | Clearly stronger — comprehensive experiments |
| g7ohDlTITL (Flow Matching on Geometries) | 8.00 | R1 | Clearly stronger — state-of-the-art, excellent experiments |
| TTrzgEZt9s (DRO with Bias/Variance) | 8.00 | R1 | Much stronger — unrelated domain but mature work |
| cNmu0hZ4CL (OT for Neural Populations) | 8.00 | R1 | Much stronger |

**Round 1 bracket:** 5.0–7.0. The paper sits well above the weak 3.0–3.5 cluster (incremental or poorly executed) and clearly below the 7.5+ cluster (well-rounded, comprehensive). The Gaussian GPCA part is solid but GPCAGEN's experimental evaluation is qualitatively-oriented and lacks quantitative metrics, placing it below the 7.33 PGPCA anchor and the 6.80 OT Flows anchor.

**Round 2 narrowing:** The most comparable anchors are bwOndfohRK (6.00, "NN on Symmetric Spaces" — solid theory, novel architecture, experiments with gaps) and sRaAt9OOnW (6.20, "Continuous GWOT" — identifies gap, proposes method, limited experiments, rejected). This paper is slightly below the 6.00 anchor because GPCAGEN's evaluation is weaker (no quantitative metrics at all vs. marginal but present quantitative results in the 6.00 paper). It is comparable to the 6.20 GWOT anchor, which was rejected due to limited experiments and unsurprising findings. The paper's Gaussian GPCA theory elevates it somewhat, but the GPCAGEN evaluation drags it down. **Final score: 5.5**, reflecting a paper with real theoretical contributions and a promising method, whose empirical evaluation is not yet at the level required to fully establish the contribution.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>