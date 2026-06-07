## Summary

This paper studies sparse support recovery when observations come from two sources with different noise levels (mixed-quality data). It provides: (i) information-theoretic sufficient conditions for recovery in agnostic and informed settings, defining a "Price of Quality" γ — the number of low-quality samples needed to replace one high-quality sample; and (ii) a LASSO phase transition in the agnostic setting showing the algorithmic threshold depends only on total sample size and average noise. The contrast reveals that the information-theoretic sufficient condition's exchange rate between high- and low-quality data is bounded (γ ≤ 2), while the LASSO threshold is entirely blind to the quality split.

## Strengths

1. **Price of Quality formalization with interpretable asymptotic regimes (Section 3.1–3.2, eqs 12–14, 18–21):** The paper defines γ as a closed-form function of σ₁², σ₂², s, and δ, then derives its behavior in three SNR regimes. The finding that γ ≤ 2 in the agnostic setting (eq. 14) and can become arbitrarily large in the informed setting (eq. 20: γ → +∞) is concrete, non-obvious, and practically interpretable — prior homogeneous-noise work could not speak to this trade-off.

2. **LASSO threshold depends only on total sample size and average noise (Theorem 3, Section 4, eqs 26–28):** The paper proves that n_ALG = 2s log(p−s) + s + 1 is independent of σ₁² and σ₂², and the regularization condition (28) involves noise only through σ_avg² = (n₁σ₁² + n₂σ₂²)/n. The proof overcomes the failure of the classical Wishart argument (caused by Σ not being a scalar multiple of the identity) via QR decomposition and Haar measure arguments — a genuine technical advance over Wainwright (2009). The result includes both necessary and sufficient conditions, making it a sharp phase transition.

3. **Systematic contrast between info-theoretic and algorithmic behavior (Section 5, paragraphs 2–3):** The paper synthesizes its two sets of results to show that the info-theoretic sufficient condition's Price of Quality depends on the noise quality split, while the LASSO threshold is entirely blind to it. This goes beyond reporting two separate results and places the findings in the broader context of robustness of algorithmic thresholds (citing Wang et al., Omidiran & Wainwright).

4. **Explicit diagnosis of technical obstacles from heterogeneity (Remark 4.2, Section 4 proof sketch):** The paper identifies precisely why extending LASSO to the informed setting is nontrivial (the presence of Σ⁻¹ in the rescaled loss destroys the Wishart structure X_SᵀX_S ∼ 𝒲(I_s, n) needed for classical inverse-Wishart moment bounds) and explains how the QR+Haar argument circumvents the isotropic Gaussian failure in the agnostic case. This level of technical specificity is a strength.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Equation (12) contains an internal inconsistency.** The Price of Quality γ in (12) has $2\sigma_1^4$ in the denominator of the numerator's log argument:  
   $$\gamma := \frac{\log(1 + \delta(2\sigma_2^2 - \sigma_1^2)s/(2\sigma_1^4))}{\log(1 + \delta s/(2\sigma_2^2))},$$  
   while the sufficient condition (9) from which γ is derived has $2\sigma_2^2$ in the corresponding position:  
   $$n_1 \log\left(1 + \frac{\delta(2\sigma_2^2 - \sigma_1^2)s}{2\sigma_2^2}\right).$$  
   The asymptotic expansion (14) is consistent with the $2\sigma_2^2$ version (yielding $2 - \sigma_1^2/\sigma_2^2$) but inconsistent with the $2\sigma_1^4$ version as written (which would give $(2\sigma_2^2 - \sigma_1^2)\sigma_2^2/\sigma_1^4$). The surrounding discussion clearly points to the intended expression with $2\sigma_2^2$, so this is a typo in a central displayed equation that should be corrected.

2. **The "fundamental difference" framing overreaches (abstract, Section 5).** The abstract's final sentence claims the results "expose a fundamental difference between how the information-theoretic and algorithmic thresholds adapt to changes in data quality." However, the agnostic information-theoretic Price of Quality (γ ≤ 2) is derived from Theorem 1, which the paper acknowledges "is not expected to be information-theoretically sharp" (Remark 3.2) and is a sufficient condition, not a threshold. The γ ≤ 2 bound may be an artifact of the Chernoff relaxation. While the paper does include the qualifier "under our sufficient condition" in the body and conclusion, the abstract and the framing in Section 5 (paragraphs 2–3) use "information-theoretic threshold" language that could give readers the impression that a proven separation between two sharp thresholds has been established. What is actually established is a separation between a sufficient condition and a sharp phase transition.

3. **The generalized sufficient condition (22) does not obviously specialize to (9).** Remark 3.4 states that (9) "extends to" (22) for general invertible Σ, but specializing (22) to the two-block-diagonal case yields a high-quality coefficient:
   $$\log\left(1 + \frac{\delta(2\sigma_2^2 - \sigma_1^2)s}{2\sigma_2^4}\right),$$
   which has $\sigma_2^4$ in the denominator, while (9) has $\sigma_2^2$. These differ by a factor of $\sigma_2^2$. The paper does not discuss this discrepancy or explain whether (22) is intended as a looser bound valid for arbitrary Σ while (9) is a tighter bound specific to the two-block-diagonal case.

### Trivial
None.

