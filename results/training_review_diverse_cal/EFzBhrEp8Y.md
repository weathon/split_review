## Summary

MME-Finance is a bilingual (English + Chinese) multimodal VQA benchmark for the financial domain, comprising 1,171 English and 1,103 Chinese questions across 11 tasks organized into perception, reasoning, and cognition ability levels. The benchmark covers diverse financial image types (candlestick charts, technical indicator charts, tables, documents, etc.) and image styles (screenshots, mobile photographs). The paper also proposes an LLM-based evaluation method that incorporates visual information and validates it against human judges. Experiments on 19 MLLMs reveal that even the best models (Qwen2VL-72B at 65.69%, GPT-4o at 63.18%) perform poorly on financially specialized tasks like candlestick chart interpretation.

## Strengths

- **First multimodal benchmark for the financial domain, with rigorous expert annotation**: The paper correctly identifies and fills a genuine gap — there is no established multimodal benchmark for finance. Each QA pair undergoes at least two stages of manual review, and complex subjective questions are evaluated by a panel of finance researchers with 10+ years of industry experience (Section 3.3). This expert-driven quality control is a clear strength.

- **Evaluation method validated against human judges**: The paper designs task-specific evaluation prompts with few-shot examples and empirically demonstrates that incorporating visual information improves evaluator consistency with human scores (Spearman 0.720→0.738 for GPT-4o, Table 4). The ablation on subjective vs. objective questions (Table 5) further supports the value of image input. The validation pipeline (three expert annotators per sample, mode/mean aggregation, variance-based re-review) is thoughtfully designed.

- **Evaluation of 19 MLLMs yields concrete, actionable insights**: The experiments go beyond a simple leaderboard by analyzing performance across tasks (Table 2), image types, and image styles (Table 3). Key findings — such as uniformly poor performance on candlestick charts (<60% for all models), severe difficulty with spatial awareness (best model at 30.31%), and degradation on mobile photographs — provide specific guidance for improving financial MLLMs.

## Weaknesses

### Fatal
None.

### Major

1. **Bilingual benchmark claim is unsupported by evaluation results.** The paper prominently advertises MME-Finance as a bilingual benchmark (abstract, introduction, contributions list), stating it comprises 1,171 English and 1,103 Chinese questions. Yet all experimental results (Tables 1, 2, 3, and all analysis in Sections 4.2–4.3) are explicitly labeled and reported on *English MME-Finance only*. No Chinese results appear in the main paper, and there is no explanation for their absence — not even a pointer to an appendix or a statement that they are forthcoming. This is not a minor omission: the bilingual nature is a headline contribution. A reader evaluating the paper must ask whether the Chinese questions have been validated, whether model behaviors differ in a Chinese context (as the abstract suggests they might), and whether the benchmark functions comparably in both languages. The gap between the claimed scope and the presented evidence is substantial. The authors should either (a) include Chinese evaluation results, at minimum a summary table, or (b) clearly state why they are omitted and appropriately qualify the bilingual claim. *(Verified: Table 2 caption reads "Evaluation results on English MME-Finance"; Section 4.2 opening sentence references "English MME-Finance." No Chinese results exist in the paper.)*

### Minor

2. **Several tasks have very small sample sizes without uncertainty quantification.** Table 1 shows Risk Warning (22), Reason Explanation (18), Investment Advice (53), Estimated Numerical Calculation (42), and Not Applicable (22) all have fewer than ~50 samples. The paper makes comparative claims based on these small-n tasks — e.g., "Qwen2VL-72B and GPT-4o demonstrate a strong ability to discern whether a question is answerable" based on 22 NA samples, or rankings of models on the 18-sample Reason Explanation task. With n=18 or n=22, a single outlier question can shift rankings substantially. No confidence intervals, bootstrap estimates, or standard errors are reported. The paper does acknowledge variable sample sizes (Section 3.4) but does not caveat the conclusions drawn from the smallest tasks. Aggregating very small tasks into broader categories or reporting uncertainty would substantially improve rigor.

