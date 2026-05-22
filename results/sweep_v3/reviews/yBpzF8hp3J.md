Now I have all the information needed to write the consolidated review.

## Summary

This paper provides the first absolute utility guarantees (upper and lower bounds) for differentially private set union, reformulated in terms of "missing mass" rather than cardinality. The authors show the Weighted Gaussian Mechanism (WGM) achieves near-optimal ℓ₁ missing mass on Zipfian data and a distribution-free ℓ∞ bound. These results are then applied to obtain the first utility guarantees for unknown-domain variants of top-k and k-hitting set via a simple WGM-then-known-domain meta-algorithm. Experiments on six real datasets demonstrate competitive empirical performance.

## Strengths

- **First absolute utility guarantees for DP set union.** Theorem 3.3 provides a high-probability upper bound on the missing mass of WGM for Zipfian datasets, and Theorem 3.5 gives a matching lower bound (up to polylog factors), establishing near-optimality. Prior work only provided relative comparisons. This is a clear theoretical advance.

- **Novel guarantees for unknown-domain top-k and k-hitting set.** Theorems 4.3 and 4.5 give the first utility bounds for these problems when the domain is not known a priori, using WGM as a domain-discovery precursor. Corollaries 4.4 and 4.6 prove that a linear k/ε dependence is unavoidable, establishing the first rigorous baselines for these variants.

- **Distribution-free ℓ∞ missing-mass bound (Theorem 3.6).** This guarantee requires no Zipfian assumption, which is essential for the top-k and k-hitting set applications that need worst-case bounds. It cleanly extends the reach of the theoretical results beyond the Zipfian setting.

- **Empirical validation across six real-world datasets.** The experiments (Figures 1–3) demonstrate that the WGM-based methods consistently match or outperform existing baselines. Particularly notable is the k-hitting set result where WGM-then-peeling actually outperforms the known-domain private greedy baseline (which assumes public knowledge of the full union).

- **Simplicity and scalability.** The paper contrasts WGM's simplicity with more complex sequential methods (Policy Gaussian, Policy Greedy), and the experimental results show WGM obtains MM within 5% of these methods despite their significantly higher computational cost — a practically useful finding.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Baseline comparison for set union has an objective mismatch.** The Policy Gaussian (Gopi et al., 2020) and Policy Greedy (Carvalho et al., 2022) baselines were designed and tuned for maximizing cardinality (ℓ₀), not minimizing missing mass (ℓ₁). The paper's central claim that WGM is "competitive with or outperform[s] existing baselines" on missing mass (Figure 1) could partly reflect this objective mismatch rather than a fundamental algorithmic advantage. The paper transparently notes prior work focused on cardinality, but does not tune the baselines for MM or discuss how much of the gap is attributable to objective mismatch. A fairer comparison would at minimum include the baselines with alternative hyperparameter settings that might improve their MM performance.

- **Gap between upper and lower bounds for top-k and k-hitting set.** Theorem 4.3 gives an upper bound with a √k term (from the known-domain peeling mechanism), while the lower bound (Corollary 4.4) scales linearly in k. The paper acknowledges this gap only briefly in Section 6 ("closing these gaps is a natural problem") without discussing which side is likely improvable or whether the gap is fundamental. Since the theoretical analysis is a core contribution, a more substantive discussion would help readers assess the tightness of the results.

- **Missing dataset statistics.** The paper repeatedly cites maxᵢ|Wᵢ| as a key