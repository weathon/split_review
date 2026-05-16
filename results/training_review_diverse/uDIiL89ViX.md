Now I have all the information I need. Let me compose my final consolidated review.

## Summary

The paper investigates whether dictionary learning can extract biologically-meaningful concepts from unsupervised microscopy foundation models (masked autoencoders trained on cell images). The authors propose a new algorithm, Iterative Codebook Feature Learning (ICFL), and combine it with PCA whitening on a control dataset. They show that sparse dictionary features correlate with cell types, genetic perturbations, and functional gene groups; that ICFL achieves higher feature selectivity and fewer dead features than standard TopK sparse autoencoders; and that the extracted features qualitatively match handcrafted CellProfiler features.

## Strengths

1. **Demonstration that DL extracts biologically-meaningful concepts from microscopy foundation models**: Figure 1 shows three learned features that correspond to distinct cellular morphologies (spindle-shaped cells, dense packing, small compact bright cells). This is the paper's core contribution—showing that unsupervised dictionary learning can recover interpretable biological patterns from a domain where little prior knowledge exists—and it is convincingly supported.

2. **ICFL+PCAWhitening improves selectivity and avoids dead features**: Figures 2d–2f show that ICFL features consistently achieve higher average and max selectivity scores than TopK SAE features across all five classification tasks. Table 1 reports ICFL+PCA yields 0 dead features (out of 8192) versus 243 for TopK+PCA. This directly supports the paper's central claim about ICFL's advantage.

3. **PCA whitening on a control dataset is shown to be crucial**: Figure 2a demonstrates that linear probing accuracy on reconstructions drops markedly without PCA whitening (e.g., ≈0.2 lower for Task 5), while with PCA whitening both methods nearly match the original representation's performance. This provides clear evidence for the pre-processing contribution.

4. **ICFL achieves higher reconstruction quality at matched sparsity**: Figure 2c shows ICFL consistently outperforms TopK at every sparsity level (e.g., ≈0.80 vs ≈0.75 cosine similarity at sparsity 100), supporting the algorithmic advantage described in Section 4.

5. **Unsupervised features quantitatively match expert-designed CellProfiler features**: Figures 3e–3g show near-identical maximum selectivity scores and a per-label Pearson correlation of r=0.71 between ICFL and 964 handcrafted CellProfiler features, validating that DL-extracted features capture patterns similar to those designed by domain experts.

6. **Qualitative analysis demonstrates biological interpretability at token level**: Section 7 provides compelling case studies (adherens junctions pathway, ALG-3 ER/Golgi localization, TSC-2 membrane signal) showing that feature heatmaps align with known biology and channel-specific stains.

## Weaknesses

### Fatal
None.

### Major

1. **The TopK SAE baseline comparison is not fully specified, leaving fairness unclear.** The paper claims ICFL avoids dead features and achieves higher selectivity than TopK SAEs, but does not state whether the TopK implementation included standard dead-feature mitigations (ghost gradients, as in the original Gao et al. (2024) TopK paper). Table 1 reports that TopK+PCA has 243 dead features (vs. 0 for ICFL+PCA), but if the TopK baseline was run without these known mitigations, the gap is inflated. The paper references Gao et al. (2024) for hyperparameter details ("similar to Gao et al. (2024), we observed that changing the learning rate has a limited impact"), which hints that their TopK implementation follows that work—where ghost gradients are standard—but this is never stated explicitly. This ambiguity weakens the central comparative claim. The authors should either confirm ghost gradients were used, rerun with them, or acknowledge the gap may shrink under optimal TopK tuning.

### Minor

2. **Selectivity scores lack statistical calibration.** With 8192 features and moderately unbalanced label sets (e.g., 1138 siRNA perturbations), some features will appear selective purely by chance. The paper reports only point estimates—no confidence intervals, permutation baselines, or significance thresholds are provided. While the relative comparison between ICFL and TopK is still meaningful (both use the same metric on the same data), the absolute interpretation of selectivity values (e.g., "moderate selectivity score of more than 0.1") is not grounded against a null distribution. A simple permutation-based null would calibrate the reader's expectations.

3. **Layer selection is partially circular for Task 5.** The paper states: "We selected this layer by finding the layer which maximized linear probing performance on the functional group task (described below) from the original embeddings." Task 5 (functional gene groups) is then used as one of the five evaluation tasks. While this does not affect the comparison between ICFL and TopK (both use the same layer), and the layer was selected on original (non-dictionary) embeddings rather than on reconstructions, it introduces optimism specifically for Task 5 results. The other four tasks are uncontaminated. Reporting results for an independently chosen layer (e.g., by maximum variance explained or using a held-out task) would strengthen robustness.

4. **PCA whitening details are underspecified.** The paper says "learn a PCA-and-centerscale transform on this control dataset" but does not state how many PCA components are retained or whether this is a full whitening or a dimensionality reduction. Since the comparison "with PCA" vs "without PCA" in Figure 2 varies something unspecified, reproducing these results requires additional clarity.

