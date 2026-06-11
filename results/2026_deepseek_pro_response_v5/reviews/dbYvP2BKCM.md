Now I have a clear picture. Let me finalize the review with calibration integrated.

---

## Summary
ZNet proposes to learn instrumental variable representations from observational data by decomposing observed covariates \(X\) into an instrument \(Z\) and confounders \(C\) via a constraint-driven neural architecture. The method directly encodes the three IV conditions (relevance, exclusion restriction, unconfoundedness) as explicit loss terms on the learned representations, departing from VAE-based probabilistic approaches. The paper evaluates ZNet across 10 semi-synthetic settings spanning four dataset classes, comparing against three IV-generation baselines and three downstream estimators.

## Strengths
- **Explicit SCM-based constraint architecture**: Unlike prior VAE-based IV generation methods (AutoIV, VIV, GIV), ZNet directly encodes the three IV conditions as interpretable loss terms (Eqs. 5–9 in Section 5.1), mapping each constraint to a specific, auditable loss. This design choice is a genuine departure from the probabilistic latent-variable approaches that dominate the literature.
- **Lemma 1 for unconfoundedness when X may depend on U**: The lemma (Section 3, lines 89–95) shows that if \(Z \sim \mathcal{N}(0, \sigma^2)\) and \(\text{Cov}(Z, e_Y - \mathbb{E}[e_Y|X,T]) = 0\), then \(\text{Cov}(Z, e_Y) = 0\). This is operationalized by training \(\Phi\) to predict \(Y\) from \(X,T\) and minimizing correlation between \(Z\) and the residuals. This relaxes the common assumption that observed covariates are independent of unobserved confounders — an assumption explicitly made by prior work.
- **Comprehensive evaluation**: Table 1 covers 10 settings spanning 4 dataset classes (Disjoint, Mixed, Latent Categorical, No Candidate) × 2 functional forms (linear/nonlinear) × 2 confounding regimes, with 50 bootstrap resamples, 4 competing IV methods plus TARNet, and 3 downstream estimators. This breadth exceeds prior IV-generation evaluations.
- **Ablation studies validate constraint contributions**: Figure 5(c) quantifies instrument recovery degradation when individual constraints are removed. \(R^2\) for predicting true instruments drops from 0.84 (full ZNet) to 0.25 (ablate Constraint 1), 0.36–0.39 (ablate Constraint 2), 0.31–0.33 (ablate Constraint 3), and 0.02–0.05 (ablate all). This provides direct evidence that the constraint design drives instrument recovery.

## Weaknesses

### Fatal
None.

### Major
- **Gap between correlation-based losses and IV independence requirements**: The three IV conditions are statements about conditional independence (\(Z \perp e_Y \mid C\), \(Z \perp Y \mid C, T\), \(Z \not\perp T \mid C\)), but ZNet enforces them through pairwise Pearson correlation penalties (Eqs. 5–9). Zero covariance does not imply independence — a gap that matters in the non-linear settings the paper claims to handle. The MI-based loss variant is mentioned in a single sentence (line 131) with no implementation details, no analysis of KDE reliability, and no indication of which experiments use which variant. The central claim that "Solutions to the ZNet loss minimization problem will always give a representation that serves as an instrument" (line 394) is therefore overstated: the loss enforces necessary but not sufficient conditions for IV validity.
- **Exclusion restriction enforcement is indirect**: Constraint 2 combines \(L_{C \rightarrow Y}\) (encouraging \(C\) to predict \(Y\)) and \(L_{Z \not\rightarrow C}\) (decorrelating \(C\) and \(Z\)). This does not directly prevent \(Z\) from having a predictive path to \(Y\) that bypasses \(T\) — the exclusion restriction requires \(Z \perp Y \mid C, T\). The loss design is a reasonable heuristic but is not equivalent to enforcing the exclusion restriction, and the paper does not discuss this limitation.

