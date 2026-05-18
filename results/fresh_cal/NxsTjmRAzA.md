Now I have everything I need. Let me produce the consolidated final review.

## Summary

This paper presents the first systematic study of test-time augmentations (TTAs) for OOD detection, categorizing them into In-distribution Augmentations (IDA) and Out-of-distribution Augmentations (OODA) based on their effect on image features. Building on the finding that mild (IDA) augmentations produce distinguishable feature differences between InD and OOD data, the authors propose a detection method that performs KNN search on TTAs (sequential masks) of the input sample rather than on the training dataset. The method is InD-independent, model-agnostic, and claims strong data efficiency — with as few as 25 TTAs matching or exceeding the performance of reference-set-based methods.

## Strengths

1. **First systematic study of TTA's effect on OOD detection.** Section 2 provides a principled categorization of test-time augmentations into IDA and OODA, supported by LPIPS measurements (Table 2), distribution analysis (Figure 2), and Grad-CAM visualizations (Figure 3). This analysis is a genuine conceptual contribution that goes beyond prior work focused solely on training-phase augmentation.

2. **Data efficiency of the proposed method.** Even setting aside the contested 1.2M comparison, the method demonstrates strong data efficiency: 25 TTAs achieving competitive results with a method (KNN) that requires orders of magnitude more reference data (200k training images on ImageNet). The method is also InD-independent, avoiding the data quantity/quality dependencies that affect KNN and VIM (Figure 1).

3. **Robustness to adversarial attacks.** Table 6 shows that under FGSM and PGD attacks, the proposed method maintains high AUROC (e.g., 90.05% and 89.70% with sequential mask), while baselines like MSP, Energy, and ODIN collapse to near-chance performance. The authors honestly report weaknesses against C&W attacks.

4. **Model-agnostic and broadly applicable.** Table 8 demonstrates consistent improvements across ResNet-50, DenseNet-121, ViT-B/16, and Swin-B architectures without model-specific tuning, showing broad applicability.

5. **Compatible with existing post-hoc methods.** Section 4.4 shows that integrating with ReAct yields further gains (from 84.22% to 85.58% average AUROC on ImageNet), demonstrating the contribution is orthogonal to activation-rectification approaches.

## Weaknesses

### Fatal
None. The paper's core claims (TTAs can serve as a data-efficient proxy for reference sets in KNN-based OOD detection) are not invalidated by any single verified issue.

### Major

- **Internal contradiction about KNN's reference set size on ImageNet.** The abstract, Figure 1 caption, and Section 4.3 (line 126) repeatedly claim that KNN uses "the entire training set (1.2 million images)" and that "25 TTAs outperform KNN with 1.2 million images as a reference set." However, Section 4.1 (line 105) states: *"VIM and KNN require 50,000 and 200,000 InD data on CIFAR-10 and IMAGENET, respectively."* This means the KNN baseline on ImageNet was evaluated with 200k images, not 1.2M. The paper never reports KNN's performance with the full 1.2M training set. This is a clear internal inconsistency that undermines the paper's headline claim. The authors must (a) clarify the discrepancy or run KNN with the full 1.2M, and (b) recalibrate any claims that depend on this comparison. Note: this does not invalidate the method's data efficiency (25 vs 200k is still impressive), but the paper's own framing is misleading.

### Minor

- **Hyperparameter selection (mask size, number of masks) not validated on held-out ID data.** Section 4.6 selects the "optimal" mask size and number of masks by evaluating performance across the six OOD test datasets (Figure 7). No validation procedure isolating hyperparameter selection from the test OOD distributions is described. While the paper does show robustness evidence ("even the worst hyperparameter achieves..."), the reported results may represent an optimistic upper bound. The authors should mask selection using only ID validation data and report both validation-chosen and test-optimal results.

- **Sequential mask procedure underspecified for reproducibility.** Section 3 (line 66) describes sequential mask as "applies masks to images in a sequential manner, generating a substantial number of similar IDAs" but never specifies how the masks are spatially arranged — sliding windows with stride? random placement? overlapping? With what stride? How do the number of masks (16 for CIFAR-10, 25 for ImageNet) relate to mask size and image dimensions? Every experimental result depends on this procedure, yet it cannot be reproduced from the description alone. A pseudocode or explicit mask-grid specification is needed.

- **Confusing claim about worst-hyperparameter performance.** Section 4.6 (line 154) states: *"even when using the worst hyperparameter, our method achieves a performance of over 86% on IMAGENET, surpassing the SOTA (85.54%)."* Yet Table 4 reports the method's average AUROC as 84.22%, which is *below* the SOTA of 85.54%. If the worst hyperparameter gives >86%, the numbers are inconsistent. This likely reflects a difference in what is being averaged (e.g., a subset of OOD datasets vs. the full 6-dataset average), but the text does not clarify this. This needs clarification.

