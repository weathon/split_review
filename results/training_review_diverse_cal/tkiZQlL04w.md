## Summary

This paper proposes RazorAttention, a training-free KV cache compression method that reduces cache size by ~70% with minimal accuracy loss. The core insight is that only ~15% of attention heads ("retrieval heads") effectively attend to distant tokens, while the rest focus locally. By keeping full KV cache for retrieval heads and compressing remote tokens into a single "compensation token" (the averaged key/value of dropped tokens) for non-retrieval heads, the method preserves long-range retrieval capability while aggressively compressing the rest. Experiments on LongBench and Needle-in-a-Haystack across Qwen, Llama, and Baichuan models show accuracy close to the uncompressed baseline and exceeding H2O and StreamingLLM.

## Strengths

- **Novel identification of retrieval heads enabling head-wise selective caching.** The paper provides both a theoretical bound for ALiBi models (Theorem 1) and empirical evidence (Table 1) that protecting only retrieval heads retains most performance (45.48%) while collapsing them drops to 40.81%, confirming that only ~15% of heads effectively use long-range context. This insight directly motivates the head-wise caching strategy that avoids the irreversible information loss of token-dropping methods.

- **Compensation token design is empirically effective.** The simple averaging of dropped tokens' keys and values (Eq. 3) demonstrably recovers information: the Needle-in-a-Haystack ablation (Figure 5) shows performance degrades sharply without it. This mechanism is lightweight and preserves more information than naive truncation.

- **Extensive evaluation across diverse models and tasks.** The paper tests on Qwen1.5-7B/72B, Llama3-8B, Baichuan2-13B, covering RoPE and ALiBi embeddings, GQA architecture, and both LongBench (15 tasks) and Needle-in-a-Haystack. Results consistently show RazorAttention matching or exceeding H2O and StreamingLLM (e.g., Qwen1.5-7B: 35.87 vs 36.03 full-cache; Baichuan2-13B: 36.45 vs 36.41 full-cache).

- **Systematic ablation studies justify design choices.** The paper ablates the number of induction heads (Table 3), the importance of echo heads (Figure 4), and the compensation token (Figure 5), providing evidence that each component contributes meaningfully to the overall performance.

## Weaknesses

### Fatal
None.

### Major

- **No efficiency, throughput, or memory benchmarks despite efficiency being a central claim.** The paper repeatedly claims RazorAttention is "efficient," "plug-and-play," "compatible with FlashAttention," introduces "negligible overhead," and "accelerates inference." Yet the experimental section contains zero wall-clock time, throughput, or peak memory measurements. The only speed-related remark is that H2O is incompatible with FlashAttention and goes OOM on long sequences (Figure 6 caption). For a method whose practical value hinges on being efficient, the complete absence of concrete speed/memory profiling makes the core practical contribution unverifiable. Adding prefill/decode latency and peak memory usage across several sequence lengths (e.g., 8K, 32K, 80K) is essential to substantiate the efficiency claims.

- **Incomplete baseline comparison weakens the claimed superiority.** The paper compares only against H2O and StreamingLLM, omitting SnapKV. The stated reason is that SnapKV "assumes that the query is known before compression, which does not hold in general cases or in a multi-round conversation." However, the **main quantitative evaluation (LongBench) is a single-query benchmark** where SnapKV's assumption *does* hold. For these cases, SnapKV is a strong, training-free, state-of-the-art baseline that should have been included. The paper's motivation (Figure 2) concerns multi-turn settings, but the quantitative results are entirely single-turn. The claim of being "the first training-free token reduction algorithm that achieves a nearly lossless 3X KV cache reduction" is not adequately supported without comparison against the best applicable method for the evaluated regime.

### Minor

- **Retrieval head identification method is not validated for stability or real-text relevance.** The identification procedure (Section 3.3) uses a synthetic sequence of random tokens repeated 4 times, then selects top 14% induction heads and top 1% echo heads. The paper does not examine whether this identification is stable across different random seeds, sequence lengths, or repetition counts. More importantly, it does not verify that the heads identified on synthetic data are the same heads that actually perform long-range retrieval on real text (e.g., by measuring attention distances on natural-language inputs and confirming overlap). Given that the entire compression strategy depends on correct head identification, this lack of validation is a gap. The strong end-task results partially mitigate the concern but do not replace direct validation.

- **Compensation token lacks theoretical or comparative analysis.** The compensation token (Eq. 3) averages the keys and values of dropped tokens. The paper offers no analysis of why this approximation should preserve semantic information — the operation is correct only if all dropped keys have similar dot products with the query, which is typically false. No comparison against alternative compression strategies (e.g., clustering with multiple centroids, random sampling, nearest-neighbor selection, or simply increasing the local window) is provided. The ablation shows it helps empirically, but does not establish *why* or characterize cases where it might fail.

