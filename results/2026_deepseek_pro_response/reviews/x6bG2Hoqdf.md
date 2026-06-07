Now I have enough anchors for calibration. Let me compare systematically:

- **Hercules (5.25)**: CALM is clearly stronger — more novel (RL fine-tuning vs. prompt engineering), more thorough ablation, better evaluation breadth.
- **LLM-LNS (5.25)**: CALM is stronger — LLM-LNS lacks ablations and has unclear component contributions; CALM has better technical depth.
- **BOPRO (6.25)**: Comparable. BOPRO is novel and well-written but has essentially negative results. CALM demonstrates genuine improvements over SOTA but has the budget asymmetry issue. CALM is slightly stronger due to positive results.
- **LLM-SR (8.00)**: CALM is weaker — LLM-SR has cleaner evaluation, stronger benchmarks, more polished presentation.

CALM lands around **6.0–6.5**. It's clearly above the 5.25 cluster and clearly below the 8.00 cluster. It's comparable to or slightly above BOPRO (6.25). The budget issue prevents it from reaching 7.0+, but the genuine novelty (first AHD framework with RL co-evolution), thorough ablation, and practical impact keep it well above the rejection boundary.

Final score: **6.5**.

Now let me write the final review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal
None.

### Major
- Budget asymmetry for non-OBP tasks

### Minor
- Key hyperparameters absent from main text
- Cross-model comparisons foregrounded over cleaner within-model ones
- Training curves only for CVRP and OP
- Only 3 runs; no standard deviations in main tables

### Trivial
- OBP test set small
- Reward function edge case

## Nice-to-Haves
...

## Removed Points
...

## Novel Insights
...

## Suggestions
...

## Score and Decision

Let me finalize the review now.Now let me write the final review with the calibrated score.

## Summary
CALM introduces the first framework for Automatic Heuristic Design (AHD) that jointly optimizes both prompt-based heuristic generation ("verbal gradients") and the LLM parameters themselves ("numerical gradients") through GRPO-based RL fine-tuning during evolutionary search. Unlike all prior LLM-based AHD methods that keep the LLM frozen, CALM treats the evolutionary loop's prompt-response-performance triplets as training data, allowing a quantized 7B model to co-evolve with the heuristic search. The framework includes novel evolutionary operators (injection, replacement, diversity-aware crossover, simplification), a probabilistically-triggered collapse mechanism with analytical backing, and a progressive reward function. Running on a single 24GB GPU, CALM demonstrates strong results across OBP, TSP, CVRP, and OP, with a comprehensive ablation study isolating each component's contribution.

## Strengths
- **Genuine conceptual novelty**: First AHD framework to jointly optimize prompts and model parameters via RL. The idea of using the evolutionary loop's natural prompt-response-performance triplets as GRPO training data is well-motivated, creating a feedback loop where the LLM improves alongside the search process. This is a clear advance over frozen-LLM approaches (FunSearch, EoH, ReEvo, MCTS-AHD) and the concurrent DPO-based fine-tuning work (EvoTune).
- **Systematic and revealing ablation study** (Table 4): Isolates every component's contribution. RL causes the largest performance drop when removed (OBP: 0.71% → 1.78%; OP: 17.41% → 19.89%). Reveals non-obvious interactions: diversity-aware crossover outperforms naive crossover, and naive crossover is *worse than no crossover at all* on OBP (1.05% vs 0.88%), directly validating the diversity-aware design.
- **Verbal gradient operators are independently effective**: CALM-API (GPT-4o-mini, no GRPO, G=1) matches or exceeds prior SOTA across all tasks (OBP: 0.82% vs MCTS-AHD's 0.89%; CVRP: beats all baselines at every scale; OP: surpasses MCTS-AHD on all instances). This cleanly separates operator design contributions from RL contributions.
- **Multi-scale out-of-domain generalization** tested across all four tasks: CALM surpasses per-scale-trained POMO at TSP N=200 (13.41% vs 20.45% gap) and generalizes to unseen scales on OBP, CVRP, and OP without retraining.
- **Practical resource efficiency**: Runs on a single 24GB consumer GPU with INT4 quantization, fine-tuning only 1.15% of weights — contrasting with API-dependent baselines that incur per-query costs and latency.
- **Principled reward design with empirical validation**: The progressive scoring scheme (Equation 4) credits improvements relative to the best parent heuristic rather than absolute performance, mitigating prompt bias. Two alternative reward schemes tested in Table 4 both underperform the proposed design, and the performance-based variant even falls below the no-RL baseline on OP (21.30% vs 19.89%).

## Weaknesses

### Fatal
None.

### Major
- **Budget asymmetry for non-OBP tasks**: For TSP, CVRP, and OP, baselines receive 1,000 heuristic evaluations while CALM receives 2,000 LLM queries (line 140-141). Since each LLM query in CALM produces one heuristic evaluation, CALM evaluates approximately twice as many heuristics as the baselines on these tasks. The paper describes these budgets as "comparable," but a 2× difference undermines direct head-to-head comparisons — it is unclear whether CALM's advantage on TSP, CVRP, and OP derives from the method or the doubled evaluation budget. For OBP the situation is reversed (baselines use >4,000 queries vs. CALM's 2,000), which actually makes OBP results more credible. The training curves in Figure 2 partially address this by showing CALM's trajectory overtaking baselines over the query budget, but the terminal comparison remains confounded. This is addressable: matching budgets or reporting CALM's performance at the 1,000-evaluation mark would resolve the concern.

