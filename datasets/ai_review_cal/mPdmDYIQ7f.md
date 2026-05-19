- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6
Now I have all the information needed to write a thorough, evidence-based review.

## Summary

This paper introduces MoLAS (Modularized LLM Agent Search), formalizing the problem of automatically designing LLM agent architectures within a modular design space. The authors extract four standardized module types (Planning, Reasoning, Tool Use, Memory) from a literature review of 16 popular agents, yielding 1,050 possible combinations. They propose AgentSquare, a search framework combining *module evolution* (LLM-based code-level generation of new modules) and *module recombination* (strategic re-selection of existing modules), with a performance predictor to accelerate search. Experiments across six diverse benchmarks (web, embodied, tool use, game) show that discovered agents outperform all 12 hand-crafted baselines and three alternative search methods, with an average 17.2% improvement.

## Strengths

- **Standardized modular design space grounded in existing literature.** Section 2 presents a concrete, extensible design space with 4 module types and uniform IO interfaces, derived from a systematic review of 16 recent LLM agents. This provides a reusable framework for consolidating otherwise fragmented prior work.
- **Consistent empirical outperformance across all benchmarks.** Table 2 shows that AgentSquare discovers agents surpassing all 12 hand-crafted baselines (CoT, ToT, Voyager, HuggingGPT, etc.) on all six tasks, and also outperforms three alternative search methods (Random, Bayesian, OPRO). This directly supports the paper's main claim.
- **Ablation study validates both search mechanisms.** Table 3 compares the full model against variants without module evolution and without module recombination. On every task the full model outperforms both ablated versions (e.g., ALFWorld full: 0.695, w/o evolution: 0.649, w/o recombination: 0.616), confirming both operations contribute to the framework's effectiveness.
- **Comparison against diverse search baselines.** AgentSquare is compared against random module search, Bayesian optimization, and prompt-level search (OPRO), and achieves the highest score on every benchmark (e.g., ALFWorld: 0.695 vs. best baseline 0.634). This provides a meaningful calibration against alternative automatic design approaches.
- **Discovered agents yield interpretable architectural insights.** Section 4.4 presents concrete examples of newly discovered modules (e.g., TD planning, SF-ToT reasoning) and identifies which module combinations work best per task (Table 4), supporting the claim that the search produces insights beyond raw performance numbers.

## Weaknesses

### Major

- **Performance predictor validation is qualitative only.** Section 3.5 and Figure 6 present scatter plots of predicted vs. actual performance, and the caption uses the word "correlation," but no correlation coefficients (Pearson/Spearman), ranking metrics, or error analysis are reported. The paper also lacks a controlled ablation that removes the predictor entirely and evaluates all recombination candidates in the real environment — such an ablation would isolate the predictor's actual contribution to search acceleration. Without these, the claim that the predictor "effectively" accelerates search at only 0.025% cost is not quantitatively substantiated. (Verifiable: Figure 6 shows scatter plots only; ablation study Table 3 tests w/o evolution and w/o recombination but not w/o predictor.)

- **Search trajectory comparison may conflate different evaluation budgets.** Figure 5 plots performance vs. number of iterations for AgentSquare, random search, Bayesian optimization, and OPRO. However, AgentSquare's module evolution phase evaluates N candidates in the real environment per iteration (line 181: "These child agents are then real-tested"), while the recombination phase additionally proposes N candidates (evaluated by the predictor). Baselines likely evaluate a single candidate per iteration. If AgentSquare consumes more real evaluations per iteration, plotting performance against iteration count rather than against number of real evaluations gives an unfair efficiency comparison. The paper mentions only controlling for "the same number of few-shot examples" (line 212), not evaluation budget. This undermines the claim that AgentSquare "provides a more efficient searching approach" (Section 4.2). (Verifiable: Algorithm 1 shows N real evaluations per evolution phase; Figure 5 shows performance vs. iterations; no budget-controlled comparison is reported.)

### Minor

