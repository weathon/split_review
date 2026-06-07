Now I have a clear picture. Let me finalize the comparisons:

**QUOKA vs HiP (6.25)**: QUOKA is clearly stronger — far more comprehensive evaluation (5 model families, 6 baselines, 4 benchmarks vs. mostly MMLU), real hardware speedup measurements across platforms, and the elegant GQA pre-aggregation trick. QUOKA > HiP by a comfortable margin.

**QUOKA vs StreamingLLM (7.50)**: Both are training-free with impactful observations. StreamingLLM's attention sink phenomenon is more novel as a finding, but QUOKA has much more comprehensive evaluation and directly addresses the prefill bottleneck. QUOKA is comparable to StreamingLLM — similar quality tier.

**QUOKA vs FlexPrefill (8.00)**: Both are strong sparse attention methods for prefill. FlexPrefill has a more novel adaptive mechanism; QUOKA has more comprehensive evaluation and the hardware-agnostic dimension. QUOKA's theorem overclaiming is a conceptual weakness that FlexPrefill doesn't have. I'd place QUOKA slightly below FlexPrefill, at ~7.5.

**Final score: 7.5, Accept.**

Now let me write the final review.

## Anchor Summary

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| IntelLLM | 4QWPCTLq20 | 3.00 | R1 | QUOKA much stronger |
| MixAttention | 2DD4AXOAZ8 | 2.00 | R1 | QUOKA much stronger |
| Cascading KV Cache | dSneEp59yX | 6.00 | R1 | QUOKA stronger across all dimensions |
| SwiftKV | z1ohBxWeL2 | 5.50 | R1 | QUOKA stronger (training-free, more models) |
| LazyLLM | am5Z8dXoaV | 5.00 | R1 | QUOKA stronger (more comprehensive eval) |
| FlexPrefill | OfjIlbelrT | 8.00 | R1,R2 | Comparable quality; QUOKA slightly below due to theorem issue |
| HiP | PTcMzQgKmn | 6.25 | R2 | QUOKA clearly stronger |
| StreamingLLM | NG7sS51zVF | 7.50 | R2 | Comparable; QUOKA similar quality tier |
| LongLoRA | 6PmJoRfdaK | 7.00 | R2 | Different focus (training-based); QUOKA competitive |

Round 1 bracket: 6.5–8.5. Round 2 narrowed to 7.0–8.0. Final: 7.5.Now I have all the information needed. Let me write the final review.

## Summary
QUOKA is a training-free, hardware-agnostic sparse attention method designed for chunked prefill in LLMs. The core idea is to select a small set of "representative" queries — those with low cosine similarity to the mean query, which are observed to interact broadly with many keys — then score keys by cosine similarity against those queries and aggregate scores (max across queries, mean across GQA heads) to subselect a reduced KV set. The method uses only standard linear algebra operations, making it portable across hardware. Evaluated across five model families on RULER, LongBench, NIAH, and Math500, QUOKA substantially outperforms six competing sparse attention baselines while achieving up to 5× attention speedup on GPUs and 7× on CPUs.

