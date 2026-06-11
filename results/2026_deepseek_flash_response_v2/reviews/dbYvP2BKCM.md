Now I have a clear picture. Let me write the final consolidated review.

## Summary

ZNet proposes a neural architecture that learns instrument (Z) and confounder (C) representations from observed covariates X by encoding the structural causal model of instrumental variables into a multi-part loss function that enforces relevance, exclusion restriction, and unconfoundedness. The learned representations can then be used as a plug-in module with standard downstream IV estimators (TSLS, DeepIV, DFIV). The paper evaluates on semi-synthetic data from IHDP across four data categories (Disjoint, Mixed, Latent, No Candidate) with both linear and non-linear variants.

## Strengths

- **Strongest ATE performance in the hardest settings (No Candidate).** In the "Non-linear No Candidate" setting — where no instrument exists in observed data and the outcome is non-linear — ZNet achieves the best ATE error with both DeepIV (0.260, significantly best) and DFIV (0.049, significantly best). In the "Linear No Candidate" setting, ZNet achieves the best error with TSLS (0.025). These are the primary use cases ZNet is designed for (Table 1).

- **Direct empirical validation of all three IV conditions.** Figure 6 separately validates relevance (F=15.34, p=8.06e-21 on train), exclusion restriction (F=0.58, p=0.446 on train, confirming Z adds no predictive power for Y beyond C and T), and unconfoundedness (avg absolute Pearson correlation between U and Z is 0.118 on train). This goes beyond reporting only downstream ATE error.

- **Ablation study confirms component contributions.** Figure 5c shows that ablating all loss constraints drops instrument recovery correlations from R² ~0.3–0.4 to 0.02–0.05, directly tying the multi-part loss to Z's instrument quality.

- **Flexible plug-in design.** ZNet is evaluated with three distinct downstream estimators (TSLS, DeepIV, DFIV) across all 8 dataset configurations (Table 1), demonstrating it is not tied to a specific second-stage method.

## Weaknesses

### Major

1. **Mathematical error in Lemma 1 proof and unsupported unconfoundedness claim.** The proof (lines 91–93) contains a critical algebraic error. The step `E[Z·(e_Y − E[e_Y|X,T])] = E[Z·e_Y] − E[Z]·E[e_Y|X,T]` incorrectly treats the conditional expectation `E[e_Y|X,T]` — a function of the random variables (X,T) — as a constant that can be pulled out of the expectation with Z. The correct expansion would be `E[Z·e_Y] − E[Z·E[e_Y|X,T]]`. More fundamentally, `Cov(Z, e_Y − E[e_Y|X,T]) = 0` implies `Cov(Z, e_Y) = Cov(Z, E[e_Y|X,T])`, not `Cov(Z, e_Y) = 0` as claimed. Since Z = g(X) is a function of X and `E[e_Y|X,T]` is a function of (X,T), the right-hand term is not generally zero, so the lemma's conclusion does not follow from its premises. This undermines the paper's key differentiation from prior work (which assumes X is not influenced by U) and means the unconfoundedness loss (Equation 6) is an inductive bias without the theoretical backing the paper claims.

2. **Decomposition identifiability gap.** The paper provides no argument that the learned (C, Z) decomposition is uniquely or causally meaningful. Multiple decompositions of X could satisfy the correlation-based loss terms (relevance, exclusion restriction via orthogonality) without corresponding to a causally valid instrument. The Discussion acknowledges that "IV estimation in general is limited by a lack of theoretical guarantees of identifiability," but this honest admission also undercuts the stronger claim that "solutions to the ZNet loss minimization problem will always give a representation that serves as an instrument."

### Minor

3. **Test-set relevance not statistically significant in key setting.** In the "Non-linear No Candidate" setting (Figure 6a), the test split F-statistic for relevance is 1.83 (p=0.081) — not significant at conventional thresholds. This suggests the learned Z's relevance to T may not generalize to held-out data, which is concerning since relevance is a core IV condition.

4. **Some baseline results are extreme, making comparisons less informative.** AutoIV on "Non-linear No Candidate" with TSLS produces an error of −25.181, and several other baseline errors are very large (e.g., AutoIV on "Non-linear Mixed" with TSLS: 10.821). These extreme values may reflect tuning difficulties rather than fundamental method quality, and outperforming such baselines is a weaker signal than the paper implies.

### Trivial

5. The loss label `L_{Z \not\rightarrow C}^{PC}` (Equation 8) makes a causal claim (Z does not cause C) for what is a purely correlational loss (`PC(C,Z)²` minimization), which is notationally imprecise.

## Nice-to-Haves

- The hyperparameter tuning pipeline optimizes proxy criteria (F-statistic and C-Z orthogonality) rather than downstream ATE accuracy, creating a potential mismatch between tuning signal and evaluation metric. The paper does not discuss whether all baselines benefit equally from this tuning protocol.
- No analysis of the learned C representation quality is provided, though C matters for downstream estimation.
- Confidence intervals or more granular statistical comparisons between ZNet and each individual baseline (beyond the top-2 vs. third comparison indicated by asterisks) would strengthen the empirical claims.

