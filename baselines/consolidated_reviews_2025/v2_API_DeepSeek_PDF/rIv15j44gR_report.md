## Summary
# Final Review Report

## Summary

This paper addresses a practical but underexplored problem in causal inference: estimating heterogeneous treatment effects (HTE) when outcomes are subject to delayed response—i.e., the treatment takes time to produce a measurable effect, and the observation window may be shorter than the response time. The authors formalize the problem by introducing potential response times D(0) and D(1) alongside the standard potential outcomes Y(0) and Y(1), and define two causal estimands: the HTE on the eventual outcome τ(x) = E[Y(1)-Y(0)|X=x] and the HTE on response times τ_D(x) = E[D(1)-D(0)|Y(0)=Y(1)=1,X=x] within the always-positive stratum. Theoretically, the paper proves identifiability of τ(x) under unconfoundedness, time-independence, and time-sufficiency, and of τ_D(x) under additional monotonicity and principal ignorability assumptions. Methodologically, the paper proposes CFR-DF (Counterfactual Regression with Delayed Feedback), which treats eventual outcomes as latent variables in an EM algorithm with IPM-regularized representation learning. Experiments on synthetic and semi-synthetic datasets (AIDS, JOBS, TWINS) show that CFR-DF consistently outperforms standard HTE methods that ignore delayed response, with PEHE reductions of 15-46% and ϵATE reductions of 17-88%.

**Strengths**: novel problem formulation that bridges the gap between HTE estimation and delayed-feedback/censored-outcome settings; rigorous identifiability analysis with careful assumptions; principled EM-based estimation framework with representation balancing.

**Core Weaknesses**: (1) strong identification assumptions (monotonicity, principal ignorability) limit practical applicability without sensitivity analysis; (2) EM implementation couples E-step and M-step through shared neural network parameters, deviating from standard EM guarantees; (3) "real-world" experiments are semi-synthetic with outcomes generated under the same parametric assumptions as the model, inflating apparent performance; (4) synthetic data generation matches model assumptions (exponential response times, logistic outcomes), creating a favorable evaluation environment.

## Strengths
**S1. Novel problem formulation.** The paper identifies a genuinely important gap in the HTE literature: existing methods assume outcomes are observable immediately, whereas in practice (drug efficacy, purchase conversion, job training effects) outcomes manifest with a delay. Formalizing this as a joint modeling problem of potential outcomes and potential response times is a well-motivated and timely contribution.

**S2. Rigorous identifiability analysis.** The paper provides a clear theoretical framework with five explicit assumptions (unconfoundedness, time independence, time sufficiency, monotonicity, principal ignorability) and proves identifiability of two causal estimands: τ(x) for the whole population and τ_D(x) for the always-positive stratum. The proofs in Appendix A.1 are logically sound and follow standard causal inference techniques (hazard-based identification, principal stratification).

**S3. Principled EM-based estimation.** The CFR-DF algorithm integrates counterfactual regression with a modified EM procedure that treats the eventual outcome as a latent variable. This provides a principled way to handle the missing-data nature of delayed feedback, and the IPM regularization addresses confounding bias from covariate shift. The flexible architecture (separate representation networks for outcome and response time) allows modular extensions.

**S4. Comprehensive experimental evaluation.** The paper evaluates on multiple synthetic datasets (varying bD, mX, observation time) and three semi-synthetic datasets (AIDS, JOBS, TWINS), comparing against nine baselines spanning representation learning, generative, and meta-learner families. The ablation study with varying observation time (Figure 2) effectively demonstrates when delayed-response modeling matters most (short observation windows) and when it converges to standard methods (long windows).

## Weaknesses
**W1. Strong identification assumptions limit practical applicability (MAJOR).** The identifiability of τ_D(x) requires Assumptions 4 (Monotonicity: Y(0) ≤ Y(1)) and 5 (Principal Ignorability). Monotonicity rules out harmful treatments, which is violated in many realistic settings (e.g., drug side effects, negative user experiences from recommendations). Principal ignorability requires that, conditional on covariates, response times are independent of principal stratum membership—an untestable assumption. The paper acknowledges these limitations in the conclusion but does not provide sensitivity analyses or partial identification bounds.

