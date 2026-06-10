Here is the final consolidated review:

---

## Summary

This paper introduces HR-Extreme, a high-resolution (3 km, from NOAA HRRR data) dataset of 17 types of extreme weather events over the US with 69 physical variables, designed for evaluating weather forecasting models specifically on extreme events. It also presents HR-Heim, a baseline deep learning model inspired by FuXi and MagViTv2. The paper evaluates four models (HR-Heim, Pangu, FuXi, and the operational NWP) on both a full-domain test set and the HR-Extreme subset, and reports that extreme weather errors are substantially larger than overall errors.

## Strengths

- **~10× higher spatial resolution than the ERA5 benchmark**: The dataset is derived from 3-km HRRR data, whereas prior ML weather forecasting datasets and models (Pangu, FuXi, FourCastNet, GraphCast) predominantly use ERA5 at 0.25° (~31 km). This is stated explicitly (lines 22, 52) and represents a genuine gap.

- **17 extreme weather types vs. 1–3 in prior datasets**: Prior datasets (ExtremeWeather: 3 types; ClimateNet: tropical cyclones + atmospheric rivers; Liu et al.: fewer types, China-only) have narrower scope. The paper's multi-source collection pipeline (NOAA Storm Events Database, Storm Prediction Center with DBSCAN clustering, manual temperature filtering) assembles all 17 types and is well-documented (lines 22–24, Section 3.2).

- **Dataset construction pipeline is well-engineered and reusable**: The DBSCAN-based clustering of SPC reports, the mask-aware cropping to 320×320 patches, the edge handling (shifting patches inward rather than padding), and the code interface for generating additional years are clearly described (Section 3.2–3.3). These are thoughtful practical details.

- **Per-variable normalized RMSE visualization**: Figure 3 (polar plot) provides a per-variable breakdown of normalized RMSE for all four models on both test sets, allowing comparison of model behavior across individual variables rather than relying solely on aggregate metrics.

## Weaknesses

### Fatal
None.

### Major

- **No disclosure of how Pangu and FuXi were adapted to HRRR data.** The paper describes the original Pangu and FuXi architectures generically (lines 116–118) but never states whether they were applied zero-shot, fine-tuned, or retrained on HRRR data. These models were designed for global ERA5 at 0.25° resolution (~31 km) with a different set of variables, a different grid structure (721×1440 vs. 1799×1059), and a different spatial domain (global vs. US-only). Using them on 3-km US-domain HRRR data with 69 specific variables requires substantial architectural adaptation that is not documented. Without this information, the central comparison in Table 1 and the claim that "HR-Heim outperforms SOTA methods" (contribution 3, line 24) cannot be evaluated.

- **The aggregate RMSE in Table 1 is unexplained.** The polar plot (Figure 3) caption specifies "normalized RMSE," but Table 1 just says "RMSE." The reported values (1.40, 2.77, 2.39, 2.35) cannot be raw RMSE averaged across 69 variables with incommensurate physical units (mean sea level pressure ~100,000 Pa, temperature ~300 K, wind speed ~10 m/s, specific humidity ~0.01 kg/kg). If the values are normalized, the normalization scheme must be specified. If they are not, the aggregate is physically meaningless. Either way, the headline percentages (34.30%, 394.23%) built on these numbers lack a clear basis, and the paper's core quantitative narrative is undermined.

### Minor

- **Missing dataset statistics essential for a dataset paper.** No per-type event counts, total number of 320×320 patches, or temporal/spatial distribution statistics are reported anywhere. Users cannot assess the dataset's coverage, balance across event types, or potential biases. A dataset paper should include at minimum a table of counts per extreme weather type.

- **The "original test set" vs. HR-Extreme comparison conflates different data distributions.** The paper compares RMSE on the full US domain (1799×1059 pixels, all timestamps) with RMSE on cropped 320×320 patches around extreme events. While this directionally supports the claim that extreme events have larger errors, the specific percentage increases are not clean measures because they compare aggregate error across two populations with different spatial extents, sample sizes, and data distributions. A within-set stratified analysis (extreme-event pixels vs. non-extreme pixels from the *same* forecast field) would provide a more rigorous comparison.

- **No training hyperparameters reported for HR-Heim.** Only batch size=8 is reported (line 136). Missing: optimizer, learning rate, scheduler, loss function, number of parameters, FLOPs, training/validation split. This makes the baseline model non-reproducible.

- **Figure 4 caption conflates the dataset name with the model name.** The caption (line 173) refers to "HR-Extreme prediction" when the model shown is actually HR-Heim. HR-Extreme is the dataset. This creates unnecessary confusion.

### Trivial

- Truncated data URL (line 106: "\url{https://huggingface.}") — appears to be a compilation artifact but should be checked.
- The paper claims "extensive evaluation" (contribution 3, line 24) but the quantitative evaluation consists of one table and one polar plot, plus two qualitative case study timestamps.

## Nice-to-Haves

- Reporting standard meteorological skill scores (e.g., anomaly correlation coefficient, CRPS) alongside RMSE would strengthen the evaluation.
- Per-event-type breakdowns or bootstrap confidence intervals for the RMSE values would quantify uncertainty.
- An ablation study isolating the contributions of causal convolutions and progressive upsampling in HR-Heim would support the architectural claims.
- Extending the dataset beyond 2020 to multiple years, or at least characterizing year-to-year variability, would increase practical utility.

## Removed Points

- The harsh critic's framing of the full-domain vs. HR-Extreme comparison as "structurally unsound" — **downgraded to Minor**. The comparison is directionally informative; the imprecision is in the specific percentages, not the comparison itself.
- The critic's quibble about ERA5 "31-km resolution" being slightly overstated at some latitudes — **removed**. Does not affect the paper's substantive claim.
- The critic's criticism about missing confidence intervals/error bars — **moved to Nice-to-Haves**, as single-run evaluation is standard practice in this field.
- The critic's assertion that the evaluation comparison is "broken" and "cannot be fixed by adding experiments" — **removed**. The comparison can be fixed by providing the missing methodological details and stratification.
- The Strength Finder's claim that "HR-Heim outperforms SOTA methods" — **kept but qualified**, as this depends on fair baseline comparison which is currently undocumented.
- Generic strengths from the Strength Finder about the problem being important — **removed** as they add no specific evidence.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- **Disclose the baseline adaptation explicitly**: State whether Pangu and FuXi were applied zero-shot (and note the architectural incompatibility), fine-tuned on HRRR, or retrained. If zero-shot was attempted despite the mismatch, caveat the comparison as a transfer-learning experiment, not a head-to-head capability comparison.
- **Clarify the aggregate RMSE**: Specify whether Table 1 reports normalized or raw RMSE. If normalized, describe the normalization (e.g., per-variable division by standard deviation, or min-max scaling).
- **Replace or supplement the aggregate comparison with within-set stratification**: Compute per-pixel errors on the full-domain predictions and stratify by whether pixels fall within extreme event bounding boxes or not. This directly tests the claim without comparing disjoint test distributions.
- **Add a dataset statistics table**: Report counts per extreme weather type, temporal distribution (monthly), and spatial distribution.
- **Provide training details for HR-Heim**: Optimizer, learning rate, scheduler, loss function, parameter count, training data split.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>