## Nice-to-Haves
- The paper could sharpen Theorem 1 by attempting to solve the cubic equation (37) mentioned in Remark 3.2, at least asymptotically, to see whether the tightened sufficient condition pushes γ closer to 1. This would either strengthen or qualify the "fundamental difference" claim.
- The informed algorithmic setting (Remark 4.2) could include a brief discussion of what one might expect the Price of Quality to be there, even if rigorous proof is deferred.

## Removed Points
- **Criticism about missing simulations:** Removed — the paper is a pure theory paper; simulations are not required and the reviewer acknowledged this.
- **Criticism about SNR₁/SNR₂ notation being ambiguous:** Removed — trivial notation/formulation nitpick that does not affect the paper's substance.
- **Criticism about insufficient caveat on γ:** Removed — the paper already qualifies the ≤2 claim with "under our sufficient condition" in the abstract, body, and conclusion.
- **Strength Finder's claim about generalization to arbitrary noise (Strength 4):** Moved with caution — the discrepancy between (22) and (9) identified in Weakness 3 undermines this claimed strength; the intent is clear but the inconsistency needs resolution.
- **Strength Finder's generic strengths about "important problem," "interesting question" etc.:** Removed as generic/superficial and lacking specific evidence.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. Fix the inconsistency in equation (12) — the denominator $2\sigma_1^4$ should be $2\sigma_2^2$ to match (9) and to make the asymptotic expansion (14) follow correctly.
2. In the abstract and Section 5, replace "information-theoretic threshold" with "information-theoretic sufficient condition" (or add an explicit qualifier) when discussing the agnostic Price of Quality, to avoid misleading readers into thinking the γ ≤ 2 bound is a proven information-theoretic limit rather than a property of a relaxed sufficient condition.
3. Clarify the relationship between (9) and (22) in Remark 3.4: state explicitly whether (22) is a looser bound applicable to general Σ while (9) is a tighter bound for the two-block-diagonal case, and explain the origin of the $\sigma_{\max}^4$ term.

## Score and Decision

**Calibration anchors used:**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/vQIVbfTMzf.md` | 3.25 | R1 (bracket <3.5) | Much weaker — had serious rigor and presentation issues |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/Zap3nZhRIQ.md` | 3.00 | R1 (bracket <3.5) | Much weaker — tangential topic with serious flaws |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/2NwHLAffZZ.md` | 2.33 | R1 (bracket <3.5) | Much weaker |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/ZDoaLbOFaP.md` | 3.00 | R1 (bracket <3.5) | Much weaker |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/Piod76RSrx.md` | 5.50 | R1 (bracket 3.5–7.5) | Weaker — generalization bounds with limited novelty |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/qZwtPEw2qN.md` | 6.80 | R1 (bracket 3.5–7.5) | Stronger — had extensive experiments alongside theory, accepted |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/sJAlw561AH.md` | 5.50 | R1 (bracket 3.5–7.5) | Weaker — mixed reviews, rejected |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/qcigbR1UYA.md` | 5.25 | R1 (bracket 3.5–7.5) | Weaker — strong assumption limits applicability, rejected |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/fMTPkDEhLQ.md` | 8.00 | R1 (bracket >7.5) | Stronger — tight lower bounds with deep technical analysis |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/5t57omGVMw.md` | 8.00 | R1 (bracket >7.5) | Stronger — different topic, stronger technical contribution |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/P7KIGdgW8S.md` | 8.00 | R1 (bracket >7.5) | Stronger — different topic |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/A3YUPeJTNR.md` | 8.00 | R1 (bracket >7.5) | Stronger — different topic |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/sIcPMMhl9W.md` | 5.80 | R2 (bracket 4.5–6.5) | Weaker — used non-rigorous approximations, rejected |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/gVVoZtiQlt.md` | 5.00 | R2 (bracket 4.5–6.5) | Weaker — same paper variant, rejected |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/f3jySJpEFT.md` | 6.33 | R2 (bracket 4.5–6.5) | Comparable — accepted, similar rigor but weaker framing, some practical concerns |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/uf5EAGmkrN.md` | 5.50 | R2 (bracket 4.5–6.5) | Weaker — rejected, less rigorous |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/GWSIo2MzuH.md` | 6.50 | R2 (bracket 6.0–8.0) | Slightly stronger — accepted, more extensive analysis but also notable technical concerns |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/0oWGVvC6oq.md` | 6.50 | R2 (bracket 6.0–8.0) | Comparable — accepted, different topic |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/eoTCKKOgIs.md` | 6.25 | R2 (bracket 6.0–8.0) | Comparable — accepted, strong theoretical claim but mixed confidence |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/Zh2iqiOtMt.md` | 6.50 | R2 (bracket 6.0–8.0) | Comparable — accepted, different topic |

**Round 1 bracket:** [5.5, 7.0] — the paper is clearly stronger than the 3.0–3.25 and 5.0–5.8 anchors (rejected with serious issues) and weaker than the 8.0 anchors.

**Round 2 narrowing:** Compared to the 6.33 Lasso Bandit paper (accepted), the current paper has comparable rigor and arguably cleaner results. Compared to the 6.50 anchors (accepted), it is slightly less expansive but has fewer technical concerns. The typo in (12) and the framing overreach are genuine weaknesses that prevent a higher score.

**Final score: 6.0** — The paper makes a genuine contribution with clean theoretical results and a nontrivial technical advance (Theorem 3 proof via QR+Haar). The weaknesses are real but bounded (a fixable typo, a framing issue, and a minor discrepancy in a generalization remark). The paper merits acceptance but would benefit from the corrections suggested above.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>