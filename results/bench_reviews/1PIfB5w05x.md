Now I have a good calibration set. Let me write the consolidated review.

---

## Summary

This paper introduces the mixed-quality data setting for sparse recovery, where a decoder receives \(n_1\) high-quality (low-variance) and \(n_2\) low-quality (high-variance) Gaussian measurements of a sparse signal. It provides the first information-theoretic sufficient conditions for support recovery in two settings: an *agnostic* setting where the decoder treats all samples identically (Theorem 1), and an *informed* setting where per-sample variances are known (Theorem 2). The trade-off between sample types is quantified via the "Price of Quality" \(\gamma\) — the number of low-quality samples needed to replace one high-quality sample. For algorithmic recovery, the paper extends the LASSO phase transition (Wainwright, 2009) to the heterogeneous-noise agnostic setting (Theorem 3), showing the recovery threshold depends only on total sample size and average noise variance, not individual noise levels.

## Strengths

- **Novel problem formulation and first sufficient conditions.** The mixed-quality data setting for sparse recovery is both practically motivated (LLM annotations, multi-site clinical trials) and previously unaddressed. The linear sufficient conditions in Theorems 1 and 2 are explicit, interpretable, and define a clear quantitative framework.

- **The Price of Quality concept (Section 3).** The coefficient ratio \(\gamma = \alpha_1/\alpha_2\) (equation 5) provides a crisp language for discussing sample-type trade-offs. The asymptotic analysis in (13)–(14) and (19)–(21) reveals genuinely different behavior across SNR regimes and between agnostic/informed settings — e.g., \(\gamma \leq 2\) uniformly in the agnostic case vs. arbitrarily large in the informed case.

- **LASSO phase transition extension (Theorem 3).** The result that the algorithmic threshold for signed-support recovery in the heterogeneous-noise agnostic setting matches the homogeneous-noise case, depending only on \(n = n_1+n_2\) and \(\sigma_{\text{avg}}^2\), is both surprising and technically non-trivial. The proof's use of the Haar measure on the orthogonal group (Lemma D.6) to handle the non-scalar covariance \(\Sigma\) is a genuine technical contribution beyond the classical Wainwright (2009) proof.

- **Transparency about limitations.** The paper explicitly acknowledges that the agnostic information-theoretic condition is sufficient but not tight (Remark 3.2), that the Chernoff bound relaxation is suboptimal, that necessity remains open (Remark 3.3), and that the informed LASSO case is not addressed (Remark 4.2). This honesty strengthens the paper's credibility.

## Weaknesses

### Major

- **Absence of necessary conditions (converse bounds) for the information-theoretic results.** Theorems 1 and 2 provide only sufficient conditions. The Price of Quality bounds — including the striking claim that \(\gamma \leq 2\) in the agnostic setting — are properties of a particular proof technique (a relaxed Chernoff bound; see Remark A.1 and the choice \(\theta^\star = 1/(4\sigma_2^2)\) in the appendix). Without converse bounds, these numbers may not reflect fundamental limits of the problem. The paper acknowledges this ("the condition in Theorem 1 is sufficient and is not expected to be information-theoretically sharp"), but the narrative still presents the Price of Quality as a property of the problem rather than of the sufficient condition. This limits the force of the central message.

- **No experimental validation.** The paper is entirely theoretical. Even small-scale simulations — e.g., a phase-transition plot for the LASSO under varying \(n_1/n_2\) ratios, or empirical validation of the predicted Price of Quality bounds — would substantially strengthen the contribution by testing whether the sufficient conditions are practically tight and illustrating the claimed phenomena.

### Minor

- **The \(n_1, n_2 = \omega(s)\) restriction in Theorem 3 is not discussed.** This condition excludes the practically relevant scenario where high-quality data is scarce (\(n_1 = O(s)\)) while low-quality data is abundant. The paper does not indicate whether this is an artifact of the proof technique or a genuine limitation of the LASSO in this setting. Since the classical Wainwright result requires only the total \(n\) to satisfy the threshold, the additional per-block requirement deserves explicit comment.

- **The agnostic LASSO penalty selection issue.** Theorem 3's regularization condition (28) and the explicit \(\lambda_p\) choice (31) depend on \(\sigma_{\text{avg}}^2 = (n_1\sigma_1^2 + n_2\sigma_2^2)/n\). While an aggregate noise statistic like \(\sigma_{\text{avg}}^2\) may be estimable without per-sample variance knowledge (e.g., from residuals, or via the \(Y_i^2\) proxy discussed in Remark 3.2), the paper does not discuss how a genuinely agnostic decoder would set \(\lambda_p\) in practice. The theory characterizes what \(\lambda_p\) works, but does not close the loop on implementability. This is a gap between the theoretical condition and the agnostic premise.

