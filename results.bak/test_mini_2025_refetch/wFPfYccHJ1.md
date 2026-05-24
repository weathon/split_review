Now I have a good picture of the calibration landscape. Let me synthesize the final review.

**Round 1 bracket:** The paper is clearly above weak anchors (<3.5) — those papers had fundamental methodological issues or were clearly preliminary. It is also clearly below the strong anchors (>7.5) — those are exceptional works with clean, thorough evaluations and no significant comparison concerns. **Initial bracket: [3.5, 7.5]**

**Round 2 narrowing:** Comparing against anchors in (4.5, 7.5):
- SCALE (6.25, accepted): cleaner benchmarking, more incremental contribution → ABeT is similar quality but different tradeoffs
- SMOT (5.75, rejected): limited gains, comparison concerns → ABeT is slightly stronger
- Imbalanced OOD (5.75, rejected): strong theory but scope concerns → ABeT addresses a broader problem
- Feature Separation/NC (6.75, accepted): robust evaluation, stronger experiments → ABeT is clearly weaker
- Image Background (5.33, accepted poster): strong results but some concerns → comparable quality

The paper sits between ~5.5 and ~6.0. The backbone mismatch on ImageNet and thin OD evaluation pull it down, while the genuinely novel contribution and clean ablation on CIFAR keep it from being lower.

**Final score: 5.5** — borderline, genuine contribution but with weaknesses that need addressing.

---

## Summary

This paper proposes Ablated Learned Temperature Energy (ABeT), a method that combines a learned temperature (Hsu et al., 2020) with the energy score (Liu et al., 2020) and then ablates a term the authors identify as counterproductive (the "Forefront Temperature Constant"). The core insight — that one of the two ways the learned temperature appears in the energy formula contradicts the desirable OOD detection property — is clean and well-motivated. ABeT is evaluated on classification (CIFAR-10, CIFAR-100, ImageNet-1k), semantic segmentation (Cityscapes → LostAndFound/RoadAnomaly), and object detection (PASCAL VOC → COCO).

## Strengths

- **Genuinely novel and well-motivated contribution**: The identification of the "Forefront Temperature Constant" as harmful and its ablation is the strongest part of the paper. The derivation from Equation 2 to Equation 3 is logically sound, and the ablation study (Section 4.2) directly validates this contribution, showing FPR@95 reductions of 28.76%, 59.00%, and 24.81% from the ablation alone on CIFAR-10, CIFAR-100, and ImageNet respectively. This is not an incremental tweak; it is a genuine analytical insight.

- **Strong and consistent results on CIFAR where comparisons are fair**: On CIFAR-10 and CIFAR-100 (where all baselines use the same ResNet-20 backbone), ABeT achieves clear improvements. For example, on CIFAR-10, ABeT achieves FPR@95 of 12.5 ± 2 vs. the best prior same-backbone method (Energy+ASH) at 20.0 ± 21. The standard deviations are also notably lower, indicating consistent performance across OOD datasets. The ablation study quantifies the isolated benefit of the Forefront Temperature Constant removal.

- **Simple, low-overhead method**: ABeT requires only a single-line architectural change (adding a learned-temperature layer and cosine-logit head), trains with standard cross-entropy on ID data only, needs no OOD exposure data, no multi-stage training, and no hyperparameter tuning. This practical simplicity is a genuine advantage over methods requiring OOD synthesis or multi-stage pipelines.

- **Extension to segmentation and detection**: The paper demonstrates ABeT's applicability beyond classification — on LostAndFound (semantic segmentation), ABeT reduces FPR@95 from 15.56 (Max Logit) to 3.42. On object detection, it improves AUROC from 60.65 (baseline) / 60.46 (VOS) to 65.34. This breadth strengthens the claim that the idea is general.

## Weaknesses

### Fatal
None.

### Major

