Now I have all the information I need. Let me write the consolidated review.

## Summary

This paper develops a continuous-time state-space method for estimating patient-specific opioid responsiveness from sparse, irregularly-sampled ordinal pain scores. The approach integrates known opioid pharmacokinetics/pharmacodynamics (PK/PD) via a mechanistic drift term in an SDE and uses black-box models to learn covariate-informed priors on latent parameters within an EM framework. The method is evaluated in simulation (self-consistency) and applied to electronic health records of 21,652 surgical patients, where estimated responsiveness ratios between opioids roughly recapitulate known potency ordering and stratify patients by postoperative outcomes.

## Strengths

**Principle contribution: a gray-box EM framework for latent parameter learning.** The core idea—using black-box predictors to learn priors on latent parameters from posterior samples within an EM loop, then feeding those back as informed priors—is a principled approach to incorporating covariates into mechanistic state-space models without hand-specifying their relationship to dynamics. This is demonstrated to work: in simulation (Table 2), the c-index rises from 0.62 to 0.80 when informative covariates are used, and performance does not degrade when covariates are uninformative, confirming the mechanism is sound and robust to uninformative inputs.

**Principled handling of irregular, sparse ordinal observations.** The continuous-time formulation yields analytic conditional state transition distributions (Equation 7), allowing MCMC sampling over only the observation times rather than discretizing the full time grid. This is well-suited to the clinical setting (average 16 pain observations over 24 hours) and is non-trivial with ordinal observations and a stochastic drift.

**Substantial real-world application on 21,652 patients with transparent limitations.** The paper applies the method to a large clinical cohort and reports results for fentanyl, hydromorphone, and oxycodone. The estimated responsiveness ordering (fentanyl > hydromorphone > oxycodone) matches clinical knowledge. Patients stratified by estimated responsiveness show meaningful differences across multiple independent outcomes (pain scores, opioid usage, chronic pain, readmission, length of stay). The paper explicitly acknowledges the key limitations (time-invariance assumption, ratio discrepancy, convergence concerns, shared cutpoint assumption) rather than glossing over them.

**Uncertainty quantification.** Rather than producing point estimates alone, the method provides full posterior distributions for each patient's responsiveness via NUTS, which is valuable for clinical decision-making when data are sparse.

## Weaknesses

### Fatal

None.

### Major

**1. The abstract's claim about "sensitivity to model misspecification" is unsupported.** The abstract states *"We evaluated our method and its sensitivity to model misspecification in simulation,"* but the simulation study (Section 3.4, Table 1–2) generates data from exactly the same model used for inference, varying only noise magnitude σ and covariate informativeness r². There is no misspecification scenario—no time-varying a, no non-Gaussian noise, no misspecified link function, no wrong PK/PD parameters. This is a self-consistency check, not a misspecification analysis. This overclaim needs to be corrected, and a proper misspecification analysis would substantially strengthen the paper.

**2. The hydromorphone/oxycodone ratio discrepancy is large and the explanation is speculative.** The median estimated ratio is 12.8, versus the cited literature range of 2.0–2.7—a roughly 5× discrepancy. The paper attributes this to tolerance developing because oxycodone is administered later. While this hypothesis is acknowledged as a limitation (Section 5.1), the paper does not test it (e.g., by partitioning into early versus late time windows or extending the model to allow time-varying a). If tolerance genuinely distorts the estimates this strongly, it calls into question whether the estimated a values for different opioids are measured on a comparable scale, which in turn weakens both the ratio comparison and the stratification analysis.

**3. The outcome stratification analysis (Table 3) does not adjust for confounders.** The paper reports that patients with above-median estimated responsiveness have better outcomes across multiple metrics. However, these are raw associations without any covariate adjustment (e.g., propensity-score matching, regression adjustment for surgical service, comorbidity count, baseline pain). Since the covariates used to inform the priors also plausibly correlate with outcomes, the observed associations could partly reflect confounding rather than the specific construct of opioid responsiveness. The paper discusses the difficulty of confounding in the related work section but does not apply any of those principles to its own outcome analysis.

**4. The black-box models f and g are underspecified.** The paper describes an EM procedure where f and g are trained to minimize KL divergence to posterior samples, but never states: (a) what functional form f and g take (neural network? linear model? Gaussian process? gradient-boosted tree?), (b) what distributional family they output (mean and variance of a Gaussian? parameters of a chosen family?), (c) how the KL divergence is minimized (gradient descent? closed-form?), (d) how many EM iterations were run, or (e) what convergence criterion was used. The paper states code is provided, which mitigates the reproducibility concern, but the description is too vague for a reader to understand the method's behavior without diving into code. Given that the black-box component is central to the claimed contribution, more detail in the paper itself is needed.

