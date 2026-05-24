Now let me write the consolidated review.

## Summary

QUOKA introduces a training-free, hardware-agnostic sparse attention method for chunked prefill in LLMs. It selects representative queries (those with low cosine similarity to the mean query) and then subselects keys most aligned with those queries using max-pooled cosine similarity, reducing the KV cache before feeding into a dense attention kernel. The method achieves near-baseline accuracy on RULER, LongBench, NIAH, and Math500 while delivering up to 5× attention speedup and 3× TTFT reduction on GPUs, and up to 7× on CPUs.

## Strengths

1. **Strong empirical accuracy under high sparsity, across many models**: On RULER (Table 1) with B_SA=1024, QUOKA outperforms all six baselines by 10–20+ absolute points across five LLM families (Llama3, Qwen2.5, Qwen3, SmollM, GPT-OSS) at sequence lengths from 4K to 32K. On Llama3.2-3B at 32K, QUOKA scores 57.01 vs. the next-best 31.73 — nearly 2× the competitor's score. This is the paper's single strongest piece of evidence.

2. **Substantial, measured latency reduction on diverse hardware**: Figure 5 reports relative speedups vs. dense FlashAttention on NVIDIA A100 (∼5× attention, ∼3× TTFT), Intel Xeon CPU (∼7×), and RTX 2080 (∼5–6×) at long sequence lengths. The speedups are consistent with the sparsity ratios being used.

3. **Clean, portable design**: QUOKA relies entirely on standard linear algebra (cosine similarity, top-k, mean pooling) — no custom CUDA kernels, no training, no profiling stage. The pre-aggregation trick for GQA (averaging normalized queries across KV groups before scoring, Section 3.3) is a concrete, implementable efficiency enhancement.

4. **Thorough hyperparameter robustness**: Ablations over B_CP, B_SA, and N_Q (Tables 5, 6, 11, 12) show gradual accuracy degradation as sparsity increases, with less than 3% drop using only 12% of KV tokens. This supports practical deployability under varied constraints.

5. **Generalization to generation**: While the paper's focus is prefill, QUOKA also outperforms a generation-specific sparse attention method on Math500 (Table 8), demonstrating versatility beyond its primary target.

## Weaknesses

### Fatal

None.

### Major

