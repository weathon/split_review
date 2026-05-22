Now I have all the information I need. Here is my consolidated final review.

---

## Summary

This paper proposes ZNet, a deep neural architecture that learns instrument and confounder representations from observed covariates for downstream IV-based causal effect estimation. The key idea is to decompose the observed feature space into an instrument component Z = g(X) and a confounder component C = f(X) by enforcing three constraints (relevance, exclusion restriction, and unconfoundedness) through a multi-loss objective. Experiments across 16 semi-synthetic data settings (covering linear/nonlinear, disjoint/latent/mixed/no-candidate instrument scenarios) with three downstream estimators (TSLS, DeepIV, DFIV) show that ZNet recovers ground-truth instruments when they exist and produces competitive ATE estimates.

## Strengths

- **Well-designed architecture that mirrors the IV structural causal model.** ZNet's explicit decomposition into Z = g(X) and C = f(X) with loss terms for relevance, exclusion restriction, and unconfoundedness is a principled approach that differs from variational autoencoder methods (AutoIV, VIV). This allows direct control over instrument validity rather than relying on unsupervised disentanglement.

- **Convincing empirical demonstration of instrument recovery.** Figure 4 shows a near-perfect confusion matrix for recovering a 5-cluster latent categorical instrument (diagonal entries all 1.0). The ablation study in Figure 5c confirms that removing each constraint degrades recovery, directly substantiating the claim that the loss terms work as intended.

- **Strong evidence that ZNet constructs valid proxy instruments even when no candidate instrument exists.** Figure 6 provides three complementary diagnostics on the Nonlinear No Candidate dataset: relevance (F=15.34, p=8.06e-21), exclusion restriction (non-significant F=0.58, p=0.446), and low average absolute Pearson correlation (0.118) with unobserved confounders U. This is the method's most interesting capability and is well-supported.

- **Comprehensive evaluation across diverse data-generating scenarios.** The paper covers 8 dataset configurations × 3 downstream estimators, plus ablation studies, instrument recovery analysis, and comparisons against AutoIV, VIV, GIV, TrueIV, and TARNet. This breadth gives a clear picture of when the method works well and when it struggles.

## Weaknesses

### Major

- **Lemma 1 proof is mathematically incorrect.** The proof of Lemma 1 (Section 3) contains an algebraic error: it treats E[Z·E[e_Y|X,T]] as E[Z]·E[e_Y|X,T] at the fourth equality. Since E[e_Y|X,T] is a random variable (function of X,T), not a scalar, the step E[Z·E[e_Y|X,T]] = E[Z]·E[e_Y|X,T] is mathematically invalid. The conclusion that Cov(Z, e_Y - E[e_Y|X,T]) = 0 implies Cov(Z, e_Y) = 0 does not follow from the presented derivation. This undermines the paper's claim that the method "relaxes this assumption" that unobserved confounders do not influence observed data. The unconfoundedness loss (Equation 6) may still work as a heuristic, but the theoretical justification provided for it is unsound. This issue does not invalidate the entire paper—the empirical instrument recovery and competitive ATE results stand independently—but it does mean a central advertised contribution is unsupported.

- **Missing uncertainty quantification for all ATE results.** Table 1 reports only mean absolute ATE error across 50 bootstrap resamples but provides no standard errors, confidence intervals, or error distributions. Without this information, the reader cannot assess whether the differences between methods are meaningful. The significance notation (single/double asterisks comparing top two methods against the rest) is non-standard and does not substitute for proper paired bootstrap inference. Several values in Table 1 are very large (e.g., AutoIV at 10.821 and -25.181), suggesting instability that is never analyzed.

- **Overclaimed language not supported by the evidence.** The abstract and discussion assert "superior" instrument representations and that ZNet "exceeds" existing methods. Table 1 shows that ZNet is competitive rather than uniformly dominant: it is bolded (best) in roughly 8–10 of 48 dataset×estimator cells and italicized (second) in several others, but in many settings other methods match or beat it. The paper would be more credible with measured language that accurately reflects competitive performance rather than claiming superiority.

### Minor

- **The bootstrap procedure is underspecified.** It is unclear whether ZNet is retrained from scratch on each bootstrap sample or only the second-stage regression is re-run. These produce very different variance estimates, and the distinction matters for interpreting Table 1.

- **The claimed guarantee that ZNet "always gives a representation that serves as an instrument" (Section 7) is too strong.** Embedding constraints in a soft loss with non-convex optimization does not guarantee constraint satisfaction. The paper acknowledges IV limitations generally later in the same paragraph, but the "always" phrasing is misleading.

- **Hyperparameter tuning procedure may create subtle asymmetry.** While all IV generation methods are tuned on the same objective (maximize relevance F-statistic, minimize C–Z correlation), ZNet's loss explicitly optimizes these quantities while the other methods were not designed around this proxy. Combined with ZNet's many hyperparameters (loss weights, PC vs. MI selection, gradient surgery), there is a risk of overfitting to the validation metric. The paper does not discuss this.

