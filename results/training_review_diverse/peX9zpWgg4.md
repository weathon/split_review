Now I have a thorough understanding of the paper and can verify the reviewer's claims. Let me produce the final consolidated review.

## Summary

This paper introduces Adaptive Shrinkage Estimation for personalized Deep Kernel Regression (pers-DKGP) to model longitudinal brain ROI trajectories. The framework combines a population-level deep kernel GP (p-DKGP) trained on a large cohort with a subject-specific GP (ss-DKGP) via a learned shrinkage weight α, where an XGBoost regressor predicts the optimal α from features. The method is evaluated on 6 brain ROIs, composite neuroimaging biomarkers (SPARE-AD/BA), and three external clinical studies (OASIS, AIBL, PreventAD), consistently outperforming LMM, GAM, deep regression, and deep mixed effects baselines in predictive accuracy.

## Strengths

- **Superior predictive accuracy consistently demonstrated across multiple settings.** The method achieves substantially lower MAE than all baselines across 6 brain ROIs, with especially large gains in AD subjects (177.66% higher MAE for LMM) and AD progressors (22.05% higher MAE for LMM). This is shown in Figure 2(a) and the quantitative analysis in Section 3.3.

- **Strong generalization to three independent external clinical studies.** The method is evaluated on OASIS, AIBL, and PreventAD—which differ in demographics, diagnosis mix, and follow-up intervals—and consistently outperforms baselines (Mean AE of 0.197±0.009, 0.259±0.006, and 0.139±0.004 respectively) with narrow confidence intervals, as shown in Figure 4.

- **Adaptive shrinkage demonstrably outperforms constant and deterministic α strategies.** The ablation (Table 1) shows that no single constant α works across ROIs (optimal α ranges from 0.3 for Lateral Ventricle to 0.7 for Thalamus), while the XGBoost-based adaptive α achieves better MAE and coverage. SHAP analysis further reveals interpretable behavior: α decreases with more observations, aligning with intuition that the subject-specific model becomes more trustworthy over time.

- **Applicability to composite neuroimaging biomarkers beyond individual ROIs.** The framework successfully extends to SPARE-AD and SPARE-BA scores (Section 3.4), demonstrating that the approach generalizes to monotonic longitudinal biomarkers of aging and Alzheimer's disease.

## Weaknesses

### Fatal

None. No error identified invalidates the paper's core claims about predictive accuracy.

### Major

- **Unjustified independence assumption in the variance combination (Section 2.4).** The combined variance formula \(v_c = \alpha^2 v_p + (1-\alpha)^2 v_s\) assumes the p-DKGP and ss-DKGP predictive distributions are independent, but they share the learned transformation Φ and are almost certainly correlated. The paper acknowledges this in the Discussion, stating it "affects only the uncertainty quantification and leaves the posterior-corrected predictive mean unaffected." This is technically true for the mean, but because the paper evaluates coverage and interval width as key metrics (Section 3.2) and claims effective uncertainty quantification, this assumption materially weakens the UQ conclusions. The ablation in Table 1 shows the adaptive method achieves lower coverage than the best constant-α baseline for some ROIs (e.g., Hippocampus R: 0.974 vs. 0.944), suggesting the intervals may be artificially narrow. The paper would benefit from either deriving a corrected variance, or providing a calibration analysis comparing achieved coverage to the nominal level. While this does not undermine the core predictive accuracy claims, it is a significant gap in the stated UQ claims.

### Minor

- **Statistical significance is not rigorously established for key comparisons.** The paper reports 95% confidence intervals in figures and makes comparative claims (e.g., percentage differences in MAE), but does not conduct paired significance tests, bootstrap confidence intervals for differences, or effect size analyses. For some diagnosis categories, the CIs of pers-DKGP appear to overlap with baselines (e.g., SPARE-BA for stable subjects and healthy controls, as acknowledged in Section 3.4: "model performance differences are minimal in stable subjects and healthy controls"). The external validation results are more convincingly separated, but formal significance testing would strengthen the core superiority claims.

- **The XGBoost α predictor lacks internal validation against oracle α values.** The two-step procedure learns optimal α values on the validation set using ground-truth full trajectories (an oracle target), then trains XGBoost to predict α from features. While the method works well in practice (external validation), the paper does not report how well the XGBoost-predicted α matches the oracle α on held-out data (e.g., correlation or MAE between predicted and oracle α). This makes it difficult to assess whether the XGBoost is learning a robust mapping or overfitting to the validation's oracle targets.

