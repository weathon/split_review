## Summary

VideoJudge is a bootstrapping framework for training small (3B/7B) multimodal LLM judge models to evaluate video understanding outputs. The pipeline iteratively generates candidate responses at different quality tiers, validates them with a large evaluator model, and discards misaligned examples. The resulting data trains both pointwise and pairwise judge models, with an additional variant (VideoJudgeR) that generates instance-specific rubrics at inference time. The paper also releases meta-evaluation benchmarks, bootstrapped datasets, and trained models for reproducible video evaluation research.

---

## Strengths

- **Validated data quality through both automatic and human checks.** Figure 2 confirms monotonic BERTScore/BLEU degradation (91.1→86.9 / 11.0→3.0) as intended rating decreases, and Section 5.2 reports 94.8% inter-annotator agreement (κ=89.5) with >92% alignment to gold preference on the hardest 2-vs-3 rating pairs, confirming the bootstrapped labels encode meaningful quality differences.

- **Strong temperature robustness vs. the base model.** Figure 4 shows a concrete, measurable advantage: VideoJudge-3B Spearman correlation *increases* from 0.66 to 0.73 as temperature rises from 0.0 to 1.0, while the base Qwen2.5-VL-3B degrades from 0.56 to 0.42. This is a practically important property for deployment.

- **VideoJudge-7B achieves the best Δ(C-D) on LongVideoBench among all models (1.16 vs. 1.08 for Qwen2.5-VL-32B and 1.06 for 72B; Table 1).** This is a fully independent benchmark based on long-form multiple-choice evaluation with no pipeline overlap, providing credible evidence of genuine temporal reasoning improvement.

- **Rubric-conditioned VideoJudgeR-3B substantially reduces MAE relative to its backbone** (0.59 vs. 1.15 for the base 3B, Table 2), reaching performance comparable to 32B/72B base models, with human win rates of 63.9% vs. Qwen-72B rubrics and 53.4% vs. GPT-4o-mini rubrics (Figure 3).

---

## Weaknesses

### Fatal
None.

### Major

- **Two of the four headline meta-evaluation benchmarks are self-constructed via the same bootstrapping pipeline used to generate training data.** Section 4.2 explicitly states that VideoJudgeLLaVA-MetaEval and VideoJudgeVCG-MetaEval were built by "generating additional responses via our bootstrapping pipeline (Algorithm 1) with threshold 0." Ground-truth ratings on these benchmarks are assigned by the same evaluator that generated the training signal. A model trained to agree with that evaluator's implicit rubric will naturally score well on a benchmark whose labels were produced by the same rubric — this is not a full generalization test. The paper acknowledges this as a "partial closed-loop effect" in Section 7 but provides no quantitative estimate of the inflation. The abstract's claim of "three out of four benchmarks" thus counts two benchmarks whose independence is in question.

- **On the two most trustworthy independent benchmarks, VideoJudge does not clearly surpass much larger models.** On VATEX PSUP — the metric most directly aligned with preference ranking — VideoJudge-3B (0.61) and VideoJudge-7B (0.66) both fall below Qwen2.5-VL-32B (0.73) and Qwen2.5-VL-72B (0.71) (Table 1). On VideoAutoArena, VideoJudge-7B (85.49 w/ feedback) trails Qwen2.5-VL-72B (89.80) and also Qwen2.5-VL-32B without feedback (90.59). The framing in the abstract and conclusion ("match or surpass much larger models") is thus supported mainly by self-constructed benchmarks and LongVideoBench; the independent pointwise ranking evidence is more modest.

- **The rubric contribution lacks the critical ablation needed to isolate its effect.** Table 2 compares VideoJudgeR-3B against zero-shot baselines only. The 10% data training regimen is unique to the rubric experiments, so the gain from MAE 1.15 → 0.59 could reflect any fine-tuning on video evaluation data, not rubric supervision specifically. A comparison against a VideoJudge-3B variant trained on the same 10% subset *without* rubrics is not included. Without this ablation, the rubric generation contribution cannot be cleanly attributed to rubric supervision.

### Minor

- **VideoJudge-3B outperforms VideoJudge-7B on Spearman correlation in VideoJudgeLLaVA (0.82 vs. 0.78; Table 1), an anomaly that is not discussed.** A 3B model with the same training procedure exceeding its 7B counterpart on this metric is unusual and could indicate benchmark-specific overfitting, a training artifact, or sensitivity to benchmark size. The paper would benefit from at least acknowledging this.

- **The overestimation bias documented in Section 6.2 is striking and its causes are not explored.** The paper reports that 81.3% of rating-4 responses are incorrectly scored as 5, and 46.6% of rating-3 responses are inflated to 5. The section correctly identifies the symptom and suggests harder negatives, but the connection to training data distribution — specifically, how many examples exist per rating level and whether the bootstrapping pipeline over-represents higher quality responses — is not analyzed. This bias plausibly explains why VATEX PSUP (pair-ranking) lags behind larger models even when RMSE and ECE improve.

- **The LLM-as-Judge rubric win rates (92.7% vs. GPT-4o-mini, 71.3% vs. Qwen-72B) are presented alongside but implicitly conflated with human win rates (53.4% vs. GPT-4o-mini, 63.9% vs. Qwen-72B).** A fine-tuned model optimized to produce structured rubrics will systematically favor rubric-like text in an LLM-judge comparison — the human win rates are the more meaningful signal, and they are considerably more modest. The framing could make the gap between LLM and human rubric evaluation clearer.

