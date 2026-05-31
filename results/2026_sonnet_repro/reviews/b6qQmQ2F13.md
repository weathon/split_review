Now let me search for calibration anchors for scoring.Round 1 bracket: **5.0–7.0**. The paper is a substantial empirical study with principled methodology (1700+ configs, Pareto frontier analysis), but lacks the theoretical formulation seen in top-scoring papers. Now narrowing.I now have sufficient calibration. Let me write the final review.

---

## Summary

This paper presents a systematic empirical study of memory-optimal inference strategies for reasoning LLMs. The central finding is that memory-optimal choices among model size, weight precision, token budget, parallel scaling, and KV cache compression are **scale-dependent**, organized around an "effective size" threshold near 8-bit 4B parameters (~4.2 GB). Below this threshold, memory is best spent on larger model weights; above it, on longer generation or parallel scaling. Over 1,700 configurations are tested across Qwen3 (0.6B–32B), DeepSeek-R1-Distill, and OpenReasoning-Nemotron, on AIME25, MATH500, LiveCodeBench, and GPQA-Diamond.

---

## Strengths

- **Directly evidenced Pareto-composition analysis (Figure 2):** Figure 2b shows that at memory budgets below ~8 GB, Pareto-optimal configurations increase effective model size, while above that the token budget becomes the dominant lever. This provides direct support for the scale-dependent allocation rule and is the clearest piece of evidence for the central claim.

- **Task-dependent precision finding is robustly demonstrated (Figures 1, 3, 4):** On AIME25 and LiveCodeBench, 8-bit and 16-bit models consistently outperform 4-bit at comparable memory. On GPQA-Diamond, 4-bit is broadly memory-optimal. The contrast across task types is concrete and well-supported, with figure caption on Figure 4 explicitly confirming that "4-bit weights remain broadly memory-optimal for this knowledge-intensive task across memory budgets."

- **Scale-dependent parallel scaling threshold is shown quantitatively (Figure 5):** The Pareto frontiers for different group sizes G visually confirm that for models effectively smaller than 8-bit 4B, the serial frontier dominates all parallel-scaling configurations, while larger models benefit from G≥4. This substantiates Finding 3.

- **KV cache compression findings are mechanistically clear (Figures 8–9):** The distinction between eviction (vertical curves: accuracy improves at constant memory) and quantization (leftward shift: same accuracy at less memory) is well-explained, and Figure 9 provides per-model comparisons that directly support Finding 5.

- **Generalization across model families is explicitly tested:** Parallel-scaling Pareto plots for DeepSeek-R1-Distill (Figure 6) and OpenReasoning-Nemotron (Appendix C.6) replicate the scale-dependent pattern, strengthening the claim's scope beyond Qwen3.

---

## Weaknesses

### Fatal
None.

### Major

- **Internal threshold inconsistency between abstract/introduction and Finding 5.** The abstract states: "This scale threshold also determines when parallel scaling becomes memory-efficient *and whether KV cache eviction outperforms KV quantization.*" The introduction (Section 1, end of bullet list) further states: "eviction offers a better memory trade-off for small models (effective size below 8-bit 4B)." However, Finding 5 reports a *different* threshold: "KV cache eviction provides a better memory-accuracy trade-off than KV cache quantization for models with an effective size **smaller than an 8-bit 8B model**." These are not the same threshold (~4.2 GB vs. ~8.94 GB from Table 1). The abstract and introduction thus misrepresent the organizing principle, implying one threshold governs all decisions when the body actually reports two distinct thresholds. For a paper whose core contribution is a principled unified framework, this inconsistency is substantive. It does not invalidate the empirical findings themselves, but it means the "single scale threshold" headline claim is overstated; the paper should either reconcile the two thresholds with an analysis of why they differ, or revise the framing to acknowledge multiple thresholds operating in different decision contexts.

### Minor

- **No uncertainty quantification on AIME25.** AIME25 has ~30 problems. While the paper averages over 32 generations per instance (and 8 generations in Section 5), the variance across the small problem pool is not reported anywhere in the main text. Several key comparisons that anchor the threshold identification—e.g., "the 8B model in 8-bit consistently outperforms the 14B model in 4-bit" (Figure 1 discussion)—are made without confidence intervals or bootstrap estimates. This does not break the conclusions (many margins appear large), but the closest comparisons near the threshold would be more credible with error bars, at minimum on Figures 1 and 2.

