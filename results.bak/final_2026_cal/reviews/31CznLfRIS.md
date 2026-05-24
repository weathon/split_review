I have thoroughly read the paper and verified all reviewer claims against the actual content. Here is my consolidated review.

---

## Summary

VideoJudge introduces a bootstrapping framework for training MLLM-based evaluators for video understanding. The core idea is a generator-evaluator pipeline that iteratively produces and validates training examples across a 1–5 rating scale, yielding 103K training examples without human annotation. Models fine-tuned on this data (VideoJudge-3B, VideoJudge-7B) show improved judgment capabilities over their base backbones, with particularly strong results in pairwise evaluation. The paper additionally explores instance-specific rubric generation at test time. The authors release models, data, and benchmarks.

## Strengths

- **Bootstrapping pipeline is a practical contribution.** The generator-evaluator loop (Algorithm 1) produces 103,825 training examples across 20,765 unique video-instruction pairs from 25K seed examples, all without human annotation. This directly addresses the real problem of scarce evaluation data for video understanding.

- **Pairwise evaluation results are solid, especially on human-annotated data.** VideoJudge-7B achieves 93.67% accuracy on VideoJudge-Pairwise-H (human-annotated) and 98.60% on the self-constructed VideoJudge-Pairwise benchmark (Table 3). On the independent VideoAutoArena benchmark, it reaches 85.49, competitive with Qwen2.5-VL-72B's 89.80. The pairwise signal is the paper's cleanest evidence.

- **Temperature robustness is a genuine improvement.** Figure 4 shows VideoJudge maintains or improves Spearman correlation as temperature increases (0.66→0.73), while the base Qwen2.5-VL-3B degrades sharply (0.56→0.42). This robustness has practical value for non-deterministic evaluation settings.

- **Instance-specific rubric generation is a novel and promising direction.** VideoJudgeR-3B, trained to generate rubrics at test time, achieves MAE 0.59 and correlations ~0.74 on 1000 examples (Table 2), comparable to Qwen2.5-VL-32B/72B. Human evaluation shows its rubrics preferred over GPT-4o-mini's (53.4% win rate) and Qwen-72B's (63.9%).

- **Open release of models, data, and benchmarks** supports reproducibility and future research — a meaningful community contribution.

## Weaknesses

### Major

- **Pointwise evaluation has a severe calibration failure that undermines the reliability claims for that setting.** The paper's own error analysis (Section 6.2) reports that 81.3% of rating-4 responses are scored as 5, 46.6% of rating-3 responses are inflated to 5, and only 36.9% of rating-3 responses receive the correct score. The model overestimates by ≥2 points in 14.8% of cases but underestimates by the same margin in only 1.5%. This means the pointwise judge effectively *cannot distinguish the middle-to-upper range of the rating scale*. While the paper acknowledges this in the Limitations section, the acknowledgment is separated from the results presentation, and the pointwise results in Table 1 are presented as primary evidence of the model's capability. The positive correlations in Table 1 may reflect rank-ordering ability that survives this bias, but the absolute rating predictions are unreliable.

- **The headline comparative claims ("matching or surpassing 10× larger models") rest heavily on self-constructed benchmarks that share distribution with the training data.** The two main pointwise benchmarks (VideoJudgeLLaVA-MetaEval, VideoJudgeVCG-MetaEval) are built using the same bootstrap pipeline (Algorithm 1) that generated the training data. The paper acknowledges a "partial 'closed-loop' effect" in Limitations (Section 7), but this appears after the results. On independent benchmarks the picture is weaker: VideoJudge-7B achieves PSUP 0.66 on LongVideoBench vs. Qwen2.5-VL-32B's 0.73, and MAE 1.46 on VateX vs. 1.43. The self-constructed benchmarks should be clearly separated from independent ones in presentation.

