Now I have sufficient anchors for calibration. Let me write the consolidated review.

## Summary

The paper proposes WeCAN, an end-to-end RL framework for heterogeneous DAG scheduling with task-pool compatibility. It introduces (1) a weighted cross-attention mechanism that encodes compatibility coefficients outside the softmax to preserve fine-grained task-pool information while maintaining adaptability to varying numbers of pools and task types, and (2) a skip-action mechanism in the single-pass setting that provably closes the optimality gap of list scheduling. Experiments on TPC-H and synthetic Computation Graphs benchmarks show consistent makespan improvements over heuristic (HEFT, Tetris) and neural (One-Shot, PPO-BiHyb) baselines, with near-heuristic runtime.

## Strengths

- **Weighted cross-attention is well motivated and empirically validated.** The outside-multiplication of compatibility coefficients after softmax (Section 3.1) is a clean architectural innovation: it preserves task-pool compatibility information that would be lost under the inside (log-form) normalization. The ablation study (Table 3) provides direct evidence — WeCA+LDDGNN achieves 14.0% improvement vs. 10.5% for the inside variant on TPC-H-30, and degrading performance when WeCA layers are skipped confirms their importance.

- **Skip-action with theoretical grounding for the optimality gap.** The paper identifies a genuine limitation of list-scheduling-based generation maps (Section 4.1): they map multiple orders to the same schedule and can exclude optimal solutions. Theorem 1 and Theorem 2 formalize this gap, and the skip-action mechanism provides a principled remedy. The heavy-task experiments (Figure 3) directly validate the practical benefit: WeCAN with skip achieves 8.3% improvement over HEFT on TPC-H-30-heavy vs. 2.6% for the non-skip variant.

- **Strong empirical results across real-world and synthetic benchmarks.** On TPC-H-100 (Table 1), WeCAN-S(256) achieves makespan 61373 vs. 66173 for One-Shot-S(256) and 70137 for HEFT — improvements of 7.3% and 12.5%, respectively. The greedy variant runs in 1.72s, matching heuristic runtime. These gains are consistent across Computation Graphs (Table 2) and hold under environment fluctuations (Figure 2), where WeCAN maintains 20.4% improvement when pool count increases while One-Shot drops to 9.2%.

- **LDDGNN improves over standard GAT.** Ablation (Table 3) shows WeCA+LDDGNN outperforms WeCA+GAT(forward) (14.0% vs. 10.5%) and WeCA+GAT(bi-direction) (14.0% vs. 9.9%), demonstrating the value of longest-directed-distance attention for DAG dependencies.

- **Generalization experiments demonstrate robustness.** Figure 2 tests WeCAN under varied pool counts, pool types, task counts, and task types without retraining, showing consistent advantages over One-Shot. This directly supports the adaptability claim made in the architecture design.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The skip-score design is under-analyzed empirically.** The specific functional form $u_a(1 - k/2n)^{u_b} + u_c$ is introduced with the claim that it "clusters most poor solutions in the high-$u_a$, high-$u_c$ region" (Section 4.2). While this is a plausible structural property of the formula, no empirical evidence is provided in the main paper — no visualization of learned parameter distributions, no analysis of where poor solutions fall in the $(u_a, u_c)$ plane, and no ablation comparing this functional form to simpler alternatives (a learned constant, linear decay, or $u_a(1 - k/2n) + u_c$). Theorem 1(iv) guarantees existence of *some* scores that enable an optimal solution, but does not establish that the proposed parametric family can represent them for all instances. This gap between existence and learnability is not addressed. The skip mechanism's practical effectiveness is validated (Figure 3), but the design rationale for the specific formula could be significantly strengthened with a small empirical analysis.

- **Baseline coverage is adequate but could be expanded.** The paper compares against PPO-BiHyb (a heterogeneous neural scheduler), One-Shot (a single-pass neural scheduler), and multiple heuristics (HEFT, Tetris, CP, SFT, MOPNR). However, the neural heterogeneous scheduling literature includes several methods cited in the related work (Grinsztajn et al., 2021; Zhadan et al., 2023; Wang et al., 2025) that are not included as baselines. While these methods use fixed-size embeddings that limit their adaptability — a limitation the paper explicitly scopes out of — including them would strengthen the claim of SOTA performance for heterogeneous scheduling. As it stands, the reported improvements over the included heterogeneous baselines (PPO-BiHyb, HEFT) are convincing, but the claim of "outperforming state-of-the-art methods" rests on a somewhat narrow set of neural comparisons.

