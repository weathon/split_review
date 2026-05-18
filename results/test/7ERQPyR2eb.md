Now I have all the information I need. Let me synthesize the final consolidated review.

## Summary

Real3D-Portrait introduces a one-shot 3D talking portrait synthesis framework with four components: (1) a large Image-to-Plane (I2P) model pre-trained on synthetic EG3D multi-view data for accurate 3D reconstruction, (2) a lightweight Motion Adapter that predicts residual tri-plane diffs conditioned on PNCC for animation, (3) a Head-Torso-Background Super-Resolution (HTB-SR) model with occlusion-aware alpha-blending fusion, and (4) a generic Audio-to-Motion (A2M) model. The method convincingly outperforms all prior one-shot methods across both video-driven and audio-driven settings on comprehensive metrics and user studies, approaching the quality of person-specific RAD-NeRF.

## Strengths

- **Hybrid ViT+VGG I2P architecture demonstrably improves reconstruction.** The paper designs a two-branch network (SegFormer for coordinate transform, convolution for high-frequency texture) with normalization removed in the VGG branch to preserve identity-specific bias (Sec. 3.1, Fig. 2a). Ablation confirms that the 87M model significantly outperforms a 40M variant (FID 45.48→43.15, Table 5) with diminishing returns at 200M, validating the design choice.

- **Residual diff-plane motion adapter with Laplacian temporal loss achieves state-of-the-art animation accuracy.** Using PNCC as an identity-agnostic motion representation and predicting a residual tri-plane diff via a shallow SegFormer, the method achieves the best AED (0.111) and APD (0.018) among all video-driven baselines (Table 1). The Laplacian loss on consecutive diff-planes demonstrably reduces temporal jitter (AED 0.158→0.138, Table 5).

- **HTB-SR with alpha-blending fusion produces realistic torso/background without hollow artifacts.** The explicit separation of head, torso, and background with occlusion-aware fusion (Eq. 7) outperforms naive channel-wise concatenation, as confirmed by ablation (CSIM 0.737→0.758, FID 46.38→42.37, Table 5). This is a principled solution to a problem most prior work ignores.

- **State-of-the-art one-shot performance across both modalities.** Real3D-Portrait outperforms all one-shot baselines on every metric in same-identity reenactment (e.g., FID 37.50 vs. next-best 42.96, Table 1) and cross-identity reenactment (CSIM 0.758, FID 42.37). In the audio-driven setting, it achieves the best AED (0.146) and Sync score (6.565, Table 2). User study MOS scores confirm superiority in visual quality and lip synchronization (Table 3).

- **Pre-training on synthetic EG3D multi-view data is critically effective.** Ablation shows removing this pre-training causes a dramatic drop in CSIM (0.487 vs. 0.758) and FID (65.32 vs. 42.37, Table 5), providing direct evidence that distilling 3D prior knowledge is essential for one-shot reconstruction quality.

- **Comprehensive ablation studies isolate each component's contribution.** Every major design choice (pre-training, fine-tuning, model scale, Laplacian loss, alpha-blending fusion, background inpainting, keypoint source) is ablated with clear quantitative impact in Table 5, allowing readers to assess the value of each piece independently.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Overstated novelty claim about being "first" to support both modalities.** The paper claims to be "the first one-shot 3D face system that both supports audio and video-driven scenarios" (line 25) and "the first work that supports video/audio-driven applications" (line 271). While no existing one-shot 3D method explicitly demonstrates both modalities in a single framework, the comparison tables evaluate video-driven and audio-driven methods separately, making it unclear whether prior methods *could* support the other modality by plugging in an external audio-to-motion or video-to-motion module. The claim should be precisely scoped (e.g., "first one-shot 3D method to jointly demonstrate both modalities with a unified framework that also supports torso/background") to avoid unnecessary skepticism.

- **Camera pose handling is not explicitly specified.** The pipeline uses camera pose `cam` as input to the volume renderer (Eq. 4), and the evaluation states "the driving motion condition and head pose are obtained from a reference video" (line 155). However, the paper never explicitly states how camera poses are extracted — presumably from the same 3DMM fitting that yields expression parameters (lines 77, 147), but this is left implicit. For audio-driven scenarios, it is also unclear how the camera pose is handled (fixed canonical pose or some other mechanism). This omission does not invalidate the method (3DMM fitting is standard in the field), but clarifying it would improve reproducibility and eliminate a point of confusion.

