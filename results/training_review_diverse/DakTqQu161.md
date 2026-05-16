Now I have a thorough understanding of the paper and have verified all claims against the source text. Let me produce the final consolidated review.

## Summary

This paper proposes using Vision-Language Models (VLMs) to represent documents in an interleaved multimodal format (text, images, and tables) for information retrieval. The method segments long documents into sections, encodes each section with a VLM, averages section representations into a document-level embedding, and uses a reranker for fine-grained section identification. Experiments on four datasets show improvements over text-only and single-image baselines, and a within-method ablation demonstrates that document-level retrieval with reranking outperforms passage-level retrieval by 22.7% R@1.

## Strengths

- **Document-level representation with reranking cleanly outperforms passage-level retrieval.** The paper provides a direct within-method comparison: document-level retrieval + reranker beats passage-level retrieval by 22.7% R@1 and 29.2% MRR@10, even while providing eight times fewer retrieval units to the reranker (Section 4.3, Table "Document vs. Passage R@1"). This is a well-controlled comparison that is not affected by baseline selection concerns and validates a core claim of the paper.

- **First systematic use of interleaved VLM token sequences for holistic document IR.** Unlike screenshot-based methods (ColPali, DSE) that encode full pages as images — fragmenting content and imposing large memory costs — this paper processes text, images, and tables as interleaved tokens within a single VLM context window, preserving cross-modal relationships. The approach is novel and well-motivated relative to the limitations it identifies in prior work.

- **Informative ablations on reranker design and negative sampling.** The ablation of negative sampling strategies (in-document, top-K, in-batch) shows that in-document negatives provide a natural, cost-effective advantage (Section 4.6, Table "Hard Negative Ablation"). The comparison of BCE vs. contrastive vs. Document+BCE reranker designs (Section 4.6, Table "Reranker Design") provides practical design guidance.

- **Honest characterization of tabular retrieval challenges.** The paper identifies that tabular retrieval remains difficult even with interleaved representations (Section 4.4, Tables 4a–4c), acknowledging that zero-shot table retrieval performs poorly and that fine-tuned rerankers still misclassify nearly half of tables due to high within-document table similarity. This provides a concrete frontier for future work.

- **Data scaling analysis revealing modality-specific data needs.** The analysis shows that multimodal query retrieval requires roughly twice as many training samples as text-only retrieval to reach near-optimal performance (Figure 5), offering practical guidance for dataset construction.

## Weaknesses

### Fatal
None.

### Major

- **Baselines are too weak and underspecified to support the paper's headline claims.** The "Text-document retriever" is never defined: is it the same VLM architecture stripped of visual tokens? A separate text-only encoder like DPR or REPLlama? Without this detail, a 64% R@1 improvement over "Text-document" cannot be interpreted — it may simply show that adding visual information helps, not that the proposed interleaved representation is superior to reasonable alternatives. The "Single-image" baseline (first image only) is trivially weak. More importantly, the paper explicitly critiques concurrent screenshot-based methods (ColPali, DSE) for memory and fragmentation issues but **does not include them as baselines**. The paper's own introduction argues these are the natural competitors; omitting them leaves the central claim — that interleaved VLM token sequences are superior — experimentally unsubstantiated against the most directly comparable alternatives.

- **Missing training hyperparameters hinder reproducibility.** The paper reports the VLM architecture (LLaVA-NeXT-Interleave 0.5B) and LoRA, but does not report batch size, learning rate, number of training epochs, exact LoRA rank/alpha, or the negative sampling strategy for the *retriever*'s contrastive loss. The retriever negative sampling is particularly important because the contrastive formulation (Eq. 1) uses only in-batch negatives. Since the paper's analysis of negative sampling strategies is limited to the reranker, the retriever's training details are incomplete.

### Minor

- **No analysis of training-inference section-count mismatch for the retriever.** The retriever is trained with exactly four sections per document but at inference averages over all sections (potentially many more). The paper studies varying section count *during training* (Section 4.6, Figure "Number of Sections"), which is a different question. Whether averaging more sections at inference dilutes or improves document representations is untested. This does not invalidate results but weakens the claim about "maintaining document coherence."

- **Section averaging is used without ablation against alternatives.** The document representation is a simple uniform average of section embeddings (Eq. 2). No comparison is made against learned pooling, attention-weighted combination, concatenation with projection, or a hierarchical encoder. Given that the paper argues prior methods "lose context" through fragmentation, the averaging choice is conspicuously naive and its impact on the reported results is unknown.

