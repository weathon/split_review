## Summary
ReMasker adapts the masked autoencoding (MAE) framework to tabular data imputation by "re-masking" a randomly selected subset of observed values during training (in addition to naturally missing values), then training a Transformer-based encoder–decoder to reconstruct those re-masked values. This creates a supervised reconstruction signal despite the data being inherently incomplete. The paper evaluates on 12 UCI benchmark datasets against 13 baselines under MAR (0.3 missingness ratio) and includes ablation, sensitivity, and theoretical analysis.

## Strengths
- **Simple, well-motivated re-masking strategy.** The core idea — randomly masking additional observed values beyond the naturally missing ones to create a reconstruction task — is clearly described (Section 3, Algorithm 1) and directly addresses a fundamental gap in applying MAE to already-incomplete tabular data.

- **Strong empirical results on MAR 0.3.** Under the main evaluation setting (MAR, 0.3 ratio), ReMasker achieves competitive or superior RMSE, Wasserstein distance, and AUROC compared to 13 baselines across all 12 datasets (Figure 1/fig:overall). The advantage is particularly notable against strong ensemble methods like HyperImpute.

- **Robustness at high missingness ratios.** Sensitivity analysis on the `letter` dataset (Figure 3c) shows ReMasker maintains RMSE below 0.1 even when 70% of values are missing, with its relative advantage over baselines growing at higher ratios (Section 4.2).

- **Informative ablation revealing a domain difference from vision MAE.** Table 3 (tab:loss) shows that including unmasked values in the reconstruction loss improves tabular imputation — opposite to the vision MAE finding. The paper offers a plausible explanation based on tabular data's higher information density vs. images' spatial redundancy (Section 4.3).

## Weaknesses
### Fatal
None.

### Major

1. **Inconsistency between headline claims and presented evidence.** The main text claims ReMasker "consistently outperforms all the baselines in terms of both fidelity (measured by RMSE and WD) and utility (measured by AUROC) across all the datasets" (Section 4.1). The figure caption instead states it "outperforms all the baseline imputers **under at least one metric** across all the datasets" (Figure 1 caption). These are substantially different claims — the former asserts a clean sweep on all three metrics, the latter only requires winning on one. The paper must correct this inconsistency and calibrate its claims to what the evidence supports.

2. **Results for MCAR and MNAR are absent despite claimed scope.** The abstract claims evaluation "under various missingness settings" and the method description (Section 3) defines all three mechanisms. Yet full numerical results are presented **only** for MAR with 0.3 ratio. MCAR and MNAR receive only a single speculative paragraph (Section 4.1) and a brief limitations note saying ReMasker "tends to perform better under MCAR" — no tables, figures, or win/loss counts. For a paper claiming superiority under "various scenarios," this is a significant evidential gap that prevents assessing generalization across missingness mechanisms.

3. **No ablation isolating re-masking from standard Transformer imputation.** The paper does not compare ReMasker against a Transformer autoencoder trained *without* re-masking (e.g., trained to reconstruct only the naturally missing values, with no additional random masking). Such an ablation is critical to attribute the performance gain to the re-masking strategy rather than to Transformer capacity or the MAE framework generally. The existing loss ablations (Table 3) are valuable but do not fill this gap.

### Minor

1. **Categorical feature handling is unspecified.** The paper acknowledges data can be categorical (Section 3.1) but never describes how categorical features are encoded, what loss function applies to them, or whether performance differs by feature type. The linear encoding function and MSE loss (Section 3.2) assume continuous values. This is a meaningful implementation gap for practical applicability.

2. **Theoretical justification is primarily a restatement, not an explanation.** The derivation in Section 5 shows that minimizing the reconstruction loss is equivalent to minimizing decoder-distance between representations under different masks. This is a re-description of the training objective rather than a mechanistic explanation of *why* invariance leads to better imputation. The assumption of near-lossless reconstruction ("it is possible to make the autoencoder lossless") is stated without justification and may not hold with limited tabular data. The CKA plot (Figure 2) is consistent with the objective but does not compare against a baseline, so we cannot tell whether ReMasker produces more invariant representations than alternatives.

3. **Key experiments use only 1–2 datasets.** Sensitivity analysis (Section 4.2), masking ratio experiments (Table 5), backbone comparison (Table 2), and loss ablation (Table 3) all use only the `letter` dataset or at most `letter` and `california`. Generalizability of these findings to the other 10 datasets is unknown.

4. **Insufficient detail on baseline tuning.** The paper does not state whether baseline imputers were hyperparameter-tuned or used with default settings, making it unclear whether the comparisons favor ReMasker.

5. **Feature normalization/scaling not described.** Whether features are normalized before linear encoding matters for MSE-based reconstruction, but this is not specified.

### Trivial

- Algorithm 1 pseudocode shows the optimizer update occurring once per epoch (outside the inner loop) rather than per mini-batch. This is likely a simplification in pseudocode but should be clarified to avoid confusion.

## Suggestions
1. **Fix the claim inconsistency**: Either change the text in Section 4.1 to match the caption ("under at least one metric") or provide evidence for the stronger claim across MCAR and MNAR as well.
2. **Add MCAR and MNAR results**: Present full tables (RMSE/WD/AUROC) for all 12 datasets under MCAR and MNAR, at minimum at one missingness ratio. Without this, the "various missingness settings" claim is unsupported.
3. **Add the critical missing ablation**: Compare ReMasker against a Transformer autoencoder variant trained *without* re-masking (reconstructing only naturally missing values), to isolate the benefit of the re-masking strategy.
4. **Specify categorical feature handling**: Describe how categorical features are encoded, what loss is used, and whether results differ by feature type.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Borderline Reject</decision>

## Questions


## Decision
Borderline Reject
