Now I have all the information I need. Let me synthesize the final review.

## Summary

QUOKA proposes a training-free, hardware-agnostic sparse attention method for chunked prefill. It operates in three steps: (1) subselecting queries that are cosine-dissimilar to the mean query, (2) scoring keys via cosine similarity against the selected queries, and (3) group-aware aggregation for GQA models. The reduced KV set is then fed to standard dense attention kernels. The paper evaluates on NIAH, RULER, LongBench, and Math500 across six model families and reports up to 5× attention speedups and 3× TTFT improvements.

## Strengths

- **Clean, practical algorithm design.** The three-step pipeline (query subselection → cosine-similarity scoring → group-aware aggregation) is well-structured and implementable with standard linear algebra. The use of cosine similarity (normalized dot product) rather than raw dot products is sensible for cross-query aggregation, and the pre-aggregation trick for GQA heads reduces computation without sacrificing accuracy. The algorithm is training-free and compatible with FlashAttention and other dense kernels.

- **Consistently large accuracy margins over baselines on long-context benchmarks.** On RULER (Table 1) with 1,024 budget, QUOKA achieves 57.01 on Llama3.2-3B at 32k, while the next best method (SparQ) reaches 31.14 — a ~26-point gap. On LongBench (Table 3), QUOKA achieves normalized accuracies of 0.94–1.0 across models while all baselines stay below 0.91. Even at aggressive sparsity (25% of cache), QUOKA incurs <3% accuracy loss across six model families (Table 2).

- **Hardware-agnostic speedups validated on diverse platforms.** Speedups are demonstrated on Nvidia A100 (5× attention, 3× TTFT), Intel Xeon W-2125 CPU (~7×), and Nvidia RTX 2080 consumer GPU (5–6×). Because QUOKA relies only on standard linear algebra rather than custom CUDA kernels, these speedups transfer across hardware, which is a genuine practical advantage over kernel-level sparse attention methods.

- **Generalization across diverse model architectures.** Evaluated on Llama3, Qwen2.5, Qwen3 (including MoE variant Qwen3-30B-A3B), SmollM3, and GPT-OSS-20B — covering RoPE, NoPE, and MoE architectures. The method shows consistent behavior across these families (Table 2), suggesting the geometric intuition generalizes beyond a single architecture.

- **Well-designed ablation on compression ratio (Table 2).** Showing accuracy loss at 25% budget across multiple models at multiple lengths is the most convincing evidence in the paper that QUOKA degrades gracefully under increasing sparsity.

## Weaknesses

### Fatal

None.

### Major

- **The core geometric claim is supported by only a single data point and conflates peak attention with attention breadth.** The paper's entire method rests on the claim that "queries with lower cosine similarity to the mean query attend to the majority of keys" (line 41). This is supported only by Figure 2, which shows data from a *single layer and single head* of one model (Llama 3.2-3B-Instruct, layer 0 head 11). No systematic evidence across layers, heads, or models is provided. Furthermore, the actual measurement in Figure 2c is a 0.737 correlation between S_q and log(max_k(A)) — this measures *peak* attention (does the query strongly attend to *any* key), not *breadth* of attention (does the query attend to *most* keys). The paper's title claim ("attend to the majority of keys") is not what is measured. This is not fatal — the method works well empirically — but it means the stated motivation is significantly weaker than advertised.

- **QUOKA exceeds full attention (score > 1.0) on LongBench for Smollm3 without explanation.** In Table 3, QUOKA achieves 1.03 and 1.028 normalized accuracy for Smollm3 at B_SA=1024 and 2048. Similarly, Math500 results (Section 4.4) mention surpassing dense attention "in some cases." Any sparse method outperforming the dense baseline is anomalous and demands an explanation — it could indicate a bug in the dense baseline, that chunked prefill harms dense attention in ways QUOKA mitigates, or noise reduction from sparsity. The paper does not discuss this. Until resolved, it undermines confidence in the experimental framework.

- **SnapKV and KeyDif appear as baselines in Table 1 but are never described in the paper.** Section 4 lists only SampleAttention, LessIsMore, SparQ, and Loki as the compared sparse attention methods. SnapKV and KeyDif appear without any description of how they were configured, what budget settings were used, or why they were included. This makes it impossible to assess whether the comparison is fair.

