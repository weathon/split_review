Now I have a thorough understanding of the paper and the calibration anchors. Let me write the final consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal
### Major
- weakness 1 — why it matters
### Minor
- weakness 1 — why it matters
### Trivial
- weakness 1

## Nice-to-Haves

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision

Let me draft the full review now.

---

Key decisions about which weaknesses to keep/remove:

**Critical Issue 1 (Unfair comparison)**: The paper's HTE learning method (Section 5) uses candidate estimators' predictions in the weighted loss function. The baselines in Table 1 do not have access to these predictions. This is a legitimate concern — the comparison is asymmetric. A simple ensemble baseline (averaging the three candidates) would be a fairer comparison. KEEP as Major.

**Critical Issue 2 (Sample splitting)**: The paper claims "does not require sample splitting" (line 33, 219). Theorem 1 requires n^{-1/4} convergence rates. When neural networks are used for nuisance estimation on the same data, the standard DML theory requires cross-fitting unless the nuisance estimators are Donsker or low-dimensional. The paper uses parametric working models (1) and (2) with a shared representation, which partially addresses this, but the representation is learned adaptively. The paper does not discuss this tension. KEEP as Major.

**Critical Issue 3 (HTE learning method lacks theoretical justification)**: Section 5 provides no theoretical analysis. The paper acknowledges this as a limitation in the conclusion. Since the main contribution is the evaluation framework, this is a Minor issue. KEEP as Minor.

**Section 4.2 note about the loss using unknown true propensity score**: The critic says the loss uses "the unknown true propensity score through $\tilde e(X_i)$" but the paper actually uses the estimated propensity score. Looking at the loss function, $\tilde e(X_i)$ is used which is the probability limit. In practice, the estimated propensity score is used. This is a minor clarity issue. I'll demote to Trivial or remove.

**"correct specification of propensity score is a mild condition" is circular**: This is a valid point. The paper's argument that adaptive representation learning makes the condition mild could be seen as circular. I'll include as a Minor weakness.

Let me now write the review.## Summary

This paper proposes a framework for evaluating heterogeneous treatment effect (HTE) estimators using relative error, relaxing the requirement from Gao (2025) that both outcome regression and propensity score models must be consistent. The key theoretical result (Theorem 1) shows that the proposed relative error estimator is √n-consistent and asymptotically normal provided only the propensity score model is correctly specified and converges faster than n^{-1/4}, even if outcome models are misspecified. The authors design a neural network architecture with a weighted least-squares loss and balance regularizers, and also extend the framework to a new HTE learning method. Experiments on IHDP, Twins, and Jobs datasets demonstrate strong performance in both evaluation accuracy and downstream HTE estimation.

## Strengths

1. **Relaxed consistency requirement for outcome models is a genuine theoretical contribution**: Theorem 1 establishes that the proposed relative-error estimator is √n-consistent and asymptotically normal requiring only that the propensity score model is correctly specified and converges faster than n^{-1/4}, even if outcome regression models are misspecified. This directly delivers on the paper's central claim and is well-motivated by the observation that outcome models rely on extrapolation across treatment groups while propensity score models do not.

2. **Superior selection accuracy while maintaining nominal coverage**: Table 2 shows the proposed method achieves coverage near 0.94–0.96 (target 90%) whereas conventional plug-in estimators achieve nominal coverage but with selection accuracy as low as 0.44 (IHDP, Regression) vs. 0.80 (Ours) and 0.86 vs. 0.94 (Twins, Boosting vs. Ours). This provides concrete evidence that the method transforms valid but uninformative confidence intervals into practically useful ones.

3. **Ablation and sensitivity studies validate the design choices**: Table 5 shows that removing the constraint loss (ℒ_const) degrades √ePEHE_in from 0.638 to 0.725 (IHDP) and selection accuracy from 0.80 to 0.71, while removing ℒ_ce causes a catastrophic failure (√ePEHE_in = 3.495). Table 4 demonstrates that PEHE, coverage, and selection accuracy remain stable over a 10× range of λ₂ (0.5 to 5). Table 6 shows that even with added Gaussian noise to the propensity score, coverage stays between 0.80–0.96 and selection accuracy between 0.74–0.82.

4. **Computational scaling is characterized**: Table 3 reports that runtime grows approximately linearly with sample size (2.527s for n=300 to 3.134s for n=700) and for a small number of candidate estimators (3 estimators: 3.13s) it is competitive with baselines (TARNet: 2.03s).

