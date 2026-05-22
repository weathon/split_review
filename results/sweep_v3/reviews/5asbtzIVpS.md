Now I have sufficient anchors for calibration. Let me write the final review.

## Summary

The paper introduces Forest-based Graph Learning (FGL), a new paradigm for semi-supervised node classification that reinterprets message passing on a graph as transportation over a forest of spanning trees. The core insight is that a spanning tree is the minimal globally-covering subgraph, enabling global receptive field with linear complexity. The framework comprises: (1) a pre-processing step that augments graphs for connectivity and increased homophily via pseudo-label k-NN, (2) a homophily-guided tree sampler using Wilson's algorithm, (3) a general linear-time tree aggregator that achieves quadratic node-pair interactions, and (4) a tree fuser combining local and global information. Theorem 2 provides a theoretical relationship between edge-score ratios and the quality of sampled trees, and experiments across 9 benchmarks show FGL achieving the best average rank (1.22) among 26 baselines with competitive efficiency.

## Strengths

1. **Genuinely novel paradigm that reframes the cost–receptive-field trade-off.** The paper identifies a fundamental limitation in existing graph learning paradigms (Eq. 1) and proposes spanning trees—the minimal globally-covering subgraph—as a principled intermediate structure. This is a clear conceptual contribution supported by the comparison in Fig. 1, and it moves beyond incremental architectural tweaks.

2. **Strong empirical results across diverse benchmarks.** Table 1 shows FGL achieves the best average rank (1.22) across 9 homophilous and heterophilous datasets, outperforming 26 baselines including deep GNNs (GCNII), Graph Transformers (SGFormer, DiFFormer), and Mamba-based methods. Gains on heterophilous datasets are particularly notable (Texas: 91.89 vs. next best 78.92; Cornell: 83.24 vs. 76.76).

3. **Linear-time tree aggregator with theoretical grounding.** Theorem 1 and the implementation in Eqs. (7)–(8) show that any aggregator satisfying Properties (I) and (II) can realize global message propagation in linear time per tree. The algorithm is genuinely elegant—two recursions over a rooted tree enable all-pair interactions at O(n) cost.

4. **Ablation studies confirm internal component contributions.** Table 3 shows that removing the global submodule, local submodule, using uniform sampling, or a single tree all degrade performance. The comparison between uniform sampling and homophily-guided sampling, and between single tree vs. forest, validates the design choices within the framework.

5. **Empirical validation of the homophily estimator's role.** Figure 5 shows performance improves monotonically with the accuracy of the homophily estimator, and Table 4 demonstrates that the two-stage estimator significantly outperforms naive variants, directly supporting the practical relevance of Theorem 2.

## Weaknesses

### Fatal

None.

### Major

1. **The graph augmentation step is not isolated in the evaluation, making it unclear how much of the gains come from the forest paradigm vs. increased input homophily.** The pre-processing (Section 4.1) uses pseudo-labels to add k-NN edges, explicitly increasing the graph's homophily ratio. The ablation studies (Table 3) evaluate all variants on the *same augmented graph*—there is no experiment that runs FGL on the original un-augmented graph, nor do baselines receive the same augmented graph. The large gains on heterophilous datasets (e.g., Texas: 91.89, Cornell: 83.24) are impressive, but without a control, the reader cannot attribute them cleanly to the tree-based message passing versus the input graph being made more homophilous. This does *not* invalidate the paper's contribution—the ablation shows that forest-specific components (guided sampling, multiple trees) matter even on the augmented graph—but it weakens the claim that the forest *paradigm itself* drives the bulk of the observed gains. Addressing this requires at minimum: (a) running FGL on the original graph, (b) giving baselines the same augmented graph, or (c) reporting homophily ratios before/after augmentation.

### Minor

2. **Theorem 2 assumes oracle knowledge of edge homophily but is applied with a learned estimator.** Theorem 2 cleanly shows that if edge scores are p for homophilous edges and q for heterophilous, the tree distribution shifts toward homophily as p/q increases. However, in practice the method uses a learned homophily estimator trained on pseudo-labels. The paper provides empirical correlation (Figure 5, Table 4) but no theoretical bridge between estimator quality and tree distribution quality under finite samples or imperfect training. This gap means the theory justifies an idealized version of the sampler rather than the deployed one. The paper should either tighten this connection or explicitly caveat the scope of the theory.

3. **Pre-processing time is excluded from efficiency comparisons.** Table 2 only reports per-epoch training time. The pre-processing step involves training a pseudo-label model (GCN or MLP) and computing k-NN across all nodes—a non-trivial one-time cost. While this is standard practice and does not undermine the per-epoch efficiency claims, reporting total wall-clock time (pre-processing + training) would give a fairer picture, especially for large datasets like ArXiv.

4. **Tree diversity is stated as important but never measured.** The paper identifies "diversity" as a key principle for the forest (Section 4.2) but provides no empirical diversity metric (e.g., edge-set overlap, homophily variance across trees). Figure 6 only reports homophily ratios. Measuring tree diversity would strengthen the motivation for using multiple trees.

