Now I have a thorough understanding of the paper and can verify the reviewer claims against the text. Let me write the consolidated review.

## Summary

The paper proposes SpherePose, a category-level object pose estimation method that replaces point-based NOCS representations with spherical representations (HEALPix grids) to achieve shape-independent correspondence learning. The method introduces three key designs: SO(3)-invariant point-wise feature extraction (using DINOv2 + a modified ColorPointNet++), a spherical attention mechanism for feature propagation across incomplete point clouds, and a hyperbolic correspondence loss that amplifies gradients near zero. Results on REAL275, CAMERA25, and HouseCat6D show competitive performance, including a 2.0% improvement over SecondPose (which shares the same DINOv2 backbone) on the 5°2cm metric.

## Strengths

- **Novel spherical representation for shape-independent correspondence learning.** The core idea—using the sphere as a shared proxy shape via HEALPix grids to define pose-only-dependent correspondence targets—is well-motivated and clearly addresses the semantic incoherence of point-based NOCS across diverse object shapes. The ablation in Table 3 (w/ point-based representation vs. full SpherePose, 49.8% vs. 59.6% on 5°2cm) directly supports the benefit of this representation.

- **Hyperbolic correspondence loss is well-motivated and empirically validated.** The gradient analysis in Figure 3 provides a clear rationale: L1/L2/smooth L1 losses have near-zero gradients around zero error, making precise predictions hard to learn. The ablation in Table 6 shows that hyperbolic L2 improves 5°2cm from 54.2% (L2) to 58.2%, a substantial gain, directly confirming the design.

- **Comprehensive ablation study across major design choices.** Tables 3, 4, 5, and 6 systematically ablate the spherical representation, feature interaction, number of transformer layers, and loss function, allowing the reader to attribute improvements to specific components.

- **Fair comparison with a backbone-matched baseline.** The paper explicitly compares with SecondPose, which also uses DINOv2 features and spherical representations, showing a 2.0% improvement on REAL275 5°2cm. This controls for the backbone advantage and supports the method-level contribution.

- **Clear problem formulation with good related-work positioning.** The paper articulates the shape-dependence problem in point-based NOCS (citing SOCS/Wan et al. 2023) and distinguishes itself from prior spherical representation works (VI-Net, DualPoseNet) on two axes: uniform vs. non-uniform grid sampling and correspondence-based vs. direct-regression paradigm.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **No rotation-only metrics reported.** All pose results are reported as combined 6D mAP (e.g., 5°2cm). Because rotation estimation is the paper's core contribution (translation and size are predicted by a separate, independent PointNet++ network), rotation-only metrics (e.g., angular mAP at 5°/10°) would directly validate the spherical representation's impact on the rotation module. The ablations (Tables 3, 5, 6) also use combined metrics, so it is unclear whether the reported improvements stem from better rotation, better translation/size, or both. This is the field-standard evaluation protocol, so it does not invalidate the results, but it weakens the ability to attribute gains to the claimed innovation.

- **Comparison with non-DINOv2 baselines is confounded.** The ablation shows that removing DINOv2 drops 5°2cm from 59.6% to 52.2% (a 7.4% absolute drop). Several baselines (e.g., AG-Pose, DPDN) do not use DINOv2, so their lower performance may partly reflect a weaker backbone. The paper fairly compares with SecondPose (same DINOv2) and shows a 2.0% gain, but claims of "superior performance" over methods like AG-Pose (3.5% gap) are difficult to attribute entirely to the spherical representation without a controlled experiment that adds DINOv2 to a point-based baseline.

- **The point-based ablation's experimental setup is underspecified.** Table 3 includes a "w/ point-based representation" variant that achieves 49.8% vs. 59.6% for the full method. The paper states this replaces spherical representation with direct point-to-NOCS prediction but does not clarify whether all other components (Transformer encoder, hyperbolic loss, feature extractors) are kept identical. Without this detail, the comparison is suggestive but not rigorous. Additionally, rotation-only metrics for this ablation are missing.

