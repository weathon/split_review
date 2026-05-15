Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper presents an energy forecasting package and comprehensive benchmark. It collects 12 load datasets, releases a new multi-level (station/city/region) renewable energy dataset with co-located meteorological data covering PV, onshore, and offshore wind, implements temperature-calendar feature engineering for load forecasting, provides a custom loss function framework linking forecasting error to dispatch cost, and benchmarks 21 probabilistic forecasting methods across these datasets.

## Strengths

- **Novel multi-level renewable energy dataset with paired meteorological data** (Section 2.2, Table 2): The released dataset is genuinely differentiated from existing resources by providing PV, onshore wind, and offshore wind at station, city, and region levels within the same first-level administrative region, with matched external factors (wind speed/direction at hub height, irradiance, temperature) and station location information. This addresses the well-recognized community problem of lacking co-located meteorological data for renewable forecasting.

- **Temperature-calendar feature engineering delivers substantial improvements on stable aggregated load datasets** (Table 3): The results show consistent and often large Pinball Loss reductions after applying the proposed feature engineering on GEF12, GEF14, GEF17, Bull, Hog, Cockatoo, and PDB across all 12 deep learning methods. For example, GEF14 FFNN drops from 79.64 to 54.96 and GEF17 FFNN drops from 56.00 to 45.28. This provides quantitative evidence that coupling calendar and temperature variables benefits load forecasting, and the benchmark systematically documents where it helps and where it hurts.

- **Modular open-source package with low-barrier extensibility** (Section 3.3): The package design cleanly separates preprocessing, feature engineering, forecasting methods, postprocessing, and evaluation. The one-command `calculate_scenario` API and simple `append` mechanism for adding new models are well-conceived design choices that lower the practical barrier for practitioners and reproducibility.

- **Large empirical scope**: Benchmarking 12 deep learning methods on 9 load datasets (Table 3) and 9 renewable datasets (Table 4) under a consistent protocol provides a useful reference point for the community, particularly the systematic evaluation of temperature feature engineering across diverse datasets.

## Weaknesses

### Fatal
None.

### Major

- **Custom loss function — a claimed core contribution — lacks any experimental evaluation.** The paper states in the Contributions (Section 1, item 2) and in Section 3.2.2 that a custom loss function linking forecasting error to simulated dispatch cost is a key offering. Section 5.1 promises "relevant point forecasting results for our proposed custom loss function," and the Contributions claim a comparison "between the traditional MSE loss function with our proposed loss function." **No such results appear anywhere in the paper.** The tables (Tables 3, 4) only report Pinball Loss for probabilistic forecasting. The paper cannot claim a loss function as a contribution without demonstrating it empirically — even a single dataset comparison (custom loss vs. MSE for point forecasting, with both Pinball Loss and simulated dispatch cost) would suffice. As submitted, this contribution is unsubstantiated.

- **Renewable energy benchmark uses an ambiguous input setup that may invalidate its results.** Section 4.2 states: "we will input the renewable energy sequence and meteorological factors of the past 24 hours, **as well as the meteorological factors of the next 24 hours**, into the model." The paper does not clarify whether these "next 24 hours" meteorological factors are ground-truth observations (which would make the evaluation unrealistic — a model reading future weather trivially outperforms any real forecast) or legitimate weather forecasts (NWP outputs). The data description (Section 2.2, Table 2) only describes historical meteorological measurements and makes no mention of forecast data acquisition. If ground-truth future data were used, every result in Table 4 and all conclusions drawn from it are invalid. This ambiguity must be resolved.

### Minor

- **The benchmark is less comprehensive than claimed.** The paper advertises "21 probabilistic forecasting methods" (Contributions, item 4) but the main quantitative table (Table 3) shows only 12 deep learning methods across 9 of the 12 load datasets. The 5 non-deep learning methods (KNNR, RF, SRF, ERT, SERT) and the 4 simpler methods (BEQ, BMQ, BECP, CE) described in Section 4.1 are discussed only qualitatively around the radar plot (Fig. radar) without tabulated results. The paper acknowledges results are "partial" but the gap between the advertised scope and the presented tables weakens the "large-scale benchmark" claim. Including full results for all methods and all datasets would substantiate the contribution.

- **Limited analysis of feature engineering failure cases.** The paper correctly notes that feature engineering degrades performance on the Covid19 and Spain datasets (Table 3), and offers brief speculation about distribution shift. However, no quantitative analysis connects data characteristics (e.g., temperature-sensitivity metrics, autocorrelation shift, distributional divergence) to the observed degradation. Understanding when feature engineering helps vs. hurts is important for practical guidance, and the current analysis is too shallow to support generalizable conclusions.

- **Dataset contribution lacks validation or comparison.** The renewable energy dataset is claimed as "the first high-quality renewable energy dataset with these characteristics" (Contribution 1), but the paper provides no quality analysis (e.g., missing rates, sensor accuracy, temporal coverage statistics), no comparison to existing open datasets (e.g., ERA5, NREL, Open Power System Data), and no description of the collection or quality-control methodology beyond a single table with licenses listed as "-". The dataset may indeed be valuable, but its quality and uniqueness are asserted rather than demonstrated.

### Trivial

- The paper reports that load data includes "actual measurement" meteorological data (Section 2.1) but does not specify the same for the renewable dataset's external variables, creating part of the ambiguity flagged in the Major issues above.

## Nice-to-Haves

- Reporting confidence intervals or performing statistical significance tests (e.g., Diebold-Mariano) over multiple time-series splits would strengthen the reliability of the comparisons.
- Adding a persistence or climatology baseline for renewable forecasting would establish a minimum-performance reference, especially given the ambiguous input setup.
- An ablation study for the renewable forecasting input design (past-only vs. perfect-future vs. forecasted meteorological factors) would cleanly resolve the ambiguity about data leakage.

## Removed Points

These points are flagged to be removed; treat them with caution:

- The critic's claim about the renewable dataset needing "collection methodology or licensing details" — Table 2 lists licenses as "-" which is a reasonable criticism, but this is a minor presentation issue that doesn't undermine the dataset's existence or potential value.
- The critic's section-by-section notes about Table 1 missing external variables for ELF and UCI — this information is clearly shown in the table (they have "No" under External variables), so the paper is transparent about this.
- The critic's note about Section 4.1 not specifying direct multi-output vs. recursive forecasting — this is a minor implementation detail common in the field and doesn't affect the validity of the results.
- The Strength Finder's claim about the custom loss function being a strength is retained (the method description is well-motivated) but weakened by the absence of experimental validation.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Most critically**: Either add a dedicated table showing point forecasting results comparing the custom loss function against MSE/MAE on at least one load dataset (reporting both Pinball Loss and simulated dispatch cost), or remove the unsubstantiated claim from the contributions. This is necessary for the loss function to count as a supported contribution.

2. **Clarify the renewable energy input setup explicitly**: State whether "meteorological factors of the next 24 hours" are NWP forecasts (and if so, from which provider/model) or ground-truth observations. If ground-truth, the renewable experiment must be redesigned. If forecasts, describe the forecast source and how it was obtained. This is essential even if the renewable results are presented only as a package demonstration rather than a rigorous benchmark.

3. **Complete the benchmark tables**: Add a supplementary table with results for all 21 methods (including non-deep learning methods) on all 12 load datasets, or adjust the stated contribution to match what is actually presented.

4. **Provide dataset documentation**: Add a data sheet or appendix describing collection methodology, quality control procedures, sensor types, and a summary of basic statistics for the renewable dataset. A brief comparison to existing open renewable datasets would substantiate the claimed uniqueness.

## Score and Decision

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>