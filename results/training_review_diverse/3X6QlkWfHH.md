I now have a complete understanding of the paper and all the reviewer claims. Let me produce the final consolidated review.

## Summary

This paper proposes a continuous-time state-space method for estimating individual opioid responsiveness from sparse, irregularly observed pain scores. The method combines mechanistic pharmacokinetic/pharmacodynamic models of opioid effect-site concentration with black-box models that learn covariate-informed priors via an expectation-maximization algorithm. The approach is evaluated in simulation (varying noise and covariate informativeness) and applied to an observational cohort of 21,652 surgical patients to estimate responsiveness to fentanyl, hydromorphone, and oxycodone.

## Strengths

- **Principled EM framework combining mechanistic and black-box components**: The paper introduces an expectation-maximization algorithm that iteratively trains black-box models to predict prior distributions of latent parameters from covariates while preserving the mechanistic state-space structure. The KL-divergence objectives (Equations 11–12) explicitly prevent black-box models from canceling out the mechanistic component — a known problem in gray-box modeling (Section 3.3). This is a genuine methodological contribution.

- **Uncertainty quantification**: The method outputs full posterior distributions over latent pain state and opioid responsiveness for each patient (Figure 3), with uncertainty increasing for sparser data — a practical advantage over point-estimate approaches (Section 5).

- **Systematic simulation ablation**: The simulation study methodically evaluates performance across varying noise levels (σ) and covariate informativeness (r²), showing that covariate-informed priors improve estimation only when covariates are actually informative and that gains are larger when the system is more identifiable (Tables 1–2, Section 4.1).

## Weaknesses

### Fatal
None.

### Major

- **The central claim of recapitulating known opioid potencies is only partially supported, with a large unexplained discrepancy.** The paper states that the hydromorphone/oxycodone responsiveness ratio is 12.8, while the literature equianalgesic dose ratio is 2.0–2.7 — a factor-of-5 discrepancy. The offered explanation (tolerance developing over time, with oxycodone given later) is speculative and untested. The fentanyl/hydromorphone ratio (4.9 vs. literature 7.5) is also not a close match, though the paper offers a reasonable rationale about fentanyl's shorter duration of action. Because "recapitulating known potencies" is a headline result in both the abstract and introduction, this discrepancy substantially weakens the real-world validation. No confidence intervals are provided for the ratios to quantify uncertainty. (Results §4, Figure 4, Discussion §5)

- **No comparison to any baseline method.** In both simulation and real data, the method is only compared to an ablation (with vs. without covariate-informed priors). There is no baseline such as a linear model regressing pain on opioid concentration, a standard state-space model ignoring covariates, or a naïve average-pain-score approach. Since the paper's primary contribution is a method, demonstrating that its complexity yields better performance than simpler alternatives is essential. (Entire Results section)

- **Outcome stratification analysis (Table 3) is unadjusted and likely confounded.** Patients are stratified into high/low responsiveness groups, and raw outcome means are compared without adjusting for baseline covariates (preoperative pain, surgical service, comorbidities, opioid naiveté) that are known to influence both pain trajectories and opioid consumption. Since these covariates also affect the estimated responsiveness (they are used as model inputs), the observed associations could largely reflect confounding rather than a genuine relationship between estimated responsiveness and outcomes. For instance, patients with high baseline pain may have both lower estimated responsiveness (because their pain remains high despite opioids) and worse outcomes — producing the pattern in Table 3 without the model adding value. (Results §4, Table 3)

- **Simulation does not test robustness to model misspecification despite claiming to.** The introduction states the method was evaluated for "sensitivity to model misspecification" (line 19), but the simulation generates data from the exact same parametric model used for inference (same SDE, same ordinal link, same PK/PD). Only process noise σ and covariate informativeness r² are varied. No structural misspecification is tested — e.g., misspecified PK/PD, time-varying responsiveness, different ordinal link functions, or unmodeled covariates that affect the observation process. Since the real-world PK/PD models are known to be imperfect, this gap is significant. (Simulation Study §3.4, Results §4.1)

### Minor

- **EM convergence is not assessed.** The E-step uses MCMC and the M-step minimizes KL divergence; the paper notes convergence is not guaranteed (Section 5.1). Yet no diagnostics are reported: number of EM iterations, trajectory of the marginal likelihood or ELBO, or checks on whether parameter estimates stabilize. Given the computational cost (~72 hours for the full dataset), it is important to know that the procedure converges to a sensible solution. (Methods §3.3)

- **The assumption of a common ordinal intercept vector β across patients is acknowledged but untested.** If patients use the 0–10 scale differently (reporting style), the latent pain state x(t) is not comparable across patients, and estimated responsiveness conflates true responsiveness with reporting bias. The paper mentions this in limitations but does not assess its impact, e.g., by simulating heterogeneous reporting thresholds or checking whether estimated β varies systematically with covariates. (Methods §3.1, Limitations §5.1)

