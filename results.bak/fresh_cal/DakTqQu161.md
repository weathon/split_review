I have thoroughly analyzed the paper and all reviewer claims. Let me now compose the final consolidated review.

---

## Summary

This paper introduces IDIRS, a framework that leverages vision-language models (specifically LLaVA-NeXT-Interleave) to embed documents containing interleaved text, images, and tables into a unified representation for information retrieval. The method addresses two limitations of prior work: (1) ignoring multimodal content in documents by treating everything as text, and (2) fragmenting long documents into independent passages, losing holistic context. IDIRS merges passage-level embeddings into document-level representations and adds a reranker for fine-grained section identification. Experiments on four datasets (Encyclopedic-VQA, InfoSeek, ViQuAE, Open-WikiTable) show substantial gains over text-only and single-image baselines, and ablations validate the document-level merging and reranker design choices.

## Strengths

1. **Large and consistent empirical gains from interleaved multimodal representation.** On Encyclopedic-VQA with multimodal queries, the interleaved format achieves a 53.0% improvement in R@1 over the Text-document baseline and 25.0% over the Single-image baseline (Section 4.3, Table 1). These margins are substantial and hold across InfoSeek (50.0% R@1 gain) and ViQuAE (29.6% R@1 gain), providing strong evidence that incorporating images and tables into document embeddings meaningfully improves retrieval.

2. **Document-level merging of section embeddings clearly outperforms passage-level retrieval.** The document retriever + reranker pipeline achieves 22.7% higher R@1 and 29.2% higher MRR@10 over a passage-level retriever with the same reranker (Section 4.3, Table 2), despite the document retriever providing eight times fewer units to the reranker. This cleanly validates the claim that preserving document context through merged embeddings is superior to retrieving segmented passages.

3. **Reranker design choices are well-validated through ablation.** The "Section+BCE" reranker (query concatenated with each section individually, trained with BCE loss) outperforms both a contrastive-loss variant and a "Document+BCE" variant that concatenates multiple sections (Section 4.4, Table 5). This provides grounded evidence for the specific architectural and loss-function choices.

4. **Systematic analysis of the number of sections per document.** Figure 4 shows MRR@10 rising from 7.5 to 15.7 as sections increase from 1 to 8, alongside a clear GPU memory trade-off, leading to the principled choice of 4 sections (Section 4.4, paragraph 1). This practical insight guides deployment decisions.

5. **Honest analysis of tabular retrieval challenges.** The paper transparently reports that table retrieval remains difficult (Section 4.3, Table 4), with zero-shot retrievers achieving roughly half the R@1 of finetuned ones and rerankers struggling to distinguish similar tables within the same document. This credible self-assessment strengthens the paper's trustworthiness.

6. **Dataset size analysis reveals modality-specific data requirements.** Figure 5 shows that multimodal retrieval benefits from more data while textual retrieval plateaus earlier, and that rerankers need larger datasets than retrievers — an actionable finding for practitioners working with limited annotations.

## Weaknesses

### Fatal
None.

### Major

1. **No empirical comparison to concurrent multimodal document retrieval methods (ColPali, DSE) that the paper explicitly criticizes.** The introduction and related work (Sections 1 and 2) directly critique ColPali (Faysse et al., 2024) and DSE (Ma et al., 2024) for limitations including fragmentation, resolution constraints, and memory costs. Yet the experimental evaluation includes no comparison against these methods — the baselines are Entity, Summary, Text-document, and Single-image, all of which are simpler ablations rather than competing multimodal document retrieval systems. Since the paper positions itself as addressing the limitations of these concurrent approaches, the absence of any empirical head-to-head comparison means the central claim that "our approach substantially outperforms relevant baselines" is only supported against weak (mainly text-only) baselines. The contribution would be substantially strengthened by comparing against ColPali/DSE on a representative subset, or by providing a clear justification for why such comparison is infeasible.

### Minor

1. **Baseline specifications are too brief.** The four baselines (Entity, Summary, Text-document, Single-image) are each described in a single sentence (Section 4.2). It is not explicitly stated whether they share the same LLaVA-NeXT-Interleave backbone (which is confirmed for the retriever and reranker but not for baselines), nor whether the Text-document and Single-image baselines are simply the proposed method restricted to one modality. Without this detail, the 50–64% improvements — while large — are harder to interpret as cleanly isolating the multimodal contribution vs. reflecting possible configuration differences.

2. **Section embedding averaging is used without discussion of alternatives.** The document representation is a simple average of section embeddings (Section 3.2). While this works well empirically, the paper does not discuss potential alternatives (attention pooling, learned weighting, sequential modeling) or justify why averaging is sufficient despite losing section ordering and relative importance information.

