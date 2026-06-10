## Summary

This paper introduces the Nacala-Roof-Material dataset: high-resolution (≈4.4 cm) drone imagery from three informal settlements in Nacala, Mozambique, with 17,954 buildings annotated across five roof types (metal sheet, thatch, asbestos, concrete, no-roof). The dataset defines a multi-task benchmark spanning building detection, roof-type classification, and semantic segmentation, motivated by malaria risk assessment where roof material is a known epidemiological factor. The paper also benchmarks U-Net, YOLOv8, and DINOv2-based models on this dataset and explores a variant of the Deep Ordinal Watershed (DOW) method (Cheng et al., 2024) using only two height levels (nₗ=2) to improve instance separation.

## Strengths

1. **Valuable public-health dataset from an underserved region.** The Nacala-Roof-Material dataset provides drone imagery at ≈4.4 cm resolution with 17,954 carefully verified building annotations across five roof types, from peri-urban and rural settlements in Mozambique. This fills a clear gap: existing remote-sensing datasets for roof classification either use low-resolution satellite imagery with noisy, misaligned labels (Helber et al.; 10m/pixel Sentinel-2 data) or cover high-income regions with different roof geometries (Alidoost & Arefi; German town). The dataset's connection to malaria risk (where metal vs. thatch roofs have documented epidemiological significance) gives it direct application value.

2. **Geographically separated test set design.** The authors hold out an entire third settlement (dtesttwo) as a second test set with no adjacent training data (lines 86–87), in addition to the stratified train/val/test split of the first two settlements. This directly tests generalization to new areas without spatial leakage — a realistic requirement for deployment and a stronger evaluation design than what many comparable datasets provide.

3. **Multi-backbone validation with statistical rigor.** The DOW extension is evaluated on both a convolutional (U-Net) and a transformer-based (DINOv2) backbone, showing consistent improvements. The pooled Wilcoxon rank-sum test across all 20 DOW trials vs. corresponding single-mask trials (p<0.001 for AP50 improvement, p>0.05 for IoU difference, line 334) provides formal evidence that DOW improves instance separation without degrading semantic segmentation.

4. **Transparent class-imbalance handling in dataset construction.** The stratified sampling procedure uses a 225m grid to partition cells by class counts, prioritizing the minority classes (concrete, asbestos). The paper further reports both 3-class and 5-class macro-averaged metrics (mIoU³, mIoU⁵, mAP³, mAP⁵) to separate the effect of the two very rare classes from results on the three frequent roof types.

5. **Useful multi-task benchmark definition.** The dataset defines a well-motivated multi-task problem (detection, classification, segmentation) where the paper transparently shows that no single method dominates across all metrics (line 321), supporting the dataset's value as a resource for future multi-task learning research.

## Weaknesses

### Major

- **The DOW improvement is confounded with increased model capacity.** The DOW variant outputs *two* segmentation masks (full object + interior) while the baseline outputs one. In the two-stage setting, DINOv2_DOW achieves 0.884 IoU vs. DINOv2's 0.833 — a substantial gap that the paper attributes to the watershed mechanism. However, this comparison conflates two changes: (a) having an additional output channel (increasing model capacity and providing an extra training signal) and (b) applying watershed post-processing. Without an ablation that adds the interior-output channel *without* watershed, the reader cannot determine whether the improvement comes from the watershed mechanism specifically or simply from the model having more parameters and a richer training target. This is a real methodological gap in the experimental design. The paper should include a control: a DOW variant that predicts the interior map but uses connected components (not watershed) for instance separation.

### Minor

- **No discussion of computational cost.** For a dataset targeting public-health applications in resource-constrained settings, the absence of any comparison of inference time, memory usage, parameter counts, or FLOPs across methods is a missed opportunity. The DOW method requires predicting two output masks and running watershed post-processing, which introduces overhead; it would be informative to quantify this. This matters for practitioners who may need to deploy on edge devices or process large areas.

- **Class imbalance is acknowledged but not discussed as a limitation.** The paper describes the extreme class imbalance (concrete: 174 instances, asbestos: 566, vs. metal sheet: 9,776) and reports both 3-class and 5-class metrics, which is good. However, the limitations section (lines 342–347) does not mention class imbalance. It would strengthen the paper to explicitly note that conclusions drawn for the rarest classes rest on very thin evidence and that methods specifically designed for long-tail distributions may be needed.

### Trivial

- **No explicit license is specified for the dataset.** The paper states the data is "made freely available" but does not state a license (e.g., CC-BY, CC-BY-NC, etc.). This should be specified for proper reuse.

## Nice-to-Haves

- Providing per-class IoU/AP values (if they are not already in a stripped appendix) would allow the community to see where progress is most needed, especially for the minority classes.
- A qualitative figure specifically showing cases where DOW successfully separates touching buildings that the baseline merges would strengthen the visual evidence.

## Removed Points

These points were raised by reviewers but removed after verification against the paper:

- **DOW contribution is "substantially overstated":** The paper transparently frames this as "a reduced variant" of the method by Cheng et al. (2024) and cites the original work throughout. Contribution 3 is slightly ambitious in phrasing but not dishonest. Not retained as a weakness.
- **U-Net border erosion creates evaluation mismatch:** The paper explicitly states the modification was applied "only during training... not when calculating any performance metrics" (line 174). The criticism misreads the paper.
- **Per-class results are missing:** The paper references "Table~\ref{object-level}" (line 325), which likely contains per-class results in the full submission but was stripped by the parser. Cannot verify as missing.
- **Inconsistent end-to-end DOW results:** The paper fully acknowledges the mixed results for unethm (line 333: "Only for \unethm\ the results were mixed"). This transparency is a strength, not a weakness.
- **Different hyperparameter tuning rigor:** The asymmetry favors YOLOv8 (baseline), not the author's methods, and the paper transparently reports the difference. This is a fair comparison for a benchmark.
- **Confidence score derivation not validated:** Using mean pixel probability as confidence is a standard approach in segmentation literature; AP50 evaluation does not require calibrated probabilities.
- **DINOv2 encoder frozen, input patch sizes differ, Wilcoxon pooling concerns:** These are either standard design choices, common in multi-architecture comparisons, or the criticism misinterprets the hypothesis being tested.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add an ablation study isolating the watershed mechanism from the extra output channel: compare baseline → baseline + interior channel without watershed → DOW (interior channel + watershed). This would cleanly attribute the improvement.
2. Report computational cost (inference speed, parameters, memory) for at least the main method families (U-Net, DINOv2, DOW variants) to support deployment decisions.
3. Explicitly mention class imbalance as a limitation and discuss potential mitigation strategies (re-weighting, data augmentation for minority classes, etc.).
4. Specify the dataset license.
5. Tone down Contribution 3 from "propose a general and simple approach" to "demonstrate that a minimal-instance of DOW with nₗ=2 provides a favorable trade-off on this task," to better match the actual contribution.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>