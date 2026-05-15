Now I have a thorough understanding of the paper and can assess each reviewer claim against the actual text. Let me write the consolidated review.

## Summary

This paper identifies a previously unrecognized limitation of GNNs: that strongly connected subgraphs (not just bottlenecks) can restrict information flow. It formalizes this through the concept of "multi-scale consistency" — at the node level (retaining a connected propagation graph across connectivity scales) and the graph level (assigning similar features to graphs describing the same object at different resolutions). The paper proposes ResolvNet, a spectral GNN based on resolvent polynomials of the graph Laplacian, provides rigorous theoretical guarantees of multi-scale consistency (Theorems 1–3), and validates with strong empirical results on node classification (top-1 on 4/8 datasets) and molecular property prediction (QM7 MAE 16.52, factor ~3.6× over the next best baseline).

## Strengths

- **Novel problem identification with concrete evidence:** The paper identifies that strongly connected subgraphs — not just bottlenecks — restrict information flow in GNNs, a genuinely overlooked phenomenon. This is supported by a concrete derivation (Eq.~\ref{effective_renorm_adj}) showing that GCN's renormalized adjacency effectively decouples propagation across scales, and by the teaser experiment (Fig.~\ref{teaser}) where GCN accuracy drops from ~72% to ~55% as clique size grows while ResolvNet remains constant.

- **Provable multi-scale consistency at node and graph levels:** Theorem~\ref{main_resolvent_theorem} bounds resolvent closeness as O(λ_max(Δ_reg.)/λ_1(Δ_high)), Theorem~\ref{varying_spaces} shows Type-0/Type-I filters achieve different forms of propagation consistency, and Theorem~\ref{graph_level_top_stab} gives an explicit Lipschitz bound for graph-level feature similarity. These go beyond heuristics and are verified experimentally: Figure~\ref{collapse_graph} shows ResolvNet's feature vectors converge as scale separation increases while baselines diverge.

- **Strong empirical performance across diverse settings:** ResolvNet achieves top-1 accuracy on 4 of 8 node classification datasets (MS. Acad. 92.73%, Cora 84.16%, Pubmed 79.29%, Citeseer 75.03%), outperforming 11 baselines. On QM7 regression it achieves MAE 16.52 (factor 3.6× better than next-best ARMA at 59.39), and this advantage grows to ~10× on coarse-grained QM7 (Table~\ref{qm7_collapsed_result_table}), directly validating the graph-level multi-scale consistency claim.

- **Principled architecture design grounded in spectral theory:** The use of resolvent polynomials (Eq.~\ref{res_poly_filter}) is justified by Theorem~\ref{approx_theorem} (universal approximation of bounded/vanishing functions via Type-0/Type-I filters), and the Type-0/Type-I distinction follows from different convergence guarantees in Theorem~\ref{varying_spaces}. The architecture is derived from mathematical necessity, not ad hoc design.

## Weaknesses

### Fatal
None.

### Major

- **Node-level multi-scale claim is validated on only one synthetic construction.** The central node-level claim — that ResolvNet retains a connected propagation graph under multi-scale structure — is demonstrated experimentally only on the Citeseer clique-expansion experiment (Section 5, Fig.~\ref{teaser}). This is a single, synthetic modification on one dataset. The paper does not (a) verify that the clique expansion produces separated spectral scales (λ_1(Δ_high) ≫ λ_max(Δ_reg.)) as required by Definition~1, (b) repeat the experiment on other base graphs (e.g., Cora, Pubmed) to confirm robustness, or (c) test on real-world weighted graphs that naturally exhibit multi-scale structure. While the theoretical guarantees (Theorems 1–3) are general, the empirical support for the node-level claim is narrower than the paper's framing suggests.

### Minor

