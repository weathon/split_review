## Summary

The paper conducts a large-scale empirical study (over 1,700 experimental configurations) investigating memory-accuracy trade-offs for reasoning models under fixed memory budgets. It examines how to optimally allocate memory across model size, weight precision, KV cache budget, token generation length, and parallel sampling. The central finding is a *scale-dependent threshold* around an 8-bit 4B effective model size: below this, memory is best spent on model capacity (larger/higher-precision weights); above it, memory is best spent on longer generation or parallel scaling. The study spans Qwen3 (0.6B–32B), DeepSeek-R1-Distill, and OpenReasoning-Nemotron families across AIME25, GPQA-Diamond, LiveCodeBench, and MATH500.

---

## Strengths

- **Timely and practical framing.** The shift from FLOPs-based analysis to memory-constrained analysis is well-motivated: KV cache can dwarf weight memory for reasoning models (e.g., a Qwen3-4B-4bit's 30k-token KV cache is ~1.8× the weight size), invalidating conclusions from non-reasoning literature. The research question is precisely the right one for practitioners deploying these models today.

- **Extensive and multi-dimensional experimental coverage.** The 1,700+ configurations spanning 6 model sizes, three weight precisions, eight token budgets, four sampling group sizes, three KV eviction budgets, and three KV quantization precisions across four benchmarks is unusually thorough for an empirical study. The inclusion of three distinct model families (Qwen3, DeepSeek-R1-Distill, OpenReasoning-Nemotron) materially strengthens generalizability claims.

- **Concrete, actionable findings.** Each of the five findings is specific enough to guide deployment decisions: the 8-bit 4B effective-size threshold, the math-vs-knowledge precision split, the parallel scaling efficiency rule, the universal benefit of KV compression, and the eviction-vs-quantization regime split. These are not vague qualitative observations.

- **Finding 2 (task-dependent precision) is genuinely novel.** The observation that 4-bit quantization is broadly memory-optimal for knowledge-intensive tasks (GPQA-Diamond) but consistently inferior for mathematical reasoning and code generation (AIME25, LiveCodeBench) is in direct and well-supported conflict with received wisdom from non-reasoning model literature. The hypothesis that mathematical precision is more sensitive to weight quantization is intuitive and supported across multiple model sizes.

- **Verification across quantization schemes.** Replicating key results with AWQ and FP8 (Appendix C.2) significantly reduces the risk that findings are GPTQ-specific artifacts.

---

## Weaknesses

### Fatal
None. The experimental design is sound and findings are internally consistent.

### Major

1. **The 8-bit 4B threshold lacks principled grounding.** The threshold is stated as an empirical observation, but no mechanistic explanation is offered for why this specific boundary emerges. Is it driven by the ratio of weight memory to KV cache memory, the absolute number of active parameters, or something architecture-specific to Qwen3? Without an explanatory principle, it is unclear whether the threshold remains valid across architectures with different head dimensions, layer counts, or attention groupings (e.g., models with very aggressive GQA might yield a different crossover). The paper acknowledges that "the inflection point...may change as models become more sophisticated," but offers no guidance on re-deriving it for a new model family without rerunning the full 1,700-configuration sweep.

2. **Inconsistent threshold definition between Finding 1 and Finding 5.** Finding 1 and Finding 3 define the threshold as "8-bit 4B" (~4.2 GB effective size), while Finding 5 explicitly states "8-bit 8B" as the boundary for KV eviction vs. quantization superiority. The two thresholds appear in the same paper without reconciliation or explanation. This inconsistency weakens the paper's central claim of a single, unified scale-dependent principle.

3. **Section 5 reduces averaging from 32 to 8 generations without justification.** The main analysis in Section 4 uses 32 generations per instance for variance reduction. In Section 5 (KV compression analysis), the paper switches to 8 generations. Given that AIME25 has only 30 problems, this reduction substantially increases variance and makes cross-section comparisons unreliable. If compute constraints forced this reduction, it should be explicitly quantified (e.g., confidence intervals or standard errors shown).

### Minor

1. **The "batched inference" assumption is under-specified.** The paper acknowledges that in batched settings, model weights are amortized and the analysis changes fundamentally. The main findings assume non-batched, single-request inference (G=1 or G>1 as a single batch). Appendix C.3 is mentioned but the main text does not summarize its conclusions. For many production deployments, the batched regime is the norm, which could invert some findings (e.g., weight memory becomes negligible, making KV cache compression universally dominant).

2. **StreamingLLM appears only in the background, not the experiments.** Section 2 introduces both StreamingLLM and R-KV as eviction baselines, but Section 5's analysis relies exclusively on R-KV for eviction. It is unclear whether R-KV's superiority over quantization also holds for simpler eviction methods, or whether the result is partially attributable to R-KV's sophisticated redundancy-aware selection.

3. **The PRM analysis (Section 4.1) uses a single, specific PRM (ActPRM-X, 7B, 13.28 GB).** The conclusion that "external verifiers are memory-inefficient" is stated broadly, but a 13 GB PRM is a particularly large overhead. A smaller verifier (e.g., 1–3B) might yield a different conclusion. The section's conclusion is overgeneralized relative to the evidence.

### Trivial

- The figure captions are repeated in triplicate (once as alt text, once as parsed caption, once as interpreted caption), likely due to PDF extraction artifacts, but this does not affect evaluation.

---

## Nice-to-Haves

- A lightweight analytical model (even a simple ratio of weight memory to KV memory at saturation length) that predicts the crossover threshold from model hyperparameters would substantially strengthen the paper's theoretical contribution and generalizability.
- Showing confidence intervals or error bars on accuracy curves would make the findings more statistically credible, especially given the limited sample size of AIME25 (30 problems).
- A unified figure or decision tree summarizing all five findings under a single framework would dramatically improve usability for practitioners.

---

## Novel Insights

The paper's most genuinely surprising contribution is the convergence of three distinct phenomena—weight-vs-KV allocation, parallel scaling efficiency, and eviction-vs-quantization preference—around the same approximate scale threshold (8-bit 4B effective size). If this convergence reflects a principled underlying cause rather than coincidence, it suggests that a model's "intrinsic capacity" at this scale crosses a threshold where it can exploit redundancy in long reasoning chains (making longer context valuable) while simultaneously being robust enough to tolerate quantization noise in the KV cache. This points toward an interesting, unexplored connection between model capacity and KV cache information density in reasoning traces—a connection that could inform future architecture design for memory-efficient reasoning.

---

## Suggestions

- Provide theoretical or analytical grounding for the 8-bit 4B threshold—even a simple predictive formula based on model architecture hyperparameters (head dimension, number of layers, GQA ratio) would allow practitioners to compute the threshold for new models without full experiments.
- Reconcile the discrepancy between the 8-bit 4B threshold (Findings 1 and 3) and the 8-bit 8B threshold (Finding 5), or explain why the two tasks (weight allocation vs. KV compression method selection) yield different inflection points.
- Report standard deviations or confidence intervals across the 32 (or 8) generation samples, especially for AIME25 where problem count is small.
- Add a brief analysis of StreamingLLM vs. R-KV to establish whether the eviction superiority result depends on the sophistication of the eviction policy.

---

## Score and Decision

The paper asks a practically important and timely question, designs a rigorous experimental study, and produces actionable findings that meaningfully update the state of knowledge relative to non-reasoning model literature. The cross-family generalization is convincing. The main weaknesses—lack of theoretical grounding for the threshold, the inconsistency between Finding 1 and Finding 5's thresholds, and the reduction in averaging for Section 5—are real but do not invalidate the core contributions. This is a solid empirical paper at the boundary of acceptance.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>