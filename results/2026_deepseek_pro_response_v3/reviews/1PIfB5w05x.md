Now I have a clear calibration picture. Let me synthesize everything into the final review.

**Calibration comparison:**

| Anchor | Score | How our paper compares |
|---|---|---|
| NHhjczmJjo (Transformers in sparse recovery) | 7.00 | Weaker — that paper has similarly strong theory plus robust empirical validation, tighter results |
| wpXGPCBOTX (Sparsistency for inverse OT) | 6.75 | Slightly weaker — comparable theory depth but our info-theoretic results are only sufficient |
| 4vzGQcVUG8 (Weak-to-strong generalization) | 6.50 | Comparable — similar tier of theory paper with clear phase transitions, acknowledged limitations |
| zhFyKgqxlz (Community recovery w/ side info) | 5.75 | Stronger — our results are cleaner, Theorem 3 is necessary+sufficient, better presentation |
| sIcPMMhl9W (Shuffled regression phase transition) | 5.80 | Stronger — our results are more complete and the PoQ concept is more novel |
| gVVoZtiQlt (Shuffled regression) | 5.00 | Clearly stronger |

**Round 1 bracket:** 5.5 – 7.5  
**Round 2 narrows to:** 6.0 – 6.5, since the paper sits between zhFyKgqxlz (5.75, clearly weaker) and NHhjczmJjo (7.00, clearly stronger), and is comparable to 4vzGQcVUG8 (6.50) but with some additional limitations (no lower bounds, PoQ anchored to sufficient conditions).

**Final score: 6.0**

---

## Summary
This paper studies sparse support recovery when observations come from two sources with different noise variances (σ₁² < σ₂²). It provides sufficient conditions on sample sizes (n₁, n₂) for information-theoretic recovery in both agnostic and informed settings, defining the "Price of Quality" γ — how many low-quality samples replace one high-quality sample for the sufficient condition to hold. The strongest contribution is Theorem 3, which establishes a necessary-and-sufficient phase transition for LASSO recovery in the agnostic setting, showing the threshold depends only on total sample size and average noise level. Together, these results expose a fundamental contrast: algorithmic recovery via LASSO is robust to data heterogeneity in a way that information-theoretic recovery is not.

## Strengths
- **Theorem 3 (LASSO phase transition) is a genuinely strong result**: It provides both necessary and sufficient conditions for signed-support recovery in the heterogeneous-noise agnostic setting, showing the threshold n_ALG = 2s log(p−s) + s + 1 depends only on total n and the regularization condition depends only on σ_avg². The proof technique — QR decomposition of X_S and Haar measure on the orthogonal group to handle the non-scalar Σ — is a non-trivial technical extension of Wainwright (2009).
- **Clean asymptotic Price of Quality analysis across SNR regimes**: The paper partitions parameter space into three regimes and derives interpretable asymptotic expressions for γ: γ ≃ 1 (high SNR), γ ≃ 2 − σ₁²/σ₂² < 2 (low SNR, agnostic), and γ → +∞ (mixed regime, informed). These formulas sharply illustrate the conceptual difference between agnostic and informed settings.
- **Transparency about limitations**: Remark 3.2 explicitly acknowledges the looseness of the sufficient condition in Theorem 1, the potential suboptimality of the agnostic estimator, and the relaxation used to obtain a closed form. This candor strengthens the paper's credibility.
- **Novel contrast between information-theoretic and algorithmic thresholds**: The juxtaposition of Theorems 1–2 with Theorem 3 reveals that algorithmic recovery is fundamentally more robust to data heterogeneity than information-theoretic recovery, adding a theoretically grounded example to the broader understanding of how these threshold types respond differently to problem perturbations.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **The Price of Quality is anchored to sufficient conditions, not to the true information-theoretic threshold**: The paper is transparent that γ measures the exchange rate "for the sufficient condition to hold" (qualifier present in abstract, §1.2.1, and §3.1). However, since Remark 3.2 acknowledges the sufficient condition in Theorem 1 is not expected to be tight, the true trade-off between high- and low-quality samples could differ from what γ reports. The framing in the title and §5 could invite readers to interpret γ as a fundamental property of the recovery problem rather than of a particular Chernoff-bound relaxation. This does not invalidate the results but slightly weakens their practical interpretation.
- **No lower bounds for Theorems 1–2**: The paper provides only sufficient conditions for the information-theoretic setting. Without matching necessary conditions, the reader cannot gauge how loose or tight the sufficient conditions are. Theorem 2 optimizes the Chernoff exponent exactly (Remark 3.3), making it plausibly close to tight, but the gap for Theorem 1 is unquantified. The paper acknowledges this honestly, so this is a scope limitation rather than an error.
- **The agnostic-informed comparison confounds estimator quality with information availability**: Remark 3.2 notes the agnostic estimator (unweighted least squares, equation 8) may be suboptimal compared to variance-aware alternatives. The contrast between agnostic (Theorem 1) and informed (Theorem 2) settings therefore mixes two differences: knowing σ² versus using a different loss function. The practical implication in §5 ("quantify uncertainty... and rescale the loss") is partly confounded as a result. The paper is transparent about this, so it remains a minor concern.