### Minor
- **F-test validation of exclusion restriction misinterprets null hypothesis testing**: Figure 6b validates the exclusion restriction by reporting non-significant F-test p-values (0.446, 0.461, 0.813) as evidence that \(Z\) does not predict \(Y\) given \(C,T\). Failure to reject the null is not evidence that the null is true. With test sets of ~200 samples and 10-dimensional \(Z\), the test likely has low power. An equivalence testing framework would be more appropriate.
- **MI-based loss variant is mentioned but not developed**: The paper states an MI-based loss is "additionally employed" (line 131) but provides no details on how MI replaces the PC formulations for each constraint, no analysis of whether KDE-based MI estimation is reliable at the dimensionalities used, and no indication of which experimental results use PC vs. MI. This makes the MI variant essentially unreported.
- **Hyperparameter tuning metrics align with ZNet's explicit objectives**: All IV methods (ZNet and baselines) are tuned to maximize the instrument's F-statistic and minimize \(\text{Cov}(C, Z)\) — precisely the quantities ZNet's loss function is designed to optimize. While these are defensible general IV quality metrics, baselines using fundamentally different objectives (VAE-based) may not be fairly evaluated when tuned by ZNet's criteria.
- **Architecture details missing from main text**: Layer widths, activation function selection criteria, and the output dimensions of \(f\) and \(g\) are not specified in the method description (Z dimensions of 9–10 appear only in figure captions).

