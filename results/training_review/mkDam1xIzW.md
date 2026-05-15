Now I have a thorough understanding of the paper and all review claims. Let me produce the consolidated review.

## Summary

This paper proposes Probabilistic Geometric Principal Component Analysis (PGPCA), which generalizes PPCA to model data distributed around a nonlinear manifold (rather than lying exactly on it or around a Euclidean mean). The model introduces a manifold-attached coordinate system K(z) (Euclidean or geometric) and derives an EM algorithm whose M-step collapses to a PPCA-like eigenvalue problem. Experiments on simulated data and real mouse head-direction neural recordings show that PGPCA outperforms PPCA and can distinguish between Euclidean and geometric coordinate choices via log-likelihood comparison.

## Strengths

- **Principled generalization of PPCA to data around nonlinear manifolds**: Section 3.1 (Equation 1) shows PGPCA reduces to standard PPCA when φ(z)=0 and K(z)=I, establishing it as a strict generalization. The paper correctly identifies the gap — prior nonlinear PPCA extensions (PPGA, torus PPCA) require data to lie exactly on the manifold, whereas PGPCA models deviations around it — and this distinction is clearly motivated by real neuroscience applications (head-direction ring, hippocampal torus).

- **Analytical EM algorithm with closed-form M-step**: Despite the nonlinear manifold, Section 3.5 derives that the log-likelihood term collapses to PPCA's form with Γ(q) replacing the sample covariance matrix (Equation 13), allowing C and σ² to be computed via eigenvalue decomposition (Equations 14–15). This is non-trivial and yields an efficient algorithm (convergence within ∼40 iterations, Figure 2C).

- **Demonstrated ability to discriminate between Euclidean and geometric coordinates**: In simulations (Figures 2B, 2D) and real neural data (Figures 4B, 4D), PGPCA with the correct K(z) yields significantly higher log-likelihood, with paired t-tests showing p < 1.7×10⁻¹² (Figure 2B) and p < 3.1×10⁻⁴ (Figure 2D).

- **Joint learning of on-manifold state distribution**: Section 3.3 provides a principled discretization of p(z) via landmarks (Equation 9) with a closed-form M-step (Equation 11). Figure 3 demonstrates that coordinate selection works even when p(z) is learned simultaneously.

- **Validated on real neural recordings**: Section 4.4 applies PGPCA to mouse head-direction neural firing rates projected to ℝ¹⁰ with a fitted loop manifold, showing consistent improvements of GeCOV over EuCOV and PPCA across all dimensions (Figures 4B, 4D).

## Weaknesses

### Fatal
None.

### Major

- **The core derivation from (12) to (13) omits intermediate algebraic steps.** The paper states that the log-likelihood ℒ₁ᴹ simplifies from Equation (12) to Equation (13), which involves expanding the determinant |Ψ(z)| and the quadratic form (yᵢ−φ(z))′Ψ(z)⁻¹(yᵢ−φ(z)) using the matrix structure Ψ(z)=K(z)CC′K(z)′+σ²Iₙ, applying the Woodbury identity and determinant lemma, and incorporating the discretization of qᵢ(z). These steps are not shown, making it difficult for readers to verify the correctness of the reduction. While the result is plausible and matches the PPCA structure, and the paper does not falsely claim a supplement exists, providing the full manipulation would strengthen confidence in the algorithm. This matters because the entire M-step — and thus every experimental result — depends on this derivation.

- **The comparison between PGPCA and PPCA on real neural data does not fully isolate the contribution of the coordinate-aware covariance.** On real data, a loop manifold is fitted first, then PGPCA and PPCA are run. The reported improvement could partly come from the nonlinear mean structure (the fitted manifold) rather than from PGPCA's coordinate-aware covariance per se. A cleaner baseline would be a two-stage approach: (i) fit the same manifold, (ii) compute residuals and apply standard PPCA to those residuals. This would isolate whether PGPCA's coordinate system adds value beyond the manifold's mean structure. The EuCOV vs. GeCOV comparison partially addresses this concern, but a direct ablation is missing.

### Minor

- **GeCOV definition could be more explicit for the general case.** The paper defines GeCOV via examples (Figure 1: loop → tangent + normal; torus → two tangents + normal) and states that K(z) just needs to be orthonormal. From context, the general definition is clear: GeCOV = K(z) whose columns are an orthonormal basis where the first l columns span the tangent space at z and the remaining n−l span the normal space. However, a formal general definition would improve clarity and reproducibility, especially for users who want to construct GeCOV for arbitrary manifolds beyond loops and tori.

