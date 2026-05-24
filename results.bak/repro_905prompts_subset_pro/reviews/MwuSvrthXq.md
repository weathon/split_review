Now I have a solid calibration picture. Let me synthesize the final review.

## Summary
WeCAN proposes an end-to-end reinforcement learning framework for heterogeneous DAG scheduling with task-pool compatibility constraints. The key contributions are: (1) a weighted cross-attention (WeCA) layer that embeds compatibility coefficients outside the softmax, enabling the architecture to adapt to varying numbers of pools and task types; (2) an LDDGNN for capturing directed acyclic dependencies; and (3) a skip-action mechanism integrated into the single-pass inference setting, with theoretical analysis showing it closes the optimality gap of list scheduling. The method achieves up to 18.1% makespan improvement over the best heuristic and 7.7% over the best neural baseline on TPC-H benchmarks, with inference times comparable to fast heuristics.

## Strengths
- **Strong and well-validated empirical performance:** Tables 1 and 2 show consistent and substantial makespan improvements across TPC-H (real-world) and Computation Graphs (synthetic) benchmarks, with WeCAN-S(256) outperforming both heuristic baselines (HEFT, Tetris, CP, etc.) and neural baselines (PPO-BiHyb, One-Shot) across all dataset scales. The gains are particularly notable given the single-pass inference speed (e.g., 0.15s for TPC-H-30 greedy).

- **Thorough ablation study isolating component contributions:** Table 3 convincingly demonstrates that both the WeCA layers and the LDDGNN are essential — removing WeCA layers collapses performance to near-heuristic levels (0.5% improvement vs. 14.0% for the full model on TPC-H-30), and replacing LDDGNN with standard GAT variants consistently degrades makespan. The inside-vs-outside softmax ablation further validates the specific design choice.

- **Theoretical analysis of the optimality gap with practical validation:** Section 4 provides a clean reduced-space framework showing why list scheduling cannot guarantee optimality, and Theorem 1 establishes that the skip-action design assigns positive probability to optimal solutions. Figure 3 validates the practical impact: on heavy-task instances, skip-enabled WeCAN achieves 8.3% improvement over HEFT while the no-skip variant degrades (-2.3%), directly confirming the theory.

- **Architecture adapts to environment fluctuations:** Figure 2 shows WeCAN maintains robust performance under changes in pool count, pool types, task count, and task types — demonstrating that the WeCA design genuinely leverages environment information rather than overfitting to a fixed training configuration.

- **Well-motivated design for compatibility handling:** The concrete example in Section 3.1 (two tasks with identical attributes but different compatibility profiles) provides a clear, intuitive justification for placing compatibility coefficients outside the softmax rather than inside.

## Weaknesses

### Fatal
None.

### Major
- **Missing comparisons to directly relevant heterogeneous neural schedulers:** The paper cites Zhou et al. (2022), Zhadan et al. (2023), and Wang et al. (2025) as prior work that also addresses heterogeneous DAG scheduling with compatibility coefficients (lines 69-74). These methods are characterized as using averaging-based or fixed-size compatibility embeddings, but they are never included as experimental baselines. Since the paper claims to "outperform state-of-the-art methods," the absence of comparisons with the most recent methods that also model compatibility weakens the SOTA claim. The current neural baselines (PPO-BiHyb 2021, which uses a bi-level approach, and One-Shot 2023, which does not model compatibility at all) do not fully cover the heterogeneous scheduler landscape the paper positions itself within. At minimum, one of the cited heterogeneous schedulers should be included to substantiate the claim that WeCAN's cross-attention design is superior to the averaging-based alternatives.

### Minor
- **Skip-action value demonstrated only on modified heavy-task instances:** The skip-action mechanism is a prominent contribution with dedicated theoretical analysis (Section 4, Theorem 1). However, empirical evidence for its benefit is confined to Figure 3, which uses a modified dataset where 1% of tasks are artificially made "heavy." No skip vs. no-skip ablation is reported for the standard TPC-H or Computation Graphs benchmarks. While the theory predicts the gap manifests most strongly with heavy tasks, showing the comparison on standard benchmarks — even if the effect is small — would strengthen confidence that the skip mechanism does not harm performance when it is not needed and would give a complete picture of its practical value.