3. **Computational cost discussion is partially incomplete.** The paper reports GPU memory trade-offs for the number of sections (Figure 4) and uses LoRA to reduce memory, but does not report inference-time metrics (latency, throughput) for either retrieval or reranking. Given that the paper criticizes DSE for its 2TB memory requirement for Wikipedia, reporting comparable resource figures for the proposed method would provide a fairer basis for the critique and aid practitioners in assessing deployability.

### Trivial
None.

## Nice-to-Haves

- **Qualitative examples**: A figure showing top-1 retrievals from the interleaved model vs. the text-only baseline for a few sample queries would help readers understand what multimodal content drives the improvements.
- **Table encoding ablation**: The paper treats tables as HTML words and acknowledges poor table retrieval performance (Section 4.3). Ablating alternative table encodings (e.g., markdown, structured JSON, or table-specific embeddings) could pinpoint whether the limitation is inherent to the task or due to the encoding choice.
- **Explicit test on the Document+BCE training-inference mismatch hypothesis**: The paper plausibly attributes Document+BCE underperformance to a mismatch in section count between training (4) and inference (8+). Training a variant with more sections to verify this would strengthen the analysis.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Open-WikiTable "conflates table detection with document retrieval"** — The paper transparently states (Section 4.1) that it "adapts this dataset, aiming at identifying the document or document section containing the target table." This is a straightforward and honest task adaptation; the criticism misunderstands the paper's scope. **Removed** (misunderstands paper).
- **"Section 4.3 framing is misleading"** — The paper compares against its stated baselines and says "our approach achieves the best performance" in that context. This is an accurate description of the table results; the paper does not claim SOTA against all methods. The underlying concern (missing concurrent methods) is already covered in Major weakness #1. **Removed** (duplicates Major #1; paper's framing is accurate for its stated baselines).
- **"Document+BCE explanation is plausible but not tested"** — The paper offers a clear hypothesis (training-inference mismatch in section count) and cites concurrent work on long-context LLMs. This is appropriately transparent for an analysis section; requiring every explanatory hypothesis to be experimentally verified is too stringent. **Removed** (overly demanding).
- **"Baselines are likely underpowered"** — This is a speculative claim. The Text-document baseline using the same VLM backbone but restricted to text is a reasonable ablation to isolate the multimodal benefit; there is no evidence in the paper that it is "underpowered." The actual issue (poor specification) is covered in Minor weakness #1. **Removed** (speculative).
- **Several generic "Strengthening the Paper on Its Own Terms" suggestions** — The suggestions to add qualitative analysis, compute cost, and table ablations are moved to Nice-to-Haves rather than presented as weaknesses. **Moved** to Nice-to-Haves.

## Novel Insights

The review surfaces an interesting tension: the paper's ablations are rigorous and internally consistent (document > passage, Section+BCE > alternatives, in-document negatives help), yet the overall evaluation stops short of engaging with the very methods it criticizes most sharply. This creates a situation where the paper convincingly demonstrates *that* interleaved multimodal representation beats text-only representation on the same backbone, but cannot answer *how much* this matters relative to the existing multimodal document retrieval paradigm (ColPali/DSE). The reviewer observations collectively suggest that the empirical contribution, while clearly positive, is incompletely scoped — the paper proves its internal design choices well but positions its external significance against a strawman (text-only retrieval) rather than the direct competitors it discusses.

## Suggestions

1. **Add a comparison against at least one concurrent multimodal document retrieval method** (ColPali, DSE, or similar) on a shared task, or provide an explicit justification (computational infeasibility, architectural incompatibility) for why such comparison is omitted. Even a single dataset comparison would substantially strengthen the paper's external validity.
2. **Specify the baselines fully**: state explicitly which baselines share the LLaVA-NeXT-Interleave backbone, what modalities each baseline sees, and how the "Text-document" and "Single-image" baselines are constructed relative to the full method.
3. **Report inference-time cost** (latency per query, total embedding time for a representative corpus) alongside the existing memory analysis to give a complete picture of practical deployability.

## Score and Decision

The paper makes a solid, well-motivated contribution — it demonstrates that using a VLM to create interleaved multimodal document representations substantially improves retrieval over text-only baselines, validates design choices (document-level merging, reranker architecture) through careful ablations, and honestly discusses remaining challenges (table retrieval, data requirements). The method is clearly presented and the experiments are well-designed for internal validation. The primary weakness is that the evaluation does not engage with the concurrent multimodal document retrieval methods (ColPali, DSE) that the paper itself criticizes, which limits the strength of the external claims. This is a significant gap but not a fatal one — the paper's core internal contribution (interleaved representation > unimodal representation) is well-supported. With the addition of concurrent comparisons (or a clear justification for their omission) and better baseline specification, this would be a strong paper.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>