Now I have all the information I need. Let me write the consolidated review.

## Summary

This paper introduces RazorAttention (RA), a training-free KV cache compression method that exploits the observation that only a minority of attention heads (~15%, termed "retrieval heads") can effectively attend to distant tokens. RA retains a full KV cache for these retrieval heads while aggressively compressing non-retrieval heads by keeping only recent tokens, sink tokens, and a learned mean-pooled "compensation token" that summarizes discarded information. The method is evaluated on LongBench and Needle-in-a-Haystack across four model families (Qwen, Llama-2/3, Baichuan) with both RoPE and ALiBi embeddings, achieving ~3× compression with minimal performance degradation.

## Strengths

- **Head-wise compression grounded in an interpretable finding about retrieval heads.** The paper provides compelling evidence (Table 1) that protecting only ~15% of heads (identified by a synthetic probe) retains nearly all of the model's long-context ability (45.48% vs 46.94% full KV), while protecting random heads yields no benefit (40.7%). This is a clean, principled approach to KV cache reduction.

- **Compensation token effectively recovers information from dropped tokens.** Figure 6 shows a clear ablation: removing the compensation token causes sharp degradation on Needle tests, while adding it restores near-original accuracy. This is a simple but well-motivated mechanism that closes the gap left by head-wise truncation.

- **Strong and consistent empirical results across diverse model families.** On LongBench (Table 2), RA matches or approaches the full-KV baseline across Qwen1.5-7B (35.87 vs 36.03), Qwen1.5-72B (45.97 vs 46.15), Llama3-8B (34.86 vs 35.44), and Baichuan2-13B (36.45 vs 36.41), while outperforming both H2O and StreamingLLM in nearly every setting.

- **FlashAttention compatibility is a practical advantage over token-dropping methods.** Unlike H2O and similar methods that require computed attention weights to score token importance, RA's head-level pruning is pre-determined and does not interfere with FlashAttention kernels. The Needle results (Figure 3) show H2O hitting OOM at 80K while RA runs successfully, validating this claimed advantage.

- **Training-free and broadly applicable.** The method requires no retraining, no calibration data, and works across RoPE and ALiBi models including GQA architectures (Llama3-8B). The ablation study (Table 3, Figure 5, Figure 6) systematically justifies hyperparameter choices.

## Weaknesses

### Fatal

None.

### Major

- **Baseline cache budgets are not reported, making the comparison with H2O/StreamingLLM incomplete.** The LongBench table (Table 2) reports RA's performance under its stated 3.125× compression, but never states how much KV cache H2O and StreamingLLM used — i.e., how many recent + heavy-hitter tokens H2O kept per layer, or what window size StreamingLLM used. Without this information, the reader cannot determine whether RA's superior performance reflects a better algorithm or simply a larger cache budget. For a paper that positions its method as outperforming prior work, this is a significant reporting gap. The authors should report the actual cache sizes for all baselines or, ideally, run comparisons at matched cache budgets.

- **The synthetic probe for identifying retrieval heads is not validated against natural language inputs.** The method uses 2500 random tokens repeated 4 times to compute echo and induction scores, then applies fixed global thresholds (top 14% induction + top 1% echo) across all models and tasks. The paper provides no evidence that the heads identified by this synthetic probe correspond to the heads that would be identified using real text from the evaluation tasks (e.g., LongBench documents), or that the selected set is stable across diverse inputs. If the identification is input-dependent, the static pre-identification could fail on inputs dissimilar to the random-token probe. The ablation in Table 1 shows that the selected heads *are* important, but does not compare the probe-based selection against alternatives (e.g., selecting heads based on average attention to distant tokens on natural text). This is the most significant methodological gap, as the entire compression strategy depends on this pre-identification.

### Minor

- **Theorem 1 for ALiBi models is incomplete as presented.** The bound states that Attn ≤ ε for all n < m − C₀, but C₀ is never defined. The formula defines L_h, and the text then uses L_h as the vision scope. The relationship between C₀ (used in the bound) and L_h (used in practice) is unclear. This does not undermine the paper's empirical results on Baichuan2-13B (which are strong), but the theoretical section needs correction before publication — either C₀ should be replaced with an expression involving L_h, or the notation should be cleaned up.

