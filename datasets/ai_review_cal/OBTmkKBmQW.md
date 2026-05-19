- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 5, 3, 5
Now I have a thorough understanding of the paper. Let me produce the consolidated review.

---

## Summary

MotionFlow proposes a camera-trajectory-controlled video generation framework. The key idea is a **reference motion network** — a separate SD1.5 UNet — that jointly encodes the input camera trajectory (via Plücker embeddings) and the reference image, producing pixel-level "reference motion maps" that are injected into an AnimateDiff-based video generation network through cross-attention. A lightweight semantic encoder (ViT/DINO) further provides object-aware features. The method is evaluated on RealEstate10K against CameraCtrl and MotionCtrl (Tables 1, 2) and on DL3DV-10k against general I2V baselines (Table 3).

## Strengths

1. **Joint pixel-level encoding of camera and object motion.** Section 3.4 introduces a reference motion network that fuses camera trajectory features and CLIP image features in a single cross-attention formulation (Eq. 4). This avoids the separate-module confusion of methods like MotionCtrl. The ablation (Table 4, first row) confirms that removing this module causes significant drops across all metrics, validating its role.

2. **Semantic encoder with object attention improves quality.** Section 3.3 describes a ViT/DINO-based semantic encoder that extracts foreground object features, injected via pixel-wise addition and object attention. The ablation (Table 4, second row) shows consistent improvements in FID, SSIM, PSNR, LPIPS, and FVD when this module is included.

3. **Consistent geometric superiority over proper baselines.** Table 1 reports lower rotation and translation errors than CameraCtrl and MotionCtrl across three different SfM estimators (Dust3R, VggSfM, ParticleSfM) on both basic and difficult trajectories. This directly supports the paper's core claim of precise camera trajectory adherence. The improvements are consistent even if modest in some cases.

4. **Improved visual quality over camera-control methods.** Table 2 shows MotionFlow outperforming CameraCtrl and MotionCtrl on all five metrics (FID, SSIM, PSNR, LPIPS, FVD) on RealEstate10K, with noticeable gaps in FID (17.73 vs. 27.54) and FVD (154.41 vs. 224.12).

## Weaknesses

### Fatal
None. The paper's core claims are supported by valid comparisons (Tables 1, 2 against CameraCtrl and MotionCtrl) and the ablation study (Table 4). The issues below are substantive but fixable.

### Major

1. **The Table 3 "generalizability" comparison is fundamentally unfair and should be removed or reframed.** The paper compares MotionFlow against I2VGen-XL, DynamicCrafter, and AnimateDiff on DL3DV-10k — none of which take camera trajectory as input. These baselines solve a different task (text/image-to-video without camera control). MotionFlow receives the exact camera trajectory plus reference image as conditioning, giving it an information advantage that trivially explains the better scores. Presenting this as evidence of "superior generalizability" is misleading. The paper should either (a) compare only to camera-control methods on this dataset, or (b) acknowledge this limitation and frame the outdoor experiments as a qualitative demonstration of zero-shot generalization, not a quantitative comparison. **This does not invalidate the paper's core claims** (which rest on Tables 1 and 2), but it does misrepresent the evidence and should be corrected.

2. **No variance estimates reported for any quantitative metric.** All tables report single-point numbers without confidence intervals, standard deviations, or indication of number of runs. Diffusion models are inherently stochastic, and several margins in Table 1 are modest (e.g., rotation error 0.064 vs. 0.071 on basic/Dust3R). Without variance information, the reader cannot assess whether these differences are statistically significant. This weakens the overall strength of the experimental evidence. The authors should report results over at least 3 seeds with mean and standard deviation.

### Minor

1. **Terminology inconsistency: "motion extractor" is not clearly defined.** Section 3.6 states: "In the first stage, we train the Trajectory Encoder and motion extractor." Section 3.3 says the semantic encoder "is trained in the first stage." The term "motion extractor" appears nowhere in the architecture sections (3.2–3.4), and the connection to the semantic encoder is never made explicit. It is clear from context that they refer to the same component, but the inconsistent naming creates confusion. The authors should use a single consistent term throughout.

