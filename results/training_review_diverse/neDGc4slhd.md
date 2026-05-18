Now I have thoroughly cross-checked all reviewer claims against the paper. Let me compose the final review.

## Summary

This paper proposes using Betti curve similarity (derived from persistent homology, a tool from topological data analysis) to compare the global functional graphs of deep neural networks. The authors train four CNN architectures (extended LeNet, AlexNet, VGG-16, ResNet-18) on 30 disjoint 10-class subsets of ImageNet, extract neuron activations, reduce them via k-means++, compute persistent homology, and compare Betti curves across models, epochs, and data subsets. The central empirical findings are that Betti curve similarity increases during training (indicating convergence of functional structure) and varies meaningfully across different model architectures and data subsets in ways not captured by accuracy alone.

## Strengths

1. **First application of Betti curve similarity to compare DNN functional graphs across datasets and epochs.** As stated in the paper (Section 2.5), this is the first time Betti curve similarity has been used in this setting. The empirical results (Figures 4–9) concretely demonstrate that the metric distinguishes models, tracks training dynamics, and detects diverging internal representations.

2. **Thorough and reproducible methodology.** The paper specifies all key design choices: 30 disjoint 10-class subsets (seed 1234), four CNN architectures, training hyperparameters (Adam, lr=0.001, weight decay 0.0005, 60 epochs), k-means++ reduction to 1000 clusters, and the Giotto-tda Vietoris–Rips implementation. Computational resource details and average runtime (66 minutes per experiment) are reported, enabling replication.

3. **Empirical evidence that Betti curve similarity captures convergence of functional structure during training.** Figure 4 shows that similarity between ResNet-18 at epoch 0 and later epochs increases over training, with the largest jump from epoch 0 to 10 coinciding with the steepest accuracy gain (Figure 2). The convergence of adjacent-epoch similarity supports the claim that the method reveals the evolution of global functional graphs.

4. **Cross-validation with accuracy reveals information not available from accuracy alone.** For subset 11, Figure 6 shows low Betti curve similarity between ResNet-18 and VGG-16 despite both achieving reasonable accuracy, while Figure 7 shows only a 5% accuracy gap. For subset 27, Figure 8 shows high similarity among ResNet-18, VGG-16, and AlexNet but low similarity with LeNet, while Figure 9 shows distinct accuracies for all four models. These examples demonstrate that the topological metric captures representational differences that accuracy alone does not.

5. **Systematic experimental design with 4 architectures × 30 subsets × 7 epochs.** The use of 30 statistically sampled disjoint subsets provides a reasonably broad experimental canvas, and the four architectures span sufficiently different topological properties (e.g., residual connections in ResNet-18) to enable comparative analysis.

## Weaknesses

### Major

1. **No comparison against baseline or existing representational similarity measures.** The paper's central value proposition is that Betti curve similarity provides a useful tool for comparing DNN representations. Yet the study never compares this TDA-based similarity against any existing representational similarity measure (e.g., CKA, SVCCA, PWCCA, RSAD) or even a simple non-topological baseline (e.g., average pairwise Spearman distance in the reduced space, or the infinity norm of the raw distance matrix difference). Without this comparison, the reader cannot determine whether the *topological* summary adds value over simpler approaches. The observations (similarity increases during training, varies across subsets) might also hold for non-topological correlation-based distances. This is the single most critical gap: for a method-application paper, the value of the method must be demonstrated relative to existing alternatives, not merely asserted.

2. **k-means++ reduction is not validated for stability and introduces uncontrolled distortion.** The paper itself acknowledges (Section 2.3) that silhouette scores show poor cluster separation. The argument that "local structure is not as important as global structure" is plausible but unsupported. No sensitivity analysis is performed — no variation of the number of clusters (k), no comparison with other reduction methods (random sampling, PCA), no check that Betti curves are stable under different k-means random initializations. Since the entire TDA pipeline depends on this reduction, the observed patterns could be artifacts of the stochastic approximation rather than properties of the true functional graph.

### Minor

3. **No error bars, confidence intervals, or statistical significance tests.** Figures 4–6 and 8 show only curves (apparently averages across 30 subsets) without any measure of variance. The paper claims 30 subsets provide a "statistically significant sample size" (Section 2.1) but never computes standard deviations, confidence intervals, or performs hypothesis tests. Without this, the reader cannot assess whether observed differences between models or epochs are reliable or could arise from noise. The paper also does not test the null hypothesis that Betti curves are indistinguishable across models.

4. **Infinity norm choice for Betti curve similarity is not justified.** The similarity is defined as the infinity norm of the difference between two Betti curves (Section 2.5). The infinity norm is sensitive only to the single largest vertical gap; an L1 or Wasserstein distance would capture the overall difference in shape across all thresholds. This choice may mask relevant patterns or amplify irrelevant ones. No discussion or justification is provided.