- **The "over 70%" compression claim is slightly overclaimed for shorter contexts.** The buffer is max(4000, N/5). For N=8K (which some LongBench tasks use), the buffer is max(4000, 1600) = 4000, yielding ~1.74× compression (42.5% reduction) rather than the advertised 3× (~70% reduction). The 3× ratio holds for contexts > 20K (where the N/5 term dominates), and the paper's caption says "under long context input." However, the abstract and intro claim "over 70%" for "contexts ranging from 8K to 100K tokens" (line 45), which is not accurate for the 8K tail. The compression ratios should be reported per-task alongside the LongBench results.

- **The interaction between echo heads and induction heads is asserted but not empirically validated.** The paper speculates (citing Olsson et al. 2022) that induction heads depend on echo heads, and shows that removing echo heads degrades performance (Figure 5). However, it does not test whether the specific echo heads selected by the synthetic probe are actually the ones that form induction circuits with the selected induction heads. This is a secondary mechanism point rather than a core flaw, but it would strengthen the paper to validate the claimed dependency.

### Trivial

- Theorem 1 uses C₀ in the inequality but defines L_h in the formula — a notation mismatch that appears to be a typo.

## Nice-to-Haves

- Wall-clock time and peak memory measurements would substantiate the claimed inference speedup from FlashAttention compatibility. Currently the speed advantage is argued at the architectural level but not directly measured.
- Validating head identification stability by comparing heads selected via the random-token probe against heads selected on a sample of natural long-context inputs (e.g., a few LongBench documents) would significantly strengthen the methodology.

## Removed Points

- **"Compression ratio claim of ~2.1x for 32K inputs" (Harsh Critic #4's specific calculation):** Removed as factually incorrect. For N=32K, buffer = max(4000, 32000/5) = 6400. With 15% retrieval heads (full cache) and 85% non-retrieval heads (buffer = N/5), the per-head average is 0.15×32K + 0.85×6.4K = 10.24K, giving 32K/10.24K = **3.125× compression**. The ratio is constant for all N > 20K where N/5 > 4000, not just at "80K–100K" as the reviewer claimed. The legitimate concern (lower compression for short contexts) is retained in the Minor section above.
- **"Overstates novelty of 'preserving all token information' — the compensation token is lossy":** Removed as a phrasing nitpick. The paper's point is clear: unlike token-dropping methods, RA does not evaluate importance based on the current query and then permanently discard tokens judged unimportant. The compensation token is acknowledged as a compressed representation, and the paper explicitly describes it as "compressing the dropped cache into one token." The distinction from query-dependent eviction is valid and well-articulated.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface an unexpected connection or framing that the paper itself does not already provide.

## Suggestions

1. **Report cache budgets for all baselines.** For H2O, state the heavy-hitter ratio and recent window size used; for StreamingLLM, state the window length. Consider adding a controlled experiment where RA and H2O are compared at matched cache sizes to isolate algorithmic advantage from resource differences.
2. **Validate the head identification method against natural text.** Compare the set of heads selected by the random-token probe against heads selected by echo/induction scores computed on a sample of real long-context documents or dialog. Report overlap (Jaccard similarity) across inputs and across model runs to demonstrate stability.
3. **Fix Theorem 1.** Either replace C₀ with L_h (or define C₀ = L_h explicitly) and ensure the bound is correctly stated. Alternatively, if the ALiBi theoretical argument is intended primarily as intuitive motivation rather than a rigorous formal claim, state this clearly and avoid the pretense of a complete theorem.
4. **Report per-task compression ratios** in the LongBench table, or at least note the range of compression achieved across tasks. Acknowledge that the 3× ratio applies to contexts > 20K and that shorter contexts achieve lower compression.
5. **Add wall-clock latency/throughput measurements** on a representative long-context task to demonstrate the practical speed benefit of FlashAttention compatibility.

## Score and Decision

The paper introduces a genuinely novel and well-motivated approach to KV cache compression, with strong empirical evidence across multiple model families. The core idea — head-wise compression based on the retrieval/non-retrieval distinction — is clean, training-free, and practically relevant. The main weaknesses (missing baseline cache budgets, unvalidated head identification) are significant reporting and methodological gaps, but they are fixable: the budget information can be added, and the head identification can be validated with additional experiments. The theoretical typo is minor.

This is a solid paper with a real contribution that, with appropriate revisions to address the reporting gaps and validate the head identification, would make a strong conference submission.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>