5. **The ICFL inner-loop feature learning step is vague.** The description says "learn the features z^(1) that best reconstruct x≈W_dec z^(1) using only these columns" but does not specify whether this is a least-squares solve (as in standard OMP) or a gradient-based inner loop. The paper references Algorithm 1 (presumably in the appendix), but the main text should at least clarify the optimization method for reproducibility.

6. **CellProfiler binarization is a rough approximation.** The binarization of continuous CellProfiler features by thresholding at quantiles α and 1−α to match ICFL's sparsity level conflates the sparsity level with the activation threshold. Since CP features are continuous and not designed to be sparse, the selectivity comparison under arbitrary binarization may not fully reflect CP's true discriminative power. The paper acknowledges this implicitly but could be more careful in interpreting these results.

7. **No variance or multi-seed reporting.** All quantitative results are reported as point estimates. While single-run evaluation is common in large-scale dictionary learning (training for 300k iterations on 40M tokens is expensive), the absence of error bars means the stability of the comparisons (especially for dead-feature counts and selectivity) is unknown.

### Trivial

8. **Qualitative feature selection is explicitly post-hoc.** The paper states "a feature we chose because it demonstrated a clear biological relationship" (Section 7.1). This is transparent but worth noting: the case studies are selected to be illustrative and do not prove most features are equally interpretable. The paper could add a sentence acknowledging this.

## Nice-to-Haves

- A computational cost comparison (training time, inference overhead) between ICFL and TopK SAE would help readers judge the practical trade-off.
- A direct test for batch effects (e.g., checking whether features selective for a perturbation remain selective in different experimental batches) would strengthen biological validity beyond the explicit batch-effect prediction task already included.
- Extending the ablation to compare ICFL vs TopK on selectivity and reconstruction *without* PCA (Table 1 appears to have this, but it is not discussed in the text) would further clarify the independent contribution of each component.

## Removed Points

The following points from the harsh review are removed with justification:

- **"The algorithm is said to be in Algorithm 1, but that algorithm is not present in the main text—this reliance on an appendix that is stripped from the review copy makes it impossible to evaluate completeness."** — Removed per the rule that criticisms about missing appendix content (stripped by the parser) should be removed. The full algorithm exists in the original submission's appendix.

- **Introduction motivation criticism ("aspirational but not specific")** — This is a stylistic/presentation preference, not a substantive weakness. The paper's motivation is clearly scoped: DL for scientific discovery in domains where text supervision is unavailable.

- **"The paper should also cover Y / domain Z / additional tasks"** style demands — The paper's scope is clearly defined (microscopy foundation models, five specific classification tasks). Requests to expand to other domains would turn the paper into a different contribution.

- **Criticism that the paper does not report "whether ICFL vs TopK in the absence of PCA for the selectivity and dead-feature metrics"** — Table 1 does include this comparison (TopK alone vs TopK+PCA vs ICFL+PCA). The paper references it.

## Novel Insights

The most interesting insight from the reviews is the observation that the layer selection protocol (optimizing for Task 5 linear probing on original embeddings) is a form of data-dependent pipeline design that, while not invalidating the ICFL-vs-TopK comparison, makes it harder to disentangle how much of the reported Task 5 selectivity arises from the method versus from the layer choice. A practical takeaway is that future work in this area should separate the layer selection task from the evaluation tasks, or use a general-purpose principle (e.g., maximum variance explained) to avoid any appearance of circularity. Beyond this, the reviews do not surface a genuinely novel perspective beyond the paper's own contributions.

## Suggestions

1. **Clarify the TopK implementation.** Explicitly state whether ghost gradients, feature resampling, or auxiliary reconstruction loss were used for the TopK baseline. If they were (as the Gao et al. reference suggests), say so. If not, rerun with these mitigations and report whether the dead-feature gap persists.

2. **Add a permutation-based null for selectivity.** Shuffle labels and recompute selectivity for all features; plot the null distribution alongside the real scores in Figures 2d–2f. This is a lightweight addition that would substantially increase confidence in the selectivity results.

3. **Specify the PCA whitening parameters.** State the number of components retained and whether dimensionality reduction occurs, so the preprocessing is fully reproducible.

4. **Clarify the ICFL inner-loop optimization.** Explicitly state whether z is obtained via least-squares (OMP-style) or gradient descent.

5. **Consider reporting multi-seed results** for at least the key comparison (Table 1 dead-feature counts, selectivity curves) to establish stability.

## Score and Decision

This paper makes a solid contribution: it demonstrates that dictionary learning can extract biologically-meaningful concepts from microscopy foundation models, proposes a new algorithm (ICFL) with a clear motivation (avoiding dead features via iterative residual pursuit), and shows that PCA whitening on a control dataset improves feature quality. The qualitative analysis is genuinely compelling. The weaknesses are real but addressable: the TopK comparison needs more transparency, and the selectivity scores need calibration. None of these issues invalidate the core claims—they mainly affect the precision with which those claims can be stated.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>