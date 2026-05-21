## Summary

This paper investigates memory-accuracy trade-offs for reasoning models, where KV cache (not weights) dominates memory. Through systematic experiments on the Qwen3 family (0.6B–32B) across math, code, and knowledge-intensive benchmarks (1,700+ configurations), the authors identify five scale-dependent findings: (1) models effectively smaller than 8-bit 4B benefit from allocating memory to larger weights rather than longer generation, while larger models benefit from the opposite; (2) 4-bit weights are optimal for knowledge tasks but higher precision (8/16-bit) is needed for math and code; (3) parallel scaling via majority voting is only memory-efficient above the same threshold; (4) KV cache compression universally advances the Pareto frontier; (5) eviction outperforms quantization for small models, while both are competitive for large models. The paper challenges the "one-size-fits-all" prescriptions from prior non-reasoning work and provides actionable deployment guidelines.

## Strengths

- **Establishes a clear empirical threshold for scale-dependent memory allocation (Finding 1).** Figure 2 decomposes the Pareto frontier, showing that below ~8 GB total memory the frontier is advanced primarily by increasing effective model size, whereas above ~10 GB the dominant lever shifts to increasing the token budget. This directly grounds the paper's central claim with a specific, measurable inflection point.

- **Demonstrates task-dependent optimal weight precision with controlled comparisons (Finding 2).** Figure 4 shows that 4-bit weights remain on the Pareto frontier on GPQA-Diamond (knowledge-intensive), while on AIME25 (Figure 1) and LiveCodeBench (Figure 3) 8/16-bit weights consistently dominate 4-bit at comparable memory. This provides comparative evidence that the same precision is not optimal across task types.

- **Validates parallel scaling effectiveness across multiple model families (Finding 3).** Figure 5 (Qwen3) and Figure 6 (DeepSeek-R1-Distill) both show that parallel scaling only improves the memory-accuracy trade-off for models above the 8-bit 4B threshold, with optimal group size growing with the memory budget. Appendix C.6 extends this to OpenReasoning-Nemotron, confirming cross-family generality for this finding.

- **Shows KV cache compression consistently advances the Pareto frontier (Finding 4).** Figure 8 demonstrates that both eviction (R-KV) and quantization (HQQ) produce aggregate Pareto frontiers strictly above the full-KV-cache baseline, especially below 10 GB, establishing that weight quantization alone is insufficient for memory-optimal reasoning.

- **Large-scale, systematic experimental design.** The study covers 1,700+ configurations across 4 benchmarks, 3 model families, multiple weight precisions, token budgets, parallel scaling group sizes, and KV compression methods. The scope is appropriate for deriving general principles.

## Weaknesses

### Fatal
None.

### Major

- **No uncertainty quantification or statistical significance.** All accuracy values are reported as point estimates (averaged over 32 generations per instance) without confidence intervals, standard deviations, or variance-aware comparisons. The paper makes fine-grained comparisons between configurations (e.g., whether 4B-4bit at 10k tokens outperforms 1.7B-8bit at 18k tokens), but it is impossible to judge whether observed differences are meaningful or noise. While the qualitative trends are plausible and the experimental scope is large, the central empirical method (Pareto frontier analysis over point estimates) rests on the implicit assumption that all measured differences are real. Bootstrap confidence intervals or seed-based variance reporting for key figures (Figures 1, 3, 4, 5, 8, 9) would substantially strengthen the paper.

- **Generalization evidence is incomplete for the majority of findings.** The paper presents its five findings as general principles for "reasoning models," but only Finding 3 (parallel scaling) is validated on model families beyond Qwen3 (DeepSeek-R1-Distill in Figure 6, OpenReasoning-Nemotron in Appendix C.6). Findings 1, 2, 4, and 5 are demonstrated on Qwen3 alone. While the limitations section acknowledges this scope choice, the abstract and conclusion present the findings as general claims without adequate caveat. At minimum, one additional model family for the weight-precision and KV compression comparisons would strengthen the claim of generality.

### Minor

- **Threshold inconsistency between Finding 1 and Finding 5.** Finding 1 uses "effective size smaller than 8-bit 4B" as the scale threshold, while Finding 5 shifts to "8-bit 8B." The paper does not explain whether these are different phenomena (i.e., the thresholds for weight-vs-token allocation and for eviction-vs-quantization are genuinely different) or whether one is a consequence of the other. This inconsistency may confuse practitioners trying to apply the guidelines.

- **Budget forcing as a potential confound is not analyzed.** The paper uses budget forcing (replacing EOS with "Wait") to extend generation length across all models. The quality of budget-forced continuations may depend on model capacity—small models forced beyond their natural termination point could produce lower-quality continuations, systematically disadvantaging them in the serial-scaling comparison. The paper does not include an ablation comparing natural-length versus budget-forced outputs for any model size.

### Trivial
None.

## Nice-to-Haves

- Including StreamingLLM as a baseline in the KV compression comparison (alongside R-KV) would calibrate the claim that eviction *per se* is better for small models, rather than R-KV specifically being a good eviction method. (The paper mentions StreamingLLM in the abstract but main-text results use only R-KV.)

