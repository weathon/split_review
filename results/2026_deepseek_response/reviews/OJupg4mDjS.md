Now let me write the final review.

## Summary
This paper proposes two algorithms for exact Geodesic Principal Component Analysis (GPCA) in Wasserstein space: one for centered Gaussian distributions via a lift to GL_d under Bures-Wasserstein geometry (Proposition 3), and one for general absolutely continuous measures (GPCAGEN) using neural parametrization of Otto geodesics (Section 4). The Gaussian part is theoretically grounded and includes a quantification of when GPCA diverges from Tangent PCA (Proposition 4). The GPCAGEN algorithm is a clever extension but its experimental validation is insufficient to support the central claims.

## Strengths
1. **Nonlinear lifting to GL_d for Gaussian GPCA (Proposition 3)** — Provides the first exact reduction of Wasserstein GPCA for Gaussians to a tractable Euclidean optimization over invertible matrices and rotation variables (equation 12). Prior work only solved approximate versions.

2. **Neural parametrization of Otto geodesics without convexity constraints (Section 4)** — Equation 9 uses MLPs for φ and f without requiring input-convex neural networks, since the geodesic only requires id + t∇f to be a diffeomorphism. This is a weaker and more practical architectural requirement than the McCann parametrization (equation 10).

3. **Quantified distortion between GPCA and TPCA (Proposition 4)** — Equation 14 gives an explicit first-order formula for the ratio of true to linearized Bures-Wasserstein distance in terms of (a−b)/(a+b) and orientation θ. Figure 4 verifies this experimentally with up to ~35% improvement, providing concrete conditions where linearization fails.

4. **Univariate Gaussian invariance result (Proposition 5)** — Shows that GPCA on univariate Gaussians stays within the Gaussian family, a nontrivial consistency check that the paper notes remains open in higher dimensions.

5. **Demonstration that GPCA bypasses the Wasserstein barycenter** — Figure 4 shows a concrete example (equal-eigenvalue matrices on a circle) where the first GPCA component does not pass through the barycenter, unlike TPCA. This provides direct evidence that the two methods are not equivalent, connected to results from Huckemann & Ziezold (2006).

## Weaknesses

### Fatal
None.

### Major
1. **GPCAGEN evaluation is purely qualitative on its strongest test case.** The synthetic MNIST geodesic experiment (Section 5.2) has known ground truth (digit interpolation and color interpolation), yet the paper provides no quantitative metric — no Wasserstein distance between learned and true geodesics, no reconstruction error, no cosine similarity of velocity fields. The claim that GPCAGEN "successfully recovers" the two geodesics (Figure 5, Figure 9) rests entirely on visual inspection. Without a quantitative measure of accuracy, it is impossible to know whether the neural network optimization has found a valid solution or a visually plausible but incorrect local minimum. This is structural because it undercuts the paper's main claim: that the proposed method solves the exact GPCA problem for general measures.

2. **Soft constraint satisfaction for the second component is unreported.** The paper uses regularization penalties ℐ (intersection) and 𝒪 (orthogonality) with fixed λ_I = λ_O = 1.0 (lines 190–192), stating the algorithm "works as expected" (line 256). No achieved violation values are reported — no orthogonality angle between horizontal fields, no intersection distance between geodesic representatives. If the soft constraints are poorly satisfied, the resulting components are not true GPCA components in the Riemannian sense. Sensitivity to λ_I, λ_O is not explored either.

### Minor
1. **Diffeomorphism condition is checked over a finite batch.** Algorithm 1 (line 5) monitors Hessian eigenvalues over a finite set of m samples, providing no guarantee over the full domain. Combined with Sinkhorn divergence (an approximation to W₂), the practical precision is weaker than the theoretical framing suggests. The paper acknowledges these approximations but does not quantify their impact.

2. **No quantitative baseline comparison or alternative validation of advantage.** The paper argues TPCA comparison is "not meaningful" due to different representations (line 264), but offers no alternative quantitative evidence of GPCAGEN's utility — e.g., using projection times as features for classification or outlier detection. TPCA results in Appendix A.2 show artifacts qualitatively, but this is insufficient to establish superiority.

3. **Statistical significance is unreported for GPCAGEN experiments.** The Gaussian experiments average over 10 runs, but the GPCAGEN experiments (MNIST, point clouds, landscape images) appear to be single runs. No standard deviations or confidence intervals are reported.

4. **No runtime or scaling analysis.** The paper does not discuss how GPCAGEN scales with dimension d, sample size n, or neural network size, making it difficult to assess practical applicability.

### Trivial
None.

## Nice-to-Haves
- Report the Sinkhorn entropic regularization parameter ε and discuss its effect on learned components.
- Discuss whether GPCAGEN suffers from the same pathological behavior as Gaussian GPCA near boundary conditions (cf. Section 6, Figure 4).
- Characterize failure modes or limitations of GPCAGEN more explicitly.

