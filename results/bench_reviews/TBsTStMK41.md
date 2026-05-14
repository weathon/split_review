Now I have sufficient calibration context. Let me write the final review.

## Summary

This paper addresses the practical problem of minimizing unnecessary desk-rejections under per-author submission limits at AI conferences. It formalizes the problem as a maximum desk-acceptance integer program, relaxes it to a linear program, and applies a custom rounding scheme to recover a feasible integer solution. The method is evaluated on 11 years of real ICLR submission data (2013–2025) and consistently outperforms current desk-rejection policies, achieving up to 19.23% relative reduction in desk-rejected papers while running in under 54 seconds.

## Strengths

- **Practical and timely problem with real-world impact.** The paper tackles a genuine issue affecting thousands of authors at major AI conferences. The formalization as an optimization problem is a natural and useful framing that prior work on this specific policy is scarce.

- **Empirical evaluation on 11 years of real ICLR data.** The authors use the only publicly available multi-year submission dataset (ICLR 2013–2025, excluding 2015–2016), covering conference sizes from 67 to 11,672 papers. The extensive results in Table 3 across 8 different submission limits (b=4 to b=25) show consistent improvements. For the largest and most relevant years (ICLR 2024, 2025), the method improves across nearly all values of b.

- **Practical efficiency.** All results computed within 53.64 seconds on modest hardware (2 vCPUs, 13GB RAM). This makes the method readily deployable in real conference workflows.

- **Clean problem formalization.** The paper provides a rigorous mathematical framework (Definitions 3.1, 4.1) and formally proves correctness and time complexity of both existing algorithms and the proposed rounding procedure.

## Weaknesses

### Fatal
None.

### Major

1. **Unexplained discrepancy between the LP relaxation and the integer program.** Definition 4.1 (the IP) uses the constraint `Ax ≤ b·1_n`, but Definition 4.3 (the LP relaxation) uses `Ax ≤ b - 1_n`. The paper never acknowledges or explains why the RHS is tightened from `b` to `b-1`. This appears to be an intentional design choice (the tighter LP leaves slack for the rounding algorithm, which checks feasibility against `b` in Algorithm 3 line 13), but the absence of any justification makes the description appear erroneous. If the LP is solved with `b-1`, the feasible region is smaller and the resulting objective is a weaker bound — the empirical results may be conservative, but the paper's mathematical presentation is confusing and incomplete.

2. **No optimality gap analysis.** The paper frames the problem as "maximizing" desk-accepted papers (Definition 4.1) and uses the term "maximum desk-acceptance," but never compares the rounded solution against the LP upper bound or an exact integer programming solution. Without reporting the LP objective value alongside the rounded integer objective, there is no evidence that the heuristic produces near-optimal solutions. This is a critical omission for a paper whose central contribution is an optimization-based method. The evaluation only compares against two simple heuristics (ALLREJECT and FORWARDREJECT), which are themselves far from optimal.

3. **ALLREJECT baseline is underspecified.** Algorithm 1 (line 6) says "Find a set R_i ⊆ P_i such that |R_i| = |P_i| - b" but does not specify how R_i is selected (e.g., by submission ID, randomly, or otherwise). Since the selection rule determines which papers are rejected and directly affects the comparison, this ambiguity makes the baseline results in Table 3 unreproducible without additional implementation details.

4. **Rounding algorithm is partially underspecified.** Algorithm 3, step 14, requires "Find the set S_i ⊆ (S ∩ T_i) such that ∑_{j∈S_i} ˜x_j ≥ (1 - x_l)" and claims this takes O(k₁) time, but no concrete procedure for constructing this set is provided. While a greedy approach is plausible, the algorithm as described cannot be reliably implemented without guessing the intended method.

### Minor

- **Evaluation limited to ICLR data.** The paper acknowledges this limitation (Section 5.1), noting that desk-rejection data from other conferences is not public. However, authorship patterns could differ across venues, and the generalizability to other conferences is unknown.

- **Absolute improvements are sometimes small.** For smaller years (e.g., ICLR 2018 at b=10, the improvement is 0 papers; at b=7, only 1 paper saved). The headline 19.23% figure (ICLR 2024, b=22) corresponds to saving 5 papers over the best baseline (26 → 21). While the relative improvements for larger years are more compelling (ICLR 2025 at b=4: 2984 → 2668 = 316 papers saved), the paper would benefit from more emphasis on absolute numbers.

- **No fairness analysis.** The algorithm may systematically desk-reject papers with many co-authors (since they consume more author budget). The paper does not discuss or analyze this potential bias.

### Trivial

- The phrase "now policies" appears twice in Section 5.2 ("the desk-rejection policies now policies in AI conferences").

