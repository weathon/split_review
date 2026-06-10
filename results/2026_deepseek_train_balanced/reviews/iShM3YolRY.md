## Summary

This paper investigates whether open-source LLMs can be practically enhanced for software tool manipulation (generating API calls from natural language goals). It diagnoses three failure modes (API selection, argument populating, non-executable generation), adapts three known techniques (model alignment via programmatic data, in-context demonstration retrieval, system prompts), and introduces the SNACT benchmark with execution-based evaluation. Results show substantial relative improvements (up to 90%) on open-source models, with certain tasks approaching GPT-4 performance under the specific comparison setup used.

## Strengths

- **Systematic diagnosis of failure modes grounded in quantitative analysis.** The paper decomposes open-source LLM failures into three categories and quantifies each across four models (Table 2, lines 173–186). Each identified failure mode directly motivates a corresponding technique, creating a clean diagnosis-to-intervention chain rather than applying generic enhancements.
- **SNACT benchmark fills a genuine gap.** It is the first open-source tool-manipulation benchmark with predefined test cases for execution-based evaluation (line 274), moving beyond heuristic matching used in prior benchmarks.
- **Quantified human supervision effort.** The paper provides concrete, reproducible cost estimates: ~1 developer day per tool (abstract, line 359), <100 alignment templates per task (line 359), O(n) demonstrations for n APIs (lines 233, 242). This specificity is valuable for practitioners evaluating the recipe.
- **Validation of O(n) generalization.** Using 10 human-curated demonstrations that do not match any test case in API combinations, the retriever boosts success rates by up to 79% on a 15-API task (line 251). This empirically supports a non-trivial generalization claim.
- **Oracle roofline analysis (Figure 2).** Before introducing the practical retriever, the paper establishes the upper bound of in-context demonstrations via hand-picked oracle examples (up to 45% improvement, line 199), making the practical retriever results interpretable.
- **Formal API complexity metric (Eq. 1).** Provides a task-agnostic analytical tool for predicting which tasks benefit most from in-context demonstrations, beyond informal difficulty categorization.

## Weaknesses

### Fatal

None.

### Major

- **The "competitive with GPT-4" headline rests on an asymmetric comparison that is not caveated in the abstract or conclusion.** What the experiments compare is *fine-tuned* open-source models against *unfine-tuned* GPT-4 augmented only with system prompts and in-context demonstrations. GPT-4 did not receive model alignment because its tuning APIs were unavailable — this is acknowledged in a footnote (line 57) and in Section 5 (line 335), but the abstract (line 8), introduction (line 57 without footnote context), and conclusion (line 426) state the models are "competitive with OpenAI GPT-4 in 4 out of 8 SNACT tasks" without this caveat. This asymmetry does not invalidate the results, but the headline claim is materially stronger than what the experimental design supports. The real finding — that fine-tuning on programmatically generated data substantially narrows the gap with GPT-4's in-context-learning performance on simpler tasks — is still useful and should be stated as such.

- **WebShop is simultaneously claimed as a "competitive" success and listed as a "remaining challenge."** Line 355 includes WebShop among the 4 tasks where open-source models are "competitive or better." Line 360 then lists WebShop alongside Google Sheets and Tabletop as tasks where "boosted open-source LLMs still have relatively low success rates." The paper does not resolve this tension. WebShop also uses rewards rather than success rate as its metric (line 281), making cross-task comparison unclear. The paper needs to clarify whether "competitive" means matching GPT-4's (potentially also low) performance, and report the actual numbers for both.

- **Ablation study reports only task counts, not success-rate magnitudes (Table 4, lines 367–384).** The table shows only the number of tasks where each technique improves or degrades performance (+N/−N). An improvement from 5% to 15% and from 70% to 85% both count as "+1 task," but have very different practical significance. The full per-task, per-model success rates are deferred to the appendix (line 395). This makes the main paper's central quantitative evidence incomplete — a reader cannot assess whether the reported improvements are meaningful or marginal without consulting supplementary material.

### Minor

- **Three of the four "competitive" tasks are the simplest in the benchmark.** Open Weather and Cat API require only a single API call per goal and are described as "simpler tasks" by the paper itself (line 348). VirtualHome uses executability/LCS metrics rather than success rate (line 281), making it not directly comparable with other tasks. The strongest evidence for the headline claim rests on disproportionately easy tasks. The remaining challenging tasks (Google Sheets, Tabletop) still show large gaps.

- **The surprising finding that instruction-tuned open-source models underperform their base models receives only a footnote (line 340).** This is a non-obvious result potentially important for practitioners and the community. A brief analysis or hypothesis (e.g., overfitting to conversational formats, catastrophic forgetting of code-generation ability) would substantively strengthen the paper.

- **"Up to 90% improvement" is reported without specifying the absolute baseline in the same sentence** (lines 8, 57, 355). Given that baselines are very low (0–7% for some model-task combinations), 90% relative improvement can still yield poor absolute performance. The paper should pair relative improvements with absolute baselines for clarity.

### Trivial

None.

## Nice-to-Haves

- Including a compact per-task, per-model, per-condition success rate table in the main paper (even as a supplementary figure) would let readers assess improvement magnitudes directly without consulting the appendix.
- Reporting GPU-hours for model alignment (fine-tuning LLaMA-30B) would give a more complete picture of the recipe's practicality, since compute cost is a separate barrier from human supervision time.
- A brief discussion of the model-scale confound (LLaMA-30B vs. GPT-4, which is likely much larger) would help contextualize the residual gap on harder tasks.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh Critic's "the paper does not discuss the computational cost of model alignment."** Moved to Nice-to-Haves. The paper's stated scope is human supervision practicality; GPU cost, while practically relevant, is a different dimension and not a core flaw of the work as presented.
- **Harsh Critic's "the paper would benefit from discussing the model scale confound."** Moved to Nice-to-Haves. A valid observation but not a weakness of the existing experiments.
- **Strength Finder's "Measured 90% improvement and competitive parity with GPT-4 in 4/8 tasks."** The "competitive parity" framing conflicts with the verified asymmetry weakness (a strength and weakness disagree → weakness wins per the conflict rule). The 90% improvement is a genuine result retained in the summary/strengths, but the "competitive parity" framing is dropped.
- **Harsh Critic's "the paper's strongest evidence supports improvement, not parity."** This is a summary judgment, not a specific, evidence-anchored weakness. The substance is fully captured by the asymmetry weakness above.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Reframe the headline claim:** Replace "competitive with GPT-4 in 4/8 tasks" with something like "fine-tuned open-source models substantially narrow the gap with GPT-4's in-context-learning performance, approaching or matching it on 4/8 benchmarks, with the largest gains on the simplest tasks." This is accurate and still demonstrates the recipe's value.
2. **Resolve the WebShop tension:** Report absolute reward/performance numbers for both open-source models and GPT-4, and explicitly state whether "competitive" means matching GPT-4's performance (even if both are low). If GPT-4 also performs poorly on WebShop, both statements can be true but need to be explained.
3. **Move a compact version of the full per-task success rate table into the main paper** (replacing or supplementing Table 4's task-count format), so improvement magnitudes are visible without requiring the appendix.
4. **Expand the instruction-tuned underperformance footnote** into a brief analysis paragraph — this is a non-obvious finding that the community would benefit from understanding.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>