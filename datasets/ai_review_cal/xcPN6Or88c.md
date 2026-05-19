- Decision: Reject
- Avg Score: 4.25
- Scores: 5, 3, 3, 6
Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

## Summary

The paper proposes ImputeINR, a time series imputation method that learns an implicit neural representation (INR) — a continuous function mapping timestamps to variable values — decomposed into trend (polynomial), seasonal (Fourier), and residual (adaptive group-based MLP) components. A multi-scale convolution module extracts features at different temporal scales, and an agglomerative clustering step groups variables with similar distributions so the residual MLP can share group-specific layers. The approach aims specifically at scenarios with high missing rates (70–90%). Experiments on seven datasets across five mask rates report large MSE reductions over baselines.

## Strengths

- **Novel application of INR to time series imputation with a structured decomposition.** The idea of using a continuous function (INR) to decouple imputation from discrete sampling frequency is well-motivated, especially for extreme missing rates. The three-component decomposition (trend, seasonal, residual) adapts the INR framework to time series' specific temporal structure. This is a genuine architectural contribution.

- **Ablation evidence supports each module's individual contribution.** Table 3 (described in Section 4.3) tests the model with each of the three modules (multi-scale convolution, variable clustering, adaptive group layers) removed individually. The text states that "adding any one of the modules will enhance the imputation capability of the model," providing per-module validation. The combination of clustering + group layers yields the best results, which is consistent with the design rationale.

- **Comprehensive evaluation across diverse settings.** Experiments span seven datasets (health, weather, energy, air quality) with varying numbers of variables (7 to 721) and sample sizes, at five mask rates (10% to 90%). This breadth supports claims of robustness.

- **The adaptive grouping mechanism is conceptually elegant.** Letting variable clustering determine both the number of groups and each group's output dimension allows the architecture to adapt to datasets with different characteristics without manual specification of group structure.

## Weaknesses

### Fatal

None. The paper's core claims are coherent and supported by some evidence, though significant concerns exist (see below).

### Major

- **Insufficient documentation of baseline tuning and experimental fairness.** The paper reports a 62.7% average MSE reduction and up to 96.1% on the IAQ dataset. These are unusually large improvements for this field. The paper states that "these settings follow those used in previous work (Wu et al., 2023; Du, 2023)" and uses the same window sizes, but provides no information about whether baseline hyperparameters were tuned per dataset, whether default settings from original papers were used, or how baselines were adapted to the specific masking protocols. On small datasets like IAQ and BAQ, baselines reportedly perform nearly as poorly as mean/median imputation, which raises the concern of suboptimal baseline configuration (e.g., transformer-based methods overfitting on small data). Without evidence of equal tuning effort and fair validation, the central claim of state-of-the-art performance is not convincingly supported. This is the most significant weakness in the paper.

- **The mapping from transformer output tokens to INR function parameters is underspecified.** The paper states that "INR tokens are essentially the parameters of the INR continuous function" and that they are "predicted by the transformer encoder," but never specifies how the output tokens are transformed into the specific coefficients of the three components: the polynomial coefficients α_i (trend), the Fourier coefficients β_i, γ_i (seasonal), and the weight matrices W, b of the global and group MLP layers (residual). The reader cannot determine whether the tokens are flattened parameter vectors, whether they are modulated via a hypernetwork, or how they are structured. This is a structural gap that prevents replication.

- **No statistical significance or variance reporting.** No confidence intervals, standard deviations, or results across multiple random seeds are reported for any experiment. This is a standard expectation in the field, and its absence makes it impossible to assess the reliability of the reported improvements.

### Minor

- **Key implementation details are missing.**
  - The polynomial degree *m* for the trend component (Eq. 6) is never specified.
  - The similarity matrix *S*(x_i, x_j) used for variable clustering (Section 3.3) is defined abstractly but no concrete computation is given — particularly important since the data has missing values, making pairwise similarity non-trivial.
  - The agglomerative clustering method is named but distance metric, linkage criterion, and cut threshold are not provided.

- **Architecture hyperparameters are not justified or ablated.** The adaptive group-based MLP uses exactly one global layer and one group layer with hidden dimension 16, with three fixed kernel sizes (3,5,7). No study shows how performance varies with these choices or why these specific values were chosen.

