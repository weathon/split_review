Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper introduces the Wasserstein distance (WD) of a neuron's output distribution to a Gaussian as a metric for identifying "entangled" neurons in LLMs, and presents an empirical study showing that these "Wasserstein neurons" are disproportionately sensitive to weight sparsification. It also proposes Sparse Expansion, an experimental framework that clusters inputs and applies per-cluster SparseGPT pruning, which the authors use as a tool to study how reducing input diversity improves sparse reconstruction of these neurons. The core contribution is the empirical finding that a small fraction of neurons identified by WD play an outsized role in maintaining model accuracy under sparsity.

## Strengths

- **Novel metric with clear empirical grounding.** The WD-to-Gaussian metric is simple, principled, and computationally efficient. The paper validates it by showing strong correlation with the proposed mapping difficulty (MD, Figure 2e), and demonstrates that it identifies a small set of neurons that behave differently from the majority — a valuable descriptive tool.

- **Sparsity-critical neurons are convincingly identified.** The core experiment (Figure 3a) is clean and informative: sparsifying just the top 3% of neurons by WD degrades perplexity far more than sparsifying the same number of neurons selected by mean output, variance, weight magnitude, or at random. This is replicated across multiple selection criteria and evaluated on multiple benchmarks (Figure 3b-d), providing robust evidence that these neurons matter disproportionately under sparsity.

- **Convergent evidence from Sparse Expansion.** The finding that Sparse Expansion preferentially recovers performance on WD-identified neurons (Figure 5a), and that WD-weighted and MD-weighted metrics decrease for these neurons post-expansion (Figures 5b, 5c), provides convergent validation that the WD metric captures something computation-relevant rather than being a statistical artifact.

- **WD is shown to predict improvement better than alternative metrics.** Figure 7 compares WD against output mean, output variance, and optimal GMM components, with WD yielding the highest R². While the comparison set is not exhaustive, the GMM baseline is a reasonable competitor that tests whether multi-modality alone explains the effect — and WD outperforms it substantially.

## Weaknesses

### Major

- **Sparse Expansion performance comparisons are presented on unequal footing.** The paper compares Sparse Expansion (which stores 16 sparse weight matrices per layer plus a router) against SparseGPT and Wanda (single sparse matrices) using perplexity at the same nominal sparsity level. At 16 clusters, Sparse Expansion uses ~16× the parameter storage of a single sparse matrix, so the comparison is not resource-equivalent. While the paper acknowledges this in §3.6 ("likely not practically implementable without further optimizations"), the performance lead in Figure 9 still creates a misleading impression. The contribution would be better served by framing Sparse Expansion purely as an analysis tool — the performance comparisons, as presented, overstate practical relevance.

### Minor

- **The entanglement narrative is conceptually motivating but not independently validated.** The paper defines entanglement operationally through MD (mapping difficulty), shows WD correlates with MD, and concludes WD measures entanglement. However, MD itself is never validated against an independent ground-truth of polysemanticity (e.g., from sparse autoencoders or controlled feature analysis). The paper's core empirical finding (WD neurons are sparsity-critical) stands independently, but the framing implies more conceptual validation than is delivered. The claims about "entanglement" would be strengthened by showing that high-WD neurons actually respond to multiple distinct features.

- **Limited statistical rigor for key claims.** Correlations (Figures 2e, 7) are presented without confidence intervals or significance tests. The "linear front" in Figures 8b-c is identified visually without quantification. Median decreases in WD and MD (Figure 5) are given without error bars or variance across seeds/calibration sets. While these results are still interpretable, the absence of basic uncertainty quantification weakens the evidentiary standards.

- **Missing experimental details.** The paper does not state: (a) the number of PCA components used before K-means clustering, (b) how many samples are used to compute output distributions (affecting WD/MD reliability), (c) whether the number of clusters (fixed at 16) was ablated or tuned. The PCA/K-means pipeline is not ablated — it is unclear how sensitive the results are to the dimensionality reduction step.

- **Potential confound in Sparse Expansion's WD/MD decrease.** The paper attributes the decrease in weighted WD and MD to "disentanglement," but an alternative explanation is that each expert simply sees fewer inputs, and any split — even random — would reduce distributional complexity. The paper does not control for this by comparing against a random-input-split baseline.

