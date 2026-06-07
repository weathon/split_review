## Summary

The paper proposes IF-PCA+, an enhanced clustering algorithm that integrates diffusion-based manifold fitting (DMF) — applied both sample-wise and feature-wise — with a modified IF-PCA pipeline to improve subject clustering on high-dimensional genomic data. The method targets four specific limitations of IF-PCA (independence assumption, univariate feature testing, dropout noise sensitivity, linear model restriction). The evaluation covers 8 single-cell and 10 microarray datasets plus simulation studies, with ablation variants isolating each design choice.

## Strengths

1. **Well-motivated, targeted improvements over IF-PCA.** The paper identifies four specific limitations of IF-PCA (lines 17–22) and maps each to a corresponding component in IF-PCA+ (DMF for dropout noise and nonlinearity, dual manifold fitting for feature/sample correlations, modified IF-PCA for manifold-shaped data). This makes the methodological motivation explicit and testable.

2. **Five ablation variants isolate each design choice.** The paper defines nolog-IFPCA+, DMF-IFPCA, Yao2-IFPCA, n0-IFPCA+, and IF-PCA(W)+ (lines 137–145), each modifying a single component. This allows readers to attribute performance differences to specific algorithmic decisions (log transform, feature-wise fitting, DMF vs. Yao2, the n₀ threshold, and modified vs. original IF-PCA).

3. **Colon dataset provides a concrete sanity check for the modified IF-PCA.** Applying orthodox IF-PCA within the IF-PCA+ pipeline yields 0.516 accuracy, while the modified version achieves 0.838 (line 109). This isolates the contribution of the two modifications (removing feature-wise normalization and using K₀ = max{4,K} singular vectors) from the manifold fitting components.

4. **Simulation studies demonstrate large feature-selection improvements from dual manifold fitting.** In Settings 1 and 2 (independent and correlated signals), the combined IF-sf achieves perfect feature selection accuracy (1.0) versus 0.75 and 0.62 for standard IF. In the more challenging Settings 3 and 4 (dropout + nonlinearity), IF-sf achieves 0.40 and 0.58 versus 0.04 and 0.20 (Table 5). These are large, systematic improvements that directly support the paper's core claim about feature selection enhancement.

## Weaknesses

### Fatal

None.

### Major

1. **No uncertainty quantification for main results, despite 10-run repetitions.** The paper reports that each algorithm is run 10 times and averages are reported (line 177), but no standard deviations, standard errors, or confidence intervals are provided for Tables 2, 3, 4, or 5. Since K-means (random initialization) is used in the clustering step of every compared method, and several methods (DESC, IF-VAE) involve stochastic training, the variance around each reported number is essential for interpretation. Without it, the reader cannot judge whether IF-PCA+'s advantage on accuracy or its second-place ranking on ARI represents a stable difference or falls within run-to-run variation. The rank and regret aggregates inherit this same problem since they are derived from point estimates. This is a significant evidential gap that weakens confidence in the paper's central claims.

2. **Parameter sensitivity is entirely unexamined.** IF-PCA+ has three tuning parameters (n₀, knn_s, knn_f). The paper states that "selecting optimal values for n₀, knn_f and knn_s is difficult" (line 133) and provides fixed defaults depending on dataset type. However, no analysis is presented of how performance varies with these choices across a reasonable range of values. For a method whose practical adoption depends on ease of use, the absence of any sensitivity analysis leaves open the question of whether the reported results depend on fortuitous parameter settings.

### Minor

1. **Abstract slightly overstates the ARI findings.** The abstract says the method "outperforms several of the most competitive algorithms nowadays (including IF-PCA, DESC, Seurat) in terms of clustering accuracy **and** ARI." The paper itself reports that IF-PCA+ is ranked second on ARI (line 193). While the method may still outperform the three named methods individually on ARI, the bundling of accuracy and ARI in one "outperforms" claim is imprecise and could mislead a reader skimming the abstract. The introduction (line 27) is more careful — it separates the accuracy and ARI results — and the abstract should match this precision.

2. **DMF projection step (Eq. 61–64) is underspecified for exact reproduction.** The arg max is over a continuous parameter t defining points on the line from xᵢ to F(xᵢ). The paper does not state how this one-dimensional optimization is performed (line search? golden-section search? grid search? over what range of t? at what resolution?). While a reasonable practitioner could guess an implementation, the core algorithmic innovation should be specified precisely enough to reproduce without guesswork.

3. **Key numerical claim about neighborhood accuracy lacks supporting evidence.** The paper states that "diffusion-based SNN achieves an average neighborhood accuracy of 0.68, while the correlation-based SNN achieves only 0.34" (line 68), and claims this improvement is consistent across various 3D manifolds, but provides no citation, experimental setup, or visible supporting data for these specific numbers. Table 1 shows clustering accuracy improvement from the two combined DMF changes, which is a different claim. The 0.68/0.34 numbers are presented as evidence for the diffusion-based approach but are themselves unsubstantiated in the main text.

4. **Clustering accuracy metric is never explicitly defined.** The paper reports "clustering accuracy" and "clustering error" but never states how the predicted labels are aligned to true labels (presumably via Hungarian matching, which is standard). This should be made explicit.

5. **Feature selection accuracy metric in simulations has an ambiguity.** The metric counts influential features among the top 500 selected features. If the IF step retains fewer than 500 features, the denominator effectively changes. This should be clarified.

### Trivial

None.

## Nice-to-Haves

- A parameter sensitivity analysis for knn_s and knn_f across a reasonable range (e.g., knn_s ∈ {5, 10, 15, 20, 30}) would substantially strengthen practical applicability claims.
- The DMF projection optimization should be specified with its range and method (e.g., "golden-section search over t ∈ [0, 2]").

## Removed Points

These points were flagged by reviewers but are removed after verification against the paper, per filtering rules:

- **Seurat tuning asymmetry** (Harsh Critic's section-by-section note): The critic noted that Seurat's δ is tuned per dataset while IF-PCA+ uses fixed parameters, suggesting an asymmetric comparison advantage. **Removed per hard rule:** If the asymmetry favors a baseline method (Seurat), not the author's method, the criticism is removed. The claim that this asymmetry "could systematically advantage one side" is speculative, and the asymmetry in question favors the baseline, making the comparison harder for the proposed method — not weaker.
- **Microarray overfitting explanation is speculative** (Harsh Critic): The critic noted the paper's explanation about possible overfitting on microarray data is speculative. The paper itself says "may lead to overfitting" (line 204), which is appropriately hedged. This is an honest discussion of a limitation, not a weakness requiring removal in the final review.
- **Strength about 0.68/0.34 neighborhood accuracy improvement** (Strength Finder): Presented as a core strength, but the supporting numbers (0.68 vs. 0.34) are stated without experimental setup or citation in the visible text. This strength conflicts with verified weakness #3 above. Moved here per rule: "Drop strengths that conflict with a verified weakness."

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Report standard deviations (or at least min/max ranges) for all main results in Tables 2, 3, 4, and 5. Since 10 runs were already performed, this data is available and reporting it would substantially strengthen the evidential basis of all claims.
2. Add a parameter sensitivity study for knn_s and knn_f (e.g., test a grid and show that accuracy/ARI is stable over a reasonable range).
3. Clarify how the arg max in Eq. (61–64) is computed (optimization method, range of t, resolution).
4. Revise the abstract to decouple the accuracy and ARI claims (e.g., "outperforms...in clustering accuracy and achieves competitive ARI performance").

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>