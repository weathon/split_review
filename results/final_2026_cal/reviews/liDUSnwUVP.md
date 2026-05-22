## Summary

This paper introduces HG-DCM, a hybrid framework for early-stage pandemic forecasting that transfers knowledge from historical pandemics (Ebola, SARS, Dengue, seasonal influenza) to forecast a novel outbreak (COVID-19). The method uses a neural network to predict parameters of the DELPHI compartmental model from time-series and metadata, trained jointly on multiple past outbreaks to learn universal epidemiological dynamics. The core idea — cross-disease temporal transfer — is novel and well-motivated, but the evaluation is too narrow to fully substantiate the claimed superiority.

## Strengths

- **First systematic cross-disease temporal transfer for pandemic forecasting.** The paper makes a clear and well-supported claim (Section 1) to being the first work that leverages multiple biologically distinct historical pandemics to guide forecasting of a novel outbreak. This is a genuine contribution.

- **Clean, interpretable architecture.** HG-DCM's design is principled: a neural network predicts the 12 parameters of the DELPHI compartmental model, which are then fed through an ODE solver to generate forecasts. This preserves epidemiological interpretability while using deep learning to learn parameter dynamics from historical data (Section 2.1, Figure 1).

- **Ablation study isolates the role of historical data.** The T-DCM variant (which removes historical pandemic data and metadata) consistently underperforms HG-DCM on median MAE across all training windows (Table 2). This cleanly attributes the improvement to historical transfer rather than architectural complexity alone.

- **Interpretable parameter inference with statistical testing.** Section 3.2.3 and Figure 5 show that HG-DCM produces narrower parameter distributions than DELPHI, with Wilcoxon signed-rank tests confirming significant differences (p<0.05) for key parameters including infection rate and action timing.

- **Data augmentation strategies tailored to data scarcity.** The window-shift augmentation for past pandemics and block-masking for the current pandemic (Section 2.2, Figure 2) are thoughtful techniques that address the core data-scarcity problem.

## Weaknesses

### Major

- **External benchmarking is far too narrow to support the paper's strongest claims.** The paper compares HG-DCM against only two external methods (GradABM and EiNNs) on only two geographical locations (Massachusetts and the United States), as shown in Table 1. The abstract and introduction claim HG-DCM "consistently and significantly outperforms state-of-the-art methods," but this is supported by only 6 out of 8 table entries across two locations. Meanwhile, the ablation study (Table 2) evaluates on 258 locations, yet no external baseline is run on those locations. The paper acknowledges data/code availability as the reason, but this does not make the external evidence sufficient for the strength of the claims made.

- **Catastrophic mean failures in the coldest-start regime are not discussed.** At 2 weeks of training data, HG-DCM's mean MAE (18,602) is worse than both CNN (15,600) and T-DCM (15,049). At 4 weeks, the mean MAE (110,452) is an order of magnitude worse than CNN (11,238) — a roughly 10x gap. The median MAE tells a different story (HG-DCM is best at both 2 and 4 weeks on median), but the divergence between mean and median (factor of ~8 at 2 weeks, ~62 at 4 weeks) indicates that HG-DCM produces excellent forecasts at many locations but catastrophic failures at some locations. The paper reports only median improvements in the main text and does not analyze or even acknowledge these failure cases.

- **Only evaluated on COVID-19; no held-out pandemic test.** Since COVID-19 data is used in training (Section 3.1.2: "HG-DCM is trained on a composite dataset of past pandemics... alongside the available early-stage data (2–8 weeks) from the current pandemic (COVID-19)"), the evaluation cannot genuinely test whether cross-disease transfer works for a truly novel disease. The paper argues that spread dynamics are universal across diseases, but this claim would be substantially stronger if tested on a held-out historical pandemic (e.g., training on all pandemics except SARS and testing on SARS). The limited historical data makes this difficult, but without it, the evaluation validates the model for COVID-19 specifically rather than for novel pandemics in general.

### Minor

- **Training/evaluation split for the 258 COVID-19 locations is not clearly described.** The paper states that HG-DCM is trained on past pandemics plus early COVID-19 data and evaluated on 258 locations, but it does not specify whether the evaluation uses the same locations as training with a temporal split, a spatial hold-out, or some other protocol. This makes it difficult to assess potential information leakage.

- **The MAPE term in the loss function can explode for small case counts.** Equations (3)–(4) include a term α|(C_{ij} − Ĉ_{ij})/C_{ij}|. In the early days of a pandemic, cumulative case counts C_{ij} can be very small (or zero), causing this term to dominate the loss or become ill-defined. The paper does not discuss clipping, smoothing, or any handling strategy.

- **The overshooting metric (5× threshold) is ad-hoc and not standard.** While it provides a useful indicator, its definition (predicted cumulative cases exceeding observed by more than 5× at the final forecast week) is not justified or benchmarked against any established metric in the epidemic forecasting literature.

- **The removal of Batch Normalization is not empirically validated.** The paper argues that BN layers are harmful for cross-pandemic training (Section 2.1) but does not include an ablation comparing HG-DCM with and without BN. Testing this claim would strengthen the architectural justification.

