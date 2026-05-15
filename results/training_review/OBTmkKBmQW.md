Now I have all the facts. Let me produce the final consolidated review.

---

## Summary

MotionFlow proposes a video generation framework for precise camera trajectory control by learning implicit pixel-level motion flows. The key idea is to use a reference motion network (initialized from Stable Diffusion) that jointly encodes camera trajectories and reference image features into pixel-level "reference motion maps," which are then injected into an AnimateDiff-based video generation network via reference attention. A semantic encoder (DINO-based) provides object awareness through object attention. The method is evaluated on RealEstate10K and DL3DV-10k, comparing against CameraCtrl, MotionCtrl, and other baselines.

## Strengths

- **Novel integration of camera and object motion via pixel-level motion maps reduces motion confusion.** Unlike prior work that models camera and object motions with separate modules, MotionFlow converts both into pixel motion and learns them jointly through the reference motion network. The quantitative trajectory alignment results (Table 1) consistently show lower rotation and translation errors across multiple SfM estimators (Dust3R, VggSfM, ParticleSfM) and across both basic and difficult trajectories, supporting the claim that this joint learning approach is effective.

- **Semantic encoder for object awareness improves foreground-background decoupling.** The DINO-initialized semantic encoder extracts salient object features and injects them via object attention and additive fusion. The ablation study (Table 4) verifies that removing the semantic extractor degrades both visual quality (FID, SSIM) and camera alignment metrics, demonstrating a clear contribution to both visual fidelity and trajectory consistency.

- **Strong generalizability to novel outdoor scenes.** Trained solely on indoor RealEstate10K, MotionFlow achieves substantially better FID and FVD on the outdoor DL3DV-10k dataset (Table 3) compared to DynamicCrafter, I2VGen-XL, AnimateDiff, and VideoComposer — all of which are image-conditioned I2V models. This large margin validates the method's robustness to domain shift, which the paper attributes to the progressive fusion of camera trajectory with image features in the reference motion network.

- **Practical downstream application demonstrated.** Section 4.4 and Figure 7 show that a single reference image with a panoramic trajectory can generate a video suitable for 3D scene reconstruction, extending the method's value beyond video generation alone.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The paper does not explain how baseline methods (CameraCtrl, MotionCtrl) were adapted to use image prompts.** The paper states (line 136): "we trained all the methods on the RealEstate10K dataset and tested them using the same camera trajectories and image prompts." However, CameraCtrl and MotionCtrl were originally designed for text-prompt conditioning. The paper does not describe how these architectures were modified to accept image inputs (e.g., replacing CLIP text features with CLIP image features, or some other adaptation). Without this detail, a reader cannot assess whether the baselines were given a fair adaptation or whether MotionFlow's advantage may partly stem from architectural choices in how image conditioning is handled rather than the proposed motion flow mechanism. The paper should clarify this setup.

- **Missing comparison against image-conditioned camera control baselines (CamCo, VD3D).** These methods are discussed in related work (line 41) and share the same image+trajectory conditioning setting, but no quantitative comparison is provided. While CameraCtrl and MotionCtrl are the most directly related baselines, including CamCo or VD3D would strengthen the evaluation.

- **No camera-trajectory-only ablation.** The ablation study (Table 4) removes the reference motion network but still feeds trajectory encoder outputs into reference attention. A baseline that removes all camera trajectory input (i.e., a plain image-to-video generation without camera guidance) would help isolate the contribution of the camera control itself, answering the question: how much of the visual quality gain is from image conditioning vs. camera control? This is not a fatal omission — the paper's primary claim is about *how* to do camera control, not *whether* it helps — but it would strengthen the analysis.

- **No error bars, variance, or SfM success rates reported.** Table 1 reports rotation and translation errors without standard deviations or confidence intervals. The paper also does not report what fraction of generated videos yielded valid SfM estimates (though it acknowledges COLMAP frequently fails on RealEstate10K). While single-run evaluation without variance is common in this benchmark setting, reporting these statistics would improve the rigor of the evaluation.

