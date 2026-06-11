Here is my final consolidated review, including all calibration details.

---

## Summary

The paper proposes ZNet, a deep learning method that decomposes observed covariates X into confounder representation C = f(X) and instrument representation Z = g(X) for use in instrumental variable (IV) regression. The architecture encodes the standard IV conditions (relevance, exclusion restriction, unconfoundedness) as differentiable loss constraints. The paper evaluates ZNet across 8 semi-synthetic data settings with 3 downstream IV estimators (TSLS, DeepIV, DFIV), showing competitive ATE estimation in settings where no explicit instrument exists.

## Strengths

1. **Ablation study confirms constraints drive instrument recovery.** Figure 5c shows that removing any single constraint drops the R² for predicting ground-truth instruments from ~0.84 to 0.19–0.39, and removing all three collapses to ~0.02–0.05. This provides clear evidence that the multi-loss design, not architecture artifacts, is responsible for learning useful representations.

2. **Competitive performance in the hardest "No Candidate" setting.** In the Non-linear No Candidate dataset (the most practically relevant scenario where no explicit instrument exists), ZNet achieves best ATE error with DeepIV (0.260**) and DFIV (0.049**), and second-best with TSLS (0.200*). These results support the paper's central claim that ZNet can construct useful proxy instruments.

3. **Flexible integration with multiple downstream IV estimators.** The learned C and Z representations can be plugged into TSLS, DeepIV, or DFIV, demonstrating the method's versatility.

4. **Gradient surgery for conflicting multi-objective optimization.** The paper identifies that the loss terms are potentially conflicting and adopts gradient surgery (Yu et al., 2020), a practical technique not addressed by prior variational IV methods.

## Weaknesses

### Major

1. **Lemma 1 contains a mathematical error that invalidates its claimed theoretical justification for the unconfoundedness constraint.** The proof (lines 91–94) incorrectly treats E[Z·E[e_Y|X,T]] as E[Z]·E[e_Y|X,T], but E[e_Y|X,T] is a random variable (a function of X,T), not a constant. The correct expansion shows that Cov(Z, e_Y − E[e_Y|X,T]) = 0 holds automatically for any Z = g(X): since Z is (X,T)-measurable, E[Z·E[e_Y|X,T]] = E[Z·e_Y] by the law of iterated expectations, making the premise an algebraic identity. Consequently, the loss term L_{Z↔ε_Y}^{PC} = PC(Y−Ŷ, Z)² does not enforce unconfoundedness as claimed. The paper's assertion (lines 386–387) that ZNet "relaxes the assumption" that observed variables are not influenced by U is therefore theoretically unsupported. This is a significant weakness but not fatal to the entire paper: the remaining constraints (relevance, exclusion restriction) and the empirical approach still have value.

2. **The test-set relevance of the learned instrument is not statistically significant in the key No Candidate setting.** Figure 6a reports test-split F=1.83, p=0.0813 for the Non-linear No Candidate dataset. A non-significant relevance F-statistic raises questions about whether the downstream IV estimators (which assume relevance) are operating reliably in the paper's most practically important scenario. This deserves discussion.

### Minor

3. **The empirical results are competitive but do not demonstrate clear superiority.** In the Disjoint Candidate setting (where true instruments exist), ZNet never beats TrueIV and often trails substantially (e.g., Linear Disjoint DFIV: ZNet −0.303 vs TrueIV 0.132**). In the No Candidate setting, ZNet is typically among the best but not universally dominant — other methods (VIV, GIV, AutoIV) show competitive or better results in specific configurations.

4. **The significance reporting is nonstandard and difficult to interpret.** The asterisk notation (one * = best two are better than third; two ** = best is better than second) does not convey whether ZNet's performance is significantly different from simpler baselines like TARNet or from zero error.

5. **The exclusion restriction constraint (Cov(C,Z)=0) is a design choice that may distort representations.** Decorrelating Z and C is neither necessary nor sufficient for the exclusion restriction. While the paper acknowledges this choice (footnote 1), it does not justify why forcing unconditional independence is compatible with recovering the true data-generating process when the true instrument Z* is correlated with confounders C*.

### Trivial

6. Several baseline entries in Table 1 show anomalously large errors suggesting optimization failures that are not discussed (e.g., AutoIV TSLS in Non-linear No Candidate: −25.181; Non-linear Mixed TSLS/AutoIV: 10.821).

## Nice-to-Haves

- ATE ablations showing how error changes when each constraint is removed, rather than just measuring correlation with known instruments.
- Standard error or confidence interval reporting alongside the point estimates in Table 1.
- A discussion of why the test-set F-statistic is non-significant and how this affects downstream estimates.

## Removed Points

These points were identified in the input reviews but removed per the filtering rules:

- **"Lemma 1 error is fatal / structural flaw invalidating the paper's core claims"** (Harsh Critic) — **Removed from Fatal tier.** The error is real and major, but the paper's empirical contributions and the remaining constraints still have value. The error undermines a specific claimed advantage (relaxing the X←U assumption), not the entire method. Demoted to Major.
- **"Constructing valid instruments without existing instruments is theoretically unsupported / creating information from nothing"** (Harsh Critic) — **Removed.** The paper acknowledges theoretical limitations in Section 7 ("IV estimation in general is limited by a lack of theoretical guarantees of identifiability in the general case"). The claim is about constructing *proxy* instruments that *reduce* bias, not guarantee perfect identification.
- **"Exclusion restriction constraint is not properly justified"** (Harsh Critic) — **Removed.** The paper provides justification in footnote 1 and cites the standard IV framework. This is a design choice, not an error.
- **"Lemma 1 provides a testable surrogate for unconfoundedness"** (Strength Finder) — **Removed** because Lemma 1 is mathematically flawed; this claimed strength is not valid.
- **Missing theoretical identifiability analysis** — **Removed** as scope creep; the paper acknowledges limitations.
- **Missing appendix content, dimensionality choices, MI vs PC comparison** — **Removed** as parser artifacts or standard hyperparameter choices.
- **Formatting/style nitpicks, missing references** — **Removed** per filtering rules.

