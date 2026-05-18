Now I have all the verification I need. Let me write the authoritative consolidated review.

## Summary

This paper proposes Hierarchical Side-Tuning (HST), a parameter-efficient transfer learning method for Vision Transformers. HST introduces a lightweight Hierarchical Side Network (HSN) that operates in parallel with a frozen ViT backbone, using a Meta-Register token, a Transformation Bridge (T-Bridge), and cross-attention-based Side blocks to fuse multi-scale features. Extensive experiments across image classification (VTAB-1K, FGVC, CIFAR-100), object detection, instance segmentation, and semantic segmentation show that HST achieves state-of-the-art results among PETL methods and, on several benchmarks, approaches or surpasses full fine-tuning with substantially fewer trainable parameters.

## Strengths

1. **Strong and consistent classification results with high parameter efficiency.** On VTAB-1K, HST achieves 76.1% average Top-1 accuracy using only 0.78M trainable parameters, outperforming strong PETL baselines (SSF, LoRA, AdaptFormer, NOAH) by 2.9–3.85%. The gains are consistent across all 19 tasks and the comparison on classification is fair — all methods share the same backbone and classification head with no architectural advantage in multi-scale features (Table 1).

2. **Surpasses full fine-tuning on several dense prediction benchmarks.** On COCO with Cascade Mask R-CNN 3×+MS, HST achieves 49.5 AP^b and 43.0 AP^m, exceeding full fine-tuning's 48.7 AP^b and 42.2 AP^m while using 68.4M vs 151.4M trainable parameters (Table 3). On ADE20K semantic segmentation with UperNet, HST achieves 47.5 mIoU (MS), the strongest among PETL methods (Table 4). This is the first PETL method to surpass full fine-tuning on several dense prediction settings.

3. **Linear-complexity cross-attention for efficient global injection.** The Side block uses cross-attention where K and V have only 2 tokens (Meta-Global), resulting in O(2Ld) complexity — linear in sequence length L (Equation 3, Figure 4). This enables efficient multi-scale feature fusion that prior PETL methods lack.

4. **Robust across pre-training paradigms.** Under MAE pre-training, most PETL methods fall significantly below full fine-tuning, but HST matches or exceeds it on 4/5 FGVC datasets (Table 2). For example, HST achieves 91.2% on Oxford Flowers vs full fine-tuning's 90.9%, while VPT-Deep only reaches 87.4%.

5. **Thorough ablation study.** The paper systematically ablates each component (LN tuning, weight sharing, GlobalT, FG injection) in Table 6, demonstrating that each contributes positively on both classification and dense prediction. Notably, weight sharing reduces params from 1.10M to 0.78M while *improving* classification accuracy (74.3% → 75.0%).

6. **Single Meta-Register token suffices.** Unlike VPT which requires searching for prompt lengths (sometimes hundreds), ablation (Table 5) shows that going from 1 to 32 Meta-Register tokens yields marginal gains (76.1% → 76.2%), simplifying deployment.

## Weaknesses

### Fatal
None.

### Major

1. **Unfair comparison in dense prediction tasks — architectural advantage is confounded with tuning method.** For object detection, instance segmentation, and semantic segmentation, HST builds a complete Hierarchical Side Network (HSN) with its own convolutional stem, cross-attention, and feature pyramids at four scales (13.21M params for ViT-B). This HSN generates multi-scale feature maps that are fed into FPN and task heads. In contrast, baseline PETL methods (VPT, AdaptFormer, LoRA, SSF) only insert lightweight modules inside the frozen backbone — they have no external side network and thus no architectural capacity comparable to HSN's multi-scale processing. The paper states (lines 185–186) that all methods follow Li et al. 2021 to upsample/downsample ViT features for FPN, but HST *additionally* processes the input image through its own convolutional stem and performs cross-attention with frozen backbone features. The performance gains on dense tasks may therefore be driven substantially by this architectural enrichment rather than by a more effective parameter-efficient tuning scheme per se. The paper would be strengthened by equipping baseline PETL methods with a multi-scale feature extractor of comparable capacity (without HST's tuning innovations) to disentangle architecture from tuning method. *Note: this does not invalidate the classification results, which are fairly compared.*

