- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 8, 6
Now I have a thorough understanding of the paper. Let me synthesize the final consolidated review.

## Summary

The paper proposes MaskFeat3D, a masked autoencoder for point cloud pretraining that predicts intrinsic surface features (normals and surface variation) at masked points instead of their Cartesian positions. It also introduces an attention-based decoder that is encoder-agnostic, working with ViT, PointNet++, and sparse CNN backbones. Experiments on classification, part segmentation, few-shot learning, and scene-level detection show consistent improvements over prior MAE-based approaches.

## Strengths

- **Encoder-agnostic decoder design works with diverse backbones.** The decoder uses only block feature pairs from any encoder. Experiments confirm it works with ViT, PointNeXt (PointNet++ variant), and MinkowskiNet (sparse CNN), consistently improving over scratch training of those encoders. This is a practical contribution that generalizes beyond transformer-specific MAE methods.

- **Self-attention in the decoder is critical and well-ablated.** Removing self-attention layers from the decoder causes a 2.0-point accuracy drop on ScanObjectNN (line 209). This cleanly validates the design choice of propagating information among query points, going beyond the cross-attention-only design used by some prior work (e.g., MaskDiscr).

- **Systematic ablation covering multiple design dimensions.** The paper ablates masking ratio (60% optimal), decoder depth (sweet spot at 4 blocks), target feature combinations (normals + variation best), query point ratio, and data augmentations. These ablations provide concrete, quantitative evidence for the design decisions.

- **Consistent improvements across diverse downstream tasks.** Beyond classification, the method shows gains on part segmentation, few-shot classification, and scene-level 3D object detection, supporting the claim of general-purpose representation learning.

## Weaknesses

### Fatal
None.

### Major

- **Core claim is confounded: the superiority of feature prediction vs. position prediction is not cleanly isolated from decoder architecture.** The paper claims that predicting intrinsic features (normals + surface variation) is superior to predicting point positions. The evidence compares the authors' method (attention-based decoder + features) against PointMAE (FC-based decoder + positions). This changes two variables simultaneously. The paper's "Decoder design" ablation (lines 199-200) compares their attention decoder predicting features against PointMAE's FC decoder predicting features — this shows the attention decoder is better, but does not isolate the *target choice*. The missing experiment is straightforward: use the authors' own attention-based decoder to predict point positions (via Chamfer distance or MSE loss) and compare downstream performance against feature prediction with the same decoder. Without this control, the paper's central claim that "restoring intrinsic point features is superior to point location recovery" is not fully substantiated — the observed gains could be driven primarily by the decoder structure rather than the choice of target. This is fixable with one additional experiment and does not invalidate the overall method (which clearly works well), but it does mean the paper overstates the specificity of what drives improvement.

### Minor

- **The scene-level extension introduces an unresolved tension with the paper's core thesis about target features.** On ScanNet (real scans), surface normal has "minor influence" (line 218), and the authors instead use color + surface variation to obtain gains. This contradicts the paper's main message that normals + variation are the ideal targets. The paper acknowledges this observation but does not discuss *why* normals break down on real data (noise? irregular sampling?) or what this implies about the generality of the proposed targets. Since this section is framed as an extension, the impact is limited, but the paper would benefit from an honest discussion of this limitation and an analysis of when different feature targets are appropriate.

### Trivial

- None.

## Nice-to-Haves

- **Missing baseline: PointMAE with the PointNeXt encoder.** The paper shows MaskFeat3D+PointNeXt beats PointNeXt from scratch, but does not compare to PointMAE+PointNeXt. This would help disentangle whether the benefit comes from the pretraining approach or simply from having a pretrained encoder on top of PointNeXt.

- **Few-shot results mentioned but numbers not visible in the extraction.** If the tables are present in the original submission, this point is moot.

## Removed Points

- **Criticism that the decoder uses masked point positions as queries (positional information leakage):** REMOVED. The paper is transparent about this (lines 82, 132), explicitly stating that positional information is "encoded implicitly" and that they avoid *explicit* position reconstruction as a loss target. The rhetoric is precise and not misleading.
- **Missing related works:** REMOVED per instructions (cannot verify from external sources).
- **Formatting/style nitpicks, typos, reproducibility complaints:** REMOVED per instructions (parser artifacts / not substantive).
- **Generalized or speculative criticisms (e.g., "evidence is weak for the claims") without concrete anchor:** REMOVED.
- **Strengths that are generic/superficial:** The strength "the paper addresses an important problem" is generic and removed. The strengths listed in the final review are those with specific, concrete evidence.

## Novel Insights

None beyond the paper's own contributions. The most interesting observation from the reviews is the parallel between this work and the 2D MAE literature (Wei et al.'s finding that HOG/feature targets beat raw pixels in 2D). The paper explicitly draws this connection, and it's well-taken.

## Suggestions

- Add the missing controlled ablation: train the proposed attention-based decoder with position prediction (Chamfer distance or MSE) as the target, and compare downstream performance to the same decoder with feature prediction. This will either strongly confirm or reframe the core claim.
- Add a brief discussion in the scene-level section explaining why surface normal becomes less effective on real scans (noise? inconsistent orientation estimation? etc.) and what this implies about the generalizability of the proposed targets.