- **Attribution of standard benchmark success to the multi-scale inductive bias is over-claimed.** The paper states (lines 514–515) that ResolvNet's outperformance on homophilic benchmarks "can be traced back to the inductive bias... that strongly connected nodes should share similar features." However, the paper explicitly notes these benchmarks are *not* multi-scale graphs (line 424: "un-weighted real world datasets"), and the multi-scale theory provides guarantees only for graphs satisfying the spectral condition of Definition~1. The inductive bias is a reasonable heuristic for homophilic graphs, but the paper's theoretical framework does not directly explain the standard benchmark results. The paper partially hedges this ("can be traced back to" is a soft claim) but the framing over-reaches.

- **The hard threshold decomposition W = W_reg. + W_high is idealized.** The paper assumes a disjoint decomposition where every edge belongs entirely to one scale. In practice, many real graphs have a continuum of edge weights, making any threshold arbitrary. The paper does not discuss sensitivity to the choice of threshold or how to determine it in practice. This is a gap between the clean theoretical model and real-world application.

### Trivial

- The Section-by-Section notes about formatting are parser artifacts and not issues in the original submission.

## Nice-to-Haves

- The node-level multi-scale experiment would be strengthened by repeating on additional base graphs (e.g., Cora, Pubmed) and by verifying the spectral gap condition empirically.
- A discussion of how to choose the threshold separating W_high from W_reg. in practice would improve applicability.

## Removed Points

These points were raised by reviewers but are not valid criticisms of the paper:

- **Point 2 from Harsh Critic (QM7 coarse-graining confound):** The critic claims that evaluating networks trained on one-hot features on coarse-grained graphs with bag-of-words features introduces an "uncontrolled confound." This is based on a misunderstanding of the paper's theoretical framework. The coarse-grained node features (bag-of-words normalized by atomic charge) are precisely J^↓(one-hot), the projected features defined in Definition~\ref{proj_ops}. Theorem~\ref{varying_spaces} guarantees that with Type-I filters, Φ(G)(X) ≈ J^↑·Φ_underline·J^↓(X), so the comparison between Φ(G)(one-hot) and Φ(G_underline)(bag-of-words) is exactly what the theory predicts should converge as scale separation increases. The experiment is a clean test of the theoretical claim, not a confound.

- **Point 1 from Harsh Critic (structural misalignment):** The critic argues that standard node classification benchmarks (Cora, Citeseer, etc.) do not satisfy the multi-scale definition and therefore cannot validate the theory. However, the paper explicitly frames these experiments as "to establish that the proposed ResolvNet architecture **not only performs well** in multi-scale settings" (line 423, emphasis original). The multi-scale validation is conducted separately through the clique expansion experiment (node-level) and the QM7 coarse-graining experiments (graph-level). The standard benchmarks test general expressivity outside the multi-scale setting.

- **Generic or unsupported reviewer claims** about missing experimental protocols, unverifiable reproducibility concerns, or demands for experiments outside the paper's stated scope.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add at least one additional base graph (e.g., Cora, Pubmed) to the node-level clique-expansion experiment to demonstrate that the multi-scale consistency effect is not dataset-specific.
2. Include a brief discussion of how the spectral gap condition (λ_1(Δ_high) > λ_max(Δ_reg.)) could be verified or approximately satisfied in practice, and address the sensitivity to the choice of threshold for separating edge-weight scales.
3. Soften the attribution of standard benchmark success to the multi-scale inductive bias, or add a clarifying note that the inductive bias is a heuristic that happens to align with homophily but is not directly justified by the multi-scale theory for unweighted graphs.

## Score and Decision

This is a solid paper with a genuinely novel contribution: identifying a previously overlooked limitation of GNNs (information suppression by strongly connected subgraphs), formalizing it through multi-scale consistency, and providing a principled architecture with rigorous theoretical guarantees and strong empirical validation. The paper is well-written, the theory is sound, and the results are impressive (especially the ~3.6× improvement on QM7). The main weaknesses are the narrow empirical validation of the node-level claim (one synthetic construction) and a mild over-attribution of standard benchmark results to the multi-scale theory — both addressable in revision but neither fatal.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>