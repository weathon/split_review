## Summary

This paper presents an empirical study of how model size (7B vs. 70B) and training data size (1.4T–18T tokens) affect LLM performance on medical reasoning tasks of varying difficulty. It introduces MedResEval, a benchmark derived from MedQA that creates more demanding tasks by reducing clues, expanding decision spaces, and increasing reasoning steps. The core empirical finding — that small models trained on large data can match old large models on simple tasks but consistently underperform on complex reasoning — is interesting and practically relevant. However, the paper overextends this finding into a quantitative scaling law that is not supported by the data, relies on confounded cross-generation comparisons as headline evidence, and mischaracterizes some subtask results.

## Strengths

- **MedResEval benchmark systematically controls knowledge while varying reasoning complexity.** The benchmark reformulates MedQA along three axes (reducing clues, expanding decision space, increasing reasoning steps) and adds a diagnosis-simulation task with contradiction detection. By keeping the underlying medical knowledge constant across tasks, the design cleanly isolates reasoning difficulty as the variable of interest — unlike prior benchmarks that mix domains. This is a genuine methodological contribution.

- **Semantic-varied task as a control for generalization effects.** The paper constructs a baseline task that replaces medical terms with synonyms. Results in Figure 5 show that 70B models maintain nearly identical performance on this task (60.1% vs. 61.0% on original MedQA), confirming that performance drops on complex tasks are attributable to reasoning demands rather than surface-form variation.

- **Instruction-tuning analysis shows the parameter-scaling gap persists after post-training.** Table 2 compares base and instruction-tuned Qwen models; the performance gap between 7B and 72B on complex tasks widens after instruction tuning (e.g., from 24.5% to 27.9% for Qwen2.5). This provides convergent evidence that model size, not just training protocol, is the dominant factor for complex reasoning.

## Weaknesses

### Major

- **The difficulty-dependent scaling law (Eq. 3) is not supported by the data presented.** Each fitted curve in Table 1 is derived from at most 3–6 data points per model-size/difficulty combination (Llama: 1.4T, 2T, 15T; Qwen: 3T, 7T, 18T) against a three-parameter power law. This yields minimal degrees of freedom; high R² values are essentially guaranteed and carry no evidence of predictive validity. The extrapolations to 54T and 157T tokens in Section 5.1, and the derived "1.3×" and "2×" error reduction ratios, are unsupported speculation. The qualitative observation that larger models benefit more from additional data on complex tasks is well-supported; the quantitative scaling law formula is not. This needs to be downgraded to a descriptive observation, with the ratios and extrapolations removed or heavily qualified.

- **Cross-generation comparisons conflate architecture and data quality with size and data quantity.** The headline comparison (e.g., Llama 3 8B vs. Llama 1 65B) attributes performance differences entirely to parameter count and data size, but these models differ in architecture (Grouped-Query Attention, training objectives, data composition, tokenizer), training data quality, and other factors. The within-generation comparisons (e.g., Llama 3 8B vs. Llama 3 70B, both on 15T tokens) are cleaner and do support the thesis. The paper gives prominent weight to the confounded cross-generation comparisons in the abstract and conclusion while under-using the cleaner within-generation evidence.

### Minor

- **The Expanding Decision Space subtask shows anomalous results mischaracterized in the text.** For 7B Llama models, normalized performance drops from 4.9% (2T) to 1.9% (15T). The paper describes this as "only a 5% improvement for 7B models" — the actual change is negative. While a group-averaged analysis (combining 1.4T and 2T as a "less" group) might produce a small positive shift, the per-model data needed to verify this is not shown. This subtask is one of three defining "Complex Tasks," and its behavior conflicts with the narrative that more data helps 7B models even modestly on complex tasks. The paper should either explain or acknowledge this counterexample.

- **The claim that "current LLMs have mastered the semantic representations of medical concepts quite well" is overstated.** Llama 3 8B scores 21.9% on the semantic-varied task vs. 36.9% on original MedQA — a 15-point gap. The claim holds better for 70B models (60.1% vs. 61.0%) but not for smaller ones. The qualitative claim needs qualification by model scale.

- **The instruction-tuning analysis is limited to a single model family (Qwen).** Only Qwen2 and Qwen2.5 instruction-tuned models are evaluated. Including an additional family (e.g., Llama-3-Instruct) would strengthen confidence that the observed pattern is general rather than family-specific.

### Trivial

- Typo: "~54.TT tokens" (Section 5.1) should read "~54T tokens."
- No error bars or statistical significance tests are reported. Given the modest number of test samples per subtask, some comparisons could be noise.
- The paper lacks a dedicated limitations section acknowledging the confounds discussed above.

