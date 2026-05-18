Now I have all the information needed. Let me compose the final consolidated review.

---

## Summary

This paper proposes RaDA (Rational Decision-Making Agent), a framework that enables LLMs to internalize utility judgment through an iterative process of Experience Exploration and Utility Learning. The key idea is to assign Elo scores to individual decision steps via pairwise comparisons between full decision sequences, then use these scores to guide further exploration — all without task-specific external performance metrics. On ToolBench, RaDA achieves a 61.92% Pass Rate (vs. 50.20% for the best baseline DFSDT) and the best Preference Rank (2.19 vs. 2.91), demonstrating both effectiveness and efficiency.

## Strengths

- **Novel framework for learning utility without task-specific heuristics.** The paper proposes an iterative loop of exploration and pairwise-comparison-based Elo scoring that stands in clear contrast to prior work requiring manually-designed external performance measures (e.g., the value prompt in Tree-of-Thought). The distinction is principled: RaDA does not need task-specific guidance, only the LLM's own comparative judgment (Section 4, lines 111–120).

- **Large and consistent empirical gains.** RaDA achieves 61.92% Pass Rate, a >10 percentage point improvement over the best baseline DFSDT (50.20%) on ToolBench (Table 1). The Elo-based selection obtains the top Preference Rank (2.19), clearly ahead of DFSDT (2.91) and its own random variant (3.24) (Table 2). These gains are directly attributable to the proposed method.

- **Efficiency under resource constraints.** Under API call limits from 30 to 300, RaDA maintains the highest Pass Rate while tree-based baselines degrade sharply in low-resource settings (Figure 1, Section 5.4). This demonstrates practical cost-effectiveness.

- **Positive correlation between Elo scores and task success.** The paper partitions ToolBench data by normalized Elo scores and shows a clear monotonic increase in Pass Rate with higher Elo scores across all methods (Figure 2, Section 5.5). This provides convergent evidence that the learned Elo scores capture task-relevant quality.

- **Detailed error analysis.** RaDA shows the lowest incidence of decision failure (14.8% vs. DFSDT 26.4%) and the highest fix rates for hallucinated tool errors (53.3%) and tool call errors (54.0%) among compared methods (Table 3, Section 5.6), supporting the claim that internalized utility judgment enables effective self-correction.

## Weaknesses

### Fatal

None.

### Major

None. The paper's core empirical findings are robust and supported by multiple analyses. No single weakness undermines the central claim that RaDA improves decision-making performance on ToolBench.

### Minor

- **The Elo propagation to intermediate steps (Eq. 5, Section 4.2) is presented without justification.** The formula $v_i = \sum_{d_j \in \text{Child}(d_i)} \alpha_j v_j$ with $\alpha_j = \text{softmax}(v_j/\tau)$ is a heuristic weighted average of children's scores, not derived from the Elo system. The paper offers no argument that this produces meaningful intermediate utilities or any analysis (e.g., correlation with direct LLM ratings of intermediate states) to validate it. Since these scores guide exploration, understanding their quality matters. However, the overall empirical success mitigates this concern — the method works, even if the theoretical underpinning of this specific formula is unclear.

- **The LLM pairwise comparator is not directly calibrated.** The LLM's reliability as a judge — how consistently it evaluates "superior performance," how its judgments correlate with objective task success — is not characterized. The paper provides *indirect* validation (Figure 2 shows Elo correlates with Pass Rate; Table 2 shows Elo-selected trajectories rank highly on the independent ToolEval metric), so this is not a gap in evidence, but a calibration experiment (e.g., comparing LLM judgments against ground-truth success/failure labels) would strengthen confidence that the utility signal is meaningful rather than reflecting the LLM's internal noise.

- **No ablation isolating the iterative feedback loop.** The method couples exploration and utility learning in a single process. Without a variant that explores randomly first and then learns utilities once, it is hard to attribute the gains specifically to the *interactive* feedback between exploration and learning, versus simply having more explored trajectories to compare. An additional variant doing fixed random exploration followed by a single utility learning phase would clarify this.

- **No analysis of the number of exploration rounds.** The paper fixes 20 exploration rounds (Section 5.1, line 271) without justification or sensitivity analysis. A plot of Pass Rate vs. number of rounds would show where performance saturates and help practitioners set this parameter.

