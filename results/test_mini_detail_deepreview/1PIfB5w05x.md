Now I have a thorough understanding of the paper and can write the final consolidated review. Let me construct it, applying the filtering rules carefully.

---

## Summary

This paper studies sparse signal recovery when observations come from two sources with different noise variances (high-quality with small σ₁² and low-quality with larger σ₂²). For the information-theoretic threshold, the paper establishes sufficient conditions for support recovery in both an agnostic setting (decoder unaware of per-sample noise) and an informed setting (decoder knows the variances). These conditions define a *Price of Quality* γ — the number of low-quality samples needed to replace one high-quality sample — which is bounded below 2 in the agnostic setting but can diverge in the informed setting. For the algorithmic threshold, the paper extends the LASSO phase transition (Wainwright 2009) to the agnostic heterogeneous-noise setting, showing the sample-size threshold is independent of the individual noise levels and depends only on the total sample size, while the regularization condition depends only on the average noise level.

## Strengths

1. **First sufficient conditions for sparse recovery under heterogeneous noise.** Theorems 1 and 2 provide closed-form sample-size conditions (9) and (16) that explicitly depend on the two noise variances, enabling the first quantification of the trade-off between high- and low-quality data in sparse recovery. The conditions factorize across blocks in a way that yields a clean linear-trade-off interpretation.

2. **Extension of the LASSO phase transition to the agnostic heterogeneous-noise setting.** Theorem 3 gives both necessary (26) and sufficient (27) conditions for signed support recovery, with the threshold n_ALG = 2s log(p−s)+s+1 independent of σ₁², σ₂². The regularization condition (28) depends on the noise only through σ_avg². The proof handles the breakdown of Wishart structure via a QR decomposition and Haar-measure arguments — a nontrivial extension of Wainwright (2009).

3. **Demonstration of bounded vs. unbounded Price of Quality.** Equations (13)–(14) show γ < 2 in the agnostic setting across SNR regimes, while (19)–(21) show γ diverges in the informed setting (e.g., γ = Θ(log SNR₁ / SNR₂) in the low-SNR₂, high-SNR₁ regime). This provides concrete evidence for a qualitative difference between how the sufficient conditions behave in the two settings.

4. **Generalization beyond two data sources.** Remark 3.4 extends the sufficient conditions to general invertible noise matrices via (22) and (23), showing the core results are not limited to the two-source model.

5. **Honest and clear discussion of limitations.** Remark 3.2 transparently addresses the looseness of the sufficient conditions, the suboptimality of the agnostic estimator, and the potential for variance-aware procedures — a model of good scholarly practice.

## Weaknesses

### Fatal

None.

### Major

1. **The comparison between information-theoretic and algorithmic thresholds compares a non-tight sufficient condition to a sharp phase transition.** The paper repeatedly claims to "expose a fundamental difference" (abstract, conclusion) between how the two thresholds adapt to heterogeneity. However, the information-theoretic side is represented only by a *sufficient* condition (Theorem 1), while the algorithmic side (LASSO, Theorem 3) is fully characterized with both necessary and sufficient conditions. The paper acknowledges this asymmetry (Remark 3.2, conclusion), but the central narrative about a "fundamental difference" rests on comparing a relaxed upper bound to a sharp threshold. The true information-theoretic threshold could behave differently — the qualitative gap (bounded vs. unbounded γ) is suggestive but not conclusive. This is not fatal (the paper is transparent about the looseness), but the claims should be softened and the caveat should appear more prominently.

2. **The LASSO necessity result (Theorem 3(i)) is conditional on the regularization parameter satisfying a limit condition.** In the homogeneous-noise setting (Wainwright 2009), necessity holds for *any* sequence λ_p (subject to mild decay). Here, Theorem 3(i) requires that (n₁σ₁²+n₂σ₂²)/(λ_p² n²) has a limit in ℝ_{≥0} ∪ {+∞}, which excludes many possible λ_p sequences. The paper does not discuss whether the failure result can be extended to all λ_p, or whether choices outside this class could potentially succeed for n < n_ALG. The necessity is therefore weaker than the homogeneous analogue, and the presentation implies a sharper phase transition than is proven.

### Minor

1. **The Price of Quality is defined from sufficient conditions, not tight thresholds.** The paper is transparent about this (Remark 3.2), but the practical takeaway — "one high-quality sample is never worth more than two low-quality samples" (abstract, Section 3.1, conclusion) — is stated without qualification in several places where the context does not immediately signal "under our sufficient condition." The bound γ < 2 applies specifically to the relaxed Chernoff bound; the true information-theoretic trade-off could be different. Adding "under the sufficient condition" in more locations would sharpen the presentation.

