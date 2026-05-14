Now I have a comprehensive understanding of the paper and the calibration anchors. Let me write the final consolidated review.

## Summary

The paper studies sparse support recovery when observations come from mixed-quality sources (high-noise and low-noise). It provides sufficient conditions for information-theoretic recovery in both agnostic and informed settings, introduces a "Price of Quality" quantifying the trade-off between high-quality and low-quality samples, and extends the LASSO phase transition (Wainwright 2009) to the heterogeneous-noise agnostic setting using QR decomposition and Haar measure.

## Strengths

- **Extension of the LASSO phase transition to heterogeneous-noise agnostic setting.** Theorem 3 proves that the sample-size condition for signed support recovery using the LASSO is \( n > 2s\log(p-s)+s+1 \), independent of the individual noise variances \( \sigma_1^2, \sigma_2^2 \). The proof overcomes the breakdown of Wishart structure when the noise covariance is not a scalar multiple of the identity, using QR decomposition and Haar-measure properties — a non-trivial technical contribution (lines 812–817).

- **First sufficient condition for sparse recovery under heterogeneous noise that quantifies the trade-off between sample qualities.** The Price of Quality \(\gamma\) (equations (12), (18)) provides explicit closed-form expressions for how many low-quality samples replace one high-quality sample under the derived sufficient conditions. The contrast between the agnostic setting (\(\gamma<2\)) and the informed setting (\(\gamma\) can grow arbitrarily large) is conceptually valuable and clearly delineated.

- **Explicit characterization of the noise-scaling condition for LASSO recovery.** Proposition 4.1 (equation (30)) provides a necessary and sufficient condition \( \sigma_{\text{avg}}^2 = o\!\left(n/(1+s/\rho^2)\log(p-s)\right) \) for the regularization parameters in Theorem 3 to exist, bridging the algorithmic threshold to allowable noise levels.

- **Clear distinction between information-theoretic and algorithmic thresholds.** The paper identifies that the information-theoretic sufficient conditions depend on individual noise variances while the LASSO threshold depends only on the total sample size, robustly independent of the quality asymmetry (Section 5, lines 920–926). This contrast is insightful and well-motivated.

## Weaknesses

### Major

- **The central information-theoretic contribution (Price of Quality \(\gamma<2\)) is derived from a sufficient condition whose looseness is unquantified.** Remark 3.2 explicitly acknowledges that the Chernoff bound used relies on a suboptimal choice of \(\theta\) (specifically \(\theta^* = 1/(4\sigma_2^2)\)) and that optimizing the exact cubic equation (37) would yield a tighter condition. However, the paper provides neither a lower bound on the true threshold nor any numerical assessment of how conservative the derived condition is. The cubic equation (37) remains unsolved, leaving readers unable to judge whether \(\gamma<2\) is a genuine property of the recovery problem or an artifact of the relaxation. While the paper qualifies its claims by consistently stating "for this sufficient condition to hold," the headline result will naturally be interpreted as a property of the problem itself. This significantly weakens the information-theoretic contribution's impact and novelty.

- **No experimental validation or simulations.** The paper is entirely theoretical with no numerical experiments. Given that the information-theoretic results are only sufficient (and potentially loose), simulations evaluating the tightness of condition (9), the phase transition boundary from Theorem 3, or comparisons with weighted estimators in the informed setting would substantially strengthen the paper's practical relevance and help readers assess the conservativeness of the bounds. Even simple phase diagrams in the \((n_1,n_2)\) plane would add significant value. In a venue like ICLR, the lack of any empirical grounding is a significant gap.

### Minor

- **LASSO analysis is restricted to the agnostic setting; the informed setting is deferred.** Theorem 3 covers only the agnostic setting. The natural extension to a weighted (variance-rescaled) LASSO in the informed setting is discussed only briefly in Remark 4.2 and left for future work with an explanation of why the proof technique breaks down. This is an honest limitation, but it means the algorithmic contribution is incomplete: the contrast between information-theoretic and algorithmic thresholds is drawn only in one of the two settings, limiting the paper's scope and the generality of its conclusions.

- **The presentation of the LASSO proof is dense and relies heavily on appendix machinery.** While the proof is technically sound, the main text provides only a sketch (lines 820–840). The full proof in Appendix D involves lengthy computations (e.g., Lemma D.5 on fourth moments of Haar matrices, the multi-page variance calculation for \(M_p\)). This makes verification challenging and obscures the key insight behind why heterogeneous noise does not affect the LASSO threshold beyond the average noise level. A more streamlined exposition of the core argument would improve accessibility.

### Trivial

- The definition of \(\gamma\) in (12) involves a logarithm ratio; it could be noted that the numerator uses \(2\sigma_2^2 - \sigma_1^2\) in one term while the denominator uses \(\delta s/(2\sigma_2^2)\). The meaning of "replacing one high-quality sample by \(\gamma\) low-quality samples" is explained but would benefit from a more explicit example.