## Strengths
- **Dominant empirical performance across benchmarks and models (Tables 1, 2, 3):** On RULER at 32K tokens with B_SA=1024, QUOKA achieves 57.01 on Llama 3.2-3B vs. 31.73 for the next-best method (SampleAttention) — a 1.8× relative improvement. On LongBench with B_SA=512, QUOKA attains 0.945 normalized accuracy vs. 0.738 for the runner-up. Table 2 demonstrates that with B_SA at 25% of KV cache length, accuracy degradation remains under 3 points even at 32K tokens across all five models.
- **Hardware-agnostic speedups validated across diverse platforms (Figure 5):** QUOKA achieves 5× attention speedup on Nvidia A100, nearly 7× on Intel Xeon W-2125 CPU, and 5–6× on consumer RTX 2080 GPU. The method's reliance on standard linear algebra rather than custom CUDA kernels is a genuine practical advantage for deployment flexibility.
- **Elegant GQA pre-aggregation trick (Algorithm 1, line 8):** By normalizing queries and averaging them across KV groups before computing QK^T, QUOKA exploits the linearity of mean and outer product to reduce scoring computation by a factor of n_Q/n_KV with no accuracy loss. This is a non-trivial efficiency gain that cleanly handles modern GQA architectures.
- **Architectural breadth:** Validation spans five model families (Llama 3.2-3B, Qwen 2.5-3B, Qwen3-4B, Qwen3-30B-A3B MoE, SmollM3, GPT-OSS-20B) with both RoPE and NoPE variants, demonstrating the method is not architecture-specific.
- **Well-motivated design choices with empirical support:** The choice of max over mean for query-aggregation is supported by the heavy-tailed distribution in Figure 3; cosine similarity over dot product is supported by a claimed >10% improvement on RULER.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **Theorem 1 overclaims its contribution (Section 3.1).** The theorem provides a geometric consistency bound: if a query is similar to a key that the mean query is dissimilar to, that query cannot be too close to the mean query. This does not establish that the queries furthest from the mean are the ones that dominate attention — it only shows consistency under specific, unverified premises (β_q > 0, α_q < 0). The paper presents this as formal justification for the query subselection criterion, but the real justification is the empirical evidence in Figure 2. The gap between what Theorem 1 actually proves and what the paper claims it proves weakens the intellectual clarity of the method's motivation, though it does not affect the method's validity.

- **Core motivating observation demonstrated on only one attention head (Figure 2).** The entire method rests on the claim that queries with low cosine similarity to the mean query interact most strongly with keys. Figure 2 demonstrates this correlation (r=0.737) for a single head — layer 0, head 11 of Llama 3.2-3B-Instruct. Attention patterns vary substantially across layers and heads. The strong benchmark results provide indirect validation, but broader evidence — e.g., correlation histograms across a stratified sample of early, middle, and late layers — would substantially strengthen the paper's foundation.

- **Scores exceeding dense baseline are not discussed (Table 3).** On LongBench, SmollM3 achieves normalized scores of 1.03 (B_SA=1024) and 1.028 (B_SA=2048), meaning QUOKA *outperforms* full dense attention. Similar claims are made for Math500 (Section 4.4). Whether this is noise, a genuine sparsity-as-regularization benefit, or an evaluation artifact should be addressed rather than passed over.

- **CPU and consumer GPU latency comparisons lack competing sparse methods (Figure 5c, 5d).** The paper emphasizes hardware agnosticism as a key advantage. Figures 5c (Intel Xeon CPU) and 5d (RTX 2080 GPU) compare QUOKA only against dense attention, not against other sparse methods. Including at least one competing sparse baseline on non-datacenter hardware would directly support the claimed portability advantage.

### Trivial
- The abstract's "88% fewer key-value pairs" claim is not tied to a specific sequence length or budget setting, making it ambiguous.
- Ablation tables (Tables 5, 6, 9, 10, 11, 12) and the Math500 comparison (Table 8) are in the appendix and cannot be verified from the provided paper text.

## Nice-to-Haves
- Broaden the Figure 2 analysis across multiple layers and heads to establish the core observation as a general phenomenon.
- Discuss why QUOKA sometimes exceeds dense accuracy — even a sentence acknowledging the phenomenon and offering a hypothesis.
- Include at least one competing sparse method in CPU and consumer GPU latency comparisons.
- Re-frame Theorem 1 honestly as a geometric consistency result and build the primary case on empirical evidence.

## Removed Points
These points are flagged to be removed, treat them with caution:

1. **"Cascading KV subselection across chunks is not analyzed" (Harsh Critic Point 3):** This is based on a misunderstanding. Algorithm 1 shows that QUOKA selects from the full K each chunk — K_{<i} is the concatenation of all original keys from prior chunks (Section 2.3, Eq. 2), not a previously subselected set. The subselection is per-attention-evaluation and re-computed fresh each chunk from the full cache. There is no cascading effect.

