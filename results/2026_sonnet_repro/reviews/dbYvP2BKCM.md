Now let me do the calibration search to determine the score.Now I have enough information to write the final consolidated review.

---

## Summary

ZNet is a multi-armed neural network that decomposes observed covariates into an instrument representation *Z = g(X)* and a confounder representation *C = f(X)*, subject to three loss-based constraints encoding IV relevance, exclusion restriction, and unconfoundedness. The learned representations can then serve as plug-in inputs to any downstream two-stage IV estimator (TSLS, DeepIV, DFIV). The paper targets settings where no domain-specified instrument exists, including the challenging "No Candidate" regime in which all features are potentially confounded by unobserved *U*.

---

## Strengths

- **Instrument recovery from observed candidates.** In the Linear Mixed Candidate dataset, ZNet's learned 10-dimensional Z is demonstrably correlated with the true instruments X₁₃, X₁₄, X₁₅ (Figure 5a,b). An ablation over each loss component (Figure 5c) confirms that all three constraints are causally necessary for recovery — ablating any single constraint degrades the correlation with the true instruments. This is a concrete, verifiable result.

- **Recovery of latent categorical instruments.** Figure 4 shows a near-perfect 5-class confusion matrix on the Linear Categorical Instrument dataset, demonstrating that the learned representation can capture a hidden discrete structure without explicit supervision.

- **Consistent ATE bias reduction across eight scenarios.** Table 1 shows that across all linear and non-linear data-generating processes, ZNet's ATE errors are consistently among the two best of the IV generation methods. Standout cases: Linear No Candidate (ZNet+TSLS = 0.025 vs. TARNet = 0.240); Non-linear No Candidate (ZNet+DFIV = 0.049 vs. TARNet = 0.423). Statistical significance markers (*/**) confirm many of these differences are not noise.

- **Comprehensive and fair benchmarking.** The evaluation spans eight semi-synthetic settings (linear/non-linear × four instrument-availability classes), three downstream estimators, three competing IV-generation baselines (AutoIV, GIV, VIV), and an observational baseline (TARNet), making it the most complete empirical comparison in this subfield.

---

## Weaknesses

### Fatal
None that invalidate the entire empirical contribution.

### Major

- **Proof error in Lemma 1 undermines the key theoretical claim.** Lemma 1 is presented as the theoretical justification allowing ZNet to handle settings where *X* may be influenced by *U* — the main differentiator over prior VAE-based IV methods. The paper's proof writes (line 4):

  > E[Z · e_Y] − E[Z] · E[e_Y|X,T] = Cov(Z, e_Y)

  This step factorises E[Z · E[e_Y|X,T]] as E[Z] · E[e_Y|X,T], which would only be valid if *Z* and E[e_Y|X,T] are independent. But Z = g(X) by construction, and E[e_Y|X,T] is a function of *X*, so these are not independent. The correct expansion gives:

  > Cov(Z, e_Y) = E[Z · E[e_Y|X,T]]

  which is not necessarily zero. The claim that minimizing Cov(Z, Y − Ŷ) implies Cov(Z, e_Y) = 0 in the confounded-X regime therefore lacks a valid proof. This is not merely a formatting artifact — it is the specific algebraic step in the published proof. The paper can still be read as providing a useful empirical regularizer for unconfoundedness, but the theoretical claim that "our method produces an instrument even more generally when X may be influenced by U" (Section 3) is not supported as proved. This matters because it is the paper's primary stated theoretical advance over AutoIV, VIV, and related methods.

- **Hyperparameter tuning uses a biased proxy in confounded settings.** Section 5.3 explicitly states that downstream estimators (DeepIV, DFIV, TARNet) are tuned by jointly minimizing "the MSE of the model's ATE against a nearest-neighbors (NN) ATE and the MSE of estimated Y on factual Y." NN-ATE is a purely observational estimator that does not adjust for unobserved confounding. In the No Candidate rows with *X^{←U} ≠ ∅* — where confounding is strongest and ZNet's contribution is most important — the tuning target is biased toward the confounded observational association rather than the true causal effect. All competing methods are tuned the same way, so the relative ranking among IV methods is not obviously distorted, but the absolute interpretation ("ZNet reduces confounding bias") rests partly on hyperparameters selected to match a biased proxy. This concern applies most directly to the Linear/Non-linear No Candidate rows of Table 1.

