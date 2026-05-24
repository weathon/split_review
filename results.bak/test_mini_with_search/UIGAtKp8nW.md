Now I have all the information I need. Let me compile the final consolidated review.

## Summary

MUBen presents a comprehensive benchmark that evaluates nine uncertainty quantification (UQ) methods (BBP, SGLD, MC Dropout, SWAG, Temperature Scaling, Deep Ensembles, etc.) on six molecular representation backbones (ChemBERTa, GROVER, Uni-Mol, DNN, TorchMD-NET, GIN) across 14 MoleculeNet property prediction datasets using standard UQ metrics. The key findings—Deep Ensembles is the most consistently reliable UQ approach across settings, Temperature Scaling is effective for classification calibration, BBP/SGLD perform well on regression calibration metrics, and larger models exhibit an expressiveness–calibration trade-off—provide actionable guidance for practitioners.

## Strengths

1. **First comprehensive UQ benchmark on pre-trained molecular backbones.** The paper systematically covers four descriptor types (SMILES, 2D graphs, 3D conformations, hand-crafted features) with nine UQ methods from four categories (deterministic, Bayesian, post-hoc, ensembles). This fills a genuine gap, as prior work (cited in §2.2) was fragmented across limited UQ methods or backbone choices.

2. **Actionable findings supported by macro-averaged rankings.** The consistent top ranking of Deep Ensembles across both classification and regression metrics (Tables tb:classification.results, tb:regression.results) provides concrete guidance. The identification of Temperature Scaling for classification and BBP/SGLD for regression calibration gives practitioners clear starting points.

3. **Scaffold splitting for realistic OOD evaluation with explicit comparison to random splits.** The benchmark uses scaffold splitting (§4.3) to create challenging out-of-distribution test sets and reports results for both splitting strategies (Table tb:random.split), strengthening the practical relevance of conclusions beyond i.i.d. evaluation.

4. **Evidence-backed analysis of the expressiveness–calibration trade-off.** The paper demonstrates that larger models (Uni-Mol) are more overconfident, that UQ methods are most critical for large models (larger calibration error gaps for Uni-Mol vs. DNN), and that simpler models tend to be better calibrated—supported by Figure fig:s5.mrrs and quantitative discussion in §5.

## Weaknesses

### Fatal

None.

### Major

1. **No variance or statistical significance reported for any metric.** Every result is reported as the average of three seeds (seeds 0, 1, 2) without standard deviations, confidence intervals, or any measure of variability (§4, line 216). For a benchmark whose core contribution is guiding method selection, this is a significant evidential weakness. The reader cannot determine whether the reported performance gaps between methods (e.g., "Deep Ensembles consistently enhances performance," "Uni-Mol secures the best prediction performance") reflect real differences or noise from random seed variation. This is the single most impactful limitation and the highest-leverage improvement.

### Minor

2. **The regression UQ recommendation for BBP and SGLD is stronger than the evidence supports.** The paper recommends BBP and SGLD as "more suitable in estimating regression uncertainty" (§6, line 325), and highlights that they capture 7 of 8 top calibration ranks (§5, line 269). However, the paper's own analysis shows that SGLD "play[s] safe by predicting larger variances" and that "we do not observe a better correlation between SGLD's error and variance" (§5, lines 271–272). This means the uncertainty estimates achieve good calibration metrics (NLL, CE) through inflated variance rather than informative correlation with error, which limits practical value for selective prediction or experimental design. The paper partially acknowledges this but the conclusion could be more circumspect.

3. **Coarse hyperparameter grids limit comparison fairness.** The authors acknowledge using "coarse-grained hyperparameter grids to maintain experimental feasibility" (§6, line 330). Methods such as BBP, SGLD, and MC Dropout are known to be sensitive to learning rate, prior scale, and sampling hyperparameters. Without evidence that the chosen grids are reasonable for all methods, the rankings should be treated as indicative trends rather than definitive conclusions about relative method quality. The paper is honest about this, but it remains a limitation worth weighting.

