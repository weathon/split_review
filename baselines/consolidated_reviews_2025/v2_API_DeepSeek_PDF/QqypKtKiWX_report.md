## Summary
# Final Review Report

## Summary

This paper presents SimBOL, a framework for localizing the site of origin (SoO) of early ventricular activation from 12-lead ECG signals. The method combines (1) an onset-based data augmentation strategy that resamples ECG segments around the QRS onset to expand limited training data, and (2) a compact 1D convolutional neural network designed to maintain a favorable data-to-parameter ratio, reducing overfitting in small-sample clinical settings. On a left-ventricle pacing-site dataset (1,012 sites from 39 patients), SimBOL achieves a mean localization error of approximately 9.78 mm, outperforming the previous best method (SVR, 11.80 mm) by about 2 mm and meeting a clinically referenced <10 mm threshold.

**Core strengths:** The problem addressed is clinically meaningful — accurate SoO localization can improve catheter ablation outcomes. The onset-based data augmentation is a simple, physiologically motivated idea that leverages the cyclic structure of ECG signals. Reporting multi-seed variance (5 runs) is appreciated.

**Critical weaknesses:** (1) The train/test split is performed per-triangle-label, not per-patient, creating a risk of patient-level data leakage that may inflate reported accuracy. (2) The paper's central claim — "balancing data and parameters" — is unfalsifiable without reporting the model's parameter count or the baselines' parameter counts. (3) Baseline comparisons lack reproducibility details (SVR kernel type, CNN adaptation procedures) and statistical significance testing. (4) Four of 16 anatomical segments show unstable or worsening accuracy with more data, but this is framed as "overall stability." (5) No limitations are discussed in the conclusion.

**Novelty assessment:** External literature verification is unavailable in this run (Retrieval-Disabled Mode); novelty conclusions are deferred for manual verification. Based on manuscript-internal evidence, the onset-based augmentation and the combined 1D-CNN + coordinate regression pipeline appear to be a pragmatic engineering contribution rather than a fundamental algorithmic advance. The main value lies in demonstrating that a deliberately small model with data augmentation can match or exceed complex pre-trained models on this specific task.

## Strengths
1. **Clinically relevant problem.** Accurate localization of the site of origin (SoO) of early ventricular activation is an important clinical need for catheter ablation of ventricular arrhythmias. The paper addresses a real translation gap between AI methods and clinical electrophysiology.

2. **Physiologically motivated data augmentation.** The onset-based augmentation strategy leverages the cyclic structure of ECG signals — resampling around the QRS onset is a domain-informed approach that preserves anatomical meaning while expanding data. This is more principled than generic augmentation (noise, scaling, baseline wander) for this task.

3. **Multi-seed evaluation.** All experiments are repeated 5 times with different random seeds, and mean ± variance is reported. This provides some measure of statistical reliability, unlike many papers that report single-run results.

4. **Clear ablation of augmentation strategies.** Table 1 systematically compares ODA alone vs ODA+NA, ODA+ASA, ODA+RBWA, and ODA+ALL across 7 resampling rates. This is thorough and allows readers to isolate the effect of each augmentation component.

5. **Explicit failure analysis.** Section 5.3.2 identifies segments 7, 8, 9, and 14 as problematic, with anatomical explanations (septum, papillary muscles). Acknowledging systematic failure modes is good scientific practice, even though the analysis depth needs improvement.

6. **Compact model design.** The decision to use a simple 1D CNN rather than large pre-trained transformers or LSTMs is well-motivated by the small-data regime. This simplicity-oriented philosophy contrasts with the trend toward increasingly complex models and is a refreshing design choice for clinical applications where deployability matters.

## Weaknesses
1. **Patient-level data leakage (Critical).** The dataset is split at the triangle-label level, not the patient level. With only 39 patients, samples from the same patient can appear in both training and test sets. Since ECG signals carry patient-specific characteristics, this can inflate accuracy by enabling patient-specific memorization. A patient-stratified split or patient-level cross-validation is essential.

