Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper investigates whether open-source LLMs can be made competitive with closed models (GPT-4) on software tool manipulation tasks using a practical amount of human supervision. The authors identify three failure modes of open-source LLMs (API selection, argument population, non-executable generation) and adapt three well-known techniques—model alignment via programmatic data generation, an in-context demonstration retriever, and a system prompt—to address them. They introduce SNACT, a benchmark of 8 diverse tools with predefined test cases, and show that the proposed recipe boosts open-source LLMs by up to 90% success rate, achieving competitive or better performance than GPT-4 on 4 of 8 tasks.

## Strengths

1. **Systematic diagnosis of open-source LLM failure modes in tool manipulation.** The paper identifies and quantitatively characterizes three distinct failure types—API selection, argument populating, and non-executable generation—providing breakdowns across models (e.g., Table 2 shows argument populating causes 32% of LLaMA failures and 63% of CodeGen failures). This taxonomy is actionable and directly motivates the three proposed techniques.

2. **Programmatic data generation for model alignment reduces required human effort to O(n) templates.** The core idea of writing a few dozen templates with placeholders and bootstrapping training data via random instantiation is practical and well-demonstrated. The paper shows that fewer than 100 templates per tool suffice (O(n) where n is the number of APIs), and ablation studies confirm model alignment is the most impactful technique, degrading up to 7 of 8 tasks when removed.

3. **Evidence that a small pool of demonstrations (O(n)) generalizes to unseen API combinations.** The home search task with 15 API functions is a convincing case study: with only 10 human-curated demonstrations that do not match any test case's API combination, the retriever boosts success rates by up to 79% across open-source models. This strongly supports the claim that the approach requires only modest human effort.

4. **Introduction of SNACT, a benchmark with pre-defined test cases for reproducible quantitative evaluation.** While prior tool-augmented LLM benchmarks (Li et al. 2023, Qin et al. 2023) focused on closed-model evaluation without standardized test cases, SNACT provides ground-truth test cases across 8 diverse tools spanning single-step and multi-step scenarios. The API complexity score is a useful auxiliary contribution for quantifying task difficulty.

5. **Insight that GPT-4 internalizes API usage knowledge during training.** Figure 2 shows GPT-4 can select correct APIs without documentation or examples, whereas open-source models fail. This observation provides a clear empirical rationale for why model alignment with API usage examples is necessary for open-source models.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Missing variance reporting on main results prevents assessing the reliability of the "competitive" claim.** The paper reports averages over 3 runs (line 343) but does not report standard deviations, confidence intervals, or any measure of variance for the headline results in the main tables (Tables 2, 3). While the observed improvements are large (up to 90%), the claim that open-source models become "competitive or better" than GPT-4 on 4 of 8 tasks would be substantially strengthened by showing error bars or explicitly defining thresholds (e.g., within 5% absolute). The paper's own text acknowledges that low-success-rate tasks are "hypothetically subject to high variance and fluctuation" (line 394), which underscores the need for variance reporting across all results.

2. **The "one developer day" supervision claim is reported as an observation rather than a measured quantity.** The paper states "we find it takes on average one day for one developer to curate the data" (line 234) and "We observe that providing these supervisions takes one developer day on average" (line 359). However, no information is provided about who performed the curation, their expertise level, the measurement methodology, or variance across tools. This is the paper's central evidence for "practical" supervision, and an anecdotal observation is weaker than the claim warrants. The paper would be stronger if it either reported this as a rough qualitative estimate or conducted a minimal measurement (e.g., two developers independently curating data for one tool and reporting time + agreement).

3. **The demonstration retriever's embedding model and similarity metric are not specified.** The paper states the retriever "selects demonstration examples with the most semantically similar goals" (Section 3.2, line 243) but does not specify which embedding model or distance function is used. The API document retriever is described as using BM25 (line 110), but the demonstration retriever appears to use a different semantic similarity mechanism that is left unspecified. This is a concrete reproducibility gap for a component that directly affects the results.

4. **The "first open-source benchmark" claim is qualified but could invite unnecessary debate.** The paper carefully qualifies this claim with "among the ones brought up in the recent tool-augmented LLM literature" and specifically contrasts with the cited works (li2023api, qin2023tool). While this is a defensible qualified claim, phrasing it more modestly (e.g., "to the best of our knowledge, the first open-source benchmark among those in the recent tool-augmented LLM literature with predefined test cases") would avoid distracting discussions. This is a minor presentational issue.

### Trivial