- **No statistical significance or variance reporting.** Pass Rates are reported as point estimates from what appears to be a single run on 500 samples. Given LLM output stochasticity, bootstrap confidence intervals or multiple-seed averages would substantially increase credibility (the Preference Rank metric does use 10 seeds, but the main Pass Rate metric does not).

- **"Fix Ratio" definition is unclear.** In Table 3, the denominator of "Fix Ratio" is ambiguous — is it the fraction of *instructions with that error type* that succeed, or the fraction of *occurrences of that error* that are subsequently corrected? The paper states "the fix ratio that models successfully fix the occurred errors to accomplish the instructions" (line 397), but without clarifying the denominator, the numbers are hard to interpret precisely.

### Trivial

- **The rationality claims (Completeness and Transitivity) are trivially satisfied.** The paper states in Section 4.3 that Elo scores satisfy these properties because they are real numbers. This is mathematically true of any real-valued assignment and does not constitute evidence that the scores correspond to meaningful utility. This is a minor presentational overclaim in the Discussion section; the paper's real evidence is empirical, not this formal point.

## Nice-to-Haves

- Validate the intermediate Elo propagation by comparing propagated scores against direct LLM ratings of intermediate states, or replace the propagation with a simpler baseline (e.g., average of children's scores without self-weighting) to isolate whether the current formula adds value.
- Calibrate the LLM comparator by running pairwise comparisons on trajectories with known outcomes and reporting agreement with ground-truth success/failure.
- Report the average number of API calls actually consumed per instruction (not just the limit cap) to clarify cost allocation across exploration rounds.
- Include an ablation varying the number of exploration rounds (e.g., 5, 10, 20, 30) to show convergence behavior.

## Removed Points

- **Criticism about missing LLM comparison prompt:** The parser strips appendix sections from all papers. The prompt details likely exist in the original submission's appendix. Removed per instructions.
- **Criticism that "the LLM comparator is itself a form of external judgment" weakening the contrast with baselines:** The paper consistently distinguishes *manually-designed* task-specific external metrics (e.g., ToolEval requiring annotated preferences) from the LLM's own self-judgment. The baselines (BFS, DFSDT) use ToolEval — a manually-constructed evaluation tool — while RaDA uses only the LLM's internal comparative judgment. This is a meaningful and correctly-drawn distinction. Removed.
- **Criticism that the Elo-Pass Rate correlation (Figure 2) is "in-sample self-consistency":** Elo scores come from pairwise comparisons, while Pass Rate comes from actual task success/failure — these are independently computed signals. The correlation shows that the LLM's comparative judgments correspond to real task outcomes, which is non-circular evidence. Removed.
- **Claim that no comparison with an independent judge exists:** Table 2 already compares Elo-based selection against Preference Rank computed via ToolEval (an independent judge), and Elo-selected trajectories achieve the best rank. Removed.
- **Generic formatting/style nitpicks and criticisms about missing apparatus/appendices:** Removed per instructions.
- Several of the Strength Finder's more generic or unsupported statements were integrated into the more specific strengths above.

## Novel Insights

The most interesting tension raised across the reviews is between the paper's strong empirical results and the theoretical opacity of its core mechanism. The Elo propagation formula is central to guiding exploration but is presented as engineering design rather than principled derivation, and the LLM comparator is uncalibrated. Yet the method works — consistently, across multiple metrics, with substantial margins. This suggests that even a heuristic propagation of pairwise comparison scores through a tree can produce useful exploration guidance, raising the intriguing question of how much *theoretical* precision matters when the underlying signal (LLM comparative judgment) is rich enough to compensate. The paper would benefit from leaning into this tension by explicitly characterizing which aspects of the design are principled and which are pragmatic choices that happen to work.

## Suggestions

1. Add a calibration experiment for the LLM comparator: compute agreement rates between LLM pairwise judgments and ground-truth success/failure on a held-out sample of trajectories. This directly addresses the most common skepticism about using the LLM as its own judge.
2. Add an ablation that does random exploration first (no Elo guidance during exploration), then learns utilities once at the end, to isolate the value of the iterative feedback loop.
3. Report Pass Rates with bootstrap confidence intervals or across multiple seeds (even 3–5) to establish statistical reliability.
4. Clarify the "Fix Ratio" denominator in Table 3.
5. Add a brief discussion acknowledging that the intermediate Elo propagation (Eq. 5) is a heuristic, possibly noting that simpler alternatives (e.g., uniform weighting) were tested or explaining why the softmax-weighted form was chosen.

## Score and Decision

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>