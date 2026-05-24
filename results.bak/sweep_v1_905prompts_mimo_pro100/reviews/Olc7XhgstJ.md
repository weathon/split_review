Now I have sufficient calibration data. Let me write the final review.

## Summary

The paper proposes Steady Thought (ST), a three-stage framework to mitigate "under-thinking" in Large Reasoning Models—where models find a promising reasoning trajectory early but abandon it via excessive thought switching. The framework consists of thought segmentation (via entropy-based detection), thought completion (suppressing switch triggers to generate committed completions), and Steady Thought Preference Optimization (STPO, a length-normalized thought-level adaptation of SimPO). Experiments across three model families (1.5B, 8B, 14B) and four benchmarks show simultaneous accuracy improvements (up to 5.3%) and token reductions (up to 39.3%), including strong OOD generalization from math training to code tasks.

## Strengths

- **Well-motivated empirical diagnosis of under-thinking**: Figures 1a and 1b provide concrete evidence that the first correct thought appears early in the reasoning chain but is subsequently abandoned, directly motivating the framework. This is a clean, visually compelling way to frame the problem.

- **Consistent simultaneous improvements on accuracy and length across diverse settings**: Table 1 shows ST improves accuracy while reducing tokens across three model families (1.5B, 8B, 14B) and four benchmarks (MATH500, AIME2024, GSM8K, LiveCode). The results are remarkably consistent—no single setting shows degradation on either axis.

- **OOD generalization validated on LiveCode (code reasoning)**: Training only on math data, ST improves Qwen3-8B on LiveCode by +5.3% accuracy with 19.0% token reduction, and DeepSeek-R1-Distill-Qwen-14B by +4.2% with 14.2% reduction. This demonstrates the method teaches general reasoning commitment patterns rather than memorizing domain-specific data.

- **Clean ablation isolating STPO's contribution**: Table 4 comparing SFT, DPO, and STPO within the same framework effectively demonstrates that STPO uniquely combines the benefits of both—SFT degrades accuracy (80.4% vs. 84.4% on MATH500), DPO fails to reduce tokens (4,273 vs. 2,809), while STPO achieves both.

- **Quantitative evidence of reduced invalid switches**: Table 2 shows the percentage of correct intermediate thoughts (PCT) drops from 54.90% to 40.40% on MATH500 and from 14.50% to 7.90% on AIME2024 for the 1.5B model, directly confirming that ST teaches the model to commit to promising thoughts.

## Weaknesses

### Fatal
None

### Major

- **Incremental methodology — three-stage pipeline assembles existing techniques**: Thought segmentation uses standard entropy-based detection; thought completion suppresses hardcoded trigger words ("wait," "alternatively") during decoding; STPO is essentially SimPO applied at the thought level. While the combination is effective, none of the individual components represent a significant methodological advance. The contribution is better characterized as a well-executed engineering contribution than a methodological innovation.

- **Training data limited to mathematical reasoning, with OOD testing only on code**: The model is trained exclusively on omni-math data (Section 4.1). While the LiveCode OOD results are encouraging, the paper does not test on other reasoning domains (commonsense, logical deduction, multi-hop QA) that would strengthen claims about general reasoning commitment. The generalizability claim rests on a single OOD benchmark.

### Minor

- **Entropy threshold tuned only for DeepSeek-R1-Distill-Qwen-1.5B**: Table 3 shows threshold analysis for only the 1.5B model (threshold 3.0 selected), but the same threshold is applied to Qwen3-8B and DeepSeek-R1-Distill-Qwen-14B. The paper acknowledges this in Section 3.1 and Appendix D but does not present the results in the main text for the larger models, leaving open whether the chosen threshold is suboptimal for them.

- **Hardcoded trigger words for thought completion**: Section 3.2 describes suppressing specific words ("wait," "alternatively") during thought completion. This is a language-specific heuristic that may not capture all switching signals, especially for non-English reasoning or models that express uncertainty differently (e.g., "hmm," "let me reconsider"). A learned suppression mechanism would be more robust.

- **No comparison to GRPO or RL-based approaches**: The baselines (NoThink, NOWAIT, SEAL) are all test-time interventions, and the ablation compares only SFT/DPO/STPO. RL-based methods like GRPO that could potentially achieve similar training-time optimization are not considered.

