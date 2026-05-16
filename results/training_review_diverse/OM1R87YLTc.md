Now I have all the information needed. Let me synthesize the final review.

## Summary

This paper proposes two techniques—Anti-Degradation Complementary Learning (ADC learning) and SAMEnhancer—for multi-task perception (drivable area segmentation + object detection) in unstructured environments where task annotations do not overlap across images. ADC learning is a two-phase alternating training strategy with pseudo-labeling to prevent performance degradation when training on non-overlapping task annotations. SAMEnhancer uses Mobile SAM to improve segmentation coherence by fusing the network's semantic predictions with SAM's structural masks guided by confidence-based point prompts. Experiments on IDD and BDD100K datasets validate the methods through internal comparisons.

## Strengths

1. **ADC learning demonstrably recovers performance under non-overlapping annotations** — Table 1 shows on IDD, mIoU drops from 88.67 (full labels) to 84.83 (non-overlap) and recovers to 86.18 with ADC; on BDD100K, detection mAP drops from 84.5 to 80.5 and recovers to 85.1. The direction and consistency of recovery across both datasets and tasks directly support the core claim.

2. **SAMEnhancer improves segmentation coherence and accuracy** — Table 3 reports mIoU rising from 91.68 (network prediction) to 93.01 (merged result) and accuracy from 95.60 to 96.92 on IDD. The qualitative examples in Figure 4 confirm reduced fragmentation. This directly supports the claimed enhancement for unstructured road segmentation.

3. **Generalization across multiple encoder architectures** — Table 2 shows ADC learning improves both mIoU and mAP over the non-overlap baseline for ConvNeXt, EfficientNet, and DenseNet backbones (e.g., mIoU on IDD: ConvNeXt from 73.38 to 78.59), demonstrating robustness beyond a single backbone design.

4. **Technically grounded point-prompt extraction** — The three-point selection (centroid weighted by confidence, circumcircle center, highest-confidence interior point, Eqs. 6–8) is geometrically principled, with morphological pre-processing to filter noise before SAM prompting. The design choices are clearly motivated and formalized mathematically.

5. **Addresses a genuine and under-addressed problem** — The non-overlapping annotation issue in unstructured datasets (IDD, RUGD, ORFD) is a real practical barrier that existing MTL approaches (which assume fully co-annotated data) do not address. The paper's problem formulation is timely and relevant.

## Weaknesses

### Fatal

None.

### Major

1. **No external baselines or comparisons to prior work** — Every experiment compares only internal variants: "not overlapping" vs "ADC learning," or network output vs SAM prediction vs merged result. There are no comparisons to any existing method (e.g., YOLOP as reported in its original paper, DeepLabV3+ variants on IDD, standard semi-supervised/self-training approaches for missing labels, or published SOTA on IDD/BDD100K). The paper claims "significant performance improvements," but without external context the reader cannot assess whether the proposed techniques are competitive with or superior to existing approaches, or whether simpler alternatives achieve similar gains. This is the paper's most consequential weakness.

2. **No ablation separating the two phases of ADC learning** — The paper does not isolate Phase 1 (alternating training without pseudo-labels) from Phase 2 (pseudo-label training). It is impossible to determine how much of the improvement comes from the alternating schedule itself versus the addition of pseudo-labels, or whether a simpler one-phase pseudo-labeling approach without alternating would perform similarly. A proper ablation (Phase 1 alone, Phase 2 with fixed pseudo-labels, Phase 2 with alternating pseudo-labels) is essential to support the claimed two-phase design.

