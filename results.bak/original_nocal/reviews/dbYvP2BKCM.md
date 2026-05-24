Now I have thoroughly examined all the evidence. Let me write the final consolidated review.

## Summary

The paper proposes ZNet, a deep learning method that learns instrument representations Z and confounder representations C from observed covariates X by enforcing standard IV assumptions (relevance, exclusion restriction, unconfoundedness) through a multi-part loss function. The learned representations can then be plugged into downstream IV estimators (TSLS, DeepIV, DFIV) for causal effect estimation. The method is evaluated on semi-synthetic datasets spanning four instrument-existence scenarios (Disjoint, Mixed, Latent, No Candidate) with linear and non-linear response functions.

## Strengths

- **Learns instrument representations without requiring pre-specified instruments in the data.** Section 3 explicitly states "We do not assume that instruments exist as a subset of the observed data." The "No Candidate" experiments (Table 1) demonstrate that ZNet produces ATE estimates that reduce bias compared to TARNet in settings where no explicit instrument exists by construction (e.g., Linear No Candidate: ZNet+TSLS ATE error 0.025 vs TARNet 0.240; Nonlinear No Candidate: ZNet+DeepIV ATE error 0.260 vs next-best 0.422).

- **Recovers ground-truth instruments with high fidelity when they exist.** In the linear latent-categorical setting, Figure 4 shows a perfect normalized confusion matrix (diagonal entries = 1.0) between the true 5-cluster instrument and ZNet's recovered Z after K-Means. In the mixed-candidate setting, Figure 5a,b shows strong univariate and multivariate correlations between ZNet's Z and true instruments X13, X14, X15. The ablation study (Figure 5c) confirms each constraint contributes to this recovery.

- **Comprehensive evaluation covering diverse data-generation scenarios.** Section 6.1 defines four instrument-existence classes (Disjoint, Mixed, Latent, No Candidate), each with linear/nonlinear response and with/without unobserved confounding. Table 1 reports ATE errors across eight settings, comparing ZNet against AutoIV, VIV, GIV, and TARNet with three downstream estimators, making this one of the broadest reported evaluations in the IV-generation literature.

- **Plug-in compatibility with multiple downstream estimators.** ZNet's learned C and Z can be used with TSLS, DeepIV, and DFIV (Section 5.2), functioning as a standalone module that does not require modifying the downstream estimator.

## Weaknesses

### Fatal
None.

### Major

- **Lemma 1's proof contains a mathematical error, undermining the theoretical justification for the unconfoundedness constraint when X is influenced by U.** The proof (lines 95-99) claims 𝔼[Z·𝔼[e_Y|X,T]] = 𝔼[Z]·𝔼[e_Y|X,T]. This step is invalid: 𝔼[e_Y|X,T] is a random variable (a function of X,T), so 𝔼[Z]·𝔼[e_Y|X,T] remains a random variable while 𝔼[Z·𝔼[e_Y|X,T]] is a scalar — the equation is dimensionally inconsistent. The equality would require Z ⟂ 𝔼[e_Y|X,T], which is not given and is essentially what needs to be shown. This invalidates the Lemma as written. Since the paper relies on this lemma to claim (line 441-442) that ZNet "relaxes" the standard assumption that observed variables X are not influenced by U, this central theoretical claim is unsupported. The method's practical performance may still be reasonable (Figure 6c provides partial empirical support via low average absolute correlation ~0.1 between Z and U), but the paper overstates its theoretical grounding.

- **Gap between the stated IV condition (full independence) and what is enforced (zero covariance).** The paper states the unconfoundedness condition as "Z ⟂ e_Y | C" (line 41), which requires full conditional independence. However, the primary loss term L_{Z↔ε_Y}^{PC} (Eq. 6) minimizes squared Pearson correlation — a measure of linear association. Zero correlation does not imply independence in general, especially in the non-linear settings the paper evaluates. While the paper mentions using mutual information (MI) as an alternative (line 135), the results do not distinguish when PC vs. MI is used, and the core theoretical framing still asserts a stronger condition than the loss enforces. The paper does not discuss the conditions under which zero covariance suffices for the downstream estimators (e.g., TSLS requires uncorrelatedness; DeepIV requires conditional mean independence).

- **Missing uncertainty measures in primary results.** Table 1 reports only mean ATE errors over 50 bootstraps with no standard deviations, confidence intervals, or standard errors. The significance notation (*, **) is described qualitatively but no statistical test is specified. Given that many entries are close (e.g., Linear No Candidate: ZNet+DeepIV −0.033 vs AutoIV+DeepIV −0.017), readers cannot assess whether differences are meaningful or due to noise.

### Minor