- **Missing experimental details.** The operator ⊙ in Φ(X ⊙ T) is never defined (element-wise product? concatenation?). The symbol mismatch between L_{Z↔ε_Y}^{PC} in Equation 6 and L_{Z↔Y}^{PC} in the text is confusing. Hyperparameter ranges and final selected values are not reported, hindering reproducibility.

### Trivial

- None that meet the threshold (formatting issues are parser artifacts, not author errors).

## Nice-to-Haves

- A simple real-data example with a known instrument (e.g., Card's college proximity data) would ground the method and demonstrate that learned Z recovers interpretable structure.
- Reporting computational cost and training time would help practitioners assess applicability.
- An analysis of cases where ZNet's learned instrument is weak and how the second-stage estimator behaves under such weakness would strengthen the evaluation.

## Removed Points

- **Strength Finder's claim about Lemma 1 being a strength**: Removed because Lemma 1's proof is invalid; it cannot serve as a valid strength.
- **Criticism about "no real-world dataset"**: Weakened to nice-to-have; semi-synthetic evaluation with known ground truth is the standard for this type of causal inference paper and is appropriate for the claims made.
- **Criticism about mutual information/KDE bandwidth selection**: This is a minor detail deferred to the appendix; not central enough to list as a weakness.
- **Criticism about the confusion matrix being "approximate" recovery**: The matrix shows perfect diagonal recovery; the criticism was inaccurate.
- **Criticism about missing related works**: Cannot be assessed without external sources.

## Novel Insights

An interesting pattern emerges from comparing the paper's strengths and weaknesses: ZNet's most compelling evidence comes from the *diagnostic* evaluations (instrument recovery in Figures 4–5, constraint satisfaction in Figure 6) rather than from the downstream ATE table. The diagnostic evaluations directly validate that the loss constraints achieve their intended effect (relevance, exclusion, low U-correlation), while the ATE results are noisier and harder to interpret. This suggests that the method's real value may lie in generating *interpretable intermediate representations* that can be validated before being fed into downstream estimators, rather than in achieving uniformly lower ATE error. The paper could lean into this framing — positioning ZNet as a structured representation-learning tool whose outputs can be checked for IV validity before use — which would make the contribution more robust to the Lemma 1 issue.

## Suggestions

1. **Fix or remove Lemma 1.** The easiest path is to present the unconfoundedness loss as an empirically motivated heuristic without claiming theoretical guarantees for handling U→X. The paper's empirical contributions are strong enough to stand without this claim.

2. **Add standard errors or confidence intervals** to all ATE estimates in Table 1 using paired bootstrap (with ZNet retrained per bootstrap iteration to capture full variance). Replace the non-standard significance notation with proper statistical tests.

3. **Tone down the language.** Replace "superior" and "exceeds" with more precise descriptions (e.g., "competitive with", "on average the best-performing among compared methods"). The empirical evidence supports competitive performance, not dominance.

4. **Clarify the bootstrap procedure** (is ZNet retrained?) and report hyperparameter ranges and final values for the main experiments.

## Score and Decision

### Calibration Report

**Round 1 — Bracketing** (3 queries):
- Weak anchors (<3.5): jFox1iMWUa (3.40, causal neural networks), 4u0ruVk749 (3.00, diffusion model for ITE), 5AJ8R4z5g0 (3.25, hidden confounders). These papers have weaker theory and experiments than ZNet.
- Middle anchors (3.5–7.5): qDhq1icpO8 (6.75, CBRL.CIV — accepted, cleaner theory), F7XPZnIUHh (4.20, ADR — rejected, had theory errors), Oc4ji1iCjQ (6.75, ShadowCatcher — rejected, similar auto-generation of causal variables).
- Strong anchors (>7.5): 3cuJwmPxXj (8.00, identifiable representations), xByvdb3DCm (8.00, causal discovery), Nx4PMtJ1ER (8.00, causal discovery). These are stronger, more rigorous papers than ZNet.

**Round 1 bracket**: 4.5 – 6.0

**Round 2 — Narrowing** (2 queries):
- wFf9m4v7oC (5.75, CFDiVAE — accepted). Compares well; both learn latent causal variables from data with theory gaps. ZNet has broader experiments but a worse theory error. ZNet is slightly weaker.
- 0gqCIaBRQ9 (5.25, Regularized DeepIV — rejected). Different focus (pure IV convergence theory). Less relevant.
- x2rZGCbRRd (5.50, PoNet — rejected). Similar representation decomposition approach. ZNet is comparable in quality — both have interesting ideas but issues with theoretical justification.

**Final score**: 5.0. The paper has genuine empirical contributions (instrument recovery, comprehensive evaluation, ablation studies) and a well-designed architecture. However, the verifiable mathematical error in Lemma 1 undermines a key advertised contribution, and the missing uncertainty quantification makes it difficult to assess the significance of the ATE results. With major revision these issues are addressable.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>