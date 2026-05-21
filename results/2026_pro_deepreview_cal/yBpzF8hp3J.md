Now I have a clear picture. Let me now write the consolidated final review.

---

## Summary

This paper studies differentially private domain discovery, reframing the objective in terms of *missing mass* (the fraction of items not recovered, weighted by frequency). It proves the first absolute utility guarantees for DP set union: an ℓ₁ missing-mass upper bound for the Weighted Gaussian Mechanism on Zipfian data (Theorem 3.3), a near-matching lower bound (Theorem 3.5), and a distribution-free ℓ∞ guarantee (Theorem 3.6). These results are then applied to obtain new utility guarantees for DP top-k and k-hitting set in the unknown-domain setting. Experiments on six real-world datasets confirm that the WGM-based methods are competitive with or outperform existing baselines.

## Strengths

- **First absolute utility guarantees for a core DP primitive.** The paper proves the first provable bounds on missing mass for DP set union — a problem deployed in industrial DP frameworks (Plume, OpenDP). The upper bound (Theorem 3.3) and matching lower bound (Theorem 3.5) together establish tight dependence on ε, N, and the Zipfian tail parameter s (up to factors depending on maxᵢ|Wᵢ|). This fills a recognized gap: prior work on DP set union lacked absolute utility guarantees.

- **Clean theoretical architecture with downstream impact.** The distribution-free ℓ∞ bound (Theorem 3.6) serves as a building block that enables new provable algorithms for DP top-k (Theorem 4.3) and DP k-hitting set (Theorem 4.5) when the domain is unknown. For k-hitting set, the guarantee depends on log M (true distinct items) rather than log |𝒳| (universe size), improving over known-domain bounds. Lower bounds (Corollary 4.4, Corollary 4.6) establish that the ε-dependence in the additive error is unavoidable.

- **Strong empirical validation.** Experiments on six diverse real-world datasets (Reddit, Amazon Games, Movie Reviews, Steam Games, Amazon Magazine, Amazon Pantry) demonstrate that WGM-based methods are competitive. For set union, WGM achieves missing mass within 5% of the more computationally expensive sequential baselines (Figure 1). For top-k, the proposed method consistently obtains smaller missing mass than all limited-domain baselines, with the advantage growing in k (Figure 2). For k-hitting set, the method matches or outperforms baselines that assume public domain knowledge (Figure 3).

- **Transparent proof structure.** The analysis of Theorem 3.3 cleanly separates the error from subsampling (Lemma C.2) and noisy thresholding (Lemma C.4) while guaranteeing high-frequency items survive both stages (Lemma C.3). This decomposition yields explicit dependence on Δ₀, N, and Zipfian parameters, and directly informs practical parameter choices.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Near-optimality claim needs qualification.** The paper states that WGM has "near-optimal ℓ₁ missing mass on Zipfian data" (abstract, §1, §3.2). However, the upper bound (Theorem 3.3 / Corollary 3.4) contains a factor maxᵢ|Wᵢ|^{(s-1)/s}, which by Lemma 3.1 can be as large as N^{(s-1)/s²}. This makes the N-dependence in the upper bound decay more slowly than the lower bound's N^{-(s-1)/s}. The near-optimality holds when maxᵢ|Wᵢ| is bounded by a constant (e.g., single-item-per-user), but the paper should explicitly state this qualification rather than leaving it implicit. The lower bound Theorem 3.5 is proved under a construction where maxᵢ|Wᵢ| = 1, so the gap is real.

- **Missing error bars in set union and top-k figures.** Figures 1 and 2 report averages over 5 trials without any indication of variability (standard error or confidence bands). Given that 5 trials is a small number, the absence makes it difficult to assess whether the observed differences (e.g., WGM within 5% of Policy Gaussian) are statistically meaningful. Figure 3 for k-hitting set does include standard error bars, so the omission in Figures 1 and 2 is inconsistent.

- **Imprecision in novelty framing.** The paper states it is "the first to prove absolute utility guarantees for DP set union" (§1.1). Desfontaines et al. (2022) provide absolute (not relative) guarantees for the single-item-per-user setting, which the paper does acknowledge (line 39: "restricted setting where each user contributes a single item"). The framing could be slightly misleading to a reader who misses this distinction. The genuine novelty — first absolute *missing-mass* guarantees, especially in the multi-item setting — should be stated more precisely.

### Trivial

- The paper gives asymptotic forms for σ and T (Θ(·), Θ̃(·) notation in §3.1) without providing explicit constants or a concrete recipe for practitioners to choose parameters from ε, δ, Δ₀.

## Nice-to-Haves

