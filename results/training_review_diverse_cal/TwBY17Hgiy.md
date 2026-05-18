## Summary

This paper proposes a 3D-aware regularizer for multi-task learning (MTL) of dense prediction tasks. The regularizer maps features from a shared encoder to a tri-plane representation, decodes them through lightweight task-specific MLPs with a learned density field, and renders task predictions via differentiable volume rendering. Crucially, the regularizer is discarded at inference time, incurring zero additional cost. The method consistently improves two strong MTL backbones (MTI-Net with HRNet-48 and InvPT with ViT-L) across all tasks on NYUv2 (e.g., +1.31 mIoU segmentation, −0.0177 depth RMSE) and PASCAL-Context (e.g., +1.51 mIoU part segmentation), and the improvement is not simply from added capacity, as shown by an ablation against auxiliary heads.

## Strengths

- **Consistent multi-task improvement across architectures and datasets.** The regularizer improves performance on every task for both the CNN-based MTI-Net and the transformer-based InvPT on both NYUv2 (Table 1) and PASCAL-Context (Table 2). Gains are positive across all 9 task×dataset combinations, not just a cherry-picked subset. This consistency is the paper's strongest empirical evidence.

- **Zero additional inference cost.** The regularizer is discarded after training, so the method enhances MTL performance without any extra computation at test time — a clear practical advantage over approaches requiring task-specific modules during inference.

- **Architecture agnosticism validated on two fundamentally different backbones.** Demonstrating improvement on both a convolutional (HRNet-48) and a transformer (ViT-L) backbone provides credible evidence that the benefit is not specific to one architectural family.

- **Ablation against auxiliary heads rules out the "extra capacity" confound.** Table 4 shows that adding simple auxiliary decoders degrades segmentation (−1.11 mIoU) while the 3D-aware regularizer improves it (+1.31 mIoU), confirming the gains are not merely from additional parameters.

## Weaknesses

### Fatal
None.

### Major

- **The claim that improvements come from learned "3D structure" rather than from specific architectural inductive biases is not directly verified.** The rendering uses a fixed orthogonal projection with no viewpoint input (stated explicitly in the Discussion), and the regularizer is trained entirely from 2D task losses on single views. While the tri-plane + volume rendering architecture is inspired by 3D methods (EG3D, NeRF), nothing in the training forces the learned tri-plane to encode geometrically consistent scene structure — the model could simply learn a "deformed 2D feature map" embedded in 3D coordinates. The improvement over auxiliary heads shows the architecture matters, but does not isolate whether the benefit comes from *3D structure* specifically or from the tri-plane encoder + MLP + rendering *as a well-chosen 2D feature transformation*. A controlled baseline — e.g., a 2D convolutional decoder with comparable complexity performing the same auxiliary tasks — would substantially strengthen the core claim. As written, the "3D-aware" label over-interprets what has been demonstrated.

### Minor

- **No error bars or multiple runs.** All results are from single runs. The NYUv2 training set has only 795 images, and some improvements are modest (e.g., +0.06 mIoU for the multi-view variant, identical 74.80 boundary at 25% data). Without variance estimates, it is impossible to assess whether the smaller gains are robust or within run-to-run noise. Multi-run reporting is the standard expectation for papers making fine-grained architectural claims.

- **The cross-view consistency experiment is underpowered as evidence of multi-view geometry.** Only depth is labeled on the second view (line 177–178), so only depth receives multi-view supervision. The gains over the single-view variant are marginal (depth RMSE 0.4879→0.4850, boundary odsF 77.90→78.00). The paper acknowledges these are modest (line 296) but then uses the experiment to support claims about 3D consistency, which requires more direct evidence.

- **The rendering resolution is very low (56×72 for NYUv2).** The paper acknowledges this and notes the regularizer's direct predictions are worse than the task-specific heads, which is acceptable for a regularizer. However, the gradient signal backpropagated through the low-resolution pathway may simply act as a form of feature regularization (e.g., smoothing or frequency-limiting) rather than providing geometrically meaningful signal. This alternative explanation is not discussed or ruled out.

