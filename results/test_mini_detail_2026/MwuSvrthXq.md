Now I have sufficient calibration. Let me write the consolidated review.

## Summary

This paper proposes WeCAN, an end-to-end RL framework for heterogeneous DAG scheduling with task-resource compatibility. The key technical innovations are: (1) Weighted Cross-Attention (WeCA) layers that encode task-pool compatibility coefficients as external attention biases, avoiding fixed-dimensionality constraints and preserving adaptability across varying environment sizes; (2) a Longest Directed Distance GNN (LDDGNN) for dependency embedding; and (3) a theoretical analysis of the optimality gap in list scheduling with a single-pass skip-action mechanism designed to close that gap. Experiments on TPC-H and Computation Graphs benchmarks show WeCAN achieving up to 18.1% improvement over the best heuristic and 7.7% over the best neural baseline, with inference times comparable to heuristics.

## Strengths

1. **Weighted cross-attention (WeCA) is a genuinely novel architectural innovation.** The design places compatibility coefficients *outside* the softmax normalization (Eq: `g_v = f_v + softmax(...)/√d · diag{K_acc(v,c(1)),...} V^c`), which the paper convincingly shows avoids the information-loss problem that arises from inside-placement (where identical-attribute tasks with different compatibility profiles would receive the same embedding after normalization). The ablation study (Table 3) confirms WeCA-outside significantly outperforms WeCA-inside (e.g., 19908 vs. 20729 on TPC-H-30). This is a principled solution to a specific limitation of prior work that either averages compatibility coefficients (Zhou et al. 2022, Zhadan et al. 2023) or uses fixed-size embeddings (Jeon et al. 2023).

2. **Strong and well-structured empirical evaluation.** Results are reported across two distinct datasets (TPC-H with 275–918 tasks; Computation Graphs with 500 tasks), including means and standard deviations for sampling-based methods. The gains over heuristics and neural baselines are consistent and substantial (7–18%). The paper also reports running times, demonstrating that WeCAN-greedy matches heuristic-level speed while delivering better makespan. Generalization experiments (Figure 2) across pool number, pool type, task count, and task type show WeCAN remains robust while One-Shot degrades significantly (e.g., 6.7% vs. 0.9% improvement for more pool types).

3. **Thorough ablation studies.** Table 3 systematically ablates both the WeCA placement (inside vs. outside, encoder-only vs. decoder-only) and the GNN architecture (LDDGNN vs. GAT forward/bidirectional), holding layer count and hidden dimension constant. Every architectural component is shown to contribute positively. This is above the standard for scheduling papers.

4. **Theoretical analysis linking skip actions to the optimality gap of list scheduling.** Section 4 formalizes the reduced space B and proves that list scheduling (S_list) is not surjective onto optimal solutions. Theorem 1 and Theorem 2 establish that the proposed skip-action-based map can represent optimal solutions. The heavy-task experiments (Figure 3) provide empirical validation that the gap materializes precisely where theory predicts (resource-intensive tasks) and that skip closes it. This theory–experiment alignment strengthens the paper.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Skip action not separately ablated on the standard benchmarks (Tables 1–2).** The skip action is highlighted as contribution (3) and is central to the theoretical claims, but Tables 1–2 only report full WeCAN (which includes skip). An ablation (WeCAN-without-skip on TPC-H-30/50 and Computation Graphs) would directly quantify how much of the performance gain comes from WeCA/LDDGNN vs. the skip mechanism. The heavy-task experiment (Figure 3) does show skip's value where theory predicts it matters most, so the absence on standard benchmarks is a gap in completeness, not a validity concern. The authors should add this ablation.

2. **Baseline comparison could be more comprehensive.** The paper cites Zhou et al. (2022), Zhadan et al. (2023), and Wang et al. (2025) as heterogeneous scheduling methods that also handle compatibility coefficients, but does not include any of them as baselines. The paper explains *why* these methods handle compatibility differently (averaging, fixed-size embeddings), but without direct comparison the reader cannot assess whether WeCAN's approach empirically improves over them. At minimum, the paper should acknowledge this limitation and explain whether these methods were excluded due to code availability, domain mismatch, or other practical constraints.

3. **Claim about variance reduction from "clustering poor solutions" is unsubstantiated.** Section 4.2 states that the skip design "clusters most poor solutions in the high-u_a, high-u_c region... this concentration makes such regions easier to handle during training and reduces variance." No empirical evidence (e.g., training curves, variance of returns with/without skip) is provided for this claim. This does not undermine the paper's core results, but the claim should be either supported or softened.

4. **Skip-score formula lacks design rationale.** The skip score formula `u_a(1 - k/(2n))^{u_b} + u_c` is introduced in Section 3.2 without derivation or justification beyond "preventing endless idling." The paper does not report sensitivity to the initialization or bounds of (u_a, u_b, u_c), nor whether training is robust to different functional forms. This is a minor methodological gap.

### Trivial

