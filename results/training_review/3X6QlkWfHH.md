Now I have all the information I need to write the consolidated review.

---

## Summary

This paper proposes a continuous-time gray-box state-space model for quantifying patient-specific opioid responsiveness from observational post-surgical pain data. The method combines a mechanistic SDE (grounded in PK/PD opioid effect-site concentration models) with black-box predictors that provide covariate-informed priors, trained via an EM procedure with MCMC-based E-steps. The method is evaluated on simulated data and applied to a large real-world cohort of 21,652 surgical cases, yielding estimated responsiveness rankings that partially recapitulate known opioid potencies and associate with postoperative outcomes.

## Strengths

- **Novel EM-based gray-box framework for incorporating covariates into mechanistic state-space models.** The core idea (Section 3.3) — using black-box predictors to provide covariate-informed priors within a mechanistic SDE, iteratively refined via EM — is methodologically interesting and goes beyond existing gray-box approaches (e.g., Zou et al. 2024, Takeishi & Kalousis 2023) that cancel or regularize black-box components. The framework is principled and potentially generalizable to other domains.

- **Principled integration of established pharmacology (PK/PD) with data-driven components.** The use of Stanpump-based effect-site concentration estimates (Shafer et al., 1990; Lamminsalo et al., 2019) grounds the model inputs in well-established pharmacology. This is a sensible gray-box design that leverages domain knowledge where it is strong and uses data-driven learning where it is needed.

- **Uncertainty quantification via full posterior distributions.** Using NUTS to sample the joint posterior of latent pain state and responsiveness (Section 3.2) yields credible intervals that widen with observation sparsity (Section 5), which is a practical advantage over point-estimate-only methods in clinical decision-making.

- **Large-scale real-world application.** The study covers 21,652 surgical cases with detailed medication and pain records, which is a substantial resource. The method handles an average of 16.3 irregularly timed observations per patient over 24 hours.

- **Systematic simulation ablation confirms the value of covariate-informed priors under controlled conditions.** Table 2 shows that when covariates are informative of the opioid responsiveness parameter, using covariate-informed priors improves concordance and rank correlation; when covariates are uninformative, there is no performance gain. This validates the core mechanism of the EM procedure.

## Weaknesses

### Fatal
None.

### Major

1. **No comparisons against any baseline method.** The paper evaluates only its own method (with and without covariate-informed priors). There are no comparisons to simpler alternatives such as a linear mixed model regressing pain scores on opioid ESC, a purely mechanistic population model, a black-box neural ODE, or even a model that ignores opioid administration entirely. Without baselines, the reader cannot assess whether the complexity of the proposed EM procedure adds value over trivial alternatives, which is a fundamental evidential gap for the paper's central claim of a "principled" approach.

2. **The key "recapitulation of known potencies" is only partial, with a large unexplained discrepancy.** The fentanyl/hydromorphone ratio (4.9 vs. literature ~7.5) is in the ballpark, but the hydromorphone/oxycodone ratio (12.8 vs. literature 2.0–2.7) is off by a factor of 4–6×. The paper acknowledges this and offers a speculative explanation (timing of oxycodone administration), but the discrepancy is large enough to undermine the claim that the model "recapitulates the known relative potency of different opioids." If the model cannot correctly reproduce known relative potencies, confidence in its per-patient estimates is weakened.

3. **Outcome associations (Table 3) are raw comparisons without confounder adjustment.** Patients stratified by estimated responsiveness show differences in pain, opioid use, readmission, etc., but these are unadjusted comparisons. Patients with higher estimated responsiveness may simply be healthier, have less severe procedures, or differ on unmeasured confounders that happen to correlate with the estimated responsiveness parameter. The paper presents no causal or even covariate-adjusted analysis, making it difficult to distinguish between the method working and the method producing an artifact that correlates with general good prognosis.

4. **Simulation does not test model misspecification despite claiming to.** The abstract and introduction (line 19) both state that the method was "evaluated... its sensitivity to model misspecification in simulation." However, the simulation study (Section 3.4) only varies parameters of the *correct* model (noise magnitude σ and covariate informativeness r²). There are no misspecification scenarios: no wrong functional form for the ESC effect, no non-Gaussian noise, no time-varying aⱼ, no mis-estimated PK/PD parameters, no omitted opioids. The paper's claim about evaluating misspecification sensitivity is not supported by the experiments.

### Minor

1. **Model identifiability of the ordinal observation scale is insufficiently addressed.** The observation model (Equation 3) is an ordinal logistic model with shared thresholds β_k. The latent state x(t) has an arbitrary additive offset: shifting all β_k and x by the same constant yields identical likelihood, and the SDE only constrains *changes* in x. The paper acknowledges this in the limitations (line 232) but dismisses it as "not necessarily fatal" without a formal identifiability argument or simulation showing that aⱼ rankings are robust under reasonable violations. In real data with inevitable model misspecification, the lack of a grounded latent scale could make estimated aⱼ rankings sensitive to arbitrary threshold choices.

2. **EM procedure convergence is acknowledged as not guaranteed, but no convergence diagnostics are presented.** The paper states (line 231) that "our EM procedure is not guaranteed to converge" due to sampling noise in the E-step. Yet no convergence diagnostics are shown: no stopping rule validation, no analysis of sensitivity to random seeds or initialization, and no demonstration that the total data log-likelihood actually increased across iterations. It is not specified how many EM iterations were used in the real-world application.

