- Decision: Accept
- Avg Score: 6.50
- Scores: 8, 6, 6, 6
Now I have thoroughly verified the paper content. Let me produce the consolidated review.

## Summary

This paper studies emergent abilities in LLMs on multiple-choice tasks. The key observation is that when questions are grouped by difficulty, easy questions show inverted-U scaling (deep double descent pattern) while hard questions show U-shaped scaling. These opposing trends offset each other at the aggregate level, explaining apparent performance stagnation followed by a sharp surge. Building on this, the authors propose the Slice-and-Sandwich pipeline that fits separate scaling trends on easy and hard question groups using pre-threshold data and averages them to forecast post-threshold performance. Experiments on MMLU, arithmetic, and Persian-QA are presented.

## Strengths

1. **Novel empirical observation of opposing scaling trends by question difficulty.** The paper demonstrates a clear and well-motivated finding: for multiple-choice tasks with emergent abilities, easy questions follow an inverted-U pattern (consistent with deep double descent) while hard questions follow a U-shaped pattern. This is documented across multiple datasets (MMLU, arithmetic, Persian-QA in the main text; three additional emergent tasks in the appendix), and the opposing trends offer an intuitive explanation for why aggregate performance can appear stagnant before sharply improving.

2. **Theoretical connection to known phenomena.** Section 3 grounds the observed patterns in existing literature: the easy-group inverted-U is linked to deep double descent (Nakkiran et al. 2021), and the hard-group U-shape is linked to distractor tasks (Wei et al. 2023, McKenzie et al. 2023). The concrete example from MMLU (Table 1) showing a negation-based distractor that misleads small models provides a plausible mechanism.

3. **Proposed continuous metric (binary Brier Score).** The conditional binary Brier Score (Eq. 4–5) focuses on the target choice probability, avoiding the calibration sensitivity of the full Brier Score. The near-linear relationship between this metric and accuracy (Fig. 7) supports its use as a bridge metric for forecasting.

4. **Validation across multiple datasets.** Results are presented on three datasets in the main paper, with extensions to three additional emergent tasks and three non-emergent tasks in the appendix. This breadth supports the generality of the observed scaling trends.

## Weaknesses

### Fatal
None.

### Major

1. **No quantitative forecasting metrics reported.** The central claim — that Slice-and-Sandwich forecasts accuracy beyond the threshold better than a Sigmoid baseline — is supported solely by visual comparison of Figures 8–10. No RMSE, MAE, correlation coefficient, or confidence intervals are reported for either method. Without quantitative metrics, the reader cannot assess whether the apparent visual improvement is meaningful, nor compare across datasets. This is not a missing ablation; it is the core evidence for the paper's second contribution.

2. **Circularity in the threshold-dependent setup.** The emergence threshold *T* is identified from the full accuracy curve (Sec. 2.1: "we recognize the emergence threshold T as the effective model size M at which the model accuracy exhibits a sharp improvement"). This same *T* is then used to (a) define the training set (models before *T*), (b) compute question difficulty (average performance of models below *T*), and (c) determine where to start forecasting. The evaluation is therefore fundamentally retrospective: the pipeline requires knowing *T* to set up the training data, but *T* can only be identified by looking at post-threshold data. The paper does not address how *T* could be determined from pre-threshold data alone, which is what a true forecasting method would require.

3. **Insufficient baseline comparison.** Only a single Sigmoid-based scaling law is compared against. Several relevant methods cited in the paper (e.g., PASSUNTIL from Hu et al. 2023, other task-specific scaling law approaches from Owen et al. 2024, Ye et al. 2023) are not included as baselines. Additionally, it is unclear whether the Sigmoid baseline also uses only pre-threshold training data — a critical detail for a fair comparison, since the paper's method is trained on pre-threshold data and the baseline may or may not be.

### Minor

1. **Difficulty measure depends on the same threshold-defined model set.** Question difficulty (Eq. 5) is defined as average binary Brier score across all models below the emergence threshold. This makes difficulty relative to the set of small models rather than an intrinsic property of questions. The U-shaped and inverted-U patterns could be partly driven by which questions happen to be well- or poorly-suited to small models. The paper does not test whether these patterns persist under alternative difficulty measures (e.g., human performance, held-out model families).