### Minor
- **Key hyperparameters (G, T, population size, ε, β, α₁, α₂, r_invalid) absent from main text**: G (GRPO group size) and T (number of rounds) are central to understanding the experimental design — particularly the relationship between the 2,000-query budget and the actual number of search rounds. These are deferred to the stripped Appendix H. The main text should be self-sufficient on G, T, and population size.
- **Cross-model comparisons foregrounded over cleaner within-model ones**: While the paper correctly notes GPT-4o-mini is a stronger base model than Qwen2.5-7B-INT4 (line 132-136), the abstract's headline claim that CALM "surpasses methods that rely solely on verbal guidance, even when those use significantly more powerful API-based models" conflates RL fine-tuning with CALM's operator suite. The CALM-API variant already matches or beats baselines without RL, so the cross-model gap cannot be attributed solely to RL. The cleanest comparison isolating RL — "local w/o GRPO" in Table 4 — shows RL provides meaningful but measured gains (OBP: 1.78% → 0.71%, OP: 19.89% → 17.41%). Foregrounding these clean comparisons would strengthen the paper.
- **Training curves shown for only 2 of 4 tasks** (Figure 2: CVRP and OP only). TSP and OBP dynamics are not shown, limiting assessment of convergence behavior across all problem domains.
- **Only 3 runs for variance; no standard deviations in main tables**: For stochastic evolutionary methods with RL, 3 runs provides limited statistical power. Standard deviations are absent from Tables 1-3, making it difficult to assess the reliability of the reported performance gaps, some of which are small.

### Trivial
- The OBP test set has only 5 scale configurations (inherited from prior work, Zheng et al. 2025), which is a small sample for generalization claims.
- The piecewise reward function (Equation 4) has a subtle edge case: the duplicate penalty (α₁ r_invalid) can exceed the underperformance penalty (α₂ r_invalid · Δ) when α₁ > α₂ · Δ, meaning duplicates are penalized more harshly than moderately-worse novel heuristics. This seems counterintuitive but is not discussed.

## Nice-to-Haves
- Extend training curves to TSP and OBP to match the CVRP/OP analysis in Figure 2.
- Report standard deviations or confidence intervals in Tables 1-3.
- Discuss the duplicate-vs-underperformance penalty edge case in the reward function.
- Specify G, T, and population size values in the main text.

## Removed Points
These points are flagged to be removed, treat them with caution:

1. **Harsh Critic — "Confounded model-quality comparisons" framed as a major flaw**: REMOVED as a major weakness. The paper explicitly acknowledges the model quality hierarchy (GPT-4o-mini ≈ Qwen2.5-Turbo > Qwen2.5-14B > Qwen2.5-7B > Qwen2.5-7B-INT4, line 132-136) and the claim is precisely about beating stronger models with a weaker one. This is a valid practical claim, not a methodological confound — if anything, the asymmetry favors the baselines. Retained only as a minor point about presentation framing (foregrounding clean comparisons).

2. **Harsh Critic — Speculation about "local w/o GRPO" using a different evaluation budget**: REMOVED. The paper does not specify the budget for this variant, but the natural reading is that all local variants share the same 2,000-query framework. The harsh critic's concern is speculative without evidence.