### Minor

- **Weak test-set instrument relevance in the hardest setting.** Figure 6(a) reports F = 1.83 (p = 0.081) for the test split on the Non-linear No Candidate dataset. By conventional rule-of-thumb (F > 10), this is a weak instrument on the hold-out data. Weak instruments inflate IV regression variance and can bias estimates toward OLS. The paper reports good downstream ATE error in this setting (ZNet+DFIV = 0.049), but does not discuss whether this result is robust to the weak test-set F or coincidental given the specific bootstrap.

- **Overclaim in Discussion.** Section 7 states: "Solutions to the ZNet loss minimization problem will always give a representation that serves as an instrument since IV constraints are explicitly embedded in the loss function." Minimizing a loss term toward zero does not guarantee satisfying the underlying structural IV conditions, especially under finite samples and local minima. The paper is appropriately cautious elsewhere ("IV estimation in general is limited by a lack of theoretical guarantees"), making this sentence inconsistent.

- **TrueIV underperforming ZNet in some settings.** In the Linear Latent row, ZNet+TSLS gives −0.125 vs. TrueIV+TSLS = −0.524. Since TrueIV is the ideal case, this discrepancy deserves a brief explanation (e.g., whether TrueIV was subjected to the same hyperparameter tuning pipeline, and whether the latent categorical instrument is naturally weak for TSLS).

### Trivial
None beyond what is already addressed above.

---

## Nice-to-Haves

- **Reframe Lemma 1 or supply a corrected proof.** If a correct version holds under additional assumptions (e.g., given some structural property of E[e_Y|X,T] relative to *Z*), state them explicitly. Otherwise, reframe Constraint 1 as an empirical regularizer motivated by heuristic intuition rather than a proved guarantee. Even a short honest note ("no formal guarantee holds in the confounded-X regime; ZNet is a heuristic in this setting") would substantially strengthen the paper's credibility.

- **Weak-instrument sensitivity analysis.** The test F = 1.83 case (Non-linear No Candidate) warrants a bootstrap-level analysis showing how ATE estimation error correlates with test-set F-statistic across bootstrap replications. This would clarify whether ZNet's performance in this hardest setting is systematic.

- **Ablation at the ATE level.** Figure 5(c) ablates on instrument recovery correlation (R² values) for a single dataset. An ablation on downstream ATE error across datasets would more directly support the paper's main claim that each constraint is necessary for good causal effect estimation.

- **Alternative hyperparameter tuning criterion.** Replacing NN-ATE as the tuning target with a criterion that does not assume away confounding (e.g., IV-based cross-validation, or using the training-set F-statistic alone for instrument generation and a held-out ATE against the known ground truth for downstream estimator tuning) would make the evaluation cleaner.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Confusion matrix perfect recovery concerns (Section 6.2, Figure 4).** The harsh critic suggests cherry-picking or easy clustering. However, the paper cites a synthetic dataset specifically designed to have a latent categorical instrument — expecting high recoverability is not unreasonable. Without specific evidence of cherry-picking or cherry-picked seed, this remains speculative.

- **Signed mean error allows cancellation.** True in principle, but this applies symmetrically to all methods and is standard in the ATE estimation literature. Not a flaw specific to ZNet.

- **"No Candidate" identifiability impossibility argument.** The harsh critic argues that no deterministic function of confounded X can produce a truly unconfounded instrument. This is a legitimate philosophical concern, but it is speculative in the sense that it asserts an impossibility that the paper's empirical results partially contradict (low Z–U correlations in Figure 6c). The paper does not claim theoretical identification; it claims empirical utility. The empirical utility may rest on approximate satisfaction rather than exact guarantees.

- **Code not publicly available.** The paper states "code will be made public upon publication" — this is standard at submission time and does not constitute a weakness under review rules.

- **Exclusion restriction not truly enforced by Constraint 2.** The critic notes that Cov(Z,C) = 0 is weaker than the true exclusion restriction. This is methodologically true but is acknowledged implicitly by the empirical F-test in Figure 6(b). Given that the paper presents this as an approximate enforcement rather than a formal guarantee, the concern is partially addressed and minor.

