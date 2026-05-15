Now I have a thorough understanding of the paper and can evaluate all claims. Let me produce the final consolidated review.

---

## Summary

This paper proposes KEEP, a two-stage prompting framework for vision-language models (e.g., CLIP) that (1) creates image-wise fine-grained knowledge-enhanced prompts by retrieving domain-specific content via RAG and domain-specific foundation models (e.g., KAD, BiomedCLIP for medical; MiniGPT-4/GPT-4 for natural images), and (2) learns to align images with these knowledge-enhanced prompts through an image-prompt attention module with matching contrastive and classification losses. The method is evaluated on 8 datasets spanning medical (dermoscopic, X-ray, MRI) and natural (objects, flowers, aircraft, textures) domains, reporting average relative gains of ~3.2% on medical and ~2.6% on natural image tasks over existing prompt learning methods, alongside qualitative and quantitative explainability analyses.

## Strengths

- **Novel integration of RAG and domain-specific FMs for image-wise knowledge in prompt learning.** The paper is, to the best of this reviewer's knowledge, the first to incorporate retrieval-augmented generation plus domain-specific foundation models to produce image-level fine-grained knowledge (not just class-level) for prompting VLMs across diverse domains (Abstract, Section 2.3). This is a principled direction that addresses a real gap in prior prompt-learning work.

- **Consistent and substantial accuracy improvements over strong baselines.** On 4 medical datasets (Table 1) and 4 natural image datasets (Table 2), KEEP outperforms 8 state-of-the-art methods (CoOp, CoCoOp, Tip-Adapter, KgCoOp, LASP, GraphAdapter, TCP) with average relative gains of ~3.2% and ~2.6% respectively. The gains are consistent across all datasets, not cherry-picked.

- **Demonstrated data efficiency.** Under reduced training data (10%/50% of medical training labels, Table 3) and few-shot settings (1–16 shots on natural images, Figure 3), KEEP shows significantly smaller performance degradation than baselines. For example, on CCBTM, LASP drops from 91.5% to 82.7% when training data goes from 50% to 10%, while KEEP only drops from 94.9% to 92.0%. This is a practically important result.

- **Ablation study validates the training components.** Table 4 shows that removing the IPA logit, IPM loss, or CLS loss all cause noticeable performance drops (e.g., average medical accuracy drops from 92.6% to 90.2% without logit fusion), confirming that the attention-based learning framework contributes beyond just the knowledge content.

- **Flexible application across modalities.** The framework handles dermoscopic, X-ray, MRI, and natural images by plugging in appropriate domain-specific FMs and RAG sources (Section 3.2), and is demonstrated on datasets both with and without existing knowledge annotations (Derm7pt uses annotated concepts; other datasets use FM-predicted concepts).

## Weaknesses

### Fatal
None.

### Major

- **The knowledge creation pipeline itself is not ablated, so the contribution of each component in that pipeline is unidentifiable.** Table 4 ablates only training-stage components (IPA logit, IPM loss, CLS loss). The knowledge creation stage — whether RAG is used, which FM generates concepts (KAD vs. BiomedCLIP vs. a simpler captioner), how concepts are filtered — is never varied. Since the knowledge content is the most novel aspect of the approach, the paper cannot rule out that most gains come from the particular choice of knowledge source rather than the KEEP learning framework. An experiment such as "KEEP with RAG vs. KEEP without RAG" or "KEEP with a weaker FM" would substantially strengthen attribution of the results.

### Minor

- **The faithfulness evaluation is a useful sanity check but falls short of the rigorous XAI evaluation implied by the paper's title and framing.** The knowledge intervention test (Figure 4) shows that replacing good knowledge with random, general, or intervened knowledge degrades performance. This confirms the knowledge is being used, but it does not measure whether the model's *decision process* is faithfully captured by the explanation — e.g., whether high-attended concepts are causally necessary for the model's predictions. No quantitative interpretability metrics (e.g., concept-deletion AUC, insertion/deletion scores, correlation with human-annotated concepts) are reported. The "Explainable" title sets an expectation for more than qualitative attention maps and a degradation test.

- **Potential data leakage from domain-specific FMs is not discussed.** The paper uses KAD and BiomedCLIP to predict the presence of clinical concepts in each test image (Section 3.2). If these FMs were pre-trained on data that overlaps with the evaluation sets (a known issue in medical benchmarks), the knowledge-enhanced prompts could encode test-set information, inflating KEEP's results while leaving baselines unaffected. The paper does not discuss this risk or take steps to verify lack of overlap.

