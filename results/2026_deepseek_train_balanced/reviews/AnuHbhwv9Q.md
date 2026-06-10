## Summary

This paper provides a theoretical analysis of OLS regression under covariate shift, identifying a phenomenon called "Spectral Inflation" where eigenvectors with small training variance can dominate at test time. The authors propose SpAR (Spectrally Adapting Regression), a post-processing method that uses unlabeled test data to identify and project out such problematic eigenvectors from the last layer of a neural regressor. The theoretical contribution—a clean closed-form characterization of OOD risk in terms of eigenspectra, plus an optimal projection guarantee—is genuine and well-presented. The empirical evaluation shows consistent but small improvements across synthetic, tabular, image, and PovertyMap-WILDS datasets.

## Strengths

- **Closed-form OOD risk characterization (Theorem 1).** Equation (4) expresses the expected OOD squared error as an explicit double-sum over the eigenspectra of source and target data, giving a concrete mechanism ("Spectral Inflation") for why OLS fails under covariate shift. This goes beyond generic distribution-shift bounds to provide an interpretable, causal explanation.

- **Optimal projection guarantee (Theorem 3 and Corollary).** The paper proves that the projected regressor using the optimal set S\* achieves strictly lower expected OOD loss than *any* other projected regressor (including the original pseudoinverse). This is a non-trivial result: the method can only improve OOD performance, and the condition for eigenvector selection (Var ≥ Bias) is precisely derived.

- **Principled chi-squared selection rule with asymptotic guarantees (Proposition 1, Lemma 1).** The derivation of a closed-form inclusion probability using the Marcum Q-function, with proven tail behavior (inclusion probability → 0 when Bias ≫ Variance and → α when Variance ≫ Bias), provides a theoretically sound decision rule rather than a heuristic threshold.

- **Consistent improvements across all settings without tuning.** SpAR improves (or matches) performance over every base method (ERM, C-Mixup, DeepCORAL, DANN) on every dataset tested—all 10/10 comparisons show improvement in the same direction—with a single fixed α = 0.999 and no dataset-specific tuning. This breadth demonstrates robustness beyond cherry-picked settings.

- **Adaptivity without degradation (Experiment 4).** When there is no covariate shift, SpAR preserves the ERM performance (1.68 ± 1.15, same as ERM), while PCR degrades catastrophically (804 ± 13). This cleanly demonstrates that the method does not blindly remove principal components but adapts based on the actual shift.

## Weaknesses

### Fatal

None.

### Major

- **Empirical improvements on real data are small and individual comparisons have overlapping standard deviations.** On the image datasets (Table 2), every SpAR-vs-baseline comparison has overlapping error bars (e.g., RCF-MNIST ERM: 0.155±0.006 → 0.154±0.006; ChairAngles DeepCORAL: 5.978±0.243 → 5.839±0.259). On PovertyMap (Table 3), the same holds (ERM r_wg: 0.497±0.099 → 0.512±0.092; C-Mixup r_wg: 0.489±0.045 → 0.515±0.091). The paper states SpAR "can significantly improve worst-group performance" (line 491), but no statistical tests (paired or otherwise) are provided. With n=10 seeds, paired comparisons could well show significance, but this is not reported. The claim of "significant" improvement is not supported by the data as presented. The paper's empirical contribution would be more honest if framed as "directionally consistent small improvements" rather than "significant" improvements.

### Minor

- **Tabular data results (Figure 3) are reported only as a bar chart with no numerical values.** The reader cannot assess the magnitude of improvement or whether these results suffer from the same noise-level issue as the image experiments. For a central experimental result, numerical reporting is expected.

- **The paper acknowledges the OLS-to-neural-network gap (lines 286–288) but does not discuss how shifting representations undermine the theoretical guarantees.** The theory assumes the last-layer weight is the OLS/pseudoinverse solution, and that the representations themselves do not shift. In practice, the frozen encoder's representations *will* shift under covariate shift, and nothing in the theory accounts for this. The paper would be stronger by explicitly discussing under what representation properties (e.g., bounded encoder Lipschitz constant) SpAR's guarantees approximately transfer.

