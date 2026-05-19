- Decision: Reject
- Avg Score: 5.67
- Scores: 5, 6, 6
Now I have a thorough understanding of the paper and can verify all reviewer claims against the actual text. Let me compose the final consolidated review.

---

## Summary

This paper proposes UniAP, an automatic parallelism method that formulates the joint optimization of inter-layer (pipeline parallelism) and intra-layer (data, tensor, and fully-sharded data parallelism) strategies as a mixed integer quadratic programming (MIQP) problem. Unlike prior hierarchical approaches that optimize these two categories separately, UniAP uses a unified MIQP formulation solved by the Gurobi optimizer, supported by a profiling-based cost model. Experiments across five Transformer models and multiple cluster configurations show throughput improvements up to 3.80× over Galvatron and Alpa, and strategy optimization time reductions up to 107×.

## Strengths

- **Novel unified MIQP formulation for joint parallel strategy optimization.** Section 3.3 presents a single objective (Equation 1) and accompanying constraints (Equations 2–9) that simultaneously determine pipeline stage placement, micro-batch splitting, and per-layer intra-layer strategy selection (DP, TP, FSDP). Prior work (Alpa, Galvatron) treats these hierarchically; the paper demonstrates this is the first formulation to optimize them jointly.

- **Substantial throughput gains over state-of-the-art baselines.** Table 1 reports up to 3.80× throughput improvement (Llama-7B on EnvC: 4.63 samples/s vs. Galvatron's 1.22 samples/s). On EnvB, UniAP achieves 10.77 samples/s vs. Alpa's 8.95 and Galvatron's 6.27 for BERT-Huge (1.20–1.71×). These gains are material and well-documented with standard deviations.

- **Dramatically faster strategy optimization.** Table 1 shows UniAP's optimization time is 0.37 minutes for BERT-Huge on EnvA vs. Alpa's >40 minutes (>107×) and Galvatron's 6.44 minutes (17.29×). The trend holds across models and environments, with typical speedups of 2–17× over Galvatron.

- **Ablation study cleanly validates the core thesis.** Table 2 shows that restricting to inter-layer-only yields infeasible solutions (OOM) for BERT-Huge and T5-Large, while intra-layer-only drops throughput to 2.48 and 2.92 samples/s vs. UniAP's jointly optimized 10.77 and 9.01. This directly confirms that joint optimization is necessary, not merely beneficial.

- **Cost model achieves low relative estimation error (3.59% vs. 11.17% for Galvatron).** Section 4.2 demonstrates accurate cost estimation, which is critical for the MIQP solver to produce trustworthy solutions.

- **Handles models that baselines cannot.** UniAP finds feasible strategies for Swin-Huge on EnvA where Galvatron hits CUDA OOM and Alpa has no working implementation.

## Weaknesses

### Fatal
None.

### Major

- **Unqualified "optimal solution" claims.** The abstract, introduction bullet points, and conclusion all state that UniAP "can jointly optimize the two categories of parallel strategies to find an optimal solution." However, the MIQP formulation includes products of binary variables (Equation 2: $P_{ui}P_{vi}(S_u^\mathsf{T}R_{uv}S_v)$ — trilinear in binary variables) and a piecewise-linear max operator in the objective. While these can be linearized for binary variables, the paper does not discuss whether Gurobi certifies global optimality within the configured time limit, nor does it report optimality gaps for instances that terminate without proof of optimality. The complexity analysis (Section 3.5) also sidesteps this by treating the solver time limit as a constant. The practical results are strong, but the "optimal" framing is overstated without empirical characterization of solver behavior. The paper should (a) soften these claims to "highly optimized" or "near-optimal," (b) report the proportion of instances solved to proven optimality, and (c) report average optimality gaps for those that are not.

### Minor

- **Optimization time comparison apples-to-apples is unclear.** Section 4 reports UniAP's strategy optimization time as "the time of the UOP" (Algorithm 1), which excludes profiling (a separate step described in Section 3.1). For Alpa, times are reported as ">40" minutes. The paper does not specify whether Alpa's reported time includes compilation, JIT tracing, and profiling overhead. If the baselines' times include these components while UniAP's does not, the claimed >107× speedup could be an overstatement. The paper should clarify what each baseline's timing includes and attempt to measure the search component alone, or report end-to-end times including profiling.

- **Scalability results on EnvE are underreported.** Section 4.3 gives only one sentence: "UniAP also outperforms other baselines in this experiment." Given that EnvE uses 8 nodes with DCU accelerators (a non-NVIDIA architecture), including throughput numbers and optimization times in a table or figure would substantially strengthen the generality claim.

- **No limitations section.** The paper lacks a dedicated discussion of limitations. Key items that should be acknowledged: (a) the MIQP solver's optimality guarantees may not hold for all instances, (b) the enumeration loop in Algorithm 1 assumes a homogeneous cluster where pp_size divides n — heterogeneous topologies are not supported, (c) the cost model errors (3.59% REE) mean the solver's "optimal" strategy is optimal with respect to an approximate model, not necessarily the true runtime.

- **Ablation study provides no explanation for why inter-only fails.** Table 2 reports "SOL×" (no solution found) for BERT-Huge and T5-Large under inter-only constraints, and CUDA OOM for ViT-Huge under intra-only. The paper does not analyze whether these failures stem from activation memory, parameter memory, or pipeline bubble constraints. Brief diagnostic detail would strengthen the ablation.

- **REE reported only for the final optimal strategies.** Section 4.2 reports 3.59% average REE for the strategies UniAP selects. Reporting REE across all candidate strategies evaluated during search would better characterize whether the cost model reliably ranks candidates (not just the top one).

- **The complexity analysis under-represents solver time.** Section 3.5 derives complexity $\mathcal{O}(|V||S|\sqrt{Bd})$ by treating the MIQP solver's time limit as a constant. While technically valid as an upper bound, this hides the fact that the solver dominates runtime in practice. A more honest characterization would note that each solver call may take up to the configured time limit, and discuss how the time budget is chosen.

### Trivial
None.

## Nice-to-Haves

- Provide a small-scale example (e.g., 6-layer model on 4 GPUs) contrasting the hierarchical solution trajectory with the joint MIQP solution, showing the objective-value gap and explaining why the joint solution wins.
- Add an ablation simulating the exact hierarchical approach: first fix intra-layer strategies greedily per device, then solve for PP, then compare throughput to the joint solution.
- Clarify that Gurobi's `NonConvex` parameter is not needed since binary-variable products are linearizable, or state which parameters are used.

## Removed Points

These points are flagged to be removed — treat them with caution:

1. **"Pipeline scheduling strategy is ambiguous" (Harsh Critic #2).** The paper explicitly states at line 110: "In this paper, we have chosen GPipe as our PP strategy for illustration." The critic claimed experiments never state this, which is factually incorrect.

2. **"Missing comparison with FlexFlow as a joint-optimization baseline" (Harsh Critic #3).** The paper correctly categorizes FlexFlow as intra-layer-only AP (Section 2, line 53: "FlexFlow ... uses the Monte Carlo method to find the optimal DP and TP strategy. ...[A]ll these methods optimize only one category of parallel strategies.") FlexFlow does not include pipeline parallelism, so it does not jointly optimize inter- and intra-layer strategies — it is not a relevant baseline for this claim.

3. **"Complexity analysis misleading because it treats solver time as constant" (part of Critic #1).** The paper explicitly states "the optimization time limit of the MIQP solver can be set as a constant hyperparameter" (line 214). Treating a bounded time limit as constant is standard for complexity analysis of iterative algorithms. The concern about practical runtime being solver-dominated is valid and has been preserved in the Minor section with softened wording.

4. **"Bilinear/nonconvex formulation means it is not standard MIQP" (part of Critic #1).** Products of binary variables can be exactly linearized; Gurobi handles this internally. The max operator can be reformulated with auxiliary variables and linear constraints. The problem is a standard MIQP (or reducible to one). This claim is technically incorrect as stated.

5. **"Heterogeneous cluster enumeration limitation" (Critic's Section 3.4 note).** The paper acknowledges this scope (line 207: "These enumerations aim to achieve load balance on a homogeneous cluster") and heterogeneous memory is supported (line 140). This is an acknowledged scope limitation, not an oversight.

6. **Strength Finder generic strengths.** The Strength Finder's "addressed an important problem" framing is generic; all concrete strengths have been kept above.

## Novel Insights

None beyond the paper's own contributions. The two reviewer inputs largely converge on the same picture: the MIQP formulation is novel and the empirical results are strong, but the "optimal solution" framing needs qualification, and some experimental details (timing breakdown, EnvE results) could be clearer. No reviewer identified an unclaimed insight or contradiction that the paper itself does not surface.

## Suggestions

- **Replace "optimal solution" with "highly optimized solution"** or add a clear qualifier: "the solver returns the best solution found within a configurable time budget, with optimality certification when convergence is reached." Report the fraction of instances solved to proven optimality and the average MIP gap for partial solves.
- **Clarify what each baseline's optimization time includes.** Explicitly state whether Alpa's ">40 min" includes compilation/JIT overhead, and whether Galvatron's times include profiling. If possible, measure only the search component for a fairer comparison, or report end-to-end (profiling + search) times for all methods.
- **Add a Limitations paragraph** addressing: (a) solver optimality caveats, (b) homogeneous cluster assumption for PP enumeration, (c) cost model approximation error — the "optimal" strategy is optimal w.r.t. an estimated cost, not ground-truth runtime.
- **Report detailed EnvE results** (throughput and optimization time) in a table, not just the single sentence in Section 4.3.
- **Diagnose ablation failures.** For Table 2, add a brief explanation of why inter-only yields "SOL×" (e.g., "activation memory per stage exceeds the 12GB limit because pipeline stages cannot be further subdivided without intra-layer sharding").