**W2. EM implementation deviates from standard EM guarantees (MAJOR).** The procedure described in Algorithm 1 and Section 4 updates neural network parameters via gradient descent after computing posterior probabilities p_i, but the same parameters ({ΦY, ΦD, hY, hD}) appear in both the E-step (computing p_i) and M-step (maximizing the weighted loss). This creates a coupling where updating parameters changes p_i, which should trigger a new E-step. The algorithm is more accurately described as a generalized EM (GEM) or EM-inspired training procedure, not a modified EM algorithm with convergence guarantees.

**W3. "Real-world" experiments are semi-synthetic with favorable assumptions (MAJOR).** The AIDS, JOBS, and TWINS datasets use real covariates X but generate all outcomes Y(w), response times D(w), and observation times T synthetically using the same generative process (exponential D, Bernoulli logistic Y) that matches the parametric assumptions of the model. This means: (a) the data generation favors CFR-DF over methods that do not model delayed response; (b) the phrase "real-world datasets" is misleading as the outcomes are not truly observed; (c) performance under model misspecification (e.g., heavy-tailed response times, non-logistic outcome mechanisms) is not evaluated.

**W4. No genuinely observational delayed-feedback evaluation.** The paper lacks any experiment where the outcome is observed with real censoring/delay from a naturally occurring or A/B-test data source. While synthetic experiments are valuable for benchmarking, the absence of a real-world case study (e.g., online conversion data with known delay) limits confidence in practical effectiveness. Even the semi-synthetic datasets use the same outcome generation as the synthetic TOY datasets.

**W5. Missing statistical significance testing.** Results are reported as mean ± SD over 10 runs, but no paired significance tests are conducted to verify whether CFR-DF's improvements over the best baseline are statistically reliable. Given that some improvements are modest (e.g., PEHE 0.404 vs 0.499 at TOY(bD=0.5)), formal testing is needed.

**W6. Percentage improvement reporting uses variable baseline.** The reported improvement percentages (23-46% PEHE reduction) are computed against the "optimal baseline method," which changes across settings and metrics. This makes the percentages non-comparable across rows of Table 2. A fixed baseline (e.g., vanilla CFR) should be used for consistent comparison.

## Key Issues
### Top-5 Ranked Defect Board

| Rank | Issue | Severity | Validity Risk | Fixability | Confidence |
|------|-------|----------|--------------|------------|------------|
| 1 | Semi-synthetic evaluation inflates apparent performance (W3) | Major | High | Medium | High |
| 2 | EM implementation lacks convergence guarantees (W2) | Major | Medium | High | High |
| 3 | Strong assumptions without sensitivity analysis (W1) | Major | High | Medium | High |
| 4 | No genuinely observational delayed-feedback validation (W4) | Major | Medium | Low | High |
| 5 | Variable baseline for improvement reporting (W6) | Minor | Low | High | High |

### Issue 1: Evaluation Favorability
The entire experimental evaluation (both TOY and semi-synthetic datasets) uses a generative process where response times follow an exponential distribution and outcomes follow a Bernoulli-logistic model. CFR-DF uses the same parametric family for its response-time model (exponential in Section 5, confirmed in Appendix A.2). This alignment between the data-generating process and model assumptions is a form of favorable evaluation: any method that correctly models the same DGP will appear to perform well. Standard HTE methods (CFR, T-learner) are at a systematic disadvantage because they do not model delayed response at all. The true test would be a setting where: (a) the true D is not exponential (e.g., Weibull, log-normal), or (b) the true relationship between X and Y is nonlinear in a way that misaligns with the logistic specification, or (c) actual observational data with natural delay.

### Issue 2: EM-ML Coupling
Standard EM provides monotone likelihood convergence because the E-step computes expectations using fixed parameters and the M-step maximizes with respect to those fixed expectations. In CFR-DF, both steps share the same neural network parameters, meaning an M-step update changes the very parameters used to compute p_i. The algorithm effectively performs a single gradient step per E-step computation, which is closer to a stochastic generalized EM. The paper should: (a) clarify whether p_i is recomputed every iteration or every epoch; (b) discuss convergence criteria; (c) report the number of EM iterations until convergence in practice.

