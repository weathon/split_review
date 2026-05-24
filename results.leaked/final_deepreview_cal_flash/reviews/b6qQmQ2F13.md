Now I have a clear calibration picture. Let me write the final consolidated review.

## Summary

This paper presents a large-scale empirical study (~1,700 configurations) of how to allocate a fixed memory budget among model size, weight precision, token budget, parallel samples, and KV cache compression for reasoning models. The central finding is that the memory-optimal strategy is scale-dependent: models with an effective size below ~8-bit 4B benefit from prioritizing weight capacity over test-time compute, while larger models benefit from the opposite. The paper also identifies task-dependent optimal weight precision (mathematical reasoning requires higher precision than knowledge-intensive tasks), demonstrates when parallel scaling becomes memory-efficient, and shows that KV cache compression (eviction or quantization) consistently improves the Pareto frontier.

## Strengths

- **Discovery of a scale-dependent memory allocation threshold.** The paper clearly demonstrates that the optimal allocation strategy flips at an effective model size threshold (Figures 1–2), directly contradicting the scale-agnostic prescriptions established for non-reasoning models. This is a novel and practically useful result.

- **Task-dependent optimal weight precision.** The paper shows that for mathematical reasoning and code generation, 8-/16-bit weights are more memory-efficient than 4-bit, whereas for knowledge-intensive tasks (GPQA-Diamond) 4-bit remains optimal (Figures 3–4). This refines prior work recommending 4-bit universally.

- **Scale-dependent analysis of parallel scaling.** The paper demonstrates that majority-vote parallel scaling improves the Pareto frontier only for models above the threshold, and characterizes how the memory-optimal group size grows with the budget (Figures 5–6). This extends the analysis beyond serial test-time scaling.

- **KV cache compression analysis.** The paper systematically compares eviction and quantization for KV cache compression, showing both improve the frontier, with eviction better for small models and quantization competitive for large ones (Figures 8–9). This provides actionable guidance beyond weight-only quantization.

- **Comprehensive empirical scope.** The study spans four benchmarks (AIME25, GPQA-Diamond, LiveCodeBench, MATH500), three model families (Qwen3, DeepSeek-R1-Distill, OpenReasoning-Nemotron), multiple quantization schemes (GPTQ, AWQ, FP8), and two KV compression methods, lending robustness to the qualitative conclusions.

## Weaknesses

### Major

- **Overclaimed generality of the quantitative threshold.** The abstract and findings present "8-bit 4B" as if it were a universal numerical bound. However, this precise threshold is derived from the Qwen3 family on AIME25 alone. The cross-family validation (DeepSeek-R1-Distill, OpenReasoning-Nemotron, Figures 6 and 16) confirms the *qualitative* scale-dependent pattern but does not test whether the same *numerical* value (≈4.2 GB) holds. The contribution is the qualitative insight that strategies flip at some effective size, not the specific number; presenting a single precise threshold overstates what the evidence supports.

- **Inconsistency between the two thresholds in Findings 1 and 5.** Finding 1 and Finding 3 use "8-bit 4B" as the threshold. Finding 5 in the body text (Section 5 and the formal statement) uses "8-bit 8B," but the introductory listing of findings on page 2 states "8-bit 4B" for Finding 5. The paper does not discuss why a different threshold applies for the KV compression choice, nor does it reconcile this discrepancy. This creates confusion about which threshold governs which trade-off and undermines the crispness of the guidelines.

- **Thin evidence for the task-dependent claim about "knowledge-intensive" tasks.** Finding 2 ("4-bit weights are broadly memory-optimal for knowledge-intensive tasks") is supported by only one benchmark, GPQA-Diamond (Figure 4). While GPQA involves scientific knowledge, a single benchmark is insufficient to establish a broad task-class generalization. The claim should be scoped to the specific benchmarks tested, or supported with additional knowledge-heavy tasks (e.g., MMLU, trivia QA).

### Minor

- **Unexplained KV cache memory numbers in Table 1.** The KV cache sizes for Qwen3-0.6B and Qwen3-1.7B are identical across all token budgets (e.g., 0.21 GB at 2k tokens, 3.20 GB at 30k), as are those for 4B and 8B. The paper does not explain whether these models share identical attention architectures (same number of layers, same head dimensions) or whether these numbers are approximations. Since the main analysis relies on these memory estimates, a brief clarification is needed — though even if the numbers are slightly off for the 1.7B model, the qualitative findings would be unaffected or strengthened (a larger KV cache would make the 1.7B model even less attractive compared to the 4B model).

