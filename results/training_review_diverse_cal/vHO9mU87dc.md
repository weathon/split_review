Now I have all the information I need. Let me write the final consolidated review.

## Summary

This paper presents ShadowKV, a high-throughput inference system for long-context LLMs. It makes two key contributions: (1) a novel observation that **pre-RoPE keys are exceptionally low-rank** and that keys within a sequence share similar low-rank subspaces, enabling efficient low-rank key cache storage on GPU; and (2) a chunk-based sparse attention mechanism with static outlier storage and value cache offloading to CPU, achieving accurate KV selection with only 1.56% sparse budget. The system demonstrates up to **6× larger batch sizes** and **3.04× throughput gains** on A100 across multiple model families (Llama-3.1-8B, Llama-3-8B-1M, GLM-4-9B-1M, Yi-9B-200K) without accuracy degradation on RULER, LongBench, and Needle In A Haystack.

## Strengths

1. **Novel discovery of pre-RoPE key low-rank structure and within-sequence subspace sharing (Figure 1):** The observation that pre-RoPE keys have the sharpest singular value decay compared to layer inputs, post-RoPE keys, and values, and that keys within the same sequence share low-rank subspaces while keys across different sequences do not, is genuinely insightful. This directly motivates storing only low-rank projections on GPU and enables the claimed 6× compression without accuracy loss (Figure 2a). This finding has potential value beyond this specific system.

2. **Strong empirical accuracy across multiple models and benchmarks (Tables 1–2):** On RULER at 128K context and LongBench, ShadowKV consistently matches or outperforms Quest and Loki across Llama-3.1-8B, Llama-3-8B-1M, GLM-4-9B-1M, and Yi-9B-200K. It achieves especially strong results on multi-key retrieval tasks (e.g., N-MK2: 98.96% vs. 85.42% for Quest on Llama-3-8B-1M), where eviction-based methods typically struggle.

3. **Substantial and well-measured throughput improvements (Table 3):** ShadowKV demonstrates 3.04× throughput gain on Llama-3.1-8B (122K context, batch 24 vs. batch 4), with consistent gains across models (2.56× for GLM-4-9B-1M, 2.66× for Yi-9B-200K). The results are based on actual deployment on A100 with clearly reported batch sizes.

4. **Theoretical equivalent bandwidth analysis (Section 4.2):** The derived formula (7.2 TB/s, 3.6× A100 memory bandwidth) provides a principled explanation for the speedup, combining GPU bandwidth, PCIe bandwidth, and sparsity into a single interpretable metric. This goes beyond a purely empirical contribution.

5. **Robustness to multi-turn conversations where eviction methods fail (Figure 5/6):** ShadowKV maintains accuracy across multiple NIAH rounds while SnapKV and StreamingLLM degrade after the first turn. This addresses a documented weakness of eviction-based methods and is practically important.

6. **Compatibility with pre-filling acceleration (Table 5):** ShadowKV combined with MInference achieves similar/better accuracy (82.04% avg) versus MInference alone (81.98%), showing the approach is modular.

7. **Extensive ablation studies (Figures 6–8):** Systematic examination of sparse budget, chunk size, and rank confirms that 1.56% budget, chunk size 8, and rank 160 provide optimal trade-offs, with trends consistent across tasks.

## Weaknesses

### Fatal
None.

### Major

1. **Ambiguous description of the low-rank compression mechanism (Algorithm 1, Section 3):** The paper applies SVD to `K ∈ R^{b×h_kv×s×d}` and outputs `A ∈ R^{b×s×r}` and `B ∈ R^{b×h_kv×r×d}`, but never explicitly states how the 4D tensor is reshaped for SVD. The shapes imply that K is reshaped to `(b, s, h_kv·d)` before SVD (since `A` has no head dimension while `B` does), but this is left implicit. This causes confusion about rank values: since `r=160` exceeds the head dimension `d=128` (e.g., Llama-3.1-8B), readers may mistakenly conclude the math is inconsistent. In reality, the effective dimension being decomposed is `h_kv·d = 1024`, so `r=160` is well within bounds and the 6× compression ratio (`1024/160 = 6.4×`) checks out. However, the paper should explicitly state the reshaping step, show the memory formula (`s·r + h_kv·r·d` vs. `s·h_kv·d`), and reconcile the rank values with model dimensions. Without this, the core technique is harder to verify and reproduce than it should be. This is the paper's most significant presentational shortcoming.

2. **The "surpassing infinite batch size" claim needs qualification (Table 3, footnote):** The "Full Attention (Inf)" column is computed using A100's theoretical memory bandwidth (2 TB/s), which assumes attention is purely memory-bandwidth-bound. At very large batch sizes, attention can become compute-bound, making this an idealized upper bound rather than a realistic baseline. While the paper's footnote does disclose the methodology, the claim in the abstract and conclusion that ShadowKV "surpass[es] the performance achievable with infinite batch size under the assumption of infinite GPU memory" is technically true only under the memory-bandwidth-bound assumption that may not hold in all regimes. The authors should either provide a compute-aware bound or more explicitly caveat the comparison — ShadowKV's main empirical wins (3.04× over practical full-attention baselines) are already strong enough to make the point without the potentially overclaimed infinite-memory comparison.