2. **Reference attention mechanism is under-specified.** Section 3.5 describes concatenating feature maps along the width dimension and then performing cross-attention, but does not specify which tensor serves as query, key, and value in this cross-attention step. The operation is non-standard (concatenating along a spatial dimension before attention), and omitting the formulation makes the method harder to reproduce or build upon.

3. **The toy experiment linking reference motion maps to optical flow is too thin.** Section 4.3 uses 12 training pairs and 2 test pairs from a single video to train a shallow network. The paper itself calls this a "toy experiment," and the result (that RMMs contain correlation with optical flow) is not surprising. This experiment provides intuitive support but does not constitute meaningful evidence. It should either be strengthened with a proper multi-video analysis or explicitly caveated as purely illustrative.

### Trivial

- "Difficult trajectory (sample every max frame we can sample)" (Section 4.2) is informal. The sampling strategy should be precisely defined.

## Nice-to-Haves

- The reference attention operation (concatenate along width → cross-attention → extract first half) would benefit from a brief rationale. Why is this preferable to standard cross-attention between the two feature maps?
- The object attention computation ("compute an attention map as a semantic mask between the semantic feature map and the output of reference attention") should specify whether this is dot-product, element-wise, or another operation.
- A more detailed ablation varying the reference motion network architecture (e.g., smaller network, or explicit optical flow input) would strengthen the paper's central claims.

## Removed Points

- **"Motion extractor is completely missing/unreproducible" (Critic claim #2, strong version):** The term "motion extractor" is indeed used inconsistently, but the paper does define the semantic encoder (Section 3.3, ViT/DINO) and states it is trained in stage 1. The critic's stronger version — that a critical component is entirely missing — is inaccurate. The issue is terminology inconsistency, not a missing component.

- **"Reference motion network containing the trajectory encoder makes the training contradictory" (Critic's Section 3.6 note):** The paper's Figure 2 and Section 3.4 clearly show the Trajectory Encoder as a separate module that feeds features *into* the reference motion network. Training the Trajectory Encoder while keeping the SD1.5 UNet (the reference motion network) fixed is internally consistent. The critic's concern rests on a misreading.

- **"Missing related works":** Removed per instructions — I cannot verify whether specific works are missing.

- **Missing appendix/proofs format criticisms:** Removed per instructions (parser artifact).

- **Strength 5 from Strength Finder ("Strong generalization to unseen outdoor scenes"):** This strength depends on the problematic Table 3 comparison and conflicts with a verified weakness. Removed.

- **Several section-by-section nitpicks (phrasing/formulation suggestions):** These are speculative or ask the paper to address questions outside its stated scope. Removed as noise.

## Novel Insights

The Strength Finder and Harsh Critic both converge on an interesting tension: the paper's strongest contribution — the reference motion network as a joint encoder of camera and image features — is simultaneously its least precisely described component. The architecture description (Section 3.4) gives the cross-attention formulation for the reference motion network, but the critical details of how its outputs ("reference motion maps") are structurally injected into the generation network via reference attention (Section 3.5) remain underspecified. This gap between claimed innovation and specification clarity is the paper's central weakness, and fixing it would significantly strengthen the work more than any additional experiment.

## Suggestions

1. **Remove or fundamentally reframe Table 3.** If the goal is to show zero-shot generalization to outdoor scenes, present it as a qualitative demonstration with appropriate caveats. Do not claim quantitative superiority over methods solving a different task.

2. **Unify terminology:** Replace "motion extractor" with "semantic encoder" (or vice versa) throughout the paper. Clearly state in Section 3.6 that the semantic encoder from Section 3.3 is the component trained in stage 1.

3. **Add variance estimates** (mean ± std over ≥3 seeds) to all quantitative tables.

4. **Fully specify the reference attention cross-attention operation** in Section 3.5 — state the Q, K, V formulation explicitly.

5. **Either strengthen or remove the toy experiment.** A proper analysis across multiple diverse videos with quantitative correlation to ground-truth optical flow would support the "RMMs encode pixel motion" claim. If not possible, explicitly downgrade the claim to a qualitative observation.
