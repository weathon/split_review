Now I have a thorough understanding of the paper and have verified each critic claim against the actual text. Let me construct the final consolidated review.

## Summary

This paper explores whether dictionary learning can extract biologically meaningful concepts from unsupervised microscopy foundation models (MAEs). The authors propose a new dictionary learning algorithm, Iterative Codebook Feature Learning (ICFL), and combine it with PCA whitening on a control dataset. They demonstrate that sparse features from MAE intermediate layers correlate with cell types, genetic perturbations, and functional gene groups, achieving selectivity scores comparable to handcrafted CellProfiler features. ICFL eliminates dead features without additional regularization, and PCA whitening improves both selectivity and linear probing performance compared to TopK SAEs.

## Strengths

- **First demonstration of dictionary learning extracting meaningful biological concepts from unsupervised microscopy foundation models.** The paper shows that sparse features from MAE intermediate layers are correlated with cell types, genetic perturbations (siRNA, CRISPR), and functional gene groups (Table 3, Figures 2d–2f), opening a path to scientific discovery via mechanistic interpretability in a domain lacking strong prior knowledge of high-level concepts.

- **ICFL eliminates dead features without extra regularization.** Table 1 reports that ICFL produces zero dead features compared to TopK SAEs, while maintaining comparable or better reconstruction quality and selectivity (§4, Figure 2c). This is a clean algorithmic improvement over standard SAE training.

- **PCA whitening on a control dataset provides a principled weakly-supervised preprocessing step.** Figure 2a shows a clear drop in balanced test accuracy for Tasks 3 and 5 when PCA whitening is omitted. The approach of downweighting dominant directions from control (unperturbed) samples is well-motivated and effective.

- **ICFL features achieve selectivity scores comparable to handcrafted CellProfiler features.** Figure 3e shows that ICFL's highest average selectivity scores nearly match those of expert-designed CP features, with a Pearson correlation of 0.71 between their scores across labels (Figure 3g). This provides a strong quantitative benchmark against established domain-engineered features.

- **Qualitative analysis reveals interpretable, biologically validated feature patterns.** Section 7 provides detailed channel-specific correlations (e.g., OPA-1 with mitochondria, ALG-3 with ER, TSC-2 with plasma membrane) with token-level heatmaps that align with known perturbation phenotypes (Figures 4 and 5), demonstrating that learned features capture non-trivial morphological changes.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Limited baseline comparisons.** The paper only compares ICFL against TopK SAEs. While TopK is a standard baseline in the mechanistic interpretability literature, the paper's claim that "the choice of dictionary learning algorithm matters" would be strengthened by including at least one additional dictionary learning baseline (e.g., an L1-regularized SAE or K-SVD). The observed improvements over TopK could partially reflect known limitations of TopK (e.g., dead features) rather than advantages of ICFL specifically. Adding one baseline would substantially increase confidence in the method-specific claims.

- **No error bars or measures of variability.** Every figure in Section 6 reports point estimates without confidence intervals, standard deviations, or results across random seeds. Training SAEs involves stochasticity (random initialization, batch sampling, random resets). While single-run evaluation is common in the SAE literature at this scale (40M tokens, 300k iterations), the reported differences—particularly the modest selectivity gaps in Figures 2d–2f and 3e—would be more convincing with even basic standard errors.

- **Ambiguity in the selectivity computation pipeline.** (a) The selectivity analysis uses center crops (§6.1: "extract from every image a feature vector using the center crop") while the linear probing analysis uses well-level aggregated representations (§5: "mean over tokens from all 36 non-edge crops"). This discrepancy is never explained or justified, making it difficult to connect the selectivity results to the information-preservation results. (b) The definition of "active" for ICFL features is not stated. The selectivity score is defined as "% of times that the feature is active" — for TopK SAEs, the top-K values are non-zero by construction, but for ICFL features (which are also sparse codes), it is unclear whether "active" means > 0 or some other threshold.

- **CellProfiler comparison methodology has limitations.** CP features are binarized by thresholding at quantiles, which discards magnitude information. The paper is transparent about this (§6.2), but the comparison would be fairer if both methods used the same type of activation criterion. The binarization step could compress or distort the selectivity comparison in ways that are hard to assess.

