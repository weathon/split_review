Now I have all the information needed. Let me write the consolidated review.

## Summary

GIFT-Eval introduces a curated, diverse time-series forecasting benchmark spanning 23 datasets (144K time series, 177M data points) across 7 domains and 10 frequencies, paired with a separate non-leaking pretraining dataset (~230B data points). The paper provides extensive evaluation of 17 baselines (5 statistical, 8 deep learning, 4 foundation models) organized by domain, frequency, prediction length, and number of variates, along with qualitative failure-case analysis.

## Strengths

- **Large-scale, non-leaking pretraining dataset provided alongside the evaluation benchmark**: GIFT-Eval is the only benchmark among those compared (Monash, TFB, LTSF, BasicTS+) that provides a dedicated, non-overlapping pretraining set (verified in Table 1, §3.2 "Pretraining Dataset"). This enables future fair zero-shot evaluation where models are pretrained on the clean split and evaluated on the held-out test data.

- **Systematically diverse coverage across multiple characteristics and time-series features**: The benchmark spans 7 domains, 10 frequencies, univariate/multivariate series, and short-to-long prediction lengths. Diversity is validated using six statistical features (trend, seasonal strength, entropy, Hurst exponent, stability, lumpiness) displayed in heatmaps (Tables 2–5, Figures 1a–1d, §3.2), offering more thorough characterization than prior benchmarks.

- **Comprehensive evaluation of 17 baselines with probabilistic forecasting**: The benchmark reports both point (MAPE) and probabilistic (CRPS) metrics, uses a rank-based aggregation across 97 configurations, and evaluates 5 statistical, 8 deep learning, and 4 foundation models including multiple sizes (Table 1, §4). Probabilistic forecasting is absent from all other compared benchmarks.

- **Qualitative analysis of failure cases**: Beyond aggregate scores, the paper provides visual forecasts highlighting where models systematically underperform (e.g., decoder-only architectures on long horizons, all foundation models on high-frequency data), offering actionable insights beyond standard metrics (§4.3, Figures 2a–2d).

## Weaknesses

### Fatal

None.

### Major

- **Potential data leakage in some foundation model results is acknowledged but not fully separated in the presentation.** The paper explicitly notes (line 234) that TimesFM, Chronos, and the original Moirai "exhibit partial data leakage issues for GIFT-Eval." The authors retrain Moirai on the clean pretraining split, so the Moirai results in all tables are clean. However, TimesFM, Chronos, and VisionTS use their original pretrained weights, which may have seen parts of the GIFT-Eval test data during pretraining. The paper tables present all results side-by-side without clearly distinguishing "clean (retrained on GIFT-Eval pretraining split)" from "zero-shot with original weights (may include test data)." This matters because findings such as "foundation models struggle on high-frequency data" (using TimesFM/Chronos results) could be affected if leakage is non-uniform across frequencies. The benchmark resource itself is unaffected, but some comparative conclusions drawn from the evaluation would be stronger if the separation were explicit.

### Minor

- **Conflating two evaluation regimes in the overall "best model" narrative.** The paper declares PatchTST as "the most dominant model" overall (Table 5, §4.1). PatchTST is a deep learning model trained and hyperparameter-tuned per-dataset on each training split, whereas the foundation models are used zero-shot. The paper's stated purpose (§3) is to "evaluate the zero-shot and universal forecasting capabilities of foundation models." While the per-characteristic tables (domain, frequency, prediction length) allow readers to extract regime-specific conclusions, the abstract and overall conclusion would benefit from explicitly separating: (i) best zero-shot model (MoiraiLarge, Rank 5.99), (ii) best trained DL model (PatchTST, Rank 5.72), and (iii) the "zero-shot gap" between them. The current framing makes the regime comparison less transparent than it could be.

