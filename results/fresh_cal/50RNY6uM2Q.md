Here is the final consolidated review.

---

## Summary

MG-LLaVA augments the LLaVA architecture with a Multi-Granularity Vision Flow that fuses three types of visual features: low-resolution ViT features, high-resolution ConvNeXt features (via a Conv-Gate fusion network), and object-level features extracted from bounding boxes produced by an open-vocabulary detector (RAM + OWL-ViT). The model is evaluated at scales from 3.8B to 34B parameters across 11 image and video benchmarks. The paper's technical contribution is the architectural design and integration strategy for combining features at these three granularities.

## Strengths

1. **Consistent multi-granularity gains across two LLM scales on the same training data.** Table 4 (ablation) shows that adding both object-level features and Conv-Gate fusion improves MMBench-Dev by +1.6% (Vicuna-7B) and +2.3% (Phi3-3.8B) over the baseline, using the same LLaVA-1.5 training data. This is the cleanest evidence for the method's contribution, and the gain is consistent across backbones.

2. **Mechanistic evidence that the two modules address complementary weaknesses on TextVQA.** Table 4 shows object-level features alone barely help on TextVQA (+0.2% on Vicuna-7B), but adding Conv-Gate fusion yields a large jump (+3.0% from baseline). This directly validates the paper's claim that the high-resolution branch compensates for the detector's inability to capture text, while the object-level branch handles other objects. The ablation narrative is well-supported by the numbers.

3. **Scalability demonstration up to 34B with strong absolute results.** MG-LLaVA with Yi1.5-34B achieves 80.1 on MMBench-Dev, 79.1 on MMBench-Test, and 73.7 on SEEDBench — exceeding GPT-4V on all three. While this comparison requires careful qualification (see Weaknesses), it demonstrates that the multi-granularity design scales effectively to larger models.

4. **Systematic ablation of design choices.** Table 3a compares Conv-Gate fusion against Resampler, Channel Concat, and Patch Info Mining, showing Conv-Gate is the best. Table 3c demonstrates that the open-vocabulary detector (RAM tags) outperforms a fixed COCO-80 class baseline. Table 3b compares concatenation vs. cross-attention for incorporating object features. These ablations provide empirical justification for the paper's design decisions.

5. **Computational cost transparency.** The paper reports exact TFLOPs and parameter counts in Table 4, showing the full model adds only 0.2B parameters and 0.45 TFLOPs over the baseline, allowing readers to quantitatively assess the efficiency claims.

## Weaknesses

### Fatal
None.

### Major

1. **Main results conflate method gains with data gains, and the ablation partially addresses this but leaves a gap.** The main results (Tables 1–2) train MG-LLaVA on an extended dataset (~1.3M instruction-tuning samples including ALLaVA, ShareGPT4V, DocVQA, DVQA, AI2D) while the reported baselines (LLaVA-1.5, Mini-Gemini, etc.) use the standard LLaVA-Instruct-665K dataset. The ablation in Table 4 does control for this by using only LLaVA-1.5's data, showing a method gain of +1.6% on MMBench-Dev. However, the paper never reports a version of LLaVA-1.5 trained on the extended dataset. This means the headline difference of ~6-7% over LLaVA-1.5 (e.g., 72.1 vs. 65.2 on MMBench-Dev) cannot be cleanly decomposed into "method" vs. "data" contributions. The ablation's baseline (68.2 on MMBench-Dev) also differs from the reported LLaVA-1.5 (65.2) without explanation, further muddying the comparison. A single controlled experiment training LLaVA-1.5 on the extended data would resolve this cleanly.

2. **The claim of surpassing GPT-4V is inadequately qualified.** The abstract and conclusion state that MG-LLaVA "outperforms... GPT-4V and GeminiPro-V" and "notably surpasses" them. This is only true on a subset of benchmarks (MMBench-Dev, MMBench-Test, SEEDBench, DocVQA) when using the 34B model. On other benchmarks where GPT-4V scores are available (MMStar, VQA^T, SQA^I), MG-LLaVA-34B underperforms GPT-4V. Moreover, GPT-4V is evaluated zero-shot while MG-LLaVA is explicitly instruction-tuned on benchmark-like data. The paper qualifies this in most locations ("on MMBench and SEEDBench") but the broader framing in the abstract and contribution list is misleading. This should be tightened.

### Minor

3. **No controlled comparison with Mini-Gemini under identical conditions.** Mini-Gemini uses a similar dual-encoder design (ViT + ConvNeXt) with high-resolution fusion and is the closest architectural competitor. The paper only cites Mini-Gemini's published scores. Given the architectural similarity and the data confound described above, it is impossible to determine what MG-LLaVA's object-level branch adds beyond Mini-Gemini's dual-encoder setup. A head-to-head comparison with Mini-Gemini retrained on the same data (with and without object-level features) would substantially strengthen the paper.

