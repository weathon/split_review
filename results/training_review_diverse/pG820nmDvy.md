I have thoroughly read the paper and verified every claim against the source text. Let me now produce the consolidated review.

## Summary

This paper proposes top-k attention for efficient long-context LLM inference: keys and values are stored in a CPU-based vector database (Faiss), and at each generation step only the k most relevant keys are retrieved via approximate nearest neighbor search. The central claim is that attention is naturally sparse—very few keys suffice for near-full performance—enabling million-token context windows on a single ~16GB GPU. The paper provides sparsity analysis on Llama-3-8B and evaluates top-k attention on the RULER benchmark (up to 128k tokens), AlpacaEval 2.0, and OpenLLM leaderboard tasks, along with a 1M-token needle-in-a-haystack demonstration.

## Strengths

- **Empirical demonstration that extremely few keys suffice for near-full performance**: Figure 1 (right) shows that on the OpenLLM leaderboard, Llama-3-8B reaches full-attention performance with only 10 keys, and all tested Llama models saturate by the 15th key. This is the paper's most compelling result and directly supports the core sparsity claim.

- **Comprehensive evaluation across multiple benchmarks at moderate lengths**: The paper tests top-k attention on RULER (13 tasks, lengths from 4k to 128k), AlpacaEval 2.0 (805 queries), and OpenLLM leaderboard tasks, showing that ~1% of context length achieves ≥95% of baseline performance on all three. The RULER experiments include a full-attention baseline comparison (Table 1, line 128). The inclusion of both base and instruction-tuned models (Llama-1/2/3/3.1/3.2, Vicuna) strengthens generality.

- **Successful million-token inference on a single commodity GPU as a feasibility demonstration**: Section 4.3 and Figure 8 show that the method runs a 1M-token needle-in-a-haystack task on a single GPU with ~16GB RAM, using k=10, and compares against StreamingLLM (Xiao et al., 2023). This concretely demonstrates the headline capability.

- **Clean sparsity analysis motivating the method**: Figures 2–4 analyze Llama-3-8B attention patterns across 50 Wikipedia articles, showing that no sample requires more than 1250 of 4000 tokens to capture 75% of attention mass, and that attention entropy is low across layers. This grounds the approach in observed model behavior rather than assumption.

## Weaknesses

### Fatal
None.

### Major

1. **No runtime or memory measurements reported anywhere in the paper.** The paper's title and central narrative emphasize efficiency—"Running Huge Context Windows On Tiny GPUs," "sublinear complexity," "tiny GPU computing power"—yet neither wall-clock time (ms/token) nor peak GPU memory usage is reported for any experiment. This includes the RULER runs (4k–128k), the AlpacaEval runs, the OpenLLM runs, and critically, the 1M generation. Without these numbers, the efficiency gains are asserted but not demonstrated. The paper also does not quantify the overhead of CPU-based vector search or CPU–GPU data transfer. For a method whose primary contribution is computational efficiency, this is a fundamental gap in the evidence. The authors would need to report at minimum: (a) generation latency (ms/token) at multiple context lengths for top-k vs. full attention, (b) peak GPU memory at those lengths, and (c) where full attention fails due to memory, the context-length threshold where it fails.

2. **The million-token evaluation is limited to a single needle-in-a-haystack task.** The paper's headline result—1M-token inference on a tiny GPU—is supported only by Figure 8, which tests basic retrieval (needle-in-a-haystack) with k=10. The full RULER benchmark (which includes multi-task NIAH variants, summarization proxies, multi-hop proxies, and QA) is run only up to 128k tokens (Table 1). The paper does not evaluate at 1M on any of the more demanding RULER subtasks (e.g., multi-hop QA, variable-tracking), nor does it run any reasoning or generation-quality task at that scale. The 95% performance claim is supported at 128k and below, but is not demonstrated at 1M. The 1M experiment demonstrates feasibility but not general capability.

### Minor

3. **The method used to construct the initial KV cache for the 1M experiment is not specified.** Section 3.4 (lines 107–112) lists several possible techniques (Ring Attention, windowed attention, vLLM, top-k at construction time) and states "In our experiments, we employ a variety of these techniques depending on the model and context window size." The paper does not state which technique was actually used for the 1M run. Since constructing a 1M-token KV cache requires a full forward pass over the context, the method matters for assessing whether the "single 16GB GPU" claim covers both cache construction and generation, or only the latter. This needs explicit clarification.

4. **It is unclear whether the RULER/AlpacaEval/OpenLLM experiments used exact or approximate k-NN search.** Faiss (approximate) is mentioned only for the 1M experiment (line 151). For the primary benchmark results in Table 1 and Figures 6–7, the search method is not stated. If those results use exact top-k (which is feasible at up to 128k with 16GB), the method's behavior under approximate search—and any accuracy degradation it introduces—is uncharacterized. If they use Faiss with approximation, that should be stated.

5. **Figure 8 compares top-k to StreamingLLM but not to full attention at 1M.** The paper shows that StreamingLLM fails at retrieving needles outside the local window, which is informative. However, without a full-attention baseline at 1M, the reader cannot assess how much accuracy is lost by using k=10 versus full attention at this scale. (The authors may be unable to run full attention at 1M on 16GB, but should state this explicitly.)

