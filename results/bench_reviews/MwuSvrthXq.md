Now I have a good picture of the paper and the calibration landscape. Let me write the consolidated review.

## Summary

This paper proposes WeCAN, an end-to-end reinforcement learning framework for heterogeneous DAG scheduling with task-pool compatibility constraints. The key architectural contribution is a **weighted cross-attention (WeCA) layer** that integrates compatibility coefficients as attention biases outside the softmax, enabling the model to handle varying numbers of pools and task types without retraining. The paper also provides a theoretical analysis of list scheduling's optimality gap and proposes a single-pass skip-action mechanism to address it. Experiments on TPC-H and Computation Graphs benchmarks show WeCAN outperforms heuristic baselines (HEFT, Tetris) by 13–18% and neural baselines (PPO-BiHyb, One-Shot) by 7–9% in makespan, while also demonstrating strong generalization across 8 distinct environment fluctuations.

## Strengths

1. **Well-designed architecture for heterogeneous scheduling with compatibility.** The weighted cross-attention (WeCA) layer is a genuinely clever architectural contribution. By placing compatibility coefficients as multiplicative biases *outside* the softmax, it simultaneously (a) captures fine-grained task-pool compatibility information, (b) handles varying numbers of pools and task types, and (c) preserves the ability to distinguish tasks with different compatibility profiles even when their static features are identical (§3.1). The ablation (Table 3) confirms that outside-WeCA consistently outperforms inside-WeCA (by 3.5–4% points) and removing encoder WeCA entirely degrades performance severely (from +14% to +0.5% on TPC-H-30). This is a principled solution to a genuine problem in heterogeneous scheduling that prior averaging or one-hot approaches struggled with.

2. **Strong empirical results and convincing generalization.** On TPC-H datasets, WeCAN-S(256) achieves 18.1% improvement over the best heuristic and 7.7% over the best neural baseline; on Computation Graphs, the gains are 13.4% and 9.5% respectively (Tables 1, 2). More impressively, the generalization experiments (Figure 2, Tables 9–17) demonstrate that a model trained on TPC-H-30 with 3 pools maintains its advantage across 8 distinct environment fluctuations (varying pool count, pool types, task types, capacities, and task counts up to 200). This validates that WeCA's design genuinely delivers on its promise of adaptability to varying environment sizes.

3. **Comprehensive ablation study.** Table 3 systematically ablates both main components (WeCA placement, LDDGNN vs. GAT variants), providing clear evidence that each architectural choice matters. The heavy-task experiments (Figure 3, Table 8) convincingly show that the skip action is beneficial when list scheduling's optimality gap is practically relevant (8.3–8.9% improvement over HEFT with skip vs. 2.6–3.4% without).

4. **Theoretical analysis of optimality gap.** The formal characterization of the feasible reduced space \(B_f\), the projection map \(S_n\), and the surjectivity condition (Theorems 1–2, Propositions 1–4 in Appendix A) provides a rigorous framework for understanding when a generation map can represent optimal solutions. While the practical skip formula is heuristic, this theoretical lens is valuable and could guide future research.

## Weaknesses

### Fatal
None.

### Major

1. **Missing comparisons with recent heterogeneous scheduling methods.** The paper cites Zhou et al. (2022), Zhadan et al. (2023), and Wang et al. (2025) as related work on RL-based heterogeneous scheduling but does not benchmark against any of them. The only neural baselines are PPO-BiHyb (2021) and One-Shot (2023), both of which are re-implemented with modifications. Without empirical comparison to these contemporary methods, the claim of "outperforming state-of-the-art methods" (§1, abstract) is not fully supported — the SOTA designation rests on a thin baseline set, especially since the paper itself acknowledges that methods like Zhou et al. address the same heterogeneous scheduling setting.

2. **Mismatch between the theoretical narrative and empirical role of the skip action.** The paper's framing emphasizes that the skip action "closes the optimality gap" of list scheduling (abstract, §4, Theorem 1). However: (a) the skip action is *disabled* on all standard benchmarks because it "tends to increase the variance of makespan" (§H.3); (b) the skip-score formula \(u_a(1-2k/n)^{u_b} + u_c\) is introduced without derivation or comparison to simpler alternatives (e.g., a learned constant, a linear function of remaining steps, or a network-generated per-step value); (c) Theorem 1 proves *existence* of scores that would suffice for optimality — not that the learned policy achieves this. On heavy-task benchmarks where skip is evaluated, the improvement over the no-skip variant is a meaningful 4–6% points (Table 8), but the paper's central theoretical claim is about an architectural *capacity* that the experiments only partially realize in specially constructed settings. The framing should be adjusted to match what is actually demonstrated.

