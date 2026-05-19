- Decision: Reject
- Avg Score: 4.25
- Scores: 6, 5, 3, 3
Now I have all the verification I need. Let me construct the final consolidated review.

## Summary

This paper presents a combined resource contribution for energy forecasting: (1) a new open-source renewable energy dataset covering onshore wind, offshore wind, and PV at station, city, and region levels with co-located meteorological variables; (2) the ProEnFo package implementing modular forecasting pipeline components including temperature-calendar feature engineering and a custom loss function derived from an IEEE 30-bus dispatch simulation; and (3) a large-scale benchmark evaluating 21 probabilistic forecasting methods across 12 datasets (load and renewable) under 11 metrics. The temperature feature engineering benchmark is the main empirically validated contribution; the custom loss function is introduced and derived but never experimentally evaluated.

## Strengths

- **New multi-type, multi-level renewable energy dataset with meteorological data.** Section 2.2 (Table \ref{renew_Dataset}) documents 72 renewable energy series across station, city, and region levels, covering onshore wind, offshore wind, and PV, each with corresponding meteorological variables (wind speed/direction at turbine hubs for wind; irradiance and temperature for PV; station locations). This is the first dataset to combine all three renewable types from the same administrative region at multiple spatial granularities, enabling cross-type analysis under shared climate conditions — a genuine gap in existing public resources.

- **Temperature-calendar feature engineering with substantial, documented improvements on deep learning models across multiple datasets.** Table \ref{prob} shows that the proposed feature engineering (Section 3.2.1) consistently improves Pinball Loss for deep learning methods on 7 of 9 load datasets. The improvements are often large (e.g., GEF14: FFNN from 79.64 to 54.96; PDB: LSTM from 552.28 to 304.66; Cockatoo: all 12 methods improve). The paper also honestly reports the COVID-19 dataset where the feature engineering harms performance and provides a plausible explanation (distribution shift → model overfits to temperature-load relationship). This empirical coverage across 9 datasets, 12 methods, and an honest accounting of failure cases is the paper's strongest contribution.

- **Large-scale benchmark covering 21 forecasting methods, 12 datasets, and 11 metrics.** Sections 4 and 5 enumerate a systematic comparison spanning simple baselines, non-deep learning quantile regression methods, and 12 deep learning architectures, evaluated across aggregated-level, building-level, and renewable energy datasets. The result tables (Tables \ref{prob}, \ref{renew_result}) provide the broadest head-to-head comparison in the energy forecasting literature to date, fulfilling the paper's claim of a "comprehensive reference."

## Weaknesses

### Fatal

- **Custom loss function — a claimed core contribution — has zero experimental validation anywhere in the paper.** Section 3.2.2 derives a piecewise-linear loss function from an IEEE 30-bus economic dispatch simulation and the paper lists it as part of Contribution 2. Contribution 4 explicitly promises: "For point forecasting, we focus on 12 widely used deep learning methods and compare the traditional MSE loss function with our proposed loss function based on the relationship between forecasting error and cost." Section 5.1 states: "In addition, we also provide relevant point forecasting results for our proposed custom loss function." **No such results appear.** There is no table, figure, or numerical comparison of models trained with MSE vs. the custom loss, no cost-based evaluation metric, and no demonstration that the custom loss actually reduces dispatching cost relative to standard losses. Every experimental table in the paper reports only probabilistic forecasting results (Pinball Loss). The contribution therefore remains an unsupported proposal. This is not a missing ablation — it is the absence of a central experiment that was explicitly claimed as part of the paper's contributions. This alone precludes acceptance in the current form. (*Verification: Lines 29–30 and 33 promise the experiment; lines 174–175 state results "are provided"; no table or figure in Section 5 or anywhere else delivers them.*)

### Major

- **No hyperparameter search or training configuration is described for any of the 21 methods, undermining the benchmark's reliability.** The paper compares 21 probabilistic forecasting methods (12 of them deep learning) across multiple datasets, yet provides zero information about learning rate, batch size, number of epochs, optimizer, validation split, hyperparameter search procedure, search space, number of trials, or random seeds. The only training detail given is "the neural network is trained based on gradient descent" (line 165). The paper references a "default strategy" (Section 4, line 137) for the 24-hour ahead task, which suggests all methods were run with default, un-tuned hyperparameters. If true, the benchmark results likely understate the capability of more complex models (Transformers, Autoformer, WaveNet, N-BEATS) that require careful tuning — and the observation that "simple FFNN, LSTM, and CNN methods usually perform better than the more complicated ones" could be an artifact of inadequate tuning rather than a meaningful finding. For a benchmark paper whose stated purpose is to serve as a "comprehensive reference," this lack of transparency is a significant limitation. (*Verification: grep for "hyperparameter|tuning|learning rate|seed|epoch|batch size|validation" returns zero matches in the paper.*)

