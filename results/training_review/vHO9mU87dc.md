Now I have all the information needed. Let me construct the final consolidated review.

## Summary

This paper presents ShadowKV, a high-throughput inference system for long-context LLMs. The core contributions are: (1) the observation that **pre-RoPE keys are exceptionally low-rank** and that within-sequence subspaces are stable, enabling aggressive low-rank key compression; (2) a system design that stores low-rank keys on GPU while offloading values to CPU, combined with chunk-based landmark selection and outlier buffering for accurate sparse attention; (3) empirical demonstrations of up to 6× larger batch sizes and **2.2–3.04× throughput gains** across multiple models and context lengths on a single A100 GPU.

## Strengths

- **Novel low-rank key insight with strong empirical support.** The paper demonstrates that pre-RoPE keys are far lower-rank than post-RoPE keys, values, or weight matrices (Figure 1a), and that 6× compression of pre-RoPE keys does not degrade needle-retrieval accuracy (Figure 2a). The observation that within-sequence subspaces are shared while cross-sequence subspaces differ (Figure 1b) is genuinely novel and directly enables the memory reduction strategy.

- **Consistently outperforms strong baselines with a minimal sparse budget.** Across RULER (Table 1), LongBench (Table 2), and Needle In A Haystack, ShadowKV with only 1.56% sparse budget consistently outperforms Quest and Loki by a wide margin (e.g., 86.88 vs. 82.03 average on RULER for Llama-3-8B-1M). The ablations systematically validate the hyperparameter choices (rank, chunk size, budget) and lend credibility to the design.

- **Meaningful throughput improvements across diverse models.** ShadowKV achieves 2.23–3.04× throughput gains across Llama-3.1-8B, Llama-3-8B-1M, GLM-4-9B-1M, and Yi-9B-200K at context lengths from 60K to 244K (Table 3). The gains are substantial even for models with only 4 KV heads (GLM-4-9B-1M: up to 2.56×), demonstrating robustness beyond ideal configurations.

- **Addresses multi-turn conversation failure of eviction methods.** Figure 4 shows that eviction-based methods (SnapKV, StreamingLLM) collapse after the first turn, while ShadowKV maintains accuracy. This is a practical strength for real-world deployments where conversations are multi-turn.

- **Compatible with pre-filling acceleration.** The integration with MInference (Table 4) shows that ShadowKV works as a drop-in module without accuracy degradation, increasing practical applicability.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **"Without sacrificing accuracy" is a slight overstatement.** The paper claims accuracy is maintained "without sacrificing accuracy" (abstract, intro, Section 6), but the results show small systematic drops on several model–benchmark pairs: Llama-3.1-8B drops ~2% on RULER (85.53 → 83.57) and ~0.8 on LongBench (48.96 → 48.13); GLM-4-9B-1M drops ~1.4% on RULER (86.82 → 85.62). While these drops are very small and the method still outperforms all baselines by a wide margin, the claim of zero degradation is imprecise. The paper would benefit from language like "with minimal accuracy loss" or quantifying the trade-off explicitly (e.g., "≤2% accuracy degradation").

- **Pre-filling SVD latency is discussed but not measured.** The paper argues that SVD cost during pre-filling is "negligible" because attention is quadratic while SVD is linear (Figure 1c), and mentions offloading to CPU or prefix caching as mitigations. However, no absolute pre-filling latency measurements are reported. For a 128K context, computing a truncated SVD on a 128K×4096 matrix per layer is a non-trivial operation, and the absolute time matters for interactive settings where pre-filling is on the critical path. Reporting end-to-end pre-filling time (including SVD, outlier detection, and value offloading) would strengthen the paper.

- **No ablation isolating the contribution of value offloading vs. attention sparsity.** The ablations vary sparse budget, chunk size, and rank, but there is no experiment running ShadowKV with both keys and values stored on GPU (using the same low-rank and sparse selection) to isolate how much of the throughput gain comes from memory savings (enabling larger batches) vs. per-token attention acceleration. This would help readers understand the relative importance of the two mechanisms.

### Trivial

- The similarity metric definition for low-rank subspaces (Frobenius inner product of projection matrices) is briefly explained but the motivation for using the projection-matrix form rather than comparing singular vectors directly could be clearer. A short intuition about why projection matrices capture subspace alignment would help.

## Nice-to-Haves

