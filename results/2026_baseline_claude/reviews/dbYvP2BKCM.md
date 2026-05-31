## Summary

ZNet is a deep learning method that automatically constructs instrumental variable (IV) representations from observational data without requiring domain expertise. The paper decomposes observed covariates X into a confounder representation C and instrument representation Z using a multi-loss architecture designed to enforce three IV conditions (relevance, exclusion restriction, unconfoundedness). A central theoretical contribution is Lemma 1, which claims that enforcing zero covariance between the learned Z and the residuals of predicting Y from (X,T) suffices for full unconfoundedness — even when observed variables are influenced by unobserved confounders. ZNet is evaluated on semi-synthetic datasets based on IHDP across 10 configurations and compared to competing IV generation methods (AutoIV, GIV, VIV).

## Strengths

- **Novel SCM-based architecture**: Unlike existing learned-IV methods (AutoIV, VIV, DVAE.CIV) which rely on VAEs and variational distributions, ZNet directly enforces IV structural constraints through explicit loss terms. This provides more direct control over the learned representations and is conceptually cleaner.

- **Comprehensive empirical evaluation**: The paper evaluates 10 data-generation configurations (linear/nonlinear × 5 data types), 3 downstream IV estimators (TSLS, DeepIV, DFIV), 50 bootstrapped resamples, and 3 competing IV generation baselines. The ablation study in Figure 5(c) concretely demonstrates that each constraint contributes to instrument recovery.

- **Instrument recovery demonstrations**: Figures 4 and 5 provide concrete, quantitative evidence that ZNet can recover latent categorical instruments (Figure 4 shows near-perfect confusion matrix) and observed instrument candidates. These are compelling illustrations of the method's representational capacity.

- **Competitive empirical performance in Table 1**: ZNet achieves the smallest or second-smallest ATE error in the majority of dataset-estimator combinations, consistently outperforming Diff-Means and TARNet across confounded settings, and is broadly competitive with other IV generation methods.

## Weaknesses

### Fatal

None that invalidate the empirical results outright.

### Major

**1. Lemma 1 proof is mathematically incorrect.** This lemma underpins the paper's central theoretical claim that ZNet "relaxes" the standard assumption that X is unconfounded by U. The proof contains an invalid step in line 4:

$$E[Z \cdot (e_Y - \mathbb{E}[e_Y|X,T])] = E[Z \cdot e_Y] - E[Z] \cdot \mathbb{E}[e_Y|X,T]$$

By linearity of expectation, the correct expansion is:

$$E[Z \cdot (e_Y - \mathbb{E}[e_Y|X,T])] = E[Z \cdot e_Y] - E[Z \cdot \mathbb{E}[e_Y|X,T]]$$

These two expressions are equal only if $Z \perp \mathbb{E}[e_Y|X,T]$, i.e., Z is uncorrelated with $\mathbb{E}[e_Y|X,T]$. But $\mathbb{E}[e_Y|X,T]$ is a random variable (a function of X and T), not a scalar constant, so $E[Z \cdot \mathbb{E}[e_Y|X,T]] \neq E[Z] \cdot \mathbb{E}[e_Y|X,T]$ in general. The conclusion Cov(Z, e_Y)=0 does not follow. More directly, a counterexample: let X = U + ε_X, Z = g(X), e_Y = U. Then Cov(Z, e_Y) = Cov(g(X),U) ≠ 0, but Cov(Z, e_Y - E[e_Y|X,T]) could be zero since E[e_Y|X,T] = E[U|X,T] captures all the Z-correlated variation in U. So the constraint is satisfied while unconfoundedness is violated. This means the claimed theoretical advantage over prior methods — handling Z constructed from X influenced by U — is not supported.

**2. Weak instrument on out-of-sample test data.** Figure 6(a) shows that for the "Non-linear No Candidate" dataset, the F-statistic for the relevance test falls to F=1.83 (p=0.0813) on the test split, which is not statistically significant and well below the conventional weak-instrument threshold of F>10. This indicates the learned instrument may not generalize out of sample, raising concerns about the method's reliability in the hardest (no-candidate) setting.

