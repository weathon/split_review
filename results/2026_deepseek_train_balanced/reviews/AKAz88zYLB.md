Now I have all the information needed. Let me write the consolidated review.

## Summary

This paper proposes a method for generating conformal prediction intervals for dose-response models with continuous treatments. The key idea is framing the evaluation of a dose-response curve across all treatment values as a covariate shift (from the observational treatment distribution to a uniform interventional distribution), then deriving propensity-based likelihood ratio weights for use in weighted conformal prediction. The paper further introduces a local variant that combines kernel-based localization with propensity weighting to produce more conditional intervals.

## Strengths

- **Clean theoretical derivation of the covariate-shift framing.** The paper formally derives (Eq. 15–16, lines 152–160) that evaluating a CADRF across all treatment values constitutes a covariate shift with likelihood ratio weight w ∝ 1/π(T|X). This cleanly connects the dose-response UQ problem to the weighted conformal prediction framework of Tibshirani et al. (2019) in a way prior work (Lei et al. 2021, Schröder et al. 2024) did not for the continuous-treatment, full-dose-response setting.

- **Local propensity weighting to reduce conservatism.** The method combines kernel localization with propensity adjustment (Eq. 18, line 178), so calibration samples near the target treatment value receive higher weight. This is a principled way to obtain more conditional (less conservative) intervals than global propensity weighting, and the paper honestly notes the trade-off in reduced effective sample size.

- **Novel synthetic benchmark (Setup 3) that stress-tests UQ under heavy confounding.** The data generation process (lines 193–198, Table 1) produces four possible dose-response functions depending on covariates, heteroscedastic noise, and heavy confounding, creating low-overlap regions where the covariate-shift correction is most needed.

- **Candid discussion of practical limitations.** The paper openly acknowledges that global propensity weighting shows high variance (line 226), that local weighting reduces effective sample size (line 279), that intervals can become infinite where data support is absent (line 226), and that only an S-learner was used (line 279). This transparency about trade-offs strengthens credibility.

## Weaknesses

### Fatal
None.

### Major

- **Results for the majority of the described experiments are not reported.** The paper describes three experimental setups (line 190) — Setup 1 (inspired by Wu & Matching 2024), Setup 2 (following Schröder et al. 2024), and Setup 3 (novel, two scenarios) — and states that 50 random seeds were used for each scenario (line 192). Yet the results section only presents qualitative descriptions of bar plots for **Setup 3 Scenario 1** (lines 224–241). No results are shown for Setup 1, Setup 2, Setup 3 Scenario 2, or any of the other scenarios. This is a significant evidential gap: the reader cannot assess whether the method succeeds in simpler settings (Setup 1), settings comparable to prior work (Setup 2), or under heteroscedastic noise (Scenario 2). The paper's core empirical claims are supported by only a fraction of the experiments that were run.

- **No numerical results are reported in tables.** The entire evaluation is conveyed through bar plots (Figures 1–2) and qualitative description. No tables of mean coverage, mean interval width, their standard deviations across the 50 seeds, or effective sample sizes are provided. For a paper whose central claim is about *guaranteeing coverage*, the absence of explicit numerical coverage values makes it difficult for readers to verify the strength of the empirical support. (The figures do exist in the original PDF and present results visually, but tables would greatly aid precision and reproducibility.)

### Minor

- **The dismissal of the most directly relevant baseline (Schröder et al. 2024) lacks substantiation.** Line 277 states that comparing with Schröder et al. "would require several years to complete the same experiments we executed in a matter of hours." No runtime analysis, complexity estimate, or even a single small-scale comparison is provided to support this claim. Since Schröder et al. is *the only prior work* applying conformal prediction to continuous treatments, a more rigorous justification — or at minimum a limited comparison — would significantly strengthen the paper.

- **The practical method uses estimated propensities that break the finite-sample coverage guarantee.** The paper correctly notes (lines 217–218) that weighted conformal prediction requires exact likelihood ratios, and that estimated propensities "can still be a valid approximation." However, no analysis is provided of how propensity estimation error affects coverage. The oracle vs. estimated comparison (line 226) discusses conservativeness but not the gap between empirical and nominal coverage. This limits what can be claimed about the practical validity of the guarantees.

