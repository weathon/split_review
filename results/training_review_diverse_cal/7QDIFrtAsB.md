Now I have all the information I need. Let me construct the final review.

---

## Summary

This paper proposes NCSBAD, an anomaly detection method for tabular data that trains a Noise Conditional Score Network (NCSN) on normal samples only and derives an anomaly score from the denoising error (prediction of added noise) at a fixed small noise scale. The method is evaluated on a large benchmark comprising 57 datasets (ADBench + 15 additional) against 49 baseline methods, reporting competitive mean AUC-ROC and AUC-PR. A validation-based variant (NCSBADVAL) achieves the highest aggregate scores. The authors also demonstrate feature-level interpretability via a toy MNIST-C example.

## Strengths

- **Very large-scale empirical evaluation**: The paper assembles and evaluates on an extensive collection of 57 datasets (121 sub-datasets) with 49 baseline methods spanning classical (LOF, IForest, kNN) and recent deep learning (DDPM, DIF, MCM) approaches, making this one of the most comprehensive tabular AD comparisons to date. This breadth is a genuine service to the community.

- **Competitive performance across multiple metrics**: NCSBAD (without validation-based selection) achieves the highest mean AUC-ROC and ranks second in F1-Score and AUC-PR across all datasets. NCSBADVAL further improves on these numbers. The method is competitive even without the validation advantage, demonstrating that the core idea has merit.

- **Fixed architecture with no per-dataset tuning**: The same MLP2048 architecture, noise schedule, and hyperparameter settings are used across all 57 datasets. The paper also uses default hyperparameters for all baseline methods. This reduces the risk of overfitting to specific datasets and makes the evaluation protocol transparent.

- **Parallelizable and efficient inference**: Unlike DDPM-based approaches that require sequential Markov chain sampling, the NCSN anomaly score can be computed independently for multiple noise draws, enabling parallelization and faster inference — a practical advantage worth noting.

## Weaknesses

### Major

**1. The anomaly score lacks principled justification and is essentially a single-scale denoising error dressed in score-matching language.**

The anomaly score is ADS = 𝔼_ε[‖S_θ(x_{t_fix}, t_fix) − ε‖²] — the prediction error for added Gaussian noise at a fixed, minimal noise level. While the network is trained via denoising score matching across multiple noise scales, inference uses only the smallest scale and the output is not converted to the actual score (−S_θ/σ_t). The paper merely asserts (line 16) that "score variation between normal and anomalous samples provides a robust mechanism" without any theoretical or empirical analysis of why this specific quantity should separate normal from anomalous data. No connection is drawn between the denoising MSE at a single noise level and any known property (e.g., monotonicity in distance from the data manifold, connection to local density). For an anomalous sample not seen during training, the prediction error will differ — but the same is true of any reconstruction-based method, and the paper does not explain why this particular formulation is preferable to, say, a standard denoising autoencoder trained at a single noise scale. The framing as "score-based" overstates the novelty; the method is better understood as a one-step denoising autoencoder operating at a fixed tiny noise level.

**2. Asymmetric comparison: NCSBADVAL uses validation-based early stopping while baselines receive no analogous advantage.**

The paper states (line 93): "For all methods used, we apply the default hyperparameters provided by the authors... No additional hyperparameter tuning or other adjustments to the code were made." Meanwhile, NCSBADVAL selects the best training epoch based on validation AUC-ROC (line 78–79). This is an asymmetric advantage: many deep learning baselines (DeepSVDD, DAGMM, GANomaly, VAE, etc.) are known to be sensitive to training length and could benefit from comparable early stopping. The paper's central SOTA claim rests on NCSBADVAL's top mean scores; the comparison would be more credible if either (a) all methods received the same validation-based selection, or (b) NCSBAD (without validation) were presented as the primary variant, with NCSBADVAL flagged as a separate, optional improvement. To the paper's partial credit, NCSBAD (without validation) is also reported and remains competitive — but the architecture, noise schedule, and t_fix were themselves chosen by the authors, while baselines are locked to defaults that may be suboptimal for these specific data splits.

### Minor

**3. No statistical significance testing for reported SOTA results.**

Figure 2 shows box plots with substantial overlap between NCSBAD, NCSBADVAL, and several baselines (LUNAR, GMM, KPCA). The paper acknowledges that "no single method universally dominates across all datasets" (line 95), yet claims "state-of-the-art performance" (abstract) based on mean ranks. No paired significance tests (e.g., Wilcoxon signed-rank) or confidence intervals are reported. Given the variance across datasets and the overlap visible in box plots, the aggregate superiority is not clearly established.

**4. Validation set contains anomalous samples and is used for model selection — a methodological concern.**

