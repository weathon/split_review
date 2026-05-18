Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper proposes NCSBAD, an anomaly detection method that trains a Noise Conditional Score Network (NCSN) on normal tabular data and uses the denoising error (MSE between predicted and true noise) at a fixed small noise level as the anomaly score. The method is evaluated on the largest tabular anomaly detection benchmark assembled to date (57 datasets / 121 sub-datasets) against 49 baseline methods. The paper reports that NCSBAD achieves competitive top-ranked mean AUC-ROC even without validation-based selection, and NCSBADVAL (with held-out validation for epoch selection) improves further to first place across all metrics.

## Strengths

1. **Largest benchmark evaluation for tabular AD**: The paper evaluates on 57 datasets (121 sub-datasets) with 49 baseline methods, making this the most comprehensive tabular anomaly detection comparison in the literature. Results are reported over 5 random seeds. (Section 4, lines 87-98)

2. **Competitive results even without validation-epoch selection**: NCSBAD (without validation-based epoch selection) achieves the highest mean AUC-ROC and second-best F1-score across all datasets (Figure 2, line 98). This demonstrates that the core NCSN-based score is effective on its own terms, not merely an artifact of validation tuning.

3. **Efficient parallelized inference over DDPMs**: Unlike DDPMs that require sequential Markov-chain denoising, NCSBAD's inference is parallelizable (70 forward passes in parallel), a genuine practical advantage (Sections 3, 8). The method also outperforms DDPM-based alternatives (Livernoche et al., 2024) in detection accuracy.

4. **Inherent feature-level interpretability**: The anomaly score can be decomposed per feature, enabling localized anomaly detection. This is demonstrated on MNIST-C, where the feature-wise error map visually aligns with the injected anomaly (Section 5, Figure 3).

5. **No per-dataset hyperparameter tuning**: All methods — including NCSBAD — use fixed default hyperparameters from their original publications with no per-dataset adjustment (line 93). The paper also attempts to include methods that require specialized tuning (Transformer, NTP-AD) on overlapping datasets where tuning was performed.

## Weaknesses

### Fatal
None.

### Major

1. **Unequal comparison due to validation-based epoch selection for NCSBADVAL only**. The paper introduces NCSBADVAL, which uses a held-out validation set to select the optimal training epoch from the full 200-epoch trajectory based on AUC-ROC. Meanwhile, all 49 baseline methods are run with fixed default hyperparameters and no analogous model selection. Deep learning baselines (DeepSVDD, DAGMM, GANomaly, etc.) could also benefit from validation-based early stopping or epoch selection, but are not given that opportunity. The paper acknowledges that all baselines use default hyperparameters (line 93) but does not address the asymmetric model-selection advantage. **Mitigation**: NCSBAD (the version without validation selection) is also reported and achieves the best mean AUC-ROC and second-best F1, so the core contribution does not depend on this advantage. However, the paper's primary promotional claim ("NCSBADVAL outperforms all baseline models") rests on an unequal comparison. A fairer primary comparison would be NCSBAD (no validation) vs. baselines, with NCSBADVAL presented as an additional improvement.

2. **No statistical significance testing**. With 121 sub-datasets, the evaluation is large enough to support meaningful paired significance tests (e.g., Wilcoxon signed-rank across datasets comparing NCSBAD/NCSBADVAL against the best-performing baseline). The paper reports mean ranks and box plots, but the interquartile ranges appear to overlap for several top methods, and without formal tests the claim of "state-of-the-art" superiority is not statistically grounded. This is a standard expectation for papers making comparative SOTA claims.

### Minor

3. **The anomaly score noise level choice (t\_fix) has limited justification and no sensitivity analysis**. The paper fixes t\_fix to the first of 1000 timesteps (very small noise), with the reasoning that "perturbations should be small" (line 62). While the intuition is reasonable — the model trained on normal data learns the score near the data manifold, and anomalies deviate — the critic's concern that the mechanism for separation at this specific noise level is not rigorously analyzed is fair. A sensitivity study varying t\_fix (or evaluating a weighted combination of multiple noise levels) would substantially strengthen confidence that the chosen operating point is not brittle. Without this, the anomaly score formulation appears somewhat arbitrary.

