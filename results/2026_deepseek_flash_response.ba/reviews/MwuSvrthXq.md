Now I have strong calibration. Let me write the final review.

## Summary

This paper proposes WeCAN, an end-to-end RL framework for heterogeneous DAG scheduling with task-pool compatibility. The core contribution is a weighted cross-attention (WeCA) layer that places compatibility coefficients outside softmax, allowing the architecture to handle varying numbers of pools/task types without retraining. The paper also provides a formal analysis of the optimality gap in list scheduling and introduces a skip-action mechanism in a single-pass setting. Empirical results on TPC-H and Computation Graphs benchmarks show up to 18.1% improvement over heuristic baselines and competitive runtime.

## Strengths

- **Weighted cross-attention design with principled motivation and validation**: The WeCA layer (Section 3.1, Eq. 2) integrates compatibility coefficients as `diag{K_acc(v, c(1)), ..., K_acc(v, c(n_c))}` multiplied outside softmax, so the number of pools can vary without retraining. The paper gives a concrete example of why outside placement matters (two tasks with identical attributes but different compatibility profiles). The ablation study (Table 3) validates this: the "inside" variant increases makespan by ~4%, and removing WeCA layers degrades improvement from 14.0% to 0.5%. This is a clean architectural improvement over prior fixed-size embedding approaches.

- **Strong empirical results across multiple benchmarks and problem sizes**: On TPC-H-30 (Table 1), WeCAN-Greedy achieves makespan 19578 in 0.15s—beating the best heuristic Tetris (23170, 0.21s), One-Shot-S(256) (20399, 2.26s), and PPO-BiHyb (21941, 20.48s). On Computation Graphs (Table 2), WeCAN-S(256) achieves 10083 on Erdős-Rényi graphs vs 11071 for One-Shot-S(256), with 4.94s runtime vs 65.51s for PPO-BiHyb. Results hold across problem sizes up to ~918 tasks (TPC-H-100).

- **Systematic ablation that disentangles architectural contributions**: Table 3 tests seven architectural variants controlled for layer count and hidden dimension. Results show that (a) outside placement of K_acc outperforms inside, (b) WeCA layers in the encoder matter more than in the decoder, (c) LDDGNN outperforms GAT forward and bidirectional variants, and (d) the WeCA-final-only variant degrades to near-baseline performance. This level of disentanglement allows attribution of improvements to specific design decisions.

- **Generalization experiments demonstrating adaptability**: Figure 2 tests four types of environmental fluctuation (more pools, more pool types, more tasks, more task types). WeCAN-S(256) maintains 6.7–20.4% improvement over best heuristics while One-Shot drops to 0.9–10.2%, with the gap starkest under "more pool type" (6.7% vs 0.9%).

- **Formal framework for analyzing list scheduling's optimality gap**: The reduced-space analysis (Section 4, Theorems 1 and 2) provides a clean formal vocabulary (A, B, T, S) for characterizing when list scheduling fails, and motivates why skip actions help. While the guarantees are expressiveness results rather than learning guarantees, the theoretical framing is a genuine conceptual contribution over prior heuristic-level analysis.

## Weaknesses

### Major

- **Unclear fairness of the One-Shot baseline comparison undermines the "neural baseline" claim**: The paper's introduction (line 29-31) states that One-Shot "does not consider compatibility coefficients or pool allocation, remaining challenges in highly heterogeneous settings." Yet One-Shot is used as a baseline in the heterogeneous setting with compatibility coefficients. The paper never describes how One-Shot was configured—whether it was given compatibility information, how pools were represented, or whether it was run as-is (which would mean it was denied information WeCAN was given). The headline claim of "7.7% improvement over the best neural baseline" thus rests on potentially asymmetrical ground. The stronger claim against heuristic baselines (HEFT, Tetris) that DO handle heterogeneity—up to 18.1% improvement—stands on firmer ground, so the paper's core empirical contribution is not invalidated, but the neural-baseline comparison needs clarification.

### Minor

- **Theoretical claims are modestly overstated**: Theorem 1(iv) is an expressiveness result: there *exist* scores enabling optimal solutions. The paper's language ("closes this gap," "fixes the optimality gap" in lines 64-65, 145) implies an operational guarantee about what the learned policy can achieve, which the theorems do not provide (REINFORCE is not proven to find those scores). The theoretical analysis is still a useful conceptual contribution, but the framing should be scoped to reflect that it shows sufficiency of expressiveness, not convergence to optimality.

- **Figure 3 has a labeling error**: The figure caption and table header list two bars both labeled "WeCAN-S(256)" without distinguishing which is the skip variant and which is the non-skip variant. The accompanying text clarifies that "WeCAN with the skip action achieves lower makespan than its non-skipping variant," but the figure itself is ambiguous. This needs correction to serve as clear evidence for the paper's central theoretical claim.

- **Skip score formula lacks ablation against alternatives**: The formula `u_π_skip = u_a(1 - k/(2n))^{u_b} + u_c` (line 145) is introduced without comparison to simpler alternatives (e.g., learned constant threshold, binary classifier, different decay functions). An ablation study varying the functional form would strengthen the paper, though the design motivation (preventing overskip, decaying priority over time) is explained.

