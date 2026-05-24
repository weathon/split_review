## Summary

This paper studies differentially private domain discovery through the lens of *missing mass* (fraction of total item frequency not recovered) rather than the standard cardinality objective. The authors prove that the Weighted Gaussian Mechanism (WGM) achieves near-optimal ℓ₁ missing mass on Zipfian data (Theorem 3.3, with a matching lower bound in Theorem 3.5) and a distribution-free ℓ∞ missing-mass guarantee (Theorem 3.6). These results are then leveraged via a simple two-stage meta-algorithm (WGM for domain discovery followed by a known-domain algorithm) to obtain novel utility guarantees for unknown-domain top-k and k-hitting set. Experiments on six datasets show the approach is empirically competitive with or outperforms existing baselines.

## Strengths

- **First absolute utility guarantees for DP set union.** The paper delivers the first provable missing-mass bounds for DP set union — a problem for which prior work only gave relative (algorithm-vs-algorithm) guarantees. Theorem 3.3 provides a high-probability ℓ₁ missing-mass upper bound for WGM on Zipfian data, and Theorem 3.5 gives a near-matching lower bound (up to logarithmic factors), establishing near-optimality.

- **Distribution-free ℓ∞ missing-mass guarantee.** Theorem 3.6 bounds MM∞ for *any* dataset without requiring a Zipfian assumption. This is leveraged to derive utility guarantees for unknown-domain top-k (Theorem 4.3) and k-hitting set (Theorem 4.5) that do not depend on distributional assumptions, making the results broadly applicable.

- **Clean synthesis of existing tools into new results.** The two-stage approach (WGM then a known-domain mechanism) and the extension of the submodular maximization (1−1/e) guarantee to the unknown-domain k-hitting set setting are technically natural but yield genuinely new guarantees. The theoretical presentation is clear and well-structured.

## Weaknesses

### Fatal
None.

### Major
**Missing statistical uncertainty in Figures 1 and 2.** The set union (Figure 1) and top-k (Figure 2) experiments report only the mean over 5 trials with no error bars, standard deviations, or confidence intervals. With only five runs, the reader cannot assess whether the observed performance ordering is stable. This is particularly conspicuous because the k-hitting set experiments (Figure 3) *do* report standard errors, demonstrating the authors know how to compute them. Since the paper makes empirical claims (e.g., "WGM obtains MM within 5% of that of the policy mechanisms"), the absence of variance information weakens the evidential weight of the experiments. This does not threaten the theoretical contributions but should be addressed before publication.

### Minor

- **Baseline objective mismatch in set union experiments.** The baselines (Policy Gaussian, Policy Greedy) were designed and tuned for *cardinality* maximization, not missing-mass minimization. The paper's comparison on missing mass naturally favors WGM, whose thresholding focuses on heavy items. The paper briefly contrasts its results with prior cardinality findings but does not explicitly acknowledge this objective mismatch. A short discussion would resolve this.

- **Near-optimality claim could be more precise.** The abstract states WGM has a "near-optimal ℓ₁ missing mass guarantee," which is supported by Theorems 3.3 and 3.5. However, the gap between the upper and lower bounds involves logarithmic factors and the lower bound is for a *specific* (C,s)-Zipfian dataset. Making this explicit (e.g., "matching up to polylog factors for a worst-case Zipfian instance") would improve precision.

### Trivial
- In the `k`-hitting set experiments, Figure 3 shows "number of missed users" (lower is better) but the main text describes it as "number of users hit." The relationship between these quantities should be clarified to avoid confusion.

## Nice-to-Haves

- Adding a simple missing-mass-tailored baseline for set union (e.g., noisy histogram with a DP threshold) would strengthen the empirical comparison.
- Closing the gap between upper and lower bounds for top-k and k-hitting set is acknowledged as future work and need not be addressed here.

## Removed Points

- **Formatting artifact in Theorem 4.5 ("1 - 1/ϵ" → "1 - 1/e"):** Removed per instruction — this is a PDF-parser artifact that does not appear in the original submission.
- **Missing appendix/proof references:** Removed per instruction — the parser strips appendices from all submissions; they exist in the original.
- **Adding missing related work:** Removed per instruction — I cannot verify the existence of unmentioned works.
- **Reproducibility concerns (undisclosed hyperparameters):** Removed per instruction — the paper states code is in the supplement, and hyperparameter details (e.g., α=3 for policy mechanisms) are provided.
- **Generic strength ("addressed an important problem"):** Removed from Strengths — lacks concrete, paper-specific evidence.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective on the work that the authors themselves do not discuss.

## Suggestions

1. Add error bars (standard deviation or 95% CI) to Figures 1 and 2, or justify with a variance analysis that 5 trials suffice.
2. Add a sentence in Section 5.1 acknowledging that the baselines were designed for cardinality and that the missing-mass comparison may favor WGM for this reason.
3. Clarify the relationship between "users hit" and "missed users" in Section 5.3 to match the figure axes.

## Score and Decision

**Calibration anchors:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| XgdVHwpgNA (DPBloomfilter) | 2.50 | R1 (weak) | Much weaker — flawed methodology |
| tm3K2omGNx (Gumbel DP top-k) | 1.50 | R1 (weak) | Much weaker — incorrect proofs |
| ldYKqmtLm5 (DP OPH) | 5.00 | R1 (mid) | Weaker — standard techniques, limited novelty |
| gIaAuu8UZZ (Private Turnstile Streams) | 6.50 | R1 (mid), R2 | Comparable — similar-tier theory DP paper with matching strengths |
| C4jAhm8L1V (Beyond Membership) | 6.00 | R2 | Slightly weaker — empirical focus vs. theoretical contribution |
| 6rvpzYGNOn (Accuracy-First Rényi DP) | 5.00 | R2 | Weaker — narrower contribution |
| EEr6cADbZx (Back to Square Roots) | 7.50 | R2 | Stronger — tighter theory with matching bounds |

**Bracketing:** Round 1 placed the paper in the mid-to-strong range (between the weak anchors at ~2-3 and strong anchors at 8). Round 2 narrowed the bracket by comparing against papers in the 4.5–8.0 range. The paper is clearly stronger than DP OPH (5.0) and Accuracy-First Rényi DP (5.0), comparable to Private Turnstile Streams (6.5) and slightly stronger than Beyond Membership (6.0). It does not match the tightness of the Back to Square Roots paper (7.5), which gives matching upper/lower bounds for a core DP problem rather than partial gaps.

The paper's theoretical contribution (first absolute guarantees for DP set union with matching bounds, plus the distribution-free ℓ∞ result) is genuine and significant. The experimental concerns are real but addressable and do not undermine the theory. The paper does not have the kind of fatal flaw that would require a low score, but the experimental gap prevents it from reaching the top tier.

**Round 1 bracket:** Between ~3.5 and ~7.5. **Round 2 narrowing:** Tightened to 6.0–7.0 based on comparison with anchors. **Final score:** 6.5.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>