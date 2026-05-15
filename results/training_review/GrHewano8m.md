Now I have all the information needed. Let me compile the final consolidated review.

## Summary

This paper introduces XXLTraffic, the longest publicly available traffic forecasting dataset spanning 23 years (2001–2024) with an evolving sensor network from California (PeMS) and New South Wales (tfNSW). The paper also presents a "beyond test adaptation" experimental setup with temporal gaps of 1–2 years between observation and prediction windows, benchmarks several forecasting models on this setting, and provides hourly/daily aggregated versions for conventional long-term forecasting.

## Strengths

- **Unprecedented temporal span for traffic forecasting**: Table 2 shows XXLTraffic covers 23 years, dwarfing prior datasets (e.g., LargeST with 4 years). This provides unique opportunities to study long-term distribution shifts and evolving infrastructure patterns that no existing public traffic dataset supports.

- **Captures evolving spatial topology over decades**: The paper documents (Figures 4b–d, Section 4.2) that sensor count grows from a few in 2001 to over 4,000 in some districts, and Figure 5 shows distributional changes across years. This reflects real urban evolution and enables research on expanding sensor networks.

- **Novel gap-based experimental configuration**: By formalizing forecasting with gaps of 1–2 years (Equation 2, Figure 6), the paper creates a realistic evaluation setting for scenarios like highway planning that existing contiguous-forecasting benchmarks cannot address.

- **Multi-scale aggregation and public release**: The dataset provides hourly and daily aggregations alongside the raw gap dataset, and the paper states the raw data, processing code, and processed data are available at an anonymous repository, supporting reproducibility.

## Weaknesses

### Fatal
None.

### Major

- **Temporal granularity of the gap experiments is never specified**: The paper uses "96 time steps" as input and "336 time steps" as ground truth (Section 5.3), and gaps of 1, 1.5, and 2 years, but never states whether a "step" is hourly, daily, or at some other resolution. The raw PeMS data has 5-minute resolution and the paper mentions hourly/daily aggregations for the non-gap benchmarks, but the gap dataset's granularity is left ambiguous. Without this, it is impossible to interpret what the models are predicting or how the gap length relates to the forecast horizon, fundamentally undermining reproducibility.

- **Gap experiment results are based on a 10% subsample without justification of representativeness**: Section 5.1 states that "due to the extensive span of up to 20 years resulting in a large sample size, we fixed a seed during data preprocessing to select 10% of the dataset for training and testing to quickly demonstrate our results." For a dataset/benchmark paper, this is a significant methodological concern. No analysis is provided to show that this 10% subset preserves the distributional properties (mean, variance, autocorrelation, trends) of the full data. The quantitative claims in Tables 3 and 4 must therefore be interpreted with caution.

### Minor

- **The "beyond test adaptation" framing is overstated relative to what the experiments actually implement**: The paper contrasts "beyond test adaptation" with test-time adaptation (Figure 1), defining the former as training separate models per gap setting. This is a coherent but thin distinction — training separate models for different data splits is standard practice. The real novelty is the dataset's temporal span and the gap setup, not a fundamentally new paradigm. The paper would benefit from either toning down the framing or providing a formal protocol that genuinely distinguishes the setting from standard forecasting.

- **Zero-shot forecasting for new sensors is claimed but never validated**: The contributions list (Section 1.2) states that the dataset "support[s] zero-shot forecasting for new sensors," but no experiment, analysis, or even schematic description of such a setup is provided anywhere in the paper. This claimed capability is unsupported.

- **Only one district (PEMS04) is shown in the input-length ablation**: Table 4 reports ablation results for varying input step lengths only on PEMS04_gap. Without results from other districts (e.g., PEMS03, PEMS08, tfNSW), it is unclear whether the observed improvement from longer inputs generalizes.

- **No analysis of why models fail on the gap task**: The paper notes that "nearly all results are poor" (Section 5.4) and speculates briefly about Autoformer, but provides no distributional analysis (e.g., domain shift metrics like MMD, trend/seasonality changes) to substantiate the claim that temporal domain shift is the cause of failure. This makes the gap results a descriptive negative result rather than an actionable insight.

### Trivial

- **The "constraints" discussion (Section 6) is vague**: It notes the large size as a limitation but immediately claims it "will become an advantage," which is a projection rather than an analysis of actual constraints.
- **No discussion of how sensor addition/removal over time is handled in training and test splits**: While the evolving network is mentioned, the paper does not specify the protocol for handling sensors that appear or disappear across the temporal split.

## Nice-to-Haves

- Providing a statistical comparison showing that the 10% subsample preserves the distributional properties of the full dataset would significantly strengthen the gap benchmark.
- Adding example prediction vs. ground truth plots for a few sensors in the gap setting would help readers understand the nature of model failures.
- Including a simple adaptation baseline (e.g., fine-tuning, mean-shifting) for the gap task would demonstrate that the setting is solvable rather than just reporting model failures.
- Expanding the input-length ablation to multiple districts and reporting variance across seeds would improve robustness.

## Removed Points

*These points are flagged to be removed, treat them with caution*

- **Criticism about Table 1 being "missing" (image placeholder)**: This is a parser artifact from the PDF extraction process. The original paper contains the table.
- **Criticism about sparse implementation details (learning rate, batch size, etc.)**: The paper states it uses "default settings of the Time-Series-Library" (Section 5.3), which is a standard and sufficient specification. The mention of "nonexistent appendix" is also a parser artifact.
- **Criticism about missing comparison with published SOTA numbers on PEMS datasets**: The paper benchmarks multiple standard models on its own splits, providing relative comparisons. Requesting absolute comparison with published numbers from different splits is a nice-to-have, not a core flaw.
- **Criticism about "no adaptation mechanism" being employed**: The paper is a dataset paper introducing a benchmark setting. Requiring adaptation methods exceeds the paper's stated scope; the paper's contribution is the data, not methods.
- **Strength Finder's generic strength "Comprehensive benchmarking reveals current model limitations"**: This conflicts with the verified weakness about 10% subsampling making the quantitative results uncertain. Since the weakness is verified, the strength is downgraded. (The benchmarking effort itself is noted in the nice-to-haves.)

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a novel observation about the dataset or the gap setting that the paper itself does not already articulate.

## Suggestions

1. **Clarify the temporal granularity of the gap dataset**: Explicitly state whether the "steps" in the gap experiments are hourly, daily, or at another resolution. This is the single most important fix for reproducibility.
2. **Either justify the 10% subsample or report results on the full dataset**: Provide distributional statistics comparing the subsample to the full data, or run the gap experiments on the complete dataset.
3. **Remove or substantiate the zero-shot claim**: Either add a zero-shot experiment (e.g., training on pre-2015 sensors and testing on post-2015 sensors) or drop the claim from the contributions.
4. **Tone down or better operationalize the "beyond test adaptation" framing**: Either define a formal protocol that distinguishes the setup from standard forecasting, or reframe the contribution around the dataset's temporal/extensional properties without claiming a new paradigm.
5. **Add domain-shift analysis**: Provide quantitative evidence (e.g., distribution distances, trend shifts) to explain why models fail on the gap task, turning a negative result into an actionable insight.

## Score and Decision

This is a potentially valuable dataset contribution (23-year span with evolving sensor networks is genuinely novel) that is undermined by several presentation and methodological gaps. The core problems — unspecified temporal granularity and unvalidated 10% subsampling — are not fatal to the dataset's existence but do prevent the gap benchmark from being accepted as a reliable reference. The dataset itself merits publication after corrections, but the paper as submitted does not yet meet the standard for a citable benchmark resource.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>