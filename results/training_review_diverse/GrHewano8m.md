Now I have all the information needed. Let me produce the final consolidated review.

## Summary

XXLTraffic is a dataset paper introducing traffic forecasting data spanning up to 23 years (2001–2024) from California (PeMS, 9 districts) and New South Wales, Australia. The dataset is distinguished by (1) an unprecedentedly long temporal span, (2) an evolving sensor network whose node count grows over decades, and (3) a novel "gap forecasting" task where observation and prediction windows are separated by gaps of 1–2 years, supporting applications like highway route planning. The paper also provides baseline results for 8 general time-series forecasting models across hourly, daily, and gap configurations.

## Strengths

- **Unprecedentedly long temporal span (23 years) with demonstrated distribution shifts.** The dataset covers 2001–2024, far exceeding the 5-year maximum of existing traffic datasets (Table 2, Figure 2). Figure 5 concretely shows that distributions at the same sensor location can change substantially over this period, validating the need for long-span data to study domain shifts in traffic forecasting.

- **Novel gap-based forecasting task.** The paper defines and benchmarks a prediction setting where observation and target are separated by temporal gaps of 1–2 years (Definition 4, Equation 2). This is structurally distinct from standard sequential forecasting and addresses real-world planning use cases (highway route planning, infrastructure investment). Tables 3–4 show that existing SOTA models perform poorly on this task (MSE > 0.85 on PEMS08_gap), confirming its novelty and difficulty.

- **Evolving sensor network over decades.** The dataset captures real infrastructure growth — sensor counts increase from a few hundred to over 4,000 per district (Figures 4b–4d, Table 2). This enables future research on zero-shot forecasting for new sensors and domain adaptation under network expansion, which static-node datasets cannot support.

- **Demonstration that longer input horizons improve gap forecasting performance.** Table 4 shows that extending input length from 96 to 1440 steps substantially reduces MSE (e.g., MICN on PEMS04_gap: from 0.968 to 0.536), directly validating the dataset's value for exploring extremely long input contexts.

## Weaknesses

### Fatal
None.

### Major

- **Five traffic-specific baselines are listed but their results are absent from all tables (Section 5.2 vs. Tables 3–5).** The paper states "we have selected five SOTA baselines Yu et al. (2018); Guo et al. (2019); Wu et al. (2019); Bai et al. (2020); Jiang et al. (2023) from traffic forecasting domain" — these correspond to STGCN, ASTGCN, Graph WaveNet, and other standard traffic models. However, Tables 3, 4, and 5 present results only for 8 general time-series models (Informer, MICN, FEDformer, PatchTST, Autoformer, iTransformer, DLinear, Mamba). The results discussion in Section 5.4 never mentions the traffic-specific models. For a dataset positioned as a traffic forecasting benchmark, this is a critical omission — the traffic community cannot evaluate the dataset's relevance without seeing how domain-specific models perform, especially on the hourly and daily benchmarks. The paper either overstates its evaluation or ran incomplete experiments.

- **Gap dataset construction is underspecified to the point of non-reproducibility (Sections 4.2, 5.1).** The paper specifies gap lengths of 1, 1.5, and 2 years (line 191), input length of 96 steps, and prediction length of 336 steps (line 209). However, it does not state: (a) the temporal granularity of the gap dataset (is it hourly? daily? aggregated from 5-min PeMS data?), (b) how gap years are converted to step counts when working with 96-step inputs and 336-step predictions, (c) how the 10% subset was sampled (random windows? sensor-based? time-based? with which seed?), and (d) what sensors are included in the gap dataset (only those active throughout the entire period, or a varying set?). Without these details, other researchers cannot reproduce the benchmark.

### Minor

- **"Beyond test adaptation" framing is conceptually unclear and adds little value.** Figure 1 defines "beyond test adaptation" as training separate models per gap setting, which is standard practice (train one model per experimental configuration). The contrast with test-time adaptation is not well-articulated, and the term does not describe a distinct technical paradigm. The paper would be stronger by simply describing the gap forecasting task directly without introducing this label.

- **No variance or confidence intervals reported.** The paper states five random seeds were averaged (line 209) but reports only point estimates without standard deviations (Tables 3–5). Given that the gap dataset uses only 10% of the data with a fixed seed, and the text notes that "nearly all results are poor," it is impossible to assess whether observed differences between baselines are meaningful or within noise. This is particularly relevant for the claim that MICN outperforms others on gap data — without variance, this could be a chance result.

