Now I have all the information needed. Let me construct the final meta-review.

## Summary

MotionFlow proposes a camera-trajectory-guided video generation framework. The core idea is to use a pretrained image stable diffusion model (the "reference motion network") to convert camera trajectories (encoded as Plücker embeddings) into pixel-level reference motion maps, which are then injected into an AnimateDiff-based video generation network via cross-attention. A separate ViT-based semantic encoder (initialized from DINO) extracts foreground object features used for object attention, improving visual quality of salient objects. On RealEstate10K, the method achieves state-of-the-art rotation/translation errors and visual quality metrics against CameraCtrl and MotionCtrl.

---

## Strengths

1. **State-of-the-art quantitative results on camera trajectory control.** On RealEstate10K, MotionFlow achieves the lowest rotation and translation errors across three different SfM methods (Dust3R, VggSfM, ParticleSfM) for both basic and difficult trajectory settings (Table 1). It also achieves the best FID (15.50), SSIM (0.746), PSNR (20.81), LPIPS (0.201), and FVD (83.90) against CameraCtrl and MotionCtrl (Table 2). These results are produced under a fair comparison setup where all methods are trained on the same data with the same baseline (SD1.5).

2. **Unified pixel-level motion representation validated by ablation.** The ablation study (Table 4) confirms that removing the reference motion network causes significant drops across all metrics, and that using pretrained SD1.5 weights for it is beneficial. This directly supports the central claim that learning pixel-level motion priors via a separate diffusion network is an effective strategy for camera-guided generation.

3. **Semantic extractor with object attention improves generation quality.** The ablation also shows that adding the semantic extractor improves all metrics (e.g., FVD drops from 91.2 to 83.90, FID from 18.53 to 15.50), confirming that object-aware conditioning contributes to video quality beyond what camera-only guidance provides.

4. **Thorough geometric evaluation with multiple SfM methods and trajectory difficulties.** Using three SfM pipelines (ParticleSfM, Dust3R, VggSfM) and testing on both basic and difficult trajectories strengthens the evidence for trajectory alignment by reducing dependence on any single estimation method.

5. **Practical downstream application demonstrated.** Section 4.4 shows that videos generated with a panoramic trajectory can be used for explicit 3D scene reconstruction, illustrating real-world utility beyond the video generation task itself.

---

## Weaknesses

### Fatal

None.

### Major

1. **Missing camera-control baselines in the generalizability evaluation (Table 3).** The paper evaluates generalizability on DL3DV-10k (outdoor scenes) by comparing with DynamicCrafter, SVD, and AnimateDiff — none of which are camera-controlled methods. Since the paper's core claim is about camera trajectory control, the generalizability comparison should include CameraCtrl and MotionCtrl (the primary competitors, which are also trained on indoor RealEstate10K). Without this comparison, Table 3 only shows that MotionFlow generalizes better than general I2V models on visual quality, not that its camera-control capability generalizes better. This undermines the quantitative evidence for the paper's generalizability claim.

2. **Ambiguous term and training signal in stage one (Section 3.6).** The phrase "motion extractor" appears exactly once in the entire paper ("we train the Trajectory Encoder and motion extractor") and is never defined, explained, or referenced elsewhere. It is unclear whether this is a separate module, a different name for the reference motion network, or part of the trajectory encoder. Moreover, if the reference motion network is kept fixed in stage one, it is not explained what training signal is used to supervise the Trajectory Encoder — the standard diffusion loss (Eq. 2) requires the video generation network to be active, yet that network is also frozen. This is a genuine gap in the method description that makes the training procedure ambiguous.

### Minor

1. **Overclaimed "object motion integration" framing.** The abstract and introduction state that the method "integrates both camera and object motions by converting them into the motion of corresponding pixels." In reality, the method does not take any object motion trajectories as input; the semantic encoder identifies salient objects from the reference image and improves their generated appearance, but there is no explicit conditioning on object dynamics. The conclusion (Section 5) acknowledges this — "it lacks explicit guidance for object motion control" — which partially mitigates the issue. However, the abstract's phrasing is still likely to mislead readers about what the method delivers. This should be rephrased to accurately reflect that the model handles both camera-induced and object-induced motion implicitly through a unified pixel-level representation, not through explicit object motion conditioning.

2. **The toy experiment on reference motion maps and optical flow is unconvincing (Section 4.3).** The experiment uses 12 training pairs from a single generated video and tests on 2 frames from the same video. Training a small network on such a tiny, non-independent sample is trivial overfitting and does not provide evidence that RMMs encode optical flow in a generalizable way. The paper then argues that RMMs "have more abundant information than OFs" — a claim this experiment cannot support. Either the experiment should be expanded to multiple videos with held-out scenes, or the argument should be tempered.

3. **Incomplete reporting of trajectory error computation (Section 4.1).** The evaluation pipeline estimates camera trajectories from both generated and real videos using the same SfM method and compares them. However, the paper does not specify the alignment procedure (e.g., Procrustes alignment for scale/rotation) between the estimated trajectories and the ground truth, nor how frame correspondence is established. While this protocol follows the general approach of CameraCtrl and MotionCtrl, the missing detail still hampers reproducibility. The paper should describe: (a) the alignment method used, (b) which frame serves as the reference, and (c) whether the error is averaged over views or frames.

