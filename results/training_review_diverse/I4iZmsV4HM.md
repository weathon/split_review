## Summary

This paper presents ConcreTizer, the first tailored model inversion attack for voxel-based 3D point cloud feature extractors used in autonomous driving. The key insight is that naive point regression fails due to (1) zero-padding ambiguity (empty voxels and valid points at the origin are indistinguishable) and (2) VoI (Voxels of Interest) dispersion, where non-empty voxels spread into surrounding empty regions through convolution. To address these, ConcreTizer transforms the regression problem into Voxel Occupancy Classification (VOC) and introduces Dispersion-Controlled Supervision (DCS), which partitions the feature extractor at downsampling layers and trains each block individually with occupancy masking. Experiments on KITTI and Waymo with two backbones show consistent outperformance over both a point-regression baseline and the generative model UltraLiDAR.

---

## Strengths

1. **First rigorous study of 3D point cloud model inversion, identifying the unique VoI dispersion challenge**: The paper pinpoints a problem specific to voxel-based 3D backbones — that during forward and inverse processes, non-empty voxels spread into empty regions via convolution, creating false VoIs that dominate MSE loss and bias restoration toward the origin (Section 3, Figure 3). This problem has no analogue in 2D inversion and is clearly demonstrated with quantitative evidence.

2. **VOC elegantly resolves the zero-padding ambiguity**: By encoding each voxel as occupied (1) or empty (0), VOC eliminates the confusion between "empty space" and "points at the origin" that plagues naive regression. The ablation study (Figure 7) shows that even VOC with BCE loss enables restoration at layer 6, whereas point regression entirely collapses — validating the core insight that occupancy determination, not coordinate regression, is the real bottleneck.

3. **DCS provides a principled solution to VoI dispersion, well-validated by ablation**: DCS partitions the backbone at downsampling layers (where VoI density spikes — Figure 3, right) and trains each inversion block with per-block occupancy masking. Figure 7 shows that only ConcreTizer (VOC + DCS) produces a point distribution matching the original at layer 12, while VOC alone still shows biased restoration. Figure 8 confirms optimal performance with 2–4 DCS instances (aligned with downsampling layers) and degradation with overly fine partitioning (10 instances) due to error accumulation.

4. **Consistent outperformance across two major datasets and two backbones**: On KITTI and Waymo, with both VoxelBackbone and VoxelResBackbone, ConcreTizer exceeds UltraLiDAR by 23.4% CD and 12.4% F1 on KITTI, and by 21.1% CD on Waymo at the deepest layer (Table 1, Figure 6). The advantage holds at all layers, not only at the deepest.

5. **Downstream task validation confirms practical threat**: ConcreTizer-restored scenes achieve 75.4–86.7% of original 3D detection AP on KITTI and 62.6–75.7% on Waymo, while point regression yields unusable results and UltraLiDAR drops sharply on Waymo's complex scenes (Table 2). This grounds the privacy threat in a concrete AV-relevant task.

---

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **DCS training procedure is underspecified** (§4.3.2). The paper states that inversion blocks are trained "in block units" and that error accumulates with too many blocks, but it does not clarify whether blocks are trained sequentially (each block trained independently before being chained), jointly (end-to-end with gradient flow through all blocks), or iteratively (trained one at a time and then fine-tuned). The loss function (L_cls + β·L_reg) is given per block, but the inference-time wiring between blocks during training is not described. This ambiguity affects reproducibility. The paper should at minimum state: "Blocks are trained sequentially: block N is trained to restore f_{N-1} from f_N, then block N-1 is trained to restore f_{N-2} from the output of block N, etc." — or whatever the actual protocol is.

2. **The point-regression baseline is minimal and the comparison slightly overstates the advantage of classification over regression**. The paper compares against the regression method from Hwang et al. (2023) as-is: no learned occupancy filtering, no architectural improvements. The paper's own analysis correctly identifies the core failure mode (zero-padding ambiguity), but a regression approach augmented with a simple binary classification head (which would essentially be a regression-based VOC variant) is not tested as a control. This is not a structural flaw — the generative baseline (UltraLiDAR) is the more demanding comparison, and DCS is the more novel component — but the "regression fails, classification works" narrative would be stronger with an explicit control showing that what really matters is the combination of classification *and* dispersion control, not classification alone.

