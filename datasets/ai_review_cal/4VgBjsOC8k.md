- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 3, 8, 8
I've now thoroughly verified each claim against the paper. Here is my consolidated review.

---

## Summary

This paper conducts a large-scale empirical analysis of trained depthwise convolutional kernels from modern DS-CNN architectures (ConvNeXt, ConvNeXtV2, MobileNet, EfficientNet, etc.). By training an autoencoder with a 1D bottleneck on millions of kernels, the authors discover that these kernels cluster into a small set (∼10) of recurring, interpretable spatial patterns that visually resemble Difference-of-Gaussian (DoG) functions and their first/second-order derivatives. The patterns persist across all layers (not just early ones), remain consistent across model scales and training datasets, and achieve >97% classification coverage on the best-performing architectures.

## Strengths

- **Large-scale, cross-architectural analysis**: The study compiles over one million kernels per kernel size from 15+ models including ConvNeXt, ConvNeXtV2, HorNet, MogaNet, ConvMixer, MobileNet, and EfficientNet (Section 3, Table 1). This breadth far exceeds prior work that focused on isolated models or early layers only.

- **Pattern persistence throughout all layers**: Unlike regular convolutions, where interpretability degrades in deeper layers, the identified DoG-like and cross-shaped patterns are shown to persist across all layers of DS-CNNs (Figure 8). The analysis of layer-wise proportions reveals systematic shifts (e.g., cross patterns increasing in later layers) that are descriptively informative.

- **Consistency across model scales and datasets**: Cluster proportions remain stable across ConvNeXt variants (tiny, large, huge) and training sets (ImageNet-1k, ImageNet-22k) as shown in Figure 9, indicating the patterns are an architectural property of DS-CNNs rather than artifacts of a specific training configuration.

- **Quantitative internal consistency check**: The boxplot of total activation per cluster (Figure 12) shows that first-derivative clusters have near-zero mean activation, which is consistent with the symmetric nature of DoG derivatives. This provides an independent sanity check linking the qualitative labels to measured statistics.

## Weaknesses

### Fatal

None.

### Major

- **DoG similarity is asserted qualitatively, without quantitative verification.** The paper's headline claim — that the discovered clusters "resemble" DoG functions and their derivatives — rests on manual visual inspection of the decoder's reconstruction spectrum (Section 4.2: "We manually assign labels to the most prominent clusters, based on their visual patterns"). No quantitative similarity metric (cosine similarity, mean-squared error, or projection coefficient) is computed between cluster centroids and mathematical DoG basis functions. The total-activation boxplot (Figure 12) provides a partial sanity check for the first-derivative clusters, but this does not directly measure DoG-likeness. Without a quantitative link, the biological claim ("echo[ing] the foundational models neuroscientists have long proposed for the vision systems of mammals") is weaker than the paper's rhetoric suggests.

- **Clustering methodology lacks validation metrics and baselines.** The analysis relies entirely on a 1D-bottleneck autoencoder with a manually tuned threshold (0.3 for 7×7, 0.2 for 5×5). No standard clustering quality metrics (silhouette score, Davies–Bouldin index) are reported. More critically, no comparison is made to alternative approaches such as k-means on raw filter vectors, spectral clustering, or clustering in a higher-dimensional latent space (e.g., 2D or 3D code with subsequent clustering). The PCA plot (Figure 4) provides suggestive independent evidence of cluster structure, but it is not used quantitatively. Without baselines, it is unclear whether the 1D bottleneck is revealing genuine structure or imposing an ordering artifact.

### Minor

- **No comparison to untrained / randomly initialized depthwise kernels.** To establish that the observed patterns are learned and not an artifact of the kernel-size, initialization scheme, or preprocessing, the analysis should include untrained depthwise kernels at the same sizes. The paper compares regular CNN to DS-CNN kernels (Figure 2) but never isolates the effect of training from the architecture itself.

- **Threshold selection (0.3 / 0.2) is not rigorously justified.** The paper provides a brief rationale (line 225: "Using stricter threshold for 5×5 kernels improves robustness because lower dimensional spaces tend to have closer vectors angularly"), but there is no knee-point analysis, ablation study, or distribution plot showing how classification rates vary with threshold choice. The reported "Filters Clustered" percentages in Table 1 are therefore threshold-dependent, and the degree of that dependence is uncharacterized.

