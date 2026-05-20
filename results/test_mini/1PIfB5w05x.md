Now I have a good basis for calibration. Let me write the final review.

---

## Summary

This paper studies sparse signal support recovery when observations come from two sources with different noise variances (mixed-quality data). It provides sufficient conditions for information-theoretic recovery in both the agnostic setting (decoder ignores per-sample noise) and the informed setting (decoder knows noise variances), introducing the "Price of Quality" — the number of low-quality samples needed to replace one high-quality sample under the sufficient condition. On the algorithmic side, it extends the LASSO phase transition (Wainwright, 2009) to the heterogeneous-noise agnostic setting, showing the threshold depends only on total sample size and average noise variance. The contrast between the settings — where the Price of Quality is bounded (≤2) in the agnostic case but can diverge in the informed case — is the paper's central conceptual contribution.

## Strengths

1. **First sufficient conditions for sparse recovery with mixed-quality data.** Theorems 1 and 2 provide explicit sample-size sufficient conditions in both agnostic and informed settings (equations 9, 16). The "Price of Quality" γ (equations 12, 18) gives a quantitative trade-off between high- and low-quality data, with concrete expressions in each SNR regime. The paper is candid about which results are sufficient conditions vs. sharp thresholds (Remark 3.2, Remark 3.3, Conclusion).

2. **Clean extension of the LASSO phase transition to heterogeneous noise (Theorem 3).** The result that the algorithmic threshold depends only on total sample size n and average noise variance σ²_avg (equation 6), not on the individual σ₁², σ₂², is a non-trivial generalization of Wainwright (2009). Handling the non-diagonal covariance Σ via QR decomposition and Haar measure (proof sketch, Section 4) is a genuine technical contribution. Proposition 4.1 further provides a necessary and sufficient condition on noise scaling for the existence of a suitable λ_p.

3. **Clear contrast between information-theoretic and algorithmic thresholds.** The paper systematically exposes a difference that is both conceptually interesting and practically relevant: the information-theoretic sufficient condition is sensitive to data quality (large γ in the informed setting), while the LASSO threshold is robust and depends only on average noise. This contrast is backed by the separate analyses in Sections 3 and 4 and is discussed in the conclusion (Section 5).

4. **Honest treatment of limitations.** Remark 3.2 candidly discusses that the agnostic information-theoretic condition (9) is not expected to be sharp, that it arises from a relaxation of the Chernoff bound, and that alternative estimators (e.g., reweighting by Yᵢ²) could potentially do better. This transparency helps readers calibrate their trust in the claims.

## Weaknesses

### Fatal
None.

### Major

1. **The agnostic "information-theoretic" result is a sufficient condition for a specific estimator, not a fundamental limit.** Theorem 1 analyzes the least-squares minimizer over exactly s-sparse binary vectors (8), which is the MLE under a *homoscedastic* model. A decoder who is agnostic to noise variances could use other procedures (Remark 3.2 mentions reweighting by observed labels). Consequently, the sufficient condition (9) and the derived Price of Quality ≤ 2 reflect a particular algorithm's performance, not a fundamental information-theoretic limit of the problem. The paper acknowledges this (Remark 3.2), and the abstract is careful ("sufficient conditions for information-theoretic... recovery"), but the framing in Section 1.2.1 ("Sampling complexity of sparse recovery") and occasional use of "information-theoretic" side could create a misleading impression. The contrast with the informed setting (Theorem 2, which analyzes the proper MLE) is therefore somewhat asymmetric: Theorem 2 uses the correct MLE (15), while Theorem 1 uses a misspecified estimator. This tempers the clean "agnostic vs. informed" contrast that the paper advertises as a key contribution.

### Minor

2. **The Price of Quality ≤ 2 in the agnostic setting relies on a relaxed Chernoff bound whose impact is not quantified.** The derivation of (9) involves a relaxation of the exact Chernoff exponent (which yields a cubic equation, referenced as (37)). The closed-form condition (9) is a looser sufficient condition than the exact one. Since the Price of Quality γ ≤ 2 is computed from this relaxed condition, it is not clear whether it reflects the actual trade-off even for the specific estimator (8). The paper acknowledges the relaxation (Remark 3.2) but does not bound the gap between the relaxed and exact price. In the homogeneous-noise case, the analogous optimization recovers the sharp threshold; the authors state they "expect" the same here, but this intuition is not developed. This is the paper's own modeling choice, so it is a structural limitation of the agnostic analysis rather than a gap the authors can defer to future work.

3. **No experimental validation.** The paper is purely theoretical, which is acceptable, but even a simple synthetic simulation (varying n₁, n₂, σ₁², σ₂² and showing the LASSO phase transition or the sufficiency conditions) would substantially strengthen the paper's impact. For a conference like ICLR that values empirical validation alongside theory, the absence of any numerical illustration is a missed opportunity to make the results more concrete and convincing.

### Trivial
None.

## Nice-to-Haves

- A simple simulation confirming the LASSO phase transition (Theorem 3) and the sufficient conditions (Theorems 1–2) for a few parameter settings.
- A discussion or bound quantifying the gap between the relaxed Chernoff condition (9) and the exact cubic equation (37), at least in specific SNR regimes.
- Clarification in the abstract or introduction that the agnostic information-theoretic result is a sufficient condition for a *natural least-squares estimator*, rather than necessarily the fundamental information-theoretic limit.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh Critic's Critical Issue 3 (LASSO necessity / degenerate λ_p regime):** The critic speculates about a degenerate λ_p regime without being able to verify the appendix proof (which is stripped by the parser). The theorem statement's condition on λ_p is well-specified, and the critic acknowledges it is a minor concern. Removed because it relies on speculation about stripped content.