- A brief remark on the computational cost of WGM versus the sequential baselines (Policy Gaussian, Policy Greedy) would complement the qualitative statement about scalability and help readers understand the practical trade-off.

- Explicit, non-asymptotic parameter settings for σ and T (beyond the asymptotic forms in §3.1) would improve reproducibility for practitioners.

- A short discussion of how the gap between the upper and lower bounds could be narrowed (e.g., by tighter analysis of the subsampling step, or by a stronger lower bound incorporating maxᵢ|Wᵢ|) would strengthen the theory section.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh critic point about Δ₀ = ∞ making the limited-domain baseline non-private.** The criticism is factually incorrect. The limited-domain mechanism from Durfee & Rogers (2019) operates on a known, bounded domain D of size k̃. In this setting, each user can contribute at most 1 to any item's count, so the L2 sensitivity of the count vector is bounded by √k̃ regardless of Δ₀. The domain constraint itself provides the sensitivity bound; Δ₀ = ∞ does not break the DP guarantee. The paper's experimental setup is valid.

- **Strength Finder point about "first absolute utility guarantees."** Already covered as a retained strength, but merged with the minor weakness about imprecise framing.

- **Harsh critic's characterization of Desfontaines et al. as providing "absolute bounds on detection as a function of true frequency."** This is partially conflated — the Desfontaines et al. guarantees are for a different setting (single-item-per-user) and different metric (cardinality-based, not missing mass). The paper already acknowledges the restricted setting. The harsh critic's framing that this is a fatal or major novelty issue is overstated. Demoted to minor.

- **Harsh critic's demand for runtime/scalability reporting.** While nice-to-have, this is a theory-focused paper and the absence of runtime experiments is not a weakness by the standards of this community.

## Novel Insights

The reviews surface an interesting tension: the paper's upper bound depends on maxᵢ|Wᵢ| while the lower bound is proved under maxᵢ|Wᵢ| = 1. This reveals that the tightness of the analysis depends on whether per-user item counts are large. For settings where each user contributes few items (common in practice), the bounds are essentially tight; for settings with heavy users, there is a genuine gap. This observation points to a natural open problem: either strengthen the lower bound to incorporate maxᵢ|Wᵢ|, or improve the upper bound analysis to eliminate the dependence on it.

## Suggestions

- Qualify the near-optimality statement (e.g., "near-optimal when per-user item counts are bounded by a constant") and briefly note the gap due to maxᵢ|Wᵢ| in the discussion after Theorem 3.3.
- Add error bars (even simple standard-error bands over the 5 trials) to Figures 1 and 2 for consistency with Figure 3.
- Rephrase the novelty claim in §1.1 to explicitly highlight missing mass and the multi-item setting as the key differentiators from Desfontaines et al. (2022).

## Score and Decision

**Calibration anchors used:**

| Paper | Avg Score | Round | Comparison |
|---|---|---|---|
| DP One Permutation Hashing (S6Dn3uyM2p) | 4.60 | R1 (low) | Clearly weaker: lacks theoretical utility guarantees, limited novelty |
| How Much is Unseen (uqWM9hBDAE) | 7.33 | R1 (mid) | Similar domain (missing mass) but non-private; our paper has more comprehensive theory |
| Privately Counting Partially Ordered Data (hVTaXJ0I5M) | 6.75 | R2 (narrow) | Our paper is stronger: more impactful problem, tighter bounds, better experiments |
| Efficiently Computing Similarities to Private Datasets (HMe5CJv9dQ) | 7.50 | R2 (narrow) | Roughly comparable: both provide solid DP theory with empirical validation; our paper has tighter lower bounds but narrower scope |

**Round 1 bracket:** 6.0 – 8.0 (well above the 3.0–4.6 weak anchors; plausibly near the 7.33 "How Much is Unseen" anchor)

**Round 2 narrowing:** The 6.75 anchor (partially ordered counting) is clearly weaker — its contributions are narrower (a faster sampler for one mechanism), its experiments are incomplete, and its novelty is contested by reviewers. The 7.50 anchor (DP similarities) is the closest comparator: both papers provide theoretical improvements over prior work, cover multiple problem variants, and include solid experiments. Our paper has slightly cleaner theoretical architecture (matching lower bounds) and addresses a more fundamental DP primitive (set union is a building block for industrial DP systems), but has a narrower scope (domain discovery vs. general similarity queries).

**Final score: 7.5.** The paper makes a clear, well-supported contribution: it introduces missing mass as an objective for DP domain discovery, proves the first absolute utility guarantees (upper and matching lower bounds) for a deployed DP primitive, extends the results to top-k and k-hitting set, and validates everything on real data. The weaknesses are minor and addressable (imprecise phrasing, missing error bars, unqualified near-optimality claim). This is a strong accept.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>