- **Pre-filling latency breakdown:** Reporting absolute wall-clock time for SVD computation, outlier detection, and value offloading for representative configurations (128K context, A100).
- **Throughput vs. latency trade-off for smaller batches:** The paper focuses on high-throughput scenarios with large batches. Showing ShadowKV's behavior at smaller batch sizes (where offloading overhead may dominate) would clarify the regime where ShadowKV is beneficial vs. where it is not.
- **Memory usage breakdown:** A pie-chart or table showing GPU memory consumed by low-rank keys, landmarks, outliers, and CPU-side values vs. original full KV cache for a representative configuration.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Surpassing infinite batch size" claim is misleading/invalid** — The harsh critic claims this comparison is "not physically meaningful" and unsupported. **Verification against the paper:** The paper's Table 3 footnote states: *"For the infinite batch size, we leverage A100's theoretical memory bandwidth (2 TB/s) for attention computations."* This is a standard roofline analysis: with infinite memory and batch size, attention throughput is bounded by memory bandwidth. ShadowKV's sparse attention achieves a higher effective bandwidth (Section 4.2 derives 7.2 TB/s) because it accesses far less data per token. The comparison is valid and common in systems research. The critic's reading that the column shows "batch-size-dependent numbers" misreads the table — the two sub-columns are clearly labeled (48) for projected throughput at ShadowKV's batch and (Inf) for the theoretical bound. This criticism is factually wrong. **Removed.**

- **Missing implementation details deferred to appendix** — The critic complains that CUDA multi-streams and cache-aware kernels are deferred to appendix. This is standard practice and the paper references the appendix. **Removed.**

- **Throughput tables should show same-batch-size comparison** — The critic claims the paper does not separate the effect of larger batch size from faster per-token attention. **Verification:** The "Full Attention (Inf)" column *does* show projected throughput at the same batch size (e.g., 168.72 at batch 48 for Llama-3-8B-1M 60K), explicitly enabling this comparison. The critic missed this. **Removed.**

- **Comparison against methods keeping full KV cache on GPU is not apples-to-apples** — The paper explicitly provides two baseline variants (with and without value offloading) to address this concern. **Removed** (already addressed by the paper).

- **Formatter-style nitpick about similarity metric definition** — The paper explains the metric and provides a footnote with its properties. The critic's complaint about it being "non-standard" is a matter of presentation preference, not substance. **Removed.**

## Novel Insights

The strongest observation from synthesizing the reviews is that the paper's core conceptual contribution — that pre-RoPE keys are not only low-rank but also exhibit *stable within-sequence subspaces* that differ *across* sequences — is genuinely novel and underexploited in the current literature. The paper uses this to store low-rank key projections, but the insight also suggests possible future directions: e.g., using the stable subspace as a compact sequence-level signature for caching, retrieval, or early exit. Additionally, the fact that temporal-locality caching (Figure 1c) can reduce sparse-attention overhead by 60% suggests that joint optimization of sparse selection and cache reuse has been under-explored in prior sparse-attention routing work.

## Suggestions

1. **Tighten accuracy claims.** Replace "without sacrificing accuracy" with "with minimal accuracy loss (≤2%)" or "while maintaining competitive accuracy," and explicitly quantify the trade-off in the abstract or conclusion. This single phrasing change would eliminate the main ground for the harshest criticism.

2. **Add pre-filling latency measurements** for a representative 128K configuration, even if just in the appendix. This would address the SVD overhead concern concretely without changing the paper's main claims.

3. **Add an ablation that isolates value offloading's contribution** by running ShadowKV with both K and V on GPU (using the same low-rank + sparse selection). This would separate throughput gains from memory savings vs. attention acceleration.

## Score and Decision

**Originality:** Good. The low-rank pre-RoPE key observation is novel, and the system-level integration is well-designed. **Quality of research question:** Important — long-context LLM throughput is a practical bottleneck. **Claims support:** Mostly well-supported; the "without sacrificing accuracy" phrasing is slightly overstated but the actual results support the method's effectiveness. **Soundness:** Experiments are thorough with appropriate baselines and ablations. **Writing/clarity:** Clear overall, though the "infinite batch" comparison provokes confusion despite being valid. **Value to community:** High — the system is practical and the insights are reproducible.

The paper makes a solid contribution with a novel observation, a well-engineered system, and strong empirical results. The weaknesses are minor and addressable in revision. There are no fatal flaws.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>