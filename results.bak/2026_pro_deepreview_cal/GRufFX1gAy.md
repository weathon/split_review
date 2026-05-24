Now I have a comprehensive understanding of the paper and the calibration anchors. Let me write the final review.

---

## Summary

InnoGym introduces the first benchmark and framework for evaluating the *innovation potential* of AI agents, moving beyond correctness-only evaluation by measuring two complementary dimensions: **performance gain** (G) — improvement over best-known solutions — and **novelty** (N) — methodological dissimilarity from prior approaches. The benchmark (iBench) comprises 18 curated "Improvable Tasks" from real-world engineering and scientific competitions, filtered through a two-stage curation pipeline, and is paired with iGym, a unified agent execution environment. Experiments across three agent scaffolds reveal that current agents achieve non-trivial novelty but consistently fail to produce positive performance gains, highlighting robustness as the primary bottleneck.

## Strengths

- **Principled innovation framework with dual metrics.** The paper formalizes innovation as a combination of performance gain and methodological novelty (Equations 2 and 3), with a clear taxonomy distinguishing breakthrough, performance, and conceptual innovation (Section 2.2). This moves beyond correctness-only evaluation and provides a replicable foundation — a genuinely novel contribution to agent evaluation.

- **Rigorous benchmark construction.** The two-stage filtering pipeline (197 → 72 → 18 tasks, Figure 2) with resource availability checks, evaluator validation (Pearson ≥ 0.9, Kendall-τ ≥ 0.8 for score consistency), and solution collection is well-documented. Each task is augmented with validators, normalized evaluators, and partitioned visible/hidden data, ensuring reproducibility and fairness.

- **Empirical demonstration of a novelty-vs-performance gap.** Table 2 provides concrete evidence that agents achieve measurable novelty (average N up to 56.55) yet consistently produce negative performance gains, with no agent surpassing known human bests on any task. This finding — that robustness, not creativity, is the current bottleneck (Section 4.2) — is both insightful and well-supported by the data.

- **Rich ablation experiments on the CirclePacking task.** The controlled experiments in Section 4.3 demonstrate the metrics' ability to track innovation dynamics: novelty decreases during iterative refinement (Figure 5), base model strength drives performance gains (Figure 6b), and sampling temperature reveals an exploration–exploitation trade-off with a sweet spot at 0.5–0.75 (Figure 6c). The complex-plane visualization (Figure 5b) is an elegant synthesis of G and N.

- **Unified execution environment (iGym).** The iGym SDK provides asynchronous tool dispatching, recovery mechanisms, and consistent resource management (Section 3.5, Figure 4), enabling reproducible long-horizon evaluations across diverse agent scaffolds — a practical infrastructure contribution beyond the benchmark itself.

## Weaknesses

### Fatal

None.

### Major

- **Novelty metric validation not summarized in the main paper.** Novelty N(s) is computed by having GPT-5 rate methodological dissimilarity on six rubric dimensions (0–4 scale), aggregated via minimum distance over S_known. This is the benchmark's most distinctive feature and the basis for its claim to evaluate innovation beyond prior benchmarks. The paper states that "a more detailed analysis of the behavior and reliability of D [is] in Appx. F" (Section 4.1), but the main paper contains no summary of validation results — no correlation with human expert judgments, no sensitivity to prompt variation, no comparison against simpler baselines (e.g., embedding distances). A reader evaluating the paper on its main body cannot assess whether the novelty scores reflect genuine methodological creativity or LLM-judge idiosyncrasies. The credibility of InnoGym's central measurement depends on this validation; at minimum, the main paper should summarize key findings from Appendix F.

### Minor

- **Tension between "conceptual innovation" and the claim that "novelty is only meaningful when effective."** Section 2.2 explicitly defines "conceptual innovation" as G(s) ≈ 0 with high N(s) — valuable novelty without performance improvement. Section 4.1 states "high novelty scores are considered important only when accompanied by substantial performance gains." While the framework clearly intends to value conceptual innovation, the Section 4.1 phrasing over-narrows the scope and creates a confusing signal about how the evaluation treats high-N, low-G solutions.

- **Best-of-3 reporting without variance information.** The paper reports only the best run among three attempts (Section 4.1), with no information about success rates, run-wise variance, or whether the reported novelty comes from the same run that achieved the best gain. For a benchmark paper, reporting these statistics would let readers assess result stability and reproducibility.

- **Task-drop transparency could be strengthened.** The filtering from 72 to 18 tasks is described as balancing "across domains, prioritizing newer and more representative tasks" (Section 3.1). A brief accounting of why specific tasks were dropped (e.g., broken evaluators, resource constraints) would preempt concerns about cherry-picking and improve benchmark credibility.

- **Analysis experiments limited to a single task and framework.** The CirclePacking analysis (Section 4.3) — while well-designed — is conducted on one task with one agent framework (AIDE). The generalizability of the temperature, model, and temporal dynamics conclusions is not established. The paper should be more explicit about this limited scope.

