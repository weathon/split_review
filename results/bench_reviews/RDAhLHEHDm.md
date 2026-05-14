Now I have enough material to write the final consolidated review. Let me compile everything.

---

## Summary

This paper challenges the prevailing sequence-centric paradigm in Scientific LLMs by arguing that raw biomolecular sequences, due to tokenization, introduce noise rather than signal. The authors propose a context-driven alternative: feed LLMs structured, human-readable functional annotations derived from bioinformatics tools (BLAST, Pfam, InterProScan) instead of raw sequences. Through systematic experiments across six models and three input modes (sequence-only, context-only, sequence+context), the paper finds that context-only consistently outperforms other conditions and, strikingly, that adding sequences to context degrades performance. The paper further diagnoses the "tokenization dilemma" through representation analysis, layer-wise decomposition of semantic misalignment, temporal degradation trends, and a small wet-lab validation.

## Strengths

- **Consistent evidence that raw sequences harm reasoning**: Across all six models in Table 1, context-only matches or outperforms sequence+context (5 of 6 models show context-only ≥ sequence+context), and sequence-only dramatically underperforms. The finding that raw sequences act as "informational noise" when added to structured context is counterintuitive and well-supported by the data pattern, even if individual differences are small.

- **Layer-wise decomposition of semantic misalignment in Evolla**: Figure 3 traces the progressive degradation of functional representation from the SaProt encoder (ARI 0.945) through the Q-Former alignment (0.916) to the final LLM layer (0.809). This is a genuinely mechanistic analysis that isolates where the cross-modal gap manifests, rather than merely asserting it exists.

- **Temporal degradation analysis showing superior generalization**: Section 5.4 demonstrates that the context-driven approach degrades far more gracefully on recently discovered proteins (slope –0.618) than Evolla (slope –0.923), while Intern-S1 shows flat, uniformly low performance. This temporal analysis is cleverly constructed and provides converging evidence for the tokenization dilemma.

- **Broad, multi-model experimental design**: The evaluation spans three specialized Sci-LLMs (Intern-S1, Evolla, NatureLM) and four general-purpose LLMs (Deepseek-v3, Gemini 2.5 Pro, GPT-5, Qwen3-235B), across three task categories. This breadth strengthens the generalizability of the findings.

- **Practical efficiency advantage with actionable numbers**: Table 2 demonstrates that the context-driven approach is 23× cheaper and 154× faster (in batch) than Evolla while achieving substantially higher accuracy, providing a concrete argument for practitioners.

## Weaknesses

### Major

1. **Unquantified answer leakage in the context-generation pipeline.** The context pipeline extracts GO annotations from BLASTp homologs in Swiss-Prot. For proteins with close, well-annotated homologs, the context may directly contain the ground-truth answer or a near-paraphrase, turning the QA task into an extractive reading exercise rather than a test of reasoning. The paper discusses anti-leakage measures (Section 4) — using InterProScan for intrinsic domain detection and reading annotations from homologs rather than the query protein — but this does not prevent the homolog's annotation from being the correct answer, which is standard for well-studied proteins. Crucially, the paper provides no quantification of answer-context overlap, no ablation that removes answer-bearing content from the context, and no retrieval-only baseline (e.g., a keyword matcher applied to the context). This means the absolute context-only scores may substantially overstate the LLM's reasoning capability. The wet-lab validation (Section 5.6) partially addresses this by testing on unpublished sequences, but the sample sizes (20 rhodopsin, 37 PETase) are too small and the binary classification task too simple to carry the burden of proof. This weakness affects the paper's central claim that context-driven LLMs excel as "reasoning engines."

2. **No statistical support for the "informational noise" claim.** The differences between Sequence+Context and Context-Only in Table 1 are often small (e.g., Intern-S1: 84.03 vs. 86.15; Deepseek-v3 reverses: 86.03 vs. 84.99). No confidence intervals, significance tests, or variance estimates are reported. The paper's central narrative — that raw sequences are "informational noise" — depends on interpreting these small differences as meaningful. The consistent direction across 5 of 6 models is suggestive, but without statistical rigor the claim remains an overstatement relative to the evidence presented.

### Minor

3. **NatureLM's sequence-only score (6.82) is unexamined.** This near-zero score raises questions about whether NatureLM can produce coherent answers in a zero-shot QA format with raw sequence input, or whether the score reflects a formatting/output failure rather than a tokenization issue. The paper does not discuss prompting strategy, few-shot examples, or output parsing for any model in sequence-only mode. However, this does not undermine the broader pattern: Intern-S1 (43.33) and Evolla (59.93) produce interpretable scores in sequence-only mode, so the overall trend holds even if NatureLM is excluded.

4. **Context representation ARI (0.958) is unsurprising and partially circular.** The paper embeds the curated context using a text-embedding model (Qwen-embedding) and reports an ARI of 0.958 (Figure 2d). Since the context is an explicit, human-readable summary of protein function, this near-perfect functional separation is expected and does not isolate tokenization as the causal factor. The comparison remains valid as a demonstration that context-based input representations are higher quality, but the framing as proof of the "weak representation" horn would benefit from more nuance.