5. **The relation between "p" in Figure 5 and estimator accuracy is imprecise.** The text says "as the accuracy of homophily estimator increases" but the x-axis is "p" (the average score assigned to homophilous edges). These are related but not identical quantities. The caption should clarify the mapping, or the x-axis should use a proper accuracy metric.

### Trivial

None.

## Nice-to-Haves

- A sensitivity study of the hyperparameter *k* (number of nearest neighbors in pre-processing) and γ (local–global balance), beyond just N_T.
- A limitations discussion covering scenarios where FGL may struggle (e.g., graphs with extreme label scarcity where pseudo-labels are unreliable, or sensitivity to the choice of k).
- Empirical comparison of different aggregator types (e.g., non-linear variants mentioned in the appendix) to demonstrate the claimed generality beyond linear attention.

## Removed Points

The following points from the reviews were removed:

- **"Claim that linear attention, linear RNNs, and SSMs can be adopted is unsupported"** — The paper explicitly references Sec. A.6 for non-linear variants. The appendix is stripped by the parser per submission format; this criticism cannot be verified from the main text alone.
- **"The theoretical analysis does not connect to practical estimator quality" (as raised as a separate Critical Issue 1)** — Merged into Minor weakness #2 above with toned-down language; the point is valid but its severity was overstated. The paper does provide *empirical* evidence (Figure 5, Table 4) for the connection.
- **"Label leakage risk from pseudo-labels"** — This is a speculative concern without concrete evidence of leakage in the paper's setting. Pseudo-label-based graph augmentation is a known technique in semi-supervised learning, and the paper acknowledges that pseudo-labels are only used for pre-processing, not for the main training.
- **Several vague "missing limitations" or "formatting" complaints** — These are either generic or not verifiable from the available text.

## Novel Insights

Beyond the paper's own contributions, the reviews surface one genuine observation that the authors may not have fully emphasized: the framework's total cost framing (Eq. 1) provides a potentially reusable lens for analyzing graph-learning paradigms beyond FGL. The tree-based paradigm can be seen as introducing a third point on the local–global spectrum (local neighborhoods → spanning trees → complete graph), and this conceptual contribution may be more impactful than the specific implementation details. A paper that fully exploited this framing could influence how future work reasons about graph-level architecture design.

## Suggestions

1. **Address the augmentation confound directly**: Run FGL on the original (un-augmented) graph and report performance. If the gap is large, also report baselines on the augmented graph. This single experiment would substantially strengthen the paper.

2. **Clarify the scope of Theorem 2**: Add a sentence explicitly stating that the theorem assumes perfect homophily labels (p/q for true homophilous/heterophilous edges), while the practical method approximates this via learned scores, with empirical validation in Figure 5.

3. **Report total wall-clock time**: Include pre-processing time alongside per-epoch time in Table 2 or a separate table.

4. **Add a diversity metric for sampled trees**: Report average pairwise edge overlap or homophily variance across the N_T sampled trees.

## Score and Decision

### Calibration Anchors

| Path | Avg Score | Comparison to FGL |
|---|---|---|
| Port-Hamiltonian Deep Graph Networks (`03EkqSCKuO`) | 7.0 | Also addresses long-range propagation with strong theory, but experiments are narrower. FGL has more datasets and stronger SOTA wins, but a larger theory-practice gap and an unresolved augmentation question. |
| DUALFormer (`4v4RcAODj9`) | 6.5 | GT addressing similar local-global trade-off. FGL has a more novel paradigm and better results, but has the augmentation confound that DUALFormer does not. Comparable overall strength. |
| Monophilic NT (`oSdrJyb4UH`) | 6.0 | Deals with heterophily and graph transformers. FGL has stronger theory and more comprehensive evaluation. Rejected due to scalability and missing baselines. |
| S4G (`0Z6lN4GYrO`) | 4.67 | S4-based graph learning with novelty concerns and a simple MPNN layer boost. FGL is clearly stronger in both novelty and results. |
| KDGCN (`GEZACBPDn7`) | 5.25 | Semi-supervised graph classification, much narrower scope. FGL is stronger across all dimensions. |
| WL-Tree (`ceNnsnA5gu`) | 3.0 | Very weak paper with fundamental definition issues. FGL is incomparably stronger. |

**Comparative judgment**: FGL is stronger than the mid-range anchors (S4G, KDGCN, WL-Tree) and competitive with the high-scoring anchors (Port-Hamiltonian at 7.0, DUALFormer at 6.5). The augmentation confound is the primary factor preventing a higher score—the paper's experiments convincingly show that the forest components matter, but the magnitude of the total improvement over baselines is partially attributed to an uncontrolled variable. The core conceptual contribution (tree-based paradigm) is more original than DUALFormer's dual-dimension approach, but not as theoretically complete as Port-Hamiltonian's framework. Positioned against these anchors, FGL merits acceptance as a strong contribution that would benefit from a targeted experimental addition.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>