- **The data-ablative experiment is partially inconsistent with the "low-data helps" narrative.** At 25% data, boundary detection is identical (74.80) for baseline and method, and segmentation improves by only +0.96 mIoU. Improvements are larger at 100% data, which is somewhat at odds with the intuition that an inductive bias from 3D structure should help *more* when data is scarce.

### Trivial

- The paper claims "consistently outperforms the baseline on all tasks in all label regimes" (line 387), but boundary at 25% is tied at 74.80. The claim is technically non-false (non-negative), but slightly imprecise.

## Nice-to-Haves

- A controlled comparison against a 2D regularizer of matched complexity (e.g., a convolutional decoder with comparable parameters performing the same auxiliary tasks) would isolate the benefit of the 3D-inspired architecture from the benefit of extra capacity + auxiliary supervision.
- A direct probe of 3D consistency — e.g., rendering predictions from two different viewpoints using the learned density and measuring their agreement — would substantially strengthen the mechanistic claim.
- An ablation of the hyperparameter $\alpha_t$ would help understand sensitivity.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"The paper never probes whether the learned representations actually capture geometric structure"** — Partially addressed by the cross-view experiment (Table 3), though the probe is weak. The underlying concern (no direct 3D consistency evaluation) is retained in Major weakness #1, but the absolute phrasing "never probes" is inaccurate.

2. **"The regularizer does not help in the low-data regime" (critic on 25% data)** — Factually incorrect for 3 of 4 tasks: segmentation (43.83→44.79), depth (0.6060→0.5972), and normals (21.76→21.57) all improve at 25%. Only boundary is identical. The critic's framing misrepresents the data.

3. **"The qualitative examples appear cherry-picked"** — Pure speculation with no evidence. Standard practice for qualitative figures across the field.

4. **"Architecture agnostic but only tests on two backbones"** — CNN (HRNet-48) and transformer (ViT-L) are fundamentally different architectural families covering the two dominant paradigms in dense prediction. This is sufficient support for the claim.

5. **"The cross-view experiment could be attributed to having more depth training data"** — While true that only depth receives multi-view supervision, the method does render from a transformed viewpoint using estimated camera pose, which does test multi-view geometric consistency for depth. The concern is acknowledged in Minor weakness #2 without needing this framing.

6. **Auxiliary heads comparison "does not control for architectural complexity"** — The critic demands a 2D regularizer of matched complexity. This is a Nice-to-Have, not a core flaw, because the ablation already controls for *capacity* rather than *architecture type*, which is the most common and interpretable confound.

## Novel Insights

Beyond the paper's own contributions, the review process reveals a tension at the heart of the work: the paper draws on the language and machinery of 3D vision (tri-planes, density fields, volume rendering) but applies it in a setting where the geometric grounding is fundamentally weaker than in NeRF-style methods (fixed orthogonal projection, single view, no camera pose input). This creates a gap between the claimed mechanism ("3D consistency") and what is actually demonstrated (architecturally beneficial auxiliary regularization). The paper would benefit from explicitly positioning itself as using 3D-*inspired* architectural inductive biases for MTL, rather than claiming to learn actual 3D structure — the empirical contribution is strong enough to stand on its own without over-claiming the mechanism.

## Suggestions

1. **Temper the "3D-aware" framing** to more precisely describe what is established: an architecture with 3D-inspired inductive biases (tri-plane, density, volume rendering) that improves MTL performance, with the mechanism being an open question that future work could probe more directly.
2. **Report means and standard deviations over at least 3 seeds** for the main experiments, especially NYUv2 where the training set is small and improvements are modest.
3. **Add a controlled 2D baseline** — replace the tri-plane encoder + MLP + volume rendering with a convolutional decoder of similar parameter count performing the same auxiliary tasks. This is the cleanest way to isolate whether the 3D-inspired design matters.
4. **Probe the learned density** by visualizing or evaluating whether the density field correlates with scene depth, or by rendering from a novel viewpoint and checking consistency.

## Score and Decision

**Score:** 6.0 — A solid paper with a clean, practical idea and consistently positive empirical results. The main concern is about interpretive framing rather than the empirical contribution itself, which is real. With modest revisions to temper the mechanistic claims and add more rigorous evaluation, this would be a strong paper.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>