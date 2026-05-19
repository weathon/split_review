- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 6, 5, 3
Now I have a thorough understanding of the paper. Let me compile the final consolidated review.

## Summary

This paper introduces HelloBench, a multi-task benchmark (647 samples across 5 tasks, 38 subcategories) for evaluating long text generation in LLMs, organized via Bloom's Taxonomy. It also proposes HelloEval, a checklist-based evaluation method where human-annotated data is used to fit weighted scores via linear regression, and then LLM-as-a-Judge evaluates checklists to produce an overall score. Experiments across ~30 LLMs yield empirical findings about output length limits, quality degradation, and trade-offs between long-context understanding and generation.

## Strengths

- **Theory-grounded task taxonomy.** The use of Bloom's Taxonomy to systematically map cognitive levels (remember → create) to long-text generation tasks (open-ended QA, summarization, chat, text completion, heuristic text generation) is a principled design choice absent from prior benchmarks (Table 1). This gives the benchmark conceptual structure beyond a bag of tasks.

- **Comprehensive empirical evaluation.** The paper evaluates ~30 LLMs (proprietary, open-source, and capability-enhanced) across all five tasks, reporting per-task scores and word counts (Table 2). The length-constrained experiments (Table 3) and long-context ablation study (Table 4) provide useful empirical maps of current model limitations — e.g., most models cap output at ~2000 words even when configured for much longer generation, and quality degrades sharply under explicit length constraints.

- **Error mode analysis with concrete examples.** The paper identifies four failure patterns (repetition, rejection, perception error in length, meaningless text) with illustrative model outputs (Figure 5). This diagnostic framing goes beyond aggregate scores and gives practitioners actionable targets for improvement.

## Weaknesses

### Fatal

None.

### Major

- **HelloEval validation is critically undersupported.** The only experiment measuring correlation with human evaluation is conducted on a single task (summarization). Furthermore, there is a serious ambiguity in the statistical reporting: based on the model-average scores in Table 4, the Spearman rank correlation between HE and HelloEval at the model level (N=7) is approximately **0.964**, not 0.3193 as reported in Table 5. The reported ρ=0.3193 must therefore be computed at the per-sample level (pooling individual responses). The paper does not state this, does not report the per-sample N, and does not report per-sample correlation alongside model-level correlation. Since the paper's central claim — "HelloEval achieves the highest correlation with human evaluation" — rests on this experiment, the insufficient documentation of the computation granularity and the lack of validation across multiple tasks make the claim significantly weaker than it needs to be. At minimum, the correlation should be reported and discussed at both the per-sample and model-average levels, with confidence intervals.

