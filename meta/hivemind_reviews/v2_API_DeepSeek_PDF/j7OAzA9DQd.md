## Summary
# Final Review Report

## Summary

This paper presents **Longitudinal Ensemble Integration (LEI)**, a framework that extends the existing Ensemble Integration (EI) approach to multimodal longitudinal data for sequential classification. LEI first generates modality-specific base predictions at each time point using standard classifiers (KNN, Logistic Regression, SVM, Random Forest, XGBoost), then stacks these predictions over time using a Long Short-Term Memory (LSTM) network. The authors propose four configurations of LEI, varying whether base predictors are time-dependent or time-distributed, and whether the LSTM classification head is time-distributed or longitudinal. A double-weighted categorical cross-entropy (DWCCE) loss is introduced to handle class imbalance and ordinal label structure. The framework is evaluated on the TADPOLE/ADNI dataset for predicting dementia progression (CN, MCI, Dementia) at the next visit. Results show that time-distributed base predictors combined with a longitudinal LSTM stacker performs best. LEI outperforms baseline LSTM and modified PPAD models on the evaluated task. The interpretation analysis identifies CDR-SB, entorhinal cortical thickness, and FAQ as top predictive features, consistent with established Alzheimer's literature.

**Core methodological contribution**: Extending EI from static to longitudinal multimodal data by replacing its static stacking algorithm with a sequence-to-sequence LSTM operating on per-modality, per-time-point base predictions. The DWCCE loss is an additional technical contribution to handle class imbalance with ordinal labels in a longitudinal setting.

## Strengths
1. **Clear problem framing**: The paper identifies a real and important gap — existing approaches for multimodal longitudinal data primarily rely on early fusion, which can obscure modality-specific signals. The motivation for extending EI to the longitudinal setting is clearly communicated.

2. **Methodologically systematic**: LEI is presented with four well-defined configurations (time-dependent vs. time-distributed base predictors × time-distributed vs. longitudinal classification head), and the experimental comparison across these configurations provides useful insights into design trade-offs.

3. **Clinically relevant application**: The evaluation on TADPOLE/ADNI data for dementia progression prediction addresses a clinically meaningful problem. The cohort selection (only CN or MCI at baseline, excluding irreversible dementia-to-non-dementia transitions) is appropriate.

4. **Robust evaluation design**: The use of nested 5-fold cross-validation repeated 20 times with median F-measure and standard errors provides reasonable statistical grounding. The use of macro-averaged F-measure is appropriate for the multiclass setting with class imbalance.

5. **Interpretability analysis**: The identification of top predictive features per time point (CDR-SB, entorhinal cortex measures, FAQ) and their consistency with established clinical knowledge adds practical value, demonstrating that LEI's predictions are clinically plausible.

6. **DWCCE loss contribution**: The double-weighted loss addressing both class imbalance and ordinal structure in a longitudinal setting is a technically sound contribution that could be useful beyond this specific application.

7. **Reproducibility effort**: The code is made available via an anonymized GitHub repository, and the use of a public benchmark dataset (TADPOLE/ADNI) facilitates replication.

## Weaknesses
1. **Baseline comparison confounded by input dimensionality (Major)**: The LSTM baselines receive the full 337-dimensional feature vector, while LEI's LSTM receives low-dimensional base predictions (3 classes × 8 modalities = 24 dimensions). This means the baseline LSTMs have substantially more parameters in their first layer and are solving a harder learning problem. The claimed superiority of LEI may partly reflect this capacity difference rather than the methodological innovation of modality-specific base predictors. A controlled ablation (LSTM trained on the same base predictions without the stacking framework) is needed to isolate the contribution.

2. **Causal attribution unsupported (Major)**: The abstract and conclusion assert that LEI "outperformed these approaches **due to** its use of intermediate base predictions" and that base predictions "**enabled** their better integration over time." These causal claims are not supported by the experimental design, which does not include an ablation that removes the intermediate base predictions while keeping all other factors constant. The paper's own discussion notes multiple design differences (input dimensionality, model capacity) that could explain the performance gap.