3. **The skip-score formula lacks ablation or motivation.** The formula \(u_a(1-2k/n)^{u_b} + u_c\) (§3.2) is presented without justification or comparison to alternatives. There is no ablation varying the functional form (e.g., fixing \(u_b\) to 0, 1, or 2), no analysis of the learned coefficient values across instances, and no study of skip frequency during inference on heavy-task vs. standard benchmarks. While the formula is reasonable as a decreasing function of steps taken, it is unclear whether its specific form is necessary or whether a simpler approach (e.g., a learned per-instance constant or a linear decay) would work equally well.

### Minor

1. **Statistical reporting is incomplete.** Standard deviations are reported only for sampling-based modes (S(64), S(256)) and One-Shot. Greedy mode and heuristic baselines lack variance information (Tables 1, 2). Several performance gaps — particularly for greedy mode and on larger instances (TPC-H-100) — are modest enough that error bars would help the reader assess significance. The paper does not report confidence intervals or statistical significance tests.

2. **The NAR vs. AR comparison is useful but not central.** The comparison in Appendix B (Table 4) shows NAR and AR achieve comparable performance, with AR requiring >10× inference time. This is valuable for justifying the NAR design, but the paper's framing of "single-pass inference" as a contribution is somewhat undercut by the fact that most prior scheduling methods also aim for efficient inference. The comparison is sound but the benefit is modest.

3. **No analysis of what the WeCA attention mechanism actually learns.** The paper motivates the outside-softmax placement with a qualitative argument about distinguishing tasks with different compatibility profiles (§3.1), but provides no visualization or case study of the learned attention weights. Such analysis would strengthen the claim that WeCA is "capturing" compatibility information rather than simply providing additional model capacity.

4. **The MILP formulation in Appendix A is never used.** The paper presents a MILP formulation of the heterogeneous scheduling problem but does not use it for any experiments or analysis (e.g., computing optimality gaps via MILP solutions on small instances). Its presence adds length without serving an explicit purpose.

### Trivial
- Some figure captions (Figures 2, 3) refer to "Figure 3 of main text" instead of their own labels.
- Table formatting in the parser output shows some artifacts, but these are parser issues.
- The paper uses both "WeCAN" and "we" inconsistently in the conclusion.

## Nice-to-Haves
- Adding skip-frequency histograms or Gantt charts for heavy-task vs. standard instances would help illustrate when the skip action is actually triggered.
- A comparison with simple concatenation baselines (where \(K_{acc}\) values are appended to task features and processed by a standard GNN) would further validate the WeCA design.
- Providing error bars for greedy mode and heuristic baselines would strengthen the statistical foundation.

## Removed Points

(The following points from the harsh critic were set aside.)

- **"The MILP formulation is never used so unclear why it is needed"** — This is speculative. The MILP provides the formal definition of the original space \(A\) and is used for Proposition 1 (bijection between MILP solutions and \(A\)). It serves a theoretical role, even if not solved directly. *Removed per soft rule: the formulation has a purpose in the theoretical framework.*
- **"The space of definitions could be more concise"** — A presentation preference, not a substantive weakness. *Removed per formatting/style nitpick rule.*
- **"The improvement over GAT is only ~2-3%"** — Actually 3.5–4.1% points (Table 3: 14.0% vs 10.5%/9.9%). The critic's number is inaccurate. *Removed per factually wrong rule.*
- **"The paper does not test simple concatenation baseline"** — While this is true, the paper does ablate WeCA against inside-WeCA, decoder-only-WeCA, and no-WeCA variants, which collectively demonstrate the mechanism's importance. The request for a concatenation baseline is a nice-to-have, not a core missing experiment. *Moved to Nice-to-Have.*
- **"The inside vs. outside comparison is only done on two datasets"** — This is adequate for an ablation. The paper uses TPC-H-30 and TPC-H-50 (different sizes) and finds consistent results. *Removed per soft rule: the ablation scope is reasonable.*
- **"Appendix B justification for NAR is based on a particular implementation"** — Every implementation is particular. The paper provides concrete runtime numbers. *Removed per strawman rule.*
- **"Theorem 1 does not guarantee learnability"** — The paper never claims it does. Theorem 1 is a statement about *capacity* of the architecture, not about learning guarantees. The theorem is correctly scoped. *Removed per factually wrong rule.*
- **"The skip action and local search discussion"** — The paper discusses this in Appendix F.4 and the results are exactly as expected (skip already captures most of the benefit). This is correct behavior, not a weakness. *Removed per factually wrong rule.*
- **Various missing experiments suggestions (histograms, sensitivity analysis, Gantt charts, etc.)** — These are standard "could-do-more" requests that don't undermine the existing contributions. *Moved to Nice-to-Have.*
- **"The theoretical analysis culminates in Theorem 1, which is about existence, not about the practical formula"** — This is correctly scoped. The theorem proves the *design* works in principle; the practical formula is a heuristic instantiation. The paper does not claim the formula is derived from the theory. *Removed per factually wrong/misread rule.*

