Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper applies dictionary learning (sparse coding) to extract interpretable features from masked autoencoder (MAE) foundation models trained on cellular microscopy images. It introduces Iterative Codebook Feature Learning (ICFL), a dictionary learning algorithm that uses a variant of orthogonal matching pursuit to update sparse codes without gradient propagation through latents, thereby avoiding dead features without auxiliary regularization. The paper further proposes applying PCA whitening on a control (unperturbed) dataset as a preprocessing step to downweight non-biological variance, and shows through five classification tasks and comparisons to CellProfiler handcrafted features that the resulting sparse representations preserve biologically meaningful information while achieving higher selectivity (monosemanticity) than TopK sparse autoencoders.

## Strengths

- **Novel algorithm (ICFL) that effectively avoids dead features**: Table 1 shows a dramatic reduction — ICFL yields only 3 dead features out of 8192 (with PCA whitening) versus 2556 for TopK SAE under identical conditions. This is a genuine practical improvement that eliminates the need for complex resampling strategies.

- **PCA whitening on a control dataset as a form of weak supervision**: The paper demonstrates that whitening the representations using unperturbed HUVEC-cell images substantially improves downstream feature quality. Figure 2a shows a clear accuracy drop across all tasks when PCA whitening is omitted (e.g., Task 3 drops from ~38% to ~28% for ICFL reconstructions). This is a simple, pragmatic idea with clear empirical support.

- **Comprehensive quantitative evaluation across multiple biological tasks**: Experiments span five classification tasks (cell types, batch effects, siRNA perturbations, CRISPR knockouts, functional gene groups), providing a thorough picture of what information is preserved in the sparse codes. The use of mutually exclusive experiments for train/test splits is good practice to avoid batch-effect leakage.

- **Qualitative validation at the pixel/channel level**: The analysis in Section 7.2 is particularly compelling — for ALG-3 (ER function), token heatmaps correlate at 0.63 with ER and RNA channels but only 0.24 with plasma membrane, precisely matching known subcellular localization. For TSC-2 (cell size control), the strongest correlation is negative (-0.71) with the membrane/Golgi channel. These channel-level validations go beyond simple label correlation and demonstrate that features recover mechanistic biological detail.

- **Favorable comparison to handcrafted CellProfiler features**: The Pearson correlation of 0.71 between ICFL and CP maximum selectivity scores per label (Figure 3g) shows that unsupervised features capture patterns similar to expert-designed features, without any domain-specific engineering.

## Weaknesses

### Fatal
None.

### Major

1. **No measures of variance or statistical significance for any quantitative result**: The selectivity comparisons (Figures 2d–2f), linear probing accuracies (Figure 2a), reconstruction cosine similarities (Figure 2c), and CellProfiler comparisons (Figures 3e–3g) are all presented as single curves or single values without error bars, confidence intervals, or standard deviations. The paper's headline empirical claims — that ICFL improves selectivity over TopK SAE — rest on these plots, and without any indication of variability across training runs, data splits, or random seeds, it is impossible to assess whether the reported improvements are statistically reliable or fall within the noise. This is the most significant weakness because it undermines confidence in the quantitative comparisons that distinguish the paper's contributions. The gap is fixable (multiple runs with different seeds) but must be addressed before the empirical claims can be taken at face value.

2. **Framing mismatch between "scientific discovery" / "unknown concepts" and the actual evaluation**: The abstract states the goal of discovering "unknown concepts from less human-interpretable scientific data" and the title reads "Towards scientific discovery with dictionary learning." Yet every quantitative experiment evaluates against *known* labels (cell types, gene perturbations, functional groups), and the qualitative analysis (Section 7) cherry-picks features that align with well-established biology. The paper never demonstrates a case where a feature corresponds to a previously unrecognized phenotypic pattern validated by expert follow-up. While the paper explicitly calls itself "a first step" and the contributions are genuinely useful (extracting known concepts is a prerequisite for discovering unknown ones), the motivating language overpromises relative to what is delivered. This is a framing problem, not a methodological flaw, and can be corrected with more precise language.

### Minor

