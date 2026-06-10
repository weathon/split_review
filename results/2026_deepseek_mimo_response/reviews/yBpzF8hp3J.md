## Summary
This paper proves the first absolute utility guarantees for differentially private set union by reframing the objective in terms of "missing mass" (the fraction of total item-frequency not captured by the output) rather than cardinality. The main results show that the simple Weighted Gaussian Mechanism (WGM) achieves near-optimal ℓ₁ missing mass on Zipfian data (Theorem 3.3, with matching lower bound Theorem 3.5) and a distribution-free ℓ∞ missing mass guarantee (Theorem 3.6). These set-union guarantees are then used as a domain-discovery precursor for known-domain algorithms for top-k selection and k-hitting set, yielding new utility guarantees for these unknown-domain variants (Theorems 4.3, 4.5). Experiments on six real-world datasets validate that WGM-based methods are competitive with or outperform existing baselines.

## Strengths
- **First absolute utility guarantees for DP set union (Theorems 3.3, 3.5, Corollary 3.4):** Prior work (Desfontaines et al. 2022, Chen et al. 2025) only proved relative/competitive guarantees. The paper proves that WGM's ℓ₁ missing mass on (C,s)-Zipfian data scales as Õ(C^{1/s}/(s−1) · (max_i|W_i|/(εN√q*))^{(s−1)/s}), and provides a matching information-theoretic lower bound (Theorem 3.5) showing this ε and N dependence is tight up to logarithmic factors, establishing near-optimality of the simple WGM.
- **Distribution-free ℓ∞ missing mass guarantee (Theorem 3.6):** Unlike the ℓ₁ result, this bound does not require the dataset to be Zipfian, broadening its applicability. This is the key technical bridge enabling the downstream top-k and k-hitting set utility guarantees without distributional assumptions.
- **Novel utility guarantees for top-k and k-hitting set in the unknown domain setting:** Theorem 4.3 provides a top-k missing mass bound that degrades gracefully with k and is meaningful for all ε > 0. Theorem 4.5 provides a (1−1/ε) multiplicative approximation for k-hitting set. Lower bounds (Corollaries 4.4, 4.6) show the linear k/ε dependence is unavoidable for Assumption 1-compliant algorithms. The finding that WGM-based domain discovery can outperform known-domain private greedy (Section 5.3) is noteworthy — WGM produces a smaller, higher-quality domain.
- **Clean unifying p-norm framework (Equation 1):** The generalization MM_p(W,S) = ‖(N(x)/N)_{x∉S}‖_p elegantly connects missing mass (p=1), max-missing-frequency (p=∞), and cardinality (p=0).
- **Simple, practical algorithm design:** WGM (Algorithm 1) has only three stages (subsample, weight, threshold), and the meta-algorithm (Algorithm 2) runs WGM for domain discovery then applies a known-domain algorithm.
- **Empirical validation across six datasets with strong baselines:** WGM obtains missing mass within 5% of the Policy Gaussian and Policy Greedy mechanisms (Section 5.1). For top-k (Figure 2), WGM-based method consistently outperforms limited-domain baselines. For k-hitting set (Figure 3), the method matches or beats baselines that are not fully private in the unknown-domain setting.

## Weaknesses

### Fatal
None.

### Major
- **The (1−1/ε) multiplicative approximation factor in Theorem 4.5 is vacuous for ε ≤ 1:** At ε = 1 (the privacy budget used in all experiments, line 273: "total privacy budget of (1, 10^{-5})-DP"), the guarantee reads Hits(W,S) ≥ (1−1)·Opt(W,k) − error = −error, which is trivially satisfied since hits are non-negative. The guarantee only becomes informative for ε > 1 (ε=2 gives 50% approximation). The paper does not acknowledge this limitation — Section 6 only notes that "upper and lower bounds for top-k and k-hitting set do not match" without noting the specific regime issue. Since the experiments show strong performance at ε = 1 (Section 5.3), there is an unexplained gap between theory and practice for the k-hitting set contribution. This does not invalidate the paper's core set-union contribution or the top-k results (which are meaningful for all ε > 0), but the k-hitting set theoretical result as presented overstates its practical applicability.

### Minor
- **Missing mass vs. cardinality metric context for set-union baseline comparisons:** The baselines (Policy Gaussian from Gopi et al. 2020, Policy Greedy from Carvalho et al. 2022) were designed and tuned to minimize cardinality-based error. Evaluating them under missing mass — a different objective — could inherently favor WGM's thresholding mechanism. The paper partially acknowledges this (line 281: "This contrasts with previous empirical results for cardinality, where sequential methods often output ≈2X more items"), but does not explicitly discuss that each baseline was optimized for a different native objective. A brief paragraph clarifying the relationship between the two metrics would strengthen the paper's positioning.

### Trivial
None.