- **"Hypothesis testing" terminology is somewhat informal.** The paper compares raw log-likelihoods between EuCOV and GeCOV models with the same number of parameters and calls this "hypothesis testing." While paired t-tests are reported (with p-values) in simulations, on real neural data (Figures 4B, 4D) only raw log-likelihood differences are shown without confidence intervals or bootstrap. Rephrasing this as "model selection via log-likelihood comparison" or adding bootstrap confidence intervals would improve rigor.

- **The manifold fitting procedure on real data is underspecified.** Section 4.4 mentions that neural firing rates are projected to ℝ¹⁰ and a 1D loop manifold is fitted, but the exact method (spline fitting, TDA, etc.) and hyperparameters are not described. While the paper cites prior work (Chaudhuri et al., 2019), the details matter for reproducibility.

### Trivial
- None.

## Nice-to-Haves

- **Robustness to manifold misspecification**: The paper acknowledges that manifold fitting is performed separately (Section 5), which is appropriate. A sensitivity analysis varying the fitted manifold (topology, over/under-fitting, landmark placement) would strengthen claims about practical applicability but is beyond the paper's stated scope.
- **Landmark sensitivity**: The discretization of p(z) uses M landmarks (Equation 9) without discussing how M is chosen. An ablation on M would help users apply the method.
- **Comparison to a nonlinear baseline**: A comparison to GP-LVM (mentioned in related work) or kernel PCA would help benchmark PGPCA's performance against other nonlinear methods, though the paper's focus is on extending PPCA specifically.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"GeCOV is never formally defined... the experimental results for GeCOV are uninterpretable"** — REMOVED. The paper defines GeCOV via Figure 1 (tangent + normal vectors for a loop; two tangents + normal for a torus). The general principle is clear: GeCOV = K(z) whose columns are an orthonormal basis aligned with the manifold's tangent and normal spaces. For the specific manifolds studied (loop in ℝ², loop in ℝ¹⁰, torus in ℝ³), the construction is well-defined.
- **"The derivation from (12) to (13) is not shown and the paper claims 'the details are provided in the supplementary' (not present)"** — REMOVED (fabrication). The paper NEVER mentions a supplementary. It presents Equation (12) and Equation (13) with text stating the result. The intermediate algebraic steps are indeed compressed, but the paper does not falsely claim a supplement exists. The genuine weakness (compressed derivation) is kept above.
- **"No p-values, confidence intervals, or model selection criteria"** — PARTIALLY REMOVED (factually wrong). The paper explicitly reports paired t-test p-values for simulations (Figure 2B: p < 1.7×10⁻¹²; Figure 2D: p < 3.1×10⁻⁴). The lack of confidence intervals on real data is noted in the Minor section above.
- **"Robustness to manifold specification is entirely unaddressed"** — REMOVED. This is scope creep; the paper correctly acknowledges this as a limitation (Section 5). The contribution is the PGPCA model and algorithm, not a universal manifold-fitting theory.

## Novel Insights

The reviews surface an interesting tension: the paper's elegance — collapsing the M-step to a PPCA-like eigenvalue problem — is simultaneously its strongest contribution and its most opaque point, because the algebraic reduction is asserted rather than derived step-by-step. A second implicit insight is that the EuCOV vs. GeCOV comparison on real neural data (Figure 4) may serve as a diagnostic tool for the geometric structure of neural noise, analogous to how TDA reveals the topology of the mean activity; PGPCA extends this to the covariance structure of trial-to-trial variability. Neither review articulates this explicitly, but it suggests a potentially broader role for PGPCA beyond dimensionality reduction.

## Suggestions

1. Expand the derivation from (12) to (13) — even a short appendix with the key identities (Woodbury, determinant of I+CC′, trace trick) and their application would suffice to remove this as a weakness.
2. Add a baseline experiment on real neural data: fit the manifold, compute residuals, run PPCA on residuals, and compare its log-likelihood to PGPCA. This would cleanly separate the benefit of the manifold mean from the benefit of the coordinate-aware covariance.
3. State the general definition of GeCOV explicitly: "GeCOV at point z is an orthonormal matrix K(z) whose first l columns form an orthonormal basis for the tangent space T_z(M) and whose remaining n−l columns form an orthonormal basis for the normal space N_z(M)."
4. Provide bootstrap confidence intervals for the log-likelihood differences on real neural data (Figures 4B, 4D) and soften the "hypothesis testing" language to "model selection via log-likelihood comparison."
5. Describe the manifold fitting procedure for the neural data (method, software, hyperparameters) for reproducibility.

## Score and Decision

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>