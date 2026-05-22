Now I have a clear picture. Let me compile the final review.

## Summary of Calibration

**Round 1 bracket:** Clearly above weak anchors (2–3 range: poor papers on TB prediction, SEIR optimization), clearly below strong anchors (8 range: state-space models, neural ODEs with full experimental rigor). Initial bracket: 3.5–7.5.

**Round 2 narrowing:** The closest topical anchor is **PEMs** (4.75, Reject) — pre-training on multiple diseases with SSL, zero-shot COVID evaluation. HG-DCM is topically similar but experimentally weaker: no held-out disease evaluation, only 2 baseline comparison locations, confusing ablation results. The paper is below PEMs. **ROSE** (5.75, Reject) and **Generalizing Dynamics** (5.25, Reject) are stronger papers experimentally. HG-DCM sits below all of these. Final score: **4.5**.

---

## Final Review

## Summary

This paper proposes HG-DCM, a framework that trains a neural network to predict parameters of a compartmental model (DELPHI) using data from multiple historical pandemics (Ebola, SARS, Dengue, seasonal influenza) alongside early data from a current outbreak (COVID-19). The goal is to improve early-stage ("cold-start") forecasting when current-outbreak data is too sparse to calibrate standard compartmental models. The core idea — cross-disease temporal transfer for parameter prediction — is well-motivated and addresses a genuine problem.

## Strengths

- **Novel and well-motivated framing of cross-disease temporal transfer for compartmental parameter prediction.** The paper operationalizes the idea that macroscopic spread dynamics (driven by human behavior and response) are shared across biologically distinct pandemics. Using a neural network to predict DELPHI parameters from historical outbreak curves is a sensible approach that combines interpretability with the flexibility of deep learning. This framing is clearly articulated in the introduction and related work.

- **Principled architectural adaptation for domain shift.** The removal of Batch Normalization layers (Section 2.1) is justified by the statistical differences in batch statistics across pandemics. This is a concrete, non-obvious design choice that addresses a real technical problem in cross-disease training, and it distinguishes the architecture from generic ResNet backbones.

- **Demonstrated reduction in overshooting behavior.** Figure 4 shows that HG-DCM produces markedly fewer extreme overpredictions (cumulative cases exceeding 5× observation) than the standard DELPHI model, especially with 2–6 weeks of training data. The U.S. 8-week example (Figure 4b) visually illustrates how historical guidance prevents the blow-up that DELPHI suffers. This is the paper's most concrete empirical finding.

- **Interpretable parameter inference.** The parameter analysis (Section 3.2.3, Figure 5) shows statistically significant differences between HG-DCM and DELPHI parameter distributions, with HG-DCM producing more conservative estimates. While this does not prove the parameters are "correct" (no ground truth exists), it does show that historical guidance changes the model's behavior in a systematic and plausible direction, which strengthens the interpretability claim.

## Weaknesses

### Major

- **Main baseline comparison is limited to only 2 locations.** Table 1 compares HG-DCM against GradABM and EiNNs on only the United States and Massachusetts. The paper honestly states this is due to data/code availability constraints for the baselines, but conclusions about "consistently and significantly outperforming state-of-the-art methods" (abstract) are drawn from an extremely thin sample. On these 2 locations, EiNNs actually beats HG-DCM on 2 of 8 cells (US 4-week: 729K vs 2.5M; MA 6-week: 25.7K vs 39.9K), undercutting the "consistent" claim.

- **Confusing and incompletely explained ablation results.** Table 2 shows that at 4 weeks of training data, the end-to-end CNN baseline has **mean MAE = 11,238 vs HG-DCM's mean MAE = 110,452** — a factor of ~10× worse for HG-DCM. Yet the paper claims "CNN generally underperforms HG-DCM across all training horizons," selectively reporting only median MAE (where HG-DCM is indeed better: 1,771 vs 2,302). The mean-vs-median discrepancy suggests HG-DCM has catastrophic outliers on some locations that are not acknowledged or explained. The 4-week mean MAE for HG-DCM (110K) is also anomalously high relative to its 2-week mean (18.6K) and 6-week mean (7.1K), which is inconsistent with the usual pattern that more training data reduces error. The paper offers no analysis of this.

- **The "258 global locations" claim from the abstract is never connected to a specific results table.** The ablation study (Table 2) never states how many locations were included, what their geographic distribution is, or how mean/median MAE is computed across them. The abstract promises evaluation at scale; the paper does not deliver a clear accounting of that scale in the experimental section.

- **The T-DCM ablation removes both historical pandemic data and metadata simultaneously.** This design cannot isolate whether the improvement comes from cross-disease temporal transfer or simply from having richer metadata features. A cleaner ablation (e.g., HG-DCM with historical data but no metadata, or with metadata but no historical data) is needed to support the paper's central claim about knowledge transfer.