- **Ambiguity about whether actual future meteorological measurements are used as inputs for renewable energy forecasting, potentially creating data leakage.** Section 4.2 (line 168) states: "we will input the renewable energy sequence and meteorological factors of the past 24 hours, as well as the meteorological factors of the next 24 hours, into the model." The renewable dataset contains actual meteorological measurements (e.g., "real-time wind speed at wind turbine hubs," line 15). If the "meteorological factors of the next 24 hours" are actual future measurements rather than forecasts, this leaks information about the future that would not be available in a real forecasting setting, invalidating the evaluation. If they are forecasts, the source and nature of those forecasts must be cited and described. The paper does neither, leaving the validity of the renewable energy benchmark results unverifiable. (*Verification: Lines 168–169 describe the input setup; the paper never states whether the future meteorological data are measurements or forecasts.*)

### Minor

- **The renewable energy dataset novelty claim ("first high-quality renewable energy dataset with these characteristics," line 26) would benefit from a concrete comparison against existing public resources.** The paper lists the dataset's distinguishing features (multi-type, multi-level, same region, locations) but does not provide a comparison table against existing datasets such as those from NREL, Open Power System Data, or ENTSO-E. The claim is plausible but currently asserted rather than demonstrated through systematic comparison. Adding a small table contrasting properties (coverage, granularity, variables, time span) across existing datasets would substantiate the claim.

- **No variance or uncertainty quantification for any benchmark result.** All tables report single numbers without confidence intervals, standard deviations, or information about the number of runs. For a benchmark paper, this limits the reader's ability to assess whether observed differences between methods are meaningful.

- **Renewable dataset license is not stated.** Table 1 lists licenses for all load datasets (CC BY 4.0, CC0), but Table \ref{renew_Dataset} has no license column.

### Trivial

- None that warrant listing beyond what is captured above.

## Nice-to-Haves

- **Add the missing custom loss experiment:** Run point forecasting with MSE and with the custom loss on the same load datasets that have temperature data; report both Pinball Loss and simulated dispatching cost. This is the single most important addition; without it the paper's second contribution remains incomplete.
- **Report training time / computational cost per method per dataset** — valuable for practitioners choosing methods.
- **Include a worked extensibility example in the paper** beyond the two-line code snippets to concretely demonstrate the claimed "one command" extensibility.
- **Provide error bars** (at least for stochastic deep learning methods over multiple seeds) to establish whether differences in benchmark tables are statistically reliable.
- **Clarify the meteorological data source** for the renewable forecasting setup — if actual measurements are used, the results should be interpreted as an upper bound under perfect meteorological foresight.

## Removed Points

These points from the inputs were evaluated and removed because they do not survive verification or violate the filtering rules:

- **"Feature engineering evidence is mixed / paper oversells it"** (Harsh Critic #4) — *Removed because the paper already acknowledges the mixed results explicitly (lines 183–184: "for the COVID-19 dataset, adding feature engineering significantly worsens the result") and provides a nuanced analysis. The paper does not claim universal improvement; it documents where it works and where it does not. The criticism misreads the paper's framing.*
- **"Claim about competition winners is unsupported"** (Section-by-section note) — *Removed as a minor introductory claim that does not affect the paper's core contributions. Too minor to include.*
- **"Stronger statistical significance / more models"** (from various notes) — *Moved to Nice-to-Haves; the benchmark is already large-scale by the standards of the field.*
- **Strength about custom loss function being well-grounded** (Strength Finder #4) — *Partially removed from Strengths section because the derivation is sound but presenting it as an unqualified strength while the evaluation is completely missing would be misleading. The derivation is acknowledged in the paper's Section 3.2.2 but not presented as an evaluated strength.*
- **"Missing appendix / proofs in appendix"** — *Removed per instructions (parser strips appendices).*
- **"Formatting / style nitpicks"** — *Removed per instructions.*

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add the missing point forecasting experiment** comparing MSE vs. the custom loss function, reporting both traditional accuracy metrics and the simulated dispatching cost. This is the single most critical fix.
2. **Document training and hyperparameter configurations** for every method: search spaces, selection criteria, number of trials, learning rates, batch sizes, epochs, and the number of random seeds used.
3. **Clarify the renewable forecasting setup** — specify whether future meteorological inputs are actual measurements (and thus the benchmark represents a perfect-forecast upper bound) or NWP forecasts (cite the source).
4. **Add a comparison table** for the renewable dataset against existing public datasets to substantiate the "first" claim.
5. **Include confidence intervals or standard deviations** across multiple runs in the benchmark tables.

**Evaluation on standard axes:**
- *Originality:* Moderate. The dataset combination is novel; the feature engineering is adapted from prior work; the custom loss derivation builds on Zhang et al.
- *Importance of research question:* High. Unified energy forecasting benchmarks are genuinely useful to the community.
- *Claims well supported:* No. A central claimed comparison (MSE vs. custom loss) is absent; hyperparameter transparency is zero; renewable forecasting setup is ambiguous.
- *Soundness of experiments:* Moderate. The feature engineering benchmark is well-executed; the broader benchmark is undermined by the lack of training details and the data leakage ambiguity for renewables.
- *Clarity of writing:* Good. The paper is generally well-organized and readable.
- *Value to community:* Potentially high, contingent on fixing the above issues.
