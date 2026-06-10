## Summary

This paper proposes PE-GQNN, a set of three architectural modifications to the PE-GNN framework (Klemmer et al., 2023) for spatial regression with uncertainty quantification: (1) postponing the τ quantile input to a late-layer concatenation (merging the two-step Kuleshov et al. procedure into a single model), (2) applying the GNN operator to features only rather than to features+positional encodings, and (3) incorporating the mean target value of spatial neighbors (ȳ) as a post-GNN feature. The method is evaluated on three geographic datasets (California Housing, Air Temperature, 3D road) with three GNN backbones (GCN, GAT, GSAGE).

## Strengths

- **Consistent predictive accuracy gains across datasets and backbones.** PE-GQNN achieves lower MSE/MAE than PE-GNN and vanilla GNN on all three datasets and all three GNN layer types. The improvement is often substantial — e.g., on 3D road, PE-GQCN achieves MSE 0.0001 vs PE-GCN's 0.0032 (a ~97% reduction). On California Housing with GSAGE, the full model reduces MSE by 22% and MAE by 19% over PE-GSAGE.

- **Principled avoidance of data leakage when incorporating neighbor target values.** The paper explicitly designs the architecture so that ȳ is introduced *after* the GNN layers, preventing the true target from leaking through message passing (Section 3, lines 154–155, Algorithm 1 Step 12 vs Step 6). This is a concrete architectural safeguard that distinguishes the approach from naive target-smearing.

- **Empirical verification of no quantile crossings.** The paper verifies that "no quantile crossings were observed in any of the PE-GQNN models" across the entire test set (line 293). Coupled with the theoretical guarantee for the special case where τ is at the prediction layer (Eq. 4), this addresses a known failure mode of independent quantile regression networks.

- **Ablation study quantifying each innovation's contribution.** The California Housing experiments (Table 2) decompose the three innovations progressively: PE-GSAGE → +τ → +Structure → full PE-GQSAGE. Each addition improves either accuracy or calibration (e.g., +τ improves MPE/MADECP; +Structure improves MSE/MAE/MPE/MADECP; +ȳ improves all metrics). This provides fine-grained evidence that each design decision contributes independently.

- **Architectural simplification over Kuleshov et al. (2022).** Merging the two-step recalibration process into a single model by postponing τ concatenation to a reduced latent dimension is a genuine architectural insight that eliminates the need for a separate recalibrator and dedicated recalibration training set.

## Weaknesses

### Fatal

None.

### Major

- **No measure of uncertainty or variability reported for any result.** Every metric in every table is a single scalar — no confidence intervals, standard errors, or multiple random seeds are provided. For a paper whose central contribution is about *uncertainty quantification*, this is a significant omission. Neural network training involves random initializations, batching randomness, and hyperparameter sensitivity; without error bars, it is impossible to assess whether the reported improvements are statistically significant or could arise from random variation. This undermines the reliability of the headline claims.

- **SMACNP comparison uses unequal training data proportions, making head-to-head claims difficult to interpret.** SMACNP is trained on 10% of California Housing and 30% of Air Temperature, while PE-GQNN uses 80% in both cases (lines 241, 300). The paper transparently follows the original SMACNP authors' specifications, but this means the comparison does not test which method is better under equal conditions — it tests which is better when one has 2.7–8× more data. Tellingly, SMACNP achieves the lowest MSE on Air Temperature (0.0018 vs PE-GQSAGE's 0.0023) *despite* this data disadvantage. The paper acknowledges this briefly but the phrase "significantly outperforms existing state-of-the-art methods" is too broad.

- **MADECP calibration substantially degrades on Air Temperature, but this is not discussed.** On Air Temperature, PE-GQNN's MADECP ranges from 0.0677 to 0.0785 across backbones, while the simple GCN baseline achieves 0.0334 (Table 3). This means the proposed method's calibration is *worse* than the simplest baseline on this dataset. The paper's narrative focuses on calibration improvements on California Housing but does not analyze this failure case. For a paper about uncertainty quantification, understanding when and why the method's calibration degrades is essential.

### Minor

- **Missing ablation control: PE-GNN augmented with ȳ alone.** The ablation table (Table 2) progressively adds τ, Structure, and ȳ to the baseline. However, there is no "PE-GNN + ȳ" baseline that adds only the neighbor target feature without the quantile or structural changes. Without this control, the MSE improvement attributed to the full PE-GQNN framework cannot be cleanly separated from simply providing the model with a KNN-smoothed version of the target — a strong inductive bias for spatial interpolation.

