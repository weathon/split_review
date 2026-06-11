## Summary
This paper studies per-author submission-limit desk-rejection at AI conferences, formalizing the problem as an integer program (maximum desk-acceptance) and proposing an LP relaxation with a deterministic rounding scheme. Evaluated on 11 years of ICLR data, the method consistently reduces desk-rejections versus current policies, with up to 19.23% relative improvement, computed in under 54 seconds. The paper also contributes a formalization of existing desk-rejection policies and a curated ICLR dataset.

## Strengths
1. **First formal optimization formulation of the submission-limit desk-rejection problem** (Definition 4.1). Prior conference policies handled this heuristically; the paper provides a clean mathematical foundation and enables principled analysis.
2. **Consistent empirical improvement on real data**. The method matches or outperforms both ALLREJECT and FORWARDREJECT across all 24 non-trivial comparisons in Table 3, never underperforming. Improvements are shown across submission limits b=4 to b=25 on 8 years of data.
3. **Practical runtime**. All results computed within 53.64 seconds on modest hardware (2 vCPUs, 13GB RAM) for up to m=11,672 papers, demonstrating deployability at real conference scales.
4. **Comprehensive 11-year ICLR dataset** with detailed per-year statistics (Table 2: n, m, nnz(A), MSPA, ASPA), supporting reproducibility and future work.
5. **Formalization of existing baselines** with proven correctness and time complexity (Algorithms 1, 2, Propositions 3.5, 3.6), creating a rigorous comparison framework absent from prior venue descriptions.

## Weaknesses

### Major
1. **Rounding algorithm's correctness guarantee is unsubstantiated.** Algorithm 3 rounds the largest fractional entry to 1, then attempts to compensate by finding S_i ⊆ (S ∩ T_i) with ∑_{j∈S_i} x̃_j ≥ (1 − x_l). Theorem 4.6 claims the algorithm always outputs a feasible solution, but the paper provides no proof that the required set S_i always exists under the LP constraints, nor does it specify how to construct S_i (line 246 is a bare "Find" instruction). A concrete failure mode exists: an author with (b−1) integer-1 papers and fractional papers whose total remaining value is < (1 − x_l), due to co-author constraints on other papers, would cause the algorithm to fail while a feasible integer solution exists. The algorithm also uses the conservative threshold (1 − x_l) rather than the actual excess, making the requirement stricter than necessary and increasing the risk of failure. This is a structural gap in the core method — the central algorithmic claim is not supported by the text as written.

2. **No comparison against the true optimal integer solution.** The paper solves the LP relaxation and rounds, but never compares against the exact IP optimum, even for small instances where it would be trivial (ICLR 2013: 67 papers, 2014: 69 papers, 2017: 490 papers). Without this comparison: (a) the gap between the rounded solution and the true optimum is unknown; (b) it is unclear whether improvements come from genuine near-optimality or simply because FORWARDREJECT is a weak baseline; (c) the LP relaxation upper bound is never reported, so the rounding gap is never measured. This significantly weakens confidence in the reported results.

### Minor
3. **Contradiction about randomness.** Algorithm 4 (line 275) states "Randomly initialize x₀" and calls LPSOLVER, while the experiments section (line 374) says "The experiments are deterministic and contain no randomness." If the solver is deterministic despite random initialization, this should be clearly stated. If there is randomness, variance reporting would be needed.

4. **Overstated "computational hardness" claim.** The abstract says the paper "establish[es] the computational hardness of the problem," but the main text (line 213) only notes a relation to the multi-dimensional knapsack problem. No formal NP-hardness proof, reduction, or citation to an existing hardness result is provided in the visible text. The claim should either be substantiated or tempered.

5. **FORWARDREJECT baseline depends on paper ordering.** The method processes papers in submission-ID order, but different orderings could give different results. No sensitivity analysis is provided, which would strengthen confidence in the baseline comparison.

### Trivial
6. **"Randomized rounding" in the abstract** (line 45) is inconsistent with Algorithm 3, which is purely deterministic.
7. **LP constraint in Definition 4.3** appears as "b − 1_n" — likely a parser artifact, should be "b · 1_n".

## Nice-to-Haves
- A discussion of fairness: the optimization maximizes total accepted papers, which could concentrate desk-rejections on papers with many over-limit co-authors.
- Sensitivity analysis of FORWARDREJECT to different paper orderings.

