Now I have enough for comparison. Let me write the final review.

**Round 1 Bracket:** The paper sits clearly above the ~3.0 weak anchors (C9pndmSjg6 — portfolio optimization with no runtime and fundamental methodological errors) and clearly below the ~8.0 strong anchors (5t57omGVMw — strong theoretical contribution with provable regret bounds). Initial bracket: **5.0–7.0**.

**Round 2 Narrowing:** Compared against scdGzuwC9u (6.00, rejected — reoptimization framework for MILP, similar applied-optimization-with-empirical-results structure) and siHHqDDzvS (6.25, accepted — BTBS-LNS for MIP, more technically sophisticated but addressing a more incremental problem in an established area), my paper is comparable: cleaner problem framing and a more novel application domain, but thinner theoretical analysis. Final score: **6.0**.

---

## Summary
This paper addresses the problem of per-author submission-limit desk-rejection at AI conferences. It formalizes existing ad-hoc desk-rejection policies (ALLREJECT, FORWARDREJECT) and proposes an optimization-based approach: maximize desk-accepted papers subject to per-author limits via an integer program, solved through LP relaxation and a greedy deterministic rounding scheme. Evaluation on 11 years of ICLR submission data (2013–2025) shows consistent improvement over both baseline policies, with relative improvements up to 19.23%. The method runs in under 54 seconds on modest hardware.

## Strengths
- **Clean problem formalization with correctness guarantees**: The paper formalizes current ad-hoc desk-rejection policies as precise algorithms with provable correctness (Propositions 3.5, 3.6) and reformulates the problem as an integer program (Definition 4.1) that explicitly optimizes author welfare rather than merely finding any feasible solution. This is a genuine conceptual improvement over current practice.
- **Consistent and well-documented empirical improvement**: Table 3 shows the proposed method never rejects more papers than either baseline across all 8 datasets and 8 submission limits. Improvements are strongest on recent large conferences (10–19% relative improvement for ICLR 2024–2025), where the problem matters most. Absolute numbers are transparently reported alongside relative improvements.
- **Practical efficiency for real deployment**: All results computed within 53.64 seconds on modest hardware (2 vCPUs, 13GB RAM) using the open-source PuLP library. This is fast enough for conference organizers to run as part of their submission processing pipeline.
- **Real-world evaluation at scale**: Uses 11 years of ICLR data (up to 38,495 authors, 11,672 papers) collected via the OpenReview API, with transparent dataset statistics (Table 2) and submission distributions (Figure 2). Given that desk-rejection data from other venues is not public, this represents the best possible evaluation without insider access.

## Weaknesses

### Fatal
None.

### Major
- **Inaccurate method characterization**: The introduction (line 45) and abstract claim the method uses "randomized rounding," but Algorithm 3 is fully deterministic (greedily picks the maximum fractional x_j), and Section 5.1 explicitly confirms "experiments are deterministic and contain no randomness" (line 374). This misrepresents the method to the reader and must be corrected.
- **Overclaimed theoretical contribution**: The introduction claims the paper "establish[es] the computational hardness of the problem" (line 45), but the paper only says the problem is "inherently related to the multi-dimensional knapsack problem" (line 213) — an association, not a hardness proof. No formal reduction is provided. The rounding algorithm (Algorithm 3) only proves feasibility (Theorem 4.6), with no approximation guarantee or integrality gap analysis. For a paper that frames itself as making both practical and theoretical contributions, the theoretical analysis is thin relative to the claims.

### Minor
- **Single-venue evaluation**: Only ICLR data is used (justified as the only venue with public submission records, Section 5.1). The generalizability of findings to conferences with different authorship patterns (e.g., CVPR with its different co-authorship norms) is unknown and not discussed.
- **No integrality gap measurement**: The LP optimum provides an upper bound on the true integer optimum. Reporting the LP objective alongside the rounded solution value for each (year, b) pair would let readers assess whether the rounding or the relaxation is the limiting factor.
- **Algorithm 4 initialization contradiction**: Algorithm 4 specifies random initialization of x₀ (line 2), yet Section 5.1 states experiments are deterministic with no randomness (line 374). This should be resolved — either the initialization is fixed or the randomness claim in Section 5.1 should be qualified.
- **Headline figure needs contextualization**: The 19.23% headline improvement for ICLR 2024 at b=22 represents 5 fewer papers rejected (26→21) out of 7,404 total submissions. The more meaningful absolute savings occur at tighter limits (e.g., 83 papers saved at b=7 for ICLR 2024, 316 at b=4 for ICLR 2025), but the abstract emphasizes the percentage figure. The paper does report absolute numbers transparently in Table 3, so this is a presentation issue rather than a data issue.

