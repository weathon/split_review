Now I have a thorough understanding of the paper and can verify claims against the actual text. Let me produce the final consolidated review.

---

## Summary

This paper introduces CoreInfer, a sentence-level adaptive sparse activation framework for LLM inference. The key idea is to define "sentence-wise core neurons" — the most frequently activated neurons across all tokens in a sentence — and predict them during the pre-filling stage without per-token MLP predictors. The authors discover that core neurons exhibit both stability (they change little when semantics are stable) and similarity (sentences with related semantics share similar core neuron sets), enabling two prediction strategies. CoreInfer achieves substantial speedups (up to 10.33× on TITAN XP and 5.5× on A100 vs. Huggingface Transformer) while largely maintaining task performance across OPT, LLaMA2, and LLaMA3.1 models on six datasets spanning information extraction, QA, and translation.

## Strengths

1. **First demonstration of sentence-level activation sparsity that eliminates per-token MLP predictors.** CoreInfer defines sentence-wise core neurons and predicts them during pre-filling only, avoiding the frequent activation-map updates and MLP predictor overhead of DejaVu and PowerInfer. This is empirically validated in Table 3 (0 ms predictor latency vs. 9.62 ms for DejaVu and 15.96 ms for PowerInfer on the same hardware).

2. **Quantitative evidence that core neurons correlate with sentence semantics via stability and similarity.** Section 3.2 provides clear evidence: core-neuron similarity tracks semantic similarity when sentences are extended (Fig. 2a,b), sentences from the same topic cluster by core neurons across layers (Fig. 3), and Table 1 reports Spearman correlations up to 0.66 (LLaMA2-7b on STS-B), generalizing across ReLU (OPT) and SiLU (LLaMA) models.

3. **Consistent speedups across multiple model families and scales without catastrophic accuracy loss.** On the TITAN XP, CoreInfer achieves 19.83 tok/s (10.33× vs. Transformer, 2.71× vs. PowerInfer) for OPT-6.7b using only 7.28 GB memory. On the A100, speedups hold across models up to LLaMA2-70b (5.5×). Table 2 shows task performance within a few points of the original model across 6 datasets and 5 models, with some zero-shot cases even matching or slightly exceeding the original.

4. **Model generality explicitly demonstrated.** The method works on OPT (ReLU), LLaMA2-7b (SiLU), and LLaMA3.1-8b (SiLU), as shown in both correlation analysis (Table 1) and task performance (Table 2), going beyond the ReLU-only focus of some prior sparsity work.

5. **Task-specific hyperparameter analysis guiding practical deployment.** Figure 5 shows that Information Extraction and QA require only β=0.2 while Translation needs β=0.4, providing actionable guidance that aligns with the hypothesis that more complex tasks need more neurons.

## Weaknesses

### Fatal
None.

### Major

1. **The similarity-guided prediction pipeline is critically underspecified for reproducibility.** The paper states (Section 4.1) that it clusters a "training dataset" based on semantic similarity and assigns inputs to clusters to select top-γ frequent core neurons, but it provides: (a) no details about what corpus is used for clustering (task-specific? general?), (b) no embedding model or clustering algorithm specified, (c) no description of how a new input is assigned to a cluster (e.g., nearest centroid in Sentence-BERT space?), and (d) no quantification of clustering quality or assignment accuracy. Since similarity-guided prediction is one of only two prediction methods and is used for zero-shot QA and translation — where CoreInfer is already being compared against the original model — this gap means a core component of the framework cannot be independently reproduced or assessed.

2. **Task accuracy is not compared against DejaVu or PowerInfer.** Table 2 compares CoreInfer only against the original full model ("Ori" vs. "Ours"). The hardware benchmarks (Table 3, Figure 6) compare speed and memory against DejaVu and PowerInfer, but without knowing whether those baselines degrade accuracy more or less than CoreInfer, the reader cannot evaluate the accuracy-efficiency trade-off. If DejaVu's accuracy drop is larger, CoreInfer's speed advantage is even more valuable; if smaller, CoreInfer might be trading accuracy for speed relative to the same baseline class. This omission prevents a complete assessment of CoreInfer's position in the sparse activation landscape.

### Minor

3. **The stability vs. similarity decision rule is a heuristic tied to task type, not an operational criterion.** The paper assigns stability-guided prediction to few-shot/extraction tasks and similarity-guided to zero-shot tasks (Section 5, paragraph "Tasks"). While this is reasonable and correlates with input length (longer inputs tend to have more stable semantics, as shown in Fig. 3c), there is no formal threshold or quantitative criterion for "stability" that would let a practitioner apply CoreInfer to a new task without copying the paper's task-level assignments. This limits the method's general applicability.

4. **No statistical uncertainty reported for task performance (Table 2).** No standard deviations or multi-run averages are provided. Several cells show CoreInfer outperforming the full model (e.g., OPT-6.7b SQuAD: 53.2 vs. 52.1; TruthfulQA zero-shot BLEU max: 9.12 vs. 7.88), and the paper speculates this is due to "specialized neurons." Without error bars, it is impossible to distinguish genuine gains from noise, weakening a key claim about lossless performance. Single-run evaluation is common in LLM benchmarking but the presence of variability-prone small-margin differences makes this a concern here.

