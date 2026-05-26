Now I have a thorough understanding of the paper. Let me synthesize the final consolidated review by cross-checking every claim from both the harsh critic and strength finder against the actual paper content.

---

## Final Consolidated Review of QUOKA: Query-Oriented KV Selection for Efficient LLM Prefill

## Summary
QUOKA proposes a training-free, hardware-agnostic sparse attention method for chunked prefill in LLM inference. The core insight is that queries with low cosine similarity to the mean query interact most strongly with keys, so the method first subsamples informative queries, then uses cosine-similarity scoring with max-aggregation to select a small set of KV pairs for each chunk. Experiments on LongBench, RULER, Needle-In-A-Haystack, and Math500 across six model families demonstrate near-baseline accuracy while achieving 3–7× latency speedups.

## Strengths

- **Validated geometric insight for query selection.** The paper identifies that queries with low cosine similarity to the mean query dominate attention. This is supported by empirical evidence: Figure 2c shows a 0.737 correlation between a query's negative cosine similarity to the mean query (\(S_q\)) and its maximal attention score with any key. Figure 2b further shows via PCA that high-\(S_q\) queries lie closer to the key cluster.

- **Strong accuracy at high sparsity across benchmarks.** On RULER (Table 1) with \(B_{\text{SA}}=1024\), QUOKA outperforms all baselines by 10–20 percentage points (e.g., Llama3.2-3B at 8k: 80.15 vs. next best 61.14). On LongBench (Table 3), QUOKA maintains 0.945–0.998 normalized accuracy across most model/budget settings while competing methods drop to 0.7–0.9. Table 2 shows that at a constant 25% compression ratio, accuracy loss relative to full attention is under 3% even at 32k length.

- **Measured latency reductions of 3–7× on diverse hardware.** Figure 5 reports up to 5× attention speedup on A100, ~7× on Intel Xeon CPU, and 5–6× on RTX 2080. TTFT improves by 3× at 50k tokens. All latency data is averaged over 100 trials. QUOKA consistently matches or exceeds the speedup of all compared sparse methods.

- **Training-free and hardware-agnostic design validated across diverse architectures.** QUOKA uses only standard linear algebra operations (no custom kernels) and is evaluated on Llama3, Qwen2.5, Qwen3, SmolLM3, Qwen3-30B-A3B (MoE), and GPT-OSS-20B, covering RoPE, NoPE, and MoE architectures (Sections 4.2–4.4).

- **Principled aggregation design backed by distributional evidence.** The choice of **max** over queries (Section 3.3) is supported by the heavy-tailed distribution of attention score deviations (Figure 3), yielding >10% improvement over mean aggregation in RULER ablations (Table 10). For GQA heads, mean aggregation is motivated by head redundancy (Bhojanapalli et al., 2021) and implemented efficiently via pre-aggregation.

## Weaknesses

### Fatal
None.

### Major
None. The issues identified below are addressable in revision and do not undermine the paper's core claims.

### Minor

- **Theorem 1 is poorly scoped and adds no meaningful theoretical grounding.** The statement uses an undefined variable \(q^*\) (should presumably be \(q_0\)), the bound is essentially \(\text{CosSim}(M_Q, q^*) \leq 1 + \text{negative terms} \leq 1\), which is a near-trivial statement for cosine similarity, and the connection between the theorem and the selection score \(S_q\) is asserted rather than derived. The paper's empirical evidence (Figure 2) already sufficiently motivates the query selection criterion; the theorem can be removed or substantially revised without affecting the contribution. (Section 3.1, lines 143–147)

- **The >1.0 normalized accuracy values on LongBench are acknowledged but not analyzed.** Table 3 reports QUOKA with Smollm3 achieving normalized accuracy of 1.03 and 1.028 at \(B_{\text{SA}}=1024\) and 2048, meaning it *exceeds* the dense baseline. The paper notes this in passing ("in some cases even surpasses the accuracy of dense attention," Section 4.4) but offers no analysis of whether this stems from evaluation noise, regularization effects of sparsity, or systematic bias. While sparse attention occasionally exceeding dense accuracy is not unprecedented, the paper should at minimum discuss possible causes and ideally provide variability estimates.

- **Missing result in Table 1.** The QUOKA row for GPT-OSS-20B at 32k prompt length is empty. This missing entry should be filled or explained.

- **The "88% fewer KV pairs" claim in the abstract is not concretely tied to any experimental configuration.** The abstract states QUOKA "utiliz[es] 88% fewer key-value pairs per attention evaluation" but the main text does not specify which \(B_{\text{SA}}\) setting and which sequence length or average cache size this figure derives from. The claim should be explicitly linked to the experimental setup (e.g., "at \(B_{\text{SA}}=1024\) with a cache of ~8.5k tokens") or replaced with a range.

