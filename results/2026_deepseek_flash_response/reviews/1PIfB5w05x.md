Now I have sufficient calibration data. Let me write the final review.

## Summary
This paper studies sparse signal support recovery when observations come from two sources with different noise variances (σ₁² < σ₂²). It derives sufficient conditions for information-theoretic recovery in both agnostic and informed settings, defining a "Price of Quality" γ that quantifies how many low-quality samples replace one high-quality sample. Key findings: (1) in the agnostic setting γ < 2 under the sufficient condition; (2) in the informed setting γ can diverge; (3) the LASSO phase transition for heterogeneous noise depends only on total n and average noise variance, showing algorithmic robustness to data heterogeneity.

## Strengths
- **Price of Quality as an interpretable metric.** The paper derives closed-form expressions for γ (equations 12, 18) from the sufficient conditions, giving a concrete, interpretable number for the high/low-quality trade-off. The finding that γ < 2 in the agnostic setting but can diverge in the informed setting (equations 14, 20) is a non-trivial quantitative result that goes beyond any prior homogeneous-noise analysis.
- **New technical machinery for the LASSO with heterogeneous noise.** Theorem 3 extends Wainwright (2009)'s LASSO phase transition to heterogeneous noise when Σ is no longer a scalar multiple of identity. The QR/Haar-measure technique (lines 304–308) to handle the loss of Wishart structure is a genuine methodological contribution, and showing the threshold depends only on σ_avg² is a clean result.
- **Systematic regime analysis.** The paper analyzes γ across three distinct SNR regimes (high SNR, low-SNR₂/high-SNR₁, low SNR) for both agnostic and informed settings, yielding a nuanced picture that would be invisible from a single-regime analysis.
- **Generalization to arbitrary noise covariance.** Remark 3.4 extends the sufficient conditions to any non-singular Σ (equations 22–23), showing the analysis is not tailored to the specific two-quality-levels model.

## Weaknesses

### Major
- **Algebraic inconsistency in a central equation.** Equation (9) (Theorem 1) gives the coefficient of n₁ as log(1 + δ(2σ₂² − σ₁²)s/(2σ₂²)). However, equation (12) defines γ with 2σ₁⁴ in the denominator instead of 2σ₂². Equation (14) carries the same σ₁⁴, but its simplification to γ ≈ 2 − σ₁²/σ₂² is algebraically correct only if the denominator were 2σ₂² (the form from (9)). This means (12) and (14) contain a typesetting error (σ₁⁴ → 2σ₂²) in the paper's signature claim. While the mathematical content is preserved through the correct expression in (9), a reader cannot verify the central quantitative claim from (12) alone, and the headline result "one high-quality sample is never worth more than two low-quality samples" depends on the algebra going through with the correct form. This must be corrected.

- **The "sharpness" claim for the informed threshold overreaches.** The conclusion (line 340) states "the informed information-theoretic threshold... [is] sharp." However, Theorem 2 only provides a sufficient condition; Remark 3.3 acknowledges that "establishing full necessity in the heterogeneous setting remains an interesting direction for future work." The "sharp convergence rate" (line 225) refers to the exponential decay rate of the error probability, not the sharpness of the threshold itself. Calling the threshold "sharp" conflates these two distinct notions and overstates what is proven.

- **Price of Quality is a property of a sufficient condition, not an information-theoretic invariant.** The paper is transparent about this in Remark 3.2 and the qualifying phrase "for this sufficient condition to hold" appears throughout the text. However, the title "PRICE OF QUALITY" and the abstract's prominent framing — "one high-quality sample is never worth more than two low-quality samples" — do not carry this qualification prominently enough. A casual reader will interpret γ as a fundamental bound on the value of data quality, when in fact it is derived from a relaxed sufficient condition for a specific estimator (the homoscedastic MLE applied to heterogeneous data). The true information-theoretic Price of Quality could be different; the paper simply does not establish this.

### Minor
- **Theorem 3 requires n₁, n₂ = ω(s), which may not hold in the motivating scenario.** The practical setup motivating the paper (a few high-quality samples, many low-quality ones) could have n₁ as small as O(1). The requirement that both sample sizes grow faster than sparsity excludes this regime, but the paper does not discuss this limitation.
- **The assumption n₂ > n₁ is stated (line 45) but never used in any theorem.** It is simply a modeling assumption in the problem setup. The theorems require only n₁, n₂ = ω(s) (for the LASSO result) or do not impose ordering on n₁ and n₂. The paper could either drop this assumption or explain its role.
- **Conclusion overclaims for the LASSO threshold by omitting the comparison baseline.** The paper presents the LASSO threshold's independence from individual noise levels as "striking," but a brief comparison with what an optimal weighted estimator would achieve would sharpen the "robustness" claim.

### Trivial
- None beyond the typographical issue noted above (which is major because it affects a central equation, not because it is a formatting problem).

## Nice-to-Haves
- **Empirical illustration would strengthen the paper.** While the paper is purely theoretical, even a simple synthetic-data simulation showing recovery probability as a function of (n₁, n₂) with the theoretical boundary overlaid would make the sufficient conditions more tangible and verify they are not vacuously loose. This is not required for a theory paper but would substantially improve persuasiveness.
- **A direct comparison of the agnostic and informed thresholds** in a table or figure for the same (n₁, n₂, σ₁², σ₂²) would help readers understand the quantitative gap between the two settings.
- **A discussion of what happens when n₁ = O(s)** (violating the ω(s) condition for the LASSO result) would clarify the practical scope of Theorem 3.

