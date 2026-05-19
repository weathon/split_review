- Decision: Accept
- Avg Score: 5.71
- Scores: 8, 5, 6, 6, 5, 5, 5
Now I have thoroughly verified all claims against the paper. Let me compose the final consolidated review.

## Summary

This paper proposes RazorAttention (RA), a training-free KV cache compression method that leverages the observation that only ~15% of attention heads (dubbed "retrieval heads" — echo and induction heads) effectively utilize long-range context. RA keeps full KV caches for retrieval heads while heavily compressing non-retrieval heads by keeping only recent tokens and attention sinks, recovering lost information via a mean-pooled "compensation token." Evaluated across Qwen1.5-7B/72B, Llama3-8B, and Baichuan2-13B on LongBench and Needle-in-a-Haystack, RA achieves ~3× compression with performance close to the full-cache baseline, consistently outperforming StreamingLLM and H2O.

## Strengths

1. **Novel and well-motivated core idea.** The paper identifies that only a small subset of attention heads (retrieval heads) effectively attend to long-range context and proposes head-wise caching as a principled compression strategy. Table 1 (tab:protect) provides direct evidence: protecting only the identified retrieval heads retains 45.48% accuracy on MultiFieldQA-en vs. 46.94% full cache, while protecting random heads drops to 40.7%. This cleanly motivates the approach.

2. **Consistent empirical outperformance over baselines across diverse architectures.** RA is evaluated on four model families (Qwen1.5-7B, Qwen1.5-72B, Llama3-8B-Instruct, Baichuan2-13B) spanning RoPE, ALiBi, and GQA architectures. The method consistently outperforms StreamingLLM and H2O on almost all of the 15 LongBench tasks (Table 1), and approaches full-cache performance: e.g., Qwen1.5-7B averages 35.87 vs. 36.03 full cache; Qwen1.5-72B averages 45.97 vs. 46.15 full cache.

3. **Compensation token as a lightweight error-recovery mechanism.** The mean-pooled compensation token (Eq. 3) compresses all dropped tokens into a single KV pair, and the ablation in Figure 6 confirms it noticeably improves retrieval accuracy on Needle-in-a-Haystack. This is a simple yet effective addition that distinguishes RA from methods that simply discard tokens.

4. **Scalability to very long contexts.** On Llama2-7B-80K (Needle benchmark, Figure 5), RA maintains near-perfect retrieval while H2O runs out of memory and StreamingLLM fails. This demonstrates practical advantages at 80K-token contexts.

5. **Theoretical grounding for ALiBi models.** Theorem 1 derives an upper bound on attention weight decay with distance for ALiBi models, providing a principled (if hard to compute in practice) attention scope per head.

## Weaknesses

### Fatal
None.

### Major

1. **Insufficient baseline comparison for the strength of the claims.** RA is compared against only two baselines: StreamingLLM (a known-weak sliding-window method) and H2O (2023). Several more recent token-dropping methods (PyramidKV, Scissorhands, FastGen, CORM) are discussed in Related Work but never evaluated. SnapKV is mentioned but excluded with a justification ("assumes query is known before compression") that chiefly applies to multi-turn settings — yet the paper's entire evaluation is single-turn on LongBench, where SnapKV could be applied. Given that the paper claims "nearly lossless 3X compression" and positions itself as "the first" to achieve this, the lack of comparison with contemporary methods substantially weakens the evidence. *(Verifiable: lines 42, 59-60, 252)*

2. **ALiBi method ambiguity for Baichuan2 experiments.** Section 3.1 describes a theoretical L_h-based compression for ALiBi models, while Section 3.2/3.3 describes an echo/induction-head identification method for RoPE models. The paper states "We choose Baichuan2-13B to demonstrate the effectiveness of RA on ALiBi models" (line 255), but never clarifies which variant was actually applied. The "General hyper-parameter settings" table (Table 2) lists induction head protection (14%) and echo head protection (1%) — concepts defined only for the RoPE method. If the RoPE method was applied to Baichuan2, then the ALiBi section becomes a disconnected theoretical aside; if the L_h method was used, the hyperparameters are missing. This ambiguity compromises reproducibility. *(Verifiable: lines 87, 129, 156-168, 221-229, 255)*

3. **FlashAttention compatibility claim is entirely unsubstantiated.** The paper states RA "is fully compatible with FlashAttention" and the compensation token introduces "negligible overhead" (line 40), but provides no runtime benchmarks, wall-clock measurements, or implementation analysis. The modified attention formula (Eq. 4) applies a multiplicative factor N_d to the compensation token's contribution — this is not a standard FlashAttention pattern and would require kernel modifications. Without evidence, this claim reads as aspirational. *(Verifiable: lines 40, 110-115)*

4. **No multi-turn evaluation despite being the primary motivation.** The entire introduction and Figure 2 motivate RA through the failure of importance-based methods on multi-turn queries ("a user might query different information from the context"). Yet every experiment (LongBench, Needle) is single-turn. This creates a direct gap between the claimed advantage and the evidence presented. *(Verifiable: lines 20-31, 252-268)*