### Trivial
None

## Nice-to-Haves
- Analysis of how ST affects problem difficulty — does it help more on harder problems where under-thinking is more severe?
- Testing on additional reasoning domains beyond math/code to validate the general reasoning commitment claim.
- Discussion of how thought completion generation cost (Appendix E) scales with model size.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **Formatting/style nitpicks**: The paper has some repetitive figure captions and minor presentation inconsistencies (e.g., Table 1 arrows), but these are parser artifacts or minor style issues that don't affect the scientific contribution.
- **NOWAIT showing +84.6% token increase on Qwen3-8B**: This is a baseline failure, not a weakness of the proposed method. It actually strengthens the case for ST by showing existing methods have model-specific failure modes.

## Novel Insights
The paper provides a genuinely useful diagnostic lens for understanding under-thinking: the observation that the first correct thought appears early but is subsequently abandoned (Figures 1a/1b) is a concrete, quantifiable characterization of the problem. The PCT metric (percentage of correct intermediate thoughts that represent invalid switches) is a useful analytical tool that could be applied to other settings. The key conceptual insight—that the problem is not switching *per se* but *inability to commit to promising thoughts*—is a meaningful reframing that distinguishes this work from pure suppression approaches.

## Scoring Calibration Report

**Round 1 anchors (bracketing):**
- pXIbcRPxWR (2.50) — Supervised Chain of Thought, rejected. Significantly weaker than this paper.
- sdpVfWOUQA (3.00) — Planning with MCTS, rejected. Much weaker.
- jRZ1ZeenZ6 (5.00) — Rational Metareasoning, rejected. Incremental, missing baselines. This paper is clearly better.
- 6VhDQP7WGX (5.80) — Inference Optimal VLMs, accepted but with many concerns. This paper is cleaner.
- BPgK5XW1Nb (8.67) — Spread Preference Annotation. This paper is less novel than SPA.
- rfdblE10qm (8.00) — Rethinking Reward Modeling. This paper lacks the theoretical depth of this anchor.

**Round 2 anchors (narrowing to 6.0-7.0):**
- O0sQ9CPzai (6.33) — TPO. Similar topic (DPO for reasoning), mixed reviews (8,5,6). This paper has cleaner motivation and more consistent results → slightly above.
- w6nlcS8Kkn (6.67) — To CoT or not to CoT. Meta-analysis with different contribution type.
- SBoRhRCzM3 (6.67) — Thought Propagation. Analogical reasoning with moderate improvements. Comparable contribution level.
- n7n8McETXw (6.50) — Training Nonlinear Transformers for CoT. Theoretical contribution, different focus.

**Round 3 anchors (confirming 6.0-7.0):**
- zpENPcQSj1 (6.33) — Generalizing Reasoning Problems. Comparable empirical contribution level.

**Bracket**: Round 1 suggests 5.0–8.0. Round 2 narrows to 6.0–7.0. This paper sits above TPO (6.33) due to cleaner motivation and more consistent empirical results, and roughly on par with the 6.50–6.67 anchors. The incremental nature of the methodology (assembling existing techniques) and limited training domain keep it below 7.0.

**Final score: 6.5** — A well-executed empirical contribution with consistent results and good analysis, but whose methodology is incremental (SimPO at thought level + existing segmentation/completion techniques). The paper would be strengthened by broader training domain coverage, learned suppression mechanisms, and comparison to RL-based training alternatives.

## Score and Decision

**Evaluation axes:**
- **Originality**: Moderate. The problem framing (under-thinking as inability to commit) is insightful, but the methodological components are largely existing techniques assembled into a pipeline.
- **Importance of research question**: High. Under-thinking is a real and practically relevant problem for reasoning model deployment.
- **Claims well supported**: Yes. The experimental design (3 models × 4 benchmarks, OOD testing, clean ablations) provides strong empirical support.
- **Soundness of experiments**: Good. Consistent improvements with multiple runs on AIME/LiveCode. Baselines are appropriate if not exhaustive.
- **Clarity of writing**: Good. The paper is well-structured with clear motivation, methodology, and analysis sections.
- **Value to the research community**: Moderate-high. Practical contribution for reasoning model efficiency, with useful diagnostic tools (PCT metric).

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>