## Removed Points
These points were raised by reviewers or the strength finder but are removed after cross-checking:
1. *Criticism that the Price of Quality is not information-theoretic / the paper does not qualify it.* **Removed** — the paper consistently qualifies γ with "for the sufficient condition to hold" (lines 77–78, 81, 191, 195). The framing concern is valid but is already a documented weakness above in a softened form.
2. *Claim that the LASSO result is "conceptually unsurprising" / the paper overstates surprise.* **Removed** — this is a subjective opinion, not a factual error. The paper acknowledges the technical challenge (QR/Haar argument) and the result is non-obvious enough to warrant explicit derivation.
3. *Criticism about missing related works.* **Removed** per instruction — cannot confirm without external sources.
4. *Criticism about the n_INF threshold and exact vs almost-full recovery.* **Removed** — the critic acknowledges this is handled correctly; it is not a weakness.
5. *Strength Finder's generic strengths (e.g., "the problem is important").* **Removed** — too generic to be useful.
6. *The "Section-by-Section Notes" about equation (2) and SNR regime derivations.* **Removed** — these are clarifications and confirmations, not weaknesses.

## Novel Insights
None beyond the paper's own contributions. The reviews surface the algebraic inconsistency but do not identify structural issues the paper itself does not discuss.

## Suggestions
1. **Fix the algebraic typo in equations (12) and (14).** Replace 2σ₁⁴ with 2σ₂² in both equations to match the form from (9). Verify all derived regime results (13–14) are consistent with the corrected expression.
2. **Qualify "sharp" when describing the informed threshold.** Replace "the informed information-theoretic threshold ... is sharp" (line 340) with language that distinguishes "sharp convergence rate" from "sharp threshold," or acknowledge that necessity remains open.
3. **Add a short empirical section** with a synthetic-data experiment validating that the sufficient conditions are not vacuously loose.
4. **Discuss the n₁ = ω(s) requirement** and its implications for the motivating scenario where n₁ may be small.
5. **Either use the assumption n₂ > n₁ in a theorem or remove it** from the problem setup to avoid misleading readers.

## Score and Decision

### Calibration Procedure

**Round 1 (Bracketing):** Three queries targeting weak (< 3.5), middle (3.5–7.5), and strong (> 7.5) score bands on topics related to sparse recovery theory and LASSO phase transitions.

**Round 1 anchors (partial list):**
- `2NwHLAffZZ.md` (2.33, Reject) — Weak paper on gradient-based learning; far below our paper.
- `ZDoaLbOFaP.md` (3.00, Reject) — Sparse covariance neural networks; below our paper.
- `Zap3nZhRIQ.md` (3.00, Reject) — Non-differentiability in NNs; below our paper.
- `qZwtPEw2qN.md` (6.80, Accept) — "How Much is a Noisy Image Worth?" on data scaling for ambient diffusion. Tangentially related (noisy vs clean data value); stronger than our paper due to thorough experiments and clearer theory-to-practice link.
- `qcigbR1UYA.md` (5.25, Reject) — Active binary testing bounds. Comparable theoretical depth but more incremental; similar quality to our paper.
- `4xWQS2z77v.md` (8.00, Accept) — Loss landscape of regularized NNs via convex duality. Superior theoretical depth and completeness; above our paper.
- `fMTPkDEhLQ.md` (8.00, Accept) — Tight lower bounds under Hölder smoothness. Exceptional theoretical contribution; above our paper.

**Round 1 bracket:** 4.5–6.5

**Round 2 (Narrowing):** Two queries targeting the (3.5, 6.5) and (5.0, 7.5) bands.

**Round 2 anchors:**
- `sIcPMMhl9W.md` (5.80, Reject) — Phase transition in shuffled regression. Similar style (phase transition analysis, theoretical). Our paper has a clearer contribution but the algebraic typo makes it slightly weaker. **Our paper ≈ comparable or slightly below.**
- `Jc0FssXh2R.md` (6.25, Accept) — Optimal criterion for feature learning in linear NNs. Clean theory with experiments. Our paper has more novel concept (Price of Quality) but the typo and lack of experiments make it weaker. **Our paper is below this anchor.**
- `ghH6YYDs15.md` (4.67, Reject) — Sparse autoencoders and amortization gap. Less relevant and weaker contribution. **Our paper is above this anchor.**
- `H8OOlBjhkU.md` (5.00, Reject) — Sparse optimization over restricted convex sets. Similar quality but our paper has more novel framing. **Our paper is slightly above.**

### Final Determination
The paper has a genuine theoretical contribution (Price of Quality, LASSO extension to heterogeneous noise) and is well-written. However, the algebraic typo in equations (12)/(14) — while almost certainly fixable — undermines the readability of the paper's central quantitative claim in its current form. The "sharpness" overclaim and the framing gap between the sufficient-condition-based γ and the paper's broader language further weaken the presentation. Compared to the round-2 anchors, the paper sits between the reject-level `sIcPMMhl9W.md` (5.80) and the accept-level `Jc0FssXh2R.md` (6.25), closer to the former due to the typo issue. With the typos fixed and the framing adjusted, the paper could be acceptable; in its current form it is marginal.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>