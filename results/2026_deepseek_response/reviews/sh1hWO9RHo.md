## Summary

This paper proposes the Agent GPA (Goal-Plan-Action) framework for evaluating LLM agents through specialized LLM judges across five metrics (Goal Fulfillment, Logical Consistency, Execution Efficiency, Plan Quality, Plan Adherence) plus two auxiliary judges (Tool Selection, Tool Calling). The core idea is decomposing agent evaluation into goal, plan, and action dimensions rather than using a monolithic judge. Empirical validation on TRAIL/GAIA (59 test traces, 281 annotated errors) shows GPA judges detect 95% of errors vs 55% for the TRAIL baseline, and localize 86% vs 49%. Additional experiments on an internal production dataset and a SWE-bench case study with prompt optimization (GEPA) provide preliminary evidence of generalization.

## Strengths

1. **Large and clean improvement over monolithic baseline**: GPA judges detect 95% (267/281) of TRAIL-annotated errors vs 55% (154/281) for the TRAIL baseline LLM judge on the test set (Table 2), and localize 86% (241/281) vs 49% (138/281) (Table 5). These are large, practically meaningful margins on a public benchmark, directly supporting the decomposition argument.

2. **Systematic taxonomy coverage**: All 570 TRAIL/GAIA errors (dev+test) are categorizable under at least one GPA dimension (Table 1), demonstrating that the taxonomy is comprehensive for this benchmark — a property prior taxonomies (TRAIL, MAST) lack. The per-judge error mapping breakdown (Table 1) is informative, showing LC, TC, and EE as the most prevalent failure modes.

3. **Thorough consistency analysis**: The paper evaluates judge stochasticity across 5 independent runs using Krippendorff's α, standard deviation, and a novel Semantic Consistency Index (Table 7, Figure 2). Six of seven metrics achieve α > 0.7, with EE reaching 0.934. This level of reliability analysis goes well beyond what is standard in the LLM-as-judge literature and strengthens confidence in the framework's practical stability.

4. **Per-judge precision/recall profiles provide actionable insight**: The detailed per-judge analysis (Tables 3, 6) reveals interpretable trade-offs — Tool Calling as a high-precision "conservative" judge (F1 > 0.92 on detection), Tool Selection as a high-recall specialist (recall > 0.97), Plan Quality as unreliable due to low precision. This granularity is exactly what the decomposition argument promises and supports practical use-case-specific judge selection.

5. **GEPA prompt optimization shows domain transferability**: On SWE-bench, GEPA-optimized prompts improved LC recall from 28.8% to 75.3% without manual domain-specific retuning (Table 9), suggesting the framework generalizes to coding agents despite being designed for general-purpose web agents. The optimization approach also addresses the practical concern of manual prompt engineering effort.

## Weaknesses

### Fatal
None.

### Major

- **Missing inter-annotator agreement for the error-to-GPA mapping**: Two annotators mapped each TRAIL error to one or more GPA dimensions, and a third verified (Section 4.1.2, line 108). No inter-annotator agreement statistic (e.g., Cohen's κ) is reported for this mapping. Since this mapping defines the ground truth for the per-judge precision/recall metrics in Tables 3 and 6, the reliability of those fine-grained numbers is unclear. Low agreement would not invalidate the headline detection/localization results (Tables 2 and 5 — those compare against TRAIL's original annotations), but it weakens a core selling point of the decomposition: the ability to analyze which specific dimensions each judge handles well or poorly. For PQ and PA in particular, which show very low precision on the test set, it is unclear whether this reflects genuinely poor judge performance or noise in the human mapping.

### Minor

- **Abstract phrasing conflates taxonomy coverage with detection**: The abstract claims the framework "provides a systematic way to cover a broad range of agent failures, including all agent errors on the TRAIL/GAIA benchmark dataset." The paper clarifies internally (line 22) that this means the *taxonomy dimensions* can categorize all errors, not that the judges detect 100%. The empirical detection rate is 95% (267/281). The current wording invites the stronger reading and should be clarified.

- **Baseline comparison does not fully isolate decomposition from prompt quality**: The GPA judges receive custom prompts with agent architecture descriptions and few-shot examples (Section 4.1.2). The baseline TRAIL judge is a single generic LLM prompt. The 40-point gap is large and likely reflects real decomposition benefits, but the comparison conflates specialized prompts with the decomposition itself. Table 8's meta-judge evaluation partially addresses this, but it uses a different evaluation protocol (meta-judge) and model (Claude-Sonnet-4.5). A cleaner ablation — comparing GPA against equally-engineered per-dimension judges without the full decomposition — would strengthen the causal claim.

- **GEPA experiments use a different model than main experiments**: The GEPA experiments (Section 4.1.5) switch from Claude-4-Sonnet (main experiments) to Claude-Sonnet-4.5. This introduces a confound: GEPA's improvements over manual prompts could partly stem from the stronger base model rather than the optimization method. Running GEPA on the same base model would enable direct comparability.

