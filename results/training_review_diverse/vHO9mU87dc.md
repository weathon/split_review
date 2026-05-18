Now I have all the information needed. Let me produce the final consolidated review.

## Summary

ShadowKV presents a system for high-throughput long-context LLM inference that combines low-rank key cache compression (pre-RoPE keys stored as SVD projections) with value cache offloading to CPU, plus accurate chunk-level sparse attention using landmarks and outlier detection. The evaluation spans six models across RULER, LongBench, and Needle In A Haystack, showing up to 6× larger batch sizes and 3.04× throughput improvement on an A100 GPU while maintaining accuracy within 1–2 points of full attention.

## Strengths

1. **Strong, multi-model empirical validation of accuracy retention under high sparsity.** ShadowKV with a 1.56% sparse budget consistently matches or stays within 1–2 points of full attention on RULER (128K) across Llama-3-8B-1M (86.88 vs. 86.68), GLM-4-9B-1M (85.62 vs. 86.82), and Llama-3.1-8B (83.57 vs. 85.53), while Quest and Loki degrade significantly. On LongBench, ShadowKV averages within 0.1–0.8 points of full attention across all four models — a convincing demonstration that the landmark + outlier selection strategy recovers almost all information with minimal budget.

2. **Substantial throughput gains that surpass the infinite-GPU-memory ideal in several configurations.** On an A100, ShadowKV achieves 245.90 tokens/s for Llama-3.1-8B at 122K context, exceeding the projected throughput of full attention with infinite batch size (134.30 tokens/s). Gains of 2.23–3.04× hold across four models and three context lengths (60K–244K), with the decomposition between batch-size and sparsity effects visible via the "Full Attention (Inf)" column at ShadowKV's batch size.

3. **Well-motivated design grounded in empirical observations.** The paper demonstrates that pre-RoPE keys are the most low-rank among the matrices studied (Figure 1a), that within-sequence low-rank subspaces are similar while cross-sequence ones are not (Figure 1b), that outlier chunks are only 0.2–0.3% (Figure 2b), and that the KV cache has high temporal locality (Figure 2c). These observations directly inform the system's four-component design (low-rank keys, offloaded values, landmarks, outlier cache).

4. **Compatibility with pre-filling acceleration and robustness in multi-turn settings.** ShadowKV integrates with MInference without accuracy loss (Table 4), and maintains performance across multiple conversation turns where eviction-based methods (SnapKV, StreamingLLM) fail (Figure 5) — demonstrating practical deployability beyond single-turn evaluation.

## Weaknesses

### Fatal

None.

### Major

None. The paper's core claims (3× throughput, accuracy retention at 1.56% budget, effective system design) are well-supported by the empirical evidence.

### Minor

1. **Absolute SVD cost for very long contexts is under-quantified.** Figure 1c shows SVD overhead as a fraction of attention computation time, which decreases with sequence length. However, for 1M-token sequences the *absolute* SVD cost on a 1M × 4096 matrix is non-trivial even if the fraction is small. The paper mentions asynchronous offloading to CPU and prefix caching as mitigations but provides no absolute timing numbers, no break-even analysis, and no evaluation of how this cost behaves in multi-batch serving where pre-filling and decoding are interleaved. While this does not invalidate the core claims, it is a gap for a systems paper targeting practical deployment.

2. **No per-model breakdown of GPU memory savings.** The paper repeatedly claims "6× memory reduction" but does not report the exact GPU memory bytes saved by low-rank key compression vs. full key cache, broken down by model, rank, and context length. This would help readers calibrate the memory–accuracy tradeoff and understand how batch-size gains scale across models with different KV head counts and hidden dimensions.

3. **The 60% reduction from cache-aware kernels lacks direct validation.** The paper claims cache-aware CUDA kernels reduce computation and value fetching by 60%, citing temporal locality (Figure 2c hit rate). While the hit rate qualitatively supports this figure, the paper would be strengthened by profiling data (e.g., a latency breakdown or bar chart showing GPU/PCIe timeline overlap) that directly validates the claimed 60% reduction and confirms that CUDA multi-streams effectively overlap key reconstruction with value fetching.

4. **Equivalent bandwidth formula presentation skips intermediate derivation.** The formula in Section 4.2 is mathematically correct (M cancels out in the full derivation, leaving the presented expression), but the presentation omits the step showing that the denominator implicitly carries an M/B_GPU factor. A reader who tries to verify the 7.2 TB/s numeric example directly from the formula without reconstructing the derivation may find the units unclear. Adding a two-line derivation would improve clarity for a broad audience.