- **The generator and evaluator models (G and E) used in bootstrapping are not identified in the main text.** The paper refers to "strong vision-language models (§A.2)" but never names them in the main body. Whether G/E is Qwen2.5-VL-72B, GPT-4o, or something else fundamentally changes how to interpret the results — if it is the same large model family used as baselines, then VideoJudge is partly a distillation of that model's preferences. This is critical methodological information that belongs in the main text.

### Minor

- **The acceptance threshold α and maximum iterations T are defined but never reported.** These are essential reproducibility details. The only threshold value mentioned is when constructing the meta-evaluation benchmarks ("threshold 0"), which is a different use of the threshold parameter.

- **Human validation of pairwise data is restricted to the 2-vs-3 rating boundary** (the region of most generator-evaluator disagreement). This yields >92% correctness on ~200 hard pairs, which is useful evidence but does not validate the overall rating scale or the pointwise ratings. The paper overgeneralizes slightly from this narrow validation.

- **The rubric-trained model is evaluated on a small subset.** VideoJudgeR-3B is trained on only 10% of the pointwise data and evaluated on 1000 examples. The results are promising but preliminary; it is unclear how well they generalize.

- **No confidence intervals or statistical significance tests are reported** for the comparisons in Tables 1 and 3, where many differences between models are small (e.g., Spearman 0.78 vs. 0.80).

### Trivial

- None.

## Nice-to-Haves

- An analysis of selection bias: of the 25K seed examples, how many were discarded for not producing 5 valid responses? Do the retained 20,765 examples have systematic differences from discarded ones?
- Reporting the computational cost of the bootstrapping pipeline would help practitioners assess the trade-off against human annotation.
- An analysis of why the pairwise feedback signal helps the 3B/7B models but has mixed effects on the VideoJudge variants would strengthen the paper.

## Removed Points

These points were flagged by reviewers but are removed or downgraded with justification:

- **Criticism that the abstract "conflates" LLM vs MLLM comparison**: The abstract states "LLM judges (Qwen3) models perform worse than MLLM judges (Qwen2.5-VL)." This is a factual comparison of the two tested families. The paper thoroughly discusses the modality difference (text descriptions vs. video input) as a key finding. The contrast is an explicit contribution, not a conflation.

- **Criticism that "several models were excluded" without identifying them**: The paper names the excluded models in Section 4.1 (VideoLLaMA3-7B, VideoChat-Flash, Keye-VL, SmolVLM2) and explains they "failed to follow instructions or produce valid scores." This is transparent.

