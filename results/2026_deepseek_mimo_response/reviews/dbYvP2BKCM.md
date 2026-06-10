## Summary
This paper proposes ZNet, a deep learning framework that decomposes observed covariates X into a confounder representation C = f(X) and instrument representation Z = g(X), with architecture and loss terms designed to enforce the three standard IV assumptions (relevance, exclusion restriction, unconfoundedness). The learned representations are fed to downstream IV estimators (TSLS, DeepIV, DFIV) for treatment effect estimation, evaluated on 10 semi-synthetic settings derived from IHDP.

## Strengths
- **Well-motivated architecture design**: ZNet's multi-armed architecture (Figure 3) directly encodes the IV structural causal model with dedicated loss terms for each assumption (equations 5–9). The ablation study (Figure 5c) confirms that removing any constraint degrades instrument recovery (R² drops from 0.84 to 0.02–0.39).
- **Instrument recovery validated empirically**: In the Linear Mixed Candidate setting, ZNet recovers true instruments X₁₃, X₁₄, X₁₅ with R² ≈ 0.84 (Figure 5b). In the Linear Categorical Instrument setting, the confusion matrix shows near-perfect cluster recovery (Figure 4).
- **Comprehensive evaluation**: 10 data generation settings (linear/nonlinear × 4 instrument scenarios × with/without U) × 3 downstream estimators, with comparisons to AutoIV, VIV, GIV, TrueIV, and TARNet, evaluated over 50 bootstraps.
- **Model-agnostic plug-in design**: ZNet produces {C, Z, T, Y} representations compatible with any two-stage IV estimator, demonstrated with TSLS, DeepIV, and DFIV.

## Weaknesses

### Fatal
- **Lemma 1 proof contains an algebraic error; the premise is vacuously true for any Z = g(X)**: The proof (lines 91–93) expands $\text{Cov}(Z, e_Y - \mathbb{E}[e_Y|X,T]) = 0$ and in the fourth equation writes $\mathbb{E}[Z \cdot e_Y] - \mathbb{E}[Z] \cdot \mathbb{E}[e_Y|X,T]$, incorrectly factoring $\mathbb{E}[e_Y|X,T]$ out of the expectation as if it were a constant rather than a random variable that depends on (X,T). The correct expansion gives $\mathbb{E}[Z \cdot e_Y] - \mathbb{E}[Z \cdot \mathbb{E}[e_Y|X,T]]$, which does not simplify to $\text{Cov}(Z, e_Y) = 0$.

  More fundamentally, $\text{Cov}(Z, e_Y - \mathbb{E}[e_Y|X,T]) = 0$ is **always** true when $Z = g(X)$: conditioning on (X,T), $\mathbb{E}[Z \cdot (e_Y - \mathbb{E}[e_Y|X,T]) | X,T] = g(X) \cdot \mathbb{E}[e_Y - \mathbb{E}[e_Y|X,T] | X,T] = g(X) \cdot 0 = 0$, so the unconditional expectation is 0 by iterated expectations. Thus the lemma's premise is vacuously satisfied by any function of X, and the conclusion does not follow (consider X correlated with U affecting $e_Y$: then $g(X)$ can be correlated with $e_Y$).

  This means the unconfoundedness loss $L_{Z \not\leftrightarrow \epsilon_Y}^{PC}$ (equation 6) is theoretically vacuous — it converges to 0 for any $Z = g(X)$, providing no gradient signal for enforcing unconfoundedness. Signal only arises because $\Phi(X \odot T)$ is an imperfect approximation of $\mathbb{E}[Y|X,T]$, relying on approximation error rather than principled enforcement. This undermines the theoretical foundation for the No Candidate case and the claim that "solutions to the ZNet loss minimization problem will always give a representation that serves as an instrument" (line 394).

### Major
- **Test-set instrument relevance degrades severely in the flagship No Candidate example**: Figure 6 shows F-statistics for learned Z in the Non-linear No Candidate setting: Train F=15.34 (p<10⁻²⁰), Val F=4.96 (p<10⁻⁵), Test F=1.83 (p=0.0813). The test F-statistic is not significant at the 5% level, and the 8× degradation from train to test suggests overfitting. The paper does not discuss this deterioration. An instrument that is not reliably relevant on held-out data cannot support valid IV estimation.

- **Empirical results are mixed despite "superior" claims**: Table 1 shows ZNet frequently loses to competitors: VIV outperforms ZNet in Linear Latent with TSLS and DFIV, GIV wins in Linear No Candidate (no U) with TSLS, AutoIV wins in several DeepIV settings. The paper claims ZNet is "on average the highest performing" (line 323) based on Appendix Tables 9, 10, but no explicit averaging or statistical test is shown in the main text, and results are highly estimator-dependent.

### Minor
- **Only semi-synthetic data from a single source (IHDP)**: All 10 settings are author-designed synthetic variations of IHDP. Claims about "real-world settings" (line 382) and "plug-in causal inference estimator" (line 392) are not supported by the evidence presented.
- **Element-wise multiplication Φ(X⊙T) is unusual and unjustified**: Equation 5 uses $X \odot T$ rather than concatenation $[X, T]$. This requires X and T to have the same dimensionality and may not capture all covariate-treatment interactions. The choice is not motivated.
- **Only mean errors reported**: Table 1 reports means but not standard errors across 50 bootstraps. Significance markers (\*, \*\*) are only relative comparisons among top methods, not absolute assessments of result stability.

