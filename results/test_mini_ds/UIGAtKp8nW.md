Now I have a thorough understanding of the paper and the calibration anchors. Let me finalize my consolidation.

## Bracketing Statement

Round 1 established that this paper sits between the weak anchors (≤3.0) and strong anchors (≥8.0), most plausibly in the 4–7 range. Round 2 narrowed the bracket: comparing against BenchMol (4.80), RoFt-Mol (5.25), EGraFFBench (6.00), and Pushing Limits of Geom-GNN (6.50), the paper is slightly above BenchMol but below the stronger benchmark papers that introduce new datasets or methods. The lack of variance reporting and the absence of new datasets/metrics cap the score below 6.

Here is my consolidated review.

---

## Summary

MUBen presents the first systematic benchmark evaluating uncertainty quantification (UQ) methods applied to pre-trained molecular representation models. The benchmark covers 4 primary backbone architectures (ChemBERTa, GROVER, Uni-Mol, DNN) plus 2 secondary ones, 8 UQ methods spanning deterministic, Bayesian, post-hoc, and ensemble categories, and 14 classification/regression datasets from MoleculeNet. Key findings include the identification of an expressiveness–calibration tradeoff (larger models such as Uni-Mol are more overconfident), the observation that Deep Ensembles and MC Dropout consistently improve OOD predictive performance, and actionable guidance for method selection by task type.

## Strengths

- **First comprehensive UQ benchmark on pre-trained molecular models.** The paper fills a concrete gap identified in prior work (limited UQ method variety, narrow task coverage, no pre-trained backbones). The systematic design — covering SMILES-based, 2D graph-based, and 3D conformation-based models — provides a unified comparison that did not previously exist. This is directly supported by Tables 5.1 and 5.2 and the explicit discussion of limitations in the Introduction (lines 33–37).

- **Identification of an expressiveness–calibration tradeoff.** The finding that larger, more expressive backbones (Uni-Mol) achieve better property prediction but are more overconfident, while smaller models calibrate better, is backed by quantitative evidence (Figure 5.3, SGLD deviation plot; lines 275–279: "models with lower expressiveness tend to exhibit better calibration"). This insight is genuinely enabled by the multi-backbone design and goes beyond prior molecular UQ work.

- **Rigorous OOD evaluation design.** The use of scaffold splitting for all datasets (line 198) plus the Tanimoto similarity analysis on QM9 (Figure 5.5, lines 309–313), which shows calibration error remains stable while RMSE degrades under distribution shift, provides concrete evidence that UQ estimates are more robust to OOD shifts than point predictions. This is a well-designed analysis component.

- **Actionable practical guidance.** The paper distills findings into concrete recommendations: Temperature Scaling and MC Dropout for classification, BBP and SGLD for regression, and the need for stronger UQ on larger backbones (Section 6, lines 323–327). These are backed by quantitative rankings across 8+6 datasets.

- **Acknowledged limitations.** The paper openly discusses its coarse hyperparameter grids and incomplete coverage (lines 329–331), which is good practice for a benchmark contribution.

## Weaknesses

### Fatal
None.

### Major

- **No variance/uncertainty estimates on reported metrics.** The paper states "Each reported metric is the average of 3 individual training-test runs with random seeds 0, 1, and 2" (line 216) but provides no standard deviations, confidence intervals, or statistical significance tests. Rankings are based on differences that can be as small as 0.3–0.5 in average rank. Without variance information, the reader cannot assess whether observed patterns are reliable or noise-driven. This is the most impactful weakness for a benchmark that derives rankings and conclusions from these numbers. At minimum, standard deviations should be reported; a Friedman test or critical difference diagram would be even stronger.

### Minor

- **Several central claims are speculative rather than directly evidenced.** The paper states that SWAG "might intensify training data overfitting due to the additional steps taken to fit the parameter distribution" (line 243) and that BBP/SGLD "can hinder network convergence, leading to insufficient exploration" (lines 244–245). These are reasonable hypotheses but are not supported by training curves, convergence diagnostics, or any direct evidence presented in the main paper. While referenced figures may be in the appendix (stripped by the parser), the main text could more clearly separate observation from speculation.

- **Regression Calibration Error's Gaussian assumption is not discussed.** The Regression CE metric (Equation on line 116) uses a Gaussian CDF, assuming the predictive distribution is Gaussian. For Bayesian methods like BBP and SGLD that may produce non-Gaussian posterior variances, this assumption could bias calibration assessment. The paper acknowledges the assumption (line 119: "assuming a Gaussian distribution for the labels") but does not discuss its potential impact or consider alternative calibration measures (e.g., interval-based).

- **Equal weighting across datasets with vastly different task counts.** Metrics are first macro-averaged across tasks within each dataset, then averaged across datasets (lines 215–216). This gives equal weight to ToxCast (617 binary tasks) and BBBP (1 task) in the final average, which could distort aggregate rankings. This is a defensible design choice but warrants explicit discussion.

### Trivial
None.

## Nice-to-Haves

- Adding training/inference cost estimates (GPU-hours or parameter counts) for each UQ method would strengthen the benchmark's practical utility, especially given the paper's acknowledgment that Deep Ensembles come at "substantial computational cost" (line 323).
- A hyperparameter sensitivity analysis (e.g., for Temperature Scaling's temperature and Focal Loss's focusing parameter) would improve reproducibility.
- Reporting OOD detection performance (e.g., AUROC for separating in-distribution vs. OOD) would broaden the paper's relevance, though this is outside the stated scope.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"Insufficient specification of UQ method integration"** — The paper explicitly defers implementation details to the appendix (line 154: "We provide a high-level sketch here of each method and leave the details to \cref{appsec:uncertainty}"). The appendix was stripped by the parser; the original submission likely contains these details. Removed per Hard Rules on missing appendix content.