3. **Harsh Critic — "Appendix H missing" as a serious methodological gap**: DEMOTED to minor. The stripped appendix contains these values; the issue is only that G and T should appear in the main text for self-sufficiency. Not a gap in the work itself.

4. **Strength Finder — Multiple redundant strengths about the same ablation study (Table 4)**: MERGED into one consolidated strength about the systematic ablation.

5. **Strength Finder — "The GRPO-trained 7B-INT4 model consistently outperforms GPT-4o-mini API baselines" as a standalone strength**: MERGED into the broader cross-model comparison discussion; retained the practical resource efficiency strength instead.

6. **Harsh Critic — "OBP test set has only 5 instances" as a significant weakness**: DEMOTED to trivial since the paper follows established protocols from prior work (Zheng et al., 2025).

7. **Harsh Critic — Request to add variance estimates, extend training curves, report G and T**: These are valid presentation suggestions; retained in Minor/Trivial rather than as standalone weaknesses.

## Novel Insights
None beyond the paper's own contributions. The review process corroborates that CALM's co-evolution of LLM parameters with heuristic search via GRPO is genuinely novel within the AHD literature. One observation from the ablation study that deserves emphasis: the finding that naive crossover (without diversity awareness) is *worse than no crossover at all* on OBP is a non-obvious result with implications for how LLM-based evolutionary operators should be designed in future AHD work.

## Suggestions
- Match evaluation budgets for non-OBP tasks, or report CALM results at the 1,000-evaluation mark to enable fair comparison.
- Move G, T, and population size values into the main implementation details paragraph.
- Add training curves for TSP and OBP.
- Report standard deviations in main result tables.
- Restructure the abstract and introduction to foreground the clean within-model comparisons (CALM vs. EvoTune, local w/o GRPO ablation) before the cross-model ones.

## Calibration Anchors Referenced

| Anchor | Avg Score | Round | Comparison to CALM |
|--------|-----------|-------|--------------------|
| LLM4Solver (XTxdDEFR6D) | 3.40 | R1 | CALM substantially stronger: more novel, better evaluation, systematic ablation |
| MHRE (sUywd7UhFT) | 2.50 | R1 | CALM much stronger: clearer contribution, more rigorous |
| LLMatic (iTrd5xyHLP) | 3.40 | R1 | CALM stronger: broader evaluation, more technical depth |
| Hercules (0fwJMANq9P) | 5.25 | R1/R2 | CALM clearly stronger: RL co-evolution is more novel than prompt engineering, better ablation |
| LLM-LNS (Usk4KzBxLW) | 5.25 | R2 | CALM stronger: has thorough ablation (LLM-LNS lacks any), clearer component contributions |
| BOPRO (aVfDrl7xDV) | 6.25 | R2 | CALM slightly stronger: both novel combinations, but CALM shows positive results while BOPRO has negative results |
| LLM-SR (m2nmp8P5in) | 8.00 | R1 | CALM weaker: LLM-SR has cleaner evaluation, stronger benchmarks, more polished presentation |
| Code Gen Prompting (Zk9guOl9NS) | 7.00 | R2 | CALM somewhat weaker: comparable novelty but cleaner evaluation in anchor |
| STOP (1gkePTsAWf) | 6.20 | R2 | CALM comparable: both self-improving code generation frameworks; CALM has broader evaluation |
| LintSeq (AqfUa08PCH) | 6.50 | R2 | CALM comparable: similar level of technical contribution and evaluation quality |
| Learning Perf Code Edits (ix7rLVHXyY) | 7.25 | R2 | CALM somewhat weaker: anchor has stronger dataset contribution and cleaner evaluation |

**Round 1 bracket**: 5.5–7.0 (between Hercules at 5.25 and LLM-SR at 8.00).

**Round 2 narrowing**: Comparison with BOPRO (6.25), STOP (6.20), and LintSeq (6.50) places CALM in the 6.0–6.5 range. CALM is clearly stronger than the 5.25 cluster (Hercules, LLM-LNS) due to genuine novelty and thorough ablation. It falls below the 7.0+ cluster due to the budget asymmetry issue and some presentation gaps.

**Final score**: 6.5 — accepting with reservations. The budget asymmetry is addressable and does not invalidate the core contribution (the OBP results and within-model ablations stand independently), but it prevents the paper from reaching the 7.0+ tier where evaluation rigor is cleaner.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>