### Minor

**1. The ordinal cutpoints β_k are not explained.** Equation 3 uses β_k as cutpoints in the logistic ordinal model, but the paper never states how they are estimated (fixed a priori? learned? shared across patients? sampled in MCMC?). Line 232 mentions "a single set of intercepts β" but does not describe their estimation or identifiability relative to the latent state dynamics.

**2. The equianalgesic ratio calculation is not described.** The paper states ratios between median estimated a values (4.9 for fentanyl/hydromorphone, 12.8 for hydromorphone/oxycodone) but does not explain the formula used to convert estimated a (in units of log-odds per ng/mL per minute) to a "ratio." It is also unclear how the cited literature ratios (2.0–2.7, 7.5) were exactly computed or why these specific values were chosen.

**3. No ablation of the covariate priors on real data.** The simulation study includes a clean ablation (with vs. without covariate-informed priors), but the real-world analysis only presents the full model. Showing how the rankings and outcome associations change when covariate priors are removed would directly demonstrate the value added by the black-box component on real data.

**4. Hyperparameter sensitivity is not discussed.** The paper does not describe how σ (state noise) and σ₀² (prior variance) were chosen—whether they were tuned, set from domain knowledge, or selected on a validation split—nor what happens when they are misspecified.

### Trivial

None.

## Nice-to-Haves

- A controlled misspecification simulation (e.g., time-varying a, non-Gaussian noise, wrong link function) would substantiate the robustness claim in the abstract.
- Partitioning the real-data analysis by early vs. late time windows could directly test the tolerance hypothesis for the ratio discrepancy.
- Propensity-score matching or regression adjustment in Table 3 would substantially strengthen the outcome stratification evidence.

## Removed Points

- **"Sign constraints described but not implemented":** The harsh critic claimed sign constraints are "not actually implemented." This is incorrect—line 56 defines a_j ∈ ℝ^m_{≥0}, and the non-negativity constraint is part of the model definition respected by the MCMC proposal. Removed as factually wrong.
- **"Gray-box framing lacks novelty relative to prior work":** This criticism is vague and the paper cites relevant prior work (Zou et al. 2024, Takeishi & Kalousis 2023), distinguishing its approach (using black-box predictors for priors rather than dynamics). The comparison is adequate for a conference paper. Removed as insufficiently grounded.
- **Generic formatting/style nitpicks:** None present in the critic's review that qualify per the hard rules about parser artifacts.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a clear tension: the paper's main validation evidence (ratio recapitulation and outcome stratification) is simultaneously its strongest selling point for practical relevance and its weakest link methodologically. The large unaccounted discrepancy in the hydromorphone/oxycodone ratio (5× off) and the unadjusted confounders in the outcome analysis mean the real-world validation is more suggestive than conclusive. This is not unusual for a first application of a new method to complex clinical data, but it means the paper is best understood as presenting a promising framework whose clinical validity requires further substantiation, rather than as a definitive clinical tool.

## Suggestions

1. **Correct the abstract:** Remove or qualify the claim about "sensitivity to model misspecification" since the simulation does not test this. Alternatively, add a proper misspecification experiment.
2. **Add a misspecification simulation:** At minimum, test time-varying a (which the paper itself hypothesizes as the explanation for the ratio discrepancy) and a misspecified ordinal link.
3. **Provide covariate adjustment in Table 3:** Even a simple regression adjustment or stratification by surgical service would strengthen the outcome evidence considerably.
4. **Specify the black-box models:** State the architecture, training procedure, loss function details, EM iteration count, and convergence criterion. The code helps, but the paper should be readable independently.
5. **Explain the β_k estimation and the ratio formula:** These are small missing pieces that affect reader understanding.
6. **Show real-data ablation without covariate priors:** This would directly demonstrate the value of the black-box component.

## Score and Decision

The paper presents a novel and principled methodological framework for a clinically important problem. The core idea—using black-box models to learn informative priors on latent parameters within a mechanistic state-space EM procedure—is well-motivated and the simulation shows it works under ideal conditions. The real-world application on 21,652 patients is substantial and produces results that are broadly consistent with clinical expectations despite imperfect quantitative agreement. 

However, the paper has three substantive weaknesses that prevent stronger claims: (1) the abstract overclaims about misspecification analysis, (2) the largest ratio validation point (hydromorphone/oxycodone) has a 5× discrepancy that the paper acknowledges but does not adequately investigate, and (3) the outcome stratification lacks any confounder adjustment. None of these is fatal—the core methodology is sound, the limitations are acknowledged, and code is provided—but together they mean the validation is weaker than the paper's narrative suggests. These are addressable with additional analysis and more careful presentation.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>