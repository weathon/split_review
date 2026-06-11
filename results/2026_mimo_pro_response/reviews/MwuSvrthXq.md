Now I have enough calibration data. Let me finalize the review.

**Calibration Analysis:**

Round 1 bracketing:
- Score 3.0: FJSP RL paper (rejected) - weaker framework, missing ablations, underperforms metaheuristics
- Score 5.75: Multi-task routing (rejected) - simple novelty, missing baselines
- Score 6.0: Sequential stochastic CO (accepted) - novel formulation but design choices poorly justified
- Score 7.5: DRL JSSP improvement (accepted) - novel GNN, comprehensive evaluation, strong results
- Score 8.0: Geometry-aware RL / DeepLTL / FlexPrefill (all accepted) - top-tier papers

Round 2 narrowing (6.5-8.0):
- Score 6.67: Deep Symbolic Discovery (accepted) - branching for CO
- Score 7.0: Multi-objective CO (accepted) - neat weight embedding
- Score 7.5: DRL JSSP (already seen)

**Initial bracket: between 6.5 and 8.0**

WeCAN is clearly stronger than the 3.0 FJSP paper (better results, better theory, better ablations), stronger than the 5.75 multi-task routing paper (stronger novelty, better evaluation), and stronger than the 6.0 SSCO paper (more comprehensive, better theoretical contribution). It's comparable to the 7.0 multi-objective CO paper (both have novel architectures, comprehensive experiments, similar weakness severity). The JSSP paper at 7.5 is the closest anchor — both have novel architectures, comprehensive evaluations, strong results, and comparable weakness severity.

WeCAN's theoretical contribution (surjection framework, Theorem 1) gives it an edge over the 7.0 paper, placing it at 7.5 alongside the JSSP paper.

---

## Summary

This paper presents WeCAN, an end-to-end RL framework for heterogeneous DAG scheduling that introduces (1) a Weighted Cross-Attention (WeCA) layer placing compatibility coefficients outside softmax normalization, (2) a Longest Directed Distance GNN (LDDGNN) for dependency encoding, and (3) a skip action mechanism in a single-pass architecture to close the optimality gap of list scheduling. Experiments on TPC-H and Computation Graphs datasets show up to 18.1% improvement over best heuristics and 7.7% over best neural baselines, with inference time competitive with heuristics.

## Strengths
- **Well-motivated WeCA architectural design**: The outside-placement of compatibility coefficients is theoretically justified with a clear motivating example (lines 125-126: tasks with identical attributes but different compatibility profiles become indistinguishable with inside-placement) and empirically validated through ablation (Table 3: 14.0% vs 10.5% improvement for outside vs inside placement on TPC-H-30).
- **Formal theoretical analysis of list scheduling's optimality gap**: The surjection framework (Assumption 1, Theorem 2) provides a reusable analytical criterion for generation maps, and Theorem 1 proves that skip actions restore the optimality guarantee that list scheduling alone lacks. Figure 3 empirically validates this: WeCAN with skip achieves 8.3-8.9% improvement over HEFT on heavy-task variants while the non-skip variant underperforms by 2.3%.
- **Strong empirical results with practical efficiency**: Up to 18.1% makespan improvement over best heuristics on TPC-H and 13.4% on Computation Graphs (Tables 1-2). WeCAN-Greedy achieves 136x speedup over PPO-BiHyb (0.15s vs 20.48s) while delivering better makespan on TPC-H-30.
- **Generalization across environment configurations**: Figure 2 shows WeCAN maintains 6.7-20.4% improvement when varying pool count, pool type, task count, and task type under fixed training conditions, substantially outperforming One-Shot (0.9-10.2%).
- **Comprehensive ablation study**: Table 3 systematically isolates contributions of each component across 7 architectural variants, showing all components contribute meaningfully.

## Weaknesses

### Fatal
None

### Major
None

### Minor
- **Skip action formula is ad-hoc.** The specific parametric form $u_{\pi_{skip}} = u_a(1 - k/2n)^{u_b} + u_c$ (line 145) lacks theoretical derivation. Theorem 1(iv) guarantees existence of *some* scores enabling optimal greedy selection but does not establish this particular parametric family can represent them. A sensitivity analysis or comparison with alternative forms (e.g., linear decay) would strengthen the claim that the design matters, not just the existence of a skip mechanism.
- **Limited neural baselines.** Only PPO-BiHyb and One-Shot are compared (line 218), while several recently cited heterogeneous scheduling methods (Zhou et al. 2022, Grinsztajn et al. 2021, Zhadan et al. 2023, Wang et al. 2025) are not included in experiments. Adding at least one more would better contextualize the improvements.
- **Non-autoregressive design tradeoff not discussed in main text.** Action scores are computed from initial state $s_1$ and remain fixed throughout schedule construction (line 137). The paper mentions comparison with autoregressive variant in Appendix B but doesn't discuss in the main text why this works well or when it could hurt—a missed opportunity to strengthen credibility.
- **All primary experiments use 3 pools** (line 216). While Figure 2 shows generalization across varying pool numbers, the main result tables (Tables 1-2) only test 3 pools. Including 5-10 pools in main tables would strengthen the heterogeneous scheduling claims.