### Issue 3: Practically Untestable Assumptions for τD(x)
The identification of τ_D(x) relies on principal ignorability: (W, Y(w)) ⟂ D(1-w) | Y(1-w), X. This is a strong conditional independence assumption that is not testable from observed data because D(1-w) is never observed for units with W=w. The paper should discuss: (a) what empirical evidence could support this assumption (e.g., if the treatment assignment is randomized, or if there is exogenous variation in T), (b) the direction of bias if the assumption is violated, (c) a sensitivity analysis framework.

### Issue 4: No Out-of-Domain Generalization
The experiments only evaluate in-distribution performance (same distribution for train and test). In practice, delayed-feedback settings often involve distribution shift (e.g., seasonality in purchase conversion, changing drug response over time). The paper should include at least one experiment with covariate shift between training and testing to evaluate robustness.

### Issue 5: Statistical Significance
All results report mean and SD over 10 runs, but no formal significance test (paired t-test, Wilcoxon) is conducted. Given that for some settings (e.g., TOY(bD=0.5): CFR-DF PEHE 0.404 vs Dragonnet 0.499) the improvements appear substantial, while for others they are modest, significance testing would strengthen the reliability claims.

## Actionable Suggestions
### Suggestion A: Add Sensitivity Analysis for Principal Ignorability (Must)
**Problem:** Principal Ignorability (Assumption 5) is untestable but required for τ_D(x) identification.
**Action:** Add a sensitivity analysis that relaxes PI by introducing a parameter Γ such that the conditional independence is allowed to deviate up to a known magnitude. For example, assume that |E[D(1)|Y(0)=1,Y(1)=1,X] - E[D(1)|Y(1)=1,X]| ≤ Γ and report how τ_D(x) changes as Γ varies from 0 (PI holds) to a maximum value.
**Evidence:** Cite Rosenbaum-style sensitivity analysis for principal stratification (Imai & Jiang, 2020).
**Expected benefit:** Quantifies the robustness of τ_D(x) estimates to PI violations.

### Suggestion B: Clarify EM Implementation and Convergence (Must)
**Problem:** The EM-ML coupling in Algorithm 1 is not a standard EM.
**Action:** 
1. Rename the procedure to "EM-inspired training" or "Generalized Expectation-Maximization (GEM)."
2. Add a subsection explaining the practical EM procedure: "At each iteration, we compute p_i from current model parameters (E-step), then take a single gradient step on the weighted loss with IPM regularization (partial M-step)."
3. Report the empirical convergence behavior: number of iterations until |L_s - L_{s-1}| < ε for each dataset.
4. Add a convergence plot in the appendix showing loss trajectories.
**Evidence:** The pseudo-code (Algorithm 1) shows a single-loop structure where loss L_s is computed and parameters updated, without a separate E-step loop.
**Expected benefit:** Removes ambiguity about the EM procedure's theoretical status.

### Suggestion C: Add Model Misspecification Experiments (Must)
**Problem:** All experiments use exponential response times matching CFR-DF's assumptions.
**Action:** Add experiments where:
1. True D(w) ~ Weibull (shape=2) instead of exponential, and CFR-DF still uses exponential model.
2. True Y(w) ~ Bern(sigmoid(θ·X^2 + c)) with higher-degree polynomial in X beyond the logistic-linear assumption.
3. Report the PEHE degradation from misspecification.
**Expected benefit:** Demonstrates robustness to (or quantifies cost of) model misspecification.

### Suggestion D: Include One Observational Delayed-Feedback Case Study (Nice-to-Have)
**Problem:** No evaluation with real delayed-outcome data.
**Action:** Use a publicly available conversion dataset with known timestamps (e.g., Criteo conversion logs, or an uplift dataset with time-to-conversion). Even if ground truth HTE is unknown, the paper can compare methods on proxy metrics (e.g., calibration of predicted conversion probabilities at different time horizons).
**Expected benefit:** Substantially increases practical credibility.

### Suggestion E: Add Statistical Significance Tests (Must)
**Problem:** No significance testing across the 10 runs.
**Action:** Add a paired t-test (or Wilcoxon signed-rank) comparing CFR-DF against the best baseline for each setting. Report p-values in the tables or a supplementary table. Flag settings where p > 0.05.
**Expected benefit:** Quantifies whether improvements are statistically reliable.

