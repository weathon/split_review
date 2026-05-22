Now I have all the information I need to verify the claims against the paper. Let me produce the final consolidated review.

## Summary

The paper studies differentially private domain discovery, providing theoretical utility guarantees for the Weighted Gaussian Mechanism (WGM) on set union, then applying it as a precursor for unknown-domain variants of top-\(k\) selection and \(k\)-hitting set problems. The key contributions are: (1) near-optimal \(\ell_1\) missing mass bounds for DP set union under Zipfian data (Theorems 3.3 and 3.5), (2) a distribution-free \(\ell_\infty\) missing mass guarantee (Theorem 3.6), and (3) new utility guarantees for unknown-domain top-\(k\) and \(k\)-hitting set that depend on \(\log(M)\) (unique items) rather than \(\log(|\mathcal{X}|)\) (full universe). Experiments on six real-world datasets show the WGM-based methods are competitive with or outperform existing baselines.

## Strengths

1. **First absolute utility guarantees for DP set union.** Theorem 3.3 gives a high-probability upper bound on the \(\ell_1\) missing mass of the WGM for Zipfian data, and Theorem 3.5 provides a matching lower bound (up to logarithmic factors) showing near-optimality in the core parameters \(\epsilon, N, C, s\). As stated in Section 1.1, all prior guarantees for DP set union were relative to other algorithms, making these the first absolute bounds in the literature.

2. **Novel distribution-free \(\ell_\infty\) missing mass guarantee.** Theorem 3.6 bounds the \(\ell_\infty\) missing mass of the WGM without any Zipfian assumption, using only dataset parameters. This guarantee serves as the technical foundation for the unknown-domain top-\(k\) and \(k\)-hitting set results (Theorems 4.3, 4.5), enabling utility bounds under minimal distributional assumptions.

3. **New utility guarantees for unknown-domain top-\(k\) and \(k\)-hitting set.** Theorems 4.3 and 4.5 provide the first provable guarantees for these problems when the domain is unknown. The additive error depends on \(\log(M)\) (unique items actually present) rather than \(\log(|\mathcal{X}|)\) as in prior known-domain work (Mitrovic et al., 2017) — a strict improvement when the universe is large relative to the data.

4. **Lower bounds establishing tightness.** Theorem 3.5 shows the \(\epsilon\) and \(N\) dependence in the set union upper bound is tight for Zipfian data. Corollaries 4.4 and 4.6 prove a \(\frac{k}{\epsilon}\) term in the additive error for top-\(k\) and \(k\)-hitting set is unavoidable under Assumption 1.

5. **Empirical validation on diverse real-world datasets.** Figures 1–3 evaluate the methods on six datasets spanning different scales and domains. The WGM-based methods are shown to be competitive with or outperform prior sequential baselines (Policy Gaussian, Policy Greedy) for set union, and outperform the limited-domain baseline for top-\(k\) selection. On \(k\)-hitting set, the method even outperforms the non-private greedy algorithm on two datasets.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Quantitative claim in Section 5.1 inconsistent with plotted results.** The text states that *"Across datasets, we find that the WGM obtains MM within 5% of that of the policy mechanisms."* This phrasing suggests WGM's missing mass is at most 5% worse (or 5% different) from the policy mechanisms. However, in Figure 1, WGM performs substantially *better* than the policy mechanisms on two of three datasets: on Reddit at \(\Delta_0=50\), WGM ≈ 0.18 vs. Policy ≈ 0.35 (a ~49% relative difference); on Movie Reviews, WGM ≈ 0.03 vs. Policy ≈ 0.12 (a 75% relative difference). Only on Amazon Games are the values plausibly close. The text understates WGM's relative advantage and does not accurately describe the plotted data. This does not harm the paper's conclusions (if anything, the results are stronger than claimed), but it is factually inconsistent and should be corrected.

2. **The \((1 - 1/\epsilon)\) approximation factor in Theorem 4.5 is a parsing artifact.** The statement reads \((1 - 1/\epsilon)\text{Opt}(W,k)\), which for \(\epsilon \leq 1\) gives a non-positive factor. This is clearly meant to be \((1 - 1/e)\) — the standard approximation factor for the greedy algorithm on submodular maximization, matching Mitrovic et al. (2017). The authors should verify the typesetting in the camera-ready version.