- **Unsupported claim about Logical Consistency as "strong proxy for success"**: The conclusion (line 306) states "logical consistency serves as a strong proxy for success, reducing dependence on ground-truth references." No experiment in the paper compares LC scores against any measure of task correctness or overall success — only against human annotations of errors. This claim is unsupported and should be removed or softened with a caveat.

- **Internal dataset is too small for strong conclusions**: The production agent evaluation (Section 4.2) uses only 17 traces and evaluates only 2 judges (LC and EE). Results (82% average agreement, Krippendorff's α 0.66/0.81) are suggestive but carry limited weight. The paper frames this as additional validation, but the sample size makes the numbers fragile. A confidence interval or explicit acknowledgment of the pilot nature would be appropriate.

### Trivial
None.

## Nice-to-Haves

- Report inter-annotator agreement (Cohen's κ) for the error-to-GPA mapping.
- Add a controlled decomposition experiment comparing GPA judges against equally-engineered per-dimension judges without architecture descriptions and few-shot examples.
- Discuss cost/latency of running seven judges per trace.
- Expand the internal dataset or reframe it as a pilot case study.
- Run GEPA experiments with the same model used in main experiments for comparability.

## Removed Points

The following points from the inputs were removed with justification:

- **"Section 4.1.2 methodology vague about how disagreements resolved"** — The paper states "a third annotator cross-checked and verified," which is a reasonable resolution process.
- **"Overlap between LC and EE not discussed"** — The paper defines LC as checking grounding in prior context/reasoning and EE as checking global optimality/redundancy. These are distinct concepts; overlap is inherent to any multi-dimensional framework and not a flaw.
- **"Comparison to MAST asserted without empirical demonstration"** — The paper does not claim to compare empirically to MAST; the critique of MAST is conceptual. Demanding empirical comparison is scope creep.
- **"Missing limitations section"** — The paper discusses limitations in the conclusion (variability of LLM judgments, difficulty focusing on small details). A dedicated section would be better but its absence is not a flaw in the science.
- **"No confidence intervals / significance tests for main comparison"** — The main gaps (95% vs 55%) are so large that formal tests would add little value.
- **"False positives analysis missing"** — Tables 3 and 6 report precision = TP/(TP+FP), directly addressing false positives per judge.
- **"Cost and latency not discussed"** — A practical consideration, not a scientific flaw.
- **"Generic strengths about 'important problem'" and similar** — Removed as superficial.
- **"Some strength finder claims about systematic coverage"** — Already covered in Strengths above.
- **"Section-by-section notes about Venn diagram clarity"** — The critique about conceptual overlap is not a concrete weakness.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Clarify the abstract to distinguish between "the taxonomy can categorize all errors" (conceptual) and "the judges detected X% of errors" (empirical).
2. Report Cohen's κ or percentage agreement for the error-to-GPA mapping — this is the single most impactful addition.
3. Remove or substantially soften the claim about LC as a "strong proxy for success."
4. Explicitly acknowledge the model difference in the GEPA section as a limitation, or run the optimization on the same base model.

## Calibration Report

**Round 1 (Bracketing):**
- Weak anchors (<3.5): Papers at 3.0–3.4 (SOP-Agent, ZeroSumEval, etc.) — clearly weaker than GPA, which has substantive empirical results.
- Middle anchors (3.5–7.5): JudgeLM (5.25, Reject), ChatEval (5.60, Accept), Generative Judge (5.33, Accept), RaDAgent (6.25, Reject), Auto-Arena (5.75, Reject).
- Strong anchors (>7.5): Papers at 8.0 (Spider 2.0, MMQA, etc.) — these are large infrastructure/benchmark contributions of a different nature.

**Initial bracket**: 5.0–6.5.

**Round 2 (Narrowing, full reads):**
- JudgeLM (5.25, Reject): GPA is clearly stronger — more comprehensive experiments, direct benchmark comparison with large margins, thorough consistency analysis.
- ChatEval (5.60, Accept): Similar type (LLM-based evaluation framework). GPA's experiments are more comprehensive (detection + localization + consistency + per-judge analysis + GEPA). GPA is slightly stronger.
- RaDAgent (6.25, Reject): More novel technically (internalized utility with Elo), but less comprehensive empirical support. GPA is comparable in quality.
- WebArena (6.33, Accept): Infrastructure/benchmark contribution of larger scale. Different type; GPA is a methodology paper.
- OpenRCA (6.75, Accept): Substantial new benchmark with extensive data. GPA is a methodology paper with narrower scope.

**Placement**: GPA is stronger than the ~5.2–5.6 papers and comparable to but slightly below the ~6.3–6.8 benchmark/infrastructure papers. Score: **6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>