- **Motion adapter training uses same-identity pairs; cross-identity generalization is not discussed.** During training, random frame pairs are drawn from the same video (same identity). During inference, cross-identity reenactment is performed (source and driving identities differ). The paper uses PNCC as an identity-agnostic representation (line 75) and concatenates PNCC_src and PNCC_drv as input to the motion adapter (line 91), which is a reasonable design. However, the paper does not explicitly discuss whether this design is sufficient for cross-identity generalization or provide any analysis of when/why it might fail. A brief discussion would strengthen the paper.

- **Temporal stability improvement claim for predefined 3DMM keypoints is qualitative only.** The paper claims that using predefined 3DMM keypoints for the torso branch "improves the temporal stability of the predicted torso" (line 117) compared to unsupervised keypoints, but this is supported only by a qualitative statement and the aggregate CSIM/FID difference (Table 5), not a dedicated temporal consistency metric (e.g., warping error or frame-to-frame smoothness). Adding such a metric would strengthen this ablation.

### Trivial
None.

## Nice-to-Haves

- A temporal consistency metric (e.g., average frame-to-frame difference) to quantify the torso stability improvement of predefined 3DMM keypoints over unsupervised keypoints in the HTB-SR ablation.
- An ablation comparing the residual diff-plane approach against a deformation-field variant of the same architecture, to cleanly demonstrate the claimed advantage over HiDe-NeRF-style deformation.
- A brief discussion of failure cases or limitations (e.g., extreme poses, heavy occlusions, unusual hairstyles) to increase credibility.
- Explicit statement of how camera pose is obtained from the video/audio driving signal (e.g., from 3DMM fitting of the reference video, or set to canonical for audio-only).

## Removed Points

- **Missing implementation details / "Implementation Details.io" criticism (Harsh Critic Point 2):** Removed because the text "Implementation Details.io in the future" (line 145) is a parser artifact that garbled the actual content, and the rule instructs to remove criticisms about formatting artifacts. Additionally, the paper's hyperparameters, loss weights, and architecture details are standard reproducibility concerns that the rules classify as nitpicks given the paper's primary empirical contributions. The original submission likely contained this information; the parser stripped it.

## Novel Insights

None beyond the paper's own contributions. The reviews surface useful suggestions for tightening presentation but do not reveal any insight about the paper's core claims that the authors themselves do not already articulate.

## Suggestions

1. **Precisely scope the novelty claim.** Replace "first one-shot 3D system that both supports audio and video-driven scenarios" with a more precise formulation (e.g., "first one-shot 3D method to jointly handle both modalities in a unified framework with realistic torso/background rendering"), which is accurate and avoids unnecessary pushback.

2. **Explicitly state camera pose handling.** Add a sentence clarifying that camera poses are obtained from the same 3DMM fitting that yields expression parameters (for video-driven) or set to a canonical pose (for audio-driven), to remove ambiguity from the pipeline description.

3. **Add a brief discussion of the motion adapter's cross-identity generalization.** Acknowledge that training uses same-identity pairs and explain why PNCC's identity-agnostic property (combined with the concatenated PNCC_src/PNCC_drv input) enables generalization to cross-identity reenactment.

## Score and Decision

**Originality:** Good — the paper combines several existing ideas (tri-plane, PNCC, ViT, EG3D pre-training) into a novel integrated system with well-motivated design choices (residual diff-plane, alpha-blending fusion, Laplacian loss).
**Importance:** High — one-shot 3D talking portrait synthesis is practically important, and the paper makes significant progress toward realistic results.
**Claims support:** Strong — extensive quantitative evaluation (Tables 1–3), user study (Table 3), and ablation (Table 5) support the claims, with the minor exception of the "first" claim which needs scoping.
**Soundness:** Good — the four-stage pipeline is clearly described, training objectives are well-defined, and ablations validate each component.
**Clarity:** Above average — the paper is generally well-structured and the contributions are clear, though camera pose handling could be more explicit.
**Value:** High — the method outperforms all prior one-shot approaches and approaches person-specific quality, suggesting it will be a strong baseline for future work.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>