### Minor

1. **Retrieval head identification stability insufficiently validated.** The calibration uses 2500 random tokens repeated 4 times (line 135). The paper does not analyze whether the same heads are identified across different random seeds, different text corpora, or different prompt lengths. There is some evidence that the identified heads matter (Table 1, tab:protect on a single task: MultiFieldQA-en), but the threshold of 14% induction heads is justified only on Needle (Table 3). Generalization of the identification procedure is assumed rather than demonstrated. *(Verifiable: lines 128-138, Table 3)*

2. **All ablations confined to Needle-in-a-Haystack.** The ablation studies for echo heads (Figure 4), number of induction heads (Table 3), and the compensation token (Figure 6) are all conducted solely on Needle, which is a single-key retrieval task. Whether these trends hold on tasks requiring multi-hop reasoning (e.g., HotpotQA, 2WikiMQA) or summarization (e.g., MultiNews) is not tested. *(Verifiable: lines 269-300)*

3. **No error bars or statistical significance.** All results are point estimates without variance. Given that the gap to the full-cache baseline is often very small (e.g., Qwen1.5-7B: 35.87 vs. 36.03), knowing whether differences are within the noise floor is important for supporting "nearly lossless" claims. *(Verifiable: Table 1)*

### Trivial
- Compression ratio is not reported per-model or per-task; only the aggregate "over 70%" and 3.125× (Table 2 caption) are given.
- The limitation section (lines 313-316) is brief and does not address several of the issues noted above (limited baselines, no multi-turn evaluation, no runtime benchmarks).

## Nice-to-Haves
- A simple robustness check for retrieval head identification (e.g., overlap of identified heads when using C4 text vs. random tokens for calibration).
- Ablation of the compensation token on at least one LongBench task to confirm the Needle results generalize.
- Reporting compression ratios alongside accuracy in the main table.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"No breakdown by task"** — This is factually incorrect. Table 1 provides per-task breakdowns across 15 LongBench tasks for all four models. **Reason: factually wrong.**

2. **"The gap to full-KV cache is within the noise floor"** (implying it's too small to be meaningful) — This is speculative. The small gap could equally be evidence of success; the paper simply needs error bars to resolve this. **Reason: speculative framing, not a concrete identified flaw.**

3. **"Figure 2 is a single cherry-picked example"** — Figure 2 is a motivating illustration, which is standard practice. The request for systematic multi-turn evaluation is valid and is already listed as a Major weakness (#4). **Reason: critique of a demonstration figure is not a substantive weakness of the method.**

4. **"SnapKV exclusion feels opportunistic"** — The paper gives a clear, principled justification for exclusion (line 252). Whether one agrees with it is a matter of judgment, not an error. The valid concern is that the paper does not include *other* methods (PyramidKV, etc.) which is already covered in Major weakness #1. **Reason: merged into Major weakness #1.**

5. **"No variance or significance tests"** — Already covered in Minor weakness #3.

6. **"Compression ratio not reported per model"** — Already in Trivial.

7. **Strength: "Plug-and-play compatibility with FlashAttention"** — This is claimed but unsubstantiated, so it should not be presented as a verifiable strength. Removed from Strengths.

8. **Strength: "Thorough ablation of each design choice"** — Retained but qualified as Needle-only in Minor weakness #2.

## Novel Insights

The two reviews present a complementary picture: the Strength Finder correctly identifies the paper's genuinely novel core insight (head-wise caching via retrieval heads as a compression strategy) and its consistent empirical signal across diverse architectures, while the Harsh Critic correctly identifies significant evaluation gaps. An interesting synthesis emerges: the paper's core contribution (that retrieval heads can be identified via a synthetic calibration and used for lossy-but-nearly-lossless compression) is genuinely novel and well-supported at a proof-of-concept level, but the paper over-claims by asserting "state-of-the-art" equivalence and "full FlashAttention compatibility" without the evidence that would be needed to substantiate those claims. The weakness in the evaluation is not that the method doesn't work — the numbers show it clearly does — but that the comparison set is too narrow to support the paper's strongest claims.

## Suggestions

1. **Add at least 2-3 more recent baselines** — SnapKV (single-turn LongBench, where its assumption holds), PyramidKV, and ideally one more (e.g., Scissorhands or FastGen). This would significantly strengthen the paper's claims.

2. **Clarify the ALiBi method used for Baichuan2** — State explicitly which compression variant was applied to the ALiBi model, report the hyperparameters used, and ideally validate that ALiBi models also exhibit retrieval-head behavior via the synthetic calibration procedure.

3. **Provide runtime measurements** showing wall-clock speed, peak memory, and FlashAttention integration details. This is essential for the efficiency claims.

4. **Evaluate on at least one multi-turn or multi-query task** — this directly addresses the paper's motivating scenario and would close the gap between motivation and evidence.

5. **Report standard deviations** (or multiple seeds) for key results, especially for the needle benchmark and the average LongBench scores.
