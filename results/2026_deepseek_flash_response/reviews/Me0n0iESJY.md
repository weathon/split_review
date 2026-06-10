## Summary

This paper introduces a benchmark for evaluating model merging methods on Multimodal LLMs (MLLMs), covering 5 capability categories (VQA, Geometry, Chart, OCR, Grounding) across two model families (InternVL2.5 and Qwen2-VL) with both full fine-tuning and LoRA scenarios. The paper also proposes OptMerge, an optimization-based merging method building on WUDI Merging with SVD-based low-rank denoising and modified initialization/optimizer choices, and explores modality merging (vision, audio, video). The benchmark contribution — trained expert models, evaluation splits, and results for 10 merging algorithms — has practical value for the community.

## Strengths

1. **First dedicated benchmark with fine-grained MLLM task categorization for model merging.** The paper constructs 5 distinct task categories with ≥100k samples each, covering two model families (InternVL2.5 full FT, Qwen2-VL LoRA), and trains/releases expert models. Prior work such as AdaMMS merges only two models at a time, and UQ-Merge treats each dataset as a separate task without categorization. This creates useful infrastructure that fills a genuine gap.

2. **Comprehensive empirical comparison across 10 merging algorithms.** The paper systematically evaluates Weight Averaging, Task Arithmetic, TIES, DARE, TSV, Iso-C, WUDI, and OptMerge on two model families and on real HuggingFace community checkpoints (Table 6), providing a broad landscape of relative method performance.

3. **Computational efficiency demonstration.** Table 7 shows OptMerge uses 3.78h/21.97GB vs. 24.56h/256GB for mixture training on Qwen2-VL-7B (~6.5× speedup, ~12× memory reduction), concretely demonstrating the cost advantage of model merging over multi-task training.

## Weaknesses

### Major

1. **Numerical inconsistency in Table 3 (WUDI Merging average).** The WUDI Merging row reports an average of 63.65, but summing the 10 individual benchmark scores in that row gives 599.72, yielding an actual average of ~59.97 — a discrepancy of 3.68 points. Other rows in the same table compute correctly, isolating this to WUDI's entry. This is not a minor arithmetic slip: if the average is correct and the individual values are wrong, OptMerge (63.30) underperforms WUDI; if the individual values are correct and the average is wrong, the gap is much larger than reported and WUDI's ranking drops below several other methods. Either way, the reader cannot trust the quantitative comparisons at face value without author clarification. The paper is positioned as a benchmark, so numerical precision is foundational.

2. **The method's claimed innovation is mostly attributable to a simple initialization heuristic.** The ablation (Table 4) on Qwen2-VL (LoRA) shows: WUDI baseline 58.65, +SGD alone drops to 48.88 (−9.77%), +initialization recovers to 63.08 (+4.43%), and +low-rank SVD truncation adds only +0.22% to reach 63.30. The paper presents OptMerge as "remov[ing] noise from task vectors and robustly optimiz[ing] the merged vector," but the evidence shows the gain is driven almost entirely by mean-initialization of the merged vector — a straightforward heuristic. Furthermore, the SVD denoising (Eq. 3) is designed for full fine-tuning models (Sec 4.1), but the ablation only evaluates its contribution on LoRA models, leaving its isolated effect on full fine-tuning unvalidated. This gap between the paper's framing (a novel denoising method) and what the evidence actually supports weakens the contribution claim.

### Minor

3. **"Emergent integrated capabilities" claim (Table 10) is overstated.** The paper states that OptMerge "demonstrates emergent integrated capabilities" (line 337). However, the individual specialist models perform poorly on these general QA benchmarks because they were narrowly fine-tuned, so a merged model naturally outperforming them is expected from task arithmetic — not evidence of "emergence." This is a framing issue that inflates the significance of the result.

4. **Mixture training comparison is not apples-to-apples across both architectures.** On InternVL2.5 (Table 2), OptMerge (57.44) slightly underperforms actual mixture training (57.66). On Qwen2-VL (Table 3), the comparison is to Qwen2-VL-Instruct — a model trained on a different, larger data mixture — not a controlled re-implementation. The paper acknowledges this asymmetry (line 224) but the headline contribution claim "model merging can outperform mixture training" (line 38, line 341) outstrips the evidence.