- **Strength: "Novel loss design relaxing the U-not-affecting-X assumption."** Moved here because this is exactly the strength that is undermined by the Lemma 1 proof error. When a strength and weakness conflict, the weakness wins.

---

## Novel Insights

The harsh critic raises a genuine and underappreciated theoretical point: the factorization step in the Lemma 1 proof fails precisely because Z = g(X) and E[e_Y|X,T] share X as a common input. This is not noise from a category sweep — it is a verifiable algebraic error with a specific counterexample structure. More broadly, any decomposition-based IV method that learns Z as a function of potentially confounded X must grapple with the circular dependency this creates in unconfoundedness proofs; ZNet's attempt to resolve this through the residual Cov(Z, Y − Ŷ) regularizer is an interesting idea but needs a corrected theoretical treatment to claim it succeeds.

---

## Suggestions

1. **Fix or reframe Lemma 1.** Check whether the result holds when an additional conditional independence assumption is imposed on E[e_Y|X,T] relative to Z. If not, explicitly classify Constraint 1 as an approximate/empirical regularizer.
2. **Replace NN-ATE tuning target** with an IV-relevant validation criterion (e.g., training-set F-statistic for IV generation; known-ATE MSE on a synthetic validation fold for downstream estimators).
3. **Add a weak-instrument robustness analysis** for the Non-linear No Candidate setting (test F = 1.83).
4. **Explain the TrueIV underperformance** in the Linear Latent row (−0.524 vs. ZNet's −0.125) with TSLS, or verify equivalence of tuning protocols.
5. **Soften the Section 7 claim** about "always" producing valid instruments to match the more careful language elsewhere in the paper.

---

## Score and Decision

**Round 1 bracket:** Based on the topical similarity to qDhq1icpO8 (6.75, Accept; IV + representation learning) and the rejection of F7XPZnIUHh (4.2; decomposed representations with a key proof error), the paper sits in a 4.5–6.5 bracket.

**Round 2 anchors and comparisons:**

| Path | Avg Score | Round | Comparison to ZNet |
|------|-----------|-------|--------------------|
| qDhq1icpO8 | 6.75 | R1/R2 | More rigorous theory, similar evaluation scope; ZNet is slightly weaker theoretically but broader empirically |
| Oc4ji1iCjQ | 6.75 | R2 | Automatic generation of statistical surrogates—very similar concept; that paper was also rejected despite a high avg |
| wFf9m4v7oC | 5.75 | R2 | Front-door VAE with proper identifiability theorem; ZNet has better empirical coverage but weaker theory |
| qe1CsfnN1W | 6.25 | R2 | Causal effect with latent confounders, accepted; comparable scope but cleaner theoretical contribution |
| x2rZGCbRRd | 5.50 | R2 | Variable decomposition for treatment effects, rejected; similar in scope, ZNet has broader evaluation |
| F7XPZnIUHh | 4.20 | R1 | Decomposed IV representations with proof errors AND novelty concerns; ZNet has stronger novelty |
| TC9r8gsaoh | 6.00 | R1 | Weighting network for causal inference; different approach, comparable quality |

**Narrowing:** ZNet is stronger than F7XPZnIUHh (4.2) due to genuine novelty and comprehensive evaluation, but weaker than qDhq1icpO8 (6.75) due to the Lemma 1 proof error — which is precisely the paper's main theoretical differentiation claim. The biased hyperparameter tuning further weakens confidence in the absolute empirical claims in the most important (confounded No Candidate) settings. Comparing to wFf9m4v7oC (5.75, Accept), ZNet's evaluation breadth is superior but its theoretical soundness is inferior. ZNet is roughly comparable to x2rZGCbRRd (5.5, Reject) and slightly below wFf9m4v7oC (5.75, Accept). 

**Final assessment:** The paper addresses a genuinely important problem, proposes a coherent and practical architecture, and provides the most comprehensive empirical comparison in this subfield. However, the proof of Lemma 1 contains a verifiable algebraic error that undermines the paper's primary stated theoretical advance over prior methods; the empirical evidence is complicated by using a confounded estimator as a hyperparameter validation target in the most challenging settings. These are correctable issues, but as written the paper overclaims its theoretical contribution and the empirical protocol has a methodological gap. Score: **5.0, Reject**.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>