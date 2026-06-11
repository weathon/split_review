## Summary

This paper studies differentially private domain discovery through the lens of "missing mass" (the fraction of item mass not recovered). It proves absolute utility guarantees for the Weighted Gaussian Mechanism (WGM) on set union under a Zipfian data assumption (ℓ₁ missing mass) and without distributional assumptions (ℓ∞ missing mass). Lower bounds show near-optimal dependence on ε and N. These results are extended to unknown-domain variants of top-k and k-hitting set. Experiments on six datasets show WGM-based methods are empirically competitive.

## Strengths

1. **First absolute (non-relative) utility guarantees for DP set union.** Prior work (Desfontaines et al., Chen et al.) gives guarantees relative to other algorithms; this paper provides high-probability bounds on missing mass directly in terms of dataset parameters (C, s, N, ε). (Lines 29–31)

2. **Lower bounds demonstrating near-optimal ε and N dependence.** Theorem 3.5 gives an Ω((1/(εN))^{(s-1)/s}) lower bound for any (ε,δ)-DP algorithm satisfying Assumption 1, matching the upper bound in ε and N. Similar lower bounds are extended to top-k (Corollary 4.4) and k-hitting set (Corollary 4.6).

3. **Distribution-free ℓ∞ missing mass guarantee (Theorem 3.6).** Unlike the ℓ₁ bound, this requires no Zipfian assumption, enabling distribution-free guarantees for downstream top-k and k-hitting set applications. This is a clean theoretical bridge.

4. **First utility guarantees for unknown-domain DP k-hitting set.** Theorem 4.5 provides a (1−1/e)-approximation with additive error depending on log(M) rather than log(|𝒳|), improving on Mitrovic et al. (2017). (Lines 263, 309)

5. **The ℓp missing mass framing (Equation 1) unifies prior objectives.** Setting p=0 recovers cardinality, p=1 is standard missing mass, and p=∞ corresponds to minimizing the maximum missing mass. This provides conceptual clarity.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Figure 3 caption does not match the described baselines (k-hitting set).** The text (lines 309–310) describes two baselines: "the non-private greedy algorithm and the private non-domain algorithm from Mitrovic et al. (2017)." The figure caption (lines 319–321) lists "DP-Top-k," "DP-Top-k with Pay-What-You-Get," and "Random Selection" — three names that do not appear in the text description, and "Random Selection" is entirely unexplained. This makes it difficult for a reader to understand exactly what was compared. Since the k-hitting set experiments are secondary to the theoretical contributions, this is a presentation issue rather than an evidential one, but it should be fixed.

2. **The "within 5%" quantitative claim (line 281) is not backed by error bars.** The set union results (Figure 1) and top-k results (Figure 2) are reported as averages over only 5 trials without error bars or confidence intervals. The paper makes a precise quantitative claim ("within 5%") based on these averages, but the reader cannot assess the variability. By contrast, Figure 3 does show standard errors, making the inconsistency noticeable. The claim should either be softened or supported with uncertainty measures.

3. **The upper and lower bounds for set union have a gap in max_i|W_i|.** Corollary 3.4's upper bound depends on (max_i|W_i|/(εN√q*))^{(s-1)/s} while Theorem 3.5's lower bound depends on (1/(εN))^{(s-1)/s}. The paper correctly states that the "dependence on ε and N can be tight" (line 149), but the abstract's "near-optimal" slightly overstates the tightness across all parameters. The gap is acknowledged in the Future Directions section, but the reader should be aware the bounds are tight only in ε and N, not in max_i|W_i| or related quantities.

### Trivial

1. Line 253: "(1 - 1/ε)" is a parser artifact; it should read "(1 - 1/e)" (the standard (1−1/e) approximation factor for submodular maximization). This is clear from context but should be corrected.

2. The k-hitting set experiments use only ε=1 in the main paper (ε=0.1 is in the appendix). The paper acknowledges this and says results are "not significantly qualitatively different." This is fine but worth noting.

## Nice-to-Haves
- Provide error bars or confidence intervals for the set union and top-k experiments (Figures 1–2), not just for k-hitting set (Figure 3).
- Add a brief remark about when the ℓ∞ bound (Theorem 3.6) becomes less informative (i.e., when max_i|W_i| is large relative to N).

## Removed Points