- **Hyperparameter tuning uses proxy metrics rather than downstream ATE.** ZNet's loss weights, PC/MI choice, and gradient surgery settings are tuned by maximizing the F-statistic of Z→T and minimizing Corr(C,Z) (line 169), which are proxy metrics for instrument quality rather than the final causal estimand. The paper does not report sensitivity of ATE error to these hyperparameter choices or validate that the Pareto-front selection correlates with low ATE error.

- **Performance is not uniformly dominant across settings.** In Table 1, ZNet is the top or second-top method in many settings but is sometimes outperformed by AutoIV (e.g., Linear No Candidate (no U): AutoIV+DeepIV −0.017 vs ZNet+DeepIV −0.033; Non-linear Latent: AutoIV+DeepIV −0.008 vs ZNet+DeepIV −0.039) or VIV. The paper's claim of "superior performance" (line 441) is too strong — a more measured claim of "competitive performance" would be more accurate.

### Trivial
None.

## Nice-to-Haves

- Report standard deviations or error bars alongside mean ATE errors and specify the statistical test used for significance notation.
- Add a non-parametric independence test (e.g., distance covariance) to verify whether the learned Z actually satisfies Z ⟂ (Y − φ(C,T)) | C, not just zero correlation.
- Evaluate on a real-world dataset with a known valid instrument (e.g., from economics or genetics) to demonstrate translation from semi-synthetic to real data.
- Show sensitivity of ATE error to the loss weight hyperparameters α_i to validate that the chosen Pareto-front point is robust.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. *"No Candidate evaluation is circular; ZNet cannot be verified to work in real observational studies"* — REMOVED. Semi-synthetic evaluation with known ground truth is standard practice in causal inference. The observation that this does not guarantee real-world performance is a generic limitation of all such evaluations, not a specific flaw. The paper does precisely what is standard: generate data where ground truth is known and test whether the method recovers it.

2. *"Hyperparameter tuning introduces data leakage because ZNet is tuned on the training set"* — REMOVED. The paper does not explicitly state which split is used for ZNet hyperparameter tuning. The concern about proxy metrics not aligning with downstream ATE is retained (see Minor), but the specific leakage claim is not verifiable from the paper text.

3. *"The evaluation cannot support the conclusion that ZNet reduces bias when no instrument exists"* — REMOVED (partially). The No Candidate experiments directly compare ATE error against ground truth and show ZNet reduces bias relative to TARNet and is competitive with other methods. This IS evidence that ZNet can construct useful proxy instruments. The critic's stronger claim that this is "circular" misunderstands the experimental design.

4. *"Reproducibility failure — data generation details not sufficiently specified"* — REMOVED. The paper references Wu et al. (2023) for functional forms, which is standard practice. The use of IHDP covariates with defined subsets (X→T, X→Y, X←U) is described.

5. *"Non-linear No Candidate: F=1.83, p=0.0813 on test split suggests relevance fails"* — REMOVED. The paper evaluates test performance separately. The F-statistic on the test split is weak (p=0.08), which is actually acknowledged in the figure. The training and validation splits show strong relevance.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Fix Lemma 1.** Provide a correct proof or replace it with a properly justified condition (e.g., using the law of iterated expectations: if Z = g(X) and the true residual Y − 𝔼[Y|X,T] is mean-independent of X, then Cov(Z, residual) = 0 automatically — but this does not imply Cov(Z, e_Y) = 0; it's a different identification strategy that should be stated honestly).

2. **Tone down claims.** Replace "ZNet relaxes the assumption that observed variables are not influenced by U" with a more measured statement acknowledging that the method provides an approximate heuristic supported by empirical evidence, not a formal relaxation.

3. **Clarify the independence vs. correlation gap.** State explicitly which IV conditions the losses enforce (uncorrelatedness vs. independence) and under what assumptions each downstream estimator's identification is valid given the enforced conditions. If MI-based losses are used for non-linear settings, report when PC vs. MI is selected by the tuning procedure.

4. **Report uncertainty.** Add standard deviations or bootstrapped confidence intervals to Table 1 and specify the statistical test used for significance annotations.

5. **Scope the "No Candidate" claims more carefully.** Acknowledge that learning an instrument from the same data that is confounded involves untestable assumptions, and that the No Candidate experiments demonstrate the method on semi-synthetic data specifically — not that ZNet can create valid instruments from nothing in arbitrary real settings.

## Score and Decision

The paper addresses an important problem and presents a clean, modular architecture with broad empirical evaluation. However, the flawed proof of Lemma 1 undermines the paper's central theoretical claim to "relax" a standard assumption, and a gap between the stated IV condition (full independence) and what is enforced (zero covariance) is not addressed. These issues are major but not fatal — the method retains practical value and the empirical results are informative. The paper requires substantial theoretical revision and more careful scoping of claims before it meets the bar for acceptance.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>