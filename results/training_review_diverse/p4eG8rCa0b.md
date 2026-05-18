Now I have all the information I need. Let me write the consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal
### Major
### Minor
### Trivial

## Nice-to-Haves

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision

Let me produce the review.

---

Let me verify one more thing — the paper's own admission of the comparison asymmetry and whether it's truly a "strength" that they outperform baselines.

From the paper (line 107): "Since our model accepts two depth maps and two exemplar images, note that we condition the same images for each modality in Figure 2."
From line 128: "For reconstruction, our model utilizes the depth maps and CLIP image embeddings extracted from the image triplets of ground truth validation images, and baseline models utilize the depth maps and CLIP image embeddings extracted from the ground truth images, since they do not support more than one condition per modality."

So the paper does acknowledge the asymmetry. The question is: does this acknowledgment make the comparison fair? No — acknowledging a bias doesn't remove it. Presenting numbers from an unequal comparison as evidence of superiority is still misleading. The paper says "we find that our model outperforms other models by a large margin" (reconstruction section) without qualifying that the comparison is apples-to-oranges.

OK, I'm confident in my analysis. Let me write the review.Now I have all the information needed. Let me produce the final consolidated review.

---

## Summary

This paper proposes Compose and Conquer (CnC), a conditional diffusion framework that extends Stable Diffusion with two components: (1) Depth Disentanglement Training (DDT), which uses synthetic image triplets (foreground, inpainted background, mask) to teach the model relative depth ordering and correct occlusion, and (2) Soft Guidance, which masks cross-attention similarity matrices to localize CLIP-derived global semantics to specific spatial regions without explicit structural cues. The method is evaluated on COCO-Stuff and Pick-a-Pic datasets against ControlNet, GLIGEN, Uni-ControlNet, and T2I-Adapter.

## Strengths

- **DDT demonstrably improves depth-aware composition.** Figure 3 provides a clean comparison: without DDT, objects fuse or disappear when placed at different depths; with DDT, the model correctly orders objects and handles occlusion. This is the paper's strongest piece of evidence, and the controlled comparison (DDT vs. no DDT within the same architecture) is fair.

- **Soft Guidance prevents concept bleeding across regions.** Figure 5 shows that even with contradictory foreground/background semantics (e.g., igloo vs. jungle), soft guidance maintains foreground semantics intact while background semantics are amplified. The qualitative effect is clear and the mechanism (boolean mask applied to cross-attention similarity) is well-specified.

- **Qualitative results suggest genuine utility for multi-condition control.** The side-by-side comparisons (Figure 2) show CnC balancing depth structure, exemplar semantics, and text prompts more coherently than Uni-ControlNet and T2I-Adapter, which respectively suppress or over-embed global semantics.

- **Two-dataset training strategy is well-motivated.** The paper deliberately combines COCO-Stuff (real images, detailed annotations) with Pick-a-Pic (synthetic, aligned with the SD prior) to prevent prior drift while maintaining strong conditioning. The discussion of this choice (Section 4.3) is thoughtful.

## Weaknesses

### Major

- **Quantitative comparisons are systematically biased by unequal conditioning inputs, undermining numerical claims of superiority.** CnC receives **two depth maps** (foreground + background) and **two CLIP image embeddings** per sample, while baselines receive a single depth map and a single exemplar image. This applies to both the reconstruction metrics (Table 2: LPIPS, SSIM, depth MAE) and the generation metrics (Table 1). The paper acknowledges the asymmetry ("since they do not support more than one condition per modality") but still presents the large-margin outperformance as evidence, without a fair-arm comparison or a direct caveat that the numbers are not apples-to-apples. Until this is addressed — either by adapting baselines to accept multiple conditions, or by showing that CnC outperforms even when restricted to a single depth map and single exemplar — the quantitative superiority claims cannot be trusted. The depth-only experiments, which are more comparable, show CnC *underperforming* on FID/IS, which the paper attributes to the extra inpainted depth map but does not resolve.

- **The claim that DDT lets the model identify "absolute positions" of objects is unsupported.** The abstract and conclusion assert that DDT infers "absolute depth placement" and "absolute positions of unseen objects." Monocular depth maps provide only relative (2.5D) depth — there is no metric 3D coordinate frame, no multi-view consistency, and no ability to rotate or re-render. The model learns relative depth ordering and occlusion, which is a useful capability, but the "absolute" language is factually incorrect. The broader "3D" framing (title: "3D Depth Aware") is also overstated relative to what is demonstrated, though more defensible as field convention.