### Suggestion F: Use Fixed Baseline for Percentage Improvement (Must)
**Problem:** "Optimal baseline method" changes per setting.
**Action:** Report improvement percentages against a single fixed baseline (e.g., CFR, which is the most natural comparison since CFR-DF builds on CFR). This makes the percentages interpretable and comparable across settings.

### Suggestion G: Clarify "Real-World" Datasets (Must)
**Problem:** "Real-world" labeling is misleading.
**Action:** Rename "Real-World Datasets" to "Semi-Synthetic Datasets" or "Real-Covariate Synthetic-Outcome Datasets" throughout the paper. Clearly state in each dataset description: "Covariates X are real; outcomes Y(w), response times D(w), and observation times T are generated synthetically."

### Suggestion H: Add Policy Learning Discussion (Nice-to-Have)
**Problem:** The paper defines two estimands but does not combine them into a decision rule.
**Action:** Add a paragraph (or short subsection) on how to use τ(x) and τ_D(x) jointly: (1) if τ(x) > 0, treat; (2) if τ(x) < 0, control; (3) if τ(x) ≈ 0 (PP or NN stratum), use τ_D(x) to decide—treat only if τ_D(x) < 0 (faster response with treatment).
**Expected benefit:** Connects the theoretical results to practical policy implications.

## Storyline Options + Writing Outlines
### Current Storyline Assessment

The current introduction follows a three-paragraph structure:
1. **P1 (Page 1, lines 22-31):** General HTE importance and challenge.
2. **P2 (Page 1, lines 32-40):** Literature survey of HTE methods.
3. **P3 (Page 1, lines 41-50 to Page 2, line 38):** Gap: delayed response is ignored, with examples.
4. **P4 (Page 2, lines 39-49):** Proposed solution outline.
5. **P5 (Page 2, lines 50-62):** Detailed approach summary.
6. **P6 (Page 2, lines 63-71):** Contribution list.

**Problem:** The gap (delayed response) is introduced too late (paragraph 3). The first two paragraphs could appear in any HTE paper and do not differentiate this work. The reader has to wait until approximately the third paragraph on Page 2 to understand what is novel.

### Selected Storyline Candidate (Recommended)

**Pattern:** *Practical Problem → Formal Gap → Solution Intuition → Theoretical Results → Algorithm → Evidence*

**Abstract Outline (5 sentences):**
- **S1 (Problem):** "Estimating heterogeneous treatment effects (HTE) is important across medicine, economics, and marketing."
- **S2 (Gap):** "Existing methods assume outcomes are observed immediately, but in practice treatments take time to produce measurable effects—leading to systematic bias when the observation window is shorter than the response time."
- **S3 (Solution):** "We formalize HTE estimation with delayed response by introducing potential response times, prove identifiability of the eventual outcome HTE, and develop CFR-DF, an EM-based algorithm that jointly estimates potential outcomes and response times."
- **S4 (Evidence):** "On synthetic and semi-synthetic benchmarks, CFR-DF reduces PEHE by 23-46% over standard HTE methods and provides the first principled estimates of treatment effects on response times."
- **S5 (Scope):** "We discuss the practical limitations of the required identification assumptions and outline directions for sensitivity analysis."

**Introduction Outline (4 paragraphs):**
- **P1 (Big Picture + Gap):** "HTE estimation is critical for personalized decision-making. However, a fundamental yet overlooked challenge arises because treatments take time to produce effects—drugs require weeks to alter prognosis, users take days to respond to recommendations. Existing methods ignore this delay, implicitly assuming outcomes are observable at the time of measurement. Figure 1(a) shows how this leads to systematic false negatives and biased estimates."
- **P2 (Formalization + Related Work Positioning):** "We connect this problem to two literatures: standard HTE methods (which assume immediate outcomes) and time-to-event HTE methods (which model survival curves but assume the event indicator is known). Neither addresses the core challenge when the outcome indicator itself is censored—units with Y=1 but D>T are indistinguishable from units with Y=0. We fill this gap by modeling both the eventual outcome Y(w) and the response time D(w) jointly."
- **P3 (Method Intuition + Theoretical Results):** "We treat the eventual outcome as a latent variable and develop a modified EM algorithm within a counterfactual regression framework (CFR-DF). Theoretically, we prove identifiability of τ(x) under standard causal assumptions, and of τD(x) under additional principal ignorability. The key insight is that posterior probabilities of being a positive eventual outcome can be computed from the observed censored data and used as soft labels in an IPM-regularized loss."
- **P4 (Contributions + Evidence Preview):** "Our contributions are: (1) formalizing HTE with delayed response, (2) identifiability proofs for two estimands, (3) the CFR-DF algorithm that extends counterfactual regression to delayed feedback using EM-based learning, and (4) empirical validation on synthetic and semi-synthetic data showing consistent improvements over nine baselines."

