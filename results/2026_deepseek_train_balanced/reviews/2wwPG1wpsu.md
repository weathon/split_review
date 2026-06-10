## Summary

This paper introduces LST-Bench, a benchmark evaluating 11 deep learning models for long sequence time-series forecasting (LSTF) across 7 standard datasets and 7 newly introduced power-industry datasets. The paper's main claims beyond the benchmark itself are two empirical observations: (1) a "Degeneracy" phenomenon where models achieve low MSE/MAE while producing meaningless predictions (repetitive oscillations or flat lines), and (2) that all models converge to near-optimal performance in roughly one training epoch.

---

## Strengths

- **Identification of "Degeneracy" as a named phenomenon.** The paper surfaces a real and underappreciated problem in the LSTF literature: models can score well on MSE/MAE while generating predictions that are semantically meaningless (periodic repetition or straight lines). Section 5 and Figure 5 provide concrete visual evidence. This is a genuine observation that challenges the adequacy of standard metrics and is worth the community's attention.

- **Discovery of extremely fast convergence across all architectures.** The finding that all 11 models, regardless of architecture, reach near-optimal validation loss in roughly one epoch (Section 4, Figure 4) is striking and contrasts sharply with typical behavior in NLP/CV domains. If substantiated, this has implications for training efficiency and suggests that current LSTF losses may not drive models to learn richer patterns.

- **Prediction-consistency analysis across horizons.** The benchmark evaluates not just aggregate error but whether model quality degrades gracefully with longer prediction horizons (Table 3, Section 4). The dimension of "consistency" (whether a model performs worse at longer horizons rather than paradoxically better) is a useful addition absent from most existing benchmarks.

- **Systematic fairness controls.** The benchmark standardizes platform (single V100), input length (336), rolling-window evaluation (stride=1), and uses the authors' own code with default hyperparameters from original repositories across 11 models spanning four architectural families. This level of standardization is more thorough than typical model-vs-model comparisons.

---

## Weaknesses

### Fatal

None.

### Major

1. **The 7 "NEW" datasets are critically underdocumented.** The entire description of what should be a core contribution reads (line 91): *"Our dataset NEW consists of two years' worth of 15-minute-level data from the power industry, primarily used for equipment monitoring in the electricity sector. The data will be made open source."* No information is provided on what distinguishes the 7 datasets from one another (different sensors? different facilities? different measurement types?), their dimensionality (univariate or multivariate, number of channels), total time steps, missing-data rates, stationarity or seasonality characteristics, or preprocessing steps. For a benchmark paper whose introduction of new datasets is listed as a primary contribution, this level of documentation is insufficient for the community to use or assess them.

2. **Results on the standard (non-NEW) datasets are not reported in accessible tabular form.** Table 1 reports MSE/MAE only for the 7 NEW datasets. The 7 standard datasets (Weather, Traffic, ECL, 4×ETT) — which are the ones the community would use for validation and comparison — have their rankings discussed qualitatively via figures (Figures 1-3) and box plots, but their actual numerical results never appear in a table. A benchmark paper's central deliverable is its results table; omitting standard-dataset results substantially undermines the paper's utility.

3. **The "Degeneracy" finding lacks systematic quantification.** Degeneracy is named, described qualitatively, and illustrated with a handful of example plots (Figure 5), but the paper provides:
   - No quantitative metric to measure degeneracy.
   - No statistics on how frequently it occurs across the 11 models × 14 datasets × 4 prediction lengths.
   - No analysis of what causes it (loss function? data characteristics? model capacity? training dynamics?).
   - No connection to related literature on mode collapse or oversmoothing.
   
   The paper calls for "a reevaluation or redefinition of evaluation metrics" (line 16) but does not do any of the analytical work that would make this finding concrete. As presented, it remains an informal observation rather than a substantiated research result.

4. **The one-epoch convergence claim is similarly undersupported.** The paper states that "regardless of the architecture... in most cases, it only took 1 epoch to achieve the lowest loss" (line 154), supported only by a single figure (Figure 4) with no numeric data, no specification of which model-dataset combinations were tested, and no analysis of whether this reflects genuine convergence or is an artifact of using default hyperparameters (tuned for longer training in original papers). No training details (learning rate schedule, number of epochs trained, optimizer settings) are reported.

### Minor

1. **Inconsistency in the paper about prediction length.** Section 3.3 (line 106) states *"the predicted data length is unified to 192,"* but Table 1 and Figure 1 describe experiments at prediction lengths of {96, 192, 336, 720}. The paper clearly ran experiments at multiple horizons, making the "unified to 192" statement erroneous or misleading. This needs correction for clarity.

2. **The "prediction consistency" definition is conceptually problematic.** The paper defines inconsistency as performing *better* at a longer prediction length than a shorter one (Table 3 caption), based on the assumption that predictions should monotonically degrade with horizon length. But if a dataset has strong periodic structure at a specific horizon, a model genuinely performing better at that horizon is not necessarily a flaw — it could reflect meaningful structure. The framing treats a potential model strength (capturing periodic patterns) as a weakness.