2. **Possible typo in equation (12).** The expression for γ in (12) uses 2σ₁⁴ in the denominator of the first logarithm's argument, while the coefficient of n₁ in the sufficient condition (9) uses 2σ₂². Based on the derivation, (12) should have 2σ₂² (not 2σ₁⁴) in that position. The asymptotic expansion in (14) is consistent with the corrected version (yielding γ → 2 − σ₁²/σ₂²), so this appears to be a typo rather than a substantive error. The authors should correct it.

### Trivial

- The discussion of how an agnostic decoder would set λ_p without knowing σ_avg² (which requires knowledge of n₁, n₂, σ₁², σ₂²) is not fully addressed. This is a minor practical gap, not a theoretical flaw.

## Nice-to-Haves

- A small synthetic experiment illustrating the LASSO threshold's independence of σ₁², σ₂² would make the algorithmic result more accessible and convincing for an ML audience.
- A discussion of whether the necessary condition on λ_p in Theorem 3(i) can be removed or is inherent to the heterogeneous-noise structure would strengthen the paper.
- A brief comment on weighted LASSO in the agnostic setting would be helpful context.

## Removed Points

- **Criticism about proofs being in the appendix / not verifiable:** The appendix is stripped by the PDF parser; these proofs exist in the original submission. Not a valid weakness.
- **Criticism that the paper lacks experiments:** This is a pure theory paper; experiments are not standard or expected. The harsh critic's "optional but recommended" framing is noted but this is not a weakness.
- **"The connection between theoretical and algorithmic thresholds might not survive a tight analysis":** The second part of this is speculation, not an identified flaw. The paper already acknowledges the looseness. The actual issue (comparison of sufficient condition to sharp threshold) is kept in Major weakness 1.
- **Strength Finder strengths about "important problem" / generic claims:** Dropped as generic. Only concrete, evidence-backed strengths are kept.
- **"Missing discussion of weighted LASSO" and "role of δ in price of quality":** These are suggestions, not weaknesses. Moved to Nice-to-Haves.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the important tension that the paper's core comparative claim (IT vs. algorithmic thresholds adapting differently) is built on a sufficient condition for one side and a sharp threshold for the other — a point the paper acknowledges but does not fully address in its narrative framing. This is the most substantive insight from the review process.

## Suggestions

1. Soften the "fundamental difference" claim to reflect that the information-theoretic side rests on sufficient conditions; add a sentence explicitly stating that a tight information-theoretic threshold (e.g., via Fano's inequality) could change the picture.
2. Add a remark discussing the condition on λ_p in Theorem 3(i) — what classes of λ_p are excluded, and whether the necessity can plausibly be extended.
3. Correct the typo in equation (12) (σ₁⁴ → σ₂²) and verify the derivation in (14) is consistent with the corrected expression.
4. Add brief qualifying phrases ("under the sufficient condition") in the abstract and conclusion when stating the γ < 2 bound.

## Score and Decision

**Round 1 — Bracketing:** Initial calibration placed weak anchors around 3.0 (rejected, significant flaws), middle anchors around 5–7 (mixed accept/reject), and strong anchors above 7.5 (strong accept). The paper is clearly above 3.0 (it has no fatal flaws, is well-structured, and makes real contributions). Initial bracket: 5–7.

**Round 2 — Narrowing:** I examined four anchors in the 5–7 range. The Shuffled Regression paper (5.80, rejected) similarly studies phase transitions but was rejected due to methodological concerns — the current paper is cleaner and better motivated. The Active Binary Testing paper (5.25, rejected) is a theoretical paper rejected partly for limited novelty under strong assumptions — the current paper is more novel and has fewer contested assumptions. The Optimal Sketching paper (6.75, accepted) provides tight bounds with experiments — the current paper has somewhat looser IT results but comparable theoretical ambition and better writing. The Log-Concave Sampling paper (6.75, accepted) provides lower bounds in a pure theory setting — comparable in rigor and contribution level.

**Final score: 6.0.** The paper makes a solid, novel theoretical contribution and is well-executed. The two main weaknesses (comparing a sufficient condition to a sharp threshold, and the conditional LASSO necessity) are real but do not invalidate the contribution; they primarily affect the strength of the narrative claims. The paper is a clear accept at a venue like ICLR but would benefit from the suggested revisions.

**Decision: Accept**

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>