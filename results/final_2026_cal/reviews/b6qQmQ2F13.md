Now I have all the information I need. Let me construct the final review.

## Summary

This paper conducts a large-scale empirical study of memory-accuracy trade-offs for reasoning models, spanning model sizes (0.6B–32B), weight precisions (4/8/16-bit), token budgets (2k–30k), parallel scaling (G=1–16), and KV cache compression (eviction and quantization) across 1,700+ configurations. The central finding is that the optimal memory allocation strategy is scale-dependent: below an effective-size threshold (~8-bit 4B parameters), memory is better spent on larger higher-precision weights; above it, memory is better spent on longer generations and parallel scaling. Task type also matters — mathematical reasoning benefits from higher weight precision while knowledge tasks tolerate 4-bit well.

## Strengths

1. **Clear, actionable findings backed by extensive evidence.** Five explicit findings (Finding 1–5) are each supported by well-designed Pareto-frontier analyses (Figures 1–2, 5, 8–9) spanning the Qwen3 family, with validation on DeepSeek-R1-Distill and OpenReasoning-Nemotron. The finding that the optimal strategy qualitatively flips at a scale threshold is the paper's strongest contribution and is visually clear in Figure 2.

2. **Task-dependent precision analysis challenges the universal 4-bit prescription.** The paper cleanly demonstrates (Figures 3–4) that 4-bit weights are memory-optimal for knowledge-intensive tasks (GPQA-Diamond) but 8-/16-bit weights are required for math (AIME25) and code (LiveCodeBench). This directly contradicts the received wisdom from non-reasoning models and is a practically valuable result.

3. **Systematic treatment of both serial and parallel scaling.** The paper jointly analyzes serial scaling (budget-forced token increase), parallel scaling (majority voting), and their interaction with weight quantization and KV compression. Finding 3 — that parallel scaling is only memory-efficient for models above the scale threshold — is validated across two model families (Figures 5–6).

4. **Robustness checks strengthen confidence.** Alternative quantization schemes (AWQ, FP8) yield nearly identical curves (Appendix C.2), and latency analysis confirms the memory-based recommendations are strictly dominant (Appendix C.1). The three-model-family validation reduces concern that findings are Qwen3-specific.

## Weaknesses

### Major

None that are unambiguously verified from the paper's presented content and would invalidate a core claim. The concerns below are substantive but do not threaten the paper's main conclusions.

### Minor

1. **Unexplained threshold discrepancy between Finding 1/3 and Finding 5.** Finding 1 and Finding 3 reference the threshold at an effective size of 8-bit 4B (~4.2 GB) as the inflection point where the optimal strategy shifts. Finding 5, on the choice between KV cache eviction and quantization, uses a *different* threshold: 8-bit 8B (~8.9 GB). The paper never acknowledges or explains this discrepancy. These are genuinely different decisions (weight-vs-token allocation vs. eviction-vs-quantization), so different thresholds are not necessarily contradictory, but the omission leaves readers wondering whether the stated thresholds are robust properties or heuristics that happen to fit Qwen3's specific architectural parameters. The paper should either explain why different decisions have different inflection points or present the thresholds as approximate guidelines rather than precise numbers.

2. **Budget forcing may introduce a confound in serial scaling comparisons.** The paper uses budget forcing (appending "Wait") to control token budgets. If forced continuations produce lower-quality reasoning steps (e.g., repetition, degradation) compared to natural continuations, the measured benefit of longer generation for small models could be *understated*. This would mean the conclusion that small models should prioritize weights over tokens might be partially inflated by the budget-forcing mechanism rather than reflecting a fundamental property of reasoning models. The paper does not analyze whether budget-forced tokens have measurably different quality than non-forced tokens, nor does it replicate key results with an alternative method. This is a valid concern, though speculative — the paper should acknowledge it and ideally provide a calibration check.

3. **Limited breadth of KV compression methods tested.** The evaluation of KV cache compression (Section 5) compares one eviction method (R-KV) against one quantization method (HQQ). While these are reasonable choices, the finding that "eviction is better for small models, quantization is competitive for large models" could be method-dependent. The paper acknowledges this in limitations, but the limitation is consequential enough to deserve mention in the main findings.

4. **External verifier conclusion is drawn from a single model.** Finding 3's corollary about external verifier memory-inefficiency (Section 4.1) is based on a single 7B PRM (ActPRM-X). A smaller or quantized verifier, or one sharing the base model's weights, could change the conclusion. The paper scopes this appropriately in limitations, but the claim in the main text ("external verifier is consistently memory-inefficient") is too strong.

### Trivial