4. **Missing standard training details.** The paper reports GPU count (8× A800), batch size (1 per GPU), optimizer (Adam), learning rates (1e-4 and 1e-5), and duration ("one day" / "three days"), but omits: input video resolution, number of training frames, exact number of training steps, and learning rate schedule. These are standard reporting details needed for reproducibility.

5. **No ablation isolating the semantic encoder's effect on foreground vs. background.** Table 4 shows overall metric improvements from the semantic extractor, but since the object attention mechanism specifically targets foreground objects, an ablation measuring foreground object quality (e.g., segmentation-aware FID or LPIPS on object regions) would be more informative. As presented, it is unclear whether the improvement comes from better foreground rendering or from general feature enrichment.

6. **No analysis of failure cases or limitations.** The paper contains a single sentence about lacking object motion control (Section 5) but otherwise presents no discussion of trajectory complexity sensitivity, occlusion handling, texture-less regions, or scenarios where the method fails. For a camera-control method, understanding the failure modes is important for assessing practical applicability.

### Trivial

- The paper states "CameraCtrl and MotionCtrl are three baseline methods" (line 136) — a minor wording issue.
- The phrase "motion extractor" in Section 3.6 is undefined; this should be clarified or replaced.

---

## Nice-to-Haves

- Evaluation of temporal consistency beyond FVD (e.g., warping error, temporal flickering) would strengthen the video quality assessment.
- An analysis of what the semantic encoder actually learns (e.g., attention map visualizations across different scenes) would improve interpretability.
- Reporting results on DL3DV-10k separately for each SfM estimation method (as done for RealEstate10K) would strengthen the generalizability evaluation.

---

## Removed Points

These points were flagged by reviewers but are removed or downgraded after verification:

- **"No description of tensor shapes for reference motion maps" (Critic 2a):** REMOVED — the paper explicitly gives the shape p_i ∈ ℝ^{f×c×h×w} in Section 3.5 (line 120). The critic's claim that tensor shapes are absent is factually wrong.
- **"No information on whether the semantic encoder is fine-tuned" (Critic 2c):** REMOVED — Section 3.6 states "subsequently, we train all parts for three days," which includes the semantic encoder. The critic overlooked this.
- **"The paper does not state whether the trajectory encoder and reference motion network are trained jointly in stage two" (from Missing Parts):** REMOVED — Section 3.6 explicitly says "train all parts" in stage two. This is stated.
- **"CLIP text encoder as LM" / "LLM generating images" style impossible asks:** Not present in this review.
- **"The camera trajectory alignment evaluation is uninterpretable" / "ranking inconsistent across SfM methods":** DOWNGRADED to minor — the evaluation follows standard protocol used in CameraCtrl and MotionCtrl (as the paper states). The critic's questions about alignment details are reasonable, but the evaluation is not "uninterpretable" and the paper does note which SfM methods are used.
- **Strength Finder's claim about the toy experiment being a strength (#5):** DOWNGRADED — the experiment is too small (12 training pairs, single video) to support the claims made, so it cannot count as a genuine strength.

---

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any observation about the method's implications that the authors themselves do not already articulate.

---

## Suggestions

1. **Re-evaluate on DL3DV-10k including CameraCtrl and MotionCtrl as baselines.** This is the single most important fix — without it, the generalizability claim is incomplete. The authors can either run those models on the outdoor dataset or provide a principled explanation (e.g., architectural incompatibility) for why they cannot.

2. **Clarify the "motion extractor" term and the stage-one training signal.** Define what the motion extractor is, how it differs from the reference motion network, and what loss supervises stage-one training when the video generation network is frozen.

3. **Tone down or clarify the "object motion integration" narrative in the abstract.** Replace phrasing that implies explicit object motion control with language about implicit pixel-level motion handling and object-aware semantic conditioning.

4. **Expand or remove the toy experiment.** Either validate RMM-to-OF mapping on multiple videos with held-out scenes, or drop the claim that RMMs encode optical flow in a generalizable way.

5. **Add trajectory error alignment details.** Describe the Procrustes or similarity alignment used between estimated and ground-truth trajectories, the reference frame, and the error aggregation method.

6. **Report input resolution, number of frames per training video, and total training steps.** These are minimal reproducibility requirements.

---

## Score and Decision

The paper addresses an important problem (camera trajectory control in video generation) with a technically sound approach that achieves state-of-the-art results on the primary benchmark (RealEstate10K). The core contributions — the reference motion network design, the unified pixel-level motion representation, and the semantic encoder — are validated by ablations and produce clear gains. However, the paper is weakened by: (1) a missing baseline comparison in the generalizability evaluation that undermines a key claim, (2) an undefined "motion extractor" that creates ambiguity in the training procedure, and (3) several presentation and evaluation detail gaps that reduce reproducibility. These issues are addressable with revisions but are not so severe as to invalidate the core contribution. The paper would benefit from a minor revision cycle to address the major weakness and clarify the method description.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>