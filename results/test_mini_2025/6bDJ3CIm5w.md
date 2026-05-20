Now I have all the information needed. Let me compose the final consolidated review.

## Summary

This paper studies A/B testing in first-price auction markets with budget-constrained buyers. It proposes a *parallel budget-controlled A/B test* design that runs experiments simultaneously in submarkets, and develops a theoretical framework — based on contaminated first-price pacing equilibria (FPPE) — for debiasing estimates when submarkets are not perfectly isolated. The debiased surrogate (Theorem 1) removes first-order contamination bias ($o(\alpha)$ vs. $\Theta(\alpha)$), and an asymptotic normality result (Theorem 3) provides a basis for inference. Real experiments at Meta and semi-synthetic experiments using historical bidding data support the work.

## Strengths

1. **Novel contamination model for interference in FPPE (Sec. 3–4):** The paper formalizes interference between concurrent A/B tests as supply contamination in the FPPE framework. This is a genuine theoretical contribution — prior FPPE inference work (Liao & Kroer, 2023) assumed no contamination, and the connection between budget-controlled experimentation and equilibrium theory is new. Theorem 1 proves that the debiased surrogate $\tilde{\beta}^*$ achieves bias $o(\alpha)$, improving on the $\Theta(\alpha)$ bias of the raw contaminated equilibrium. This is a clean, non-trivial result.

2. **Asymptotic normality results for debiased estimators (Theorem 3):** The paper provides two asymptotic normality results (general market and under a bid-gap condition) with closed-form influence functions and explicit covariance matrices ($\Sigma_1, \Sigma_2$). This enables confidence interval construction for the debiased pacing multipliers — a capability not available in prior FPPE-based interference models.

3. **Bias reduction confirmed in semi-synthetic experiments (Fig. 3):** Using budgets and values sampled from historical Meta ad auction data, the experiments show that the debiased surrogates reduce normalized bias by roughly a factor of 4–5 across contamination levels $\alpha = 0.1$ to $0.5$, relative to the contaminated limit quantities. The bias reduction grows with $\alpha$, consistent with the theoretical guarantee.

4. **Real-world deployment at Meta (Sec. 1.1, Fig. 1):** The paper reports results from 99 production experiments showing that the parallel budget-controlled design agrees with the gold-standard budget-split design in 75% of cases (79% with a guardrail metric). This demonstrates practical viability in a large-scale advertising marketplace.

## Weaknesses

### Fatal
None.

### Major
1. **Coverage is systematically below nominal (Table 1):** The 95% confidence intervals for $\hat{\beta}$ achieve coverage between 0.826 and 0.877 — well below the nominal level. For revenue, the bootstrap CI coverage ranges from 0.81 to 0.95 (most below 0.91). The paper acknowledges this under-coverage and attributes it to underestimated variance, stating it "deserve[s] more future research," but this is not merely a calibration issue: in the regimes tested ($n=40$ buyers, up to 15,000 items), the method's advertised inferential property does not hold. The abstract's claim that the debiasing technique "achieves the desired coverage properties" is overstated given these results. The paper does not explore finite-sample corrections (e.g., bootstrap-t, variance inflation) or diagnose why the asymptotic variance is underestimated.

2. **Real-world experiment lacks essential details (Sec. 1.1):** The guardrail metric that improves sign agreement from 75% to 79% is never defined. The selection mechanism for the 99 experiments is not described. The treatment effect metric and the meaning of the "neutral" value of 1.0 are not explained. Without this information, the real experiment cannot be interpreted or reproduced, weakening one of the paper's main practical claims.

### Minor
3. **Debiased estimator not applied to real experiments:** The paper's real-world validation (Fig. 1) compares the *raw* parallel design against the budget-split design, but the debiased estimator — which is the paper's central theoretical contribution — is never applied to real data. The semi-synthetic experiments test the estimator, but these use sampled budgets and values, not actual A/B test data. The reader cannot assess whether the debiasing matters in practice or whether its assumptions hold on real interference scenarios. This disconnect between the theoretical contribution and the main empirical evidence is a genuine gap, though the paper is transparent about what each experiment does and does not show.

4. **Sensitivity to $\alpha$ estimation unexplored (Sec. 4):** The estimator assumes $\alpha$ is known. The paper notes that $\alpha$ can be estimated from the data (line 136: "this can often be estimated from historical data; in the parallel A/B test setting, this can be estimated directly from the sampled set of items"), but does not analyze how estimation error in $\hat{\alpha}$ propagates through the debiasing procedure or how it affects the theoretical guarantees (bias $o(\alpha)$, asymptotic normality).

### Trivial
None.

## Nice-to-Haves
- Apply the debiased estimator to the same Meta experiments (or a realistic simulation of them) to directly connect the theoretical contribution to the motivating application.
- Explore finite-sample variance corrections (bootstrap-t, jackknife) to address the coverage gap.
- Provide guidance on practical choices for the step size $\varepsilon_t$ and slackness $\iota_t$ in Hessian estimation.
- Disclose the guardrail metric and experiment selection protocol to make the real experiment independently interpretable.

## Removed Points
*(These points were raised in the individual reviews but are excluded from the final assessment for the reasons stated below.)*

- **"No comparison with alternative debiasing methods":** The paper references related work in App. D (stripped by the parser). The main paper appropriately scopes its contribution — the contamination model is novel and there is no existing comparable method for FPPE-based debiasing. Keeping this criticism would penalize the paper for a missing appendix section that likely exists in the original submission.

- **"α known assumption is unrealistic":** The paper explicitly addresses this (line 136), noting that $\alpha$ can be estimated from historical data or directly from the sampled item set. Downgraded to a minor point about sensitivity analysis rather than an assumption flaw.

