I now have a thorough understanding of the paper and the reviewer inputs. Let me produce the consolidated review.

---

## Summary

This paper proposes RagVL, a three-stage multimodal RAG framework that addresses the multi-granularity noisy correspondence (MNC) problem. It (1) uses CLIP for first-stage retrieval, (2) instruction-tunes an MLLM as a reranker with a caption-aware template to filter coarse-grained noise, and (3) applies noise-injected training (NIT) at data and token levels during generation to handle fine-grained noise. Experiments on WebQA and MultimodalQA subsets show strong retrieval improvements and competitive generation accuracy.

## Strengths

- **Large and consistent retrieval gains from MLLM-based reranking.** Instruction-tuning MLLMs with a simple caption-aware template yields dramatic improvements over CLIP retrieval across five MLLM backbones. On WebQA, R@2 rises from 57.10 (CLIP) to 82.00 (InternVL2-1B reranker), an average improvement of ~40% as stated (Table 1). On MultimodalQA, rerankers reach 98.26% R@1 with multiple MLLMs. These results directly support the claim that knowledge-enhanced reranking effectively mitigates coarse-grained noise.

- **Cross-dataset generalization demonstrated.** The reranker fine-tuned on WebQA achieves competitive performance when evaluated on MultimodalQA (Figure 2a), and with only 2.5% of WebQA training data it surpasses the strong retriever InternVL-G in R@2 (Figure 2b). This provides evidence that the approach transfers across datasets and is sample-efficient.

- **Systematic evaluation across multiple MLLM backbones and threshold strategies.** The paper tests five MLLMs (LLaVA, mPLUG-Owl2, Qwen-VL-Chat, InternVL2-1B, InternVL2-2B) with two threshold strategies (natural and adaptive), showing consistent improvements across all settings (Tables 1, 2, 3). This thoroughness strengthens the empirical support.

- **Clear problem decomposition.** The paper identifies a real and underexplored problem (MNC in multimodal RAG) and provides a reasonable decomposition into coarse-grained noise (query-caption mismatch) and fine-grained noise (query-image mismatch), motivating each pipeline component.

## Weaknesses

### Fatal
None.

### Major

- **The "w/o NIT" baseline in Table 3 is ambiguous, undermining the generation results.** The paper reports that "RagVL w/o NIT" achieves 44.67 overall accuracy on WebQA (InternVL2-2B), while "RagVL w/ NIT" achieves 62.23 — a ~17.5 point gain. However, it is never stated whether the generator in "w/o NIT" was fine-tuned on the dataset (without noise) or left as the base MLLM. The near-identity of "InternVL2-2B w/ CLIP Top-N" (44.39) and "RagVL w/o NIT" (44.67) strongly suggests the generator is the *base* MLLM, meaning the comparison conflates standard fine-tuning with noise injection. The controlled ablation in Table 4 shows that removing both NIT components (ND & NLC) from the full model drops accuracy only ~1.8 points (64.25 → 62.42), confirming that most of the gain in Table 3 comes from fine-tuning itself, not noise injection. A row showing the generator fine-tuned on clean data (no NIT) is essential to interpret NIT's contribution.

- **No experimental comparison to existing multimodal RAG methods (MuRAG, SKURG).** The paper discusses MuRAG and SKURG as the closest prior work on multimodal RAG (lines 27, 49) and claims to "advance multimodal RAG," yet includes zero experimental comparisons to these systems. The baselines are either MLLMs without retrieval or MLLMs with CLIP/InternVL-G retrieval. Without this comparison, the paper cannot establish an advance over the existing state of the art in multimodal RAG. This is a serious gap given that both systems were designed for the same datasets.

### Minor

- **Adaptive threshold tuned and evaluated on the same validation set.** The paper tunes the adaptive threshold on the validation set (line 289: "plotted the interpolated curves... on the validation set") and reports all results on the same validation set (line 123: "Since the test set labels... are not publicly available, we report the results on the validation set"). This is a form of data leakage that inflates the precision numbers for the adaptive threshold condition. The natural threshold (η=0.5) avoids this issue and achieves very similar results (Table 2), but the adaptive threshold numbers should be interpreted with caution.

- **Missing dataset statistics.** The paper describes using "image-related subsets" of WebQA and MultimodalQA but provides no basic statistics: number of queries, size of the retrieval corpus, distribution of hard negatives per query, or CLIP's actual Recall@20. Without these, it is difficult to interpret the near-perfect R@1 on MultimodalQA (98.26%) or to assess the difficulty of the retrieval task.

