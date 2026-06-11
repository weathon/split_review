Now I have a clear calibration picture. Let me finalize the review.

**Round 1 bracket**: 5.0–8.0 (widened from 5.5–7.5 per hint)

**Round 2 narrowing**: 
- Lower band (5.0-6.5): ChunkKV (5.25), HiP (6.25), Cascading KV Cache (6.00)
- Upper band (6.5-8.0): ZETA (7.00), Radar (6.60), Selective Attention (6.75), Transformer-VQ (7.33)

**Comparison**: QUOKA is clearly stronger than ChunkKV (5.25, rejected for limited evaluation) and Cascading KV Cache (6.00, limited baselines). It is comparable to or slightly stronger than HiP (6.25, accepted — training-free, prefill-focused, but narrower evaluation). ZETA (7.00) has stronger theoretical foundations but no speedup benchmarks and only small models. QUOKA's comprehensive evaluation (5 models, 3 hardware platforms, 4 benchmarks, 6+ baselines) is a strength, but the single-head geometric validation is a real limitation. FlexPrefill (8.00) is a clear tier above with a more sophisticated adaptive mechanism.

QUOKA lands at **6.5** — an accept with solid empirical breadth but a notable weakness in the theoretical/geometric foundation.

---

## Summary
QUOKA proposes a training-free, hardware-agnostic sparse attention method for chunked prefill. It selects a small subset of KV pairs by (1) retaining queries with low cosine similarity to the mean query, (2) scoring key relevance via cosine similarity, and (3) aggregating with max-over-queries. The method achieves near-baseline accuracy on RULER and LongBench while using ~88% fewer KV pairs, with up to 5× attention speedup on GPUs and 7× on CPUs, validated across five model families and three hardware platforms.

## Strengths
- **Consistent and substantial accuracy gains across model families on RULER (Table 1).** With B_SA=1024, QUOKA achieves the highest score in 19/20 settings across Llama3.2-3B, Qwen2.5-3B, Qwen3-4B, SmolLM3, and GPT-OSS-20B, often by 10–20 points over the best baseline (e.g., 57.01 vs. 31.73 for SampleAttention at 32K on Llama3.2-3B). This directly supports the claim that QUOKA achieves near-baseline accuracy while outperforming existing sparse attention methods.
- **Near-lossless accuracy under aggressive KV reduction on LongBench (Table 3).** At B_SA=512, QUOKA retains 94.5–99.8% of dense baseline accuracy across four models, compared to 73.8–85.6% for SampleAttention. This demonstrates that the query-subselection strategy meaningfully improves over uniform query sampling, which is the closest prefill-specific baseline.
- **Hardware-agnostic speedups verified on three distinct platforms (Figure 5).** QUOKA delivers the highest attention-module speedup among all competitors on A100 GPU, Intel Xeon W-2125 CPU, and RTX 2080 consumer GPU, validating the claim that reliance on standard linear-algebra primitives yields portability without sacrificing efficiency.
- **Clear, self-contained algorithm specification (Algorithm 1).** The 12-line pseudocode uses only standard operations (mean, CosSim, topk, gather) and explicitly handles GQA pre-aggregation, making the method straightforward to implement and reproduce.
- **Well-motivated design choices.** The max-over-queries aggregation is justified by the heavy-tailed distribution in Figure 3; cosine similarity scoring is supported by an ablation showing >10% improvement over dot product; the overall design is intuitive and each component has empirical backing.

## Weaknesses

### Fatal
None.

### Major
- **Motivating geometric observation validated on only a single attention head (Figure 2).** The method's core claim — that queries with low cosine similarity to the mean query dominate attention — is supported by evidence from one head (layer 0, head 11) of one model (Llama 3.2-3B-Instruct) on one 60-token sequence. The correlation of r=0.737 is moderate. While the method's strong downstream performance across five model families and multiple benchmarks provides indirect validation, the paper would be substantially stronger with evidence that this geometric pattern generalizes across layers, heads, and model families. The paper's central motivating claim is supported anecdotally rather than systematically, which weakens the theoretical foundation of the approach.

### Minor
- **Generation-focused baselines (SparQ, Loki, LessIsMore) serve as context rather than competitive comparisons.** The paper is transparent that these methods were designed for generation and that naive query-averaging degrades performance (Section 2.4). However, the presentation could be sharper by explicitly distinguishing between the primary prefill baseline (SampleAttention) and the generation-focused methods that illustrate why naive extensions fail. The substantive comparison against SampleAttention — where QUOKA shows a large and meaningful gap — is the one that matters.
- **Math500 / generation-phase section (4.4) is too thin to carry its claims.** The section asserts QUOKA "outperforms a sparse attention method specifically designed for generation, and in some cases even surpasses the accuracy of dense attention," but provides no quantitative support in the main text. The key result is deferred entirely to an appendix table. While the appendix presumably contains the data, the claim is surprising (sparse attention beating dense) and deserves at least a headline number and brief analysis in the main paper.
- **Normalized scores exceeding 1.0 are not discussed (Table 3).** QUOKA scores of 1.03 and 1.028 on SmolLM3 pass without comment. A brief note on whether these reflect sampling noise, beneficial regularization, or a normalization artifact would aid interpretation.

### Trivial
- GPT-OSS-20B QUOKA entry at 32K in Table 1 is blank without explanation.

