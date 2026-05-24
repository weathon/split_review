## Summary

This paper proposes ZNet, a deep learning model that learns instrumental variable (IV) representations from observed covariates X by decomposing them into confounder C = f(X) and instrument Z = g(X) components. The model enforces three constraints derived from standard IV conditions—relevance, exclusion restriction, and unconfoundedness—through a multi-part loss function, and can be used as a plug-in front-end for downstream IV estimators (TSLS, DeepIV, DFIV). Experiments across eight semi-synthetic data scenarios show that ZNet can recover ground-truth instruments when they exist and construct proxy instruments when none are available, with competitive ATE estimates compared to AutoIV, VIV, GIV, and TARNet.

## Strengths

- **Novel approach to learned instruments via explicit IV-condition-inspired losses.** ZNet directly encodes the three IV conditions (relevance, exclusion restriction, unconfoundedness) as trainable loss terms, differentiated from prior variational methods (AutoIV, VIV) that rely on variational inference without explicit causal constraints. The unconfoundedness loss derived from Lemma 1 is a genuine attempt to handle cases where X may be influenced by unobserved confounders U—a setting prior methods explicitly assume away ("Existing methods assume that unobserved confounders do not influence the observed data, while our method relaxes this assumption").

- **Strong instrument recovery results.** In the linear latent categorical setting, ZNet achieves perfect recovery of the true 5-cluster instrument (normalized confusion matrix diagonal = 1.00 for all clusters, Fig. 4). In the mixed-candidate setting, the learned Z dimensions show strong multivariate correlation with true instruments (Fig. 5a,b). In the no-candidate setting (no true instrument exists), ZNet constructs representations that pass relevance and exclusion-restriction tests and show minimal correlation with unobserved confounders U (avg absolute PC = 0.118 on training, Fig. 6).

- **Ablation study convincingly validates the multi-part loss design.** When each constraint (unconfoundedness, exclusion restriction, relevance) is ablated, the R² of predicting true instruments from learned Z drops from 0.84 to at most 0.36; removing all constraints drops R² to 0.02–0.05 (Fig. 5c). This provides direct empirical evidence that all three loss terms contribute meaningfully.

- **Comprehensive evaluation scope.** The paper tests 8 data-generation scenarios (linear/non-linear × disjoint/mixed/latent/no-candidate × with/without U), 3 downstream IV estimators (TSLS, DeepIV, DFIV), and 4 IV-generation baselines (AutoIV, VIV, GIV, TrueIV) plus TARNet. This breadth is unmatched among existing learned-IV papers.

## Weaknesses

### Major

1. **The correlation-based constraints are necessary but not sufficient for IV validity; the paper's claims overreach.** The three constraints enforced by ZNet (Cov(Z, residual)=0, Cov(C,Y)>0 with Cov(Z,C)=0, Cov(T,Z)>0) are observable correlation patterns, not the causal conditions required for IV validity (Z ⟂ e_Y | C, no direct Z→Y path, Z ⟂̸ T | C). The gap is nontrivial: zero covariance between Z and C does not guarantee that Z has no direct effect on Y (exclusion restriction), and zero covariance between Z and finite-sample residuals does not guarantee Z ⟂ e_Y (unconfoundedness) unless the outcome model Φ is perfectly specified. The paper acknowledges "IV estimation in general is limited by a lack of theoretical guarantees of identifiability" (Discussion) yet also claims "Solutions to the ZNet loss minimization problem will always give a representation that serves as an instrument since IV constraints are explicitly embedded in the loss function"—a contradiction. This is a limitation the paper shares with all learned-IV methods (AutoIV, VIV, etc.), but it should be acknowledged more honestly rather than presented as a solved problem.

2. **Table 1 does not convincingly support the claim that ZNet is "on average the highest performing."** ZNet is bolded (best) in approximately 8 of 30 estimator-dataset cells and italicized (second-best) in others, but the pattern is mixed. In several settings (e.g., Linear Disjoint: TARNet −0.025 vs ZNet+DeepIV 0.054, ZNet+DFIV −0.303), simpler methods match or outperform ZNet+IV. Critically, the paper provides no aggregate summary statistic (mean rank, average absolute error across settings, or win/loss count) to support the "on average" claim—the reader must manually inspect 48 cells. The reference to Appendix Tables 9/10 for aggregated results does not substitute for a main-text summary. The claim that "IV generation generally exceeds that of TARNet" is also not consistently supported by the data.

3. **CATE results are relegated entirely to the appendix.** The paper discusses conditional average treatment effects (Section 2, Eq. CATE) and claims "Performance of ZNet is comparable to using the ground truth instrument... for both ATE, Table 1, and CATE, Appendix Tables 3, 4." For a method that outputs (C, Z) representations and targets causal effect estimation, not including CATE metrics (e.g., PEHE) in the main text is a notable gap.

### Minor