- **The synthetic motivation for grouping (Figure 2) is not backed by real-data diagnostic evidence.** The paper uses a synthetic four-variable dataset to motivate the group-based design, showing that grouping similar-distribution variables helps. However, on the seven real benchmarks, the paper does not provide any diagnostic metric (e.g., silhouette score) to confirm that the clustering captures meaningful structure, nor does it compare against simpler alternatives such as a per-variable MLP without grouping or a shared MLP with learned variable embeddings. The ablation confirms the combination works, but the *why* — that similar-distribution grouping drives the improvement — is not directly validated on real data.

- **Only random masking is evaluated.** Real-world missingness often has block/temporal structure (e.g., sensor dropouts). The paper only tests random masking, which may advantage a continuous-function approach.

### Trivial

None.

## Nice-to-Haves

- Add clustering diagnostic metrics (e.g., silhouette score) and show imputation performance when groups are randomly permuted or set to fixed values (1, 2, N) to further validate the grouping rationale.
- Evaluate on block-missing or non-uniform missing patterns to strengthen claims of practical usefulness.
- Report runtime and parameter count comparisons to contextualize computational cost.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Ablation only removes clustering+group together, cannot separate their effects."** — Factually incorrect. The paper explicitly states that each of the three modules was tested individually ("adding any one of the modules will enhance the imputation capability"). The ablation *does* separate the individual contributions.

2. **"Table 2 is missing from the text" / "Figures are not shown."** — Parser artifacts. The original submission contains these elements as embedded images, which the text extractor cannot render.

3. **"The reported improvements are implausibly large (62.7%, 96.1%)."** — This is speculation about magnitude. Large relative reductions are possible when baseline MSE is very high (especially on small datasets like IAQ with 935 samples). The legitimate concern is about *whether baselines were fairly tuned*, not that the numbers are inherently implausible. The tuning concern is retained above.

4. **"Novelty claim about 'first to focus on extremely absent data' is overstated."** — The paper makes a "to the best of our knowledge" claim about being the first to focus on 70%/90% mask rates. Per reviewer guidelines, I cannot verify or refute this without full knowledge of prior work, so this point is removed.

5. **"Seasonal component has too many parameters (95 coefficients for T=96)."** — This is a design choice. The paper does not discuss overfitting, but the concern about parameter count is a natural consequence of the Fourier representation and not a flaw per se. For context, many time series models (e.g., FPT) use full-spectrum representations.

6. **Missing related works.** — Excluded per guidelines.

7. **"The paper does not specify how m is determined."** — Retained as a minor weakness (see above). The critic's framing of this as a structural gap was inflated; it is a missing implementation detail.

## Novel Insights

None beyond the paper's own contributions. The reviews identified the paper's substantive strengths and weaknesses but did not uncover an analytical insight about the method that the authors themselves missed.

## Suggestions

1. **Document the baseline tuning protocol in detail.** For each of the nine baselines, state whether hyperparameters were tuned per dataset (and how: grid search range, validation metric), or whether published defaults were used. Run all methods with identical window sizes and masking. Report results over ≥3 random seeds with standard deviations. Without this, the central experimental claim cannot be trusted.

2. **Specify the INR token-to-parameter mapping explicitly.** Add a figure or pseudocode showing how the transformer's output tokens are decoded into the specific parameters of each component: the α_i coefficients (trend polynomial), the β_i, γ_i coefficients (Fourier series), and the W, b matrices of the global and group MLP layers (residual). This is essential for reproducibility.

3. **Add variance reporting.** Report all results with standard deviations over multiple runs. Fix the missing implementation details: polynomial degree m, similarity metric S, agglomerative clustering parameters (distance metric, linkage, threshold).

4. **Validate the grouping mechanism on real data.** Add a simple comparison against a variant with a single per-variable MLP (no grouping) and a variant with a fixed number of groups (e.g., K=1, K=N). Provide clustering quality metrics (e.g., silhouette score) on real datasets.

5. **Shorten or qualify the novelty claim** about being "first" to focus on extreme missing rates. The contribution stands on its method; the framing is unnecessary and invites scrutiny.
