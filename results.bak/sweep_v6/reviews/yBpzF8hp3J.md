Now I have all the context I need. Let me write the final consolidated review.

## Summary

This paper studies differentially private domain discovery, reframing the set union problem in terms of *missing mass* (ℓ₁ fraction of unrecovered item mass) rather than cardinality. The authors prove that the Weighted Gaussian Mechanism (WGM) achieves near-optimal ℓ₁ missing mass guarantees on Zipfian data (Theorem 3.3), with a matching lower bound (Theorem 3.5), and a distribution-free ℓ∞ missing mass bound (Theorem 3.6). They then use WGM as a domain-discovery front-end for known-domain top-k and k-hitting set algorithms, obtaining the first provable utility guarantees for those problems in the unknown-domain setting. Experiments on six real-world datasets compare WGM-based methods against existing baselines.

## Strengths

- **First absolute utility guarantees for DP set union.** The paper is the first to prove absolute (not relative) utility guarantees for DP set union (Section 1.1, line 41). This fills a long-standing gap in the literature.

- **Near-optimal ℓ₁ missing mass bound with matching lower bound.** Theorem 3.3 gives a high-probability upper bound on missing mass for WGM under a (C,s)-Zipfian assumption. Corollary 3.4 shows the dependence on ε and N matches the lower bound in Theorem 3.5 up to logarithmic factors, establishing near-optimality.

- **Distribution-free ℓ∞ missing mass guarantee.** Theorem 3.6 bounds MM_∞ without any distributional assumption on the data, and the paper cleanly uses this bound as a building block for downstream tasks (top-k, k-hitting set) without requiring Zipfian conditions.

- **First provable guarantees for unknown-domain top-k and k-hitting set.** Theorems 4.3 and 4.5 give explicit utility bounds for these problems using WGM as a domain-discovery precursor. The k-hitting set result is the first such guarantee in the unknown-domain setting, and the matching lower bounds (Corollaries 4.4, 4.6) confirm that the linear k/ε term is unavoidable under Assumption 1.

- **Empirical advantage on top-k and k-hitting set.** Figures 2 and 3 show consistent gains: the WGM-based method achieves lower top-k missing mass than limited-domain baselines across three small datasets, and on k-hitting set it even surpasses a known-domain private greedy algorithm that assumes public knowledge of the full item set — because WGM produces a smaller, higher-quality domain.

## Weaknesses

### Major

- **Set union experiments compare only on missing mass without reporting cardinality.** The baselines (Policy Gaussian, Policy Greedy) were designed to maximize cardinality; the paper evaluates them only on missing mass, the metric WGM is tailored for. The paper acknowledges the trade-off ("sequential methods often output ≈2X more items"), but without cardinality results the reader cannot assess whether WGM's competitive missing mass (within 5%) comes at a substantial cost in unique items recovered. Reporting cardinality alongside missing mass would clarify the operating characteristics of each method and is necessary to fully support the claim that WGM is "competitive with" the baselines.

- **The ℓ₁ missing mass guarantee requires a Zipfian (s>1) assumption.** Theorem 3.3 only holds for (C,s)-Zipfian data with s>1. The paper is transparent about this, but the practical relevance is weakened: there is no guidance on how to verify whether a given dataset is Zipfian, or what to do if it is not. The ℓ∞ bound (Theorem 3.6) is distribution-free but only bounds the maximum missing frequency, not the total missing mass — a much weaker object for downstream analysis.

- **The k-hitting set experiments lack a valid unknown-domain private baseline.** The paper compares against a non-private greedy algorithm and a known-domain private greedy algorithm that assumes public knowledge of the full union — neither is a valid unknown-domain private algorithm. While the paper acknowledges this, the lack of a meaningful private baseline reduces the strength of the empirical demonstration for k-hitting set.

### Minor

- **The top-k bound (Theorem 4.3) contains a log(M) term where M = |∪ᵢ Wᵢ|.** When M is large (comparable to N), this term can dominate, and the paper does not discuss when the bound is meaningful. A brief discussion of regimes where the bound is tight vs. weak would be helpful.

- **The lower bounds (Theorems 3.5, Corollaries 4.4, 4.6) apply only to algorithms satisfying Assumption 1 (output is subset of input).** Many practical algorithms may not satisfy this (e.g., they may generate synthetic items), so the lower bounds' applicability to broader DP settings is limited. This is not discussed explicitly.

- **No WGM-only baseline for top-k.** The two-stage algorithm (WGM + peeling exponential mechanism) is compared against limited-domain baselines, but a simple WGM-only baseline (output the WGM domain directly as the top-k set) would help isolate the benefit of the second stage.

### Trivial

- None.

## Nice-to-Haves

