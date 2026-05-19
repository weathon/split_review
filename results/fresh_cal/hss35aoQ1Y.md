Now I have a thorough understanding of the paper and can verify all claims against the actual text. Let me produce the final consolidated review.

## Summary

This paper proposes InstructDET, a data-centric method that leverages foundation models (LLaVA, LLaMA) to automatically generate diverse referring instructions for single and multiple objects in images, producing the large-scale InDET dataset (3.6M instructions across 120.6K images). The authors then train a conventional DETR-based ROD model (DROD) on this data and compare it against existing visual grounding methods. The core idea is that diversifying instructions via foundation models can push referring object detection toward more practical usage.

## Strengths

1. **Large-scale, diverse instruction dataset with strong quantitative evidence.** InDET contains 3.6M instructions across 120.6K images with an average length of 6.2 words and a vocabulary of 63K words. Figure 3 shows that InDET has lower pairwise CLIP cosine similarity (higher diversity) and balanced coverage across all six guideline groups (G1–G6), whereas existing REC datasets (RefCOCO, Flickr) concentrate on simpler groups. This provides concrete, measurable evidence that InDET covers a broader range of user intentions.

2. **Controlled experiment shows InDET improves reasoning across different model architectures.** Figure 9(a) shows that when MDETR, Grounding-DINO, and UNINEXT are trained on InDET instead of RefCOCO or Flickr30K, their accuracy on 2k logic-reasoning test samples increases (e.g., UNINEXT from ~40% with RefCOCO to ~48% with InDET). This is a well-controlled experiment that isolates the data contribution across multiple model families, providing the strongest evidence for the dataset's value.

3. **Shuffled-words evaluation provides an interesting diagnostic for instruction comprehension.** The paper evaluates models on shuffled-instruction data (Table 1) and interprets larger performance degradation as evidence of better whole-instruction understanding. DROD drops 8.46 AP vs. UNINEXT's 5.76 on shuffled data, which is an inventive diagnostic even if the interpretation requires further validation.

4. **Clear and well-structured methodology.** The two-pipeline generation strategy (global prompt via LLaMA with in-context learning, local prompt via fine-tuned LLaVA) is clearly motivated, and the CLIP-based filtering mechanism (Equation 1) addresses an acknowledged hallucination problem. The multi-object expression generation via DBSCAN clustering + LLaMA summarization is a reasonable approach.

## Weaknesses

### Fatal
None.

### Major

1. **Uncontrolled comparison on the InDET test set undermines the headline superiority claim.** The paper reports that DROD achieves 62.24 AP on the InDET test set vs. UNINEXT's 43.37 (Table 1) and claims "our DROD largely surpasses UNINEXT." The paper does not state that the baselines were fine-tuned on InDET training data. As a result, DROD benefits from being trained on the InDET distribution (including its instruction style and vocabulary), while the baselines are evaluated off-the-shelf on a distribution they have never seen. The gap may largely reflect the data advantage rather than model design. The paper's own Figure 9 confirms that training baselines on InDET improves them, which supports the data contribution but simultaneously confirms that Table 1 is not a fair model-to-model comparison. This needs to be explicitly acknowledged and addressed, e.g., by fine-tuning baselines on InDET or presenting the comparison as a data-centric ablation rather than a method superiority claim.

### Minor

2. **Data mixture differs on standard benchmarks, confounding data and model contributions.** On RefCOCO/g/+ (Table 2), DROD uses O365+CC+InDET while UNINEXT uses O365+CC+RefC. The improvements are modest (e.g., 88.92 vs. 87.64 on RefCOCO val) and could reflect the additional/different training instructions rather than model design. Since the paper's model is described as "a conventional ROD model," the contribution is primarily data-centric, but the presentation blurs this distinction. An ablation training DROD on the same data as baselines (or vice versa) would sharpen the claim.

3. **No human evaluation of generated instruction quality.** The entire pipeline depends on whether the generated instructions are correct, natural, and free of hallucination. The paper relies on CLIP-based filtering and reports statistics (length, diversity) but provides no human ratings of instruction correctness or naturalness. The claim that "foundation models produce human-like expressions" is asserted without direct evidence. A human evaluation on a sample (e.g., 500–1000 instructions) would substantially increase confidence in the dataset quality.

