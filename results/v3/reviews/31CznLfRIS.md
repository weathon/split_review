Now I have thoroughly analyzed the paper and verified the reviewer claims against the actual text. Let me produce the final consolidated review.

## Summary

VideoJudge introduces a bootstrapping framework for training MLLM-based evaluators specialized for video understanding. The core idea is a generator–evaluator pipeline that iteratively produces candidate responses across a 1–5 rating scale, validates them with an evaluator, and refines mismatched cases, yielding over 100K training examples from 25K seed video–instruction pairs without additional human annotation. The trained 3B and 7B judge models (fine-tuned from Qwen2.5-VL) are evaluated across pointwise and pairwise meta-evaluation benchmarks, including both self-constructed and human-annotated datasets. The paper also explores instance-specific rubric generation and provides a suite of benchmarks, datasets, and trained models.

## Strengths

- **Bootstrapping pipeline generates training data at scale without extra human annotation.** The automatic evaluation (Figure 2) shows monotonic degradation in BERTScore (91.1 → 86.9) and BLEU (11.0 → 3.0) as rating gap increases, and human evaluation on the hardest 2-vs-3 pairs achieves 94.8% inter-annotator agreement with >92% correctness relative to the gold preference (§5.2). This validates that the synthetic ratings are sufficiently reliable for supervision.

- **Strong pairwise results demonstrate practical utility for relative quality assessment.** VideoJudge-7B achieves 98.6% accuracy on VideoJudge-Pairwise (VJ) and 93.67% on VideoJudge-Pairwise-H (VJ-H, human-annotated), surpassing all baselines including Qwen2.5-VL-72B (93.25% on VJ-H) (Table 3). These results hold on human-annotated data, mitigating closed-loop concerns for the pairwise setting.

- **Instance-specific rubric generation is a novel capability for video judges.** VideoJudgeR-3B produces rubrics preferred by human annotators over those from GPT-4o-mini (53.4% win rate) and Qwen-72B (63.9%), while maintaining scoring performance (MAE 0.59, correlations ~74) comparable to 32B/72B models (Table 2, Figure 3). This provides interpretability alongside evaluation, a useful feature absent in prior video judge work.

- **Comprehensive evaluation across diverse benchmarks.** The paper evaluates on four pointwise benchmarks (including the independent VATEx and LongVideoBench) and three pairwise benchmarks (including human-annotated VideoAutoArena and VJ-H), covering both self-constructed and external datasets. Ablation studies on frame count and decoding temperature provide practical deployment insights.

- **Demonstrates that video input is essential for video judging.** Text-only LLM judges (Qwen3 variants, including with thinking mode) consistently underperform MLLM judges that process video directly (Table 1), validating the multimodal design choice with a controlled comparison.

## Weaknesses

### Major

- **Severe calibration and overestimation bias undermines pointwise rating reliability.** The paper's own error analysis (§6.2) reveals that VideoJudge overestimates scores by ≥2 points in 14.8% of cases (vs. 1.5% underestimation). Only 36.9% of rating-3 responses are correctly identified—46.6% are inflated to a perfect 5—and 81.3% of rating-4 responses are also incorrectly rated as 5. This means the model cannot meaningfully distinguish between mediocre (3), good (4), and excellent (5) responses in pointwise evaluation, which is arguably the most important regime for judge models. The paper acknowledges this as a limitation but does not address it; it is not a minor calibration issue but a structural limitation that severely limits the practical value of the pointwise judge.

- **Missing ablations that would isolate the bootstrapping mechanism's specific contribution.** The central methodological claim is that the generator–evaluator iterative pipeline produces superior training data. However, there is no ablation comparing against: (a) training on unfiltered generator outputs (skipping evaluator filtering), (b) training on simpler quality augmentation without the iterative refinement loop, or (c) training on the seed data alone. Without these, the paper cannot attribute performance gains to the bootstrapping process specifically rather than to simply having more diverse training data.

- **Rubric generation analysis does not isolate the contribution of rubrics.** Table 2 compares VideoJudgeR-3B (fine-tuned to generate rubrics) against *zero-shot* base Qwen2.5-VL models of various sizes. This comparison conflates fine-tuning with rubric generation. The meaningful comparison would be VideoJudgeR-3B vs. VideoJudge-3B (trained on the same data without rubric generation) to isolate whether generating rubrics adds value beyond standard pointwise training. As presented, the results only show that fine-tuning helps over zero-shot, which is expected.

### Minor

