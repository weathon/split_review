## Summary

This paper identifies risks of KV cache eviction in LLM inference (safety prompt breaches, hallucination, loss of critical context) and proposes MiKV, a mixed-precision strategy that retains "evicted" KV pairs at low precision (INT2) instead of discarding them, while keeping important KV pairs at higher precision (INT4). The method combines eviction-preservation via quantization, outlier-aware channel balancing, and adaptive precision allocation. Experiments across multiple benchmarks (GSM8k, HumanEval, Line Retrieval, MMLU, RULER) and models (Llama-2-7b, Llama-3-8b, Mistral-7b) show MiKV outperforms both eviction-based (H2O, SnapKV) and uniform-quantization (KIVI, RTN) baselines at matching compression ratios.

## Strengths

- **First documented evidence that KV cache eviction can breach safety guardrail prompts.** Section 3.1 (Figure 2a) qualitatively shows that H2O at 50% compression evicts system-level safety prompts, causing Llama-2-7b-chat to generate harmful responses. This identifies a risk beyond standard accuracy metrics that prior eviction work did not examine, and is a genuinely important community contribution regardless of MiKV itself.

- **The "oracle sparsity" experiment (Section 3.2) is a genuinely insightful theoretical finding.** The paper demonstrates that even with perfect future-importance prediction (top-k sparsity applied after computing the full attention map), performance still degrades. This reveals that sparsity itself — not merely prediction error — causes information loss, a distinction no prior eviction paper makes.

- **Controlled quantitative evidence that low-precision retention recovers information that eviction loses.** Table 1 directly compares line retrieval accuracy across H2O eviction vs. low-precision retention of the same KVs at multiple bit-widths. The paper shows that even INT2 retention recovers substantial accuracy compared to full eviction, cleanly supporting the central claim.