5. **New contributions relative to Corneanu et al. (2019) are not itemized.** The paper states it "modifies and adds upon" this prior work (Section 1) and later notes that this is the first application of Betti curve similarity to DNN comparison across datasets and epochs (Section 2.5). However, the exact novel elements are never explicitly listed. The key innovations (Betti curve similarity rather than raw persistence diagrams, cross-dataset comparison, systematic multi-architecture comparison) should be clearly delineated.

6. **Only anecdotal evidence that Betti curve similarity provides information beyond accuracy.** The subset 11 and 27 examples are suggestive but the paper does not systematically analyze whether Betti curve similarity correlates with accuracy or provides orthogonal information. A simple correlation analysis across all 30 subsets or a test of whether Betti curve similarity predicts something about transferability/generalization would substantially strengthen the claims. Without this, the "information beyond accuracy" claim rests on two isolated examples.

7. **No discussion of whether higher homology dimensions (2, 3) are meaningful for 1000 points.** With only 1000 points in the reduced space, higher-dimensional holes (dimension 2 or 3) are unlikely to be statistically meaningful, yet the paper presents results for dimensions 0–3 without acknowledging this limitation or justifying their inclusion.

### Trivial

None. (Typographical and formatting artifacts are parser-related, not author errors.)

## Nice-to-Haves

- A comparison of Spearman vs. Pearson correlation for constructing the distance metric, to assess sensitivity of the topological features to this choice.
- A discussion situating the approach in the context of existing representational similarity literature (CKA, SVCCA, etc.), even if only briefly.
- Systematic analysis correlating Betti curve similarity with accuracy differences across all 30 subsets.

## Removed Points

These points were flagged during review but are removed or downgraded per the review guidelines:

- **"Paper does not distinguish models better than accuracy itself"** — Kept but downgraded to Minor (#6 above). The paper does provide partial evidence (subset 11 and 27 examples), but the claim is not systematically examined.
- **"Missing related work section"** — Removed per hard rule (DO NOT mention missing related works).
- **"Missing hypothesis tests"** — Merged into Minor weakness #3 (no error bars / statistical inference).
- **"Modifications from Corneanu et al. not clearly stated"** — Kept as Minor weakness #5; the paper does partially state the novelty but does not itemize it.
- **"Spearman vs Pearson not compared"** — Moved to Nice-to-Haves; this is a design exploration rather than a core flaw.

## Novel Insights

The reviews converge on the observation that this is a well-executed empirical demonstration of a plausible idea, but the paper systematically avoids the hard validation question: does the topology actually add value? The harsh reviewer correctly identifies that the paper's central gap is the absence of baselines, while the strength finder correctly notes that the observations are novel and the methodology is reproducible. The tension between these perspectives reveals that the paper is caught in a middle ground — it has done enough to be interesting but not enough to be convincing as a research contribution. The most actionable insight is that the paper's own evidence (subset 11 and 27) actually undermines the "accuracy alone" framing: if the goal is to show that Betti curve similarity provides information beyond accuracy, the authors should test this systematically rather than anecdotally. The paper would also benefit from asking itself the harder question: "What can you do with Betti curve similarity that you cannot do with a simpler non-topological method?"

## Suggestions

1. **Add a baseline comparison.** Compute a simple non-topological similarity measure (e.g., the infinity norm of the difference between the raw Spearman distance matrices) and show that Betti curve similarity provides information not present in this baseline. If it does, explain what topological structure the homology dimensions capture. This single experiment would address the paper's largest weakness.

2. **Validate k-means++ stability.** Run the full pipeline with different k-means random seeds for a few representative models/subsets and show that resulting Betti curves and similarities have low variance. Also vary k (e.g., 500, 1000, 2000) to assess sensitivity. Without this, the reader cannot trust that the patterns reflect the networks rather than the reduction.

3. **Add error bars to all averaged figures.** With 30 subsets, standard deviations can be computed and shown as shading or ribbons. This is standard practice for empirical studies and would immediately strengthen credibility.

4. **Run a systematic correlation analysis.** Across all 30 subsets, compute the correlation between Betti curve similarity and accuracy difference to determine whether the topological metric provides orthogonal information.

5. **Justify the infinity norm choice** or provide results with alternative distance metrics (L1, Wasserstein) for comparison.

## Score and Decision

This paper presents a plausible application of TDA to DNN analysis with a thoughtfully designed experimental setup. The core observations (functional convergence during training, model distinguishability, subset-specific patterns) are interesting and potentially useful. However, the paper's central contribution is not adequately validated: the Betti curve similarity is never compared against any baseline or existing representational similarity measure, leaving the reader unable to assess whether the topological summary adds value over simpler approaches. The k-means++ reduction is not validated for stability despite acknowledged poor clustering. Combined with the absence of error bars and statistical inference, these gaps mean the paper, in its current form, does not meet the standard for acceptance as a research contribution. Substantial additional validation experiments would be needed to establish the method's value.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>