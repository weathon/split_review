I've verified all the relevant text. Let me now produce the final consolidated review.

## Summary

This paper provides the first systematic study of test-time augmentation (TTA) for out-of-distribution (OOD) detection. It categorizes TTAs into In-Distribution Augmentations (IDA) and Out-of-Distribution Augmentations (OODA) using LPIPS, showing that only mild augmentations preserve InD score distributions. The proposed method performs a K-nearest-neighbor search on TTAs (sequential masks) instead of a training-data reference set, aiming for data-efficient, InD-independent OOD detection. Experiments on CIFAR-10 and ImageNet benchmarks are reported.

## Strengths

- **First systematic study of TTA's role in OOD detection with a principled categorization.** The paper classifies test-time augmentations into IDA and OODA using LPIPS and provides empirical evidence (Table 1, Figure 2, Table 2) that IDA preserves InD score distributions while OODA causes harmful shifts. This analysis is clean, practically useful, and goes beyond prior work focused on training-time augmentation. The LPIPS-based categorization itself is a reusable finding.

- **Data-efficient and genuinely InD-independent design.** The method performs KNN on generated TTAs without requiring a training-data memory bank, eliminating dependence on InD data quantity/quality (Figure 1). This makes it applicable when training data is unavailable or privacy-restricted. The approach works across architectures (ResNet, ViT, Swin) without model modification (Table 8), and the core method does not need OOD exposure or dataset-specific tuning unlike ASH (which requires different shaping algorithms for CIFAR-10 vs. ImageNet).

- **Extensive ablations providing practical guidance.** The paper systematically studies mask size (Figure 7), number of masks (Figure 5), k-value (Figure 8), source space (Figure 6), and TTA strategies (Table 7), showing graceful performance degradation and intuitive hyperparameter choices.

## Weaknesses

### Fatal
None.

### Major

- **Abstract/contribution framing overreaches relative to reported results.** The abstract claims the method "outperforms state-of-the-art methods using the entire training set (1.2 million images) on IMAGENET." However, Section 4.3 reports the method achieves 84.22% average AUROC while ASH-B (which does not use the training set as a reference) achieves 85.54%—the SOTA on ImageNet. The method is below ASH. The "outperforms" claim is only true for KNN and VIM (which use the training set as reference), but this qualification is absent from the abstract, title, and introduction. Readers will reasonably interpret it as a blanket claim. This framing issue undermines the paper's credibility and needs correction.

- **Missing experimental comparison to the most directly related prior work (He et al., 2022).** The paper cites He et al. (2022) as having "demonstrated that TTAs can be used for OOD detection" and claims to present "the first comprehensive study" of TTA for OOD detection, but never benchmarks against this existing TTA-based OOD method. This is a significant omission that weakens both the novelty claim and the empirical evaluation.

- **The KNN mechanism is not ablated against simpler alternatives.** The paper chooses the k-th largest cosine similarity among TTAs but never compares to using the mean, maximum, or median similarity (or even a single TTA with k=1 on ImageNet). The k-value ablation (Figure 8) shows a U-shaped curve but does not establish that k-th ranked similarity outperforms simpler aggregation. Without this control, it is unclear whether the KNN mechanism adds value beyond basic self-consistency measurement, and the "KNN" framing is not properly justified.

### Minor

- **On CIFAR-10, the improvement over simple baselines is marginal.** Per Table 1 (as described), horizontal flip alone achieves ~93.91% AUROC while the full method achieves 94.19%—an improvement of ~0.28%. While the margin is small, the paper does quantify the individual TTA contributions, which is appreciated.

- **ImageNet results do not report single-TTA baselines.** The paper does not report the performance of a single sequential mask (k=1) or a single horizontal flip on ImageNet, making it impossible to quantify the benefit of using multiple TTAs and KNN aggregation on the primary benchmark.

