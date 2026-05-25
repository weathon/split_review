Now I have all the information needed to write the consolidated review.

## Summary

The paper introduces **VideoJudge**, a bootstrapping framework for training MLLM-based evaluators specialized for video understanding. It uses a generator–evaluator feedback loop to automatically create training data on a 1–5 rating scale without human annotation, then fine-tunes small Qwen2.5-VL models (3B, 7B) as judges. The paper releases trained models, bootstrapped datasets, and meta-evaluation benchmarks. Experiments show that VideoJudge-7B matches or surpasses larger baselines (Qwen2.5-VL-32B/72B) on several benchmarks, and the rubric-generating variant (VideoJudgeR-3B) produces rubrics preferred by both humans and LLM judges.

---

## Strengths

1. **Novel bootstrapping pipeline for video judge training.** The generator–evaluator feedback loop that iteratively generates, evaluates, and refines candidate responses across a 1–5 scale is a clean, well-motivated design for producing supervision without human annotation. The human validation experiment (§5.2) — 94.8% annotator agreement (κ=0.895) and >92% correctness against gold preference on 250 hard 2-vs-3 pairs — provides direct evidence that the bootstrapped data captures meaningful quality distinctions.

2. **Impressive scaling efficiency.** VideoJudge-3B achieves Spearman correlation 0.82 on VideoJudgeLLaVA, exceeding Qwen2.5-VL-72B (0.80), a model ~24× larger (Table 1). In pairwise evaluation, VideoJudge-7B reaches 95.6% accuracy (w/ FB) on the VJ benchmark vs. 94.0% for Qwen2.5-VL-72B (Table 3). This demonstrates that small models trained on bootstrapped data can close much of the gap with far larger general-purpose models.

3. **Instance-specific rubric generation is a genuine plus.** VideoJudgeR-3B produces rubrics that win against GPT-4o-mini (53.4%) and Qwen-72B (63.9%) in human preference, while maintaining competitive pointwise performance (MAE 0.59, correlations >73) — comparable to Qwen2.5-VL-32B/72B (Table 2, Figure 3). This adds interpretability without sacrificing accuracy, a practical advantage over black-box scoring.

4. **Comprehensive experimental scope.** The paper evaluates across 4 pointwise benchmarks (2 synthetic, 2 human-annotated), 3 pairwise benchmarks (VideoAutoArena with human preferences, VJ, VJ-H with human annotation), includes ablations on maxframes and temperature, and compares against a wide range of unimodal (Qwen3) and multimodal (Qwen2.5-VL, LLaVA-NeXT, OneVision, Video-R1) baselines. The released models, benchmarks, and datasets are a tangible contribution to reproducible research.

5. **Informative ablations.** The analysis of maxframes (training benefits up to 240 frames, evaluation saturates at ~120) and decoding temperature (VideoJudge is robust while base model degrades) provides actionable guidance for deployment.

---

## Weaknesses

### Major

- **Systematic overestimation bias and poor calibration in the mid-to-high range (§6.2).** The model overestimates by ≥2 points in 14.8% of cases vs. 1.5% underestimation. Only 36.9% of rating-3 responses are scored correctly (46.6% inflated to 5), and 81.3% of rating-4 responses are incorrectly rated as 5. For a model whose primary function is to assign accurate scores, this is a serious functional limitation: it compresses the top of the rating scale, cannot meaningfully distinguish 4 from 5, and will inflate scores for mediocre responses. The paper flags this as future work but does not attempt to diagnose or mitigate it within the current framework (e.g., by analyzing training data distribution, augmenting with harder high-rating negatives, or reweighting). This substantially reduces the practical utility of the judge for fine-grained evaluation.

### Minor

- **The two primary pointwise meta-evaluation benchmarks (VideoJudgeLLaVA, VideoJudgeVCG) are constructed using the same bootstrapping pipeline (threshold 0) that generates the training data.** While the video–instruction pairs are drawn from different source datasets (LLaVA-Video, VideoChatGPT vs. VideoInstruct-100K/VCG-Plus/VideoChat2-IT), the response ratings are assigned by the same type of evaluator model that labeled the training data. The strongest results (VideoJudge-3B S=0.82 vs. Qwen2.5-VL-72B S=0.80) come from these benchmarks. The independent human-annotated benchmarks tell a more nuanced story: on VATEx, VideoJudge-7B PSUP (0.66) trails Qwen2.5-VL-32B (0.73); on VideoAutoArena, VideoJudge-3B (71.76 w/ FB) trails Qwen2.5-VL-32B (80.78). The paper acknowledges the closed-loop concern in Limitations but the abstract and conclusion do not distinguish which results rely on synthetic vs. human-annotated ground truth. The framing should better separate what is demonstrated on each type of benchmark.

