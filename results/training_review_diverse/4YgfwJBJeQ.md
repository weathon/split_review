Now I have all the information I need to produce the consolidated review. Let me compile it.

## Summary

This paper proposes StructChart, a two-stage pipeline for visual chart understanding that: (1) extracts chart information using a learned CIE (chart image → LCT text), (2) converts LCT to structured triplets (STR) as a bridge representation, and (3) feeds STR to GPT-3.5 for downstream reasoning (QA, summarization, redrawing). Key contributions include the STR format (which improves over LCT for reasoning), a new SCRM perception metric, and an LLM-based data simulation method (SimChart9K) that dramatically reduces the need for real annotated charts.

## Strengths

1. **STR demonstrably improves downstream QA over LCT.** Table 4 shows StructChart+GPT-3.5 with STR achieves 68.4% Exact Match on ChartQA vs. 55.6% with LCT — a clean 12.8-point gain. This directly supports the paper's core design claim.

2. **SimChart9K enables dramatic reduction in required real data.** Table 5 (and the surrounding text) demonstrates that with SimChart9K, only 20% of real ChartQA samples suffice to match the perception performance of 100% real data. This is a practically impactful result for reducing annotation costs. The result generalizes to PlotQA (10%) and Chart2Text (20%) per Table 6.

3. **SCRM provides a structured, tunable perception metric applicable across chart types.** Unlike prior metrics tied to single chart types (bar-only, pie-only), SCRM evaluates entity and value accuracy under three tolerance levels, making it dataset-agnostic. It is used consistently across all perception experiments (Tables 2, 3, 5, 6).

4. **Performance scales predictably with more simulated data.** Table 3 shows consistent mPrecision gains as SimChart9K increases from 0.1K to 9K (e.g., from 57.3% to 73.6% at slight tolerance), confirming the simulation scheme produces useful training signal.

5. **The two-stage design with explicit STR bridge enables interpretability and modularity.** The STR output can be inspected, debugged, and fed to any reasoning module, and the paper demonstrates competitive QA results using only an off-the-shelf GPT-3.5 without prompt engineering (Table 4).

## Weaknesses

### Fatal
None.

### Major

1. **No quantitative evaluation for summarization and redrawing tasks, despite advancing them as part of the paper's scope.** The paper claims to be "generally applicable to different downstream tasks, beyond the question-answering task" (Abstract) and includes chart summarization and redrawing in the stated scope (Section 1, Section 4). However, the only quantitative reasoning evaluation is on QA (ChartQA, FigureQA). For summarization and redrawing, the paper states "due to the lack of public datasets and annotations, it is difficult to provide quantitative results" and refers to qualitative comparisons in figures (line 196). This is a significant gap: the paper's framing as a general chart understanding paradigm is not supported by quantitative evidence for half the claimed task scope. The paper would be stronger if scoped more narrowly to "chart perception and QA."

2. **Perception evaluation (CIE) lacks comparison against existing chart perception methods.** The paper evaluates its CIE model only on the proposed SCRM metric. There are no comparisons against existing chart perception approaches (e.g., ChartOCR, ChartReader, or other OCR-based methods) on established metrics such as cell-level accuracy, F1 for value extraction, or row/column assignment error rates. Without such baselines, it is impossible to assess whether the CIE model advances the state of the art in perception or is merely adequate. The paper's perception results (Tables 2, 3, 5, 6) are only relative to its own variants.

3. **SCRM is not validated as a reliable metric.** The paper claims "SCRM can effectively reflect the quality of CIE, as verified on the QA task" (line 186), but provides no correlation analysis, no ablation showing SCRM-picked models outperform alternatives, and no human evaluation. Table 4 shows QA accuracy (EM), not SCRM scores. The implicit reasoning — that better CIE leads to better QA, therefore SCRM is validated — is circular. A metric's value in a paper that introduces it should be established independently, not assumed from the pipeline it is part of.

### Minor

1. **"Unified paradigm" overclaims what is a sequential pipeline.** The paper describes StructChart as a "unified and label-efficient learning paradigm for joint perception and reasoning tasks" (Abstract), but the perception (CIE) and reasoning (GPT-3.5) stages are trained independently with no gradient flow between them. To the paper's credit, Section 3.1 is transparent: "we fulfill CU by solving two independent tasks: perception and reasoning" and the conclusion acknowledges end-to-end as future work. However, the "unified" framing in the abstract and introduction is inflated relative to what is delivered.