- **No ablation comparing the proposed query subselection to random query subsampling.** The method's main novelty is selecting queries via cosine dissimilarity to the mean query. However, no experiment isolates the benefit of this specific criterion over a simpler baseline (e.g., selecting \(N_Q\) queries uniformly at random before applying the same cosine-similarity scoring and max-aggregation). The comparison to SampleAttention is not a substitute, since SampleAttention uses uniform query sampling for *scoring* but not for *subselection* in the same way. An ablation directly comparing random vs. cosine-dissimilarity query subsampling at the same \(N_Q\) budget would strengthen validation of the core design choice.

- **Table 2 compares QUOKA at 25% compression only to the full baseline, not to other sparse methods at the same ratio.** This makes it difficult to assess whether QUOKA's accuracy-compression trade-off is better than alternatives (e.g., SampleAttention) at the same compression rate.

### Trivial
- **Theorem 1 contains undefined notation.** \(q^*\) appears in the bound without definition.
- **Latency results are reported only as relative speedups.** Absolute latency numbers (ms) would improve interpretability and allow readers to calibrate practical gains.
- **The Loki row in Table 3 has an anomalous value (0.384→0.801→0.622 progression across budgets) that is not commented on.** This appears to be a data quality issue that could be noted.

## Nice-to-Haves
- Adapt the generation-oriented baselines (SparQ, Loki) to the prefill setting by applying their scoring functions chunk-wise with the same budget, for a more direct comparison. The paper already acknowledges these methods are generation-focused, but adapting them would make the comparison more rigorous.
- Report absolute latency numbers alongside the speedup ratios in Figure 5.
- Provide the breakdown of selection overhead vs. attention computation cost to help assess real-world feasibility on resource-constrained hardware.

## Removed Points
*These points are flagged to be removed; treat them with caution.*

- **"Unfair comparison with generation-oriented baselines" (Harsh Critic, point 2):** The paper transparently acknowledges (Sections 1, 2.4, 5) that SparQ, Loki, LessIsMore, KeyDif, SnapKV are designed for generation and that extending them to multi-query prefill degrades performance. The paper also includes SampleAttention, a prefill-specific method, as a baseline. The comparison is not "unfair" — it demonstrates that methods not designed for prefill underperform in that setting, which is an informative result. QUOKA's advantage is earned by addressing the prefill setting directly. This criticism is acknowledged in the Nice-to-Haves as a strengthening suggestion rather than a weakness.

- **"Unexplained and suspicious accuracy results on LongBench" framed as undermining the central claim (Harsh Critic, point 1):** The >1.0 values affect only 2 of 12 QUOKA entries in Table 3 (Smollm3 at \(B_{\text{SA}}=1024\) and 2048) and exceed 1.0 by only 0.03 and 0.028. The vast majority of entries (10/12) show normalized accuracy between 0.945 and 0.998, supporting the "near-baseline accuracy" claim. The >1.0 values do not "undermine the central claim" as the critic asserts; they are a minor curiosity that deserves a brief comment. Downgraded from the critic's framing to Minor.

- **"No error bars" as a significant omission:** Standard NLP benchmarks like LongBench and RULER are conventionally reported as single-run evaluations. The latency results (Figure 5) are averaged over 100 trials. The demand for error bars on all benchmarks is not standard practice for this type of paper and type of evaluation.

- **"Table 2 compares only to full baseline" as a standalone weakness:** This is valid but minor; the main comparison to other methods is already provided in Table 1.

- **Strength Finder's "Theoretical grounding for query subselection":** Removed because Theorem 1 is problematic (see Minor weaknesses). The empirical grounding (Figure 2) is a genuine strength and is already captured in the first strength bullet.

- **Generic strengths from Strength Finder** (e.g., "this paper addressed an important problem"): These were not included in the strengths list above, as they lack specific, concrete evidence tied to the paper's content.

## Novel Insights
None beyond the paper's own contributions. The key empirical finding — that low-cosine-similarity queries dominate attention — is the paper's own insight, and the reviews do not add new analytical perspectives beyond what is presented.

## Suggestions
- Remove or substantially rewrite Theorem 1 to either provide a non-trivial bound with clear notation or replace it with a brief empirical justification.
- Add a brief discussion of the >1.0 normalized accuracy results (e.g., "these small deviations likely reflect evaluation noise or mild regularization effects from sparsity, and do not indicate systematic improvement over the dense model").
- Fill the empty cell in Table 1 for GPT-OSS-20B at 32k, or explain why it is missing.
- Explicitly link the "88% fewer KV pairs" claim to a specific \(B_{\text{SA}}\) and sequence length configuration.
- Add an ablation comparing random query subsampling to the cosine-dissimilarity-based selection at the same \(N_Q\) budget.
- Include comparisons to other sparse methods at the same compression ratios in Table 2.
- Add absolute latency values (ms) alongside the speedup ratios.

## Score and Decision

MY FINAL SCORE: <score>8.0</score>
MY FINAL DECISION: <decision>Accept</decision>