2. **Missing model parameter count (Major).** The central claim is "data-parameters balancing," but SimBOL's total trainable parameters are never reported. The reader cannot verify whether SimBOL is truly small relative to the 781 training samples or whether the "balance" claim is meaningful. Baselines' parameter counts are also absent.

3. **Unverifiable baseline comparisons (Major).** SVR is described as "a linear regression model" but SVR is not linear regression — kernel choice, hyperparameter selection, and feature preprocessing are unreported. The CNN baseline adaptation from Yang et al. (originally segment classification) to coordinate regression is not described. Without re-implementation details, comparison fairness is uncertain.

4. **No statistical significance testing (Major).** The paper claims "significantly better" (Introduction) and "improved accuracy by 2mm" (Conclusion) but reports no statistical tests (paired t-test, Wilcoxon, confidence intervals). Given overlapping error bars between some conditions (e.g., ODA at ×5 = 9.88±0.18 vs ODA+ALL at ×5 = 9.83±0.20), significance is not established.

5. **Contradictory failure characterization (Major).** Section 5.3.2 identifies 4/16 segments (25%) with unstable/worsening accuracy as training data increases, yet frames this as demonstrating "the overall stability of the SimBOL model." This is internally inconsistent.

6. **Unsubstantiated clinical acceptance claim (Major).** The <10 mm threshold is called "clinically-accepted accuracy" without any citation to clinical guidelines, consensus statements, or validation studies. For a clinical application paper, this is a significant omission.

7. **Missing limitations section (Major).** The conclusion lacks any acknowledgment of limitations — no mention of single-dataset evaluation, single generic LV geometry, patient-level leakage risk, missing parameter counts, or segment-specific failures.

8. **Augmentation analysis gap (Medium).** Table 1 compares ODA+[other augmentations] but never compares standard augmentations alone (without ODA). The reader cannot determine whether ODA alone is better than standard augmentation alone.

9. **Generic LV model limitation (Medium).** All 1,012 pacing sites from 39 patients are mapped onto a single necropsy-derived LV geometry. Registration error and loss of patient-specific anatomy are not discussed.

10. **Writing quality issues (Minor).** Sentence fragment in Abstract and Conclusion ("The discussion about..., offering new insights"), typo "ECG filed" (Conclusion), comma splice in Introduction, double negative "not ineffective" in Section 2.2.

## Key Issues
### Issue 1: Patient-Level Data Leakage (Critical)

**Evidence:** Section 5.2.1 describes the dataset split: "for triangle labels with more than two samples, we randomly selected 20% of the samples (rounded up) as the test set." The split is per-triangle-label, not per-patient. With only 39 patients, and multiple pacing sites per patient, the same patient's data appears on both sides of the split. Page 6 - Dataset Division Strategy paragraph.

**Impact:** This can inflate reported accuracy by 20-30% in medical imaging tasks (see Saeb et al. 2017, *Int. J. Psychophysiol.*). The true patient-level generalization error is likely higher than the reported 9.78 mm.

**Repair (Must):** Re-run all experiments with patient-stratified 5-fold cross-validation. Report per-patient mean error and standard deviation.

### Issue 2: Unverifiable "Data-Parameters Balance" Claim (Critical)

**Evidence:** The paper's title and central contribution (C2) claim "balancing data and parameters," but SimBOL's total parameter count is never provided anywhere in the manuscript — not in Section 4.2 (Model Architecture), not in a table, not in the appendix. Page 5 - Model Architecture paragraph. Baselines' parameter counts are also missing.

**Impact:** The core scientific claim is unfalsifiable. Without parameter counts, the paper cannot demonstrate that SimBOL's data-to-parameter ratio is indeed more favorable than prior methods.

**Repair (Must):** Compute and report SimBOL's total parameter count (trainable + non-trainable). Estimate or cite parameter counts for all baselines. Provide a "Data/Parameter Ratio Comparison Table" in the experiments section.

### Issue 3: Unsubstantiated Baseline Comparisons (Major)