2. **Few-shot claims lack statistical rigor.** The paper states "only 20% real-world charts can basically achieve equal CIE performance under the 100% real-world training samples" (line 171). No confidence intervals, multiple random seeds, or statistical tests are reported. Given that few-shot splits and model training are stochastic, the results may not be reproducible as reported. The phrase "basically achieve equal" is also vague without precise numbers and variance bars.

3. **LCT position-sensitivity claim is asserted without ablation.** The paper states LCT is "highly position-sensitive" (line 65) and "the LCT format is sensitive to positional variations" but provides no ablation or experiment quantifying how much positional variation actually degrades performance. A controlled experiment (e.g., permuting row/column order in LCT and measuring downstream accuracy changes) would strengthen this motivation.

4. **No quality analysis of SimChart9K.** The LLM-based data production scheme is a contribution, but the paper does not report quality metrics for the generated charts: fraction of valid charts after self-inspection, diversity compared to real charts, or human evaluation of plausibility. The only evidence of quality is t-SNE visualization (Fig. 2) and the positive impact on training. Reporting the self-inspection success rate and basic diversity statistics would increase confidence in the simulation pipeline.

5. **SCRM tolerance levels and IoU thresholds appear arbitrary.** The three tolerance levels (strict, slight, high) and the IoU threshold range (0.5:0.05:0.95) are chosen without sensitivity analysis. It is unclear how results would shift with different thresholds.

### Trivial
- The CIE decoder type (autoregressive? cross-entropy loss?) and vocabulary size are not specified, slightly hindering reproduction.
- The cost trade-off of using GPT-3.5 for data generation (API costs vs. human annotation costs) is not discussed.

## Nice-to-Haves
- A comparison of the CIE model against existing chart perception methods (ChartOCR, ChartReader) on a common metric (e.g., cell-level F1) would strengthen the perception claims.
- Reporting few-shot experiments with 3–5 random seeds with mean and std would make the 20% claim more convincing.
- A correlation analysis (Spearman or Pearson) between SCRM scores and human judgment of perception quality would validate the metric.
- If the paper were re-scoped to focus on "perception + QA" rather than "general chart understanding," the missing summarization/redrawing results would no longer be a weakness.

## Removed Points
These points are flagged to be removed; treat them with caution.
- **"No comparison with ChartLlama or UniChart"** — Removed per instructions: missing related works cannot be verified as real or relevant by the reviewer.
- **"Tables are difficult to parse due to the text extraction"** — Parser artifact, not a paper issue.
- **"Qualitative visualization is weak evidence" (regarding t-SNE)** — This was rated down: t-SNE visualizations are standard practice for distributional alignment and the paper does not claim quantitative rigor from them; the point is kept only as a minor limitation rather than a major weakness.
- **"The data cost argument is weakened because SimChart9K is generated by GPT-3.5"** — This overreaches: the paper's claim is about reducing *human annotation* cost, not total compute cost. GPT-3.5 API calls are orders of magnitude cheaper than hiring domain experts. Kept as trivial only.
- **"No comparison with Matcha/Deplot on quantitative metrics"** — Removed as factually incorrect: the paper explicitly compares with Liu et al. 2022b (Matcha) in text on ChartQA (line 186: "comparable QA performance").
- **"Figures not shown in the extracted text"** — Parser artifact; figures exist in the original submission.

## Novel Insights
None beyond the paper's own contributions. The reviews surface the gap between the paper's broad claims ("general chart understanding") and its narrow quantitative evidence (QA only), and the lack of external perception baselines, but these are evaluation gaps rather than novel analytical insights.

## Suggestions
1. **Scope the paper's claims to match the evidence.** Either provide quantitative results for summarization and redrawing, or reframe the contribution as "chart perception and QA" — what is quantitatively demonstrated.
2. **Add external baselines for the CIE perception stage** against existing methods (ChartOCR, ChartReader) on a common metric.
3. **Validate SCRM** by showing its correlation with either human judgment or downstream task accuracy across multiple model checkpoints.
4. **Report error bars** for the few-shot experiments (multiple seeds, mean and std) to make the 20% claim statistically grounded.
5. **Report SimChart9K quality statistics** — fraction of valid charts after self-inspection, distribution of chart types, etc.

## Score and Decision

This paper makes three concrete contributions (STR, SCRM, SimChart9K) and provides solid evidence for two of them (STR improves QA, SimChart9K reduces real-data needs). The SCRM contribution is weaker due to lack of validation. The central weakness is the gap between the broad "general chart understanding" framing and the narrow quantitative evidence (QA only). This is a paper with real but incomplete contributions — publishable but needing refinement.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>