Now I have sufficient calibration data. Let me write the final consolidated review.

**Round 1 bracket:** Based on calibration search, the paper sits between the weak anchors (~2.5-3.0, clearly reject-level DP papers) and the strong anchors (~7.5+, strong accept). The middle-band anchors (3.5-7.5) are most relevant. Initial bracket: **between 4.5 and 7.0**.

**Round 2 narrowing:** Inside the bracket, I examined:
- *Private Mechanism Design via Quantile Estimation* (avg 6.5, accept poster) — pure theory, no experiments, accepted
- *Near-Exact Privacy Amplification for Matrix Mechanisms* (avg 6.25, accept poster) — framework + experiments, missing formal guarantees
- *DP-BAI for Linear Bandits* (avg 7.0, accept poster) — tight theory + limited synthetic experiments
- *DP One Permutation Hashing* (avg 4.5, reject) — incremental techniques

The paper under review has stronger theoretical novelty than the 6.25 and 4.5 anchors, and comparable theory to the 6.5-7.0 anchors. Its experiments are on real data (stronger than DP-BAI's synthetic-only eval). The main issues (ambiguous "5%" claim, missing error bars in Figs 1-2) bring it slightly below the 7.0 anchor. Final score: **6.0**.

Here is the full review:

## Summary
This paper studies differentially private domain discovery through the lens of *missing mass*. It proves the first absolute utility guarantees for the Weighted Gaussian Mechanism (WGM) under the ℓ₁ missing mass objective on Zipfian data (near-optimal, Theorem 3.3) and under a distribution-free ℓ∞ missing mass objective (Theorem 3.6). It then applies WGM as a domain-discovery precursor for unknown-domain top‑k and k‑hitting set, obtaining novel utility guarantees (Theorems 4.3, 4.5) with matching lower bounds. Experiments on six real datasets show that WGM-based methods are competitive with or outperform existing baselines.

## Strengths

**1. First absolute utility guarantees for DP set union.** Section 1.1 correctly notes that prior work (Desfontaines et al., Chen et al.) only provided relative guarantees between mechanisms. The paper proves the first *absolute* high-probability upper bounds on missing mass for the WGM (Theorems 3.3, 3.6), which is a genuinely novel theoretical contribution.

**2. Near-optimal ℓ₁ missing mass bound with matching lower bound.** Theorem 3.3 gives a high-probability upper bound on ℓ₁ missing mass for Zipfian datasets, and Theorem 3.5 gives a matching lower bound (up to logarithmic factors) showing that the dependence on ε and N is essentially tight. The Zipfian parameterization (Definition 3.1) cleanly captures the intuition that datasets with faster frequency decay permit stronger guarantees.

**3. Distribution-free ℓ∞ missing mass guarantee and clean downstream applications.** Theorem 3.6 bounds ℓ∞ missing mass for *any* dataset (no Zipfian assumption), and Theorems 4.3 and 4.5 extend this to obtain the first utility guarantees for unknown‑domain top‑k and k‑hitting set. The meta-algorithm (WGM + known-domain mechanism with budget splitting) is simple yet principled.

**4. Competitive empirical results on real data.** The experiments span six datasets across multiple domains. The k‑hitting set experiments (Figure 3) include standard error bars, and the top‑k experiments (Figure 2) show a clear advantage over the limited‑domain baseline across all tested k values. The code is provided in the supplement.

## Weaknesses

### Major

**1. Ambiguous "within 5%" claim contradicting the figure description (Section 5.1, Figure 1).** The text (line 291) states "the WGM obtains MM within 5% of that of the policy mechanisms." However, the figure's alt text describes WGM as dropping to a "low value" while policy mechanisms "remain relatively high" across all Δ₀ values — which would imply WGM is substantially *better* (lower MM), not close. If WGM's MM is meaningfully lower, the "within 5%" wording is incorrect (underrating the method). If the figure description is inaccurate, the caption needs correction. Either way, the central empirical claim of Section 5.1 needs clarification. Since MM is lower-is-better, the paper would be stronger by simply stating the actual observed gap rather than using ambiguous phrasing.

**2. No error bars in Figures 1 and 2.** The set union experiments (Figure 1) and top‑k experiments (Figure 2) report only averages over 5 trials without any indication of variance. With only 5 trials, the stability of comparisons is unclear. Figure 3 does include standard error bars, so the authors were aware of this best practice — Figures 1 and 2 should follow the same convention.

### Minor

**3. Imperfect k‑hitting set baseline comparisons.** Section 5.3 includes a known‑domain private greedy baseline that the authors themselves acknowledge "is not a valid private algorithm in the unknown domain setting" (line 319). While the authors are transparent about this limitation, including a properly private unknown‑domain baseline (even a simple one) would strengthen the evaluation. The meta-algorithm's advantage — that using a WGM-discovered domain makes the subsequent selection problem easier — is demonstrated indirectly, but an ablation comparing WGM‑discovered domains to the true union (non‑private domain knowledge) would directly validate this claimed benefit.

**4. No empirical comparison to Chen et al. (2025).** The paper cites Chen et al.'s adaptive weighting approach as "dominant" over WGM but does not compare against it empirically. Given the paper's emphasis on WGM competitiveness, including this comparison (even on a subset of datasets) would strengthen the empirical claims.

### Trivial

None.

## Nice-to-Haves
- An ablation isolating the effect of WGM domain discovery (e.g., compare to running the downstream algorithm on the true union as the domain) would directly validate the ℓ∞ bound's practical value.
- Brief runtime or scalability numbers would support the claimed advantage of WGM's simplicity over policy mechanisms.

## Removed Points
- **"Severe mismatch ... evaluation is untrustworthy" (Harsh Critic #1):** The critic's framing that the "central empirical claim is contradicted" overstates the issue. The text says WGM is "within 5%" of policies (conservative, underselling WGM if the gap is larger). The figure description suggests WGM is better. The text and figure don't contradict on *whether* WGM is competitive — they differ on *how much better* it is. This is an ambiguity needing clarification, not a fatal contradiction. I have downgraded this to a Major weakness with a precise description of the actual ambiguity.
- **"No comparison to adaptive weighting approach of Chen et al. (2025)" (Harsh Critic, Missing Parts):** This is a valid suggestion but not a fundamental weakness since Chen et al. is a contemporary work. I moved it to Minor weakness #4.
- **"Baseline configurations for top‑k may not be fairly tuned" (Harsh Critic #3):** The paper actually *does* describe the hyperparameter choices (k̃ ∈ {k, 5k, 10k, ∞}) and follows the original paper's recommendations for Δ₀. The comparison asymmetry (full budget for baseline, split budget for WGM-based method) favors the baseline, not the proposed method — if anything, this makes the WGM method's advantage more convincing, not less. Removed.
- **"Lower bounds are simple information-theoretic arguments" (Harsh Critic):** The lower bounds (Corollaries 4.4, 4.6) are indeed derived from Lemma D.1 (from the set union lower bound), but this is standard practice for corollaries and does not constitute a weakness.
- **"ℓ∞ bound can be weak when max_i|W_i| is large" (Harsh Critic):** This is a known property of the bound, not an oversight. All utility bounds degrade with problem complexity parameters. Removed as not a weakness.
- **Strength Finder's generic strengths** (e.g., "addressed an important problem"): Removed as too generic. Only specific, evidence-grounded strengths retained.

## Novel Insights
The most striking finding across the reviews is that the paper's theory is consistently judged as solid and novel, but the experimental narrative has a clarity gap. The figure description for Figure 1 paints a picture of WGM dominating policy mechanisms (low MM vs. high MM), yet the text describes WGM as merely "within 5%." This tension suggests the paper may be underselling its own empirical results — a rare problem. Typically, authors overclaim; here, the opposite may be happening. The real question for the reader is whether WGM is competitive with (similar performance, "within 5%") or superior to (much lower missing mass) the policy mechanisms. Either outcome is favorable for the paper's thesis, but the ambiguity undermines confidence in the experimental reporting.

## Suggestions
1. Clarify the "within 5%" claim in Section 5.1. If WGM's MM is substantially lower than the policy mechanisms, say so directly and report the actual gap. If the gap is truly <5%, provide a corrected figure or explanation.
2. Add error bars or confidence intervals to Figures 1 and 2. With only 5 trials, even ±1 standard error would greatly improve interpretability.
3. Include an ablation comparing WGM‑discovered domains against the true union as the domain, to directly validate the ℓ∞ bound's practical benefit for downstream tasks.

## Score and Decision

### Calibration Anchors
| Paper | Path | Avg Score | Round | Comparison |
|-------|------|-----------|-------|------------|
| Privately Counting Partially Ordered Data | hVTaXJ0I5M.md | 6.75 | R1 | Theory-heavy DP paper with novel sampler; accepted poster. The current paper has stronger experimental evaluation but more presentation ambiguity in figures. Similar tier. |
| DP One Permutation Hashing | ODzT43I5lJ.md | 4.50 | R1 | Incremental technique (randomized response applied to OPH); rejected. The current paper has far deeper theoretical novelty and real-data experiments, clearly stronger. |
| Near-Exact Privacy Amplification | txV4dNeusx.md | 6.25 | R2 | Framework + experiments, but lacked formal guarantees for Monte Carlo estimates; accepted poster. Comparable: both have novel contributions with some empirical gaps. |
| Optimality of Matrix Mechanism (ℓₚ) | fbqOEOqurU.md | 7.00 | R2 | Tight theory paper extending known framework to new metric; accepted poster. The current paper's contributions are more application-grounded (domain discovery) with broader scope. |
| DP-BAI Fixed Budget | vrE2fqAInO.md | 7.00 | R2 | Tight upper/lower bounds for DP bandit problem; accepted poster. The current paper has more extensive real-data experiments but the DP-BAI paper's experimental presentation is cleaner. |
| Private Mechanism Design via Quantile Estimation | JQQDePbfxh.md | 6.50 | R3 | Pure theory (no experiments), accepted poster. The current paper has both theory and experiments, comparably strong. |
| Avoiding Pitfalls for Privacy Accounting | fj5SqqXfn1.md | 5.00 | R1/R2 | Clarifying paper with practical guidance; rejected (split reviews). The current paper's theoretical novelty is substantially greater. |

**Final score rationale:** The paper's theoretical contributions (first absolute utility guarantees, near-optimal ℓ₁ bound, ℓ∞ bound, downstream applications) are genuinely novel and well-supported, placing it above the 4.5–5.0 rejected anchors. The experiments use real data and show the method is competitive. The main shortcoming is an ambiguous empirical claim (the "within 5%" vs. figure description inconsistency) and missing variance information in two of three figures. These issues are addressable but prevent the paper from reaching the 6.5–7.0 tier of the cleanest theory papers. The paper is comparable to the 6.25-level accepted anchors.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>