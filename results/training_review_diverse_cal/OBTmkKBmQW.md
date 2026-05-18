Now I have a thorough understanding of the paper. Let me construct the final consolidated review.

---

## Summary

MotionFlow introduces a camera-trajectory-guided video generation framework that jointly encodes camera and object motion into pixel-level representations via a reference motion network (a separate SD1.5 UNet), avoiding the confusion caused by learning camera and object motions with separate modules. A semantic encoder (initialized from DINO) extracts object-aware priors to improve foreground consistency. On RealEstate10K, the method achieves lower trajectory errors (rotation/translation across three SfM estimators) and better visual quality (FID: 40.29, FVD: 176.21) than CameraCtrl and MotionCtrl, with ablations confirming the contribution of each component.

## Strengths

- **Integrated pixel-level motion representation is well-motivated and validated by ablation.** Rather than modeling camera and object motions through separate modules (as in MotionCtrl), the paper converts both into pixel trajectories via a reference motion network. The ablation (Table 4) shows that removing this network causes large drops in all metrics (FID: 40.29→58.16, FVD: 176.21→338.79), directly confirming that the integrated pixel-flow design is critical to performance.

- **Consistent quantitative outperformance across trajectory alignment and visual quality.** On RealEstate10K, MotionFlow achieves lower rotation and translation errors than CameraCtrl and MotionCtrl across all three SfM estimators (Dust3R, VggSfM, ParticleSfM) for both basic and difficult trajectories (Table 1). It also achieves the best FID (40.29), SSIM (0.532), PSNR (12.82), LPIPS (0.705), and FVD (176.21) among compared methods (Table 2). On the unseen outdoor dataset DL3DV-10k, it again achieves the best FID (48.66) and FVD (212.32), demonstrating generalization beyond its training domain (Table 3).

- **Semantic extractor meaningfully improves foreground consistency.** The semantic encoder (Section 3.3) identifies salient object regions and injects them via object attention into the generation network. Ablation (Table 4, row 2) confirms its contribution: removing it raises FID from 40.29 to 46.78 and FVD from 176.21 to 214.79.

- **Application to 3D scene reconstruction from a single image (Section 4.4) demonstrates practical utility.** A video generated from one reference image with a panoramic trajectory can feed into standard 3D reconstruction, confirming geometric consistency beyond what metrics alone capture.

## Weaknesses

### Fatal
None.

### Major

1. **Comparison against CameraCtrl/MotionCtrl lacks explanation of how text-conditioned baselines were adapted to use image prompts.** The paper states "we trained all the methods on the RealEstate10K dataset and tested them using the same camera trajectories and image prompts" (Section 4). Both CameraCtrl and MotionCtrl were originally designed for text prompts — replacing CLIP text features with CLIP image features is a significant architectural modification that is not described. Without knowing how this adaptation was done (or whether it was done correctly), the reader cannot assess whether the comparison is genuinely fair or whether the observed gains partially reflect asymmetric conditioning capability. This is the most consequential weakness because it affects the believability of the paper's central quantitative claims. (Note: the claim itself — that image prompts were used for all methods — is assumed to be true; the problem is the absence of description, not the claim.)

2. **The toy experiment on reference motion maps (Section 4.3) is too weak to support the claim that RMMs encode optical flow.** The experiment uses 12 training pairs from a *single* generated video and tests on 2 held-out pairs. With such a tiny training set and a small network (3 deconv + 2 conv layers), the network could easily memorize the mapping. The stronger claim that RMMs have "more abundant information than OFs" is entirely unsupported by this experiment. A systematic evaluation across many videos with proper train/test separation and baseline comparisons (e.g., random features, raw image features) would be needed to substantiate the interpretation that RMMs genuinely encode pixel-level motion rather than simply being correlated features that a small network can overfit to.

### Minor

1. **The term "motion extractor" is used once (Section 3.6) and never defined.** Section 3.6 states "In the first stage, we train the Trajectory Encoder and motion extractor" but the method sections (3.3, 3.4, 3.5) make no mention of a "motion extractor." It is unclear whether this refers to a sub-component of the reference motion network, the semantic encoder, or something else entirely. Additionally, Section 3.3 promises that the semantic encoder's training will be detailed in Section 3.6, but Section 3.6 does not mention the semantic encoder at all — it only mentions the "Trajectory Encoder and motion extractor." These discrepancies hurt reproducibility.

2. **No discussion of inference cost.** The method uses two large diffusion models (a reference motion network SD1.5 UNet + the base AnimateDiff UNet). The paper reports no inference time, parameter count, or FLOPs. Given the practical relevance of camera-controlled video generation, the computational overhead of the twin-diffusion design should be acknowledged.

