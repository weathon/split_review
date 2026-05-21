Now I have all verification done. Let me produce the final consolidated review.

---

## Summary

This paper introduces a missing-mass perspective for differentially private domain discovery. For set union, it proves that the Weighted Gaussian Mechanism (WGM) achieves a near-optimal ℓ₁ missing mass guarantee on Zipfian data (matching lower bound up to polylogs) together with a distribution-free ℓ∞ guarantee. It then uses the ℓ∞ bound as a generic domain-discovery primitive, composing WGM with known-domain algorithms to obtain new utility guarantees for unknown-domain top-k and k-hitting set. Experiments on six datasets show WGM-based methods are broadly competitive with existing baselines.

## Strengths

1. **First absolute utility guarantees for DP set union.** Theorem 3.3 provides a high-probability ℓ₁ missing-mass upper bound for WGM under Zipfian data, and Theorem 3.5 gives a lower bound showing the dependence on ε and N is tight. Prior work (Desfontaines et al., 2022; Chen et al., 2025) only gave relative guarantees. This is the central novel contribution.

2. **Distribution-free ℓ∞ missing mass guarantee (Theorem 3.6).** This holds for any dataset without Zipfian assumptions and is the key enabler for the downstream applications. The modular framing — run WGM, then apply a known-domain algorithm — is clean and practically useful.

3. **New unknown-domain guarantees for top-k and k-hitting set.** Theorems 4.3 and 4.5 provide missing-mass guarantees for top-k and an approximation guarantee for k-hitting set that depends on log(M) (actual items) rather than log(|𝒳|) as in prior known-domain work. Corollaries 4.4 and 4.6 give matching lower bounds showing k/ε dependence is unavoidable under Assumption 1.

4. **The parametrized MMₚ framework (Equation 1)** unifies cardinality (p=0), ℓ₁ (p=1), and ℓ∞ (p=∞) objectives, giving a clean mathematical structure that enables a single analysis to yield both the ℓ₁ and ℓ∞ results.

5. **Competitive empirical trends across six datasets.** Figures 1–3 show WGM-based methods match or outperform baselines on set union, top-k, and k-hitting set, including settings where WGM+top-k beats the only prior unknown-domain algorithm (Durfee & Rogers, 2019).

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Empirical evaluation is too thin to fully support the performance claims.** All reported results average only 5 trials. Figures 1 (set union) and 2 (top-k) display no variance information whatsoever. For a stochastic process involving Gaussian noise, Gumbel noise, and subsampling, trial-to-trial variability could be substantial enough to affect method rankings, especially where curves are close. Only Figure 3 reports standard error. The paper's claim that WGM methods "obtain strong empirical utility" is directionally supported but not conclusively demonstrated. This is an evidential weakness, not a structural one — the conclusions may be correct, but the current evidence (5 trials, no error bars on primary results) is insufficient to rule out high variance.

2. **The abstract overstates the "near-optimal" claim.** The abstract (line 19) says WGM has a "near-optimal ℓ₁ missing mass guarantee on Zipfian data." The actual Theorem 3.5 only shows tightness for the ε and N dependence; the lower bound is constructed on a dataset where max_i|W_i|=1, so it does not capture the (max_i|W_i|/√q^*)^{(s-1)/s} factors present in the upper bound. The paper's own qualified statement after Theorem 3.5 — "the dependence of ε and N in our upper bound … can be tight" — is more precise. The abstract should reflect this qualification.

3. **No comparison to the most recent competing method (Chen et al., 2025).** Chen et al. (2025) is cited in related work and described as "dominating the WGM (albeit by a small margin, empirically)," but it is not included as a baseline in any experiment. Even a brief comparison on a single dataset would strengthen the paper's claim that WGM is "competitive."

4. **"Uniform" baseline in Figure 2 is unexplained in the text.** The Figure 2 legend includes a "Uniform" method (purple line), but Section 5.2's baseline description (lines 303–307) only describes the limited-domain algorithm variants. The Uniform baseline appears without definition or motivation.

### Trivial

- The x-axis labels in Figures 2 and 3 list values "0, 25, 50, 100, 150, 175, 200" which is inconsistent with the text's stated k ∈ {5, 10, 20, 50, 100, 200}. This appears to be a plotting artifact.
- The ℓ₁ missing mass results for top-k are described in a single sentence ("Plots in Appendix F.2 demonstrate similar trends") but shown only in the appendix. Since ℓ₁ missing mass is the paper's main objective, including these in the main text would strengthen presentation.

## Nice-to-Haves

- A brief practical discussion of how to choose Δ₀ when max_i|W_i| is unknown, e.g., using a small fraction of the privacy budget for a rough estimate via a truncated Gaussian mechanism, or simply adopting a fixed default (as the experiments do) with a comment on graceful degradation. The current discussion (lines 155–158) assumes public knowledge of max_i|W_i|, which may not hold in the motivating setting.
- Runtime comparisons. The introduction motivates WGM as scalable, but no wall-clock times are given. A simple table would support this claim.

## Removed Points

