## Summary
HG-DCM (History-Guided Deep Compartmental Model) addresses the "cold-start" problem in pandemic forecasting, where insufficient early data causes standard epidemiological models to overfit or fail. The framework trains a ResNet backbone (with batch normalization removed) on historical pandemic data (Ebola, SARS, Dengue, Influenza) to predict DELPHI compartmental model parameters, which are then used to generate cumulative case forecasts. The key premise is that macroscopic spread dynamics—shaped by human behavior and public health responses—share universal patterns across biologically distinct pathogens.

## Strengths

- **Well-motivated research question with genuine public health impact.** The cold-start problem is a real and underexplored challenge; the analogy to an experienced epidemiologist's mental library is compelling and the operationalization via cross-disease transfer is principled.
- **New multi-pandemic dataset.** The paper constructs and releases a novel dataset covering COVID-19, Ebola, SARS, Dengue, and Influenza with associated meta-data. This is a concrete artifact that benefits the community beyond the proposed model.
- **Thoughtful design choices backed by reasoning.** Removing batch normalization to avoid distributional shift across pandemics is well-motivated. The window-shift augmentation stopping at the first-wave peak (LDoA) avoids look-ahead bias. The block-masking strategy for the current outbreak mimics real data gaps.
- **Comprehensive ablation at scale.** Comparing HG-DCM vs. DELPHI (no deep learning), CNN (no compartmental model), and T-DCM (no historical data) across 258 global locations with 2/4/6/8-week training windows thoroughly isolates each component's contribution.
- **Interpretable parameter analysis.** The Wilcoxon signed-rank comparisons of inferred DELPHI parameters show HG-DCM produces systematically more conservative (realistic) estimates, and the overshooting analysis in Figure 4 gives qualitative insight into why DELPHI fails.

## Weaknesses

### Fatal
None identified.

### Major

1. **Unexplained mean MAE anomaly in the ablation undermines reliability claims.** Table 2 shows HG-DCM mean MAE at 4 weeks is 110,452.4, which is approximately 10× worse than CNN (11,238.1) and also worse than DELPHI (813,807.8 is worse, but the CNN comparison is damning). The paper does not address this striking regression at all, relying entirely on median MAE to argue for HG-DCM's superiority. This discrepancy strongly suggests extreme outlier behavior or instability in HG-DCM for a substantial fraction of locations, which is precisely the concern for a public health tool. Reporting median while suppressing the mean anomaly misrepresents model stability.

2. **External comparison restricted to only 2 locations (US and Massachusetts).** The paper claims HG-DCM outperforms GradABM and EiNNs, but this comparison is conducted exclusively at two locations "due to limited data accessibility." The abstract and conclusion make broad claims about outperforming state-of-the-art methods, yet the critical comparison is essentially a two-data-point evaluation. For the 4-week US window, EiNNs substantially outperforms HG-DCM (729,091 vs. 2,548,004 MAE)—a result the paper does not discuss, only bolding the better model per window without acknowledging where HG-DCM is significantly worse.

3. **No evaluation on a truly held-out target pandemic.** The entire experimental validation uses COVID-19 as the target disease—the same outbreak whose early data appears in the training objective (Eq. 4). To demonstrate the framework's cross-disease generalization claim, the paper should have held out one historical pandemic (e.g., SARS or Ebola) as a target and trained on the remainder. Without this, it is unclear whether HG-DCM learns universal dynamics or overfits to COVID-19's specific structural features.

### Minor

1. **Hyperparameter β (historical vs. current loss balance) is undisclosed.** The loss function (Eq. 5) gives β as the weight between historical and current pandemic losses—a critical hyperparameter that controls the degree of knowledge transfer—but its value, sensitivity, and selection criterion are never discussed.

2. **T-DCM median MAE worsens with more data**, which is counterintuitive (2 weeks: 2745.8, 8 weeks: 4335.2). This suggests T-DCM is itself unstable and its role as an ablation for "HG-DCM without historical data" is questionable if the isolated model degrades with more information.

3. **Linear interpolation for weekly historical data is used without error quantification.** The paper acknowledges that Ebola and SARS reported weekly, requiring interpolation to daily resolution, but provides no analysis of how interpolation error propagates into learned parameters.

### Trivial
None worth noting.

## Nice-to-Haves
- A leave-one-pandemic-out experiment (e.g., train on Ebola/SARS/Dengue/Influenza, predict SARS) would directly validate the cross-disease transfer claim.
- Uncertainty quantification for predictions, especially critical for early-stage public health decisions.

## Novel Insights
The paper's most genuinely novel contribution is the operational insight that cross-disease transfer of *parameter dynamics* (how transmission rates decay in response to interventions) rather than specific parameter values is the right level of abstraction for generalizing across biologically distinct pathogens. The removal of batch normalization to prevent batch-statistic contamination across pandemics is a minor but non-obvious architectural insight. The LDoA-based augmentation stopping rule elegantly prevents look-ahead bias while maximizing sample diversity from historical data.

## Suggestions
- **Address the mean MAE anomaly directly.** Identify which locations drive HG-DCM's large mean MAE at 4 weeks, and either improve stability for those cases or explicitly characterize the failure mode.
- **Run GradABM and EiNNs on a larger set of locations** (even 10–20) to move beyond the two-location comparison, or clearly reframe claims to avoid overstating generality.
- **Add a leave-one-pandemic-out experiment** to validate the cross-disease claim without COVID-19 in the target.
- **Report both mean and median MAE together** and discuss the gap explicitly as a signal of variance/stability.

## Score and Decision
The research question is important and the architectural framing is principled. The ablation at 258 locations and the new dataset are genuine contributions. However, the unexplained 10× mean MAE regression at 4 weeks is a significant unaddressed reliability concern, the external baseline comparison covers only 2 locations, and the absence of any held-out target pandemic leaves the core cross-disease generalization claim unvalidated. These are substantive methodological gaps that weaken confidence in the paper's central claims.

MY FINAL SCORE: <score>4</score>
MY FINAL DECISION: <decision>Reject</decision>