- **Outlier-aware channel balancing (Section 4.2) enables INT2 quantization to work in practice.** The channel balancer (Eq. 1) redistributes outlier magnitudes between keys and queries. Table 2 (comparing against Table 1's baseline) shows that this technique recovers accuracy in the INT2 regime where naive quantization fails, directly enabling MiKV's high compression ratios. (The technique is adapted from SmoothQuant-style methods, which the paper transparently acknowledges.)

- **MiKV is demonstrated as a plug-and-play framework, not just a single instantiation.** Section 5.3 (Table 4) shows MiKV works comparably with both H2O and SnapKV importance policies, establishing it as a general framework rather than a method tightly coupled to a specific importance criterion.

- **Latency advantage validated empirically.** Figure 7 shows MiKV (avg. ~2.4-bit/3-bit) achieves lower end-to-end latency than the FP16 full-cache baseline and KIVI, while H2O at the reduced compression ratio needed to preserve accuracy is slower. This addresses the practical concern that keeping all KVs (even at low precision) would hurt throughput.

## Weaknesses

### Fatal

None.

### Major

None. The paper's core contributions are well-supported; the issues below are addressable weaknesses rather than fatal flaws.

### Minor

- **Structural tension between the motivation and the solution is acknowledged but insufficiently quantified.** The paper convincingly shows (Section 3.2, Figure 3b) that H2O's importance criterion misidentifies tokens at positions 320–340 that later become critical. MiKV then uses the *same* H2O criterion to decide which 20% of tokens receive INT4 vs. INT2. The paper's defense — that INT2 retention is better than full eviction — is logically sound, but it never provides a principled analysis of *how* much information survives INT2 quantization, how often MiKV assigns INT2 to tokens that later become critical, or what the *worst-case* degradation is when a critical token is at INT2 rather than INT4. A distributional analysis (e.g., cosine similarity between original and quantized keys for mispredicted tokens) would substantiate the claim that "much of the lost detail can be recovered." Without it, the reader cannot fully assess whether the precision-allocation scheme inherits the failure modes it was designed to avoid.

- **The 20%/80% importance split hyperparameter is never ablated.** The paper fixes the important-KV ratio at 20% (line 134) without any sensitivity analysis. This is the central hyperparameter of the method; performance at 10%/90% or 30%/70% splits should be shown to demonstrate robustness and justify the choice.

- **Scale/zero-point storage overhead is not accounted for in effective bitrate claims.** The paper reports MiKV operating at "an average precision of 3 bits" (line 182) — but with 20% INT4 + 80% INT2, the data precision alone is 0.2×4 + 0.8×2 = 2.4 bits. A claim of "~3 bits" suggests either rounding or inclusion of auxiliary overhead (scale factors, zero points). The paper should clarify what the 3-bit figure includes and report the true effective bitrate with metadata accounted for.

- **No analysis of INT2 information retention at the individual KV level.** The paper evaluates task-level accuracy (Line Retrieval, etc.) but does not analyze per-element retention quality — e.g., cosine similarity between original and quantized keys, signal-to-noise ratio, or distribution shift. This would strengthen the claim that "much of the lost detail can be recovered" at INT2.

- **Limited model scale.** Only 7B–8B models are tested (Llama-2-7b, Llama-3-8b, Mistral-7b, Longchat-7b). The KV cache bottleneck is most acute at larger scales (30B–70B+) where the memory pressure from a full cache is highest. Testing on at least one larger model would meaningfully strengthen the generalization claims.

- **The 1-shot setting for GSM8k and MMLU is non-standard and could affect comparability.** GSM8k is typically evaluated in 8-shot and MMLU in 5-shot. The paper's justification ("to ensure a controlled evaluation with minimal contextual redundancy," line 147) is reasonable but the impact of this choice on absolute accuracy numbers is not discussed.

- **Outlier balancing is transparently adapted from prior work but its marginal contribution is not fully isolated.** The paper acknowledges adopting per-token quantization with outlier balancing from SmoothQuant (Xiao et al., 2022; Lin et al., 2023) (line 112). However, the ablation between "MiKV without outlier balancing" vs. "MiKV with outlier balancing" exists only implicitly across Table 1 and Table 2. A dedicated ablation would cleanly separate the contribution of the core mixed-precision idea from the outlier-mitigation engineering.

### Trivial

- **The paper states "four open-source LLMs" (line 147) but lists only three by name in that sentence (Llama-2-7b, Llama-3-8b, Mistral-7b).** The fourth (Longchat-7b) appears later in Section 5.2, but the presentation could be clearer.

## Nice-to-Haves

- Adding an iso-bitrate comparison where both MiKV and KIVI are configured to use the exact same average bits per KV element (including metadata) would address a natural reviewer question, even though the current comparison (same % of full cache size) is already a fair memory-budget control.
- A sensitivity study of the INT4 vs. INT2 precision pair (e.g., INT3+INT3, INT4+INT3, FP8+INT2) would strengthen the claim that the chosen configuration is optimal.
- Reporting results on a larger model (e.g., Llama-2-13b or 70B) would address the model-scale concern.

## Removed Points

The following points from the inputs were removed:

- **"All tables and figures are raster images — numerical evidence is inaccessible"** — Removed per hard rules on formatting artifacts. The tables and figures exist in the original PDF submission; the extracted text cannot render embedded images as numbers. This is a parser limitation, not a paper flaw.
- **"Comparison against KIVI not controlled at iso-bitrate"** — Removed as factually incorrect. The paper's x-axis ("compressed KV cache size %") represents total memory budget as a percentage of full FP16 cache size. Both methods are compared at the same memory budget, which is the standard and correct form of control.
- **"Only three models named, not four"** — The fourth model (Longchat-7b) appears in Section 5.2. The paper does have four models; the listing is just split across sections. Trivial presentation issue.
- **"Related works thin on recent mixed-precision/adaptive KV works"** — Removed per hard rules on missing related works. The reviewer cannot confirm which works are contemporaneous with the submission.
- **"No concrete numbers in running text"** — This is a presentation preference, not a weakness. Many papers put all numerical results in tables and figures.

## Novel Insights

The most interesting insight from the review process is that the paper's strongest contribution may not be MiKV itself, but rather the diagnostic analysis in Section 3. The oracle sparsity finding (even perfect future prediction degrades performance) is a genuinely fundamental limitation of eviction that previous work missed entirely. The safety guardrail breach observation (Figure 2a) also identifies a real deployment risk. These contributions stand independently and are arguably more novel than the mixed-precision method itself — which, while sensible and well-executed, is a natural engineering extension of the insight that "keeping something is better than keeping nothing."

## Suggestions

1. **Add a hyperparameter sensitivity study for the 20%/80% importance split.** This is the single most actionable improvement — it would directly address the main hyperparameter concern and strengthen the paper's empirical rigor.
2. **Provide distributional analysis of INT2 retention quality** (e.g., cosine similarity between original and quantized keys across importance percentiles) to quantify the "much of the lost detail can be recovered" claim.
3. **Clarify the effective bitrate calculation.** State explicitly whether the "~3-bit average" figure includes scale/zero-point overhead, and if so, report the true data-only bitrate separately.
4. **Add a dedicated ablation of the outlier balancing component** to isolate its contribution from the mixed-precision idea.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>