3. **Potential evaluator conflict of interest is not discussed.** GPT-4o serves as the primary evaluator (with image input) and is also one of the evaluated models. The paper does not address the possibility that the evaluator might systematically favor its own outputs. While the fact that Qwen2VL-72B outscored GPT-4o overall (65.69 vs. 63.18) mitigates concerns about rank-level bias, per-task bias could still exist — GPT-4o does lead in cognition tasks, where the evaluator's own reasoning style might be preferred. The human-consistency experiment (Section 4.3) uses MiniCPM2.6 outputs only and therefore does not test for evaluator bias toward GPT-4o. A short analysis comparing how the GPT-4o evaluator scores GPT-4o responses vs. other models' responses on a per-task basis would address this.

4. **The "first introduces visual information" claim is overframed.** The paper claims its evaluation method "first introduced in the multi-modal evaluation process" by incorporating visual information. While the paper provides useful empirical evidence that adding images improves evaluator consistency (Tables 4, 5), claiming priority ("first") is unnecessary and invites debate. The substantive contribution — showing that visual information improves LLM-as-judge evaluation for financial VQA, backed by human validation — stands on its own without this framing.

### Trivial

5. **The human consistency experiment (Section 4.3) samples 100 outputs from a single model (MiniCPM2.6).** The paper should clarify whether these 100 samples were randomly selected across all tasks or disproportionately drawn from certain tasks. If not representative, the correlation numbers may not generalize uniformly.

## Nice-to-Haves

- **Additional proprietary models (Claude, Gemini)** would strengthen the breadth of the evaluation, though the current set is defensible for a benchmark paper.
- **A structured error taxonomy** for the hardest tasks (spatial awareness, estimated numerical calculation) beyond the two qualitative examples would increase the diagnostic value of the benchmark.
- **A comparison of leaderboard scores** using GPT-4o evaluator with vs. without image input on the full benchmark (currently only reported for the 100-sample subset in Table 4) would clarify how much the visual input matters for overall rankings.

## Removed Points

These points were flagged by reviewers but are not included in the main assessment:

- **"Limited proprietary models" as a weakness**: The paper evaluates GPT-4o and GPT-4o-mini. Choosing a specific set of proprietary models is the authors' prerogative; demanding Claude and Gemini is scope creep. Moved to Nice-to-Haves.
- **"Only 1,171 English questions is modest"**: The paper acknowledges plans to expand. The current size is adequate for a specialized domain benchmark; further expansion would be a future contribution, not a present flaw.
- **"The paper should add an error taxonomy"**: This is a suggestion for a different kind of paper. The paper provides illustrative examples, which is appropriate for a benchmark paper.
- **Generic strengths from Strength Finder**: Some claimed strengths (e.g., "this paper addressed an important problem") are generic and lack specific evidence; these have been omitted in favor of concrete, citation-grounded strengths.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the expected tension between a benchmark paper's dataset contribution (which is real and bilingual) and its empirical evaluation scope (which is English-only). The most novel insight from the review process is that the bilingual gap is structural enough to weaken acceptance despite the dataset's genuine value — reviewers would likely converge on requiring Chinese results before accepting the bilingual claim at face value.

## Suggestions

1. **Include Chinese evaluation results.** Even a single summary table showing the same 19 models on the Chinese MME-Finance subset (and optionally a comparison with English results) would transform the paper. If the Chinese subset has not been evaluated, state this clearly and qualify the "bilingual benchmark" claim as referring to the dataset resource rather than the empirical findings.

2. **Add a brief evaluator-fairness analysis.** Compare the scores GPT-4o (as evaluator) assigns to GPT-4o's own responses vs. Qwen2VL-72B's responses on a per-task basis, or use a non-evaluated model (e.g., GPT-4o-mini) as an alternate judge to check for systematic bias.

3. **Report uncertainty for small-n tasks.** Add bootstrap confidence intervals or at minimum note the sample size in the discussion of each small task's results, with a caveat that rankings on tasks with n<50 are tentative.

4. **Clarify the human evaluation sampling procedure.** State whether the 100 samples were randomly selected across all tasks and, if not, describe the stratification.

5. **Tone down the "first" claim** regarding visual information in evaluation, or support it with a concrete citation showing that no prior work has done this.

## Score and Decision

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>