## Weaknesses

### Major

1. **Sample splitting claim lacks adequate theoretical support.** The paper states twice (line 33, line 219) that the proposed method "does not require sample splitting" and presents this as an advantage over Gao (2025). Theorem 1 requires that the nuisance estimators converge to their probability limits faster than n^{-1/4}. When neural networks estimate the nuisance parameters on the same data used to compute the relative error estimator, establishing √n-consistency and asymptotic normality typically requires additional conditions such as Donsker properties or cross-fitting (Chernozhukov et al., 2018). The paper's parametric working models (1) and (2) with a shared representation Φ(X) partially address this concern, but Φ(X) is learned adaptively by the neural network, making its effective dimension potentially large. The paper acknowledges the convergence rate concern but does not discuss the correlation between nuisance estimation error and the evaluation term that arises without sample splitting. This is a significant gap in the theoretical presentation, especially given that the paper emphasizes the no-sample-splitting property as a key advantage.

2. **The HTE learning method comparison (Table 1) may be unfair.** The proposed HTE learning method (Section 5) trains outcome regression models using a weighted least-squares loss where the weights depend on the predictions of candidate estimators (Causal Forest, X-Learner, TARNet). These candidate predictions provide information not available to any baseline method in Table 1. The baselines (Dragonnet, DCFR, DESCN, etc.) are standard individual estimators that do not leverage the predictions of other methods. A simple ensemble baseline — averaging the predictions of the three candidate estimators — would be a fairer comparison and would help isolate whether the improvement comes from the novel loss/architecture or simply from ensembling/using additional information. The reported improvements (e.g., √ePEHE_in = 0.638 vs. next best 0.741 on IHDP) are striking, but the asymmetric comparison makes it difficult to attribute the gains to the proposed methodological innovations.

### Minor

3. **The HTE learning method (Section 5) lacks theoretical justification.** The proposed aggregation estimator averages outcome regression models across all pairs of candidate estimators, but the paper provides no theoretical analysis of this estimator's properties. Questions left unanswered include: Why should averaging over pairs be an effective strategy? Does the average converge to something meaningful? Is the estimator consistent under any conditions? The paper acknowledges this limitation in the conclusion ("a remaining limitation is our use of a simple uniform averaging scheme"), but for a method that is presented as a contribution and evaluated in Table 1, the absence of any theoretical grounding is a gap. The main contribution of the paper is the evaluation framework, so this is not a fatal issue, but it weakens the learning method as a standalone contribution.

4. **The claim that correct propensity score specification is "a mild condition" is somewhat circular.** The paper argues (Section 4.4) that because Φ(X) can be adaptively learned, the parametric logistic working model can approximate the true propensity score. But if the representation is learned flexibly, the effective dimensionality grows with sample size, which could affect the convergence rates required by Theorem 1. The tension between flexibility for the propensity score model and the parametric-rate convergence requirement is not addressed.

### Trivial

5. The notation in the Taylor expansion (Section 4.1) uses the same symbols for probability limits and estimates, making the derivation slightly harder to follow at first reading.

## Nice-to-Haves

