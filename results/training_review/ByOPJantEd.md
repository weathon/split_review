I've carefully read the full paper and verified each reviewer claim against the actual text. Let me now produce the consolidated review.

---

## Summary

This paper introduces "Wigner kernels," a class of rotationally equivariant, body-ordered kernels for atomistic machine learning. The kernels are computed via an iterative Wigner iteration (Eq. 12) that avoids the explicit construction of a radial-chemical basis, thereby sidestepping the exponential feature growth that plagues linear body-ordered models like ACE. The method is evaluated on gold cluster energetics, random methane configurations, and the QM9 benchmark (both energies and dipole moments), achieving state-of-the-art accuracy (4.3 meV) on QM9.

## Strengths

- **Iterative kernel construction that avoids exponential feature explosion of feature-space models.** The Wigner iteration (Eq. 12) computes body-ordered equivariant kernels with cost linear in the maximum body order ν and independent of the radial-chemical basis. This is a genuine methodological advance over ACE, whose feature space grows as (a_max n_max λ_max)^ν (Section 3.4). The paper explicitly acknowledges the complementary drawback of λ_max^7 scaling, presenting an honest trade-off.

- **Systematic body-order convergence demonstrated on gold cluster energetics.** Learning curves (Fig. 1) show monotonic improvement as ν increases from 2 to 6, with ν=6 essentially converged. This demonstrates the value of explicit body-ordering: non-systematic constructions (squared SOAP, squared ν_max=2 WKs) saturate at higher error, while the true ν=4 model (capturing all 5-body correlations) significantly outperforms them. The comparison with ν=6 LE-ACE is informative and fairly presented.

- **State-of-the-art accuracy on the QM9 energy benchmark (Table 1).** Wigner kernels achieve 4.3 meV test MAE (16-run average), surpassing the previous best Allegro model (4.7 meV) and all other compared equivariant neural networks. The standard deviations (0.1 vs 0.2) indicate the improvement is reliable. For dipole moments (Fig. 3), Wigner kernels avoid the saturation that limits λ-SOAP models at larger training set sizes, demonstrating the advantage of a full body-ordered equivariant kernel over the combination of linear ν=2 and non-linear scalar kernels used in SA-GPR.

- **Theoretical rationalization of low-λ_max effectiveness.** The paper provides a principled explanation for why Wigner kernels with λ_max=3 can compete with LE-ACE using l=20 on the random methane dataset (Section 4.2): the tensor-product structure of the iterations incorporates higher-frequency components, and the multi-center ansatz reduces the need for very high angular resolution at individual centers. This connects to a broader observation in equivariant ML.

## Weaknesses

### Fatal
None.

### Major

- **Large-scale KRR implementation details are missing, impairing reproducibility.** The paper reports results on gold clusters (105,092 structures) and QM9 (110,000 training points) using full kernel ridge regression, but never describes how the KRR system was solved at these scales. Standard O(n³) matrix inversion is infeasible at n=110k (~10¹⁵ FLOPs), and naive O(n²) storage (~97 GB for double precision) is non-trivial. The paper mentions only that "inference is linear in n_train" and that "sparse KRR" is future work (lines 163, 292), but does not state what numerical linear algebra strategy (e.g., conjugate gradient with implicit matrix-vector products, Cholesky decomposition with optimized BLAS, distributed computing) was actually employed. Without this information, the large-scale experimental results cannot be independently reproduced or assessed for computational plausibility. This is the most significant weakness in the submission.

### Minor

- **The λ_max ablation is limited.** The paper claims "excellent performance can be achieved with low λ_max" (line 168) but only tests λ_max=3 for the two datasets (methane, QM9) where the λ_max scaling would be most constraining. No systematic sweep of λ_max is performed for any dataset to empirically characterize the accuracy-λ_max trade-off. This does not undermine the paper's core claims—the results at λ_max=3 are strong—but it leaves the generality of the "low λ_max suffices" claim less substantiated than it could be.

