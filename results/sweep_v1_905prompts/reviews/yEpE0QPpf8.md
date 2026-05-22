## Summary

This paper introduces **Grounding-IQA**, a new task paradigm that integrates multimodal referring and grounding with image quality assessment (IQA). The paradigm comprises two sub-tasks: GIQA-DES (quality descriptions with bounding boxes) and GIQA-VQA (quality QA with spatial locations). The authors contribute an automated annotation pipeline to construct GIQA-160K (167K instruction-tuning samples from 43K images) and a manually-annotated benchmark GIQA-Bench (100 images, 250 samples). Fine-tuning four MLLM backbones (LLaVA-v1.5-7B/13B, LLaVA-v1.6-7B, mPLUG-Owl2-7B) on GIQA-160K yields consistent improvements across description quality, VQA accuracy, and grounding precision metrics compared to general, grounding-specific, and IQA-specific baselines.

## Strengths

1. **Novel and well-motivated task paradigm.** The paper is the first to formally define grounding-IQA as two complementary sub-tasks (GIQA-DES and GIQA-VQA) that combine spatial localization with quality assessment. This is a natural extension of prior MLLM-based IQA methods that lack fine-grained spatial awareness. The motivation is clearly articulated with concrete examples (Figure 2).

2. **Well-designed automated annotation pipeline.** The four-stage pipeline (object tag extraction via Llama3 with three-tuple quality tags → bounding box detection via Grounding DINO → IQA-Filter and Box-Merge refinement → coordinate discretization) is carefully engineered. The chain-of-thought-style three-tuple tag ($\mathcal{T}_r, \mathcal{T}_q, \mathcal{T}_c$) and the use of description phrases rather than object names for detection (Figure 4) are thoughtful design choices. The ablation in Table 2a validates that refinement improves mIoU (0.5624 → 0.5851) and Tag-Recall (0.5045 → 0.5497).

3. **Consistent and multi-dimensional improvements.** Table 5 shows that Grounding-IQA fine-tuning improves all four base models across nearly all metrics. The gains are substantial on VQA accuracy (e.g., LLaVA-v1.5-7B Acc Total 0.4733 → 0.6850) and grounding (e.g., Tag-Recall from N/A to 0.5961). Importantly, the ablation in Table 3 confirms that multi-task training (both GIQA-DES and GIQA-VQA) is beneficial over single-task training.

4. **Compatibility across diverse architectures.** Table 4 demonstrates that the same GIQA-160K dataset improves four distinct MLLMs (different versions, sizes, architectures), showing the dataset is model-agnostic and generalizable.

## Weaknesses

### Major

1. **The benchmark is too small to support fine-grained metric comparisons without uncertainty quantification.** GIQA-Bench contains only 100 images, 100 GIQA-DES samples, and 150 GIQA-VQA samples. No confidence intervals, bootstrap estimates, or statistical significance tests are reported. Differences as small as 1–4 points in LLM-Score (e.g., Q-Instruct 62.00 vs. Grounding-IQA 63.00) or ~0.9 points in BLEU@4 are interpreted as meaningful improvements, but with 100 test samples these could easily fall within noise. The consistent pattern across *models* partially mitigates this concern, but individual metric comparisons lack statistical grounding. The paper would be substantially stronger with bootstrap confidence intervals or variance estimates.