4. **No variance or significance reporting.** None of the tables report standard deviations or confidence intervals. This is especially problematic for the ablation results, where several gains are small (e.g., +0.4% on SEED, +0.2% on TextVQA from object-level features alone). Without multiple seeds or significance tests, these small differences may be within the noise of evaluation.

5. **Object-level feature gains are modest on most benchmarks.** In the controlled ablation (Table 4), object-level features alone contribute +1.0% on MMBench-Dev, +0.4% on SEED, and -0.2% on TextVQA (Vicuna-7B). The paper describes this as "significant," but the improvements are small and inconsistent across benchmarks. The narrative would benefit from more measured language and an error analysis showing when object-level features help versus hurt.

6. **No failure case or error analysis of the detector pipeline.** The method depends critically on an external open-vocabulary detector (RAM + OWL-ViT) for generating bounding boxes. The paper does not analyze what fraction of bounding boxes are correct, how often critical objects are missed, or how detector failures affect downstream VQA performance. This is a notable omission for a system whose core novelty relies on external object detection.

7. **Missing inference cost analysis for the multi-stage pipeline.** Training FLOPs are reported, but there is no analysis of inference-time latency, the number of additional tokens from the object-level branch (up to 100 per image), or the overhead of running the detector at inference time. For a multi-stage pipeline, this practical cost matters.

8. **Video results are thin evidence for generality.** The improvement on MSVD (+0.8%) and MSRVTT (+0.6%) over Video-LLaVA is minimal, and no statistical significance is reported. The paper presents video as a demonstration of generality, but the evidence is too weak to support this claim persuasively.

### Trivial

None.

## Nice-to-Haves

- An error analysis of the detector (what fraction of objects are correctly boxed, how often the detector misses text vs. objects) would deepen understanding of when the object-level branch is useful.
- Reporting inference latency (ms/image) across the full pipeline (detector + fusion + LLM) would help practitioners assess the practical cost.
- Training LLaVA-1.5 on the extended dataset and reporting the result would fully disentangle the data vs. method effect.
- The discrepancy between the ablation baseline (68.2 on MMBench-Dev) and the reported LLaVA-1.5 score (65.2) should be explained.

## Removed Points

The following criticisms from the harsh review were removed with justification:

- *"The abstract statement 'trained solely on publicly available multimodal data' is misleading because ALLaVA is GPT-4V-generated and the detector is pre-trained on proprietary data."* — ALLaVA is publicly distributed as a dataset; being GPT-4V-generated does not make it non-public. The detector pre-training is not part of MG-LLaVA's training. The statement is accurate.

- *"Conv-Gate fusion is nearly identical to LLaVA-HR; novelty rests entirely on object-level features."* — The paper openly cites LLaVA-HR as inspiration (line 201). The novelty claim is the multi-granularity *combination* (low-res + high-res + object-level), not just the fusion mechanism itself. This criticism conflates a component's origin with the overall contribution.

- *"The paper's baseline table stops at models from early 2024; more recent models like InternVL2 and LLaVA-NeXT are absent."* — Removed per instruction: missing related works cannot be cited without external confirmation.

- *"The bounding boxes per frame vs. shared across frames is not reported for video."* — This is a genuinely missing detail but is too narrow to retain as a standalone weakness. It is subsumed by the broader point about missing inference pipeline details.

- *"GPT-4V evaluation version and prompt not disclosed."* — This is standard practice in the field; GPT-4V scores are cited from the original paper. Not a meaningful omission.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface any observation that the paper itself does not already articulate.

## Suggestions

1. Retrain LLaVA-1.5 (or Mini-Gemini) on the same extended dataset used for MG-LLaVA's main results, and report the result. This single experiment would resolve the primary confounding concern and cleanly separate the method's contribution from the data's contribution.

2. Add standard deviations or confidence intervals (multiple seeds) to the ablation results, especially since several gains are in the <1% range.

3. Include an error analysis of the detector pipeline: show examples of correct and missed detections, and quantify how often the detector fails on text vs. objects. This would strengthen the claim that object-level features are meaningfully integrated.

4. Report inference latency or per-sample token counts for the full pipeline, not just training FLOPs.

5. Temper the GPT-4V comparison language to match the evidence: MG-LLaVA-34B outperforms GPT-4V on 4 of 7 benchmarks where GPT-4V scores are available. The abstract should say "outperforms GPT-4V on MMBench and SEEDBench" rather than the broader "on various multimodal benchmarks."

## Score and Decision

This paper makes a clean, well-motivated architectural contribution: combining low-resolution, high-resolution, and object-level features in a multi-granularity vision flow. The ablation studies properly control for data and demonstrate consistent 1.6–2.3% gains across two LLM scales. The strongest evidence supports the method's value. However, the main results are presented in a way that conflates data improvements with architectural improvements, the GPT-4V claims are modestly overstated, and the evaluation lacks both a controlled comparison with the closest competitor (Mini-Gemini) and basic variance reporting. These issues are addressable but need attention.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>