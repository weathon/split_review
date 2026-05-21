Now I have all the information needed. Let me write the final consolidated review.

## Summary

The paper proposes WeCAN, an end-to-end reinforcement learning framework for heterogeneous DAG scheduling with task-pool compatibility coefficients. The key ideas are: (1) a weighted cross-attention (WeCA) layer that places compatibility coefficients outside the softmax to handle variable numbers of pools and task types without fixed-dimensional embeddings, (2) a longest-directed-distance GNN (LDDGNN) to encode task dependencies, and (3) a skip-action mechanism inserted into single-pass list scheduling to close a proven optimality gap. Empirical results on TPC-H and Computation Graphs benchmarks show WeCAN achieves 12-18% makespan improvement over heuristics while running at comparable speed.

## Strengths

- **Weighted cross-attention is a principled architectural innovation for heterogeneous scheduling.** The WeCA layer (Eq. 3) places compatibility coefficients outside the softmax, which avoids the information-loss issue of inside-softmax variants that can wash out compatibility profiles. The ablation (Table 3) confirms this design choice matters: the outside version improves over the inside version by ~3.5 percentage points on TPC-H-30 (14.0% vs. 10.5%). This is a concrete, well-motivated contribution with empirical backing.

- **Single-pass inference achieves heuristic-level speed while clearly outperforming all baselines.** WeCAN-Greedy runs in 0.15-1.72s on TPC-H (vs. HEFT 0.18-1.86s) yet delivers 12-18% makespan improvements over the best heuristic. WeCAN-S(256) outperforms the best neural baseline (One-Shot-S(256)) by 5-7.7% on TPC-H and 4-9.5% on Computation Graphs (Tables 1, 2). This is a strong empirical result for a method that generates schedules in one forward pass.

- **Generalization to varying heterogeneous environments is validated.** Figure 2 shows WeCAN maintains strong improvement rates across "more pool," "more pool type," "more task," and "more task type" settings, while One-Shot degrades sharply (e.g., 6.7% vs. 0.9% on "more pool type"). This directly supports the claim that the WeCA design preserves adaptability, and the comparison against a non-heterogeneous baseline (One-Shot) is informative for this particular claim.

- **Theoretical analysis of the list-scheduling optimality gap is novel and well-structured.** Theorem 1 and 2 characterize conditions under which list scheduling cannot reach optimal solutions, and show that adding the skip action (under Assumption 1) recovers surjectivity. The notion of reduced space \(B\) and the analysis of \(TS_{list}\) not being surjective provides a clean framework for a gap that prior work treated heuristically.

## Weaknesses

### Fatal
None.

### Major

- **The paper claims to outperform "state-of-the-art methods" but omits comparison with cited heterogeneous neural schedulers.** The Introduction cites Zhou et al. (2022), Zhadan et al. (2023), and Wang et al. (2025) as methods specifically designed for heterogeneous DAG scheduling, and identifies limitations in how they handle compatibility coefficients. Yet none appear as baselines. The only heterogeneous neural baseline is PPO-BiHyb (Wang et al., 2021), which the paper itself notes is an order of magnitude slower due to its bi-level beam search. Including at least one recent heterogeneous scheduler would be necessary to substantiate the claim of superiority over SOTA. This is the paper's most significant evaluation gap.

- **The skip-action contribution is not isolated on the standard benchmarks.** Tables 1 and 2 report the full WeCAN system (with skip actions), and Table 3 ablates architectural components but does not include a "WeCAN without skip" variant on the standard TPC-H or Computation Graphs datasets. The only skip ablation is Figure 3, which uses an artificially modified heavy-task dataset (1% task replacement). Without this control, it is unclear how much of the 12-18% improvement over heuristics comes from the encoder architecture vs. the skip mechanism. Since the skip action is presented as a key contribution backed by theoretical analysis, its effect on the core results should be quantified directly.

### Minor

- **Evidence that the skip score is learned effectively is thin.** The paper claims the skip-score formula \(u_a(1 - k/2n)^{u_b} + u_c\) "clusters most poor solutions in the high-\(u_a\), high-\(u_c\) region" (Section 4.2), but provides no empirical evidence for this claim (e.g., analysis of learned skip-score values during training, visualization of solution-space clustering, or training dynamics). The theoretical existence guarantee (Theorem 1(iv)) does not ensure the parametric form can express the needed scores or that the REINFORCE objective will discover them.

- **The heavy-task experiment (Figure 3) demonstrates the skip action's benefit only on an artificially constructed scenario.** While this validates the theoretical prediction that heavy tasks trigger the optimality gap, the paper does not characterize whether such tasks occur naturally in the TPC-H or Computation Graphs datasets. This weakens the connection between the theoretical motivation and the practical impact claim.