2. **Polynomial fitting procedure underspecified.** The paper states "We use simple polynomial functions" (Sec. 4.3) but does not specify the degree, selection procedure (e.g., cross-validation), or regularization used. This is a reproducibility concern for a core step of the pipeline.

3. **The medium-group claim is asserted without demonstration.** The paper states that the medium group's pattern is "simply aggregating the scaling trend between easier and harder question groups" (Sec. 4.3) but does not empirically verify this claim (e.g., by showing that averaging easy and hard groups reconstructs the medium group's trajectory).

4. **Coincidence between threshold and reversal point is not quantified.** A key claim is that "the point at which performance on easy questions reverts from inverse scaling to standard scaling roughly coincides with the emergence threshold" (abstract, Sec. 2.3), but no quantitative distance or alignment measure is reported across datasets.

### Trivial
None.

## Nice-to-Haves

- Error bars or confidence bands on the group-mean scaling trends (bootstrapped across questions within each difficulty group) would strengthen confidence that the U-shaped/inverted-U patterns are real and not driven by noise.
- Testing robustness of the difficulty grouping to the choice of G (the number of groups) in the main paper — currently robustness discussion appears deferred to the appendix.
- Reporting the distance between the easy-group reversal point and the emergence threshold across datasets would quantify a claim currently left as qualitative visual inspection.

## Removed Points

These points are removed with justification:

- **"Conditional Brier Score is not invariant to the number of choices."** This is a property of conditional probability and is not a flaw — the paper is about multiple-choice tasks, and the conditional metric measures relative confidence among available options. The paper also notes that the effect of conditionality is discussed in the appendix.
- **"G=10 for phenomenon description vs. G=3 for the pipeline is inconsistent."** The paper explicitly states this choice is to reduce data noise in the fitting step (Sec. 4.3), which is a reasonable justification.
- **"The observed inverted-U is not compared to classic double descent quantitatively."** Section 3 provides a qualitative link to double descent, which is appropriate for an explanatory discussion. A quantitative comparison (e.g., relating the dip's location to model/data size) would strengthen but is not required.
- **"OLS regression on a small number of models is fragile."** This is a speculative concern; without knowing the number of models and seeing confidence intervals, it cannot be evaluated as a concrete weakness.
- **"Error bars on observations are missing."** A nice-to-have, not a methodological gap.
- **"Missing comparison to more baselines beyond the Sigmoid."** This was kept in the Major section (Point 3) but additional specific baselines (PASSUNTIL etc.) would strengthen. The original criticism is kept in a condensed form.
- **"The Sigmoid baseline details are not described."** Condensed into the main Major point about baseline fairness.
- Various Section-by-section notes from the harsh critic that are minor observations or formatting concerns rather than substantive weaknesses (e.g., the paper's multiple-choice focus being a limitation — the paper honestly acknowledges this).

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any observation that the paper itself does not already present.

## Suggestions

1. **Add quantitative forecasting metrics.** Report RMSE or MAE on held-out models past the threshold for both Slice-and-Sandwich and the baseline, ideally with bootstrap confidence intervals. This is the single most impactful change.

2. **Address the threshold circularity.** Either (a) propose a principled method for detecting *T* from pre-threshold data alone (e.g., fitting a piecewise linear model and selecting the breakpoint), or (b) restructure the evaluation as a time-series forecasting task: train on models up to size *M*, forecast beyond *M*, and report error as a function of *M*. This would demonstrate out-of-sample predictive power without presupposing knowledge of the true threshold.

3. **Validate difficulty grouping robustness.** Test whether the U-shaped/inverted-U patterns persist under alternative difficulty definitions (e.g., using a held-out model family or human performance) to address the concern that patterns are artifacts of the threshold-dependent difficulty measure.

4. **Expand the baseline comparison** to at least include straightforward alternatives such as fitting the same polynomial or sigmoid to aggregate binary Brier Score directly, to isolate the benefit of grouping by difficulty.

5. **Specify polynomial fitting details** (degree selection, regularization, if any) for reproducibility.