- Cardinality results for set union (number of unique items recovered as a function of Δ₀ and ε).
- A scatterplot or Pareto-style visualization of the missing-mass vs. cardinality trade-off for WGM and the policy methods.
- A synthetic non-Zipfian dataset experiment to validate the distribution-free ℓ∞ guarantee.
- An analysis of whether the six real datasets are approximately Zipfian, with estimated C and s parameters.
- Practical guidance on choosing Δ₀ without a priori knowledge of maxᵢ|Wᵢ|.

## Removed Points

These were flagged by the reviewers but are removed or downgraded with justification:

- **"Set union comparison is fundamentally unfair and invalidates the paper's central empirical claim"** — The paper claims WGM is *competitive with* (not uniformly better than) the baselines on missing mass, and it shows this. The paper transparently acknowledges the cardinality trade-off. The criticism overstates the issue; the real gap is the omission of cardinality results, which is already listed as a Major weakness above.

- **"No evaluation on cardinality invalidates conclusions"** — The paper's central contribution is a new theoretical framework (missing mass), and evaluating on that metric is natural. The absence of cardinality is a gap but does not invalidate the core theoretical claims. Kept as Major weakness, not fatal.

- **"The lower bound only applies to algorithms satisfying Assumption 1, limiting its applicability"** — This is a standard and transparent assumption in the unknown-domain literature; the paper explicitly adopts it. The criticism is valid but not novel or damaging — it's an inherent scope condition. Downgraded to Minor.

- **Strength Finder's generic strengths** — Removed generic statements like "the paper addressed an important problem" and "the problem is well-motivated." Only concrete, evidenced strengths are kept.

- **"ℓ₁ guarantee requires Zipfian assumption, limiting practical relevance"** — The paper is transparent about this and also provides the distribution-free ℓ∞ bound. Kept as a valid observation but as a Major weakness (not fatal) since the distribution-free alternative exists.

## Novel Insights

The harsh critic's framing of the set union comparison as "unfair" overlooks an interesting insight: the baseline Policy methods achieve higher cardinality by including low-frequency items, but these items contribute negligible missing mass. The paper implicitly reveals that on real data, the vast majority of the item mass is captured by high-frequency items that are easy to discover privately. This suggests that for many practical applications where total item coverage matters more than unique-item diversity (e.g., identifying the most popular search queries), WGM may indeed be the right tool, and the missing mass perspective is the correct evaluation lens. The cardinality-oriented baselines are paying a high computational cost to recover low-frequency items of little practical value under the mass-weighted objective. This tension — cardinality vs. mass — is an important design consideration that the paper surfaces but does not fully explore.

## Suggestions

1. **Add cardinality results for set union** (Section 5.1). Report the number of unique items recovered by all methods alongside the missing mass results. This single addition would address the most significant weakness in the evaluation.

2. **Include a simple WGM-only baseline for top-k** (Section 5.2). Passing the WGM domain directly as the top-k output isolates the value added by the peeling exponential mechanism second stage.

3. **Discuss regimes where the log(M) term in Theorem 4.3 dominates and whether the bound remains meaningful.**

4. **Add a synthetic non-Zipfian experiment** to demonstrate the distribution-free ℓ∞ guarantee in action — even a simple uniform-frequency dataset would help validate Theorem 3.6 empirically.

5. **Provide practical guidance on estimating maxᵢ|Wᵢ| or choosing Δ₀** without relying on a priori public knowledge, perhaps leveraging the Zipfian bound maxᵢ|Wᵢ| ≤ (CN)^{1/s} from Lemma 3.1.

## Score and Decision

**Calibration anchors** (from the human-review corpus):

| Path | Avg Score | Comparison to current paper |
|------|-----------|---------------------------|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/HMe5CJv9dQ.md` | 7.50 | Stronger theory and more thorough experiments than the current paper. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/uqWM9hBDAE.md` | 7.33 | Cleaner problem framing and stronger empirical validation; current paper has more restrictive assumptions. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/fbqOEOqurU.md` | 7.00 | Similar level of theory contribution; current paper's experiments are weaker. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/yLhJYvkKA0.md` | 6.67 | Very comparable: both have solid theory with acknowledged practical limitations; similar overall quality. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/fj5SqqXfn1.md` | 5.00 | Current paper has substantially stronger theoretical novelty and originality. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/S6Dn3uyM2p.md` | 4.60 | Current paper is significantly stronger in both theory and experimental validation. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/NqkSUwMc0K.md` | 3.60 | Current paper is far more rigorous and complete; the blind model averaging paper suffered from fundamental correctness issues. |

The paper makes a genuine theoretical contribution — first absolute utility guarantees for DP set union, matching lower bounds, and clean extensions to top-k and k-hitting set. The main weakness is that the experimental evaluation has a notable gap (no cardinality comparison), but this does not undermine the theoretical claims. The paper is comparable in quality to the 6.67 anchor (hierarchical clustering with DP), which was accepted. The Zipfian assumption is a real limitation but is clearly scoped and partially mitigated by the ℓ∞ result.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>