3. **No classification accuracy metrics reported for VOC** (§5.2, §5.4). The paper reports only final CD, HD, and F1 scores, but never reports VOC's precision, recall, or F1 for occupancy prediction at any layer. Reporting these would (a) directly validate that VOC correctly identifies which voxels are occupied, (b) help diagnose whether remaining errors come from classification mistakes or coordinate estimation, and (c) strengthen the claim that "once classification is achieved, localization is straightforward." Given that the entire method hinges on accurate occupancy prediction, this is a notable omission.

4. **The detector used for the main detection results (Table 2) is not specified**. The paper names SECOND only in the context of the augmentation experiments (Table 3, Figure 9) but does not state which detection model was used for the KITTI and Waymo detection benchmarks in Table 2. Since detection AP depends heavily on the detector architecture, this should be stated explicitly.

5. **UltraLiDAR baseline is not fine-tuned for the inversion task**. The paper acknowledges this (the encoder was modified to accept voxel features, then trained from scratch), but UltraLiDAR was originally designed for unconditional LiDAR scene generation. Some form of task-specific adaptation or fine-tuning of the generative backbone could have been explored. This does not invalidate the comparison — even without tuning, ConcreTizer outperforms consistently — but the advantage may be less extreme against a fully optimized generative baseline.

### Trivial

- The paper does not state the voxel resolution or coordinate ranges used for voxelization (§4.2), which would aid reproducibility.
- The intermediate regression targets c_i (channel values at non-first blocks) are described as "normalized" but the normalization scheme is not specified.
- The paper defers several training hyperparameters (learning rate, optimizer, batch size, inversion network architecture) entirely to supplementary material. While this is common practice, a brief summary in the main text would be helpful.

---

## Nice-to-Haves

- **Direct measurement of VoI suppression per layer**: The paper infers DCS's effect from final CD/AP. Computing the number of active voxels in restored intermediate features with and without DCS would directly demonstrate the suppression mechanism quantitatively (e.g., "DCS reduces false VoIs by X% at downsampling layer 2").
- **Privacy-specific leakage analysis**: Detection AP is a coarse proxy. Showing person re-identification or trajectory recovery from restored scenes would concretely demonstrate the privacy threat the paper warns about.
- **Cross-dataset generalization test**: Does the inversion model trained on KITTI transfer to Waymo without retraining? This would test the attack's generality and robustness to domain shift.
- **Runtime comparison**: For an attack method, computational cost matters. A brief comparison of training/inference time vs. baselines would be informative.

---

## Removed Points

These points are flagged to be removed per guidelines; treat them with caution:

- **"Domain of coordinates not specified"** (Harsh Critic §4.2): The paper describes voxelization of a 3D point cloud in ℝ^(k×3) with x,y,z channelized — coordinates are clearly in the original metric space. This is a misreading.
- **"Training hyperparameters not in main text"** (Harsh Critic §5.1): Per guidelines, undisclosed hyperparameters are a reproducibility nitpick and should be removed as a weakness. The paper appropriately references supplementary material.
- **"Missing appendix content"**: The reviewer mentions supplementary may clarify DCS training. Per guidelines, appendix-stripping by the parser is not an author error.

---

## Novel Insights

The most interesting insight from the reviews is about the relationship between classification accuracy and final restoration quality. Both the Harsh Critic and Strength Finder converge on the observation that the paper's strongest evidence is the ablation study (Figure 7) showing progressive improvement from BCE→SF loss→DCS. What is *not* clear from the current evaluation is whether the remaining gap to the original point cloud is dominated by classification errors (VOC false positives/negatives) or by residual localization errors in deeper blocks — and decomposing these two sources would sharpen the paper's contribution considerably. A second cross-cutting insight is that the tradeoff analysis (§5.6) reveals a fundamentally asymmetric vulnerability: empty-centric noise barely affects the attack while degrading utility, whereas feature-centric noise affects both, which suggests that defense strategies must target the non-empty voxels specifically — a finding that could guide future defense work.

---

## Suggestions

1. **Clarify the DCS training protocol explicitly in §4.3.2**: state whether blocks are trained sequentially, jointly, or iteratively, and how ground-truth intermediate features are provided during training.
2. **Add a table reporting VOC precision/recall/F1 at each layer** to the ablation study or restoration performance section — this would directly validate the core claimed mechanism.
3. **State the detector model used for Table 2** in §5.3.
4. **Add a brief note on voxel resolution and coordinate ranges** in §4.2.

---

## Score and Decision

MY FINAL SCORE: <pineapple>3.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>