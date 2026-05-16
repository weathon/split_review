Now I have thoroughly verified all claims against the paper. Let me produce the consolidated review.

## Summary

**MotionFlow** proposes a video generation framework that achieves camera-trajectory control by learning implicit pixel-level motion flows. It uses a secondary stable-diffusion network (reference motion network) to jointly encode camera trajectories and reference images into motion maps, which are then injected into an AnimateDiff-based video generation network via reference attention. A ViT-based semantic extractor further provides object-aware priors. The paper reports improved camera-trajectory alignment and visual quality over CameraCtrl and MotionCtrl on RealEstate10K and DL3DV-10k.

## Strengths

- **Consistent camera-trajectory alignment across multiple pose estimators and trajectory difficulties (Table 1).** MotionFlow achieves lower rotation and translation errors than CameraCtrl and MotionCtrl for both basic and difficult trajectories using ParticleSfM, Dust3R, and VggSfM. For example, rotation error with ParticleSfM on basic trajectories: MotionFlow 0.096 vs. CameraCtrl 0.115 vs. MotionCtrl 0.142. The consistency across three different SfM methods strengthens confidence in the result.
- **Higher visual quality on both in-domain and out-of-domain scenes (Tables 2 and 3).** On RealEstate10K (indoor), MotionFlow outperforms baselines on FID, SSIM, PSNR, LPIPS, and FVD. On the held-out outdoor DL3DV-10k dataset, it maintains superior quality (FID 13.78 vs. CameraCtrl 18.15 vs. AnimateDiff 20.31), demonstrating generalization beyond the training distribution.
- **Ablation study validates both major components (Table 4).** Removing the reference motion network or the semantic extractor leads to clear degradation across all metrics (e.g., FVD 527 → 590 without semantic extractor, 527 → 642 without reference motion network), confirming the contribution of both modules.
- **Interpretability experiment linking reference motion maps to optical flow (Figure 6).** The toy experiment showing that a lightweight network trained on only 12 pairs can translate RMMs to optical flow provides concrete evidence that the learned maps encode meaningful pixel-level motion, not just unstructured features.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims are supported by evidence and no verified weakness invalidates them.

### Minor

- **The adaptation of baseline methods (CameraCtrl, MotionCtrl) to accept image prompts is underspecified.** The paper states (line 136) that all methods were "tested them using the same camera trajectories and **image prompts**," but does not describe *how* the baselines — originally designed for text conditioning — were modified to accept image inputs (e.g., whether CLIP text features were replaced with CLIP image features, or whether some other mechanism was used). While this does *not* constitute a "structural flaw" (the paper explicitly claims equal conditioning), the missing detail makes it hard for readers to assess whether the comparison fully isolates the motion-flow architecture from the choice of conditioning modality. This is a clarity gap, not an invalidation of results.

- **The reference attention mechanism is ambiguously described and likely insufficient for reproduction.** Section 3.5 describes concatenating feature maps $p_i$ and $m_i$ along the width dimension, performing cross-attention, then extracting the first half. It is not specified what serves as queries, keys, and values in this cross-attention, nor how the spatial concatenation interacts with attention computation. The phrase "perform cross-attention" without specifying the Q/K/V sources leaves the mechanism under-defined.

- **The object attention mechanism is similarly vague.** The paper states "compute an attention map as a semantic mask between the semantic feature map and the output of reference attention" without specifying the attention operation (queries, keys, values, softmax). The subsequent description of "pointwise multiplied with the semantic mask" suggests the attention map is used as a gating signal, but how the attention map itself is computed is not clear.

- **SfM-based evaluation on generated videos lacks validation.** The paper uses ParticleSfM, Dust3R, and VggSfM to estimate camera poses from generated videos. While using multiple SfM methods mitigates concerns, the paper provides no validation that these learned pose estimators produce reliable trajectories on synthetic video outputs (which may contain artifacts like temporal flickering or object deformation). A controlled study on synthetic data with known ground-truth poses would strengthen this evaluation.

- **"Motion extractor" appears as an undefined term.** The training strategy section (3.6) introduces "motion extractor" for the first time without clarifying whether this refers to the reference motion network or a different component. Earlier sections consistently use "reference motion network." This naming inconsistency harms readability.

- **Toy experiment on RMM-to-optical-flow is too limited to support general claims.** The experiment uses 12 training pairs from a single video and tests on 2 pairs. While the paper is appropriately modest about this analysis ("we hypothesize," "toy experiment"), the sample size is too small for the results to be more than suggestive.

