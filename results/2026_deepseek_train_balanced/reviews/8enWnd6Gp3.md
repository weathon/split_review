## Summary

This paper introduces TetSphere Splatting, a Lagrangian geometry representation that uses deformable volumetric tetrahedral meshes (tetrahedral spheres) as primitives for 3D reconstruction. The method formulates deformation as a geometric energy optimization with bi-harmonic regularization of the deformation gradient field and non-inversion constraints, optimized via differentiable rendering. Experiments on multi-view and single-view reconstruction show substantially cleaner meshes (ALR, MR, CC Diff) compared to Eulerian and Lagrangian baselines, with competitive volumetric accuracy and computational efficiency.

## Strengths

1. **Massively cleaner mesh quality across all three proposed metrics** (verified in Table 1): ALR 0.6602 vs. DMesh's 0.1193 and FlexiCubes' 0.0722; MR 100% vs. DMesh's 9.09%; CC Diff 0.0 vs. DMesh's 3.75. These are not incremental — they represent a step-change improvement that directly validates the claim that volumetric tetrahedral primitives with geometric regularization resolve irregular triangles, non-manifoldness, and floating artifacts.

2. **Highest Volume IoU in both reconstruction tasks** (verified in Tables 1 and 2): Multi-view Vol. IoU = 0.6844 vs. next-best 0.5887 (FlexiCubes); single-view Vol. IoU = 0.6317 vs. next-best 0.5945 (Open-LRM). Combined with superior efficiency (Table 3: batch size 120 and 6.59 iter/s on a 40GB A100 vs. DreamGaussian's 80/4.43), the method offers a favorable accuracy-efficiency profile.

3. **Principled deformation framework with clear theoretical rationale** (Section 3, Eqs. 1–2): The formulation uses bi-harmonic energy on the deformation gradient field (not vertex positions), which the authors correctly argue avoids over-smoothing by regularizing relative rather than absolute deformation. The non-inversion constraint with soft penalty reformulation (Eq. 2) is clean and well-specified.

4. **Introduction of targeted mesh-quality metrics** (Section 5, lines 322–323): ALR (triangle uniformity), MR (manifoldness rate), and CC Diff (floating artifacts) expose a blind spot in standard reconstruction benchmarks. These metrics reveal that prior methods produce meshes that are geometrically accurate on CD/Vol. IoU but practically unusable — e.g., DMesh achieving only 9.09% manifold rate.

5. **Effective handling of thin/slender structures** (Section 5.3, lines 367–369): Qualitative results show the method captures fine details (fingers, sorter prongs, dress folds) that Eulerian grid-based methods miss — directly attributable to Lagrangian adaptive positioning.

## Weaknesses

### Major

- **The ablation study is essentially absent.** The only ablation (Fig. 9/line 405) is a single qualitative image showing coefficient sensitivity on one shape. There is no controlled experiment isolating the contribution of individual components: What happens without the bi-harmonic term? Without the non-inversion penalty? How does performance vary with the number of TetSpheres or tetrahedra per sphere? How does the silhouette-coverage initialization compare to a simpler alternative like random initialization or uniform grid? These are not peripheral — the method has two regularization terms plus an initialization algorithm, and the paper provides no quantitative evidence for their individual contributions. This is a significant gap in scientific rigor for a top-venue submission.

- **No variance or uncertainty estimates are reported.** Tables 1 and 2 report only point estimates with no standard deviations, confidence intervals, or per-shape distributions. With only 12 shapes in the multi-view evaluation, a single outlier can shift aggregated metrics substantially. The combination of a small evaluation set and no uncertainty quantification makes it impossible to assess whether the reported gaps are meaningful or within noise.

### Minor

- **The multi-view reconstruction evaluation uses only 12 shapes** (4 Thingi32 + 4 DeepFashion3D + 3 Objaverse/Adobe + 1 GSO). While this follows the precedent of the DMesh baseline, it is a thin basis for concluding "superior mesh quality" as a general property. The single-view evaluation on 30 GSO objects is more adequate but still on the smaller side.

- **The reconstruction accuracy (Chamfer Distance) is consistently worse than the best baseline, and this trade-off is not seriously engaged with.** In multi-view (Table 1), DMesh achieves CD 0.0136 vs. TetSphere's 0.0184 (a 35% relative gap). In single-view (Table 2), SyncDreamer achieves 0.0261 vs. TetSphere's 0.0351 (a 34% gap). The paper notes this through the word "competitive" but does not discuss whether the CD gap is fundamental to the representation or addressable (e.g., by adding a surface-fitting term). The paper treats accuracy and quality as independent axes rather than weighing the trade-off concretely.

- **The mesh quality metrics (especially ALR and MR) are aligned with what the method explicitly optimizes for.** The bi-harmonic energy penalizes non-smooth deformation gradients, which naturally produces uniform surface triangles (high ALR). The non-inversion constraint prevents element flips, which is related to manifoldness (high MR). This does not diminish the impressive magnitude of the gains — the gap over baselines is enormous — but it means the metrics are not fully independent validations; they partly reflect that the optimization objective and evaluation metrics are closely coupled. Downstream task validation (e.g., physics simulation, rendering under deformation) would strengthen the case that these quality improvements translate to practical benefit.

### Trivial

- The limitation about topology preservation (line 415) is stated only in the conclusion but bears on what the representation can and cannot represent — it should appear earlier in the method section.
- The Laplacian matrix discretization (lines 169–170) would benefit from a citation to the specific discretization used, as it is not obvious that the described block structure correctly discretizes the bi-harmonic energy on a tetrahedral mesh.

## Nice-to-Haves

- A downstream task evaluation (physics simulation, rendering under deformation) showing that the mesh quality improvements translate to practical benefits, which would substantially strengthen the paper's motivating claim that mesh quality matters for "downstream tasks such as rendering and simulation."
- A larger evaluation on a full benchmark (e.g., complete GSO or Objaverse-LVIS) to confirm that the mesh quality advantages hold at scale.
- Reporting the number of TetSpheres (M), vertices per sphere (N), and tetrahedra per sphere (T) used in experiments — these are natural implementation details that aid reproducibility.

## Removed Points

*These points are flagged to be removed; treat them with caution.*
- *"ICP alignment may mask reconstruction errors, making it unclear whether the Vol. IoU advantage reflects genuinely better geometry"* — removed as speculative; ICP is applied uniformly to all methods and is standard practice in the field.
- *"Missing F-Score, Normal Consistency, Edge Chamfer Distance, and Edge F-Score from main tables"* — removed; these metrics are mentioned in line 320 as also reported, and likely appear in the appendix (stripped by parser).
- *"The paper overclaims in the abstract and introduction"* — removed; the abstract's characterization of "competitive reconstruction accuracy" is defensible given the method achieves the best Vol. IoU in both settings and the CD gap is numerically modest.
- *"The number of TetSpheres (M), vertices per sphere (N), and tetrahedra per sphere (T) are not stated"* — potentially in the stripped appendix; not verifiable from the available text.
- *"FlexiCubes CC Diff of 201.3 is extraordinarily high and makes the comparison less informative"* — removed; this is an observation about a baseline, not a weakness of the paper.
- *"The paper's own thesis statement suggests a strengthening path"* — these are not weaknesses but suggestions; incorporated into Nice-to-Haves.
- *"The evaluation is too small to support the strength of the claims"* as an absolute statement — retained in weakened form as a minor weakness since the field standard is comparable.

## Novel Insights

The most informative synthesis from these reviews is the clear identification of a gap between the method's genuine engineering achievement and the thinness of its scientific validation. The reviewers converge on the same tension: the representation is novel, the formulation is principled, and the mesh quality results on the tested shapes are dramatic, but the evaluation lacks the rigor expected at a top venue — specifically, an absent ablation study and no uncertainty quantification. Notably, the harsh critic's strongest attacks (small evaluation, metrics measuring the optimization target) are partially mitigated by the fact that the improvements are orders of magnitude larger than what would arise from mere objective-metric alignment (100% vs. 9% manifold rate is not a measurement artifact). The paper's core weakness is not that its claims are false, but that the evidence provided is incomplete.

## Suggestions

1. **Add a quantitative ablation study on 5–10 shapes**: remove the bi-harmonic term, remove the non-inversion penalty, vary TetSphere count, and compare initialization strategies. Report both mesh quality (ALR, MR, CC Diff) and accuracy (CD, Vol. IoU) for each condition.
2. **Report per-shore results or standard deviations** for all metrics in Tables 1 and 2.
3. **Add a discussion section** explicitly addressing the CD gap: is it fundamental to the representation, or could a surface-fitting term close it without degrading mesh quality?
4. **Move the topology limitation** (line 415) from the conclusion to the method section.
5. **Add a citation** for the specific Laplacian discretization used for the bi-harmonic energy.

## Score and Decision

This paper presents a genuinely novel and well-motivated representation with strong preliminary results. The formulation is clean, the mesh quality improvements are striking, and the efficiency gains are real. However, the evaluation is significantly below the rigor expected at ICLR — the ablation study is essentially absent, no uncertainty estimates are provided, and the multi-view reconstruction comparison rests on only 12 shapes. The paper's core claims are likely correct, but the evidence as presented is insufficient for acceptance at a top venue.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>