2. **Empty "Efficiency Analysis" section (§4.6).** The paper includes the subsection heading "Efficiency Analysis" (line 376) but provides no content, figures, tables, or discussion. Efficiency (computational/memory cost, inference latency, training throughput) is a core motivation for PETL methods. HST's inference requires running both the frozen ViT backbone and the HSN (with multi-scale convolutions and cross-attention), so FLOPs likely exceed simpler PETL methods significantly. The absence of any efficiency data — even a basic FLOPs or latency comparison — leaves a critical gap in supporting the paper's efficiency claims. This is a structural omission in the main paper body (not a stripped appendix issue).

3. **Discrepancy in VTAB-1K full fine-tuning baseline inflates claimed improvement.** The paper reports full fine-tuning on VTAB-1K with ImageNet-21K pre-trained ViT-B at 65.57% average accuracy (line 199), citing Jia et al. (VPT, CVPR 2022). The VPT paper reports 68.9% for the identical configuration. The paper does not explain this 3.33% gap — whether it stems from a different pre-training checkpoint, training schedule, or data split. Since the headline result "outperforms full fine-tuning by 10.5%" (76.1% vs. 65.6%) is built on this baseline, the claim is not reliably established. Even with the VPT number (68.9%), the improvement would be 7.2% — still impressive — but the paper should clarify the discrepancy or rerun the baseline consistently. This concern applies to the *magnitude* of the claim, not the relative ranking among PETL methods (which uses consistent comparisons).

### Minor

1. **Abstract overclaims relative to full fine-tuning on dense tasks.** The abstract states HST "even surpassed full fine-tuning" on dense prediction tasks. However, on Mask R-CNN 1× with ViT-B, HST achieves 40.3 AP^b vs. full fine-tuning's 43.1 AP^b (a 2.8 gap), and on Mask R-CNN 3×+MS, the AP^b gap is 1.2 (Table 2). The paper acknowledges these gaps in the text (line 344–345) but the abstract does not qualify the claim. The "surpassing" result is specific to Cascade Mask R-CNN 3×+MS and certain semantic segmentation settings.

2. **HST is not the most parameter-efficient among PETL methods on dense tasks.** On Mask R-CNN 1× with ViT-B, HST uses 30.6M params vs. LoRA's 28.4M and SSF's 28.0M (Table 2). While still far below full fine-tuning (113.6M), the paper should explicitly acknowledge this trade-off rather than emphasizing parameter efficiency uniformly.

3. **LST discussion is superficial and lacks empirical comparison.** The related work (§2) mentions LST (Sung et al.) but only says "it has not been proven to be effective in vision models and initializing the side network poses a challenge." Since HST is essentially a vision-adapted hierarchical version of LST, the paper should explain how HST specifically overcomes LST's limitations and ideally include an empirical comparison (e.g., adapting LST to vision). This weakens the positioning of HST's novelty.

4. **Cosine similarity analysis (Fig. 3) lacks statistical rigor.** The paper shows cosine similarity between Meta-Register and image tokens across layers but does not specify whether this is averaged over multiple images or based on a single example. No error bars or variance information is provided. While LN tuning plausibly helps, the visual evidence is anecdotal.

5. **No analysis of why HST excels on specific VTAB-1K tasks.** On tasks like Clevr/count, dSprites/loc, and SmallNORB/ele, HST shows very large gains (≈3–7%) over the next-best PETL method. The paper notes this but offers no analysis of whether the side network's multi-scale inductive bias is responsible. This is a missed opportunity for insight.

6. **Different side network sizes for classification vs. dense tasks not discussed.** HSN dimensions are [32,48,64,72] for classification (0.78M params) and [64,128,256,384] for dense tasks (13.21M params). The paper should discuss whether a smaller HSN would suffice for dense tasks and what performance trade-off this entails, to clarify how much of the dense-task gain comes from added capacity.

### Trivial
None.

## Nice-to-Haves

- **Controlling for architectural capacity in dense prediction:** Implementing baseline PETL methods (LoRA, AdaptFormer, SSF) with an identical HSN attached to the frozen backbone but without HST's tuning innovations would disentangle architecture from tuning method.
- **FLOPs and inference time measurements** for all methods on at least one detection and one classification task.
- **Error bars / multiple seeds** on the main results (VTAB-1K, COCO) to establish statistical significance.
- **Qualitative detection/segmentation examples** (side-by-side predictions of HST vs. full fine-tuning vs. leading PETL baseline).
- **Ablation with smaller HSN on dense tasks** to explore the parameter-performance trade-off.