### Current Title Recommendation

**Current:** "ESTIMATING HETEROGENEOUS TREATMENT EFFECT WITH DELAYED RESPONSE"

**Recommended:** "Estimating Heterogeneous Treatment Effects Under Delayed Response: Identifiability, EM-based Estimation, and Counterfactual Regression"

This title adds specificity ("Identifiability, EM-based Estimation, and Counterfactual Regression") and improves readability while keeping the core contribution visible.

## Priority Revision Plan
### P0 (Publication-Critical, Must-Do Before Resubmission)

| Priority | Action | Related Issue | Expected Impact | Estimated Effort |
|----------|--------|---------------|-----------------|------------------|
| P0 | Rename "real-world" datasets to "semi-synthetic" and add explicit model-misspecification experiments (Weibull D, nonlinear Y) | W3, W4 | Eliminates favorable-evaluation concern | 1-2 weeks |
| P0 | Clarify EM implementation: rename to GEM, add convergence discussion, report iteration counts | W2 | Removes theoretical ambiguity | 2-3 days |
| P0 | Add sensitivity analysis for principal ignorability (Γ-parameter approach) | W1 | Addresses strongest assumption concern | 1-2 weeks |
| P0 | Add statistical significance tests (paired t-test across 10 runs) | W5 | Provides reliability quantification | 1 day |
| P0 | Fix percentage improvement reporting: use fixed baseline (CFR) instead of varying "optimal baseline" | W6 | Consistent evaluation | 1 day |

### P1 (High Impact, Should-Do)

| Priority | Action | Related Issue | Expected Impact | Estimated Effort |
|----------|--------|---------------|-----------------|------------------|
| P1 | Add one genuinely observational case study (e.g., Criteo conversion data with delay) | W4 | Substantially increases practical credibility | 2-4 weeks |
| P1 | Introduce IPM penalty conceptually before the loss equations (Section 4) | Writing | Improves readability | 1 day |
| P1 | Add explicit policy-learning subsection connecting τ(x) and τ_D(x) | Writing | Enhances practical significance | 2-3 days |
| P1 | Add out-of-domain generalization experiment (train/test covariate shift) | Key Issues #4 | Tests robustness | 1-2 weeks |

### P2 (Quality Improvement, Nice-to-Have)

| Priority | Action | Expected Impact | Estimated Effort |
|----------|--------|-----------------|------------------|
| P2 | Rewrite abstract to include quantitative results | 1 day | Improves first-impression |
| P2 | Restructure introduction to state delayed-response gap earlier | 2 days | Improves narrative flow |
| P2 | Add error bar discussion in Figure 2 (currently only lines, no variance shading) | 1 day | Improves transparency |
| P2 | Add visual diagram for EM training loop (E-step/M-step alternation) | 2 days | Clarifies algorithm |
| P2 | Add discussion of partial identification when Assumption 3 (time sufficiency) is violated | 1-2 days | Enhances theoretical completeness |

### ASCII Diagram — Revision Strategy Roadmap

