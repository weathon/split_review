Now I have a thorough understanding of the paper and calibration anchors. Let me compile my final review.

**Round 1 bracket:** The paper sits between the weak band (papers at ~3.0 with incomplete evaluation, weak theory) and the strong band (papers at 8.0 with strong theory + experiments). Comparing against middle-band anchors at 5.0–6.5, the paper lands in **5.0–6.5**.

**Round 2 narrowing:** Compared against anchors at 5.75 (Fair Bandit, rejected), 6.00 (Reopt MILP, rejected), 6.25 (Guided Diffusion IP, rejected), and 6.50 (L2P-MIP, accepted), this paper is comparable in quality to the 5.5–6.0 range. It is empirically stronger than the theoretical GNN-LP paper (5.5, accepted with mixed reviews) but has less technical novelty than the L2P-MIP paper (6.50). The paper's main weakness — no optimality guarantee and no comparison with exact IP — is analogous to criticisms that led to rejection of the 6.25 Guided Diffusion paper.

**Final score:** 5.5.

---

## Summary
This paper addresses a practical problem in AI conference management: how to minimize unnecessary desk-rejections when enforcing per-author submission limits. The authors formalize current ad-hoc desk-rejection policies (ALLREJECT, FORWARDREJECT), reformulate the problem as an integer program maximizing desk-accepted papers, and propose a two-stage algorithm: solve an LP relaxation, then round the fractional solution to a feasible integer solution with a correctness guarantee. Evaluation on 11 years of real ICLR submission data shows consistent improvement over current policies, with relative reductions in desk-rejections of up to 19.23%.

## Strengths
- **Clear problem formalization with practical relevance.** The paper provides rigorous mathematical formulations of existing desk-rejection policies (Algorithms 1 and 2, with time-complexity bounds in Propositions 3.5–3.6) and reframes the problem as an optimization task (Definition 4.1). This moves beyond ad-hoc conference rules to a principled optimization perspective, directly motivated by real policies at CVPR, AAAI, KDD, and other major venues (Table 1).
- **Feasibility-guaranteed algorithm.** The LP relaxation + rounding framework (Algorithm 4) comes with a correctness guarantee (Theorem 4.6): the rounded solution provably satisfies all per-author submission limits. The algorithm runs in at most 53.64 seconds on ICLR-scale data, demonstrating practical deployability.
- **Real-world empirical validation at scale.** The evaluation uses 11 years of ICLR submissions (2013–2025) obtained via the OpenReview API, spanning 67 to 11,672 papers. The proposed method consistently reduces desk-rejections compared to both ALLREJECT and FORWARDREJECT across all tested submission limits (b = 4 to 25) and all years where violations occur, with relative improvements reaching 19.23% (ICLR 2024, b = 22).

## Weaknesses

### Major
- **No approximation guarantee and no comparison with exact IP optimum.** The paper formulates the problem as an integer program (Definition 4.1) and solves it via LP relaxation + rounding, but provides no bound on how close the rounded solution is to the optimal integer solution — no approximation ratio, no integrality gap analysis. The paper states it establishes "computational hardness" (line 49) but offers only a remark relating the problem to multi-dimensional knapsack without a formal NP-hardness proof. More importantly, the experiments do not include a comparison with an exact IP solver even for the smaller ICLR years (e.g., 2013 with only 67 papers, or 2014 with 69 papers) where computing the true optimum would be tractable. Without this, the reader cannot judge whether the reported improvements arise from genuinely near-optimal solutions or simply from being somewhat better than deliberately simple baselines. The paper's framing as "maximum desk-acceptance" (Definition 4.1) implies optimality, which is not substantiated. Comparing against an exact IP solver on small instances, or deriving even a weak approximation bound, would substantially strengthen the central claim.

### Minor
- **Rounding algorithm under-specified.** Algorithm 3, line 14, states "Find the set S_i ⊆ (S ∩ T_i) such that Σ_{j∈S_i} x̃_j ≥ (1 − x_l)" and asserts this takes O(k₁) time, but does not specify *how* the subset is chosen. Different selection strategies (e.g., smallest subset vs. largest fractional values first) could yield different final solutions. This is a reproducibility gap that should be resolved with a concrete selection rule and, ideally, a sensitivity analysis.
- **Limited baseline comparison.** The only baselines are the two current conference policies (ALLREJECT and FORWARDREJECT). While these are the most policy-relevant comparisons, adding a simple alternative heuristic — e.g., a greedy algorithm that orders papers by number of co-authors (ascending) or total author conflict — would help disentangle the benefit of the LP formulation from the benefit of any non-trivial ordering. This would strengthen the case that the LP is necessary, not merely sufficient.
- **No discussion of which papers are saved.** The paper reports aggregate rejection counts but provides no analysis of which papers or author collaboration patterns benefit from the method. Understanding whether the method systematically favors certain types of papers (e.g., those with fewer co-authors, or those from large labs) is important for fairness perceptions in practice, and this is not addressed.

### Trivial
- **Typo in Definition 4.3.** The constraint is written as "Ax ≤ b − 1_n" but should be "Ax ≤ b · 1_n" to match Definition 4.1 with the domain relaxed to [0,1]^m. The current expression is dimensionally inconsistent.
- **Runtime reporting lacks context.** "All results on ICLR data computed within at most 53.64 seconds" does not specify whether this is per instance, per year, or total wall-clock time across all experiments, nor whether it includes data loading and preprocessing.

