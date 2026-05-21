Now I have all the calibration data I need. Let me synthesize the review.

## Final Analysis

**Bracket (Round 1)**: The paper sits between the weak anchors (2-3.4) and the strong anchors (7.5+). Middle anchors cluster at 4.5-6.8. Initial bracket: 4.5-7.0.

**Narrowing (Round 2)**: Compared to the 4.50 DRL-PP paper (weak evaluation, unclear contributions) and the 4.75 multi-task CO solver (limited novelty), the WeCAN paper is clearly stronger — it has more original architecture, better ablation studies, and theoretical analysis. Compared to the 5.00 quantum scheduling paper (high variance, unclear problem framing), WeCAN has clearer contributions and stronger empirical validation. Compared to the 6.50 GraphRouter paper (accepted, thorough evaluation), WeCAN has less rigorous evaluation (baseline fairness concerns, missing ablation). The paper sits between these anchors.

**Final score**: 5.5

Now let me write the review.

Key decisions on which weaknesses to keep/remove:
1. **Baseline fairness (One-Shot, PPO-BiHyb)**: KEEP as MAJOR. The paper doesn't describe how these baselines were adapted for heterogeneous settings. The paper cites heterogeneous-aware methods (Zhou et al. 2022, Wang et al. 2025) but doesn't compare against them. This is a real gap.

2. **Missing skip-action ablation on standard datasets**: KEEP as MINOR. The paper's theory specifically identifies heavy tasks as the key case for skip actions, so the absence on standard datasets is notable but not fatal.

3. **Overclaiming theoretical guarantees**: KEEP as MINOR but rephrase. The theorems are existence claims, not performance guarantees for the learned policy. The paper's framing ("closes the gap") is slightly overstated.

4. **Generalization results lack error bars**: KEEP as MINOR. Figure 2 reports single numbers.

5. **PRO-BALM undefined**: REMOVE. The appendix is stripped from the extracted text; PRO-BALM could be defined there.

6. **Skip-score formula lack of justification**: KEEP as MINOR. The specific functional form isn't derived.

7. **√d placement**: WEAKEN to a trivial note. Could be a typesetting issue.

8. **Missing related works**: REMOVE per instructions.

Let me write the final review.## Summary

This paper proposes WeCAN, an end-to-end reinforcement learning framework for heterogeneous DAG scheduling with task-pool compatibility coefficients. The key technical contributions are (1) a weighted cross-attention (WeCA) mechanism that multiplies compatibility coefficients outside the softmax normalization to preserve task-pool compatibility information, (2) a longest-directed-distance graph neural network (LDDGNN) for encoding task dependencies, and (3) a skip-action mechanism that enables the single-pass scheduler to overcome the optimality gap inherent in list-scheduling-based methods. The paper provides a theoretical analysis showing that list scheduling cannot represent optimal solutions and that the proposed skip action can close this gap (in an existence sense). Empirical results on TPC-H and Computation Graphs datasets show that WeCAN achieves 9-18% improvement over the best heuristic baselines and 7-10% improvement over existing neural baselines, while maintaining runtime comparable to heuristics.

## Strengths

- **Weighted cross-attention with compatibility coefficients outside softmax (Section 3.1).** The design places the compatibility coefficient matrix outside the softmax normalization, which the paper motivates with a concrete counterexample: two tasks with identical attributes but different compatibility profiles would collapse to the same embedding under an inside-softmax placement, whereas the outside placement preserves the distinction. The ablation study (Table 3) validates this design empirically — the outside-placement variant (WeCA + LDDGNN, 19908 makespan) outperforms the inside-placement variant (WeCA-inside + LDDGNN, 20729 makespan) by ~4% on TPC-H-30. This is a clean architectural insight with clear empirical support.

- **Empirical outperformance with competitive runtime (Tables 1 and 2).** WeCAN-greedy achieves the lowest makespan among all methods across both datasets (e.g., 18.1% improvement over best heuristic on TPC-H-30, 9.5% over best neural baseline) while requiring only 0.15s inference time — comparable to heuristics and orders of magnitude faster than the multi-round PPO-BiHyb (20.48s). The WeCAN-S(256) sampling variant further improves results with only modest additional computation (2.43s on TPC-H-30). The standard deviations reported across random seeds are small (typically ±10–50), indicating stable performance.

