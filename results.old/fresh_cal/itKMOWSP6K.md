Now I have all the information needed. Let me produce the consolidated review.

## Summary

FusionFormer proposes a transformer-based multi-modal fusion framework for 3D object detection that uses deformable attention to jointly sample from 2D image and 3D voxel features, avoiding the prior compression of voxel features to BEV space. The method achieves 75.1% NDS on the nuScenes test set, which is state-of-the-art, along with 72.6% mAP. It also demonstrates graceful degradation when a modality is missing and can be adapted to a camera-only configuration via a depth prediction branch.

## Strengths

- **Preservation of height information via voxel-level LiDAR features.** Ablation in Table 7 shows that using voxel features (67.3 NDS) outperforms BEV features (66.1 NDS), with notable reductions in center location error (mATE: 34.4 vs. 35.7) and orientation error (mAOE: 31.4 vs. 36.9). This empirically validates the paper's central argument that compressing the Z-axis loses useful information for 3D detection.

- **State-of-the-art single-model NDS on nuScenes without test-time augmentation.** Table 1 reports 75.1% NDS, surpassing all prior methods including CMT (74.1), BEVFusion4D (74.7), and BEVFusion (73.3). This is a genuine leaderboard improvement on the primary nuScenes metric.

- **Clear temporal fusion benefit demonstrated.** Table 2 shows that temporal fusion raises NDS from 73.2% (single-frame) to 74.1% (8-frame) on the val set, providing an explicit ablation of the temporal module's contribution.

- **Flexible camera-only variant outperforms BEVFormer.** Table 3 shows FusionFormer-Depth achieves 53.3% NDS and 43.9% mAP, compared to BEVFormer's 51.7% and 41.6%, demonstrating the framework's adaptability beyond the multi-modal setting.

- **Robustness to missing modalities is explicitly tested.** Table 4 shows the model retains 45.5 NDS with only cameras and 68.6 NDS with only LiDAR (vs. 74.1 with both), providing a concrete demonstration of graceful degradation under missing modalities.

## Weaknesses

### Fatal
None.

### Major
- **Table 8's fusion ablation does not isolate the fusion mechanism.** The text states that for the "addition" and "concatenation" baselines, "the image BEV features were obtained through BEVFormer" (line 304). This means the image features used by these baselines come from a different pipeline (BEVFormer) than FusionFormer's own image processing, while the LiDAR features may also differ. The comparison thus conflates the fusion operation with the feature extraction method. Consequently, the conclusion that "our proposed method enables enhanced fusion" is not supported by this experiment. To properly ablate the fusion mechanism, all baselines should use identical image and LiDAR feature representations, varying only how they are combined.

### Minor
- **The SOTA claim for both mAP and NDS is imprecise.** The abstract states "state-of-the-art single model performance of 72.6% mAP and 75.1% NDS." However, Table 1 shows BEVFusion4D achieves 73.3 mAP (higher than 72.6). NDS is genuinely SOTA, but mAP is not. While the phrase "state-of-the-art single model performance" could be read as overall combined performance being SOTA (which is debatable), the wording invites misinterpretation and should be clarified.

- **The "residual structure" claimed in the abstract and introduction is never technically specified in Section 3 (Method).** The abstract and introduction (lines 4, 23, 52) state that the fusion encoder "incorporates residual structures" to ensure robustness with missing modalities. However, the method section (lines 66–148) describes only self-attention, points cross-attention, images cross-attention, and feed-forward networks — standard transformer components — without any explicit description, equation, or diagram of where residual connections are placed, how they interact with modality masking, or why they specifically enable robustness. The modality mask is described (line 256) but that is a training augmentation, not a residual mechanism. This omission affects both reproducibility and the paper's claim about residual-driven robustness.

- **The robustness study (Table 4) lacks a baseline comparison.** Table 4 shows FusionFormer's performance with single modalities (C, L) and both (CL), which is useful as a self-diagnostic. However, no comparison is provided to standard fusion models (e.g., BEVFusion or CMT) under the same missing-modality conditions. Without a baseline, the claim of "strong robustness" is an internal reference point rather than a demonstrated advance over existing methods.

- **The camera-only comparison (Table 3) could better control for backbone/architecture differences.** FusionFormer-Depth is compared against BEVFormer but the paper does not specify BEVFormer's image backbone in this comparison. If the backbones differ, the improvement could partly come from the backbone rather than the FusionFormer architecture or the depth prediction branch. An ablation controlling for backbone choice would strengthen this result.

