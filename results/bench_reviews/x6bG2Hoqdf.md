Now I have all the information needed. Let me synthesize the final review.

## Summary

This paper introduces CALM, a framework for automatic heuristic design (AHD) that co-evolves both the prompt generation strategy and the LLM itself via GRPO-based reinforcement learning. While prior LLM-based AHD methods keep the underlying LLM frozen and only manipulate prompts ("verbal gradients"), CALM uses heuristic performance as a training signal to fine-tune the LLM during search ("numerical gradients"), enabling it to discover better heuristics. Using an INT4-quantized Qwen2.5-7B model on a single 24GB GPU, CALM outperforms SOTA baselines that rely on much more powerful API-based models (GPT-4o-mini) across four optimization tasks (OBP, TSP, CVRP, OP), and the paper includes a thorough ablation study decomposing each component's contribution.

## Strengths

- **Novel integration of RL-based LLM fine-tuning into AHD.** CALM is a first framework that jointly optimizes both the prompt generation process and the LLM parameters via GRPO during heuristic search. The ablation (Table 4) confirms that removing GRPO degrades OBP performance from 0.71% to 1.78% gap, directly validating that the co-evolution mechanism drives improvement. This is a clear departure from prior work (EoH, ReEvo, MCTS-AHD) that keeps the LLM frozen.

- **Consistent SOTA performance with a substantially weaker base model.** Across all four tasks, CALM using an INT4-quantized Qwen2.5-7B-Instruct (objectively the weakest model in the comparison) outperforms GPT-4o-mini-based baselines: OBP 0.71% vs. next best 0.82% (MCTS-AHD), CVRP 3.83% vs. 5.44% (MCTS-AHD), OP 12.58% vs. 15.10% (ReEvo). This demonstrates that RL-based co-evolution can compensate for a significant gap in foundation model capability.

- **Thorough and systematic ablation study.** Table 4 evaluates 11 ablation conditions covering reward design variants, collapse mechanism hyperparameters, and operator removal. This allows readers to decompose the contribution of each component — e.g., removing simplification causes the largest drop (1.35% on OBP), and the collapse mechanism with poor hyperparameters (δ₀=0.005, C=15) hurts markedly (1.93%). The ablation isolates the RL component's contribution from the prompt operator design.

- **API-based ablation disentangles operator design from RL.** The "CALM (API, w/o GRPO)" variant shows that even without RL, CALM's prompt operators (using GPT-4o-mini with G=1) are highly competitive with MCTS-AHD — e.g., OBP 0.82% vs. 0.89%, and outperforming on CVRP and OP. This cleanly separates the contribution of the prompt engineering from the RL fine-tuning.

## Weaknesses

### Fatal
None.

### Major

- **Unequal evaluation budgets compromise the main baseline comparison for TSP, CVRP, and OP.** The paper reports "1,000 heuristic evaluations for baselines and a fixed budget of 2,000 LLM queries for CALM" on these three tasks (p. 7, lines 447–448). Since each LLM query in CALM produces a response that is evaluated, CALM effectively evaluates up to 2,000 candidates versus the baselines' 1,000. This 2× advantage in evaluation budget could explain part of the performance gap, independent of the method's innovations. The paper acknowledges this framing only for OBP (where baselines get 2,000 evaluations from 4,000+ queries, making the comparison there actually query-efficient for CALM) but does not correct or control for it on TSP, CVRP, and OP. A controlled comparison where CALM is run with 1,000 queries (e.g., T=250, G=4) against baselines at 1,000 evaluations would be needed to isolate the method's contribution from the extra search budget. While the ablation study (Table 4) holds budget constant within CALM's internal comparisons, the headline superiority claim over baselines on these three tasks remains partly confounded.

- **Budget reporting inconsistency.** The paper states that baselines use "1,000 heuristic evaluations" but also that the API-based CALM variant matches "the query budgets of prior LLM-based AHD methods" at 2,000 queries for TSP/CVRP/OP (Section 5.2). These two statements are difficult to reconcile — it is unclear whether "heuristic evaluations" and "LLM queries" refer to different things in the baseline context, or whether the paper is internally inconsistent. Either way, the ambiguity makes it hard for readers to assess the fairness of the comparison.

### Minor