- **No limitations or failure-case discussion.** The paper lacks a limitations paragraph — e.g., acknowledging that the skip-score formula is a specific design choice, discussing when the approach might struggle (very large instances? extreme heterogeneity patterns?), or addressing distribution shift beyond the tested fluctuations. This is standard practice and would improve the paper's completeness.

### Trivial
- Statistical variance for greedy results and heuristic baselines is not reported. Reporting variance across test instances would help assess reliability.

## Nice-to-Haves

- An empirical analysis of learned skip parameters ($u_a, u_b, u_c$) to validate the clustering claim about poor solutions, and an ablation comparing the proposed skip formula against simpler alternatives.
- A sketch of the surjectivity proof construction (Theorem 1) in the main text, even briefly, would make the theoretical contribution more self-contained.
- A brief summary of key hyperparameters (layers, hidden dimensions, learning rate) in the main text rather than only in the appendix.

## Removed Points

These points were flagged for removal with justification:

- **"Appendix is stripped, making theoretical argument impossible to verify"** — REMOVED per hard rule: missing appendix content is a parser artifact, not an author error.
- **"One-Shot is a mismatched baseline, making comparison uninformative"** — DEMOTED from the critic's stronger framing. The paper acknowledges One-Shot's limitations and includes PPO-BiHyb as a heterogeneous neural method. One-Shot is included as the main single-pass neural competitor; the comparison is informative for showing the value of explicit heterogeneity handling. The concern about additional heterogeneous baselines is retained (Minor).
- **"Skip action benefit is only moderate (5pp)"** — WEAKENED: 5 percentage points on makespan improvement is practically meaningful for scheduling, and the ablation validates the theoretical claim.
- **"Theorem 1(iv) existence vs learnability gap"** — RETAINED in Minor form but softened: this is a standard issue in theoretical ML papers and the experimental results serve as practical validation; the concern is about the specific parametric form's justification, not a fatal flaw.
- **"Inside vs outside WeCA empirical comparison is missing"** — REMOVED: Table 3 explicitly compares inside vs outside variants; the reviewer simply missed this.
- **"Request for user studies, theoretical proofs for an empirical paper"** — REMOVED: not standard for this type of paper.

## Novel Insights

None beyond the paper's own contributions. The key insight — that compatibility coefficients should be multiplied outside the softmax to preserve task-pool distinction, supported by both theory and ablation — is well articulated in the paper itself.

## Suggestions

1. Add a small analysis of the learned skip-action parameters: show distributions of $u_a, u_b, u_c$ learned across test instances, and verify (or qualify) the claim that poor solutions cluster in the high-$u_a$, high-$u_c$ region. If the claim holds, this would convert a plausible design into a demonstrated one.
2. Add a brief sketch of the surjectivity construction in Section 4 (1–2 paragraphs). Even a sentence stating that the enlarged $B_f$ including skip actions and the modified $T$ create a bijection between subspaces of $A$ and points in $B_f$ would help readers who cannot access the appendix.
3. Include a "Limitations" paragraph in the conclusion discussing scope conditions and potential failure cases.
4. Report variance (standard deviation across test instances) for greedy results and heuristic baselines to match what is already provided for sampling methods.

## Score and Decision

**Round 1 (Bracketing):** Weak anchors at 2.0–3.0 (scheduling/CO papers with significant flaws) are well below this paper. Middle anchors at 5.0–7.0 (heterogeneous scheduling, neural CO with cross-attention, multi-task VRP) span the relevant range. Strong anchors at 8.0+ (diffusion, LTL, graph NNs) are in different areas but confirm what an 8+ paper looks like. **Initial bracket: 5.5–7.5.**

**Round 2 (Narrowing):** The paper clearly outperforms DKfcxPxunu (5.75, multi-task VRP, criticized for low novelty and weak baselines), 8WtBrv2k2b (5.0, quantum scheduling with serious formulation flaws), and yEwakMNIex (6.25, RedCO — interesting but applicability concerns). It is comparable to hB2hXtxIPH (7.0, GSE — clear contribution, sound method, minor weaknesses), but slightly below the polish of top 8.0 papers which have no unaddressed concerns. **Narrowed bracket: 6.5–7.5.** The paper's contributions (WeCA architecture, theoretical gap analysis, skip mechanism) are genuine, the experiments are thorough, and the weaknesses are minor and addressable. The final score is anchored at the upper end of the middle band, just below the 8.0 level which would require a cleaner justification of every design choice.

**Final score: 7.0 — Accept.** The paper makes a solid contribution to heterogeneous DAG scheduling with a well-motivated architecture, formal theoretical analysis of the optimality gap, and convincing empirical results. The weaknesses (skip formula justification, baseline scope) are minor and do not undermine the core claims.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>