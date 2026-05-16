Now I have all the evidence I need. Let me compose the consolidated review.

## Summary

This paper studies off-policy learning (OPL) in contextual bandits where the target reward is only partially observed (due to missingness, delay, censoring) but secondary rewards (clicks, dwell time, etc.) are fully observed. The authors formalize this setting and propose HyPeR (Hybrid Policy Optimization for Partially-Observed Reward), a policy gradient estimator that combines the partially-observed target reward with densely observed secondary rewards using a control-variate structure. They prove unbiasedness, derive a variance reduction condition, and introduce a strategic weight-tuning procedure that intentionally uses a different mixture weight to improve the bias-variance trade-off. Experiments on synthetic data and the KuaiRec dataset show consistent improvements over baselines.

## Strengths

1. **Novel and well-motivated problem formulation.** The paper formally defines the OPL setting with partially-observed target rewards and fully observed secondary rewards (Section 3), covering missing data, delayed rewards, censoring, and data fusion as special cases. Table 1 provides concrete real-world examples. This is a genuine generalization that captures practical scenarios existing methods do not jointly address.

2. **Principled estimator with theoretical guarantees.** The HyPeR estimator (Eq. 10-11) is proven unbiased (Theorem 1) and shown to reduce variance relative to r-DR when the secondary-conditional q-function q̂(x,a,s) estimates the reward better than q̂(x,a) alone (Theorem 2). The combination of a control-variate term (using secondary rewards to reduce variance) with an IPW term (using partially observed target rewards to maintain unbiasedness) is a clean, theoretically sound design.

3. **Strategic weight-tuning innovation.** Section 4.1 introduces the counterintuitive idea of intentionally using γ ≠ β (deviating from the true objective weight) to improve finite-sample performance, supported by a bootstrap-based tuning procedure (Eq. 14). The empirical results (Figures 4-5) consistently show that HyPeR(Tuned) outperforms HyPeR(γ=β) and all baselines, especially under challenging conditions (low observation probability, small data). This is a practically useful contribution beyond the core estimator.

4. **Consistent empirical gains across synthetic and real-world data.** Figures 1-5 show HyPeR variants achieving the highest combined policy value across varying observation probabilities, data sizes, correlation levels (λ), and weights (β). The gains are shown in both target policy value and combined policy value, and they hold on the KuaiRec dataset where the ground-truth reward matrix is fully observed. The advantage is most pronounced precisely in the high-variance regimes where the method is designed to help.

## Weaknesses

### Fatal
None.

### Major
1. **The KuaiRec experiment constructs secondary rewards that partially derive from the target reward, and s-IPS/s-DR baselines are weakened by using only one dimension.** Two of the four secondary rewards (s₁, s₂) are deterministic binary thresholds of the target watch-ratio r. While binary thresholds lose significant information (and the paper empirically shows the overall correlation is slight), these dimensions are not "genuinely separate signals" like clicks predicting ratings — they are derived from r. Meanwhile, s-IPS and s-DR in this experiment use *only* s₁ (a single binary threshold: "1 if r ≥ 2.0, else 0") for their aggregation function F(s), ignoring the other three dimensions including s₃ (upload recency) and s₄ (video length) which are genuinely independent. This simultaneously gives the baselines an unnecessarily weak proxy and tests HyPeR on a setting where secondary rewards have an informational advantage (they contain information derived from the target). An experiment where secondary rewards are genuinely separate signals (e.g., clicks as secondary for a rating target) and where s-IPS uses a learned or multi-dimensional aggregation would provide stronger evidence for the method's real-world applicability.

### Minor
2. **The synthetic experiment's s-IPS/s-DR baselines use a noisy oracle rather than a learned aggregation.** In the synthetic setup, the aggregation F(s) is set to s̄ᵀ(θ_f + ε_F) where θ_f is the true weight from the data-generating process and ε_F ~ N(0, 0.4²). This is a reasonable approach to simulate not knowing the exact aggregation (the noise term is conservative), but it is somewhat generous to s-IPS/s-DR (they get the true weight plus noise rather than having to learn an aggregation from scratch). Conversely, HyPeR learns q̂(x,a,s) via regression. The comparison would be cleaner if s-IPS/s-DR also learned their aggregation from the portion of data where target rewards are observed, or if the paper included an ablation where the noise level σ_F is varied. This does not invalidate the results — HyPeR's advantage is consistent and large — but it makes it harder to attribute how much of the gain comes from the control-variate structure vs. simply using a better-learned regression model.

