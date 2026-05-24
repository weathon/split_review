Now I have a thorough understanding of the paper. Let me synthesize the final review.

## Summary

This paper presents XXLTraffic, a traffic forecasting dataset spanning up to 23 years (2001–2024) from PeMS (California) and tfNSW (Australia), with evolving spatial nodes that grow from a few sensors to thousands. It also proposes a "beyond test adaptation" benchmark setting where predictions are separated from observations by a temporal gap (1–2 years), alongside conventional hourly/daily forecasting benchmarks. Experiments with eight time-series forecasting baselines show that existing methods perform poorly on the gap setting, and that longer input sequences (up to 1440 steps) improve results.

## Strengths

- **Unmatched temporal span and node growth**: Table 2 shows XXLTraffic covers up to 23 years (~8,400 days) and up to 19,000+ sensors, far exceeding the next-longest dataset (Large-ST at 5 years). This is a clear, well-documented contribution.
- **Distribution shift visualization**: Figure 5 plots sensor traffic distributions across years (2005–2024 for PeMS District 8, 2016–2022 for NSW), documenting that some sensors remain stable while others shift dramatically. This empirically grounds the claim of evolving temporal distributions.
- **Open release pipeline**: Section 4.1 and line 153 state that raw data, sensor metadata, processing pipeline code, and processed datasets will be publicly released (anonymous link provided). This supports reproducibility and community adoption.
- **Gap setting reveals methodological failure**: The text (line 216) reports that "nearly all results are poor" on the gap dataset and that traditional SOTA rankings do not hold, with MICN (weak on standard benchmarks) performing best. While the paper would benefit from in-text numbers, this finding is a useful signal for the community.

## Weaknesses

### Major

- **Data preprocessing is critically underspecified**: Section 4.2 consists of a single paragraph (lines 160–161) stating only that "rigorous filtering and aggregation" was applied. No details are given about: how missing values are handled across 23 years, how sensor IDs are tracked as nodes appear/disappear, what filtering criteria are used, how outliers are treated, what the sensor metadata schema is, or how data quality varies across years. For a dataset paper whose primary contribution is the curated data, this is a significant gap that undermines users' ability to understand the dataset's limitations or reproduce its construction.

- **Baseline evaluation is unclear for the five traffic-specific models**: Section 5.2 (line 202) states "we have selected five SOTA baselines ... from traffic forecasting domain," but Sections 5.4 (gap results) and 5.5 (hourly/daily results) discuss only the eight time-series baselines. It is never clarified whether the traffic-specific models were evaluated on the gap setting, the hourly/daily setting, both, or neither. This creates confusion about the completeness of the benchmark.

- **No quantitative results in the main text**: The paper makes qualitative claims such as "nearly all results are poor" and "performance improves significantly with input length increase" (lines 216, 222) without reporting any numerical values (e.g., MSE ranges, naive baseline comparisons) in the text. The results exist only in image-based tables that are unreadable after PDF extraction. For a benchmark paper, the community needs to see at least approximate error levels or key numbers inline to evaluate the difficulty of the setting.

### Minor

- **"Beyond test adaptation" framing oversells a straightforward configuration**: The paper claims this as a new direction, but the setting (predicting across a temporal gap of 1–2 years using separate models per gap) is a natural consequence of having long-span data rather than a conceptual or methodological innovation. The distinction from test-time adaptation (Figure 1 caption, line 19) is explained, but the framing inflates what is essentially a benchmark configuration into a paradigm shift. The dataset contribution is strong enough to stand on its own without this terminology.

- **Gap dataset uses only 10% sampling with thin justification**: Line 195 states that 10% of the full gap dataset was sampled "to quickly demonstrate our results." This reduces statistical reliability and is not convincingly justified—especially since the large size is one of the dataset's claimed advantages. The paper should explain whether the 10% subset preserves the temporal and spatial diversity of the full dataset.

- **Constraints section ignores data-quality limitations**: Section 6 (lines 244–246) only mentions computational resource requirements as a constraint. It does not discuss sensor coverage bias, missing data rates, temporal gaps in raw records, cross-year inconsistencies, or any other data-quality limitations that users of a long-span dataset need to know about.

- **No hyperparameter tuning for baselines**: The paper uses Time-Series-Library default settings (line 209) without any tuning on the new data. While this is a common practice for time-series benchmarks, 23-year domain-shifted data may warrant some adjustment to avoid disadvantaging particular methods.

### Trivial

- Several minor typos are present (e.g., "flitering" → "filtering" in line 160, "flies" → "files" in line 147, "beyong" → "beyond" in line 40, "fti" → "fit" in line 19). These do not affect comprehension but should be corrected.

## Nice-to-Haves

- Include a graph adjacency construction method (or explicitly state that no graph is provided) to clarify the dataset's compatibility with GNN-based models. The paper mentions that sensors are "densely interconnected, enabling the formation of a high-quality traffic graph dataset" (line 167) but never specifies whether a graph is included in the release.
- A naive/trivial baseline (e.g., repeating last observed value or seasonal persistence) would help calibrate how much better (or worse) the learned methods are on the gap setting.

## Removed Points

- **"Graph construction is a critical omission"** (Harsh Critic point 1): The paper's phrase "enabling the formation of a high-quality traffic graph dataset" is aspirational rather than a claim of providing a graph. The dataset release includes sensor metadata with IDs and coordinates (line 153), which is sufficient for users to construct their own graphs. This is a weaker criticism than presented.
- **"Figure 1 explanation is poor"**: The figure caption (line 19) clearly explains the distinction between test-time adaptation and beyond test adaptation. The criticism reflects a subjective readability preference rather than a verifiable flaw.
- **"Data processing is impossible to assess"** (Harsh Critic point 1, second sentence): While underspecified, the paper commits to releasing the processing pipeline code (line 153), which addresses the reproducibility concern.
- **Generic criticisms about "evaluation lacks rigor" / "evidence is weak"**: These are framed as area-concern sweeps without anchoring to specific missing numbers or experiments.
- **Strength Finder generic strengths** ("this paper addressed an important problem"): Removed because they are superficial and lack specific citation to paper content.
- **"Table images are unreadable"**: This is a PDF extraction artifact, not a flaw in the original submission. The tables exist in the paper.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any observation about the paper that is not already stated or implied in the manuscript.

## Suggestions

1. **Expand Section 4.2 substantially**: Describe missing-value handling, sensor-tracking methodology, filtering criteria, outlier treatment, and summary statistics (e.g., active sensors per year, missing-data rates per district). This is the single most impactful improvement.
2. **Add specific numbers to Section 5.4**: Include at least MSE/MAE ranges for the best and worst baselines on each gap dataset, and compare against a naive seasonal baseline to quantify difficulty.
3. **Clarify baseline coverage**: State explicitly which baselines (time-series and traffic-specific) were evaluated on which settings, and either include traffic-specific results or explain their omission.
4. **Justify the 10% sampling**: Explain whether and how the 10% subset preserves the full dataset's temporal and spatial distribution.
5. **Expand Section 6 (Constraints)**: Discuss sensor-coverage bias, data-quality variations across years, missing-data characteristics, and other limitations that users of a long-span dataset need to know.

## Score and Decision

This paper introduces a genuinely valuable dataset with clear advantages over existing resources (longest temporal span, evolving nodes, open release pipeline). However, the paper is weakened by a critically underspecified data preprocessing section, the absence of any quantitative results in the main text, and unclear baseline coverage. These issues are addressable through revision but are significant in their current form. The dataset is a real contribution; the paper does not yet do it justice.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>