- **The "w/o knowledge" row in Table 4 is not clearly described in the text.** The ablation text (lines 133–137) only describes ablations of the IPA logit, IPM loss, and CLS loss. If "w/o knowledge" appears in the table as an additional ablation, its setup (e.g., does it use standard CLIP prompts? Are the knowledge-generated prompts simply discarded?) should be explained in the text to make the ablation meaningful.

### Trivial

- Algorithm 1 (referenced in Section 3.2 for clinical concept generation) is not present in the main paper body. The description in prose is reasonable, but a visual pseudocode would aid reproducibility.

- The claim of being "the first work to incorporate RAG and domain-specific FMs for prompt learning" (Abstract, Section 2.3) is plausible but somewhat undermined by the lack of comparison to knowledge-based baselines that use different knowledge sources (e.g., KgCoOp, LASP are cited as using class-level knowledge, but no direct comparison with an oracle-knowledge variant of these methods is provided).

## Nice-to-Haves

- **Ablate the knowledge creation pipeline.** Vary the knowledge source systematically: e.g., KEEP with RAG vs. without RAG, KEEP using GPT-4 vs. a simpler captioner for natural images, KEEP using a general FM (CLIP zero-shot) vs. a domain-specific FM for medical concepts. This would establish which component of the pipeline drives the gains.

- **Provide quantitative interpretability metrics.** Concept-deletion AUC or insertion/deletion scores over the learned attention weights would substantially strengthen the XAI claims.

- **Check for data leakage.** Verify whether KAD/BiomedCLIP training data overlaps with the test sets used (Pneumonia, Open-i, CCBTM). If overlap exists, rerun the knowledge-creation step with those images excluded.

- **Give baselines access to the same knowledge-enhanced prompts.** To isolate the contribution of the attention module and losses from the knowledge content, run CoOp or CoCoOp with the same knowledge-enhanced prompts (without the KEEP attention mechanism) and compare to full KEEP.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Unfair baseline comparisons that invalidate the headline results" (Harsh Critic's Point 1).** This criticism claims the entire evaluation protocol is "fundamentally biased" because KEEP's knowledge sources are not shared with baselines. This is a misunderstanding: KEEP's contribution is the complete system (knowledge creation + attention-based learning). Comparing against standard prompt-learning methods that use generic prompts is standard practice. The paper *does* include a "w/o knowledge" ablation (Table 4), which partially addresses the concern about whether knowledge itself drives gains. The criticism as framed is overblown and does not invalidate the paper's results. The legitimate ablation concern (varying the knowledge source) is captured separately above.

- **Generic formatting/style complaints and speculation about missing appendices.** Removed per hard rules.

- **"Breadth of evaluation" strength from Strength Finder** — kept, but not included as a separate bullet since it's subsumed under the "flexible application" strength.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a genuine tension: the paper's core novelty lies in the knowledge creation pipeline, yet the experimental design does not ablate that pipeline. This means the community cannot cleanly attribute the reported gains to the knowledge content versus the attention-based learning framework. Addressing this would significantly strengthen the paper's contribution claims.

## Suggestions

1. **Add a knowledge-source ablation study.** The single most impactful addition would be to vary the knowledge creation method (e.g., with/without RAG, different FMs, different concept sets) while keeping the KEEP learning framework fixed. This would cleanly separate the contribution of the knowledge content from the learning architecture.

2. **Add quantitative XAI metrics.** Supplement the faithfulness degradation test and qualitative attention maps with standard metrics (e.g., concept-deletion AUC, correlation with human-annotated concepts) to substantiate the "Explainable" claim.

3. **Discuss data leakage risk.** Acknowledge the potential overlap between domain-specific FMs' pre-training data and the evaluation sets, and either verify no overlap or note it as a limitation.

4. **Clarify the "w/o knowledge" ablation in the text.** Describe exactly what this condition means and how it was implemented so readers can interpret the ablation properly.

## Score and Decision

The paper proposes a well-motivated framework with a novel integration of ideas, demonstrates consistent gains across 8 datasets, and provides a reasonable initial set of analyses. The weaknesses are real but addressable: the knowledge pipeline should be ablated, the XAI evaluation should be deepened, and the data leakage concern should be discussed. These do not invalidate the core contribution but do prevent the paper from being accepted in its current form without these additions. The paper would be significantly strengthened by the suggested ablations and could become a strong accept after revision.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>