I now have a thorough understanding of the paper and all claims. Let me synthesize the final review.

---

## Summary

This paper presents DICE, the first end-to-end regression-based method for deformation-aware hand-face interaction recovery from a single image. It uses a two-branch Transformer architecture (MeshNet for global mesh, InteractionNet for local deformation/contact) with a weakly-supervised training pipeline incorporating in-the-wild images, depth priors from Marigold, and adversarial pose priors. The key empirical result is that DICE achieves competitive reconstruction accuracy (PVE 8.32) against the prior state-of-the-art optimization-based Decaf (PVE 9.65) while running at 20 fps — a ~400× speedup — and achieves the best accuracy and contact F-scores among all regression-based approaches.

## Strengths

- **First end-to-end method for hand-face interaction recovery with deformations.** The paper fills a clear gap: the only prior work (Decaf) requires per-image optimization (>15s), making it unusable for interactive applications. DICE operates at 20 fps, directly enabling AR/VR use cases. This is a genuine contribution, not an incremental improvement.

- **Strong reconstruction accuracy (PVE 8.32) with dramatic speedup.** Table 1 shows DICE outperforms Decaf (PVE 9.65) and all other baselines in reconstruction error. Combined with real-time inference, this represents a favorable point on the accuracy-speed Pareto frontier that did not previously exist for this task.

- **Two-branch architecture validated by ablation.** The ablation (Table 2) shows the two-branch design outperforms a single-branch variant across all accuracy metrics (PVE: 8.32 vs. 9.29, MPJPE: 9.95 vs. 11.6) and F-Score (72.7 vs. 69.3), demonstrating that disentangling global mesh regression from local deformation/contact estimation is beneficial.

- **Weakly-supervised training scheme with clear ablative support.** Each component of the weak-supervision pipeline (in-the-wild data, depth loss, adversarial loss, parameter supervision) is individually ablated in Table 2, and each removal degrades performance. This provides reasonable evidence that the pipeline contributes to accuracy.

- **Best contact estimation among all methods.** Table 3 reports higher contact F-scores than Decaf for both face (0.61 vs. 0.57) and hand (0.50 vs. 0.47), indicating more precise contact detection.

## Weaknesses

### Fatal
None.

### Major

- **Overclaiming on physical plausibility in the abstract and conclusion.** The abstract states DICE achieves "state-of-the-art performance... in terms of accuracy and physical plausibility" and the conclusion claims "state-of-the-art accuracy and plausibility, compared with all previous methods." However, Table 1 shows Decaf achieves F-Score 89.6 vs. DICE's 72.7 — a substantial gap in the very metric designed to measure physical plausibility. The paper correctly qualifies this only in the results section ("highest overall physical plausibility (F-Score) among all regression-based methods," line 276), but the abstract and conclusion omit this qualification, creating a misleading impression of universal superiority. This is a framing issue that misrepresents the paper's actual position relative to Decaf.

- **No quantitative evaluation on in-the-wild data despite claiming generalization.** The paper repeatedly claims superior performance on "challenging in-the-wild images" (abstract, introduction, conclusion), and the weakly-supervised pipeline is motivated as improving generalization. However, all quantitative evaluations are conducted exclusively on the Decaf test set (studio data with green screens). The only support for in-the-wild performance is qualitative (Figures 5, 6). The ablation (Table 2) shows that adding in-the-wild data improves metrics on the *Decaf* test set, which is an indirect effect, not a direct measure of generalization to truly unconstrained images. Without any quantitative metric on in-the-wild data — even a proxy like 2D keypoint reprojection error or a user study — the generalization claim remains unsupported at the level the paper asserts it.

### Minor

- **METRO* baseline is underspecified.** The paper introduces a modified METRO with "extra output heads added to predict contact and deformation" (line 165) but provides no details on how these heads were designed, how the model was trained, or whether hyperparameters were tuned for this new task. The claimed "30% reduction in reconstruction error" relative to this baseline is difficult to evaluate without knowing whether the comparison is fair. A baseline whose adaptation to the task is not documented carries limited meaning.

- **The depth supervision pipeline's reliance on Marigold is not analyzed for failure modes.** The ablation (Table 2) shows that removing the depth loss causes PVE to degrade from 8.32 to 15.6 — worse than training without any in-the-wild data at all (PVE 8.93). While the paper notes this (lines 328–330), it does not characterize when Marigold's depth estimates are unreliable (e.g., near hand-face occlusions, close-range contacts), nor discuss how such errors propagate. Since the entire weakly-supervised pipeline hinges on this component, understanding its failure cases is important for assessing practical robustness.

