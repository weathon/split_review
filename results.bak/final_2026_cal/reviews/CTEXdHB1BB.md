Now I have a solid calibration. Let me write the final consolidated review.

**Calibration summary:**

Round 1 bracketing: The paper sits clearly above the weak band (scores ~2-3, Reject) and well below the strongest band (scores ~8, Oral). I bracketed it between 3.5 and 7.5.

Round 2 narrowing: I read 6 anchors in full and compared against CANON systematically:

- **Segmental Advantage Estimation (4.67, Reject)**: Narrower evaluation, less theoretical grounding. CANON is clearly stronger.
- **QAE (5.50, Accept Poster)**: Related problem (advantage baseline design) but tested on only 3 math benchmarks vs. CANON's 6 math + 3 logic tasks across 3 models. CANON is broader and comparably principled.
- **ExGRPO (6.00, Accept Poster)**: Experience replay for GRPO. Comparable evaluation breadth but CANON has stronger theoretical framing (Theorems 1 & 2). CANON is slightly stronger.
- **GFPO (6.00, Accept Poster)**: Length control via filtering. Only tested on 1 model (Phi-4) vs. CANON's 3 models. CANON has broader scope and theoretical grounding. CANON is stronger.
- **Entropy Control (6.50, Accept Poster)**: Entropy regularization for LLM-RL. Only tested on 1.5B models vs. CANON's 1.5B/7B/8B. CANON has comparable theoretical depth and broader empirical validation.

Based on these comparisons, CANON sits at the higher end of this cluster — it has stronger evaluation breadth and comparable theoretical grounding to the best anchors. Score: **6.5**.

---

## Summary

This paper introduces CANON (Conditional advaNtage estimatiON), a method that regroups sampled responses by a target metric (e.g., entropy, response length) into two equal-sized groups, then computes an inter-group advantage (revealing which metric trend yields higher reward) and an intra-group advantage (identifying better responses within the same group). The core idea — letting the data determine which metric trend is beneficial rather than imposing a hand-crafted directional penalty — is clean and well-motivated. Results across three LLMs (Qwen2.5-Math-7B/1.5B, Llama3.1-8B) on six math benchmarks and three complex logic reasoning tasks show consistent improvements: CANON-Inter (entropy) achieves +1.9 points on math, CANON-Intra (entropy) achieves +2.9 points on logic, and CANON-Eff (length-based) establishes a better Pareto frontier for the performance-efficiency trade-off.

## Strengths

1. **Empirical gains on both math and complex logic reasoning are credible and consistent.** CANON-Inter (entropy) achieves 57.6 average math accuracy vs. DR.GRPO's 55.7 (+1.9), with a 5.0-point gain on AIME24. CANON-Intra (entropy) achieves 29.1 on logic vs. 26.2 (+2.9), with a 5.2-point gain on the XLarge subset. The improvements hold across six math benchmarks and three logic difficulty tiers (Table 1).

2. **Theoretical grounding for the regrouping design.** Theorem 1 proves that the inter-group advantage amplifies the grouping metric's influence relative to DR.GRPO when groups are equal-sized. Theorem 2 proves that CANON does not amplify independent conditions — the effect is selective. Eq. (7) shows DR.GRPO is a special case of CANON with μ=0.5, cleanly connecting the new method to prior work.

3. **Efficiency experiments (CANON-Eff) are thorough and convincing.** The Pareto frontier analysis (Figure 4c) shows CANON-Eff dominates all baselines across the performance-efficiency trade-off. CANON-Eff (α=0.96) reduces token consumption by 26.3% with only 0.4% accuracy loss. The finding that Length Reward (+) collapses from 54.8 to 22.5 when over-tuned while CANON remains stable is a strong practical advantage.

4. **Training dynamics analysis validates the mechanism.** Figure 2 shows CANON-Inter drives rapid math improvement with decreasing entropy, while CANON-Intra promotes exploration and reflection gains that later boost complex logic performance. Figure 6 shows CANON-Dynamic achieves both positive rethinking gain and high training reward — a combination neither individual variant attains.

5. **Evaluation across three LLMs (1.5B, 7B, 8B) and two task families.** This breadth strengthens the claim that the method generalizes beyond a single architecture or task type.

## Weaknesses

### Major

1. **CANON-Dynamic scheduling strategy selection appears to use test-set results.** The paper tries four scheduling strategies per model and selects the best one to report as CANON-Dynamic (Section 5.2). The authors state that "The shown results of CANON-Dynamic are derived from one of the tried scheduling strategies that achieve strong performance in both scenarios" and select different strategies per model (Cosin-First-Inter-Later-Intra for Qwen-7B/Llama-8B, First-Inter-Later-Intra for Qwen-1.5B). No validation set is mentioned. The baseline (DR.GRPO) had no equivalent strategy search, so the comparison in Figure 3 is not properly controlled. This inflates the apparent improvement from scheduling. **However, this issue is bounded in scope**: (a) the paper's core contributions (CANON-Inter, CANON-Intra, CANON-Eff in Table 1, Table 3) do not depend on the scheduling, and (b) the broad trend "First-Inter-Later-Intra consistently performs better than DR.GRPO across three models and two tasks" is stated *before* the model-specific selection and is supported by Table 2. The CANON-Dynamic claims in Section 5.2 need either a proper validation split or a downgraded claim; the rest of the paper is unaffected.

