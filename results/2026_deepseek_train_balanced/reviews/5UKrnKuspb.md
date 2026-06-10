## Summary

NeuralPlane proposes an annotation-free pipeline for multi-view 3D plane reconstruction that fuses inconsistent 2D plane observations into a unified neural field representation. It uses a monocular module to extract 2D plane segments, a geometry branch with plane-guided regularization (normal consistency + pseudo-depth supervision), and a semantics branch combining a Neural Coplanarity Field (NCF) trained via contrastive learning with a Neural Parser for semantic discrimination. The method achieves strong results on ScanNetv2 and ScanNet++, outperforming baselines (including supervised approaches) across both geometric and segmentation metrics.

## Strengths

- **State-of-the-art results without plane annotations**: Tables 1 and 2 show NeuralPlane outperforming all baselines on both ScanNetv2 (8 scenes) and ScanNet++ (4 scenes) across all five metrics (Chamfer Distance, F-score, RI, VOI, SC), despite never using ground-truth plane labels. It beats ObjectSDF++ (which uses ground-truth instance annotations) on segmentation metrics while relying only on machine-predicted masks — a genuinely impressive result.

- **Geometry-gated contrastive learning is a principled design for over-segmented primitives**: The push loss in Eq. (8) only treats two local planar primitives as negative pairs when their estimated plane geometry differs (‖ōₐ − ō_b‖ > tₒ or ‖n̄ₐ · n̄_b‖ < tₙ). This gating prevents pushing apart features that belong to the same real plane across different views — a naive contrastive loss applied to over-segmented 2D primitives would mishandle this ambiguity.

- **Joint refinement of plane parameters through the neural field**: Gradient signals from the pseudo-depth loss (ℒₚ₋dₑₚₜₕ) backpropagate through to the estimated plane parameters π̄ₐ (line 62), enabling initially noisy local plane estimates to be corrected during training. This self-correcting loop between the neural field and parametric primitives is a novel departure from prior work where plane parameters are fixed or decoupled.

- **Systematic ablation confirms synergy of components**: Table 3 shows that removing any component degrades performance across all metrics while the full model excels. This provides clean evidence that the specific combination, not any single element, drives the result.

- **Level-of-detail control via semantic prototypes**: Section 4.3 and Fig. 7 demonstrate that varying Nₚ adjusts the granularity of plane decomposition, offering a controllable trade-off — a capability absent from prior plane reconstruction methods.

- **Cross-dataset generalization to unseen layouts**: On ScanNet++ (Table 2), where scenes have layouts not encountered by the pre-trained models, NeuralPlane still achieves competitive geometry and top segmentation, supporting robustness beyond the primary testbed.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **NCF push loss does not address the paper's own motivating example**: The paper motivates NCF with the case of a door that is geometrically coplanar with but semantically distinct from the enclosing wall (lines 69–70), and frames NCF as "the core driver of involving the semantic separation via contrastive learning" (line 23). However, the push loss (Eq. 8) activates **only** when two primitives have different geometry (‖ōₐ − ō_b‖ > tₒ or ‖n̄ₐ · n̄_b‖ < tₙ). For the door-wall case — where both primitives share similar offset and normal — the indicator evaluates to false and no push signal is applied. The semantic separation in practice relies on the monocular module's over-segmentation being preserved by the pull loss, and on the Neural Parser's prototype assignment. The paper overstates what the contrastive loss alone contributes to semantic separation; this is a framing mismatch between the claimed contribution and the actual formulation. The method still works empirically, but the paper's central narrative about NCF's role should be revised.

- **Ablation models A–C are underspecified**: Table 3 references "Models A through C" (line 164) but never explicitly states which component each removes. The text says they "struggle with insufficient geometric guidance," suggesting they are geometry-related ablations, but the specific configuration of each model is left unclear. This undermines the reproducibility and completeness of the ablation study.

- **Evaluation limited to 12 scenes without variance reporting**: The experiments use 8 scenes from ScanNetv2 and 4 from ScanNet++ (line 123). No error bars, confidence intervals, or per-scene breakdowns are reported. While this sample size follows standard practice from prior work (Xie et al., 2022) and the datasets are challenging, it limits confidence in the robustness of the claimed superiority.

- **Unsubstantiated "40× training speedup" claim**: Line 153 states that representing geometry as volume density "allows for a 40× training speedup compared to other neural implicit methods," but no comparison methods are named, no training times for baselines are provided, and no supporting evidence appears in the captured text. While ~6 minutes training time is reported (line 140), the speedup claim itself is unverifiable.

- **No discussion of failure cases or limitations**: The paper presents only successful results. There is no analysis of conditions where NeuralPlane might fail — e.g., curved surfaces, heavy clutter, scenes where the monocular module produces poor segmentations. A limitations paragraph would strengthen the paper and guide future work.

- **Joint plane parameter refinement is not ablated**: The paper enables gradient descent over plane parameters (line 62) but does not include an ablation that freezes them to verify this refinement actually helps.

### Trivial
None.

## Nice-to-Haves
- Report per-scene results alongside aggregate metrics.
- Analyze sensitivity to Neural Parser's DBSCAN hyperparameters, which determine online centroids.
- If the two "robust vision models" used in the monocular module are not named in the full paper (Section 3.1 is missing from this extraction), explicitly identify them for reproducibility.

## Removed Points

The following were removed from the harsh critic/strength finder inputs with brief justification:

- **"Two robust vision models" never named**: Section 3.1 is missing from the parser extraction; this detail likely exists in the original submission. Removed as a parser artifact.
- **RANSAC thresholds not discussed**: Generic concern that applies to any RANSAC-based method; the paper cites standard practices. Removed.
- **"40× training speedup" listed as a strength**: Conflicts with verified weakness that the claim is unsubstantiated. Removed from strengths.
- **Concerns about degenerate solutions in plane parameter refinement**: Speculative — no evidence presented that this occurs in practice. Removed.
- **Reference to "1 for more details" at end of Section 3.3**: Parser artifact. Removed.
- **Generic strength about "addressing an important problem"**: Insufficiently specific to this paper's contributions. Removed.
- **Missing related works**: Per policy, cannot verify external references. Removed.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- Revise the framing of NCF's contribution: either reformulate the push loss so that semantically distinct but geometrically coplanar primitives are pushed apart (e.g., by using the monocular segment labels directly as the source of negative pairs, with the geometry gate as an auxiliary term), or explicitly clarify in the paper that semantic separation is a joint product of the monocular over-segmentation, the pull loss, and the Neural Parser, with the push loss handling only geometrically distinct planes.
- Specify the exact configurations of Models A, B, and C in Table 3.
- Substantiate or remove the 40× speedup claim by providing direct wall-clock training time comparisons against named baselines on the same hardware.
- Add a limitations paragraph discussing failure cases.
- Provide per-scene results or error bars to support the statistical significance of reported improvements.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>