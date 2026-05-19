- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 3, 8
Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper develops conformal inference methods for image segmentation that produce inner and outer confidence sets with finite-sample probabilistic guarantees on per-image coverage of the full mask. The key technical idea is to calibrate thresholds based on the distribution of the *maximum* of (transformed) logit scores over false-positive and false-negative regions in a calibration set. The paper proves Theorems 1–3 establishing coverage guarantees under exchangeability, and demonstrates that learning different score transformations for inner sets (identity) versus outer sets (distance transform) yields tighter bounds than using a single transformation, on a polyp segmentation dataset with the PraNet model.

---

## Strengths

- **Rigorous finite-sample coverage guarantees.** Theorems 1 and 2 (Section 2.2) prove that the constructed inner and outer sets contain the true mask with probability at least \(1-\alpha_1\) and \(1-\alpha_2\) respectively under exchangeability and score independence — the standard assumptions for split conformal inference. Theorem 3 and Corollary 1 extend these to joint coverage. The proofs are clearly presented and follow from standard conformal arguments.

- **Clear and practically useful distinction between score transformations for inner vs. outer sets.** Using a held-out learning dataset (298 images), the paper shows empirically that original scores give tight inner sets while distance-transformed scores give tight outer sets (histograms in Figure 1, surface plots in Figure 2). The chosen combination (identity for inner, distance transform for outer) is then validated on separate calibration/test sets and quantified in efficiency analyses (Figures 5–6, Section 3.4), confirming the learning-dataset intuitions with clean quantitative curves.

- **Thorough validation of coverage control.** The paper runs 1000 validation splits (Section 3.3), each with 1000 calibration and 500 test images, and reports that coverage rates average at or above the nominal level for all score transformations (Figure 4). This convincingly verifies that the theoretical guarantees hold in practice across multiple data partitions.

- **Clear treatment of marginal vs. joint coverage with practical guidance.** Section 2.3 derives both alpha-weighting (Corollary 1) and joint-threshold approaches (Theorem 3) and discusses the trade-offs — pivotality vs. dependence structure — providing practical guidance for practitioners.

---

## Weaknesses

### Fatal
None.

### Major
- **Single dataset, single model limits the empirical scope.** All experiments use one dataset (polyp images from five open-source datasets, 1798 images total) and one segmentation model (PraNet). While the theory is general, the paper claims applicability to biomedical image segmentation broadly but provides evidence from only one domain. Properties of score distributions — and whether distance transforms are helpful — are dataset- and model-dependent. An additional task (e.g., lung CT, histopathology) or model architecture would substantially strengthen the claim of generality. This does not invalidate the theory but limits what the empirical section can establish about the method's general effectiveness.

### Minor
- **Informal description of the learning-dataset decision procedure.** The paper correctly advocates using a separate learning dataset to choose score transformations and alpha weights, but the actual decision process is described in judgmental, non-algorithmic terms: "Based on the results of the learning dataset we decided to combine…" and "A ratio of 4 to 1 seems appropriate here in light of the fact that…" (Section 3.1). While the choices themselves appear sensible and are validated on held-out test data, the procedure is not reproducible as a concrete algorithm. A simple rule (e.g., "choose \(f_I\) and \(f_O\) to minimize average set size on the learning set subject to coverage constraints") would strengthen the paper's methodological contribution.

- **No confidence intervals or variance bands in efficiency comparisons.** While the 1000-validation-split averages produce clean curves (Figures 5–6), the paper reports no variability measures (e.g., standard deviation bands, percentile intervals) for the efficiency metrics. Adding these would clarify whether the observed differences between score transformations are reliable.

- **The max aggregation function's conservatism is acknowledged but underexplored.** Remark 1 notes that any increasing combination function works, but the paper does not discuss when the max is well-calibrated vs. overly conservative (e.g., whether a quantile-based threshold would yield tighter sets in some settings). A brief discussion of this trade-off would strengthen the theoretical framing.

### Trivial
None.

---

## Nice-to-Haves

- **Additional baselines from the conformal segmentation literature.** While the paper compares different score transformations within its own framework (including bounding box scores grounded in existing work De2022, Andeol2023), including a pixelwise conformal + Bonferroni baseline — even if the statistical target differs — would provide a familiar reference point for readers.
- **Formalize the learning dataset decision rule** into a concrete optimization objective (e.g., select transformations and alpha weights that minimize a loss on the learning dataset).
- **Add a second biomedical segmentation domain** to demonstrate generalizability.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

1. **"No comparison to existing conformal segmentation methods"** — Removed. The paper *does* compare to bounding box scores, which are grounded in existing work (De2022, Andeol2023, cited in Section 2.5). The paper's contribution is specifically per-image *mask coverage* guarantees, which is a different statistical target from pixelwise conformal + Bonferroni (per-pixel coverage) or risk-controlling methods (expected risk control). The paper clearly states this distinction (Section 1, paragraph 4). A comparison to methods with fundamentally different guarantees is not necessary to establish the method's validity.

2. **"The paper does not specify how scores are thresholded to produce predicted masks \(\hat{M}(X)\)"** — Removed as a reproducibility nitpick. This is a standard implementation detail routinely omitted from methodology papers. The paper specifies that scores are "logit scores" from PraNet; the exact binarization threshold does not affect the theoretical contributions.

3. **"It is unclear whether the distance transform is computed from the predicted mask or from the ground truth in the calibration step"** — Removed as factually incorrect. The paper clearly states (Section 3.1, line 164) that the distance transform uses \(\hat{M}(X)\), the predicted mask.

4. **"Missing related work"** — Removed per instructions (no external sources to confirm).

5. **Formatting/style nitpicks from harsh critic** — Removed per instructions (parser artifacts, not author errors).

---

## Novel Insights

None beyond the paper's own contributions. The harsh critic's calibration sweep surfaces the observation that the max-based aggregation may be conservative and that the learning procedure could be formalized, but these are natural extensions stemming from the paper's own framework rather than novel insights not present in the paper.

---

## Suggestions

1. **Add at least one additional biomedical segmentation domain** (e.g., lung nodules from CT, nuclei from histopathology) and at least one additional model architecture to the empirical evaluation. This would transform the experiments from a case study into a genuine validation of a general method.

2. **Formalize the learning dataset procedure** into a concrete, repeatable algorithm: define a loss function on the learning set (e.g., sum of inner undercoverage and outer overcoverage proportions), select transformations and alpha weights to minimize it, and report the chosen rule.

3. **Include variability estimates** (e.g., confidence bands, percentile intervals) for the efficiency curves in Figures 5–6 to clarify the reliability of the observed differences.

4. **Add a brief discussion** of scenarios where the max may be overly conservative and whether alternative aggregation functions (e.g., quantiles) could be used, noting that Remark 1 guarantees validity for any increasing combination function.

---