- **Comparison fairness on ImageNet is partially compromised**: Two key baselines on ImageNet — Energy+ReAct (FPR@95=31.4) and Energy+DICE (FPR@95=34.7) — are reported from their original papers using ResNet-50, while ABeT uses ResNetv2-101. The paper transparently acknowledges this with an asterisk and the statement "This is due to our inability to reproduce their results with ResNet-101." This means the reader cannot determine how much of the reported improvement is due to the method vs. the larger backbone. Since these are competitive prior methods, their inclusion with a different backbone undermines the central claim of state-of-the-art performance on ImageNet. The paper would need either (a) reproducing ReAct/DICE on ResNetv2-101, or (b) running ABeT on ResNet-50 to enable a fair comparison. (Note: the ABeT+ASH vs. ASH comparison on ImageNet *is* same-backbone and shows a dramatic improvement from 16.7→3.7, which supports the method's value even after accounting for this concern.)

### Minor

- **Object detection evaluation is too thin to support a state-of-the-art claim**: Only one baseline (VOS) is compared against in Table 3. While ABeT shows improvements on AUROC (65.34 vs. 60.46) and AUPRC (91.76 vs. 88.49), claiming state-of-the-art on a single-baseline comparison is overextended. Additional baselines or an explanation of why other methods cannot be compared would strengthen this section.

- **Section 5 ("Understanding ABeT") is qualitative and lacks metric-based confirmation**: The paper provides TSNE visualizations and positions them as providing "intuition (but not proof)" — which is intellectually honest. However, the analysis relies on visual inspection without quantitative metrics (e.g., correlation between ABeT scores and distance to class centers, or AUROC of distinguishing correct vs. misclassified ID points). The paper cites Appendix C.1 for non-dimensionality-reduction evidence, but this appendix is not accessible in the submission extract, so the main paper's argument stands as qualitative.

- **State-of-the-art claim is used too broadly**: The phrase appears throughout the paper (abstract, introduction, Table 2 caption for segmentation despite PEBAL outperforming on several metrics). In semantic segmentation, PEBAL (which uses OOD training data) outperforms ABeT on most metrics (e.g., RoadAnomaly AUPRC: 45.10 vs. 31.12), yet the paper still claims SOTA. The paper should more carefully qualify which setting (methods without OOD training data vs. all methods) it claims SOTA in.

### Trivial
- The paper's abbreviation switches between "ABeT" and "AbεT" and "AbeT" in different places; minor but should be consistent.
- Figure 3 caption text is very small and hard to read.

## Nice-to-Haves
- A per-OOD dataset breakdown in the main paper (not just averages) would help assess whether the method is truly consistent or relies on a few easy OOD datasets.
- Running ABeT on ResNet-50 for ImageNet to directly compare with ReAct/DICE numbers would substantially strengthen the paper.

## Removed Points

These points were flagged by the harsh critic but are removed after cross-checking:

- **"Standard deviations are large for several methods"** — This is a general characteristic of OOD detection evaluation (variance across OOD datasets), not a specific flaw of this paper. The paper reports standard deviations transparently, and ABeT's standard deviations are consistently lower.
- **"Could not reproduce ReAct/DICE with ResNet-101 is a red flag for reproducibility"** — The paper honestly reports this limitation. The concern is about comparison fairness (kept above as Major weakness), not about reproducibility of the paper's own method.
- **"Section 5 reads as speculation"** — The paper explicitly calls this "intuition (but not proof)" and cites Appendix C.1 for further evidence. The critic overstates the issue; the analysis is framed as hypothesis-building, not as rigorous proof. I've kept a Minor weakness noting the lack of quantitative metrics.
- **"Segmentation baselines from other papers differ in training protocols"** — This is standard practice in the field. The paper identifies which results are from other papers and explicitly excludes methods with different training paradigms. This is not a weakness unique to this paper.
- **"Missing confidence intervals on percentage improvements"** — The paper reports standard deviations, which is the standard approach in this field.
- **Criticism about "Forefront Temperature Constant study being in appendix"** — The appendix was stripped by the parser; the paper does contain this study.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective on the paper's mechanism that the authors themselves do not already articulate.

## Suggestions

1. **Address the backbone mismatch on ImageNet**: Either (a) reproduce ReAct and DICE on ResNetv2-101 using the recommended hyperparameters, or (b) train ABeT with ResNet-50 and present those results alongside the ResNetv2-101 results with an explanation of the trade-off. Without this, the ImageNet results cannot be taken at face value for comparisons against those specific baselines.

2. **Tone down the "state-of-the-art" claim**: Qualify it more carefully (e.g., "state of the art among methods that do not use OOD training data" for segmentation where PEBAL outperforms ABeT; and note the backbone caveat for ImageNet).

3. **Strengthen Section 5 with quantitative metrics**: Add at least one quantitative analysis (e.g., AUROC of ABeT on distinguishing correctly vs. incorrectly classified ID points, or a correlation measure between ABeT score and distance to the nearest class prototype).

4. **Add at least one more baseline for object detection** (e.g., energy score applied to the baseline detector, Mahalanobis distance).

## Score and Decision

**Round 1 bracket**: The paper is above weak anchors (<3.5 — papers with fundamental methodological or evaluation failures) and below strong anchors (>7.5 — papers with clean, thorough evaluations and no significant comparison concerns). Bracket: [3.5, 7.5].

**Round 2 anchors** (all within (3.5, 7.5)):
- SCALE (avg 6.25, accepted poster): Cleaner OpenOOD benchmarking and no comparison issues, but more incremental contribution. ABeT has a more original contribution but weaker experimental rigor. ABeT slightly weaker.
- Regularizing Energy (avg 6.0, accepted poster): Good theory+experiments but limited practical gains. ABeT similar tier.
- SMOT (avg 5.75, rejected): Limited improvements, comparison concerns. ABeT slightly stronger.
- Imbalanced OOD (avg 5.75, rejected): Strong theory but limited scope. ABeT addresses a broader problem.
- Feature Separation/NC (avg 6.75, accepted poster): Robust evaluation, stronger experiments. ABeT clearly weaker.
- Image Background SSOD (avg 5.33, accepted): Strong results but methodological concerns. ABeT comparable.

Comparing ABeT to these anchors: it has a more novel contribution than SCALE but messier experiments. The backbone mismatch is a real but contained issue (affects only two ImageNet baselines; ABeT+ASH vs. ASH on same backbone shows dramatic improvement). The OD evaluation is thin. The paper's core contribution is genuine and the ablation study convincingly isolates it.

**Final score: 5.5** — The paper has a genuine, well-motivated contribution that is convincingly validated by ablation. However, the comparison fairness issue on ImageNet and thin OD evaluation prevent it from being a clear accept. These weaknesses are addressable and do not invalidate the core contribution.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>