3. **Missing quantitative result reporting (Major)**: The results section (Section 4.1) describes performance entirely in qualitative terms ("preferable," "consistently performed weaker," "improved significantly") without reporting actual F-measure values, confidence intervals, or effect sizes. The phrase "improved significantly" is ambiguous — it is unclear whether this refers to statistical significance (no test reported) or practical significance (no effect size reported). Figure 6 shows curves but no numerical anchors are provided in the text.

4. **Unsupported generalizability claim (Major)**: The introduction claims LEI "is general with respect to applications, modalities, and constituent models" and "can be adapted for other data integration-based longitudinal prediction problems." LEI has been tested on exactly one dataset (TADPOLE/ADNI) with one task (3-class dementia prediction) using only structured clinical modalities. No evidence supports this broad generalizability claim.

5. **Novelty boundary unclear (Moderate)**: The paper describes LEI as a "novel" framework, but the core idea — generating per-modality base predictions and combining them via a meta-learner — is directly inherited from EI. The extension to longitudinal data is intuitive (replacing a static stacker with an LSTM). The technical challenges that made this extension non-trivial are not explicitly articulated. The paper does not compare against the straightforward baseline of training a standard LSTM on per-modality base predictions (without the stacking framework), which would isolate the value added.

6. **Missing data handling concerns (Moderate)**: KNN imputation with K=5 is used for missing values, but the proportion of imputed values is not reported. In ADNI follow-up data, missingness is likely informative (patients who progress to dementia may drop out). KNN imputation under informative missingness can introduce bias. Categorical features (e.g., sex) are treated as continuous without justification.

7. **Interpretation method mismatch (Minor)**: The feature importance analysis uses static EI models at each time point rather than the LEI LSTM stacker itself, because LSTMs are "hard to interpret." This creates a disconnect: the interpretation comes from a model that does not capture temporal dynamics, while the predictive model does. The paper acknowledges this implicitly but does not discuss how this might affect the reliability of the identified temporal patterns.

8. **DWCCE notation ambiguity (Minor)**: The DWCCE loss formula mixes scalar representation (y_t for the ordinal weight w_o) and one-hot representation (y_{t,c} for the main loss term) without clarifying the dual notation, which could cause implementation errors.