- **No analysis of which eigenvectors SpAR selects on real datasets.** The theory tells a clear causal story (Spectral Inflation → eigenvectors with high Var/Bias ratio are projected out), but the experiments never verify this mechanism on real data: how many eigenvectors are selected, which singular values correspond to them, and whether the selected directions align with known spurious features or the spectral inflation documented in Figure 2. This weakens the link between theory and experiments.

- **No discussion of what happens when the assumption Rows(Z) ⊆ Span(Rows(X)) is violated** (Theorem 1 assumption). In high-dimensional settings with deep representations, test data may have components outside the training data's row space. This is a natural concern that goes unaddressed.

- **The computational cost claim (line 251) is vague.** "Slightly less computationally expensive than simply performing inference" is not quantified. Given that SVD is O(min(N,D)ND), which can be non-trivial for high-dimensional representations, a more precise characterization would be helpful.

### Trivial

None.

## Nice-to-Haves

- A sensitivity analysis varying the severity of covariate shift (e.g., degree of spectral mismatch) would strengthen the empirical validation.
- Reporting paired differences or confidence intervals on the improvement (Δ = SpAR − baseline) for each seed would clarify whether the improvements are statistically meaningful despite overlapping univariate error bars.

## Removed Points

These points were flagged during review but do not survive verification:

- **"Table 4's comparison against in-processing methods is likely unfair"**: The baselines in Table 5 (DANN, DeepCORAL, AFN, RSD, DARE-GRAM) are cited from the published WILDS leaderboard results (Sagawa et al., 2022), not re-implemented by the authors. The fact that some DA methods underperform ERM on PovertyMap is a known property of this benchmark, not evidence of an unfair setup. The SOTA claim is a factual statement about the leaderboard and is appropriately documented with a citation.

- **"α = 0.999 used everywhere with no tuning"**: The paper states a sensitivity analysis exists in the appendix (line 350). Per evaluation protocol, missing appendix content is not a valid criticism.

- **"The method may be insensitive to α — which would be worth demonstrating"**: This is a speculation, not a verified problem. The appendix is referenced as containing the analysis.

- **"The hyperparameter α at such an extreme value"**: This is an observation, not a weakness. α = 0.999 corresponds to a conservative threshold (only project out eigenvectors where the evidence strongly favors projection), which is defensible.

## Novel Insights

The most interesting insight emerging across the reviews is the disconnect between the paper's strong theoretical machinery and the modest empirical results. The theory is clean and complete (closed-form risk, optimal projection, chi-squared selection with asymptotics), but the experiments validate it only at the aggregate level (overall RMSE improvements) rather than at the mechanism level (which eigenvectors were selected and why). The paper would be substantially strengthened by connecting the two: showing on real data that SpAR's selected eigenvectors correspond to directions with high Var/Bias ratios, that the spectral inflation phenomenon from Figure 2 aligns with the selected directions, and that the selection procedure makes correct decisions in the asymptotic regimes predicted by Lemma 1. Such an analysis would turn "SpAR modestly improves RMSE" into "SpAR correctly identifies and removes the exact eigenvectors causing OOD failure, which we can verify."

## Suggestions

- Provide numerical values for the tabular experiments (Figure 3) so readers can assess effect sizes.
- Perform a paired comparison (SpAR vs baseline per seed) and report whether the improvements are statistically significant via a paired t-test or sign test.
- Add an analysis on at least one real dataset showing: (a) how many eigenvectors SpAR selects, (b) their singular values, (c) whether their Var/Bias ratio matches the selection criterion, and (d) whether they align with known spurious features or the spectral inflation shown in Figure 2.
- Discuss the condition under which the theoretical guarantees approximately transfer to neural representations (e.g., when the encoder's representations have bounded shift).
- Replace the vague computational cost claim (line 251) with a concrete complexity analysis or wall-time measurement.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>