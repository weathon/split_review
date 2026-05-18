Now I have a thorough understanding of the paper and can verify each claim. Let me write the consolidated review.

## Summary

The paper proposes ResTran, a simple transformation of node features via multiplication by the shifted inverse-square-root graph Laplacian ($L_b^{-1/2}$), followed by standard vector-based classifiers (SVM, simple NNs). The core idea is to obtain a representation that captures both graph structure and features without the architectural bias toward homophily that GNNs inherit from their propagation design. Theoretical connections are established between ResTran and spectral clustering (via $k$-means, for the featureless $X=I$ setting), effective resistance, and ratio-cut objectives. Experiments on homophilous and heterophilous benchmarks show ResTran + simple classifiers outperforming GCN, GAT, and SGC on heterophilous graphs.

## Strengths

1. **Rigorous theoretical result for the featureless setting (Theorem 8).** The paper proves that in the featureless setting ($X = I$), $k$-means on the ResTran coordinates $\mathbf{v}_i' = L_b^{-1/2}\mathbf{e}_i$ is equivalent (in the relaxed sense) to ratio-cut spectral clustering. This is a clean, non-trivial connection grounded in the $k$-means / spectral-clustering framework of Dhillon et al. (2004), but extended to discrete graph data and the ratio cut specifically. Proposition 7 further grounds the objective in effective resistance. This is a genuine contribution that holds independently of the graph-with-features extension.

2. **Clear spectral intuition for why ResTran balances homophily and heterophily.** Section 4.1 explains via Proposition 3 that $L_b^{-1/2}$ spectrally reorders $L$: the largest eigenvalues of $L_b^{-1/2}$ correspond to the smallest eigenvalues of $L$ (homophilous information), while small eigenvalues of $L_b^{-1/2}$ still preserve heterophilous components. Unlike GNN message-passing that increasingly amplifies low frequencies, ResTran applies the transformation once, so both frequency bands survive. This is a principled and well-motivated explanation.

3. **Improved unsupervised representations over graph-only or feature-only.** Table 1 shows that spectral clustering on a graph built from ResTran vectors consistently outperforms graph-only and feature-only spectral clustering across all five datasets (e.g., Cora: 57.1% vs. 37.9% graph-only vs. 39.6% feature-only). This validates that ResTran combines structural and feature information more effectively than either modality alone.

4. **Empirical evidence that ResTran + simple classifiers outperforms GCN/GAT/SGC on heterophilous datasets.** On all six heterophilous benchmarks (Wisconsin, Cornell, Texas, Chameleon, Squirrel, Actor), at least one ResTran variant surpasses these standard GNNs, often by large margins (e.g., Wisconsin: 69.0% ResTran+AVAE vs. 55.0% GCN). This supports the claim that ResTran is more robust to homophily bias than these particular GNN architectures.

## Weaknesses

### Major

1. **The "theoretical justification" for the graph-with-features setting is an analogy, not an equivalence, yet the paper claims it is justified "in the same sense" as Dhillon et al. (2004).** Section 4.2.1 proves a rigorous equivalence for the featureless setting ($X=I$). Section 4.2.2 extends this by *replacing $I$ with $X$* in the Frobenius-norm objective and calling the result a "natural extension." The paper states: "With these connections, we say that ResTran is justified in the same sense as the feature map for spectral clustering as done by Dhillon et al. (2004)." But Dhillon et al. proved a rigorous equivalence between weighted kernel $k$-means and normalized-cut spectral clustering for *general* feature maps — not for a single special case. Here, no proof is given that $k$-means on $X_G = X L_b^{-1/2}$ corresponds to any graph-with-features clustering objective. The general case is a heuristic motivated by the featureless result. The paper should either (a) prove a genuine equivalence (e.g., that $k$-means on $X_G$ equals a generalized cut objective incorporating features) or (b) explicitly reframe this as an empirically motivated heuristic with the featureless spectral-clustering result as inspiration.

2. **Missing comparisons with heterophily-aware GNNs weaken the central claim of robustness.** The paper claims ResTran is "more robust to the homophilous bias than established GNN methods," but the GNN baselines are limited to GCN, GAT, and SGC — all known to perform poorly on heterophilous graphs. The introduction itself cites methods designed for heterophily (Pei et al., 2020; Luan et al., 2021; Azabou et al., 2023) as "mitigating this bias." Without comparisons to H2GCN, LINKX, GPRGNN, or similar methods, the results only show that ResTran + a simple classifier beats three homophily-biased GNNs. This is interesting and suggestive, but does not establish that ResTran is competitive with the state of the art for heterophily. If ResTran also matches or beats heterophily-specific GNNs, the claim would be much stronger; if not, it should be tempered.