- **Zero-shot forecasting for new sensors is claimed but never evaluated.** Line 41 lists "zero-shot forecasting for new sensors" as a contribution, and Section 1.2 frames it as a key challenge. However, no experiment, evaluation protocol, or even a discussion of how this would work is provided in the paper. This should either be demonstrated or moved to future work.

- **Missing data handling is not described.** PeMS data has known gaps and sensor outages, but the paper does not specify how missing values are treated (imputation method? masking? sample dropping?). Section 4.2 mentions "rigorous data filtering and aggregation" but gives no criteria (missing value thresholds, outlier removal procedures, aggregation method).

- **The 10% sampling for the gap dataset is insufficiently justified.** The paper states that due to the large span, 10% was selected with a fixed seed "to quickly demonstrate our results" (line 195). However, no analysis is provided on whether this subsample preserves the distributional properties of the full dataset. If the sample is biased (e.g., toward certain years or sensors), the benchmarking results may not be representative.

### Trivial
None.

## Nice-to-Haves

- A simple baseline (e.g., naïve seasonal forecast, historical average, last-observed-repeat) for the gap dataset would help contextualize the "poor" performance of learned models.
- An explicit table summarizing data format, file sizes, and number of time steps per sub-dataset would improve usability.
- A discussion of sensor placement bias (PeMS covers freeways only, tfNSW covers major roads) and its implications for generalizability would strengthen the prospects section.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Default hyperparameters from other domains are unlikely to be optimal"** (from reviewer). This is a standard practice for benchmarking — using default settings provides a fair comparison of out-of-the-box performance. Not a weakness, especially since the paper is introducing a dataset, not claiming to achieve SOTA results.

- **"The paper could show how the number of available sensors changes over time for each district"** (from reviewer). Figures 4b–4d already illustrate evolving sensor counts. Requesting per-district breakdowns extends an already adequate visualization into a more detailed analysis that is not necessary for the paper's core claims.

- **"Computational requirements... concrete estimate of disk space"** (from reviewer). The paper provides a public repository link and notes the data will be released post-publication. Disk/GPU requirements are useful documentation but not a requirement for publication. This belongs in repository README, not the paper.

- **"Missing discussion of sensor selection bias and representativeness"** (from reviewer). This is a scope-extension request for a paper that already acknowledges its computational limitations in Section 6.

## Novel Insights

The most interesting observation from the reviews is that the intersection of two separate weaknesses — missing traffic baselines and the 10% subsampling — creates a deeper concern than either alone. Without traffic-specific baselines, the hourly/daily benchmarks cannot serve the traffic community effectively; without a justified 10% sample, even if those baselines were added, the gap benchmarking results might not generalize to the full dataset. This suggests the paper should either commit to running a complete evaluation on the full gap dataset (or a properly stratified sample) with traffic-domain models, or scale back its benchmarking claims to reflect what was actually done.

## Suggestions

1. **Either run the five traffic-specific baselines and report their results, or explicitly remove them from the paper and explain why they were omitted** (e.g., they are designed for short-term prediction and adapting them to gap forecasting is non-trivial). If they were run, include them in all tables; if not, remove the statement.
2. **Fully specify the gap dataset construction**: state the temporal granularity, describe how a "gap of 1 year" maps to step counts given the input/prediction lengths, document the 10% sampling procedure (including seed), and report whether the sample preserves the full-data distribution.
3. **Provide standard deviations** for all reported metrics (Tables 3–5) so readers can assess significance.
4. **Either add an experiment for zero-shot new-sensor forecasting, or move this claim to the prospects/future work section.**
5. **Drop or significantly downplay the "beyond test adaptation" framing.** The gap forecasting task is the real contribution — describing it directly is clearer and more honest.

## Score and Decision

The XXLTraffic dataset itself is a valuable contribution — 23 years of evolving traffic sensor data genuinely fills a gap in the community. However, the experimental evaluation does not live up to the paper's benchmarking claims. The absence of any traffic-specific model results (despite being promised), the underspecified gap dataset construction, and the lack of variance reporting mean the paper does not currently provide a reliable or reproducible benchmark. These are fixable in revision but are substantive gaps in the current submission.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>