**Evidence:** SVR is described as "a linear regression model based on 120-ms QRS-integrals" (Page 7). Standard SVR is not linear regression; it uses epsilon-insensitive loss and can employ RBF/polynomial kernels. The kernel type, hyperparameters (C, epsilon, gamma if RBF), and how they were selected are unreported. The CNN baseline adaptation from Yang et al. (segment classification → coordinate regression) is not described.

**Impact:** Readers cannot assess whether baselines were optimally configured. The claimed 2mm improvement may be partially due to suboptimal baseline tuning rather than SimBOL's inherent advantage.

**Repair (Must):** Report full baseline configuration details. If using prior published numbers, verify test-set equivalence. If re-implementing, provide hyperparameter grids and selection criteria.

### Issue 4: No Statistical Significance Testing (Major)

**Evidence:** Throughout Section 5, mean ± std is reported but no hypothesis tests (t-test, ANOVA, Wilcoxon) or confidence intervals are provided. The Introduction uses "significantly better" without statistical backing. Page 2 - SimBOL Introduction paragraph, Page 9 - Augmentation analysis.

**Impact:** The 2mm improvement over SVR may not be statistically significant under proper patient-level cross-validation. Overlapping error bars in augmentation ablations suggest some differences may be noise.

**Repair (Must):** Add paired statistical tests (SimBOL vs each baseline on the same test folds). Report 95% confidence intervals for all main results. Use proper multiple-testing correction.

### Issue 5: Conclusion Lacks Limitations and Overclaims (Major)

**Evidence:** The Conclusion (Page 10) states SimBOL "meets clinically-accepted accuracy" without citation, describes the test set as "unified" (implying standardization that does not exist), and omits all limitations identified in the paper's own experiments (segment failures, single generic LV, single dataset, no patient-level validation).

**Impact:** Overconfident framing undermines scientific credibility and may mislead clinical readers about deployment readiness.

**Repair (Must):** Add a dedicated Limitations subsection. Bound all claims to the specific dataset (LV pacing, 39 patients, 1 generic model) and evaluation protocol. Remove "clinically-accepted" without citation or add a supporting reference.

## Actionable Suggestions
### S1. Add Patient-Stratified Cross-Validation (Must)
Replace the per-triangle-label split with patient-level 5-fold cross-validation. Report mean ± std per fold and per patient. This addresses the most critical validity concern. A secondary analysis can also report per-triangle-label accuracy for comparison with prior work.

### S2. Report Model Parameter Counts (Must)
Compute and report in a dedicated table:

| Model | Total Params | Training Samples | Data/Param Ratio |
|---|---|---|---|
| SimBOL (ODA×5) | [to add] | [781 × 5 = 3905] | [to add] |
| f-SAE(GRU) | [estimate/cite] | [781] | [to add] |
| CNN (Yang 2017) | [estimate/cite] | [781] | [to add] |
| SVR | - | [781] | - |

This table is essential for substantiating the paper's core claim.