- **No variance or uncertainty reported across runs.** None of the results in Tables 2, 3, or the search trajectories report standard deviations, confidence intervals, or any measure of stochastic variation. Given that the tasks involve LLM stochasticity (both from the backbone models and the module-proposing LLMs), single-run results make it difficult to assess whether performance differences are meaningful. (Verifiable: grep for "variance," "standard dev," "confidence interval," "std." returns no matches in the main paper.)

- **Hand-crafted baselines not tested within the modular framework.** The 12 hand-crafted baselines are evaluated in their original monolithic form. The paper does not verify whether each agent retains its performance when re-implemented within the proposed modular interface. If the modular decomposition breaks tight couplings in the original design (e.g., Voyager's planning and memory may be interdependent in ways the standardized IO interface does not preserve), the baseline numbers may not reflect a fully controlled comparison. This does not invalidate the results but is a caveat that should be acknowledged. (Verifiable: Table 2 tests baselines in original form; no re-implementation in modular interface is reported.)

- **Validity of arbitrary module combinations not empirically tested.** The paper states the design space yields 1,050 possible combinations but does not assess whether all combinations are actually functional. The standardized IO interface is designed to guarantee compatibility, but no experiments or analysis confirm that arbitrary cross-agent module combinations (e.g., a Voyager planning module with a Generative Agents memory module) execute correctly without modification. (Verifiable: Line 56 mentions 1,050 combinations; Section 2 discusses the IO interface but provides no empirical verification of cross-combination validity.)

### Trivial

- **Abstract's phrasing "best-known human designs" is slightly ambiguous** — it could be interpreted as a single best overall design rather than the best per-task baseline. The per-task breakdown in Section 4.2 clarifies this, but the abstract's wording could mislead a casual reader.

## Nice-to-Haves

- A controlled efficiency plot using number of *real environment evaluations* (rather than iterations) as the x-axis would cleanly separate the benefit of the search algorithm from the benefit of the predictor.
- Reporting variance (mean ± std) across multiple independent search runs with different random seeds would significantly strengthen confidence in the results, especially given the inherent stochasticity.
- A table reporting per-method total API costs for the full search process would help readers assess practical deployability.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Lack of LLM proposer prompt details.** The reviewer criticizes the omission of meta-prompt content, few-shot examples, and code error handling. Since the appendix (which likely contains these details) is stripped by the parser, this criticism cannot be verified from the available text and is excluded per policy.
- **TravelPlanner ablation analysis.** The observation that TravelPlanner's w/o-recombination variant drops to 0.280 is a descriptive observation about ablation behavior, not a weakness of the paper. The paper already acknowledges that recombination has a larger impact and this task-specific result is consistent with that claim.
- **"Overlap/redundancy among 1050 combinations"** — the reviewer asks whether some combinations are redundant. This is speculative and not a concrete error in the paper; the standardized IO interface by design treats all combinations as distinct.
- **"17.2% average claim" phrasing ambiguity.** Merged into Trivial section as a very minor presentation point.

## Novel Insights

None beyond the paper's own contributions. The two reviews largely agree on the paper's strengths and gaps. A genuinely novel observation from the cross-review is that the efficiency claim (AgentSquare as a *more efficient* search method) rests on two unvalidated pillars — the predictor's accuracy and the fairness of the per-iteration comparison — and that addressing either could change the claim significantly. This is not a new insight per se but a sharper framing of what the paper would need to do to fully substantiate its efficiency narrative.

## Suggestions

1. **Run an ablation without the performance predictor** where all recombination candidates are evaluated in the real environment, and plot performance vs. number of real evaluations across all methods (AgentSquare with and without predictor, Random, Bayesian, OPRO). This single experiment would simultaneously validate the predictor and provide a fair efficiency comparison.
2. **Report correlation coefficients** (Pearson/Spearman) for the predictor's accuracy on each task, along with a top-k selection accuracy metric (how often the predictor ranks the true best candidate in the top 2/3/5).
3. **Report variance** by running the full search at least 3 times with different random seeds and reporting mean ± std for the best discovered agent.
4. **Acknowledge the modular interface caveat** — briefly test 2-3 hand-crafted agents re-implemented in the modular framework to measure any performance shift, or at minimum note this as a limitation.
