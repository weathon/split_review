Now I have a thorough understanding of the paper. Let me produce the consolidated review.

## Summary

CoreInfer proposes a sentence-level sparse activation inference method for LLMs. The key idea is to identify "sentence-wise core neurons" during the pre-filling stage — a static subset of neurons used throughout decoding — eliminating per-token MLP predictors required by prior methods (DejaVu, PowerInfer). The paper discovers two correlations between core neurons and semantics (stability under consistent semantics, similarity under similar semantics) and designs two prediction methods (stability-guided for few-shot/long inputs, similarity-guided for zero-shot/short inputs). Results show up to 10.33× speedup over HuggingFace on a TITAN XP with OPT-6.7B.

## Strengths

- **First demonstration of sentence-wise activation sparsity in LLMs.** The paper formally defines sentence-wise core neurons (Definitions 1 and 2, Sec. 3.1) and empirically shows that using only these neurons during decoding causes only modest performance loss (e.g., perplexity increases ~2% at α=0.4, Fig. 2a–b). This is a novel contribution — prior work assumed activation patterns must be determined token-by-token.

- **Discovery that core neurons correlate with semantics in stability and similarity.** Through systematic experiments (Fig. 3, Fig. 4), the paper shows that core neurons remain nearly unchanged when semantics are stable, and cluster by topic when semantics are similar. This insight is supported by Spearman correlations on STS-B (up to 0.66) and SICK (up to 0.51) across multiple models (Tab. 1), providing quantitative evidence.

- **Two semantic-guided prediction methods that eliminate MLP predictors.** The stability-guided method (Sec. 5.1) reuses pre-filling core neurons for decoding; the similarity-guided method uses offline cluster-level statistics. Both avoid per-token, per-layer MLP predictors, directly addressing the two weaknesses of prior work (irregular resource calls, extra computation). This is validated by zero predictor latency and memory in Table 4.

- **Substantial speedup and memory reduction on resource-constrained hardware.** On a TITAN XP with OPT-6.7B, CoreInfer achieves 19.83 t/s vs. 1.92 t/s for HuggingFace (10.33×), and uses 7.28 GB memory vs. 12 GB. The memory savings enable the entire model to fit on GPU, eliminating I/O overhead. Speedups hold across model sizes (Fig. 5, Upper) and architectures (OPT ReLU-based, LLaMA SiLU-based).

## Weaknesses

### Fatal
None.

### Major

- **The similarity-guided prediction method is underspecified, undermining reproducibility of zero-shot results.** The paper describes this method as clustering a training dataset and selecting the top-γ neurons per cluster (Sec. 5.1, lines 238–240). However, it does not specify: (a) which training dataset is clustered, (b) what clustering algorithm is used, (c) how many clusters, (d) how a new input sentence is assigned to a group at inference time, or (e) whether cluster-specific neuron sets are computed once offline or per-prompt. Since similarity-guided prediction is used for all zero-shot QA and translation results in Table 3, the missing implementation details make these experiments difficult to reproduce or assess for potential data leakage. This is a genuine gap, though it affects only the zero-shot branch of the evaluation, not the stability-guided method used for few-shot tasks.

- **The claim of "negligible performance loss" is overstated.** Table 3 shows several non-trivial drops: LLaMA2-7b Xsum rouge drops from 6.4 to 5.9 (7.8% relative), OPT-6.7b wmt16-de-en few-shot drops from 30.4 to 27.9 (8.2%), and OPT-13b wmt16-de-en few-shot drops from 32.6 to 33.4... wait, that one improves. But looking more carefully: LLaMA3.1-8b wmt16-de-en few-shot drops from 43.4 to 41.2 (5.1%), OPT-6.7b SQuAD drops from 52.1 to 53.2... that improves too. The pattern is mixed, which the paper acknowledges but does not deeply explain. Several results show 5–8% relative degradation, which is not "negligible" for high-stakes applications. A more precise characterization (e.g., "most results are within 5% relative of the original, with some tasks showing larger variance") would be more accurate.

### Minor

- **No statistical significance reported.** No error bars, confidence intervals, or multiple-run statistics are provided for any metric (Table 3, Fig. 3). Given that CoreInfer sometimes *outperforms* the original model (e.g., OPT-6.7b SQuAD 53.2 vs. 52.1; OPT-13b wmt16-de-en zero-shot 35.2 vs. 31.3), it is unclear whether these differences are meaningful or within measurement noise. Multiple runs with standard deviations would substantially strengthen confidence in the results.

- **Speedup claims lack pre-filling vs. decoding breakdown.** All speedup experiments (Fig. 5) use a short input length (~64 tokens). CoreInfer requires computing core neurons during pre-filling (full forward pass plus sorting/percentile aggregation), but this overhead is not quantified separately from decoding speedup. For longer prompts, the pre-filling cost grows while decoding benefits remain constant, meaning end-to-end speedup would decrease. Reporting the latency breakdown would clarify the practical regimes where CoreInfer is most beneficial.