### Trivial
None

## Nice-to-Haves
- Ablation of skip action on main datasets (not just heavy-task variants) to clarify whether skip helps in standard settings.
- Training curves or convergence analysis for the REINFORCE training.
- Discussion of when fixed non-autoregressive scores could underperform autoregressive approaches.

## Removed Points
- Proofs in appendix — the parser strips appendix content; these exist in the original submission.
- Notation typo $F(t, v)$ vs $F(t, c)$ at line 87 — trivial formatting issue, carries no weight.
- No training method comparison (REINFORCE vs PPO/A2C) — this is a nice-to-have, not a core weakness.

## Novel Insights
The paper's most novel contribution beyond its architecture is the formal characterization of list scheduling's optimality gap through the surjection framework. The insight that list scheduling's image excludes optimal solutions because $TS_{list}$ is neither identity nor surjective, and that skip actions can restore surjectivity while preserving single-pass efficiency, provides a principled theoretical foundation for an important practical mechanism. This framework (Assumption 1, Theorem 2) is reusable for analyzing other list-scheduling-based approaches.

## Suggestions
- Add at least one additional neural baseline for heterogeneous scheduling comparison.
- Include results with more than 3 pools in the main experimental tables.
- Add a brief sensitivity analysis on the skip score parametric form.
- Discuss the non-autoregressive design tradeoff in the main text.

## Anchor Papers Retrieved

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| Uj0h13lVrR.md (GFlowNets) | 1.00 | 1 | Much weaker; flawed methodology |
| nSDOkm0SKo.md (Financial NN) | 1.00 | 1 | Much weaker; toy problem |
| bEgDEyy2Yk.md (Minimax path) | 1.00 | 1 | Much weaker; implementation only |
| 10eQ4Cfh8p.md (FJSP RL) | 3.00 | 1 | Weaker; missing ablations, underperforms metaheuristics |
| Gs8jWk0F01.md (Dynamic CVRP) | 2.20 | 1 | Weaker; limited novelty |
| bntJK4NyIW.md (Decentralized Training) | 2.00 | 1 | Weaker; different topic, limited results |
| 8WtBrv2k2b.md (Quantum Scheduling) | 5.00 | 1 | Weaker; less comprehensive evaluation |
| b9aCXHhdbv.md (Pipeline Parallelism) | 4.50 | 1 | Weaker; less rigorous |
| CJEBFNBLhO.md (Parallel CO Envs) | 4.25 | 1 | Weaker; infrastructure paper |
| jBYQAtzp5Z.md (Fair Scheduling) | 6.80 | 1 | Comparable topic but theoretical focus; WeCAN stronger empirically |
| DKfcxPxunu.md (Multi-task Routing) | 5.75 | 1 | Weaker; simple novelty, missing baselines |
| AloCXPpq54.md (Sequential Stochastic CO) | 6.00 | 1 | Weaker; poorly justified design choices |
| 7BLXhmWvwF.md (Geometry-aware RL) | 8.00 | 1 | Stronger; top-tier robotics RL |
| 9pW2J49flQ.md (DeepLTL) | 8.00 | 1 | Stronger; top-tier RL formal methods |
| OfjIlbelrT.md (FlexPrefill) | 8.00 | 1 | Stronger; top-tier efficient inference |
| jsWCmrsHHs.md (DRL JSSP) | 7.50 | 1 & 2 | **Closest anchor.** Comparable novelty, evaluation, and results. Both accepted. |
| CpiJWKFdHN.md (ROS Max-k-Cut) | 5.67 | 2 | Weaker; less comprehensive |
| CFLEIeX7iK.md (Neural Solver Selection) | 5.75 | 2 | Weaker; meta-level contribution |
| jKhNBulNMh.md (Symb4CO) | 6.67 | 2 | Weaker contribution scope |
| GM7cmQfk2F.md (MOCO Weight Embedding) | 7.00 | 2 | Comparable quality; WeCAN has stronger theoretical contribution |
| 9EfBeXaXf0.md (Quasi-Quantum Annealing) | 6.75 | 2 | Different approach; WeCAN stronger |

**Bracket**: Initial bracket was [6.5, 8.0]. After Round 2, narrowed to [7.0, 7.5]. WeCAN is comparable to the DRL JSSP paper (7.5, accepted) — both have novel architectures, comprehensive evaluations, and strong results. WeCAN's theoretical contribution (surjection framework) gives it a slight edge over the 7.0 MOCO paper. Settled at 7.5.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>