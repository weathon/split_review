Now I have all the data I need. Let me write the consolidated review.

## Summary

This paper introduces HG-DCM, a framework that combines deep learning (CNN-based parameter predictor) with a compartmental model (DELPHI) to forecast pandemics during the data-scarce early stages. The core innovation is cross-disease temporal transfer learning: the neural network is trained on historical pandemic data (Ebola, SARS, Dengue, seasonal influenza) to learn universal dynamics that can guide parameter estimation for a new pandemic (COVID-19) when its own data is minimal. The architecture preserves the interpretability of compartmental models while using historical data as a regularizer against overfitting.

## Strengths

1. **Novel and well-motivated architecture for an important problem.** The idea of cross-disease temporal transfer in pandemic forecasting is genuinely novel and practically significant. The hybrid design — using a CNN to predict DELPHI parameters rather than directly forecasting case counts — is a clean architectural choice that preserves epidemiological interpretability. As the paper notes, this is the first framework to systematically leverage data from multiple prior pandemics to forecast a newly emerging one (Section 1, lines 33-35).

2. **Controlled ablation cleanly isolates the contribution of historical guidance.** The comparison of HG-DCM against T-DCM (same architecture but trained without historical data) provides direct evidence that the historical-data component improves forecasting. Median MAE improves from 2,745.8 (T-DCM) to 2,231.1 (HG-DCM) at 2 weeks, and from 2,799.1 to 1,770.9 at 4 weeks (Table 2). This controlled comparison is the strongest evidence for the paper's core thesis.

3. **History guidance substantially reduces overshooting, a known failure mode.** Figure 4 quantifies this clearly: DELPHI exhibits dozens of overshoot events across training windows while HG-DCM shows nearly zero in most settings. This demonstrates that historical regularization stabilizes the compartmental dynamics in a practically meaningful way, addressing a limitation explicitly identified in the paper's motivation.

4. **Parameter inference yields more stable and interpretable estimates.** Figure 5 and the Wilcoxon signed-rank tests show that HG-DCM produces narrower interquartile ranges for DELPHI parameters compared to standard DELPHI fitting. This provides mechanistic interpretability beyond pure forecast accuracy and supports the claim that historical data acts as a regularizer.

5. **Thoughtful data augmentation with anti-leakage design.** The window-shift augmentation for past pandemics (stopping at the LDoA, which is explicitly never used during inference on the current pandemic) and the masking augmentation for the current pandemic are carefully designed to prevent look-ahead bias (Section 2.2). This strengthens the reliability of the reported gains.

## Weaknesses

### Major

1. **Overclaiming on the CNN comparison — the paper's text contradicts its own table.** The paper states: "CNN generally underperforms HG-DCM across all training horizons. The performance gap is largest in the early stage (2–4 weeks of training data), where HG-DCM's integration of historical knowledge and compartmental dynamics yields markedly lower forecasting error (Table 2)" (line 192). However, Table 2 shows that on **mean MAE**, CNN substantially **outperforms** HG-DCM at 2 weeks (15,600 vs 18,603) and at 4 weeks (11,238 vs 110,452 — an order of magnitude difference). The paper appears to be selectively citing median MAE without qualification, and the claim about the gap being "largest in the early stage" where HG-DCM "yields markedly lower error" is factually incorrect for the mean metric. This is not a minor imprecision — it is a mismatch between the paper's claims and its own evidence. The authors must either report transparently on both metrics, explain the mean/median discrepancy (e.g., heavy-tailed failures from HG-DCM), or adjust their claims.

2. **External validation against SOTA methods is extremely thin.** The only comparisons against non-ablation baselines (GradABM, EiNNs) are on two locations — the entire US and Massachusetts — and even there, EiNNs wins on two of eight tasks (Table 1: 4-week US, 6-week Massachusetts). The paper acknowledges this limitation (lines 142-143) but still draws broad conclusions: the abstract claims HG-DCM "consistently and significantly outperforms state-of-the-art methods." Evaluating on 258 locations in the ablation but only 2 for external SOTA comparison is a significant gap between evidence and claim. At minimum, the authors should acknowledge that the external validation is preliminary and that the strongest evidence comes from the controlled ablation against DELPHI and T-DCM.

### Minor

3. **Mean vs. median MAE gap suggests undiagnosed catastrophic failures.** At 4 weeks, HG-DCM's mean MAE (110,452) is ~62× its median MAE (1,770.9), while CNN's ratio is ~5× (11,238 mean vs 2,302 median). This suggests HG-DCM produces occasional extreme errors that are not discussed. Understanding what causes these failures (specific metadata profiles, short time series, particular diseases) and how to mitigate them would strengthen the paper's practical utility.

4. **DELPHI model fit on historical pandemics is unexamined.** The compartmental backbone (DELPHI) was designed for COVID-19 with states for hospitalization, quarantine, and under-detection that may not be meaningful for Dengue, seasonal influenza, or SARS. The paper provides no diagnostic — e.g., training loss on historical trajectories or retrospective validation — to show that DELPHI can adequately represent these diseases. If DELPHI systematically mis-represents historical diseases, the learned "universal patterns" could be artifacts. The paper's argument that human-driven dynamics are universal is plausible, but some evidence of model fit on historical data is needed.