### Minor

2. **No confidence intervals or variance estimates for any benchmark.** This is especially relevant for AIME 2024 (30 problems) and AIME 2025 (30 problems), where a 5-point difference (e.g., CANON-Inter vs DR.GRPO on AIME24: 32.7 vs 27.7) could fall within sampling noise. While the overall pattern across six math benchmarks is consistent, the small benchmarks would benefit from standard errors or significance tests. This is a common limitation in the field (single-run evaluation is standard), but worth noting.

3. **The weighted advantage design (Eq. 9) could use a clearer intuitive explanation.** When o∈C⁺ (the group being penalized, e.g., longer responses), the formula becomes α·R_o – mean(C⁻). The multiplication of α on R_o rather than on the baseline is somewhat unintuitive and the paper does not explain why this asymmetry was chosen over alternatives.

### Trivial

4. **The method only tests two grouping metrics (entropy and length).** While this is sufficient to demonstrate the idea, an ablation with a random (non-informative) grouping would provide a cleaner demonstration that the signal comes from the metric rather than the splitting operation itself.

## Nice-to-Haves

- Include a random-grouping ablation to confirm that the conditional regrouping signal, not just any split, drives improvement.
- Add a held-out validation split for the CANON-Dynamic schedule selection, or present the scheduling results as exploratory/post-hoc analysis.

## Removed Points

- Criticism that proofs are "in the appendix (unavailable to the reviewer)" — removed per instructions (appendix content exists in the original submission).
- Criticism about missing related work — removed per instructions (cannot verify from external sources).
- Criticism about the method not being validated on tasks beyond the paper's stated scope — removed per instructions (scope creep).
- Strength about "addressing an important problem" — removed as generic/superficial.

## Novel Insights

Beyond the paper's own contributions, the most interesting synthetic observation from the review process is that CANON's core idea — using the data's own group-conditional reward structure rather than a predefined penalty — creates a form of implicit curriculum learning. The training dynamics (Figure 2) show that CANON-Inter rapidly exploits known patterns while CANON-Intra nurtures exploration, and the scheduling finds a middle path. This suggests that the advantage *baseline design* in group-relative RL may be a more powerful control knob than the field has appreciated — a point reinforced independently by the QAE anchor paper (which replaces mean with quantile). One could view CANON as generalizing the baseline from a single global mean to a two-group conditional mean, opening the door to richer multi-group or hierarchical advantage structures.

## Suggestions

1. **For the scheduling results**: commit to a single pre-specified schedule (e.g., First-Inter-Later-Intra, which already consistently beats DR.GRPO across models) and report results on test data not used for schedule selection. Alternatively, clearly state which results are post-hoc selections and downgrade the CANON-Dynamic claims from head-to-head comparison to exploratory analysis.
2. **Add error bars or confidence intervals for small benchmarks** (AIME 24/25, AMC) where sampling variance is high.
3. **Include a random-grouping ablation** where responses are split randomly rather than by metric, to directly verify Theorem 2's prediction that the signal comes from the grouping metric, not the split itself.
4. **Clarify the intuition behind Eq. (9)**: explain why α multiplies the reward rather than the baseline in the weighted advantage formulation.

## Score and Decision

**Bracket (Round 1)**: [3.5, 7.5] — clearly above rejected-level GRPO variants (scores 2-4) and below oral-level papers (score 8).

**Narrowing (Round 2)**: Compared against QAE (5.50), ExGRPO (6.00), GFPO (6.00), and Entropy Control (6.50). CANON has stronger empirical breadth (more models, more tasks) and comparable theoretical grounding to the best of these. The scheduling weakness is real but bounded and does not affect the core claims.

**Final Score**: 6.5 — a solid Accept with a worthwhile contribution and clear, well-supported core results, despite a non-trivial issue with the scheduling experiments that the authors should address.

**Calibration anchors used across rounds**:
| Anchor ID | Score | Round | Comparison |
|---|---|---|---|
| 0vs1YLmmQa | 2.00 | R1 | Much weaker — rejected diff. LM paper |
| OHaFgEa0yZ | 3.00 | R1 | Much weaker — GRPO calibration critique |
| VZermIifAQ | 3.00 | R1 | Much weaker — withdrawn entropy GRPO |
| 0czAcXMBNO | 3.00 | R1 | Much weaker — withdrawn λ-GRPO |
| OxipawhYpE | 4.67 | R1 | Weaker — segmental advantage, narrower eval |
| 4DJoBOQNd0 | 5.50 | R1 | Weaker — conditional reward modeling, less evaluative breadth |
| 7JbWlwNltD | 4.00 | R1 | Weaker — judge LRM, different problem |
| WDP5b3mtFV | 5.50 | R1 | Comparable — QAE has similar problem framing but narrower eval |
| LqazVN5epT | 6.50 | R2 | Comparable — entropy control, but tested only on 1.5B models |
| 701tjQXWVk | 6.00 | R2 | Slightly weaker — ExGRPO, comparable breadth, less theory |
| UKOqoULbZS | 6.00 | R2 | Slightly weaker — GFPO, only 1 model tested |
| cRJNk4bhZi | 6.50 | R2 | Different domain (chart), comparable rigor |
| 0tzvmjMcXC | 6.00 | R2 | Different domain (MLLM), comparable approach |

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>