2. **"Incomplete presentation of results (only 4 datasets shown)"** — The paper shows macro-averaged rankings across all datasets (Tables 5.1 and 5.2) and notes "Please refer to \cref{appsec:uq.resource.analysis} and \cref{appsubsec:uq.visualization.and.analysis}" for per-dataset breakdowns. These are in the stripped appendix. Removed per Hard Rules on missing appendix content.

3. **Criticisms about "unreleased" or "unverifiable" models/datasets** — The paper cites existing models and datasets (ChemBERTa, GROVER, Uni-Mol, MoleculeNet, etc.) that are published and available. Removed per Hard Rules.

4. **Formatting, typography, and presentation nitpicks** — Removed per Hard Rules.

5. **Missing related works** — Removed per Hard Rules ("DO NOT mention missing related works").

6. **"Regression CE assumption" criticism as "fatal"** — While kept as a Minor weakness, the critic's framing of this as a severe issue was disproportionate. The assumption is standard in the UQ literature (Kuleshov et al., 2018) and is clearly stated.

## Novel Insights

The reviews do surface one genuinely novel observation that the paper itself does not fully articulate: the finding that **larger pre-trained molecular models show a systematic overconfidence problem that is qualitatively different from the calibration issues observed in smaller models**, and that this overconfidence is driven not just by overfitting but by the model mistaking shared 3D conformational features for in-distribution similarity. This is a subtle failure mode specific to 3D molecular representations (Uni-Mol) that goes beyond the standard "larger models are more overconfident" trope from the general deep learning calibration literature (Guo et al., 2017). The paper could more sharply frame this as a distinct insight.

## Suggestions

1. **Report standard deviations or confidence intervals for all metrics.** This is the single highest-impact improvement. A critical difference diagram (Demšar, 2006) with a Friedman test would immediately strengthen the statistical basis of the rankings.

2. **Separate observation from speculation.** Clearly mark which claims (SWAG overfitting, BBP/SGLD convergence issues) are supported by evidence vs. speculative, and consider adding convergence diagnostics (training loss curves, gradient norms) to support these claims.

3. **Add a brief discussion of the Gaussian assumption in Regression CE** and its potential limitations for Bayesian methods.

4. **Discuss the dataset-weighting scheme** (equal weight across datasets despite varying task counts) and its potential effect on aggregate rankings.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>

### Calibration Anchors

| Path | Avg Score | Round | Comparison to this paper |
|------|-----------|-------|-------------------------|
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/N4lUNwEn1c.md | 3.00 | 1 (weak) | Significantly weaker; this paper lacks coherent scope |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/rEQ8OiBxbZ.md | 3.00 | 1 (weak) | Weaker; method paper with limited evaluation |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/u8L1zzGXRq.md | 3.00 | 1 (weak) | Weaker; narrower scope and limited experiments |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/B6B6EhC1bW.md | 2.50 | 1 (weak) | Weaker; less systematic |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/1JgWwOW3EN.md | 4.80 | 1+2 (mid) | Comparable benchmark paper; MUBen is more focused on UQ but BenchMol covers more modalities |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/P5jreWnIjV.md | 4.00 | 1 (mid) | Lower quality; computational dataset with questionable labels |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/R8YCBH5HWo.md | 4.50 | 1+2 (mid) | Comparable; method + benchmark paper, similar execution quality |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/4S2L519nIX.md | 6.50 | 1+2 (mid) | Stronger; accepted paper with more novel empirical analysis |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/ym7pr83XQr.md | 7.00 | 1 (mid) | Stronger; accepted method paper with more novel contribution |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/aqTipMg9CZ.md | 5.25 | 1 (mid) | Comparable; similar quality level |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/IbCvnpJ4py.md | 5.25 | 2 (mid) | Comparable; similar benchmark of methods on pre-trained molecular models |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/PfPnugdxup.md | 5.75 | 2 (mid) | Slightly stronger; accepted, introduces a new method |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/NvJxTjTQtq.md | 6.00 | 2 (mid) | Stronger; introduces new datasets and metrics |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/NSDszJ2uIV.md | 6.33 | 2 (mid) | Stronger; accepted benchmark with new datasets |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/vrBVFXwAmi.md | 8.00 | 1 (strong) | Much stronger; accepted with higher novelty and technical quality |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/NSVtmmzeRB.md | 8.00 | 1 (strong) | Much stronger |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/KSLkFYHlYg.md | 8.00 | 1 (strong) | Much stronger |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/gHLWTzKiZV.md | 8.00 | 1 (strong) | Much stronger |

**Round 1 bracket:** Between 4.0 and 7.0.

**Round 2 narrowing:** The paper is comparable to BenchMol (4.80) and RoFt-Mol (5.25) — solid benchmark papers that fill identifiable gaps without introducing new datasets or methods. It is weaker than EGraFFBench (6.00) and Pushing Limits of Geom-GNN (6.50), which contribute new datasets/metrics or have method components. The absence of variance reporting prevents the paper from reaching the 5.5–6.0 range. Score settled at **5.0**.