2. **"SnapKV and KeyDif are weaker baselines included to inflate the apparent gap" (Harsh Critic):** These are KV cache eviction methods, a related but distinct line of work. The paper correctly positions eviction methods as complementary in Section 5. Their inclusion in Table 1 alongside query-dependent sparse attention methods is reasonable, not deceptive.

3. **"Claim that query-dependent methods are primarily designed for generation is stated without citation" (Harsh Critic):** The relevant citations (Ribar et al., 2024; Tang et al., 2024; etc.) appear in the same paragraph and the claim is elaborated in Section 2.4. This is a characterization of cited work, not an unsupported assertion.

4. **"Calling LessIsMore, SparQ, and Loki 'generation-focused' is inaccurate" (Harsh Critic):** The paper's characterization is that these methods were "primarily designed for generation," which is a reasonable reading of their original papers. This is a framing dispute, not a factual error.

5. **Strength Finder: "Theoretical grounding for query subselection (Theorem 1)"** — This conflicts with the verified weakness about Theorem 1 overclaiming. The theorem does not establish the claimed theoretical grounding, so it is removed as a strength.

## Novel Insights
None beyond the paper's own contributions. The key insight — that queries with low cosine similarity to the mean query are the most informative for key selection — is the paper's contribution, and the reviews do not surface additional novel observations beyond evaluating its validity and scope.

## Suggestions
- Reframe Theorem 1 honestly as a geometric consistency result showing that queries far from the mean cannot be similar to keys the mean is dissimilar to. Build the primary case for the method on the empirical evidence in Figure 2 (and ideally an expanded version of it).
- Add a figure or table showing the correlation between S_q and attention dominance across a stratified sample of layers to establish the core observation as a general phenomenon.
- Add a brief discussion of cases where QUOKA exceeds dense accuracy.
- In the CPU/consumer GPU latency plots, add at least SampleAttention as a competing sparse baseline to directly evidence the hardware-agnosticism claim.

## Score and Decision

### Anchor Summary
| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| IntelLLM | 4QWPCTLq20 | 3.00 | R1 | QUOKA much stronger — more comprehensive evaluation, better results |
| MixAttention | 2DD4AXOAZ8 | 2.00 | R1 | QUOKA much stronger |
| Cascading KV Cache | dSneEp59yX | 6.00 | R1 | QUOKA stronger — better baselines, more comprehensive benchmarks |
| SwiftKV | z1ohBxWeL2 | 5.50 | R1 | QUOKA stronger — training-free, tested on 5 model families vs 1 |
| LazyLLM | am5Z8dXoaV | 5.00 | R1 | QUOKA stronger — more comprehensive evaluation |
| FlexPrefill | OfjIlbelrT | 8.00 | R1,R2 | Comparable quality; QUOKA slightly below due to theorem overclaiming and single-head evidence, but has more comprehensive evaluation |
| HiP | PTcMzQgKmn | 6.25 | R2 | QUOKA clearly stronger across evaluation breadth, hardware diversity |
| StreamingLLM | NG7sS51zVF | 7.50 | R2 | Comparable tier; StreamingLLM has a more novel core observation, QUOKA has more comprehensive evaluation |
| LongLoRA | 6PmJoRfdaK | 7.00 | R2 | Different approach (training-based); QUOKA competitive as training-free alternative |

**Round 1 bracket: 6.5–8.5.** Round 2 narrowed to 7.0–8.0 by comparison against HiP (6.25, QUOKA clearly better), StreamingLLM (7.50, comparable), and FlexPrefill (8.00, QUOKA slightly below). QUOKA sits between StreamingLLM and FlexPrefill — stronger evaluation than StreamingLLM, but the theorem overclaiming and narrow motivating evidence place it below FlexPrefill's cleaner framing.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>