The validation split includes 40% of anomalies (line 89). The paper then uses AUC-ROC on this validation set to pick the best training epoch (line 78–79). Standard practice in one-class anomaly detection is to use anomaly-free validation data; including known anomalies in the validation set risks leaking information about what constitutes an anomaly into the model selection process. The paper does not discuss or justify this choice.

**5. Unconventional noise scale formula and limited exploration of design choices.**

The noise schedule σ_t = √((σ^{2t}−1)/(2 log σ)) with σ=0.01 is non-standard (score-matching literature typically uses geometric progressions). The maximum σ_T ≈ 0.5 means the largest perturbation is still below one standard deviation of standardized data, limiting exploration of low-density regions. The choice of t_fix (first of 1000 time steps), the number of noise samples (70), and the noise schedule itself are not ablated. Without sensitivity analysis, it is unclear how robust the method is to these design decisions.

**6. Interpretability demonstration uses a vision dataset, not tabular data.**

The feature-level interpretation (Section 5) is shown on flattened MNIST-C images. While the paper acknowledges this is a "toy example" and notes the difficulty of visualizing tabular feature attributions (line 113), the claimed "inherent interpretability" is not demonstrated for the paper's intended domain of mixed-type, heterogeneous tabular features. A simple ablation on a real tabular dataset (e.g., showing which features drive the score on a dataset with known ground-truth anomalous columns) would be more convincing.

### Trivial

- The abstract claims "we created the world's largest benchmark" (line 4), but the paper is primarily using ADBench (Han et al., 2022) with 15 additional datasets. This is an extension, not a new creation. The claim should be toned down.

## Nice-to-Haves

- **A simple single-scale denoising autoencoder baseline**: Training an MLP to denoise samples corrupted only at σ ≈ σ_{t_fix} (the fixed inference noise) would directly test whether the multi-scale training used by NCSBAD provides any benefit over a simpler single-scale approach. If NCSBAD outperforms this baseline, the multi-scale training is doing useful work; if not, the added complexity is unnecessary.

- **Ablation of t_fix and σ**: Sensitivity analysis over different fixed noise levels (e.g., t_fix corresponding to steps 1, 5, 10, 50 of 1000) and different numbers of noise samples would strengthen the empirical claims.

- **Synthetic 2D demonstration**: Showing on synthetic 2D data that the anomaly score behaves monotonically with distance from the training data manifold would replace the MNIST-C vision toy with direct evidence in the paper's target setting.

## Removed Points

- **"The paper claims 'world's largest benchmark' but ADBench already exists" (from Harsh Critic's Other Observations)**: The paper uses ADBench + 15 additional datasets. Whether this constitutes a "new" benchmark is largely a semantic issue; the evaluation is genuinely large-scale. Retained only as a trivial phrasing concern above.

- **"The approach is only 'self-contained' in the narrow sense that it does not use external dataset labels"**: This is a wording quibble. The paper's self-contained claim refers to not requiring pre-trained models or external knowledge — a defensible description.

- **"The reproducibility statement references supplementary material that is not present in the review text"**: Parser artifact; the supplementary material exists in the original submission.

- **Points about missing analysis of the learned score vector field, or about mixed-type feature handling**: These are not core to the paper's contribution and/or are outside the paper's stated scope (the paper focuses on numeric tabular data). Moved to Nice-to-Haves above.

## Novel Insights

None beyond the paper's own contributions. The core observation — that an NCSN trained on normal data produces higher denoising error at a fixed noise level for anomalous samples — is intuitive and consistent with how any reconstruction-based method behaves. The main contribution is the scale of the empirical evaluation, not a novel theoretical insight about anomaly detection.

## Suggestions

1. **Re-frame the method honestly**: Describe NCSBAD as a "multi-scale denoising autoencoder with fixed-noise-level scoring" rather than as a "score-based" method. The connection to score functions is tangential to the actual anomaly score used, and the current framing invites skepticism.

2. **Fix the comparison asymmetry**: Either apply the same validation-based early stopping to all deep learning baselines, or make NCSBAD (without validation) the primary reported variant and clearly separate NCSBADVAL as a secondary result. Report the comparison both ways.

3. **Add statistical significance tests**: Report paired Wilcoxon signed-rank tests or bootstrap confidence intervals comparing NCSBAD to the top-3 baselines. This would either support or qualify the SOTA claim.

4. **Ablate the key design choices**: Report sensitivity of results to t_fix, number of noise samples, and the noise schedule formula. Even 2–3 additional settings would substantially strengthen the paper.

5. **Demonstrate interpretability on a genuine tabular dataset**: Select a dataset with known feature-level ground truth (e.g., a dataset where only specific columns are corrupted for anomalies) and show that the feature-wise ADS reliably identifies those columns.

## Score and Decision

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>