- **The TTFT speedup (3×) is not obviously consistent with the attention speedup (5×).** The paper states that chunked prefill accounts for >70% of total runtime, but does not state what fraction of prefill time is attention. If attention is ~70% of prefill, a 5× attention speedup yields ~2.3× overall TTFT improvement (using standard Amdahl's law), not 3×. If attention is a larger fraction, that should be stated. Without a latency breakdown, the relationship between these two headline numbers is unclear.

### Minor

- **Theorem 1 (Section 3.1) is sloppily stated.** The variable q* appears in the bound (Eq. 5) but is never defined — the theorem introduces q_0 but then uses q*. The condition α_q < 0 (mean query has *negative* cosine similarity to every key) is a strong assumption that is never empirically checked. The theorem's connection to the actual geometry of LLMs is asserted but not demonstrated.

- **No latency breakdown of QUOKA's components.** The paper reports end-to-end speedups but never decomposes QUOKA's runtime into selection overhead (mean computation, cosine similarity, top-k) vs. attention computation. On CPU where top-k can be expensive, this matters. Providing a breakdown would strengthen the latency claims.

- **The `q*` notation and the theorem's framing are confusing.** The reader cannot connect the theorem's bound to the actual selection rule without guessing at the missing variable definition. This is a presentation issue but should be fixed.

### Trivial

None that survive filtering.

## Nice-to-Haves

- A random-query-subselection ablation would help isolate the benefit of the cosine-dissimilarity rule. (SampleAttention already provides a form of this, though it uses uniform random query sampling for scoring rather than query subselection — clarifying the distinction would help.)
- Query-key similarity heatmaps (analogous to Figure 2a) comparing QUOKA's selected subset to the full attention pattern would provide qualitative validation.
- A case study on a RULER or LongBench task showing where QUOKA succeeds and a baseline fails would illustrate the practical benefit.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The proof is in the missing appendix, so the reader cannot evaluate it."** — The appendix was stripped by the parser; the original submission contains it. Removed per hard rules.
- **"LoLi typo for Loki."** — Typo/formatting artifact. Removed per hard rules.
- **"TTFT is plotted for QUOKA vs. dense only (Figure 5b)."** — The figure description explicitly states five methods are compared in subplot (b). This claim is factually incorrect. Removed.
- **"Selection overhead is not accounted for... the paper never states whether selection time is included."** — The speedup numbers are for the full QUOKA method (Algorithm 1), which includes all selection operations. Overhead is inherently accounted for in the reported timings. Removed.
- **"Baseline asymmetry: Loki/SparQ use 64 dimensions while QUOKA keeps full dimension."** — This is how those methods are defined in their original publications; it is not an unfair configuration chosen by the authors. Removed.
- **"Missing related works."** — Per instructions, I cannot confirm the existence of missing references. Removed.
- **"Pre-aggregation is not exact."** — The critic acknowledges the implementation is correct and the explanation is only "slightly imprecise." This is a presentation nuance rather than a genuine error. Removed.
- **"Demand random query subselection baseline"** — SampleAttention already serves this role. Removed to avoid duplication.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a novel interpretation of the method that the paper itself does not provide.

## Suggestions

1. **Validate the geometric claim systematically across layers, heads, and models.** Provide a figure showing the correlation between S_q and (a) max attention and (b) attention breadth (e.g., number of keys with weight > ε) for multiple layers, heads, and at least 2–3 models. This directly addresses the most serious concern about the paper's motivation.

2. **Explain the >1.0 LongBench results.** Either demonstrate that the dense baseline has a reproducible bug, explain how QUOKA's sparsity provides a denoising benefit, or add a caveat to the claim. This is essential for the results to be trusted.

3. **Describe all baselines appearing in the main tables.** SnapKV and KeyDif should either be described or their appearance in Table 1 should be justified with a reference and configuration details.

4. **Provide a latency breakdown** decomposing QUOKA's runtime into query subselection, cosine-similarity scoring, top-k selection, and attention computation. This would clarify the overhead and help the community understand where optimization effort should focus.

5. **Fix the notation in Theorem 1.** Define q* explicitly and clarify the relationship between q_0 and q*.

## Score and Decision

**Anchor comparisons (calibration batch):**

| Anchor | Avg Score | Comparison to QUOKA |
|--------|-----------|---------------------|
| SparseSkeleton (Y5kgP4x20k) | 2.67 | Much weaker: no wall-clock speedups, single model, less convincing results. QUOKA is substantially stronger. |
| ILRe (GiI6tPrPAG) | 2.00 | Significantly weaker: unclear presentation, limited experiments. QUOKA is far more rigorous. |
| TFCA-Attention (0lGVMSAazo) | 3.50 | Similar topic (training-free sparse prefill) but weaker latency gains and narrower evaluation. QUOKA is stronger. |
| CSAttention (CEpNboUJyw) | 4.00 | Similar method family. CSAttention has prefill overhead and memory concerns; QUOKA's algorithm is cleaner but its core motivation is less validated. Comparable quality. |
| SALE (yTeDQeuKKz) | 4.00 | Custom-kernel approach with narrower evaluation. QUOKA has broader model coverage and hardware portability. |
| LessIsMore (3iwDzfIk60) | 5.00 | Comparable: both are training-free sparse attention with strong empirical results. LessIsMore targets generation; QUOKA targets prefill (arguably harder). Similar quality level. |
| ASEntmax (PsB6Lynznk) | 6.50 | More theoretically rigorous with formal guarantees. QUOKA is more empirically driven. ASEntmax is a stronger paper overall. |

**Final score and decision:** QUOKA presents a clean, practical algorithm with convincing empirical results on multiple benchmarks and hardware platforms. Its accuracy margins over baselines are genuinely large. However, the core geometric motivation is insufficiently validated (single data point), there is an unexplained anomaly (exceeding full attention), and the baseline descriptions are incomplete. These are real issues but addressable. The paper is comparable in quality to the 5.0-scored LessIsMore paper. I recommend a borderline decision — the contribution is worthwhile but needs strengthening before acceptance.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>