4. **Missing ablation studies on key design choices**. The paper fixes hyperparameters (hidden dimension 2048, NUM=70 epsilon samples, noise schedule σ=0.01, 200 epochs) across all datasets, but provides no analysis of how sensitive results are to these choices. For a method claiming generalizability, ablations on (a) the number of epsilon samples NUM, (b) the noise schedule parameters, and (c) the network size would be informative. The paper's use of 2048 hidden units — larger than the maximum feature dimension — is explained (avoiding compression bottleneck), but whether smaller architectures suffice is unexplored.

5. **Interpretability demonstration is on a vision toy example, not on actual tabular data**. The paper acknowledges this (line 113: "this is indeed a vision example") and notes that flattened images are structurally similar to tabular vectors. However, a real tabular dataset with known feature-level ground truth (e.g., medical data where specific features are known to be anomalous) would make the interpretability claim more convincing for the paper's primary domain.

### Trivial
None.

## Nice-to-Haves

- Report actual wall-clock inference times on comparable hardware to substantiate the parallelization efficiency claim.
- Vary the proportion of normal data used for training (e.g., 30%, 70%) to test robustness to training set size.
- Include a tuned version of OCSVM (RBF kernel with cross-validated bandwidth) as a strong classical baseline reference.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Unsupervised vs. semi-supervised terminology** (Critic's "Other Observations"): The paper explicitly addresses this (line 14: "This is also often called semi-supervised learning") and correctly frames the setting as LPUE/one-class. This is a non-issue.
- **"The model can simply output the input"** (Critic's Critical Issue #3): This argument misunderstands the training objective. The model predicts ε (the added noise), not x₀. A model that "outputs the input" would produce a large prediction error since the target is ε, not x. The score-based mechanism for detecting anomalies at small noise levels is sensible.
- **"The empirical contribution is weakened by above issues"** (Critic's Critical Issue #5): This is not a standalone weakness but a summary of concerns already addressed individually.
- **Generic strengths from Strength Finder** that conflict with verified weaknesses: None found; the verified strengths are all substantive and supported by the paper.
- **Missing related works**: Instructions preclude this.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any perspective on the method or its evaluation that the paper itself does not already contain or clearly imply.

## Suggestions

1. **Reframe the primary comparison**: Present NCSBAD (without validation selection) as the main result against baselines, and NCSBADVAL as an additional improvement. This removes the fairness concern about asymmetric model selection.

2. **Add paired statistical tests**: Report Wilcoxon signed-rank tests comparing NCSBAD/NCSBADVAL against the strongest baselines across all datasets. Report win/tie/loss counts.

3. **Ablate the noise level t\_fix**: Show that the method is not brittle to this choice by evaluating a range of t\_fix values on a representative subset of datasets, or report results using a weighted combination of multiple noise levels.

4. **Ablate NUM and network size**: Demonstrate that NUM=70 is sufficient (score saturates) and that the method does not require the full 2048 hidden dimension to work well.

5. **Add tabular feature-level interpretability**: On a small dataset with known relevant features (e.g., medical or synthetic), show that the feature-wise ADS correctly highlights anomalous dimensions.

## Score and Decision

**Originality**: 5/10 — Applying NCSN to tabular anomaly detection with a simplified score-based anomaly measure is a reasonable contribution but not a conceptual breakthrough.  
**Importance of research question**: 7/10 — Tabular anomaly detection is practically important and benchmarks are valuable to the community.  
**Claims support**: 4/10 — The SOTA claim is partially supported but weakened by the asymmetric validation advantage and absence of significance testing.  
**Soundness of experiments**: 5/10 — Large-scale and well-structured, but the unfair comparison and lack of statistical rigor undermine confidence.  
**Clarity of writing**: 7/10 — Generally clear and well-organized.  
**Value to community**: 7/10 — The benchmark assembly and comprehensive comparison are valuable even with the methodological caveats.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>