- **Implementation details affecting reproducibility are omitted.** The architecture of the black-box predictors f and g, optimization details, MCMC sampling parameters (number of samples, chains, warmup), and the number of EM iterations are not reported. While some of these may be in the appendix (which is stripped), they should be summarized in the main text.

- **Simulation covariates are generated as independent Gaussians**, which is a weak test — real covariates are correlated and may have non-linear relationships with the latent parameters.

### Trivial

- **No confidence intervals are reported for the potency ratios** (the key real-world result). The paper reports point estimates (medians) from the posterior distributions but does not quantify the uncertainty around the ratios themselves.

## Nice-to-Haves

- A confounder-adjusted outcome analysis (e.g., regression models controlling for preoperative pain, age, sex, surgical service, and opioid naiveté) would directly test whether the model's estimates add predictive value beyond these common factors.
- Testing at least one form of structural model misspecification (e.g., data generated with time-varying responsiveness or a different ordinal link) would substantiate the "sensitivity to model misspecification" claim.
- Reporting the full posterior over the population distribution of responsiveness coefficients (rather than just point estimates) would strengthen the potency comparison.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Strength: "Recovers known opioid potency from observational data"** — Conflicts with the verified weakness showing the hydromorphone/oxycodone ratio is off by a factor of ~5. The fentanyl/hydromorphone comparison is in the right ballpark, but the overall claim is undermined by the large discrepancy in the other comparison.

- **Strength: "Clinically meaningful patient stratification"** — Conflicts with the verified weakness that the outcome analysis (Table 3) is unadjusted and likely confounded. The observed associations cannot be attributed to the model's added value without addressing confounding.

- **Criticism: "Exclusion of patients who only received fentanyl postoperatively is noted but not justified"** — The paper justifies this (line 180: "fentanyl was only administered intraoperatively or immediately after surgery in the PACU"). The criterion is reasonable for the study design.

- **Criticism: "The text in §4.1 begins with 'Our observational cohort consisted of…', which is a methods detail, not results"** — This is a formatting/structure nitpick, not a substantive weakness.

- **Criticism: "Abstract promises sensitivity to model misspecification"** — The abstract does not mention model misspecification; it appears only in the introduction (line 19). The underlying concern (that the simulation doesn't test structural misspecification) is kept as a major weakness.

## Novel Insights

Beyond the paper's own contributions, the reviews surface two important observations. First, the hydromorphone/oxycodone potency ratio being off by a factor of ~5 is not merely a minor calibration issue — it suggests a systematic problem with how the model handles oxycodone specifically, possibly due to active metabolites, different PK/PD, or the timing of administration relative to opioid tolerance development. This points toward a targeted diagnostic that the authors should run (e.g., restricting to early time windows) before claiming the method generalizes across opioids. Second, the confounding critique of Table 3 reveals a subtle issue: because the same covariates used to inform the priors are also predictors of outcomes, the stratification analysis is circular unless adjusted. This is not a fatal flaw but means the outcome validation is currently uninformative.

## Suggestions

1. **Address the potency ratio discrepancy directly.** Compute confidence/credible intervals for each median and for the ratios. Test whether the hydromorphone/oxycodone ratio changes when restricting to early postoperative time windows (e.g., first 12 hours) where tolerance is less developed. If the ratio still deviates, acknowledge that the model may be misspecified for oxycodone (e.g., active metabolites, different PK/PD) rather than attributing it to timing without evidence.

2. **Add at least one simple baseline comparison.** In simulation, a patient-level linear regression of pain score on opioid effect-site concentration would show whether the proposed method recovers the true ranking better than a much simpler approach.

3. **Provide confounder-adjusted outcome analyses.** At minimum, include regression models that control for preoperative pain, age, sex, surgical service, and opioid naiveté when comparing high/low responsiveness groups.

4. **Report EM convergence diagnostics** — number of iterations, trajectory of the objective, and sensitivity to initialization.

5. **Scale back or substantiate the "sensitivity to model misspecification" claim.** Either test at least one form of structural misspecification (e.g., time-varying a(t), probit link instead of logistic) or rephrase to accurately describe what was evaluated (varying process noise and covariate informativeness).

## Score and Decision

This paper presents a genuinely novel and principled methodological framework. The EM-based approach for integrating black-box covariate predictors with mechanistic state-space models is a real contribution, and the simulation demonstrates that the method works under ideal conditions. However, the real-world validation has significant gaps: the central claim of recapitulating known potencies is contradicted by a factor-of-5 discrepancy for one comparison, the outcome analysis is confounded, there are no baseline comparisons, and the simulation does not test the model misspecification it advertises. These weaknesses are individually addressable but collectively mean the paper's evidence does not yet match the strength of its claims. The paper is on the right track but needs substantial revision to the validation before it can be accepted.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>