Now I have all the information needed. Let me construct the final consolidated review.

## Summary

This paper proposes WeCAN, an end-to-end reinforcement learning framework for heterogeneous DAG scheduling with task-pool compatibility. The key technical contributions are (1) a weighted cross-attention (WeCA) layer that integrates compatibility coefficients as attention weights outside the softmax, enabling the network to distinguish tasks with identical attributes but different pool compatibility profiles while remaining agnostic to the number of pools and task types; (2) a longest-directed-distance GNN (LDDGNN) to capture directed dependencies; (3) a theoretical analysis showing the optimality gap of list-scheduling-based methods and a skip-action mechanism that closes this gap in the single-pass setting; and (4) empirical results on TPC-H and Computation Graphs datasets showing state-of-the-art makespan with computation time close to heuristic baselines.

## Strengths

- **Weighted cross-attention (WeCA) layer is a principled architectural contribution.** Placing compatibility coefficients outside the softmax (Eq. 2) allows the network to capture a task's overall compatibility profile across all pools, not just the relative ranking. The ablation in Table 3 confirms that removing or modifying WeCA degrades performance (e.g., WeCA-inside + LDDGNN yields 10.5% improvement vs. 14.0% for full WeCA on TPC-H-30), isolating the effect of this design choice.

- **Strong and consistent empirical performance across multiple datasets and scales.** WeCAN outperforms all baselines on TPC-H-30/50/100 and on all three Computation Graph types (Erdős-Rényi, Layer Graphs, Stochastic Block). On TPC-H-30, WeCAN-Greedy (19,578 makespan, 0.15s) surpasses the best heuristic Tetris (23,170, 0.21s) and the best neural baseline One-Shot-S(256) (20,399, 2.26s). On Computation Graphs, WeCAN-Greedy (10,270 makespan on Erdős-Rényi) beats PPO-BiHyb (10,795) while running 115× faster (0.57s vs. 65.51s), demonstrating both quality and efficiency.

- **Theoretical analysis that motivates and bounds the skip-action mechanism.** Theorem 1 formally characterizes the optimality gap: without skip, the optimal solution can be unreachable (iii); with skip, there exist scores enabling a greedy optimal solution (iv). This provides formal grounding for a design decision that could otherwise appear ad-hoc.

- **Systematic ablation study isolating architectural components.** Table 3 evaluates eight variants (WeCA placement variants, LDDGNN vs. GAT variants), showing each component's contribution. The controlled comparisons (same layer count, hidden dimensions) lend credibility to the attribution of performance gains.

- **Generalization experiments under varying environment conditions.** Figure 2 shows WeCAN maintains larger margins over the best heuristic compared to One-Shot under four types of fluctuations (more pools, more pool types, more tasks, more task types) without retraining, supporting the claim that the architecture adapts to heterogeneous environments.

## Weaknesses

### Major

- **Unclear adaptation of the One-Shot baseline to the heterogeneous setting.** The paper states One-Shot "does not consider compatibility coefficients or pool allocation" (Sec. 1) yet reports its results on heterogeneous problems with three pools and compatibility coefficients. The paper does not explain whether or how One-Shot was modified to handle pool assignment and compatibility information. If the authors used One-Shot's priority mechanism with some pool-selection rule, this should be stated explicitly. As written, the reader cannot assess whether the comparison is fair. This concern undermines the headline "best neural baseline" claims in Tables 1 and 2.

- **The skip-action ablation lacks a clean controlled comparison.** Figure 3 is meant to demonstrate the benefit of the skip action, but the "non-skipping variant" is not explicitly identified. The closest candidate is WeCAN-inside-S(256), but this changes the WeCA placement (inside vs. outside softmax) simultaneously, not just the presence of skip. The paper does not present a simple ablation of "same WeCAN architecture with vs. without skip." Without this, the claim that skip closes the optimality gap is not directly supported by the presented data. (The separate theoretical analysis motivates it, but the empirical evidence is indirect.)

### Minor

- **The skip score formula is described without sufficient justification.** The formula $u_a(1 - k/2n)^{u_b} + u_c$ is motivated by "prevent[ing] the skip action from overly prioritized," but there is no discussion of why this particular functional form (rather than alternatives) was chosen, how hyperparameters interact with the training dynamics, or empirical evidence that the formula works as intended (e.g., how often skip is selected during training, whether it reduces the variance as claimed).

- **Generalization results lack error bars.** Figure 2 reports only a single improvement percentage per condition with no error bars or raw makespans. It is impossible to assess whether the differences between WeCAN and One-Shot under each fluctuation are statistically significant.

- **"PRO-BALM" appears in Figure 3 but is never defined in the paper.** This baseline name is introduced in the figure/table without definition in the main text, making the figure uninterpretable without external information.

