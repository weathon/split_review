## Summary

This paper proposes a point-based instance scene completion framework that adapts object-level point completion (which normally requires canonical coordinates) to scene-level completion without canonical alignment, while integrating sparse scene constraints (free/occluded space shells) via cross-attention. The authors also release ScanWCF, a new dataset that fixes alignment and collision issues in prior datasets (Scan2CAD, ScanARCW). Experiments show significant improvements over RfD-Net and DIMR in completion quality and collision avoidance.

## Strengths

- **Center-offset seed generator with global attention enables pose/scale-robust completion.** The paper predicts an object center and produces seed coordinates as offsets, combined with global attention in the seed generator. Table 3 provides direct ablation evidence that this design significantly improves both coarse and dense completion quality over the SeedFormer baseline under arbitrary pose and scale, matching and even beating canonical-coordinate performance.

- **Sparse scene constraints integrated via cross-attention improve plausibility.** The paper introduces a sparse point representation of free/occluded space (two bounding shells resampled to 10 cm resolution) and injects it into the seed generator through cross-attention. Table 4 shows a 7% relative improvement in completion quality (CD) and a 29% relative improvement in collision depth (COL) from this component alone. No prior point-based completion method incorporates scene constraints of this form.

- **ScanWCF dataset demonstrably fixes known dataset flaws.** The paper identifies specific problems in Scan2CAD (misalignment between partial scans and ground truth) and ScanARCW (collisions in ground truth), then constructs a new dataset with only 0.14% of points in collision (vs. 2.5% in ScanARCW), verified through optimization and manual correction (Section 4). This provides a cleaner evaluation benchmark for the instance scene completion task.

- **Strong evidence under controlled conditions (Table 2).** Under GT instance masks, the method achieves substantially better partial reconstruction fidelity (One-Sided CD: 0.057 vs. 0.239/0.246), completion quality (CD: 0.075 vs. 0.135/0.149), and collision avoidance (%COL: 0.87% vs. 3.02%/4.00%) compared to RfD-Net and DIMR. The gaps are large and consistent, demonstrating that architectural innovations — not instance segmentation differences — drive the improvement.

## Weaknesses

### Major

- **Missing comparison against DDIT (Li et al., 2023a), the most relevant contemporary baseline, weakens the SOTA claim.** DDIT is discussed at length in the related work (Section 2, line 35) as an instance scene completion method. It is described alongside RfD-Net and DIMR, yet it is never compared against in Tables 1 or 2. The stated justification is that DDIT "requires an iterative procedure for estimating object pose and a per scene optimization step... which is slow" — a criticism of computational cost, not output quality. If DDIT produces comparable or better completions, the paper's headline claim of "state-of-the-art performance" (abstract, conclusion) is unsupported. The comparisons against only RfD-Net (2021) and DIMR (2022) leave the most recent relevant baseline unaddressed. This is not a minor addition; it directly affects the paper's central claim.

### Minor

- **Ablation study conducted on a single ShapeNet category (chair).** Table 3 ablates the architectural design choices (VI-PointConv, center-offset prediction, global attention in upsampling) only on chairs (Section 5.5, line 176). While the main results on the full 34-category dataset (Tables 1, 2) demonstrate the complete method works, the ablation evidence for individual component contributions is narrow. Chairs have a specific structure (central body with legs/backrest, often symmetric). It is unknown whether the center-offset prediction or global attention behaves similarly for objects without clear centroids (e.g., tables, lamps, sofas) or where the partial observation covers a small fraction of the total shape. Expanding the ablation to 2–3 geometrically distinct categories would meaningfully strengthen the evidence for claimed generality.

- **Scene constraint parameter δ is unspecified.** The constraints are defined as "$P_{in} \pm \delta N_{in}$" (Section 3.3, line 72), but the value of δ is never reported, nor is there any sensitivity analysis. The 10 cm resolution is given, but δ controls the offset distance of the free/occluded shells from the surface. Without specifying δ, the method is not fully reproducible from the paper alone, and the robustness of the constraint representation to this parameter is unknown.

- **No variance or confidence intervals reported.** No standard deviations are reported for any metric in any table. Given the modest test set size (246 scenes), the significance of the reported gaps — especially for collision metrics in Table 2 — would be clearer with error bars.

## Nice-to-Haves

- Analyze how Mask3D instance segmentation errors (false negatives, oversegmentation) propagate to final completion quality. The pipeline depends on Mask3D, and a characterization of this failure mode would help assess real-world robustness.
- Discuss the selection bias from discarding scenes with "too many collisions" during ScanWCF construction. Since scenes with many collisions are excluded, the test distribution may skew toward easier scenes.
- Characterize cases where a single deterministic completion is inadequate (e.g., symmetrically ambiguous objects) and whether scene constraints help disambiguate.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **PaSCo dismissal "without quantitative comparison"**: REMOVED — factually incorrect. The paper states "our 2cm resolution indoor scans would require ∼4-5× more voxels than the outdoor scans with 20cm voxels used in their work," which is a quantitative justification.
- **Demand for SCARP comparison**: REMOVED — scope creep. SCARP is an object-level completion method, not scene-level. The paper correctly distinguishes this and explains why SCARP's pose-estimation approach is different.
- **OCR artifacts / formatting complaints**: REMOVED per rules (parser issues, not author errors).
- **Related works missing**: REMOVED per rules (do not mention missing related works without external confirmation).
- **Generic speculation about global shape descriptor expressiveness**: REMOVED — no concrete problem identified; the method demonstrably works across 34 categories in the main results.
- **Generic strength from Strength Finder (e.g., "this paper addressed an important problem")**: REMOVED — too generic/superficial.

## Novel Insights

None beyond the paper's own contributions. The two reviews largely converge on the same points: the core technical contribution (center-offset seed generator + sparse scene constraints) is solid and well-motivated, but the evaluation scope is narrower than the claims warrant. The most perceptive observation from the harsh review is that the exclusion of DDIT is a structural gap rather than a minor omission, and that the single-category ablation is a real evidential limitation rather than a nitpick.

## Suggestions

1. **Add DDIT as a baseline** in Tables 1 and 2, or provide a substantive, quality-based justification for exclusion that goes beyond implementation difficulty.
2. **Expand the ablation (Table 3)** to at least 2–3 additional geometrically diverse ShapeNet categories (e.g., table, sofa, lamp) to demonstrate that the architectural benefits generalize beyond chairs.
3. **Report the value of δ** used in the scene constraint construction and add a brief sensitivity analysis showing how completion quality or collision metrics vary with δ.
4. **Report standard deviations or confidence intervals** for the main quantitative results.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>