Now I have a clear picture. Let me write the final consolidated review.

## Summary

QUOKA proposes a training-free, hardware-agnostic sparse attention method for chunked prefill. The key insight is that queries with low cosine similarity to the mean query interact more broadly with keys; by retaining only those representative queries and then selecting keys via cosine similarity, the method achieves near-baseline accuracy while using 88% fewer KV pairs. The approach works with standard dense kernels (no custom CUDA), yielding up to 5× attention speedup and 3× TTFT reduction on A100, and 5-7× on consumer hardware.

---

## Strengths

1. **Strong empirical results across diverse models and hardware.** Table 1 shows QUOKA achieving 10–20% higher RULER scores than the best competing method (SampleAttention) across five model families (Llama3.2-3B, Qwen2.5-3B, Qwen3-4B, SmolLM3, GPT-OSS-20B), including MoE (Qwen3-30B-A3B) and NoPE variants. Table 2 confirms that at a 25% budget, QUOKA loses <5% on RULER vs. full attention even at 32K length. The evaluation spans NVIDIA A100, RTX 2080, and Intel Xeon CPU — genuinely demonstrating hardware-agnostic efficiency.

2. **Latency improvements are clearly documented.** Figure 5 shows QUOKA achieving the highest relative speedup among all sparse methods across every tested platform: ~5× attention speedup on A100, ~7× on CPU, 5-6× on RTX 2080. The TTFT improvement (3× at 50K tokens) is measured end-to-end, not just in the attention module. The overhead of QUOKA's own scoring/selection is included in the measured time.

3. **Clean, well-specified algorithm.** Algorithm 1 is precise and implementable. The pre-aggregation trick for GQA (averaging normalized queries across KV groups before computing the score, rather than scoring each head separately) is elegant — it reduces computation by the GQA ratio while producing the same result. The method uses only cosine similarity and top-k operations, making it genuinely portable.

4. **LongBench results demonstrate a wide margin over baselines.** Table 3 shows QUOKA achieving normalized accuracy of 0.945–0.998 at B_SA=1024 across models, while the next-best method (SampleAttention) scores 0.738–0.947 at the same budget. The gap is 10–20+ percentage points, which is unusually large for sparse attention comparisons.

5. **Graceful accuracy-sparsity trade-off.** The paper reports that accuracy degrades by less than 3% when using only 12% of the original tokens (Section 4.5), and the method is robust to choices of B_CP and N_q. This is supported by ablation results referenced in the appendix.

---

## Weaknesses

### Fatal

None.

### Major

1. **Unfair comparison to generation-oriented baselines.** The paper compares QUOKA against LessIsMore, SparQ, and Loki — methods designed for single-query generation — adapted to prefill by "naively averaging" importance scores across queries. The paper openly acknowledges this degrades their performance (Section 2.4). This stacks the comparison in QUOKA's favor; the claimed advantage over "existing sparse attention methods" is therefore overstated. The one prefill-native baseline (SampleAttention) is fairly compared and QUOKA beats it, but the paper would be stronger by also citing published accuracy numbers from prefill-specific kernel-level methods (e.g., Zhang et al. 2025, Lai et al. 2025 — mentioned in related work but not quantitatively compared). This would help establish whether QUOKA's accuracy–sparsity trade-off is competitive with the best prefill techniques, not just with poorly-adapted generation methods.

### Minor

1. **Theoretical justification does not directly support the main claim.** Theorem 1 bounds CosSim(M_Q, q) under specific conditions on a single key k (CosSim(k,q_0)>0 and CosSim(M_Q,k)<0). This shows that if a query attends strongly to *a particular key* with certain geometric properties, then S_q is large. But the paper's claim is that low-S_q queries "attend to the majority of keys" — a statement about breadth of attention, not strength to one key. The empirical correlation in Figure 2c (r=0.737) provides more direct evidence than the theorem, but comes from a single layer/head of one model. The theorem is decorative rather than explanatory. This does not invalidate the method, but the theoretical framing is weaker than presented.

2. **Normalized accuracy >1.0 is not discussed.** In Table 3, QUOKA achieves normalized accuracy of 1.03 on SmolLM3 at B_SA=1024, exceeding the dense baseline. The paper does not mention or explain this. Possible explanations (benchmark noise, regularization effect of sparsity, or a baseline implementation issue) are not discussed, which undercuts the "near-baseline accuracy" framing and raises questions about benchmark variance.

3. **No error bars on accuracy results.** The paper reports single-run accuracy values without standard deviations or confidence intervals. Given that some differences between methods on LongBench are small (<2%), it is unclear whether the reported gaps are statistically significant. The paper does specify that latency numbers are averaged over 100 trials, so this practice could have been extended to accuracy benchmarks.

### Trivial

- The selection of N_Q=16 as the default is not motivated beyond the ablation claim that accuracy drops by only ~3% even at N_q = (1/16)B_CP. A brief justification for the specific value would improve clarity.

---

## Nice-to-Haves

- Report published accuracy numbers from prefill-specific kernel-level sparse attention methods (Zhang et al. 2025, Lai et al. 2025) on the same benchmarks. Even if those methods use custom CUDA kernels that don't run in the same setup, the comparison would help calibrate QUOKA's accuracy–sparsity trade-off against upper bounds from other approaches.
- Provide a runtime breakdown showing how much time QUOKA spends on scoring/selection vs. the attention computation itself.
- Extend the empirical validation of the query subselection principle (Figure 2c) to more layers, heads, and models to strengthen the claim that S_q correlates with attention breadth.