- **PCA whitening vs. ICFL contributions partially confounded.** Figure 2a shows all four combinations (ICFL ± PCA, TopK ± PCA), but the paper's selectivity-focused figures (2d–2f, 3e–3g) primarily show the full method (ICFL + PCA) vs. TopK. It is unclear how much of the selectivity gain is attributable to PCA whitening alone versus the ICFL algorithm itself — a PCA + TopK condition in the selectivity plots would disentangle this.

### Trivial

- Table 1 caption states results are shown "for both TopK and ICFL with and without PCA whitening" (implying four conditions), but the table (rendered as an image) may only show two labeled rows. The row labels should explicitly indicate the PCA condition for each method.

- The paper does not ablate the inner parameters of ICFL (J = number of residual iterations, k = atoms per iteration). These are fixed to match a max sparsity of 100, but their individual impact on selectivity and reconstruction quality is not explored.

## Nice-to-Haves

- A quantitative audit of the qualitative features: e.g., how many of the top-100 most selective features produce token heatmaps that a domain expert would rate as biologically plausible. This would raise the qualitative analysis from anecdote to evidence.
- An ablation showing whether the linear probing drop on Tasks 3 and 5 (many perturbations, functional groups) is due to information loss or linear unintelligibility of the underlying representations.
- A table comparing the number of dead features for all four conditions (TopK ± PCA, ICFL ± PCA) explicitly labeled.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Missing citations to the dictionary learning literature (Mairal, Elad, Aharon, etc.)"** — Removed per policy: missing related works should not be flagged as a weakness. The paper does cite Mallat & Zhang (1993) for OMP, and is positioned within the SAE/mechanistic interpretability literature, not the classical sparse coding literature.
- **"Qualitative analysis is anecdotal / cherry-picked"** — Removed because the paper's title ("Towards scientific discovery") and framing (§8: "these sparse features are clearly incomplete") explicitly acknowledge this is a proof-of-concept. The qualitative examples are illustrative, not claimed as systematic validation.
- **"Figure 2a does not disentangle PCA and ICFL"** — The caption states the figure shows "ICFL and TopK SAEs in combination with PCA whitening and with out," which implies all four conditions are present. The underlying concern (would PCA+TopK match ICFL+PCA?) is partially addressed by the data already shown; the remaining ambiguity about selectivity-specific plots is retained in Minor.

## Novel Insights

The collation of reviews surfaces one observation not emphasized in the paper: the PCA whitening step is doing substantial work, potentially more than the ICFL algorithm itself. The harsh critic notes that Figure 2a shows a clear performance drop without PCA for both methods, and the paper confirms this in text. This raises the substantive question of whether a simpler approach — PCA whitening + a standard dictionary learning baseline — could approach the full method's performance. The paper would benefit from directly addressing this question rather than leaving it implicit. Additionally, the disconnect between the center-crop selectivity pipeline and the well-aggregated linear probing pipeline suggests the paper is effectively evaluating two different model behaviors, which weakens the narrative that selectivity and information preservation are coherently linked.

## Suggestions

1. Add at least one additional dictionary learning baseline (e.g., L1-regularized SAE) to the selectivity and linear probing comparisons.
2. Report standard deviations from multiple random seeds for the three core experiments (linear probing accuracy, reconstruction cosine similarity, average selectivity).
3. Explicitly define the activation threshold for ICFL features in the selectivity computation, and reconcile the center-crop vs. well-level aggregation discrepancy.
4. Include PCA + TopK conditions in all selectivity figures (at minimum Figures 2d–2f) to disentangle the contributions of PCA whitening vs. ICFL.
5. Clarify Table 1 row labels to explicitly show the PCA condition for each method.

## Score and Decision

The paper makes a genuine contribution by demonstrating that dictionary learning can extract biologically meaningful concepts from microscopy foundation models — a novel and timely application. ICFL is a clean algorithmic contribution that solves the dead-feature problem, and the PCA whitening preprocessing is well-motivated. The quantitative comparison to CellProfiler features is a strong benchmark. However, the experimental rigor is uneven: limited baselines, no error bars, and some ambiguity in the selectivity pipeline prevent the method-centric claims from being fully convincing. These issues are addressable in revision and do not undermine the paper's core contributions. The paper is a solid cross-disciplinary demonstration that opens a promising direction.

**Score:** 6.5

**Decision:** Accept

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>