- The statement in Section 5 (line 929) that "the informed information-theoretic threshold and the LASSO threshold are sharp" for the informed setting could be slightly misleading — Theorem 2 is also a sufficient condition, and the paper notes in Remark 3.3 that "establishing full necessity in the heterogeneous setting remains an interesting direction."

## Nice-to-Haves

- A numerical simulation testing the tightness of the sufficient condition (9) — for example, fixing \(p,s,\sigma_1^2,\sigma_2^2\) and varying \(n_1,n_2\) around the boundary to plot empirical recovery probabilities against the predicted threshold — would directly address the main weakness.
- Solving the cubic equation (37) numerically for representative parameter regimes and comparing the resulting exponent to the relaxed one would quantify the looseness.
- A phase diagram in the \((n_1,n_2)\) plane showing boundary (9) alongside the homogeneous-noise threshold would help visualize the Price of Quality.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The proofs in Appendix make verification difficult"** — This is a presentation/personal taste comment, not a substantive weakness about correctness. The proofs are provided and appear sound.
- **"The heavy machinery raises the question of whether a simpler argument might have sufficed"** — Speculation without evidence; the difficulty is inherent to the heterogeneous-noise setting.
- **"The abstract could be read as stating a fundamental property... the body clarifies"** — The abstract explicitly qualifies "for this sufficient condition to hold." This is a reader-interpretation concern, not an error.
- **Criticism about missing related work** — I do not have external sources to confirm whether work is missing or not.
- **"The paper only compares against..."** — No such claim is made; the critic's specific comparison complaints are not applicable.
- **Formatting/style nitpicks** — Removed per instructions.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Quantify the looseness.** Solve the cubic equation (37) numerically for representative parameter regimes and compare the resulting optimal Chernoff exponent to the one obtained with \(\theta^* = 1/(4\sigma_2^2)\). This would give readers a concrete sense of how conservative \(\gamma<2\) is and whether the Price of Quality would change qualitatively under the optimal bound.

2. **Add simulations.** The paper would benefit substantially from even simple synthetic experiments: (a) phase transition plots for Theorem 1's sufficient condition, (b) verification of the LASSO threshold in Theorem 3 under heterogeneous noise, (c) comparison with a weighted estimator in the informed setting to illustrate the Price of Quality gap.

3. **Sharpen the presentation of the LASSO proof sketch.** The main text's proof sketch (lines 820–840) could more explicitly highlight why the Haar-measure argument breaks the dependence on individual noise variances. The current sketch is too terse to convey the key insight.

4. **Consider a lower bound for the agnostic information-theoretic threshold.** Even a simple lower bound showing \(\gamma \ge 1 + c\) in some regime would demonstrate that the Price of Quality is not an artifact of the sufficient condition alone.

## Score and Decision

### Calibration Anchors

| Path | Avg Score | Comparison |
|------|-----------|-----------|
| `/home/wg25r/review_agent/human_reviews_2026/6UpstNltZ4.md` | 6.40 (Accept) | Sparse NN recovery with theory + experiments. Our paper has comparable technical depth for the LASSO part but lacks experiments and has a weaker information-theoretic contribution. |
| `/home/wg25r/review_agent/human_reviews_2026/pliEmukDsv.md` | 5.00 (Reject) | Sparse spiked Wigner with a strong assumption limiting scope. Our paper has a similar pattern — solid technical contribution limited by weaknesses (looseness of sufficient condition, no experiments). Comparable overall. |
| `/home/wg25r/review_agent/human_reviews_2026/zXu7faqHCj.md` | 4.67 (Reject) | Sparse recovery preconditioner with theory + experiments but incomplete validation. Our paper has weaker empirical support but more thorough theory. |
| `/home/wg25r/review_agent/human_reviews_2026/TP4gsjpi7z.md` | 3.50 (Reject) | Shuffled regression phase transition theory with clarity issues. Our paper is clearer and more rigorous. |
| `/home/wg25r/review_agent/human_reviews_2026/yRtgZ1K8hO.md` | 8.00 (Accept Oral) | High-scoring paper on matrix sign methods. Not directly comparable in topic but serves as a high-score anchor. |
| `/home/wg25r/review_agent/human_reviews_2026/mVFFqmvkDi.md` | 1.50 (Withdrawn) | Very weak paper; our paper is far stronger in technical contribution and clarity. |

**Overall assessment:** The paper makes a genuine technical contribution in extending the LASSO threshold to heterogeneous noise and introduces a conceptually interesting Price of Quality. However, the information-theoretic contribution is significantly weakened by the unquantified looseness of the sufficient condition on which its headline result depends. The absence of any experimental validation further limits the paper's impact and ability to ground its claims. The LASSO contribution is solid but restricted to the agnostic setting. On balance, the weaknesses are substantial enough that the paper would benefit from major revisions (quantifying the looseness, adding simulations) before being competitive at a top venue.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>