- **F-Score slightly decreases when adding in-the-wild data, but this is not discussed.** Table 2 shows the full model has F-Score 72.7 vs. 73.3 for the model trained without in-the-wild data. While this small decrease does not undermine the contribution, the paper states the weak-supervision "maintains a high plausibility (F-Score)" (line 325) without acknowledging the slight drop. A candid discussion would strengthen the paper.

- **No variance or error bars reported.** All metrics are reported as single numbers without standard deviations or confidence intervals. Given the use of adversarial training and a small (500-image) in-the-wild set, the variance across training seeds could be non-negligible.

### Trivial

- **λ_adv appears in the loss equation (Eq. 6) but its value is not specified.** The paper lists λ_mesh = 12.5, λ_interaction = 5, λ_depth = 2, but omits λ_adv.
- **The Transformer masking fraction is not specified.** The paper states "we mask the image feature maps corresponding to a random subset of vertices" (line 87) without indicating what fraction is masked, which matters for reproducibility.

## Nice-to-Haves

- A quantitative evaluation on in-the-wild data (e.g., 2D keypoint reprojection error against MediaPipe detections as a proxy, or a user study on interaction plausibility) would directly support the generalization claim.
- Separately evaluating deformation field accuracy (not just overall vertex error) would strengthen the deformation-specific contribution claims.
- A few representative failure cases (e.g., where Marigold depth is inaccurate) would help calibrate reader expectations about the method's limitations.

## Removed Points

- *"Depth supervision ablation reveals a fragile training pipeline"* — This critique oversells a normal ablation result. The paper explicitly acknowledges the depth loss is critical (lines 328–330) and explains why removing it degrades performance. Showing that a component matters is the purpose of an ablation, not evidence of fragility. However, the related point about not analyzing Marigold failure modes is retained as a Minor weakness (see above).
- *"Decaf's collision distance (1.03) is suspiciously high"* — This concerns Decaf's numbers, not DICE's. Not a weakness of the paper under review.
- *"The paper could be more precise about Decaf's use of temporal information"* — This is a minor suggestion about clarity, mentioned elsewhere in the introduction already (line 273).
- *Strength Finder claim "best physical plausibility among regression-based methods"* conflicts partially with the verified overclaiming weakness — retained because the strength is factually correct when properly qualified, but the qualification issue is captured under Major weaknesses.

## Novel Insights

The reviews surface a consistent tension: the paper has a real contribution (speed + accuracy, first end-to-end), but it weakens its own case by stretching claims beyond what the evidence supports. The most actionable insight is that the paper would be *stronger* if it leaned into its actual differentiator — end-to-end speed with competitive accuracy — rather than claiming universal superiority. The missing quantitative in-the-wild evaluation is the single largest gap; filling it would resolve the main uncertainty about whether the weakly-supervised pipeline genuinely generalizes.

## Suggestions

1. **Reframe the contributions honestly.** Replace unqualified "state-of-the-art accuracy and plausibility" with precise language: "state-of-the-art reconstruction accuracy, best among regression-based methods in physical plausibility, and interactive speed (20 fps)." This is still impressive and avoids misleading readers.

2. **Add at least one quantitative measure on in-the-wild data.** Even an indirect metric (e.g., 2D keypoint reprojection error on the 500 in-the-wild images using MediaPipe detections as reference) would substantiate the generalization claim far more than qualitative figures alone.

3. **Document the METRO* adaptation** — architecture details, training protocol, hyperparameters — so readers can assess the fairness of the comparison.

4. **Add a brief analysis of depth prior failure cases** to the limitations section, and expand the limitations paragraph to acknowledge the small in-the-wild dataset size and the F-Score gap with Decaf.

## Score and Decision

**Originality:** 7/10 — First end-to-end method for this specific task, with a well-motivated two-branch architecture and a novel weak-supervision pipeline.

**Importance of research question:** 8/10 — Hand-face interaction recovery has clear practical value for AR/VR, and the speed limitation of prior work was a real bottleneck.

**Claims well-supported:** 5/10 — Accuracy and speed claims are well-supported; physical plausibility and in-the-wild generalization claims are not supported at the level asserted.

**Soundness of experiments:** 6/10 — Ablations are thorough and well-structured; missing in-the-wild quantitative evaluation and underspecified baseline weaken the overall experimental package.

**Clarity of writing:** 7/10 — Generally clear; overclaiming in high-level summaries detracts from otherwise careful technical presentation.

**Value to the research community:** 7/10 — A useful benchmark for future work on this task, providing both a strong baseline and a practical speed-accuracy tradeoff.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>