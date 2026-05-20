## Summary

This paper introduces Dual-Stream Adapters (DSA), a parameter-efficient adapter architecture for anomaly segmentation that freezes a ViT backbone and learns separate in-distribution (ID) and out-of-distribution (OOD) feature streams through an anomaly prior module, dual-stream feature refinement, and an uncertainty-based hyperbolic loss. DSA achieves the highest average AuPRC (81.3) across five standard benchmarks while using 38% fewer training parameters than the prior state-of-the-art (133M vs. 216M), and it maintains strong in-distribution semantic segmentation performance (83.71 mIoU on Cityscapes).

## Strengths

1. **First adapter architecture explicitly tailored for anomaly segmentation.** DSA is the first work to design vision adapters specifically for pixel-level OOD detection, with a dual-stream mechanism that separates ID and OOD features at the architectural level (Anomaly Prior Module + Dual-Stream Feature Refinement). This is a clear and genuine novelty.

2. **Competitive AuPRC with fewer training parameters.** Table 3 shows DSA-Large achieves the highest average AuPRC (81.3) among all compared methods, outperforming Mask2Anomaly (79.3) and RbA (77.6), while using 38% fewer trainable parameters (133M vs. 216M). The parameter efficiency claim is well-supported.

3. **Maintains in-distribution performance.** Table 4 demonstrates that DSA-Large achieves the best Cityscapes validation mIoU (83.71 without outlier supervision, 82.58 with) among all anomaly segmentation models, showing that the dual-stream design does not degrade and slightly improves ID accuracy — a meaningful practical consideration.

4. **Well-structured ablation study.** The component-wise ablation (Table 5) cleanly isolates the contribution of each architectural component: removing all three components yields AuPRC 12.0, adding the anomaly prior yields 18.5, adding dual-stream refinement yields 50.2, and the full model reaches 59.6. The hyperbolic loss ablation (Fig. 6b) shows L_ubhl (47.8 AuPRC) substantially outperforms BCE (20.0) and contrastive loss (41.7).

## Weaknesses

### Fatal

None.

### Major

1. **AuPRC values in Figure 1 do not match Table 3.** Figure 1 reports DSA-Large AuPRC = 86.0 and Mask2Anomaly AuPRC = 81.5, but Table 3 reports average AuPRC values of 81.3 and 79.3 respectively. The discrepancy is consistent (~4-5 points) for all methods, suggesting Figure 1 may report a different aggregation or dataset subset, but the paper does not explain this. This undermines the quantitative story in the headline figure and needs to be reconciled.

2. **Evaluation metric inconsistency across tables.** The paper states (Experiments section) "We employ AuPRC and FPR_{0.5} as evaluation metrics," but Table 2 and Table 3 use FPR_{0.1}, while Figure 1, Figure 6, and Table 5 use FPR_{95}. Different FPR thresholds serve different analytical purposes, but switching between them without explanation makes it difficult to compare results across experiments. The paper should adopt a consistent primary metric — FPR_{95} is the established standard in the anomaly segmentation literature.

3. **Void-label supervision confounds the comparison with baseline methods.** DSA-Large uses Cityscapes void/background pixels as OOD supervision (denoted by ▽ in Table 3), while the mask-based baseline methods (Mask2Anomaly, RbA, EAM) do not use this signal. This creates an uncontrolled variable: the performance gap could partly reflect the extra supervision rather than the adapter architecture itself. The paper should ablate the void-label supervision (e.g., train DSA without L_ubhl on void pixels) and, ideally, provide a baseline where mask-based methods also receive void-label supervision, to isolate the architectural contribution. The paper is transparent about this (▽ symbol), but does not address the confound.

4. **No analysis of model behavior on void regions.** Since DSA is explicitly trained to treat void pixels as OOD, a critical missing analysis is the anomaly score distribution on Cityscapes void regions. If the model assigns high anomaly scores to ordinary unlabeled scene content, the method is partly learning void detection rather than anomaly detection. This experiment is necessary to validate the training signal.

### Minor

5. **Training time and GPU-hours not reported.** The paper's efficiency claim rests solely on trainable parameter count (38% fewer). Parameter count is a useful proxy, but training time, GPU memory, and FLOPs would provide a more complete efficiency picture. The frozen backbone still requires a forward pass through ViT-L (304M parameters), so total inference model size is larger than that of Swin-L-based methods (197M). The paper should clarify this distinction.