**3. Biased tuning signal.** The hyperparameter optimization for causal inference methods uses the nearest-neighbors (NN) ATE MSE as a tuning objective. However, the NN ATE estimator is itself biased under unobserved confounding — the very problem the paper is designed to solve. Using a biased signal to select hyperparameters could preferentially select configurations that incidentally match the NN ATE rather than the true causal effect, potentially inflating estimated performance under confounding.

### Minor

- **Exclusion restriction enforcement is incomplete**: Constraints enforce Cov(C,Y)>0 and Cov(Z,C)=0, but zero linear correlation between Z and C does not preclude a direct path from Z to Y through other channels. The exclusion restriction requires Z to have no direct effect on Y independent of T — this is a structural condition that linear covariance constraints only weakly approximate.

- **Performance in some settings is notably poor**: ZNet's TSLS error of 2.718 in "Linear No Candidate (no U)" setting (true ATE=1.882) is worse than the Diff-Means baseline (−0.296), suggesting instability with some estimator-dataset combinations.

- **Evaluation limited to IHDP-derived semi-synthetic data**: All 10 configurations share the same 25-covariate IHDP base, which limits generalizability claims. The method may be well-suited to this particular covariate structure but untested on other domains.

### Trivial

- The notation in the Lemma proof conflates random variables and scalars in a way that may confuse readers even setting aside the error.

## Nice-to-Haves

- Providing a corrected version of Lemma 1 with appropriate additional conditions (e.g., requiring Z constructed to be independent of X, or providing a weaker claim matching the proof), or reframing Constraint 1 as a heuristic proxy rather than a theoretically justified sufficient condition.
- Including at least one real-world dataset (e.g., 401(k) eligibility, Vietnam draft lottery) alongside the semi-synthetic evaluation to demonstrate practical applicability.
- Reporting confidence intervals (not just bootstrap mean errors) in Table 1 to assess whether ZNet's advantage is statistically significant.

## Novel Insights

ZNet's core insight — that instrument representations can be extracted from observational data by constructing an SCM where the learned functions f, g enforce IV conditions directly through correlation-based loss terms — is conceptually appealing and practically useful. The use of residuals from a pretrained outcome predictor Φ as a proxy for outcome error e_Y in the unconfoundedness loss (building on Lemma 1, even if the proof is flawed) is an interesting direction that might be correct under tighter conditions than stated. The gradient surgery approach for handling conflicting losses in multi-constraint optimization is a practical contribution to multi-objective learning in causal representation models.

## Suggestions

- Fix or remove Lemma 1: Either provide a corrected proof with appropriate conditions (e.g., Z ⊥ (X,T) in addition to the stated assumptions), or drop the theoretical claim and characterize Constraint 1 as a heuristic approximation. The empirical motivation for the constraint is clear without the flawed proof.
- Add a formal F-statistic threshold analysis across all datasets: the strength of the learned instrument in the test set is crucial for IV validity and should be reported systematically.
- Include a sensitivity analysis of hyperparameter choices to test the robustness of conclusions.

## Score and Decision

The paper addresses a practically important problem with a clean conceptual approach (SCM-based rather than VAE-based IV learning) and presents a reasonably thorough empirical evaluation. However, the central theoretical novelty claim — that ZNet handles the harder setting where X is influenced by U — rests on a Lemma with a flawed proof (and likely a false conclusion in general). This is not a minor presentational issue; it undermines the theoretical framing that distinguishes ZNet from prior work. The weak F-statistic on test data and the biased tuning objective compound these concerns. The empirical results as an engineering contribution remain interesting, but at the current state the paper overclaims its theoretical guarantees.

MY FINAL SCORE: <score>4</score>
MY FINAL DECISION: <decision>Reject</decision>