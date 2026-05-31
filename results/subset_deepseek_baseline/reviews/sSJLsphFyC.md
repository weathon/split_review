## Summary

This paper proposes an extension to Maximum Variance Unfolding (MVU) for nonlinear dimensionality reduction that handles data lying on disjoint manifolds (disconnected neighborhood graphs). The method embeds each connected component separately via MVU, selects representative points from each component, performs a "global MVU" on these representatives to position components relative to each other, and then translates the remaining points via affine transformations. The approach reduces computational cost through parallelization and enables MVU to be applied to multimodal data where standard MVU fails.

## Strengths

- **Addresses a genuine limitation of MVU**: The inability to handle disconnected neighborhood graphs is a well-known practical issue for MVU, and the paper proposes a principled solution that maintains MVU's local isometry guarantees.
- **Computational efficiency gains**: By decomposing the problem into smaller subproblems and enabling parallel computation, the method achieves significant speedups (up to 15x in reported experiments) while also reducing memory requirements.
- **Competitive empirical performance**: The method achieves the best or near-best results on several datasets across multiple metrics (1-NN error, trustworthiness, continuity), particularly on natural datasets where it outperforms vanilla MVU.

## Weaknesses

### Major

- **Insufficient experimental detail and rigor**: The paper reports results in Tables 1-3 without any variance or confidence intervals. Given the stochastic nature of some datasets and the sensitivity of manifold learning methods to hyperparameters, single-run results are insufficient to establish statistical significance. The paper also does not report how hyperparameters (e.g., k for nearest neighbors, embedding dimensionality) were selected for each method, making it impossible to assess whether comparisons are fair.

- **Missing critical implementation details**: The "global MVU" step (Equation 8-11) involves solving an SDP on the representative points, but the paper does not specify how this SDP is solved, what solver is used, or how the computational complexity scales. The affine transformation step (step 6) is described only as "computing an affine transformation matrix" without specifying the method (e.g., least squares, Procrustes analysis). These omissions prevent reproducibility.

- **The method's theoretical guarantees are unclear**: While the paper claims MVU-DM "retains strong local isometry," it does not analyze how the two-stage procedure (separate embedding + global positioning) affects the isometry properties. The global MVU only constrains distances between representative points, not all points, so the final embedding may not satisfy the same local isometry guarantees as standard MVU. This is a significant theoretical gap.

- **Limited comparison with relevant baselines**: The paper does not compare against the simple baseline of running MVU on the largest component and projecting other points (as done in Van Der Maaten et al., 2009), nor against landmark MVU (Weinberger et al., 2005) which is directly relevant. The exclusion of t-SNE is questionable—while t-SNE emphasizes clustering, it is widely used and its performance on the reported metrics would provide useful context.

### Minor

- **The representative point selection method (extrema along principal directions) is heuristic**: While intuitively reasonable, the paper provides no theoretical justification that 2d_p points are sufficient to capture the component's geometry, nor does it analyze the approximation error introduced by this subsampling.

- **The "global MVU" problem (Equation 8-11) may still be expensive**: If the number of components C is large, the total number of representative points (sum of 2d_p) could still be substantial, potentially limiting the computational benefits.

### Trivial

- The paper states "We will provide all the software used to obtain the results presented in this paper as soon as deanonimisation is allowed" but does not provide a link or repository name, making it impossible to verify results.

## Nice-to-Haves

- An ablation study comparing different representative point selection strategies (e.g., random sampling vs. principal direction extrema) would strengthen the paper.
- Analysis of how the number of components C and the choice of k affect both embedding quality and computational speedup would be valuable.
- A theoretical bound on the distortion introduced by the two-stage procedure relative to standard MVU would significantly strengthen the contribution.

## Novel Insights

None beyond the paper's own contributions. The core idea of decomposing a manifold learning problem into component-wise embeddings followed by global alignment is not entirely novel (similar strategies exist for Isomap and other methods), though its application to MVU with the specific representative point selection is new.

## Suggestions

- Report all results with standard deviations over multiple runs (at least 5) with different random seeds or train/test splits.
- Provide a clear description of the SDP solver used, its convergence criteria, and the computational cost of the global MVU step.
- Include comparisons with the simple baseline of embedding the largest component and projecting others, as well as landmark MVU.
- Add a theoretical analysis of how the two-stage procedure affects the local isometry guarantees of MVU.

## Score and Decision

The paper addresses a real limitation of MVU and proposes a reasonable solution with promising empirical results. However, the lack of experimental rigor (no variance reporting, unclear hyperparameter selection), missing implementation details that hinder reproducibility, and the absence of key baselines prevent me from recommending acceptance. The core idea is sound but the paper needs substantial strengthening in evaluation and exposition.

MY FINAL SCORE: <score>4</score>
MY FINAL DECISION: <decision>Reject</decision>