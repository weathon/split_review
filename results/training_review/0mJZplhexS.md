Now I have sufficient information to produce the consolidated review.

---

## Summary

This paper investigates scaling inefficiencies in image classifiers and proposes a simple two-pass inference algorithm: a lightweight "Little" model screens all samples, and a large "Big" model processes only low-confidence ones. The key insight—that scaled-up models disproportionately help on difficult/low-confidence samples—is supported by empirical analysis. The method achieves large MACs reductions (62–81%) across diverse architectures (EfficientNet, EfficientViT, DeiT3, InternImage) without modifying any model, and the operating point selected on ImageNet-1K transfers to ImageNet-ReaL and ImageNet-V2 with negligible accuracy loss.

## Strengths

- **Drastic compute reductions across diverse model families.** The paper reports MACs reductions of 76% for EfficientViT-L3-384, 81% for EfficientNet-B7-600, and 71% for DeiT3-L-384 on ImageNet-1K while maintaining top-1 accuracy, and 62% for InternImage-G-512 at 90% accuracy. These results are demonstrated across CNNs, transformers, and hybrid models at scales from 1 to 2700 GMACs (abstract, Section 4.3).

- **Model-agnostic design requiring no retraining or architecture modification.** The two-pass algorithm is a post-hoc method that pairs independently trained models, including cross-family pairs (e.g., an EfficientViT Little with a DeiT3 Big). This contrasts with pruning or adaptive-compute methods that require retraining and are often architecture-specific (Section 4.3, Table 1).

- **Well-motivated by empirical analysis of scaling behavior.** Section 3 systematically decomposes scaling benefits by confidence, showing that 90% of correctable mistakes fall below confidence thresholds of 0.47–0.67 across EfficientNet pairs. This directly motivates the confidence-based gating mechanism and provides a principled reason for the method's effectiveness.

- **Robust generalization of the selected threshold.** The optimal threshold T=0.24 identified for G_{B4,B7} on ImageNet-1K transfers to ImageNet-ReaL (0.04% accuracy drop) and ImageNet-V2 (0.07% drop). Moreover, selecting the threshold on the smaller ImageNet-V2 (10K samples) still achieves 78% MACs reduction on ImageNet-1K, demonstrating practical robustness (Section 4.2).

## Weaknesses

### Fatal
None.

### Major
- **No wall-clock latency or throughput measurements.** The paper centrally claims "speeding up" classifiers but evaluates only MACs—a theoretical compute proxy that does not capture memory I/O, model loading overhead, batch-size effects, or the routing/control logic between the Little and Big models. The two-pass design could introduce sequential dispatch overhead (the Little model's predictions must be computed before deciding whether to invoke the Big model), potentially reducing or negating theoretical speedups in practice. While MACs are standard in the compression literature, a paper that frames itself around "speeding up" and "practical method for large model compression" (abstract) needs at least representative wall-clock timings on target hardware (e.g., GPU/CPU). The limitations paragraph (Section 7) discusses storage/memory trade-offs but provides no empirical latency data. This is the most significant gap in the evaluation.

### Minor
- **The "lossless accuracy" claim is slightly overstated.** The abstract claims "without loss of accuracy," and Section 4.3 says "without any loss of accuracy." The threshold selection procedure (Section 4.2) is designed to match the Big model's accuracy on ImageNet-1K validation by construction (setting ΔAcc ≥ 0), so the claim holds on the primary benchmark. However, on the generalization datasets (ImageNet-ReaL, ImageNet-V2), drops of 0.04% and 0.07% are reported. While these are tiny, the paper does not report whether these differences are within the noise floor of the benchmark (e.g., via bootstrap confidence intervals or McNemar's test). A more precise framing—e.g., "without measurable accuracy loss on ImageNet-1K"—would better match the evidence.

- **The comparison with prior compression methods is contextual rather than controlled.** Table 9 compares Little-Big's accuracy–MACs trade-offs with published pruning methods (WDPruning, X-Pruner, SPViT), but the baselines for these methods are not the same Big models being compressed. For instance, SPViT-DeiT-B is compared against DeiT3-S (a different, better-trained baseline). The paper's argument—that many pruning methods fail to outperform better-trained small models—is valid and interesting, but this does not constitute a controlled comparison on the same Big model. A direct experiment (e.g., applying structural pruning to EfficientNet-B7 to match the MACs budget of G_{B4,B7} and comparing accuracies) would make the comparison more compelling.