```text
[Current manuscript issues]
    |
    ├── [Evaluation favorability (W3/W4)]
    |       -> Add misspecification experiments (P0)
    |       -> Clarify dataset labeling (P0)
    |       -> Optional: observational case study (P1)
    |
    ├── [EM theory gap (W2)]
    |       -> Rename to GEM, add convergence analysis (P0)
    |       -> Add convergence plots (P2)
    |
    ├── [Strong assumptions (W1)]
    |       -> Add sensitivity analysis for PI (P0)
    |       -> Add partial identification discussion (P2)
    |
    └── [Statistical rigor (W5/W6)]
            -> Add significance tests (P0)
            -> Fix baseline for % comparisons (P0)
    
[Expected outcome after P0 fixes]
    -> Credible evaluation: misspecification robustness shown
    -> Clear algorithm: EM implementation properly documented
    -> Honest claims: assumptions bounded with sensitivity
    -> Reliable statistics: p-values support all claimed improvements
```

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|-----------|-------|---------|-------------|----------------|--------------------|
| E1 (Table 2) | HTE on eventual outcome with varying bD | TOY(bD=0,0.5,1), N=20K train, 3K test, 10 runs | PEHE, ϵATE | CFR-DF best across all bD | C1 (problem formalization) + C3 (CFR-DF algorithm) | DGP matches model assumptions; no misspecification |
| E2 (Table 3) | HTE on response times τ_D(x) | TOY(bD=0,1), same split | PEHE on P(D(1)>d)-P(D(0)>d) and τ_D(x) | CFR-DF accurately estimates response time HTE | C2 (identifiability) + C3 | Requires strong PI assumption |
| E3 (Figure 2) | Ablation: varying observation time | TOY(bD=0,1), T̄ ∈ {0.5,1,5,10,20,50} | PEHE | CFR-DF best at short T; converges to CFR at long T | C3 (algorithm effectiveness) | DGP assumes exponential D and T |
| E4 (Table 4) | HTE on eventual outcome with real covariates | AIDS (1156), JOBS (3212), TWINS (11400) | PEHE, ϵATE | CFR-DF best across all three datasets | C3 (effectiveness) + C4 (experiments) | Outcomes/survival are synthetic, not real; favorable DGP |
| E5 (Table 7, Appendix) | Varying feature dimensions | TOY(mX=5,10,20,40), bD=0.5 | PEHE, ϵATE | CFR-DF best across all mX | C3 | Same DGP alignment as E1 |

### Research-Theme Gap Diagnosis

| Research Value | Current Evidence Level | Gap |
|----------------|----------------------|-----|
| New knowledge (delayed-response HTE) | Good theoretical framework + favorable synthetic evidence | Missing: model misspecification, real-world delayed data |
| Reproducibility | Good: architecture/hyperparameters/seed reported | Acceptable: code not yet publicly available (anonymous) |
| Impact on practice/understanding | Theoretical: clear. Empirical: limited by synthetic-only evaluation | Missing: real-world case study, policy-learning demonstration |

### Proposed Research Experiments

#### P0 Experiments (Must-Do Before Resubmission)

**Exp-R1: Model Misspecification — Weibull Response Time**
- **Target Claim:** C3 (CFR-DF works under realistic conditions)
- **Hypothesis:** CFR-DF is robust to misspecification of D distribution
- **Minimal Design:** Generate D(0), D(1) ~ Weibull(shape=2, scale=exp(θ·X)) instead of exponential; keep CFR-DF's exponential assumption
- **Controls:** Same baselines as Table 2
- **Metrics:** PEHE, ϵATE
- **Success Criterion:** CFR-DF still outperforms baselines (PEHE lower by >10%), or degradation is explicitly quantified
- **Estimated Cost/Time:** 3-5 days (code adaptation + runs)
- **Expected Gain:** Eliminates favorable-evaluation concern; tests robustness

**Exp-R2: Sensitivity Analysis for Principal Ignorability**
- **Target Claim:** C2 (τ_D(x) identifiability under PI)
- **Hypothesis:** τ_D(x) estimates are sensitive to PI in predictable ways
- **Minimal Design:** Introduce bias parameter Γ such that E[D(1)|Y(0)=Y(1)=1,X] = E[D(1)|Y(1)=1,X] + δ(X), with δ(X) bounded by Γ; estimate τ_D(x) under varying Γ
- **Controls:** None (sensitivity analysis)
- **Metrics:** τ_D(x) range (min-max) as Γ varies
- **Success Criterion:** Report how τ_D(x) changes; ideally small sensitivity
- **Estimated Cost/Time:** 1-2 weeks
- **Expected Gain:** Quantifies credibility of τ_D(x) estimates

