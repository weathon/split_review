Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper presents the first in-depth study of model inversion attacks on voxel-based 3D point cloud feature extractors. It identifies two unique challenges — semantic ambiguity of zero-padded voxels (which makes point regression cluster points near the origin) and VoI dispersion (non-empty voxels spreading into empty neighboring voxels through convolutions, especially at downsampling layers). To address these, the authors propose ConcreTizer with Voxel Occupancy Classification (VOC, converting regression to binary occupancy classification with focal loss) and Dispersion-Controlled Supervision (DCS, partitioning the feature extractor at downsampling layers and training each block with explicit masking). Experiments on KITTI and Waymo with two backbones show ConcreTizer substantially outperforms both point regression and a generative baseline (UltraLiDAR), and the restored scenes retain 62.6–86.7% of original 3D detection performance.

## Strengths

1. **First effective inversion attack for 3D point cloud scenes, exposing a real privacy vulnerability.** The paper contradicts the assumption (Hwang et al., 2023) that disseminating 3D features inherently prevents restoration. Table 2 shows restored scenes enable 3D object detection at 62.6–86.7% of original performance, confirming the restored data is practically usable for privacy-compromising tasks.

2. **Identifies and solves a challenge unique to 3D inversion: VoI dispersion.** The paper pinpoints that non-empty voxels spread into surrounding empty voxels during downsampling, causing false positives and clustering near the origin (Section 3, Figure 3). This phenomenon has no analog in 2D inversion. DCS mitigates this by partitioning at downsampling layers and applying per-block masking (Section 4.3.2, Figure 4). The ablation (Figure 7) validates that only VOC+DCS recovers a distribution matching the original point cloud.

3. **Transforming regression to occupancy classification resolves the zero-padded-voxel ambiguity.** The insight that a zero channel value is semantically ambiguous (empty voxel vs. point at origin) is cleanly addressed by binary occupancy classification (Section 4.3.1). This eliminates the clustering problem that plagues point regression (Figure 5, Table 1). Using Sigmoid Focal Loss correctly handles the severe label imbalance inherent in sparse 3D data.

4. **Rigorous evaluation across datasets, backbones, and downstream tasks.** Experiments cover KITTI and Waymo, two major feature extractors (VoxelBackbone, VoxelResBackbone), multiple metrics (CD, HD, F1), and 3D object detection validation (Table 2). ConcreTizer consistently outperforms both point regression and the UltraLiDAR generative baseline across all settings.

5. **Informative ablation and analysis of design choices.** The paper systematically ablates VOC vs. VOC+DCS (Figure 7) and studies DCS partitioning policies (Figure 8), finding that 2–4 blocks aligned with downsampling layers works best, while too many blocks accumulate error. This provides clear practical guidance.

6. **Analysis of defenses and privacy-utility trade-off.** Experiments with point cloud augmentations and Gaussian noise (Section 5.6, Table 3, Figure 9) show defenses degrade detection accuracy before meaningfully increasing restoration error, highlighting the difficulty of mitigating ConcreTizer without harming utility.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims are well-supported by experiments. The issues below are about clarity and depth, not validity of results.

### Minor

1. **DCS training procedure is underspecified.** The paper states DCS "trains each segment individually" (Section 1) and "performs restoration progressively" (Section 4.3.2), and that "the restoration error of each block accumulates" (Section 5.5), which suggests a cascaded architecture. However, the exact training protocol is ambiguous: are blocks trained independently in sequence (with ground-truth features serving as targets at each partition point), or is the entire cascade trained jointly? The paper provides the per-block loss but does not specify whether gradients flow through multiple blocks, how ground-truth intermediate features are obtained, or whether blocks share weights. This matters for reproducibility and for understanding whether DCS's benefit comes from multi-stage supervision or from architectural partitioning alone. The main text should clarify the training procedure; if it is deferred to supplementary materials, this should be explicitly stated and the key protocol summarized.

2. **The UltraLiDAR generative baseline adaptation lacks sufficient detail.** The paper states it "modified the encoder part of UltraLiDAR to accept voxel features as an input" (Section 5.2) but does not describe what changes were made, whether the model was re-trained from scratch or fine-tuned, or what hyperparameters were used. Since UltraLiDAR was originally designed for unconditional or 2D-conditioned generation, the modification is non-trivial. The paper correctly identifies that UltraLiDAR converts 3D sparse features to 2D dense features and loses detail — which is a plausible explanation — but without knowing the quality of the adaptation, a reader cannot assess whether UltraLiDAR could perform better with a more tailored conditioning mechanism. The comparison is informative as-is (the gap is large and consistent), but the paper would benefit from a brief description of the adaptation or a candid acknowledgment of this limitation.

