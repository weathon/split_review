Now I have all the evidence needed. Here is the final consolidated review.

---

## Summary

TC-Bench is a benchmark (150 T2V prompts, 120 I2V pairs) targeting temporal compositionality in video generation — a genuinely under-addressed aspect of video evaluation. It formalizes three scenarios (attribute transition, object relation change, background shift) via scene-graph transitions and proposes VLM-based metrics (TCR and TC-Score). An evaluation of 14 T2V and 2 I2V models shows that even the best proprietary system (Gen-3 Alpha) achieves only ~22% TCR, confirming that temporal compositionality remains a hard, open problem.

## Strengths

1. **Principled formalization of temporal compositionality.** The paper defines a clean scene-graph formalism ($s_0 \Rightarrow s_T$) covering attribute transitions, object relation changes, and background shifts (Section 3.1). This moves beyond existing benchmarks that test static compositions or simple motions, and provides a structured taxonomy for future work.

2. **Novel VLM-based metrics with significantly higher human correlation than existing metrics.** The proposed TCR (transition completion ratio) and TC-Score (average pass rate across assertions) achieve substantially better rank correlation with human judgments than prior metrics (CLIP, ViCLIP, UMTScore, EvalCrafter). Table 3 shows the proposed metrics dominate across all comparisons — a result that holds despite the moderateness of human-human agreement, which actually makes the gap *more* impressive, not less.

3. **Revealing empirical results that establish a clear frontier.** The comprehensive evaluation quantifies that *all* current models fail on most TC-Bench prompts (overall TCR: Gen-3 Alpha at 22.00%, Dream Machine at 14.00%, open-source models mostly below 12%). This provides a concrete, measurable challenge for the community and a diagnostic tool for model improvement.

4. **Insightful analysis of failure modes.** Figure 5's temporal attribute similarity curves show that T2V models fail to decrease the initial attribute or increase the final attribute over time (flat CLIP similarity curves), while I2V models exhibit sharp consistency drops between conditional frames and their neighbors. This goes beyond aggregate scores and gives model developers actionable diagnostic evidence.

## Weaknesses

### Fatal
None.

### Major
None. The weaknesses listed below are real but addressable; none invalidate the core contribution.

### Minor

1. **Human evaluation is underdescribed, limiting assessment of metric validation.** The paper mentions "5-point Likert scale" and "two different annotators" (Table 3 caption) but does not specify: (a) how many videos were rated by each annotator and whether all or only a subset was double-annotated, (b) the exact Likert scale anchors (e.g., what 1 vs. 5 means for temporal compositionality), and (c) whether the same videos were used for T2V and I2V human evaluations. The inter-annotator correlation (Kendall 0.49 T2V, 0.32 I2V) is moderate — the paper claims ratings are "consistent across individuals" without discussing this limitation or comparing it to typical agreement in similar video evaluation tasks. The metrics' correlation with human judgments is the central validation claim; the reader needs enough detail to assess the quality of that gold standard.

2. **The I2V TC-Score (Eq. 4) is defined with unspecified weighting factors and a broken reference.** Line 134 introduces $w_1$ and $w_2$ as "weighting factors" with a parenthetical "As shown in Fig.2)," but Fig. 2 is about scene-graph categories — it does not specify these weights. Without stating the values (or at least the range) used in the experiments, the I2V metric definition is incomplete and irreproducible.

3. **VLM evaluation protocol lacks full reproducibility specifications.** The paper uses GPT-4 Turbo for assertion verification, CogVLM2-19B, and LLaVA-NeXT-7B, but does not fix the GPT-4 Turbo version/date, temperature, exact system prompt, or the complete set of in-context exemplars that produced the reported assertions. While the promise to release pre-generated assertions (Section 8) partially mitigates this, the evaluation pipeline itself cannot be independently re-run by third parties. This is a practical limitation for a benchmark intended to track progress over time, especially since proprietary API behavior can drift.

4. **Results for open-weight VLMs are missing from Table 3.** The paper states it adopts three VLMs (GPT-4 Turbo, CogVLM2-19B, LLaVA-NeXT-7B) to assess assertions, but Table 3 appears to report human correlation only for GPT-4 Turbo. Reporting the rank correlations for the open-weight models would clarify whether the metric's validity depends on the specific VLM choice, or transfers across VLMs.