- **The SO(3)-invariance claim is reasoned but not experimentally verified.** The paper argues that DINOv2 features are robust to rotations (citing prior work) and that ColorPointNet++ achieves invariance by using RGB instead of XYZ. However, no quantitative experiment (e.g., rotating input point clouds and measuring feature stability or correspondence consistency) is provided to substantiate this claim. The ablation showing that removing these components hurts performance provides indirect evidence, but a direct test would strengthen the paper.

- **No analysis or visualization of feature propagation into empty spherical anchors.** The paper notes that "almost half of the spherical anchors" are empty due to self-occlusion and claims the attention mechanism fills them meaningfully. However, no ablation, visualization, or quantitative analysis shows that these inferred features are semantically coherent or beneficial beyond the aggregate performance gain reported in Table 4.

### Trivial

- **The term "shape-independent" is conceptually clear but never formally defined.** The paper states that spherical anchors are "coherent across various object shapes" and thus the spherical NOCS coordinates are shape-independent, but a precise definition distinguishing "shape-independent target" from "shape-independent mapping" would improve precision.

## Nice-to-Haves

- **Rotation-only and translation-only metrics** would allow the community to separately evaluate the rotation module (the paper's core contribution) and the translation/size module, making the ablation results more informative.
- **A controlled experiment adding DINOv2 to a point-based baseline** (e.g., DPDN with DINOv2 features) would disentangle backbone gains from representation gains and strengthen the claim that the spherical representation itself provides benefit.
- **Error bars or multiple-run statistics** would help assess the significance of the reported 1–2% margins.
- **A sweep over HEALPix resolution (Nside)** would justify the choice of Nside=8 and characterize the trade-off between granularity and computational cost.
- **Failure case analysis** (e.g., which object categories, poses, or occlusion levels the method struggles with) would add depth, especially for the challenging HouseCat6D dataset with transparent/reflective objects.

## Removed Points

*These points are flagged to be removed, treat them with caution*

- **Criticism about missing appendix/proofs.** The harsh critic's request for formal proofs is not applicable to this type of empirical computer vision paper; the paper provides the appropriate level of mathematical justification for its claims.
- **Criticism about the paper not discussing gradient instability of arcosh for large errors.** The paper's ablation (Table 6) empirically validates the loss works well; the theoretical one-sidedness is a minor observation that does not undermine the contribution. The paper mentions the gradient advantage near zero, which is the relevant regime for fine-tuning precise predictions.
- **Criticism about missing error bars / statistical significance.** Single-run evaluation without confidence intervals is standard practice in category-level pose estimation benchmarks (consistent with all cited prior work). This is a field-standard practice, not a deficiency of this paper.
- **Request for HEALPix resolution sweep.** This is an interesting follow-up experiment but not necessary to validate the core contribution at the chosen resolution.
- **Criticism equating "unfair comparison" directly without acknowledging the SecondPose comparison.** The paper does compare with a backbone-matched method (SecondPose) and acknowledges it, so the claim of unfair comparison is overstated.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective that the paper's authors have not already considered.

## Suggestions

1. **Add rotation-only metrics** (e.g., angular mAP at 5°/10°) to the main paper and all ablations. This is the single most impactful addition, as it directly validates the core claim about rotation estimation and would also strengthen the ablation analysis.
2. **Clarify the "w/ point-based representation" ablation** by explicitly stating which components (Transformer encoder, hyperbolic loss, feature extractors) are shared and which differ, and ideally report rotation-only numbers for this variant as well.
3. **Add a brief experimental verification of SO(3)-invariance** — for example, perturb the input point cloud by random rotations and measure the variance of predicted spherical NOCS or features. Even a small-scale experiment in the supplement would substantiate this claim.
4. **Tone down the language of "superior performance"** over non-DINOv2 baselines or add a caveat about backbone differences. The comparison with SecondPose already provides a fair benchmark.

## Score and Decision

The paper presents a well-motivated and technically sound approach with clean ablations supporting each design choice. The weaknesses identified are addressable and do not invalidate the core claims. The lack of rotation-only metrics is the most notable gap, as the paper's central contribution is about rotation estimation, but this is the field-standard evaluation and the ablations still demonstrate relative improvements. The paper would be strengthened by the suggested additions but is already a solid contribution in its current form.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>