- **Reconstruction comparison (Figure 2c) conflates optimization objective with feature quality**: ICFL computes sparse codes by directly solving for the best reconstruction given the decoder (via its OMP variant), whereas TopK SAE learns an encoder jointly with the decoder. It is expected that a method which explicitly optimizes reconstruction per-input will achieve lower reconstruction error — the advantage is baked into the procedure. The paper presents this as evidence of superiority without acknowledging this confound. The reconstruction metric is reported alongside selectivity results, creating the impression that ICFL uniformly outperforms TopK, when in fact the methods are compared on a metric that inherently favors ICFL. This does not invalidate the selectivity results (which are the paper's main claim), but the reconstruction comparison should be contextualized.

- **Figure 2b (sparsity ablation) only shows ICFL, not TopK**: The paper claims that "increasing the number of non-zeros improves the accuracy, the effect is limited compared to PCA whitening," but this claim is supported only by ICFL data. Including TopK at multiple sparsity levels would strengthen the comparison.

- **Layer selection via linear probing on the functional group task could leak information**: The paper selects the MAE layer that "maximized linear probing performance on the functional group task." If this selection uses the same data as subsequent evaluation, it introduces information leakage. Clarification of whether a held-out validation set was used for layer selection is needed.

- **PCA whitening details are underspecified**: The paper mentions a "PCA-and-centerscale transform" but does not define "centerscale" (standard scaling? mean-centering only?), and does not report how many PCA components were retained. These details affect reproducibility.

- **"Active" is not explicitly defined for DL features in the selectivity computation**: The selectivity formula ("% of times that the feature is active given label i") likely means non-zero, but this is not stated, unlike the explicit threshold definition given for CellProfiler features.

- **No systematic assessment of what fraction of features are interpretable**: The qualitative analysis (Section 7) shows compelling examples but explicitly selects the most interpretable features. Without a broader characterization — e.g., distribution of maximum selectivity scores across all 8192 features, or a human evaluation of feature-to-perturbation matching — it is unclear how representative these examples are.

### Trivial

- The ablation in Figure 2b would benefit from including TopK SAE for completeness (noted above; placed here as it does not affect the paper's main conclusions, which are supported by Figures 2d–2f where both methods are shown).

## Nice-to-Haves

- Reporting error bars (from multiple training runs) would substantially strengthen the paper's empirical claims.
- An experiment demonstrating feature discovery in a setting without pre-existing labels (e.g., applying the dictionary to a novel perturbation and having a biologist interpret the top features) would directly address the "scientific discovery" framing.
- A histogram of the maximum selectivity per feature across all 8192 features would help calibrate expectations about how many features are genuinely selective versus random.
- Showing failure cases (features dominated by batch effects or with no biological correlate) would provide a more balanced view.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"No indication of how many experiments are in train vs. test for each task"**: The paper states "we always use mutually exclusive experiments for test and train data" (Section 5), which addresses the spirit of the concern. Specific counts would be nice but are not essential.

- **"The training procedure for TopK SAEs (whether they used auxiliary losses or resampling) is not described"**: The paper references Gao et al. (2024) and Bricken et al. (2023) as the standard implementations, which is standard practice. The dead feature comparison in Table 1 is self-contained — it reports the actual counts. This concern reflects a reproducibility nitpick that goes beyond standard expectations for a conference paper.

- **"The algorithm description is insufficient for reproducibility"**: The paper specifies J=20, k=5 (max sparsity 100), learning rate 5e-5, batch size 8192, 300k iterations, and the random reset mechanism (every 100 gradient steps, reset pairs with cosine similarity > 0.9). The OMP variant is described in text with residual subtraction and column selection. While an explicit pseudocode figure is missing (stripped by parser), the textual description is adequate for a reader familiar with matching pursuit.

## Novel Insights

The paper reveals an interesting tension in applying mechanistic interpretability tools to scientific foundation models: the same dictionary learning techniques that recover human-interpretable concepts in LLMs can recover biologically meaningful features from microscopy MAEs, but the features are naturally dominated by the highest-variance directions in representation space. The use of PCA whitening on a *control dataset* (unperturbed cells) to suppress these dominant but non-biological directions is a clever adaptation — it injects a minimal form of weak supervision (what *doesn't* change under perturbation) without requiring any labeled examples. This suggests that in scientific domains, interpretability of foundation models may need to be reframed from "what does the model encode" to "what can we extract that aligns with real-world structure," and that variance partitioning against control data could be a general strategy for improving feature quality in other scientific applications (e.g., medical imaging, genomics).

## Suggestions

1. **Add error bars**: Repeat all main experiments (selectivity, linear probing, reconstruction) with at least 3 random seeds and report means with error bars (standard deviation or confidence intervals). This is the single most important improvement.
2. **Tone down the "discovery" framing**: Replace language about discovering unknown concepts with more precise claims about extracting known biological concepts, or add a dedicated experiment that validates a genuinely novel feature through expert follow-up.
3. **Clarify the reconstruction comparison**: Acknowledge that ICFL's reconstruction advantage is partly an artifact of its optimization procedure, and focus the comparison on selectivity, which is the more meaningful metric for both methods.
4. **Specify PCA whitening details**: Report the number of components retained and define "centerscale" explicitly.
5. **Show the full distribution of selectivity scores**: A histogram or cumulative distribution of per-feature maximum selectivity across all 8192 features would help readers understand what fraction of the dictionary is actually informative.
6. **Clarify layer selection**: State explicitly whether a held-out validation set was used when selecting the layer that maximizes linear probing performance.

## Score and Decision

This paper makes genuine contributions — a practical dictionary learning algorithm that avoids dead features, a clever control-based whitening strategy, and a thorough biological evaluation demonstrating that learned features align with known cell biology and compete with handcrafted CellProfiler features. The qualitative validation at the specific channel level (Section 7.2) is particularly strong.

However, the paper is significantly weakened by the complete absence of variance or statistical significance reporting for any quantitative metric, making it impossible to assess the reliability of the claimed improvements. Combined with the framing mismatch (motivating unknown-concept discovery but evaluating only known labels) and several underspecified methodological details, the paper in its current form has notable evidential holes. These are all fixable with additional experiments and writing revisions, and the underlying work is solid enough that the contribution is likely to hold.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>