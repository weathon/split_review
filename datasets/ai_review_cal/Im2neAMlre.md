- Decision: Accept
- Avg Score: 7.33
- Scores: 6, 8, 8
Now I have all the information needed. Let me synthesize the final review.

## Summary

This paper introduces the Gecko evaluation suite — a curated 2K prompt set (Gecko2K) covering 12 skills and 26 sub-skills, with >100K human annotations across four templates (Likert, Word Level, DSG(H), and side-by-side) for four T2I models. The paper demonstrates that evaluation conclusions (model rankings, metric rankings) change depending on the "slice" of evaluation (prompt set, annotation template, evaluation task), establishing that single-slice evaluation yields unstable conclusions. It also proposes an improved QA/VQA metric (Gecko metric) with three modifications — coverage-guided QA generation, NLI-based hallucination filtering, and VQA score normalization — and shows it consistently outperforms prior interpretable metrics across templates and tasks.

## Strengths

- **Empirical demonstration that evaluation conclusions change across slices**: Figure 2 directly shows that the relative ordering of T2I models (SD1.5, SDXL, Muse, Imagen) differs depending on the human annotation template (Likert, WL, DSG(H), SxS) and the prompt set (Gecko(R) vs Gecko(S)). This validates the paper's central claim that "one slice is not enough."

- **Largest multi-template human-annotation benchmark in T2I alignment**: Table 1 shows Gecko2K far exceeds prior benchmarks (TIFA, DSG1K, HEIM, etc.) in annotation volume (>100K annotations), sub-skill coverage (26), and most importantly, is the only dataset collecting ratings across four distinct human annotation templates.

- **Gecko metric shows consistent improvement over interpretable baselines**: Component ablations (Table 5) validate that each of the three proposed improvements (coverage, NLI filtering, score normalization) individually raises correlation with human judgment. The paper reports the Gecko metric performs consistently best across all three evaluation tasks (model ordering, pair-wise instance scoring, point-wise instance scoring) and on the held-out TIFA160 benchmark.

- **Statistically principled model ordering methodology**: The paper introduces Wilcoxon signed-rank testing (p<0.001) for model comparisons, moving beyond simple mean-comparison practices. This reveals that conclusions based on averages alone can be misleading (e.g., SDXL and Muse are not significantly different on Gecko(R) despite average ratings suggesting otherwise).

- **Systematic prompt generation with fine-grained sub-skill coverage**: Section 3.2 details a controlled, LLM-based prompt generation methodology with manual validation, producing a prompt set with better sub-skill coverage than prior datasets. The paper's decomposition into 12 skills and 26 sub-skills (e.g., text rendering divided into English vs Gibberish, short vs long text) enables diagnostic evaluation.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims are well-supported by the empirical evidence available in the main text.

### Minor

- **NLI filtering threshold (0.005) is set by manual inspection without sensitivity analysis**: The paper determines the threshold by examining QA pairs with NLI scores below 0.05 and observing that those below 0.005 are "typically hallucinations" (Sec. 6.1). No sweep over threshold values is provided to show that performance is robust to this choice. While the threshold likely has limited impact (the component ablation in Table 5 validates that NLI filtering broadly helps), the absence of sensitivity analysis weakens the methodological rigor.

- **The coverage-step quality is not evaluated**: The Gecko metric's first improvement involves prompting an LLM to identify "visually groundable words" in the prompt. The paper does not evaluate how accurately the LLM performs this decomposition (e.g., precision/recall against human annotation). This matters because errors at this step propagate to the QA generation stage.

- **The "reliable prompts" analysis has acknowledged circularity**: Selecting prompts by inter-rater agreement and then showing that templates agree more on this subset is partially circular. The paper validates on the held-out SxS template (not used in selection), showing α increases from 0.49 to 0.54 on Gecko(S). However, the claim that this subset demonstrates that certain prompt sets are inherently "more discriminative" is weakened by the selection procedure itself. The paper does acknowledge this trade-off ("at the expense of removing some potentially meaningful prompts"), which is commendable, but the interpretability of the analysis remains limited.

- **The 40.5%/22% improvement claims lack context**: The abstract states the Gecko metric "performs on average 40.5%/22% better than interpretable baselines on our dataset in terms of pair-wise/point-wise instance scoring respectively." The paper does not specify whether these are absolute or relative improvements. Since Spearman/Pearson correlations are bounded between -1 and 1, a 40.5% *relative* improvement from a small base could be modest in absolute terms. This should be clarified.

- **No statistical significance testing for metric correlation comparisons**: The paper reports correlation values (Spearman, Pearson) for metrics but does not report confidence intervals or test whether the differences between Gecko and the next best metric are statistically significant. Given the paper's own emphasis on significance testing for human evaluations (Wilcoxon test for model ordering), the same rigor should apply to metric comparisons.

### Trivial

- None of note.

## Nice-to-Haves

- **Sensitivity analysis for the NLI threshold**: A sweep over threshold values (e.g., 0.001–0.1) on Gecko2K and TIFA160 would show the chosen threshold is not cherry-picked.
- **Ablation controlling for question count**: The coverage step likely generates more QA pairs per prompt. An ablation that samples the same number of QA pairs from the Gecko and TIFA methods would isolate the effect of coverage coverage from question quantity.
- **Comparison with TIFA's original questions**: Applying the same coverage/NLI/normalization improvements on top of TIFA's original question set would isolate the effect of question generation from the effect of filtering and scoring.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Model ordering results for metrics are underspecified in the main text"** — REMOVED. The model ordering task results for metrics are described as presented in App. F.1 (Sec. 6). Per instructions: the parser strips appendix sections from all papers; these exist in the original submission. The main text states the claim clearly ("Gecko metric consistently performs best for Gecko(S)/(R) across tasks and on TIFA160") and points to the appendix for full tables.

- **"Interpretability is not a new contribution"** — REMOVED. The paper describes the metric as "interpretable" (alongside "reference-free" and "modular") as a property of the QA/VQA approach, not as a novel claim. It does not claim interpretability as a new contribution.

- **"Reproducibility with proprietary models"** — REMOVED. The paper uses the same backend models (PaLM-2, PaLI) for all compared metrics for a fair comparison, and also explores a Gemini Flash variant. Using state-of-the-art models that happen to be proprietary is standard practice in the field, and the paper provides complete generation prompts and methodology.

- **"Missing apples-to-apples comparison with TIFA's original questions"** — MOVED to Nice-to-Haves. This is a useful additional experiment, not a missing essential comparison.

- **"The paper does not report how many prompts were manually validated or the rejection rate"** — REMOVED. This is a minor implementation detail that does not affect the validity of the benchmark construction.

- Several generic "Strengthening the Paper on Its Own Terms" points — MOVED to Nice-to-Haves where they are actionable and specific; otherwise REMOVED.

## Novel Insights

None beyond the paper's own contributions. The key novel findings — that model rankings shift across annotation templates, prompt sets, and evaluation tasks, and that a comprehensive multi-slice evaluation is necessary for stable conclusions — are the paper's own primary contributions, not observations synthesized from the reviews.

## Suggestions

1. Clarify whether the 40.5%/22%/10.5% improvement figures are absolute or relative improvements, and provide baseline correlation values for context.
2. Add a sensitivity analysis for the NLI filtering threshold (sweep over 0.001–0.1) on both Gecko2K and TIFA160 to demonstrate robustness.
3. Evaluate the accuracy of the LLM coverage step (groundable word identification) by comparing against human annotation on a sample of prompts.
4. Add confidence intervals or significance tests for the metric correlation comparisons to match the rigor applied to the human evaluation analysis.
