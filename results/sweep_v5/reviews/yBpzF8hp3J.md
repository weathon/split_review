Now I have all the information needed to write the final review. Let me compile it.

## Summary

This paper studies differentially private domain discovery, focusing on set union, top-k, and k-hitting set problems where the domain is unknown. The main contributions are: (1) proving the first absolute utility guarantees (in terms of missing mass) for DP set union using the Weighted Gaussian Mechanism (WGM), including near-optimal ℓ₁ bounds on Zipfian data and distribution-free ℓ∞ bounds; (2) extending these guarantees to unknown-domain variants of top-k and k-hitting set via a simple meta-algorithm that runs WGM for domain discovery then applies a known-domain algorithm; and (3) empirical validation on six real-world datasets showing the WGM-based methods are competitive with or outperform existing baselines.

## Strengths

- **First absolute utility guarantees for DP set union.** The paper is the first to prove high-probability bounds on missing mass (rather than relative comparisons) for DP set union. Theorem 3.3 provides an ℓ₁ bound for Zipfian data, and Theorem 3.6 provides a distribution-free ℓ∞ bound. Prior work by Desfontaines et al. (2022) and Chen et al. (2025) only gave relative guarantees. (Section 1.1, lines 39-41)

- **Matching lower bound on ε and N dependence.** Theorem 3.5 proves an Ω lower bound for any private algorithm satisfying Assumption 1 on Zipfian data. The dependence on ε and N matches the upper bound in Corollary 3.4 (up to logarithmic factors), establishing near-optimality in those key parameters. (Section 3.2, lines 159-163)

- **New guarantees for unknown-domain top-k and k-hitting set.** Theorems 4.3 and 4.5 provide the first utility guarantees for these problems in the unknown-domain setting by using WGM as a domain-discovery precursor. The additive error depends on log(M) rather than log(|X|), improving over known-domain algorithms when |X| is huge. Corollary 4.4 provides a matching lower bound (up to polylog factors) for top-k. (Section 4, lines 235-247)

- **Empirical validation across diverse datasets.** Experiments on six real-world datasets (Reddit, Amazon Games, Movie Reviews, Steam Games, Amazon Magazine, Amazon Pantry) show that the WGM-based methods are competitive with or outperform existing baselines. The top-k results show consistent improvement over the limited-domain mechanism across all k values, and the k-hitting set results match or exceed even non-private baselines despite operating with less information. (Section 5, Figures 1-3)

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **"Near-optimal" claim is slightly overbroad.** The abstract claims "near-optimal ℓ₁ missing mass guarantee on Zipfian data," but the lower bound (Theorem 3.5) constructs a dataset where each user holds exactly one item (max_i|W_i| = 1), so it does not capture the max_i|W_i|/√q^* term appearing in the upper bound (Corollary 3.4). The paper's more precise statement (line 159, "the dependence of ε and N... can be tight") is accurate. The abstract should be qualified to clarify that the near-optimality is in the dependence on ε and N, not in all dataset parameters.

- **Privacy composition argument could be more explicit.** The paper states that the meta-algorithm "spend[s] half of the overall privacy budget" on each stage (lines 177-181) and the parameter choices in Theorems 4.3 and 4.5 use Θ notation with δ/2 subscripts (e.g., T = Θ̂_{Δ₀,δ/2}(max{σ,1}), λ = Θ̂_{δ/2}(√k/ε)). This is correct — the Θ notation absorbs the constant factor from the ε/2 budget split, and the δ/2 subscripts handle the δ split. However, a brief explicit verification that the composition of two (ε/2,δ/2)-DP mechanisms yields (ε,δ)-DP would improve clarity for readers less familiar with asymptotic notation.

- **Missing mass as sole evaluation metric for set union baselines.** For set union, the baselines (Policy Gaussian, Policy Greedy) were originally designed to maximize cardinality, not minimize missing mass. The paper reports only missing mass on these baselines. While the paper is transparent about this (and the baselines are the strongest known for the problem), reporting cardinality alongside MM would help readers assess whether the WGM's comparable MM comes at the cost of recovering fewer total items. This is a relatively minor concern given that WGM's MM is "within 5%" of the baselines.

### Trivial
None beyond standard presentation refinements.

## Nice-to-Haves

- For the top-k experiments, the legend in Figure 2 uses multiple "Limited-Delta" entries with different hyperparameter settings (k̃ ∈ {k, 5k, 10k, ∞}) — adding the specific k̃ values to the legend labels would improve readability.
- An ablation study on the privacy-budget split in the meta-algorithm (e.g., 50/50 vs. 75/25) would probe whether the symmetric split is necessary.
- A case study showing the domain size produced by WGM vs. the full union size for the k-hitting set experiments would help illustrate the benefit of domain discovery.