## Removed Points
*These are flagged for removal; treat them with caution.*

- **Missing training details (learning rates, batch sizes, optimizer, etc.):** The paper's appendix (stripped by the parser) likely contains these details. Per instructions, weaknesses about missing appendix content are removed.
- **Inference speed/memory measurements as a separate point:** Subsumed into the empty "Efficiency Analysis" weakness above.
- **"HST is not versatile because evaluation limited to four task families":** The paper covers classification, detection, instance segmentation, and semantic segmentation — four major vision task families. This is a reasonable scope.
- **Strength Finder strength about "state-of-the-art VTAB-1K accuracy":** Kept (it is valid). Only generic/superficial strengths from the Strength Finder were considered for removal; this one is concrete and well-supported.

## Novel Insights
None beyond the paper's own contributions. The core architectural insight — a hierarchical side network with linear-complexity cross-attention for parameter-efficient multi-scale feature fusion — is the paper's genuine contribution.

## Suggestions

1. **Fill the Efficiency Analysis section** with at minimum: FLOPs comparison (training + inference), peak GPU memory, and training/inference throughput for HST vs. the leading baseline and full fine-tuning on one classification and one detection task. This is the single highest-leverage addition.

2. **Clarify or rerun the VTAB-1K full fine-tuning baseline.** If the 65.57% number is from a different training recipe or checkpoint than VPT's 68.9%, explain this explicitly. Better yet, run full fine-tuning under consistent settings to establish a reliable baseline for the claimed 10.5% improvement.

3. **Disentangle architecture from tuning method for dense prediction.** Either (a) equip baseline PETL methods with an equivalent multi-scale side network (without HST's tuning innovations) and compare, or (b) explicitly reframe the contribution to acknowledge that HST's edge on dense tasks is a combined result of the side network architecture and the tuning scheme, and that the architecture itself provides a significant advantage.

4. **Qualify the abstract claim** about surpassing full fine-tuning to reflect that this holds on certain settings (Cascade Mask R-CNN 3×+MS, UperNet) but not universally (Mask R-CNN 1× shows a gap).

5. **Add error bars or multiple seeds** to the main results tables to establish statistical significance, especially for the VTAB-1K results where per-task variances could be meaningful.

## Score and Decision

### Calibration Anchors (batch retrieval results)

| Path | Avg Score | Comparison to HST |
|------|-----------|-------------------|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/bJx4iOIOxn.md` (VPT analysis) | 7.50 | Stronger analytical depth and more insights; HST is weaker in analysis but stronger in proposing novel architecture |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/YNbLUGDAX5.md` (ProPETL) | 6.00 | Similar-tier paper: both propose new PETL methods with strong results but have evaluation concerns; HST covers more tasks |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/vJkktqyU8B.md` (META) | 6.00 | Similar-tier paper: both address PETL for dense prediction; HST has stronger VTAB-1K results but META provides efficiency data HST lacks |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Fb93MfxX7T.md` (PETL survey) | 4.75 | HST proposes a novel method with stronger empirical contributions; clearly stronger |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/sOHVDPqoUJ.md` (SubTuning) | 4.00 | HST has clearer novelty and more comprehensive evaluation; clearly stronger |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/0Xc6o1HKXD.md` (test-time prompt tuning) | 3.67 | HST has far stronger methodology and results; clearly stronger |

**Relative positioning:** HST is stronger than the Reject-tier anchors (4.0–4.75) and comparable to Accept-tier anchors at ~6.0. It is weaker than the exceptional 7.5 anchor. The empty Efficiency Analysis section and the dense prediction fairness concern prevent it from reaching the high-6/low-7 range, but the genuine architectural contribution, thorough ablations, and strong classification results place it solidly in Accept territory.

This paper presents a genuinely novel architecture (hierarchical side network for ViT PETL) with carefully designed components and strong empirical results across multiple task families. The two major concerns — the uncontrolled dense-prediction comparison and the empty efficiency analysis — are addressable in revision. The paper's core contributions on classification are clean and independently convincing.

**Score:** 6.0

**Decision:** Accept

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>