### Trivial
- None beyond parser artifacts (removed from consideration per review rules).

---

## Nice-to-Haves

- A direct quantification of the closed-loop inflation: train VideoJudge on the existing bootstrapped data but evaluate on a benchmark whose gold labels are assigned by a *different* evaluator or collected from humans on the same video pool. If the advantage persists, the core claim is robust; if it collapses, that informs the scope of the contribution.
- A distributional breakdown of training examples by rating level (how many 1s, 2s, 3s, 4s, 5s) would help explain the overestimation bias and guide targeted improvements.
- Extending LongVideoBench evaluation to also report PSUP (not only Δ(C-D)) would provide a more complete picture of whether the Δ(C-D) advantage persists across both preference metrics.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Train-test distribution mismatch (dense descriptions vs. raw frames):** The harsh critic flags that the generator and evaluator use pre-computed video descriptions during bootstrapping, while fine-tuned models process raw video. However, the experimental setup (Section 4.2) states all models are trained with fps=1 and frame caps, indicating fine-tuning is on actual video frames. Descriptions are used only for the generator/evaluator during data creation, not as the fine-tuning input modality. This concern does not translate to a real mismatch in the fine-tuning pipeline.

- **LLM vs. MLLM comparison is "confounded" by different input modalities:** The paper explicitly acknowledges in Section 4.1 that unimodal models "are provided with the description, instruction, and candidate response" and discusses the inference cost in Section 6.1. The comparison is framed as an input-modality difference from the start, not a capability claim.

- **Criticism of BERTScore/BLEU as insufficient data-quality evidence:** The harsh critic argues that monotonic degradation in these metrics only shows dissimilarity, not evaluation soundness. This is accurate but the paper explicitly characterizes Figure 2 as a "sanity check" / proxy, and pairs it with VQAScore (§A.5) and human evaluation (Section 5.2). Calling the BERTScore/BLEU use misleading ignores the multi-method validation.

- **"Abstract claim about 3 out of 4 benchmarks elides self-construction":** This is partially valid (retained as a Major weakness), but the strength finder's claim that this is a "concrete contribution to the video-understanding evaluation ecosystem" is kept as a supporting strength since the benchmarks are real resources even if partially derived.

- **Strengths about "addressing an important problem" / "promising direction":** Removed as generic — not tied to specific results in the paper.

---

## Novel Insights

The temperature-robustness finding is genuinely interesting: fine-tuning specifically for video evaluation inverts the degradation pattern seen in base models, suggesting that task specialization stabilizes the evaluation prior even under stochastic decoding. The LongVideoBench Δ(C-D) advantage (1.16 vs. ~1.06–1.08 for 32B/72B) suggests that bootstrapped supervision on diverse video instruction pairs may specifically strengthen temporal reasoning for evaluation, a capability dimension where larger general-purpose models scale less efficiently. The overestimation bias (81.3% of rating-4 responses rated as 5) implies that the bootstrapped rating scale may be systematically compressed at the top end — a structural issue attributable to the generator-evaluator equilibrium that future bootstrapping work should address.

---

## Suggestions

1. Restructure the abstract to make clear that "three out of four benchmarks" includes two self-constructed benchmarks; move VATEX and VideoAutoArena results to the forefront of the empirical narrative.
2. Add the rubric ablation: train a non-rubric VideoJudge-3B on the same 10% data subset and report Table 2-style metrics, enabling attribution of gains to rubric supervision specifically.
3. Investigate training data distribution by rating level and correlate it with the overestimation bias; this is the most actionable path to fixing the calibration gap.
4. Clarify the discrepancy between LLM-as-Judge rubric win rates and human win rates for VideoJudgeR-3B — the former likely reflects format preference artifacts.
5. Explain the 3B > 7B Spearman anomaly on VideoJudgeLLaVA (0.82 vs. 0.78) in the analysis section.

---

## Score and Decision

**Originality:** The bootstrapping generator-evaluator approach for video evaluation is a concrete and novel operationalization. The rubric-generation extension adds further novelty. Score: 4/5.

**Importance:** Scalable automatic evaluation of video models is a real and growing need; this addresses it with an open, reproducible framework. Score: 4/5.

**Claims supported:** The main claims about "matching 32B/72B" are well-supported on self-constructed benchmarks and LongVideoBench but overstated relative to the independent VATEX/VideoAutoArena evidence. Score: 3/5.

**Soundness of experiments:** Methodology is sound, but the critical rubric ablation is missing and the self-construction issue is unquantified. Score: 3/5.

**Clarity:** The paper is clearly written and well-organized; the self-constructed benchmark issue requires more prominent disclosure. Score: 4/5.

**Community value:** The released models, benchmarks, and datasets are a concrete contribution; the bootstrapping recipe is generalizable. Score: 4/5.

The paper makes a genuine methodological contribution but its headline claim rests more on self-constructed benchmarks than on independent evidence. The core approach is sound, the framework is useful, and the released resources have real community value — but the framing outpaces what the independent experiments conclusively demonstrate.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>