### Trivial
- **No empirical validation**: The paper is entirely theoretical. While standard for this subfield (Wainwright, 2009; Reeves et al., 2019 are purely theoretical), even a small simulation verifying the γ ≃ 2 − σ₁²/σ₂² bound or the LASSO threshold independence would strengthen the empirical grounding.

## Nice-to-Haves
- Deriving even a simple lower bound (e.g., via Fano's inequality) for the information-theoretic setting would anchor the sufficient conditions.
- A numerical study of the gap between the relaxed and exact Chernoff exponents mentioned in Remark 3.2 would help readers calibrate the PoQ analysis.
- Extending the analysis to the informed LASSO setting (discussed in Remark 4.2) would complete the picture, though this is acknowledged as nontrivial.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **Harsh Critic: "The agnostic estimator may not be the best agnostic procedure" framed as a structural/methodological gap**: The paper already acknowledges this candidly in Remark 3.2. This is not a hidden flaw — it is an explicitly discussed and honestly stated limitation. Moved from potential Major to already-addressed.
- **Harsh Critic: Discrepancy between equations (9) and (12) as evidence of mathematical error**: The σ₁⁴ vs σ₂² discrepancy between (9) and (12) is almost certainly a PDF parser artifact, not an author error. The asymptotic analysis in (13)–(14) is internally consistent and would not work with the σ₁⁴ version. Removed per hard rules on parser artifacts.
- **Strength Finder: "Extension to arbitrary noise covariance structures" as a core strength**: This extension is stated without proof in Remark 3.4 and further loosens the already-loose sufficient condition for Theorem 1 via σ_max(Σ). It is a reasonable generalization remark but not a core strength of the paper.
- **Harsh Critic: "The framing elevates the PoQ to a status the mathematics does not fully support" as a structural/fatal issue**: The paper includes the qualifier "for the sufficient condition to hold" in the abstract, §1.2.1, and §3.1. The issue is one of emphasis rather than accuracy. The harsh critic's stronger version of this claim is demoted; the retained version in Minor reflects the genuine but limited concern.

## Novel Insights
The most valuable insight is the contrast between information-theoretic and algorithmic recovery under data heterogeneity: while the information-theoretic sufficient conditions reveal a nuanced Price of Quality that distinguishes high- from low-quality samples (and differs dramatically between agnostic and informed decoders), the algorithmic (LASSO) threshold treats all samples equally regardless of their noise variance, depending only on the average noise level σ_avg². This provides a concrete, theoretically grounded example adding to the broader observation that algorithmic thresholds tend to be more "robust" to problem perturbations than information-theoretic ones (Wang et al., 2010; Omidiran & Wainwright, 2008; Gamarnik & Zadik, 2022).

## Suggestions
- Tighten the framing of the Price of Quality by using the qualifier "for the sufficient condition to hold" more consistently in prominent locations — especially the title and conclusion, which currently read more expansively than the careful language in the abstract and §3.1.
- Consider adding a brief discussion quantifying (even approximately) how much the relaxation in Theorem 1 costs relative to the cubic-equation optimum mentioned in Remark 3.2, perhaps through a numerical comparison for representative parameter values.
- If space permits, a small simulation verifying the theoretical predictions (especially the γ ≃ 2 − σ₁²/σ₂² bound and the LASSO threshold independence from quality composition) would substantially strengthen the empirical grounding.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>