5. **The implementation pathway for sparse decoding is not described.** The paper claims (Section 5.3) that only "a fixed, small subset of neurons" participates in decoding, enabling the reported memory (7.28 GB for OPT-6.7b) far below the full FP16 parameter size. Standard GEMM kernels do not support loading arbitrary column subsets of a weight matrix on the fly; a custom sparse kernel or tailored slicing strategy would be needed. The paper provides no description of the compute kernel, memory layout, or batching strategy used. Since the hardware results (Table 3, Figure 6) are a central contribution, the absence of implementation details makes them unverifiable. However, this concern is partially mitigated because the feasibility of sparse FFN computation is already demonstrated by prior work (PowerInfer, DejaVu), and the paper's algorithmic innovation is the *prediction* method, not the sparse execution engine.

6. **The stability experiment (Fig. 2a,b) adds only short continuations (8, 64 tokens) to a 256-token sentence.** "Semantic similarity near 1.0" combined with "core neuron change of only 3-6%" may not generalize to realistic multi-topic generation where the model shifts between subjects. The paper partially addresses this with the length-sweep visualization (Fig. 2 lower: 10→300 tokens), but the explicit stability measurement only uses narrowly factual continuations.

### Trivial
- The ag_news clustering (Figure 3) shows separation only across four coarse news topics; the paper does not test whether similarity-guided prediction works for finer-grained semantic distinctions within the same topic.
- The speed measurement protocol (pre-fill vs. decode breakdown, batch size, generation length control) is not explicitly stated, making detailed comparison with other systems difficult.
- The claim that prior methods "believe that the activation pattern of neurons cannot be predicted before the inference" (Section 2) is a slight over-simplification — DejaVu already predicts activations per-token before computing them — though the paper's real point (prediction can be done at sentence level before decoding starts, not per-token during decoding) is valid and correctly distinguishes the contribution.

## Nice-to-Haves
- Include task accuracy comparisons against DejaVu and PowerInfer on a subset of benchmarks (e.g., TruthfulQA, Xsum) to directly substantiate the claim that CoreInfer's accuracy preservation is competitive.
- Report end-to-end latency (pre-fill + decode) for short-generation scenarios where pre-fill overhead is not fully amortized.
- Explicitly state how attention layers are handled (they appear to be computed fully; stating this would remove ambiguity).

## Removed Points
These points are flagged to be removed; treat them with caution:
- **Criticism that PowerInfer's speed numbers may be due to poor implementation rather than algorithmic advantage**: This is speculative and unsupported by evidence in the review. Removed as conjecture.
- **Criticism that the Transformer baseline (1.92 tok/s) seems artificially low**: The paper explains this is due to GPU memory swapping (OPT-6.7b FP16 ≈ 13.4 GB on a 12 GB GPU). This is the normal behavior being benchmarked against, not a rigged baseline. Removed as misunderstanding.
- **Strawman about "missing comparison of which method degrades accuracy more" being framed as a structural gap**: Already addressed in Major weakness #2, but the reviewer's framing as "the central claim of large speedups rests on an implementation detail that is not disclosed" overstates the severity — the algorithmic contribution is the prediction method, and sparse FFN computation is a known engineering technique from prior work.
- **Generic strength claims from Strength Finder (generic statements not tied to specific evidence)**: None found — all listed strengths had specific empirical backing.

## Novel Insights
The most interesting observation from the combined reviews is that the paper's central conceptual contribution — sentence-level core neurons are predictable from semantics without per-token MLPs — is well-supported and genuinely novel, but the empirical evaluation is split across two disconnected comparison dimensions: accuracy (vs. full model only) and efficiency (vs. baselines). Connecting these dimensions (comparing accuracy of all methods on the same table) would significantly strengthen the evaluation without requiring new experiments. The reviews also surface a tension: the paper presents itself as a complete inference system (with hardware benchmarks) but omits engineering details that a systems paper would typically include, while simultaneously presenting an algorithmic contribution (sentence-level sparsity) that is methodologically novel. Clarifying which contribution is primary would help set appropriate evaluation expectations.

## Suggestions
1. Specify the similarity-guided prediction pipeline in full: report the clustering corpus, embedding model, clustering algorithm, number of clusters, and how input sentences are assigned to clusters (with accuracy/cluster-purity numbers).
2. Add a "head-to-head" task accuracy table comparing CoreInfer against DejaVu and PowerInfer on at least 2-3 tasks (e.g., TruthfulQA zero-shot, SQuAD, Xsum) to close the evaluation gap.
3. Provide a brief description of the sparse decoding implementation (e.g., "we load only the weight columns corresponding to active neurons in the FFN layers; attention layers are computed fully; CUDA kernel based on [reference]"). This would make the hardware results verifiable.
4. Report error bars or multi-run averages for Table 2, especially for cells where CoreInfer appears to outperform the original model.
5. Formalize the stability criterion: e.g., "if the variance of core neuron membership across pre-fill tokens is below threshold T, use stability-guided prediction; otherwise use similarity-guided."

## Score and Decision

The paper presents a genuinely novel idea (sentence-level sparse activation without MLP predictors) with strong speedup results and reasonable accuracy preservation across multiple model families. The core discoveries about stability and similarity of core neurons are well-supported by empirical evidence. However, two substantive gaps — the underspecified similarity-guided pipeline and the lack of accuracy comparisons against baselines — prevent the paper from being fully convincing as a complete, reproducible system. These are addressable in revision, and the underlying contribution is solid.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>