- **Gap between Theorem 1(iv) and the parametric skip-score implementation:** Theorem 1(iv) states that "there exist scores enabling an optimal solution" via greedy selection. However, the actual implementation constrains the skip score to the parametric form \(u_a(1-k/2n)^{u_b} + u_c\) with only three scalar parameters produced by a global MLP. The theorem is an existence result over an unrestricted score space, while the implementation uses a heavily restricted parametric family. The paper does not discuss whether this parametric family is expressive enough to realize the optimal schedules whose existence is proved, creating a gap between the theoretical guarantee and the practical algorithm.

### Trivial
None.

## Nice-to-Haves
- Adding a sensitivity analysis for the skip-score parameters \(u_a, u_b, u_c\) (e.g., how performance varies when the MLP producing them is replaced or when the functional form is changed) would strengthen the design justification.
- Specifying how compatibility coefficients are generated for the TPC-H and Computation Graphs datasets would aid reproducibility and clarify the generality of the heterogeneous setting.
- Showing skip vs. no-skip ablation on the standard (non-heavy) benchmarks would complete the evaluation picture.

## Removed Points
*These points are flagged to be removed — treat them with caution.*

- **Training hyperparameters, network sizes, and computational budget not described in the main paper (from Harsh Critic):** REMOVED per hard rule — these are standard appendix material and the paper references Appendices D, E, H for experimental details. Undisclosed hyperparameters are a trivial reproducibility concern that does not affect the paper's contribution assessment.

- **Harsh Critic's assertion that the theoretical guarantee is a "fatal" or "structural" overclaim:** DEMOTED to Minor. The Theorem 1(iv) claim is an existence result, which is standard in this type of analysis. The gap between existence and parametric learnability is real but is a standard theory-practice tension, not a fatal error. The theorem does not claim the MLP can achieve the scores — it claims they exist.

## Novel Insights
The reduced-space framework in Section 4 — characterizing generation maps via the composition \(TS\) and using surjectivity as a criterion for whether a map can reach optimal solutions — is a conceptually clean lens for analyzing scheduling algorithms. The observation that list scheduling fails because \(TS_{list}\) is not surjective, and that adding skip actions makes the composition surjective while clustering poor solutions in high-\(u_a\), high-\(u_c\) regions, is a genuinely insightful way to bridge theory and algorithm design in neural scheduling.

## Suggestions
- Add at least one of the cited heterogeneous neural schedulers (Zhou et al. 2022, Zhadan et al. 2023, or Wang et al. 2025) as a baseline. Even a partial comparison on a subset of benchmarks would substantially strengthen the SOTA claim.
- Report skip vs. no-skip performance on the standard TPC-H and Computation Graphs benchmarks, even if the difference is small. This would provide a complete picture and address the concern that the skip mechanism's benefit is limited to contrived scenarios.
- Discuss the expressivity of the parametric skip-score family relative to Theorem 1(iv), or soften the theorem statement to clarify that it applies to an idealized score space.

## Score and Decision

**Round 1 bracket:** Based on comparison with anchors across three bands, WeCAN sits between the mid-band (avg 4.25-5.00 for pipeline parallelism / parallel CO environments) and the top-band anchors (avg 8.00 on unrelated topics). Initial bracket: **5.5–7.5**.

**Round 2 narrowing:** Compared against:
- `jsWCmrsHHs` (avg 7.50, DRL for JSSP): WeCAN is somewhat weaker — the JSSP paper has stronger theoretical guarantees (proven linear complexity), broader benchmark coverage, and a cleaner theory-practice connection. 
- `WfxPVtYRlL` (avg 6.25, GNNs Gone Hogwild): WeCAN is comparable or slightly stronger — both have novel architectures with theoretical backing, but WeCAN has real-world dataset evaluation and more thorough ablation, while the GNN paper has experiments primarily on synthetic tasks.
- `yEwakMNIex` (avg 6.25, Unified Neural Solvers for TSP): WeCAN is comparable in contribution level.
- `jKhNBulNMh` (avg 6.67, Symbolic Discovery for CO): WeCAN is slightly below this in novelty and evaluation comprehensiveness.

WeCAN has genuine technical contributions (WeCA, LDDGNN, skip-action theory), strong empirical results, and thorough ablation. The main weaknesses — missing heterogeneous scheduler baselines and limited skip-action evaluation — are real but not fatal. The paper is above the 6.25 accept threshold and has clear value.

**Final score: 6.5**, positioned between the GNN Hogwild paper (6.25) and the JSSP paper (7.50), closer to the former.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>