5. **No confidence intervals or significance tests for the main results.** The TCR scores in Tables 1–2 are point estimates on ~50 prompts per category. The paper does not report standard errors, confidence intervals, or any statistical significance assessment. This would help readers assess how much weight to place on differences between models.

6. **Conditions for running proprietary models are not described.** The evaluation includes Kling, Gen-3 Alpha, and Dream Machine, but does not state whether fixed seeds were used, whether prompts were fed verbatim, or how generation parameters were selected. This is a known challenge when evaluating closed-source systems, but it should be explicitly acknowledged.

### Trivial

- The reference "As shown in Fig.2)" at Eq. 4 (line 134) has an extra closing parenthesis and points to the wrong figure.

## Nice-to-Haves

- A failure-mode analysis of VLM assertion verification (e.g., examples where the VLM incorrectly accepts or rejects a correct transition) would help users understand the noise floor of the metric.
- Reporting the distribution of specific attributes (color vs. shape vs. texture changes), objects, and actions in the prompt set would help users understand the benchmark's coverage.
- The concatenated-frame input strategy (Section 4.1) is justified with a single sentence; a brief ablation comparing concatenated vs. sequential frame input would strengthen the design choice.

## Removed Points

These points are flagged for removal; treat them with caution.

1. **"Low inter-annotator reliability undermines the metric validation."** — Removed because the reviewer overstates the severity. Kendall 0.49 (T2V) is moderate agreement, not "low," and is common in subjective video evaluation tasks. If the proposed metrics achieve Spearman ~0.68 with human judgments while human-human agreement is lower (e.g., Spearman ~0.58), that is consistent with the metrics capturing the shared signal near the theoretical noise ceiling — it does *not* invalidate the metrics. The valid substratum of this point (underdescribed human eval, insufficient discussion of agreement) is preserved in Minor weakness #1.

2. **"The benchmark might be too difficult for current models."** — The reviewer acknowledges this is not a flaw of the benchmark itself. A benchmark's purpose is to expose gaps; difficulty is a feature, not a bug.

3. **"The benchmark sizes (150/120) are modest."** — This is a generic limitation statement, not a specific weakness. The paper does not claim exhaustive coverage; the sizes are reasonable for a focused benchmark testing a specific capability. The reviewer also labels this "not a critical issue."

4. **Generic formatting/style nitpicks.** — None present in the original review; all raised points are substantive.

## Novel Insights

The most insightful observation across the reviews is one the paper itself raises but does not fully exploit: the fact that current metrics (CLIP, ViCLIP, UMTScore) achieve near-zero correlation with human judgments on temporal compositionality (Table 3) implies that standard video-text alignment models are *temporally blind* — they encode frame-level semantics without any understanding of change, state transition, or attribute dynamics across time. This diagnosis goes beyond benchmarking and suggests a fundamental architectural limitation in how video-language models represent temporality. The paper's Figure 5 analysis corroborates this interpretation by showing that CLIP similarity to initial and final attributes remains essentially flat across all frames for T2V models.

## Suggestions

1. **Complete the I2V metric definition** by specifying the values (or at least the adopted range) of $w_1$ and $w_2$ in Eq. 4, and fix the "Fig. 2" reference.
2. **Expand the human evaluation section** with: number of videos annotated, annotation overlap structure, exact Likert scale anchors (what does each rating level mean for temporal compositionality?), and a brief discussion of the inter-annotator agreement numbers in context of the broader literature.
3. **Report human correlations for CogVLM2 and LLaVA-NeXT** alongside GPT-4 Turbo in Table 3 (or explain why they are omitted).
4. **Document the exact VLM evaluation protocol** — GPT-4 Turbo version/date, temperature, system prompt, and the in-context exemplars — in the supplementary materials or a GitHub repository.
5. **Add standard errors or bootstrapped confidence intervals** to the TCR results in Tables 1–2, especially given the modest per-category sample sizes (~50).

## Score and Decision

The paper addresses a real gap in video generation evaluation with a clean benchmark design, well-motivated metrics, and extensive experiments that reveal a clear and urgent limitation in current models. The weaknesses are concrete but fixable — they concern presentation depth (human eval details, metric specification, reproducibility documentation) rather than fundamental flaws. None of the issues invalidate the core contribution.

**Score: 6.5 / 10**

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>