### Minor

- **The ablation of Soft Guidance lacks quantitative support.** Figure 5 shows visually that soft guidance prevents concept bleeding, but there is no quantitative measure (e.g., CLIP similarity per region, or semantic leakage scores) to back this up. A simple experiment varying λ and measuring per-region CLIP similarity would substantially strengthen the claim.

- **No connection is drawn between Soft Guidance and related attention-masking techniques.** The paper cites GLIGEN as a baseline but does not discuss how soft guidance (binary masking of cross-attention similarity) relates to GLIGEN's gated self-attention, SpaText's spatial attention conditioning, or other layout-control mechanisms. Since the paper itself describes soft guidance as "masking out parts of S," a comparison to these related approaches would clarify the novelty.

- **The advantage of the two-stage training strategy (independent pre-training followed by joint finetuning) is not analyzed.** The paper trains the local fuser for 28 epochs, global fuser for 24 epochs, then finetunes jointly for 9 epochs. No ablation quantifies how much each stage contributes, or whether joint training from scratch would perform differently. This makes it hard to assess whether the multi-stage approach is essential or incidental.

### Trivial

- The phrase "boolean" appears with LaTeX markup artifacts in the text — clearly a parser issue in the extracted version, not a paper problem.
- The "absolute positions" claim appears only at two points (abstract and conclusion); the technical sections consistently describe "relative depth," which is accurate.

## Nice-to-Haves

- A **human preference study** would strengthen the qualitative claims about "balance" and "faithful recreation," especially given known limitations of automated metrics like FID and CLIPScore for perceptual quality.
- A **discussion of failure cases** beyond the brief limitation note (e.g., cases where monocular depth estimation fails, or non-convex masks lead to artifacts) would improve completeness.
- Reporting **total GPU-hours** rather than just epochs × GPUs would help readers assess computational cost.

## Removed Points

These points were raised by reviewers but removed or downgraded per the meta-review guidelines:
- *Criticism about comparing to 3D-aware GANs/NeRF* — This evaluates the paper against a different class of methods (true 3D generation vs. 2D depth-conditioned synthesis). Removed as scope-inappropriate.
- *Claim that DDT novelty is merely a data recipe* — The critic understates the contribution; the data generation pipeline + separate-stream architecture + training methodology together constitute a training paradigm. The paper's own admission of "late fusion" shows appropriate self-awareness. Downgraded from the critic's framing.
- *Formatting/style nitpicks about parser artifacts* — Removed per hard rules.
- *Strength about "unified framework outperforms baselines" from Strength Finder* — Conflicts with the verified major weakness about unfair comparison. Per rules, when strength and weakness disagree, weakness wins. Reframed below as a qualitative observation rather than a verified quantitative claim.

## Novel Insights

None beyond the paper's own contributions. The meta-review reveals that the paper's strongest evidence is qualitative (Figure 3 for DDT, Figure 5 for soft guidance), while the quantitative evaluation is compromised by an unequal comparison setup. A recurring pattern in the reviews is the gap between the paper's compelling visual demonstrations and its unreliable numerical claims — the qualitative results are likely sufficient to establish the method's viability if the quantitative evaluation were repaired.

## Suggestions

1. **Fix the baseline comparison.** The single most important revision: either (a) adapt baselines to accept two depth maps and two exemplar images, or (b) restrict CnC to a single depth map and single exemplar for a fair comparison. If CnC still outperforms in the fair setting, the case is much stronger. If not, the paper should honestly report this.
2. **Remove or rephrase the "absolute positions" claim.** Replace with "relative depth ordering" or "depth-aware placement," which accurately describes what the model does.
3. **Add quantitative ablations for Soft Guidance.** Measure per-region CLIP similarity with and without the mask, varying λ, to quantify the concept-bleeding prevention shown qualitatively in Figure 5.
4. **Discuss connections to related attention-masking methods** (GLIGEN, SpaText, etc.) to clarify what soft guidance adds over existing techniques.
5. **Ablate the two-stage training strategy.** Show what changes when training the full model jointly from the start versus the proposed staged approach.

## Score and Decision

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>