3. **No runtime or efficiency measurements for the SAMEnhancer pipeline** — The paper repeatedly describes SAMEnhancer as "lightweight," "plug-and-play," and "suitable for real-time applications" (citing Mobile SAM's efficiency), but reports no actual inference time, FPS, parameter count, or FLOPs for the combined pipeline (YOLOP + Mobile SAM). Without these measurements, the efficiency claims are unsupported, and a reader cannot judge the practical deployability of the approach.

4. **The degradation phenomenon is asserted but never measured** — The paper claims that alternating training causes a "significant drop in performance on the previous task" (degradation), which motivates the pseudo-label design in Phase 2. However, no learning curves, epoch-by-epoch metrics, or quantitative evidence of this degradation are shown. The improvement from ADC learning could plausibly come entirely from the extra supervision of pseudo-labels rather than from "anti-degradation" specifically.

### Minor

1. **Missing experimental details that affect reproducibility** — The following details are absent: (a) number of epochs for Phase 1 ("limited number of epochs" is not specified); (b) whether/how often pseudo-labels are updated during Phase 2; (c) whether pseudo-labels are thresholded and at what confidence; (d) the exact alternating schedule for the "not overlapping" baseline (one epoch per task? one full pass?); (e) kernel sizes for the morphological operations (open/close) in SAMEnhancer; (f) the train/val/test split used for IDD experiments. While these are fixable in a revision, they currently leave critical gaps for reproducibility.

2. **SAMEnhancer fusion logic is ambiguously described** — Equation 10 and the surrounding text are contradictory. The text states "portions with confidence above the threshold (0.9 in this paper) are retained, while the other parts keep the results from Y˜," which implies both branches use the network output (Y˜), making the fusion trivial. The equation notation suggests using Y˜ above Ŷ (or vice versa), but the choice is unclear. This needs clarification. Additionally, the confidence threshold of 0.9 is used without any sensitivity analysis or justification.

3. **No comparison of SAMEnhancer to simpler post-processing alternatives** — The paper does not compare to standard post-processing techniques such as Conditional Random Fields (CRF), morphological closing, or simple thresholding, which are standard baselines for improving segmentation coherence. Without such comparisons, the added value of using SAM specifically is not isolated.

4. **No statistical significance or variance reporting** — There is no mention of whether results are from single or multiple runs, no standard deviations or confidence intervals, and no discussion of experimental variance. This makes it difficult to assess whether the reported improvements (often 1–3% absolute) are reliably above noise.

5. **No analysis of pseudo-label quality** — The paper does not report the accuracy, coverage, or noise level of the pseudo-labels generated in Phase 2, nor what percentage of images receive pseudo-labels. Such analysis would provide insight into why ADC learning works and where it might fail.

### Trivial

- The absence of a limitations/discussion section; failure cases of SAMEnhancer (e.g., dependence on good initial segmentation) are not acknowledged.
- No detection metrics beyond recall and mAP50 (e.g., mAP at varying IoU thresholds, per-class AP).
- The paper does not specify the train/val/test split used for IDD.

## Nice-to-Haves

- A code release would significantly aid reproducibility, as the training pipeline has several details that benefit from reference implementation.
- A comparison to a single external baseline per dataset (e.g., the original YOLOP numbers on BDD100K, or a published IDD segmentation method) would help calibrate the reader and would not require running additional experiments if numbers are available from prior work.
- Runtime measurements (FPS, parameters) for the full YOLOP+Mobile SAM pipeline would substantiate the lightweight/efficiency claims.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The use of BDD100K is confusing"** — REMOVED. The paper explicitly states BDD100K is used to *simulate* non-overlapping annotations in a controlled setting where ground truth for both tasks exists. This is a standard and valid experimental design; the paper does not claim BDD100K is unstructured. The criticism reflects a misreading.
- **"No discussion of semi-supervised learning methods in related work"** — REMOVED per rule (DO NOT mention missing related works, as external sources cannot be confirmed).
- **"Formatting/table legibility issues"** — REMOVED. These are parser artifacts from PDF extraction, not author errors.
- **"The paper should also cover Y / domain Z / additional tasks"** — REMOVED as scope creep. The paper focuses on two specific tasks (drivable area segmentation + object detection) with two proposed techniques; broadening to additional tasks would change the paper rather than improve it.
- **"The paper should compare against reviewer-preferred baselines"** — WEAKENED. The demand for specific baselines (DeepLabV3+, YOLOP original) is valid and is kept in Major Weakness #1 under "no external baselines." The demand for "standard semi-supervised or self-training approaches" is also covered there. However, the complaint about lacking comparisons to published IDD results is incorporated into that single weakness rather than listed separately.

## Novel Insights

Beyond the paper's own contributions, the reviews surface one genuinely useful insight: the fusion of semantic segmentation with SAM's structural masks via confidence-guided point prompts is a technically clean design that could generalize to other segmentation refinement tasks beyond drivable area. The idea of using the network's own confidence map to both select SAM prompts and gate the fusion is a natural design pattern worth noting. However, the reviews do not reveal additional insights beyond what the paper already proposes.

## Suggestions

1. **Add at least one external baseline per dataset.** For IDD, report the performance of a standard YOLOP variant (with lane detection removed) trained on fully annotated data, and/or cite published results from IDD segmentation/detection benchmarks. For BDD100K, the original YOLOP paper provides ready-to-use numbers. This is the single highest-impact improvement.

2. **Ablate ADC learning's two phases separately.** Report: (a) Phase 1 alternating training alone, (b) Phase 2 with pseudo-labels generated once and not updated, (c) Phase 2 with alternating pseudo-label updates. This would isolate the contribution of each component and validate the claimed two-phase design.

3. **Provide a complete, numbered algorithm for ADC learning** with all hyperparameters (epochs per phase, learning rate schedule, batch size per task, pseudo-label threshold, update frequency). This is essential for reproducibility.

4. **Clarify the SAMEnhancer fusion equation (Eq. 10)** and fix the contradictory text. Report a sensitivity analysis for the confidence threshold (0.9).

5. **Measure and report runtime** (FPS or ms per image) for the full YOLOP+Mobile SAM pipeline to support the lightweight/real-time claim. Compare to a CRF baseline or morphological post-processing to isolate SAM's added value.

6. **Report the degradation phenomenon quantitatively** — show a learning curve or epoch-by-epoch metrics demonstrating performance drop on Task A after switching to Task B during alternating training.

## Score and Decision

The paper tackles a genuine problem with two reasonable techniques, and the internal validation is directionally consistent. However, the absence of any external baselines, the incomplete ablation of the core method (ADC learning's two phases), and the unsupported efficiency claims leave the evaluation insufficient to accept the paper's claims of "significant performance improvements" at face value. The ideas are worth pursuing, but the paper requires substantially stronger empirical validation for publication.

**Score**: 4.0

**Decision**: Reject

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>