- The paper could clarify that the weighted least-squares loss uses the estimated propensity score (not the unknown true one) in practice, acknowledging the two-step estimation error.
- A comparison against an ensemble baseline (simple averaging of the three candidate estimators' predictions) would strengthen the HTE learning claims.
- A brief remark about why the standard DML cross-fitting concerns do not apply in the specific parametric working model setup, or a reference to similar results derived without sample splitting, would improve the theoretical presentation.

## Removed Points

These points from the reviewers were removed for the following reasons:

- **"The HTE learning method is an underdeveloped add-on"** — This overlaps with Weakness #3 above. The method is indeed presented without theory, but the paper frames it as a secondary application of the evaluation framework, not a primary contribution. The experimental results are strong. Moved to Weakness #3 (Minor).

- **"The loss uses the unknown true propensity score"** — The paper writes the loss with $\tilde e(X_i)$ but uses the estimated propensity score in practice. This is a notational issue, not a substantive error. The critic's concern about a two-step estimation error is valid but is already addressed by the convergence rate conditions in Theorem 1. Removed as it misreads the intention.

- **"Missing appendix, missing proofs, missing related works"** — The parser strips these sections; they exist in the original submission. Removed per hard rules.

- **"Typos, grammar, formatting"** — These are parser artifacts, not author errors. Removed per hard rules.

- **"No sample-splitting required" as a strength** — Given the theoretical concern in Weakness #1, this is not a clean strength. Removed from strengths.

- **"State-of-the-art HTE estimation performance"** — The strength itself is valid, but given the potential unfair comparison issue (Weakness #2), the claim should be interpreted with caution. The experimental results are real, but the baseline comparison is asymmetric. The strength is retained but with this caveat implicitly noted.

## Novel Insights

The paper's core insight — that the relative error framework can be made robust to outcome model misspecification by carefully designing loss functions that enforce score conditions derived from the influence function — is genuinely novel and well-executed. The observation that outcome models are more prone to extrapolation errors than propensity score models (Section 3) is clearly articulated and provides a strong practical motivation. The design of the weighted least-squares loss to satisfy the first condition in Eq. (4) even under misspecified outcome models is a clever piece of methodological engineering. None beyond the paper's own contributions.

## Suggestions

1. **Address the sample splitting concern**: Either provide a proof sketch showing why the specific parametric working model with adaptively learned Φ avoids the standard DML concerns, or acknowledge that cross-fitting is recommended when using neural networks for nuisance estimation and show that the method still works empirically without it. A brief discussion of empirical process conditions would significantly strengthen the theoretical contribution.

2. **Add a fair ensemble baseline for Table 1**: Compare the proposed HTE learning method against a simple averaging of the three candidate estimators' predictions (Causal Forest, X-Learner, TARNet). If the proposed method still outperforms this ensemble, that would isolate the value of the learned outcome regression models. If not, the contribution of the learning method is weakened and the paper should refocus on the evaluation framework.

3. **Provide intuition or a simple result for the HTE learning method**: Even a brief argument showing that the aggregated estimator is consistent for τ(x) under certain conditions (e.g., when the propensity score is correctly specified) would significantly improve the paper. Alternatively, if the learning method is intended as a secondary application, acknowledge its exploratory nature more explicitly.

4. **Discuss the effective dimension of the learned representation**: The paper should address the tension between adaptive representation learning (which makes the propensity score model flexible) and the parametric convergence rates required by Theorem 1.

## Score and Decision

**Round 1 (bracketing)**: I retrieved anchors across three bands. Weak anchors (avg 2.33–3.40) had fundamental flaws; this paper is clearly above that range. Middle anchors (avg 4.25–7.33) had solid contributions with some weaknesses; this paper fits within this band. Strong anchors (avg 8.00) were polished papers with minimal weaknesses; this paper has non-trivial unresolved issues. **Initial bracket: between 5.5 and 7.5.**

**Round 2 (narrowing)**: I retrieved anchors within the (5.5, 7.0) and (6.0, 7.5) ranges. The most relevant comparisons:

- **6.00 (Accept)** — "Do Contemporary CATE Models Capture Real-World Heterogeneity?" — Large-scale benchmark with some overclaiming. This paper has a stronger theoretical contribution, clearer motivation, and more innovative methodology. **This paper is stronger.**
- **6.00 (Reject)** — "Nuisance-Robust Weighting Network" — Had missing related work and clarity issues. This paper is better written and more complete. **This paper is stronger.**
- **6.25 (Accept)** — "Stabilized Neural Prediction of Potential Outcomes in Continuous Time" — Solid method, some limitations. Comparable in quality but on a different problem. **Comparable.**
- **6.33 (Accept)** — "Treatment Effects Estimation By Uniform Transformer" — Good method with experiments. This paper has stronger theoretical grounding. **This paper is slightly stronger.**
- **6.50 (Accept)** — "Bayesian Neural Controlled Differential Equations" — Interesting uncertainty quantification. The theoretical contribution here is comparable. **Roughly comparable.**
- **7.00 (Accept)** — "Model-agnostic meta-learners for estimating HTE over time" — Comprehensive theory and experiments. That paper has more complete theoretical analysis. **This paper is slightly weaker.**
- **7.33 (Accept)** — "Variational Framework for Continuous Treatment Effects with Measurement Error" — Strong theoretical and empirical contribution. **This paper is slightly weaker.**

The paper under review has a genuine theoretical contribution and thorough experiments, but the unresolved sample splitting concern and the asymmetric comparison in the HTE learning part prevent it from reaching the 7+ range occupied by papers with more complete theoretical justification. It is stronger than the 6.00 anchors and comparable to the 6.25–6.50 anchors, placing it around **6.5**.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>