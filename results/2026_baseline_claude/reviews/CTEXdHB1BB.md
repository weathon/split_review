## Summary
CANON (Conditional advaNtage estimatiON) is a novel advantage estimation method for RLVR (Reinforcement Learning with Verifiable Rewards) training of LLMs. It groups sampled responses into two equal-sized groups based on a target metric (e.g., per-token entropy or response length), then computes inter-group advantages (which metric trend leads to higher reward) and intra-group advantages (which response within the same trend is better). The approach is direction-agnostic—it does not presume whether higher or lower metric values are better—and is theoretically shown to be a strict generalization of DR.GRPO (recovered at µ=0.5). CANON is evaluated across three LLMs, six math benchmarks, and complex logic reasoning tasks, and also shows efficiency gains via weighted advantage on response length.

## Strengths

- **Elegant conceptual contribution**: The core insight—that incorporating a metric via directional advantage shaping is brittle, whereas a group-comparison approach is direction-agnostic—is well-motivated. The paper shows that entropy can favor lower values (more certainty, math tasks) or higher values (more exploration, hard logic), which a fixed directional prior cannot simultaneously exploit. The regrouping mechanism handles this naturally.

- **Theoretical grounding**: Theorem 1 proves that equal-sized groups yield a strictly stronger advantage signal than DR.GRPO when the metric correlates with reward differences. Theorem 2 shows selective amplification: grouping by metric *c₁* does not amplify an independent metric *c₂*, confirming that CANON amplifies only the targeted factor. Both results directly motivate the design decisions.

- **DR.GRPO as a special case**: Equation 7 elegantly shows that DR.GRPO equals CANON at µ=0.5, providing a theoretical unification and a principled baseline rather than an ad hoc comparison.

- **Comprehensive empirical validation**: The paper tests across three models of varying sizes and families (Qwen2.5-Math-7B, Qwen2.5-Math-1.5B, Llama3.1-8B), six math benchmarks, three complexity levels of ZebraLogic, and performs efficiency analysis with full Pareto curves. The ablation comparing CANON to direct numerical scaling of advantages (Table 4) is particularly informative—it confirms the improvement comes from selective signal amplification, not simply larger gradients.

- **Pareto efficiency gains**: For token efficiency, CANON-Eff Pareto-dominates all tested baselines (Clip Length, Length Reward +/*, DR.GRPO) in Figure 4c. The instability of Length Reward (+) (performance drops from 54.8 to 22.5 on a small coefficient change) versus CANON-Eff's stable exploration of the frontier is a compelling practical advantage.

## Weaknesses

### Fatal
None.

### Major

- **Model-specific scheduling strategy selection is opaque and limits generalizability**: The paper applies different scheduling strategies to different models (Cosine-First-Inter-Later-Intra for 7B and Llama-8B, First-Inter-Later-Intra for 1.5B). The paper partially acknowledges this ("different models may have different numbers of parameters… a specifically designed strategy is acceptable"), but provides no principled criterion for choosing among the four strategies without running experiments. In the absence of such guidance, practitioners must perform expensive strategy selection sweeps, which substantially reduces the method's practical plug-in value.

- **The radar chart visualization (Figure 3) presents schematic rather than actual values**: The table embedded in Figure 3 shows values (e.g., Llama-8B CANON-Dynamic = 35.2/35.2) that do not correspond to any directly traceable calculation from Table 2 (where Llama-8B Cosin-First-Inter-Later-Intra has math Acc=22.6 and logic Acc=18.9). The radar positions appear to be schematically chosen for visual clarity, but the lack of an explicit normalization explanation makes it appear as if CANON-Dynamic reaches 35.2% math accuracy for Llama-8B, when the actual value is 22.6%. The actual Table 2 results support the claims adequately; the chart should either use direct values or explicitly state its normalization convention.

### Minor

- **Sensitivity to group balance is not analyzed**: Theorem 1 requires equal group sizes for the inter-group advantage to dominate. In practice, sorting by metric and splitting 50/50 is straightforward, but the paper does not show what happens when the metric distribution is highly skewed or the number of responses per prompt is odd/small. An ablation on unequal group sizes would confirm robustness.

- **AIME 24/25 are noisy small benchmarks**: Results on AIME 24 and AIME 25 are reported as Avg@10 over very small sets (30 problems each). Differences like "CANON-Inter achieves 32.7 on AIME24 vs. DR.GRPO's 27.7" could reflect high variance. Reporting confidence intervals or standard deviations for these benchmarks would strengthen the claims on the most challenging math subsets.

- **Two hyperparameters introduced without joint tuning guidance**: CANON introduces µ (inter-vs-intra balance) and α (group weighting for efficiency). Sections 5.1–5.3 address each separately, but there is no discussion of how to tune them jointly in a combined setting.

### Trivial
- The paper's notation uses $G_q$ to denote both the group size (scalar) and the group set of sampled responses, which occasionally creates notational ambiguity.

## Nice-to-Haves
- A principled automatic strategy selection criterion for scheduling µ (e.g., based on validation performance, task type detection, or training signal statistics) would greatly increase practical usability.
- Extending experiments to non-math reasoning domains (e.g., coding, multi-step QA) would show whether the entropy-grouping insight generalizes beyond the evaluated tasks.
- Showing training curves for efficiency experiments (CANON-Eff) analogous to Figure 2 would help verify that the length reduction is not simply due to mode collapse.

## Novel Insights
The most genuine novel insight beyond the stated contribution is the identification that *inter-group and intra-group advantages serve complementary roles aligned with different reasoning modes*: inter-group advantage implicitly promotes certainty (lower entropy, math) while intra-group advantage implicitly promotes diversity (higher entropy, exploration for complex logic). This provides a principled post-hoc explanation for why DR.GRPO (µ=0.5) exhibits mediocre performance on both task types—it is unable to favor either mode, whereas CANON's scheduling can transition between them. The "gain of rethinking" curve in Figure 6 elegantly operationalizes this trade-off, showing CANON-Dynamic achieves positive rethinking gains while maintaining high training reward, which neither CANON-Intra nor CANON-Inter alone can do.

## Suggestions
- Replace or clearly annotate the radar chart to indicate that its positional values are normalized/schematic, and provide a table of actual benchmark numbers alongside it (Table 2 partially serves this role but is separated from the figure).
- Add a simple decision rule or heuristic (even if heuristic) for choosing between scheduling strategies, based on observable training signals such as training accuracy range or model size category.
- Report standard deviation across multiple runs for small-sample benchmarks (AIME 24/25) to confirm statistical reliability of claimed gains.

## Score and Decision
The paper addresses a genuine and important problem in RLVR training, proposes a clean and theoretically grounded solution, demonstrates consistent improvements across multiple models and tasks, and provides a useful unification of DR.GRPO as a special case. The weaknesses—primarily the model-specific scheduling and the radar chart transparency issue—are real but do not invalidate the core contribution. The method is well-executed and the efficiency experiments present a compelling Pareto improvement. This is a solid contribution to the RLVR community.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>