- **Biological framing slightly exceeds the evidence.** The paper describes the results as "a bridge between artificial and biological visual processing systems" and "echo[ing] the foundational models neuroscientists have long proposed." The similarity to DoG derivatives is visually plausible, and the neuroscience citations (YoungDoG, rodieck_1965) are appropriate, but the evidence is purely morphological — no functional comparison (orientation tuning, spatial frequency tuning) or quantitative match to biological receptive-field data is provided. A more measured framing would better match the paper's empirical scope.

- **Single training run per architecture.** All analyses use publicly available pre-trained weights. The paper does not assess run-to-run variability (e.g., different random seeds, training from scratch). It is possible that some of the observed cluster structure is specific to the standard training recipe rather than fundamental to DS-CNNs.

### Trivial

- The label "Filters Clustered" in Table 1 could be clarified — it refers to filters whose reconstruction cosine dissimilarity falls below threshold, not to the number of distinct clusters found.

## Nice-to-Haves

- Computing quantitative similarity between each cluster centroid and a dictionary of DoG derivative basis functions (varying scale, orientation, derivative order), then comparing these similarities against a random-filter baseline. This would directly convert the visual claim into a testable one.
- Repeating the analysis with a 2D or 3D autoencoder bottleneck + k-means to verify that the same cluster patterns emerge without the linear-ordering constraint.
- Releasing the trained autoencoder models and cluster assignment data to facilitate reproducibility and follow-up work.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"The paper does not compare its clusters to actual neuroscience data (e.g., receptive fields recorded from V1 or LGN)"**: This demands the paper address biological validation outside its stated scope as an ML interpretability study. The paper draws a visual parallel, not a functional biological equivalence.
- **"No code release" / reproducibility nitpicks about undisclosed implementation details**: Per instruction guidelines, these concerns about artifacts impractical to include in a submission are removed from consideration.
- **"Weight decay could be a trivial explanation"**: Speculative and not verified against evidence in the paper. The centering step removes the DC component that uniform shrinkage would primarily affect, and the observed zero-crossing structures are not trivially explained by L2 regularization.
- **"Clusters could be an artifact of decoder interpolation"**: Speculative. The paper provides random sample visualizations (Figures 5–7) from each cluster that match real filter appearances, not just decoder artifacts. The independent PCA plot (Figure 4) also shows cluster structure without using the decoder.
- **Generic concerns from the strength finder** about the "problem being important" or sycophancy — removed for lack of specific, citable content.

## Novel Insights

The two reviews together surface a key tension: the paper makes a genuinely interesting and well-supported empirical observation (DS-CNN kernels are highly structured into a small vocabulary of recurring patterns that persist across all layers), but the headline biological interpretation (that these patterns are DoG derivatives) rests on a qualitative visual link rather than a quantitative one. The most productive path forward is not to discard the observation but to strengthen the quantitative connection, which is straightforward to implement (cosine similarity to DoG bases) and would significantly increase the paper's impact.

## Suggestions

1. **Add a quantitative DoG similarity analysis**: For each cluster centroid, compute the maximum cosine similarity to a family of DoG derivative basis functions (varying σ, orientation, derivative order). Report the distribution and compare against random filter baselines and regular convolution kernels. This directly addresses the paper's weakest evidential link.
2. **Validate cluster stability**: Apply k-means directly to the centered, normalized kernel vectors (k=10) and compare the resulting centroids to the autoencoder-derived clusters. Report silhouette scores. If similar patterns emerge, the claims about "identifiable clusters" are substantially strengthened.
3. **Include untrained kernel baselines**: Show that randomly initialized depthwise kernels at the same size do not exhibit the same cluster structure, confirming that the patterns are learned.
4. **Tone down the biological framing**: Replace "bridge between artificial and biological visual processing" with "qualitatively similar to..." unless functional evidence is provided.
5. **Release the autoencoder weights and cluster labels** to enable independent verification and follow-up work.