**Exp-R3: Statistical Significance**
- **Target Claim:** C3 (CFR-DF outperforms baselines)
- **Hypothesis:** Improvements are statistically significant
- **Minimal Design:** Paired t-test (or Wilcoxon) comparing CFR-DF vs best baseline per setting, across 10 runs
- **Controls:** Bonferroni correction for multiple comparisons
- **Metrics:** p-value, effect size
- **Success Criterion:** p < 0.05 for most settings
- **Estimated Cost/Time:** 1 day
- **Expected Gain:** Statistical reliability

#### P1 Experiments (High-Value, Should-Do)

**Exp-R4: Out-of-Domain Generalization**
- **Target Claim:** C3 (robustness)
- **Hypothesis:** CFR-DF maintains advantage under covariate shift
- **Minimal Design:** Train on TOY(bD=0.5, mX=20), test on TOY with shifted X distribution (e.g., X~N(1, I) instead of X~N(0, I))
- **Controls:** Same baselines
- **Metrics:** PEHE, ϵATE
- **Success Criterion:** CFR-DF PEHE degradation < 20% relative; still best
- **Estimated Cost/Time:** 1 week
- **Expected Gain:** Tests generalization robustness

**Exp-R5: Non-Binary Outcome Extension**
- **Target Claim:** C1 (problem generalizability)
- **Hypothesis:** CFR-DF framework extends to continuous Y
- **Minimal Design:** Generate continuous Y(w) with censoring threshold; adapt outcome model to Gaussian (linear regression) instead of Bernoulli; compare against standard continuous HTE methods
- **Controls:** CFR (adapted), T-learner
- **Metrics:** RMSE of τ(x)
- **Success Criterion:** CFR-DF outperforms baselines
- **Estimated Cost/Time:** 1-2 weeks
- **Expected Gain:** Broadens applicability

### ASCII Diagram — Experiment Upgrade Plan

```text
P0 (Before resubmission):
    [Current experiments: favorable DGP]
        -> Add Weibull misspecification (Exp-R1)
        -> Add PI sensitivity analysis (Exp-R2)
        -> Add significance tests (Exp-R3)
    
P1 (Before resubmission, if time permits):
    [Robustness gap]
        -> Add covariate shift test (Exp-R4)
        -> Add continuous outcome test (Exp-R5)
    
P2 (Future work):
    [External validity gap]
        -> Add observational case study (e.g., Criteo data)
        -> Add multiple treatments extension
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6.5 / 10**

This score reflects the paper's genuine conceptual contribution (formalizing HTE with delayed response, rigorous identifiability analysis) weighed against the following concerns: (1) the experimental evaluation is conducted entirely under favorable conditions where the data-generating process matches the model's parametric assumptions; (2) the EM implementation deviates from standard guarantees without adequate discussion; (3) the strong identification assumptions for τ_D(x) are acknowledged but not accompanied by sensitivity analysis; (4) no genuinely observational delayed-feedback validation is provided. The paper has a solid theoretical core and addresses a practically important problem, but the empirical claims are overstated relative to the evidence provided.

**Post-Revision Target: [7.5, 8.5] / 10**

If the authors address all P0 items (model misspecification experiments, EM clarification, sensitivity analysis for principal ignorability, statistical significance tests, and consistent baseline reporting), the paper would be substantially strengthened. Addressing P1 items (observational case study, covariate shift experiment) would further increase credibility. A post-revision score of 7.5-8.5 is achievable assuming the key results hold under misspecification and the sensitivity analysis shows reasonable robustness.

### Scoring Rationale

| Dimension | Score | Reasoning |
|-----------|-------|-----------|
| Research Value / Novelty | 7/10 | Novel problem formulation; first principled treatment of delayed response in HTE; strong identifiability theory |
| Validity / Soundness | 6/10 | Theory is sound; EM implementation needs clarification; evaluation is favorable to method |
| Reproducibility | 7/10 | Architecture and hyperparameters well-documented; code not yet public (anonymous); experiments reproducible in principle |
| Empirical Strength | 5/10 | All evaluations are semi-synthetic with favorable DGP; no model misspecification test; no observational validation |
| Presentation / Clarity | 6/10 | Well-structured but introduction could motivate delayed-response gap earlier; abstract lacks quantitative results |
| Overall | 6.5/10 | Promising theoretical contribution with meaningful practical potential, but experimental evaluation needs fundamental strengthening