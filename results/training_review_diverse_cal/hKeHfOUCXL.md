I have thoroughly verified the paper content against all reviewer claims. Let me now compile the final consolidated review.

---

## Summary

This paper presents an open-source energy forecasting package (ProEnFo) that includes domain-specific feature engineering (temperature-calendar coupling), a custom loss function linking forecasting error to dispatching cost, and a new renewable energy dataset with station/region-level PV, onshore wind, and offshore wind data alongside meteorological variables. It also provides large-scale benchmarks comparing 21 probabilistic forecasting methods on 12 energy datasets. The temperature feature engineering analysis is empirically validated on multiple datasets, but the paper's most distinctive claimed contribution — a comparison of the custom cost-aware loss function against MSE for point forecasting — is entirely absent from the experimental section, leaving a central claim unsubstantiated.

## Strengths

1. **New renewable energy dataset with station-level and region-level data covering multiple generation types and meteorological factors.** The dataset (Section 2.2, Table II) includes 21 station-level series (10 onshore wind, 1 offshore wind, 10 PV) with wind speed/direction, irradiance, temperature, and location data, plus 46 region-level series across multiple cities. Providing multiple generation types at different scales under similar climate conditions differentiates this from prior renewable energy datasets and is a genuine community resource.

2. **Temperature-calendar feature engineering empirically shown to improve deep learning probabilistic load forecasting on most stable aggregated datasets.** The coupling formula (Section 3.2.1) is tested across 9 datasets and 12 deep learning methods. Table "prob" shows consistent Pinball Loss improvements on GEF12, GEF14, GEF17, Bull, Cockatoo, PDB, and Hog datasets (e.g., GEF14: FFNN drops from 79.64 to 54.96). The paper also honestly reports where it hurts performance (COVID-19, partially Spain) and offers plausible explanations. This is concrete large-scale evidence that was previously lacking in the literature.

3. **Fully modular open-source package with low barrier for adding new forecasting models.** The package splits the forecasting pipeline into five modules (data preprocessing, feature engineering, forecasting methods, postprocessing, evaluation) as shown in Figure 1, and provides code snippets (Section 3.3) demonstrating one-command model integration. This lowers the barrier for researchers to compare and contribute new methods in a standardized energy forecasting framework.

4. **Extensive benchmarking effort covering 21 probabilistic methods across 12 datasets and 11 metrics.** Despite partial presentation (see Weaknesses), the scope of the benchmark — spanning aggregated-level, building-level, and renewable energy data — substantially exceeds prior energy forecasting comparisons. The analysis of how temperature feature engineering interacts with model complexity yields practically useful insights.

## Weaknesses

### Fatal

1. **The promised point-forecasting comparison between the custom cost-aware loss function and MSE is entirely absent.** Contribution 4 states: "For point forecasting, we focus on 12 widely used deep learning methods and compare the traditional MSE loss function with our proposed loss function based on the relationship between forecasting error and cost." Section 5.1 states: "In addition, we also provide relevant point forecasting results for our proposed custom loss function." **No such table, figure, or quantitative result appears anywhere in the paper.** The custom loss function is described in Section 3.2.2 and visualized in Fig. 3, but its effect on actual forecasting performance is never evaluated. This is the paper's most distinctive claim (Cost-aware loss is what differentiates energy forecasting from general time-series forecasting per the paper's own thesis), yet the evidence needed to support it is missing entirely. This is not a minor omission; it is a fatal gap that undermines a core contribution. *Verification: I searched the full paper for any mention of point-forecasting results, MSE comparison tables, or custom loss evaluation. No such content exists beyond the promises quoted above.*

### Major

2. **Incomplete benchmark presentation for a paper claiming to be "the first large-scale benchmark."** The paper states 21 probabilistic forecasting methods were compared. However, Table "prob" shows detailed numerical results for only 12 deep learning methods. Non-deep learning methods (KNNR, random forest, etc. — 7 methods in total including BEQ, BMQ, BECP, CE, and five non-deep learning methods) are mentioned in text and referenced in a radar plot (Fig. "radar"), but no numerical results are provided in a table. The text makes comparative claims about non-deep learning methods ("non-deep learning methods perform better than deep learning methods without the temperature transformation strategy") without quantitative support. For a paper whose Contribution 4 is a benchmark, the reader needs full method-by-method numerical results to verify claims and enable future comparisons. *Verification: Table prob explicitly says "partial" in its caption. No other table with non-deep learning method results exists in the paper.*

3. **The renewable energy dataset's value is asserted, not demonstrated.** The paper's motivation emphasizes that "an excellent renewable energy dataset not only requires generation data but also corresponding meteorological data" (Section 1). Yet the renewable energy experiments (Section 5.2) do not include any ablation comparing forecasting performance with versus without meteorological inputs, nor any analysis showing that the provided meteorological variables actually improve forecasting over using generation data alone. The dataset description (Table II) provides no basic statistics (mean, variance, temporal coverage ranges, missingness handling procedures, sunset handling for PV) that would allow researchers to assess its suitability. The quality of the dataset is asserted but not evidenced. *Verification: Section 4.2 and 5.2 describe the renewable forecasting setup — meteorological inputs are always included, no ablation column comparing with/without them. Table II has no statistics columns beyond count and type.*