- **Linear regression fitting is underspecified.** Section 3.2 states that five annotators annotated responses from four LLMs to fit checklist weights via linear regression, but the paper omits: (1) the number of instruction–response pairs annotated, (2) the R² or any goodness-of-fit measure for the regression, (3) inter-annotator agreement (e.g., Krippendorff's alpha), and (4) the fitted weight values themselves. Without these details, the reliability and reproducibility of HelloEval cannot be assessed. The regression is the core mechanism that makes HelloEval "human-aligned," yet its quality is entirely opaque.

- **The "negative correlation" claim between long-context understanding and generation is overstated.** The paper asserts "there exists a negative correlation" based on three model pairs (Yi-1.5-34B vs.-16K, InternLM-2.5-7B vs.-1M, GLM-4-9B vs.-1M) in Table 4. Three data points do not support a correlation claim — they suggest an observed trend at best. The language should be toned to "suggestive evidence" or "observed degradation" rather than implying a general relationship.

### Minor

- **Checklist grading scheme inconsistency.** The checklists are described as "4-6 yes or no questions" for human annotation (Section 3.1), but the LLM-as-a-Judge uses five graded levels (0, 0.25, 0.5, 0.75, 1). It is unclear whether human annotations are binary and LLM evaluations are graded, or whether both use the same scale. This distinction matters because the regression weights are fit from human data, and if the annotation and execution stages use fundamentally different scales, the transfer may break.

- **No confidence intervals or significance tests for main benchmark results.** Model scores in Table 2 are reported as point estimates. Many differences between adjacent models are small (e.g., LLaMA-3.1-8B at 14.48 vs. GLM-4-9B at 13.85). Without error bars (e.g., bootstrap confidence intervals) or pairwise significance tests, readers cannot distinguish signal from sampling noise.

- **Score rescaling to [-300, 100] is under-explained.** The formula $S = (score - 0.75) \times 4$ and the claimed range shift from [0,100] to [-300,100] are inconsistent as written (the formula yields [-3, 1] if score ∈ [0,1], or would need additional scaling if score ∈ [0,100]). The rescaling rationale and mechanics need clarification.

### Trivial

- The "In-The-Wild" descriptor is slightly overstated for the summarization subtask, which draws from existing datasets rather than real user queries (acknowledged but not qualified in the claim).

## Nice-to-Haves

- **Cross-task validation of HelloEval.** Running the same human-correlation analysis on at least one more task (e.g., open-ended QA or chat) would substantially strengthen the evaluation method's credibility.
- **Ablation of weighting vs. equal weighting.** Comparing the regression-weighted HelloEval against simple averaging of checklists — to quantify the value added by the regression — would make the contribution more concrete.
- **Frequency counts for error modes.** The error mode analysis is qualitative; adding per-model frequencies for each error type would make it more diagnostic.

## Removed Points

The following points from the reviewers were removed with justification:

- **"Missing related works on checklist-based evaluation / regression-based weighting"** — Removed per rule: do not mention missing related works without external confirmation.
- **"Dataset and annotation release status"** — Removed per rule: do not question existence/release status of cited items.
- **"Prompt templates are missing"** — Removed per rule: parser strips appendix/figures; these exist in the original submission.
- **"BERTScore, GPTScore missing as baselines"** — Removed per rule: mentioning missing comparison baselines when the existing baseline set is already adequate (10 baselines) is a generic scope-creep weakness.
- **"Could compute at per-sample level"** — The reviewer faulted the paper for not using per-sample correlation, but the paper may already be doing this (as the ρ values suggest); this is an ambiguity to clarify, not a clear omission.
- **Strength: "HelloEval achieves highest correlation"** — Tempered rather than removed; the reported correlation is factually highest among methods compared, but its scope (one task, ambiguous computation level) weakens the strength significantly. Retained in context with the major weakness.
- **Generic strengths about "problem importance" / "addressed an important problem"** — Removed as generic/superficial.

## Novel Insights

A genuinely novel observation emerging from this review is the **granularity mismatch in the Spearman correlation reporting**. Computing Spearman's ρ from the model-average scores in Table 4 yields ρ ≈ 0.964 for HelloEval vs. human evaluation — dramatically higher than the reported ρ = 0.3193. This suggests the paper computed correlation at the per-response level (which is actually more informative and rigorous) but presented the results alongside model-average tables without flagging this difference, inadvertently making the numbers look worse than the data imply. Clarifying this — and reporting both per-sample and per-model correlations — would substantially strengthen rather than weaken the paper's claims. The apparent p-value anomaly (4.67e-7 with ρ=0.3193) is plausibly consistent with a per-sample N ≈ 100-200, not a model-level N=7. The paper is doing more statistical work than it appears, but the presentation obscures it.

## Suggestions

1. **Clarify the Spearman computation granularity.** State explicitly whether the correlation in Table 5 is per-sample or per-model-average, report the N used, and ideally report both levels with confidence intervals.
2. **Add regression diagnostics.** Report the number of annotation pairs, inter-annotator agreement, R², and the fitted weight values (or a table of them) for the linear regression.
3. **Validate HelloEval on at least one more task** (e.g., open-ended QA) to show the method generalizes beyond summarization.
4. **Tone down the long-context vs. generation claim** from "negative correlation" to "observed degradation trend" given only three model pairs.
5. **Add bootstrap confidence intervals to the main results table** so small score differences between models can be properly interpreted.
6. **Resolve the checklist scale inconsistency** — clarify whether human annotations use binary yes/no while LLM evaluation uses graded levels, and explain why this transfer is valid.
