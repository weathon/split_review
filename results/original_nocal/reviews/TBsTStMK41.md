Now I have a thorough understanding of the paper. Let me synthesize the final review.

## Summary

This paper formalizes the desk-rejection problem at AI conferences (where papers exceeding per-author submission limits are rejected) as an integer program maximizing the number of papers kept ("maximum desk-acceptance"). It proposes a two-stage algorithm: solve the LP relaxation, then round to a feasible binary solution via a greedy rounding scheme (Algorithm 3). Evaluated on 11 years of real ICLR submission data (2013–2025), the method reduces desk-rejections by up to 19.23% compared to current conference policies, running in under 54 seconds.

## Strengths

**1. Formal optimization reframing of desk-rejection.** The paper redefines desk-rejection as the maximum desk-acceptance IP (Definition 4.1), explicitly maximizing the number of papers retained under per-author caps. This goes beyond the feasibility-only formulation used by current conferences (Definition 3.1, Remark 4.2). The problem formulation is clean, well-motivated, and clearly stated.

**2. Demonstrated empirical gains on a decade of real data.** The method consistently reduces desk-rejections across all years and submission limits where baselines also reject papers (Table 3). Improvements reach double-digit percentages in recent large years (e.g., 19.23% for ICLR 2024 at b=22; 12.56% for ICLR 2025 at b=7). The use of 11 years of real, publicly-crawled ICLR data (not synthetic) gives the results strong ecological validity.

**3. Practical efficiency.** All results are computed within 53.64 seconds maximum using a standard LP solver (PuLP) on a CPU with 2 vCPUs and 13GB RAM (Section 5.2). This demonstrates the algorithm is fast enough for real conference operation without specialized hardware.

**4. Well-specified baselines.** The paper formalizes the two actual policies used by conferences (ALLREJECT, Algorithm 1; FORWARDREJECT, Algorithm 2) and compares against them systematically across b ∈ {4,7,10,13,16,19,22,25} (Table 3, Appendix E). This is a fair comparison against status quo practice.

## Weaknesses

### Fatal
None.

### Major

**1. No analysis of solution quality relative to optimal.** The rounding algorithm (Algorithm 3) guarantees only *feasibility* (Theorem 4.6), not any approximation factor or bound on the gap between the rounded solution and the true IP optimum or the LP upper bound. The paper claims to "maximize" desk-acceptance (Definition 4.1), but the actual algorithm is a heuristic whose distance from optimality is uncharacterized. Without knowing whether the method closes most of the optimality gap or leaves a large gap, the reader cannot assess how much further improvement is possible. This is the paper's most significant limitation.

**Supporting evidence:** Theorem 4.6 states only that the algorithm "outputs the feasible solution for x as defined in Definition 3.1." No approximation factor, integrality gap analysis, or bound on the rounded solution's objective value is provided. The paper mentions the problem is related to multi-dimensional knapsack (line 217) and acknowledges the LP may not be integral (line 231), but does not analyze how much the rounding loses.

### Minor

**2. No comparison to exact optimal or near-optimal solutions.** The baselines are the two current conference policies, which is appropriate for demonstrating improvement over the status quo. However, the paper would be strengthened by comparing the LP+rounding solution against the exact IP optimum (solved via branch-and-bound) on smaller instances where that is tractable (e.g., subsampled years or early ICLR years). This would reveal whether the heuristic is near-optimal or whether a more sophisticated approach could yield further gains.

**Impact:** The empirical claim of improvement over current policies is valid without this comparison, but the paper's claim about "maximizing" welfare is incompletely supported.

**3. Rounding algorithm step is underspecified.** Algorithm 3, line 14: "Find the set S_i ⊆ (S ∩ T_i) such that ∑_{j∈S_i} x̃_j ≥ (1 - x_l)" does not specify how to construct such a set, nor is there an argument that such a set always exists under the given conditions. While a simple greedy accumulation of fractional values would likely suffice, the procedure and its correctness depend on details deferred to an inaccessible appendix (Theorem B.3). The time complexity claim of O(k₁) for this step assumes this operation is trivial, which requires justification.

**4. LP relaxation constraint is inconsistent with the IP constraint.** The IP (Definition 4.1) uses the constraint "Ax ≤ b·1_n", while the LP relaxation (Definition 4.3) writes "Ax ≤ b - 1_n". The subtraction of one from each author's limit is unmotivated. If intentional, this would mean the LP solves a strictly tighter problem than the IP relaxation, potentially reducing the objective value. If a formatting artifact, it should be corrected. This needs clarification.