- **The claim that the outside placement is "crucial" is modestly overstated.** The ablation (Table 3) shows outside placement improves over inside by ~3.5pp on TPC-H-30 (10.5% → 14.0% improvement over Tetris). This is a meaningful but not dramatic difference. The intuitive justification ("normalization effect could lead to the same embeddings") is provided without formal analysis.

### Trivial
None.

## Nice-to-Haves
- Report the number of random seeds used and include standard deviations for all methods in Tables 1 and 2 (currently only reported for neural sampling methods).
- Include a simple heuristic baseline that explicitly accounts for compatibility coefficients (e.g., greedy by \(K_{acc}\)) for a cleaner lower bound.
- Provide analysis of how the skip action is used in practice on standard datasets (e.g., frequency of skip actions taken by the learned policy).

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Reproducibility concerns about missing architectural/training details** — Removed per hard rules: the paper's appendix was stripped by the parser; hyperparameters such as learning rate, embedding dimensions, number of layers, etc., are standard implementation details that the original submission would contain in the appendix. The main text provides sufficient architectural description (Eq. 1-4, Algorithm 1) and the training loss formulation.

- **Criticism that the paper does not cite relevant related work** — Removed per hard rules: you do not have external sources to confirm the existence of any missing related work. The paper already provides a substantial related work discussion.

- **The "inside vs. outside" placement criticism as a structural flaw** — Demoted from what could be read as a fatal criticism to minor. The ablation validates the improvement, and the intuitive justification is provided. The improvement is real even if modest.

- **Missing appendix/proofs** — Removed per hard rules: the parser strips these sections; they exist in the original submission.

- **Formatting/style nitpicks** — Removed per hard rules.

- **Strength Finder strengths that conflict with verified weaknesses** — Several strengths about the skip action closing the optimality gap are retained in weakened form to reflect that the empirical evidence is limited to the heavy-task setting.

## Novel Insights

The harsh critic and strength finder together reveal a paper that has a genuine architectural innovation (weighted cross-attention) and a genuine theoretical contribution (analyzing the list-scheduling optimality gap through the lens of surjectivity between the reduced space and the solution space). However, the skip-action mechanism — despite being the theoretical centerpiece — has surprisingly thin empirical support in the paper's main evaluation. The paper would be significantly strengthened by decoupling these two contributions: show what WeCA alone achieves without skip on standard benchmarks, and separately show what skip adds in the heavy-task regime. This would also resolve the tension between the paper's framing (skip action is central) and the evidence (the main results could plausibly come from WeCA alone).

## Suggestions

1. **Add at least one recent heterogeneous neural scheduler as a baseline** (e.g., Zhou et al., 2022 or Zhadan et al., 2023). Without this, the "SOTA" claim is unsubstantiated.
2. **Report a "WeCAN without skip" variant on the standard TPC-H and Computation Graphs datasets** — this is essential to attribute the improvement to the correct component and connect the theoretical analysis to the main empirical results.
3. **Characterize the natural occurrence of "heavy tasks" in the standard datasets** to ground the skip-action motivation in the actual evaluation setting.
4. **Provide an analysis of learned skip-score values** (e.g., distribution of \(u_a, u_b, u_c\) across training, frequency of skip action selection) to support the claim that the skip score is learned successfully.

## Score and Decision

**Calibration anchors (all from the batch):**

| Path | Avg Human Score | Comparison to Paper Under Review |
|------|----------------|----------------------------------|
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/jsWCmrsHHs.md | 7.50 | Stronger evaluation completeness; comparable contributions. Our paper has a more novel architecture but weaker baseline coverage. |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/jBYQAtzp5Z.md | 6.80 | Stronger theoretical rigor; comparable empirical scope. Our paper is slightly weaker overall. |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/8WtBrv2k2b.md | 5.00 | Similar evaluation quality; different domain. Our paper has clearer contributions. |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/b9aCXHhdbv.md | 4.50 | Weaker empirical evaluation; less clear contributions. Our paper is notably stronger. |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/CJEBFNBLhO.md | 4.25 | Engineering contribution with limited novelty. Our paper has more novel architecture and theory. |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/10eQ4Cfh8p.md | 3.00 | Much weaker in writing, evaluation, and contribution clarity. Our paper is substantially stronger. |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/bntJK4NyIW.md | 2.00 | Fundamentally flawed. Our paper is far stronger. |

The paper sits above the 4-5 range papers (b9aCXHhdbv, CJEBFNBLhO) due to genuine architectural and theoretical novelty, and below the top scheduling papers (jsWCmrsHHs at 7.50, jBYQAtzp5Z at 6.80) due to incomplete baseline coverage and the un-isolated skip-action contribution. The core contributions are solid and well-validated by ablation, but the evaluation gaps prevent acceptance at the stronger anchor level.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>