These points from the input reviews are removed after verification; treat them with caution if encountered elsewhere.

- **"Inconsistency between described k-hitting set baselines is an evidential issue":** Demoted to Minor. The mismatch between text and caption is a presentation problem, not an evidential one. The experimental comparison is clearly secondary to the theoretical contributions.

- **"The distribution-free ℓ∞ bound has hidden dependence on dataset difficulty":** Removed. The bound's dependence on max_i|W_i| is explicitly stated in Theorem 3.6. Using "distribution-free" to mean "no distributional (Zipfian) assumption required" is standard terminology. The paper is not hiding anything.

- **"Only one privacy budget"**: Removed. The paper explicitly states the appendix contains ε=0.1 experiments and that results are "not significantly qualitatively different." This is standard practice.

- **"Large datasets trivially easy for top-k"**: Removed. The paper honestly reports this and shifts focus to small datasets where results are informative.

- **"k-hitting set baselines are weak"**: Removed. The paper explicitly acknowledges there are no existing private algorithms for unknown-domain k-hitting set and honestly describes baseline limitations (line 309: "Note that the latter baseline is not a valid private algorithm in the unknown domain setting"). This is transparency, not a weakness.

- **All missing-appendix, missing-related-work, and reproducibility nitpicks**: Removed per filtering rules (parser artifacts or speculative, not author errors).

- **Generic strengths from Strength Finder** (e.g., "addresses an important problem"): Removed as generic/superficial.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions
- Align the Figure 3 caption with the text description of baselines and explain "Random Selection" if it remains.
- Add standard errors or confidence intervals to Figures 1 and 2, or soften the "within 5%" claim.
- Consider adding a brief remark about regimes where the ℓ∞ bound is meaningful vs. less informative (large max_i|W_i|).

---

## Calibration

### Round 1 — Bracketing
Initial bracket: **5.5 – 7.5**. The paper is clearly stronger than weak anchors (2.5–3.0 on unrelated DP applications) and clearly weaker than highly polished papers on unrelated topics (7.6–8.0). The relevant DP theory anchors sit at 4.6–7.0.

### Round 2 — Narrowing

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| "Optimality of Matrix Mechanism on ℓ_p^p-metric" | fbqOEOqurU.md | 7.00 | R1, R2 | **Comparable.** Both are DP theory with upper/lower bounds. The Matrix Mechanism paper has tighter bounds but less practical motivation; our paper has clearer practical significance but looser bounds and minor presentation issues. |
| "On the Price of DP for Hierarchical Clustering" | yLhJYvkKA0.md | 6.67 | R1, R2 | **Comparable.** Both are DP theory + experiments with some assumptions limiting scope. Our paper has cleaner motivation and broader application scope. |
| "Privately Counting Partially Ordered Data" | hVTaXJ0I5M.md | 6.75 | R1, R2 | **Comparable.** Both present mechanisms with theoretical guarantees + experiments. Our paper addresses a broader set of problems. |
| "Fixed-Budget DP Best Arm Identification" | vrE2fqAInO.md | 7.00 | R2 | **Slightly stronger.** This paper has matching upper/lower bounds and tighter results, though on a more specialized problem. |
| "Differentially Private Range Subgraph Counting" | FZS5m1cbFU.md | 5.67 | R2 | **Clearly weaker.** This paper was rejected due to concerns about novelty vs. technique adaptation. Our paper has clearer novelty. |
| "Private Mechanism Design via Quantile Estimation" | JQQDePbfxh.md | 6.50 | R2 | **Slightly weaker.** Narrower scope, less practical impact. |
| "Differentially Private One Permutation Hashing" | S6Dn3uyM2p.md | 4.60 | R1 | **Clearly weaker.** More incremental contribution. |

### Final Score Determination
The paper is comparable to accepted DP theory papers in the 6.5–7.0 range. It is clearly stronger than papers scoring ≤5.67. The theoretical contributions (first absolute guarantees, near-optimal ε/N dependence, distribution-free ℓ∞ bound, extensions to top-k and k-hitting set) are solid and well-motivated. All weaknesses are confined to presentation (figure/text mismatch, missing error bars on some experiments) rather than the theoretical core. The upper/lower bound gap, while acknowledged, slightly tempers the "near-optimal" claim. Overall, this is a solid contribution that should be accepted with minor revisions.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>