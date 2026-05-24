Now I have a clear picture. Let me write the consolidated review.

## Summary
This paper introduces Dig-DEC, a new model-free decision-estimation coefficient that replaces optimism with pure information-gain exploration within the DEC/AIR framework. The authors apply it to obtain the first model-free regret bounds for hybrid MDPs with bandit feedback (resolving an open problem from LWZ25), and improve online function-estimation procedures to sharpen regret rates in standard stochastic MDP settings. The framework generalizes prior AIR analyses and is supported by new theoretical tools including an unbiased split-sample estimator and a refined two-timescale posterior update.

## Strengths
- **Genuinely novel complexity measure.** Dig-DEC (Eq. 8) is a creative synthesis of information-gain and estimation-error terms that avoids the optimism mechanism of prior work. Theorem 13 proves it is comparable to optimistic DEC (up to an additive η gap), and Theorem 14 provides a concrete 3-armed bandit where Dig-DEC yields constant regret while optimistic DEC forces Ω(√T) regret — a clean separation result.

- **First model-free bandit-feedback bounds for hybrid MDPs.** Table 2 provides explicit sublinear regret expressions for hybrid bilinear classes and coverable MDPs under linear reward and bandit observations. This directly addresses the open question from LWZ25 and is enabled by the removal of optimism (which avoids explicit reward estimator construction). This is a meaningful advance for the DEC community.

- **Improved estimation procedures with concrete rate gains.** Theorem 7 achieves O(N log|Φ| T^{1/2}) for average estimation error via an unbiased split-sample estimator (improving on the biased estimator of FGQ+23). Theorem 11 achieves O(log²|Φ|) constant estimation penalty for squared error in Bellman-complete MDPs via a refined two-timescale procedure, enabling √T regret that matches optimism-based methods for the first time in the DEC framework.

- **Flexible and unifying framework.** The generalization to an arbitrary convex divergence D (Eq. 2) and the new analysis via Bregman divergences (Eq. 5–6) cleanly recovers prior results (XZ23, LWZ25) while enabling the new developments. This is a solid analytical contribution that simplifies the presentation of DEC-based algorithms.

## Weaknesses