### Minor

4. **Origin of forecast meteorological variables for renewable energy is unclear.** Section 4.2 states that the model uses "meteorological factors of the next 24 hours" as inputs, but does not specify whether these are real forecasts from a meteorological service, perfect knowledge (ground truth), or simulated. This critically affects the difficulty and realism of the forecasting task and is necessary for reproducibility. *Verification: Line 168: "meteorological factors of the next 24 hours" — no source or type specified.*

5. **Key preprocessing details for the renewable dataset are missing.** The paper does not describe how missing values were handled for the renewable dataset (Table II marks all renewable series as "No" missing, but this is unusual for real-world sensor data and deserves explanation), how sunset/dawn periods were handled for PV (zero-generation periods), or any quality control procedures. *Verification: Table II shows "No" for Missing across all renewable series. No preprocessing section discusses these specifics.*

6. **No discussion of computational cost.** For a large-scale benchmark involving 21 methods across 12 datasets, training time, inference time, and hardware requirements would be valuable for practitioners choosing models. This is not fatal but would meaningfully strengthen the paper's practical utility.

### Trivial

- None identified beyond the issues already listed.

## Nice-to-Haves

- An ablation of the temperature feature engineering on the COVID-19 dataset restricted to the stable period, to test the paper's hypothesis that distribution shift causes the degradation.
- A demonstration of how a user would add a new forecasting method end-to-end, perhaps as an appendix walkthrough.
- Basic dataset statistics (temporal coverage, station coordinates, descriptive statistics) for the renewable dataset.

## Removed Points

The following points from the reviewers were evaluated and removed per the filtering rules:

- *"The feature engineering approach is a standard interaction-term construction and the piecewise linearization is adapted from prior work"* — This is not a weakness; it is how engineering contributions work. The paper explicitly cites Zhang et al. 2022. The contribution is in packaging, testing at scale, and demonstrating empirical value, not in proposing a novel mathematical derivation. Removed as mismatched expectation (the paper is a benchmark/package paper, not a theoretical methods paper).

- *"The paper claims the package is 'accessible and extensible' but provides only two code snippets"* — Two code snippets demonstrating the core commands are reasonable for an 8-page paper. Removed as a nitpick.

- *"Missing computational cost analysis"* — Moved to Minor rather than being treated as a major weakness, as it's a nice-to-have for a benchmark paper but not central to the claims.

- *Radar plot not being included* — The paper references Fig. "radar" which likely exists in the full PDF. The text extraction process strips figures. This is a parser artifact, not a paper flaw. However, the underlying concern (non-deep learning results lack numerical tables) is kept in Major #2.

## Novel Insights

The reviewers collectively identify a clear pattern: the paper makes ambitious claims (cost-aware loss function comparison, "first large-scale benchmark," high-quality dataset) but only delivers evidence for a subset of them. The temperature feature engineering analysis is genuinely informative and well-executed, but it constitutes the least novel part of the paper's thesis about what differentiates energy forecasting. The most novel claim — that cost-aware optimization beats MSE for point forecasting — is left completely unvalidated. This asymmetry between claimed and delivered contributions is the paper's fundamental structural problem.

## Suggestions

1. **Add the missing point-forecasting experiment.** This is the single highest-leverage action. Run the 12 deep learning methods with both MSE and the custom cost-aware loss on a representative load dataset (e.g., GEF14 or GEF17), report Pinball Loss and estimated dispatch cost on the IEEE 30-bus system. If the cost-aware loss reduces dispatch cost relative to MSE-optimized models, this single result would validate the paper's core thesis and transform the contribution.

2. **Complete the benchmark tables** by adding numerical results for all 21 methods (including non-deep learning) in a full table, even if in an appendix. The radar plot is helpful for visualization but does not substitute for precise numbers.

3. **Add a renewable dataset analysis section** with basic statistics and at minimum one ablation showing forecasting performance with versus without meteorological inputs, to demonstrate the dataset's value proposition.

4. **Clarify the source of forecast meteorological variables** (real forecasts vs. perfect knowledge) in the renewable energy setup.

## Score and Decision

The paper has genuine contributions: a useful renewable energy dataset, a well-tested feature engineering analysis, a modular open-source package, and an extensive (if partially presented) benchmark. However, the fatal omission of the central custom-loss experiment means that the paper's most distinctive claimed contribution cannot be evaluated. This is not a paper with minor flaws; it is a paper missing a core experimental result that is explicitly promised in both the contributions list and the experimental setup description. The paper cannot be accepted in its current form.

**Score: 4.5** — Clear contribution potential, but a fatal evidence gap prevents acceptance.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>