- **Criticism about BERTScore/BLEU being weak proxies**: The monotonicity check in Section 5.1 is a sanity check (not the paper's main evidence), and the paper supplements it with VQAScore and human evaluation. The criticism expects standards beyond what a data quality sanity check requires.

- **Criticism that the pairwise human validation "over-generalizes"**: The paper says the human evaluation "validates that the generated pairwise data is consistent and reliable, even in the most ambiguous rating regions." This is precisely scoped to pairwise data at the 2-vs-3 boundary and appropriately qualified. The claim is not overgeneralized.

- **Criticism about rubric quality evaluation being on a small subset**: The paper explicitly acknowledges the 10%/1000-example scope and frames the rubric results as preliminary evidence. This is a fair limitation, not a flaw.

- **Criticism about random sampling of 50% of pairs causing sampling bias**: The paper states this is due to computational limitations. There is no evidence this introduces systematic bias (pairs are sampled randomly), so this is speculative.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Separate the narrative into two distinct claims**: (a) the bootstrapping pipeline can generate training data that improves judge models over their base backbones, and (b) the resulting judges show competitive performance on independent, human-annotated benchmarks. Present the self-constructed benchmarks as distribution analysis, not primary evidence.

2. **Confront the calibration failure directly.** Investigate whether the overestimation bias originates from the generator producing implausibly good low-rated responses, the evaluator model having its own upward bias, or the training objective. A targeted analysis would strengthen the paper even if the issue is not fully resolved.

3. **Disclose G and E model identities in the main text.** This is a one-line addition that critically affects interpretation.

4. **Report α and T values** used in the bootstrapping pipeline.

5. **Add confidence intervals or bootstrap estimates** for the key comparisons in Tables 1 and 3.

6. **Evaluate rubric generation on the full dataset** rather than 10% to strengthen those claims.

## Score and Decision

### Calibration Process

**Round 1 — Bracketing:** Three queries anchored weak papers (high_score=3.5), middle papers (3.5–7.5), and strong papers (low_score=7.5). The weak anchors (b3mk8XrH9N, 3.20; 5blK5QHZpR, 3.00) were clearly weaker than VideoJudge — they propose benchmarks/synthetic data without the training pipeline or judge model contributions. The strong anchors (DM0Y0oL33T, 8.00; VKGTGGcwl6, 8.00) were far stronger, with cleaner methodology and fewer foundational weaknesses. The middle band contained the relevant comparison set. **Initial bracket: [4.0, 6.5].**

**Round 2 — Narrowing:** Queried inside [4.0, 6.0] and [5.5, 7.5]. Key anchors:
- **MF2** (4.80, Reject): A benchmark-only paper with human-annotation quality concerns and limited model diversity. VideoJudge contributes a method (bootstrapping pipeline) and trained models, making it slightly stronger, though MF2's benchmark quality is higher.
- **LLaVAction** (5.00, Accept Poster): A model+benchmark paper with some methodological concerns (hard negative validity, unnecessary design choices) but clear performance gains. Comparable to VideoJudge in overall quality — both have genuine contributions paired with significant weaknesses.
- **MMR-V** (5.50, Accept Poster): A benchmark paper with thorough human annotation and model evaluation. VideoJudge's method contribution is stronger but its evaluation rigor is weaker.
- **J1** (6.50, Accept Poster): A cleanly executed LLM-as-Judge training paper with comprehensive ablations and independent benchmarks. VideoJudge tackles a harder multimodal problem but has more significant methodological concerns.

**Final score:** 5.0. The paper sits between LLaVAction (5.00) and MMR-V (5.50) — it has a genuine method contribution (bootstrapping pipeline) and solid pairwise results, but the severe pointwise calibration failure and reliance on self-constructed benchmarks for headline claims prevent it from reaching the 5.5–6.0 range. The paper is better than pure benchmark papers (3–4) but not as clean as J1 (6.5).

### Anchor Table

| Anchor ID | Avg Score | Round | Comparison |
|-----------|-----------|-------|------------|
| b3mk8XrH9N | 3.20 | R1 (weak) | Weaker — proposes RL for video reasoning without judge training |
| 5blK5QHZpR | 3.00 | R1 (weak) | Weaker — synthetic supervision for VideoQA, no judge model |
| 8I8NNAcosC | 3.00 | R1 (weak) | Weaker — frame sampling method, not about evaluation |
| cC3TW1s309 | 4.80 | R1 (mid) | Slightly weaker — benchmark-only paper; VideoJudge has method contribution |
| pPKqLyWiNr | 5.00 | R1 (mid) | Comparable — both have method contributions and notable weaknesses |
| xk8EqWDPQw | 5.50 | R1 (mid) | Slightly stronger — cleaner benchmark construction, but benchmark-only |
| pD2xQxYMhE | 5.50 | R2 (narrow) | Comparable — both address video evaluation with automatic methods |
| QuW5RUDwMo | 5.00 | R2 (narrow) | Comparable — both have method+eval contributions with limitations |
| dnJEHl6DI1 | 6.50 | R2 (narrow) | Stronger — cleaner methodology, independent evaluation, comprehensive ablations |
| DM0Y0oL33T | 8.00 | R1 (strong) | Much stronger — verifier plugin with thorough evaluation |
| VKGTGGcwl6 | 8.00 | R1 (strong) | Much stronger — multi-turn conversation evaluation |

<score>5.0</score>
<decision>Accept</decision>