Now I have all the information I need. Let me compose the consolidated review by carefully cross-referencing each claim against the actual paper.

---

## Summary

This paper proposes TNT, a multi-modal framework that treats tabular data as a distinct modality alongside text. TNT uses a dedicated Table Encoder with bi-dimensional attention to produce structure-enriched column embeddings, which are aligned with an LLM via a Table-Language Adaptor with learnable queries. A three-stage training pipeline (encoder pre-training with column-wise contrastive learning on 86k tables → multi-task feature alignment on 292k table-language samples → instruction tuning on SPIDER) is introduced. Experiments on NL2SQL (SPIDER and its variants) show consistent improvements, with up to 14.4% higher execution accuracy on datasets with non-semantic column names.

## Strengths

- **Novel multi-modal table representation with clear architectural motivation**: The paper identifies a genuine problem — LLMs are brittle to table serialization and lack structure-aware reasoning — and proposes a principled solution: a Table Encoder with bi-dimensional attention (row-then-column) that produces column-level embeddings, paired with an Adaptor using learnable queries. This mirrors successful VLM design patterns (e.g., Q-Former) adapted for tabular data. (Sections 3, 4.1)

- **Strong empirical results on a challenging stress test**: TNT achieves up to 14.4% higher execution accuracy on SPIDER variants with 80% anonymized column names compared to text-serialization baselines (Table 1), and the gap persists (0.3–3.6% EX) even on standard benchmarks with semantic schemas (Table 2). The non-semantic column name stress test is a clever and revealing evaluation design.

- **Ablation studies confirm each training stage contributes**: Table 3 shows that removing any single training stage (encoder pre-training, feature alignment, or instruction tuning) causes a substantial performance drop (up to −23.4%), and the loss curves in Figure 5 support the claim that pre-training prevents shortcut exploitation during alignment.

- **Column embeddings are shown to be more than soft prompts**: Table 4 compares TNT against soft prompts with the same parameter budget, finding that soft prompts do not yield comparable gains. This helps rule out the possibility that the improvement is simply from adding learnable parameters.

- **Token efficiency demonstrated**: Table 5 shows TNT with just one example value achieves its best performance, while text-only baselines degrade with more values — supporting the claim that column embeddings provide a more compact and semantically informative representation.

- **Compatibility with existing techniques**: Table 6 shows TNT integrates well with Schema Filtering, Code Correction, and Self-Consistency, approaching GPT-4-level results with an 8B backbone.

## Weaknesses

### Fatal
None.

### Major

1. **The main comparison confounds representation design with additional training data and capacity.** TNT benefits from (a) encoder pre-training on 86k tables, (b) multi-task feature alignment on 292k samples, (c) an Adaptor module with learnable queries, and (d) the bi-dimensional attention mechanism. The text-serialization baselines receive none of these — they are only instruction-tuned on SPIDER. While this is the standard comparison paradigm in multi-modal LLM research (VLMs also compare their full pipeline against text-only baselines), the paper attributes its gains specifically to "structure-enriched semantics in column embeddings" (Section 6.2). The ablation studies (Tables 3, 4) partially address this concern by showing that each component helps and that column embeddings outperform soft prompts, but the missing controlled comparison — training a baseline that compresses *text-serialized* tables into column-level tokens using the same pre-training and alignment data — means the central claim that TNT's *structure-awareness* (rather than its additional training/capacity) drives the improvement remains incompletely isolated. (Tables 1–3, Section 6.2)

2. **Evaluation on a single task limits the generality of the claimed contribution.** The paper's title, abstract, and framing position TNT as a general solution for "bridging the semantic gap between text and table" and enabling "abstract structure-enriched semantics from tabular data." However, all experiments are conducted exclusively on NL2SQL (SPIDER and its perturbations). While NL2SQL is an important and challenging table understanding task, the paper does not evaluate on table question answering (e.g., WikiTableQuestions, TabFact), table fact verification, or any other table reasoning benchmark. The paper acknowledges this scope on line 27 ("For better clarity, we will focus on the NL2SQL task") and the conclusion ("Extensive experiments on the NL2SQL task"), but the title and broader claims suggest a generality that the evidence does not yet support. (Abstract, Sections 1, 5, 6, 8)

### Minor