- **"Clustering procedure described only qualitatively":** The paper provides a practical description of the graph construction, edge weighting, and balancing constraints (Sec. 1.1). Specifying the exact clustering algorithm would be appropriate for a systems paper but is not expected at the algorithmic level required here.

- **"Missing related works":** Cannot be independently confirmed; the appendix containing related work discussion was stripped by the parser.

- **"Disconnect between real experiments and theory is structural/fundamental":** The paper clearly separates two claims: (1) the parallel design works in practice (real experiments), and (2) the debiased estimator reduces bias (semi-synthetic experiments). The abstract and contributions section are explicit about this division. The disconnect is real but minor, not structural — the paper does not claim to have validated the debiased estimator on real data.

- **All formatting/style nitpicks and typo concerns:** These are parser artifacts, not author errors.

## Novel Insights

The reviews surface an interesting tension that the paper does not fully resolve: the theoretical framework (contamination model) assumes a one-sided contamination story (a clean limit market corrupted by bad items), but in the parallel A/B testing setting, the "bad" items arise precisely because the submarket clustering is imperfect — a design choice made by the experimenter. This means $\alpha$ is not an exogenous nuisance parameter but rather a tunable experimental-design knob that trades off between bias (via contamination) and variance (via submarket size). The paper's current framing treats $\alpha$ as something to debias away rather than optimize over. A more complete treatment would characterize the optimal $\alpha$ given a bias-variance objective, or at minimum provide guidance on how to choose the number/quality of submarkets to balance the cost of contamination against the statistical power gains from parallelization. This direction is latent in the paper's setup but never made explicit.

## Suggestions
1. Address the coverage gap: diagnose whether the variance underestimate stems from the plug-in covariance estimator or from higher-order bias in the debiased surrogate. Show coverage after a finite-sample correction (e.g., bootstrap-t, variance inflation) or clearly characterize the regimes where asymptotic coverage does/does not hold.
2. Disclose the guardrail metric and experiment selection protocol for the real experiment. If space is a concern, a brief description in the main paper with full details in the appendix would suffice.
3. Either apply the debiased estimator to a realistic simulation built from the Meta experiment data (using the actual submarket clustering), or explicitly scope the paper's claims to separate the parallel design validation from the debiased estimator validation more sharply.
4. Add a sensitivity analysis for $\alpha$ misspecification: show how bias and coverage degrade when $\alpha$ is mis-estimated by $\pm 10\%$ or $\pm 20\%$.

## Score and Decision

**Calibration anchors used:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `J7hbPeOZ39.md` | 3.00 | 1 | Weak anchor — flawed method, rejected. Current paper is substantially stronger. |
| `HLxWF7xqiK.md` | 3.00 | 1 | Weak anchor — withdrawn. Current paper is much stronger. |
| `5AJ8R4z5g0.md` | 3.25 | 1 | Weak anchor — rejected with confounder issues. Not comparable. |
| `y2ch7iQSJu.md` | 2.00 | 1 | Weak anchor — rejected. Not comparable. |
| `Ivk2j3uRYh.md` | 4.50 | 1,2 | Similar topic (interference in two-sided markets). Criticized for limited novelty (applying existing methods), no real data. Current paper has stronger novelty and real experiments. |
| `QV6uB196cR.md` | 4.75 | 1,2 | A/B testing interference topic. Had presentation issues, unconvincing experiments. Current paper is more rigorous. |
| `iTjSqQQ4f8.md` | 4.00 | 1 | Data markets paper. Not directly comparable. |
| `eB7T1bqthA.md` | 5.75 | 2 | Poster accepted. Algorithm novelty concerns ("very similar to prior literature"). Current paper has stronger theoretical novelty. |
| `iKLSISIPH7.md` | 4.80 | 2 | Withdrawn. |
| `JQQDePbfxh.md` | 6.50 | 2 | Poster accepted. Clean theory, no experiments. Current paper has experiments but coverage issues. |
| `lsxeNvYqCj.md` | 7.00 | 2 | Spotlight — stronger than current paper. |
| `XZ71GHf8aB.md` | 6.25 | 2 | Withdrawn. |
| `DOXnqYLCcd.md` | 6.50 | 1,2 | Poster accepted. Strong theory + experiments. Current paper is comparable but has coverage gap. |
| `A3YUPeJTNR.md` | 8.00 | 1 | Oral — significantly stronger in completeness. |
| `QuIiLSktO4.md` | 8.00 | 1 | Poster — not comparable topic. |
| `t8FG4cJuL3.md` | 8.00 | 1 | Oral — stronger. |
| `EUSkm2sVJ6.md` | 7.60 | 1 | Oral — stronger. |

**Round 1 bracket:** 4.0 – 7.0. The paper is clearly above the weak anchors (2.0–3.25) and below the top-tier anchors (7.6–8.0).

**Round 2 narrowing:** The paper is stronger than the 4.50 anchor (Random Graph Asymptotics — criticized for limited novelty, no real data) and the 4.75 anchor (A/B testing under Identity Fragmentation — presentation issues, unconvincing experiments). It is comparable to the 6.50 anchor (Private Mechanism Design — clean theory, no experiments; current paper trades coverage issues for experimental validation) and the 5.75 anchor (Pairwise Elimination — algorithm novelty concerns). The paper has genuine theoretical novelty (contamination model) that exceeds the 5.75 anchor's novelty. Its main detractor is the coverage gap and missing real-experiment details, which pull it below the 6.50 anchor's polish.

**Final score:** The paper makes a solid theoretical contribution with real-world grounding, but the coverage gap and incomplete experimental reporting prevent it from reaching the 6.5+ tier. It is stronger than the ~4.5–5.75 papers in this space.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>