- **GPQA-Diamond's task-type finding sits outside the scale-governed framework without acknowledgment.** Finding 2 reports that for GPQA-Diamond, "4-bit weights remain broadly memory-optimal… across memory budgets" — a result that does not respect the scale threshold that organizes Findings 1, 3, and 5. This is structurally a *task-type-governed* finding rather than a *scale-governed* one. The paper would benefit from explicitly clarifying which findings are organized by effective size and which are organized by task type, since the current framing suggests a single "scale threshold" organizes everything.

### Trivial
- Section 3 states 32 generations per instance as the default, while Section 5 reduces to 8 generations per instance. The choice to halve the sampling again for Section 5's KV compression comparisons is acknowledged but not validated; a brief sensitivity note would be reassuring.

---

## Nice-to-Haves

- A small analysis of *why* the eviction-vs-quantization threshold sits at ~8-bit 8B rather than at the same ~8-bit 4B that governs other decisions. Whether the shift relates to GQA ratio, KV head count, or another architectural feature would substantially sharpen the organizing principle.
- Budget-forcing ("Wait" injection) interacts differently with models of different sizes; an analysis of whether the forced continuations are qualitatively coherent across scale would strengthen confidence in the serial scaling comparisons.
- The PRM comparison (Section 4.1) uses a single 7B PRM (13.28 GB). A lighter PRM option would make the "external verifiers are memory-inefficient" conclusion more general rather than tied to that specific choice.

---

## Removed Points

*These points were flagged for removal; treat with caution.*

- **"AWQ/FP8 vs. GPTQ validation lacks transparency"** — The paper explicitly states (Section 4) that the AWQ and FP8 comparison is confirmed in Appendix C.2. The appendix exists; this is not a gap.
- **"Budget-forcing mechanism is an uncontrolled variable"** — The paper follows Muennighoff et al. (2025) transparently and acknowledges this approach. This is not a methodological flaw, merely a scope limitation that the paper explicitly acknowledges in Section 7.
- **"Mechanism for task-type precision sensitivity is speculative"** — The paper appropriately acknowledges this as empirical without causal claim ("Mathematical reasoning may rely on numerical precision within the weights"). This is the right tone for an empirical study; criticizing the absence of mechanistic explanation is scope creep.
- **"Memory amortization under batched inference changes the analysis"** — The paper explicitly analyzes this in Appendix C.3. Not a gap.

---

## Novel Insights

The most genuinely novel observation is the *compositional shift* in Pareto-optimal configurations: at low memory budgets, the frontier is advanced by increasing effective model size (larger weights), while at higher budgets the dominant lever flips to the token budget. This is empirically clean and practically actionable in a way that prior compute-optimal inference work (which typically focuses on FLOPs rather than peak memory) does not address. The secondary insight — that KV cache eviction and quantization shift the frontier in qualitatively different ways (vertical vs. leftward curves) — elegantly explains why they are not interchangeable and why eviction dominates for small models where the full-KV memory ceiling binds first. Both insights are specific to the reasoning-model regime where KV cache can equal or exceed weight memory.

---

## Suggestions

1. **Resolve the threshold inconsistency:** Either unify the abstract/intro framing to say "scale thresholds" (plural), or add a paragraph reconciling why the eviction-vs-quantization threshold (~8-bit 8B) is higher than the weight-vs-KV-allocation threshold (~8-bit 4B).
2. **Add bootstrap error bars to Figures 1 and 2** for the key comparisons that define the threshold.
3. **Reorganize the findings into two categories explicitly:** "scale-governed" (Findings 1, 3, 4, 5) and "task-governed" (Finding 2), so readers understand which axis each result belongs to.
4. **Quantify sensitivity to number of generations in Section 5:** Even informally reporting that reducing from 32 to 8 generations does not change the rank ordering of compression strategies would increase confidence in the KV compression results.

---

## Score and Decision

### Calibration

**Round 1 — Bracketing anchors:**

| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| `wg1PCg3CUP.md` (Scaling Laws for Precision) | 8.00 | R1 | Derives formal predictive scaling laws over 465+ runs; stronger theoretical grounding than this paper |
| `OfjIlbelrT.md` (FlexPrefill) | 8.00 | R1 | Proposes a novel sparse attention mechanism with clear computational savings; more methodologically novel |
| `9HK2rHNAhd.md` (SqueezeAttention) | 5.50 | R1 | Proposes a specific layer-wise KV method; comparable scope; this paper is broader |
| `z1ohBxWeL2.md` (SwiftKV) | 5.50 | R1 | Novel model transformation for prefill; more methodologically specific; this paper covers more ground |
| `eZAlb8fX5y.md` (KVTQ) | 4.40 | R1 | Proposes ternary KV compression; narrower; weaker evaluation |
| `2DD4AXOAZ8.md` (MixAttention) | 2.00 | R1 | Architecture modification paper with weaker evaluation |

**Initial bracket: 5.0–7.0.**

**Round 2 — Narrowing anchors:**

| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| `VNckp7JEHn.md` (Inference Scaling Laws) | 5.75 | R2 | Closest analog: also studies compute-optimal inference trade-offs between model size and tokens; proposes REBASE algorithm; limited to math tasks only; mixed reviews |
| `6VhDQP7WGX.md` (Inference Optimal VLMs) | 5.80 | R2 | Studies VLM token-size trade-offs; derives scaling laws; proposes QueCC method; more novel in VLM context but less breadth |
| `6qUUgw9bAZ.md` (Learning How Hard to Think) | 6.50 | R2 | Proposes adaptive compute allocation method; methodologically more novel than empirical study; accepted |
| `OVxmpus9NA.md` (Progressive Mixed-Precision) | 6.00 | R2 | Novel phase-aware quantization method; cleaner methodological contribution; comparable acceptance threshold |
| `1RrOtCmuKr.md` (Network Memory Footprint) | 6.33 | R2 | Novel codebook quantization method; more algorithmically novel |
| `lDbjooxLkD.md` (Predicting Emergent Abilities) | 6.00 | R2 | Empirical study of scaling; broader scope; accepted |
| `0xUEBQV54B.md` (Large Language Monkeys) | 5.00 | R2 | Related repeated sampling analysis; rejected; less breadth |

**Narrowing analysis:**
- The paper is clearly better than the 5.75 "Inference Scaling Laws" anchor: it covers 5 factors vs. 2–3, tests multiple model families, includes KV cache compression, and provides more consistent results with cleaner evaluation.
- The threshold inconsistency (abstract/introduction vs. Finding 5) and the GPQA-Diamond finding not fitting the scale-governed narrative are genuine framing issues that pull the paper below the 6.5 "Learning How Hard to Think" anchor (which has a clear, novel methodological contribution).
- The 6.0 anchors ("Progressive Mixed-Precision," "Predicting Emergent Abilities") represent papers with a clear novel contribution or a clean empirical scope — this paper is at that tier in terms of empirical quality and breadth, slightly moderated by the framing inconsistency.

**Final score: 6.0.** The paper is stronger than the 5.75 anchors in empirical breadth and practical relevance, at the level of 6.0 anchors in terms of overall contribution, but pulled from 6.5 by the threshold inconsistency and the partially unified narrative.

**Originality:** Moderate-high. Studying memory-optimal reasoning model deployment via Pareto frontier analysis is genuinely new; the specific findings about scale-dependent thresholds are not obvious.

**Importance:** High. With reasoning models now the dominant deployment paradigm, practitioners urgently need memory optimization guidelines of exactly this kind.

**Claim support:** Good overall; weakened by the threshold inconsistency between abstract and Finding 5, and the absence of uncertainty quantification on AIME25.

**Soundness of experiments:** Good. 1,700+ configurations, multiple model families, multiple benchmarks, ablation on quantization scheme (AWQ/FP8 vs GPTQ). The reduction to 8 generations in Section 5 is the only methodological uncertainty.

**Clarity:** Good, with the threshold inconsistency as a notable clarity problem.

**Value to research community:** High. Provides actionable, Pareto-grounded guidelines for reasoning model deployment decisions.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>