- **No task-performance comparison with prior sparse inference methods.** Table 4 compares hardware metrics against DejaVu and PowerInfer, but Table 3 compares task accuracy only against the original dense model. Adding DejaVu/PowerInfer task accuracy numbers (or citing their reported results) would directly show whether CoreInfer preserves task quality comparably to prior work, strengthening the claim that eliminating MLP predictors does not come at a task-performance cost.

### Trivial

- **The claim that semantic similarity = 1 after adding 8 tokens to a 256-token sentence** (Sec. 3.2, line 175) is likely an artifact of rounding or the specific similarity measure. Sentence-BERT similarity of exactly 1.0 between non-identical sentences is improbable. The intended point (very high similarity) stands, but the absolute wording should be corrected.

- **Figure 6 caption** (line 331) describes the impact of β and γ but does not label which curves correspond to which tasks on the plots, making the figure less interpretable on its own.

## Nice-to-Haves

- Adding a Limitations section discussing cases where the method may underperform (e.g., long-form generation with topic drift, out-of-domain inputs for similarity-guided prediction, models with non-{ReLU, SiLU} activations).
- Ablating the α hyperparameter across tasks (currently fixed at 0.4 from a single C4 perplexity experiment) to show robustness.
- Analyzing why CoreInfer sometimes outperforms the original model (e.g., comparing output distributions or attention patterns), to ground the "specialized response" speculation.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism about "I/O Free" labeling for PowerInfer.** The reviewer claimed PowerInfer should not be marked "I/O Free" because it relies on CPU offloading. However, in the specific configuration reported (OPT-6.7B on TITAN XP, 9.26 GB < 12 GB), PowerInfer fits on GPU without I/O. The table documents this experimental setup accurately. *(Removed: factually wrong/misunderstands the experimental configuration.)*

- **Criticism about "Predictor Latency" and "Predictor Memory" for Ours being marked "NA".** The reviewer argued the pre-filling overhead (sorting, aggregation) should be measured here. However, the table specifically tracks *MLP predictor* metrics — CoreInfer has no MLP predictors, so "NA" is correct. The pre-filling overhead is a separate concern, not a "predictor" metric. *(Removed: category confusion between predictor overhead and pre-filling overhead.)*

- **Criticism about "only five models... all from the same family."** OPT and LLaMA are different model families with different architectures (ReLU vs. SiLU activations), developed by different teams. Calling them "the same family" is inaccurate. *(Removed: factually incorrect.)*

- **Criticism about missing appendix content / proofs / references.** Parser instructions confirm these sections exist in the original submission and are stripped by the extraction process. *(Removed per meta-reviewer instructions: known parser artifact.)*

- **Various formatting/style nitpicks and demands for unrelated scope expansions** (e.g., demanding the paper address long-form generation with topic drift as a core requirement, or requiring confidence intervals at a level not standard for this type of benchmark paper). *(Removed: scope creep or style nitpicks.)*

## Novel Insights

Beyond the paper's own contributions, the most interesting pattern emerging from the reviews is the asymmetry between the two prediction methods: the stability-guided approach (used for few-shot tasks) is well-specified and its results are clearly interpretable, while the similarity-guided approach (used for zero-shot tasks) is described at a high level only. This suggests the paper's core contribution — sentence-level core neurons for decoding — is robust when the input provides enough context to establish stable semantics, but its generality to zero-shot settings via the similarity-guided pipeline remains the least substantiated component. The fact that CoreInfer sometimes outperforms the original model (e.g., OPT-6.7b SQuAD, several zero-shot translation entries) is also intriguing and underexplored — it hints that sparsity may act as a regularizer or noise filter, which could be a direction for future work.

## Suggestions

1. **Fully specify the similarity-guided prediction pipeline** — provide the clustering algorithm, training dataset, number of clusters, inference-time group assignment procedure, and whether per-cluster neuron sets are computed offline. Even a brief appendix section would resolve the reproducibility concern.

2. **Add a pre-filling vs. decoding latency breakdown** for at least two input-length regimes (e.g., 64-token and 512-token prompts) so readers can assess end-to-end speedup.

3. **Report standard deviations** for at least a subset of the task-performance results (3 runs) to establish whether observed differences are meaningful, especially where CoreInfer outperforms the original model.

4. **Tone down the "negligible" language** — replace with a quantitative characterization (e.g., "most results are within 5–8% relative of the original").

## Score and Decision

This paper makes a genuine contribution: identifying sentence-level core neurons and demonstrating their correlation with semantics is novel, the stability-guided prediction is well-specified and effective, and the hardware speedups are substantial. However, the similarity-guided prediction pipeline is underspecified to the point of not being reproducible, the "negligible loss" claim is somewhat overstated, and the evaluation lacks statistical rigor. These are addressable weaknesses — the core idea is sound — but in their current form, the similarity-guided results cannot be fully assessed. This places the paper below the accept threshold for a major venue.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>