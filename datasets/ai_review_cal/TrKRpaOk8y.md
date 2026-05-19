- Decision: Accept
- Avg Score: 6.40
- Scores: 6, 6, 6, 8, 6
Now I have all the information I need. Let me construct the final consolidated review.

## Summary

This paper proposes \name, which integrates long-context length-extension training with a GPU-friendly sparse attention architecture. It fine-tunes a pretrained LLM (Llama-2 7B and 70B) into a hybrid model where 1/3 of layers (placed in the middle) retain full attention and the remaining 2/3 use either attention-sink or blockwise-strided sparse patterns. Evaluated on NIAH, BABILong, and RULER, \name closely matches full-attention performance while achieving 1.55× training speedup, 62% KV cache reduction, and measurable inference speedups.

## Strengths

- **Training-time integration of sparse patterns demonstrably outperforms post-hoc KV eviction.** Table 1 (line 244) shows inference-time methods (Attention Sink 28%, H2O 32%, RazorAttention 46%, PyramidKV 51%) all underperform dramatically on NIAH, while \name achieves 100%. This direct comparison (Figure 3) provides key evidence that post-hoc cache reduction without architecture adaptation is insufficient for long contexts — a clean and well-supported finding.

- **Hybrid architecture closely matches full-attention performance while delivering substantial efficiency gains.** Table 5 (line 306–312) reports \name-7B: NIAH=100%, BABILong=0.27, RULER=0.38 vs Full-Attention-7B (0.29, 0.41); at 70B the gap narrows further (BABILong 0.46 vs 0.46). These are paired with measured 1.55× training speedup, 62% KV reduction (from 69.2 GB to 26.5 GB), 1.67× prefilling speedup, and 1.41× decoding speedup (Figure 2). The efficiency-performance trade-off is convincingly documented.

- **Systematic ablation identifies optimal placement (middle layers) and fraction (1/3) of full attention layers.** Tables 6 and 7 (shown as figures, described in Sections 4.3.1–4.3.2) show that stacking full layers in the middle substantially outperforms top/bottom/interleaved placements, and that 1/3 full layers provides a principled trade-off. This ablation directly informs the final design and gives the paper practical value beyond a single configuration.

- **Lightweight 5B-token training budget makes the approach accessible.** Section 4.1 reports that post-training consumes only 0.2% of the pretraining corpus (74 GPU hours for 7B), referencing the data-balancing approach of Fu et al. 2024. This concretely supports the claim that integrating efficient architecture reduces length-extension cost.

- **Evaluation includes discriminative reasoning benchmarks beyond simple retrieval.** The paper evaluates on BABILong (multi-hop reasoning, Table 4) and RULER QA subtasks, providing a more demanding test than needle-in-a-haystack alone. This strengthens the evidence that the method preserves reasoning capability.

## Weaknesses

### Fatal
None.

### Major

- **Insufficient implementation details for the sliding window and YOCO training baselines.** The paper includes these as "long context training methods" in Table 1 and claims superiority (100% vs 48% for sliding window, 88% for YOCO), but does not describe how these baselines were adapted and trained. For sliding window: what window size was used, and was it trained on the same 5B tokens with the same hyperparameters? For YOCO: the paper itself acknowledges in Related Work (line 410) that "it's unclear how to use the architecture in context extension, as it diverges significantly from default decoder-only models," yet includes it as a baseline without explaining how this architectural gap was bridged. Without these details, readers cannot assess whether the performance gap is meaningful or an artifact of the baseline setup. The core claim of the paper does not rest on this comparison alone (the comparison to inference-time methods and full attention is more central), but the paper explicitly asserts "Among the long context training methods, \name uniquely achieves perfect needle retrieval results" (line 288), which requires credible baselines to support.

### Minor

- **No variance or significance estimates reported for any metric.** The paper reports BABILong accuracy values like 0.27 vs 0.29 (name vs full attention at 7B) without standard deviations or confidence intervals. Given how close these numbers are, the reader cannot assess whether the gap is statistically meaningful. The paper does average over 3 seeds for BABILong (line 268), which is good, but does not report the resulting variance.