- **The generator (`G`) and evaluator (`E`) models used in the bootstrapping pipeline are not explicitly specified in the main text.** The paper states "strong vision-language models (§A.2)" for dense description generation and references the appendix for details, but the identity of `G` and `E` — which are the actual teacher models that produce the training signal — is omitted. Similarly, the acceptance threshold `α` is formally defined (§3.1) but its numerical value for training data generation is never given (only threshold 0 for benchmark construction is stated in §4.2). If these details reside in the appendix (which is stripped here), they should be moved to the main body for reproducibility.

- **"w/ FB" vs. "w/o FB" distinction is ambiguous for zero-shot baseline models in Table 3.** The table shows both "w/ FB" and "w/o FB" columns for baselines (Qwen2.5-VL-3B, 7B, 32B, 72B) that were not trained on any feedback data. It is unclear whether "feedback" refers to the training data used for VideoJudge models, different versions of the evaluation benchmarks, or something else. The caption and text say "with/without feedback" but do not clarify what this means for models that were not trained.

- **Human evaluation covers only the 2-vs-3 rating pairs.** While the 94.8% agreement validates that the bootstrapped pairwise data is reliable for the hardest ambiguous region, the broader rating scale (particularly correctness of ratings 4 and 5, and the overestimation pattern) is not validated against independent human judgments. The paper's claims about alignment with human judgment would be strengthened by human evaluation covering the full rating range.

- **No confidence intervals or variance estimates.** All results in Tables 1 and 3 are single point values. Given the modest size of some benchmarks (VATEx, VJ-H with ~200 samples), it is impossible to assess which differences are meaningful. This is especially relevant for close comparisons (e.g., S=0.82 vs 0.80 on VideoJudgeLLaVA).

- **Monotonicity validation uses BLEU and BERTScore against the gold reference (§5.1).** These reference-based metrics are weak proxies for actual rating quality in open-ended video understanding, where multiple semantically correct responses can differ in surface form. A complementary qualitative analysis showing that rating-1 responses are genuinely worse in content (not just lexically dissimilar) would strengthen the validation.

### Trivial

- Figure 4 would benefit from error bars or variance bands for the temperature sensitivity analysis.

---

## Nice-to-Haves

- **Ablation varying the strength of `G` and `E`** (e.g., using a weaker evaluator) to test how sensitive the final judge quality is to teacher capability, and whether the bootstrapping methodology truly enables small models to outperform the teacher.
- **Breakdown of training data distribution by rating level** to investigate whether the overestimation bias stems from imbalanced training data (e.g., more rating-5 examples than rating-3).
- **Comparison with a fine-tuned baseline trained on direct distillation** from a strong model (e.g., GPT-4o judgments on the same seed data) to isolate the value of the bootstrapping feedback loop vs. simpler distillation.
- **Qualitative examples of generated responses at each rating level** to validate that the progressive degradation is meaningful beyond surface-form similarity.

---

## Removed Points

These points from the input reviews are excluded with justification:

- **"Closed-loop concern: if G and E are the same model..."** — Speculative inference not directly supported by the paper. The paper does not state which models G and E are, so asserting a closed-loop scenario is conjectural. The actual closed-loop concern (benchmarks sharing the pipeline) is retained in the Minor weaknesses above.
- **"Novelty boundary needs sharper articulation relative to existing work (Kim et al, Lee et al)"** — No specific missing related work is identified; this is a generic concern that could apply to any paper. The paper cites Kim et al. 2024a,b and Lee et al. 2024a in §2 and its approach differs (bootstrapping feedback loop, video domain).
- **"LLM judges vs MLLM judges finding is not surprising/nor novel"** — This is an opinion about the significance of a finding, not a specific problem with the paper. The finding itself (video input is essential) is supported by the experiments.
- **"Does not analyze how description quality affects bootstrapping outcome"** — A nice-to-have analysis, not a core flaw. The paper uses "strong vision-language models" for descriptions and focuses on the bootstrap pipeline.
- **"Ablation on teacher model"** — Nice-to-have additional experiment.
- **"Comparison with strong fine-tuned judge baselines from related domains"** — Nice-to-have; the paper compares against available baselines in the video understanding domain.
- **"Qualitative analysis of generated responses at each rating"** — Nice-to-have validation beyond BLEU/BERTScore.