- **Dataset generation details are underspecified.** The paper adds "random memory constraints and task types" to the TPC-H dataset but does not specify how compatibility coefficients were sampled. Without this, the results cannot be independently reproduced.

### Trivial

- The figure description in the parsed text shows "WeCAN-S(256)" appearing twice in the Figure 3 table with different values, suggesting a labeling issue in the original figure.

## Nice-to-Haves

- A sensitivity analysis for the skip-action hyperparameters ($u_a, u_b, u_c$) and WeCA architectural choices (number of layers) would further strengthen the robustness claims.
- Reporting makespan with variance over instances (not just over random seeds) would strengthen the generalization results.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"The claim that prior works average compatibility coefficients is not cited"** — The paper does cite Zhou et al. 2022, Zhadan et al. 2023, and Wang et al. 2025 for this claim (lines 72–74). The criticism is factually wrong.
- **"LDDGNN description too brief; masks and biases not explained"** — The equations in the main text clearly show $M_{v,w}^j$ (attention mask) and $b_{d_c(v,w)}$ (learnable bias). Full details are deferred to Appendix G, which is standard for a conference paper. This is not a missing piece.
- **"Decoder section is vague"** — The decoder uses WeCA layers "detailed in Appendix G." The main text provides the score computation and the non-auto-regressive design choice. The level of detail is appropriate for the page budget.
- **"Statistical significance: heuristics lack error bars"** — Heuristics are deterministic on a given instance. Reporting standard deviations over random seeds for sampling methods (as done) and single values for deterministic algorithms is standard practice.
- **"Theoretical guarantees not connected to empirical learnability"** — This is a general limitation of every RL-based method that proves existence of optimal scores but uses REINFORCE to find them. It is not a specific weakness of this paper. The paper's central claim is about the *existence* of optimal scores with skip (Theorem 1(iv)), which the theory supports.
- **"Missing training details (learning rate, batch size) in main text"** — These are standard implementation details appropriately relegated to Appendix H. The page budget in ICLR is tight.
- **General category-driven concerns about methodology soundness, evaluation validity, and comparison fairness** raised without specific anchors in the paper text have been removed as speculative.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Clarify the One-Shot baseline adaptation.** Add 2–3 sentences explaining explicitly: (a) whether existing code was used or the method was re-implemented, (b) how pool assignment was handled for One-Shot (e.g., whether the generated priorities were combined with a pool-selection rule, and what rule), and (c) whether One-Shot had access to compatibility coefficients or only to task attributes. Without this, the comparison is not reproducible.

2. **Add a direct skip-action ablation.** Train the identical WeCAN architecture with and without the skip action (keeping WeCA placement, LDDGNN, decoder all fixed). Report makespan, skip frequency during training, and the variance of returns. This single experiment would directly validate the core claim of the paper.

3. **Define PRO-BALM** in the main text (or in the figure caption if it is a baseline from the literature). Fix the duplicate "WeCAN-S(256)" label in Figure 3.

4. **Add error bars to the generalization results** (Figure 2) by running multiple random seeds or multiple problem instances per condition.

5. **Provide a concrete illustrative example** of the optimality gap (3–4 tasks, 2 pools) where list scheduling fails and the skip action fixes it, as suggested by the harsh critic. This would significantly improve the accessibility of Section 4.

## Score and Decision

**Calibration anchors** (all retrieved from the batch):

| Path | Avg Human Score | Comparison to Paper Under Review |
|------|----------------|----------------------------------|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/jsWCmrsHHs.md` (DRL for JSSP) | 7.50 | Stronger experimental design and presentation; the current paper has comparable technical depth but less polished ablation and a few clarity gaps. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/TbTJJNjumY.md` (VRP cross-attention) | 6.25 | Similar structure: novel architecture + strong empirical results + some baseline concerns. Current paper is slightly below in presentation polish but comparable in substance. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/DhH3LbA6F6.md` (RL combinatorial actions) | 6.00 | Similar quality: solid contributions, some concerns about baseline comparisons and missing analysis. Current paper is at a comparable level. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/b9aCXHhdbv.md` (Pipeline parallelism DRL) | 4.50 | Weaker than the current paper: less thorough evaluation and missing key details. Current paper has stronger experiments and more baselines. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/8WtBrv2k2b.md` (Quantum scheduling RL) | 5.00 | Weaker than the current paper: higher variance in reviewer scores, less convincing empirical validation. Current paper has more comprehensive experiments. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/10eQ4Cfh8p.md` (FJSP RL) | 3.00 | Much weaker: poor experimental design, missing baselines and standard deviations. Current paper is substantially stronger. |

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>