- **Harsh Critic's section-by-section notes on missing related works, notation reuse, scope comments:** Most are observations rather than actionable weaknesses. The notation reuse point (n^* appearing in two theorems) is a presentation style choice that does not affect correctness.

- **Strength Finder's generic strengths about "addressing an important problem" and "clear motivation":** These are generic and lack specific concrete content; moved here per the filtering rules.

## Novel Insights

The harsh critic raises a valid meta-point that neither the Strength Finder nor the original paper fully addresses: the agnostic information-theoretic analysis (Theorem 1) and the informed analysis (Theorem 2) are not just analyzing different *settings* but also different *estimators* with different optimality properties. Theorem 2 analyzes the proper MLE (which is the optimal procedure under the model), while Theorem 1 analyzes an estimator that is optimal only under a misspecified (homoscedastic) model. This asymmetry means the "Price of Quality" values across settings are not directly comparable as measures of fundamental problem difficulty — they partially reflect the estimators' differing quality. The paper touches on this in Remark 3.2 but does not fully own the implication: a truly agnostic decoder who tries to estimate variances from data (e.g., via the Yᵢ² reweighting mentioned in Remark 3.2) might achieve a Price of Quality between the agnostic bound of ≤2 and the informed bound that can diverge. The paper's central contrast (agnostic ≤2 vs. informed →∞) is therefore better understood as a contrast between two *estimator-agnostic-setting pairs* rather than between two *problem settings* alone. This does not invalidate the results but refines how they should be interpreted.

## Suggestions

1. Add a short discussion clarifying that Theorem 1 gives a sufficient condition for a specific estimator (the homoscedastic MLE), and that the "information-theoretic" framing should be read as "for a natural estimator that does not use variance information." A small amendment could be: replace "information-theoretic" with "sufficient condition for a least-squares estimator" in the abstract's first reference to the agnostic result.

2. Quantify the gap between the relaxed condition (9) and the exact Chernoff condition. Even a crude bound showing that the Price of Quality ≤ 2 is robust to the relaxation (or, conversely, could be larger under exact optimization) would significantly strengthen the agnostic analysis.

3. Add a small synthetic experiment. A single figure with two panels (one for the LASSO phase transition, one for the MLE sufficient condition) would greatly increase the paper's accessibility and impact without requiring significant additional work.

## Score and Decision

### Calibration

**Round 1 — Bracketing:**
- Weak anchors (avg < 3.5): Found papers scoring 2.67–3.33 on topics like generalization bounds, mean-field models, quantization. These are significantly weaker (less novel, less rigorous, or with flawed central claims) than the paper under review.
- Middle anchors (3.5–7.5): Found papers scoring 5.00–7.00. Key comparisons:
  - *"Column Thresholding: Bridging the Computational-Statistical Gap in the Sparse Spiked Wigner Model"* (5.00, rejected): Similar sparse-recovery theme but rejected due to overclaimed framing. The current paper's framing is more honest, and its theoretical contribution is cleaner.
  - *"A Recovery Guarantee for Sparse Neural Networks"* (6.40, accepted poster): The most directly comparable anchor — both give theoretical sparse recovery guarantees. The neural networks paper has experiments validating its theory, which the current paper lacks. The current paper's theory is more standard (extending known thresholds to heterogeneous noise), but its clean conceptual framework (Price of Quality) is a nice addition.
  - *"Closed-form ℓ_r norm scaling"* (6.00, accepted poster): Theory-heavy contribution with experiments. Similar quality tier — both extend known theory to new settings.
- Strong anchors (avg > 7.5): Found papers scoring 8.00 on topics like quantum neural networks, kernel methods, multi-turn LLM evaluation. These are not in the sparse-recovery space and are qualitatively different contributions.

**Round 1 bracket: 5.0–6.5.**

**Round 2 — Narrowing (5.0–7.0):**
- *"Breaking the Total Variance Barrier: Sharp Sample Complexity for Linear Heteroscedastic Bandits"* (6.67, accepted poster): Similar in dealing with heteroscedastic noise theoretically. Has tighter theory (matching lower bounds) but also lacks experiments. Slightly stronger than the current paper because of the lower bounds.
- *"On Coreset for LASSO Regression Problem with Sensitivity Sampling"* (6.00, accepted poster): LASSO theory paper with experiments. Similar quality tier.
- The reviewed paper sits above the 5.00 rejected paper (Column Thresholding — overclaimed framing) and the 5.50 paper (Fast Escape — narrower scope). It is comparable to the 6.00–6.40 accepted posters in its space. It is slightly below the 6.67 paper (heteroscedastic bandits) because that paper has matching lower bounds and a tighter theoretical contribution.

**Final score: 6.0**. The paper makes a solid, clean theoretical contribution. It extends well-known sparse recovery results to the natural and practically motivated heterogeneous-noise setting, introduces the useful Price of Quality concept, and honestly discusses its limitations. The main weaknesses are that the agnostic information-theoretic result is a sufficient condition for a specific estimator (not a fundamental limit), and the lack of any empirical validation. These are genuine but not fatal.

### Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>