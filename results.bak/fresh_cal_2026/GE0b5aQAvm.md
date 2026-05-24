Now I have a good calibration. Let me write the consolidated review.

**Round 1 Bracket**: From the bracketing search, weak anchors scored 2-3 (low quality papers with clear issues), middle anchors scored 4-5 (papers with significant weaknesses but some redeeming qualities), and strong anchors scored 8+ (strong accepts). I place this paper between 2.5 and 4.5.

**Round 2 Narrowing**: Anchors in the 3-4.5 range show papers with partial contributions but significant flaws. Most of these were rejected. Comparing specifically against the 3.33-scored "Neural Policy Iteration" paper (withdrawn) and the 4.0-scored "Policy transfer for LQR" paper (rejected), the current paper has more severe issues — unsupported central claims, contradictory experimental descriptions, and experiments that don't test stated hypotheses — placing it at the lower end of this band.

Here is my final consolidated review:

## Summary
This paper argues that neural policy ensembles are fundamentally inferior to linear policy ensembles, providing theoretical theorems (suboptimality, stability violation, convexity advantage) and empirical validation on linear and nonlinear control benchmarks. The core claim is that nonlinearity in policies breaks the beneficial averaging properties that linear ensembles enjoy.

## Strengths
1. **Convexity advantage result (Theorem 3 + Corollary 1):** The paper proves that for LQR systems with weighted-average cost, convex mixing with weights matching the cost weights achieves strictly lower cost than any non-convex mixing, with an explicit quadratic penalty term. This is a clean, potentially novel theoretical contribution that isolates a formal advantage of linear mixing over neural mixing (Section 3.3.1).

2. **Stability violation threshold (Theorem 2):** The theorem provides a computable condition (β > min α_i / (2 max ||V_i||_∞)) under which a neural ensemble can become unstable even when all component policies are individually stable. This gives a concrete, testable link between weight adaptation speed and instability (Section 3.2).

3. **Diversity-controlled experiments (Figure 3):** The systematic sweep over ensemble diversity δ shows the neural-linear performance gap remains large across all diversity levels, suggesting the suboptimality is not an artifact of a particular diversity setting (Section 4.5).

## Weaknesses

### Major
1. **Abstract's "2 orders of magnitude" claim is unsupported.** The abstract (lines 13, 19) claims neural ensembles underperform "often by 2 orders of magnitude" (i.e., ~100×). The actual empirical results show at most ~6-7× (647% relative loss on Pendulum in Figure 4) and typically ~1.85× (432.21 vs 234.06 in Figure 1). This is a factor of 2, not 100. This discrepancy between the paper's headline claim and the presented evidence is serious and undermines credibility.

2. **Claim that linear ensembles "guarantee stability" under varying weights is unproven and likely incorrect.** The Contributions section (line 31) states "a linear policy ensemble composed of stable linear policies guarantees stability; these results hold for varying rates of nonstationary change." This claim is not proven in the paper — Theorem 2 only proves instability for neural ensembles. Classical switched-systems results show that a convex combination of stable closed-loop matrices does **not** guarantee stability under time-varying weights; rapid switching between stable systems can cause instability. The paper provides no proof or reference to support this assertion. This is a core contribution claim that is not substantiated.

3. **Stability experiments do not test the stated claim.** Figure 4 compares a neural ensemble against a single "Linearized LQR" controller, not against a **linear ensemble**. The paper claims that linear ensembles are more stable than neural ensembles, but the experiment uses a single controller, not an ensemble. This experiment design does not test the hypothesis it is intended to validate.

4. **Figure 5 contains contradictory descriptions.** Panel (a) reports that "For Linear Systems, all methods perform similarly" while Panel (c) simultaneously reports a "Relative Performance Loss" of 166.1% for neural mixing on the same system. These cannot both be true: if all methods perform similarly, the relative loss should be near 0%. This inconsistency undermines the policy mixing experimental results. Furthermore, for Soft Pendulum, the figure description reports Neural Non-Convex Mixing has a higher mean episode count than Linear Convex Mixing (≈1500 vs ≈500), which would contradict the paper's claim that neural mixing is suboptimal.

### Minor
1. **Neural policy quality is not controlled.** Theorem 1 compares neural ensembles against optimal LQR policies. The paper provides no evidence that the trained neural policies are individually competitive with the optimal LQR policies — no learning curves, no per-policy cost comparisons, no hyperparameter search details. The observed suboptimality gap could stem from poor neural training rather than from the nonlinearity of the ensemble. The paper acknowledges the neural controller is "trained using gradient descent" (line 213) but gives no training details.

2. **Theorem 1 condition is stated without intuition.** The sufficient complexity condition L_f κ_0 δ > ρ is stated (line 111) without derivation or intuitive explanation in the main text. The reader cannot assess whether this condition is natural or restrictive without consulting the appendix.

3. **"vadDerPol" typo.** Line 293 refers to "vadDerPol systems" — appears to be a typo for van der Pol oscillator.

### Trivial
None beyond those noted above.

## Nice-to-Haves
- The paper could strengthen its case by verifying that neural policies are individually competitive with LQR policies before forming ensembles, then showing the gap emerges only when combining them.
- The stability experiments could be redesigned to compare neural and linear ensembles under time-varying mixing weights, directly testing the paper's claims about stability.
- Providing proof sketches or intuition for the conditions in Theorem 1 in the main text would improve readability.