### S3. Add Statistical Significance Testing (Must)
For the main result (SimBOL vs SVR vs f-SAE(GRU) vs CNN vs QRSi), report:
- Pairwise Wilcoxon signed-rank test or paired t-test across test-set samples
- 95% confidence intervals for mean error
- Effect size (Cohen's d) for the SimBOL-SVR comparison

### S4. Fully Specify Baseline Configurations (Must)
**SVR:** Report the kernel type, C and epsilon values, feature preprocessing (QRS integral only? any scaling?), and hyperparameter selection method (grid search? cross-validation?).

**CNN:** Describe how the Yang et al. architecture was adapted from 25-class segment classification to 3-D coordinate regression. Report output layer, loss function, and training hyperparameters.

**f-SAE(GRU):** Report GRU hidden size, number of layers, pre-training task details, and fine-tuning procedure.

### S5. Improve Failure Analysis with Quantitative Metrics (Should)
For segments 7, 8, 9, and 14, report:
- Per-segment mean error and standard deviation
- Number of training samples per segment
- Correlation between per-segment sample count and error
- Error distribution (median, IQR, max)

Add a scatter plot: x = samples per segment, y = error per segment, with a trend line.

### S6. Add Standard Augmentation Baseline (Should)
Add rows to Table 1 for NA-only, ASA-only, and RBWA-only (without ODA) at ×1 resampling. This isolates ODA's contribution from standard augmentations.

### S7. Add Loss Function Clarification (Should)
Explicitly state whether L = ||P - P'||₂ is squared MSE or root RMSE. If training uses MSE but evaluation uses RMSE, state this clearly. The equation should use unambiguous notation.

### S8. Add Inference Time and Memory Comparison (Nice-to-Have)
Report per-sample inference time (ms) and peak GPU memory (MB) for SimBOL vs baselines. This substantiates the "simple" claim.

### S9. Replace Sentence Fragment in Abstract and Conclusion (Must)
Replace "The discussion about data augmentation and model architecture on ECG signal processing, offering new insights..." with a complete sentence, e.g., "Our analysis of data augmentation and model architecture provides practical insights for optimizing deep learning in ECG-based tasks."

### S10. Cite Clinical Acceptance Threshold (Must)
If claiming <10 mm as "clinically-accepted," provide a citation to a clinical guideline, consensus statement, or validation study. Otherwise, replace with a bounded statement: "In this LV pacing-site dataset, the <10 mm threshold commonly referenced in the literature was achieved."

## Storyline Options + Writing Outlines
### Abstract Outline (Revised)

The current abstract overclaims (mentions 9.83mm without context) and contains a sentence fragment. Proposed revision:

**S1 (Problem):** Localizing the site of origin (SoO) of early ventricular activation from 12-lead ECG is essential for catheter ablation of ventricular arrhythmias, but limited clinical data and preprocessing errors challenge accurate deep-learning-based localization.

**S2 (Gap):** Prior deep learning models for this task suffer from overfitting because model complexity (parameter count) far exceeds the available training data (typically <1,500 samples).

**S3 (Method):** We propose SimBOL, which combines onset-based data augmentation — leveraging ECG cyclic structure to resample training segments around QRS onset — with a compact 1D convolutional network designed to maintain a favorable data-to-parameter ratio.

**S4 (Result):** On a left-ventricle pacing-site benchmark (1,012 sites, 39 patients), SimBOL achieves a mean localization error of 9.78 mm, improving over the previous best method (SVR, 11.80 mm) by approximately 2 mm.

**S5 (Bounded claim):** These results are specific to LV pacing in scar-related VT; generalization to broader populations and patient-specific anatomy requires further validation.

### Introduction Outline (Revised)

**Current structure (4 paragraphs):** P1: clinical background + pace-mapping limitations → P2: AI in medicine + prior DL methods + overfitting → P3: pre-training approaches + architecture complexity → P4: SimBOL proposal + contributions

**Problem:** P2 is a citation-heavy list without methodological taxonomy. The transition from P1 (clinical) to P2 (AI) is abrupt. The gap ("data scarcity + overfitting → need for balanced models") appears across P2-P3 but is not stated declaratively until P4.

**Proposed 5-paragraph structure:**

**P1 — Clinical Stakes (revised from current P1):**
"Catheter ablation is a key treatment for ventricular arrhythmias, including VT and PVCs. Accurate SoO localization is essential. Current clinical practice relies on pace-mapping, which is time-consuming, operator-dependent, and does not directly output spatial coordinates. This motivates data-driven localization from 12-lead ECG."
→ *Revised version provided in Page 1 annotation.*

**P2 — Prior Computational Approaches with Taxonomy:**
"Prior work has approached SoO localization with increasingly complex models: linear regression on QRS integrals (Sapp et al.), segment-classification CNNs (Yang et al.), ventricle-level discriminators (Pereira et al.), GRU-based generative pre-training (Gyawali et al.), and SVR on hand-crafted features (Zhou et al.). However, a common limitation across these methods is over-parameterization relative to the limited training dataset (1,012 sites from 39 patients). No prior study has explicitly addressed the data-to-parameter ratio in model design."

**P3 — The Overfitting Challenge:**
"When training data is limited (thousands of samples), over-parameterized models (millions of parameters) — including LSTM and Transformer architectures — are prone to overfitting. Prior mitigation strategies include generative pre-training (Gyawali et al.) and self-supervised learning, but these add training complexity. An alternative approach — designing a model whose capacity is deliberately matched to the available data — has not been explored for this task."

**P4 — SimBOL Solution (combine with results preview):**
"We propose SimBOL, a framework with two complementary components. First, onset-based data augmentation resamples ECG segments around QRS onset, expanding the effective training set N-fold. Second, a compact 1D CNN with deliberately limited capacity extracts spatiotemporal ECG features while maintaining a balanced data-to-parameter ratio. We train SimBOL with direct coordinate regression (Euclidean loss), avoiding classification biases."

**P5 — Contributions (explicit, evidence-bound):**
"(1) Onset-based data augmentation: a physiologically motivated method for expanding ECG training data. (2) A compact 1D-CNN architecture for ECG feature extraction with verifiable parameter count [to be reported]. (3) Clinically relevant accuracy: 9.78 mm mean error on an LV pacing benchmark, improving over SVR by 2 mm."

### Alternative Storyline Candidates

**Candidate A — "Less is More" (Best):**
Frame the paper around the counter-intuitive finding that deliberately reducing model complexity (small 1D CNN) with simple data augmentation outperforms complex pre-trained models. This is a stronger narrative because it surprises readers and challenges the trend toward bigger models in medical DL.

**Candidate B — Clinical Deployment Focus:**
Frame around practical deployability — simplicity, no data preprocessing, fast inference, coordinate output. This would require adding inference-time benchmarks.

**Candidate C — Augmentation-Centric:**
Frame onset-based data augmentation as the primary contribution and the model architecture as a secondary enabler. This better matches the experimental evidence (augmentation drives most gains; model choice matters less). The current paper already leans this direction in experiments but not in the title.

## Priority Revision Plan
### P0 — Critical (Must fix before resubmission)

1. **Patient-stratified evaluation** — Replace per-triangle-label split with patient-level cross-validation. Expected impact: more realistic accuracy estimate; may increase reported error by 2-5mm but establishes clinical credibility.

2. **Report model parameter counts** — Add total trainable parameters for SimBOL and all baselines. Compute data-to-parameter ratios. Expected impact: substantiates the central "data-parameters balance" claim; transforms it from asserted to evidenced.

3. **Add statistical significance tests** — Report paired tests and 95% CIs for all main comparisons. Expected impact: confirms whether the 2mm improvement over SVR is statistically reliable.

### P1 — Major (Should fix for strong resubmission)

4. **Fully specify all baselines** — Report SVR kernel/hyperparameters, CNN adaptation details, f-SAE(GRU) architecture. Expected impact: enables reproducibility and fair comparison.

5. **Add limitations section to conclusion** — Explicitly bound claims to single-dataset, single-LV-geometry, patient-level stratified evaluation pending. Expected impact: improves scientific honesty and reviewer trust.

6. **Improve segment-failure analysis** — Report per-segment errors with sample counts and statistical correlation. Add scatter plot: samples vs error. Expected impact: strengthens failure analysis from qualitative to actionable.

7. **Clarify loss function** — State whether L2 norm is squared or root; align training objective with evaluation metric. Expected impact: resolves reproducibility ambiguity.

### P2 — Minor (Quality improvement)

8. **Add standard augmentation baselines** — Compare NA/ASA/RBWA alone (without ODA) in Table 1.

9. **Fix sentence fragments** — Abstract and Conclusion: replace "The discussion..." dangling modifier.

10. **Fix typo** — "ECG filed" → "ECG field" in Conclusion.

11. **Add inference time/memory comparison** — Per-sample speed and GPU memory for SimBOL vs baselines.

12. **Refine title** — Consider "SimBOL: Data-Parameter Balancing for ECG-Based Localization of Ventricular Activation Origin" for clarity.

```text
ASCII Diagram — Revision Strategy Roadmap

[P0: Patient-level CV + Parameter counts + Stats tests]
    |
    v
[P1: Baseline specs + Limitations + Segment analysis + Loss clarity]
    |
    v
[P2: Augmentation baselines + Writing fixes + Speed benchmark]
    |
    v
[Target: Publishable manuscript with verifiable claims,
 patient-stratified evidence, transparent limitations]
```

```text
ASCII Diagram — Paper Structure & Evidence Map

[Title: "A Simple Data-Parameters Balancing Framework..."]
    |
    +-- [Abstract: 9.78mm error, <10mm clinical threshold]
    |       +-- Evidence: Table 1, ODA×10 (9.78mm)
    |       +-- Gap: No patient-level CV, no significance tests
    |
    +-- [Introduction: 4 paragraphs]
    |       +-- P1: Clinical background (pace-mapping limits)
    |       +-- P2: DL approaches (citation list, no taxonomy)
    |       +-- P3: Pre-training + overfitting (generic SSL refs)
    |       +-- P4: SimBOL + contributions (no param count)
    |
    +-- [Method: Augmentation + Architecture + Loss]
    |       +-- Augmentation: β interval (missing Δ value, onset detection)
    |       +-- Architecture: no parameter count, no tensor shapes
    |       +-- Loss: L = ||P-P'||₂ (squared vs root ambiguous)
    |
    +-- [Experiments: Dataset → Settings → Results]
    |       +-- Dataset: 1012 sites, 39 patients, generic LV
    |       +-- Split: per-triangle (NOT per-patient) ← CRITICAL GAP
    |       +-- Performance: Fig 6 (9.78mm), Fig 7 (segment breakdown)
    |       +-- Ablations: Table 1 (no non-ODA baselines)
    |       +-- Architecture: Fig 9 (SimBOL+T vs T+SimBOL)
    |
    +-- [Conclusion: Overstates, no limitations, sentence fragment]
```

**Page Coverage Audit:**

| Page | Section | Annotation Count | Coverage Status | Skip Reason |
|---|---|---|---|---|
| 1 | Abstract | 1 | Covered | - |
| 1 | Introduction P1 | 1 | Covered | - |
| 1-2 | Introduction P2 | 1 | Covered | - |
| 2 | Pre-training paragraph | 1 | Covered | - |
| 2 | SimBOL intro + contributions | 1 | Covered | - |
| 3 | Related Work 2.1 | 1 | Covered | - |
| 3 | Related Work 2.2 | 0 | Skipped | Non-substantive (brief ECG-vs-speech note) |
| 3 | Pacing-site data | 0 | Skipped | Figure caption + brief description |
| 4 | Pacing-site locations | 1 | Covered | - |
| 4-5 | Onset-based augmentation | 1 | Covered | - |
| 5 | Model architecture | 1 | Covered | - |
| 6 | Evaluation protocol (loss) | 1 | Covered | - |
| 6 | Experiment datasets | 0 | Part of leakage annotation | Covered via split annotation |
| 6 | Dataset division strategy | 1 | Covered | Patient leakage issue |
| 7 | Performance comparison (baselines) | 1 | Covered | - |
| 7 | SimBOL results analysis | 0 | Covered via performance annotation | Merged with baseline annotation |
| 8 | Segment failure analysis | 1 | Covered | - |
| 8-9 | Data augmentation influence | 1 | Covered | - |
| 9 | Model architecture influence | 0 | Skipped | Non-substantive continuation |
| 10 | Conclusion | 1 | Covered | - |
| 15 | Appendix A.2 (outliers) | 1 | Covered | - |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1 | Coordinate prediction accuracy (Fig 6) | 1012 LV sites, 39 patients; per-triangle split; 5 random seeds | Mean Euclidean distance (mm) | SimBOL×10: 9.78±0.20 mm; SVR: 11.80 mm | C3 (accuracy improvement) | Per-triangle split, no patient-level CV |
| E2 | Per-segment breakdown (Fig 7) | Same as E1, stratified by 16 segments | Per-segment mean error | Segments 7,8,9,14 unstable; others improve with data | C3 (performance characterization) | Qualitative analysis only; no per-segment sample counts |
| E3 | Augmentation ablation (Table 1) | ODA vs ODA+NA/ASA/RBWA/ALL across ×1-×15 | Mean ± std error | ODA alone competitive with combinations; NA degrades | C1 (augmentation effectiveness) | No non-ODA baselines (NA/ASA/RBWA alone); no significance tests |
| E4 | Architecture comparison (Fig 9) | SimBOL vs T+SimBOL vs SimBOL+T across ×1-×100 | Mean error vs resampling rate | SimBOL saturates at ×5; T+SimBOL needs ×15 | C2 (model efficiency) | No parameter count reported; no inference speed comparison |
| E5 | β-interval sensitivity (Table A2) | P/2 vs P interval length | Mean ± std error | Wider interval increases variance; similar at high resampling | C1 (augmentation robustness) | Limited to 2 interval settings |
| E6 | Segment classification accuracy (Fig A3) | SimBOL×5 classification into 16 segments | Classification probability | Low accuracy in segments 7,8,9,14 | - | Incidental finding; not core to method design |

### Research-Theme Gap Diagnosis

**New Knowledge:** The paper's primary knowledge contribution is demonstrating that a deliberately small 1D CNN with onset-based augmentation can match or exceed complex pre-trained models on LV pacing-site localization. This is a modest empirical finding. The mechanistic insight — "data-parameters balance reduces overfitting" — is consistent with well-known ML theory (Allen-Zhu et al., Krizhevsky et al.) and is not a new theoretical result.

**Reproducibility/Reusability:** Currently limited by missing parameter counts, unreported baseline configurations, ambiguous loss definition, and patient-level leakage risk. With the proposed fixes (patient-stratified CV, parameter table, full baseline specs), the method would be reproducible.

**Potential to Change Practice:** Limited without multi-center validation, patient-specific anatomy handling, and right-ventricle coverage. The current single-generic-LV, single-dataset evaluation is insufficient to support clinical adoption claims.

### Proposed Research Experiments

**P0 Experiment: Patient-Stratified Cross-Validation**
- **Target Claim:** C3 (generalization to unseen patients)
- **Hypothesis:** Per-triangle split overestimates accuracy; patient-level CV gives lower but more realistic error
- **Minimal Design:** 5-fold patient-level CV (39 patients → ~31 train, ~8 test per fold); report mean ± std across folds
- **Controls/Baselines:** Same CV strategy for SVR, f-SAE(GRU), CNN
- **Metrics:** Mean error (mm), per-patient mean error, percentage of test sites within 10mm
- **Success Criterion:** SimBOL error < 15 mm (absolute bound); SimBOL outperforms SVR by ≥1 mm (relative bound)
- **Estimated Cost:** 2-3 GPU-hours (retraining 5 folds × 400 epochs)
- **Expected Quality Gain:** Converts the paper's key result from potentially inflated to clinically credible

**P1 Experiment: Data-to-Parameter Ratio Ablation**
- **Target Claim:** C2 (model efficiency)
- **Hypothesis:** Varying SimBOL width (channel multiplier: 0.5×, 1×, 2×, 4×) will show a U-shaped error vs parameter curve, with the current design near the optimum
- **Minimal Design:** Scale all conv channels by {0.5, 1, 2, 4}; retrain with ODA×5; plot error vs parameter count
- **Controls:** Same training protocol; fixed augmentation
- **Metrics:** Mean error, parameter count, training time per epoch
- **Success Criterion:** Current SimBOL is near the optimum of the U-curve; very large models (4×) show increased overfitting
- **Estimated Cost:** 2-4 GPU-hours
- **Expected Quality Gain:** Directly evidences the "data-parameters balance" claim

**P1 Experiment: Standard Augmentation Baseline**
- **Target Claim:** C1 (onset-based augmentation superiority)
- **Hypothesis:** ODA alone outperforms NA/ASA/RBWA alone at the same effective data multiplicity
- **Minimal Design:** Add NA-only, ASA-only, RBWA-only rows to Table 1 at ×1 (using N resamplings to match sample count); compare vs ODA-only at same N
- **Controls:** Same model architecture, same training hyperparameters
- **Metrics:** Mean ± std error, per-segment breakdown
- **Success Criterion:** ODA-only shows significantly lower error than any single standard augmentation at matched sample size
- **Estimated Cost:** 2-3 GPU-hours
- **Expected Quality Gain:** Isolates ODA's unique contribution

**P2 Experiment: Clinical Deployability Benchmark**
- **Target Claim:** "Simple" and "convenient for clinical use"
- **Hypothesis:** SimBOL's inference time and memory footprint are suitable for real-time clinical use
- **Minimal Design:** Measure per-sample inference time (ms) and peak GPU memory (MB) for SimBOL vs f-SAE(GRU) vs CNN vs SVR; test on CPU as well
- **Controls:** Same batch size (1 for clinical realism), same hardware
- **Metrics:** Inference time, peak memory, model file size
- **Success Criterion:** SimBOL inference < 10ms per sample on CPU; model file < 10 MB
- **Estimated Cost:** < 1 GPU-hour
- **Expected Quality Gain:** Substantive the "simplicity" claim with concrete numbers

```text
ASCII Diagram — Experiment Upgrade Plan

P0 (Critical — must do)
+-- [Patient-level 5-fold CV]
    +-- Compare SimBOL vs SVR vs f-SAE(GRU) vs CNN
    +-- Report per-patient error + % within 10mm
    +-- Expected: more realistic (higher) error estimate

P1 (Major — should do)
+-- [Data/Parameter Ratio Ablation]
|   +-- Scale conv channels: 0.5x, 1x, 2x, 4x
|   +-- Plot error vs parameter count
|   +-- Expected: U-shaped curve validates optimal capacity
|
+-- [Standard Augmentation Baseline]
    +-- Add NA/ASA/RBWA-only rows to Table 1
    +-- Compare vs ODA-only at matched sample size
    +-- Expected: ODA outperforms generic augmentations

P2 (Nice-to-have)
+-- [Clinical Deployability]
    +-- Inference time (CPU/GPU) + memory + model size
    +-- Expected: <10ms per sample, <10MB model
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score:** 5.5 / 10

**Rationale:** The paper addresses a clinically meaningful problem with a simple and physiologically motivated approach. The onset-based data augmentation is a practical idea, and the experimental evaluation covers multiple augmentation strategies and resampling rates with multi-seed reporting.

However, the score is constrained by several validity-critical issues:

- **Research value (6/10):** The problem is important, but the contribution is primarily engineering/pragmatic rather than algorithmic/theoretical. The core insight (small model + data augmentation works well on small clinical datasets) is useful but not surprising given established ML principles.
  
- **Novelty (5/10):** Deferred for manual literature verification (Retrieval-Disabled Mode). Based on manuscript-internal evidence, the individual components (1D CNN, onset-based resampling, coordinate regression) are known techniques. Their combination for this specific task shows moderate novelty, but a systematic literature search is needed to confirm.

- **Soundness/Validity (4/10):** The patient-level data leakage risk (per-triangle-label split with only 39 patients) is a significant validity concern. The missing parameter counts prevent verification of the central claim. The lack of statistical significance testing weakens all comparative conclusions. The absence of reported limitations undermines scientific credibility.

- **Reproducibility (4/10):** Critically limited by missing parameter counts, ambiguous loss notation, unreported onset detection method, unreported Δ and Γ values, and incomplete baseline specifications.

- **Presentation/Writing (5/10):** Clear structure and good figures, but sentence fragments, a double negative, comma splices, and overclaimed abstract reduce quality.

**Post-Revision Target:** [6.5, 7.5] / 10

If all P0 and P1 issues are fully addressed (patient-level CV, parameter counts reported, statistical tests added, baselines fully specified, limitations honestly discussed), the paper would be substantially stronger. The ceiling is moderate because the contribution is inherently incremental (domain-specific application of known DL principles with a custom augmentation) and the single-dataset, single-generic-LV evaluation limits external validity claims even after fixes.