Now I have a thorough understanding of the paper and all reviewer claims. Let me produce the final consolidated review.

---

## Summary

ProtoReg introduces a regularization method for fine-grained transfer learning that addresses the "granularity gap"—the mismatch between coarse pre-trained features and the fine-grained discriminative details needed for downstream tasks. The method initializes class-discriminative prototypes (via feature means or linear probing weights) and uses aggregation and separation losses to pull features toward their correct prototype while pushing them away from others, with prototypes refined during training. Experiments on four fine-grained benchmarks show average gains of 6.4% over standard fine-tuning (13.4% with only 15% training data), and strong OOD robustness on Waterbirds.

## Strengths

- **Large and consistent gains across multiple fine-grained benchmarks**: ProtoReg (LP) achieves substantial margins over seven transfer learning baselines across four datasets and four sampling rates (Section 5.2, Table 1). For example, 11.88% improvement over CE on FGVC Aircraft at 100% sampling, and the pattern is consistent across all settings, not just one favorable configuration.

- **Exceptional limited-data performance directly validates the granularity gap motivation**: At 15% training data—where the paper argues overfitting to non-discriminative information is most severe—ProtoReg achieves 13.4% average improvement over CE, and outperforms the next-best method by 8.73% on Stanford Cars (Section 5.2, Table 1). This ties the empirical result directly to the paper's core thesis.

- **OOD robustness confirms genuine class-discriminative feature learning**: On Waterbirds, ProtoReg shows only a 10% accuracy drop from in-distribution to OOD at 100% sampling (vs. 24% for CE), and only 19% at 15% sampling (vs. 49% for CE and 32% for the best-compared method) (Section 5.3, Table 2). This directly validates that ProtoReg prioritizes object-discriminative features over background correlations.

- **Ablation study cleanly isolates each component's contribution**: Table 4 (Section 5.5) shows aggregation alone yields +4.92%, adding prototype refinement raises to +8.70%, and adding separation loss pushes to +9.24%—confirming each design choice contributes positively and as intended.

- **CKA analysis and prototype-accuracy correlation provide mechanistic evidence**: Figure 4 (Section 5.4.1) shows ProtoReg produces substantial representation shifts in intermediate layers (unlike CE which only changes the penultimate layer), and Figure 6 (Section 5.4.3) reports a Pearson correlation of 0.92 between initial prototype discriminativeness and final accuracy.

- **Early-stage regularization matters most (Section 5.4.4, Table 3)**, consistent with the paper's framing that preventing initial overfitting to non-discriminative information is critical.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Single architecture and single pre-training paradigm**: All experiments use ResNet-50 pre-trained on ImageNet-1K. The method's generality to other architectures (ViT, ConvNeXt) or pre-training paradigms (self-supervised, CLIP, DINOv2) is not demonstrated. The paper claims to address the granularity gap as a general problem in transfer learning but provides no evidence that ProtoReg transfers across different architectural inductive biases or pre-training distributions.

- **No variance or statistical significance reporting**: All results in Table 1 are single numbers without error bars, confidence intervals, or indication of the number of independent runs. While single-run evaluation is common in the cited baselines, the absence of variance information makes it impossible to assess whether the reported margins over the best competing methods are stable or could arise from random seed variation.

- **Absence of FGVC-specific method discussion**: The paper is framed around fine-grained transfer learning and the granularity gap, yet does not discuss or compare against any methods from the FGVC literature (e.g., part-based models, bilinear pooling, TransFG, PMG). While ProtoReg is a regularization technique and architectural differences make direct comparison non-trivial, the paper should at minimum explain why such comparisons are out of scope and discuss how ProtoReg relates to these approaches.

- **Ambiguity in classifier initialization for ProtoReg (LP)**: Section 4.2 states the classifier is randomly initialized for the mean-based variant but does not clearly specify whether the classifier in ProtoReg (LP) is initialized from the linear probing weights or randomly. This matters because the comparison between LP-FT (LP-initialized classifier + CE fine-tuning) and ProtoReg (LP) in Table 1 cannot be cleanly interpreted as isolating the regularization effect without knowing this detail. If the classifier in ProtoReg (LP) is randomly initialized, the comparison conflates initialization and regularization benefits.