2. **Selective visualization in the radar chart (Figure 1).** The radar chart compares Grounding-IQA variants against only Shikra and one other baseline, omitting Ferret — which achieves higher Tag-Recall on GIQA-DES (0.6778 vs. the best Grounding-IQA variant's 0.5981). While Table 5 presents the full results honestly and the text acknowledges the trade-off ("grounding MLLMs excel in grounding tasks but underperform on quality-related objects"), the radar chart visually overclaims "significantly higher performance across most metrics" by excluding the one model that outperforms the proposed method on a key metric.

### Minor

1. **The automated pipeline lacks direct human validation of output quality.** The GIQA-160K dataset is constructed entirely automatically via Llama3, Grounding DINO, and Q-Instruct. The paper provides indirect evidence of quality (box area distribution comparison in Figure 6, ablation showing refinement helps) but does not include a human evaluation of, e.g., what fraction of generated bounding boxes correctly correspond to the intended object, or how often the quality tags ($\mathcal{T}_q$) match human judgment. The primary data sources (Q-Pathway, DQ-495K) have human-annotated descriptions, but the object extraction and box detection steps introduce error that is not directly measured. A small-scale human audit (100–200 samples) of the training data would substantially increase confidence.

2. **The Yes/No distribution mismatch between training and benchmark.** GIQA-160K training data is artificially balanced (25,242 Yes / 25,242 No), while GIQA-Bench has an imbalanced split (35 Yes / 55 No). This mismatch could create a systematic bias — a model trained on 50/50 data may not be optimally calibrated for the benchmark's real-world skew. The impact is likely small but worth discussing.

3. **Slight overclaim in the abstract/introduction.** The paper states that the proposed method "outperforms existing MLLMs," but this is not universally true: on GIQA-DES Tag-Recall, Ferret-7B achieves 0.6778 vs. the best Grounding-IQA variant's 0.5981. The claim should be qualified to acknowledge the grounding-precision vs. IQA-quality trade-off, which the paper's Section 4.3 does discuss accurately.

### Trivial

- Box-Merge thresholds ($T_a = 0.256$, $T_o = 95\%$) are presented without sensitivity analysis. A brief ablation showing how performance varies with these choices would increase confidence.
- The paper uses both "IQG" and "IQA" interchangeably in some places (e.g., "IQG models" vs. "IQA models" in Table 5 and conclusion).

## Nice-to-Haves

- Comparison with a simple two-stage pipeline that applies Grounding DINO as a post-hoc detector on top of Q-Instruct outputs, to isolate the benefit of end-to-end learned grounding vs. a pipelined alternative.
- Failure case analysis: what types of images/objects does the model systematically get wrong (small objects, heavy blur, overlapping boxes)?
- Discussion of whether the balanced Yes/No prior in training data could affect real-world deployment.

## Removed Points

- **"Ferret beats us on both GIQA-DES mIoU and Tag-Recall" (Harsh Critic):** Factually incorrect. Ferret's mIoU (0.6458) is *lower* than the best Grounding-IQA variant (0.6583, LLaVA-v1.6-7B). Only Tag-Recall favors Ferret. The critic's central factual claim is wrong on one of two metrics.
- **"Radar chart omits Shikra" (Harsh Critic):** The figure caption explicitly lists "Shika-7B" (Shikra-7B) among the compared methods. Shikra is present.
- **"Multi-task ablation shows grounding adds little" (Harsh Critic):** Table 3 shows the full dataset (GIQA-160K) achieves Acc (Total) 0.7417 vs. Only-VQA's 0.7217, and Tag-Recall of 0.7372 vs. 0.4872. Grounding clearly adds substantial value.
- **"Missing related works" (general):** Not verifiable without external sources; papers cited are assumed to exist per review guidelines.
- **Formatting/style nitpicks:** Parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add bootstrap confidence intervals (or similar uncertainty estimates) for all metrics on GIQA-Bench.
2. Conduct a small-scale human evaluation (e.g., 200 random samples) of the automated pipeline's output quality — box correctness, tag accuracy, description relevance.
3. Include Ferret in the radar chart (Figure 1) to give a complete visual comparison, or at minimum note in the caption which grounding models are excluded and why.
4. Qualify the "outperforms" claim to acknowledge the specific metrics where Ferret remains superior (Tag-Recall).
5. Provide a sensitivity analysis of the Box-Merge thresholds ($T_a$, $T_o$).

## Score and Decision

**Calibration details.**

*Round 1 (bracketing):* Retrieved four weak anchors (avg 2.50–3.40), four middle anchors (4.75–5.75), and four strong anchors (7.75–8.00). The paper is clearly above the weak band (3ish) and clearly below the strong band (8ish), placing it in the 4–7 range.

*Round 1 bracket:* 4.0–7.0.

*Round 2 (narrowing):* Retrieved seven anchors in (4.5, 6.5) and (5.5, 7.5). Compared against:
- **Dog-IQA** (4.75, rejected): Grounding-IQA is stronger in novelty (new paradigm vs. standard-guided scoring) and has more thorough ablations.
- **Q-Adapt** (5.25, rejected): Comparable overall; Grounding-IQA has clearer motivation and more novel task formulation.
- **EDQA** (5.75, rejected): Comparable; both contribute datasets and pipelines. Grounding-IQA has a more novel paradigm but smaller benchmark.
- **UniQA** (5.75, rejected): Comparable; both use automated data construction. Grounding-IQA has clearer novelty in task definition.
- **EvalAlign** (4.75, rejected): Grounding-IQA is stronger in breadth and novelty.
- **LLMs as Aligners** (6.00, accepted): This paper has a more comprehensive automated pipeline for benchmark construction but is less novel in the core task; Grounding-IQA is slightly weaker.
- **Ferret** (6.67, accepted): Ferret is substantially stronger in architectural innovation, dataset scale (1.1M), and community impact; Grounding-IQA is a narrower application of similar ideas to IQA.

*Round 2 comparison:* The paper sits between the 5.25–5.75 range (Q-Adapt, UniQA, EDQA — all rejected) and the 6.0+ range (LLMs as Aligners — accepted). It is stronger than the 4.75 papers but not as strong as the accepted papers in this space. The evaluation gaps (small benchmark, no confidence intervals, no human validation of pipeline) prevent it from being as convincing as the accepted anchors.

*Final score: 5.5.* This reflects a solid contribution with a genuinely novel paradigm and careful pipeline design, held back by evaluation evidence that is incomplete in ways that are fixable but materially weaken the current presentation.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>