## Nice-to-Haves
- A brief runtime comparison between WGM and the policy baselines would be useful given scalability is a stated advantage (Section 5.1).
- Brief guidance on setting Δ₀ in practice; the experiments fix Δ₀ = 100 without detailed justification.
- Additional experiments at larger ε values (e.g., ε = 2, 5) for k-hitting set would bridge the theory-practice gap.
- Cardinality-based experimental results as supplementary would give readers a complete picture across metrics.

## Removed Points
These points are flagged to be removed, treat them with caution.
- **Typo on line 261 (q^ε instead of q*):** This is a parser artifact; the paper correctly uses q* in all other occurrences (lines 131, 145, 161, 229, 255). Not an author error.
- **Only 5 trials reported:** The trends are consistent across datasets and standard errors are reported. Sufficient for the claims made.
- **Computational complexity not discussed:** This is a nice-to-have rather than a core weakness.

## Novel Insights
The paper's most novel insight is that reframing DP set union in terms of missing mass rather than cardinality unlocks the first absolute utility guarantees for this well-studied problem. The matching upper and lower bounds (Theorems 3.3 vs. 3.5) establish that the Weighted Gaussian Mechanism — despite its simplicity and existing deployment — is essentially information-theoretically optimal under this metric. The distribution-free ℓ∞ bound (Theorem 3.6) then serves as a clean bridge to downstream applications, demonstrating that domain discovery via WGM enables provable unknown-domain algorithms. The finding that WGM-based domain discovery can produce a higher-quality domain than the full private union (Section 5.3), causing the downstream k-hitting set to outperform even known-domain private greedy, is a practically insightful observation.

## Suggestions
- Clearly state that the (1−1/ε) approximation guarantee for k-hitting set is meaningful only for ε > 1, and discuss the gap between this regime and the ε = 1 experimental setting.
- Add a brief paragraph discussing the relationship between missing mass and cardinality metrics — clarifying that WGM is naturally suited to missing mass while sequential methods are optimized for cardinality — and how this affects interpretation of the experimental comparisons.
- Consider providing experiments at larger ε values for k-hitting set to demonstrate when the theoretical guarantee becomes informative.

## Calibration Report

**All retrieved anchors:**

Round 1 (bracketing):
- "Nonlinear Inference Learning for Differentially Private Massive Data" (avg 2.50) — weak DP paper, limited contribution. Much weaker than our paper.
- "Advancing DP through Synthetic Dataset Alignment" (avg 2.50) — weak DP paper. Much weaker.
- "Differentially Private Federated k-Means" (avg 3.00) — rejected, limited contribution. Much weaker.
- "D2P2-SGD" (avg 3.00) — rejected, incremental. Much weaker.
- "Differentially Private One Permutation Hashing" (avg 4.60) — rejected, straightforward DP technique without utility analysis. Our paper is clearly stronger.
- "On the Price of DP for Hierarchical Clustering" (avg 6.67) — accepted, upper/lower bounds + experiments. Similar structure but our paper has better bound matching for the core problem.
- "Optimality of Matrix Mechanism on ℓ_p^p-metric" (avg 7.00) — accepted, tight bounds for DP linear queries. Our paper has comparable tightness with cleaner presentation and more applications.
- "Avoiding Pitfalls for Privacy Accounting" (avg 5.00) — rejected, narrower contribution. Our paper is stronger.
- "How much of my dataset did you use?" (avg 7.60) — accepted, different topic (data usage inference).
- "Privacy-Preserving In-Context Learning" (avg 8.00) — accepted, different topic.
- "The Hidden Cost of Waiting" (avg 8.00) — accepted, different topic.
- "On the Hölder Stability of GNNs" (avg 8.00) — accepted, different topic.

Round 2 (narrowing):
- "Privately Counting Partially Ordered Data" (avg 6.75) — accepted, novel DP algorithm + experiments. Criticized for dense presentation. Our paper is clearer and more comprehensive.
- "Near-Exact Privacy Amplification for Matrix Mechanisms" (avg 6.25) — accepted, narrower contribution. Our paper is broader and stronger.
- "Efficiently Computing Similarities to Private Datasets" (avg 7.50) — accepted, novel algorithms + theory + experiments. Similar breadth. Our paper's first-absolute-guarantees contribution is stronger, but the k-hitting set weakness is notable. Comparable overall.
- "On the Price of DP for Hierarchical Clustering" (avg 6.67) — retrieved again in Round 2, same comparison as above.

**Round 1 bracket:** 6 to 8

**Round 2 narrowing:** The paper is clearly above the 6.25–6.75 anchors (better presentation, more comprehensive results, matching bounds for the core problem). It is comparable to the 7.00 anchor ("Optimality of Matrix Mechanism") — both prove tight bounds for a DP problem, but our paper extends to more applications and has empirical validation. It is slightly below the 7.50 anchor ("Efficiently Computing Similarities") due to the vacuous k-hitting set guarantee at ε = 1.

MY FINAL SCORE: <score>7</score>
MY FINAL DECISION: <decision>Accept</decision>