- **No hyperparameter sensitivity analysis for α and β.** The balancing weights for the MAPE term (α) and the past/current pandemic trade-off (β) in the loss function (Eqns. 3–5) are not analyzed. How results vary with these critical choices is unknown.

### Trivial

None.

## Nice-to-Haves

- Evaluate on a held-out historical pandemic (e.g., leave out one disease from training) to test true cross-disease generalization.
- Analyze the failure cases where HG-DCM produces catastrophic mean errors at 2- and 4-week cold-start windows and discuss whether these can be mitigated (e.g., ensemble forecasting, clipping, or uncertainty quantification).
- Report confidence intervals or variance estimates for MAE across the 258 locations, not just mean and median point estimates.

## Removed Points

These points were raised in the input reviews but are excluded from the main weakness list for the following reasons:

- **"Comparison setup is opaque; appendix A.2 not available"** — The appendix is stripped by the PDF parser; the per-reviewer instructions prohibit penalizing missing appendix content.
- **"LDoA could leak future information for past pandemics"** — The paper explicitly addresses this: "this retrospectively calculated LDoA is never used during inference on the current pandemic, preventing look-ahead bias" (Section 2.2). For past pandemics, using complete historical trajectories to define augmentation ranges is standard and not a leakage issue.
- **"Performance degradation relative to T-DCM directly contradicts the central thesis"** — Overstated. The mean MAE is worse, but the median MAE (arguably more relevant for skewed epidemic data) shows consistent improvement. The real issue is the unexamined mean/median divergence, which is listed as a major weakness above.
- **"Missing related works"** — Per-review rules prohibit penalizing missing citations without external confirmation.
- **"Should use more Forecast Hub models"** — The paper explains why this is infeasible (lack of reproducible code, no early-stage forecast outputs). This is a practical constraint, not a methodological flaw.
- **Formatting, spacing, and typographical concerns** — These are parser artifacts, not author errors.
- **"No testing on a truly novel disease beyond COVID-19"** is retained (above) but demoted from "fatal" to "major" because the paper's historical dataset is limited and a held-out test would significantly reduce training data; it is a genuine limitation but not one that invalidates the existing results.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Expand the external benchmark** to cover a meaningful subset of the 258 locations. The paper already has code for DELPHI and could compare HG-DCM against it (as in the ablation) on all 258 locations in the same format used for Table 2. If external baselines cannot be run at all locations, the claims of "state-of-the-art outperformance" should be scaled back proportionally.

2. **Analyze the catastrophic mean failures explicitly** — identify which locations produce extremely high MAE at 2 and 4 weeks, and discuss whether this is a structural limitation (e.g., a few pathological parameter estimates) or a solvable issue. Consider adding an error analysis figure (e.g., per-location MAE scatter plots) to make the distribution visible.

3. **Clarify the evaluation protocol** — state explicitly how the 258 locations are split between training and testing, whether there is any temporal or spatial overlap, and whether results aggregate across all locations or only held-out ones.

4. **Add an ablation with Batch Normalization** to empirically validate the claim that removing BN is beneficial for cross-pandemic training.

5. **Report results with both mean and median** prominently in the abstract and discussion, and address the divergence transparently.

## Score and Decision

### Calibration Report

All rounds used `calibration_search` over the human-review anchor corpus.

**Round 1 (Bracketing):** Three queries targeting pandemic forecasting / hybrid models at score bands (0–3.5), (3.5–7.5), and (7.5–11). Results confirmed that no topically similar paper resides in the 7.5+ band. The most relevant anchors were:
- CAPE (avg 4.00, reject) — pre-training epidemic forecasters with compartmental prototypes, most topically similar
- EpiDiff (avg 4.40, reject) — hybrid diffusion + mechanistic model for epidemic forecasting
- MORL pandemic policies (avg 3.00, reject) — weaker, less relevant
- BLUE avian flu (avg 2.00, withdrawn) — weaker, less relevant

**Round 1 bracket: 3.5–7.5** (paper clearly above the 2–3 group but below the 8+ group).

**Round 2 (Narrowing):** Two queries focused on the (4.0–5.5) and (3.0–4.5) bands with epidemic forecasting terms. Retrieved CAPE (4.00), EpiDiff (4.40), and a zero-shot forecasting paper (5.00, accept) that is not topically comparable. HG-DCM has a stronger novelty claim than CAPE but a narrower evaluation (1 disease vs 17). Compared to EpiDiff, HG-DCM has clearer methodological novelty but a less comprehensive empirical evaluation.

**Final score: 4.5.** The paper addresses an important problem with a genuinely novel approach, but the evaluation is insufficient to support the strongest claims. The limited external benchmarking (2 baselines, 2 locations), the unexplained mean/median divergence in early cold-start windows, and the absence of a held-out pandemic test all prevent acceptance at the current bar. The core idea has clear promise, but the paper needs substantially stronger evidence before it can be accepted.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>