- **Inference evaluation is limited to single-sequence latency.** The paper measures prefilling and decoding speedup on a single 128K sequence with TP=4 (line 348). In production, long-context inference often involves batching, where KV cache reduction translates to larger batch sizes and higher throughput. The claimed inference gains are valid for the reported setting, but the practical system-level benefits under realistic serving conditions (e.g., concurrent requests, throughput under memory pressure) are not demonstrated.

- **The training speedup claim could be better contextualized.** The paper reports 1.55× wall-clock speedup (line 341), which is far below the theoretical FLOPs reduction (~3× for 1/3 full layers). The gap is attributed to overhead, but no decomposition (e.g., communication vs. compute vs. kernel launch) is provided. This does not invalidate the result but makes it harder for readers to assess where the efficiency ceiling lies and how it scales to different configurations.

### Trivial

- The paper could more explicitly state that the baseline full-attention training used the same parallelism settings (TP=8, distributed optimizer, activation checkpointing) for a clean speedup comparison. This is the natural reading but stating it explicitly would remove ambiguity.

## Nice-to-Haves

- A brief discussion of limitations would improve the paper — e.g., acknowledging that sparse patterns may not be optimal for tasks requiring dense reasoning over the full context, or that the small gap to full attention on BABILong may widen in more demanding settings.
- The "GPU-friendly memory access" claim could be supported with simple profiling metrics (e.g., GPU utilization, SM occupancy) rather than just wall-clock speedup, though the latter is sufficient for the main claims.

## Removed Points

These points were raised by reviewers but are removed after cross-checking against the paper. Treat with caution:

- **"The KV cache budget comparison is ambiguous because budgets are not explicitly stated per method."** The paper states at line 117: "For fair comparison, we keep the same KV cache budget for Attn Sink, PyramidKV, and \name, i.e., 60% of the original full transformer." And at lines 282–283: "we maintain consistent KV cache budgets across all methods... KV budgets may fluctuate by approximately 5%." For their own method, the paper gives the exact budget: ~2K retained tokens for a 128K sequence (line 235). The ambiguity concern is addressed.

- **"The paper should specify block size, stride, and rollback buffer details."** These ARE specified: "Each kernel block handles 64 tokens" (line 232); "For name with attention sink, we retain the first block for sink tokens and the most recent 32 blocks for local context" (line 233); "for name with block sparse, we set the stride length as 64 blocks" (line 234). The details are present.

- **"No analysis of which layers become full."** The paper conducts an entire ablation on layer position (Table 6, Section 4.3.1), showing middle placement is optimal, and cites prior work on middle-layer specialization. A full attention-map visualization would be a nice addition but is not missing analysis of "which" layers.

- **"The GPU-friendly memory access claim is not validated."** The paper provides wall-clock speedup measurements (Figure 2), which is the standard and most practically relevant validation. Additional profiling would be a nice-to-have.

- **"The paper overstates the novelty of the sparse patterns."** The paper does not claim novelty of the patterns themselves. The contribution is in the training integration and hybrid placement (stated explicitly at lines 71–74): "we conduct context extension with various GPU-friendly KV cache-saving designs" and "uses this sparse attention in a hybrid architecture." The paper correctly cites prior work for the individual patterns.

- **"Speedup baseline settings are unclear."** The paper states: "We measured the latency of training a Llama2-7b model on 128K sequence length with 256 A100-80G GPUS. We set tensor parallel size as 8 and use distributed optimizer and checkpoint activation" (lines 337–338). The natural reading is that both name and full-attention were measured under identical settings. The critic's speculation about different batch sizes is not supported by the text.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Provide implementation details for the sliding window and YOCO baselines** — or, if these comparisons are secondary to the paper's core claims, consider moving them to the appendix and de-emphasizing the "uniquely achieves perfect needle retrieval" claim about training methods.
2. **Add standard deviations or confidence intervals** to the BABILong and RULER results, especially where the gap to full attention is small (e.g., 0.27 vs 0.29).
3. **Expand the inference evaluation** with a brief analysis of how the 62% KV cache reduction translates to batch throughput or serves under memory-constrained settings.