1. **Baseline adaptation fairness**: The paper compares against methods (SparQ, Loki, LessIsMore, SnapKV, KeyDif) that were designed for single-query generation. The paper acknowledges (Section 2.4) that naively extending them to multiple queries via averaging degrades performance. However, no attempt is made to adapt these baselines to the prefill setting with better aggregation (e.g., max-pooling, or the authors' own query subselection) before comparing. While the comparison against SampleAttention — which IS designed for prefill — is fair and QUOKA wins convincingly (e.g., 57.01 vs. 31.73 at 32K on Llama3.2-3B), the broader comparison set may be under-optimized. The reported gaps of 10–20% on LongBench could partly reflect suboptimal baseline extension rather than pure superiority of QUOKA's mechanism.

2. **Selective attention budget B_SA not reported for latency experiments**: Section 4.6 and Figure 5 report speedups but never state the B_SA value used. The caption specifies B_CP=128 but omits B_SA. Since speedups are directly proportional to the sparsity ratio, the reader cannot assess whether the reported ∼5× speedup comes from a very aggressive budget (e.g., B_SA=256) or a moderate one. This is a significant reproducibility gap.

### Minor

1. **Theoretical grounding (Theorem 1) does not carry weight**: Theorem 1 depends on conditions (β_q > 0, α_q < 0) not shown to hold broadly, involves unknown quantities, and does not directly connect to the actual selection criterion S_q = –CosSim(M_Q, q*). The method stands on its strong empirical evidence (Figure 2 correlation of 0.737), but the theorem is overclaimed as formal justification.

2. **Overhead breakdown not reported**: The latency speedups (Figure 5) include selection overhead but do not separate it from the attention savings. Without absolute latencies or a breakdown, the reader cannot assess whether overhead dominates at short sequence lengths or small chunk sizes.

3. **SnapKV and KeyDif appear in RULER results (Table 1) but are not introduced in the baselines section (Section 4)**: The baseline list describes only SampleAttention, LessIsMore, SparQ, and Loki. SnapKV and KeyDif are used in Table 1 without explanation of how they were configured or extended to prefill.

4. **QUOKA exceeding dense baseline on Smollm3**: Table 3 reports normalized accuracy of 1.03 and 1.028 on Smollm3 with B_SA=1024 and 2048, meaning QUOKA surpasses full attention. The paper mentions this only briefly; a clearer discussion of whether this is variance, a regularizing effect of sparsity, or a benchmark artifact would improve confidence.

5. **Figure 2 limited to one layer/head**: The empirical motivation (correlation of S_q with max_k(A)) is shown for only layer 0, head 11 of Llama 3.2-3B. The paper does not demonstrate that this relationship holds across layers and heads.

6. **"88% fewer KV pairs" in abstract is ambiguous**: The fraction depends on context length and budget. At 4K with B_SA=1024 the reduction is ∼75%; at 32K it is ∼97%. The headline figure is unanchored.

### Trivial

None.

## Nice-to-Haves

- Test baselines (at least SparQ or Loki) with max-pooling instead of averaging over queries, to see if the gap to QUOKA narrows.
- Isolate the effect of query subselection by ablating it while keeping all other components fixed — this would directly validate the paper's primary claim.
- Report absolute latencies (ms per token) alongside relative speedups for a few representative sequence lengths.
- Include variance or confidence intervals over benchmark tasks.
- Discuss whether QUOKA is beneficial in the single-chunk (full prefill) setting, since many practitioners use that regime.

## Removed Points

- The harsh critic's claim that "source code is not provided" as a weakness — the paper provides a complete algorithmic specification (Algorithm 1), and code is not required for a training-free method using standard ops.
- "Missing appendix/ablation on B_CP promised in appendix" — appendix content is stripped by the parser; this is not a paper weakness.
- "dim=2 in Algorithm 1 ambiguous" — this is a parser formatting artifact, not a clarity issue in the original submission.
- "Could the method be extended to single-chunk prefill?" — this is outside the paper's stated scope (chunked prefill), and the paper is not required to cover every regime.

## Novel Insights

None beyond the paper's own contributions. The observation that queries with low cosine similarity to the mean query are the most informative for KV selection is the paper's key geometric insight, and the reviews do not add a deeper perspective beyond what the paper presents.

## Suggestions

1. In the latency experiments, explicitly state B_SA and ideally provide a breakdown of selection overhead vs. attention compute time. This would address the most significant reporting gap.
2. Run at least one baseline (e.g., SparQ or Loki) with max-pooling across queries instead of averaging, and report whether the gap to QUOKA narrows. This would substantially strengthen the comparative claims.
3. Add an ablation that keeps scoring and aggregation fixed and toggles query subselection on/off, to directly validate the paper's primary novelty.
4. Clarify the "88% fewer" claim by specifying the context length and budget it refers to.
5. Introduce SnapKV and KeyDif alongside the other baselines in Section 4, and explain how they were configured for the prefill setting.

## Score and Decision

**Round 1 bracketing**: The paper was compared against anchors in [<3.5, 3.5–7.5, >7.5]. Weak anchors (avg 2.0–3.0, Reject/Withdrawn) correspond to lower-quality LLM efficiency papers. Mid-range anchors include HASA (5.0, Reject), RetrievalAttention (5.5, Reject), MoA (5.5, Reject), OmniKV (6.0, Accept Poster), HeadKV (6.5, Accept Poster), Radar (6.6, Accept Poster), ShadowKV (6.75, Reject). Strong anchors (8.0+) are on substantially different topics (Diff Transformer, speculative decoding, sparse autoencoders) and are not directly comparable. Round-1 bracket: [5.0, 7.0].

**Round 2 narrowing**: Inside the bracket, QUOKA is clearly stronger than HASA (training-required, modest speedups, novelty concerns), RetrievalAttention (FlashAttention incompatibility, split reviews), and MoA (complex profiling, only modest speedups). It is comparable to OmniKV (6.0, simpler idea, 1.68× speedup vs. QUOKA's 5× but OmniKV targets decode acceleration), Radar (6.6, both training-free with strong results; Radar has better theory but narrower hardware evaluation), and HeadKV (6.5, head-level compression, accepted poster). Compared to these anchors, QUOKA has the strongest empirical accuracy results (RULER margins are unusually large for this space), the most comprehensive model/hardware coverage, but also the most notable reporting gaps (B_SA omission) and a baseline fairness concern that is real though not fatal.

**Final score**: 6.5. The paper's core contribution — a simple, training-free, geometry-motivated KV selection method for chunked prefill — is well-supported by strong empirical results. The method is clearly effective. However, the baseline adaptation concern and the missing B_SA in latency experiments prevent the case from being airtight. These issues are addressable in revision.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>