## Removed Points

These points from the harsh critic or strength finder were removed after verification:

1. **"Minimizing Cov(Z, Y−\hat{Y}) toward zero is identically zero for any Z that is a function of X with mean zero"** — This claim by the harsh critic is factually incorrect. Cov(Z, e_Y − E[e_Y|X,T]) is not identically zero for arbitrary Z = g(X); the quantity depends on the relationship between Z and e_Y and is not guaranteed to vanish by iterated expectations alone. Removed because it is wrong.

2. **Strength: "Lemma 1 provides a principled, tractable approach to enforcing unconfoundedness"** — Since the Lemma 1 proof is incorrect and the conclusion does not follow, this claimed strength is not valid. Removed.

3. **Missing related works** — Removed per instructions (cannot verify).

4. **Formatting/style nitpicks** — Removed per instructions.

5. **Reproducibility concerns about undisclosed hyperparameters** — Removed per instructions (the tuning procedure is described in Section 5.3).

## Novel Insights

The paper's core operational insight — that learning instrumental representations by encoding SCM constraints into a multi-part loss is feasible and can reduce bias in settings without explicit instruments — is genuinely interesting and finds some empirical support. The ablation study (Figure 5c) usefully demonstrates that all three constraints contribute to instrument recovery. However, the primary theoretical insight (Lemma 1) for relaxing the unconfoundedness assumption is not mathematically supported as presented, and this gap limits the paper's claimed advance over prior variational IV methods.

## Suggestions

1. Correct the Lemma 1 proof or honestly reframe the unconfoundedness constraint as an inductive bias (with appropriate discussion of what guarantees are lost) rather than claiming theoretical enforcement of Cov(Z, e_Y) = 0.

2. Address the non-significant test-set relevance F-statistic in the "Non-linear No Candidate" setting — analyze whether this reflects overfitting, model capacity issues, or whether different hyperparameters could improve held-out relevance.

3. Provide identifiability analysis or empirical evidence (e.g., on known-instrument datasets) that the learned Z is uniquely determined and causally meaningful.

4. Report confidence intervals for all comparisons and consider using more stable baseline configurations to avoid the extreme errors that make some comparisons uninformative.

## Score and Decision

### Calibration Anchors

**Round 1 (Bracketing):**
| Path | Avg Score | How it compares |
|------|-----------|-----------------|
| `/5AJ8R4z5g0.md` (Potential Outcomes Under Hidden Confounders) | 3.25 | Weaker — ZNet has stronger empirical evaluation |
| `/qDhq1icpO8.md` (CBRL.CIV) | 6.75 | Stronger — has sound theoretical guarantees for its method |
| `/Oc4ji1iCjQ.md` (ShadowCatcher) | 6.75 | Stronger — well-motivated with sound theory |
| `/F7XPZnIUHh.md` (ADR) | 4.20 | Comparable — both have proof errors, ZNet has stronger experiments |
| `/3cuJwmPxXj.md` (Intervention Extrapolation) | 8.00 | Much stronger — principled identifiable representations |

**Round 2 (Narrowing, bracket 4.5–6.0):**
| Path | Avg Score | How it compares |
|------|-----------|-----------------|
| `/qe1CsfnN1W.md` (CiVAE) | 6.25 | Stronger — has theoretical identifiability results ZNet lacks |
| `/qac43AwuL9.md` (Causal Information Bottleneck) | 6.00 | Slightly stronger — clean theory but limited experiments |
| `/x2rZGCbRRd.md` (Post-Treatment Covariates) | 5.50 | Comparable scope but different problem |
| `/TC9r8gsaoh.md` (Nuisance-Robust Weighting) | 6.00 | Stronger — more principled approach |
| `/TwMLUpPg8G.md` (Physics Laws via Invariant Functions) | 5.00 | Not directly comparable |

**Bracket determined after Round 1:** 4.0 – 6.0

**Narrowing after Round 2:** The paper is clearly weaker than CiVAE (6.25) and CIB (6.00), which have sound theoretical foundations. It is most comparable to ADR (4.20), which also had a verified proof error, but ZNet has more comprehensive experiments and a better-motivated evaluation. The mathematical error in Lemma 1 is a genuine flaw that prevents the paper from being scored in the 6+ range.

**Final Score:** 5.0 — The paper addresses an important problem and provides a reasonably thorough empirical evaluation. However, the mathematical error in Lemma 1 undermines the core theoretical claim about enforcing unconfoundedness, which is the paper's key differentiation from prior work. The empirical results are promising but mixed enough (some settings ZNet is best, others not; test-set relevance non-significant) that they do not fully compensate for the theoretical gap.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>