## Key Issues
### Key Issue 1: Baseline Comparison Confound (Major, Validity Risk)
**Location**: Page 8 — Benchmarks for Assessing LEI's Performance  
**Problem**: LEI's LSTM receives 24-dimensional base predictions (3 classes × 8 modalities), while baseline LSTMs receive the full 337-dimensional raw feature vector. This means baseline LSTMs have substantially more parameters in the first layer and face a harder optimization problem. When LEI outperforms these baselines, it is unclear whether the gain comes from (a) the modality-specific base prediction design, (b) the lower input dimensionality and different optimization landscape, or (c) the interaction of both.  
**Required fix**: (1) Report input dimensionalities and parameter counts for all compared methods. (2) Add a controlled ablation: train an LSTM directly on per-modality base predictions (same 24-dim input as LEI's stacker) without the EI stacking framework. This ablation isolates the contribution of the stacking design from the benefit of lower-dimensional input. (3) Discuss the capacity confound explicitly in the results.

### Key Issue 2: Unsupported Causal Claims (Major, Overclaim Risk)
**Location**: Page 1 — Abstract; Page 10 — Discussion  
**Problem**: The abstract states LEI "outperformed these approaches **due to** its use of intermediate base predictions" and "**enabled** their better integration over time." These causal attributions are not supported by the experimental design. The paper does not include an ablation that removes the intermediate base predictions while keeping everything else constant. The observed performance difference could also be explained by differences in input dimensionality, optimization dynamics, or random seed variation.  
**Required fix**: Replace causal language with evidence-consistent wording throughout. Use "is consistent with" instead of "due to" and "enabled." In the abstract, state the bounded empirical finding: "LEI achieved higher median F-measure than the evaluated baselines under the reported settings."

### Key Issue 3: Missing Numerical Results (Major, Reproducibility Risk)
**Location**: Page 9 — Section 4.1 Relative Performance of LEI Configurations  
**Problem**: The results section describes performance only qualitatively ("preferable," "weaker," "improved significantly") without reporting actual F-measure values, standard errors, or confidence intervals for any configuration at any time point. Figure 6 is referenced but the text provides no numerical anchors. The phrase "improved significantly" is ambiguous — it is not clear if this means statistical significance (no test reported) or practical significance.  
**Required fix**: Report key F-measure values ± standard errors in the text for all four configurations at each time point (baseline, month 6, 12, 24, 36). Specify whether "significant" refers to statistical significance (with test type and p-value) or observed practical improvement. If no statistical test was performed, remove "significantly" and use "notably" or "observably."

### Key Issue 4: Unsupported Generalizability Claim (Moderate, Scoping Risk)
**Location**: Page 2 — Introduction, last sentence  
**Problem**: LEI is claimed to be "general with respect to applications, modalities, and constituent models" and adaptable "for other data integration-based longitudinal prediction problems." The framework has been tested on one dataset (TADPOLE/ADNI) with one task type (3-class clinical diagnosis) using only structured clinical features. No imaging, genomic, or unstructured data were tested. This claim is unsupported.  
**Required fix**: Replace with a bounded statement: "While demonstrated here for early dementia detection, LEI's modular design makes it a candidate for other longitudinal multimodal prediction problems, though this generalizability requires future validation across diverse applications and data types."

### Key Issue 5: DWCCE Notation Ambiguity (Moderate, Implementation Risk)
**Location**: Page 4 — Equation (1)  
**Problem**: The DWCCE loss uses the same symbol y_t to represent both the true label as a scalar (for the ordinal weight w_o, where |ŷ_max − y|/C−1 + 1 uses y as a scalar index 0,1,2) and as a one-hot vector (for y_{t,c} in the main loss term). This mixed notation could lead to implementation confusion. Additionally, it is ambiguous whether argmax(ŷ) in w_o is taken over the full sequence or per time step.  
**Required fix**: Introduce separate notation: let l_t ∈ {0,1,2} be the scalar ordinal label at time t, and y_t be the one-hot encoding. Define w_o(ŷ_t, l_t) = |argmax(ŷ_t) − l_t|/(C−1) + 1, applied per time step. Update the DWCCE equation accordingly.

## Actionable Suggestions
### Suggestion 1: Add a Controlled Ablation Baseline (Must, High Impact)
Add an ablation study where a standard LSTM is trained on the same 24-dimensional base predictions (3 classes × 8 modalities) that LEI's LSTM stacker receives. This ablation, called **LEI-no-stacking** or **LSTM-on-base-predictions**, has the same input dimensionality as LEI but removes the EI-inspired stacking framework. If LEI (with stacking) outperforms this ablation, the value of the stacking meta-learner is demonstrated. If performance is similar, the gain is primarily from the modality-specific base prediction design rather than the stacking mechanism.

**Implementation**: Use the same LSTM architecture, training procedure, CV splits, and evaluation metrics as Configurations 1-4. Replace the stacking framework with direct LSTM training on base prediction sequences. Report results in a new row in Figure 6.

### Suggestion 2: Report Numerical Results and Statistical Tests (Must, High Impact)
Add a table (Table 2 in the main text) reporting median F-measure ± standard error for all four LEI configurations and all baselines at each of the four prediction time points (month 6, 12, 24, 36). For each time point, include the number of test samples. If the claim "improved significantly" is intended to mean statistical significance, add paired statistical tests (e.g., Wilcoxon signed-rank test across CV folds) and report p-values. If not, replace "significantly" with a more appropriate qualifier.

### Suggestion 3: Revise Causal Attribution Language (Must, High Impact)
Replace all causal attribution language with evidence-consistent wording across the manuscript:

- Abstract: Replace "LEI outperformed these approaches **due to** its use of intermediate base predictions, which **enabled** their better integration over time" → "LEI achieved higher median F-measure than the evaluated baselines under the reported settings, consistent with the benefit of modality-specific base predictions before temporal integration."
- Discussion Page 10: Similarly revise causal claims.
- Introduction Page 2: Replace "we extended the capabilities of EI" with "we propose Longitudinal Ensemble Integration (LEI), which extends EI's design to the longitudinal setting by [...]" (factual, non-causal).

### Suggestion 4: Bound the Generalizability Claim (Must, Medium Impact)
In the introduction and discussion, replace broad generalizability statements with bounded claims that acknowledge the limited empirical scope of this study. Suggested replacement for the last sentence of the introduction: *"While LEI's modular design makes it a candidate for other longitudinal multimodal prediction problems, this generalizability remains to be validated in future work with diverse applications, modalities, and data types beyond the structured clinical data studied here."*

### Suggestion 5: Clarify DWCCE Notation (Must, Medium Impact)
Introduce separate notation for the scalar ordinal label and the one-hot vector in Equation (1):
- Let $l_t \in \{0,1,2\}$ be the true ordinal label at time $t$.
- Let $y_t$ be the one-hot encoding of $l_t$.
- Define $w_o(\hat{y}_t, l_t) = \frac{|\text{argmax}(\hat{y}_t) - l_t|}{C-1} + 1$, applied per time step.

The updated equation: $\text{DWCCE}(y, \hat{y}) = -\sum_{t=1}^{T} \sum_{c=1}^{C} w_o(\hat{y}_t, l_t) \cdot w_t^c \cdot y_{t,c} \log(\hat{y}_{t,c})$

### Suggestion 6: Report Missing Data Characteristics and Sensitivity Analysis (Nice-to-Have, Medium Impact)
Report the proportion of imputed values per modality after the 30% threshold. Add a brief discussion of whether missingness in ADNI follow-up data may be informative (patients with progression may drop out) and how this could affect results. If feasible, add a sensitivity analysis comparing KNN imputation with complete-case analysis or multiple imputation for a subset of features.

### Suggestion 7: Clarify Categorical Feature Encoding (Nice-to-Have, Low Impact)
In the data preprocessing section (Page 7), clarify that binary categorical features (sex) were coded as 0/1 in the TADPOLE dataset, which is equivalent to one-hot encoding for 2-category variables. Remove the phrase "treated as continuous" as it may cause confusion about whether inappropriate distance metrics were applied.

### Suggestion 8: Report Hyperparameter Selection Details (Nice-to-Have, Low Impact)
Add a supplementary table listing the hyperparameter search space and selected values for each base predictor type (KNN, SVM, RF, XGBoost) and the LSTM (number of layers, hidden units, learning rate, dropout, batch size, epochs). This is critical for reproducibility.

## Storyline Options + Writing Outlines
### Current Storyline Assessment

The current manuscript follows the structure: **Problem (multimodal longitudinal data) → Prior gap (early fusion limitation) → Existing method (EI) → Extension (LEI) → Application (dementia detection) → Results → Discussion**. This arc is coherent in content but has two structural weaknesses: (1) the transition from the EI paragraph to the LEI paragraph is abrupt, with the paper's own contribution statement appearing only after a lengthy application listing of EI; (2) the contribution claims are distributed across three separate locations (end of introduction, method Section 2.1, and the DWCCE subsection) rather than consolidated.

### Recommended Storyline Revision

**Revised arc**: Clinical Motivation → Specific Gap → Proposed Solution (LEI) → Key Design Decisions → Empirical Evidence → Scoped Contribution.

### Abstract Outline (Complete)

**S1 — Problem + Domain**: "Effectively modeling multimodal longitudinal data is critical for biomedical prediction, where patient outcomes depend on diverse data modalities collected over time."

**S2 — Prior work gap**: "Existing approaches for sequential classification from such data predominantly use early fusion — concatenating modalities into a single feature vector — which can obscure modality-specific signals and limit the use of cross-modal complementarity."

**S3 — Proposed method**: "We propose Longitudinal Ensemble Integration (LEI), which first generates modality-specific base predictions at each time point and then stacks these predictions over time using an LSTM network. A double-weighted cross-entropy loss handles class imbalance and ordinal structure in longitudinal labels."

**S4 — Key result (bounded)**: "Evaluated on TADPOLE/ADNI data for dementia progression prediction (CN, MCI, Dementia), LEI achieved higher median macro F-measure than baseline LSTM and modified PPAD models under the reported settings."

**S5 — Contribution + limitation note**: "LEI's design also enables feature importance analysis across time. While demonstrated on structured clinical data, LEI's modular design is a candidate for broader longitudinal multimodal tasks pending further validation."

### Introduction Outline (Complete)

**Paragraph 1 — Problem significance + early fusion limitation** (Current P1, revised)
- Role: Establish stakes, define the problem, identify the gap.
- Claim: Multimodal longitudinal data are important for medical forecasting, but existing approaches using early fusion can obscure modality-specific signals.
- Transition: This gap motivates a need for integration methods that preserve modality-specific information while capturing temporal dependencies.
- **Mentor revision** is provided in Annotation #2 (Page 1).

**Paragraph 2 — EI framework + its limitation** (Current P2, compressed)
- Role: Introduce the relevant prior method (EI) that LEI extends.
- Claim: EI works well for static multimodal data by using per-modality base predictors + stacking, but it has not been designed for longitudinal data.
- Transition: This creates a natural extension opportunity.
- **Mentor revision**: Compress the EI application list; end with a clear gap statement: "EI has thus far only been applicable to non-longitudinal multimodal data."

**Paragraph 3 — LEI contribution + application context** (Current Page 2 P1-P2, consolidated)
- Role: Present LEI's design, the application domain, and bounded contribution claims.
- Claim: LEI extends EI by replacing its static stacker with a sequence-to-sequence LSTM operating on per-modality, per-time-point base predictions.
- Sub-claims: (1) Four configurations are possible; (2) Evaluated on TADPOLE for dementia prediction; (3) DWCCE loss addresses class imbalance in the longitudinal ordinal setting; (4) Interpretation identifies predictive features across time.
- **Key revision needed**: Remove the unsupported generalizability claim ("our approach is general with respect to applications...") and replace with bounded wording as specified in Key Issue 4.

**Paragraph 4 — Paper roadmap (NEW, optional)**
- Optional closing paragraph that briefly previews the rest of the paper structure: Section 2 describes LEI configurations, Section 3 covers experimental setup, Section 4 presents results, Section 5 discusses limitations.

## Priority Revision Plan
### P0 Items (Must — Publication-Critical)

| ID | Issue | Location | Action | Expected Impact |
|----|-------|----------|--------|-----------------|
| P0-1 | Baseline comparison confound | Page 8 — Benchmarks | Add controlled ablation (LSTM on base predictions); report input dims & param counts | Removes the strongest threat to validity of the comparison claims |
| P0-2 | Causal attribution unsupported | Abstract, Page 10 — Discussion | Replace causal wording with evidence-consistent language throughout | Aligns claims with actual evidence strength |
| P0-3 | Missing numerical results | Page 9 — Section 4.1 | Report F-measure values ± SE in text or table; clarify "significant" | Enables readers to assess effect magnitude and reliability |
| P0-4 | DWCCE notation ambiguity | Page 4 — Equation (1) | Clarify scalar vs one-hot notation for y_t | Prevents implementation errors |

### P1 Items (Must — Important)

| ID | Issue | Location | Action | Expected Impact |
|----|-------|----------|--------|-----------------|
| P1-1 | Unsupported generalizability claim | Page 2 — Introduction | Replace with bounded wording acknowledging limited empirical scope | Improves scientific defensibility |
| P1-2 | Missing data handling transparency | Page 7 — Data preprocessing | Report proportion of imputed values; discuss informative missingness | Addresses potential bias concerns |
| P1-3 | Hyperparameter details missing | Page 7 — Training section | Add supplementary table with search space and selected values | Improves reproducibility |

### P2 Items (Nice-to-Have — Quality Improvement)

| ID | Issue | Location | Action | Expected Impact |
|----|-------|----------|--------|-----------------|
| P2-1 | Interpretation model mismatch | Page 9 — Interpretation | Acknowledge static vs dynamic model gap; optionally validate top features | Strengthens interpretability claims |
| P2-2 | Categorical feature encoding | Page 7 — Preprocessing | Clarify binary coding is equivalent to one-hot | Prevents reviewer confusion |
| P2-3 | Softmax timing ambiguity | Page 6 — Longitudinal head | Clarify per-timestep vs final-only output | Resolves minor reproducibility ambiguity |

### Revision Order

```text
Revision Strategy Roadmap
[P0-2: Fix causal language]
    → [P0-4: Fix DWCCE notation]
    → [P0-3: Add numerical results]
    → [P0-1: Add ablation experiment + parameter counts]
       (ablation experiment runs in parallel with text revisions)
    → [P1-1: Bound generalizability claim]
    → [P1-2, P1-3: Report missing data stats + hyperparameters]
    → [P2-1, P2-2, P2-3: Polish remaining items]
```

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup (Data/Split/Protocol/Baselines) | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|--------------------------------------|---------|--------------|----------------|-------------------|
| E1 | Compare LEI configurations (time-dependent vs time-distributed BPs × time-distributed vs longitudinal classification head) | TADPOLE/ADNI; 749 patients; outer 5-fold CV (80/20), inner 5-fold CV; nested CV repeated 20 times; KNNImpute missing data | Macro F-measure (median ± SE) | Time-distributed BPs + longitudinal stacker performs best, especially at later time points | LEI's design space exploration | No numerical values reported in text; trends only in Figure 6 |
| E2 | Compare best LEI configuration vs baseline LSTMs and PPAD | Same TADPOLE data; baselines: LSTM+TD classifier, LSTM+longitudinal classifier, modified PPAD; early fusion (concatenated features) | Macro F-measure (median) | LEI outperforms all baselines | LEI superiority over evaluated baselines | Input dimensionality confound (24 vs 337 dims); PPAD modified from original binary design |
| E3 | Identify most predictive features per time point | Static EI interpretation at each time point; labels at t+1 | Top-10 feature importance | CDR-SB, entorhinal thickness/volume, FAQ are top predictors | Clinical plausibility of LEI's predictions | Static model doesn't capture temporal dynamics; no validation of feature importance |

### Research-Theme Gap Diagnosis

The manuscript addresses the theme of multimodal longitudinal integration. Three research-value claims are made but not fully supported:

1. **New knowledge**: The claim that LEI "expands our knowledge of key characteristics of progression to dementia" (Page 10) is not supported — the identified features are well-established in the literature. The paper confirms known predictors rather than discovering new ones.

2. **Reproducibility/reusability**: The code is available but hyperparameter details are not reported, making exact reproduction difficult for the base predictors and LSTM.

3. **Impact on practice/understanding**: The performance improvement over baselines is promising, but the comparison confound (input dimensionality) limits the strength of the conclusion that the modality-specific approach is the cause of improvement.

### Proposed Research Experiments

#### P0 Experiment: Ablation to isolate stacking contribution
- **Target Claim**: C1 (LEI framework) — that the stacking of per-modality base predictions via LSTM improves performance
- **Hypothesis**: LEI (with stacking) outperforms an LSTM trained directly on the same base predictions (without stacking)
- **Minimal Design**: Train a standard LSTM on the same 24-dimensional per-modality base predictions that LEI's stacker receives. Use the same architecture, CV procedure, seeds, and evaluation metrics as the main LEI experiments. This ablation is called **LSTM-on-BP**.
- **Controls/Baselines**: Compare against (a) LEI Config 4 (best configuration), (b) LSTM-on-BP, (c) LSTM on raw features (current baseline)
- **Metrics**: Macro F-measure at each time point
- **Success Criterion**: LEI outperforms LSTM-on-BP by >0.02 F-measure at ≥3 time points
- **Estimated Cost/Time**: Low — no new data processing needed; 1-2 days for training and analysis
- **Expected Paper-Quality Gain**: High — removes the strongest validity concern about the comparison confound

#### P1 Experiment: Statistical significance testing
- **Target Claim**: C1 (LEI superiority over baselines)
- **Hypothesis**: The observed performance differences are statistically significant
- **Minimal Design**: Apply Wilcoxon signed-rank test (paired by CV fold) comparing LEI Config 4 vs each baseline at each time point
- **Controls/Baselines**: All baselines from current experiments
- **Metrics**: p-values, effect sizes (Cohen's d)
- **Success Criterion**: p < 0.05 for at least 3 of 4 time points against strongest baseline
- **Estimated Cost/Time**: Very low — statistical computation only; <1 day
- **Expected Paper-Quality Gain**: High — supports "significant" wording with quantitative evidence

#### P2 Experiment: Feature importance validation
- **Target Claim**: C3 (interpretability)
- **Hypothesis**: Removing top-10 features causes larger performance drop than removing bottom-10 features
- **Minimal Design**: For each time point, train LEI after removing the 10 most important features (identified by the interpretation algorithm) and measure performance drop. Repeat with 10 least important features as control.
- **Controls/Baselines**: Full-feature LEI performance; bottom-10 feature removal
- **Metrics**: Macro F-measure drop at each time point
- **Success Criterion**: Top-10 removal causes ≥2x larger drop than bottom-10 removal
- **Estimated Cost/Time**: Low — no new models needed; 1 day
- **Expected Paper-Quality Gain**: Medium — strengthens the interpretability claim with quantitative validation

```text
Experiment Upgrade Plan
[P0: LEI vs LSTM-on-BP ablation]   →  Validity of stacking contribution
[P1: Statistical significance]     →  Reliability of performance claims
[P2: Feature importance removal]   →  Validation of interpretability
       ↓
Integrated revision: stronger claims, bounded scope, validated evidence
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score**: 5.5 / 10

**Rationale**: The paper addresses a relevant problem and presents a systematic exploration of LEI configurations. The core methodological contribution — extending EI to longitudinal multimodal data — is sensible but incremental. The evaluation is thorough in its use of nested CV with 20 repetitions, but the comparison is confounded by input dimensionality differences between LEI and baselines, which weakens the main performance claim. The results are reported only qualitatively without numerical values, preventing independent assessment of effect magnitude. Several claims (causal attribution, generalizability) overreach the available evidence. The DWCCE loss is a reasonable technical contribution. The interpretation analysis adds practical value, though it relies on a static model rather than the dynamic LEI framework.

**Post-Revision Target**: [6.5, 7.5] / 10

**Prerequisites**: To reach this target, the following must be addressed:
- Add the controlled ablation experiment (LSTM on base predictions) to resolve the comparison confound (P0-1)
- Replace causal language with evidence-consistent wording throughout (P0-2)
- Report numerical F-measure values and statistical tests (P0-3)
- Fix DWCCE notation (P0-4)
- Bound generalizability claims (P1-1)

If these revisions are executed, the paper would present a methodologically sound framework with claims appropriately bounded by the available evidence, supporting a score in the 6.5-7.5 range.