- **EvoTune re-implementation lacks validation.** The paper re-implements EvoTune within Unsloth because the original requires ~80GB of GPU memory (Appendix H.2). No validation is reported that the re-implementation reproduces the original EvoTune's performance on a common benchmark. Since EvoTune is the main RL-based baseline, any deviation (reward scaling, quantization, hyperparameters) could bias the comparison. This concern is somewhat mitigated by EvoTune's very poor results (e.g., 2.40% on OBP vs. CALM's 0.71%), but the uncertainty remains unaddressed.

- **No direct evidence that fine-granularity operators improve RL credit assignment.** The paper motivates the injection and replacement operators as helping GRPO "more effectively identify the contribution of individual structural changes" (Section 4.1). The ablation shows removing these operators hurts performance, but this is equally compatible with the explanation that the operators simply reduce the search space or introduce useful inductive biases — not that they improve token-level gradient attribution. Direct evidence (e.g., gradient analyses, token attribution comparisons) would strengthen this claim.

- **Collapse mechanism hyperparameters require careful tuning.** The collapse mechanism's probabilistic triggering depends on δ₀ and C. Table 4 shows that while most configurations work well, the setting (δ₀=0.005, C=15) causes a large degradation (OBP: 1.93% vs. 0.71%). The paper acknowledges this but does not provide a systematic sensitivity analysis across tasks. This limits the mechanism's turn-key applicability, though the default configuration (δ₀=0.0005, C=25) performs robustly.

### Trivial
None.

## Nice-to-Haves

- Run CALM with 1,000 total queries (e.g., T=250, G=4) and compare directly against baselines at 1,000 heuristic evaluations to verify that the performance advantage persists under budget-matched conditions.
- Validate the EvoTune re-implementation by reporting its performance on a standard task from the original paper under the same LLM and GPU configuration.
- Provide gradient-based analysis (e.g., token attribution scores) to substantiate the claim that injection/replacement operators improve RL credit assignment beyond search space reduction.

## Removed Points

- **Criticism that the RL component is not unique to CALM because adding RL to MCTS-AHD also helps (Appendix I.9).** This is not a weakness — the paper transparently reports this experiment and correctly notes that CALM benefits *more* from RL than MCTS-AHD does, which supports the claim that CALM's operator design is tailored for RL integration. Removed as the paper actually addresses this constructively.

- **Criticism about the analytic approximation (Equation 2) being tangential.** While fair, this does not harm any core claim; it is presented as a supplementary detail. Removed as a non-substantive complaint about scope.

- **Strength Finder's claim about "comprehensive and fair evaluation against baselines" regarding budget.** This conflicts with the verified budget disparity weakness described above, so per instructions the weakness wins. The strength is dropped from the Strengths section.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface novel observations about the method or results that go beyond what the paper itself articulates.

## Suggestions

1. **Address the budget confound directly.** Either provide a controlled experiment with matched evaluation budgets, or clearly explain why the "1,000 heuristic evaluations" and "2,000 LLM queries" are in fact comparable (e.g., because a fraction of prior methods' queries fail and do not yield evaluable heuristics, or because "evaluation" has a different meaning in each context). The paper's own reporting is ambiguous, and until this is clarified the central comparison is under a cloud.

2. **Validate the EvoTune re-implementation**, even briefly in the appendix, by showing it reproduces similar results on a task from the original paper under the same conditions.

3. **Clarify the distinction between prompt operators' role in search space reduction vs. RL credit assignment** — this could be addressed with even a simple analysis (e.g., measuring token-level gradient norms with and without the operators).

## Score and Decision

I compared this paper against the following calibration anchors (all from the ICLR 2026 human review corpus):

| Anchor Path | Avg Score | Comparison |
|---|---|---|
| `aITKXFeivk.md` (RFTHGS) | 6.00 | Similar topic (RL fine-tuning LLM for optimization). RFTHGS focuses on CVRP only; CALM covers 4 tasks with more thorough ablations but has a budget confound that RFTHGS does not. Roughly comparable quality. |
| `tIQZ7pVN6S.md` (MoH) | 5.00 | Meta-optimization for LLM heuristic generation. CALM's empirical validation is broader and the ablation is more systematic. CALM is stronger. |
| `6f8qlK7wN4.md` (RedAHD) | 5.33 | End-to-end AHD via reductions. RedAHD has a larger conceptual scope but the score is split (8, 4, 4). CALM's experiments are cleaner and more controlled. CALM is slightly stronger. |
| `yX1gmPYHOL.md` (AutoHD) | 5.50 | Inference-time heuristic discovery for LLM reasoning. Different framing but related methodology. CALM is more comprehensive in empirical scope. CALM is stronger. |
| `HWxHUO15Yy.md` (HeuriGym) | 6.00 | Benchmark for LLM-generated heuristics. Different contribution type (evaluation framework vs. method). Not directly comparable. |
| `VEMknlIPtM.md` (TPD-AHD) | 3.00 | LLM-AHD with preference optimization. Much weaker novelty and validation. CALM is substantially stronger. |
| `oD9RwlFqEE.md` (EvoPH) | 2.00 | Co-evolution of prompts and heuristics. Very similar high-level framing but lacks RL fine-tuning, has narrower evaluation, and was withdrawn. CALM is substantially stronger. |

Relative to these anchors, CALM presents a well-motivated and well-validated contribution. The budget confound is a genuine concern but does not rise to the level of invalidating the paper's contributions, given that (a) the OBP comparison is fair or favors baselines, (b) the internal ablation cleanly validates the RL component with budget held constant, and (c) the API-based variant (without RL) is competitive at comparable budgets. The paper's thorough ablations, consistent SOTA across 4 tasks with a weaker base model, and the novel integration of RL fine-tuning into AHD represent a solid contribution.

**Score: 6.0 / Decision: Accept (Poster)**

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>