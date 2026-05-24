Now I have a thorough understanding of the paper and its relationship to the calibration anchors. Let me compile the final review.

---

## Summary

This paper presents a systematic empirical study of memory–accuracy trade-offs for deploying reasoning LLMs under fixed GPU memory budgets. The authors investigate five factors — model size, weight precision, generation length, parallel sampling, and KV-cache compression — across the Qwen3 model family (0.6B–32B) on mathematical reasoning (AIME25), knowledge-intensive reasoning (GPQA-Diamond), and code generation (LiveCodeBench) benchmarks. The central finding is that memory-optimal strategies are scale-dependent rather than universal, with a threshold around an 8-bit 4B effective size separating two regimes: below it, memory is better spent on larger/higher-precision model weights; above it, allocating memory to longer generations and parallel scaling is more efficient. The paper also finds that KV-cache compression (both eviction and quantization) consistently advances the Pareto frontier across configurations.

## Strengths

- **Comprehensive, principled empirical framework.** The paper systematically explores five interacting factors (model size, weight precision, token budget, group size, KV compression) under a unified memory accounting model (Equation in §3, Table 1). The study spans over 1,700 configurations, giving the findings unusual breadth for a deployment-oriented study. The total memory metric (weights + KV cache) correctly captures what matters for batched reasoning inference, where the KV cache often dominates.

- **Refutation of one-size-fits-all quantization advice.** The paper convincingly demonstrates that the common prescription of 4-bit weights as universally memory-optimal breaks for reasoning models on mathematical and code tasks (§4, Figures 1, 3). On AIME25, 8-bit and 16-bit configurations consistently dominate 4-bit ones at comparable memory — e.g., the 8B-8bit model outperforms the 14B-4bit model. This finding is cross-validated on LiveCodeBench and contrasted with GPQA-Diamond, where 4-bit remains memory-optimal, establishing a clear task-dependence (Finding 2).

- **Cross-family validation of the parallel-scaling threshold.** The finding that parallel scaling via majority voting is memory-inefficient for small effective sizes but beneficial above the 8-bit 4B threshold (Finding 3) is replicated across three model families: Qwen3, DeepSeek-R1-Distill, and OpenReasoning-Nemotron (Figures 5, 6, and Appendix C.6). This is the paper's best-validated claim and provides genuinely actionable guidance.

- **KV-cache compression as broadly beneficial.** The demonstration that both KV eviction (R-KV) and KV quantization (HQQ) consistently advance the Pareto frontier across all tested model sizes and weight precisions (Figure 8, Finding 4) is well-supported and practically important. The further finding that eviction dominates for small effective sizes while quantization becomes competitive for larger ones (Finding 5, Figure 9) adds useful nuance.

- **Honest limitations section.** The paper explicitly acknowledges its Qwen3-centric analysis and the limited set of benchmarks (§7), giving readers an accurate picture of what is and is not demonstrated.

## Weaknesses

### Fatal

None.

### Major

- **The central serial-scaling threshold (Finding 1) lacks cross-model-family validation.** Finding 1 — that memory allocation between model weights and the KV cache flips at an effective size of 8-bit 4B — is the paper's headline result. However, the full serial-scaling Pareto-frontier analysis (varying model size, weight precision, and token budget simultaneously) is presented only for Qwen3 on AIME25 (Figures 1–2). The LiveCodeBench results (Figure 3) show a qualitatively similar pattern, which provides partial cross-task support, but the DeepSeek-R1-Distill and OpenReasoning-Nemotron experiments are limited to parallel scaling (Finding 3) and do not replicate the central serial-scaling regime. While the paper is honest about this in §7, the abstract and introduction frame Finding 1 as a general property of "reasoning models" without sufficient qualification. This gap between the claim's framing and its evidential scope is the paper's most significant limitation.

- **No uncertainty quantification.** All accuracy numbers are reported as point estimates (e.g., averages over 32 generations) without error bars, standard deviations, or confidence intervals. Given that the paper draws sharp conclusions about Pareto dominance — e.g., that one configuration "strictly dominates" another, or that a specific threshold separates two regimes — the absence of any measure of statistical reliability makes it difficult to assess whether these dominance relationships are robust or could be reversed by sampling noise. This is particularly concerning for the threshold claims, where small accuracy differences near the crossover could shift the identified boundary.

### Minor

- **KV-cache compression findings are anchored to a single eviction method (R-KV).** While the paper mentions StreamingLLM as an alternative eviction policy in §2, the main analysis in §5 uses only R-KV. The sensitivity of Finding 5 (eviction vs. quantization preference) to the choice of eviction algorithm is not explored, leaving open the question of whether the conclusion is about eviction in general or R-KV specifically.

- **Only one external verifier evaluated.** The PRM-based Best-of-N analysis (§4.1) tests only ActPRM-X (7B). While the conclusion that external verifiers are memory-inefficient is plausible and well-justified by the fixed memory overhead argument, testing only one verifier limits the generality of this claim.

