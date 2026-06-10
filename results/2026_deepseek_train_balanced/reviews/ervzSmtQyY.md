Here is my consolidated final review.

---

## Summary

This paper proposes Fair MEDL, a framework combining mixed effects deep learning (MEDL) with adversarial debiasing to simultaneously handle clustered (non-i.i.d.) data and improve algorithmic fairness. The method extends a base MEDL architecture with fairness-promoting adversarial subnetworks that enforce equalized odds, and is evaluated on three datasets (Adult, IPUMS, Heritage Health) across classification and regression tasks using three fairness metrics. The paper reports substantial fairness improvements in many settings while maintaining predictive performance.

## Strengths

- **OOD fairness improvements are well-documented**: The paper demonstrates that Fair MEDL improves fairness not only on in-distribution clusters but also on clusters unseen during training. For example, on IPUMS unseen occupations, TPR SD for Age dropped from 0.274 to 0.076 (72.3%) and for Sex from 0.182 to 0.060 (67.0%), all with p < 0.001 and 95% CIs from 120 runs. This goes beyond typical fairness evaluation that only considers i.i.d. or in-distribution data.

- **Confounding mitigation demonstrated via probe experiments**: The paper introduces confounding probe features and shows Fair MEDL de-weights them while standard NNet ranks them among the most important features (e.g., two probes ranked 3rd/5th on Adult, three probes in top-10 on Heritage Health eliminated entirely). This provides direct evidence that the framework jointly addresses clustered confounding and fairness.

- **Rigorous statistical methodology**: All comparisons are based on 40–120 training runs with different random seeds, 95% confidence intervals are reported, and p-values from t-tests against baselines are provided throughout. This level of rigor is uncommon in adversarial debiasing work, and the paper explicitly notes this gap in prior work.

- **Systematic comparison of adversarial debiasing vs. absolute correlation loss**: The paper evaluates both approaches on the Adult dataset and provides empirical evidence that Fair(ADB) yields more consistent fairness improvements across all sensitive variables with less accuracy degradation (1% vs 1.6% drop), justifying the design choice.

- **Extension to regression tasks**: The paper formally adapts equalized odds, demographic parity, and counterfactual fairness for regression and validates on the Heritage Health dataset, extending beyond the classification-only scope of prior adversarial debiasing work.

## Weaknesses

### Major

- **Abstract selectively reports best numbers from different metrics without transparency**: The abstract states "improves fairness by 86.4% for Age, 64.9% for Race, 57.8% for Sex, and 36.2% for Marital status." Tracing these: 86.4% for Age comes from TPR SD on IPUMS seen clusters (Mixed Effects); 57.8% for Sex comes from **counterfactual fairness** on IPUMS (Mixed Effects); 36.2% for Marital-status comes from TPR SD on IPUMS seen clusters (Mixed Effects); and the 64.9% for Race is not clearly traceable in the main results (the IPUMS Race TPR SD improvement is 58.2%, not 64.9%). These four numbers are drawn from **different metrics** and from a **single dataset** (IPUMS), presented in parallel as if they represent a unified improvement across all variables simultaneously. No single experiment achieves all four percentages at once. This presentation in the abstract is misleading — a reader would reasonably interpret the claim as aggregate or representative across experiments.

- **"Counterfactual fairness" metric is an input-perturbation approach, not the causal quantity defined by Kusner et al.**: The paper defines counterfactual fairness (Eq. 130–133) as the average absolute prediction difference when the sensitive attribute is swapped while holding all other covariates X fixed. This operationalization ignores that many covariates are causally downstream of the sensitive attribute (e.g., occupation, education are affected by sex and race). The paper does not construct a structural causal model, discuss identification assumptions, or justify why holding X fixed is appropriate for counterfactual estimation. The cited work (Kusner et al., 2017) requires a causal model for proper counterfactual estimation. While simplified perturbation-based approaches appear in the literature, the paper presents this as the formal definition without acknowledging this limitation. Since a headline improvement percentage (57.8% for Sex) and the paper's contribution claims rely on this metric, the lack of proper causal grounding is a significant issue. The paper's core contributions (equalized odds improvements via combining MEDL with adversarial debiasing) are unaffected, but the counterfactual fairness claims are not properly supported.

### Minor