- **PPO-BiHyb baseline lacks reported variance**: In Tables 1 and 2, PPO-BiHyb has no standard deviation despite being a stochastic RL method. Its running time (20–179s) is also orders of magnitude higher than other methods (<1–10s), making the comparison less informative.

### Trivial

- The heavy-task experiment uses only a single 1% injection rate without sensitivity analysis. Showing results across multiple proportions would strengthen the theoretical claim that benefits increase with heavy-task proportion.
- The ablation study uses only 10 test problems (line 308). Standard deviations are reported and small, but a larger test set would increase confidence, especially for the WeCA-final-only variant which shows negative improvement on TPC-H-50.

## Nice-to-Haves

- A small concrete DAG example (2–3 tasks, 2 pools) showing where list scheduling fails and skip actions fix it would make Section 4 much more accessible.
- Training details (number of instances, hyperparameters, GPU used, training curves) would help reproducibility; the appendix is stripped so these may already be present.

## Removed Points

- **Running time comparison where WeCAN-Greedy is faster than heuristics** (Harsh Critic point 5): This is not a weakness—it's a strength that the paper could even brag about more. Removed.
- **Generalization experiments (Figure 2) inherit One-Shot fairness concern**: The generalization experiments compare WeCAN vs One-Shot under environmental fluctuations. This inherits the same One-Shot concern noted above. However, the generalization experiment itself is about *relative* robustness to environment change, not absolute performance; the trend comparison is informative even without perfect baseline equivalence. Demoted to be subsumed under the One-Shot concern rather than listed separately.
- **Harsh Critic's "theoretical guarantees are existence theorems, not learning guarantees"** framed as a Critical Issue: This is accurate but overstated. The paper's theory is a standard expressiveness analysis common in ML theory papers. It is a Minor rhetorical issue, not a fatal flaw. Kept but downgraded from the critic's framing.
- **Strength Finder strengths about "addressing important problem"** etc.: Removed generic strengths. The five retained strengths above are all concrete and specific.
- **Parser artifacts, formatting complaints**: Removed per instructions.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Clarify the One-Shot adaptation**: Describe exactly how One-Shot was configured for the heterogeneous setting. If it cannot handle compatibility coefficients at all, consider reframing the neural-baseline comparison or removing the "7.7% over best neural baseline" claim.
2. **Fix Figure 3 labels**: Distinguish "WeCAN-S(256) w/ skip" from "WeCAN-S(256) w/o skip" (or similar) in both the figure and table.
3. **Scope theoretical claims precisely**: Replace "closes the optimality gap" with "the architecture is sufficiently expressive to represent optimal solutions" throughout.
4. **Add skip-score ablation**: Compare the proposed formula against at least one simple alternative (e.g., a learned constant skip score).
5. **Add sensitivity analysis for heavy-task proportions**: Test multiple proportions (0.5%, 1%, 2%, 5%) to validate the theoretical trend.

## Score and Decision

**Initial bracket (Round 1):** The paper sits between weak scheduling-RL papers at ~3.0 and strong theoretical CO papers at ~8.0. Comparison with the FJSP-RL paper (3.0) shows WeCAN is clearly stronger on every dimension. Comparison with PolyNet (5.25, accepted at ICLR) shows WeCAN has similar or better evaluation rigor, ablation studies, and theoretical framing. This places the paper in the 5–7 range.

**Narrowing (Round 2):** Anchors inside the bracket:
- HexGen-2 (6.0, accepted) — heterogeneous scheduling for LLM inference, similar empirical rigor but addressing a trendier topic. WeCAN has cleaner methodology and stronger ablations.
- PolyNet (5.25, accepted) — RL for CO. WeCAN has comparable methodology clarity and better problem-size scalability (918 vs 300 tasks).
- Neural Solver Selection (5.75, rejected) — meta-framework for CO, rejected possibly due to being a framework rather than a solver.
- VColRL (5.0, rejected) — RL for vertex coloring, solid but limited baselines.

WeCAN is comparable to the accepted papers in this range and stronger than several of the rejected ones. The core methodological contribution (WeCA layer) is clean and well-validated. The main weakness (One-Shot fairness) is addressable in rebuttal and does not undermine the broader empirical claims.

**Final calibration:** Setting the score relative to PolyNet (5.25, accepted) and HexGen-2 (6.0, accepted), where WeCAN has stronger ablation studies than PolyNet, comparable empirical evaluation, and a theoretical contribution that neither has. The One-Shot concern prevents a higher score.

**All anchors considered:**
- 10eQ4Cfh8p (3.0) — FJSP-RL, weaker in every dimension
- RAdBtquPiI (3.4) — Safe RL scheduling, incremental contribution
- 9qtswuW5ux (4.25) — Unsupervised GNN for QUBO, limited novelty
- nIBmwm7ixo (5.0) — RL vertex coloring, solid but limited baselines
- TKuYWeFE6S (5.25) — PolyNet, accepted at ICLR, comparable contributions
- CFLEIeX7iK (5.75) — Neural Solver Selection, rejected
- Cs6MrbFuMq (6.0) — HexGen-2, accepted, similar rigor but trendier topic
- WszeEzjcq2 (5.33) — NAR GNN analysis, mixed reviews

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>