- **Closed-loop evaluation on self-constructed benchmarks.** Two of the four main pointwise benchmarks (VideoJudgeLLaVA and VideoJudgeVCG) are constructed using the same bootstrapping pipeline that produced the training data (§4.2, threshold α=0). The paper acknowledges this (§7) but does not quantify how much of the reported advantage over baselines is attributable to fitting the pipeline's internal preferences vs. learning generalizable evaluation capabilities. The performance gap is stark: on independent benchmarks (VATEx, LongVideoBench), VideoJudge models are competitive but not consistently superior (e.g., VideoJudge-3B PSUP 0.61 vs. Qwen2.5-VL-32B's 0.73 on VATEx).

- **Performance inconsistency across pointwise benchmarks.** VideoJudge-3B achieves Spearman 0.82 on VideoJudgeLLaVA (best among all models) but drops to 0.59 on VideoJudgeVCG (worse than LLaVA-OneVision's 0.77 and even the untrained Qwen2.5-VL-7B's 0.65) (Table 1). This across-benchmark variance is not discussed, making it difficult to understand when the model works well and when it does not.

- **Inconsistent use of metrics criticized in the paper.** Section 1 criticizes BERTScore and BLEU as "struggling to capture semantic fidelity" and being "misleading" for open-ended tasks, yet §5.1 relies primarily on these exact metrics to validate data quality (Figure 2). While VQAScore is also computed, the main presentation uses BERTScore/BLEU, creating an inconsistency.

- **No statistical significance reported.** Given the mixed pattern across benchmarks and metrics, it is impossible to know whether observed differences (e.g., Spearman 0.82 vs. 0.80) are meaningful. This is especially important for the pairwise results where differences are small (e.g., VideoJudge-7B 93.67 vs. Qwen2.5-VL-72B 93.25 on VJ-H, both w/ FB).

- **Limited human evaluation scope.** The human evaluation (§5.2) covers only 250 pairs, only the 2-vs-3 rating boundary, and only pairwise preference. The absolute rating assignments (which the pointwise benchmark relies on) are never directly validated against human judgment.

### Trivial

- The pairwise "w/ FB vs. w/o FB" results show counterintuitive patterns: VideoJudge-3B achieves 89.45 (w/ FB) vs. 90.72 (w/o FB) on VJ-H—the feedback mechanism sometimes hurts performance (Table 3). The paper notes this is "mixed" but does not analyze why.

## Nice-to-Haves

- Computational cost of the bootstrapping pipeline (number of generator/evaluator calls, total API cost) is not reported. The paper claims "cost efficient" but provides no evidence.
- No comparison against other fine-tuned judge models (e.g., adapting JudgeLM or similar for video via descriptions), only zero-shot baselines.
- Analysis of the bootstrapping pipeline's internal dynamics (e.g., acceptance rates per iteration, distribution of ratings, number of refinement rounds) would help establish whether the pipeline is functioning as intended.

## Removed Points

The following points from the harsh critic are removed after verification:

- **"The paper does not thoroughly discuss prior bootstrapping-for-evaluation work (e.g., Self-Rewarding, SPIN)"** — Removed per the rule about not mentioning missing related works. The paper does cite relevant self-refinement and self-verification literature (§3, §2).
- **"Methodology details relegated to appendix which is stripped by the parser"** — Removed per the rule about missing appendix content being a parser issue, not a paper problem.
- **"The paper claims 'eliminates the need for costly human annotation' but seed datasets required human annotation"** — The paper's claim is about not needing *additional* human annotation beyond existing datasets, which is clearly stated and reasonable.
- **"VideoJudge-3B performance on VideoJudgeVCG (Spearman 0.59) is among the worst"** — While factually correct, this is retained in Minor weaknesses above as "performance inconsistency" rather than a standalone fatal issue.
- **Criticisms about "generator and evaluator models not specified in main text"** — Moved to Nice-to-Have/Trivial since this level of implementation detail is commonly in appendices and the paper states Qwen2.5-VL as the backbone.

## Novel Insights

The reviews collectively surface one genuinely novel insight: the bootstrapping pipeline's internal quality control (generator produces responses for intended ratings → evaluator validates → refinement loop) provides a method for creating fine-grained 5-point rating training data without human annotation, which prior LLM-as-Judge work has not demonstrated for the video domain. However, the severity of the calibration problem revealed by the paper's own analysis (§6.2) suggests that the pipeline may systematically fail to generate hard negatives at the upper end of the rating scale (ratings 3–5), explaining why the trained judge inherits this blind spot. This tension between the pipeline's efficiency and its inability to teach fine-grained upper-range discrimination is the paper's most interesting unresolved finding.

## Suggestions

1. **Add ablations that isolate the bootstrapping mechanism:** Train judges on (a) unfiltered generator outputs, (b) randomly paired responses with assigned ratings (no refinement), and (c) seed data only, all with the same training budget. This would directly demonstrate whether the iterative refinement pipeline is responsible for the observed gains.

