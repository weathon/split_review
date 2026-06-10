## Summary
This paper proposes a method that learns continuous invariance manifolds for individual visual neurons (via implicit neural representations, INR) and then aligns these manifolds across neurons by learning affine transformations on pixel coordinates. The alignment enables construction of an asymmetric activation matrix and hierarchical clustering of neurons by invariance type. The method is validated on simulated Gabor-based neurons with known ground-truth types and applied to 100 macaque V1 neurons modeled by a response-predicting DNN.

## Strengths
- **Template matching via learned affine transformations (Section 3.2) enables cross-neuron invariance comparison that handles receptive field differences.** The method explicitly handles position, orientation, and scale variation across neurons — going beyond prior work that addressed only shifts (Klindt et al., 2017) or rotations (Ustyuzhaninov et al., 2019). The continuous INR representation ensures affine coordinate transforms do not introduce discrete pixel artifacts.
- **The asymmetric activation matrix (Section 3.3) captures hierarchical relationships between invariance manifolds**, such that a simple-cell manifold can activate a complex cell but not vice versa. This is a more informative metric than symmetric similarity measures used in prior clustering approaches.
- **Cross-model generalization (Section 4.2, Fig. 3E: 89% activation strength across architectures)** provides evidence that the learned invariance manifolds reflect properties of the biological data rather than idiosyncrasies of a specific DNN architecture.
- **Simulated-neuron validation (Section 4.1) provides clean ground-truth benchmarks** demonstrating the method recovers known neuron types (six instances per type with varying RF position, orientation, and scale) with both activation similarity and manifold similarity metrics, plus cross-seed consistency analysis.

## Weaknesses

### Fatal
None.

### Major

1. **Novelty over Baroni et al. (2023) is incremental, and the core alignment step lacks ablation.** The template learning stage (Section 3.1) is directly adopted from Baroni et al. with minor architectural modifications. The novel contribution is template matching (Section 3.2): learning an affine transformation to align one neuron's manifold to maximally activate another. This is a sensible idea but amounts to a straightforward optimization once the manifold representation exists. The paper does not include an ablation comparing alignment flexibility (no alignment vs. translation-only vs. full affine) on simulated data, which would isolate the value added by the alignment procedure from the manifold representation itself.

2. **Baseline comparisons are purely qualitative and insufficient for a method paper.** The comparison to Klindt et al. (2017) and Ustyuzhaninov et al. (2019) on simulated data (Section 4.1, lines 154–159) consists of a single sentence stating these methods handle only subsets of affine transformations, with no quantitative clustering metrics (ARI, NMI, purity) reported for any baseline on the same data. Without quantitative comparisons, the reader cannot assess whether the proposed method actually outperforms existing approaches even under ideal simulated conditions. No comparison to a naive baseline (e.g., clustering on MEIs directly, or measuring manifold distance without alignment) is provided.

3. **V1 cluster validation is circular.** The dendrogram cut-off threshold was selected "while ensuring that neurons within each cluster shared similar invariance properties, as verified through visual inspection of their invariance manifolds" (Section 4.2). The clusters are then presented as validated by looking at the same invariance manifolds that were used to define them. This is not independent validation. Additional checks (cross-animal distribution, cross-seed ARI=0.75) are useful but show only that the clustering is reproducible, not that it corresponds to functionally meaningful neuron types. A held-out prediction experiment (e.g., within-cluster vs. cross-cluster response prediction) would provide a much stronger test.

4. **V1 analysis uses a heavily selected sub-population without adequate discussion of selection bias.** The method is applied to 100 best-predicted neurons out of 458 available (a 78% reduction; line 163). The paper references a supplementary figure but does not discuss how this selection biases the findings. The striking claim that the method "could have potentially found novel types of invariances" is based on the neurons the response-predicting DNN happens to fit best — which may be the simplest, most stereotypical neurons. The prediction correlation distribution for selected vs. excluded neurons is not reported.

### Minor

1. **Missing implementation details for reproducibility.** Key hyperparameters are not specified: INR training protocol (learning rate, optimizer, number of iterations, batch size), contrastive loss parameters (λ, τ, N, positive/negative neighborhood definition), the MEI optimization procedure, the affine transformation parameterization (full 6-parameter or constrained subset), and the hierarchical clustering linkage criterion (cosine dissimilarity is specified but linkage — Ward? Complete? Average? — is not).

2. **Only one of three non-canonical clusters is characterized.** The paper identifies five clusters (Section 4.2), with Clusters 3–5 labeled as potentially novel. Only Cluster 5 (checkerboard-like texture) is described. Without characterization of Clusters 3–4, it is unclear whether they represent meaningful invariance types or artifacts of the dendrogram cut-off.

3. **The asymmetry interpretation conflates subset relations with possible optimization failures.** Section 3.3 interprets the non-symmetric activation matrix as M_i ⊆ M_j, but Section 5 acknowledges the alignment problem is non-convex. If optimization for neuron i's manifold against neuron j stalls in a poor local minimum, the resulting low activation would appear to indicate M_i ⊈ M_j when the actual issue is optimization failure. The paper provides no analysis to distinguish these cases.

### Trivial
None.

## Nice-to-Haves
- An ablation comparing clustering performance with no alignment, translation-only alignment, and full affine alignment on the simulated data.
- Quantitative clustering metrics (ARI, NMI) against Klindt et al., Ustyuzhaninov et al., and a naive MEI-clustering baseline.
- A held-out validation: do within-cluster neuron pairs predict each other's responses to novel stimuli better than cross-cluster pairs?
- Analysis of the prediction correlation distribution across all 458 neurons vs. the selected 100.
- A permutation test for V1 cluster significance.

## Removed Points
- **"FIX"/"NEW" markers in parsed text**: These are PDF parser artifacts, not present in the original submission. Removed per formatting-artifact rule.
- **Criticism about Figure 2 being "not visible in the text"**: Acknowledged by the harsh critic as a parser limitation, not a paper flaw. Removed.
- **Criticism about missing appendix content (Fig. S3)**: The parser strips supplementary content; the original submission includes it. Removed per rule.
- **Strength Finder's generic strengths** about the problem being "important" or "well-motivated": removed as superficial / not specific to the paper's concrete contributions.
- **"Strengthening the Paper on Its Own Terms" suggestions** from the harsh critic: these are constructive suggestions, not weaknesses. Moved to Nice-to-Haves/Suggestions.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. Add quantitative baseline comparisons with ARI/NMI on simulated data to substantiate the claimed advantages over prior methods.
2. Include an ablation of alignment flexibility (no alignment, translation-only, full affine) to isolate the value of the core contribution.
3. For the V1 analysis, add a held-out response prediction experiment to validate clusters independently of the manifolds used to define them.
4. Report the prediction correlation distribution for the 100 selected vs. the 358 excluded neurons.
5. Disclose all hyperparameters for reproducibility (INR training, contrastive loss, affine alignment, clustering linkage).
6. Characterize all identified clusters (Clusters 3 and 4, not just Cluster 5).

## Score and Decision
The paper proposes a clean, sensible method, and the simulated validation convincingly demonstrates the pipeline works under controlled conditions. However, at the ICLR level, the contribution is limited by: (a) incremental novelty over Baroni et al. (2023) with no ablation isolating the alignment step's value; (b) purely qualitative baseline comparisons that cannot support the claimed methodological advantages; (c) a circular V1 cluster validation that weakens the main biological demonstration; and (d) a heavily selected V1 subpopulation (22% of available neurons) with inadequate discussion of selection bias. These are fixable issues, but in its current form the experimental support is not strong enough for a top venue.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>