- **Some implementation details are missing.** The paper reports image backbone (VoVNet-99), LiDAR backbone (VoxelNet), input sizes, and BEV query size, but does not specify learning rate, optimizer, batch size, GPU count, or training time for the main results. These are standard to infer given MMDetection3D conventions but should be stated for full reproducibility.

- **No statistical variance is reported.** All results appear to be from single runs. Given that the val-set margins between methods are small (e.g., 74.1 vs. 73.5 NDS for temporal models in Table 2), it is unclear whether these differences are significant relative to run-to-run variation.

### Trivial
None.

## Nice-to-Haves
- An ablation of the number of fusion encoder layers (6 are used) would clarify whether performance saturates or could be reduced for efficiency.
- Adding a comparison of the robustness study (Table 4) against another fusion method (e.g., BEVFusion or CMT with modality dropout) would directly substantiate the robustness claim.
- Clarifying whether the "uniform sampling strategy" refers to uniform sampling of height anchors along pillars (which is described in lines 99–104) would help connect the abstract's terminology to the method's implementation.

## Removed Points

*These points were raised by reviewers but are removed after cross-checking against the paper; they should be treated with caution.*

- **"Temporal fusion encoder is never ablated"** (Harsh Critic). Removed because Table 2 explicitly compares FusionFormer-S (single-frame, 73.2 NDS) with FusionFormer (temporal, 74.1 NDS), which IS an ablation of temporal fusion. The criticism is factually incorrect.
- **"Uniform sampling strategy is not defined"** (Harsh Critic). Removed because Section 3.1 (lines 99–104) describes the sampling of 3D reference points from pillars with height anchors: "from each pillar corresponding to a query, we sample a fixed number of N_ref reference points... a set of height anchors {z_i} are defined along its Z-axis." The method is defined even though the term "uniform sampling" is not repeated verbatim in the method section.
- **"Missing implementation details (learning rate, optimizer, batch size)"** — these are minor omissions but the paper does state backbone choices, input sizes, voxel size, BEV resolution, epoch count, CBGS strategy, and query denoising. The omitted details (e.g., learning rate, batch size) are standard for MMDetection3D-based papers and can be inferred from the codebase. This is not a substantive weakness.
- **"Missing appendix, missing proofs, missing references"** — parser artifact. These sections exist in the original submission.

## Novel Insights

The most interesting observation emerging from these reviews is that the paper's claimed advantages are supported by different kinds of evidence with varying strengths. The core architectural idea — using deformable attention to directly sample from voxel-level (rather than BEV-compressed) LiDAR features — is well-supported by Table 7's direct comparison (voxel 67.3 vs. BEV 66.1 NDS) and by the overall strong NDS score. However, the paper's weakest evidentiary link is the fusion mechanism itself: the ablation that should isolate it (Table 8) is confounded by differing image feature pipelines, and the robustness claim hinges on a residual structure that is asserted but never described. This creates an unusual profile where the paper's headline contribution (height-preserving voxel fusion) is supported, but the more specific claims about fusion mechanism design and residual-driven robustness are not.

## Suggestions
1. **Redesign Table 8's ablation**: Use identical image features (extracted from the same backbone with the same view-transformer) and identical LiDAR features across all fusion methods (addition, concatenation, deformable attention). This would properly isolate whether deformable-attention-based fusion is superior.
2. **Add a residual structure description to Section 3**: Show where residual connections are placed in the encoder, with an equation or figure annotation, and explain how they interact with modality masking to enable robustness.
3. **Clarify the SOTA claim**: State explicitly that FusionFormer achieves SOTA NDS and competitive mAP, rather than the current phrasing which readers may interpret as SOTA on both metrics.
4. **Add robustness baselines**: Compare FusionFormer's single-modality performance (Table 4) to one or two standard fusion models under the same condition of missing modalities.

## Score and Decision

The paper presents a sound architectural contribution (voxel-level fusion via deformable attention, avoiding BEV compression) supported by strong benchmark results (SOTA NDS) and a clean temporal fusion ablation. The two most significant weaknesses — the confounded fusion ablation (Table 8) and the underspecified residual structure — are both addressable in revision and do not invalidate the paper's core contribution, which is independently supported by Table 7's voxel-vs-BEV ablation and the overall leaderboard standing. The paper's claims about the fusion mechanism itself need better evidence, but the overall method is clearly effective.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>