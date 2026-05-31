## Summary
The paper addresses the problem of per-author submission limits at AI conferences (e.g., CVPR, AAAI, KDD). Current venues desk-reject all papers from any author exceeding the limit, prioritizing by submission ID — an approach the authors formalize as a suboptimal feasibility problem. They reformulate it as a maximum desk-acceptance integer program (max papers forwarded to review subject to per-author constraints), prove it is NP-hard via reduction to multi-dimensional knapsack, and solve it via LP relaxation plus a greedy rounding scheme. Evaluated on 11 years of ICLR data under simulated submission limits ($b = 4$–$25$), their method desk-rejects up to 19.23% fewer papers than the strongest greedy baseline, in at most 53.64 seconds.

## Strengths

- **Practically important and novel problem formulation.** The paper is among the first to cast conference desk-rejection as a combinatorial optimization problem. The integer program in Definition 4.1 is clean and the connection to multi-dimensional knapsack is appropriate. The practical stakes (author welfare, early-career researcher impact) are well-motivated.
- **Comprehensive empirical evaluation.** 11 years of real ICLR submission data covering $n$ up to 38,495 authors and $m$ up to 11,672 papers, across 22 values of $b$, is thorough. The consistent improvement over both ALLREJECT and FORWARDREJECT baselines (Table 3) is convincing. Runtime scales gracefully to the largest instances.
- **Meaningful magnitude of improvement.** Up to 19.23% fewer desk-rejections at ICLR 2024 ($b=22$) and 10–13% across all $b$ values for ICLR 2024–2025 is non-trivial at the scale of thousands of submissions, corresponding to hundreds of authors whose papers are saved from desk-rejection.
- **Practical efficiency.** The sub-minute runtime (≤53.64 s for the largest dataset) removes any operational barrier to deployment, a real concern for conference chairs using this algorithm.

## Weaknesses

### Fatal
None.

### Major
1. **The "LP relaxation" in Definition 4.3 is not a relaxation of the IP in Definition 4.1.** The IP has constraint $Ax \leq b \cdot \mathbf{1}_n$, while the LP uses $Ax \leq (b-1)\cdot\mathbf{1}_n$. Tightening the constraint makes the LP's feasible region a *strict subset* of the IP's feasible region, so the LP optimum is at most (not at least) the IP optimum. This breaks the standard LP-relaxation guarantee (LP optimal ≥ IP optimal), meaning the paper's LP does not provide an upper bound for the IP. The method is better described as a "slack-constrained LP heuristic." While the tighter constraint appears designed to simplify the rounding proof (rounding up $x_l$ by at most 1 cannot increase any row sum above $b$), this design choice is never explicitly justified, and the label "LP relaxation" will mislead readers familiar with LP theory.

2. **No comparison with the exact ILP optimum.** Since the authors already use PuLP for the LP, running PuLP's ILP solver (e.g., CBC) on the same instances would directly measure how much optimality is sacrificed by the rounding step. For the smaller datasets (ICLR 2013–2022, $m \leq 2{,}617$), an exact ILP is tractable in seconds. Without this comparison, the reader cannot know whether the 10–19% improvement over baselines represents, say, 90% or 40% of the possible gain over the IP optimal.

### Minor
1. **The rounding step in Algorithm 3 may have a subtle correctness gap.** Line 14 requires finding $S_i \subseteq (S \cap T_i)$ such that $\sum_{j \in S_i} \tilde{x}_j \geq (1 - x_l)$. After several rounding-up steps, the residual fractional mass in $S \cap T_i$ can be less than $(1 - x_l)$, so no valid $S_i$ exists. The correctness claim (Theorem 4.6) needs to explain why this situation cannot arise — presumably the $(b-1)$ slack in the LP ensures sufficient residual fractional mass, but this argument is not made in the main text.

2. **All experiments are simulated.** ICLR does not enforce per-author submission limits; the $b$ values are applied artificially in simulation. Conferences that do enforce limits (CVPR, AAAI, KDD) have non-public submission records. The paper acknowledges this, but readers should be aware that the effectiveness on actual constrained submissions cannot be directly confirmed.

3. **The improvement is sometimes negligible.** For ICLR 2018–2021 at $b \geq 10$, the relative improvement is 0% in many cases. While the paper explains this by the small tail of prolific authors, the headline "up to 19.23%" is driven by a single cell (ICLR 2024, $b=22$, 30 vs. 21 rejections). A more nuanced framing of when the method helps most would strengthen the contribution.

### Trivial
- Algorithm 4 says "Randomly initialize $x_0$," but the experiments are described as deterministic. This inconsistency should be reconciled.

## Nice-to-Haves
- Adding an exact ILP comparison (even on the smaller years) would quantify the approximation quality of the rounding step.
- A theoretical worst-case or average-case bound on the approximation ratio of the LP+rounding relative to the true IP optimal would sharpen the contribution.
- Providing a brief analysis of the structural conditions (e.g., sparsity of $A$) under which $A$ is totally unimodular — and the LP therefore yields integer solutions directly — would help practitioners anticipate when rounding is needed at all.

## Novel Insights
The core novel observation is that current conference desk-rejection policies (which check authors independently and reject greedily) fail to account for the coupling structure among papers that share multiple authors. By solving a joint IP/LP over all papers simultaneously, the algorithm exploits this structure to save papers that the greedy approaches discard. The empirical finding that improvement scales with conference size (near-zero gain at ICLR 2018 vs. consistent 10–13% at ICLR 2024–2025) implies that the coupling effect becomes meaningful only at larger submission volumes — a practical and actionable insight for conference organizers.

## Suggestions
- Rename Definition 4.3 to something like "slack-constrained LP" or "tightened LP heuristic" to avoid the misleading "LP relaxation" label, and add a sentence explicitly justifying the $(b-1)$ slack.
- Add a column to Table 3 showing the exact ILP optimum (using PuLP/CBC) for each cell where it is tractable, so readers can see the approximation gap of the rounding step.
- Address the potential infeasibility in the rounding step (Algorithm 3, line 14) with either a proof that sufficient fractional mass always exists given the $(b-1)$ LP constraint, or a fallback rule.
- Discuss the sensitivity of the improvement to the power-law structure of author submission counts — does the method help more for heavy-tailed distributions?

## Score and Decision
The paper tackles a practically important, novel problem in AI conference organization with a clean formulation and thorough experiments. Its main weaknesses — the misnaming of the LP, the missing exact-ILP comparison, and the potential correctness gap in the rounding step — are significant but correctable. The empirical contribution (consistent 10–19% improvement on 11 years of real data, sub-minute runtime) is sufficiently compelling to merit acceptance at this stage, though the theoretical framework should be tightened.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>