### Trivial

1. **Multi-turn needle experiment (Figure 5) is a single curve without confidence intervals or replication.** The trend aligns with the paper's claims, but the lack of error bars makes it difficult to assess whether the reported gap is robust or within noise.

2. **The invariance of hit rate with chunk size is noted but not discussed.** Figure 8b shows hit rate is ~60% across all chunk sizes. The paper observes this but does not discuss why — e.g., whether this implies accuracy drop at larger chunks is driven entirely by poorer landmark approximation rather than cache efficiency. Brief commentary would make the ablation more informative.

## Nice-to-Haves

- A latency breakdown (bar chart or table) for the decoding step showing GPU memory reads, PCIe transfers, key reconstruction, and attention computation — to validate the CUDA multi-stream overlap claim and the 60% cache-kernel reduction.
- Show the singular value spectrum of the value cache explicitly alongside the other curves in Figure 1a. While the paper states this analysis was conducted (Section 3, Observation paragraph), making the value cache curve explicit in the figure and caption would close any ambiguity about the design justification for full value offloading.

## Removed Points

These points were raised by reviewers but are not valid weaknesses of this paper:

- **Equivalent bandwidth formula is "dimensionally inconsistent" / "mathematically incorrect":** REMOVED — the formula is correct. The derivation: total dense bytes = 2MS; sparse time = M/B_GPU × [S/C + 2(K+O)C + (1-α)KC·B_GPU/B_PCIe]; therefore B_equivalent = (2S·B_GPU) / (denominator). M cancels. The critic's claim that M is "missing" or that the units are wrong reflects a failure to trace the derivation. The numerical example (7.2 TB/s) checks out.

- **"No empirical evidence" that value cache is not low-rank:** REMOVED — the paper states in Section 3 ("by conducting SVD on ... the value cache ... we visualize the relative singular value distributions in Figure 1a") and in the Introduction ("pre-RoPE keys are exceptionally low-rank compared to ... values ... as indicated in Figure 1a"). The evidence exists in the figure; the caption simply does not enumerate all curves. At most a caption clarity issue.

- **Throughput comparison "conflates two sources of improvement":** REMOVED — Table 3 provides the decomposition. The "Full Attention (Inf)" column first number projects full-attention throughput *at the same batch size as ShadowKV*, which isolates the sparsity benefit. The "Gain" column shows the combined effect. Both are visible; no conflation.

- **Chunk size hit rate "paper does not comment on this":** REMOVED — the paper explicitly states "the chunk size choice has minimal impact on the chunk hit rate" (Section 5.3). The paper does note the observation.

- **Cache-aware kernel 60% claim "no experimental validation":** REMOVED — the hit rate plot (Figure 2c) provides empirical support for temporal locality. The specific 60% figure is derived from this measured hit rate. A more direct measurement would strengthen but is not absent.

- **Missing related works, formatting/typo nitpicks, reproducibility nitpicks about undisclosed hyperparameters:** REMOVED per policy — these are either parser artifacts or otherwise not valid criticisms.

## Novel Insights

The most interesting observation from the reviews is the tension around the equivalent bandwidth formula: a reader who jumps directly to the formula without tracing the derivation (where M cancels and B_GPU factors are properly handled) can easily conclude the units are wrong. This suggests that even well-motivated readers may find the presentation citation gap a barrier to verification. The paper would benefit from a more explicit walkthrough of the algebraic steps — not because the formula is incorrect, but because the current condensed presentation is fragile to casual reading.

## Suggestions

1. Add a two-line derivation of the equivalent bandwidth formula in Section 4.2 showing B_equivalent = 2MS / (M/B_GPU × [...]) = 2S·B_GPU / [...] to make the cancellation explicit.
2. Profile the decoding step with a latency breakdown (e.g., stacked bar chart showing GPU landmark loading, PCIe value transfer, key reconstruction, attention computation) to validate the claimed overlap and 60% reduction.
3. Report absolute GPU memory savings (in GB) broken down by model, rank, and context length — this is more informative than a single "6×" ratio.
4. Report absolute SVD time for the longest context evaluated (e.g., 1M tokens) to help readers assess the system's applicability to extreme-length scenarios.

## Score and Decision

This paper presents a well-engineered system with strong empirical support across multiple models and benchmarks. The core claims (3× throughput, accuracy retention at high sparsity) are validated. The identified weaknesses are minor and addressable — none threaten the central contribution. The paper should be accepted.

**Score: 7.5**

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>