### Trivial

- **Notation imprecision in the normalized ratio.** Ratio(s) is defined as G(s)/V*(s) (Section 4.1), where V* is the theoretical optimum. In Table 2, the computed ratios use the best-known leaderboard score V*_known (consistent with G's definition in Equation 2). The notation should be corrected to Ratio(s) = G(s)/V*_known to avoid confusion.

## Nice-to-Haves

- Comparing the LLM-judge novelty scores to a simpler baseline (e.g., embedding-based code dissimilarity) would demonstrate that the expensive GPT-5 step adds genuine value over cheaper alternatives.
- A concrete worked example showing the novelty extraction and evaluation process end-to-end would make the pipeline more tangible for readers.
- Acknowledging that the framework measures innovation at the product level (submitted solution) rather than the process level (how the agent arrived at it) would strengthen the paper's framing of its own scope.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Overclaims that existing work overlooks innovation entirely"** (Harsh Critic): The paper's statements that "most existing benchmarks focus solely on whether an answer is correct" and "methodological differences are often overlooked" are reasonable characterizations, not overclaims. Removed.
- **"Ignores the process by which the agent arrived at the solution"** (Harsh Critic): This is a legitimate design choice, not a weakness. The paper evaluates output innovation; process-level evaluation is out of scope. Removed.
- **"Novelty scores high even when performance is near worst"** (Harsh Critic): This is an interesting finding the paper explicitly discusses (Section 4.2, "The Primacy of Robustness over Novelty"), not a weakness. Removed.
- **"The benchmark may be resource-intensive"** (implied by some calibration anchors): The paper targets long-horizon, complex tasks; computational cost is inherent and acknowledged by using a 10-task subset. Not a weakness of the contribution.
- **"No evidence the LLM judge correlates with human assessment" treated as fatal** (Harsh Critic): Demoted to Major because the paper defers validation to Appendix F, and a fatal claim depending on appendix content is speculative per the review guidelines.

## Novel Insights

The calibration exercise surfaces an important distinction for benchmark papers: conceptual novelty (like InnoGym's innovation framework) and execution scale (number of tasks, models evaluated) are often in tension. MLE-Bench (8.0) succeeds through comprehensive scale and rigorous execution on a simpler concept; InnoGym contributes a more novel evaluation paradigm but at a smaller scale with the core metric's validation deferred to appendix. The field appears to reward execution rigor somewhat more than conceptual ambition for benchmark papers at ICLR. This paper's contribution would be significantly elevated by even a brief summary of human-validation results for the novelty metric in the main body.

## Suggestions

- **Summarize Appendix F validation in the main paper.** Even two sentences reporting correlation with human expert judgments, inter-annotator agreement, or sensitivity to prompt variation would substantially strengthen the core claim.
- **Align the language in Section 4.1** with Section 2.2's taxonomy by clarifying that "novelty is most impactful when accompanied by non-negative performance" rather than requiring "substantial performance gains."
- **Report success rates and variance** (number of valid submissions out of 3, mean ± std for G and N across successful runs) alongside the best-of-3 results in Table 2.
- **Add a brief task-drop table** listing the most common failure categories from the 72→18 filtering step.

---

**Calibration anchors used:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| StarCraft II Arena | 3.00 | R1 | Much weaker; basic benchmark with limited contribution |
| TeamCraft | 3.25 | R1 | Much weaker; domain-specific without conceptual novelty |
| ZeroSumEval | 3.00 | R1 | Much weaker; competition protocol, not a benchmark framework |
| ScienceAgentBench | 6.00 | R2 | Comparable or slightly weaker; expert-validated but conceptually narrower |
| AgentBench | 6.20 | R1/R2 | Comparable; diverse environments but limited conceptual novelty |
| AgentQuest | 6.25 | R2 | Similar tier; game-based agent evaluation |
| VisualAgentBench | 5.75 | R2 | Weaker; domain-specific visual agent benchmark |
| SPA-BENCH | 7.33 | R2 | Stronger; larger scale (340 tasks, 11 agents) with thorough engineering |
| MLE-Bench | 8.00 | R1/R2 | Stronger; comprehensive scale (75 tasks) with rigorous execution |
| Cybench | 8.67 | R1 | Much stronger; excellent curation, high impact, clear significance |

**Round 1 bracket:** Between 5.5 and 8.0, based on comparison with ScienceAgentBench (6.00) on the low end and MLE-Bench (8.00) on the high end.

**Round 2 narrowing:** InnoGym's conceptual contribution (innovation framework) is stronger than ScienceAgentBench (6.00) and AgentBench (6.20), but its execution scale and the novelty-metric validation gap place it below SPA-BENCH (7.33) and MLE-Bench (8.00). The paper lands in the 6.5 range — a clear accept with reservations about the central metric's validation being invisible in the main text.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>