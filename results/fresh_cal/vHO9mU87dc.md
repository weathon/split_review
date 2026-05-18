Now I'll compose the final consolidated review.

## Summary

ShadowKV is a high-throughput long-context LLM inference system that reduces GPU memory by storing a low-rank decomposition of pre-RoPE keys on GPU while offloading values to CPU. During decoding, it uses chunk-based landmarks and outlier detection to select minimal sparse KV pairs (≈1.56%) for attention, and employs CUDA multi-streams to overlap key reconstruction (from low-rank factors) with value fetching over PCIe. Across models (Llama-3.1-8B, Llama-3-8B-1M, GLM-4-9B-1M, Yi-9B-200K) and benchmarks (RULER, LongBench, NIAH), ShadowKV maintains accuracy while supporting up to 6× larger batch sizes and boosting throughput by up to 3.04× on an A100, even exceeding the theoretical throughput limit of full-attention with infinite GPU memory.

## Strengths

1. **Novel and well-motivated combination of low-rank key compression + value offloading.** The observation that pre-RoPE keys are substantially more low-rank than post-RoPE keys, values, or weight matrices (Figure 1a) is clearly demonstrated and directly inspires the system design. The insight that a sequence and its continuation share low-rank subspaces (Figure 1b) justifies storing only the low-rank factors per sequence. This is a physically grounded approach to the long-context memory bottleneck.

2. **Strong accuracy preservation across diverse models and tasks.** With only 1.56% sparse budget, ShadowKV matches or exceeds full-attention accuracy on RULER (86.88% vs. 86.68% for Llama-3-8B-1M), LongBench (39.94% vs. 39.86%), and the Needle In A Haystack test, across models with up to 1M context windows. It substantially outperforms both Quest and Loki at the same sparse budget (e.g., 86.88% vs. 82.03% and 9.33% on RULER for Llama-3-8B-1M). The multi-turn NIAH experiment (Figure 4) further demonstrates robustness against information loss that plagues eviction-based methods.

3. **Substantial and well-measured throughput gains on real hardware.** Table 3 reports end-to-end generation throughput on an A100 showing 3.04× improvement for Llama-3.1-8B at 122K context (245.90 vs. 80.78 tokens/s), with consistent gains across models (2.56–2.97×) and context lengths (60K–244K). The batch size scaling from 4→24 for Llama-3.1-8B at 122K directly demonstrates the memory reduction benefit.

4. **Theoretical equivalent bandwidth analysis provides explanatory framework.** Section 4.2 derives an equivalent bandwidth of 7.2 TB/s (3.6× A100 memory bandwidth), explaining how sparse attention + value offloading can surpass the theoretical full-attention throughput limit. This calculation is transparent and parameterized (chunk size, budget, hit rate, etc.).

5. **Thorough ablation studies.** The paper ablates sparse budget (vs. Quest across budgets), chunk size (accuracy vs. batch size trade-off), and rank (accuracy stabilization at rank 160), providing practical guidance for deployment.

## Weaknesses

### Fatal
None.

### Major

1. **The central latency-hiding mechanism (CUDA multi-streams overlapping key reconstruction with value fetching) is asserted without any empirical validation.** The paper states that key reconstruction from low-rank factors (a matrix multiplication of shape `Gather(A,I) @ B`) is overlapped with PCIe value fetching, and that this "conceals" reconstruction overhead. However, no profiling, latency breakdown, microbenchmark, or scaling analysis is provided to confirm that (a) the overlap actually occurs in practice, (b) reconstruction is not itself a bottleneck, and (c) the 2× overhead reduction claim (line 42) is realized. This mechanism is central to the throughput claims — if reconstruction becomes the bottleneck, the equivalent bandwidth formula (which assumes perfect overlap) overstates the gain. The paper must provide an empirical decomposition of decoding-step latency (landmark scoring, key reconstruction, value fetching, sparse attention) to validate this claim.

2. **SVD pre-fill overhead is dismissed without reporting absolute wall-clock times.** The paper states the "linear cost of low-rank decomposition during pre-filling is negligible" (line 42), citing Figure 1(c) which shows relative overhead decreasing with sequence length. However, absolute overhead matters for realistic workloads: computing a (randomized) SVD of a 128K×4096 matrix per layer at pre-fill time imposes non-trivial latency for first-time requests. The asynchronous/prefix-cache mitigation (footnote 1) does not eliminate this for cold-start requests. Wall-clock pre-fill times should be reported across sequence lengths and compared against the decoding throughput gains.

### Minor

1. **Throughput evaluation compares only against full-attention baselines, not against other sparse methods with offloading.** The efficiency results (Table 3) compare ShadowKV against full attention at various batch sizes plus a theoretical infinite-memory bound. However, there is no throughput comparison against Quest or Loki with CPU offloading (the accuracy section does include these baselines, but not for throughput). Such a comparison would isolate the benefit of ShadowKV's specific design choices (low-rank keys + chunk-based selection) from the general benefit of sparsity + offloading. While this omission does not invalidate the results, it limits the reader's ability to assess the marginal contribution.

2. **Ambiguous baseline specification for accuracy comparisons.** The paper states baselines use "computation cost set to 1/16 of full attention for selecting sparse KV pairs" (line 276). This is ambiguous: does "1/16 computation cost" mean 1/16 of the KV cache is selected (6.25% density) or 1/16 of the attention compute budget is spent on the selection mechanism? The table caption states a 1.56% budget for ShadowKV, but the baseline budgets are not explicitly stated in comparable terms. Furthermore, Loki's catastrophic failure at this sparse budget (9.33% on RULER for Llama-3-8B-1M) is unsurprising — Loki is designed for 10–20% density regimes — making the comparison against it less informative. The comparison would be strengthened by including baselines at their recommended or best-performing budgets.