3. **The additive independent-effects assumption for multiple opioids is untested.** The model (Equation 2) assumes that the effect of each opioid is linear and additive in their effect-site concentrations. Many patients received multiple opioids simultaneously (Section 3.5), and this assumption is not validated or tested for interactions (e.g., synergy or tolerance cross-effects).

4. **The proportional odds assumption of the ordinal observation model is not tested.** The same β_k thresholds are shared across all patients (Equation 3). This proportional odds assumption is stated but not tested or relaxed, and the paper notes in limitations that different patients may use the numeric pain scale differently.

5. **The paper's claim about the method's ability to "stratify patients by pain and opioid use related outcomes" would be strengthened by confounder-adjusted analysis.** As noted above, the raw comparisons in Table 3 are the only real-world evidence.

### Trivial
None.

## Nice-to-Haves

- **Misspecification robustness experiments** (non-linear dynamics, time-varying aⱼ, mis-specified PK/PD, non-Gaussian noise) would strengthen confidence in the method's applicability to real data, though these go beyond the current scope.
- **Convergence diagnostics for the EM procedure** (e.g., log-likelihood trace across iterations, sensitivity to initialization) would be helpful.
- **Posterior predictive checks** for a few example patients, showing predicted vs. observed pain score distributions, would help validate the observation model.
- **An investigation of the oxycodone discrepancy** (e.g., comparing patients who received only hydromorphone vs. only oxycodone vs. both; or examining how timing of administration affects estimates).
- **External validation** using genetic markers or experimental pain study data is a natural next step but beyond the current paper's scope.

## Removed Points

*These points are flagged to be removed from consideration; treat them with caution if referenced.*

- **Criticism about MCMC hyperparameters and black-box model architecture details (number of chains, warmup, learning rate, optimizer, early stopping, covariate encoding).** The paper includes a reproducibility statement offering source code for all methods and simulations, which mitigates these concerns. Per the meta-review guidelines, requesting granular hyperparameter values that are available in the code is classified as a nitpick.
- **Criticism that the paper does not "position itself against any specific baseline from [the] literature."** This is effectively a request for missing related-work positioning, which the meta-review guidelines prohibit from being raised as a weakness (the reviewer does not have complete knowledge of the literature).
- **Generic "strengths" from the Strength Finder that are superficial** (e.g., "clinically important problem" — important but not a technical contribution of the paper). These add no discriminative value to the assessment.
- **Criticism about small simulation sample size (n=500, 1000).** The paper explicitly demonstrates that sample size affects only confidence bound width, not point estimates, since patients are estimated independently. This is a standard and adequate design.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a tension not addressed in the paper: the EM procedure's strength — using black-box models to learn priors from MCMC posterior samples — is also its vulnerability, because the targets the black-box models are trained on are themselves noisy samples from a previous iteration. The paper acknowledges the convergence concern but does not analyze whether the procedure converges to a self-consistent solution or memorizes sampling noise. This issue is worth careful study in future work.

## Suggestions

1. **Add at least 2–3 baseline methods** to the simulation study (e.g., a population-averaged linear model with ESC input, a purely mechanistic SDE without covariates, a neural ODE). Compare ranking performance (C-index, Kendall's τ) to demonstrate that the proposed method's complexity adds value.
2. **Present confounder-adjusted analyses for Table 3** (e.g., regression with covariates for pain outcomes, stratified analyses by surgery type or preoperative pain score) to distinguish genuine stratification from confounding artifacts.
3. **Investigate and explain the oxycodone discrepancy** more thoroughly. Compare patients receiving hydromorphone alone vs. oxycodone alone vs. both. Examine whether the discrepancy persists when controlling for timing of administration.
4. **Provide convergence diagnostics** for the EM procedure on a representative subset of patients (log-likelihood trace, seed sensitivity).
5. **Add a formal identifiability analysis** for the ordinal observation model, or at minimum a simulation showing that aⱼ rankings are robust to rescaling of the latent state.
6. **Either remove the claim about "sensitivity to model misspecification"** from the abstract and introduction, or actually run misspecification experiments.

## Score and Decision

**Originality:** The EM-based framework for covariate-informed priors in mechanistic state-space models is a novel contribution, though the individual components (MCMC sampling, black-box prediction, EM) are standard.

**Importance of research question:** Highly important — quantifying opioid responsiveness could improve postoperative pain management and reduce opioid-related harm. The question is clinically significant.

**Claims supported:** Only partially. The "recapitulation of known potencies" claim is undermined by the large oxycodone discrepancy. The "stratify patients by outcomes" claim lacks confounder adjustment. The "evaluated sensitivity to misspecification" claim is not supported by the experiments. The lack of baselines means the core methodological claim cannot be assessed relative to alternatives.

**Soundness of experiments:** The simulation is clean but limited (no misspecification, no baselines). The real-world evaluation is the main weakness: unadjusted outcome associations and a partially failed potency validation.

**Clarity of writing:** Generally clear and well-structured. The model is described with appropriate mathematical detail. The limitations section is honest, though some issues are underplayed.

**Value to community:** The framework itself is of potential interest to researchers working on gray-box modeling with sparse irregular observations. However, the current evidence is insufficient to demonstrate that the method works well enough to be adopted.

**Overall:** The paper presents a genuinely interesting methodological idea applied to an important problem, but the empirical validation has critical gaps: no baselines, no confounder-adjusted outcome analysis, a large discrepancy in a key validation result, and a claim about misspecification testing that is not borne out by the experiments. The contribution is not convincingly demonstrated in its current form.

**MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>**