- **Limited baseline comparisons**: The only fairness methods compared against are the paper's own variants (Fair(ADB) DA-NNet and Fair(ACL) DA-NNet). The DA-NNet ablation serves as a reasonable comparator — it is essentially adversarial debiasing without the MEDL random effects component, and the paper shows the full MEDL variant achieves higher accuracy (1.3% higher on seen, 1% on unseen). However, the paper would be substantially strengthened by including standard external baselines such as preprocessing methods (e.g., reweighing) or other in-process approaches. The discussion compares against Yang et al. (2023) qualitatively ("<5% improvement") without running their method, weakening the claim of superiority over prior work.

- **Hyperparameter values not reported**: The full loss function (Eq. 5) has five hyperparameters (λ_F, λ_g, λ_K, λ_FE, λ_ME) tuned via BOHB, but no chosen values, search ranges, or sensitivity analysis are reported. With this many interacting coefficients, the sensitivity of results to these choices is unknown. This limits reproducibility and makes it difficult to assess how much tuning drives the reported improvements.

- **Statistical significance conflated with practical significance**: Many comparisons with tiny absolute differences (e.g., Counterfactual Fairness for Race on Adult: 0.024 → 0.026; for Race on IPUMS: 0.030 → 0.030 unchanged with p=0.466 in one case, yet p<0.001 in another for essentially the same values) yield p < 0.001, driven by the large number of repeated runs (120). The paper should discuss the distinction between statistical and practical significance, especially for near-identical values that reach significance due to sample size.

- **Equalized odds is the only directly optimized metric**: The paper optimizes only for equalized odds but includes counterfactual fairness and demographic parity in the claimed contribution list. The argument that equalized odds "can promote counterfactual fairness and demographic parity as well" (line 147) is stated without rigorous support, and the results bear this out inconsistently (counterfactual fairness for Age on IPUMS worsens from 0.040 to 0.047; for Race on Adult it is essentially unchanged 0.024→0.025). The paper acknowledges some of these cases but the abstract and conclusion present improvements across all three metrics as a firm achievement.

### Trivial

- **Table caption copy-paste error**: The caption for Table tab:IPUMS_ARMED_CF_DP (showing Demographic Parity and Counterfactual Fairness) reads "The best fairness outcomes (min. std. dev. of classification accuracy across categories within each sensitive var.) are bolded" — the columns contain DP and CF, not classification accuracy. This appears to be an error from an earlier table.

## Nice-to-Haves

- Report computational cost (training time, model size, convergence behavior) for practical adoption.
- Apply or discuss multiple-testing correction for the many comparisons across 4 variables × 3 datasets × 2 model variants × multiple metrics.
- The paper could acknowledge that the counterfactual fairness metric used is a simplified perturbation-based approximation, distinguishing it from the causal quantity.

## Removed Points

These points were raised by reviewers but are removed or downgraded from the main review:

- **"The method lacks comparisons against any standard fairness baselines, making it impossible to assess relative effectiveness"** — Downgraded from fatal/major to minor. The paper does compare against Fair(ADB) DA-NNet, which is adversarial debiasing without MEDL — a reasonable ablation for the key question. The criticism is retained in minor form because external baselines would still strengthen the paper.
- **"Fairness improvements on unseen data may partly reflect task difficulty on small clusters"** — Removed as speculative. No evidence is provided for this claim.
- **"Headline percentages are not found in the results"** — The percentages are in the results (lines 553, 600); the issue is selective/opaque presentation, not absence.
- **"Accuracy drop should be discussed quantitatively rather than minimized"** — The paper does quantify it (~1% absolute) and discusses it (lines 346, 677). Retained as a minor note but not a distinct weakness.
- **Strength: "Fairness improvements far exceed prior work (Yang et al. <5%)"** — Weakened from a core strength. The comparison to Yang et al. is qualitative, not experimentally replicated, and belongs as a discussion point rather than a verified strength. Removed from strengths.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- Reframe the abstract to honestly report results: state which dataset, metric, and model variant each improvement number comes from. Present results in a way that avoids conflating different metrics, or report aggregate/representative numbers.
- Either (a) remove counterfactual fairness from the claimed contributions and report only equalized odds and demographic parity, or (b) explicitly acknowledge the simplified perturbation approach used and discuss the causal assumptions required for proper counterfactual estimation.
- Add at least one standard external fairness baseline to substantiate the claim that the MEDL framework contributes beyond what a standard fairness-aware network provides.
- Report the chosen hyperparameter values from BOHB tuning and include a brief sensitivity analysis for the key λ coefficients.
- Distinguish between statistical and practical significance, especially for changes of magnitude <0.01 that reach p < 0.001 due to large numbers of runs.
- Fix the table caption copy-paste error.

## Score and Decision

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>