Now I have sufficient calibration context. Let me write the final review.

## Summary

This paper empirically studies memory-accuracy trade-offs for deploying reasoning LLMs, examining how to allocate fixed memory budgets across model size, weight precision, token budget (serial scaling), parallel samples, and KV cache compression. Through systematic experiments across the Qwen3 family (0.6B–32B) and validation on DeepSeek-R1-Distill and OpenReasoning-Nemotron, the paper identifies a scale-dependent inflection point at an effective size of ~8-bit 4B: smaller models benefit from allocating memory to larger weights (higher precision), while larger models benefit from longer generation. Additional findings address task-dependent optimal weight precision, scale-dependent efficacy of parallel scaling, and comparative benefits of KV cache eviction vs. quantization.

## Strengths

1. **Timely and well-motivated problem.** As reasoning models generate very long sequences, the KV cache can dominate memory, making prior findings from non-reasoning LLMs (where weights dominate) potentially inapplicable. The paper correctly identifies this gap and reframes deployment optimization around total memory rather than FLOPs.

2. **Systematic and large-scale empirical exploration.** The study covers ~1,700 configurations spanning 6 model sizes × 3 weight precisions × 8 token budgets × multiple group sizes × KV compression variants, which is a substantial experimental effort. The use of a single model family (Qwen3) with a consistent architecture across a wide size range (0.6B–32B) enables clean isolation of scale effects.

3. **Clear, actionable findings with practical relevance.** The five findings (scale-dependent allocation, task-dependent precision, parallel scaling threshold, KV compression necessity, eviction vs. quantization choice) are stated concretely and provide deployable guidance. The finding that 4-bit weights are suboptimal for mathematical reasoning but optimal for knowledge tasks directly challenges the universal 4-bit prescription from prior work on non-reasoning models.

4. **Generalization evidence across model families and quantization schemes.** Key results are replicated on DeepSeek-R1-Distill and OpenReasoning-Nemotron, and robustness to weight quantization scheme is verified with AWQ and FP8 (Appendix C.2). This reduces the risk that the conclusions are artifacts of a single model or method.

5. **Well-organized presentation.** The paper is clearly structured, with each finding motivated, presented with accompanying figures, and summarized. The limitations section is honest about scope constraints.

## Weaknesses

### Major

1. **No uncertainty quantification for any reported accuracy.** The paper makes precise comparative claims (e.g., "8B 8-bit consistently outperforms 14B 4-bit," "the threshold is at 8-bit 4B") without any error bars, confidence intervals, or variance estimates. AIME25 has only 30 problems, so each correct/incorrect answer shifts accuracy by ~3.3%. The paper provides no evidence that the observed differences are statistically significant or that the estimated Pareto frontiers are stable under sampling variability. This is especially concerning for the threshold claims (Findings 1, 3, 5), where a sharp numerical boundary (8-bit 4B ≈ 4.2 GB) is presented despite the underlying accuracy measurements being inherently noisy. The related "Inference Scaling Laws" paper (ICLR 2025, avg score 5.75) addressed a similar problem and included error bars; their absence here weakens the conclusions.

2. **Inconsistent thresholds between findings.** Finding 1 uses "8-bit 4B" as the threshold for weight-vs-KV allocation, and Finding 3 uses the same threshold for parallel scaling efficacy. Finding 5 shifts to "8-bit 8B" as the threshold for eviction vs. quantization preference. The paper never explains why the threshold changes between these findings, nor does it acknowledge or discuss the inconsistency. This is confusing for readers and undermines the claim that these thresholds are fundamental properties of reasoning models.

### Minor

3. **Core Pareto analysis concentrated on a single benchmark (AIME25).** While the paper lists four benchmarks, the main Pareto analyses driving Findings 1, 3, 4, and 5 (Figures 1, 2, 5, 8, 9) all use only AIME25. LiveCodeBench and MATH500 are mostly confined to the appendix, and GPQA-Diamond is used only for Finding 2. The thresholds (8-bit 4B, 8-bit 8B) are therefore derived from a single math competition benchmark with 30 problems. The paper shows consistency of trends across model families (DeepSeek-R1-Distill, Nemotron) but not across diverse benchmarks for the same threshold findings.

4. **Very narrow evaluation of external verifiers (PRM).** The paper tests only one PRM (ActPRM-X 7B) and concludes that "external verifier is consistently memory-inefficient." This is too strong a conclusion from a single verifier at a single size. Different verifier architectures, smaller verifiers, or quantized verifiers could yield different trade-offs. The paper acknowledges this is limited but still presents the conclusion as a notable result (Figure 7, Section 4.1).

5. **Computational overhead of R-KV eviction not discussed.** R-KV dynamically estimates token importance during decoding, which adds non-trivial compute. The paper focuses entirely on memory but does not discuss the latency or compute cost of the eviction policy itself. While Appendix C.1 analyzes latency for the main experiments, the KV cache compression section omits any discussion of R-KV's computational overhead, which could affect practical deployment decisions.

### Trivial

6. The abstract mentions "34B" in one instance where the paper clearly means model sizes up to 32B. Minor transcription issue.
7. The paper claims "over 1,700 experimental configurations" which is correct but inflated by combinatorial enumeration — the reader should be aware this count includes token budget × group size × compression variants, not 1,700 independent experiments.

## Nice-to-Haves

- The latency analysis in Appendix C.1 is appreciated but would be stronger if included in the main text for the KV compression experiments.
- The paper could discuss how its findings interact with emerging hardware support for low-precision compute (e.g., FP8 tensor cores), which affects whether precision selection is purely a memory trade-off or also a throughput one.