## Removed Points
- **Criticism that Theorem 1 compares apples to oranges (neural vs linear ensembles):** This is what the paper is about — comparing neural and linear ensembles. The comparison is not "unfair" in principle; the issue is that individual policy quality is not controlled, which is already captured under Major weakness #1 (Minor tier converted up).
- **Criticism that Theorem 1 does not prove neural ensembles are inherently suboptimal:** The theorem proves Π^N is worse than Π^L under stated conditions, which is a form of suboptimality. The criticism overstates by claiming the theorem is "not a suboptimality result" — it is, but the interpretation needs the caveat about policy quality. This point is merged into Minor weakness #1.
- **Criticism about Theorem 3 conflating λ as cost weight and mixing weight:** The theorem explicitly uses λ in both roles, and its statement is logically consistent. The critic's concern that this "requires that the optimal mixing weight equals the cost weight λ" is actually what the theorem claims to prove for LQR, which may be mathematically valid. Removed because the critic did not demonstrate an actual error in the mathematical statement.
- **Criticism about "missing appendix" or "proofs not in main text":** Per instructions, appendix stripping is a parser artifact. Removed.
- **Strength Finder's generic strengths about "importance of the problem" and "well-tuned neural ensembles":** These are superficial without specific evidence. Removed.
- **Criticism about p-value not being explained:** The paper reports p < 10^{-5} and mentions specific tests. This level of detail is standard.
- **Criticism about no confidence intervals for single-run evaluation:** Large-scale RL benchmarks often report single-run evaluations; this is not a fatal flaw.

## Novel Insights
None beyond the paper's own contributions. The harsh critic raises a valid point that the linear ensemble stability guarantee is likely incorrect for time-varying weights (a subtle switched-systems issue that practitioners often overlook), but this is a critique, not a novel insight.

## Suggestions
1. **Correct the "2 orders of magnitude" claim** in the abstract and introduction to match the actual empirical results (~2-6×).
2. **Remove or properly qualify the claim that linear ensembles guarantee stability under time-varying weights.** Provide a proof or a reference, or explicitly scope the claim to fixed-weight ensembles only.
3. **Redesign the stability experiments** to compare neural ensembles against linear ensembles (not a single controller) under time-varying weights.
4. **Control for individual policy quality:** Show that neural policies are individually competitive with LQR policies before comparing ensembles. Provide learning curves and per-policy costs.
5. **Resolve the contradictions in Figure 5:** Clarify what "Relative Performance Loss" measures and explain the apparent inconsistency between panels (a) and (c). If Neural Non-Convex Mixing outperforms Linear Convex Mixing on Soft Pendulum, discuss this exception.
6. **Provide proof sketches** for Theorem 1's conditions in the main text so readers can assess whether they are natural or restrictive.

## Score and Decision

**Score: 3.0** — The paper tackles an interesting question and contains some potentially valid theoretical results (particularly Theorem 3). However, the core claims are overstated ("2 orders of magnitude"), an important stability claim about linear ensembles is unsubstantiated and likely incorrect, the stability experiments do not test the stated hypothesis, and there are internal contradictions in the empirical results. These problems are structural: fixing them would require substantial rewriting of claims and redesign of experiments. The paper in its current form does not meet the bar for acceptance.

**Decision: Reject**

**Calibration Anchors Referenced:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| /home/wg25r/review_agent/human_reviews_2026/2w4gHXaHK5.md | 2.00 | 1 (low) | Better — more theoretical ambition and structured experiments |
| /home/wg25r/review_agent/human_reviews_2026/qckiBWmodZ.md | 3.00 | 1 (low) | Similar — both have methodological gaps but this paper has a clearer thesis |
| /home/wg25r/review_agent/human_reviews_2026/9YIhV4pVKh.md | 2.00 | 1 (low) | Better — more interesting theoretical framing |
| /home/wg25r/review_agent/human_reviews_2026/jAoh2pj9Id.md | 3.00 | 1 (low) | Similar — both have interesting ideas undermined by execution issues |
| /home/wg25r/review_agent/human_reviews_2026/ZzC26cS22K.md | 4.00 | 2 (mid) | Worse — less coherent claims and more internal inconsistencies |
| /home/wg25r/review_agent/human_reviews_2026/AIONsRr6n7.md | 5.00 | 2 (mid) | Worse — the accepted paper has much cleaner claims and experiments |
| /home/wg25r/review_agent/human_reviews_2026/mLLAc1FhWV.md | 4.50 | 2 (mid) | Worse — similar ambition but this paper has more unsupported claims |
| /home/wg25r/review_agent/human_reviews_2026/geLzACYeE0.md | 4.00 | 2 (mid) | Worse — this paper has overclaimed results by a wider margin |
| /home/wg25r/review_agent/human_reviews_2026/7UPZMoLRTI.md | 4.00 | 3 (narrow) | Worse — cleaner paper but more limited scope, fewer internal contradictions |
| /home/wg25r/review_agent/human_reviews_2026/iElE0OESEf.md | 3.33 | 3 (narrow) | Similar — both have interesting theoretical ideas but poor execution |
| /home/wg25r/review_agent/human_reviews_2026/pSgvlDjNOM.md | 4.00 | 3 (narrow) | Worse — this paper has more severe structural issues |

MY FINAL SCORE: <score>3.0</score>
MY FINAL DECISION: <decision>Reject</decision>