## Nice-to-Have

- Reporting the LP objective value alongside the rounded solution to establish an optimality gap would substantially strengthen the "maximization" framing.
- Implementing the actual conference policy (reject papers with highest submission IDs) as a concrete instantiation of ALLREJECT, rather than leaving R_i abstract.
- A theoretical approximation guarantee for the rounding scheme would elevate the contribution.

## Removed Points

- **Criticism about "LP relaxation being incorrectly formulated causing invalid results" (Harsh Critic point 1):** The use of `b - 1_n` instead of `b · 1_n` is an unexplained design choice, not necessarily an error. If the LP was solved with `b-1`, the results remain valid (just potentially conservative). The rounding algorithm checks feasibility against `b`, so the combined procedure produces feasible IP solutions. The core issue is lack of explanation, not invalidity of results.

- **Criticism about FORWARDREJECT not being equivalent to actual policy (Harsh Critic point 3):** FORWARDREJECT processes papers in order (j=1..m) and accepts if authors have room, which is equivalent to keeping papers with smallest IDs — exactly what the CVPR 2025 policy (reject highest IDs) does. This baseline is faithful to actual practice.

- **Criticism about Remark 4.4 being irrelevant:** The remark cites a specific LP solver complexity, which is standard context for an optimization paper and not irrelevant.

- **Generic strengths from Strength Finder** (e.g., "rigorous problem formalization"): These are kept substantively; the truly generic ones are filtered.

## Novel Insights

None beyond the paper's own contributions. The reviews surfaced no cross-cutting insight that the authors missed.

## Suggestions

1. **Explain the b-1 choice.** Clarify in Section 4.2 why the LP relaxation uses `Ax ≤ b - 1_n` rather than `Ax ≤ b · 1_n`. If this is a deliberate tightening to enable feasibility-preserving rounding, say so explicitly.

2. **Report the LP upper bound.** Add a column in Table 3 (or an appendix table) showing the LP relaxation's optimal objective value alongside the rounded solution, so readers can assess the optimality gap.

3. **Specify ALLREJECT's selection rule.** State explicitly how R_i is chosen in the experiments (e.g., by submission ID, as in the CVPR 2025 policy), or remove the ambiguity from Algorithm 1.

4. **Provide a concrete procedure for Algorithm 3 step 14.** Even a brief description (e.g., "sort fractional values descending and greedily select papers until the sum reaches the threshold") would resolve the ambiguity.

5. **Add a fairness discussion.** Analyze whether the method systematically disadvantages papers with many co-authors, and discuss potential mitigations.

## Score and Decision

**Calibration anchors (batch-retrieved, listed with comparison):**

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| `/home/wg25r/review_agent/human_reviews_2026/QvN5FZ3tNW.md` | 1.50 | Similar topic (desk rejection optimization) but much weaker — no empirical evaluation, unrealistic assumptions. This paper is clearly stronger. |
| `/home/wg25r/review_agent/human_reviews_2026/OH7joQ9jpl.md` | 2.50 | Methodologically unsound paper with 0 scores. My paper is substantially better — it has a coherent method and real-data evaluation. |
| `/home/wg25r/review_agent/human_reviews_2026/iSqOXQ7bCc.md` | 3.00 | ICLR data analysis with major methodological issues and conflicting reviews (8,0,4,0). My paper's empirical evaluation is more focused and sound. |
| `/home/wg25r/review_agent/human_reviews_2026/SFgXPipvXw.md` | 5.00 | RL for ILP solving — similar level of mixed quality. Has a practical method and some evaluation but also significant gaps (weak baselines, missing details). Comparable to my paper. |
| `/home/wg25r/review_agent/human_reviews_2026/CyKVrhNABo.md` | 5.50 | ICLR data system paper accepted as poster. Strong practical contribution but limited novelty. Comparable in practical value to my paper. |
| `/home/wg25r/review_agent/human_reviews_2026/vqNg2Vl8o1.md` | 5.50 | MILP constraint reduction accepted as poster. Stronger technical contribution than my paper but similar evaluation limitations. |
| `/home/wg25r/review_agent/human_reviews_2026/yRtgZ1K8hO.md` | 8.00 | Oral-quality paper with novel theory and thorough empirical validation. My paper is not at this level. |

The paper has a well-motivated problem, clean formalization, and solid empirical evaluation on real data — clearly above the 1.5–3.0 papers with major methodological flaws. However, the unexplained LP formulation discrepancy, missing optimality analysis, and underspecified algorithm details (ALLREJECT selection rule, rounding step) are significant issues that would need to be addressed. The paper is comparable to the 4.5–5.5 range papers in the calibration set.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>