3. **No results on standard datasets = no community validation.** The paper reports no MSE/MAE numbers for the 7 standard datasets in tabular form. Since these datasets have published results from prior work, the community has no way to verify whether the benchmark's implementations and hyperparameter choices reproduce expected performance levels, which is a basic sanity check for any benchmark.

4. **Single input length (336) limits comprehensiveness.** All experiments use input length 336. Model behavior is known to vary with input length in LSTF, and restricting to a single value limits the benchmark's claims to generality.

5. **No statistical significance assessment.** No standard deviations, confidence intervals, or significance tests are reported. Given that tier assignments are based on average rankings (e.g., tier 1 vs. tier 2 separated by rank 2 vs. rank 3-4), it is unclear whether these differences are statistically meaningful.

6. **Overstated claim about being the "first benchmark."** The paper states (line 67): *"Our work can be considered as the first benchmark for this problem after the widespread application of deep learning in time series forecasting."* This is historically inaccurate given the existence of the Monash Time Series Forecasting Archive (Godahewa et al., 2021) and other benchmarks. The paper cites only Libra as an existing benchmark, which underrepresents prior work.

7. **No limitations section.** The conclusion does not discuss any limitations of the benchmark (constrained input length, single-GPU setup, fixed hyperparameters, lack of statistical testing, undersupported Degeneracy/convergence findings), which is a notable omission for a benchmark paper.

### Trivial

- Several grammatical issues (e.g., "phenomenons" → "phenomena") and minor typos throughout.
- The citation syntax occasionally lacks proper spacing (e.g., "NLPDevlin et al.", "CVLiu et al.").

---

## Nice-to-Haves

- Include simple but strong baselines: seasonal naive (persistence forecast), ARIMA, and a straightforward linear regression. If DLinear barely beats seasonal naive on certain datasets, that is an informative result.
- Consider evaluating at more than one input length (e.g., 96, 168, 336) to assess input-length sensitivity.
- The authors could strengthen the Degeneracy finding by proposing a quantitative metric (e.g., spectral similarity between prediction and ground truth, or autocorrelation at dominant frequency) and reporting its frequency across the full experiment grid.
- Include RevIN as an optional experiment to assess whether normalization affects degeneracy.

---

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh critic's claim about "tables rendered as images that the parser could not extract"** — The tables are embedded as images in the original PDF; this is a formatting choice, and the parser's inability to extract text from images is a parsing artifact, not a paper flaw. Removed per hard rule re: parser/formatting artifacts.

- **Harsh critic's criticism about missing models from 2023–2024 (TimesNet, Crossformer, iTransformer, etc.)** — Per hard rule, missing related works cannot be raised as a weakness without external verification sources.

- **Harsh critic's concern about "not yet released" status of NEW datasets** — The paper states the data "will be made open source." Per hard rule, questioning the release status of a cited dataset/artifact is not permitted.

- **Harsh critic's claim about "fairness" of default hyperparameters being from different data splits** — This is speculative without evidence that the hyperparameters are indeed unfair; the paper transparently states it used default hyperparameters from the original repositories.

- **Strength Finder's generic/misdirected strengths are removed as per instructions:** The strength about "systematic fairness controls" is kept (it is specific). The strength about the 7 new datasets is kept but with caveat. Strengths that were purely about "addressing an important problem" or generic praise are removed.

---

## Novel Insights

None beyond the paper's own contributions.

---

## Suggestions

1. **Document the NEW datasets properly.** Provide a table with: dataset name, domain (what sensor/facility), number of time series, dimensionality (univariate/multivariate), total time steps, sampling frequency, train/val/test splits, and key statistical properties (trend/seasonality strength, stationarity test results, missing data rate).

2. **Report full numerical results for all 7 standard datasets in a main-table or appendix.** Without this, the benchmark cannot be verified or used by the community.

3. **Quantify Degeneracy.** Propose a metric (e.g., spectral distance, autocorrelation match, or prediction variance threshold) and report its frequency across the full model × dataset × horizon grid. This would turn a qualitative observation into a reproducible finding.

4. **Resolve the prediction-length inconsistency** in Section 3.3 (line 106).

5. **Reconsider the "inconsistency" definition** in the prediction-consistency analysis — performing better at longer horizons may reflect actual data structure rather than model pathology.

6. **Add standard deviations or confidence intervals** to the main result tables, even via bootstrapping over sliding windows.

---

## Score and Decision

This paper identifies genuinely interesting phenomena (Degeneracy, fast convergence) and takes a useful step toward standardized evaluation in LSTF. However, as a benchmark paper, it has three structural problems: the newly contributed datasets are essentially undocumented, the numerical results on standard (community-used) datasets are not presented in any accessible table, and the two headline findings are supported by qualitative examples rather than systematic quantification. These are not fatal individually, but together they mean the paper does not deliver a complete, usable benchmark or rigorously substantiate its claimed empirical discoveries at the level expected by ICLR.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>