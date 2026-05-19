- Decision: Reject
- Avg Score: 4.75
- Scores: 8, 5, 3, 3
Now I have all the information needed to produce a thorough, verified final review.

## Summary

This paper introduces MetaDD, a method for improving cross-architecture generalization in dataset distillation. The core idea is to decompose distilled data features into "meta features" (common across architectures, measured via CAM overlap) and "heterogeneous features" (architecture-specific), then use a CAM variance loss combined with architecture-invariant and positivity losses to amplify meta features. Experiments on CIFAR-10, Tiny-ImageNet, and ILSVRC-2012 with four DD methods (DC, DM, MTT/TesLa, Sre2L) show consistent improvements over GLaD and ModelPool baselines, with substantially lower memory overhead.

## Strengths

1. **Well-motivated empirical analysis**: The CAM-based visual analysis (Figure 1) showing that original datasets have substantially more cross-architecture CAM overlap than distilled datasets directly motivates the problem. The erasing experiment (Section 3.2, Figure 3) further validates that heterogeneous and meta features have measurably different effects on different architectures. This grounding is stronger than typical for the area.

2. **Consistent cross-architecture accuracy gains**: Across all three datasets and four DD methods, MetaDD (listed as MetaCAM in some tables) consistently outperforms GLaD and ModelPool. For example: on Tiny-ImageNet with DM (IPC=50), MetaDD achieves 13.5% average vs. GLaD's 11.9% (Table 1 bottom subtable); on ILSVRC-2012 with TesLa, MetaDD achieves 13.1% average vs. GLaD's 12.1% (Table 1 top subtable). The gains hold for both seen (auxiliary) and unseen architectures.

3. **Practical memory efficiency**: Table 3 shows MetaDD adds ~3GB on CIFAR-10 (22.6 GB vs. GLaD's 39.1 GB) and ~8GB on ILSVRC-2012 (76.4 GB vs. GLaD's 119.1 GB), while being faster. This is a genuine practical advantage over generator-based methods.

4. **Ablation confirms the core mechanism**: Table 4 shows the variance loss provides the largest gain (MTT: 52.1→52.9; Sre2L: 59.8→60.4), confirming that the technical novelty is the primary driver of improvement, with $L_{ai}$ and $L_{pos}$ contributing smaller increments.

## Weaknesses

### Fatal

- **Unsupported headline claim in the abstract**: The abstract states: *"On the Distilled Tiny-Imagenet with Sre2L (50 IPC), MetaDD achieves cross-architecture NN accuracy of up to 30.1%, surpassing the second-best method (GLaD) by 1.7%."* **This claim does not appear in any table in the paper.** The Tiny-ImageNet experiments (Table 1 bottom subtable) only report results for DC and DM — not Sre2L. The highest cross-architecture accuracy reported for Tiny-ImageNet is 15.1% (DM+MetaDD on Swin-S). The 30.1% figure is completely unsubstantiated by the presented evidence. Even if results exist in a stripped appendix, the main paper must support its headline claim; the absence of any reference or trace of Sre2L Tiny-ImageNet results in the main experimental section makes this a serious integrity issue. This must be corrected by either removing the claim or presenting the supporting evidence.

### Major

- **The mechanism is not quantitatively validated**: The paper defines meta features as the binary overlap of thresholded CAMs (Equation 1: values ≥ 0.5 across all architectures). The optimization, however, minimizes the *variance of raw normalized CAM values* (Equation 7/var), which is related to but not equivalent to maximizing the overlap mask. There is **no quantitative measurement** showing that MetaDD actually increases the meta-feature overlap ratio (the percentage of pixels in the meta-feature mask). The paper only shows visual examples (Figure 5) and uses downstream accuracy as indirect evidence. The ablation study (Table 4) tests the loss components but does not track meta-feature coverage. Directly measuring whether the overlap increases would validate the claimed mechanism and rule out the possibility that the method works through a different, unexamined channel.

### Minor

- **Same-architecture accuracy is not reported**: The paper only reports cross-architecture results. If MetaDD degrades accuracy on the same architecture used for distillation (the backbone), the method's utility is limited. This is a straightforward control that should be added.

- **No statistical assessment of improvement significance**: The gains are typically 0.5–2 percentage points, and many individual architecture comparisons have overlapping error bars (e.g., ILSVRC-2012 Sre2L on ViT-B-16: GLaD 14.6±1.2 vs. MetaDD 14.2±0.4). While the *pattern* of consistent improvement across architectures is compelling, the paper would benefit from a paired sign test, Wilcoxon, or bootstrapped confidence intervals across the 8 architectures to show the improvement is systematic.

- **Naming inconsistency**: The method is called "MetaDD" in the title/abstract and the main tables, but the CIFAR-10 table, memory/time table, and figure captions use "MetaCAM." Standardize for clarity.

### Trivial

- The justification for the KL divergence term in the architecture-invariant loss (Section 3.3) is opaque: *"architecture-invariant loss maximumly displays heterogeneous features antagonistic to the main NN, which will be transferred to meta features."* The reasoning for why KL divergence specifically generates diverse CAMs is not explained clearly.
- The average for DC+MetaDD on Tiny-ImageNet (Table 1 bottom) is listed as 13.8%, but the individual values (13.6, 14.1, 14.7, 14.7, 13.8, 14.9, 12.6, 13.7) average to ≈14.0%. While a small discrepancy, it suggests possible rounding inconsistencies.

## Nice-to-Haves

- Ablation on the number of auxiliary architectures (2 vs. 4 vs. 6) to test whether "contagious generalizability" scales.
- Sensitivity analysis on the 0.5 CAM threshold used to define meta features.
- Ablation on larger datasets beyond CIFAR-10.

## Removed Points

- **"Per-sample loop is computationally heavy and not clearly accounted for"** (Harsh Critic Section 3): The algorithm clearly presents the loop structure, and the runtime analysis (Table 3) shows only modest overhead, which the reviewer themselves acknowledges is *"plausible."* No concrete evidence contradicts the reported costs. Removed as speculative.

- **"KL divergence justification is opaque / undermines theoretical grounding"**: Demoted to Trivial. The explanation is somewhat unclear but does not undermine the method; the empirical results validate the approach regardless of the theoretical justification's polish.

- **"No CIFAR-10 or Tiny-ImageNet results for Sre2L"** (as applied to the unsupported claim): CIFAR-10 Sre2L results DO appear in Table CIFAR-10. Only Tiny-ImageNet Sre2L results are missing. Merged into the Fatal weakness above.

- **"No discussion of failure cases"**: This is a generic request applicable to any paper; not specific enough to retain as a weakness.

- **Strength about "empirical motivation via CAM analysis"**: Already incorporated above; kept.

- **Strength about "novel feature decomposition"**: Already incorporated.

- **Strength about "contagious generalizability to unseen architectures"**: Already incorporated.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Fix the abstract**: Remove or substantiate the 30.1% Tiny-ImageNet Sre2L claim. Replace it with a supported number (e.g., the best CIFAR-10 Sre2L result of 61.2% on unseen architectures, or the average Tiny-ImageNet gains over GLaD reported in the introduction).
2. **Quantify meta-feature ratio**: Compute and report the percentage of meta-feature pixels (Equation 1) before and after MetaDD across a sample of images. This directly validates whether the loss achieves its stated goal.
3. **Report same-architecture accuracy**: Add a column to the main tables showing backbone-architecture accuracy to verify no degradation.
4. **Add a simple statistical test**: A paired sign test or Wilcoxon across the 8 architectures in each table would significantly strengthen the claim of systematic improvement.
5. **Standardize naming**: Use "MetaDD" consistently throughout.
