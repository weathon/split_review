Here is my final consolidated review.

---

## Summary

This paper introduces HG-DCM, a framework that uses a neural network to predict compartmental model (DELPHI) parameters by learning from multiple historical pandemics (Ebola, SARS, Dengue, seasonal influenza) and transferring this knowledge to improve early-stage COVID-19 forecasting. The core idea—cross-disease temporal transfer via learned parameter prediction—is novel and addresses a genuine problem in pandemic response. An ablation study across 258 global locations shows that incorporating historical data consistently reduces forecasting error compared to DELPHI (median MAE reduction of 38.2% at 2 weeks) and a deep-learning-only variant (T-DCM). However, the evaluation has significant gaps: the main SOTA comparison is limited to 2 locations, cross-disease transfer is validated on only one target disease (COVID-19), and key design choices lack ablation. The paper's strong claims are not fully supported by the current evidence.

## Strengths

1. **Novel cross-disease temporal transfer.** The paper is the first to systematically leverage data from multiple biologically distinct past pandemics (Ebola, SARS, Dengue, seasonal flu) for cold-start forecasting of a new pathogen. This goes beyond spatial transfer or single-outbreak methods (Section 1, Section 1.1).

2. **Solid ablation isolating the contribution of historical data.** The T-DCM ablation (same architecture but without historical data) consistently underperforms HG-DCM across all settings in median MAE (Table 2). The DELPHI comparison across 258 locations shows that HG-DCM reduces median MAE by 38.2% (2 weeks) to 32.4% (4 weeks) and strongly reduces overshooting events (Figure 4). This provides credible evidence that historical data helps.

3. **Construction of a new multi-pandemic dataset.** The authors compiled and cleaned a dataset spanning COVID-19, Ebola, SARS, Dengue, and seasonal influenza with metadata, filling a gap in available public resources for this type of cross-disease learning (Section 3.1.1).

4. **Interpretable parameter inference with statistical validation.** HG-DCM produces more stable parameter distributions than DELPHI, with statistically significant differences (Wilcoxon, p<0.05). The parameter analysis provides a concrete diagnostic tool beyond pure black-box forecasting (Section 3.2.3, Figure 5).

5. **Careful data augmentation strategy.** The window-shift and masking augmentations (Section 2.2) are thoughtfully designed to increase training diversity without look-ahead bias during inference.

## Weaknesses

### Fatal
None.

### Major

1. **Cross-disease transfer is validated on only one target disease (COVID-19).** The paper's central premise is that training on historical pandemics enables forecasting of *any* novel pathogen. Yet every experiment targets COVID-19. There is no leave-one-disease-out experiment where, e.g., SARS is held out and treated as the "novel" disease while training on COVID-19, Ebola, Dengue, and flu. Without this, it is impossible to know whether the method works for arbitrary new diseases or only happens to transfer to COVID-19 (which may have similar transmission dynamics to seasonal flu). This fundamentally limits the generality of the core claim.

2. **Main SOTA comparison is restricted to 2 locations.** Table 1 compares HG-DCM against GradABM and EiNNs on only the United States and Massachusetts. The paper justifies this by citing data/code availability for baselines, but for a claim as strong as "consistently and significantly outperforms state-of-the-art methods," this is too thin. The ablation study (Table 2) covers 258 locations, but it only compares against DELPHI, CNN, and T-DCM—not against the external SOTA methods. Without expanding the SOTA comparison to more locations, the "state-of-the-art outperformance" claim is unsubstantiated.

3. **Missing simple baselines.** The paper does not compare against standard lightweight models such as ARIMA, exponential growth, or a simple SIR model fit only on current data. These baselines are critical for isolating whether the benefit comes from historical data or simply from having any model at all. The paper dismisses the COVID-19 Forecast Hub models as lacking early-stage outputs, but ARIMA and SIR can be fit on 2–8 weeks of data with minimal effort and require no historical data.

4. **Inconsistent comparison against CNN.** In Table 2, CNN has substantially *lower* mean MAE than HG-DCM at 2 weeks (15,600 vs 18,603) and especially at 4 weeks (11,238 vs 110,452, a ~10× gap). The paper says "CNN generally underperforms HG-DCM across all training horizons" — this is misleading. The claim is only true for *median* MAE, not mean. The enormous gap in mean MAE at 4 weeks suggests that HG-DCM produces catastrophic failures at some locations that are not discussed. The paper should report both mean and median honestly and explain the outlier behavior.

### Minor

5. **DELPHI's suitability for non-respiratory diseases is not discussed.** The DELPHI compartmental model was designed for COVID-19-like respiratory transmission with explicit intervention modeling. Training it on Dengue (vector-borne) or Ebola (contact-transmitted) via ODE solves may produce unrealistic parameter estimates that corrupt the learned representations. The paper neither discusses nor controls for this mismatch.

6. **Parameter inference analysis lacks ground truth.** Section 3.2.3 claims HG-DCM parameters are more "conservative" and "realistic" than DELPHI's, but no ground-truth parameters exist for COVID-19 at early stages. Lower infection and death rates could simply reflect bias induced by historical pandemics (which had lower severity), not increased accuracy. The analysis is interesting but speculative.

7. **No ablation of batch normalization removal.** The paper motivates removing BN layers due to domain shift between pandemics (Section 2.1) but provides no experiment confirming this improves transfer performance. Similarly, the masking augmentation and metadata contributions are not ablated.

8. **No discussion of how training/validation splits handle window-shift augmentation.** The window-shift augmentation generates highly overlapping training samples (shifting by one day). The paper should clarify whether cross-validation splits are performed on entire outbreaks (non-overlapping) or on individual shifted windows, to rule out information leakage in hyperparameter selection.

