Now I have a thorough understanding of the paper and can verify each claim. Let me write the final consolidated review.

## Summary

This paper presents an empirical study applying topological data analysis (persistent homology and Betti curve similarity) to analyze the functional graphs of convolutional neural networks. Four CNN architectures (extended LeNet, AlexNet, VGG-16, ResNet-18) are trained on 30 disjoint 10-class subsets of ImageNet; their neuron activations are reduced via k-means++, converted to Vietoris–Rips complexes, and compared using Betti curve similarity (BCS) across models, datasets, and training epochs. The claim is that BCS can distinguish models and detect representational differences that accuracy alone does not reveal.

## Strengths

1. **Evidence that BCS distinguishes different CNN models and captures dataset-specific differences.** The paper shows that for subset 11, ResNet-18 and VGG-16 have "very low" BCS (Figure 6), and this low similarity correlates with ResNet-18 outperforming VGG-16 by ~5% on test accuracy (Figure 7). For subset 27, BCS reveals high similarity among ResNet-18, VGG-16, and AlexNet, while all differ from extended LeNet — a pattern not visible from accuracy alone (Figures 8–9). This supports the claim that BCS provides information complementary to standard metrics.

2. **Evidence that BCS captures training dynamics.** For ResNet-18 compared with itself across epochs, temporal similarity is low at initialization and increases over training (Figure 4), with the largest shift occurring between epochs 0 and 10 where accuracy rises fastest. Across-model similarity at the same epoch also increases over training (Figure 5), hinting at convergence of functional graph structure.

3. **Systematic experimental design.** Training four distinct CNN architectures on 30 disjoint 10-class subsets of ImageNet provides a reasonably broad basis for comparing functional graphs across models and datasets.

## Weaknesses

### Fatal
None.

### Major

1. **The k-means++ dimensionality reduction (to 1000 points) is not empirically validated, undermining confidence in the topological analysis.** The paper acknowledges that silhouette scores show the clusters are "poorly separated" and that neuron activation means are "not well-separated." However, no sensitivity analysis is performed on the choice of k (500, 1000, 2000), and no comparison is made between PH on the reduced set and PH on the original full activation space (even for a single small network/layer where the original might be tractable). The justification that local structure is "more representative of overfitting" is cited from prior work (Corneanu et al., 2019) rather than demonstrated in this setting. Since every subsequent BCS result depends on this reduction, the absence of validation is a significant gap. The paper would be substantially stronger with even one direct validation experiment.

2. **No baseline comparisons to simpler similarity measures.** BCS is introduced as a tool for comparing DNNs, but it is never benchmarked against alternatives: the ℓ∞/Frobenius distance between the raw Spearman correlation matrices, Wasserstein distance between activation distributions, or even clustering based on accuracy. Figures 4–8 show that BCS varies across models, epochs, and subsets, but without a baseline it is impossible to tell whether these variations add information or simply reproduce patterns already captured by simpler metrics. The central claim that BCS provides a "more nuanced understanding" is unsupported without such comparisons.

3. **Insufficient statistical reporting.** The study uses 30 subsets, yet all averaged results (Figures 4–6, 8) are presented without error bars, standard deviations, confidence intervals, or any indication of variance across subsets. Given that the paper notes "for certain models and subsets, the similarity was quite low," it is unclear whether the reported trends are robust or driven by a few outliers. Standard deviations or per-subset scatter plots are needed to assess reliability.

### Minor

1. **The distance function d_ρ = √(1 − |ρ|) is stated to satisfy "all properties of a metric except for positivity," but the triangle inequality is not guaranteed for this form using Spearman correlation.** The Vietoris–Rips complex can be defined for non-metric distance matrices, but the paper should clarify whether the Giotto-tda implementation has any metric requirement. This does not invalidate the results but is a technical inaccuracy.

2. **Using identical hyperparameters (learning rate, batch size, weight decay) across four very different architectures** (from extended LeNet to ResNet-18) raises the question of whether observed functional differences partly reflect suboptimal training for some models rather than architectural differences alone. The paper notes this is "reasonable for comparability" but does not discuss the trade-off.

3. **The conclusion states BCS "could be utilized in ablation studies and hyperparameter tuning," but no demonstration or sketch of how this would work is provided.** This overstates what the evidence supports and should be tempered or accompanied by a concrete example.

4. **Averaging BCS across all epochs for cross-model comparisons (Figures 5, 8)** may obscure temporal dynamics that the paper itself highlights as important (Figure 4). Presenting per-epoch similarity for these cross-model comparisons would be more informative.

### Trivial

- The random seed for k-means initialization is not specified (only the data subset seed is given as 1234), introducing a minor reproducibility gap.
- No discussion of the sensitivity of PH/Betti curves to the choice of filtration parameter range [0,1] or the computational cost scaling to larger networks.

## Nice-to-Haves

- A sensitivity analysis on the number of k-means clusters (e.g., k=500, 1000, 2000) to show qualitative stability of BCS patterns.
- A comparison between BCS and a simple baseline such as the ℓ∞ distance between raw Spearman correlation matrices for the same model pairs — this would directly test whether PH adds value.
- Correlation of BCS patterns with an established representation similarity measure (e.g., CKA) to anchor the results in the broader literature.
- A brief limitations paragraph discussing the sensitivity of PH to parameter choices and the interpretability of Betti numbers in terms of network behavior.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *Criticism about using the nearest neuron to centroid rather than the centroid itself*: A minor implementation choice; using a real activation point is arguably more principled than a synthetic centroid.
- *Criticism that the paper should discuss whether local structure preservation matters*: The paper already addresses this by citing Corneanu et al. (2019) and arguing global structure is the focus.
- *Criticism about Section 3 averaging "across epochs" being uniformly problematic*: Figure 4 explicitly shows temporal dynamics, so the paper does not wholly obscure them; Figures 5 and 8 average across epochs for cross-model comparison, which is a different use case (minor weakness, moved above).

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add a validation experiment for the k-means reduction: compute PH on the full (unreduced) activation set from at least one small network/layer and compare the resulting Betti curves to those obtained after reduction. Even a single-case comparison would significantly strengthen the evidence.
2. Add error bars (e.g., ±1 standard deviation across the 30 subsets) to all averaged plots, or provide per-subset scatter plots.
3. Add at least one baseline comparison: compute the ℓ∞ distance between the raw Spearman correlation matrices (before PH) for the same model pairs and compare it to BCS. If the two are highly correlated, the added value of PH is questionable; if they diverge, that divergence is the novel contribution and should be highlighted.
4. Temper the conclusion's claim about "ablation studies and hyperparameter tuning" unless a concrete sketch of how BCS would guide these is provided.

## Score and Decision

The paper tackles an interesting question — whether topological summaries of activation patterns can reveal structure in DNN representations. The experimental design is reasonably systematic (4 models × 30 subsets × 7 epochs). However, the three major weaknesses — unvalidated dimensionality reduction, no baseline comparisons, and insufficient statistical reporting — are not fatal, but they collectively prevent the paper from making a convincing case. The core idea is worth pursuing, but the evidence as presented does not yet support the claim that BCS provides meaningful insight beyond what simpler approaches would capture.

A major revision addressing the validation of the reduction and adding baselines could turn this into a solid empirical contribution.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>