### Trivial
None.

## Nice-to-Haves
- A sensitivity analysis showing how treatment effect estimation degrades as IV assumptions are violated to varying degrees.
- Reporting average rank or average MSE across all settings with confidence intervals to substantiate the "on average highest performing" claim.
- Using independence-based losses (e.g., HSIC) instead of correlation-based losses to better match IV assumptions, especially since the paper already mentions MI-based losses as an option.

## Removed Points
These points are flagged to be removed, treat them with caution.
- **Covariance vs. independence gap**: The harsh critic noted the standard IV assumption is independence $Z \perp e_Y | C$, not merely zero covariance. While technically correct, the paper mentions MI-based losses as an alternative (line 131), and for linear downstream estimators (TSLS), zero covariance suffices. This concern is subsumed by the more severe Lemma 1 proof error.
- **Circularity argument for No Candidate case**: The harsh critic argued if $X \perp U$ there's no confounding problem, and if X is not independent of U, g(X) can't be independent of U. However, Φ models $\mathbb{E}[Y|X,T]$, a directly observable conditional expectation rather than a causal quantity, weakening the circularity claim. The real issue is the Lemma 1 proof error.
- **Strength about Lemma 1 providing theoretical foundation**: The Strength Finder claimed Lemma 1 "provides a theoretical foundation for enforcing unconfoundedness." This conflicts with the verified proof error and is therefore invalid.
- **Strength about "principled treatment of the no-instrument case"**: The Strength Finder claimed Figure 6 validates the No Candidate approach, but the test-set F=1.83 (p=0.0813) undermines this claim.

## Novel Insights
The key novel observation from this review is that Lemma 1's proof contains a fundamental algebraic error: the step $\mathbb{E}[Z \cdot \mathbb{E}[e_Y|X,T]] = \mathbb{E}[Z] \cdot \mathbb{E}[e_Y|X,T]$ (line 93) treats a random variable as a constant. Moreover, the lemma's premise $\text{Cov}(Z, e_Y - \mathbb{E}[e_Y|X,T]) = 0$ is always true for $Z = g(X)$ by iterated expectations (since $g(X)$ is measurable w.r.t. X, and the inner residual has zero conditional expectation given (X,T)), making the lemma vacuously true. This means the unconfoundedness loss (equation 6) provides no meaningful gradient signal — it only functions due to approximation errors in Φ, not by principled enforcement. This goes beyond the original review's observation about covariance vs. independence: even the weaker covariance condition is not being enforced by the proposed loss.

## Suggestions
- Fix or replace Lemma 1. Consider using HSIC or distance covariance as the independence measure, which would provide non-vacuous enforcement of unconfoundedness.
- Discuss train-to-test degradation in the No Candidate case (Figure 6) and its implications for downstream estimates.
- Replace Φ(X⊙T) with Φ([X,T]) and justify the architectural choice.
- Report standard errors or confidence intervals for Table 1 results.
- Include an explicit aggregate comparison (e.g., average rank across all 10×3 settings).
- Add at least one real-data application to strengthen practical relevance.

## Calibration Report

**Round 1 anchors (bracketing):**
| Paper | Score | Round | Comparison |
|-------|-------|-------|------------|
| jFox1iMWUa (Causal Neural Networks) | 3.40 | R1 | ZNet clearly stronger |
| 4u0ruVk749 (DFITE) | 3.00 | R1 | ZNet clearly stronger |
| 5AJ8R4z5g0 (Potential Outcomes) | 3.25 | R1 | ZNet stronger |
| AvXrppAS2o (Causal Structure Learning) | 3.00 | R1 | ZNet clearly stronger |
| F7XPZnIUHh (ADR decomposed repr.) | 4.20 | R1 | ZNet slightly stronger: more comprehensive eval, but both have proof errors |
| qDhq1icpO8 (CBRL.CIV) | 6.75 | R1 | ZNet clearly weaker: sound theory, no proof errors |
| 3cuJwmPxXj (Intervention Extrapolation) | 8.00 | R1 | ZNet clearly weaker |
| xByvdb3DCm (Selection meets Intervention) | 8.00 | R1 | ZNet clearly weaker |
| k38Th3x4d9 (Root Cause Analysis) | 8.00 | R1 | ZNet clearly weaker |
| 8zJRon6k5v (Amortized Control) | 8.00 | R1 | ZNet clearly weaker |

**Round 2 anchors (narrowing):**
| Paper | Score | Round | Comparison |
|-------|-------|-------|------------|
| F7XPZnIUHh (ADR) | 4.20 | R2 | ZNet slightly stronger (more comprehensive eval) |
| QV6uB196cR (A/B testing) | 4.75 | R2 | Similar level |
| MqEQbvPvkE (Exposure Shifts) | 5.00 | R2 | Similar level |
| 0gqCIaBRQ9 (Regularized DeepIV) | 5.25 | R2 | ZNet weaker: DEIV has correct theory |
| TC9r8gsaoh (Nuisance-Robust) | 6.00 | R2 | ZNet weaker: sounder theoretical foundations |
| qDhq1icpO8 (CBRL.CIV) | 6.75 | R2 | ZNet clearly weaker |

**Round 1 bracket: 3.5–7.0.** Round 2 bracket: 4.0–5.5. The paper sits above ADR (4.20) due to more comprehensive evaluation and a more ambitious problem formulation, but below 5.0–5.25 papers due to the fatal Lemma 1 proof error. Final score: **4.5**.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>