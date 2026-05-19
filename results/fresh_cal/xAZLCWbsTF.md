Here is the synthesized final review.

---

## Summary

This paper proposes CRAFT, a self-supervised multi-frame depth estimation method that replaces the traditional epipolar geometry-based cost volume with a cross-attention map. The authors demonstrate that a cross-attention map is mathematically similar to a full cost volume (considering all pixel pairs), and that masked image modeling pretraining (CroCo-v2) causes the cross-attention layers to implicitly learn a warping function resembling epipolar warping. They design the CRAFT module to compress and refine the cross-attention map, and arrange it hierarchically for coarse-to-fine depth prediction. The method requires no pose network at inference and shows strong results on dynamic-object and noisy-image benchmarks (Cityscapes, KITTI/RoboDepth).

## Strengths

- **Novel insight connecting cross-attention to full cost volumes.** The paper clearly derives the mathematical similarity between cross-attention maps (Eq. 7) and a full cost volume (Eq. 6), and explains why MIM training (CroCo-v2) makes the cross-attention map function as an implicit warping mechanism. This provides a principled alternative to epipolar cost volumes.

- **Impressive robustness in dynamic and noisy scenarios.** Tables 1 and 2 show that CRAFT substantially outperforms prior self-supervised multi-frame methods on moving objects (Cityscapes dynamic-object subset) and under multiple noise types (motion blur, defocus blur, Gaussian noise, impulse noise) across three noise scenarios. These are the settings where epipolar methods fundamentally struggle, and the gains are large.

- **Ablation confirms the CRAFT components are necessary.** Table 5 shows that removing attention aggregation, feature aggregation, or the consistency mask degrades performance, and that the hierarchical CRAFT structure outperforms using a DPT head (single-frame decoder) with the same backbone. This confirms that the multi-frame cross-attention processing proposed in the paper adds value beyond the backbone alone.

- **No pose network needed at inference.** Unlike prior multi-frame methods (ManyDepth, DynamicDepth, DualRefine) that require a pose network or monocular depth prior, CRAFT generates depth with a single forward pass, simplifying the pipeline and reducing computational overhead.

- **Comprehensive evaluation following established protocols.** The dynamic-object evaluation follows DynamicDepth and the noise evaluation follows RoboDepth, using standard metrics and multiple noise scenarios. This makes the results directly comparable and the experimental design reproducible.

## Weaknesses

### Fatal

None.

### Major

- **Controlled comparison between cost-volume types is missing, conflating core claim with backbone strength.** The paper's central claim is that a cross-attention map functioning as a full cost volume is more robust than epipolar cost volumes. However, every comparison against prior methods (ManyDepth, DynamicDepth, DualRefine) uses a ViT encoder initialized with CroCo-v2, while the baselines use ResNet encoders trained from scratch. The paper does not include a controlled experiment that keeps the same ViT+CroCo backbone but attaches an epipolar cost volume (with a small pose network). Without this, the reported gains cannot be cleanly attributed to the cross-attention map mechanism vs. the stronger backbone and pretraining. The ablation in Table 5 compares CRAFT vs. a DPT head (single-frame), which isolates the multi-frame benefit but not the cost-volume type. This is the single most important missing experiment; it directly impacts whether the paper's main claim is supported.

### Minor

- **Unspecified whether CroCo-initialized weights are frozen or fine-tuned during depth training.** The paper states that the encoder and decoder are "initialized with CroCo-v2 weights" (Section 5.1) but never specifies whether the cross-attention layers are frozen or fine-tuned during the self-supervised depth training stage. If fine-tuned, the depth loss itself could be teaching the correspondences, weakening the "emergent" framing. This matters for understanding how the cross-attention map acquires its geometric functionality. The distinction between "initialized" and "initialize-and-freeze" should be stated explicitly.

- **Final depth prediction head is not described in the main text.** The paper describes the CRAFT modules producing refined cost volumes at four hierarchical levels, but how these refined cost volumes are mapped to a final depth map is not specified. The ablation mentions a "DPT head" as a baseline, but the actual depth regression layer(s) used in the full CRAFT pipeline are not explained. The paper references an appendix (Section B) for details, but the main text should at least outline this step for a self-contained understanding.

- **No discussion of limitations or failure cases.** The paper does not acknowledge potential limitations of the approach, such as: reliance on a large pretraining dataset (CroCo), the memory footprint of the h×w×h×w cross-attention map, or scenarios where the approach might underperform (e.g., severe occlusions, textureless regions). Including a limitations paragraph would strengthen the paper.

### Trivial

- **Training hyperparameters (learning rate, batch size, epochs, data augmentation) are absent from the main text.** The paper says "Further details … in Section B" — but since the appendix content may be stripped in review formats, key hyperparameters should be summarized in the main paper.

## Nice-to-Haves

- A quantitative evaluation of the cross-attention map's correspondence accuracy (e.g., measuring keypoint matching or comparing to ground-truth optical flow on static scenes) would strengthen the claim that the attention map "implicitly learns geometry" rather than just being a flexible feature fusion mechanism.

## Removed Points

These points from the reviewer inputs have been removed with justification:

- **"Not entirely novel" (Section 4.1.2 connection mirrors prior work)** — Removed. This is an opinion, not a concrete weakness. The paper's contribution is the specific application of cross-attention maps as cost volumes for self-supervised depth estimation, which is novel in this context.

- **"Baselines not re-trained with same augmentation"** — Removed. Using published numbers from baseline papers is standard practice. The criticism asks for a standard not typically required.

- **"One qualitative example in Figure 3 is not sufficient evidence"** — Removed as a standalone weakness. The paper provides quantitative results (Tables 1–4) and ablations (Table 5) that collectively support the claim; the figure is illustrative. The point about limited quantitative correspondence evaluation is preserved as a Nice-to-Have.

- **"Missing appendix content"** — Removed. The appendix is stripped by the parser; we cannot penalize the paper for content that exists in the original submission.

- **"Evaluation fairness is questionable because models not trained with noise"** — Removed. The noise evaluation protocol follows RoboDepth, which tests robustness to distribution shift; training with noise would defeat the purpose of measuring robustness to unseen corruptions.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface a perspective or connection that the paper itself does not discuss.

## Suggestions

1. **Add the critical controlled experiment**: Use the same ViT encoder + CroCo-v2 initialization, equip it with a standard epipolar cost volume (plus a small pose network), train under the same photometric loss and data, and compare to CRAFT. This isolates the effect of the cost-volume type from the backbone strength and directly supports or refines the paper's central claim.

2. **Explicitly state the training regime**: Clarify in Section 5.1 whether the CroCo-v2 weights (encoder, decoder, cross-attention layers) are frozen or fine-tuned during self-supervised depth training. If frozen, this strengthens the "emergent" claim; if fine-tuned, acknowledge this and discuss its implications.

3. **Describe the final depth regression head**: Add a sentence or two in Section 4.3 or 5.1 explaining how the refined cost volumes from the hierarchical CRAFT modules are converted into a final depth map (e.g., a convolutional prediction head or a DPT-like reassemble-then-regress layer).

4. **Add a limitations paragraph**: Acknowledge the reliance on CroCo pretraining (compute/data cost), the memory footprint of the full cross-attention map, and potential failure cases (severe occlusions, textureless regions).

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>