2. **Conduct a controlled comparison between VideoJudge-3B (standard) and VideoJudgeR-3B (rubric) on the same data and training budget** to isolate whether rubric generation adds value beyond standard pointwise training. Without this, the rubric contribution is unsubstantiated.

3. **Quantify the closed-loop effect** by measuring performance drop when moving from self-constructed benchmarks to human-annotated benchmarks, and present this analysis prominently rather than burying it in limitations.

4. **Diagnose the calibration problem** in the upper rating range (3–5). Analyze whether the generator produces sufficiently hard negatives at rating 4 that are distinguishable from rating 5, and consider targeted data augmentation or rebalancing for the upper range.

5. **Report statistical significance** (e.g., bootstrap confidence intervals) for the main comparative results, especially where differences are small.

6. **Run the rubric judge without rubric tokens** (via prompting "do not generate a rubric") to isolate rubric contribution.

## Score and Decision

### Calibration Anchor Analysis

**Round 1 bracket:** I searched in three topic bands (<3.5, 3.5–7.5, >7.5) plus weakness-anchored queries. The most relevant anchors are:

| Anchor | Avg Score | Round/Query | Comparison |
|--------|-----------|-------------|------------|
| JudgeLM (87YOFayjcG) | 5.25 | R1-weakness (MLLM as judge) | Similar closed-loop concern (training on pipeline judgments, evaluating on pipeline-derived benchmarks). VideoJudge has broader multi-benchmark evaluation but also the additional calibration problem. |
| Self-Taught Evaluators (I7uCwGxVnl) | 5.40 | R1-weakness (bootstrapping data) | Similar approach (synthetic data for judges without human annotation). VideoJudge addresses video domain (more challenging) but Self-Taught Evaluators has cleaner ablations. |
| AutoBench-V (kUsXwE98Cs) | 3.75 | R1-weakness (closed-loop) | Automated LVLM benchmarking with closed-loop concerns. VideoJudge is substantially stronger (more benchmarks, human evaluation, trained models released). |
| Is Your VLM a Reliable Judge? (m8yby1JfbU) | 6.50 | R1-topic-mid | About studying VLM judge reliability, not training judges. Higher quality paper but different contribution type. |
| Limits to Scalable Eval (NO6Tv6QcDs) | 6.50 | R1-weakness | Theoretical analysis of LLM-as-judge limitations. Different genre but relevant framing. |
| JudgeLM (xsELpEPn4A) | 7.50 | R1-weakness | Same JudgeLM at NeurIPS. Accepted version with good ablations and comprehensive analysis. |
| VideoEval (wMRFTQwp1d) | 4.00 | R2 (3.5–5.0) | Benchmark paper for video foundation models. Less directly comparable. |
| Video Instruction Tuning (8Livf4oZxz) | 4.50 | R2 (3.5–5.0) | Synthetic data for video LMMs. Lower quality contribution. |

**Round-1 bracket:** I identified 3.5–5.5 as the plausible score range based on comparison with JudgeLM (5.25, Reject) and Self-Taught Evaluators (5.40, Reject) as the closest methodological peers, and AutoBench-V (3.75) as the lower bound.

**Round 2 narrowing:** I searched within (3.5–5.0) and (4.5–6.0) to refine. The additional anchors confirmed that papers with comparable quality in this topical area (video understanding + evaluation) cluster around 4.0–5.5, with most being rejected.

**What the low-band anchors and weakness-anchored hits failed at:** JudgeLM (5.25) failed partly because its evaluation was tied to the same GPT-4 judgments used for training (closed-loop). AutoBench-V (3.75) failed due to data quality issues and the judge being the same model generating the data. VideoJudge shares the closed-loop concern (strongest results on self-constructed benchmarks) but mitigates it through evaluation on external human-annotated benchmarks (VATEx, LongVideoBench, VideoAutoArena, VJ-H). However, VideoJudge has an *additional* failure mode that these comparators do not: the severe calibration problem confirms that even on its own terms, the pointwise judge cannot reliably distinguish rating 3 from 5. This is a more concrete weakness than the closed-loop concern alone, and it is self-reported in the paper.

**Final position:** The paper is stronger than AutoBench-V (3.75) but weaker than JudgeLM (5.25, Reject) and Self-Taught Evaluators (5.40, Reject) because: (1) it shares their closed-loop concern without quantifying it, (2) it adds a severe calibration problem that those papers do not have, and (3) its core methodological claim (the bootstrapping mechanism) lacks ablation support. The pairwise results are genuinely strong and the problem is important, which prevents the score from falling below 4.0. I place this paper at **4.5**.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>