- **Skip action mask corner case (Algorithm 1):** The skip action is masked "if no running tasks on all pools." This blocks skip at time zero (before any tasks start). Theorem 1 posits existence of scores enabling optimal solutions, but the mask could theoretically block an optimal solution that requires initial idling. The paper should discuss whether this scenario is possible and, if so, adjust the mask condition.

## Nice-to-Haves

- Diagnose learned skip behavior during evaluation: what fraction of decisions are skip actions, and how does this correlate with task characteristics (resource demand, duration)?
- Report training variance (reward curves with/without skip) to support the "clustering reduces variance" claim.
- Sensitivity analysis for skip-score parameter initialization.

## Removed Points

- **"Theorem 1(IV) is existence-based and does not translate to empirical guarantees" / "paper conflates expressivity with learnability"** — Removed: The paper clearly frames Theorem 1 as an existence/expressivity result about representation capacity, not a convergence guarantee. Section 4 (theory) and Section 3.3 (REINFORCE training) are structurally separated, and no RL scheduling paper provides convergence-to-optimal guarantees. The criticism misreads the paper's own framing.

- **"The paper does not clarify whether decoder WeCA layers are applied once or repeatedly"** — Removed: Algorithm 1 states "Perform WeCAN to get the scores" once at initialization, confirming single-pass processing. This is clear from the paper.

- **"The skip-score functional form is asserted without evidence for clustering"** — This specific point is merged into Weakness #3 above (variance reduction claim), but the stronger framing that the theory "remains disconnected from empirical results" is removed as overblown given the heavy-task experiments.

- **Various formatting/style nitpicks and generic area-of-concern sweeps** — Removed per filtering rules.

## Novel Insights

The most interesting observation that emerges across the reviews is the tension between the skip action being a core theoretical contribution (closing the optimality gap of list scheduling) and the empirical strategy of evaluating it only on synthetic heavy-task modifications of the original benchmarks. This is not a flaw per se — the theory predicts skip matters most precisely where resource-intensive tasks exist — but it highlights that the paper's two contribution clusters (WeCA/LDDGNN architecture improvements vs. skip-action theory) operate on somewhat separate empirical tracks. A more integrated evaluation could strengthen the narrative connecting theory to practice.

## Suggestions

1. **Add a WeCAN-without-skip variant to Tables 1 and 2.** This single addition would directly quantify the contribution of the skip mechanism on standard benchmarks and is the most impactful improvement the authors could make.

2. **Include or explicitly justify the omission of the heterogeneous schedulers cited in the intro** (Zhou et al. 2022, Zhadan et al. 2023, Wang et al. 2025) as baselines. Even a brief discussion of practical constraints would significantly strengthen the evaluation.

3. **Provide empirical support for the variance-reduction claim** (training curves, return variance with/without skip) or remove/weaken the claim.

4. **Discuss the skip-action mask corner case** (time zero) and either justify why it cannot affect optimality or adjust Algorithm 1.

## Score and Decision

**Round 1 — Bracketing:** I queried for DAG scheduling / RL scheduling papers in three score bands. Weak anchors (avg < 3.5): papers scoring 2.5–3.0 on related scheduling topics; middle anchors (3.5–7.5): GAA-PtrNet (4.50, Reject), RESCHED (5.00, Accept Poster), DEFT (5.00, Accept Poster), RAISE (4.00, Reject); strong anchors (7.5+): papers scoring 8.0 on non-scheduling topics. Based on this, I bracketed the paper between 5.0 and 7.0.

**Round 2 — Narrowing:** I queried inside (4,6) and (6,8) for scheduling-specific anchors. The most informative comparisons are:
- **GAA-PtrNet (4.50, Reject):** One-shot DAG scheduling with GNN. WeCAN is clearly stronger — more architectural novelty (WeCA vs. standard GNN attention), better theory, more thorough ablation, and larger performance margins over baselines.
- **RESCHED (5.00, Accept Poster):** FJSP with Transformer + minimal features. WeCAN has stronger architectural novelty, comparable experimental rigor, and adds a theoretical contribution (skip optimality gap). RESCHED had a substantive concern about training-data fairness that WeCAN does not share.
- **DEFT (5.00, Accept Poster):** MoE for dynamic cloud workflows. WeCAN has more thorough ablation studies and a cleaner evaluation. DEFT's main weakness (missing MoE ablation) mirrors the skip-ablation gap in WeCAN, but WeCAN's skip gap is smaller because heavy-task experiments directly validate it.
- **Multi-Objective FJSP (5.50, Accept Poster):** Different problem setting, comparable score level.

**Final Score: 6.0.** The paper has genuine architectural novelty, a solid theoretical contribution, and thorough empirical validation with good results. The minor weaknesses (skip ablation on standard benchmarks, baseline completeness, unsubstantiated variance claim) prevent it from being a strong accept but do not threaten its core claims. This places it above RESCHED and DEFT (both 5.00) and near the level of papers scoring 5.5–6.5 in comparable domains.

**Decision: Accept.**

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>