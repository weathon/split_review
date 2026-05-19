- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6
I have thoroughly read and analyzed the paper. Let me now produce the consolidated review.

---

## Summary

This paper presents DICE, the first end-to-end learning-based method for recovering hand-face interactions with deformations from a single monocular image. It introduces a two-branch Transformer architecture (MeshNet and InteractionNet) that disentangles global mesh regression from local deformation/contact estimation, along with a neural inverse-kinematics network (IKNet) that converts vertex predictions into animatable parametric model parameters. A weakly-supervised training scheme using only 500 in-the-wild images with off-the-shelf depth (Marigold), 2D keypoint detectors, and adversarial pose priors improves generalization beyond the studio-collected Decaf dataset. DICE achieves a 14% lower per-vertex error (PVE 8.32mm vs. 9.65mm) and a 200× speedup over the optimization-based state-of-the-art (Decaf), while running at 20 fps.

## Strengths

1. **First end-to-end method for this task with dramatically faster inference and higher reconstruction accuracy.** Table 1 shows DICE achieves PVE of 8.32 mm vs. Decaf's 9.65 mm (14% reduction) while running at 0.088 s per image compared to Decaf's 19.59 s — a 200× speedup over the optimization-based prior art. This directly demonstrates the practical advantage of a regression-based architecture for interactive applications.

2. **Two-branch architecture (MeshNet / InteractionNet) is well-motivated and empirically validated.** The ablation (Table 3) shows the two-branch design increases the Touchness ratio from 57.4 to 79.9 (a 39% improvement) and reduces PVE from 9.29 mm to 8.32 mm, confirming that separating global mesh regression from local contact/deformation estimation is a beneficial design choice.

3. **Weakly-supervised depth supervision from a diffusion-based monocular depth estimator substantially improves reconstruction accuracy.** The ablation row "w.o. L_depth" (Table 3) shows PVE increases from 8.32 mm to 15.6 mm (nearly doubled) and F-Score drops from 72.7 to 64.2. Since depth supervision is applied only to the 500 in-the-wild images, this demonstrates the pipeline effectively leverages monocular depth priors to avoid overfitting to the controlled Decaf dataset.

4. **Adversarial priors trained on separate hand-only and face-only datasets improve both accuracy and pose plausibility.** The ablation "w.o. L_adv" shows PVE rises from 8.32 mm to 11.1 mm and Touchness drops from 79.9 to 60.7. By using RenderMe-360, FreiHand, and Decaf data for the discriminators, the method injects diverse pose distributions beyond the Decaf training set.

5. **Contact estimation surpasses the only prior work (Decaf) on F-Score.** Table 2 reports face F-score 0.61 vs. Decaf's 0.57 and hand F-score 0.50 vs. 0.47 — a consistent improvement achieved without a separate contact estimation network trained with 3D annotations.

## Weaknesses

### Fatal
None.

### Major

1. **The abstract and introduction overclaim physical plausibility superiority.** The paper states that DICE achieves "superior performance in terms of accuracy, physical plausibility, inference speed, and generalizability" (line 40). However, on the primary plausibility metric (F-Score), DICE scores 72.7 while Decaf scores 89.6 — a substantial gap. The paper does honestly discuss this trade-off in the results section (lines 275-277), noting that DICE is best *among regression-based methods*. But the high-level framing in the abstract and introduction is misleading: the method is not superior in physical plausibility to the prior state-of-the-art overall. This overstatement weakens the paper's credibility and should be corrected.

### Minor

1. **Generalization to in-the-wild images lacks quantitative evaluation.** The paper claims that the weakly-supervised training scheme "significantly improves generalization capability" (contribution item 2, line 45-46), but the only evidence for in-the-wild performance is qualitative (Fig. 5, Fig. 6). No quantitative metric — 2D reprojection error, keypoint accuracy, or any other measure — is reported on in-the-wild images. Additionally, the ablation (Table 3) shows that removing in-the-wild data *increases* F-Score from 72.7 to 73.3, a small decrease that the paper should acknowledge rather than describing as "maintaining high plausibility." While the reconstruction error metrics (PVE, MPJPE, PAMPJPE) do improve with in-the-wild data, the generalization claim would be substantially strengthened by any quantitative evaluation on in-the-wild data.

2. **Depth supervision pipeline lacks camera model specification.** The paper uses a differentiable rasterizer to render depth maps from the predicted meshes and applies a SILog loss against affine-invariant Marigold depth (Eq. 7). However, the camera model is never specified: is a perspective, weak-perspective, or orthographic camera assumed? What intrinsic parameters are used for projection? The scale and shift alignment between rendered depth and Marigold's affine-invariant output is also implicit. This is a nontrivial reproducibility gap given that the depth loss is the single most impactful component in the ablation (PVE jumps from 8.32 to 15.6 without it).