- **Inconsistency between Sections 4.3 and 4.6.** Section 4.3 reports the method's average AUROC on ImageNet as 84.22% with the optimal setup. Section 4.6 states "even when using the worst hyperparameter, our method achieves a performance of over 86% on IMAGENET, surpassing the SOTA (85.54%)." These numbers are difficult to reconcile: if the worst hyperparameter yields >86%, the optimal setup should be even higher, yet the reported average is 84.22%. The paper should clarify whether different OOD datasets, metrics, or evaluation protocols are used.

- **Robustness evaluation is preliminary.** The adversarial analysis (Table 6) is reported without error bars, attack strength parameters (ε), or statistical significance. The paper notes C&W causes a performance drop but does not quantify relative degradation compared to baselines.

- **Texture sensitivity is identified but not analyzed.** The paper notes poor performance on texture datasets but provides no analysis of why or what characterizes OOD data that is insensitive to masking.

### Trivial
- None that survive filtering.

## Nice-to-Haves

- Ablate k-th similarity against mean, max, and median similarity across TTAs to justify the KNN mechanism.
- Report single-TTA baseline performance on ImageNet (k=1 with sequential mask, or a single horizontal flip).
- Compare against He et al. (2022) experimentally, or clearly explain why comparison is infeasible.
- Report error bars or clarify the deterministic nature of the method and baselines.
- Specify attack parameters (ε) for robustness evaluations.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Central claim is directly contradicted by the paper's own results" (Harsh Reviewer Issue 1, part about KNN at 85.28%).** The reviewer claims Table 4 shows KNN at 85.28% on ImageNet, contradicting the paper's repeated claim of outperforming KNN. The number 85.28% does not appear in the paper text, and Table 4 is an image that cannot be read from the extracted text. The paper explicitly and repeatedly states it outperforms KNN. Absent verification, this specific numerical contradiction is treated as unsubstantiated. The *framing imprecision* is kept as a major weakness above.

- **"KNN on TTAs is not nearest-neighbor search in any meaningful sense; paper never acknowledges distinction" (Harsh Reviewer Issue 2).** The paper explicitly states: "Unlike KNN which performs a nearest neighbor search in the feature space of the entire training data, our approach focuses on searching within the local neighborhood of input samples provided by TTAs" (Section 3). Calling the method KNN on TTAs is reasonable and the paper clearly distinguishes it from training-set KNN. The missing ablation (vs. mean/max) is kept as a major weakness above.

- **"Contradictory statements about SimCLR in robustness" (part of Harsh Reviewer Issue 4).** The paper says SimCLR gives optimal average detection under attack but decreases clean OOD performance. These are two different measurements (adversarial vs. clean), not a contradiction—the paper is describing a trade-off.

- **"Method is not model-agnostic if combined with ReAct" (Harsh Reviewer Section 4.4 note).** ReAct is presented as an optional add-on in a separate subsection. The core method is model-agnostic.

- **Various formatting/style nitpicks and missing appendix/related work complaints** per the removal rules.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an angle or connection that the paper itself misses.

## Suggestions

1. **Fix the framing in the abstract and introduction.** Replace "outperforms state-of-the-art methods using the entire training set (1.2 million images)" with a precise claim such as "outperforms KNN and VIM that use the full training set as a reference, while approaching the performance of ASH (85.54%) without using any training data." The current wording overclaims and will harm credibility.

2. **Add the missing ablation of k-th similarity vs. mean/max/median similarity** across TTAs on both CIFAR-10 and ImageNet. This single ablation would either strongly validate the KNN design or reveal that simpler aggregation suffices.

3. **Report single-TTA baselines on ImageNet** (one mask, one horizontal flip) to quantify the benefit of multiple TTAs and KNN aggregation.

4. **Compare against He et al. (2022)** experimentally, or explain why the comparison is infeasible and how the methods fundamentally differ.

5. **Resolve the inconsistency** between Section 4.3 (84.22% average) and Section 4.6 (>86% with worst hyperparameter). Clarify which OOD datasets and evaluation settings are used in each.

6. **Add error bars or explicitly state that results are deterministic** given fixed random seeds, and specify attack parameters (ε) for the robustness evaluation.

## Score and Decision

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>