5. **MAPE in the loss function is undefined at zero case counts.** Equations 3 and 4 use a MAPE term (|C_{ij} − Ĉ_{ij}| / C_{ij}) which is unbounded when C_{ij}=0, as can occur in early days. The paper does not discuss how this is handled (e.g., adding a small epsilon, skipping zero-valued points). This is a straightforward fix but should be documented.

6. **Hyperparameter sensitivity not discussed.** The loss weights α (MAPE vs MAE balance) and β (past vs current pandemic balance) are introduced but their values, tuning procedure, and sensitivity are not reported. Since β directly controls how much influence historical data has, this is important for reproducibility.

### Trivial

- The description of the ResNet architecture (number of layers, filter sizes, kernel dimensions) is not provided in the main text (possibly in the appendix which was stripped).
- No error bars or confidence intervals reported for any results (Tables 1 and 2 show only point estimates).

## Nice-to-Haves

- The paper would be substantially strengthened by testing on a held-out pandemic (e.g., train on all diseases except SARS, then test on SARS) to directly measure cross-disease generalization rather than conflating it with within-disease transfer on COVID-19.
- Uncertainty quantification (prediction intervals) would improve practical utility for decision-makers.
- Training/inference time comparison would help assess real-time deployment feasibility.

## Removed Points

These points from the inputs are removed with justification:

- **"Related work is thin on citations"** / **"misses related works"** — Generic criticism. The reviewer asserts missing citations without specific evidence. Removed per instructions to not mention missing related works without external sources.
- **"Figure 3 is difficult to read"** — Formatting nitpick (figure display issues are parser artifacts).
- **"Wilcoxon test only shows difference, not accuracy"** (harsh critic on parameter inference) — While true that the test shows difference rather than accuracy, the paper's claim about the parameters being "more conservative and realistic" is supported by the narrower IQRs and the overshoot reduction evidence. This is a minor conceptual point, not a flaw. Removed.
- **"The model has only been tested on COVID-19 as target"** — The paper explicitly scopes itself to COVID-19 as the target. Criticizing it for not testing on other target pandemics is scope creep. Moved to nice-to-have as a suggestion for future work.
- **"Potential data leakage from metadata"** (harsh critic on limitations) — Speculative. The paper describes the metadata and the LDoA anti-leakage design. No concrete evidence of actual leakage is presented. Removed.
- **Strength Finder strengths about the problem being "important" or "compelling"** — Generic/superficial. Only strengths with specific evidence are retained.

## Novel Insights

None beyond the paper's own contributions. The two reviews largely reinforce each other: the strength finder correctly identifies that the T-DCM ablation and overshoot reduction are the strongest evidence for the core claim, while the harsh critic correctly identifies that the overclaiming on the CNN comparison and thin external validation are the paper's most significant weaknesses. The main novel observation from synthesis is that the mean/median discrepancy at 4 weeks (ratio ~62× for HG-DCM vs ~5× for CNN) is a red flag that both reviews touched on indirectly but neither fully articulated as a diagnostic concern about the model's stability.

## Suggestions

1. **Correct the overclaiming in Section 3.2.2.** Qualify the CNN comparison to acknowledge that on mean MAE, CNN outperforms HG-DCM at 2 and 4 weeks. Explain why median is the preferred metric, discuss the outlier issue, and present both metrics transparently.
2. **Add a held-out pandemic experiment.** Train on all historical diseases except one, then test on the held-out one, to directly measure cross-disease generalization.
3. **Diagnose the mean/median gap.** Investigate what causes HG-DCM's occasional very large errors at 4 weeks and report failure cases.
4. **Report DELPHI fit statistics on historical pandemic data** (e.g., training loss convergence, retrospective forecasts) to validate that the model backbone is appropriate for the source domain.

## Score and Decision

**Round-1 Bracket:** Based on calibration search, the most comparable anchor is PEMs (avg 4.75), with other relevant anchors at 5.25, 5.50, and 5.75. The strong anchors (7.5+) are not in the same problem area (general time series foundation models). The initial bracket is **[4.5, 5.75]**.

**Round-2 Narrowing:** Within this bracket, the paper was compared to:
- **PEMs (4.75)**: Most directly comparable — cross-disease epidemic pre-training. HG-DCM has more architectural novelty (hybrid deep compartmental vs. SSL pre-training) but a more serious overclaiming issue. HG-DCM's external validation is thinner. **HG-DCM is slightly stronger than PEMs → around 5.0.**
- **RePST (5.50)**: Physics-aware spatio-temporal forecasting. RePST has more comprehensive experiments but its scores are very split (8, 3, 5, 6). HG-DCM is not as strong as the average of RePST due to the overclaiming issue.
- **ROSE (5.75)**: General time series pre-training with comprehensive benchmarks and ablations. HG-DCM addresses a more specific real-world problem but is less polished in presentation and evidence. **HG-DCM is weaker than ROSE.**

**Final Score:** Given the paper's genuine novelty and the clear T-DCM ablation showing the value of historical data, balanced against the overclaiming on the CNN comparison and thin external validation, the paper sits near the lower end of the mid-range bracket. It is borderline — interesting ideas with significant presentation and evidential issues that need correction before the paper's claims can be fully trusted.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>