## Removed Points
- **"Metric framing inflates significance" (Harsh Critic, point 5)**: The paper reports both absolute numbers and relative percentages in Table 3 transparently. The critic's claim that the framing is misleading is not supported — the absolute numbers are right there in the table.
- **Missing baselines (random rejection, round-robin, etc.)**: These are not actual conference policies. The paper compares against what conferences use. Adding random baselines would not be informative.
- **"Theoretical runtime disconnected from actual implementation" (Remark 4.4)**: The paper cites state-of-the-art LP solver complexity for context — a standard academic practice. This is not a weakness.
- **"The utilitarian social welfare mention adds little"**: This is a stylistic preference, not a substantive issue.
- **"Single-conference limitation"**: Acknowledged by the authors. ICLR is the only venue with public data; this is a constraint of the problem domain, not an oversight.
- **"NP-hardness proof should be in main text"**: The paper does not claim to have a novel NP-hardness proof; it notes a relationship to the known-hard multi-dimensional knapsack problem. The abstract's "establish the computational hardness" is slightly overstated (see weakness #4) but this framing of the criticism goes too far.
- **"Code/data not released"**: The paper states code/data will be released upon acceptance and provides API instructions. This is acceptable and common for double-blind submissions.
- **Strength Finder point about "transformative social impact" in conclusion**: The strength finder didn't list this as a strength; it was part of the harsh critic's criticism, and I'm removing it as a nitpick.
- **Duplicate criticisms merged**: The harsh critic's points about missing optimality guarantees, missing hardness proof, and missing comparison against IP optimality were merged into weaknesses #1, #2, and #4 above.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. **Fix or replace the rounding algorithm.** Either provide a formal proof that S_i always exists under the LP constraints (with an explicit construction), or replace the algorithm with a provably correct method. For these moderate-sized instances, directly solving the IP may be simplest.
2. **Add IP optimality comparison for small years.** Solving the IP exactly for ICLR 2013, 2014, and 2017 would directly validate the approach and measure the optimality gap.
3. **Report the LP relaxation upper bound** alongside rounded results to quantify the rounding gap.
4. **Clarify the randomness issue:** state whether the LP solver is deterministic and what "randomly initialize" means in context.
5. **Tone down or substantiate the computational hardness claim.**

## Score and Decision

**Calibration anchors considered:**

*Round 1 (bracketing):*
- Low band: Conference desk-rejection / MILP papers (~3.0) — Rejected papers about MILP and combinatorial optimization; the current paper is clearly stronger due to real experiments and practical motivation.
- Mid band: LP/optimization papers (5.0–5.75) — Papers about LP solving, GNNs for LP, diagonal networks for LP; comparable to current paper.
- High band: Strong theory papers (8.0) — Papers with tight theoretical guarantees irrelevant to the submission-limit problem.

*Round 2 (narrowing within bracket):*
- "Peer Review as Multi-Turn Dialogue" (5.67, Reject) — Built dataset from ICLR/NeurIPS, limited technical novelty. Current paper has stronger technical contribution (optimization formulation) and clearer empirical results. **Current paper is stronger.**
- "Reoptimization Framework for MILP" (6.00, Reject) — GNN+Thompson Sampling for MILP reoptimization across 9 datasets. Similar type of gap (no convergence guarantees). Stronger empirical validation (9 datasets vs. 1 venue). **Current paper is slightly weaker.**
- "Multi-play Multi-armed Bandit with Scarce Capacities" (5.50, Reject) — Theoretical bandit paper with tight bounds but writing issues. **Comparable overall quality.**
- "GNN for LP" (5.50, Accept) — Theoretical paper, no experiments, accepted despite missing validation. **Different paper type; current paper is weaker theoretically but stronger empirically.**
- "Diagonal Linear Networks for LP" (5.75, Reject) — Good theory, limited experiments. **Current paper has better applied contribution but weaker theory.**

*Final positioning:* The paper is stronger than the ~3.0 band and comparable to the middle band (~5.0–5.75). However, the unsubstantiated rounding correctness guarantee — a structural gap in the core method — prevents it from reaching the 5.5–6.0 level. Score 5.0 reflects a borderline paper with genuine contributions (problem formulation, empirical results, dataset) but a significant methodological gap that must be resolved before acceptance.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>