---

## Novel Insights

None beyond the paper's own contributions.

---

## Suggestions

1. **Frame the results by benchmark provenance.** Separate the claims into two categories: (a) results on synthetic benchmarks that share the training pipeline (strong evidence of distillation efficiency), and (b) results on independent human-annotated benchmarks (evidence of generalization). The abstract and conclusion should reflect this distinction.

2. **Diagnose and mitigate the overestimation bias.** At minimum, analyze the training data rating distribution and check whether the evaluator `E` itself exhibits this bias. Even a simple experiment with balanced training data or harder negatives at ratings 4 and 5 would demonstrate that the issue is tractable.

3. **Specify `G`, `E`, and the training threshold `α` in the main paper body.** These are not optional details for a pipeline whose central claim depends on the teacher-student performance gap.

4. **Clarify the "w/ FB"/"w/o FB" columns in Table 3** — explicitly state what the distinction means for zero-shot baselines that were not trained on feedback data.

5. **Add bootstrap confidence intervals** for the main benchmark results (or at minimum, note the sample sizes and report standard errors where feasible).

6. **Expand human evaluation** to include a sample of full-range rating pairs (not only 2-vs-3) to validate the model's discrimination across the entire 1–5 scale.

---

## Score and Decision

**Round-1 bracket:** 4.5 – 6.0  
**Round-2 narrowed range:** 5.0 – 6.0 (informed by Self-Taught Evaluators at 5.40, JudgeLM at 5.25, and Is Your VLM a Reliable Judge at 6.50)

**Anchor comparison:**
- `ujNe7sybJu` (2.50, round1-weak) — Much weaker paper with limited methodology; VideoJudge is substantially stronger.
- `YGWxpOI6Y0` (3.40, round1-weak) — Video summarization paper; not directly comparable in quality.
- `m8yby1JfbU` (6.50, round1-mid) — Most directly comparable topic (VLM-as-judge). Simpler, cleaner analysis, fewer contributions but also fewer flaws. VideoJudge is more ambitious but has the overestimation bias and circular benchmark issues that this anchor avoids.
- `ToWKyjwDqO` (5.00, round1-weakness) — LLM-as-judge training with DPO. Similar synthetic-data concerns. VideoJudge has stronger evaluation and releases artifacts.
- `I7uCwGxVnl` (5.40, round2) — Self-Taught Evaluators. Very similar concept (synthetic training of evaluators). Reviews criticized limited model testing and synthetic data quality. VideoJudge is stronger (multiple sizes, more baselines, human validation) but has overestimation bias that Self-Taught doesn't have (binary preference).
- `87YOFayjcG` (5.25, round2) — JudgeLM (text-only). VideoJudge addresses a harder domain with more novelty.
- `NO6Tv6QcDs` (6.50, round1-weakness) — Theoretical analysis of LLM-as-judge limitations. Stronger theoretical contribution but different type of paper.

**What the low-band anchors and weakness-anchored hits failed at:** The low-band (<3.5) papers had weak methodology, limited experiments, or unclear contributions — VideoJudge does not share these. The weakness-anchored papers (Self-Taught 5.40, JudgeLM 5.25) were criticized for synthetic data quality concerns, limited generalization evidence, and missing comparisons — VideoJudge partially shares the synthetic data circularity concern and additionally has the overestimation bias, which is arguably a more significant functional flaw than anything in those anchors.

The paper has genuine contributions (novel pipeline, strong human validation, released artifacts, rubric generation) but the overestimation bias is a significant functional limitation for a judge model, and the strongest empirical claims are anchored on benchmarks that share the training pipeline. On balance, the paper is stronger than the rejected 5.25–5.40 anchors but has clearer flaws than the accepted 6.50 anchor. Score 5.5 reflects a paper with real merit that needs substantial revision to match its claims with its evidence.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>