- **No statistical significance reported.** For several comparisons the gains are modest (e.g., +1.3% R@1 on ViQuAE textual queries, +4.2% R@1 on Encyclopedic-VQA section retrieval). Without confidence intervals or significance tests, the reader cannot assess whether these small improvements are reliable or within noise.

- **"Too many samples degrade retrieval performance" is observed but not explained.** The paper notes that beyond a certain point, adding more training samples hurts retrieval performance (Figure 4_num_samples) and speculates about overfitting, but provides no analysis (training loss curves, validation behavior). This weakens an otherwise useful data-efficiency finding.

- **No inference time or memory comparison against baselines.** The paper criticizes screenshot-based methods for high memory usage (citing 2TB for Wikipedia) but reports no quantitative comparison of its own inference cost or memory footprint relative to any baseline.

### Trivial

- The baseline descriptions in Section 4.2 are too brief — "Entity and Summary baselines" are not explained (what exactly are they trained on?).

- The discussion of table handling in the method section could briefly note why HTML-linearized tables remain difficult (this is deferred entirely to the experiments section).

## Nice-to-Haves

- **Compare against at least one concurrent multimodal retrieval method** (ColPali, DSE, or a standard dual-encoder fusing CLIP + text encoder) to ground the claim that interleaved token sequences are superior to screenshot-based or separately fused representations. This is the single change that would most strengthen the paper.

- **Ablate the section-averaging step** against learned pooling or hierarchical encoding to support the claim that the averaging procedure preserves context.

- **Analyze the training-inference mismatch** by reporting retrieval performance as a function of inference-time section count, keeping training fixed at 4 sections.

- **Report statistical significance** (e.g., bootstrap confidence intervals) for the key comparisons, especially where gains are small.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Introduction dismisses concurrent approaches without quantitative comparison later"** — This is largely the same as the baseline weakness already listed as Major. Redundant.

- **"Table handling not discussed in method section"** — The method section does discuss table handling (HTML tokenization via the word embedding layer, Section 3.1). The difficulty is analyzed in experiments. The point to add a few sentences of explanation is a nice-to-have, not a weakness.

- **"No error analysis for cases where interleaved format hurts"** — The paper does discuss this indirectly via data-scaling analysis (ViQuAE's small size explains its modest textual query gains). The specific request for error analysis is a reasonable suggestion but not a necessary condition for acceptance.

- **"Document+BCE training-inference mismatch should be controlled for"** — The paper already acknowledges this limitation and provides a clear explanation. The suggestion to train with full documents is a natural extension but does not reflect a flaw in the current design.

## Novel Insights

The reviews surface a tension that the paper itself does not fully engage with: the claim that interleaved VLM representations are superior to screenshot-based methods (ColPali, DSE) is argued theoretically (memory, fragmentation) but never tested empirically. The paper's strongest experimental contribution — that document-level representation + reranking beats passage-level retrieval — is orthogonal to this modality question and stands on its own. The reviews collectively suggest that the paper is telling two stories (multimodal representation format + document-level retrieval) but only rigorously supports one of them.

## Suggestions

1. **Define the Text-document baseline precisely** and, ideally, add a stronger multimodal baseline (ColPali or a CLIP + text-encoder fusion). Without this, the paper's central experimental claim cannot be evaluated against the methods it critiques.
2. **Report all training hyperparameters** (batch size, learning rate, epochs, LoRA configuration, retriever negative sampling) to meet basic reproducibility standards.
3. **Ablate the section-averaging step** (e.g., compare against attention-pooled section embeddings) to justify the design choice that underlies document coherence.
4. **Analyze the inference-time section-count mismatch** for the retriever, or at minimum discuss why averaging more sections is expected to be benign.

## Score and Decision

**Originality:** 6/10 — First use of interleaved VLM tokens for document IR is novel, but the technical building blocks (VLM, contrastive learning, reranking) are all standard.  
**Importance of research question:** 7/10 — Multimodal document retrieval is a timely and practically important problem.  
**Claims well-supported:** 4/10 — The document-level vs. passage-level comparison is well-supported, but the headline claim of "substantially outperforms" is undermined by weak baselines.  
**Soundness of experiments:** 5/10 — Reasonable experimental scope but missing critical baselines and some methodological controls.  
**Clarity of writing:** 6/10 — Clear motivation and method description, but baseline descriptions are too sparse.  
**Value to the community:** 5/10 — The document-level retrieval finding and reranker ablations are useful, but the paper's full value depends on stronger comparisons.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>