- **Confidence-as-hardness proxy is only verified on EfficientNet.** The analysis in Section 3, which establishes that correctable mistakes have low confidence, uses only the EfficientNet family. While the method empirically works across other families (shown in Table 1), the paper does not verify calibration quality (e.g., expected calibration error) or confirm that the confidence–hardness relationship holds for ViTs or hybrid architectures. A brief calibration analysis for the Little models used would strengthen the theoretical grounding.

### Trivial
- The paper uses "speeding up" and "MACs reductions" nearly interchangeably in several places (abstract, Section 4.3), but MACs and speed are not identical. Clarifying the distinction would prevent misinterpretation.

## Nice-to-Haves
- Evaluation on datasets with stronger distribution shift (e.g., ImageNet-A, ImageNet-R, ImageNet-Sketch) to test whether the threshold selected on ImageNet-1K generalizes to out-of-distribution scenarios.
- A small-scale proof-of-concept for extending the method to semantic segmentation or video classification, as suggested in the extensions paragraph.
- Visualizations of examples that the Little model predicts with low confidence but the Big model corrects, to qualitatively illustrate the hardness decomposition.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Missing related work on early-exit networks (BranchyNet, MSDNet).** Removed per policy: the reviewer cannot independently verify whether these citations were present in the original submission or are relevant; the paper does discuss adaptive computation mechanisms conceptually (Section 2.3).

- **"Confusing T=0 statement" about replacement.** The critic found the paper's statement about T=0 being a trivial replacement case confusing. The paper's logic is correct—if the Little model already outperforms the Big model, optimal strategy is replacement. This is a natural edge case, not an error. Removed.

- **Rounding of "0.00%" accuracy drops.** The critic speculates about rounding artifacts without evidence. The accuracy numbers are in figures (not text) and cannot be verified. Removed.

## Novel Insights

The key insight that emerges from the reviews more clearly than from the paper alone is the following tension: the method is embarrassingly simple (a thresholded cascade of two independently trained classifiers), yet achieves Pareto-dominating accuracy–MACs trade-offs compared to sophisticated pruning and adaptive-compute methods that require retraining. This suggests that the community may have been over-investing in complex compression techniques for problems that can be solved by better exploiting the confidence calibration of existing models. However, the strength of this insight is tempered by the indirectness of the comparison (pruning methods operate on weaker baselines) and the absence of latency validation. A direct latency comparison on the same hardware would either confirm that this simple approach is genuinely faster in practice—which would be a significant practical finding—or reveal that MACs savings do not translate to real speedups, which would limit the method's applicability.

## Suggestions

1. **Add wall-clock latency measurements** on GPU (and optionally CPU) for the primary G_{B4,B7} pair vs. running EfficientNet-B7 alone. Report throughput (images/second) for batch sizes 1, 16, 64. This is the single most important addition to support the "speeding up" claim.

2. **Run a controlled comparison** with a pruning method applied to the **same Big model**. E.g., apply structural pruning to EfficientNet-B7 to achieve a MACs budget comparable to G_{B4,B7}(T=0.24), then compare accuracies.

3. **Provide statistical significance** for the accuracy differences reported as "lossless." A bootstrap confidence interval or McNemar's test on the 50K validation set would show whether the tiny differences (0.04%, 0.07%) are within expected noise.

4. **Report ECE** for the Little models used, to validate that confidence is a reliable hardness surrogate for each model family.

## Score and Decision

**Originality:** The two-pass cascade idea itself is not novel (early-exit networks, cascade classifiers), but the paper's specific contribution—showing that off-the-shelf pretrained models can be paired this way, with a detailed analysis of *why* it works—has genuine value.

**Importance of research question:** The question of whether scaling compute is worthwhile for marginal accuracy gains is practically important, and the paper offers a useful perspective.

**Claims supported:** The core claim (large MACs reduction without accuracy loss on ImageNet-1K) is supported. However, the practical "speeding up" claim is under-evidenced (MACs only), and the "lossless" framing is slightly overstated.

**Soundness of experiments:** Generally solid for the main results across many architectures. The comparison with prior work is indirect. Missing latency measurements.

**Clarity of writing:** Clear and well-structured. The motivation and method are easy to follow.

**Value to community:** Moderate. The method is simple enough to be immediately useful, and the analysis of scaling inefficiency is instructive.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>