### Trivial

- None worth flagging.

## Nice-to-Haves

- A figure plotting \(\gamma\) as a function of SNR\(_1\)/SNR\(_2\) in both agnostic and informed settings would make the regimes discussed in the text visually immediate.

- Discussion of whether the \(n_1, n_2 = \omega(s)\) condition can be relaxed to only require the total \(n = \omega(s)\), as in the classical homogeneous case.

## Removed Points

*These points are flagged to be removed, treat them with caution.*

- **Harsh Critic's "λ inconsistency as fatal":** The critic claims the agnostic premise is contradicted because \(\sigma_{\text{avg}}^2\) must be known. The paper's agnostic setting means the decoder lacks *per-sample* variance knowledge, not aggregate noise knowledge. An aggregate statistic could be estimated without per-sample labels. The critic's claim of contradiction is overstated — this is a presentation gap, not a logical contradiction. Moved to Minor.

- **Harsh Critic's claim that Theorem 2's "sharp convergence rate" claim is unsupported:** The paper's Remark 3.3 explicitly states "Establishing full necessity in the heterogeneous setting remains an interesting direction for future work." The paper does not claim sharpness — it says the Chernoff optimization "yields a sharp convergence rate" in the sense that the bound is optimized (as opposed to the agnostic relaxation), not that the threshold is necessarily tight.

- **Strength Finder's "Sharp contrast between agnostic and informed settings":** This strength is retained but qualified — the contrast is between *sufficient conditions*, not fundamental limits.

- **Formatting/typo nitpicks:** All removed per hard rules.

## Novel Insights

The most genuinely novel insight from the reviews is the observation that the algorithmic threshold (LASSO) appears *more robust* to data heterogeneity than the information-theoretic threshold. Theorem 3 shows the LASSO threshold is invariant to how noise is distributed across the two blocks, depending only on the total \(n\) and average noise — yet the information-theoretic sufficient conditions change substantially between agnostic and informed settings. This asymmetry between computational and statistical recovery under heterogeneity mirrors a pattern observed in other sparse recovery variants (sparse designs, Wang et al. 2010) and may point to a broader principle worth investigating.

## Suggestions

1. Add even a minimal simulation (e.g., a phase-transition heatmap for the LASSO at a few \(n_1/n_2\) ratios) to ground the theoretical results empirically.
2. Explicitly discuss whether the \(n_1, n_2 = \omega(s)\) condition can be weakened, or clarify that it is likely an artifact of the proof.
3. Add a brief paragraph discussing how \(\sigma_{\text{avg}}^2\) could be estimated from data in the agnostic setting, connecting Remark 3.2's \(Y_i^2\) approach to the LASSO penalty selection.
4. Tone down language that implies the Price of Quality is a fundamental property (e.g., replace "one high-quality sample is never worth more than two" with "under our sufficient condition, one high-quality sample is never worth more than two") — the paper already does this in places but not consistently.

---

**Anchor comparison:**

| Anchor | Score | Comparison |
|--------|-------|------------|
| Q3yLIIkt7z (Scaling Laws, Accept Oral) | 7.00 | More complete: full phase diagram, experiments, tight results. Our paper is narrower (sufficient only, no experiments). |
| 6UpstNltZ4 (Sparse NN Recovery, Accept Poster) | 6.40 | Similar "first guarantees" contribution but includes experiments and practical algorithm validation. Our paper lacks experiments. |
| pliEmukDsv (Column Thresholding, Reject) | 5.00 | Similar strength: theoretical contribution with contested claim strength. Our paper is more transparent about limitations and has deeper technical novelty (Theorem 3). |
| TP4gsjpi7z (Shuffled Regression, Reject) | 3.50 | Much weaker: poor writing, unjustified approximations. Our paper is considerably stronger on clarity and rigor. |
| m3BJUh0h8J (Generalization Bounds, Reject) | 3.00 | Limited evidence, narrow scope. Our paper's technical contribution is substantially deeper. |

The paper under review sits between the 5.00 and 6.40 anchors. It has genuine novelty and technical depth but lacks experimental validation and converse bounds that would make it a clear accept. Score: **5.5**.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>