4. **Metric choice on standard benchmarks is inconsistent with prior work.** Table 2 reports "AP values" on RefCOCO/g/+, where the standard evaluation metric in the REC literature is accuracy (predicted box IoU > 0.5). The paper should clarify whether this is detection AP, accuracy, or another metric, and justify why a different metric is used. This makes direct comparison with published numbers difficult.

5. **Local pipeline fine-tuning improvement is only qualitatively described.** The paper states "after finetuning, we observe the LLaVA output becomes informative and closely related to the target object" (line 63) without quantitative evaluation (e.g., CLIP scores, human ratings, or automatic metrics comparing pre- vs. post-fine-tuning outputs on a held-out set). This weakens confidence in a key component of the pipeline.

6. **Shuffled-words interpretation requires more careful framing.** The paper interprets a larger performance drop on shuffled instructions as evidence of better instruction comprehension (line 176–177). An alternative explanation is that DROD, having been trained on InDET's specific instruction patterns, is more sensitive to word-order disruptions — which could reflect overfitting to training distribution patterns rather than deeper semantic understanding. This does not invalidate the diagnostic but needs to be discussed.

### Trivial
- The assignment of instructions into six guideline groups (G1–G6) is done by LLaMA via in-context learning without validation of assignment accuracy.
- The paper does not ablate the contributions of the global vs. local generation pipelines separately.

## Nice-to-Haves
- An ablation of the CLIP filtering step showing recall/precision on a validation set would be useful.
- Error analysis of DROD's false positives and multiple-detection behavior.
- Reporting results on RefCOCO/g/+ using the standard accuracy metric for direct comparability.

## Removed Points
The following points from the input reviews were removed:
- **"Prompts not shown in main paper"**: The prompts are deferred to the appendix; the parser strips appendix content from all papers.
- **"α₁ value not given"**, **"DBSCAN threshold not reported"**, **"in-context examples count missing"**, **"training protocol details missing"**: These are standard details deferred to the appendix. The parser strips appendix content; they exist in the original submission.
- **Strength about "DROD substantially outperforms UNINEXT on InDET test set"**: This conflicts with the verified weakness (uncontrolled comparison); the weakness takes precedence per filtering rules, so this strength is removed. The data contribution is still recognized via other strengths.
- **Section-by-section notes about "appendix" content and "missing verification of assignment accuracy" as major issues**: These are minor or appendix-deferred and were demoted to Trivial/Nice-to-have.

## Novel Insights
None beyond the paper's own contributions. The two reviews largely agree on what the paper does well (dataset analysis, logic reasoning experiment) and what it does poorly (uncontrolled comparison on InDET test set, lack of human evaluation). The reviews do not surface a genuinely novel interpretation of the paper's results that the paper itself does not offer.

## Suggestions
1. **Retrain baselines on InDET data** and re-evaluate on the InDET test set. This separates data contribution from model design and would make the headline comparison credible.
2. **Add a controlled ablation on standard benchmarks** by training DROD on the same data mixture as UNINEXT (O365+CC+RefC) and comparing to DROD trained on O365+CC+InDET. This directly measures the value of InDET instructions.
3. **Conduct a human evaluation** on a sample of 500–1,000 generated instructions for correctness, naturalness, and diversity. Report the results alongside the CLIP-based filtering statistics.
4. **Clarify the evaluation metric** on RefCOCO/g/+ and, if possible, report accuracy (IoU > 0.5) for direct comparability with the existing literature.
5. **Acknowledge the uncontrolled nature of the InDET test set comparison** explicitly in the paper and reframe the claims accordingly (e.g., from "our DROD surpasses existing methods" to "training on InDET significantly improves a conventional ROD model").

## Score and Decision

The paper makes a genuine contribution through the InDET dataset and the instruction generation pipeline. The dataset analysis is thorough, and the controlled logic-reasoning experiment (Figure 9) provides credible evidence that InDET improves model performance across architectures. However, the headline experimental comparison (Table 1) is uncontrolled — DROD benefits from InDET training data while baselines are evaluated off-the-shelf — which undermines the claimed model superiority. Additional issues (no human evaluation of generated instructions, metric inconsistency on standard benchmarks, qualitative-only validation of pipeline components) further weaken the evaluation. These issues are addressable and do not invalidate the core data contribution, but they prevent the paper from being a definitive demonstration. The paper would be significantly strengthened by fair comparisons and human validation.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>