- **No variance or confidence intervals.** The main results are averaged over 32 generations, but no error bars are reported. Given the large number of configurations and the stochasticity of generation, some uncertainty quantification would strengthen comparisons, especially for claims like "32B 4-bit is strictly dominated by 14B 8-bit."

### Trivial

- Finding 5 threshold discrepancy between the abstract listing (8-bit 4B) and the body (8-bit 8B) — already noted above in Major, but at the presentation level this is a straightforward fix.

## Nice-to-Haves

- A practical summary table mapping effective size ranges and task types to recommended configurations would increase the paper's utility for practitioners.
- A joint optimization of token budget and parallel group size under a memory budget (2D sweep) could strengthen the parallel scaling analysis.
- Replicating the full weight/token allocation analysis on another model family (beyond parallel scaling) would either confirm the ±4.2 GB threshold or reveal it as model-specific — either outcome would be informative.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"KV cache memory numbers may be incorrect / structural concern"** (Harsh Critic, Critical Issue 1, in its framing as a potentially fatal flaw). The identical KV cache numbers are unexplained, but the harsh critic's claim that the "quantitative threshold (8-bit 4B) ... may be an artifact of these numbers" is speculative and unsupported. Even if the 1.7B model's KV cache is understated, the 0.6B → 1.7B → 4B qualitative trend (small models better with larger weights) would be unchanged or strengthened. Demoted from "Fatal/Structural" to Minor.

- **"External verifier claim too strong"** (Harsh Critic, Section 4.1). The paper itself acknowledges the limited verifier comparison in Section 7. The finding is clearly scoped ("under tight memory budgets, self-contained strategies ... are preferable") and supported by Figure 7 for the specific verifier tested. This is an acknowledged limitation, not a weakness.

- **"No statistical uncertainty"** — kept as Minor but the harsh critic framed this more strongly than warranted. Single-run evaluation on these benchmarks is standard; treating it as a major gap would be a field-mismatch. Retained as Minor.

- **"Missing related works"** — removed per rules.

- **"Should disentangle N from effective size"** — moved to Nice-to-Haves; it's a suggestion, not a weakness.

- **"Interaction between parallel scaling and token budget"** — moved to Nice-to-Haves.

## Novel Insights

Beyond the paper's own contributions, the reviews collectively surface an important nuance: the paper's most robust contribution is the *qualitative* insight that memory-optimal strategies are scale-dependent for reasoning models, not the specific numerical threshold. The harsh critic correctly identifies that the 8-bit 4B threshold is presented with more generality than the evidence supports, and the Finding 5 threshold inconsistency (4B vs. 8B) reveals that the paper has not fully resolved which scale governs which dimension of the trade-off. A clearer articulation of *why* the KV compression threshold differs from the weight-vs-token threshold would significantly strengthen the framework.

## Suggestions

1. **Reconcile the threshold inconsistency.** Clarify whether Finding 5's threshold is 8-bit 4B or 8-bit 8B, and explain why the KV compression choice has a different inflection point than the weight-vs-token allocation. If the thresholds genuinely differ, discuss the implications.
2. **Scope the quantitative claims.** Replace "8-bit 4B" in the abstract and findings with language like "approximately 4 GB effective size (corresponding to an 8-bit 4B model in the Qwen3 family)" to avoid implying universal numerical precision.
3. **Expand the knowledge-intensive evaluation.** Add at least one additional knowledge-focused benchmark (e.g., MMLU) to support Finding 2, or explicitly scope the claim to the tasks tested.
4. **Explain the KV cache calculations.** Add a brief note in the main text or caption of Table 1 clarifying why models of different sizes share identical KV cache footprints (shared architectural parameters or approximating assumptions).

## Score and Decision

**Round 1 bracketing:** The paper sits above weak anchors (avg 2–3, rejected quantization papers) and the "Empirical Guidelines" anchor (avg 4.75, rejected — its findings were deemed common-sense, whereas this paper's findings are counterintuitive). It sits in the middle band (avg 4.5–7.5) alongside other empirical studies.

**Round 2 narrowing:** Compared to accepted anchors at 6.33–7.00 (codebook compression, compute-optimal sampling, compression benchmarks, scaling laws), this paper is comparable in scope and rigor but has notable weaknesses in specificity of its quantitative claims and one inconsistency. It is stronger than the rejected "Empirical Guidelines" paper (4.75) because its findings are genuinely novel and counterintuitive rather than restating common knowledge.

**Final placement:** The paper's empirical contribution is solid and practically useful, but the overclaimed generality of the numerical threshold, the Finding 5 inconsistency, and the thin evidence for the task-type generalization prevent it from reaching the 6.5–7.0 range. Score: **6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>