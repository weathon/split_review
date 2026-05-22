Now let me write the consolidated review.

## Summary

This paper proposes WeCAN, an end-to-end RL framework for scheduling DAGs on heterogeneous resource pools with task-pool compatibility coefficients. The key technical contributions are (1) a weighted cross-attention (WeCA) layer that encodes compatibility coefficients as attention biases outside softmax, preserving adaptability across varying numbers of pools and task types; (2) a longest-directed-distance GNN (LDDGNN) for capturing DAG dependency structure; and (3) a skip-action mechanism in the single-pass generation map, theoretically shown to close list scheduling's optimality gap. Empirical results on TPC-H and Computation Graphs benchmarks show substantial makespan improvements over heuristics and prior neural baselines, with single-pass inference speed close to heuristic methods.

## Strengths

- **Weighted cross-attention with outside-softmax compatibility design.** The WeCA layer (Section 3.1) treats compatibility coefficients as multiplicative biases applied *outside* softmax, enabling the network to distinguish tasks that share identical attribute vectors but differ in their compatibility profile across pools. The ablation study (Table 3) confirms that this outside-placement variant (14.0% improvement over Tetris on TPC-H-30) significantly outperforms the inside-placement variant (10.5%), validating the design choice concretely.

- **Theoretical analysis of the list-scheduling optimality gap and its closure via skip actions.** The paper provides a formal analysis (Section 4, Theorems 1–2) showing that list scheduling cannot guarantee optimality and that introducing skip actions in the single-pass setting yields a surjection capable of representing optimal solutions. The heavy-task experiments (Figure 3) empirically confirm that this gap matters: WeCAN with skip actions achieves 8–9% improvement on heavy-task datasets while the non-skip variant shows only 0–3%, which is consistent with the theory's prediction that heavy tasks benefit most from skip actions.

- **Consistent and substantial empirical gains across diverse benchmarks.** WeCAN achieves up to 18.1% makespan improvement over the best heuristic and up to 9.5% over the best neural baseline on TPC-H and Computation Graphs datasets (Tables 1–2). The gains hold across different graph types (Erdős–Rényi, Layer, Stochastic Block) and the single-pass inference time is competitive with heuristics.

- **Generalization to varying environment sizes.** Under fixed training, WeCAN maintains 6.7–20.4% improvement over best heuristics when pool count, pool type, task count, or task type change, while One-Shot degrades to 0.9–10.2% (Figure 2). This validates the adaptability claim of the WeCA layer.

## Weaknesses

### Major

- **Missing comparison against heterogeneous-capable neural baselines.** The paper cites Zhou et al. (2022), Zhadan et al. (2023), and Wang et al. (2025) as related work on neural schedulers for heterogeneous environments, noting that they handle compatibility coefficients via averaging or fixed-size embeddings. But none of these methods are included as baselines. The comparison with One-Shot (Jeon et al., 2023) is informative — it shows that handling heterogeneity matters — but One-Shot is a homogeneous scheduler and was never designed for compatibility coefficients. To substantiate the claim of "outperforming state-of-the-art methods" for *heterogeneous* scheduling, the paper should include at least one heterogeneous-capable neural baseline, ideally the most directly comparable version of Zhou et al. (2022) or an adapted One-Shot that receives compatibility features. Without this, it is unclear whether WeCAN's advantage stems from its specific architectural innovations or simply from addressing heterogeneity at all.

### Minor

- **Figure 3 has confusing labels.** The figure shows two bars both labeled "WeCAN-S(256)" (blue and green) with very different performance (8.3% vs -2.3% on TPC-H-30-heavy). From context, the green bar is the non-skip variant, but this is not clear from the label. The results themselves are internally consistent — heavy tasks substantially change the problem structure and it is expected that non-skip WeCAN struggles on that variant — but the labeling needs to be disambiguated for readers.

- **Training seed variance is not reported.** Tables 1–2 report standard deviations from sampling multiple trajectories from a single trained model. The ablation study (Table 3) reports variance across 10 test problems. Neither provides variance across independent training runs with different random seeds. For an RL method trained with REINFORCE, this is standard reporting practice and would help establish that the reported improvements are statistically reliable rather than artifacts of a particular training run.

- **The skip-score formula is heuristic and not ablated against alternatives.** The design $u_{\pi_{skip}} = u_a(1 - k/(2n))^{u_b} + u_c$ is motivated by "preventing endless idling" but no comparison is provided against simpler alternatives (e.g., constant score, linear decay, learned state-dependent score). The theoretical guarantee (Theorem 1-iv) only shows that *some* scores exist that achieve optimality; it does not establish that this hand-designed parameterization can realize them. An ablation over skip score formulations would strengthen the practical connection between theory and implementation.

### Trivial

- The figure description from the parser shows garbled text for Figure 1 (confusing "LDDNN" vs "LDDGNN" mentions) — presumably a parser artifact, but the original should be checked.

## Nice-to-Haves