### Trivial

5. Expert model training hyperparameters are not reported ("we minimize parameter changes by adjusting the learning rate" without stating actual values), hindering full reproducibility of the benchmark.

## Removed Points

- **"First benchmark claim is overstated":** Removed. The paper claims "the first model merging benchmark that provides a fine-grained categorization of MLLM capabilities" (line 36), which is qualified. Prior work (AdaMMS, UQ-Merge) did not provide this categorization, making the claim defensible.
- **"Only 2 datasets for modality merging":** Removed. The paper frames this as exploratory, and the observation is better placed in Nice-to-Haves.
- **"Missing statistical reliability / confidence intervals":** Removed. Single-run evaluation on large benchmarks is standard practice in this community.
- **"SGD rationale is unjustified":** Removed. The paper cites Smith et al. (2021) and Wang et al. (2022) for implicit regularization, which is a reasonable citation-supported rationale.
- **Missing training details**: Removed per hard rules about nitpicks on undisclosed hyperparameters.
- **"Methodological underspecification"**: Removed — the method description is at an appropriate level for the paper's scope.

## Nice-to-Haves

- Extend modality merging evaluation beyond the current 2 datasets (MUSIC-AVQA, AVQA) to more benchmarks.
- Report results over multiple random seeds to assess variance, especially given small improvements (<1%) in some settings.
- Provide a clearer breakdown of how the "2.48% average performance gain" claimed in the abstract is computed.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Correct the Table 3 WUDI average** to match the individual values (or vice versa) and explain the source of the discrepancy. Without this fix, the quantitative claims lack credibility.
2. **Re-frame the method contribution** to honestly acknowledge that the primary benefit on LoRA models comes from mean-initialization, and provide an ablation isolating the SVD denoising on full fine-tuning models (InternVL2.5).
3. **Tone down "emergence" language** for the Table 10 results and clarify that the mixture training comparison is asymmetric across architectures.

## Score and Decision

**Score: 5.0 — Reject**

**Calibration anchors used (all rounds):**

| Paper (path) | Round | Avg Score | Comparison |
|---|---|---|---|
| `gNoqEdT2wO` — MCL benchmark | R1 (low) | 2.33 | Weaker — much less relevant scope |
| `lNtio1tdbL` — ATM model merging | R1 (low) | 3.00 | Weaker — smaller scope |
| `fvUVe2gJh0` — What Matters for Model Merging at Scale? | R1 (mid) | 5.33 | Comparable — systematic study with clean evaluation but no benchmark |
| `lIdc5DUplq` — SUPERMERGE | R1 (mid) | 4.33 | Weaker — presentation issues, but comparable method contribution |
| `Bq3fEAGXUL` — Realistic Evaluation of Model Merging | R1 (mid) | 5.33 | Comparable — both have evaluation contributions and thin method novelty |
| `2pvMZKGYDR` — WIDEN | R1 (mid) | 5.67 | Slightly stronger — addresses a genuinely new merging problem (PT models) |
| `HnhNRrLPwm` — MMIE | R1 (high) | 8.00 | Stronger — large-scale clean benchmark with no method combination |
| `SO0manOwUF` — UQ-Merge | R2 | 5.50 | Comparable — both on MLLM merging, UQ-Merge has more novel method idea but weaker benchmark |
| `1v7SRWsYve` — MAP | R2 | 6.33 | Stronger — cleaner method contribution, no numerical errors, accepted |
| `plflYGf23L` — CABS | R2 | 4.75 | Comparable — both have incremental merging contributions |

**Round 1 bracket:** (3.5, 7.5) — clear that the paper is neither a weak paper (2–3) nor a standout paper (8+).

**Round 2 narrowing:** Comparison with UQ-Merge (5.50), MAP (6.33), WIDEN (5.67), and CABS (4.75) places this paper around 5.0. The benchmark contribution is genuine and useful, distinguishing it from purely-incremental method papers. However, the numerical error in Table 3 is a quality control problem not present in the higher-scored anchors, and the method contribution is thinner than UQ-Merge's or WIDEN's. The paper offers a reasonable benchmark resource but does not meet the bar for a top venue in its current form.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>