## Removed Points

These points were raised by one or both reviewers but are not included as weaknesses for the following reasons:

1. **Privacy composition for meta-algorithm not correctly specified (Harsh Critic Critical Issue 1):** REMOVED — This criticism is factually incorrect. The critic claims the parameters use full (ε,δ) when they should use half, but (a) σ = Θ(1/ε √log(1/δ)) has the same asymptotic form for both (ε,δ) and (ε/2,δ/2) because Θ absorbs constant factors; (b) T and λ explicitly use δ/2 subscripts (Θ̂_{Δ₀,δ/2}, Θ̂_{δ/2}). The composition is correctly handled. The presentation could be more explicit, which is retained as a Minor weakness above.

2. **Experimental comparisons unfair because baselines designed for different metrics (Harsh Critic Critical Issue 3):** REMOVED — This is speculative ("it is possible that baselines would achieve better MM if tuned differently"). The paper is transparent about all baseline settings and does not claim WGM outperforms on set union (it says "within 5%"). On top-k, the limited-domain method is the only existing unknown-domain algorithm, and comparing on MM is legitimate. The concern about missing cardinality results is retained as a Minor weakness above.

3. **Missing error bars in figures (Harsh Critic):** REMOVED — The parser strips visual elements (error bars, legend labels) from figures; this is a PDF extraction artifact, not a paper flaw. The paper text for Figure 3 states it plots "standard error across 5 trials."

4. **Figure 2 legend uses "Limited-Delta" repeatedly with no differentiation (Harsh Critic):** REMOVED — Parser artifact. The paper text (lines 305-306) explains each variant uses a different k̃, and the original PDF likely labels them distinctly.

5. **Missing related works:** REMOVED per instructions — as meta-reviewer I cannot confirm existence of missing references.

6. **Lemma 4.2's bound not proven for top-k missing mass (Harsh Critic):** REMOVED — The paper states the proof "appears in Appendix C.3" and "similar upper bounds for other performance metrics have also been derived." The appendix is stripped by the parser.

7. **Theorem 3.3 is hard to parse (Harsh Critic):** REMOVED — Complexity of bounds is inherent to the problem's multi-parameter nature, not a flaw in the paper.

## Novel Insights

None beyond the paper's own contributions. Both the harsh critic and strength finder reaffirm the paper's stated contributions without identifying contradictions or hidden patterns not already presented by the authors.

## Suggestions

1. Qualify the "near-optimal" claim in the abstract to say "near-optimal in its dependence on ε and N" rather than the current unqualified phrasing.
2. Add one sentence in Section 4 explicitly verifying that plugging (ε/2,δ/2) into Theorem 3.2 and Lemma 4.1 yields the stated asymptotic parameter expressions.
3. Report cardinality alongside missing mass for the set union experiments (Figure 1) to help readers evaluate whether the MM comparison fully captures the trade-offs.

## Score and Decision

**Calibration anchors (all retrieved, non-exhaustively read):**

| Anchor | Score | Comparison to current paper |
|--------|-------|-----------------------------|
| `uxFme785fq` (DP + BLB inference) | 2.50 | Much weaker — trivial contributions, no real theory. Current paper is far superior. |
| `S6Dn3uyM2p` (DP OPH) | 4.60 | Weaker — straightforward application of DP to hashing, no deep theory. Current paper has stronger and more novel theoretical results. |
| `gG7P1SL0QS` (DP-SGD analysis) | 3.20 | Weaker — unclear contributions, speculative analysis. Current paper's theory is rigorous and well-supported. |
| `hkSjjs4o5d` (DP clustering) | 6.50 | Comparable — solid theory + experiments, accepted paper. Current paper has similar rigor and broader scope across three problems. |
| `hVTaXJ0I5M` (DP counting, partial orders) | 6.75 | Comparable — good theory + experiments, accepted. Current paper has similar structure and depth but addresses more problems. |
| `fbqOEOqurU` (Matrix mechanism optimality) | 7.00 | Comparable — tight bounds for linear queries, accepted. Current paper matches this level of theoretical rigor. |
| `HMe5CJv9dQ` (DP similarity computation) | 7.50 | Slightly stronger — more comprehensive theoretical developments. Current paper is comparable but slightly narrower in scope. |

The paper is a genuine theoretical contribution: it provides the first absolute utility guarantees for DP set union, establishes nearly matching lower bounds, and extends cleanly to two downstream problems. The weaknesses are minor (a slightly overbroad "near-optimal" claim in the abstract, and a composition argument that could be spelled out more explicitly) and do not threaten the core claims. The experiments, while not exhaustive, credibly demonstrate practical viability. The paper sits comfortably alongside accepted DP theory papers in the 6.5–7.5 range.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>