- The paper could provide a brief summary of key implementation details (learning rate, network dimensions, training steps) in the main text rather than deferring entirely to the appendix, which was stripped from this review.
- An intuitive illustrative example of how list scheduling fails and skip actions fix it (beyond the theoretical framing) would make Section 4 more accessible.

## Removed Points

The following points from the reviewer inputs were removed after verification against the paper:

1. *"The comparison with One-Shot is not a fair test because One-Shot cannot represent task-pool compatibility"* — This criticism is overblown. The paper's claim is that WeCAN outperforms existing approaches including a state-of-the-art neural DAG scheduler. Showing improvement over a method that doesn't handle the target problem's key feature is informative; it quantifies the value of addressing heterogeneity. The real issue (addressed above under Major weaknesses) is the absence of a *heterogeneous*-capable neural baseline.

2. *"The non-skip ablation contradicts the main results (0.0% improvement over HEFT vs ~15% on regular data)"* — The heavy-task dataset (1% of tasks replaced with extreme tasks) is fundamentally different from the regular dataset. The non-skip variant performing near/below HEFT on the heavy-task version is not a contradiction; it is exactly what the theory predicts — without skip actions, the model cannot recover from deadline-induced suboptimal orders caused by extreme-resource tasks.

3. *"Claims about compatibility coefficient handling are not well-documented"* — The paper cites specific approaches (Zhou et al., 2022; Zhadan et al., 2023; Wang et al., 2025) and describes why their representations are limiting. This is sufficient for a related-work discussion.

4. *"Specific pool-selection rules for baselines not described"* — These are likely in the appendix which was stripped. Minor point in any case.

5. *"Theoretical analysis not connected to empirical design"* — The paper does connect them: Theorem 1 identifies the gap, the skip action design closes it, and the heavy-task experiments (Figure 3) verify it. The connection is present.

## Novel Insights

None beyond the paper's own contributions. The reviews surface known tensions (heuristic design choices vs theoretical guarantees, completeness of baselines) but do not reveal any unexpected synthesis.

## Suggestions

1. **Add at least one heterogeneous-capable neural baseline.** The most straightforward path is to adapt One-Shot's priority network to accept compatibility features (e.g., include $K_{acc}$ as input), or implement a variant of Zhou et al. (2022). This is the single highest-leverage improvement for the paper.

2. **Fix Figure 3's labeling** so the non-skip and skip variants are clearly distinguished. Report the non-skip variant's performance on both regular and heavy-task TPC-H for clean comparison.

3. **Report results from 3–5 independent training seeds** for at least the main TPC-H-30 and CG-Erdos-Renyi comparisons (greedy and S(64)). This is standard for REINFORCE-based methods.

4. **Ablate the skip-score formula** against simpler alternatives (constant score, linear decay) on the heavy-task datasets to strengthen the connection between the theoretical existence result and the practical design choice.

## Score and Decision

**Calibration process:**

*Round 1 (bracketing):* Searched for "reinforcement learning DAG scheduling heterogeneous" papers in three score bands. Low band (<3.5): returned papers scoring 2.0–3.4 (reject-level). Mid band (3.5–7.5): returned papers scoring 4.0–6.8 (mixed to accept). High band (>7.5): returned papers scoring 8.0 (strong accept). The paper clearly sits in the mid band — well above weak/reject papers but not at the 8.0 level of top papers.

*Bracket: 4.5–7.0*

*Round 2 (narrowing):* Searched more targeted queries inside the bracket. Retrieved anchors at 5.33 (NCO critique — serious comparison issues, rejected), 5.75–6.00 (neural solver selection, WS-option SSCO), 6.00 (HexGen-2), 6.67 (Symb4CO). Reading the 5.33 paper and 6.00 paper in full confirmed that the current paper is substantially stronger than the 5.33-level papers (which had methodological flaws) and comparable to the 6.00-level papers (solid contributions with identifiable but fixable gaps).

*Anchor comparison summary:*
- `bntJK4NyIW` (2.00): Decentralized training — much weaker, different domain.
- `ArJikvI6xo` (3.40): Green FL — weaker, different domain.
- `10eQ4Cfh8p` (3.00): FJSP RL — weaker in empirical depth.
- `b9aCXHhdbv` (4.50): Pipeline parallelism DRL — less empirical breadth.
- `8WtBrv2k2b` (5.00): Quantum scheduling RL — mixed quality.
- `jBYQAtzp5Z` (6.80): Scheduling with predictions — stronger theoretical contributions but different framing.
- `WszeEzjcq2` (5.33): NCO critique — weaker, had serious evaluation issues.
- `AloCXPpq54` (6.00): SSCO HRL — comparable quality; our paper has stronger empirical breadth.
- `CFLEIeX7iK` (5.75): Neural solver selection — comparable.
- `Cs6MrbFuMq` (6.00): HexGen-2 — systems paper, comparable.

*Final score:* 6.0. The paper has a novel architecture, theoretical grounding, and strong empirical results across diverse settings. The main gap is the missing heterogeneous neural baseline, which is fixable and does not invalidate the core contributions but does weaken the "state-of-the-art" claim in its current form.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>