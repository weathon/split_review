## Summary

VideoJudge introduces a bootstrapping framework that automatically generates training data for MLLM-based evaluators of video understanding without costly human annotation. A generator–evaluator pipeline iteratively produces candidate responses across a 1–5 rating scale, validates them, and refines mismatches. Fine-tuned 3B and 7B Qwen2.5-VL models trained on this data are evaluated in both pointwise and pairwise settings, and are shown to match or approach the performance of models 10× larger (32B/72B). The paper also trains models to generate instance-specific rubrics at test time, yielding interpretable evaluations. Models, bootstrapped datasets, and meta-evaluation benchmarks are released.

## Strengths

- **Bootstrapped data validated by human evaluation on the hardest rating gap.** On the 2‑vs‑3 rating pair (the most ambiguous region), two annotators achieved 94.8% agreement (Cohen's κ = 0.895) and >92% correctness relative to the gold preference (§5.2, Table 7). This provides concrete evidence that the automated pipeline produces supervision aligned with human judgment for the most difficult distinctions.

- **Small models match or surpass much larger baselines in pairwise evaluation on human-annotated benchmarks.** VideoJudge‑7B achieves 93.67% on VideoJudge‑Human (VJ‑H), competitive with Qwen2.5‑VL‑72B (94.51%), and 98.6% on the VJ benchmark (Table 3). This directly supports the central claim that fine-tuned small models can approach models ~10× larger.

- **Instance‑specific rubric generation closes the gap to 72B performance with a 3B model.** VideoJudgeR‑3B, trained on only 10% of pointwise data, achieves MAE 0.59 and correlations ~74, close to Qwen2.5‑VL‑72B (MAE 0.54, correlations ~78) when both produce rubrics (Table 2). Human evaluators prefer VideoJudgeR‑3B rubrics over GPT‑4o‑mini (53.4%) and Qwen‑72B (63.9%) (Figure 3). This demonstrates that rubric‑driven supervision substantially closes the performance gap without scaling model size.

- **Robustness to decoding temperature.** The trained VideoJudge model maintains Spearman correlation ~0.73 at temperature 1.0, while the base Qwen2.5‑VL‑3B drops from 0.56 to 0.42 (Figure 4). This is a practically important property for non‑deterministic inference settings.

- **Effective long‑form video evaluation.** On LongVideoBench, VideoJudge‑7B achieves the highest Δ(C‑D) score of 1.16, substantially above Qwen2.5‑VL‑72B (1.06) and all other baselines (Table 1), demonstrating generalization to long-context temporal reasoning.

- **Comprehensive resource release.** The paper releases trained judge models, bootstrapped datasets (over 100K examples), and meta-evaluation benchmarks, providing reusable infrastructure for the community.

## Weaknesses

### Major

- **Partial closed‑loop evaluation on pipeline‑generated benchmarks.** The strongest headline results (e.g., VideoJudge-3B achieving Spearman 0.82 on VideoJudgeLLaVA) come from benchmarks constructed via the same generator–evaluator pipeline used to produce training data. Although the seed instruction–video pairs are drawn from held-out datasets (LLaVA-Video, VideoChatGPT), the response generation and rating process is identical to training. Performance on these benchmarks therefore conflates generalization to human judgment with reconstruction of the pipeline's internal preferences. The paper does evaluate on independent human-annotated benchmarks (VATEx, LongVideoBench, VideoAutoArena, VJ‑H) — on VATEx, VideoJudge-7B's Spearman (0.66) is below Qwen2.5‑VL‑32B (0.73) — and acknowledges this limitation in §7, but the abstract and conclusions do not caveat the pipeline-benchmark results. This risks overinterpretation.

- **Human validation of training data covers only one rating gap (2 vs. 3).** The paper's human evaluation (§5.2) focuses on 250 pairwise examples from the 2‑vs‑3 rating pair — the hardest gap — and demonstrates high annotator agreement. However, the training data spans a full 5‑point scale, and there is no human validation for gaps involving ratings 1, 4, and 5. The error analysis in §6.2 reveals that VideoJudge consistently overestimates scores and is poorly calibrated at higher ratings (81.3% of rating-4 responses are incorrectly rated as 5), which is consistent with noise in training supervision at the top end. Without coverage of the full rating scale, the paper cannot fully rule out that the fine-tuned judge is learning pipeline-specific artifacts rather than genuine quality distinctions, especially at the upper end.

### Minor

- **Generator and evaluator models are not identified in the main text.** The methodology (§3) refers to generator *G* and evaluator *E* but does not state which models instantiate them. The dense video description model is mentioned as a "strong vision-language model (§A.2)" in the stripped appendix. Without knowing whether *G* and *E* are the same model used for fine-tuning or much larger models, the reader cannot assess potential biases in the bootstrapping dynamics (e.g., whether the pipeline is essentially self-distilling or cross-distilling). This is fixable and the appendix likely contains the information, but it is an omission in the main paper that affects reproducibility assessment.

- **Acceptance threshold α and refinement iteration statistics are not reported.** The pipeline uses a threshold α for acceptance and up to *T* iterations, but neither value is stated in the main text. Knowing the typical number of refinement rounds and the proportion of responses that fail the acceptance criterion would help readers assess the pipeline's efficiency and quality control.

- **No statistical significance or confidence intervals.** Many comparisons (e.g., VideoJudge‑7B vs. Qwen‑72B on several metrics) involve numerically close values with no reported variance. This makes it difficult to assess whether observed differences are meaningful.

- **Failure rates for excluded video models are not provided.** The paper excludes several video models (VideoLLaMA3-7B, VideoChat-Flash, Keye-VL, SmolVLM2) because they "often failed to follow instructions." Concrete failure rates would be informative and should be reported.

### Trivial

None.

## Nice-to-Haves

- Expand human validation of the training data to cover additional rating pairs (e.g., 3‑vs‑4, 4‑vs‑5), even with a smaller sample per pair, to validate the full rating scale.
- Structure the narrative to foreground results on human-annotated independent benchmarks (VATEx, LongVideoBench, VAA, VJ‑H) as primary evidence, with pipeline-benchmark results as diagnostic/diagnostic tools.
- Report acceptance threshold α and average/max refinement iterations for the bootstrapping pipeline.
- Quantify the failure rate for each excluded video model.

## Removed Points

- **Criticism about automatic metrics (BERTScore, BLEU) being poor proxies for response quality** — The paper only uses these as a sanity check (monotonic degradation should hold), not as evidence of absolute quality. The primary validation is the human evaluation. The criticism overstates the role of these automatic metrics.
- **"Strengthening the paper on its own terms" framework suggestions about restructuring the narrative** — These are editorial suggestions, not weaknesses per se. They are captured in Nice-to-Haves above.
- **Criticism about the rubric human evaluation having only 53.4% unanimous win rate against GPT-4o-mini** — "Barely above chance" ignores that unanimous agreement is a very strict criterion. The majority vote figure (likely higher, noted as not shown) would be the fairer comparison. The results against Qwen-72B (63.9%) are cleanly positive.
- **Concerns about "not yet released" artifacts** — The paper provides a code/model/data link, and we assume these exist as of the review date per instructions.
- **Formatting/style nitpicks** — Parser artifacts, not author errors.

## Novel Insights

Beyond the paper's own contributions, the most striking finding that emerges is the asymmetry in where the bootstrapping pipeline succeeds and fails: the pipeline generates high-quality supervision for distinguishing coarse quality differences (ratings 1–3) but systematically breaks down at the top end (ratings 3–5), where the trained judge overestimates scores and is poorly calibrated. This pattern — that bootstrapping without explicit hard negatives at the high end produces inflated evaluations — is a generalizable caution for any self-supervised evaluation pipeline. It suggests a design principle: bootstrapped judge training may need explicit upsampling of near-perfect-but-not-quite responses to avoid calibration collapse at the top of the scale.

## Suggestions

1. Add a single sentence in §3 specifying which models instantiate *G* and *E* (e.g., "We use Qwen2.5-VL-72B for both G and E").
2. Report the acceptance threshold α and refinement iteration statistics (average number of iterations, % of responses requiring refinement) alongside the bootstrapping description.
3. Add bootstrapped confidence intervals or standard deviations to the main result tables, especially for comparisons where scores are close.
4. Include a clear "caveat" sentence in the abstract and conclusion noting that the strongest correlations are on pipeline-constructed benchmarks and that performance on human-annotated benchmarks is competitive but not uniformly superior.

## Score and Decision

**Calibration report:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| m8yby1JfbU — Is Your VLM a Reliable Judge? | 6.50 | 1, 2 | Weaker contribution: only analyzes existing models as judges, no method or training. VideoJudge is clearly stronger. |
| uHgVrGF2Wn — LVBench | 4.50 | 1 | Different type (benchmark-only); lower quality. Not directly comparable. |
| WyEdX2R4er — Visual Data-Type Understanding | 8.00 | 1 | Different topic; stronger evaluation rigor. |
| JYV2hrtFSv — Video-STaR | 6.25 | 2 | Self-training for video instruction tuning. VideoJudge has stronger empirical evidence and less reliance on heuristic filtering. |
| xsELpEPn4A — JudgeLM | 7.50 | 2 | Closest analog (LLM-as-Judge training). VideoJudge tackles harder modality (video) and evaluates on independent human benchmarks, but JudgeLM has cleaner evaluation. Comparable quality; VideoJudge slightly below. |
| X1OfiRYCLn — VLB Bootstrapping | 7.50 | 2 | Dynamic evaluation via bootstrapping. Different contribution; similar quality level. |
| Gf1uBeuUJW — Unhackable Temporal Reward | 6.50 | 2 | Different topic. |
| Acdd83rF1s — LLM-VTP | 5.80 | 2 | Different topic; lower quality. |
| le4IoZZHy1 — CG-Bench | 6.20 | 2 | Benchmark paper; different contribution type. |
| bjyf5FyQ0a — Valley | 4.75 | 2 | Video assistant model; lacks novelty. VideoJudge is significantly stronger. |

**Round-1 bracket:** 6.5 – 8.5  
**Round-2 narrowing:** Compared to JudgeLM (7.50) — the most thematically similar anchor — VideoJudge is comparable in contribution scope but has two notable weaknesses (closed-loop evaluation on pipeline benchmarks, limited human validation across the rating scale) that JudgeLM did not face in its text-only setting. Compared to Video-STaR (6.25) and "Is Your VLM a Reliable Judge?" (6.50), VideoJudge is clearly stronger. The paper falls between the 6.5 and 7.5 anchors.

**Final score: 7.0** — A solid paper with a well-motivated contribution, extensive evaluation, and released resources. The weaknesses (closed-loop evaluation concern, limited human validation of training data) are real but not fatal; they can be addressed through clearer presentation and modest additional validation. The paper advances the state of the art in MLLM-based video evaluation.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>