1. **Sensitivity to cell value selection (the paper's own motivating experiment) is never tested for TNT.** Figure 1 compellingly demonstrates that LLMs are highly sensitive to *which* cell values are serialized into the prompt, motivating the need for better table representations. However, the paper never evaluates TNT on this exact setup — i.e., feeding TNT different *sets* of cell values and measuring variance in outputs. Table 5 tests different *numbers* of values (1, 3, 5), but this does not replicate the variance-over-different-sets experiment from Figure 1. This is a direct gap between the paper's motivation and its evaluation. (Figure 1 vs. Table 5, Section 6.4)

2. **No error bars or statistical significance reported.** With 10k+ questions in SPIDER, even small differences could be meaningful or not. Reporting single-run results without variance estimates (even via bootstrapping) reduces confidence in the reported gains, especially for the smaller improvements on standard benchmarks (e.g., 0.3–2.6% EX on SPIDER-Dev for LLAMA3 in Table 2). (Tables 1–6)

3. **The soft prompt baseline is not given the same pre-training/alignment data.** Table 4 compares TNT against soft prompts trained only during instruction tuning. A stronger control would train soft prompts on the same multi-task alignment data with access to the 86k table corpus. As designed, the experiment cannot fully rule out that TNT's advantage comes from additional pre-training rather than from column embeddings being "truly tied to table semantics." The paper acknowledges this partially (describing the experiment as addressing whether embeddings "function merely as soft prompts rather than being truly tied to table semantics"), but the control is weaker than it could be. (Section 6.3, Table 4)

4. **Limited details on the 86k business table dataset.** The 86,046-table corpus is a key resource for pre-training, but the paper provides minimal information about its collection, composition, deduplication, missing-value handling, or domain distribution beyond a brief mention of "finance, education, and medicine." The release status is stated as "included in the supplementary materials" (Reproducibility Statement), but dataset documentation and quality analysis would strengthen reproducibility. (Section 4)

5. **Token efficiency is claimed but never measured.** One of the three identified limitations of text-based serialization is "redundancy" / token inefficiency (Section 1), and TNT's column embeddings are claimed to be more token-efficient (Section 6.4). However, the paper never reports actual token counts, prompt length comparisons, or computational cost measurements. Table 5 provides indirect evidence (TNT with 1 value outperforms text with more values), but direct measurement would be more informative. (Sections 1, 6.4)

### Trivial

- Section 5 makes an unsupported claim that prior embedding methods "typically impose high requirements on table curation" without providing evidence or citations to substantiate this.
- The "Dynamic Context Integration" description (Section 3) is somewhat underspecified — the hybrid prompt template is referenced but the exact format is deferred to figures and citations, making the presentation slightly harder to follow in the main text.

## Nice-to-Haves

- A controlled comparison where a learned compressor (trained on the same 86k tables and alignment data) compresses *text-serialized* tables into column-level tokens, to isolate whether the bi-dimensional attention mechanism specifically is beneficial.
- Evaluation on a second table understanding task (e.g., WikiTableQuestions or TabFact) to support the claim of general table understanding.
- A full curve of anonymization rates (0% to 100%) for the non-semantic column name experiments, rather than the single 80% rate.
- Replication of the Figure 1 sensitivity experiment with TNT (different sets of cell values → variance) to directly demonstrate that column embeddings reduce sensitivity.
- Heatmaps or visualizations of the bi-dimensional attention patterns to demonstrate structural awareness.

## Removed Points

The following points from the reviews were removed with justification:

- **"Dynamic context integration section appears truncated"**: The section provides a clear description of the hybrid representation; the actual prompt template format is likely in a figure, and the content given (columns embeddings + textual column names/foreign keys) is sufficient for understanding.
- **Dataset release questioned**: The paper states all resources are in supplementary materials (Reproducibility Statement). The critic's concern about "whether it will be released" is unfounded.
- **"The 86k corpus is modest given that many table corpora contain millions of tables"**: This is a subjective comparison without context; the corpus size is reasonable for a multi-stage training pipeline and the paper doesn't claim state-of-the-art scale.
- **Several formatting/style nitpicks** (garbled line numbering in the PDF-extracted text, which are parser artifacts).
- **Generic strength from Strength Finder** ("the paper identifies a real and well-documented problem") — dropped because it's generic and not specific to this paper's contribution.

## Novel Insights

The reviews reveal an interesting tension: the paper adopts the standard evaluation paradigm of multi-modal LLM research (compare full pipeline against text-only baselines), but its claim is more specific — that *structure-aware encoding* (not just additional pre-training or capacity) is the source of improvement. The missing controlled comparison (compressing text-serialized tables with the same pre-training data) is a deeper methodological question about how to properly isolate modality-specific architectural contributions in multi-modal systems. This issue is not unique to this paper and would benefit from community-wide attention.

## Suggestions

1. **For the current paper**: Strengthen the central claim by either (a) training a text-compression baseline on the same 86k tables and alignment data, or (b) explicitly reframing the contribution as demonstrating the *overall effectiveness* of a multi-modal table encoding pipeline (rather than isolating structure-awareness per se). Also add error bars and a direct sensitivity analysis (varying sets of cell values following Figure 1's setup).

2. **For future work**: Extend evaluation to additional table understanding tasks (Table QA, fact verification). Release the 86k table dataset with documentation. Provide direct token efficiency measurements and attention visualizations.

## Score and Decision

This paper addresses a meaningful problem (LLMs' fragile understanding of tabular data) with a plausible and well-motivated architectural solution. The architectural design choices (bi-dimensional attention, column-wise contrastive learning, Adaptor with learnable queries) are thoughtful and the multi-stage training pipeline is validated through ablation. The non-semantic column name stress test is a creative evaluation that produces compelling results. However, the paper's central claim — that structure-aware encoding specifically drives improvements — is incompletely supported because the main comparison confounds representation design with additional training data and capacity. Additionally, claims of general table understanding are supported by only a single task (NL2SQL). These are significant limitations, but the paper still constitutes a solid contribution with clear positive results and thorough ablation. The paper would be strengthened by addressing these gaps but the core ideas and empirical findings have value.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>