3. **Critical implementation details for reproducibility are omitted.** The experimental section does not state:
   - The value of the parameter $b$ (which controls inter-component separation and appears in Propositions 3, 6, and Theorem 8 with specific conditions).
   - The Krylov subspace dimension $r$ — Algorithm 1 calls `KRYLOVSUBSPACEMETHOD(L, X, r)` but neither $r$ nor the specific Krylov method (Lanczos? CG?) is reported.
   - Whether the experiments used the Krylov approximation or exact computation of $L_b^{-1/2}$ (feasible for small citation networks but not for larger graphs).

   If exact computation was used for all datasets, the scalability claims are unvalidated. If approximation was used, its effect on accuracy is unknown and unreported. Without these details, the results cannot be reproduced or properly evaluated.

### Minor

1. **No standard deviations reported for SSL results.** The paper reports averages over 10 random splits but no standard deviations. At a 5% label rate, variance across splits is typically high, and without error bars, it is impossible to assess whether observed differences (especially the comparable results on homophilous datasets) are statistically meaningful.

2. **The connection between the unsupervised spectral-clustering justification and the SSL classification task is not argued.** Theorem 8 justifies ResTran for *clustering* via $k$-means on the featureless $X_G$. The paper then applies ResTran in a *supervised/SSL classification* setting where features are present and labels are used. The assumption that a good clustering representation is also good for few-label classification is plausible but should be discussed explicitly rather than left implicit.

3. **The claim that Theorem 8 is "the first to show the spectral connection for the ratio cut" should be carefully scoped.** The paper correctly notes that Dhillon et al. (2004) only covers the normalized cut. However, the specific formulation involving $L_b^{-1/2}$ rather than the raw Laplacian eigenvectors makes the novelty claim narrow enough that it would benefit from clearer positioning relative to known connections between $k$-means and spectral clustering on graph eigenvectors.

### Trivial

None that warrant mention beyond the parser-artifact noise.

## Nice-to-Haves

- Comparison with simple node-embedding baselines (e.g., node2vec, DeepWalk) concatenated with raw features would help contextualize whether ResTran's strength comes from the specific $L_b^{-1/2}$ form or simply from using any graph-structural information.
- Sensitivity analysis for the parameter $b$ across datasets would provide practical guidance on choosing its value.
- A validation experiment comparing exact vs. Krylov-approximated ResTran on a medium-size graph (e.g., Pubmed) to demonstrate approximation quality.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism about Theorem 8 novelty being "well known":** The reviewer claimed "it is well known that relaxed ratio-cut spectral clustering is equivalent to minimizing the $k$-means objective on the bottom eigenvectors of $L$" and that the $L_b^{-1/2}$ formulation does not change this. This is not verifiable as a factual error; the paper claims novelty specifically for connecting ratio cut, $k$-means, and $L_b^{-1/2}$ simultaneously — a formulation not identical to the claimed well-known equivalence. Removed because it is an unsubstantiated assertion from the reviewer without citation.

- **"The paper does not compare with node2vec, DeepWalk":** This is a suggestion for broadening experimental scope, not a weakness that undermines the paper's claims. The paper explicitly focuses on comparing with GNN methods as stated in its framing. Moved to Nice-to-Haves.

## Novel Insights

The most interesting observation emerging from these reviews is the disconnect between the paper's rhetorical framing and its actual technical contribution. The theoretical core (Theorem 8) is a solid, non-trivial connection for a specific special case (featureless setting + ratio cut + $L_b^{-1/2}$). The paper would be *stronger*, not weaker, if it leaned into this precise contribution and presented the feature-plus-graph case as an empirically motivated heuristic — similar to how many successful methods (e.g., spectral clustering itself) are justified by a combination of theoretical special-case results and empirical performance rather than by a monolithic proof covering all cases. The actual paper already contains most of the hedging language ("natural extension," "may be seen as") but contradicts it with the stronger claim of being "justified in the same sense" as Dhillon et al.

## Suggestions

1. **Reframe the theoretical contribution precisely.** Distinguish clearly between the featureless setting (rigorous equivalence via Theorem 8) and the graph-with-features setting (motivated heuristic). Drop the claim that the general case is "justified in the same sense" as Dhillon et al. (2004).

2. **Add comparisons with at least 2–3 heterophily-aware GNNs** (e.g., H2GCN, LINKX, GPRGNN) on the same heterophilous benchmarks. This single addition would either strengthen or honestly bound the robustness claim.

3. **Report $b$, $r$, and the specific Krylov method used** in the experimental setup. Include a brief sensitivity study for $b$ on one dataset, and validate the Krylov approximation against the exact computation on a small dataset.

4. **Add standard deviations to all SSL tables** — with 5% labels and 10 random splits, variance is essential for interpretation.

## Score and Decision

The core idea — a fixed, simple transformation followed by standard classifiers — is appealing and practically motivated. The featureless theoretical result (Theorem 8) is a genuine contribution. However, the paper's central claim about theoretical justification for the general case is overclaimed, the experimental evaluation against the actual heterophily literature is incomplete, and missing implementation details prevent reproducibility. These are addressable weaknesses, but they are substantive enough that the paper in its current form does not meet the bar for acceptance at a competitive venue.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>