### Major
- **Numerically inconsistent regret bounds across the paper.** The abstract claims improvements from T^{3/4} to T^{3/5} (on-policy) and T^{5/6} to T^{7/8} (off-policy) for the average-estimation-error case. Table 1 shows T^{2/3} for both on-policy and off-policy rows under average estimation error — a different exponent from what the abstract states. Further, Table 2 contains multiple entries with exponents T^{3/2} and T^{13/8}, which are superlinear and cannot be valid sublinear regret bounds (the framework's own formula T·dig-dec + Est/η with optimal η should produce sublinear rates). The derivation from the theoretical framework to the final optimized η and regret column is not shown anywhere in the main text, making it impossible for a reader to verify which numbers are correct and which are typos. These errors propagate through the paper's principal numerical claims and must be corrected.

- **Under-specified connection between the general framework and concrete algorithms.** The regret decomposition (Theorem 6) bounds regret by T·dig-dec + Est/η. The paper provides Est bounds (Theorems 7 and 11) and dig-dec bounds (Tables 1–2), but the main text does not show how these are combined — specifically, how the optimal η is chosen and how the final regret exponents in the tables are derived. The POSTERIORITYUPDATE equation (Eq. 4) is left as an uninstantiated placeholder; Algorithms 2–4 that realize it are referenced but their key mechanisms (batching structure, two-timescale update) are only sketched. The claim that Theorem 7 gives Est ≲ N log|Φ| T^{1/2} is stated without walking through how Algorithm 4 achieves this from Assumption 5. While appendix deferral is standard for proofs, the main text should contain enough derivation for the reader to verify the bridge between the framework, the Est bounds, and the final regret columns.

### Minor
- **Overstated comparison with optimistic DEC.** The abstract states "Dig-DEC is always no larger than optimistic DEC," but Theorem 13 establishes dig-dec ≤ o-dec + η. The additive η gap means that for finite η, Dig-DEC could be larger. The abstract and introduction should use the precise relation stated in Theorem 13. This is addressable by a wording correction.

- **The hybrid-setting assumptions are restrictive, and the discussion of this restriction could be sharper.** Assumptions 3 and 4 (linear reward with known features, transition partition independent of specific transitions given feature expectations) are acknowledged by the authors as not covering all known hybrid MDPs (e.g., low-rank MDPs with unknown features). The paper notes this limitation and the connection to LWZ25's similar restriction, but a brief discussion of what is lost relative to model-based alternatives would help readers assess the significance of the "first model-free" claim.

### Trivial
- **Garbled sentence in §4.2.1.** Line 219 states "[FGQ+23]'s rate of Est from √T to T^{1/2}" — these are the same rate, so the sentence is self-contradictory. The intended claim is clear from context (the improvement comes from the unbiased vs. biased estimator construction), but the sentence as written says nothing.

- **T^{3/2} appears in the introduction** (line 39: "improve the T^{3/2}/T^{5/8} regret of [FGQ+23] to T^{3/2}/T^{5/6}") where T^{3/4} was likely intended, given that the abstract cites T^{3/4} as the prior on-policy rate. This is another instance of the numerical inconsistency problem.

## Nice-to-Haves
- A brief discussion of lower bounds or conjectured optimality of the obtained regret rates would strengthen the contribution and help readers evaluate tightness.
- A comment on computational feasibility of solving the minimax problem (Eq. 3) for realistic MDPs, even if only to acknowledge it as a common limitation of DEC-based work.

## Removed Points
These points are flagged to be removed; treat them with caution.

- **Harsh Critic claim about "inconsistent regret bounds being a structural presentation flaw that invalidates the paper's ability to support its own conclusions."** This overstates the problem. The inconsistencies are real but affect only the table entries and abstract numbers — the underlying theoretical framework (Theorems 6, 7, 11, 13) appears coherent and the framework-level claims are not contradicted by the framework itself. The errors are fixable calculation/typographical issues in the summary tables, not contradictions in the theorems. Retained as Major (not Fatal) since they undermine verifiability of the concrete claims but do not invalidate the core framework.

- **Harsh Critic claim that "the Est-to-regret connection is under-specified and potentially flawed" and "casts doubt on the correctness of the entire estimation procedure."** This is speculative. The main text does under-explain the connection, but the Est bounds are stated as theorems and the regret formula is T·dig-dec + Est/η. The missing piece is the optimization-over-η step that produces the final table entries, which is a derivation gap rather than evidence of incorrectness. Retained as Major (under-specified derivation) but the "potentially flawed" framing is removed.

- **Harsh Critic claim that "the hybrid setting may rely on an overly restrictive reward structure" and questioning whether resolving LWZ25's open problem is meaningful.** The paper explicitly acknowledges the limitation (discussion after Assumption 3) and notes LWZ25 has the same restriction. The restriction is real but the paper does not overclaim — it states the limitation clearly. Retained as Minor (discussion of restriction could be sharper) but the implication that the open-problem resolution is meaningless is removed.

- **Strength Finder claim that Theorem 7 achieves O(log|Φ| T^{1/3}).** The Strength Finder itself corrects this mid-sentence to T^{1/2}. The actual Theorem 7 states N log|Φ| T^{1/2}. The T^{1/3} mention appears to be a confusion in the Strength Finder, not a paper claim.

- **Strength Finder generic strengths** about "broad applicability" and "flexible generalization" — these are real aspects of the paper but are stated at too high a level without concrete anchors. Kept the more specific framing in the actual Strengths section above.

## Novel Insights
The most interesting conceptual move in this paper is the decomposition of the KL information-gain term into a regularization component and a pure information-gain component (discussed after Theorem 13). The regularization component alone suffices to recover optimistic DEC bounds, while the information-gain component enables strict improvement. This cleanly separates two roles that were previously conflated in DEC-based exploration, and the removal of optimism is what unlocks the hybrid bandit setting — a connection that was not obvious before this work.

## Suggestions
- Unify all numerical regret claims. Pick one consistent set of exponents and propagate them through the abstract, introduction, Table 1, and Table 2. Show the η-optimization step explicitly in the main text for at least one row of each table so the reader can verify the derivation.
- Correct the superlinear exponents in Table 2. Based on the framework, the regret for hybrid bilinear on-policy without completeness should be on the order of T^{2/3} or T^{5/6}, not T^{3/2}.
- Replace "always no larger than" with the precise relation from Theorem 13 in the abstract and introduction.
- Provide a self-contained sketch in the main text of how Algorithm 4 achieves the Est bound in Theorem 7 (the split-sample unbiased estimator trick is the key idea and can be explained in a few lines) and how Algorithm 3 achieves the constant Est bound in Theorem 11.
- Fix the garbled sentence about "√T to T^{1/2}."

## Score and Decision

**Round 1 bracket:** The paper sits between the weak anchors at ~3.0 and the strong irrelevant anchors at 8.0. Within the middle band (3.5–7.5), it is clearly stronger than the 4.25 VBMLE anchor but below the 6.0 cleanly-executed horizon-free anchor.

**Round 2 narrowing:** Compared to anchors in the 4.5–6.0 range:
- aPNwsJgnZJ (6.00, Accept): Cleaner paper with a single well-executed contribution. Our paper is more ambitious but has serious presentation issues — **weaker**.
- Yx7TnC6AAp (5.75, Reject): Similar pattern — first results in a new setting but concerns about assumptions and lack of experiments. **Slightly weaker** due to the numerical table errors.
- en3NwykrHW (5.50, Reject): Solid bounds but presentation issues and limited scope. **Slightly weaker** because numerical errors are more severe.
- 6HfNB34x9I (5.25, Reject): Interesting idea but significant concerns about assumptions and missing details. **Comparable**, with our paper having more significant contributions but worse table errors.

**Final score:** 5.0 — borderline. The theoretical ideas are strong and novel, and the first model-free bandit bounds for hybrid MDPs are a genuine contribution to the DEC literature. However, the numerical inconsistencies in the tables (especially the superlinear exponents in Table 2) and the under-explained derivation chain make the current version unverifiable in its concrete claims. These are fixable issues that do not undermine the core framework, but they prevent acceptance in the present form.

**Anchor comparison summary:**
| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| Zi1QNJKXAD | 3.20 | R1 | Our paper is substantially stronger |
| lFzUHGebeb | 2.00 | R1 | Not comparable (different area) |
| EWKPEtwjTy | 2.50 | R1 | Not comparable |
| A1WwYw5u8m | 3.00 | R1 | Our paper is stronger |
| w8Zo7jACq7 | 5.20 | R1 | Our paper has similar quality, slightly weaker presentation |
| 2h3m61LFWL | 4.25 | R1,R2 | Our paper has more novelty, stronger contributions |
| aPNwsJgnZJ | 6.00 | R1,R2 | Our paper is weaker — less clean, has numerical errors |
| 8eNLKk5by4 | 6.00 | R1,R2 | Not directly comparable (constrained MDP) |
| 6HfNB34x9I | 5.25 | R2 | Comparable quality; our paper has stronger ideas but worse table errors |
| SbV2eJC7Ci | 5.67 | R2 | Our paper is weaker — has numerical errors |
| Yx7TnC6AAp | 5.75 | R2 | Similar pattern; our paper slightly weaker due to table issues |
| en3NwykrHW | 5.50 | R2 | Similar quality; our paper has more ambition but more errors |
| 3k6raldhEd | 5.00 | R2 | Comparable in overall quality |
| U0c2IaQhHk | 5.00 | R2 | Comparable |

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>