- **General dataset results not reported**: The experimental setup (Section 5.1) lists Caltech101 and CIFAR100 among the six evaluation datasets, but Table 1 is described as covering only "the four benchmarks" (fine-grained). The paper does not discuss whether ProtoReg improved, matched, or underperformed on general tasks—information that would clarify whether the method is specifically beneficial for fine-grained tasks or more broadly applicable.

- **t-SNE claims lack quantitative backing**: Section 3's claim that pre-trained features show "comparable degree of class separation" to random features rests solely on visual inspection of t-SNE plots. Quantitative separability measures (e.g., nearest-neighbor accuracy, linear probe accuracy, silhouette score) would substantially strengthen the motivational observations.

### Trivial

- The memory bank storage cost for ProtoReg (self)—storing features for all training samples per epoch—is not discussed, which could be prohibitive for large-scale datasets.

## Nice-to-Haves

- A version of the ablation that starts from LP initialization and adds ProtoReg components (mirroring the ProtoReg (LP) setting) would cleanly isolate the regularization benefit from the initialization benefit, complementing the implicit LP-FT vs. ProtoReg (LP) comparison already present in Table 1.
- Validation on at least one additional backbone (e.g., ViT-B/16) on a subset of benchmarks would substantially strengthen claims of generality.
- Quantitative class separability metrics to back the t-SNE-based claims in Section 3, as noted above.

## Removed Points

These points from the inputs were filtered according to the review-merging guidelines:

- **"No FGVC method comparison as Major weakness"**: Demoted from Major to Minor. The paper is a transfer learning regularization method, and the baselines (L2-SP, BSS, SN, Co-tuning, LP-FT, Robust FT, DR-Tune) are appropriate for this framing. FGVC methods involve architectural modifications that would introduce confounders. The criticism is valid as a request for discussion/context but does not constitute a structural flaw threatening acceptance.

- **"LP initialization conflation as structural weakness"**: Removed as a standalone point because the comparison already exists implicitly: LP-FT (LP initialization + CE fine-tuning) vs. ProtoReg (LP) (LP prototypes + ProtoReg losses) is present in Table 1. The paper does not frame it as such, but the data is available. The genuine underspecification issue (classifier initialization in ProtoReg (LP)) is retained as a Minor weakness above.

- **Criticism about prototype refinement underspecification**: Section 4.3 clearly states prototypes "are set to be learnable and refined through backpropagation while optimizing Eq 7." Since prototypes appear only in L_aggr and L_sep, they receive gradients from those losses. This is sufficiently specified.

- **Typos, formatting, style nitpicks**: These are parser-induced artifacts, not author errors.

- **Missing related works**: The reviewer does not have access to external sources to verify whether specific works are missing.

- **Missing appendix/proofs**: These sections are stripped by the parser; they exist in the original submission.

## Novel Insights

Beyond the paper's own contributions, the reviews reveal a productive tension: ProtoReg achieves empirically impressive gains (6–13% improvements, strong OOD robustness) that are rare in the transfer learning regularization literature. Yet the single-backbone evaluation and the absence of FGVC-specific comparisons leave an open question about scope—is ProtoReg solving a problem unique to ImageNet-pretrained ResNet-50 on fine-grained tasks, or does it represent a more general principle? The Waterbirds experiment is the strongest evidence for the latter interpretation. A particularly revealing follow-up would be testing whether ProtoReg's benefits persist when pre-training data already contains fine-grained structure (e.g., a ViT pre-trained on ImageNet-21K or a CLIP model), which would directly test the granularity gap hypothesis: if the gap is small, the regularizer should contribute less.

## Suggestions

1. **Clarify classifier initialization in ProtoReg (LP)**—specify whether the fine-tuning classifier is initialized from the LP weights or randomly, and discuss how this affects interpretation of comparisons with LP-FT.
2. **Report error bars** (at least 3 runs with standard deviation) for the main results in Table 1.
3. **Discuss ProtoReg's relationship to FGVC-specific methods**—even a brief note explaining why architectural comparisons are not made would clarify the paper's positioning.
4. **Add results on Caltech101 and CIFAR100** to clarify whether ProtoReg is specifically beneficial for fine-grained tasks or generalizes to non-fine-grained classification.
5. **If space permits, validate on at least one additional backbone** (e.g., ViT-B/16) on the most informative benchmark (e.g., FGVC Aircraft at 15% and 100% sampling).

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>