## Nice-to-Haves
- Discuss how the objective could be modified if a conference wants to target a specific total review volume rather than maximizing desk-acceptance unconditionally.
- Include an analysis of the increase in total papers forwarded to review versus current policies, so readers can weigh author-welfare gains against reviewer-load increases.
- Consider a fairness-aware variant of the optimization (e.g., maximizing the minimum number of papers per author group rather than total papers).

## Removed Points
These points from the harsh critic were examined and are not retained as valid weaknesses:

- **"Algorithm 1 as a straw-man"** — The paper includes both ALLREJECT (Algorithm 1) and FORWARDREJECT (Algorithm 2) as baselines and computes relative improvement against the *stronger* baseline (FORWARDREJECT). The paper is transparent about both. The gap is not inflated.
- **"Optimization objective conflicts with reviewer workload"** — The submission limit b is set by the conference to control workload. The paper's method respects the same limit b as current policies; it does not increase the total number of papers beyond what any author is allowed. If a conference wants the same total review volume, it can lower b accordingly. The tension exists but is a conference-policy choice external to the method.
- **"Ethics statement omission regarding reviewer load"** — The ethics statement appropriately centers on author welfare, particularly for early-career researchers, which is the paper's stated concern. Reviewer load is controlled by the limit b, which the method does not alter.
- **"The method has no optimality or approximation guarantee — fatal"** — Retained as Major (not fatal) because the paper's practical claim of improving over current policies does not require optimality to be valid; the lack of guarantee weakens but does not invalidate the contribution.
- **"Missing related works"** — Not evaluated; no external sources to verify.
- **"Presentation nitpicks / typos"** — The typo in Definition 4.3 is retained as Trivial. All other formatting criticisms are parser artifacts removed per instructions.

## Novel Insights
None beyond the paper's own contributions. The paper's framing of conference desk-rejection as an explicit optimization problem (rather than a feasibility check) is its core novel insight, and this is already claimed by the authors.

## Suggestions
- Run an exact IP solver (e.g., Gurobi or SCIP) on ICLR 2013, 2014, and 2017 data (67, 69, and 490 papers respectively) to establish how close the LP+rounding heuristic comes to the true optimum. Report the optimality gap.
- Fully specify the subset selection rule in Algorithm 3, line 14, and add a brief ablation comparing different selection strategies.
- Add at least one alternative heuristic baseline (e.g., greedy by ascending co-author count) to strengthen the empirical case for the LP formulation.
- Fix the typo in Definition 4.3 ("b − 1_n" → "b · 1_n").
- Report the absolute number of papers saved per year alongside the relative improvement, and discuss which collaboration patterns benefit.

## Score and Decision

### Calibration Anchors

| Anchor ID | Avg Score | Round | Comparison |
|---|---|---|---|
| yYylDyLnzt | 3.00 | R1 | Dantzig-Wolfe + RL for bin packing — clearly weaker; limited evaluation |
| C9pndmSjg6 | 3.00 | R1 | Portfolio optimization with relaxation — weaker; less practical motivation |
| psDvcWtFdE | 3.00 | R1 | MILP instance generation — weaker; narrow contribution |
| ghk8lnOYRq | 5.00 | R1 | k-hyperplane clustering via multi-norm — comparable weakness tier but less applied |
| 2oWRumm67L | 5.00 | R1 | Light-MILPopt — comparable; similar LP-focused optimization with practical bent |
| INow59Vurm | 5.50 | R1 | GNNs for LP — accepted with mixed reviews; theoretical, no experiments; our paper is empirically stronger |
| REKRLIXtQG | 5.00 | R2 | Supermodular rank — theoretical; less applied than our paper |
| o0oroLuPLZ | 4.60 | R2 | SPO+ extension for LP — clearly weaker; limited validation |
| C9YyVygCpG | 5.75 | R2 | Max-min fair bandit — theoretical with regret bounds; rejected; our paper has real data |
| scdGzuwC9u | 6.00 | R2 | Reoptimization MILP — similar quality tier; rejected for limited novelty and easy instances |
| joMMM9eadc | 6.25 | R2 | Guided diffusion for IP — stronger technical novelty; rejected for insufficient comparison |
| McfYbKnpT8 | 6.50 | R1 | L2P-MIP — stronger; novel learning approach, broader impact; accepted |

**Round 1 bracket:** 4.5–7.0
**Round 2 narrowing:** The paper is most comparable to scdGzuwC9u (6.00, rejected) and C9YyVygCpG (5.75, rejected), with similar levels of technical contribution and types of weaknesses. It is empirically stronger than INow59Vurm (5.50, accepted) but has less technical novelty than McfYbKnpT8 (6.50, accepted). The major weakness — no optimality bound or exact-IP comparison — mirrors the criticism that led to rejection of joMMM9eadc (6.25).

**Final placement:** 5.5. The paper makes a genuine practical contribution with real-world data and consistent improvements over current policies. However, the absence of any quality guarantee for the heuristic relative to the true optimum, combined with under-specified algorithmic details and limited baselines, prevents a higher score. The paper would benefit substantially from an exact-IP comparison on small instances and a fuller specification of the rounding procedure.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>