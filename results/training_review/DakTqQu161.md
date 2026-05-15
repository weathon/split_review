Now I have enough information to write the final consolidated review. Let me carefully synthesize everything.

**Verification of harsh critic claims against the paper:**

1. **Point 1 (Strawman baselines):** The paper (line 13, line 31) discusses ColPali and DSE as concurrent work, acknowledging their existence, and criticizes their limitations. However, the experimental section (line 106) only compares against Entity/Summary, Text-document, and Single-image baselines. No comparison to ColPali or DSE. This is a valid weakness — the paper both cites these methods as relevant and criticizes them, making their omission from experiments conspicuous.

2. **Point 2 (Multimodal contribution not isolated):** The paper (line 103) states LLaVA-NeXT-Interleave is the basis VLM. The baselines section (line 106) doesn't specify what backbone the "Text-document" baseline uses. The paper shows gains on text-only queries (4.3% on Encyclopedic-VQA, 1.3% on ViQuAE — line 126). This partially addresses the concern but doesn't fully resolve it.

3. **Point 3 (Tables as HTML):** Confirmed. Line 53: "tables do not have a specific representation layer... we treat HTML-format table data as a linearized sequence of HTML words." Line 137: "Zero-shot reranker performs similarly to a random selection... Finetuned reranker... still misclassifies nearly half of the tables." The paper acknowledges this openly.

4. **Point 4 (Passage-level comparison):** Line 120: The passage retriever uses the same VLM backbone trained on sections. The comparison is within-model (document-level vs. passage-level). The critic's demand for DPR/ColBERT-v2 is scope creep.

Now let me write the review.

## Summary

This paper proposes a framework (IDRIS) that uses vision-language models (VLMs) to represent documents containing interleaved text, images, and tables in a unified token sequence for information retrieval. The method segments long documents into sections, encodes each using a VLM with a special `[EoS]` token, averages section embeddings into a single document representation, and adds a reranker for fine-grained section identification. Experiments on four datasets (Encyclopedic-VQA, InfoSeek, ViQuAE, Open-WikiTable) show improvements over text-only and single-image baselines.

## Strengths

- **Holistic document-level retrieval beats passage-level retrieval with the same backbone**: The paper cleanly demonstrates (Table 2 area) that document retriever + reranker achieves 22.7% higher R@1 over passage retrieval using the same VLM backbone, even with 8× fewer candidates fed to the reranker. This is a clean within-model ablation that supports the core claim that maintaining document context matters.

- **Thorough ablation studies**: The paper systematically analyzes number of sections (Figure 1), negative sampling strategies (Table on hard negatives — in-document negatives are best), reranker training objectives (Section+BCE > Contrastive > Document+BCE), and dataset-size sensitivity (Figure 5). These provide actionable insights for future work and are the strongest part of the evaluation.

- **Honest failure analysis on tabular retrieval**: The paper explicitly reports that the zero-shot reranker performs near-random on table section identification and that the finetuned reranker still misclassifies ~half of tables. This rare scientific candor provides a clear direction for follow-up work and correctly identifies that HTML-linearized tables behave differently from text despite both being token sequences.

- **Cross-dataset and cross-modality evaluation**: Experiments span four datasets and both multimodal and text-only queries, showing that the interleaved representation benefits multimodal retrieval substantially (e.g., 50% R@1 gain on InfoSeek) and text-only retrieval modestly (1.3–4.3% R@1 gains).

## Weaknesses

### Fatal
None.

### Major

- **Missing empirical comparison to existing multimodal document retrieval methods (ColPali, DSE)**: The paper cites ColPali and DSE in both the introduction (line 13) and related work (line 31), discusses their limitations at length, but never includes them as baselines. The paper claims its approach "substantially outperforms relevant baselines," yet omits the most directly relevant prior work that also handles multimodal documents. This is especially conspicuous because the paper criticizes these methods on efficiency and representation quality grounds without backing those criticisms with experiments. The authors should either add comparisons on at least one shared dataset or clearly scope the paper's contribution as orthogonal to screenshot-based methods and explain why a fair comparison is infeasible.

- **The contribution of multimodal content vs. stronger backbone is not cleanly isolated**: The paper does not specify what model or architecture the "Text-document" baseline uses. Since the proposed method uses LLaVA-NeXT-Interleave (0.5B), a modern VLM, it is unclear whether the gains come from the VLM's superior text encoding capacity or from the visual information specifically. A controlled ablation — the same VLM backbone processing the same document with and without images — would resolve this. The text-only query results (1.3–4.3% gains) provide partial evidence that multimodal content helps even when the query has no images, but this does not fully substitute for a direct text-only vs. multimodal ablation of the encoder itself.

### Minor