6. **Statistical significance not reported.** Many performance differences are small (e.g., Table 4 mIoU differences < 0.5 points). Without variance estimates or significance tests, it is unclear whether reported improvements are reliable.

### Trivial

None.

## Nice-to-Haves

- The paper could discuss why the Cityscapes void class is a reasonable OOD proxy (e.g., cite precedents in the anomaly segmentation literature that use void/background for supervision).
- Reporting inference latency and FLOPs would strengthen the practical contribution of the efficiency claim.

## Removed Points

These points are flagged to be removed — treat them with caution:

- **Criticism that "void includes buildings, fences, sidewalks, sky, vegetation"**: This is factually incorrect. All of these are labeled classes in Cityscapes (part of the 19 training categories), not void. The void class covers pixels that do not belong to any training category.
- **Claim that "Table 2 uses FPR₀.₅"**: The header for Table 2 clearly shows FPR₀.₁.
- **Criticism that Table 5(a) is garbled or has inconsistent numbers**: The parsed output shows identical checkmarks across all rows, but this is a PDF-parsing artifact — the original table presumably uses different check marks (✓/✗) to indicate removed components. The text clearly explains the ablation setup ("removing one at a time").
- **Criticism about total model size being larger for inference**: The paper's claim is specifically about *training* parameters (38% fewer), and this is accurately stated. The efficiency claim does not extend to total inference model size, which the paper does not assert.
- **Generic requests for "larger dataset" or "more models"**: The evaluation on five benchmarks with current SOTA methods is already thorough.
- **Strength Finder's generic/superficial strengths**: Several strengths about "the problem being important" or "addressing an interesting question" are removed as they lack concrete evidence specific to this paper.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a conflict between the paper's claimed state-of-the-art status and the evaluation confounds (void label supervision, metric inconsistency) that prevent clean attribution of results to the architectural innovations. This is a useful framing for the authors to address in revision.

## Suggestions

1. **Reconcile Figure 1 and Table 3** by explaining which aggregation method is used in the figure — or use a consistent set of numbers.
2. **Adopt FPR₉₅ as the primary false-positive metric** throughout the paper, consistent with the anomaly segmentation literature. Report FPR₀.₁ and FPR₀.₅ as supplementary thresholds if desired.
3. **Ablate the void-label supervision** by training DSA without L_ubhl (or without void labels entirely) to isolate the effect of the extra supervision signal from the architectural contribution.
4. **Add an analysis of anomaly score distribution on Cityscapes void regions** to validate that the model does not simply learn to flag unlabeled pixels as anomalous.
5. **Report training GPU-hours and inference FLOPs/latency** to support the efficiency claim beyond parameter count.
6. **Include variance estimates** (e.g., multiple seeds) for key results to assess statistical significance of small differences.

## Score and Decision

**Round 1 bracket (bracketing):**
- Weak anchors (avg < 3.5): anomaly adapter papers avg 2.5–3.0 — clearly below this paper.
- Middle anchors (avg 3.5–7.5): AnomalyCLIP (6.17), ProPETL (6.0), MuSc (5.2), ST-SSAD (5.67) — this paper sits here.
- Strong anchors (avg > 7.5): avg 8.0–9.0 — far above this paper.

Initial bracket: **5.0 – 6.5.**

**Round 2 (narrowing within bracket):**
- AnomalyCLIP (6.17, accepted poster): well-written, comprehensive experiments, mostly minor weaknesses. DSA has more substantive evaluation concerns → DSA is weaker.
- ProPETL (6.0, accepted poster): clear motivation, strong results on PETL for segmentation. DSA's evaluation confounds are larger → DSA is weaker.
- MuSc (5.2, accepted poster): serious assumption concern (access to entire test set), comparable severity to DSA's issues → DSA is slightly stronger.
- ST-SSAD (5.67, rejected): strong assumptions that reviewers found problematic → comparable.

**Final score: 5.5.** The paper has genuine architectural novelty and competitive results, but the evaluation is undermined by metric inconsistencies across tables, a discrepancy between Figure 1 and Table 3, and an uncontrolled void-label supervision variable that prevents clean attribution of performance to the architectural contribution. These issues are addressable in revision but are too substantive to overlook for acceptance in the current form.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>