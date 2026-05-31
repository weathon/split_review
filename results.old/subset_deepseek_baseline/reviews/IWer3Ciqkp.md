## Summary

PG-VLM introduces a modular pipeline that constructs a Hierarchical Panoptic Scene Graph (HPSG) from panoptic segmentation, extracts semantic triplets via a local instruction LLM, and decodes paragraphs with T5-Large. The explicit symbolic bottleneck (HPSG → triplets → text) improves spatial grounding and reduces hallucination compared to end-to-end VLMs on Cityscapes, with favourable zero-shot trends on BDD100K. A new instance-level grounding metric, NRDS, is proposed to tie detection correctness to narrative realization.

## Strengths

- **Novel architecture with a symbolic bottleneck.** Inserting an explicit HPSG→triplet stage between vision and generation is a clean, principled way to enforce factuality and spatial fidelity. The approach naturally supports traceability and interpretability.
- **Strong empirical results on Cityscapes.** PG-VLM outperforms BLIP-2, LLaVA-1.5, and SpatialVLM across all standard captioning metrics, with particularly large margins on CIDEr (+16.8 over SpatialVLM) and SPICE (+5.2). Hallucination metrics (CHAIR-s/i) are roughly halved relative to BLIP-2.
- **Meaningful new metric (NRDS).** NRDS bridges the gap between text-only metrics and object-level grounding. The metric explicitly rewards faithful description of narratively important detections, which is well-motivated for urban scenes and complements existing evaluation.
- **Ablation studies isolate contributions.** The paper shows that removing the HPSG bottleneck (Direct ViT→T5) substantially degrades CIDEr, SPICE, CHAIR, and NRDS, confirming the value of the structured intermediate representation.
- **Zero-shot cross-dataset check.** On a held-out subset of BDD100K, PG-VLM retains a clear advantage over all baselines, suggesting the pipeline generalises beyond Cityscapes without dataset-specific tuning.

## Weaknesses

### Fatal
None.

### Major

1. **Potentially unfair comparison due to teacher-generated pseudo-labels.**  
   The T5 decoder is trained on pseudo-labels produced by a LLaMA-2-7B-Chat teacher that also generates the triplets. Baselines (BLIP-2, LLaVA-1.5, SpatialVLM) are evaluated *zero-shot* on these same pseudo-label references. This introduces a strong bias in favour of PG-VLM, especially for lexical-overlap metrics (BLEU, CIDEr, ROUGE-L). The paper acknowledges this bias but does not present the human evaluation it references in the main paper; the appendix results are not available in the provided manuscript. Without human judgements comparing model outputs directly against the *image* (not the teacher text), the reported gains on text-based metrics are suspect.

2. **NRDS formula inconsistency and lack of human validation.**  
   The NRDS formula in Figure 1 shows a different numerator (DetAcc·NarrImport·ParaAcc) from the text version (DetAcc·NarrImport + ParaAcc). It is unclear which is correct. Moreover, NRDS itself is not validated against human preferences; the paper only notes a correlation with CIDEr. A new metric introduced without human grounding weakens the claim that NRDS is a reliable indicator of narrative relevance.

### Minor

- The zero-shot experiment on BDD100K uses only 50 images. The sample is too small to draw strong statistical conclusions about cross-dataset generalization.
- The ablated “Direct ViT→T5” baseline is not fully specified (e.g., which ViT, how visual features are fed into T5). This makes it hard to assess whether the comparison is fair.
- The paper states that the teacher model “receives the triplets and produces a concise, spatially grounded paragraph”, but does not detail the prompt or any few-shot examples used, making reproduction difficult.
- The computational overhead of running Mask2Former + HPSG construction + triplet extraction + T5 decoding is not discussed, though this is not a core flaw.

### Trivial

- None beyond what is excluded by guidelines.

## Nice-to-Haves

- Include a small-scale human evaluation in the main paper (or at minimum summarise the appendix results) to support the claims of improved grounding and reduced hallucination.
- Validate NRDS against human ratings of narrative–detection alignment on a subset of Cityscapes.
- Provide a more complete ablation of the teacher LLM choice (e.g., a smaller or larger model) and its impact on pseudo-label quality.
- Report inference throughput or latency to help practitioners assess deployability.

## Novel Insights

None beyond the paper’s own contributions. The key insight—that a structured symbolic bottleneck (panoptic scene graph → triplets → text) improves both factuality and spatial grounding over end-to-end VLMs—is clearly demonstrated, though the evaluation bias tempers its immediate novelty until the human evaluation is confirmed.

## Suggestions

1. Perform a controlled human evaluation (e.g., pairwise preference between PG-VLM and a strong baseline, with annotators shown only the image) and report results in the main paper.
2. Clarify the NRDS formula and, if possible, show that NRDS correlates with human judgments of narrative–detection alignment.
3. Run the zero-shot experiment on a larger held-out set (e.g., 500 images from BDD100K) to increase statistical reliability.
4. Describe the prompt and few-shot examples used for the teacher LLM to enable reproduction and to clarify possible information leakage.

## Score and Decision

Score: 6

Decision: Accept

**Rationale:** The paper presents a well-motivated architecture that directly addresses central problems (spatial grounding, hallucination) in detailed captioning. The empirical results are strong, even after discounting for the evaluation bias, because hallucination and entity-grounding metrics are less affected by pseudo-label alignment. The novel NRDS metric, once clarified and validated, could be a useful addition to the evaluation toolbox. The main reservation (potential unfair comparison) could be resolved by human evaluation; if the human evaluation in the appendix supports the automatic results, the paper would be a clear accept. At the current state, it is a borderline accept with an expectation that the authors address the bias concern.

MY FINAL SCORE: <score>6</score>
MY FINAL DECISION: <decision>Accept</decision>