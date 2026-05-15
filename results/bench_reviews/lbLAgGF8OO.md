Now I have all the information I need. Let me synthesize the final review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal
### Major
### Minor
### Trivial

## Nice-to-Haves
## Removed Points
## Novel Insights
## Suggestions

## Score and Decision

Let me compose the review now.

---

Actually, first let me verify one more thing about the abstract claim. The abstract says "improving their regret bounds from T^{3/4} to T^{3/5} (on-policy) and from T^{5/6} to T^{7/8} (off-policy)" for average estimation error. Let me check if there's any other place in the paper where T^{3/5} or T^{7/8} appear.

I already grepped and confirmed these only appear in the abstract (line 19) and the introduction has garbled numbers. So the abstract's T^{3/5} and T^{7/8} are claimed as general results for "average estimation error minimization," while Table 1 shows T^{2/3} for bilinear classes (which is also an average estimation error setting). These are indeed inconsistent.

Now let me write the review.Now I have sufficient information. Let me construct the final consolidated review.

---

## Summary

This paper introduces Dig-DEC (dual Information Gain Decision-Estimation Coefficient), a model-free complexity measure that removes the optimism principle from earlier DEC/E2D frameworks and drives exploration purely through information gain. The authors show Dig-DEC is always no larger than optimistic DEC and can be much smaller. They instantiate this framework in both stochastic and hybrid MDPs, obtaining the first model-free regret bounds for hybrid MDPs with bandit feedback (resolving an open problem from [LWZ25]), and improving regret rates in the stochastic setting — including achieving √T for Bellman-complete MDPs. Two refined online function estimation procedures (unbiased estimator for average estimation error, refined two-timescale for squared error) are developed as technical tools.

## Strengths

- **Novel complexity measure Dig-DEC that can strictly improve on optimistic DEC (Theorem 13, Theorem 14):** The paper rigorously shows Dig-DEC ≤ o-dec + η and provides a concrete 3-armed bandit instance where optimistic DEC suffers Ω(√T) regret while Dig-DEC achieves O(1) regret. This demonstrates genuine conceptual advance over the prior optimistic DEC framework.

- **First model-free regret bounds for hybrid MDPs with bandit feedback (Section 5.2, Table 2):** The paper obtains sublinear regret for model-free learning in hybrid bilinear classes and Bellman-complete coverable MDPs with linear reward and bandit feedback. This addresses a problem left open by [LWZ25], whose model-free algorithm required full-information feedback.

- **Improved regret rates for Bellman-complete MDPs to √T (Table 1):** For Bellman-complete MDPs (bilinear, BE, coverable) in the stochastic setting, the paper achieves √T regret using the squared-error estimation procedure. This matches the performance of optimism-based approaches [JLM21, XFB⁺23] and is a significant improvement over the prior T^{5/6} rate from [FGQ⁺23].

- **Clean general framework unifying prior AIR-based approaches (Section 4, Algorithm 1):** The algorithm handles general divergences D via a new analysis that connects to mirror descent and avoids the restrictive "constructive minimax theorem" of prior work. This recovers results from [XZ23] and [LWZ25] with simpler analysis, and Est can even be made independent of log|Φ| for some settings.

- **Technically interesting estimation procedures (Section 4.2):** The unbiased product estimator (Algorithm 4) for average estimation error and the refined two-timescale posterior update (Algorithm 3) for squared error are well-motivated and could be of independent interest.

## Weaknesses

### Fatal

None.

### Major

- **Abstract consistently reports regret rates that do not match Table 1.** The abstract claims (line 19) that for average estimation error minimization the paper achieves regret T^{3/5} (on-policy) and T^{7/8} (off-policy). The introduction (line 39) further gives garbled rates (T^{3/2}/T^{5/6}) that appear to be parser-damaged. However, Table 1 reports T^{2/3} for both on-policy and off-policy bilinear classes (and BE, coverable) under average estimation error. T^{3/5} ≡ T^{0.6} is substantially better than T^{2/3} ≡ T^{0.667}; T^{7/8} ≡ T^{0.875} is substantially worse than T^{2/3}. The abstract and the main results table are not reconciled, and the reader cannot determine which rates the paper actually achieves without deriving them from scratch. This is a **presentation failure that obscures the paper's quantitative contribution** and must be fixed in revision.

- **Table 2 contains entries with superlinear T-exponents that are incompatible with the paper's core claims.** Specifically, the regret bounds listed for "bilinear on-policy" (T^{3/2}), "bilinear star on-policy with completeness" (T^{3/2}), and "coverable" (T^{3/2}) — along with "bilinear off-policy" (T^{13/8}) — are all superlinear, contradicting the claim of sublinear regret for hybrid MDPs. From the dig-dec entries and the stated regret decomposition (T·dig-dec + Est/η), the correct rates should be sublinear (e.g., T^{2/3} or similar). These exponents are almost certainly formatting/parsing errors, but **as printed, the table does not support the paper's central contribution claim**. This must be corrected.