### Minor

3. **Multi-turn evaluation details are underspecified in the main text (Figure 5/6):** The model used for the multi-turn NIAH experiment is not named in the main text or figure caption. The task construction (number of turns, context length, retrieval depth) is not described in the main body — presumably deferred to the appendix. Given that the multi-turn result is a key argument for ShadowKV over eviction methods, the main text should at minimum state the model and provide a brief description of the setup.

4. **Fixed outlier count vs. percentage ambiguity (Section 5):** The paper sets outliers to a fixed count of 48 (with chunk size 8, this is 384 tokens) regardless of sequence length, but the earlier observation (Figure 2b) describes outliers as "0.2–0.3%" — a percentage that would vary with sequence length. For a 128K context, 384/128K ≈ 0.3% which is consistent, but for shorter contexts the percentage would be higher. This minor inconsistency should be clarified.

5. **Accuracy decline at larger chunk sizes unexplained (Figure 5a,b):** The ablation shows accuracy dropping when chunk size exceeds 8, but no explanation is offered. A brief comment on why (e.g., poorer landmark approximation due to more diverse tokens within chunks) would improve understanding.

### Trivial

6. **Algorithm 1 comment says "low-rank decomposition of the post-RoPE key cache" (line 154)** but the actual decomposition is applied to pre-RoPE keys — a minor inconsistency in the explanatory text vs. the algorithm and the main insight.

## Nice-to-Haves

- Report throughput/latency for Quest and Loki baselines (not just accuracy), to strengthen the claim that ShadowKV is faster than these alternatives, not just more accurate.
- Add a brief description of the CUDA multi-stream overlap strategy in the main text (currently only one sentence).
- Include a limitations discussion: when might the low-rank assumption weaken (specific layers, very fine-grained retrieval tasks)? How does SVD overhead scale beyond 128K to 1M tokens?
- Consider adding Needle In A Haystack plots for additional models in the main text.

## Removed Points

- **Criticism about SVD being "not a standard operation on 3D+ tensors":** This is a presentational ambiguity but not a correctness issue. The shapes `A ∈ R^{b×s×r}` and `B ∈ R^{b×h_kv×r×d}` inherently communicate that the KV heads are concatenated before SVD. The concern that the reader "cannot determine whether the system actually achieves the claimed compression" is overstated — the compression ratio is verifiable from the stated shapes and rank.
- **Criticism that RULER results are only for one model:** The paper shows RULER for 4 models (Table 1), so this is factually wrong.
- **Assertion that the paper doesn't report wall-clock time for Quest/Loki baselines as a core weakness:** This is a nice-to-have, not a weakness — the paper's efficiency comparison is against full attention, and the accuracy comparison against Quest/Loki is clearly separated.
- **Missing related works and appendix content:** Per guidelines, references cannot be verified as missing, and appendix stripping is a known parser artifact.
- **Formatting/style nitpicks and grammar concerns:** Parser artifacts, not author errors.

## Novel Insights

Beyond the paper's own contributions, the most striking pattern across the reviews is the tension between the paper's **clear empirical strength** and its **fuzzy methodological exposition**. ShadowKV's numbers are strong enough that several baseline comparisons (Quest, Loki on accuracy; full attention on throughput) are convincingly in its favor even before considering the low-rank mechanism. However, the reviewers' inability to precisely verify the SVD mechanics from the main text reveals a mismatch between the paper's engineering ambition and its mathematical precision. A systems paper can get away with "it works and here's why at a high level," but when the headline claim involves a specific compression ratio (6×) derived from a specific decomposition, the math needs to be watertight in the main paper — not inferable from tensor shapes. This is the kind of clarity gap that can cause a perfectly sound paper to get desk-rejected at a venue with stronger mathematical expectations.

## Suggestions

1. **Explicitly state the SVD reshaping.** Add one sentence: "We reshape K from (b, h_kv, s, d) to (b, s, h_kv·d), perform truncated SVD to obtain A ∈ R^{b×s×r} and right singular vectors ∈ R^{b×r×(h_kv·d)}, then reshape the right vectors to (b, h_kv, r, d) as B." Also provide the memory formula: storage = s·r + h_kv·r·d vs. s·h_kv·d, and note the 6× ratio for Llama-3.1-8B (1024/160 = 6.4×).

2. **Qualify the infinite-batch comparison.** Change "surpassing infinite batch size under infinite GPU memory" to "surpassing a memory-bandwidth-bound upper bound for full attention at infinite batch size" or similar. The 3.04× gain over the practical baseline is already impressive.

3. **Specify the model and setup for multi-turn NIAH** in the main text (or at minimum in the figure caption).

4. **Clarify whether the outlier count (48) is fixed or proportional to sequence length**, and reconcile with the "0.2–0.3%" description.

5. **Add a limitations paragraph** to the conclusion.

## Score and Decision

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>