5. **Wet-lab validation is too small and restricted to support generalization claims.** The rhodopsin/PETase binary classification involves only ~57 total samples and a simplified task relative to the main benchmark. While the result is directionally encouraging, the possibility of diagnostic keywords in the context (e.g., distant Pfam hits mentioning "rhodopsin") making the task trivial is not explored.

### Trivial

- The paper would benefit from explicitly reporting how models were prompted in the sequence-only condition, including whether few-shot examples were used, to enable assessment of whether the models were tested in a regime they support.

## Nice-to-Haves

- A controlled experiment on a benchmark where all proteins are guaranteed absent from Swiss-Prot and Pfam would cleanly separate retrieval from reasoning.
- Per-category analysis of how often the answer text or a paraphrase appears in the generated context, with performance stratified by overlap, would allow readers to calibrate the reasoning-vs-extraction contribution.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Sequence-only baseline is not a valid use of the tested models"**: The critic argues the models may not be capable of generative QA from raw sequences. However, Intern-S1 (43.33) and Evolla (59.93) clearly produce interpretable, non-zero results in sequence-only mode, and the Context-Only scores for all models (including NatureLM at 39.50) demonstrate they can generate answers when given interpretable input. The sequence-only failure for NatureLM is worth discussing but does not invalidate the baseline.

- **"The representation analysis equates curated text with learned embeddings and is structurally circular"**: The paper does compare a text-embedding model's output to Sci-LLM embeddings, but the point it makes — that context-based inputs yield functionally more separable representations — is legitimate. The 0.958 being "foregone" is true but the comparison still has value for quantifying the gap between input modalities. This point is weakened and moved to minor.

- **"Missing appendix" / "Appendix is unavailable"**: The parser strips appendices from all papers. This is not an author error.

- **Missing related works**: Per instructions, I do not flag missing related works as I cannot verify their existence.

- **Formatting nitpicks, typos, grammar concerns**: Per instructions, these are parser artifacts and not author errors.

## Novel Insights

The paper's most novel empirical contribution is the consistent observation that adding raw biomolecular sequences to an already informative context *degrades* performance across multiple models, rather than merely failing to help. This is genuinely counterintuitive and, if robust, challenges the default assumption in the field that more modalities are always better. The layer-wise decomposition of Evolla (encoder → alignment → decoder) provides a rare mechanistic trace of where cross-modal alignment fails in a concrete deployed system, rather than merely asserting a modality gap.

## Suggestions

- The paper should quantify answer-context overlap (e.g., BLEU or ROUGE between ground-truth answers and generated context) and bin performance by overlap level. This would let readers see how much of the context-only advantage comes from reasoning vs. extraction, substantially strengthening the contribution without requiring new experiments.
- Reporting bootstrapped confidence intervals or pairwise significance tests for the Sequence+Context vs. Context-Only comparisons in Table 1 would solidify or appropriately temper the "informational noise" claim.
- The NatureLM sequence-only result deserves explicit discussion — was the model producing garbled output, or were its answers simply wrong? A brief qualitative analysis would address the concern.

## Score and Decision

**Anchor comparison:**

| Paper | Avg Score | Decision | Comparison |
|-------|-----------|----------|------------|
| GeoBPE (55e5f3GVFc) | 7.50 | Accept (Poster) | Substantially stronger: novel method, rigorous experiments, breakthrough results. Current paper is less technically deep. |
| PepBenchmark (NskQgtSdll) | 6.00 | Accept (Poster) | Stronger execution: comprehensive benchmark with rigorous preprocessing. Current paper has more conceptual novelty but weaker evaluation validation. |
| QAProt (cliPM6kk9J) | 5.00 | Reject | Most comparable: interesting premise, systematic experiments, but significant methodological issues (data quality, evaluation metrics). Current paper has a similar profile. |
| NABench (d0gvsym66h) | 5.00 | Reject | Solid benchmark but limited novelty. Current paper addresses a broader, more conceptual question. |
| CoPeP (QI2xC19p7U) | 4.50 | Reject | Benchmark with limited novelty. Current paper is more ambitious and original. |
| LiveProteinBench (ACroNFU7Do) | 4.00 | Reject | Benchmark with limited scale and novelty. Current paper has more substance and broader experiments. |
| PFMBench (KJNgtPNxtv) | 3.50 | Reject | Benchmark with significant issues. Current paper is clearly stronger. |
| ProtFunAgent (KjyQhJUobQ) | 3.00 | Reject | Trivial technical design over existing LLMs. Current paper has much more systematic analysis and genuine insights. |

The paper under review makes a genuine conceptual contribution — identifying and diagnosing the tokenization dilemma — and supports it with systematic multi-model experiments. The finding that raw sequences degrade performance when added to context is counterintuitive and valuable. However, the evaluation has a structural weakness (unquantified answer leakage in context) that inflates the absolute context-only advantage and undermines the "reasoning engine" framing. The lack of statistical testing further weakens the "informational noise" claim. These issues are fixable with additional analysis but are significant enough in the current version to limit confidence in the paper's strongest conclusions. The paper sits between QAProt (interesting premise, methodological concerns → 5.0, Reject) and PepBenchmark (solid execution, clear contribution → 6.0, Accept). The evaluation validity concern pulls it below the accept threshold, but the conceptual framing and empirical insights prevent it from falling into clearly rejectable territory.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>