- **Several experimental details are insufficiently specified.** (i) The Gaussian Process baseline is mentioned with no kernel, length-scale, or fitting details (line 219). (ii) The "CatBoost with Uncertainty" method is described by name but its citation (`duan_ngboost_2019`) references NGBoost, creating a description–citation mismatch. (iii) No effective sample sizes are reported for the reweighting methods, despite the paper acknowledging their importance (line 279).

- **The local propensity method would benefit from a clearer algorithmic specification.** The derivation correctly shows that for the test point itself, the local weight reduces to the global weight (line 180), making it clear the benefit comes from calibration sample reweighting. However, the presentation would be strengthened by a concrete algorithm showing how calibration is performed for a predefined set of treatment values.

### Trivial

- The equation on line 180 contains a typesetting artifact (`K((t-t/h))` with missing parentheses and incorrect indices) that makes the intended expression ambiguous.
- The bandwidth parameter on line 221 is truncated (`$h = 2 \cdot (0.`).
- The overlap assumption (line 27) is stated as `0 < P(T = t | X = x) < 1` for continuous T, which conflates probability mass with density — this is common in the literature but worth noting.

## Nice-to-Haves

- A comparison with Schröder et al. (2024) on at least one small-scale scenario would greatly strengthen the positioning relative to prior work.
- An analysis of how controlled misspecification of the propensity model affects coverage (e.g., comparing oracle vs. estimated vs. deliberately misspecified propensities).
- Reporting effective sample sizes alongside coverage and interval width would help readers understand the cost of reweighting in different treatment regions.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

1. **"The experimental evaluation is essentially unverifiable" (Harsh Critic, Issue 1).** The claim that "no numerical results are reported anywhere" and that "the evaluation does not constitute evidence" is overblown. Figures 1 and 2 present coverage bar plots that *do* contain quantitative information. The criticism that no tables exist is fair but downgraded to Minor above. The stronger claim that the evaluation is "unverifiable" or "not evidence" is removed because the figures in the original PDF constitute visible evidence.

2. **"The local propensity weight equation contains an apparent error" (Harsh Critic, Issue 3, part about the equation being wrong).** The critic argues that the equation should be `K((t-T_i)/h)`. However, for the *test point* X_{n+1} evaluated at treatment t, the kernel should be `K((t-t)/h)=K(0)` (a constant), not `K((t-T_i)/h)`. The paper's mathematical claim — that the local weight equals the global weight for the test point — is correct. The garbled typesetting (`K((t-t/h))`) is a parser/formatting artifact, not a derivation error. The substantive observation that the local method's benefit comes from calibration reweighting is accurate and is reflected in the Minor weakness above about clearer specification.

3. **Bandwidth truncation (Harsh Critic).** The truncated bandwidth on line 221 is a parser artifact — per hard rules, formatting artifacts from PDF extraction are not author errors.

4. **Missing appendix/proofs references.** Per hard rules, the parser strips these sections from all papers.

5. **Criticism that the no-covariate-shift-on-X assumption limits scope (Harsh Critic, section notes).** The paper explicitly states this assumption (line 164: "We assume that there is no distribution shift for X"). Criticizing the paper for having an assumption it states is not a weakness — it is proper scope definition.

6. **"Standard conformal prediction and locally weighted conformal prediction (without propensity adjustment) produce inaccurate prediction intervals" strength.** This strength is kept but qualified; it is supported by the paper's description of Figure 1.

## Novel Insights

None beyond the paper's own contributions. The reviews largely recapitulate what the paper states: the covariate-shift framing is novel and sound, the local propensity variant is a reasonable extension, and the experimental evaluation is incomplete in its current form. Neither reviewer identified a flaw in the core theoretical argument or surfaced a contradiction in the paper's logic.

## Suggestions

1. Add tables reporting mean coverage, mean interval width, and their standard deviations across the 50 seeds for **all** experimental conditions (all setups, all scenarios, both α levels). This is the single highest-leverage improvement.
2. Include the results for Setups 1 and 2, or explicitly justify why they are omitted if a space constraint applies.
3. Provide at least a limited comparison with Schröder et al. (2024) on one scenario, or supply concrete runtime estimates to justify the "several years" claim.
4. Add an analysis of how propensity estimation error impacts coverage (e.g., by comparing oracle vs. estimated vs. deliberately misspecified propensities).
5. Clarify the "CatBoost with Uncertainty" baseline — either describe how it relates to the NGBoost citation, or use a different baseline with proper citation.
6. Present the local propensity method as a step-by-step algorithm for clarity.

## Score and Decision

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>