### Trivial
None.

## Nice-to-Haves
- Discuss how many additional papers enter the review pipeline under the proposed method and whether this interacts with the intended reviewer workload constraint set by the conference's choice of b.
- Provide a runtime breakdown (LP solve time vs. rounding time vs. preprocessing).
- Discuss tie-breaking fairness when the LP has multiple optimal solutions, since the ethics statement emphasizes equity for early-career researchers.
- Note that the framework naturally supports weighted objectives (Σ w_j x_j) if conferences want to prioritize certain papers.

## Removed Points
These points are flagged to be removed; treat them with caution:

- **Harsh critic: "The tension between maximizing desk-accepted papers and controlling reviewer workload is never addressed."** → REMOVED. The paper's contribution is algorithmic (minimizing rejections given a fixed b). The choice of b is a conference policy decision outside the paper's scope. The paper does acknowledge the tradeoff in the abstract. Demanding the paper also solve the policy question of what b should be is scope creep. Moved to Nice-to-Haves.
- **Harsh critic: "The time complexity can be as bad as O(mnk₂) in the worst case when k₁=Θ(m)."** → REMOVED. This is a speculative worst-case that does not materialize in practice. k₁ (max papers per author) is bounded by author submission behavior, not by m. At ICLR 2025, k₁=42 while m=11,672. Practical runtime is demonstrated empirically (≤53.64 sec).
- **Harsh critic: "FORWARDREJECT ordering sensitivity and fairness not discussed."** → REMOVED. The paper discusses ordering in Section 3.2 (line 141: "conferences often prioritize papers with higher submission IDs"), acknowledges Algorithm 5 (reverse) exists and is equivalent, and uses FORWARDREJECT as the baseline in experiments. The criticism is addressed.
- **Harsh critic: "Need proofs from appendix to verify Theorem 4.6."** → REMOVED. The appendix is stripped by the parser; the original submission includes these proofs with explicit cross-references (Theorem B.3).
- **Strength Finder: "The paper systematically documents the real-world policy landscape" (Table 1).** → DEMOTED from main strengths. Table 1 is useful background context but is not a research contribution of the paper.

## Novel Insights
None beyond the paper's own contributions. The core insight — that current desk-rejection policies are suboptimal and can be improved via global optimization — is the paper's novel contribution.

## Suggestions
- Replace "randomized rounding" with "deterministic greedy rounding" throughout (abstract, line 45, and any other mentions).
- Either provide a formal NP-hardness reduction (e.g., from Set Packing or Multidimensional Knapsack) or remove the claim that the paper "establishes computational hardness" and instead state that the problem is related to known-hard problems.
- Report the LP relaxation objective value alongside the rounded integer solution for each (year, b) pair to quantify the integrality gap.
- Clarify Algorithm 4's initialization to match the deterministic claim in Section 5.1.
- Discuss in a limitations paragraph: single-venue evaluation, ordering independence as an unexamined fairness property of the LP approach, and transparency concerns (LP-based policies are harder to explain to authors than rule-based baselines).

## Score and Decision

**Calibration anchors used:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| C9pndmSjg6 (Portfolio optimization MIQP + heuristics) | 3.00 | R1 | Paper is clearly stronger: cleaner methodology, real-world evaluation, runtime reported |
| CW2aryHm95 (Policy learning for video streaming) | 4.00 | R1 | Paper is stronger: more novel problem, clearer formulation, more consistent results |
| 5t57omGVMw (Learning to Relax — bandit for SOR) | 8.00 | R1 | Paper is clearly weaker: lacks theoretical depth, provable guarantees, and rigorous analysis |
| scdGzuwC9u (Reoptimization framework for MILP) | 6.00 | R2 | Comparable quality. My paper has cleaner problem framing and more novel application, but similar level of theoretical gaps relative to claims |
| siHHqDDzvS (BTBS-LNS for MIP) | 6.25 | R2 | Slightly stronger technically than my paper (GNN+RL+branching, competition with Gurobi, 13 baselines). My paper opens a more novel application area |

**Round 1 bracket:** 5.0–7.0  
**Round 2 narrowing:** The paper is comparable to scdGzuwC9u (6.00) and slightly below siHHqDDzvS (6.25). The clean problem formulation and strong empirical results are offset by overclaimed theory and inaccurate method description. **Final score: 6.0.**

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>