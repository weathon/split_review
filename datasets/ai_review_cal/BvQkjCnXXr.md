- Decision: Reject
- Avg Score: 4.50
- Scores: 3, 5, 5, 5
Now I have a thorough understanding of the paper and can evaluate each claim against the actual text. Let me produce the final consolidated review.

---

## Summary

This paper proposes FastLSH, a locality-sensitive hashing scheme that reduces per-hash complexity from O(n) to O(m) by randomly sampling m out of n dimensions *before* applying the standard random projection (E2LSH). The collision probability is derived (Theorem 4.2), and asymptotic equivalence to E2LSH is argued. The method is validated on three tasks (outlier detection, neural network training, ANN search) with reported end-to-end speedups of up to 6.1×, 1.7×, and 20× respectively.

## Strengths

- **Provable complexity reduction with a clean design.** The method is elegantly simple: random dimension sampling followed by the standard E2LSH projection. Section 3.1 clearly states the reduction from O(n) to O(m), and the hash function (Equation 3) is well-defined. The sampling and projection steps are implemented with just two basic operations.

- **Rigorous collision probability expression.** Theorem 4.2 gives the exact form of p(s,σ) = ∫ f_{|s̃X|}(t)(1−t/w̃)dt. Lemmas 4.1–4.4 provide the distributional building blocks (CLT for s̃², truncated normal model for s̃, characteristic function of s̃X). The derivation of the characteristic function (Lemma 4.4) is nontrivial and explicitly displayed.

- **Broad empirical validation across three distinct tasks.** The evaluation covers outlier detection (3 datasets: Musk, a9a, Statlog Shuttle), neural network training (2 large recommendation datasets: Delicious-200K, Amazon-670K), and ANN search (12 datasets). End-to-end speedups are reported for each task, with the most striking being up to 20× reduction in index construction time (Figure 3d) and 6.1× in anomaly detection latency (Table 1).

- **Source code provided.** The anonymous repository link is given in the abstract, supporting reproducibility.

## Weaknesses

### Fatal
None.

### Major
- **The Musk outlier-detection results (Table 1) contain an unexplained discrepancy that the paper does not acknowledge.** The text claims FastACE offers "around the same performance as ACE in terms of the numbers of correctly reported outliers and missed ones." However, the reviewer reports that FastACE detects 4 outliers (all correct) versus ACE's 16 detected (8 correct) — a 50% reduction in correctly-reported outliers. This is not "around the same," and the paper offers no discussion of why FastACE misses outliers that ACE catches, nor any explanation (e.g., precision/recall trade-off, near-boundary cases). Since the table is an embedded image, I cannot independently verify the exact numbers, but if the reviewer's reading is accurate, this directly contradicts a stated claim and needs author clarification. This is the single most concerning evidential issue in the paper.

### Minor
- **No variance or multiple-trial reporting for any experiment.** All results (outlier detection counts, training times, query times, recall) are reported as single numbers. LSH is inherently randomized — both FastLSH and E2LSH draw random projections and (for FastLSH) random samples — yet no error bars, confidence intervals, or mention of multiple trials are provided. This makes it impossible to assess whether observed speedups or accuracy differences are statistically significant. (I note that single-run reporting is common in large-scale benchmark papers in this subfield, but given the randomized nature of the method, even 3–5 trials with means would substantially strengthen the evidence.)

- **Sampling with replacement is used but not justified.** The paper explicitly samples with replacement (multiset S, line 82: "draw m i.i.d. samples… to form a multiset S"), which allows duplicate dimensions. This inflates the variance of the distance estimator s̃² compared to sampling without replacement. The choice is never discussed, nor is the simple alternative of sampling without replacement considered. An ablation would help understand the trade-off.

- **Section 5 (extensions) is too brief to be useful.** Extensions to angular similarity and maximum inner product search are sketched in two sentences with no derivation, analysis, or experiments. This section could be removed or expanded; in its current form it adds little.

### Trivial
- Some equation cross-references (e.g., "Eqn. 2" and "Eqn. 6") are mentioned but the equation numbers are not clearly labeled in the extracted text. Clarifying references would improve readability.

## Nice-to-Haves
- A plot of recall vs. m (number of sampled dimensions) and speedup vs. m would help readers understand the trade-off controlled by this key hyperparameter.
- A comparison of FastLSH with a simple fixed-subset baseline (using the same m dimensions for all hash functions without resampling) would isolate the benefit of randomized sampling.
- A discussion of failure modes: when could random sampling degrade accuracy (e.g., dimensions with small variance, heavy-tailed per-dimension distances)?

## Removed Points
- **Criticism of the theoretical analysis as "structurally flawed" / "incomplete."** The harsh critic claims a "structural gap" and asserts that "the actual variance of s̃X is E[s̃²] = (m/n)s² + mσ², not (m/n)s²." This is mathematically incorrect: E[s̃²] = m·μ = m·s²/n (no σ² term in the expectation; the reviewer conflated the variance of s̃² with its mean). The critic further faults Section 4.2 for lacking a theorem statement — but the theorem was deferred to the appendix, which the parser stripped. Per the review guidelines, missing appendix proofs are not penalized. The paper's main text provides Theorem 4.2, Lemma 4.4, the characteristic function, and Figure 1 as numerical evidence, so the theoretical criticism as stated is substantially weakened or invalid.

- **"Missing related work."** Per the review guidelines, I do not have external sources to verify this.

- **Formatting/style nitpicks and "strengthening the paper" suggestions that are standard methodological expectations.** These have been incorporated into Nice-to-Haves or Minor weaknesses where substantive.

From the Strength Finder, the following were removed as too thin or conflicting with verified weaknesses: "Extension to other similarity measures" (one paragraph, no derivations or experiments) and generic/superficial praise not anchored to specific paper content.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. **Clarify the Musk results.** Verify whether FastACE's correctly-reported outlier count is truly comparable to ACE's; if not, provide an explanation (e.g., FastACE achieves higher precision at the cost of recall, or the missed outliers are near-boundary decisions). A precision-recall scatter plot would help.
2. **Report means and standard deviations over multiple runs** for the outlier detection and ANN experiments, where randomness is inherent. Even 3–5 trials would substantially increase confidence in the reported speedups.
3. **Justify or experimentally compare sampling with replacement vs. without replacement.** A one-paragraph discussion or a small ablation would address this concern.
4. **Include an ablation on m.** Show how recall and hashing time vary with m (e.g., for one or two datasets) to illustrate the practical trade-off between speed and accuracy.