4. **No standard deviations or confidence intervals reported for ATE estimates.** The paper reports mean ATE error across 50 bootstraps with significance markers (*/**) for best-vs-second comparisons, but the absence of standard deviations or confidence intervals makes it difficult to assess the variability and reliability of the estimates. This is especially important given the multi-stage tuning procedure and the complex loss landscape.

5. **The dimensionality of Z and C is a critical design choice left unexplained.** The paper notes that ZNet "generates a 10-dimensional variable Z" for the linear mixed dataset but provides no discussion of how the dimensionality of Z or C should be chosen, nor how it affects downstream ATE estimation. This is a nontrivial hyperparameter that strongly influences the bias-variance tradeoff.

6. **Lemma 1 assumes a perfectly specified outcome model Φ.** The practical loss uses residuals Y−Ŷ from a finite-sample neural network Φ(X⊙T). The gap between Ŷ and E[Y|X,T] introduces approximation error that Lemma 1 does not cover. The paper does not discuss this limitation or analyze the sensitivity of results to Φ's specification quality.

## Nice-to-Haves

- A summary statistic (e.g., mean absolute ATE error across all settings, with standard errors) would strengthen the empirical case. A simple win/loss tally against TARNet across all settings would clarify when ZNet+IV helps and when it hurts.
- A sensitivity analysis showing how ATE estimates vary with the dimensionality of Z and with the choice of PC vs MI loss type.
- A brief discussion of settings where ZNet could increase bias relative to TARNet (e.g., weak instruments, severe Φ misspecification) would improve trustworthiness.

## Removed Points
These points were raised by reviewers but removed after cross-checking against the paper. They should be treated with caution.

- **"The tuning procedure introduces potential overfitting to proxy metrics"** — Removed because tuning on validation-set F-statistic and C-Z correlation, then evaluating on held-out test ATE, is standard hyperparameter optimization, not circular overfitting. The paper separates validation-metric tuning from final ATE evaluation.
- **"The recovery of a latent categorical instrument is trivial"** — Removed because it is speculative. The paper shows that the recovered clusters satisfy IV-relevant criteria (relevance, exclusion, low U-correlation), not merely that clustering was achieved.
- **"The graph cannot be interpreted as a standard SCM"** — Removed. The paper's framing of learning "a new SCM" is standard language in the causal representation learning literature; it is clear that f and g are learned functions, not pre-existing causal mechanisms.
- **"Missing standard deviations" and "CATE results"** — Not removed; these are included above as Weaknesses 3 and 4.
- **Strength Finder strength "Explicit encoding of IV conditions via novel unconfoundedness loss"** — Not removed; included as Strength 1 above, with appropriate caveats.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a genuinely novel perspective that the paper itself misses.

## Suggestions

1. **Add an aggregate summary to Table 1.** Report mean absolute error or mean rank across all dataset×estimator combinations, with standard errors across bootstraps, so readers can evaluate the "on average" claim without manual counting.
2. **Include CATE evaluation in main text.** Even a single figure or table showing PEHE or similar metric across the 8 settings would substantially strengthen the empirical case.
3. **Acknowledge the theory-practice gap explicitly.** Add a paragraph in Section 5 or the Discussion clarifying that the correlation constraints are necessary conditions and that, like all learned-IV methods, there is no guarantee that optimizing them recovers a causally valid instrument, though the method is evaluated empirically on this question.
4. **Report standard deviations or bootstrapped confidence intervals** alongside the mean ATE errors.
5. **Discuss the choice of Z and C dimensions** and ideally include an ablation showing ATE sensitivity to this choice.

## Score and Decision

**Round 1 bracket:** The paper sits between weak anchors (avg <3.5) and strong anchors (avg >7.5). The closest topical match is the middle band. Initial bracket: plausible score range [4.5, 6.5].

**Round 2 narrowing:** Compared against anchors in the (4.5, 7.5) range:
- CIV paper (qDhq1icpO8, 6.75, Accept) — stronger theoretical grounding (proof of soundness for conditional IV regression) but narrower evaluation. ZNet has broader experiments but weaker theory. **ZNet is below this anchor.**
- Regularized DeepIV (0gqCIaBRQ9, 5.25, Reject) — rigorous theory but simulated-only experiments. ZNet has a more novel problem formulation and broader evaluation. **ZNet is above this anchor.**
- CFDiVAE (wFf9m4v7oC, 5.75, Accept) — similar structure (representation learning + causal estimation), provided formal identifiability proofs but had proxy-variable limitations. **ZNet is comparable but slightly below; it lacks the formal identifiability guarantees CFDiVAE provides.**
- Adversarial Decomposition (F7XPZnIUHh, 4.20, Reject) — similar decomposition task but had verified theoretical errors. **ZNet is clearly above this anchor.**

**Final score:** 5.5. This reflects a paper with a genuine and novel contribution (learning IV representations via explicit causal-constraint losses, with strong instrument recovery and broad evaluation), but held back by (a) a gap between the correlation-based constraints and causal IV conditions that is not adequately acknowledged or analyzed, (b) empirical results that are competitive but not dominant and lack aggregate statistics to support the strongest claims, and (c) missing standard deviations and main-text CATE evaluation. The paper is above pure algorithm papers (5.25) but below the level of rigor and presentation expected for a top-tier acceptance (6.75+).

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>