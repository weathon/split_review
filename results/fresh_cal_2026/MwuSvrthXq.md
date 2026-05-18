Now I have sufficient calibration data. Let me synthesize my final review.

**Round 1 bracket:** Based on the most comparable papers (GAA-PtrNet at 4.50, RESCHED at 5.00, DEFT at 5.00, YAgOaYedLQ at 5.50), the paper sits in the 4.5–6.5 range.

**Round 2 narrowing:** The paper is clearly stronger than GAA-PtrNet (4.50, Reject) — it has better empirical gains, a genuine theoretical contribution, and cleaner architectural novelty. It is comparable to or slightly better than RESCHED (5.00), DEFT (5.00), and YAgOaYedLQ (5.50), which were all accepted as posters despite having similar kinds of weaknesses (missing ablations, limited baselines). The paper does not match the polish of NfWrLOKnfk (6.50) which had very clean experimental validation and was accepted. **Final score: 5.5**.

---

## Summary

This paper proposes WeCAN, an end-to-end reinforcement learning framework for heterogeneous DAG scheduling with task-resource compatibility coefficients. The key ideas are: (1) a weighted cross-attention (WeCA) layer that places compatibility coefficients outside softmax to preserve discriminative signal, (2) a longest-directed-distance GNN (LDDGNN) for dependency embedding, and (3) a skip action mechanism that operates within a single network forward pass, supported by a theoretical analysis showing that skip actions can close the optimality gap inherent in list scheduling. Experiments on TPC-H and Computation Graphs datasets show consistent improvements over heuristic and neural baselines (7–18%) with inference times competitive with heuristics.

## Strengths

1. **Principled weighted cross-attention design (Section 3.1).** The decision to place the compatibility coefficient outside (multiplying after) softmax rather than inside (as a log bias) is clearly motivated with a concrete example showing that inside placement would normalize away the distinction between tasks that differ only in their number of compatible pools. This is a non-obvious architectural choice with a clear rationale.

2. **Theoretical analysis of the list-scheduling optimality gap (Section 4).** The paper formally defines the reduced space and generation maps, proves that list scheduling is not surjective onto the optimal schedule (Theorem 1(iii)), and shows that the skip-augmented design can cover the optimal solution (Theorem 1(iv), Theorem 2). This goes beyond the typical empirical-only scheduling paper and provides a principled framework for understanding why skip actions help.

3. **Consistent and substantial empirical gains.** On TPC-H-30, WeCAN-S(256) achieves makespan 18,964 vs. the best heuristic (Tetris at 23,170, −18.1%) and the best neural baseline (One-Shot-S(256) at 20,399, −7.0%). Similar margins hold across TPC-H-50, TPC-H-100, and all three Computation Graph types (Tables 1 and 2). Inference time (2.43s for 256 samples) is competitive with heuristics and far below PPO-BiHyb (20.48s).

4. **Ablation study isolating architectural contributions (Table 3).** The paper systematically ablates the WeCA placement (outside vs. inside), the presence of WeCA at different stages, and the GNN choice (LDDGNN vs. GAT variants). Each variant increases makespan, providing controlled evidence for the design decisions.

5. **Robust generalization to environment fluctuations (Figure 2).** Models trained on a fixed environment maintain 6.7–20.4% improvement over the best heuristic when tested on different pool counts, pool types, task counts, and task types, where One-Shot degrades to 0.9% under pool-type changes.

## Weaknesses

### Fatal
None.

### Major

1. **Missing direct ablation of the skip action.** The skip action is a central contribution — the paper argues it closes the optimality gap and improves performance on heavy-task cases. Yet the main experiments contain no apples-to-apples comparison between WeCAN *with* skip and WeCAN *without* skip, holding all other architectural choices fixed. Table 3 ablates cross-attention placement and the graph encoder but never removes the skip mechanism. Figure 3 compares on heavy-task datasets but the "non-skipping variant" is not clearly identified (the legend shows duplicated "WeCAN-S(256)" entries, likely a formatting artifact). Without this ablation, the empirical evidence for the skip action's benefit is substantially weaker than it should be for a paper that elevates skip as a first-order contribution. The paper's theoretical analysis establishes existence of optimal solutions via skip, but the clean empirical link is missing.

2. **No comparison with optimal solutions on small instances.** Theorem 1 is an existence result (there *exist* scores enabling an optimal solution via greedy selection with skip). The paper does not verify on small problems where the MILP optimum is tractable that the learned policy actually approaches this optimum. This would directly demonstrate the claimed gap-closing in practice. Without it, the empirical story for skip remains incomplete.

### Minor

3. **Incomplete comparison with recent heterogeneous schedulers.** The introduction cites multiple neural schedulers for heterogeneous environments (Zhou et al. 2022, Wang et al. 2025, Zhadan et al. 2023, Grinsztajn et al. 2021) but does not include them in experiments. The claim of "outperforming state-of-the-art methods" is weakened when the most directly comparable prior work is absent. The paper should either include these comparisons or acknowledge the limitation and discuss how the method differs.

4. **Limited generalization validation scope.** The environment fluctuation experiments (Figure 2) are conducted only on TPC-H-30 and lack error bars/statistical tests. While the paper references Appendix F for additional results, the main-text evidence for generalization beyond one base dataset is thin. Adding at least one additional real-world benchmark (e.g., Pegasus workloads) would substantially strengthen this claim.

### Trivial

5. **Figure 3 duplicated legend entries.** The legend shows two "WeCAN-S(256)" bars, which is confusing. The paper claims "WeCAN with the skip action achieves lower makespan than its non-skipping variant" but the non-skipping variant cannot be identified in the figure as rendered. This needs correction.