6. **The sparsity analysis (Figures 2–4) is conducted only on Llama-3-8B with 4000-token Wikipedia articles.** While the later evaluation across model families partially validates the sparsity assumption, the analysis does not examine how sparsity patterns change at longer context lengths (e.g., 128k) or across different models. The paper would be stronger if this analysis were extended to the lengths where the method is actually deployed.

### Trivial
None.

## Nice-to-Haves

- Compare top-k attention against other approximate attention methods (e.g., SnapKV, Keyformer, sliding window) on the RULER benchmark to better situate the method's accuracy–efficiency trade-off.
- Release code or embeddings to facilitate reproducibility and practical deployment.
- Provide a breakdown of which RULER subtasks (NIAH, multi-hop, QA, summarization) drive the performance changes as k varies, since the paper notes (line 140) that QA tasks are "most indicative."

## Removed Points

These points were flagged by reviewers but removed after verification against the paper. Treat them with caution rather than discarding outright.

- **Criticism about the paper not comparing to other methods (SnapKV, sliding window)**: The paper cites these methods in Related Work. Requesting experimental comparisons is a reasonable suggestion but not a weakness—the paper does compare to StreamingLLM, and the other methods are different in character (e.g., SnapKV is a cache-selection method, not a generation-time attention sparsification). Moved to Nice-to-Haves.

- **Criticism about missing code/reproducibility plan**: A reasonable practical suggestion but not a weakness in the scientific content. Moved to Nice-to-Haves.

- **Criticism claiming the 95% figure is claimed "at 1M context"**: The paper does not claim the 95% figure at 1M. The abstract states "achieve over 95% of model performance on common long context benchmarks (LM-Eval, AlpacaEval, and RULER)" without specifying 1M for this claim, and the RULER results in Table 1 (up to 128k) support this. The 1M experiment is presented separately as a feasibility demonstration. The misattribution was not included in the final review.

- **Criticism about "sublinear runtime" being imprecise due to cache construction cost**: The paper acknowledges the cache construction cost explicitly in Section 3.4 and discusses how it could be addressed. The "sublinear" claim applies to per-token generation cost (retrieval over a vector index), which is a reasonable characterization. WEAKENED to Minor.

## Novel Insights

None beyond the paper's own contributions. The reviews converge on the same observations that the paper itself makes: the key insight is the empirical finding that very few keys suffice for near-full attention performance, and this can be exploited for efficient long-context inference. The primary novel contribution of the reviews is identifying that the paper's efficiency claims are not backed by measurements.

## Suggestions

1. **Report efficiency numbers.** Add a table showing (a) generation latency (ms/token) at 4k, 32k, 128k, 512k, and 1M for top-k (various k) and, where possible, full attention; (b) peak GPU memory at those lengths; (c) the context length at which full attention on the same 16GB GPU becomes infeasible. Without these, the paper's title claim is unsubstantiated.

2. **Specify the cache construction method for the 1M experiment.** State explicitly whether the 1M KV cache was built using full attention (on what hardware), vLLM, windowed attention, or some other method, and report the GPU memory used during construction.

3. **Clarify exact vs. approximate search.** State for each experiment (RULER tables, AlpacaEval, OpenLLM) whether exact top-k or approximate (Faiss) search was used. If exact was used for shorter contexts, include an ablation showing accuracy degradation when switching to approximate at the same k.

4. **Broaden the 1M evaluation.** Run at least the multi-needle and multi-hop NIAH variants from RULER at 1M to demonstrate that the method supports more than basic single-needle retrieval at scale.

5. **Include a full-attention baseline in Figure 8.** State whether full attention at 1M on 16GB is possible, and if not, explain why. Show the needle-success rate of full attention at shorter lengths where it fits, and extrapolate.

## Score and Decision

**Originality**: Moderate. The core idea (top-k attention via vector search) has been explored before (Gupta et al., 2021; Klett & Ahle, 2024), but scaling it to 1M tokens on a single GPU is the claimed novel contribution.

**Importance of research question**: High. Enabling long-context inference on inexpensive hardware is practically important.

**Claims well-supported**: Partially. The accuracy preservation claim is well-supported up to 128k across multiple benchmarks and models. The efficiency claim (sublinear, tiny GPU) is asserted but not supported by any measurements. The 1M claim is demonstrated only for a single simple task.

**Soundness of experiments**: Moderate. The benchmark methodology is sound but critically incomplete—the absence of runtime/memory measurements makes it impossible to evaluate the paper's central efficiency claims.

**Clarity of writing**: Good. The paper is clearly written and well-structured.

**Value to the research community**: Potentially high, contingent on the authors providing the missing efficiency evaluations. The core finding (attention is extremely sparse) is valuable regardless.

The paper makes a plausible contribution with clean accuracy evaluations up to 128k, but it cannot be accepted in its current form because the efficiency claims that distinguish it—sublinear runtime, operation on tiny GPUs at million-token scale—are asserted without any runtime or memory measurements. This is not a minor omission; it is the central missing piece of evidence for the paper's headline claim.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>