### Trivial

- The overshoot analysis (Figure 4a) shows raw counts of overshooting predictions, but without normalizing by the number of locations analyzed per setting, it is hard to compare across training horizons.

## Nice-to-Haves

- A sensitivity analysis showing which historical pandemics contribute most to the transfer, or whether performance degrades when training on only one historical disease (e.g., seasonal flu only).
- Real-time (out-of-sample) evaluation where the model is retrained as each new week of data arrives.
- Goodness-of-fit of the DELPHI model on non-COVID historical training data to verify that the compartmental model provides a reasonable signal.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"If metadata includes disease identifier, the network could simply learn a lookup table instead of universal patterns"** — This speculates about the content of the appendix (which was removed by the parser). The paper states the metadata list is in Section A.1, which cannot be verified. Speculation about removed appendix content should not factor into the evaluation.
- **"The narrative of consistent outperformance is not supported"** — The paper says "consistently achieves lower MAE in most tasks" (emphasis on "most"). HG-DCM wins 6 of 8 comparisons in Table 1. This is a reasonable characterization. The single loss at 4-weeks US is notable but does not contradict "most tasks."
- **"Window-shift augmentation risks severe label leakage: adjacent windows from the same outbreak share almost all future data, inflating apparent training accuracy"** — Leakage of this form would affect training accuracy but not generalization to the held-out target disease (COVID-19). However, it could affect hyperparameter selection if splits are done per-window rather than per-outbreak. Moved to Minor with reduced severity.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface any perspective that the paper itself does not already articulate or implicitly acknowledge.

## Suggestions

1. **Add leave-one-disease-out validation.** Hold out each historical disease (Ebola, SARS, Dengue, flu) in turn, train on the rest plus COVID-19 data, and report forecasting error on the held-out disease. This is the single most important missing experiment and directly validates the core claim of cross-disease transfer.

2. **Expand SOTA comparison to at least 10–20 locations** from the 258-location ablation pool. Even if GradABM and EiNNs code cannot be run on all locations, add ARIMA, Prophet, and simple SIR as baselines that any location can support.

3. **Correct the misleading CNN comparison.** The claim that "CNN generally underperforms HG-DCM across all training horizons" should be qualified to specify that this holds for median MAE, while noting that mean MAE at 2 and 4 weeks favors CNN. Analyze and explain the high-variance behavior of HG-DCM at 4 weeks (mean MAE ~110K vs CNN's ~11K).

4. **Ablate the BN removal** with a version of HG-DCM that retains batch normalization, and **ablate metadata** by running HG-DCM without metadata features.

5. **Tone down the language.** Replace "establishes a new paradigm" and "consistently and significantly outperforms state-of-the-art methods" with more measured claims that reflect the limited evaluation scope.

---

## Score and Decision

### Calibration Anchors

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `/home/wg25r/review_agent/human_reviews_2026/5veGth37O2.md` (CAPE) | 4.00 | Very similar topic (pre-training epidemic forecasters from historical data). CAPE evaluates across 17 diseases (more comprehensive) but was rejected due to novelty concerns. HG-DCM has stronger core novelty but weaker evaluation breadth. Similar tier. |
| `/home/wg25r/review_agent/human_reviews_2026/JZp0GcNjH8.md` (EpiDiff) | 4.40 | Epidemic forecasting with hybrid model. Mixed reviews (4,6,2,2,8). Comparable quality and contribution level. |
| `/home/wg25r/review_agent/human_reviews_2026/G5zJaSxMGN.md` (Tabular Pretraining) | 4.00 | Well-executed empirical audit paper, rejected. Different topic but similar rigor level. |
| `/home/wg25r/review_agent/human_reviews_2026/ZOLUTSU5gk.md` (SarSim) | 5.00 | Time series forecasting paper, accepted as poster. More polished experiments but different topic. |
| `/home/wg25r/review_agent/human_reviews_2026/syfWdclGE1.md` (δ-Adapter) | 6.00 | Time series post-processing, accepted. Stronger theoretical grounding and more comprehensive experiments. |
| `/home/wg25r/review_agent/human_reviews_2026/iAPSx90gwJ.md` (MOIRAI Theory) | 5.33 | Theory paper on time series transformers, accepted. Rigorous theoretical analysis. |
| `/home/wg25r/review_agent/human_reviews_2026/hgj1LQmD09.md` (BLUE) | 2.00 | Weak paper on avian influenza forecasting, withdrawn/rejected. HG-DCM is substantially stronger. |
| `/home/wg25r/review_agent/human_reviews_2026/qckiBWmodZ.md` (MORL) | 3.00 | Pandemic intervention policy paper, rejected. Comparable to lower-bound anchor. |

**Reasoned score:** HG-DCM introduces a genuinely novel idea (cross-disease temporal transfer for pandemic forecasting) that is well-motivated and has plausible initial evidence. The ablation study across 258 locations provides reasonable support for the claim that historical data helps. However, the evaluation has significant gaps: the SOTA comparison is limited to 2 locations, cross-disease transfer is validated on only COVID-19, simple baselines are missing, and the reporting against CNN is misleading. Compared to the most similar anchor (CAPE, 4.00, rejected), HG-DCM has stronger novelty but weaker evaluation breadth. On balance, the paper is a middle-of-the-distribution submission with real contributions but insufficient evidence for its strongest claims. It is below the acceptance threshold for ICLR but could be viable after substantial revisions.

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>