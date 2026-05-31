## Summary

GUI-Spotlight is an iterative visual grounding model for GUI agents that "thinks with images" by invoking specialized tools (*crop*, *extract*, *find_color*) to progressively narrow its focus to the target screen element. The model is trained in three stages—SFT warm-up, RL with a modified GSPO objective (with an auxiliary cross-entropy loss to prevent collapse), and a further RL stage on high-resolution data with bucketed tool-balanced sampling. With only 18.5K curated training samples, it achieves 52.8% on the high-resolution ScreenSpot-Pro benchmark, outperforming 7B-scale peers that use orders of magnitude more data.

---

## Strengths

- **Exceptional data efficiency on the primary benchmark.** GUI-Spotlight reaches 52.8% on ScreenSpot-Pro with only 18.5K samples, while closest 7B competitors use 107K (UI-Venus), 1.56M (GTA-1), or 9.6M (V2P, GUI-Actor) samples. The absolute improvement of +14.1 pp over the UI-TARS-1.5-7B initialization and the +11.9 pp improvement when starting from the non-GUI-specific Qwen2.5-VL-7B are both credible evidence of the approach's value.

- **Technically sound stabilization of multi-turn RL.** The paper identifies a real failure mode—vanilla GRPO/GSPO collapses in multi-turn tool-use settings because format violations produce sparse rewards and high-variance gradients—and proposes a concrete fix: an auxiliary cross-entropy term computed only over format-valid, result-correct rollouts. Figure 3 (right panel) shows the collapse at step ~300 for baselines vs. monotonic improvement for the proposed objective. This is a practical contribution to the RL-for-tool-use literature.

- **Transparent reporting including negative results.** The systematic ablation in Section 4.1 (seven RL variants) and Section 4.2 (answer reward shape, crop/extract weight ratio) honestly documents what failed and why. This is relatively rare and valuable for practitioners.

- **Training-free vs. trained iterative inference ablation (Section 5.4).** Demonstrating that the base model has "virtually no multi-step reasoning capacity" (7.6%) whereas the trained version reaches 52.8% cleanly isolates the contribution of post-training.

---

## Weaknesses

### Fatal
None.

### Major

1. **Inference overhead is not characterized.** The iterative tool-use pipeline requires multiple model forward passes and image operations per query. Since the method is compared against single-pass models, the per-sample latency, average number of tool calls, and total FLOPs are essential for a fair evaluation. A method that is 3-5× slower in wall-clock time achieves a fundamentally different cost-accuracy trade-off, which the paper leaves entirely unquantified.

2. **Performance gains are inconsistent across benchmarks.** On OSWorld-G (Table 5), GUI-Spotlight (UI-TARS init) achieves 62.7%, barely above its own baseline (UI-TARS-1.5-7B: 61.9%, +0.8 pp), and clearly below GTA1-7B (67.7%). On UI-Vision (Table 4), GUI-Spotlight (UI-TARS) at 23.4% falls below UI-Venus-Ground-7B (26.5%). The abstract's claim of "substantially outperforming comparable 7B baselines" is accurate only for ScreenSpot-Pro; on the other two benchmarks the gains are marginal or absent. This cross-benchmark inconsistency is unexplained and weakens the generality claim.

3. **The gain over simple iterative inference (strategy ②) is modest.** Figure 5 shows that merely cropping around a first-pass click prediction (47.6%, requiring no special training) already closes most of the gap to fully trained GUI-Spotlight (52.8%). The +5.2 pp incremental benefit of the full multi-tool RL system is real but modest, and the paper does not deeply analyze what qualitative capabilities (e.g., color-guided focusing, multi-step reasoning chains) account for that delta.

### Minor

1. **Stage 1 SFT causes a large accuracy drop (39.3% → 17.8%)** that is acknowledged but not sufficiently explained. The drop is attributed implicitly to format re-learning, but this is a large regression that could indicate SFT overfitting or catastrophic forgetting. More analysis would strengthen the paper's narrative.

2. **Reward weight ablation is incomplete.** The five reward weights (α₁,...,α₅) are fixed without ablation beyond varying the crop/extract ratio. Given that *r₁* (answer), *r₄* (find_color), and *r₅* (format) each have significant weights, the sensitivity of final performance to these choices is unknown.

3. **Figure 2 axis and stage labeling are inconsistent** with the text's stage numbering (the figure's "Stage 0" through "Stage 3" maps to "initialization," "Stage 1," "Stage 2," "Stage 3" in the text), which creates momentary confusion when cross-referencing.

### Trivial

None of consequence.

---

## Nice-to-Haves

- A latency and average-tool-call count comparison with single-pass baselines would let readers evaluate the accuracy–compute trade-off.
- Qualitative analysis of failure cases, especially across the three benchmark domains, would help explain the cross-benchmark inconsistency.
- An ablation removing any one of the three tools (crop-only, extract-only) would sharpen understanding of how much each tool type contributes.

---

## Novel Insights

The most substantive novel observation is the training-stability finding: in multi-turn tool-use RL, the standard GRPO/GSPO collapse mechanism is triggered by format violations rather than reward sparsity per se, and it can be remedied by anchoring the policy with a lightweight cross-entropy term computed over correctly-formatted, correct-answer rollouts (with bucketed tool-type sampling in later stages to prevent tool-selection imbalance). This is a non-obvious, empirically grounded insight that generalizes beyond GUI grounding to any agentic RL scenario with structured tool output formats.

---

## Suggestions

- Add a table or paragraph reporting average number of tool calls per query and per-query inference latency relative to single-pass baselines; this is essential context for practitioners.
- Provide a per-domain breakdown for UI-Vision and OSWorld-G comparable to the ScreenSpot-Pro analysis, and discuss why gains are smaller on these benchmarks (potential hypotheses: lower resolution, different UI modality, reduced benefit of iterative zooming).
- Ablate the contribution of the `find_color` tool specifically; it depends on the model correctly identifying an RGB color for the target element, which may fail for icons or text-only elements—understanding when it helps vs. hurts would be informative.
- Clarify whether the comparison to UI-Venus-7B (107K samples) and GTA-1-7B (1.56M samples) controls for the backbone model strength; if those models start from weaker backbones, the data efficiency story changes somewhat.

---

## Score and Decision

The paper makes a genuine, well-documented contribution: iterative tool-use for GUI grounding trained with a stabilized multi-turn RL objective achieves strong data efficiency on the ScreenSpot-Pro benchmark. The methodological insight on RL collapse prevention is practically valuable. However, the lack of inference cost characterization, inconsistent cross-benchmark gains, and modest marginal improvement over simple iterative inference (without special training) prevent a higher rating. The work is above the acceptance bar but not a clear strong accept.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>