## Removed Points

No removed points — both the strength finder and my own critical reading produced content that I have incorporated above.

## Novel Insights

Beyond the paper's own contributions, the reviews collectively surface that evaluating empirical trade-off papers in the deployment/compression space requires assessing both the specificity and generality of the claims. The paper is strong on specificity (clear thresholds, clear recommendations) but weaker on generality (single benchmark for core analysis, no uncertainty quantification). The most interesting cross-cutting observation is that the community's standards for empirical rigor in deployment-oriented papers may be lower than for method papers — several accepted anchors in this space also lack error bars, while rejected ones were penalized more for lack of novelty than for statistical rigor. This paper would benefit from tighter alignment with the standard expected of empirical-scaling-law work (e.g., the Inference Scaling Laws paper's use of confidence bands).

## Suggestions

1. Add error bars or confidence intervals (e.g., bootstrap over problems) to all main accuracy plots, especially the Pareto frontiers in Figures 1, 5, 8, and 9. This is the single most impactful improvement.
2. Acknowledge and discuss the threshold shift between "8-bit 4B" (Findings 1, 3) and "8-bit 8B" (Finding 5). Either provide a rationale or present both as approximate guidelines rather than sharp boundaries.
3. For the PRM analysis (Figure 7), either weaken the conclusion to reflect the limited evaluation, or test at least one additional verifier at a smaller size.
4. Add a brief discussion of the computational overhead of R-KV-style eviction policies when presenting Finding 5.

## Score and Decision

### Calibration Anchors

All anchors retrieved across rounds:

**Round 1 — Topic bands (memory optimization, quantization, reasoning LLM):**
- 6Mdvq0bPyG (avg 3.00, low band) — "EfficientQAT" — rejected, method paper with weak evaluation. Less relevant genre.
- vw0NurJ7UX (avg 3.00, low band) — "PrefixQuant" — rejected quantization method paper. Less relevant genre.
- KJzz4UwqTb (avg 4.50, mid band) — "L4Q" — rejected, incremental method. Less relevant genre.
- 1RrOtCmuKr (avg 6.33, mid band) — "Network Memory Footprint Compression" — accepted, codebook method. Less relevant genre.
- 8Wuvhh0LYW (avg 6.40, mid band) — "OmniQuant" — accepted quantization method. Less relevant genre.
- wg1PCg3CUP (avg 8.00, high band) — "Scaling Laws for Precision" — accepted, theoretical depth, broader scope. Not comparable in genre to this empirical study.

**Round 1 — Weakness-anchored queries:**
- E2RyjrBMVZ (avg 4.17) — "Quantifying Variance in Evaluation Benchmarks" — rejected, about evaluation methodology. Shares the variance/uncertainty theme.
- 3xjc9PhEPd (avg 4.75) — "Empirical Guidelines for Deploying LLMs onto Edge Devices" — rejected, same genre (empirical deployment guidelines). Criticized for single-run experiments, common-sense findings. The paper under review has more novel findings but shares the no-error-bars weakness.
- FJFVmeXusW (avg 6.50) — "Not All Heads Matter" — accepted KV compression method. Different genre.
- VNckp7JEHn (avg 5.75) — "Inference Scaling Laws" — accepted, same genre (empirical trade-off analysis). Had error bars, theoretical analysis, but narrower scope (math only, older models). The paper under review is broader but lacks error bars.

**Round 2 — Narrowed bracket (4.5–6.5):**
- 6VhDQP7WGX (avg 5.80) — "Inference Optimal VLMs" — accepted, similar genre (trade-off analysis). Had some uncertainty quantification.
- ISqx8giekS (avg 5.17) — "LeanQuant" — accepted quantization method. Different genre.

**Round 1 bracket:** After reading the paper and surveying anchors, my initial bracket was [4.5, 6.0] — above the rejected empirical guidelines paper (4.75) due to stronger novelty, but below the accepted inference scaling paper (5.75) due to the lack of error bars and narrower benchmark coverage for core findings.

**Round 2 narrowing:** Anchors inside (4.5, 6.5) confirmed the bracket. The most relevant comparison paper, "Inference Scaling Laws" (5.75, accepted), provides the strongest benchmark: it had error bars, theoretical analysis, and a novel method, but tested only on math with older/smaller models. The paper under review has broader scope (more models, compression types, task types) and more actionable practical findings, but lacks error bars and has the threshold inconsistency. These roughly balance, placing the paper just below that anchor.

**What the low-band anchors failed at:** The "Empirical Guidelines" paper (4.75) was rejected for (a) conclusions that aligned with common sense, (b) single-run experiments without confidence intervals, and (c) limited novelty. The paper under review does NOT share failure (a) — its findings are genuinely novel and counterintuitive. It partially shares failure (b) — no error bars, though the experiments are multi-run within each configuration (32 generations per instance). It does not share failure (c) — the findings are novel. The paper is clearly stronger than the 4.75 anchor. But the lack of error bars is real, and the Inference Scaling Laws paper (5.75) shows that including them is feasible in this type of work.

**Final score: 5.5.** The paper makes a solid empirical contribution with actionable findings on an important problem. It is significantly stronger than the rejected empirical-guidelines anchor (4.75) and comparable to the accepted inference-scaling anchor (5.75) but with different strengths and weaknesses. The lack of uncertainty quantification and the threshold inconsistency prevent a higher score.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>