- Activation memory: the paper's memory equation omits activation memory, which is negligible for long generations but may be non-trivial for the smallest configurations (e.g., 0.6B at 2k tokens). A quantitative justification for this omission would strengthen the setup.

## Removed Points

- **"The claim 'modern reasoning models generate substantially more tokens' is qualitative"** — removed because the paper already provides a concrete quantitative example (Qwen3-4B: weights = 2.49 GB, KV cache at 32k = 4.42 GB, ≈1.8× weights).
- **"The threshold 8-bit 4B should be defined earlier"** — removed because it is defined in the abstract and again in the introduction (line 34: "effective size (parameters × bits per weight) below 8-bit 4B (≈4.2 GB)").
- **"StreamingLLM baseline missing"** — removed because the appendix was stripped by the parser; results that may exist there cannot be verified.
- **"External verifier finding depends on choice of verifier"** — removed because the paper explicitly acknowledges this limitation ("under tight memory budgets" and in the limitations section).
- **Budget forcing as systematic bias** was downgraded from the critic's framing to a Minor weakness (see above), as the concern is reasonable but speculative and unsupported by evidence in the paper.
- Strength Finder's claim that findings are "validated across multiple model families and benchmarks" — partially removed because this is only true for Finding 3; kept the observation as a reduced strength qualified by this caveat.
- Strength Finder's generic statements about "important problem" and "timely" — removed as they are too generic to count as concrete strengths.

## Novel Insights

The most interesting meta-observation that emerges from the reviews is that the paper's empirical paradigm—Pareto frontier analysis over point estimates—is both its greatest strength and its most exposed weakness. The five findings are non-trivial and practically useful, but the absence of any uncertainty quantification means the paper is fundamentally an exploratory analysis rather than a confirmatory one. This is not disqualifying (many influential empirical papers in systems and deployment contexts operate this way), but it means the findings should be interpreted as strong qualitative patterns rather than precisely quantified trade-offs. A second observation: the threshold inconsistency between Findings 1 and 5 (8-bit 4B vs. 8-bit 8B) is not clearly a mistake—it may reflect a genuinely different phenomenon (weight-vs-token allocation saturates at a smaller effective size than the eviction-vs-quantization comparison)—but the paper misses the opportunity to state this explicitly as an additional finding.

## Suggestions

1. **Add confidence intervals** to the key figures (Figures 1, 2, 3, 4, 5, 8, 9) via bootstrap over instances or seeds. This is the single highest-leverage improvement. Even basic standard-deviation bars would allow readers to judge which comparisons are reliable.

2. **Validate at least one more finding on an additional model family.** Showing that Findings 2 and 5 (task-dependent precision and eviction-vs-quantization) also hold on DeepSeek-R1-Distill or another family would substantially strengthen the claim of generality.

3. **Reconcile the threshold inconsistency** between Finding 1 and Finding 5, or explicitly state that they are different thresholds for different decisions (weight-vs-token allocation vs. eviction-vs-quantization).

4. **Include a brief budget-forcing ablation** for one model size, comparing natural-length outputs against budget-forced outputs at the same token count, to validate that the experimental tool does not introduce systematic bias.

## Score and Decision

### Calibration Report

**Round 1 (bracketing):**
- Weak band (< 3.5): IntelLLM (3.00), MixAttention (2.00), PrefixQuant (3.00). All clearly reject, with narrow scope or flawed methodology. The current paper is substantially stronger.
- Middle band (3.5–7.5): SliM-LLM (5.40, Reject), Dissecting Bit-Level (4.75, Reject), Network Memory (6.33, Accept), Exploring Trade-Off (3.75, Reject).
- Strong band (> 7.5): Scaling Laws for Precision (8.00, Accept), Cut Your Losses (8.50, Accept). These are broader theoretical or system contributions; the current paper is not at this level.

**Round‑1 bracket estimate:** 4.5–7.0.

**Round 2 (narrowing, 4.5–7.5 range):**
- Progressive Mixed-Precision Decoding (6.00, Accept): A method paper with comparable experimental rigor. Both papers have missing baselines gaps. The current paper has larger scope (1,700 vs. a few configurations) but lacks error bars. Comparable quality.
- Compressing LLMs (6.75, Accept): A benchmark paper re-evaluating compression evaluation. Strong analytical depth but limited to one model family (Vicuna). The current paper has broader experimental scope but less analytical depth. Slightly weaker, so ≈6.0.
- Q-GaLore (5.00, Reject): Method paper with insufficient comparisons. Current paper is clearly stronger.
- MoE PTQ Benchmark (4.60, Reject): Narrower scope. Current paper is clearly stronger.

**Final placement:** The paper sits between the 5.40 (SliM-LLM) and 6.33 (Network Memory) anchors from round 1, closer to the upper end. It is comparable to Progressive Mixed-Precision Decoding (6.00). The core contributions are clear and practically valuable, but the absence of statistical rigor and incomplete generalization breadth prevent it from reaching the 6.5+ range.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>