### Minor

- **No leave-one-pandemic-out experiment.** The paper's core claim is that historical pandemics help forecast a novel one, but COVID-19 data is included in training alongside historical pandemics. While this reflects a realistic use case (you would have early COVID data in a real outbreak), a true test of cross-disease generalization would hold out one pandemic entirely. For example, training on all non-COVID pandemics plus 0 weeks of COVID data would directly test whether the historical prior suffices alone. Its absence leaves the "transfer learning" framing undersupported.

- **Parameter inference analysis lacks ground truth.** Figure 5 shows that HG-DCM's parameters are statistically different from DELPHI's and more conservative, but there is no way to verify whether they are more *accurate* — the compartmental parameters are latent even in the true system. The interpretation is plausible but speculative.

- **Hyperparameter values (α, β) not stated in the main text.** The loss weighting hyperparameters that control the influence of past pandemics vs. current pandemic are critical for understanding the method and are not reported.

### Trivial

- None that are worth listing.

## Nice-to-Haves

- A sensitivity analysis on the LDoA threshold (25% of global maximum) used for data augmentation.
- An ablation comparing HG-DCM with vs. without Batch Normalization to justify the removal experimentally.
- Reporting confidence intervals or statistical significance tests for the ablation study comparisons.

## Removed Points

- **"Evaluation does not demonstrate cross-disease transfer" (harsh critic #1, as stated).** The critic claimed the experiment is fatally flawed because COVID data is in training. This is an overstatement: the setup tests whether *adding* historical data improves over models that only use COVID data (DELPHI, T-DCM, CNN). COVID data inclusion reflects the real-world scenario. Demoted from fatal to minor concern about missing leave-one-out experiment.
- **"Main comparative evaluation is anecdotal" (harsh critic #2).** The limitation is real but the paper acknowledges it; the critic's framing as "cherry-picked" is unwarranted given the stated constraint. Kept as major weakness (first bullet) but reframed.
- **"Conflates cross-disease transfer with multi-location pooling" (harsh critic #3).** Partially valid, but addressed by retaining the T-DCM ablation concern (third major weakness). The critic's claim that the paper "does not disentangle" is correct; this is reflected in the revised T-DCM weakness.
- **"BN removal not experimentally justified."** Nice-to-have, not a weakness.
- **"LDoA threshold arbitrary, no sensitivity analysis."** Nice-to-have.
- **"Overshoot definition arbitrary."** 5× is a reasonable threshold; not a weakness.
- **"CNN comparison in overshoot is uninformative."** Including CNN in the overshoot comparison is informative as a lower-bound reference.
- **"EiNNs beats HG-DCM on some cells."** Already reflected in the revised weakness about the Table 1 comparison being limited.
- **Strength: "Architectural modification (BN removal) tested implicitly."** The implicit testing through overall performance is insufficient to call this a strength; moved here.
- **Strength: "Tailored data augmentation."** Sensible but standard practice for time series; not a distinctive strength.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add a leave-one-pandemic-out experiment.** Train on Ebola + SARS + Dengue + Influenza (zero COVID data) and evaluate on COVID. This directly tests whether cross-disease transfer works without any current-disease supervision. Even if performance is poor, reporting it honestly would strengthen the paper's claims about what the method can and cannot do.

2. **Expand the ablation study.** Add variants that isolate the contribution of (a) historical pandemics alone (no metadata), (b) metadata alone (no historical pandemics), and (c) larger training set from the same pandemic. Report the number of locations in every table. Include per-location error distributions, not just aggregate mean/median.

3. **Explain the 4-week mean MAE anomaly.** The spike in HG-DCM's mean MAE at 4 weeks (110K vs 18.6K at 2 weeks and 7.1K at 6 weeks) needs explanation. Is this a data artifact, an evaluation bug, or genuine behavior? If the latter, it undermines the "more training data helps" narrative.

4. **Add standard compartmental baselines.** If the COVID-19 Forecast Hub models cannot be run, at least compare against per-location SIR/SEIR fits and a simple pooled compartmental model. This would ground the comparison and make the benefits of the neural mapping clearer.

## Score and Decision

**Score: 4.5**

**Decision: Reject**

**Calibration report:** The closest topical anchor is **PEMs** (avg 4.75, Reject — pre-trained epidemic time-series models with SSL on multiple diseases, zero-shot COVID evaluation). HG-DCM is experimentally weaker: no zero-shot evaluation, only 2 baseline locations, confusing ablation results. Other anchors in the mid-range — **ROSE** (5.75, Reject), **Generalizing Dynamics** (5.25, Reject) — have more rigorous experimental evaluations. HG-DCM is below these. The paper's genuine novelty and sound framing are acknowledged, but the experimental gaps are too significant to support the central claims at an acceptance level.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>