### Trivial
None.

## Nice-to-Haves

- **Ablation on privacy budget split.** The combined algorithms (Algorithm 2) assume an equal split of the privacy budget between the WGM domain-discovery step and the downstream mechanism. The paper does not experimentally explore the trade-off of allocating different fractions of the budget to each stage.

- **ℓ₀ bound sensitivity analysis.** The experiments vary \(\Delta_0\) for set union (Figure 1), but the top-\(k\) and \(k\)-hitting set experiments fix \(\Delta_0 = 100\). An ablation of this parameter for the downstream tasks would give a fuller picture.

## Removed Points

These points were raised by reviewers but are not included as weaknesses in the final review. They are listed here for completeness and should be treated with caution.

1. **Privacy accounting for combined algorithms (Critic's Critical Issue 1).** The critic argued that Theorems 4.3 and 4.5 do not halve \(\epsilon\) for each component and therefore the claimed \((\epsilon,\delta)\)-DP does not follow. **This criticism is incorrect.** The paper's Section 4 (lines 177–181) explicitly states that the budget is split. The asymptotic expressions \(\sigma = \Theta(\frac{1}{\epsilon}\sqrt{\log(1/\delta)})\) and \(\lambda = \Theta(\sqrt{k}/\epsilon)\) absorb constant factors (including the halving) via \(\Theta\) notation — \(\Theta(2/\epsilon) = \Theta(1/\epsilon)\). The \(\delta/2\) subscripts on \(T\) and \(\lambda\) confirm that \(\delta\) is halved for each component. The theorems are technically correct as stated.

2. **"Limited-Delta" vs "limited-domain" labeling.** The figure description parser renders the baseline label as "Limited-Delta" while the text (Section 5.2) describes it as "the limited-domain mechanism." This is either a parser artifact from figure OCR or a trivial labeling choice; it does not affect interpretability.

3. **"Near-optimal" claim for Zipfian guarantees.** The critic noted the lower bound (Theorem 3.5) does not incorporate the same \(\max_i|W_i|\) and \(q^*\) dependencies as the upper bound (Theorem 3.3). The paper's use of "near-optimal" refers to the core parameters \((\epsilon, N, C, s)\), which do match; the dependency on algorithmic parameters \((\max_i|W_i|, q^*)\) in the upper bound is a separate artifact of the mechanism. This is standard for the area and not a substantive weakness.

4. **Request for comparison with Chen et al. (2025).** The critic suggested including Chen et al. (2025)'s adaptive weighting method, which claims to dominate WGM empirically. The paper acknowledges this work in the related work section and notes it in future directions (Section 6). Its omission from experiments is justified by its very recent publication date and the fact that the paper's focus is on *absolute* (not relative) guarantees.

5. **Other speculations** about missing lower bounds, missing ablations, and format/style nitpicks were removed per the filtering guidelines.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- Correct the quantitative claim in Section 5.1 to accurately reflect that WGM substantially *outperforms* the policy baselines (not "within 5% of" them), since the plotted data show WGM achieving much lower missing mass on most datasets.
- Fix the parser artifact in Theorem 4.5: \((1 - 1/\epsilon)\) should be \((1 - 1/e)\).
- Consider adding an ablation varying the privacy budget split ratio in the Meta Algorithm (Algorithm 2) to validate the design choice of equal splitting.

## Score and Decision

The paper makes solid theoretical contributions — the first absolute utility guarantees for DP set union, a distribution-free \(\ell_\infty\) bound, and new guarantees for unknown-domain top-\(k\) and \(k\)-hitting set. The lower bounds establish near-optimality for core parameters. The experiments are thorough and support the claims. The major privacy accounting concern raised by one reviewer is factually incorrect (the asymptotic notation absorbs the budget split). The only verified weakness is a minor textual overstatement that actually understates the paper's empirical results. This is a strong paper with well-supported contributions.

MY FINAL SCORE: <score>8.0</score>
MY FINAL DECISION: <decision>Accept</decision>