3. **Discriminator network architectures are not described.** The hand and face discriminators ($D_F$, $D_H$) are central to the adversarial training but their architectures (MLP depth, hidden dimensions, activation functions) are omitted. This prevents reproduction of the adversarial training component.

4. **In-the-wild dataset (500 images) lacks collection and annotation details.** The paper states these images were "collected from the internet" with no details about collection protocol, diversity filters, annotation process, or licensing. This dataset is a claimed contribution; its description is currently insufficient for reproducibility or assessment of potential biases.

### Trivial

1. **Slight F-Score decrease with in-the-wild data is framed inaccurately.** The paper states that adding in-the-wild data "maintains a high plausibility (F-Score)," but the F-Score drops from 73.3 to 72.7. The drop is negligible and does not undermine the contribution, but the framing should be precise.

## Nice-to-Haves

- A quantitative in-the-wild evaluation protocol (e.g., 2D reprojection error on a held-out set of 50-100 in-the-wild images with manually annotated keypoints) would transform the generalization claim from qualitative to verifiable.
- Reporting variance or multiple-seed runs for the main results would strengthen statistical reliability, though this is not standard practice for this type of benchmark.
- Including METRO* as a contact estimation baseline in Table 2 (if feasible) would broaden the comparison.

## Removed Points

These points were raised in the inputs but are removed here with justification:

- **"Method motivation (global vs. local) is hand-wavy"** — Subjective presentation judgment; the design is validated by the ablation study, which is sufficient.
- **"Detector noise under occlusion is not discussed"** — Generic concern applicable to any weakly-supervised method; not a specific problem identified in the paper's results.
- **"Table 1 comparison is unfair because Decaf uses temporal information"** — The paper explicitly acknowledges this (line 273: "Decaf also requires using temporal information in successive frames, while our method only uses a single frame").
- **"Collision distance is not the lowest"** — The paper correctly says "low collision distance" (not "lowest") and frames it in context of the Touchness trade-off.
- **"Single branch ablation trade-off not discussed"** — The paper explicitly states the two-branch design "improves both accuracy and plausibility," which is supported by the data.
- **"Contact estimation baselines missing"** — METRO* does not natively predict contacts; requesting new baselines for a task that only one prior method evaluates is scope creep.
- **"No statistical significance reported"** — Single-run evaluation on fixed benchmarks is standard for this subfield.
- **"Depth supervision magnitude warrants further analysis"** — The paper offers a plausible explanation (noise from unsupervised data); this is an observation, not a weakness.

## Novel Insights

The reviews converge on a clear picture: DICE makes a genuine contribution as the first end-to-end method for hand-face interaction recovery, with strong empirical support for its core claims (accuracy, speed, architecture design). However, the reviews also surface a persistent gap between the paper's confident framing and what the evidence supports — particularly regarding physical plausibility (where Decaf remains superior) and generalization (which is only qualitatively shown). An interesting meta-observation is that the paper's strongest components (the two-branch design, depth supervision pipeline, and adversarial priors) are all validated by careful ablations, while its weakest claims (plausibility superiority over Decaf, quantitative generalization) correspond to components where the paper relies on high-level framing rather than targeted experiments. This pattern suggests that the paper's architecture and training scheme are sound, but it should more clearly delineate *which* dimensions of performance it genuinely advances (accuracy, speed, contact estimation) and which remain trade-offs (plausibility) or are supported only qualitatively (generalization).

## Suggestions

1. **Correct the plausibility framing in the abstract and introduction.** Replace "superior performance in terms of ... physical plausibility" with a precise statement such as "the best plausibility among regression-based methods, while achieving state-of-the-art reconstruction accuracy at interactive rates." The trade-off with Decaf's higher F-Score should be acknowledged early.

2. **Add a quantitative in-the-wild evaluation.** Even a small held-out set with 2D keypoint annotations (e.g., 50-100 images) and 2D reprojection error would substantiate the generalization claim. A user study on perceptual plausibility would be even stronger but is not strictly necessary.

3. **Specify the camera model and projection details** used in the differentiable renderer for depth supervision. Clarify how the scale/shift mismatch between Marigold's affine-invariant depth and rendered depth is handled.

4. **Describe the discriminator architectures** ($D_F$, $D_H$) — at minimum the number of layers, hidden dimensions, and activation functions.

5. **Provide basic metadata for the 500-image in-the-wild dataset** — collection sources, approximate diversity distribution, and release plans.