3. **VoI dispersion is characterized only qualitatively.** The paper's entire motivation hinges on VoI dispersion (Section 3, Figure 3), stating "the density of VoI spikes significantly at downsampling layers" and "increases exponentially." Yet no quantitative measurement is provided — e.g., the number of non-zero voxels at each layer, the true-to-false VoI ratio, or how DCS reduces these counts. While the final restoration metrics (Table 1) and ablation (Figure 7) empirically validate the approach, directly measuring VoI dispersion would strengthen the causal narrative and distinguish DCS's mechanism from other forms of multi-stage training. A diagnostic plot showing voxel counts per layer in forward/inversion passes with and without DCS would be a clean addition.

4. **Computational cost of DCS vs. end-to-end is not discussed.** The paper does not address whether partitioning increases training time (if blocks are trained sequentially) or memory footprint (if trained jointly). For practitioners evaluating the method, this is useful context.

### Trivial

1. The terms "VoI" (Voxel of Interest) is defined primarily as non-empty voxels in the inversion process, but the paper sometimes uses it to refer to originally non-empty voxels vs. voxels that become non-empty during inversion. A consistent distinction between "true VoI" (originally non-empty) and "false VoI" (originally empty but non-zero during inversion) — the paper already introduces this in Section 3 but could use it more consistently throughout.

## Nice-to-Haves

- A quantitative plot of non-zero voxel count per layer for forward pass, inversion without DCS, and inversion with DCS, directly validating that DCS suppresses VoI spread.
- An ablation comparing (a) end-to-end VOC training with a single deep model vs. (b) VOC with intermediate auxiliary losses at downsampling points *without partitioning*, to isolate the effect of architectural partitioning from the effect of additional gradient signals.
- A brief discussion of the relationship between voxel size and the practical localization error of placing points at voxel centers, noting cases where large voxels could reduce attack precision.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **DCS training ambiguity about "learning rates per block" and other hyperparameters:** The reviewer demanded specific learning rates, batch sizes, optimizer, etc. Per the hard rules, these are reproducibility nitpicks that are standard to defer to supplementary materials.
- **Missing training costs of UltraLiDAR relative to ConcreTizer:** Request for training time/data requirements is a reproducibility detail per hard rules.
- **"Missing appendix / proofs / references":** The paper references supplementary materials for structural details and further experiments; the parser strips appendix sections. The paper's structure is standard for this class of submission.
- **Generic framing of "the paper should also cover Y / domain Z / additional tasks":** The paper clearly scopes itself to voxel-based feature extractors for autonomous driving scenes. Demands for broader coverage (e.g., non-voxel representations beyond a future work mention) are scope creep.

## Novel Insights

Beyond the paper's own contributions, the reviews surface one novel observation that the paper itself does not fully articulate: **the paper's approach reveals a fundamental asymmetry in inversion difficulty between 2D and 3D data.** In 2D, inversion attacks succeed because pixel values are dense and regression targets are unambiguous. In 3D, the extreme sparsity turns the naive regression approach into a pathological problem — the loss is dominated by empty voxels, and convolution-induced spread of non-zero values creates false positives at scale. The paper's key insight is that for sparse 3D data, *existence* is the hard problem and *localization* is the easy one (bounded by voxel size), which is the reverse of the dense 2D setting. This observation could guide future work on inversion attacks for other sparse modalities (e.g., event cameras, sparse radar).

## Suggestions

1. Clarify the DCS training protocol explicitly in the main text: are blocks trained independently (each with ground-truth intermediate features as targets), sequentially (output of one block fed as input to the next during training), or jointly? State the training order and whether blocks share weights.
2. Add a 2–3 sentence description of the UltraLiDAR adaptation (what was modified, how it was trained) so readers can assess baseline fairness.
3. Include a simple diagnostic figure showing non-zero voxel counts per layer in forward/inversion passes with and without DCS, to directly validate the VoI dispersion claim quantitatively.

## Score and Decision

The paper makes a clear contribution to an underexplored problem. The core ideas (VOC and DCS) are well-motivated, the experimental evaluation is thorough, and the results are convincing. The weaknesses are about clarity and depth of analysis, not about validity of the claims. The paper can be strengthened with relatively minor revisions.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>