## Novel Insights

None beyond the paper's own contributions. The reviews surface no genuinely novel observation about the method or problem that the paper itself does not articulate.

## Suggestions

1. **Fix or remove Lemma 1.** If the lemma cannot be corrected, the unconfoundedness constraint should be presented as a heuristic regularization rather than a theoretically justified condition. The paper should clearly state that the claimed relaxation of the X←U assumption is not supported.

2. **Add ATE ablation experiments** showing how treatment effect estimation degrades when each constraint is removed individually, complementing the current representation-correlation ablations in Figure 5c.

3. **Discuss the test-set relevance failure** (Figure 6a, test split F=1.83, p=0.0813) and its implications for the downstream IV estimates.

4. **Provide standard error or confidence interval reporting** alongside the point estimates in Table 1.

5. **Tone down the claims** about relaxing the X←U assumption. Frame ZNet as a practical empirical approach to learning instrument-like representations, with appropriately narrowed claims that do not depend on the invalid Lemma 1.

## Calibration

**Round 1 — Bracketing (score < 3.5, 3.5–7.5, > 7.5)**

| Anchor | Path | Avg Score | Round | Comparison to ZNet |
|--------|------|-----------|-------|-------------------|
| Causal Neural Nets for Continuous TRE | jFox1iMWUa | 3.40 | R1 weak | Much weaker — vague contribution, less rigorous |
| DFITE (Diffusion for ITE) | 4u0ruVk749 | 3.00 | R1 weak | Much weaker |
| Potential Outcomes Under Hidden Confounders | 5AJ8R4z5g0 | 3.25 | R1 weak | Much weaker |
| Better outcome prediction w/ causal structure learning | AvXrppAS2o | 3.00 | R1 weak | Much weaker |
| Missingness-aware Causal Concept Explainer | UoGv8d3MMy | 3.00 | R1 weak | Much weaker |
| **CIV Regression w/ Rep Learning (CBRL.CIV)** | qDhq1icpO8 | 6.75 | R1 mid | Stronger — valid theory, accepted; ZNet has flawed Lemma |
| **ADR (Adversarial Decomposed Reps)** | F7XPZnIUHh | 4.20 | R1 mid | Most comparable — both have theory errors; ZNet more thorough experiments |
| Causal Information Bottleneck | qac43AwuL9 | 6.00 | R1 mid | Stronger theory, different problem |
| Feature Matching Intervention | 8GhwePP7vA | 4.25 | R1 mid | Weaker topic match |
| **ShadowCatcher (Shadow Variables)** | Oc4ji1iCjQ | 6.75 | R1 mid | Stronger — cleaner theory, accepted-quality work |
| Identifying Reps for Intervention Extrapolation | 3cuJwmPxXj | 8.00 | R1 strong | Much stronger — accepted with perfect scores |
| Various strong papers (causal discovery etc.) | ~8.00 | ~8.00 | R1 strong | Not directly comparable, but much stronger work |

**Round 1 bracket:** 3.5–6.5 (ZNet is clearly above the 3.0–3.4 papers but well below the 8.0 papers)

**Round 2 — Narrowing (3.5–5.5 and 4.5–6.5)**

| Anchor | Path | Avg Score | Round | Comparison to ZNet |
|--------|------|-----------|-------|-------------------|
| **ADR (Adversarial Decomposed Reps)** | F7XPZnIUHh | 4.20 | R2 | Most similar paper — both have theoretical errors in core claims; ZNet has more comprehensive experiments and a more novel problem framing → ZNet slightly stronger |
| Learning Latent Structural Causal Models | 0sO2euxhUQ | 4.00 | R2 | Different topic, lower quality |
| Causal Rep Learning w/ Distribution Shifts | q07DDpu8Xb | 5.25 | R2 | Valid theory but incremental; ZNet more novel but flawed theory |
| Feature Matching Intervention | 8GhwePP7vA | 4.25 | R2 | Weaker topic match |
| **Regularized DeepIV with Model Selection** | 0gqCIaBRQ9 | 5.25 | R2 | Valid theory, but seen as incremental; ZNet more novel but theory is weaker |
| Causal Estimation of Exposure Shifts | MqEQbvPvkE | 5.00 | R2 | Different topic |
| Nuisance-Robust Weighting Network | TC9r8gsaoh | 6.00 | R2 | Stronger — valid theory, accepted-quality |
| **Transformers Handle Endogeneity** | QfhU3ZC2g1 | 6.00 | R2 | Valid theory backing claims; ZNet's theory is flawed |

**Narrowing conclusion:** ZNet is stronger than the ADR paper (4.20) due to more comprehensive experiments and a more novel problem framing, but weaker than papers at 5.25+ that have valid theoretical contributions. The Lemma 1 error prevents it from reaching the 5.0+ range. The paper sits between 4.20 (ADR) and 5.25 (Regularized DeepIV) — closer to the ADR paper given the similar pattern of a theoretical error in the core claim.

**Final score:** 4.5

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>