## Novel Insights

The reviews surface a tension that the paper itself does not fully resolve: the WeCA architecture is clearly a well-motivated and empirically successful contribution for heterogeneous scheduling with compatibility, but the paper wraps it in a secondary theoretical narrative (skip action closing the optimality gap) that is weaker than advertised. The skip action is an important idea that demonstrably helps in heavy-task regimes, but the specific formula and the fact that it must be disabled on standard benchmarks suggest that the skip contribution is best seen as a *robustness feature* for certain edge cases rather than a general-purpose improvement. The strongest contribution is WeCA's ability to encode compatibility information while preserving adaptability to environment size — this is what the generalization experiments validate most convincingly. If the paper foregrounded this and relegated the optimality-gap closure to a secondary finding, its narrative would better match its evidence.

## Suggestions

1. **Add comparisons to at least one recent heterogeneous scheduler (Zhou et al. 2022, Zhadan et al. 2023, or Wang et al. 2025)** to substantiate the "state-of-the-art" claim. Even if re-implementation is imperfect, the effort would substantially strengthen the paper.

2. **Revise the skip-action narrative.** Acknowledge directly that the skip action is most beneficial in heavy-task regimes and disabled on standard benchmarks due to variance concerns. Tone down claims like "closes the optimality gap" to "provides the architectural capacity to represent optimal solutions" or "addresses the optimality gap in characteristic cases."

3. **Add a simple ablation for the skip formula** — at minimum, compare to a learned constant skip score or a linear decay of the form \(u_a (1 - k/n) + u_c\). This would either validate the formula's specific form or replace it with something simpler.

4. **Report standard deviations for greedy mode** and for heuristic baselines where feasible, or at minimum note that greedy results are deterministic single runs.

5. **Add a brief case study or attention visualization** showing that the WeCA layer's attention weights correlate with compatibility coefficients, to support the claim that it "captures" compatibility information rather than just adding capacity.

## Score and Decision

**Calibration anchors used** (all from ICLR 2026 human reviews):

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `/home/wg25r/review_agent/human_reviews_2026/UbWy2QVmke.md` (GAA-PtrNet) | 4.50 | Weaker paper — GAA-PtrNet had more limited novelty and less convincing empirical results. WeCAN's architectural contribution (WeCA) is more novel and better validated. |
| `/home/wg25r/review_agent/human_reviews_2026/rnrENwgDsn.md` (MACE) | 3.50 | Weaker paper — MACE had limited baselines (only Decima), marginal gains, and evaluation misaligned with ICLR audience. WeCAN has stronger baselines, larger gains, and more comprehensive evaluation. |
| `/home/wg25r/review_agent/human_reviews_2026/yVFOdLjd7V.md` (DEFT) | 5.00 | Comparable — Both have well-motivated architectural innovations (MoE vs. WeCA) applied to scheduling. Both have missing ablations and baseline concerns, but WeCAN's generalization experiments are more extensive. |
| `/home/wg25r/review_agent/human_reviews_2026/s5pWbwf2tk.md` (RESCHED) | 5.00 | Comparable — Both accepted as posters. RESCHED had strong results with simplified design; WeCAN has more architectural novelty but more framing issues. |
| `/home/wg25r/review_agent/human_reviews_2026/7gA6ZYii0e.md` (RAISE) | 4.00 | Weaker — RAISE had ensemble-based RL for scheduling with less clear architectural innovation. WeCAN's WeCA design is more novel. |
| `/home/wg25r/review_agent/human_reviews_2026/o7avj3PWNC.md` (BrokenMath) | 5.00 | Different topic (benchmark), but this score band represents work with clear contributions but significant limitations. WeCAN's contributions are stronger but its framing issues are more prominent. |
| `/home/wg25r/review_agent/human_reviews_2026/2UVYeupOsM.md` (IntelliAsk) | 3.00 | Different topic. WeCAN is clearly a more substantive paper with more technical depth. |

The paper sits above the rejected anchors (3.5–4.5 range) and at the level of accepted poster papers (5.0 range). Its main architectural contribution (WeCA) is genuinely novel and well-validated, and the generalization results are strong. However, the mismatch between the skip-action theoretical framing and its limited practical role, combined with missing baseline comparisons, prevent it from being a strong accept. Relative to the 5.0 anchors, it has slightly stronger empirical validation but also more prominent framing issues.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>