- **The Rank metric averages across 97 configurations with vastly different sample sizes without discussion of the distortion.** Some configurations contain 22 time series (e.g., 10S frequency) while others contain ~48,000 (Transport, Table 2). The unweighted average rank treats each equally. The paper itself notes a discrepancy: Crossformer has the most "best" counts (16, Table 6) but does not lead the overall Rank (PatchTST leads at 5.72), and the paper observes that "certain datasets may disproportionately influence the metric-based results" (line 427) but does not analyze whether the equal-weighting choice drives this discrepancy. A sensitivity analysis (e.g., weighting by number of series or observations) is needed to check whether the overall ranking is robust.

- **Absence of a limitations discussion.** The conclusion (Section 5) is brief and does not discuss limitations such as: the leakage issue for some FMs, the different training regimes compared, the dataset imbalance in the Rank metric, or the fact that only Moirai supports multivariate natively while others flatten the series. Including a limitations paragraph would improve scientific rigor.

- **Interesting observations on scaling laws and model behavior are noted but not analyzed.** The paper observes that MoiraiSmall sometimes outperforms MoiraiLarge and that Crossformer excels in "best counts" but not in average rank. These observations are presented without follow-up analysis (e.g., why might smaller models outperform larger ones on certain configurations?).

### Trivial

- None.

## Nice-to-Haves

- A sensitivity analysis with a series-count-weighted or observation-weighted version of the Rank metric would strengthen the claims about overall "best model."
- Reporting variability or stability of rankings across different random seeds would be useful, though not standard for this type of benchmark paper.
- The paper could note the approximate computational cost of evaluating all 17 baselines to help with practical adoption.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **Verifiability of the non-leaking claim (§4 of Harsh Critic):** The critic questions whether the appendix provides enough detail on how the non-leaking condition was verified. The paper states "Further details on pretraining dataset can be found in Appendix" — the appendix content is stripped by the parser and exists in the original submission. Removed per the hard rule about missing appendix content.

2. **"Lumpiness depends on series length":** The critic notes that lumpiness "is highly dependent on series length" which "could confound cross-dataset comparisons." This is speculative and not argued with evidence from the paper. Removed.

3. **"Summary of hyperparameter search space needed in main text":** The paper references the appendix for hyperparameter details. Removed per hard rules about appendix content.

4. **Criticism that TFB (Qiu et al. 2024) is "not entirely fair to fault for lacking pretraining data":** This is a comment on the paper's framing in Table 1 rather than a weakness of the paper itself. Removed.

5. **Strength Finder's generic strengths** such as "addressed an important problem" or generic praise — removed as they lack specificity or conflict with verified weaknesses.

## Novel Insights

None beyond the paper's own contributions. The key observation that foundation models underperform on high-frequency (secondly/minute) data and on datasets with high entropy/low trend (Transport domain), while PatchTST dominates in multivariate and long-horizon settings, is already well-articulated in the paper.

## Suggestions

1. **Clearly separate "clean" from "potentially contaminated" results in the tables.** Add a footnote or a row label indicating which foundation models were retrained on the GIFT-Eval pretraining split (Moirai variants) vs. those using original weights with potential leakage (TimesFM, Chronos, VisionTS). Alternatively, present two separate summary tables: one for zero-shot models (all using GIFT-Eval pretraining or clearly labeled) and one for trained DL models.

2. **Add a weighted Rank analysis** as a robustness check (e.g., weighting by number of time series or total observations per configuration). Report whether the overall ranking changes.

3. **Explicitly state the zero-shot gap** in the conclusion: e.g., "The best zero-shot model (MoiraiLarge) achieves Rank 5.99, compared to the best trained model (PatchTST) at 5.72, leaving a gap of X%."

4. **Add a limitations paragraph** to the conclusion acknowledging the leakage issue for some FMs, the regime mixing, and the equal-weighting choice in the Rank metric.

## Score and Decision

The paper makes a solid contribution by providing a much-needed diverse benchmark with a clean pretraining split. The benchmark resource itself is valuable, future-proof (any model can be pretrained on the provided clean data and evaluated on the test split), and fills a genuine gap in the time series community. The evaluation of 17 baselines is extensive and yields useful insights even with the caveats noted. The weaknesses (leakage in some FM evaluations, regime conflation in the narrative, unweighted rank metric) are real but addressable and do not undermine the core contribution.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>