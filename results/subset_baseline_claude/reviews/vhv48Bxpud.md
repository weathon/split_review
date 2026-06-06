## Summary

StructZip proposes a two-stage framework for compressing large structured prompts (tables, tool descriptions, classification schemas) into a single token via parametric memory. The "Structured Information Decoding" stage converts the structured data into QA pairs, and the "Description-based Knowledge Encoding" stage fine-tunes the LLM on these QA pairs mixed with general SFT data. A special compressed token (`<|data|>`) acts as the retrieval key at inference time. The method is evaluated on text classification, table QA (TableBench), and tool invocation (xLAM), where it reportedly achieves extreme compression with minimal performance degradation.

---

## Strengths

- **Well-motivated problem**: Structured prompt compression is an underexplored and practically relevant problem. The observation that JSON/schema-format prompts possess minimal lexical redundancy—making token-level compression harmful—is a valid and insightful diagnosis.
- **Comprehensive evaluation across diverse tasks**: The paper covers three structurally distinct task types spanning both Chinese and English data, providing breadth. Ablation studies (Section 5.2 on number of tokens; Section 5.4 on coverage and parallel corpora) are informative and strengthen understanding of design choices.
- **Strong empirical gains over baselines**: On all five datasets, StructZip clearly outperforms the four soft/hard compression baselines, and the latency measurements under VLLM add practical credibility.
- **Coverage ablation insight**: The finding that both full coverage of the structured data and parallel corpora (original prompt + compressed representation) are necessary is a useful empirical contribution.

---

## Weaknesses

### Fatal

1. **Test-set contamination**: For TableBench the paper states explicitly: *"we constructed table description corpora for all the tables used in the test set."* The model is fine-tuned on QA pairs derived directly from the test-set tables and is subsequently evaluated on queries about those same tables. This is direct information leakage, which invalidates the TableBench results entirely. The same concern applies to the tool-invocation setting, where all 30k+ tool descriptions in xLAM are used to construct the training corpus, and test queries draw from the same tool pool.

2. **Fundamentally unfair comparison with baselines**: All competing methods (LongLLMLingua, AutoCompressors, Gist, 500xCompressor) operate without task-specific fine-tuning on the test data. StructZip, by contrast, encodes test-time data directly into model parameters before evaluation. The comparison conflates inference-only compression with supervised memorization and is therefore not a valid apples-to-apples evaluation.

### Major

3. **The "compression" framing is misleading**: The paper bills this as reducing "millions of tokens to one," but the information is not eliminated—it is displaced into model weights via costly fine-tuning. The computational cost of constructing QA corpora and fine-tuning is never reported or compared against the inference savings. A practical system must amortize retraining cost over many queries; this analysis is absent.

4. **The method requires retraining for every new structured input**: Whenever a table, tool description, or label set changes, the model must be entirely retrained. This severely limits the method's utility compared to inference-time compression methods, which handle arbitrary inputs without retraining. The practical deployment scenario is never discussed.

5. **Inconsistent method naming**: Section 5.3 evaluates unstructured-text performance under the name **"LDPC"**, not StructZip. This suggests the paper may be assembled from multiple prior drafts. The method described there also differs from StructZip—it is applied to documents, uses a different evaluation setting, and the connection to the core StructZip design is never explained.

### Minor

6. **The gain of StructZip over its own uncompressed baseline (w/o → w/) is often negligible or negative**: e.g., TNEWS: 0.905 → 0.903; Dolly 2.0: 0.753 → 0.754; xLAM: 0.982 → 0.945. This shows the value is almost entirely attributable to fine-tuning on the test data, not to the compressed-token design itself. A proper comparison would pit StructZip-compressed against a fine-tuned model given the full prompt, which never appears.

7. **GPT-4o "3M context" claim is self-refuted**: Table 1 states the xLAM GPT-4o baseline uses a 3M-token context, but the table note immediately explains that GPT-4o actually uses the top-20 retrieved tools (1346 tokens). This inconsistency undermines the paper's narrative of "compressing millions of tokens to one."

8. **Latency improvements are modest relative to the reported compression ratio**: For Firefly (15× compression), total latency improves by only ~11% (6252→5547ms). For TableBench (13× compression), the improvement is ~7% (2511→2335ms). These numbers suggest the bottleneck is output generation, not context encoding—yet the framing emphasizes inference speedup.

### Trivial

- Section 4 contains a first-person statement written in inconsistent voice ("To the best of my knowledge") that conflicts with double-blind conventions.

---

## Nice-to-Haves

- An experiment training on a held-out portion of the structured data and testing on truly unseen tables/tools would give a fair measure of generalization.
- Reporting the fine-tuning cost (compute hours, number of training steps, GPU-hours) would allow users to properly assess amortized efficiency.
- A comparison with a strong fine-tuned baseline that receives the full (uncompressed) structured prompt would isolate the contribution of compression from fine-tuning.

---

## Novel Insights

The framing of structured prompt compression as "unzipping" structured data into QA pairs is an interesting conceptual direction. The empirical finding that a single special token suffices for eliciting a broad structured knowledge base—and that beyond ~10 tokens marginal benefit vanishes—is genuinely interesting. However, because the experiments are confounded by test-data leakage and training/inference asymmetry, these insights cannot be taken at face value in their current form.

---

## Suggestions

- **Most critical**: Rerun TableBench and xLAM experiments with a strict train/test split, ensuring no test-instance tables or tools appear in the fine-tuning QA corpus.
- Provide compute cost figures (QA generation time, fine-tuning time per dataset) to give a complete efficiency picture.
- Add a "fine-tuned, uncompressed" row to all tables to isolate the compression benefit from the fine-tuning benefit.
- Reconcile or explain the "LDPC" vs. "StructZip" naming in Section 5.3.
- Discuss the practical update scenario: when a tool description changes, what is the cost to update the parametric memory?

---

## Score and Decision

The core problem (structured prompt compression) is genuinely valuable and underexplored. However, the paper's central experimental comparison is invalidated by test-data contamination (models are fine-tuned on QA pairs derived from test-set tables/tools before evaluation) and an asymmetric baseline comparison (inference-only methods vs. a method with full test-data pre-training). Without correcting these fundamental issues, the reported performance numbers cannot be interpreted as evidence that StructZip is an effective compression method, as opposed to an effective fine-tuning recipe. These are not presentation deficiencies—they go to the core validity of the claims.

MY FINAL SCORE: <score>3</score>
MY FINAL DECISION: <decision>Reject</decision>