### Minor

- **The claim of "resolving the main open problem left by [LWZ25]" is stated without necessary qualification in the abstract.** The paper itself acknowledges (Section 3, lines 121–123) that Assumption 3 excludes important cases (e.g., hybrid low-rank MDPs with unknown reward features) and that [LWZ25] had the same limitation even in the full-information case. The open problem resolution is therefore within the same assumption framework as [LWZ25], which is an honest contribution but should be qualified in the abstract to avoid overclaiming.

- **The derivation of Est bounds (Theorems 7, 11) and the dig-dec bounds for each concrete setting are relegated to the appendix.** While this is common practice for theory papers, the inconsistent rates in the main text make the absence of worked derivations more costly — the reader cannot easily verify the claimed rates from first principles.

- **The introduction's list of improvements (line 39) contains garbled exponents (T^{3/2}/T^{5/8} → T^{3/2}/T^{5/6}) that appear parser-damaged.** The T^{3/2} values cannot be regret exponents and should be corrected in revision.

### Trivial

- The dig-dec bound for "bilinear star on-policy with completeness" in Table 2 (entry $(H^5 d^4 \eta)^{1/2}$) appears to have a worse d-dependence than the corresponding entry without completeness ($(H^5 d^3 \eta)^{1/2}$). This seems counterintuitive and should be verified.
- Table 1/2 column formatting is difficult to parse due to garbled delimiters (e.g., $\log \Phi$ missing absolute-value brackets).

## Nice-to-Haves

- A brief sketch (1–2 paragraphs) in the conclusion on how Assumption 3 might be relaxed would improve completeness, as the paper already acknowledges this limitation.
- A worked example showing the explicit η optimization for one row of each table would help readers connect the dig-dec bounds to the final regret rates.
- High-probability bounds (mentioned briefly on page 8, line 278) are stated as possible but not given explicitly; presenting them in the tables would strengthen the paper.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh critic's point about "unfair comparison with other methods"**: Not present; no action needed.
- **Harsh critic's point about "missing proofs in appendix"**: The appendix is stripped by the parser — all proofs exist in the original submission. Removed per hard rule.
- **Harsh critic's point about "missing related works"**: Removed as the meta-reviewer cannot verify the existence or relevance of unmentioned works from external sources alone.
- **Strength Finder's claim that "improved online function estimation for average estimation error reduces Est from ~√T to ~T^{1/2}"**: These are the same rate (√T = T^{1/2}); the improvement is in the constant/bias, not the T-exponent. The text (line 219) correctly notes the improvement is in achieving an *unbiased* estimator rather than a *biased* one, which enhances η tuning. The Strength Finder's phrasing is misleading. Removed (moved here for context).
- **Strength Finder's claim about "coverability of diverse settings"** is generic; removed as superficial.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective not already present in the paper.

## Suggestions

1. **Reconcile the abstract with Table 1.** Provide a unified, consistent set of regret rates. If the abstract's T^{3/5} and T^{7/8} correspond to a different setting than the bilinear class shown in Table 1, this must be clearly stated. If Table 1 is correct, the abstract must be revised.
2. **Fix Table 2's exponents.** Ensure all regret bounds are sublinear. Provide corrected expressions or, if the pdf parsing introduced errors, include a note in the camera-ready version.
3. **Qualify the "resolved open problem" claim** in the abstract to reflect the assumptions (linear known-feature reward, Assumptions 3–4) under which the resolution holds.
4. **Add a supplementary table or worked example** showing the η optimization that yields each T-exponent from the dig-dec and Est bounds, so readers can verify rates independently.

## Score and Decision

### Calibration Anchors

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| `fE0RJto3Na.md` — Q-learning gap-dependent regret | 6.50 | Cleaner presentation, narrower scope. Current paper has more ambitious scope but worse presentation. |
| `kW0SudrQEQ.md` — Frozen Policy Iteration | 6.00 | Similar tier of theoretical contribution; this paper's ideas are comparably novel but the presentation issues are more severe. |
| `QEcSLhfOoQ.md` — Minimax Optimal Adversarial RL | 6.50 | Both resolve open problems in adversarial RL settings. The AD-FTRL paper has cleaner presentation and matching lower bounds. |
| `SoeTEnG7tY.md` — Hybrid CMAB | 3.50 | This paper's technical novelty is substantially greater than this incremental CMAB work. |
| `K42xtH1sqG.md` — Attacking CMABs | 2.67 | This paper's contributions are far more substantial. |

The paper makes genuine theoretical contributions — Dig-DEC is a conceptually clean improvement over optimistic DEC, and the first model-free hybrid MDP bounds with bandit feedback are a meaningful advance. However, the presentation contains unresolved inconsistencies between the abstract and Table 1, and Table 2 reports superlinear T-exponents that contradict the paper's own claims. These issues prevent the reader from reliably extracting the paper's quantitative results from the main text. While the underlying mathematics appears sound, the paper in its current form does not communicate its contributions clearly enough for acceptance.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>