- **Imprecise claim about SOTA gap.** Section 4.3 (line 124) says the method is *"only 2 percentage points below the SOTA performance of ASH."* ASH-B achieves 85.54% and the method achieves 84.22%, a gap of 1.32 points, not 2. Small but should be precise.

### Trivial

- The LPIPS analysis (Table 2) is used to quantify "mildness" of augmentations, but LPIPS itself is trained on ImageNet and is not an objective perceptual measure for all image types, especially OOD data. The paper notes an exception (grayscale) but does not discuss this limitation. Minor caveat.

## Nice-to-Haves

- **Inference cost analysis.** The method requires 16 or 25 forward passes per test sample. A discussion of FLOPs or wall-clock time relative to single-pass methods (MSP, Energy, ASH) would help practitioners assess the trade-off.
- **Intuition for k-th neighbor choice.** The paper shows k=2 or 4 works best (Figure 8) but does not explain why the k-th largest similarity is more robust than the maximum or average. Providing intuition (e.g., robustness to a single anomalous TTA) would strengthen the methodological contribution.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh critic's claim that "The KNN paper (Sun et al., 2022) uses the full training set; performance typically improves with more reference data."** This is an external claim about another paper that cannot be verified from this paper alone. Removed as speculative. The *internal* contradiction (paper says 200k in §4.1 but 1.2M elsewhere) is retained as a verified weakness.
- **Harsh critic's "structural flaw" label and "core claim collapses" rhetoric.** The method's data efficiency (25 vs 200k) still holds; the core contribution does not collapse. Reframed from "fatal" to "major" after verification.
- **Strength Finder's claim that "with only 25 TTAs, the proposed method outperforms KNN and VIM, which require the entire 1.2-million-image ImageNet training set."** This repeats the contested 1.2M framing from the paper's abstract rather than the 200k stated in §4.1. Retained as a strength but qualified.
- **Strength Finder's claim about "worst hyperparameters on ImageNet achieve >86% AUROC... surpassing previous SOTA."** This repeats the confusing and potentially inconsistent claim from the paper. Retained as a weakness (needs clarification) rather than a strength.
- **Harsh critic's claim about "ASH achieves higher AUROC (85.54 vs 84.22) on ImageNet" as downplaying the contribution.** The paper openly reports this comparison; the critic's framing is not a weakness of the paper.
- **Generic strengths from Strength Finder about "addressed an important problem" — removed as generic/superficial.**
- **Typo/formatting nitpicks** from both reviews — removed as parser artifacts.

## Novel Insights

Beyond the paper's own contributions, the reviews do not surface genuinely novel observations that the paper itself missed. The IDA/OODA categorization and the finding that masking yields the mildest augmentation (lowest LPIPS) are already in the paper. The adversarial robustness analysis is a clear strength that the paper already highlights.

## Suggestions

1. **Resolve the KNN data size contradiction.** Either run KNN with the full 1.2M ImageNet training set (you have access, since you use a pre-trained ResNet50) or explicitly explain in the main text why 200k was used and adjust all claims accordingly. If KNN with 1.2M performs comparably or better, reframe the contribution around data efficiency and InD-independence rather than "outperforming 1.2M with 25."

2. **Specify the sequential mask procedure** with a pseudocode or explicit grid specification: mask stride, overlap, spatial ordering, and how the number of masks relates to mask size and image dimensions.

3. **Clarify hyperparameter selection.** Describe a clean validation protocol (e.g., held-out ID validation data) for mask size and number of masks. Report both the validation-chosen and test-optimal configurations to show sensitivity.

4. **Clarify the >86% claim.** Explain what metric is being reported in Figure 7 and why the worst-hyperparameter performance (stated as >86%) differs from the Table 4 average (84.22%).

5. **Report computational cost** (inference time or FLOPs) for the method vs. single-forward-pass baselines.

## Score and Decision

The paper makes a genuine contribution: the first systematic study of TTA's effect on OOD detection, a clean IDA/OODA categorization, and a novel method that uses TTAs as a data-efficient reference set. The CIFAR-10 experiments are sound, the adversarial robustness analysis is strong, and the method is demonstrated across multiple architectures. 

The primary weakness is an internal contradiction about the KNN baseline's reference set size on ImageNet (200k stated in §4.1 vs. 1.2M claimed in the abstract and elsewhere). This damages the headline claim but does not collapse the paper's core contribution — the method's data efficiency and ID-independence remain even against 200k. The sequential mask procedure is underspecified, hyperparameter selection needs clearer validation, and one ablation claim (86%) appears inconsistent with the main results.

With a clear resolution of the KNN data size issue, a detailed specification of the masking procedure, and clarification of the inconsistent numbers, the paper would be a solid contribution. As-is, these issues prevent acceptance.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>