- **Quantile crossing guarantee does not strictly apply to the actual architecture.** The theoretical guarantee against quantile crossing (Eq. 4) applies when τ is introduced *at the prediction layer* with a monotonic activation. However, PE-GQNN introduces τ at an earlier layer (Step 12–13 of Algorithm 1), followed by additional fully-connected layers. The paper notes this caveat (line 168) and provides empirical verification, but the theoretical framing in the section header ("Quantile crossing") could mislead a casual reader into thinking a stronger guarantee exists.

- **ȳ computation at test time is underspecified.** For predicting at new locations without observed neighbors, the mechanism for obtaining ȳ is not explained. The paper states ȳ was "pre-calculated using the entire training set" (line 211), but it is unclear how this works for test points whose nearest neighbors in geographic space may be other test points rather than training points, and whether this introduces any information leak during evaluation.

- **Claims without supporting evidence.** The abstract claims the method works "without increasing computational complexity" and "applicable beyond spatial data contexts." No runtime measurements are provided to support the complexity claim, and no non-spatial experiments support the general applicability claim.

- **No sensitivity analysis.** Key hyperparameters — k (number of neighbors), embedding dimensions (u, g, s), and the number of Monte Carlo samples d (only d=1 is tested, with no ablation comparing d>1) — are not analyzed. For k=5 in particular, the spatial scale of dependence varies substantially across datasets, and sensitivity to this choice should be reported.

- **No limitations section.** The conclusion (Section 5) presents only strengths. The paper's own results show calibration degradation on one of three datasets, which would naturally belong in a limitations discussion.

### Trivial

None.

## Nice-to-Haves

- An ablation of d=1 vs. d>1 Monte Carlo samples would strengthen the LLN-based justification (line 169) with empirical evidence at finite batch sizes.
- A fair SMACNP comparison with matched training proportions (even if supplementary) would allow cleaner conclusions.
- Runtime (wall-clock) measurements would support the claim of "no increase in computational complexity."
- Sensitivity analysis for the number of neighbors k across datasets.

## Removed Points

These points were flagged but removed from the main review for the reasons stated:

- **"Calibration baselines for GNN/PE-GNN are constructed adversarially by forcing a Gaussian assumption."** This is a standard practice in the literature for comparing non-probabilistic baselines on calibration metrics. The paper transparently describes the approach (line 211). The paper also includes SMACNP as a proper probabilistic baseline. This is not "adversarial" — it is a conventional if imperfect approximation. The comparison is imperfect but not invalid; it is downgraded to a minor weakness above.

- **"The machine used is a consumer laptop, raising questions about hyperparameter tuning."** This is speculative. The paper reports results; the hardware does not invalidate them.

- **"The paper does not provide error bars"** — already in Major weaknesses as a central issue.

- **"Criticism about the LLN argument being only asymptotic"** — the paper itself acknowledges this implicitly, and the core claim stands. Kept as a minor observation in the no-sensitivity-analysis point.

- **"Nitpicks about missing appendix content"** — these are parser-stripped sections; the original submission includes them.

- **Strength Finder's generic strengths** (e.g., "addressed an important problem") — removed as superficial.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the central tension: the paper proposes a method for uncertainty quantification but evaluates it with no uncertainty quantification on its own results (no error bars, no multiple runs), and the calibration claim is clearest on California Housing while degrading on Air Temperature. This gap between what the method promises and how its evidence is presented is the review's main diagnostic finding, not a new insight about the method itself.

## Suggestions

1. **Run all experiments with at least 5 random seeds and report means ± std. dev. or confidence intervals.** Without this, the paper's claims about "significant" improvements are unverifiable, which is especially critical for a UQ paper.

2. **Add a control: PE-GNN + ȳ (without quantile/structural changes).** This isolates whether the accuracy gains come from the quantile/structural innovations or primarily from feeding a spatially smoothed target to the network.

3. **Discuss the Air Temperature MADECP degradation explicitly.** Analyze why PE-GQNN's calibration is worse than a simple GCN on this dataset — this would strengthen the paper's credibility and provide guidance for practitioners.

4. **Either match SMACNP's training proportion or include a supplementary experiment with equal data.** Consider also comparing PE-GQNN with fewer data to match SMACNP's 10%/30% regime.

5. **Qualify the out-of-scope claims** ("applicable beyond spatial data contexts," "without increasing computational complexity") with explicit caveats, or remove them.

## Score and Decision

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>