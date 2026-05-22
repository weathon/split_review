Now I have all the information needed. Let me produce the consolidated review.

## Summary

GRAID proposes a framework to generate spatial reasoning VQA data using only 2D bounding boxes from object detectors, avoiding the cascading errors of single-view 3D reconstruction and hallucinations from caption-based generation. The paper instantiates 22 VQA templates on BDD100k, NuImages, and Waymo to produce 8.5M+ VQA pairs, and demonstrates through human evaluation and fine-tuning experiments that (a) GRAID-generated data has higher validity than a comparable dataset from SpatialVLM, and (b) models fine-tuned on GRAID data learn transferable spatial concepts that improve performance on held-out question types and external benchmarks across four backbone architectures.

## Strengths

- **Core insight is clean and well-motivated.** Using only 2D geometry (bounding boxes) to determine qualitative spatial relationships is an elegant way to avoid the known failure modes of metric-depth estimation and LLM hallucination. The method requires no architectural changes to VLMs and no 3D reconstruction, making it easy to adopt.

- **Strong evidence for transferable spatial concept learning (RQ2).** Fine-tuning Llama 3.2 11B on only 6 question types from GRAID-BDD improves accuracy on over 10 held-out question types in both GRAID-BDD (+47.5 pp overall) and the unseen GRAID-NuImages (+37.9 pp overall). This is the paper's strongest internal evidence that the generated data teaches spatial primitives that generalize beyond template memorization.

- **Consistent gains across multiple backbones on external benchmarks (RQ3).** The paper reports that models fine-tuned on GRAID data outperform SpatialVLM-tuned models across 5 benchmarks (BLINK, A-OKVQA, RealWorldQA, NaturalBench, VSR) and 4 backbones (Llama 3.2 11B, Gemma 3 4B, Qwen2.5 VL 3B, Qwen3 VL 8B). Concrete numbers are provided: e.g., +15.94% overall on BLINK, +32.5% on A-OKVQA for Llama. The consistent trend across architectures is a real strength.

- **Practical engineering contribution (SPARQ).** The predicate-based filtering approach yields meaningful speedups (9× for representative templates, up to 1407× for the heaviest), enabling generation at the stated scale within practical compute budgets.

- **Large-scale open-source release.** Generation of 8.5M VQA pairs from three datasets with a clean, extensible framework is a valuable community resource.

## Weaknesses

### Fatal

None.

### Major

- **Human evaluation methodology limits the headline quality claim.** The paper's central advertised number (91.16% vs. 57.6%) rests on a human evaluation with several methodological concerns: (a) the comparison is not apples-to-apples — GRAID-BDD (qualitative spatial questions) is compared to OpenSpaces from SpatialVLM (metric distance questions), so the gap may partly reflect task difficulty rather than data-generation quality; (b) only 317 GRAID pairs and 250 SpatialVLM pairs were evaluated, which is modest for a headline claim about dataset quality at the million-pair scale; (c) no inter-annotator agreement is reported for the 4 human evaluators, so the reliability of the validity judgments is unknown. The 57.6% figure for SpatialVLM is also for "answers incorrect" while the GRAID figure aggregates question validity, answer correctness, and labeling errors, making the comparison imprecise. The gap is large and likely real, but the paper's strongest advertised contribution — data quality — would benefit substantially from a controlled side-by-side evaluation on the same images.

### Minor

- **Unusual learning rate for LoRA fine-tuning.** The paper states a learning rate of \(2^{-4}\) (0.0625) for all LoRA experiments (p. 7). Typical LoRA learning rates for VLMs are \(1\times10^{-4}\) to \(5\times10^{-4}\). While AdamW8bit can accommodate larger rates, this is roughly 100× above typical practice and warrants clarification — particularly because the results are consistent across models and benchmarks, suggesting the training was stable, but the stated hyperparameter is an outlier.

- **Inconsistency between described algorithm and pseudocode for RightOf.** The text (Section 3.2, p. 4) states that the RightOf question realization checks two conditions: "(1) the bounding boxes of each potential pair should be non-overlapping, and (2) they should lie on similar planes." However, Algorithm 1 (the "full algorithm") only implements condition (1) (IoU=0 check) and the class-count check; there is no "similar planes" computation in the pseudocode. This discrepancy makes it unclear what the actual implementation does and whether the appendix resolves it.

- **The "cascading modeling errors" claim is asserted rather than demonstrated.** The abstract and introduction attribute SpatialVLM's failures to "cascading modeling errors" from single-view 3D reconstruction, but the human evaluation only measures final answer correctness — it does not isolate error sources (depth estimation vs. camera calibration vs. geometry). The claim is plausible but is an untested assumption in the paper's framing of the problem.

### Trivial

- The 1407× speedup figure for `LargestAppearance` (comparing 0.02ms predicate vs. 28.1ms realization) is technically accurate but represents the most extreme case. The paper does report the more representative 9× figure for `RightOf`, so this is not misleading — just worth contextualizing.

## Nice-to-Haves

- Run the human evaluation on the **same set of images** with questions generated by both GRAID and SpatialVLM pipelines, to isolate generation methodology from image/domain differences.
- Ablate the effect of detection quality (ground-truth boxes vs. off-the-shelf detector outputs) on downstream task performance.
- Break down BLINK improvements by sub-category in the main text to show which spatial concepts benefit most from GRAID training.
- Analyze why `LessThanThresholdHowMany` regresses after SFT beyond the paper's brief "overfitting" speculation.
- Evaluate on non-driving domains (e.g., indoor scenes) using detected boxes to further demonstrate domain agnosticism.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

1. **"Missing RQ3 results (Tables 4, 5, 6)"** — Removed. These tables are in the appendix, which was stripped by the parser. The paper explicitly references them and provides concrete summary numbers (+15.94% on BLINK, +32.5% on A-OKVQA) in the main text.
2. **"91.16% vs. 'less than 9%' numbers are inconsistent"** — Removed. These are the same quantity expressed differently. "Less than 9% invalid/confusing" ⟺ "more than 91% valid." The 91.16% figure rounds correctly (28/317 ≈ 8.84% → 91.16%).
3. **"Baseline for RQ1 is too low (31%)"** — Removed. The improvement (+49.7 pp on held-out BDD; +29.1 pp cross-dataset on NuImages) is large regardless of starting point. The cross-dataset result in particular is strong evidence of transfer.
4. **"RQ2 regression not explained"** — Removed. The paper already addresses this: "we suspect that this is a symptom of overfitting." A deeper analysis would strengthen the paper but the absence is not a flaw.
5. **"SPARQ 1400× speedup is cherry-picked"** — Removed. The paper presents both the extreme case (1407× for `LargestAppearance`) and the representative case (9× for `RightOf`), with appropriate context. The phrasing "up to 1400×" is standard and accurate.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Strengthen the human evaluation with an apples-to-apples comparison on identical images, report inter-annotator agreement, and use a larger sample.
2. Clarify the LoRA learning rate — confirm that \(2^{-4}\) is correct rather than a typo, and explain why it works at this scale.
3. Resolve the discrepancy between Algorithm 1 (no plane check) and the text describing the RightOf algorithm (which mentions a plane check).
4. Include a brief breakdown of the BLINK sub-task improvements in the main body, not only the aggregate number.

## Score and Decision

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>