- **No empirical isolation of coarse-grained vs. fine-grained noise.** The paper claims the reranker addresses coarse-grained noise (query-caption) and NIT addresses fine-grained noise (query-image), but no experiment separately measures these two noise types or demonstrates that each component specifically addresses its claimed level. The claims about which component handles which noise granularity remain untested.

### Trivial

- The paper mentions "the upper limit of Recall@20 (98.26%) from CLIP" in the text (line 167), but CLIP's R@20 is not reported in any table, making it difficult to verify this figure.

- The low-resource experiment (Figure 2b) compares the reranker (which benefits from CLIP first-stage retrieval) to the InternVL-G first-stage retriever. While not an unfair comparison — the paper is comparing its full retrieval pipeline to a strong retriever — it is not a pure measure of the reranker's sample efficiency in isolation.

## Nice-to-Haves

- Reporting results with confidence intervals or over multiple seeds would strengthen confidence in the 1–2 point differences in the ablation study.
- A failure analysis or case studies showing where the reranker or NIT fails would be informative.
- Testing on a larger-scale retrieval corpus (full Wikipedia-scale image collection) would validate whether the reranker scales beyond the current dataset-specific hard negatives.

## Removed Points

These points were removed from the critic input (with rationale):

1. **Criticism that the 98.26% R@1 on MultimodalQA is "implausible" or "extraordinary."** The paper explicitly states this equals CLIP's Recall@20 upper bound. The MultimodalQA subset is small; such recall levels are plausible. The critic's concern reflects a knowledge gap about the dataset scale, not an author error.

2. **Criticism about the reranker training data "exactly matching the test distribution."** This is standard supervised learning, not a flaw. The paper also provides a cross-dataset generalization experiment that directly mitigates this concern.

3. **Claim that the low-resource experiment is an "unfair comparison" between a reranker and a retriever.** The comparison shows the *full retrieval pipeline* (CLIP + reranker trained on minimal data) outperforming a strong *first-stage retriever* (InternVL-G). The asymmetry favors the baseline (InternVL-G has no reranking), making the result more, not less, convincing.

4. **Demand for statistical significance tests.** Single-run evaluation on these benchmarks is standard practice. This is a scope-creep requirement.

5. **Formatting/style nitpicks and reproducibility nitpicks about undisclosed hyperparameters/artifacts.** These are either parser artifacts or standard detail levels for a conference submission.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface a perspective not already present in the paper.

## Suggestions

1. **Add a controlled fine-tuning baseline for the generator.** Include a row in Table 3 showing the generator fine-tuned on the *clean* dataset (without noise injection) with the same reranking pipeline. This will cleanly separate the effect of fine-tuning from the effect of noise injection and make the NIT improvement interpretable.

2. **Add experimental comparisons to MuRAG and SKURG** on the same subsets. Even if these methods have different architectures or training recipes, reporting their generation accuracy provides necessary context for the claimed advance in multimodal RAG.

3. **Report dataset statistics** — number of queries, retrieval corpus size, number of hard negatives per query, and CLIP's recall at various K (including K=20) — to contextualize the retrieval difficulty and the near-perfect MultimodalQA results.

4. **Report all results on a held-out test set or use cross-validation** for the adaptive threshold to avoid data leakage. The natural threshold results are clean; the paper should either use only the natural threshold or properly separate threshold tuning from evaluation.

5. **Isolate noise granularities experimentally.** Design an experiment that coarsely measures each component's effect on the specific noise type it claims to address (e.g., evaluate the reranker on queries where caption ambiguity is the primary challenge, and NIT on queries requiring fine-grained visual discrimination).

## Score and Decision

The paper identifies a meaningful problem (MNC in multimodal RAG) and proposes a reasonable pipeline. The reranking component is well-validated with consistent gains across multiple backbones and a cross-dataset generalization test. However, the evaluation of the noise-injected training component is undermined by an ambiguous baseline that conflates fine-tuning with noise injection, and the missing comparison to prior multimodal RAG systems (MuRAG, SKURG) prevents the paper from establishing an advance over existing work. These are substantive issues that require both clarification and additional experiments to resolve. A revision that adds a controlled fine-tuning baseline, compares to MuRAG/SKURG, and provides dataset statistics could make this a strong paper.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>