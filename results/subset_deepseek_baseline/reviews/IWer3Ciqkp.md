## Summary

PG-VLM proposes a modular framework for generating paragraph-level descriptions of urban scenes. The pipeline first builds a Hierarchical Panoptic Scene Graph (HPSG) from panoptic segmentation, then distills the graph into semantic triplets using a local instruction model, and finally generates a narrative with a T5 decoder. Evaluations on Cityscapes and a zero-shot subset of BDD100K show improvements over BLIP-2, LLaVA-1.5, and SpatialVLM in captioning metrics (CIDEr, SPICE, BERTScore), hallucination reduction (CHAIR), and a newly proposed instance-level grounding metric (NRDS).

## Strengths

- **Clear and well-motivated architecture.** The explicit HPSG→triplet bottleneck is a principled way to enforce spatial grounding and reduce hallucination. The three-stage pipeline (perception, triplet extraction, structured-to-text generation) is easy to follow and decomposes the problem.
- **Comprehensive evaluation on multiple dimensions.** The paper goes beyond standard captioning metrics by reporting hallucination rates (CHAIR-s/i, Entity-Precision), the proposed NRDS for instance-level grounding, and a cross-dataset zero-shot transfer check. This multi-faceted evaluation strengthens the empirical claims.
- **Strong empirical gains.** PG-VLM achieves sizable margins on CIDEr (+16.8 over SpatialVLM) and NRDS (+0.24 over BLIP-2) while nearly halving CHAIR-s rates compared to BLIP-2. The zero-shot results on BDD100K maintain a consistent advantage, suggesting the bottleneck helps generalization.
- **Proposed NRDS metric addresses an important gap.** The metric directly ties detection correctness and narrative importance to textual realization, which is lacking in lexical-overlap metrics. The motivation and design are sound in principle.

## Weaknesses

### Fatal
None.

### Major

- **Pseudo-label bias threatens internal validity.** The teacher model (LLaMA-2-7B-Chat) generates both the triplet-to-paragraph training targets for PG-VLM *and* the reference paragraphs used to compute all automatic metrics (CIDEr, SPICE, BERTScore, etc.) for all models. Because PG-VLM’s decoder is trained on teacher-generated texts, it will naturally achieve higher lexical and semantic similarity to those references than baselines that were not trained on them. The paper acknowledges this but only partially addresses it with hallucination metrics and a human evaluation relegated to Appendix A.8 (not available in the review). Without seeing the human evaluation results in the main paper, the headline improvements on text-based metrics are unconvincing as evidence of superior quality.
- **NRDS metric formulation is inconsistent and insufficiently defined.** The equation in Section 4.4 multiplies `DetAcc, NarrImport, ParaAcc`, but the pipeline figure (Figure 1) shows `DetAcc * NarrImport + ParaAcc`. The denominator is `TotalNarrImport_i`, which is defined as the sum of narrative weights over narratively relevant ground-truth instances, but the numerator includes `ParaAcc_j` for each detection. The interaction between detection accuracy, narrative importance, and paragraph accuracy is not clearly justified, and the figure suggests a different combination rule. This ambiguity undermines the reliability of NRDS as a reported metric.
- **Baselines are not trained on the target data.** BLIP-2, LLaVA-1.5, and SpatialVLM are used off-the-shelf without any fine-tuning on Cityscapes paragraphs or even prompt adaptation for urban scene description. A fairer comparison would either fine-tune baselines on the same pseudo-labels or use human evaluation as the primary measure. The current comparison likely favors PG-VLM due to distribution shift and reference alignment.

### Minor

- **Cross-dataset generalization evidence is weak.** The zero-shot check uses only 50 images from BDD100K. While the results are promising, a larger and more diverse sample (including nighttime, weather, different city types) would be needed to claim robust generalization.
- **Lack of failure analysis.** The paper does not discuss cases where the HPSG construction fails (e.g., missed objects, incorrect spatial relations) and how those propagate to the final narrative. Understanding failure modes would help assess practical robustness.
- **Reproducibility details are partial.** The geometric functions `γ_r` for edge scoring, predicate-specific thresholds for triplet filtering, and the salience score combining geometric confidence, predicate prior, and degree centrality are described at a high level without precise formulations. This makes re-implementation harder.

### Trivial
None.

## Nice-to-Haves

- Present the human evaluation results in the main paper (Appendix A.8) to strengthen the case that improvements are not solely due to reference bias.
- Release code and pre-trained models to facilitate reproducibility and downstream use.
- Include an ablation showing results when baselines are fine-tuned on the same pseudo-labeled data.
- Provide a failure case example with full breakdown (HPSG miss, triplet omission, decoder error).

## Novel Insights

Beyond the paper’s own contributions, the key insight is that *enforcing a symbolic bottleneck* (panoptic graph → compact triplets) before language generation can yield higher spatial fidelity and lower hallucination than end-to-end vision-language models, even when the bottleneck relies on a separate segmentation model. This supports the broader idea that structured intermediate representations can compensate for the lack of explicit reasoning in large pretrained models, at least for domain-constrained tasks like urban scene description.

## Suggestions

1. **Clarify and correct the NRDS formula.** Align the equation with the pipeline figure or provide a clear justification for the chosen combination rule. Ensure the metric is unambiguously defined so that readers can reproduce it.
2. **Address the pseudo-label bias more convincingly.** Either (a) fine-tune the baselines on the same pseudo-labels, (b) use a reference-free human evaluation as the primary assessment, or (c) adopt a second reference set (e.g., human-written paragraphs if available) that is independent of the pseudo-label generator.
3. **Expand the cross-dataset evaluation.** Use a larger and more varied subset of BDD100K (e.g., 200-500 images across different conditions) to support claims of cross-domain generalization.
4. **Provide concrete details for HPSG construction.** Release the geometric scoring functions, edge filtering thresholds, and the salience scoring formula to improve reproducibility.

## Score and Decision
6.0

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>