- **Undefined "motion extractor" in training description.** Section 3.6 states "we train the Trajectory Encoder and motion extractor," but the term "motion extractor" is not defined anywhere in the visible sections of the paper. It is unclear which component this refers to.

### Trivial

- **"CameraCtrl and MotionCtrl are three baseline methods"** (line 136) — two methods are referred to as "three." This appears to be either a minor writing oversight or a parser artifact from an earlier version.

## Nice-to-Haves

- Report SfM success rates and per-metric confidence intervals to strengthen the trajectory alignment claims.
- Provide an ablation that removes all camera trajectory input to establish the value of camera guidance over image-only I2V generation.
- Show trajectory overlay visualizations (ground-truth vs. estimated camera paths) for qualitative insight into the error numbers.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Unfair comparison: baselines use text prompts while MotionFlow uses image prompts"** — REMOVED because it is factually contradicted by the paper. Line 136 explicitly states: "we trained all the methods on the RealEstate10K dataset and tested them using the same camera trajectories and **image prompts**." All methods received image conditioning. The reviewer's central structural criticism is based on a misreading.

- **"SfM confounded because MotionFlow frames look more like GT due to image conditioning"** — REMOVED as a consequence of the above. Since all methods (including baselines) were tested with image prompts, any SfM advantage from better visual quality applies symmetrically and is a legitimate reflection of method quality, not a confound.

- **"Toy experiment insufficient"** — REMOVED. The toy experiment (Section 4.3) is explicitly presented as a lightweight verification that reference motion maps correlate with optical flow. It trains a small network on 12 pairs in ~40 seconds. The reviewer's criticism that this is "insufficient to establish any reliable correspondence" ignores the stated purpose: it is a probe, not a rigorous benchmark. The paper appropriately acknowledges the experiment's limited scope.

- **"MotionCtrl's 'relatively simple encoding' is unsupported"** — REMOVED. This is a qualitative observation in the introduction (line 12), not a quantitative claim. The paper later provides architectural motivation for this (Section 3.2 explains why flattened 12D vectors are limited compared to Plücker embeddings), which sufficiently supports the qualitative statement.

- **"Semantic encoder training objective not specified"** — REMOVED as a standalone criticism. The semantic encoder is initialized from DINO and trained end-to-end in the first stage alongside other components using the standard diffusion loss (Eq. 1), which applies to all trainable modules. This is standard practice and does not require a separate objective specification.

- **Missing appendix / missing proofs in appendix** — REMOVED. The parser strips appendix sections from all papers.

- **Pure formatting/style nitpicks** — REMOVED per instructions.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a fundamentally new perspective on the work that the paper itself does not already articulate.

## Suggestions

- Clarify the adaptation of CameraCtrl and MotionCtrl for image prompts: describe how CLIP text conditioning was replaced with image conditioning, and whether the baselines' architectures required any modifications. This is the single most important addition for reproducibility and fairness.
- Add a plain I2V ablation (no camera trajectory input) to Table 4 to establish the value of camera guidance itself.
- Include variance/std over multiple seeds or runs for Table 1 metrics, and report the SfM success rate for each method.
- Add quantitative comparison against CamCo or VD3D on the RealEstate10K benchmark, or explain why these are excluded.
- Define "motion extractor" in Section 3.6 or remove the ambiguous term.

## Score and Decision

The paper presents a technically sound and well-motivated approach for camera trajectory control in video generation. The core methodological contribution — joint pixel-level motion learning via a diffusion-based reference motion network — is novel and supported by consistent quantitative improvements across multiple metrics and datasets. The primary criticism raised by the reviewer (unfair text-vs-image conditioning) is factually incorrect; the paper explicitly states all methods were tested with image prompts. The remaining issues are minor: missing clarification of baseline adaptation, no variance reported, absent comparison with CamCo/VD3D, and a few presentation ambiguities. None of these threaten the paper's core claims. The experiments are sound and the results appear credible. Revisions should focus on transparency about baseline adaptation and additional rigor in error reporting, neither of which undermines the existing conclusions.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>