4. **Only binary classification tasks are covered.** All eight classification datasets are binary (§4, line 194). The paper does not discuss whether its conclusions (e.g., that Temperature Scaling is the most effective calibration method) might differ for multi-class settings. This is a scope gap that should be acknowledged.

### Trivial

None.

## Nice-to-Haves

- **Standard deviations for all metrics** (as noted in Major weakness 1). This is the most impactful single improvement and is within scope of the existing experimental setup.
- **Runtime or FLOPs comparison** of different UQ methods, since the paper notes Deep Ensembles' "substantial computational cost" but never quantifies it.
- **Selective prediction analysis** (e.g., risk-coverage curves) to better evaluate whether BBP/SGLD's inflated variance is practically useful despite weak error correlation.
- **Extension of distribution-shift analysis** (Figure fig:s5.distribution) beyond QM9/Uni-Mol to other backbones and datasets.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Number of ensembles not specified"** — The paper defers the exact count to the appendix (\cref{appsec:uncertainty}), which is stripped by the parser. The information exists in the original submission.
- **"MC Dropout claim is vague without quantitative backing"** — The statement "MC Dropout also exhibits a similar trend, albeit less pronounced" (§5, line 260) is a reasonable qualitative observation in an analysis section, not a formal claim requiring a p-value.
- **"Missing analysis of ChemBERTa/GROVER expressiveness-calibration trade-off"** — The paper already discusses multiple backbones (Uni-Mol, ChemBERTa, and DNN) in §5, lines 275–280.
- The distribution-shift analysis being limited to QM9/one backbone is scope-appropriate; the paper cannot cover every combination.

## Novel Insights

The harsh critic's observation that the BBP/SGLD regression recommendation is partially undercut by the paper's own evidence (good calibration metrics but poor error-variance correlation) is genuinely insightful and not fully surfaced in the paper's own discussion. This tension between distributional calibration and informativeness is a known issue in UQ, but the paper's framing could better address it. No other novel insights emerge beyond the paper's own contributions.

## Suggestions

- Report standard deviations (or at least min/max ranges) for all metrics across the three seeds. This alone would substantially strengthen the paper's central contribution.
- In the conclusion, qualify the BBP/SGLD recommendation: note that while they achieve strong calibration scores (NLL, CE), their inflated variance and weak error correlation limit practical utility for tasks like selective prediction.
- Add a brief discussion of whether conclusions are expected to generalize to multi-class classification (or explicitly scope this to binary settings).
- Consider adding a runtime comparison table or a note on computational cost differences (e.g., Deep Ensembles vs. single-model methods).

## Score and Decision

### Calibration Details

**Round 1 bracket:** [5.0, 6.5], determined from three band queries.

**Round 2 anchors read in full:**
- **PepBenchmark (6.0, Accept Poster)** – A standardized peptide ML benchmark with strong dataset unification and preprocessing. MUBen is slightly weaker due to the variance reporting gap.
- **3DCS (5.5, Accept Poster)** – Molecular representation benchmark evaluating conformational sensitivity. MUBen is comparable in scope and contribution quality.
- **MolLangBench (5.0, Accept Poster)** – Molecular language benchmark. MUBen is stronger in terms of breadth of evaluation and insight depth.
- **ECHO (6.5, Accept Poster)** – Long-range graph propagation benchmark with rigorous hyperparameter tuning. MUBen is weaker; ECHO's experimental rigor sets a higher bar.
- **Retinal UQ Benchmark (5.5, Reject)** – UQ benchmark in clinical AI. Similar UQ evaluation scope; MUBen covers more UQ methods and backbones but shares the limitation of being a pure benchmark without methodological novelty.
- **Equivariant UQ (4.5, Reject)** – Method paper on UQ for molecular vectors. Not directly comparable.

**Narrowing:** The paper sits between MolLangBench (5.0) and PepBenchmark (6.0), and is comparable to 3DCS (5.5) and the Retinal UQ benchmark (5.5). The variance reporting gap and mild overclaim on BBP/SGLD prevent it from reaching the PepBenchmark/ECHO tier, while its comprehensive coverage and clear insights elevate it above MolLangBench.

**Final score:** 5.5

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>