- **Φ architecture details are minimal in the main text.** The paper states Φ is an MLP (Section 2.2) but does not report the number of layers, hidden units, activation function, latent dimension L, or regularization in the main body. These details are important for reproducibility and assessing whether the deep kernel is overfitting. (The supplement likely contains this information but was not available for review.)

- **The handling of subjects with very few follow-ups could be clarified.** The method starts personalization from 4 observations (Section 2.5). For subjects with only 1–3 follow-ups, it is unclear how the method operates—is α set to 1 (purely population), or is the XGBoost applied with the available h? This edge case should be explicitly addressed.

### Trivial

- The harmonization procedure (Pomponio et al., 2020) is applied to the training data; it would be helpful to explicitly state whether the same harmonization model was applied to the external test studies or whether they were harmonized separately.

## Nice-to-Haves

- A calibration analysis comparing achieved coverage to nominal levels (e.g., 95%) across methods, along with a discussion of the coverage–width tradeoff, would substantiate the UQ claims.
- Reporting the number of parameters, training time, and computational cost would aid practical deployment decisions.
- Ablating the deep kernel itself (e.g., replacing Φ with a fixed linear transformation) would isolate whether gains come from the deep kernel, the shrinkage, or both.
- Reporting coverage and interval width for the main results (Figures 2 and 4) in addition to the ablation study would give a more complete picture of UQ performance.

## Removed Points

The following points from the reviewer are removed with justification:

- **"The theoretical justification in Supplementary Section D.1 is referenced but absent; a main review must judge what is in the paper."** — REMOVED per rules: the parser strips appendix/supplement sections; they exist in the original submission. Do not penalize for missing content that was removed by the PDF extraction pipeline.

- **"The DME method likely has a similar deep-population + subject-specific GP structure, but the paper does not discuss why it underperforms."** — PARTIALLY REMOVED: The paper does discuss this at line 180: "These issues stem from the limitations of the RBF kernel in managing multivariate, high-dimensional data." The paper provides a clear explanation, though additional analysis would be welcome.

- **"The term 'reconstruct' is used for validation subjects... the notation can be confusing."** — REMOVED as a formatting/style nitpick per rules.

- **"The paper should discuss whether the GP marginal likelihood optimization for ss-DKGP converges reliably given small h."** — DOWNGRADED: This is speculative without evidence of convergence failure. The paper starts from 4 observations, which is standard for small-data GP optimization.

- **"Details of Φ: The MLP architecture, activation, number of layers, latent dimension L, and any regularization... should be reported. These are essential for reproducibility."** — PARTIALLY REMOVED: This criticism is legitimate but the paper is a conference submission that likely defers these details to the supplement (parser-stripped). Keeping the criticism as Minor rather than removing entirely, since some architecture details should be in the main text.

## Novel Insights

The most novel observation that emerges from this review is the tension between the paper's UQ ambition and its methodological pragmatism: the independence assumption in the variance combination is a deliberate trade-off (simplicity for principled UQ) that the paper acknowledges, but then the paper proceeds to evaluate coverage as though the intervals are well-calibrated. This is not uncommon in applied GP work, but the paper would be stronger if it either embraced a different UQ evaluation (e.g., ranking methods by coverage-width tradeoff rather than claiming near-nominal coverage) or developed a more principled combination. A second insight is that the XGBoost-based α predictor is effectively a meta-learner that interpolates between population and subject-specific predictions based on features of agreement/disagreement between the two models—this meta-learning framing could be made more explicit and connected to the stacked generalization literature.

## Suggestions

1. **Address the independence assumption for UQ.** Either derive a covariance-aware combination (e.g., via a joint GP formulation) or empirically validate that the coverage is acceptable despite the assumption by reporting achieved vs. nominal coverage rates and discussing the coverage–width tradeoff explicitly.

2. **Add internal validation of the α predictor.** On a held-out subset where the full trajectory is known (e.g., a secondary split of the validation set), report the correlation or MAE between the XGBoost-predicted α and the oracle α to demonstrate that the learned mapping is faithful.

3. **Add statistical significance testing.** For the main comparisons (pers-DKGP vs. each baseline), report paired permutation tests or bootstrapped confidence intervals for the difference in MAE, stratified by diagnosis and ROI.

4. **Provide MLP architecture details in the main text.** Report the number of layers, hidden units, activation function, latent dimension L, and any regularization used for Φ.

## Score and Decision

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>