- **No quantitative evaluation of joint camera + object motion.** The paper motivates joint modeling of camera and object motions, but quantitative evaluation is on RealEstate10K (mostly static indoor) and DL3DV-10k (mostly static outdoor). No quantitative results demonstrate performance on dynamic scenes with simultaneous camera and object motion. The paper acknowledges this as a limitation, but it narrows the scope of the claimed contribution.

- **No confidence intervals or multiple-run statistics.** Reported metrics are single-run, which is common in this field but worth noting given the "large margin" claim.

### Trivial

- Line 120: "objection attention" appears to be a typo for "object attention."
- Line 172: Table 3 caption has "IC" abbreviation without expansion in the caption body (though it appears to mean "image condition," which is clear from context).

## Nice-to-Haves

- A clearer specification of how CameraCtrl and MotionCtrl were adapted to accept image prompts (e.g., replacing CLIP text encoder with CLIP image encoder), which would put the comparison on fully transparent footing.
- A controlled validation experiment on synthetic data (e.g., Kubric or rendered scenes) where ground-truth camera poses are known, to establish the accuracy of SfM-based evaluation on generated videos.
- Quantitative results on a dynamic-object dataset (e.g., with moving foregrounds) to support the claim of joint camera+object motion handling.
- A more detailed training recipe: number of optimization steps, learning rate schedule details (warmup, decay), and how overfitting was monitored during the two-stage training.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Unfair baseline comparisons as a "structural flaw."** The paper explicitly states (line 136) that all methods were tested using "the same camera trajectories and **image prompts**." The harsh critic assumes baselines were "still using text prompts," contrary to the paper's claim. The real issue is insufficient detail about *how* baselines were adapted, which is a clarity concern, not a structural flaw. Moved to Minor (above) with appropriate framing.

- **ControlNet critique.** The critic claims Section 3.4's argument about ControlNet is "hand-wavy" and the real challenge is data availability. The paper makes a specific architectural argument about domain mismatch between camera space and image space; this is a substantive design choice, not a weakness.

- **Missing baselines (Direct-a-video, CamCo).** The paper quantitatively compares against the two most relevant camera-control methods (CameraCtrl, MotionCtrl). Comparing against every method in related work is scope creep.

- **"three baseline methods" grammar issue.** Per hard rules, removed as a formatting/style nitpick.

- **Section 3.4 framing about data availability.** The critic says the paper "later admits this" about data availability, but the paper's framing is not misleading — it simply identifies one of the challenges.

## Novel Insights

The reviews surface a tension that the paper itself does not fully grapple with: the core architectural claim is that jointly encoding camera trajectories and images through a secondary diffusion network yields better motion understanding than separate modules, yet the quantitative evidence for this advantage is partially confounded by the underspecified adaptation of baselines to image conditioning. The strongest evidence for the method's value is actually the trajectory alignment results (Table 1), where the advantage holds across three different SfM estimators — this is harder to attribute to conditioning asymmetry and more directly supports the motion-flow learning claim. The toy optical-flow experiment, while limited, is a genuinely clever sanity check that most papers in this area do not provide, and it gives concrete interpretability evidence that goes beyond typical qualitative visualizations.

None beyond the paper's own contributions.

## Suggestions

- **Clarify baseline adaptation.** Add a sentence or footnote describing how CameraCtrl and MotionCtrl were adapted to accept image prompts (e.g., "We replaced the CLIP text encoder with a CLIP image encoder for all baselines, following Chen et al. (2023)").
- **Specify the attention operations.** Provide a clear equation or figure specifying what Q, K, V are in both the reference attention and object attention mechanisms. The current concatenation-then-cross-attention-then-slice description is ambiguous without specifying the attention inputs.
- **Validate SfM on synthetic data.** Add a controlled experiment on a synthetic dataset (e.g., Kubric) with known ground-truth camera poses to confirm that the SfM-based evaluation is reliable on generated videos.
- **Replace "motion extractor" with "reference motion network"** throughout Section 3.6 for consistency, or define the term at first use.
- **Add a dynamic-scene benchmark** (e.g., on a dataset with moving objects and known camera poses) to quantitatively support the claim of joint camera-object motion handling.

## Score and Decision

The paper introduces a well-motivated framework with a clear architectural contribution (learning pixel-level motion flows via a secondary diffusion network) and provides substantial quantitative evidence across multiple metrics and datasets. The main concerns are about clarity of method description and evaluation details rather than structural flaws. The weaknesses identified are addressable in revision.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>