3. **Citation inconsistency for SD1.5.** Section 3.4 cites Voleti et al. (2024) as the source for the "pretrained image stable diffusion (SD1.5 Unet) architecture," but Voleti et al. is a different work (SV3D). Section 3.6 correctly cites Rombach et al. (2022) for SD1.5. This is a small error but suggests uneven proofreading.

4. **Limited discussion of failure cases.** The Conclusion acknowledges the absence of explicit object motion control as a limitation, but there is no discussion of when the method breaks — e.g., extreme viewpoint changes, scenes with many small objects, or out-of-distribution camera trajectories. Figure 5 shows some qualitative artifacts in baselines but not in MotionFlow itself.

### Trivial
- Table 1 layout is compressed (three SfM methods × two trajectory difficulties) and column labels could be clearer when cross-referenced with the text.
- The sentence "CameraCtrl and MotionCtrl are three baseline methods" contains a stray word ("three") — a parser artifact but should be caught in camera-ready.

## Nice-to-Haves
- A controlled experiment replacing the image prompt with a text prompt in MotionFlow (using a text-conditioned SD as the reference network, or CLIP text features) and comparing to CameraCtrl/MotionCtrl would cleanly isolate the effect of the motion-flow mechanism from the conditioning modality. This is the cleanest way to address the comparison concern.
- Reporting FVD confidence intervals or multiple-seed runs would strengthen the quantitative claims.
- A finer-grained ablation ablating *just* the reference motion network's pretrained initialization (random vs. SD1.5) would help attribute the gains to the architecture vs. the pretrained prior.

## Removed Points
These points are flagged to be removed — treat them with caution:
- **Criticism that the reference motion network training is "underspecified" or lacks a dedicated loss function.** The paper explicitly states "Through end-to-end training" (Section 3.4) and uses the standard diffusion loss (Eq. 1) as the training objective. The intermediate motion maps emerge as learned representations, not supervised outputs — this is a standard design pattern in representation learning, not a flaw. Removed as a misunderstanding of end-to-end training.
- **Criticism that SfM methods might fail on generated videos, biasing comparison.** The paper uses three different SfM methods, all showing the same trend. Any SfM failure mode would apply equally across all methods; if anything, better FID/FVD could cause SfM to work *better* on MotionFlow's outputs, which the critic acknowledges. This is a generic concern without evidence of systematic bias. Removed as speculative and not specific to this paper.
- **Criticism that the network was "never trained to produce interpretable motion maps."** Post-hoc visualization of learned representations via VAE decoding is a standard analysis technique (e.g., in GAN inversion, feature visualization). It does not require the network to have been supervised on those representations. Removed as misunderstanding of standard practice.
- **Request for explicit ablation of conditioning modality (replace image with text).** While this would strengthen the paper, the absence of this specific experiment is not a flaw — the paper makes a design choice (image-conditioning) and provides the best-possible comparison by claiming to use image prompts for baselines too. Moved to Nice-to-Haves.
- **Demand for hyperparameter table.** The training details given (Adam, 8× GPUs, batch size 1, two-stage learning rates 1e-4 / 1e-5, training duration) are standard and sufficient for a conference submission. Moved to Nice-to-Haves.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a useful tension: the paper's main architectural claim (pixel-level motion integration) is well-supported by the ablation study, yet the central quantitative comparison is weakened by a description gap (how the text-conditioned baselines were adapted for image prompts). Resolving this tension — either by better documenting the adaptation or by running a text-conditioned ablation — would substantially strengthen the paper.

## Suggestions

1. **Clarify the confusion around "motion extractor" vs. reference motion network vs. semantic encoder.** Either align the terminology across Sections 3.3, 3.4, and 3.6, or explicitly state that the "motion extractor" trained in the first stage is a specific sub-component and name it.
2. **Document how CameraCtrl and MotionCtrl were adapted to accept image prompts.** If the baselines were implemented by replacing CLIP text features with CLIP image features (analogous to how DynamicCrafter handles images), state this explicitly and cite any modifications made to the original architectures. If the baselines were not image-conditioned and the comparison is therefore asymmetric, this should be disclosed and discussed.
3. **Replace or remove the toy experiment.** A proper evaluation of RMMs would use many videos, larger train/test splits, and baseline comparisons (e.g., raw VAE features, random features). Alternatively, simply remove the "more abundant information than OFs" claim.
4. **Report inference time (seconds per video) and parameter count.** This is standard for systems papers and helps readers assess the practical trade-off.
5. **Add a brief failure analysis.** Even one paragraph discussing cases where the method struggles (e.g., large viewpoint jumps, scenes with extreme depth variation, fast object motion) would strengthen the paper's honesty and help future work.

## Score and Decision

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>