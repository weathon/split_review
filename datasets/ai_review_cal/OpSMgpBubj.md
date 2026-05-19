- Decision: Reject
- Avg Score: 5.60
- Scores: 8, 5, 5, 5, 5
Now I have all the information needed. Let me produce the consolidated final review.

## Summary

The paper proposes CLIP-DETR, a training framework for DETR-based object detectors that integrates CLIP's vision-language knowledge into both encoding and decoding. Two modules are introduced: (1) **AlignNet**, which performs category- and scale-aware feature refinement on the encoder output by aligning pooled ground-truth features with CLIP text embeddings via contrastive learning, and (2) **DynQL (Dynamic Query Learning Mechanism)**, which creates multiple sets of decoder queries at varying noise levels from CLIP attribute features to improve query-object adaptability. Experiments on COCO, LVIS, and open-vocabulary COCO show consistent improvements over several DETR-based baselines.

## Strengths

1. **AlignNet's use of ground-truth boxes (not region proposals) for feature pooling is a clean design choice that reduces noise.** Section 3.2 explicitly contrasts with RegionCLIP and similar work by leveraging GT bounding boxes for ROI pooling (Eq. 1), enabling cleaner alignment between encoder features and CLIP-derived semantic+scale features. This is a principled improvement over proposal-based alternatives.

2. **The AblationNet analysis in Table 5 reveals a non-trivial insight: scale information [w,h] alone outperforms full bounding box [cx,cy,w,h] for feature alignment.** The paper provides a reasoned explanation — translation invariance makes absolute position features confusing for encoding — which goes beyond a simple engineering trick and offers a principled design lesson.

3. **DynQL is well-ablated along its key design dimensions.** Table 6 compares fixed noise levels (β=0.3, 0.5, 0.9) against the proposed uniform multi-noise schedule (0.1→0.9), showing that the multi-noise variant performs best. Table 7 ablates the number of query sets. Together, these experiments provide concrete evidence that the multi-level noise design is the source of the improvement, not a single noise level.

4. **Consistent, non-trivial gains across multiple benchmarks and backbones.** On COCO, CLIP-DETR achieves +3.9 % mAP (ResNet-50) and +5.1 % (CLIP backbone) over Deformable-DETR. LVIS results in Table 2 show consistent improvements over Co-DETR. Open-vocabulary results on OV-COCO (Table 3) show gains on both novel and base categories for two different baselines (OV-DETR and CORA).

5. **Component-level ablation (Table 4) cleanly isolates the contribution of each module.** Both AlignNet and DynQL independently improve the baseline, and their combination yields the best result, supporting the paper's claim that both encoding and decoding enhancements are necessary.

## Weaknesses

### Fatal
None.

### Major

1. **The claim of "state-of-the-art" performance is not supported by the experimental scope.** The abstract claims CLIP-DETR "significantly outperforms state-of-the-art models in object detection and open-vocabulary detection tasks." However, the open-vocabulary evaluation (Table 3) is limited to two DETR-based baselines (OV-DETR, CORA) and shows only modest gains (1.4–1.7 % AP50 on novel categories). Strong non-DETR open-vocabulary detectors are not compared. The closed-set evaluation does compare against strong DETR training schemes (DINO, Co‑DETR), but this still does not warrant an unqualified "state-of-the-art" claim. The claim should be scoped to "DETR-based detectors" or the comparison set must be expanded. This overclaim inflates the perceived contribution.

2. **The open-vocabulary evaluation is too narrow to support the paper's broad claims.** Only the OV-COCO split is used; the more challenging LVIS open-vocabulary setting is not evaluated. Additionally, only two DETR-based open-vocabulary methods are compared. For a paper claiming SOTA in open-vocabulary detection, this limited evaluation undermines the claim.

### Minor

1. **DynQL's novelty against standard denoising is not fully disentangled.** While Table 6 compares single-noise vs. multi-noise DynQL variants (which is good), the ablation does not include a head-to-head comparison against a standard DINO-style denoising module (noise on 4D anchors + labels, without CLIP attribute features) implemented in the same codebase. Without this comparison, it is unclear how much of the gain comes from (a) the multi-noise design, (b) using CLIP features as query content, or (c) simply adding any form of supervised denoising queries. The paper plausibly argues for (a), but the evidence is circumstantial rather than directly isolating it.

2. **Baseline implementations are not fully confirmed to be controlled re-implementations.** The paper states "we chose Deformable-DETR as the foundational detector and built all models upon it to ensure a fair comparison" (Section 4.1), which implies re-implementation. However, it does not explicitly state whether the DINO and Co‑DETR results come from re-runs under identical hyperparameters or from published papers. Standard tricks in learning rate scheduling, data augmentation, and decoder layer count can shift mAP by several points. Explicit confirmation and reporting of variance across seeds would strengthen confidence in the claimed improvements.

3. **The claim that AlignNet enhances "feature map sensitivity to objects" is slightly overreaching.** The contrastive loss in AlignNet only supervises features at GT box locations (pooled regions), not the entire feature map. While gradients back-propagate to the encoder, the paper provides no analysis (e.g., feature-map visualizations, per-location gradient analysis) showing that the effect propagates beyond the pooled regions. The design is sensible, but the claim about the feature map as a whole goes modestly beyond what is demonstrated.

4. **No statistical significance or variance reported.** All results appear to be single runs. Given that detection mAP can vary by 0.2–0.4 points across seeds, the small differences in some open-vocabulary results (0.5–1.7 % AP50) could partially fall within noise.

### Trivial
None.

## Nice-to-Haves

- Compare DynQL directly against a standard DINO-style denoising module (label+box noise, without CLIP features) in the same codebase. This would cleanly attribute the source of improvement.
- Report training-time overhead (extra forward passes, contrastive loss cost) since the paper emphasizes inference-time efficiency is unchanged.
- Include a limitations paragraph discussing failure cases (e.g., when CLIP representations are poor for rare categories, or when GT boxes are used during training but inference relies on learned queries).
- Report results on the LVIS open-vocabulary setting to broaden the evaluation.

## Removed Points

- **"DynQL never compares against a simpler denoising baseline"** — Removed as factually inaccurate. Table 6 directly compares fixed single-noise query sets (β=0.3, 0.5, 0.9) against the multi-noise uniform variant. The paper does compare simpler baselines; the criticism is downgraded to Minor weakness #1 (missing a specific DINO-style formulation).
- **"Missing related works (GLIP, OWL-ViT, ViLD)"** — Removed per instructions (missing-related-work critiques are excluded). The substantive issue (overclaiming SOTA without comparing those methods) is already captured in Major weakness #1.
- **Reproducibility nitpicks about unspecified hidden dimensions, number of decoder layers, etc.** — Removed as nitpicks. These are standard Deformable-DETR defaults and can be inferred; the paper specifies batch size, LR, schedule, and backbone.
- **Strength Finder item about "addressed an important problem"** — Removed as generic/superficial.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface a perspective on the paper that meaningfully reframes or extends its contributions beyond what the authors themselves claim.

## Suggestions

1. **Scale back the SOTA claims** to "strong performance among DETR-based detectors" or provide a broader comparison including non-DETR open-vocabulary methods. The current framing invites justified skepticism.
2. **Add a controlled comparison** between DynQL and a standard DINO-style denoising module using the same codebase and CLIP features. This directly answers the main validity concern about the decoder contribution.
3. **Explicitly confirm** that all baseline results (DINO, Co‑DETR) are re-implemented under identical settings and report variance over at least 3 seeds.
4. **Expand open-vocabulary evaluation** to include at minimum the LVIS OV setting, and clarify that the comparison scope is DETR-based methods.