- **Tables are handled as text tokens, not as a visual modality**: The method linearizes tables as HTML text (line 53), meaning the "table modality" is not actually processed through a visual pathway. This is conceptually inconsistent with the paper's framing of a unified multimodal representation. The poor results on Open-WikiTable (zero-shot reranker near random; finetuned reranker misclassifies ~50%) confirm that this representation choice is a genuine limitation. The paper is honest about this, but the framing of handling "text, images, and tables" as three modalities in a unified way overstates what is actually done.

- **The reranker operates on individual sections, not the full document**: The reranker (Section 3.3) concatenates the query with each section independently, meaning it cannot use document-level context to disambiguate similar sections. The paper acknowledges this (line 129: "rerankers assess query relevance using a single section, they may lack access to broader contextual information"), but this partially undermines the "holistic" framing. The Document+BCE variant tried to address this but underperformed due to training/evaluation mismatch.

- **Image preprocessing ("four-into-one" merging) is not analyzed**: Four images are combined into one by scaling each to half its original dimensions (line 103). No ablation measures whether this degrades retrieval quality compared to processing images individually, making it hard to assess whether this efficiency trade-off comes at a performance cost.

- **Very small gains on text-only queries**: Improvements on text-only queries are modest (1.3% R@1 on ViQuAE, 4.3% on Encyclopedic-VQA). This tempers the claim that multimodal content "significantly enhances" retrieval — the benefit is large for multimodal queries but small for text-only queries.

### Trivial

- The reranker's design (query + section concatenation with BCE) is standard and similar to existing cross-encoder rerankers; the methodological novelty lies more in the overall pipeline than in the reranker itself.

## Nice-to-Haves

- A comparison to a state-of-the-art passage-level retriever (e.g., DPR, ColBERT-v2) for the document vs. passage analysis would strengthen the claim that "holistic document context matters." Currently the passage retriever uses the same VLM backbone, so the comparison is fair for within-model assessment but does not situate the approach against established passage retrieval methods.
- Reporting variance across multiple seeds or bootstrap confidence intervals would help assess the reliability of the reported gains.
- A retrieval case study showing a concrete example where the interleaved format succeeds and text-only fails would improve reader understanding.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. *"Weakness about lack of comparison to DPR/ColBERT-v2 for passage retrieval"* — This is scope creep. The paper's document-vs-passage comparison is a within-model ablation designed to show that holistic document context helps when using the same backbone. Demanding comparisons to entirely different passage retrieval systems addresses a different question than the one the experiment is designed to answer.

2. *"Criticism that the paper's introduction 'overstates' that existing methods consider only text"* — The paper explicitly acknowledges ColPali/DSE in line 13, so the framing is accurate concerning the approaches it primarily targets (dense text retrieval).

3. *"Criticism about averaging as pooling without justification"* — While alternative pooling could be explored, this is a standard approach that is simple and effective; the critic provides no evidence that other pooling methods would change results.

4. *"Several formatting/style nitpicks from the harsh critic"* — These are parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the key tension: the paper's experimental design is internally consistent (proposed method vs. text-only baselines using the same general architecture) but lacks external positioning against the concurrent screenshot-based multimodal document retrieval methods it criticizes. The most insightful observation across the reviews is that the paper's tabular retrieval failure is not just a "challenge" to be noted but reveals a structural limitation of equating HTML-linearized tables with true multimodal understanding — an insight the paper partially makes but does not fully reckon with.

## Suggestions

1. **Add a controlled ablation**: Run the proposed VLM encoder on documents with and without images (strip visual tokens) while keeping all other training details identical. This directly isolations the contribution of multimodal content from model capacity.

2. **Compare against at least one screenshot-based method** (ColPali or DSE) on Encyclopedic-VQA. Even a single benchmark comparison would significantly strengthen the positioning. If infeasible, clearly explain why (e.g., different document formats, incompatible tokenization) and scope the contribution accordingly.

3. **Ablate the image merging preprocessing**: Compare retrieval performance with and without the "four-into-one" merging on a subset to quantify any quality degradation.

4. **Clarify baseline specifications**: Explicitly state what model architecture the Text-document and Single-image baselines use. If they use the same VLM backbone with text-only / first-image-only inputs, say so; if they use a different model, justify the choice.

5. **Consider rendering tables as images** rather than HTML text, which would allow the VLM's visual encoder to process their structure, potentially addressing the tabular retrieval weakness.

## Score and Decision

The paper tackles a timely and well-motivated problem with a sensible approach. The ablations are thorough and the failure analysis on tables is commendable. However, the evaluation has two significant gaps: (1) the empirical positioning against existing multimodal document retrieval approaches (ColPali, DSE) that the paper itself discusses and criticizes is absent, and (2) the contribution of multimodal content is not cleanly isolated from the VLM backbone's text encoding capacity. These weaknesses are real but addressable — they weaken but do not invalidate the core contribution. The paper would benefit from a major revision adding the suggested experiments.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>