- The ablation study in the main text (Table 7) reports only the count of tasks improved/hurt rather than the magnitude of changes. While the full results are referenced in the appendix (Table "baselines_over_techniques"), the count-based summary alone is weak evidence for the contribution of each technique in the main text.

- The paper compares tuned open-source LLMs with untuned GPT-4 (since GPT-4 tuning APIs are unavailable). This asymmetry is acknowledged in a footnote (line 57) but could be made more explicit in the main narrative framing.

## Nice-to-Haves

- A per-task breakdown of which failure modes persist after enhancement on the 4 tasks where open-source models are not competitive would provide actionable insight for future work.
- A small-scale inter-annotator study (e.g., two developers independently creating templates for one tool) to add rigor to the "one developer day" claim.
- A brief error analysis on the 4 tasks where open-source models still lag behind GPT-4, quantifying how much of the gap is attributable to each of the three failure modes.

## Removed Points

These points were flagged by the reviewers but are removed after verification against the paper:

- **"Comparison asymmetry is not discussed":** The paper explicitly acknowledges this in a footnote (line 57: "Model alignment is not applicable to GPT-4 as there is no publicly available tuning APIs for it during our experiments"), so the reviewer missed this discussion.
- **"The novelty claim about the benchmark may be overstated":** The paper carefully qualifies its "first" claim with "among the ones brought up in the recent tool-augmented LLM literature" and specifically contrasts with the benchmarks it cites (li2023api, qin2023tool). The reviewer's concern about hypothetical prior benchmarks like ToolBench is already addressed — ToolBench (qin2023tool) is cited and is the very benchmark the paper contrasts against.
- **Strength Finder's "Cost and effort analysis validates practicality":** This conflates the anecdotal "one day" claim (which is a genuine weakness) with a validated finding. Since the weakness is verified, this strength claim conflicts and is removed.
- **Generic/misaligned strength claims:** None remaining in Strength Finder output after filtering.
- **Weaknesses about missing appendix content:** References to appendix tables (baselines_over_techniques, training_data, app_exp_details) are standard — the parser strips appendix sections from all papers.

## Novel Insights

The meta-review reveals that the reviewers broadly agree the paper's core empirical contribution is solid and well-executed, but disagree on how much weight to assign to the paper's softer claims (the "one developer day" estimate and the "competitive" framing). The most interesting tension is between the paper's candid reporting of an approximate human-effort estimate — which is standard practice in systems papers — and the harsh critic's expectation of a controlled user study. This reflects an unresolved methodological question in the LLM-plus-human-supervision literature: when a paper claims a technique is "practical," what level of evidence is sufficient? The paper's template-count evidence (O(n), <100 templates per tool) is arguably the more important and falsifiable claim than the exact time estimate, and the review would benefit from recognizing that distinction.

## Suggestions

1. Add standard deviations or confidence intervals (e.g., from the 3 runs already conducted) to all main-result tables.
2. Specify the embedding model and similarity metric used for demonstration retrieval, or replace the "semantic similarity" description with the actual mechanism (e.g., if BM25 is also used for demonstrations, state this clearly).
3. Reframe the "one developer day" claim as a qualitative observation rather than a measured result, or conduct a minimal measurement (even n=1 or n=2 developers on one tool) to add credibility.
4. Consider adding a per-task failure-mode analysis for the 4 tasks where open-source models still underperform GPT-4.

## Score and Decision

**Originality:** The paper's main novelty lies in the empirical demonstration that combining three known techniques with modest human effort bridges the gap to closed models on tool manipulation — the individual techniques are not novel, but the recipe and the diagnosis of failure modes are. This is a solid empirical contribution rather than a methodological breakthrough. **Importance of research question:** High — enabling open-source LLMs for tool manipulation has clear practical implications for industrial adoption of LLMs without exposing sensitive data. **Claims supported:** Mostly well-supported for the core results, but the "competitive" claim and the "one developer day" supervision claim need tighter grounding. **Soundness:** The experimental design is reasonable, with runs over 3 seeds, diverse models and tasks, and ablation studies. The main gap is missing variance reporting. **Clarity:** Generally well-written and well-structured. **Value to community:** High — the benchmark (SNACT) and the practical recipe are likely to be useful for practitioners and future researchers.

The paper makes a useful and well-executed empirical contribution. The weaknesses identified (missing variance, soft supervision claim, unspecified retriever details) are real but minor — they do not undermine the paper's central findings. The improvements are large enough that the core conclusions are robust despite these issues.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>