- **The paper's abstract overstates the cross-family evidence.** The abstract says the findings come from "systematic experiments on mathematical, code generation, and knowledge-intensive reasoning tasks" but does not mention that the central threshold finding is primarily from one model family. A more precise abstract would better align with the evidence.

### Trivial

- The distinction between the 8-bit 4B threshold (Findings 1, 3) and the 8-bit 8B threshold (Finding 5) could be confusing to readers. A brief explanation of why different decisions have different crossover points would improve clarity.

## Nice-to-Haves

- Replicating the full serial-scaling Pareto analysis on at least one additional model family (e.g., DeepSeek-R1-Distill) would substantially strengthen Finding 1.
- Adding confidence intervals or standard errors to the main accuracy-vs-memory plots would make the Pareto-dominance claims more credible.
- Exploring at least one additional KV eviction method in §5 would test whether the eviction-vs-quantization preference generalizes beyond R-KV.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh Critic claim that the threshold is "essentially a characterisation of one model family on one task"** — This overstates the issue. The paper shows a qualitatively consistent pattern on LiveCodeBench (Figure 3), and the parallel-scaling threshold is replicated across three model families. The criticism is partially valid (see Major weakness above) but was softened after verification against the paper.

- **Harsh Critic claim that the paper should "clearly separate the portion of the findings that are demonstrated to hold across families"** — The paper already does this to a reasonable degree in §7 (Limitations), and Findings 1–5 are each scoped with qualifying language. Moved to Nice-to-Haves as a presentation improvement.

- **Strength Finder's "Robustness across quantization schemes and model families"** — Partially valid but overstated. Cross-quantization robustness (AWQ, FP8) is verified, but cross-family robustness is limited to parallel scaling only. Retained the quantization-robustness aspect but qualified the cross-family claim.

- **Strength Finder's claim that "all reported trade-offs are grounded in this real-world memory metric"** — Retained as a genuine strength.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface methodological insights or connections that the paper itself does not already articulate.

## Suggestions

- The most impactful revision would be to add even a partial serial-scaling sweep on DeepSeek-R1-Distill (e.g., 2–3 model sizes × 2 weight precisions × 3–4 token budgets). This would directly address the cross-family gap for Finding 1 without requiring the full 1,700-configuration treatment.
- Report standard errors or bootstrap confidence intervals for the key accuracy measurements, at minimum on the Pareto-frontier configurations. This is standard practice for empirical studies making comparative claims.
- Consider renaming the paper or reframing the abstract to foreground the scale-dependent principle while being precise about which findings have cross-family evidence and which are currently demonstrated on Qwen3.

---

## Score and Decision

**Round 1 bracket:** The paper sits between the weak band (avg ~3.0) and the strong band (avg ~8.0). Comparing against "Exploring the Trade-Off between Model Complexity and Numerical Precision" (3.75) — a small-scale study of a similar question — the paper under review is clearly far stronger in scope, rigor, and practical relevance. Comparing against "Scaling Laws for Precision" (8.00) — which provides theoretical scaling laws with 465+ pretraining runs — the paper under review lacks the theoretical contribution and has narrower evidential support for its central claim. Initial bracket: **5.0–7.5**.

**Round 2 narrowing:** Within the bracket, the closest comparator is "Inference Scaling Laws" (5.75), another systematic empirical study of test-time compute trade-offs for reasoning, limited to math tasks with 2–3 model families. The paper under review has broader task coverage (math, code, knowledge) and studies more factors (5 vs. 2–3), but shares the limitation of anchoring central findings to a narrow model set and lacks error bars. "The Cost of Scaling Down" (6.00) is another empirical characterization study of similar scope and quality. "HeadKV" (6.50) proposes a novel method with strong results but limited scope. The paper under review is comparable in quality to the 6.00–6.50 range — its empirical breadth is a strength, but the gap between the headline claim and cross-family evidence holds it back from the 7+ tier.

**Final score:** 6.0. The paper makes a solid empirical contribution with practical deployment value. The systematic framework and several findings (especially Findings 2–3) are well-supported. The central Finding 1 is plausible and partially validated cross-task but undersupported cross-family for the weight it carries in the paper's framing. These are addressable limitations, and the paper's honesty about them is commendable.

**Anchor summary:**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| Exploring the Trade-Off (Model Complexity vs Precision) | NLfWQfy5zp | 3.75 | 1 | Much weaker: smaller scale, less systematic, on non-LLM tasks |
| Progressive Mixed-Precision Decoding | OVxmpus9NA | 6.00 | 1 | Similar quality; proposes a method rather than a study |
| Inference Scaling Laws | VNckp7JEHn | 5.75 | 2 | Closest comparator; both systematic empirical studies of inference trade-offs for reasoning; this paper has broader task/factor coverage |
| The Cost of Scaling Down | ldJXXxPE0L | 6.00 | 2 | Similar type (empirical characterization); comparable quality |
| HeadKV | FJFVmeXusW | 6.50 | 2 | Proposes novel method; this paper is pure empirical study, slightly less novel but broader in scope |
| Scaling Laws for Precision | wg1PCg3CUP | 8.00 | 1 | Clearly stronger: theoretical contribution, rigorous fitting on 465+ runs |

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>