---

## Removed Points

**These points are flagged to be removed — treat with caution:**

- *Missing appendix/ablation tables (Tables 5, 6, 8, 9, 10, 11, 12).* The parser strips appendix content from all papers; these tables exist in the original submission. Not a valid weakness.
- *Figure 4 "Full" panel shows lower accuracy than QUOKA.* The figure description in the extracted text is generated by the PDF parser from the image and may not be accurate. The paper text does not claim QUOKA beats full attention on NIAH. Without the original figure, this cannot be verified.
- *Missing prefill-specific baselines from Zhang et al. 2025, Lai et al. 2025, Gao et al. 2024.* This is partially addressed as a Major weakness above, but the removed version (speculating about fairness without evidence) is replaced by the more measured version in Major weakness #1.
- *Baseline hyperparameters not discussed.* The paper states "Hyperparameters follow original publications," which is standard practice.
- *The paper does not address prefill-specific methods in related work.* The paper explicitly cites and discusses Zhang et al. 2025, Gao et al. 2024, Lai et al. 2025 in Section 2.4 and the Related Work section.

---

## Novel Insights

None beyond the paper's own contributions. The harsh critic's observations about baseline fairness are well-taken but represent a standard evaluation concern rather than a novel framing. The strength finder correctly identifies that the LongBench margin (10-20+ points over SampleAttention) is the paper's strongest single piece of evidence.

---

## Suggestions

1. In the rebuttal, address the baseline comparison directly: acknowledge that generation-oriented methods are at a disadvantage when naively adapted, but argue that this illustrates the *need* for a prefill-specialized method (which is your contribution). Report published numbers from the kernel-level prefill methods cited in related work.

2. Add a brief discussion of the SmolLM3 >1.0 normalized accuracy — even a sentence noting it as within expected benchmark variance or as a regularization benefit would resolve the concern.

3. Strengthen the empirical support for the query subselection principle by showing the S_q correlation across more layers and heads, or by measuring recall of top-k attention weights under query subselection.

---

## Score and Decision

**Calibration process:**

**Round 1 — Bracketing:** Searched for similar papers (sparse attention, KV cache, prefill) in three score bands.

| Anchor paper | Avg score | Band | Comparison |
|---|---|---|---|
| ILRe (GiI6tPrPAG) | 2.00 | <3.5 | Much weaker — unclear methodology, minimal evaluation |
| SentKVCompress (T0ii3nAxk4) | 2.50 | <3.5 | Weaker — limited model/hardware coverage |
| SparseSkeleton (Y5kgP4x20k) | 2.67 | <3.5 | Weaker — sparse attention decomposition, less comprehensive eval |
| OracleKV (k3IAjIsfyw) | 4.00 | 3.5-7.5 | Comparable — also training-free KV selection for prefill, but has oracle construction concerns |
| HBW-KV (sQjYtFSEuZ) | 4.00 | 3.5-7.5 | Comparable — block-wise KV compression, but incremental novelty concerns |
| TAKE (kMLfUshPwo) | 4.00 | 3.5-7.5 | Comparable — chunked prefill eviction, similar evaluation breadth |
| SALE (yTeDQeuKKz) | 4.00 | 3.5-7.5 | Comparable — low-bit sparse attention, custom kernel required |
| LookaheadKV (RVLMGPXt2i) | 5.00 | 3.5-7.5 | Slightly weaker — fewer hardware platforms, smaller model zoo |
| ProtoKV (kXhPkDaFbJ) | 5.00 | 3.5-7.5 | Similar — KV selection approach, comparable experimental scope |
| RESA (ktcq26hMCH) | 5.50 | 3.5-7.5 | Similar — accepted poster, has missing derivation gap; QUOKA has stronger evaluation breadth |
| ProxyAttn (m3HXHQYmZu) | 6.50 | 3.5-7.5 | Stronger — accepted poster, more principled head-similarity motivation, but QUOKA covers more hardware |

**Round 2 — Narrowing:** I examined ProxyAttn (6.50) and RESA (5.50) in full detail as the most relevant anchors in the (4.5, 7.5) band.

**Round-1 bracket:** 4.5 – 7.0.  
**Round-2 anchor comparison:** QUOKA is stronger than the 4.0-4.67 papers (OracleKV, HBW-KV, TAKE, SALE, CLAA) due to its more comprehensive evaluation across models and hardware, clearer algorithm specification, and stronger empirical margins. It is comparable to RESA (5.5) but slightly below ProxyAttn (6.5). ProxyAttn has a more principled motivation (head similarity validated across layers) while QUOKA's main weakness is the stacked baseline comparison and thin theory. QUOKA's evaluation breadth (5+ models, 3 hardware platforms, 4 benchmarks) is broader than ProxyAttn's.

**Final score:** 6.0. The paper makes a genuine contribution — a clean, training-free, hardware-agnostic sparse attention method for chunked prefill with strong empirical results — but is held back from a higher score by the unfair baseline comparison (most baselines are generation-oriented methods naively adapted to prefill) and the thin theoretical justification for the core query-selection principle.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>