6. **Skip score formula appears ad-hoc.** The formula \(u_a(1 - \frac{k}{2n})^{u_b} + u_c\) is justified with an intuitive explanation ("prevents the skip action from being overly prioritized") but no analysis of whether the form is learnable or whether simpler alternatives would suffice. This is a minor concern since the formula works in experiments.

## Nice-to-Haves
- **Optimality gap verification on small synthetic instances.** Solving small DAGs to optimality (via MILP) and showing WeCAN with skip recovers or approaches the optimum would directly validate the theory.
- **Wider range of pool counts in generalization experiments** (e.g., 2, 5, 10 pools) and additional real-world benchmarks (e.g., Pegasus workflows, HPC2N traces).
- **Statistical significance tests** on the environment fluctuation results.

## Removed Points
- *Criticism about the skip action claim being "rest[ing] on analysis alone, with no clean empirical support"* — While the missing direct ablation is a real weakness (retained as Major #1), the paper does provide *some* empirical evidence via the heavy-task experiments in Figure 3 and the Appendix C reference. The original framing overstates the absence of evidence. The retention is as Major #1 with appropriate nuance.
- *Criticism about PPO-BiHyb and One-Shot being "insufficient" baselines* — The paper compares against two strong neural baselines (One-Shot from ICLR 2023, PPO-BiHyb from NeurIPS 2021) plus five heuristics. This is a reasonable baseline set. The concern about additional heterogeneous schedulers is retained (Minor #3) but scaled down from the original framing.
- *Weakness about "no ablation quantifying individual contribution of skip action"* — Already merged into Major #1.
- *Weakness about clustering of poor solutions in high-\(u_a, u_c\) region not being analyzed* — This is a theoretical claim in the analysis section; while the paper could provide more empirical verification, this is a secondary claim rather than a core weakness.
- *Strength about "rigorous theoretical analysis"* — Retained but scaled to context: the analysis is well-structured but is an existence result, not a learning guarantee.
- *Strength about LDDGNN outperforming GAT* — Retained as it is backed by Table 3.

## Novel Insights

None beyond the paper's own contributions. The two reviewer inputs largely agree on the core strengths (WeCA design, theoretical analysis, strong empirical results) and weaknesses (missing skip ablation, limited baselines). The harsh critic's deep concern about the skip-action evidence gap is the genuinely penetrating observation; the strength finder's catalog is accurate but does not surface anything the paper's own text does not already convey.

## Suggestions

1. **Add a direct skip-action ablation.** Train WeCAN without the skip action (always pick a task when available, never idle) on the same datasets and report makespan and variance. This is the single highest-leverage experiment to validate the paper's central claim.
2. **Add a small-instance optimality study.** Solve small synthetic DAGs (10–30 tasks) to MILP optimality and show that WeCAN with skip finds solutions closer to the optimum than list-scheduling variants, demonstrating the gap is closed in practice.
3. **Include or acknowledge missing heterogeneous schedulers.** Add at least one recent heterogeneous scheduler baseline (Zhou et al. 2022, Wang et al. 2025, or Zhadan et al. 2023), or add a limitations paragraph explaining why these are impractical to compare against.
4. **Fix Figure 3 legend duplication** and explicitly label the non-skipping variant.
5. **Add error bars to environment fluctuation experiments** (Figure 2).

## Score and Decision

**Calibration anchors across all rounds:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|-----------|
| Ikjxsa5RHD (RL distributed scheduling) | 2.50 | 1 | Much weaker; rejected for vague modeling and simple handcrafted rewards |
| e1osUquspZ (BJSP hierarchical optimizer) | 3.00 | 1 | Much weaker; limited to small-scale instances |
| bisWxwcK8D (RL vehicle routing) | 2.50 | 1 | Different domain, weaker contribution |
| t0fU6t3Skw (LLM job shop scheduling) | 2.50 | 1 | Different approach, weaker results |
| UbWy2QVmke (GAA-PtrNet, one-shot DAG) | 4.50 | 1/2 | Less empirical improvement, less theoretical depth; WeCAN is stronger |
| s5pWbwf2tk (RESCHED, FJSP) | 5.00 | 1/2 | Comparable contribution but had 5000× training data concern; WeCAN is cleaner methodologically |
| yVFOdLjd7V (DEFT, cloud workflow) | 5.00 | 2 | Similar missing-ablation weakness; comparable |
| YAgOaYedLQ (Multi-objective FJSP) | 5.50 | 1/2 | Similar missing-baselines weakness; WeCAN's theoretical contribution is stronger |
| qRjLjYrvMi (Foundation model scheduling) | 6.00 | 1/2 | More ambitious scope but split reviews (8,4,4,8); WeCAN is more focused and cleaner |
| NfWrLOKnfk (SAT solver guidance) | 6.50 | 2 | Different domain, cleaner experimental validation; WeCAN is weaker |
| Zcn4n57lHg (Scheduling with predictions) | 6.00 | 2 | Different subproblem (online with predictions); WeCAN is comparable on its own terms |
| zsNUc2iMzp (LMask constrained routing) | 6.00 | 2 | Different problem (routing); WeCAN is comparable |
| 9gw03JpKK4 (Gaia2 LLM agents) | 8.00 | 1 | Different domain entirely |
| oBXfPyi47m (RL world models) | 8.00 | 1 | Different domain entirely |

**Round 1 bracket:** 4.5 – 6.5  
**Round 2 narrowing:** The paper is stronger than GAA-PtrNet (4.50) due to better empirical margins and genuine theoretical contribution, and comparable to RESCHED (5.00), DEFT (5.00), and YAgOaYedLQ (5.50) — all accepted as posters despite similar weaknesses. It does not reach the experimental rigor of the 6.50 anchor.  
**Final score: 5.5**

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>