- **Skip-action mechanism and theoretical analysis of the list-scheduling optimality gap (Section 4).** The paper formalizes the reduced-space framework (B_f, T, S) and proves that list scheduling (S_list) is not surjective, meaning it cannot represent optimal solutions for certain instances. The skip-action construction extends the generation map to achieve surjectivity (Theorem 1). The heavy-task experiments (Figure 3) provide empirical validation that the skip action closes this gap specifically where it matters most: instances with high-resource-demand tasks. This combination of theoretical analysis and targeted empirical validation strengthens the paper's core narrative.

- **Comprehensive ablation study (Table 3).** The paper systematically ablates both the WeCA layer (inside vs. outside placement, encoder-only vs. decoder-only variants) and the LDDGNN (forward GAT, bidirectional GAT). Each variant produces higher makespan, confirming that both components contribute meaningfully. The "WeCA-final-only + LDDGNN" variant degrades to near-heuristic levels (0.5% improvement), which convincingly demonstrates that the WeCA layers throughout the architecture are essential.

## Weaknesses

### Fatal
None.

### Major

- **Fairness of neural baseline comparisons.** The paper compares against One-Shot (Jeon et al., 2023) and PPO-BiHyb (Wang et al., 2021), neither of which was designed for heterogeneous DAG scheduling with compatibility coefficients. The paper itself acknowledges that One-Shot "does not consider compatibility coefficients or pool allocation" (line 63). However, it does not describe how these baselines were adapted to the heterogeneous setting — whether their architectures were modified, whether compatibility information was provided as input, or whether the training distribution was changed. Meanwhile, the paper cites heterogeneous-aware methods (Zhou et al., 2022; Wang et al., 2025) but does not compare against them. This makes the claimed "state-of-the-art" comparison over baselines that are structurally disadvantaged uninterpretable. The comparison against heuristics (Tetris, HEFT, CP, etc.) remains valid and informative, but the neural baseline comparison needs either proper adaptation of the baselines or explicit acknowledgment of the limitation.

### Minor

- **Missing skip-action ablation on standard (non-heavy) datasets.** The skip action is a core contribution, and the paper claims it is important even in the general case (Theorem 1). Yet the only empirical comparison of skip vs. no-skip is on synthetic heavy-task instances (Figure 3). The main results (Tables 1, 2) report only the full WeCAN model with skip actions. Without a no-skip variant on standard datasets, the reader cannot determine how much of WeCAN's improvement over baselines is attributable to the skip mechanism versus the weighted cross-attention or LDDGNN architecture. The paper's theory specifically identifies heavy tasks as the major beneficiary, so the absence is not fatal, but it is a gap that should be addressed.

- **Generalization results lack statistical reporting (Figure 2).** The out-of-distribution generalization experiments report single percentage improvements without error bars, confidence intervals, or indication of variance across seeds or test instances. Given the modest dataset sizes, this makes it difficult to assess whether the reported gains (e.g., 6.7% on "more pool type") are stable or due to random variation.

- **Overclaiming on theoretical guarantees.** Theorems 1 and 2 are existence claims: there exist scores that allow the greedy algorithm or sampling to reach an optimal solution. The paper's language ("closes the gap," "fixes the optimality gap") implies a stronger practical guarantee than the theory supports. The paper does not analyze optimization difficulty, provide bounds on the suboptimality of the trained policy, or show that the network actually learns to exploit the skip action on non-heavy instances. The theory shows the *capacity* exists; the experiments show it works on heavy tasks. The framing should match this more carefully.

- **Skip-score formula lacks justification.** The formula `u_skip = u_a (1 - k/(2n))^{u_b} + u_c` is presented without derivation or analysis of why this specific functional form is chosen. The paper states it "prevents the skip action from being overly prioritized" (line 148) but provides no formal analysis of how this formula achieves that goal versus alternatives. Given the heuristic nature of the formula, this detracts from the otherwise well-motivated architecture.

### Trivial

- **Equation notation for attention scaling.** The WeCA equation (line 124) writes `g_v = f_v + softmax(q_v^T K^c) / sqrt(d) diag{K_acc} V^c`, where the division by sqrt(d) is applied to the softmax output rather than inside the softmax as in standard Transformer attention. This is an unusual placement that could be a typesetting error. The authors should clarify whether this is intentional or a formatting artifact.