- **Slight overclaim in the abstract: "preserves all token information."** The abstract states the method "preserves all token information," but the results in Table 2 show RazorAttention's average is consistently slightly *below* the full-cache baseline (e.g., Qwen1.5-7B: 35.87 vs 36.03). The paper acknowledges this gap in the body (lines 106–107 "a notable accuracy gap remains") and in the Limitations section, but the abstract's wording is stronger than what the evidence supports.

### Trivial

- The practical computation of the attention scope \(L_h\) for ALiBi models (Theorem 1) requires weight matrix norms and LayerNorm parameters. The paper states the theorem and then says "we first compute the effective attention scope \(L_h\)" without detailing the actual implementation steps or hyperparameters (e.g., how \(\epsilon\) is chosen), leaving a gap for reproducibility.

## Nice-to-Haves

- A comparison against SnapKV on LongBench (where it is applicable) would strengthen the empirical claims.
- A stability analysis of the retrieval head identification (varying random seeds, sequence lengths) would increase confidence.
- A comparison of the compensation token against alternative pooling strategies (multiple centroids, learned summarization) would help understand *why* averaging works.
- Speed/memory benchmarks quantifying the FlashAttention compatibility benefit and the overhead of the compensation token.

## Removed Points

These points were flagged by reviewers but are removed or downgraded after verification against the paper:

- **"Data-free" overhead complaint** (Harsh Critic, Other Observations): The reviewer claimed the identification procedure requires "not 'no overhead'" and should be quantified. However, the paper calls the method "data-free" (no training data needed), which is correct — a single forward pass on synthetic random data is negligible one-time cost, and "data-free" does not mean "zero compute." Removed as a misunderstanding.

- **"14% choice is arbitrary"** (Harsh Critic, Other Observations): The paper presents a clear ablation (Table 3) showing monotonic improvement with more heads and explains the trade-off. This is a standard design choice justified by the ablation, not a weakness. Removed.

- **"The 70% compression number is a point on a trade-off curve"** (Harsh Critic, Other Observations): This is true of every compression method. It does not constitute a weakness. Removed.

- **Strength Finder claim that "Compatibility with FlashAttention yields practical inference benefit"**: This strength is claimed by the paper but is NOT empirically demonstrated (no speed benchmarks). However, the strength itself (FlashAttention compatibility is a genuine architectural advantage over H2O) is a real property, not a false claim. I keep it as a strength but note that the claimed "practical inference benefit" lacks empirical verification.

## Novel Insights

The most interesting finding from the reviews is the tension between the paper's narrative and its evaluation: the method is motivated as a solution for multi-turn/unknown-query scenarios (Figure 2), yet all quantitative results are on single-query benchmarks (LongBench). This disconnect means the paper's claimed advantage over SnapKV is asserted but never empirically demonstrated in the regime where it would matter most. Conversely, the paper's core discovery — that LLMs have dedicated retrieval heads handling long-range attention — is provocative and well-supported, and could have standalone value beyond the compression application. The reviews also surface a pattern common in compression papers: efficiency claims are treated as self-evident consequences of reduced cache size, but without wall-clock verification they remain unvalidated architectural claims.

## Suggestions

1. **Add speed and memory benchmarks.** This is the single most important addition. Report prefill and decoding latency, peak GPU memory usage, and throughput for full cache, RazorAttention (with and without FlashAttention), H2O, and StreamingLLM across several sequence lengths (8K, 32K, 80K) on the same hardware.

2. **Include SnapKV on LongBench.** Since LongBench is a single-query benchmark where SnapKV is applicable, add it as a baseline to properly support the claim that RazorAttention is superior to existing training-free methods.

3. **Validate retrieval head identification.** Show stability across random seeds and verify that synthetic-identified heads actually correspond to heads with the longest attention spans on real text (e.g., by measuring attention distance on LongBench examples).

4. **Tone down the abstract** to more accurately reflect the (slightly below full-cache) performance, e.g., "preserves all token information relevant to future queries" or "near-lossless."

## Score and Decision

The paper makes a genuine contribution — the discovery of retrieval heads and the head-wise caching strategy are novel and well-supported by accuracy experiments. However, the missing efficiency benchmarks undermine the core practical claim, and the incomplete baseline comparison weakens the empirical support relative to the paper's own narrative. These are addressable in a revision but are significant gaps in the current submission.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>