3. **The variance reduction condition in Theorem 2 is stated but its limitations are not discussed.** The theorem shows that HyPeR(γ=0) has lower variance than r-DR when q̂(x,a,s) estimates q(x,a,s) better than q̂(x,a) estimates q(x,a). This condition is intuitive but not verifiable from logged data (we never observe q(x,a,s)), and adding s increases the dimensionality of the regression problem, so q̂(x,a,s) could in principle be worse with limited data. The paper should explicitly acknowledge this and discuss practical diagnostics or failure cases. (The experiments do show consistent gains, so the concern is theoretical rather than empirical, but it is worth flagging.)

4. **The missing-at-random assumption is not explicitly stated or discussed.** The paper models the observation indicator as p(o|x), which implicitly assumes o is conditionally independent of a and r given x (i.e., missing at random). In many real scenarios — delayed conversions that correlate with action quality, or users reporting extreme ratings more often — o may depend on a or r, which would bias the r-IPS/r-DR correction and, by extension, HyPeR's target-reward term. Discussing this limitation and potential extensions (e.g., modeling p(o|x,a)) would strengthen the paper.

### Trivial
5. The paper does not report the number of bootstrap samples used for the γ-tuning procedure (Section 4.1), which is relevant for reproducibility.
6. The variance expression in Theorem 2 is written for a scalar g_θ (i.e., a single parameter). The paper should clarify that it applies element-wise or provide the matrix extension.

## Nice-to-Haves
- An experiment where secondary rewards are genuinely separate signals (e.g., Criteo with clicks → conversions, or MovieLens with implicit feedback → ratings) would directly test the core motivation.
- A comparison with a simple imputation-based baseline (impute missing target rewards via regression on secondary rewards, then apply standard DR) would clarify whether HyPeR's control-variate structure adds value beyond a two-step approach.
- The paper could discuss how errors in estimating p̂(o|x) affect HyPeR vs. r-DR differently.
- Adding a synthetic experiment where q̂(x,a,s) is intentionally misspecified (e.g., linear when the truth is non-linear) would test robustness.

## Removed Points

These points are flagged to be removed by the meta-reviewer instructions; treat them with caution.

- *"The aggregation noise is added to coefficients rather than predictions, over-penalizing s-IPS."* — This is a minor implementation choice; adding noise to coefficients is equivalent to adding noise to predictions scaled by s̄. The distinction does not change the qualitative result.
- *"Section 4 estimator lacks intuition."* — This is a presentation style nitpick; the estimator structure (control variate + doubly robust correction) is clearly derived and the paper explains the logic of each term.
- *"The logging policy is synthesized, not from the system."* — The critic acknowledges this is standard in OPL research. Not a weakness.
- *"The paper lacks a limitations section."* — The limitations are partially addressed via the theoretical conditions and experimental setup; a dedicated section would be nice but its absence is not a flaw in the claims.

## Novel Insights

The most interesting insight from the reviews is the observation that the KuaiRec experiment simultaneously weakens the baselines (s-IPS uses only one binary threshold dimension) while giving HyPeR an advantageous setup (secondary rewards contain information derived from the target), making the magnitude of HyPeR's improvement harder to interpret than the raw numbers suggest. Combined with the synthetic baseline concern (noisy oracle for s-IPS), there is a pattern where the evaluation stack is tilted in HyPeR's favor — not enough to doubt the method works, but enough to question *how much better* it is than a fairer version of the existing approaches. A cleaner evaluation design would substantially strengthen the paper's empirical claims.

## Suggestions

1. **Augment the KuaiRec experiment:** Use all four secondary reward dimensions for the s-IPS/s-DR aggregation (e.g., a learned linear combination or simple average) so the baselines are not artificially limited to a single binary threshold.
2. **Add a synthetic ablation with aggregated baseline:** Include a version of s-IPS/s-DR that learns its aggregation function F(s) from the observed target rewards via regression, and vary the noise level σ_F systematically to show the comparison is robust.
3. **Explicitly state the missing-at-random assumption** and discuss how violations would affect each estimator differently.
4. **Report the bootstrap sample count** used in the γ-tuning procedure.

## Score and Decision

The paper proposes a well-motivated, theoretically grounded method for a practical OPL problem. The HyPeR estimator is novel, the strategic weight-tuning is a nice addition, and the empirical results show consistent improvement. The main weaknesses are in the experimental design — the baselines in both synthetic and real experiments are not set up as strongly as they could be, and the KuaiRec secondary rewards partially overlap with the target. These issues are real but do not invalidate the core contribution; they reduce the strength of the empirical evidence rather than undermine the method itself. With reasonable revisions to the evaluation, this could be a strong paper.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>