## Nice-to-Haves

- Provide a version of WeCAN without skip actions on the standard datasets (Tables 1, 2) to isolate the contribution of the skip mechanism.
- Add error bars or variance information to Figure 2's generalization results.
- Include a brief justification or derivation of the skip-score formula, or replace it with a more principled mechanism (e.g., a learned threshold).

## Removed Points

- **PRO-BALM undefined in Figure 3:** The paper's appendix is stripped from the extracted text; PRO-BALM may be defined there. Additionally, the figure's text description shows "WeCAN-S(256)" appearing twice, which is likely a parser artifact from the original figure. These are not verifiable issues from the paper as extracted.
- **Missing related works:** Per policy, I cannot verify the existence of external references.
- **Pure formatting/style nitpicks:** Removed per instructions.
- **Criticisms about reproducibility (hyperparameters, training details):** The paper provides the architecture, training algorithm (REINFORCE), and references to Appendix for details. The appendix is stripped, so these are not verifiable gaps.
- **The √d as a major issue:** This is a minor notation question, not a substantive weakness.

## Novel Insights

The reviews surface an interesting tension in the paper's evaluation strategy. The paper's strongest empirical evidence — the heavy-task ablation showing that skip actions improve performance precisely where list scheduling's optimality gap is largest — directly supports the theoretical claim about the *existence* of a gap. But the same experiments also reveal the paper's weakness: by not testing the no-skip variant on standard datasets, the paper leaves open the question of whether the skip action is a general-purpose improvement or a targeted fix for edge cases. This is a genuinely informative gap that points to a clear path for strengthening the paper in revision.

## Suggestions

1. **Address the baseline fairness concern directly.** In the rebuttal, describe how One-Shot and PPO-BiHyb were adapted (or state that they were used as-is, and acknowledge this as a limitation of the comparison). If feasible, add a comparison against a heterogeneous-aware baseline such as Zhou et al. (2022) or a simple adaptation of One-Shot that accepts compatibility coefficients as input features.

2. **Add a no-skip variant of WeCAN to Tables 1 and 2.** This is a single additional row that isolates the contribution of the skip mechanism on standard datasets. If the improvement is small, this is still informative — it would validate the theoretical claim that the skip action primarily benefits heavy-task cases.

3. **Add error bars or confidence intervals to Figure 2** and report the number of test instances and random seeds used.

4. **Tone down the theoretical framing** to match the existence nature of the guarantees. Replace "closes the gap" with "can close the gap in principle; empirically validates on heavy-task instances."

5. **Clarify the skip-score formula** with a brief derivation or a reference to the appendix for the full justification.

## Score and Decision

**Calibration Details:**

**Round 1 (bracketing):** Searched for "reinforcement learning for DAG scheduling heterogeneous" in three bands:
- < 3.5: Papers scoring 2.0–3.4 (irrelevant or weak submissions)
- 3.5–7.5: Papers scoring 4.0–6.8 (e.g., DRL-PP at 4.50, quantum scheduling at 5.00, fair scheduling with predictions at 6.80)
- > 7.5: Papers scoring 7.75–8.0 (strong accepted papers)

**Initial bracket:** 4.5–7.0

**Round 2 (narrowing):** Searched 4.5–6.0 and 6.0–7.5 for more specific anchors:
- **H-Rockmate (5.00, Reject):** A practical systems paper for memory re-materialization scheduling. Clearer practical motivation than WeCAN but weaker architectural novelty and more ad-hoc design choices. WeCAN has stronger theoretical grounding and cleaner architecture. *WeCAN is slightly stronger.*
- **Multi-task CO solver (4.75, Reject):** Applies existing MAB techniques to multi-task CO training. Limited novelty, missing error bars, unconvincing performance claims. *WeCAN is clearly stronger.*
- **GraphRouter (6.50, Accept):** A graph-based LLM selection method with thorough experiments and clear motivation. Some concerns about realistic setting and missing justifications. *WeCAN has comparable architectural novelty but weaker evaluation rigor. GraphRouter is slightly stronger.*

**Final calibration:** The paper sits above the 4.5–5.0 range of rejected scheduling papers with fundamental issues, but has evaluation gaps (baseline fairness, missing ablation, statistical reporting) that prevent it from reaching the 6.5+ level of accepted papers. Score: 5.5.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>