### Trivial
- The statistical test used for significance annotations (*/**) in Table 1 is not explicitly described. The paper mentions "across 50 resampled bootstraps" but does not specify whether tests are paired, corrected for multiple comparisons, or comparing within or across methods.

## Nice-to-Haves
- No real-data experiment: the motivating examples (EHRs, consumer AI tools) are compelling but all evaluation is on semi-synthetic data built from IHDP covariates. A demonstration on even one real dataset would strengthen the empirical case.
- The Latent Categorical setting produces a perfect confusion matrix (Figure 4, 100% accuracy on all 5 clusters), raising questions about whether the latent instrument is trivially recoverable in a way that doesn't stress-test the method.
- The paper does not report what happens when all \(X\) are used directly as \(C\) in TARNet (the natural non-IV baseline), which would help contextualize whether learned IV representations outperform simply adjusting for all observed covariates.

## Removed Points
These points are flagged to be removed; treat them with caution.

- **Harsh Critic claim that the tuning protocol "creates an uneven comparison" and that computational budget differences make fairness unassessable**: The F-statistic and Cov(C,Z) metrics are standard IV quality measures, not ZNet-specific. All methods received the same tuning protocol. The computational budget concern is speculative. The point was demoted to Minor.
- **Harsh Critic claim that Lemma 1's premise "depends on Φ(X,T) being a consistent estimator" with "no discussion of model misspecification"**: The paper acknowledges Φ is a learned model; misspecification risk is inherent to all learned nuisance models and is not a specific flaw. Too generic to retain.
- **Harsh Critic criticism about "no comparison to simply using all X as C with no Z"**: TARNet is included as a non-IV baseline. Moved to Nice-to-Haves.
- **Strength Finder claim about "fair hyperparameter tuning via unified Bayesian optimization protocol"**: Toned down due to the alignment concern raised in Minor weaknesses. The unified protocol is still a positive feature but not presented as an unqualified strength.
- **Strength Finder claim about "three-stage training with gradient surgery" as a standalone strength**: This is a standard engineering choice, not a methodological contribution. Removed as a standalone strength.
- **Harsh Critic assertion about "no real-data experiment" as fatal**: The paper's motivation mentions real-world applications but all evaluation is semi-synthetic. This is common in causal ML papers and the evaluation design is appropriate. Moved to Nice-to-Haves.

## Novel Insights
None beyond the paper's own contributions. The core insight — that IV conditions can be encoded as architectural constraints rather than learned through probabilistic generative modeling — is the paper's contribution, and the reviews do not surface fundamentally new framing beyond this.

## Suggestions
- Strengthen the exclusion restriction enforcement by adding a loss that directly penalizes the predictive power of \(Z\) for \(Y\) conditional on \(C\) and \(T\) (e.g., an adversary trained to predict \(Y\) from \(Z\) given \(C,T\), whose success is penalized).
- Replace the F-test validation with an equivalence testing framework (e.g., TOST) or a sensitivity analysis bounding how much direct effect would be needed to meaningfully bias ATE estimates.
- Provide a theoretical characterization of when the correlation-based constraints are sufficient for IV validity, even if the conditions are strong — this would allow readers to judge when the method can be trusted.
- Specify which experiments use PC-based vs. MI-based losses, and if the MI variant is used, report its implementation details and any ablation comparing the two.
- Tone down the claim on line 394 from "will always give a representation that serves as an instrument" to something like "is designed to produce representations that satisfy necessary conditions for IV validity."

## Calibration and Score

**Round 1 (Bracketing):** Searched across five score bands. The most topically relevant anchors were Regularized DeepIV (avg 5.25), ADR decomposition for ITE (avg 4.20), and CBRL.CIV (avg 6.75, the closest topical match — conditional IV with representation learning). ZNet sits between Regularized DeepIV and CBRL.CIV, with initial bracket 5.0–7.0.

**Round 2 (Narrowing):** Retrieved anchors in 4.5–6.0 and 6.0–7.5, finding Causal Representation Learning from Multimodal Data (avg 5.80, accept) and the same CBRL.CIV (6.75). ZNet has a cleaner empirical contribution than the 5.80 anchor (which had significant theoretical issues flagged by reviewers) but weaker theoretical grounding than CBRL.CIV (6.75).

**All anchors considered:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| p1b96KC6rj (Sources of Gain: CADR Decomposition) | 2.17 | R1 | ZNet far stronger |
| lt6xKGGWov (Feature Selection with Neural MI) | 2.33 | R1 | ZNet far stronger |
| aoW5Sm8Op8 (Benchmarking Survival Models) | 2.33 | R1 | ZNet far stronger |
| p79lnC36CO (Automatic Calibration Diagnosis) | 2.00 | R1 | ZNet far stronger |
| jFox1iMWUa (Causal NN for Continuous Treatment) | 3.40 | R1 | ZNet stronger |
| F7XPZnIUHh (ADR: Decomposed Reps for ITE) | 4.20 | R1 | ZNet clearly stronger — ADR had derivation errors and unclear motivation |
| qsAckNdySL (Causality is Invariance) | 4.25 | R1 | ZNet stronger |
| oos6KyAUsW (Mitigating Confounding via Diffusion) | 4.25 | R1 | ZNet stronger |
| MqEQbvPvkE (Causal Estimation of Exposure Shifts) | 5.00 | R1 | ZNet stronger |
| 0gqCIaBRQ9 (Regularized DeepIV) | 5.25 | R1 | ZNet stronger — broader evaluation, more practical contribution |
| q07DDpu8Xb (Distribution Shifts for CRL Identifiability) | 5.25 | R2 | ZNet stronger |
| x2rZGCbRRd (Post-Treatment Covariates for HTE) | 5.50 | R1 | ZNet comparable |
| kz5igjl04W (Latent Space Exploration + Causal) | 5.50 | R2 | ZNet stronger |
| TC9r8gsaoh (Nuisance-Robust Weighting Network) | 6.00 | R1 | ZNet comparable |
| hjROBHstZ3 (Causal RL from Multimodal Data) | 5.80 | R2 | ZNet slightly stronger — fewer theoretical issues, more focused empirical work |
| qe1CsfnN1W (Mixed Latent Confounders) | 6.25 | R1/R2 | ZNet comparable |
| nmvmPIi185 (Neural Causal Graph) | 6.25 | R1 | Different topic, comparable quality |
| **qDhq1icpO8 (CBRL.CIV — closest anchor)** | **6.75** | R1/R2 | ZNet slightly weaker — less theoretical grounding but more comprehensive evaluation |
| S46Knicu56 (Variational Framework for Continuous Treatment) | 7.33 | R1/R2 | ZNet weaker |
| 3cuJwmPxXj (Identifying Reps for Intervention Extrapolation) | 8.00 | R1 | ZNet weaker |
| xByvdb3DCm (Selection + Intervention) | 8.00 | R1 | ZNet weaker |

ZNet sits between the 5.80 and 6.75 anchors. Its comprehensive evaluation and clean constraint-driven approach outweigh the correlation-vs-independence limitation, but the overclaim on line 394 and the indirect exclusion restriction enforcement prevent it from reaching the 6.75 level of CBRL.CIV. **Score: 6.0.**

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>