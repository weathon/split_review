## Summary
This paper extends the Ensemble Integration (EI) framework to longitudinal multimodal data by combining modality-specific base predictors (KNN, SVM, RF, etc.) with an LSTM stacker. Four configurations are systematically explored (time-dependent vs. time-distributed base predictors × time-distributed vs. longitudinal classification heads). The best configuration — time-distributed base predictors with a longitudinal LSTM stacker — is evaluated on the TADPOLE benchmark for dementia progression prediction (CN vs. MCI vs. Dementia). LEI shows improved F-measure compared to standard LSTM (early fusion) and PPAD baselines, and a static-EI-based interpretation analysis identifies clinically meaningful features that vary across time.

## Strengths
1. **Systematic architectural exploration of four LEI configurations.** The paper clearly defines time-dependent vs. time-distributed base predictors and time-distributed vs. longitudinal LSTM heads (Section 2.2, Figures 3–4). Figure 6 provides a clear comparison of all four, revealing that time-distributed base predictors + longitudinal stacker performs best, with a plausible explanation about semantic consistency and increased training data for base predictors. This ablation provides actionable insight for practitioners.

2. **Clear outperformance over the tested baselines.** The best LEI configuration achieves higher F-measure than both the multi-layered LSTM baseline and PPAD at all time points, with the gap widening at later time points (Figure 7). The two LSTM variants use the same architecture as LEI's stacker and process the same raw features (concatenated), isolating the benefit of LEI's modality-separated base predictions.

3. **Interpretability analysis identifies clinically coherent features.** Using the static EI interpretation toolkit, the paper identifies CDR-SB, Entorhinal cortical thickness, and FAQ as top predictive features, with FAQ importance increasing at later time points (Figure 8). These findings align with established Alzheimer's literature, lending face validity to the analysis.

4. **Careful data preprocessing to prevent modality dominance.** The MRI ROI modality (313 features) is split into five semantic sub-modalities (Table 1) to avoid artificial domination, and a 30% missingness threshold is applied with KNN imputation — methodological rigor that reduces risk of artifacts.

## Weaknesses
### Fatal
None. The core claims are supported by the evidence presented; the weaknesses below are addressable through strengthening the evaluation.

### Major

1. **The DWCCE loss is claimed as a contribution but never validated.** Section 2.1 introduces the double-weighted categorical cross-entropy loss (Equation 1) as "another contribution of our work" (line 56), combining class-weighting and ordinal penalties. However, no experiment compares LEI with DWCCE vs. standard CCE, class-weighted CCE, or any variant. The discussion (line 198) admits "the problem still affected performance" despite this loss. Without an ablation isolating its effect, the contribution of the loss function is unsubstantiated — the reader cannot know whether DWCCE helps, hurts, or has no effect.

2. **No statistical significance testing for the claimed superiority.** The paper reports median F-measures with standard errors over 20×5-fold CV but conducts no formal significance test (e.g., paired bootstrap, Wilcoxon signed-rank, corrected repeated k-fold CV). This is compounded by the use of "significantly worse" at line 180 ("The baseline LSTM + MLP classifier… performed significantly worse than all others over time") without any supporting test. Given Figure 7 where error bars visually overlap at several time points, the reader cannot determine whether the observed advantages are reliable.

### Minor

1. **Limited baseline comparisons relative to the breadth of the claim.** The paper cites several recent methods for multimodal sequential classification (Eslami23, Zhang11, Wang16, Zhang24; line 12) but compares LEI only against standard LSTM (early fusion) and PPAD. While the paper's specific claims about outperforming "these approaches" can be interpreted as referring only to the tested baselines, the abstract and conclusion frame the comparison more broadly ("LEI outperformed these approaches" — abstract). A more comprehensive benchmark — e.g., a multi-stream LSTM (separate per modality with late fusion) or a transformer-based approach — would substantially strengthen the paper. The current set of only three baselines (two LSTM variants + PPAD) is thin for a framework paper.

2. **Interpretation analysis uses static EI models, not LEI itself.** The paper transparently states (Section 2.4, line 105) that "we adopted an alternate approach based on the interpretation of static EI models" because LSTMs are hard to interpret. However, the abstract states "LEI's design also enabled the identification of features that were consistently important across time," and Section 4.3 says "we interpreted the best-performing LEI model." This framing conflates LEI with a separate static EI analysis. The features identified are informative, but the paper should more carefully distinguish that this is a post-hoc analysis using a different model class applied to the same data, not an intrinsic property of LEI.

3. **Claim about $t$-to-$t$ vs. $t$-to-$(t+1)$ base predictor labeling is stated without supporting data.** Line 102 asserts that "the $t$ to $t$ approach outperformed the $t$ to $t + 1$ approach in all LEI configurations" with no figure, table, or quantitative result shown. This is a methodological design choice that should be empirically backed.

4. **LSTM architecture details are missing.** The paper does not report the number of layers, hidden units, dropout, learning rate, or any hyperparameter tuning procedure for the LSTM stacker. Since the LSTM baselines use "exactly the same architecture and parameters as the corresponding stacker used in LEI" (line 149), this gap affects both reproducibility and fairness assessment — if no hyperparameter search was conducted, the same architecture may be suboptimal for raw-feature inputs, biasing the comparison in LEI's favor.

### Trivial
None.

## Suggestions
1. **Validate the DWCCE loss** with a direct ablation (LEI with DWCCE vs. standard CCE vs. class-weighted CCE) and report the results.
2. **Add a stronger multimodal baseline**, such as a per-modality LSTM with late fusion or a cross-modal attention model, to contextualize LEI's advantage over simple early fusion.
3. **Report statistical significance** between the best LEI configuration and each baseline (e.g., Wilcoxon signed-rank or paired bootstrap across CV folds).
4. **Report LSTM hyperparameters** (layers, hidden units, dropout, learning rate, tuning procedure) to support reproducibility and fair baseline comparison.
5. **Provide the supporting data** for the $t$-to-$t$ vs. $t$-to-$(t+1)$ claim, either as a table or supplementary figure.
6. **Recalibrate the abstract and conclusion** to clarify that the interpretation analysis uses static EI models (not LEI) and that the performance comparison is against the specific baselines tested.

## Score and Decision

The paper presents a clearly described and well-motivated extension of EI to longitudinal data, with a systematic ablation of four architectural configurations. The core idea is sound and the results show improvement over the tested baselines. However, three issues prevent acceptance in the current form: (1) a claimed contribution (DWCCE loss) is presented without any experimental validation; (2) the paper uses "significantly" without a statistical test, and the visual overlap in Figure 7 raises legitimate questions about whether the advantage is reliable; (3) the baseline set is too narrow to support the paper's framing. These are addressable with additional experiments, but as-is the evidence is insufficiently robust.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>

## Questions


## Decision
Reject