**5. Minor inconsistency: "randomized rounding" claimed but algorithm is deterministic.** The introduction (line 49) states the algorithm uses "linear programming relaxation and randomized rounding," but Algorithm 3 is entirely deterministic. The only randomness is the initial point for the LP solver (Algorithm 4, line 2), which does not affect the solution of a convex LP. This should be corrected for precision.

### Trivial
- The paper does not explicitly discuss the limitation that the rounding algorithm is a heuristic with no optimality guarantee (this is connected to Major weakness #1).

## Nice-to-Haves
- Compare against exact IP optimum for small instances (e.g., ICLR 2013–2018 with small b) to measure the optimality gap.
- Test sensitivity to paper ordering in the rounding step (Algorithm 3 picks the paper with largest x̃ⱼ; does tie-breaking matter?).
- Plot the LP objective vs. the rounded solution's objective for each year to visualize the gap introduced by rounding.
- Discuss when the constraint matrix might yield integral LP solutions (e.g., certain graph structures).

## Removed Points

These points were raised by reviewers but are filtered out as invalid, overstated, or noise:

- **"Fatal: no theoretical guarantee on solution quality"** — Downgraded from Fatal to Major. The paper's primary claim is empirical (reducing rejections vs. current policies), and this is well-supported. The lack of optimality guarantee is a genuine limitation but does not invalidate the empirical contribution. Many applied/heuristic papers at ICLR make similar empirical contributions without approximation guarantees.
- **"Fatal: baselines too weak"** — The baselines (ALLREJECT, FORWARDREJECT) are the actual policies used by conferences. Comparing against these is appropriate and not weak. The critic's assertion that improvements are "single-digit papers saved" is factually incorrect — Table 3 shows improvements of dozens to hundreds of papers (e.g., ICLR 2025 b=4: 316 papers saved vs. FORWARDREJECT). The request for "greedy by author count" is reasonable but not fatal to omit. Demoted to Minor and merged with weakness #2.
- **"Rounding algorithm cannot be trusted"** — Overstated. While the algorithmic description is slightly underspecified (Weakness #3), the step's intent is clear and the construction is straightforward. Demoted to Minor.
- **"Problem is a trivial IP"** — This is a subjective assessment, not a concrete weakness. Many practical problems reduce to simple IPs. The contribution is in the formalization, algorithm, and empirical validation.
- **"Conclusion overstates contributions"** — Subjective opinion about tone, not a verifiable weakness.
- **Generic concerns about missing variance/sensitivity** — The experiments are deterministic as stated; this is acceptable for a deterministic algorithm.
- **Related works / missing references** — Cannot verify.

## Novel Insights

None beyond the paper's own contributions. The synthesis of reviewer perspectives does not yield new observations that the paper itself does not present.

## Suggestions

1. **Analyze the optimality gap.** For small instances where the exact IP can be solved (e.g., subsample early ICLR years), compare the LP+rounding objective against the true IP optimum. This would show how much optimality is lost and contextualize the heuristic's quality.
2. **Clarify the LP constraint.** Resolve the "b - 1_n" vs. "b·1_n" discrepancy in Definition 4.3. If the paper intentionally uses a tighter bound, explain why.
3. **Flesh out Algorithm 3 line 14.** Specify how S_i is constructed (e.g., "take papers from S∩T_i in any order until their x̃ values sum to at least (1−xₗ)") and argue existence.
4. **Discuss the heuristic nature.** Add a limitations paragraph explicitly noting that the rounding scheme does not guarantee optimality or a constant-factor approximation, and that the empirical results should be interpreted in this light.
5. **Correct the "randomized rounding" claim.** The rounding is deterministic; remove or correct this descriptor.

## Score and Decision

The paper addresses a timely, practical problem with a clean formulation and a simple, fast algorithm that demonstrably improves upon current conference policies on real data. The main weakness is the lack of optimality analysis, which is significant but does not undermine the core empirical contribution. The paper would benefit from additional comparison to exact optimal solutions for small instances, but the results as presented are sufficient to support the claim that the method reduces unnecessary desk-rejections compared to status quo policies. On balance, the paper represents a useful and well-motivated contribution.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>