## Nice-to-Haves
- A breakdown of selection overhead vs. attention computation in the latency measurements would clarify where QUOKA's speedup originates.
- Error bars or variance estimates for benchmark results would help distinguish signal from noise.
- Extended Figure 2-style analysis across more layers and model families would strengthen the theoretical foundation.
- A fuller discussion of QUOKA's interaction with the attention sink phenomenon (the paper notes results are "outside of the sink token" in Section 3.1 but does not elaborate).

## Removed Points
These points are flagged to be removed, treat them with caution.

- **"Math500 results unsubstantiated because Table 8 is in stripped appendix" (Harsh Critic Issue 3):** Per hard rules, removed because the appendix was stripped by the parser — it exists in the original submission. Retained only the concern about main-text thinness as a Minor weakness.
- **"Selection overhead not analyzed; complexity in stripped Appendix C" (Harsh Critic Issue 4):** Per hard rules, removed because Appendix C was stripped. Moved to Nice-to-Haves.
- **"No discussion of sink token interaction" (Harsh Critic):** Factually incorrect — the paper explicitly addresses this on line 151 ("outside of the sink token"). Removed.
- **"Custom CUDA kernel claim is inaccurate for SparQ/Loki/LessIsMore" (Harsh Critic Section-by-Section):** The paper's claim at line 121 refers to kernel-level sparse attention methods (Zhang et al. 2025; Gao et al. 2024; Zhu et al. 2024; Jiang et al. 2024; Lai et al. 2025), not SparQ/Loki/LessIsMore. The harsh critic misread the paragraph. Removed.
- **"The evidence for the paper's central motivating observation is thin (fatal)" (Harsh Critic Issue 1):** Partially merged into the Major weakness. The harsh critic's framing as fatal is softened because the method's empirical success across five model families and multiple benchmarks provides downstream validation independent of the single-head Figure 2 observation.
- **"Baseline comparison is a straw-man" (Harsh Critic Issue 2):** The paper is transparent about adapting generation methods naively and uses this as motivation. The primary baseline (SampleAttention) is prefill-specific. Retained as Minor only regarding presentation sharpness.
- **Strength Finder "Unexpected generation-phase benefit on Math500":** Reduced prominence since the evidence is in the stripped appendix and the main-text section is thin. Still mentioned but not as a core strength.
- **Strength Finder "Comprehensive hyperparameter robustness ablation":** Tables 5, 6, 11, 12 are in the stripped appendix; cannot independently verify. Not included as a core strength.

## Novel Insights
The paper's key insight — that geometrically "outlier" queries (those far from the mean query in cosine space) dominate the attention distribution and can serve as a compact proxy for KV selection — is genuinely novel. The combination of PCA visualization (Figure 2b), correlation with max attention (Figure 2c), and Theorem 1's formal bound provides converging evidence for this geometric perspective, even if limited to a single head. The max-over-queries aggregation (motivated by the heavy-tailed distribution in Figure 3) is a simple but effective design choice that meaningfully differs from the averaging approaches in prior work and explains much of QUOKA's advantage over SampleAttention's uniform query sampling.

## Suggestions
- Extend the Figure 2 analysis to 3–4 representative layers and at least two model families to transform the motivating observation from anecdotal to systematic.
- Make explicit in the results narrative that SparQ/Loki/LessIsMore illustrate why naive query averaging fails, while SampleAttention is the primary competitive prefill baseline — this would preempt confusion about comparison fairness.
- Add the headline Math500 numbers (even a single sentence) to Section 4.4 rather than deferring entirely to the appendix.

## Calibration

### Round 1 (Bracketing)
- **DynamicKV** (avg 4.40, Reject): KV cache compression. Weak evaluation, no latency data, no FlashAttention compatibility. QUOKA is clearly stronger.
- **Cascading KV Cache** (avg 6.00, Accept): Training-free context extension. Limited baselines, limited benchmarks. QUOKA is stronger with broader evaluation.
- **FlexPrefill** (avg 8.00, Accept): Most similar topic — dynamic sparse attention for prefill. More sophisticated adaptive mechanism, all-8 scores. QUOKA is weaker on novelty and theoretical foundation.
- **Bracket**: 5.0–8.0

### Round 2 (Narrowing)
- **ChunkKV** (avg 5.25, Reject): Semantic chunk-based KV compression. Narrower evaluation. QUOKA is stronger.
- **HiP** (avg 6.25, Accept): Training-free hierarchical pruning, prefill-focused. Comparable scope. QUOKA has broader model coverage and more benchmarks; HiP has stronger theoretical analysis. QUOKA is slightly stronger on empirical breadth.
- **ZETA** (avg 7.00, Accept): Top-k attention via Z-order curves. Stronger theory, small-scale models only, no speedup benchmarks. QUOKA has better empirical scale; ZETA has better theoretical depth. QUOKA sits slightly below.
- **Radar** (avg 6.60, Accept): Training-free dynamic sparse attention. Similar quality level.
- **Final score**: **6.5** — Accept. The paper has solid empirical validation across diverse models and hardware, clear practical benefits, and a well-motivated method. The single-head geometric validation is a real limitation that prevents it from reaching the 7–8 range, but the overall contribution is substantial and the evaluation is thorough.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>