1. **KV cache memory values for 0.6B and 1.7B models are identical in Table 1** (both 0.21 GB at 2k tokens, 1.92 GB at 18k, 3.20 GB at 30k). This is likely because these model sizes share the same attention architecture (hidden dimension, layer count), which is common in model families, but the paper does not explain this. A brief note would avoid reader confusion.

2. **The abstract's claim "over 1,700 experimental configurations" is impressive but the paper does not break down how these are distributed** across models, tasks, and conditions, making the claim hard to verify from the main text alone.

## Nice-to-Haves

- An analysis of how the threshold varies with attention architecture (e.g., MQA, MLA, GQA). The paper tests three model families but all are transformer-based with similar attention mechanisms; the KV cache scaling behavior could differ substantially for architectures like Multi-Query Attention or Multi-Head Latent Attention.
- Problem-level variance analysis within benchmarks. Average accuracy may hide cases where some problems benefit from more tokens while others do not, which would strengthen the practical recommendations.
- A brief discussion of how the single-GPU/amortized framing interacts with tensor parallelism and pipeline parallelism in multi-GPU deployments.

## Removed Points

These points were flagged by reviewers but are removed for the following reasons:

- *"The introduction's example uses full-precision KV cache, slightly exaggerated"* — This is a framing choice, not a weakness. The paper later shows KV cache compression is beneficial, which is precisely the motivation.
- *"Parallel vs serial scaling comparison is not controlled for total tokens"* — The paper compares accuracy vs. memory, which implicitly accounts for the different total token counts. This is the correct framing for a memory-constrained analysis.
- *"No analysis of how threshold varies with architecture"* — Moved to Nice-to-Haves; the paper tests three model families, which is reasonable scope.
- *"Memory equation doesn't account for parallelism"* — The paper explicitly assumes a single-GPU/amortized setting, stated in Section 3. Scope criticism.
- *"Effective size measure conflates bit-width with quantization quality"* — The paper tests AWQ and FP8 in Appendix C.2 and reports robustness. The specific numerical threshold's sensitivity to quantization quality is a valid concern but is implicitly addressed by the paper's framing of "effective size" as a first-order cost metric, not a quality metric. Different quantization schemes at the same bit-width may shift the exact threshold slightly, but the qualitative finding (small models → prioritize weights, large models → prioritize tokens) would remain.
- *"Missing related works"* — Cannot verify without external sources; rule prevents mentioning missing related works.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Resolve the threshold discrepancy.** Add a brief discussion of why Finding 5's threshold (8-bit 8B) differs from Findings 1/3 (8-bit 4B). If they genuinely reflect different underlying mechanics (weight-vs-token allocation vs. compression strategy choice), that is itself an interesting insight worth highlighting. If the thresholds can be unified with a more nuanced characterization, do so.

2. **Add a validity check on budget forcing.** Sample a subset of generations with and without budget forcing, and compare whether forced tokens differ in quality (e.g., correctness of intermediate reasoning steps, repetition rate, token type distribution). If budget forcing is neutral, state this explicitly; if it degrades quality, quantify the effect and discuss implications.

3. **Soften the external verifier conclusion** from "consistently memory-inefficient" to "memory-inefficient for the tested 7B PRM; smaller or quantized verifiers may yield different results."

---

My round-1 bracket placed this paper between approximately 4.5 and 6.5 based on initial anchorage. Round-2 comparison to ThinKV (6.00, Oral — a method paper, stronger on novelty) and Reasoning LLM Serving (5.00, Poster — a less thorough empirical study) places the paper above the 5.00 anchor (more systematic, more findings) but below the 6.00 anchor (less novel, more descriptive than prescriptive). The paper is most comparable to empirical studies accepted as posters in this space.

**Calibration anchors used:**

| Anchor ID | Score | Round | Comparison |
|---|---|---|---|
| PYkGKPHBi0 | 3.00 | R1 | Weak anchor; paper is substantially stronger |
| dcPH77OVgN | 5.00 | R1 | Comparable breadth but paper has clearer findings |
| QpbtT95S95 | 6.00 | R1 | Stronger on methodology novelty, weaker on scope |
| ZXr3Xx7Z1O | 5.50 | R1 | Similar type (empirical study), similar quality |
| 3jDSqfTSrn | 5.50 | R1 | Stronger on theory, comparable empirical depth |
| M3CeHnZKNC | 6.00 | R2 | ThinKV — method paper; more novel but narrower scope |
| 6CGjZYp6ft | 5.00 | R2 | RLLM serving study; less thorough than this paper |
| Vem6FQvRvq | 4.67 | R2 | KV quantization paper; narrower contribution |

The paper is stronger than the 5.00 serving study anchor and comparable to the 5.50 anchors, but the unresolved threshold inconsistency and budget-forcing confound prevent it from reaching the 6.0+ level.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>