- **The methane comparison with REANN is caveated but the limitation is significant.** The paper notes that REANN achieves higher accuracy by training on forces, while the Wigner kernel implementation "does not allow to train with target gradients" (Section 4.2). The paper compensates with a note that preliminary results show LE-ACE and REANN are comparable when both use forces, but this indirect comparison weakens the methane section's central claim that Wigner kernels are "competitive with LE-ACE"—since LE-ACE itself is compared only on energies, while the strongest baseline (REANN) uses a different data modality.

### Trivial
None.

## Nice-to-Haves

- Wall-time scaling plots for the Wigner kernel evaluation as a function of ν_max, λ_max, and n_train, to empirically validate the theoretical scaling analysis (Section 3.4).
- An ablation study varying λ_max on at least one dataset, to empirically characterize the accuracy-cost trade-off and support the "low λ_max suffices" claim.
- Implementation of sparse KRR (e.g., Nyström or inducing points), which the paper identifies as the natural path to practical applicability (line 292).

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Comparison with Allegro on QM9 may be unfair because Allegro might train on both energies and forces."** — Removed. The QM9 energy benchmark is standardly conducted with energy-only training across the literature. The reviewer provides no evidence that Allegro's QM9 result (4.7 meV) uses force information. The paper's QM9 comparison follows the standard protocol. The methane-specific discussion about force training (Section 4.2) is properly caveated and does not apply to QM9.

2. **"Scaling analysis is incomplete/misleading; linear-in-ν claim ignores λ_max^7 and O(n³) scaling."** — Removed. The paper explicitly acknowledges both factors: λ_max^7 scaling (line 166: "the steep scaling with λ_max is a potential drawback") and KRR O(n³) scaling (implied by "full KRR models" discussion in lines 163, 292). The abstract's "linear with body order" claim refers specifically to ν-scaling of the kernel iteration, which is correct, and the paper does not present it as the complete cost picture.

3. **"The integrals in Eq. ... is a fragment—the description is cut off" (line 152).** — Removed. This is a formatting/parser artifact. The paper references an appendix (Section app:implementation) that was stripped by the PDF parser and likely contains the missing details. The hard rules instruct removal of criticisms about missing appendix content.

4. **"The paper never explains how the rotation and spatial integrals in Eq. 11 are evaluated."** — Removed. The method for evaluating these integrals is standard in the field (Gaussian overlap integrals, Wigner-D integration) and the missing details are likely in the stripped appendix. The paper's core contribution is the iterative construction, not the ν=1 base kernel evaluation.

5. **"No explanation for how KRR is tractable with 105,092 structures — a glaring omission."** — This is related to the Major weakness retained above but phrased more dramatically. The retained Major weakness captures the substantive concern without overstatement.

## Novel Insights

The harsh critic correctly identifies the KRR scalability omission as the paper's most significant weakness, but several of its criticisms (Allegro fairness, scaling analysis completeness) are factually incorrect when checked against the paper. The strength finder correctly identifies the core methodological contribution and the QM9 SOTA result. A genuinely novel observation that emerges from the reviews is that the paper's two most impressive experimental achievements (SOTA on QM9, body-order convergence on gold) are also the ones that raise the most acute computational feasibility questions—the paper would be substantially strengthened by a frank description of how KRR was actually implemented at these scales. Conversely, the least computationally demanding experiment (random methane) is where the method faces the stiffest challenge and where the comparison is most carefully controlled, lending credibility to those results.

## Suggestions

1. **Describe the KRR solver used for large-scale experiments.** State explicitly whether conjugate gradient, Cholesky with optimized BLAS, randomized SVD, or another solver was employed, along with approximate compute time and hardware. This is essential for reproducibility and for readers to assess computational plausibility.
2. Add at least one λ_max sweep (e.g., λ_max = 1, 2, 3, 4 on methane or QM9) to empirically support the "low λ_max suffices" claim.
3. Clarify in the abstract that "linear with body order" refers to the kernel evaluation cost per pair of environments, not the total training cost.

## Score and Decision

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>