## Nice-to-Haves

- Report per-subtask results for all models (not just Llama) with variance estimates (e.g., multiple seeds for unanswerable question generation). Include inter-annotator agreement statistics for the diagnosis-simulation contradiction annotations.
- Provide confidence intervals on scaling law parameters via bootstrapping, if the fit is retained in any form.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Criticism about missing appendix details (dataset statistics, prompt formats, CoT examples):** Removed per instructions — the parser strips appendices; these details exist in the original submission.
- **Concern that the semantic-varied task should not be grouped as "simple":** Removed — the task shows the same trend pattern as original MedQA (both improve with data/model scale), so the grouping is justified. The retained weakness about the "mastered" overclaim captures the substantive concern.
- **Strength about the scaling law fit having high R² values:** Removed — the high R² is an artifact of fitting 3 parameters to ~3–6 data points and conflicts with the verified weakness about the scaling law being unsupported.
- **Strength about the 157T extrapolation being "concrete evidence":** Removed — this derives from the weak scaling law fit and conflicts with the verified weakness.
- **Criticism about the diagnosis-simulation plateau being "only speculation":** Removed — the paper does acknowledge this as an open question ("may be attributed to differences in training data distribution"), which is appropriate for a case study.
- **Concern about missing "Limitations" section:** Merged into trivial weaknesses as a minor presentation gap.

## Novel Insights

None beyond the paper's own contributions. The observation that the data-scaling vs. model-scaling benefit ratio flips with task complexity, while not entirely unprecedented, is the paper's most useful empirical contribution.

## Suggestions

1. **Restructure around within-generation comparisons.** Let the primary narrative be: "Llama 3 8B vs. 70B (both 15T) and Qwen2.5 7B vs. 72B (both 18T)." Present cross-generation comparisons as supplementary motivation with explicit caveats about architectural and data-quality confounds.

2. **Downgrade the scaling law to a qualitative observation.** Drop the 54T/157T extrapolations, the 1.3×/2× ratios, and any predictive claims. Keep only the fitted exponent pattern (α is smaller for 7B than 70B on complex tasks), which is consistent with the core empirical finding without overclaiming precision.

3. **Address the Expanding Decision Space anomaly directly.** Investigate and report why 7B models degrade with more data. If artifacts from unanswerable-question generation are responsible, explain them. If not, acknowledge the counterexample and discuss its implications.

4. **Add a brief limitations section** covering: (a) confounds in cross-generation comparisons, (b) limited data for scaling law fitting, (c) single-family scope of instruction-tuning analysis, (d) absence of statistical significance tests.

## Score and Decision

**Calibration report:**

Round 1 bracketing: I placed the paper between 4.0 and 6.0 by examining three bands of similar-topic papers.

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| ClinicalBench (medical LLM benchmark) | 5.5 | R1 | Stronger empirical scope but the paper under review has more novel task design |
| Sub-Scaling Law (scaling study) | 4.5 | R1 | Similar limitations in scaling law fitting, current paper has cleaner core finding |
| Small-to-Large Generalization | 5.25 | R1 | Cleaner methodology than current paper, accepted as poster |
| Sloth (scaling for skills) | 4.25 | R1 | Comparable type of overclaim, current paper has better benchmark contribution |
| Language models scale reliably (over-training) | 6.5 | R1 | Significantly more rigorous — current paper is weaker |
| ClinicalLab (medical benchmark) | 4.2 | R2 | Weaker than current paper |
| MedFuzz (medical QA robustness) | 4.25 | R2 | Comparable rejected paper, current paper slightly stronger |
| Scaling Math Reasoning | 5.25 | R2 | Similar profile: interesting empirical findings with methodological limitations |
| Revisiting Superficial Alignment | 5.75 | R2 | Cleaner methodology, similar topic — current paper is weaker |
| 3-SAT Reasoning | 5.25 | R2 | Similar score range — both rejected with interesting but limited evidence |

The paper shares characteristics with rejected papers scoring 4.25–5.75. Its strongest comparable is the Scaling Math Reasoning paper (5.25, Reject), which had similar methodological issues (confounded comparisons across model families, limited task scope) but also a genuine empirical contribution. The current paper's MedResEval benchmark is more novel, but the scaling law overclaim and confounded comparisons are more severe weaknesses. The paper is clearly weaker than the "Language models scale reliably" (6.5, Accept Poster) anchor, which had far more rigorous methodology (104 models, clear validation).

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>