3. **Low-rank property demonstrated for only one model at the observational level.** The singular-value decay analysis (Figure 1a) is shown for Llama-3.1-8B on one PG-19 sample. While the downstream accuracy results across many models indirectly validate that low-rank compression works broadly, showing singular-value distributions for additional models (e.g., GLM-4-9B-1M, Yi-9B-200K) would strengthen the generality claim. Similarly, the subspace similarity analysis (Figure 1b) is shown for one layer; persistence across layers is relevant for the design.

4. **No total GPU memory breakdown.** The paper claims 6× KV cache memory reduction but does not report total GPU memory usage of the full system (low-rank factors A, B, landmarks, outliers, model weights, activations). Without this, the claim of "up to 6× larger batch sizes" is not directly verifiable from the reported numbers — the effective batch size multiplier depends on how much GPU memory is consumed by non-KV-cache components.

5. **Method scope limited to RoPE-based models without discussion.** The approach explicitly relies on pre-RoPE key low-rankness. The paper does not discuss whether similar properties hold for models using other positional encodings (AliBi, NoPE, etc.), which would affect the method's applicability.

6. **No throughput-accuracy trade-off curves varying rank.** The ablation on rank (Figure 5c) shows accuracy stabilizing around rank 160 but does not show the corresponding impact on throughput. Since higher ranks increase reconstruction cost, a trade-off curve (accuracy vs. throughput for different ranks) would be more informative for deployment decisions.

### Trivial
- The "1/16 computation cost" phrasing in the baseline setup is genuinely ambiguous and should be clarified (e.g., specifying the token/page budget for each baseline).

## Nice-to-Haves
- A profiling breakdown of the decoding step: time spent on (a) landmark score computation, (b) key reconstruction (with CUDA stream overlap measurement), (c) value fetch over PCIe, (d) sparse attention computation, and (e) the cache-aware kernel hit rate and its overhead reduction.
- Wall-clock pre-fill times (including SVD) at various sequence lengths to quantify the one-time cost.
- Throughput comparison against Quest/Loki with offloading at matching batch sizes.
- Error bars or multiple-run statistics for accuracy results (common in LLM evaluation but would increase confidence).
- Discussion of applicability to non-RoPE positional encodings.

## Removed Points

- **Hit rate "adopted without validation" (Harsh Critic, Observations section):** The critic claims the 60% hit rate figure is "adopted without validation on these models/tasks" and speculates it comes from PQCache. This is factually incorrect — the paper's own ablation study (Section 5.3, Figure 5b) empirically shows the chunk hit rate is ~60% and discusses how chunk size minimally affects it. The paper cites PQCache for the *cache policy implementation*, not for the hit rate measurement.

- **"Infinite batch size" comparison is "apples to oranges" (Harsh Critic, Critical Issue 2):** The critic claims comparing ShadowKV against infinite-batch full attention is misleading. This comparison is standard and meaningful: it shows that ShadowKV's effective bandwidth (via sparsity + offloading) exceeds the theoretical memory-bandwidth limit of full attention. The baseline is explicitly defined as "leveraging A100's theoretical memory bandwidth (2 TB/s) for attention computations" — it is a theoretical upper bound, not a practical system claim. This comparison strengthens rather than weakens the paper.

- **Missing appendix content (Harsh Critic):** The critic notes that the cache-aware kernel implementation is "deferred to appendix (which was not provided)." Per the review guidelines, appendix stripping by the parser is not an author error; criticisms about missing appendix content should be removed.

- **Speculative fatal claim about reconstruction becoming the bottleneck (Harsh Critic, Critical Issue 1):** The critic asserts that reconstruction "involves a matrix multiplication...which is non-trivial compute" and speculates this could be a bottleneck. While the lack of empirical validation is a legitimate weakness (kept as Major above), speculating about specific failure modes without evidence should not be elevated to a fatal claim. The weakness is the *missing evidence*, not the hypothetical failure.

## Novel Insights

None beyond the paper's own contributions. However, the review process surfaces an interesting tension: the community has been developing sparse attention methods (Quest, Loki, TriForce) and offloading methods (FlexGen, InfiniGen) largely separately. ShadowKV's key insight is that the low-rank structure of pre-RoPE keys allows a *hybrid* strategy — keep compressed keys on GPU, offload values — that neither pure-sparsity nor pure-offloading approaches exploit. This specific observation (pre-RoPE keys are uniquely low-rank among cache components) and its system implication (reconstruct keys cheaply while fetching values) is the paper's genuine contribution.

## Suggestions

1. **Add a decoding-step profiling breakdown** showing wall-clock time for each sub-operation (landmark scoring, key reconstruction, value fetch, sparse attention) with and without the multi-stream overlap. Include a comparison against a non-overlapped version to justify the "2× overhead reduction" claim.
2. **Report absolute pre-fill SVD times** for at least the sequence lengths tested (60K, 122K, 244K) and discuss the practical impact on cold-start latency.
3. **Include a throughput comparison against Quest with value offloading** to isolate the benefit of the low-rank key design from general sparsity + offloading.
4. **Clarify the baseline specification** in Section 5.1: state the exact sparse budget (token count or percentage) used by each baseline method, not just the "1/16 computation cost" proxy.
5. **Provide a memory usage breakdown** showing total GPU memory consumed by ShadowKV components (factors A, B, landmarks, outliers, weights, activations) vs. full-attention baselines.
6. **Add a trade-off plot** showing throughput (y-axis) vs. rank (x-axis) alongside the existing accuracy vs. rank plot, to help readers navigate the accuracy-speed trade-off.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>