## Removed Points
These points are flagged to be removed; treat them with caution.
- *Missing reproducibility details (optimizer, learning rates, hyperparameters, Appendix D.2/E content):* The paper states these details are in Appendices D.2 and E. The appendices were stripped by the PDF parser, not missing from the original submission.
- *Missing related works:* Cannot verify without external sources.
- *Criticism that GPCAGEN operates on discrete measures / batch sampling contradicts "continuous" claim:* The paper's phrasing "operates directly on continuous distributions" refers to avoiding empirical approximations of intermediate measures ν_s (discussion, lines 282–285). The use of batch sampling of ρ and Sinkhorn divergence is a separate practical implementation choice. The paper does not claim full simulation-free exactness.
- *Formatting/style nitpicks:* Parser artifacts, not author errors.
- *Speculative concerns about unfair comparisons with baselines when the asymmetry favors the baseline.*
- *Generic "methods not compared to X" without anchoring.*
- *Generic "lack of ablation on X" that amounts to scope creep.*

## Novel Insights
The most interesting observation across the reviews is that the Gaussian GPCA case (Section 3, Figure 4) provides a fully verified, analytically tractable setting where GPCA and TPCA diverge meaningfully, and the paper could have used this as a stronger testbed for GPCAGEN's general claims — e.g., applying GPCAGEN to recover Gaussian geodesics and comparing against the closed-form Gaussian GPCA solution. This missed opportunity to bridge the two halves of the paper is a genuine insight: rather than separate Gaussian and general-case sections, the general-case method could have been validated against the known Gaussian ground truth, providing quantitative evidence of correctness that is currently absent.

## Suggestions
- **Quantitatively validate GPCAGEN on the synthetic MNIST geodesic experiment.** Report the Wasserstein distance between learned and true geodesics at several t-values, the cosine similarity between learned and ground-truth velocity fields, and the variance explained relative to the optimal GPCA objective. This is the single highest-impact improvement.
- **Report constraint satisfaction for the second GPCAGEN component:** provide the orthogonality angle (deviation from 90°) and intersection distance achieved during training and at convergence. Include a sensitivity analysis for λ_I and λ_O.
- **Provide one quantitative real-data demonstration.** For example, use projection times from the ModelNet40 chairs/lamps experiments as features for classification (chairs vs. armchairs) and compare against a simple baseline like a VAE embedding with standard PCA.

## Score and Decision

### Calibration Anchor Summary

| Paper | Avg Score | Round | Comparison |
|---|---|---|---|
| F5UgXkPgSn (Matrix completion) | 3.00 | R1 (weak) | Weaker; lacks this paper's theoretical grounding |
| FjifPJV2Ol (Schrödinger bridge) | 3.40 | R1 (weak) | Weaker; stronger theory here |
| RmOXAa5H5Y (Simplicial Wasserstein) | 3.00 | R1 (weak) | Weaker |
| 9WG1ga39Dq (Consistent OT) | 6.00* | R1 (weak) | Mixed scores, not directly comparable |
| WPz5e5V85k (Wasserstein proximal) | 6.00 | R1 (mid) | Comparable theory but stronger experiments |
| **HB4lr0ykTi (Wasserstein Flow Matching)** | **6.33** | **R1 (mid)** | **Similar situation (clever idea, entropic OT approximations, unconvincing point-cloud results); this paper has slightly weaker experimental validation** |
| rY8xdjrANt (OT Barycenter WDHA) | 6.20 | R1 (mid) | Similar: good theory, questions about experimental evaluation |
| mkDam1xIzW (Probabilistic Geo PCA) | 7.33 | R1 (mid) | Stronger; accepted with more complete validation |
| g7ohDlTITL (RFM) | 8.00 | R1 (strong) | Stronger; thorough experiments |
| **a72vorQK8v (FlatVI)** | **5.50** | **R2** | **Similar level: good motivation, limited experiments; this paper has stronger theory but weaker validation** |
| EyWKb7Ltcx (SPD classifiers) | 5.00 | R2 | Comparable but different method; this paper is slightly more novel |
| ZLSdwjDevK (Riemannian diffusion) | 5.67 | R2 | Similar level |
| gxhRR8vUQb (Diffeomorphic mesh) | 7.00 | R2 | Stronger; accepted with solid experiments |

*Note: 9WG1ga39Dq has avg 3.0 but widely varying scores (10,6,5,3).*

**Round 1 bracket:** Plausible range 4.5–6.5, informed by the distance between weak anchors (~3.0) and strong anchors (~8.0).

**Round 2 narrowing:** Comparing against the 5.0–6.33 band: the paper is structurally similar to Wasserstein Flow Matching (6.33) and FlatVI (5.50). Like WFM, this paper proposes a clever framework but relies on entropic OT approximations without quantifying their effect. Like FlatVI, the validation is more qualitative than quantitative. The paper is weaker than WFM in that WFM at least provides quantitative comparisons on benchmarks, while the current paper offers none for GPCAGEN. The Gaussian GPCA contribution is solid, but it is only half of the paper's claimed deliverable. The paper is stronger than the Intrinsic Riemannian Classifiers (5.00) due to its well-motivated theoretical framework and nontrivial propositions (3, 4, 5).

**Final score: 5.0.** The theoretical contributions (Gaussian GPCA with Propositions 3–5) are solid and well-motivated. However, the GPCAGEN algorithm — half the paper's contribution — lacks the experimental validation necessary to support its central claims, and the evaluation remains insufficiently rigorous even by the generous standards of a methods paper.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>