- The harsh critic's note about "no error bars" for Figures 1 and 2 is kept as a real weakness (Minor). The "only 5 trials" concern is also kept.
- The harsh critic's comment about "Figure 3 does indicate standard error" is acknowledged but doesn't negate the criticism — Figures 1 and 2 still lack it.
- The harsh critic's "Section-by-Section Notes" section contains general commentary that is not structured as weaknesses; actionable points from it are absorbed above.
- The Strength Finder's strength about "competitive empirical performance" is kept but qualified by the experimental weakness above — the evidence is directionally supportive, not conclusive.

## Novel Insights

None beyond the paper's own contributions. The key insight — that missing mass (an ℓ₁ objective) is a more tractable lens than cardinality for DP set union, and that the ℓ∞ variant of this perspective enables a clean "discover-then-apply" modularity — is the paper's own doing, not something emergent from the reviews.

## Suggestions

1. Increase the number of trials to at least 20–30 per setting and add error bars (standard error or 95% confidence intervals) to Figures 1 and 2. This is the single highest-leverage improvement.
2. Tone down the "near-optimal" claim in the abstract to match what is actually proved: tight dependence on ε and N, with a gap in the max_i|W_i|/√q^* factor.
3. Add a comparison to Chen et al. (2025) on at least one dataset, or clearly explain why it is omitted.
4. Define the "Uniform" baseline in the Figure 2 caption or the main text.
5. Move the ℓ₁ top-k missing-mass results (currently Appendix F.2) to the main text, or at minimum add a sentence summarizing the trend.

## Score and Decision

**Calibration summary (all anchors retrieved across rounds):**

| Path | Avg Score | Round | Comparison to this paper |
|---|---|---|---|
| /home/wg25r/review_agent/human_reviews_2026/XgdVHwpgNA.md | 2.50 | R1 (low) | Much weaker — DPBloomfilter had flawed methodology and poor evaluation |
| /home/wg25r/review_agent/human_reviews_2026/FmLGEJEvJ9.md | 3.00 | R1 (low) | Weaker — DP string distances, limited contribution |
| /home/wg25r/review_agent/human_reviews_2026/lXioFCPhcp.md | 3.00 | R1 (low) | Weaker — domain unlearning, not comparable topic or rigor |
| /home/wg25r/review_agent/human_reviews_2026/SWA4zSrv6R.md | 3.00 | R1 (low) | Weaker — attack paper, different contribution type |
| /home/wg25r/review_agent/human_reviews_2026/ldYKqmtLm5.md | 5.00 | R1/R2 | Weaker — DP-OPH had limited novelty (straightforward RR+OPH) and thin technical depth; this paper has stronger theory |
| /home/wg25r/review_agent/human_reviews_2026/gIaAuu8UZZ.md | 6.50 | R1/R2 | Slightly stronger — turnstile streams paper is polished, clean contribution, accepted as poster; this paper has similar theoretical novelty but weaker experiments |
| /home/wg25r/review_agent/human_reviews_2026/vSXIEbTVhE.md | 4.00 | R1/R2 | Weaker — ULDP censoring paper had a fundamental privacy flaw identified by reviewers |
| /home/wg25r/review_agent/human_reviews_2026/KAy7mlYIrm.md | 4.00 | R1 | Weaker — domain adaptation, unrelated topic |
| /home/wg25r/review_agent/human_reviews_2026/vrlj7anjeq.md | 4.00 | R2 | Weaker — Rao DP definitional paper with limited empirical support |
| /home/wg25r/review_agent/human_reviews_2026/6rvpzYGNOn.md | 5.00 | R2 | Weaker — Accuracy-First RDP criticized as "illustrative rather than substantive"; this paper has more concrete results |
| /home/wg25r/review_agent/human_reviews_2026/KmMEQOtXAy.md | 7.20 | R2 | Stronger — clustering paper, different subfield, but cleaner evaluation |
| /home/wg25r/review_agent/human_reviews_2026/17h5Sl2EaK.md | 7.00 | R2 | Stronger — distributed clustering, more thorough evaluation |
| /home/wg25r/review_agent/human_reviews_2026/sOpAa8iR0A.md | 6.80 | R2 | Stronger — coresets paper, polished theory+experiments |

**Round-1 bracket:** Between 4.0 and 7.0 (the paper is clearly stronger than the 3.0 anchors and the 4.0–5.0 DP papers, but below the 7.0+ clustering papers which are in different subfields).

**Round-2 narrowing:** The most directly comparable DP-theory anchors are DP-OPH (5.0, weaker — this paper has more novel theory), Accuracy-First RDP (5.0, weaker — same assessment), and turnstile streams (6.5, slightly stronger due to clearer evaluation). The paper sits between 5.5 and 6.5. It is clearly above 5.0 (stronger theory, first absolute guarantees, matching lower bounds) but below 6.5 (experiments need strengthening, framing needs correction).

**Final score:** 6.0. The theoretical contributions are genuinely novel and significant — first absolute utility guarantees for a well-studied problem, matching lower bounds, clean ℓ∞ extension with downstream applications. The empirical evaluation is the weak point: 5 trials with no error bars on the primary results is insufficient to fully back the empirical claims. The abstract's "near-optimal" framing slightly overreaches what the theorems prove. Both issues are fixable in revision. The paper should be accepted on the strength of its theoretical contributions, with the expectation that the experimental concerns will be addressed.

**Decision:** Accept.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>