- **"Capability charts" (Figure 3b-d) lack y-axis labels in the caption.** The metric on the y-axis is not defined, making these figures hard to interpret independently.

### Trivial

- The choice of median (rather than mean) as the normalizer N_y in Equation 2 is not justified.
- The number of PCA components for dimensionality reduction before K-means is unspecified.
- The claim that Wasserstein neurons "arise relatively early on in training" (within 10-20B tokens) is stated without confidence bounds or systematic tracking.

## Nice-to-Haves

- Validate the MD metric against SAE-discovered polysemantic features to ground the "entanglement" label.
- Add a control experiment for Sparse Expansion: split inputs randomly (not by clustering) and measure whether weighted WD/MD still decreases.
- Report correlations with bootstrapped confidence intervals and/or permutation test p-values.
- Ablate the number of clusters (e.g., 2, 4, 8, 16, 32) to show sensitivity.
- Compare WD against additional distributional metrics (kurtosis, skewness, entropy) for the "best predictor" claim.

## Removed Points

- **"Connection to mechanistic interpretability is overstated"** — The paper explicitly frames its contribution as studying entanglement in the context of sparsity, not delivering human-interpretable features. This is not overclaimed relative to what is actually presented.
- **"Does not discuss whether normalization step removes informative signal"** — The paper clearly explains the normalization rationale (shape vs. scale/location). This is a design choice, not an oversight.
- **"GMM comparison is an odd choice"** — Modeling a distribution's optimal number of Gaussian components is a reasonable baseline for testing whether multi-modality explains improvement. The criticism misunderstands the comparison.
- **"§3.5 is speculative and adds little"** — Connecting empirical observations to theoretical bounds on superposition is a legitimate contribution for this type of empirical paper.
- **"Missing appendix content"** — The appendix exists in the original submission; the parser stripped it. These are not author errors.
- **Sample size concerns about median stability** — The median is more robust than the mean to small samples, not less. This criticism is factually backwards.
- **"§5 does not discuss metric's specificity"** — This is a minor omission that does not affect the paper's contribution.

## Novel Insights

The most valuable insight from the reviews — not fully articulated in the paper itself — is that the WD-to-Gaussian metric could serve as a practical diagnostic tool for pruning-aware architecture design, independent of whether the "entanglement" narrative holds up mechanistically. The reviewers collectively surface a tension between the paper's two framing devices (entanglement theory vs. compression performance) and suggest that leaning fully into the former (as an empirical study of a novel metric for neuron importance under sparsity) would resolve most of the criticisms. The correlation between WD and sparsity-sensitivity is well-supported; the remaining issues are primarily about how the work is framed and presented, not about the validity of the core empirical findings.

## Suggestions

1. **Reframe Sparse Expansion as an analysis tool, not a compression method.** Remove or substantially qualify the performance comparisons against SparseGPT/Wanda, or add an iso-resource comparison (e.g., fix total memory footprint). The paper is stronger when read as an empirical study of entanglement → sparsity-sensitivity, not as a new compression technique.

2. **Add uncertainty quantification.** Report bootstrapped confidence intervals for the correlation coefficients in Figures 2e and 7. Add error bars to the median WD/MD decreases in Figure 5. These are small changes that would substantially improve evidentiary quality.

3. **Acknowledge and control for the confound in Sparse Expansion's disentanglement effect.** Compare against a baseline where inputs are split randomly (not by clustering) before applying per-expert SparseGPT, to show that the clustering itself — not just fewer inputs per expert — drives the improvement.

4. **Specify the missing experimental details:** PCA components, sample sizes for distribution estimates, ablation of cluster count.

5. **Tone down the "entanglement" claims** or add validation against an independent ground truth (e.g., SAE-discovered features). The core finding (WD neurons are sparsity-critical) does not depend on the entanglement framing and would be equally valuable presented as "a metric for identifying sparsity-sensitive neurons."

## Score and Decision

This paper makes a genuine contribution: it identifies a simple, computationally cheap metric (WD to Gaussian) that flag neurons disproportionately important under sparsity, and provides convergent empirical evidence across multiple models and experiments. The core finding is novel and well-supported. The main weaknesses — the unfair Sparse Expansion performance comparison and the lack of statistical rigor — are addressable presentation/analysis issues, not fatal flaws that invalidate the contribution. The entanglement narrative is motivating rather than essential to the empirical result.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>