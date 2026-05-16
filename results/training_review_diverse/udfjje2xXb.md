Now I have all the evidence I need. Let me produce the final consolidated review.

## Summary

The paper introduces GKAN (Graph Kolmogorov-Arnold Network), which replaces fixed activation functions in GNN message passing with learnable B-spline functions on edges, extending KANs to graph-structured data. The authors claim improved accuracy and inherent interpretability over GCN, GAT, and GraphSAGE on node classification, link prediction, and graph classification benchmarks.

## Strengths

- **Novel architecture transferring KAN's spline-based activations to graph edges**: The paper proposes a genuine architectural innovation by placing learnable B-spline activation functions on edges rather than fixed activations at nodes (Section 2.2). The mathematical formulation of the message-passing and aggregation pipeline is provided, and the idea of extending KANs to graph data is timely given the recent interest in KANs.
- **Consistent accuracy gains across multiple tasks and datasets**: In Table 2, GKAN achieves the highest reported accuracy on 7 out of 8 benchmark tasks (Cora, PubMed, CiteSeer for node classification; Cora, CiteSeer for link prediction; MUTAG, PROTEINS for graph classification), with results averaged over 100 runs. The gains are especially notable on graph classification (MUTAG: 85.0 vs. 75.1 for GAT; PROTEINS: 77.7 vs. 73.8 for GCN).
- **Transparent discussion of computational trade-offs**: Table 3 explicitly reports per-epoch training times, showing GKAN is ~1,000× slower than GCN (2.05s vs. 0.0016s on an Apple M1). The paper openly acknowledges this cost rather than obscuring it, which is commendable.
- **Honest acknowledgment of interpretability limitations**: The "Limitations" subsection (Section 4.1) clarifies that GKAN is "more interpretable than other models" rather than fully interpretable, and notes that deep layers cause information loss — a more nuanced position than the abstract and introduction suggest.

## Weaknesses

### Fatal
None. The paper's core claims are not invalidated by fatal errors; the weaknesses below are major but addressable.

### Major

- **Dataset statistics in Table 1 are swapped between PubMed and CiteSeer, undermining trust in experimental reporting.** The table lists PubMed with 3,327 nodes, 9,104 edges, 3,703 features, and 6 classes, and CiteSeer with 19,717 nodes, 88,648 edges, 500 features, and 3 classes. These match the *opposite* standard Planetoid datasets: standard CiteSeer has ~3,327 nodes / ~9,104 edges / 3,703 features / 6 classes, while standard PubMed has ~19,717 nodes / ~88,648 edges / 500 features / 3 classes. While the actual experiments likely used the correct PyTorch Geometric datasets (so results may be unaffected), this presentation error raises unnecessary doubt about whether the correct data splits and input dimensions were used. It must be corrected, and the authors should explicitly confirm that the experimental data was correctly assigned.

- **No variance reporting for any result, making the significance of the improvements unverifiable.** All results in Table 2 are point estimates without standard deviations, confidence intervals, or significance tests. The margin over GAT on CiteSeer (69.4 vs. 68.2, a 1.2-point gap) and PubMed (81.0 vs. 78.2) is small enough to fall within typical run-to-run variance. Even the large MUTAG gain (85.0 vs. 75.1) cannot be assessed without variance on a dataset of only 188 graphs. Although 100 runs were performed, the variance information from those runs is absent. Without it, the reader cannot determine whether the claimed improvements are reliable.

- **Interpretability, a central claimed contribution, is not substantiated.** The evidence consists of a single qualitative figure showing normalized spline weights on edges for one node in Cora, plus a side-by-side comparison with GNNExplainer. There is no task-based evaluation (faithfulness, sparsity, stability), no quantitative comparison to other interpretability methods, no synthetic experiment with known ground-truth decision rules, and no human evaluation. The statement that "the values truly represent the message of the network" (line 452) is an assertion without justification. Furthermore, the methodology section describes sparsity regularization and pruning as necessary for KAN interpretability (lines 161–175), but the experimental section never states whether these techniques were applied to GKAN — the hyperparameter search mentions only L2-regularization, not sparsity regularization or pruning. This gap means the paper's flagship contribution lacks credible evidence.

- **Ambiguity in how the scalar spline function is applied to multi-dimensional node feature vectors.** The message-passing equation (line 232) defines $\mathbf{m}_{j \to i}^{(l)} = \mathrm{spline}(\mathbf{x}_j^{(l-1)})$ where $\mathbf{x}_j^{(l-1)}$ is a vector, but the spline function $\varphi(x) = w_b b(x) + w_s \mathrm{spline}(x)$ (line 258) is defined for a scalar $x$. It is never specified whether $\mathrm{spline}$ is applied element-wise, whether separate splines are learned per feature dimension (as in the original KAN), or whether features are first projected to a scalar. The same ambiguity applies to the node-update spline (line 252). This is a genuine reproducibility gap.

### Minor

- **Baseline comparison is limited and may not support the "state-of-the-art" claim.** The paper compares only against GCN, GAT, and GraphSAGE — all introduced before 2018. Stronger modern baselines such as GIN (which the paper itself cites in the introduction), GATv2, or PNA are absent. For the graph classification task specifically, this is a significant omission. The paper claims "outperforming state-of-the-art GNN models" (abstract, line 10), which is unsupported given the narrow baseline set.

- **No ablation studies.** The paper does not isolate the effect of the spline activation versus a standard MLP-based message-passing baseline using the same architecture. Without an ablation (e.g., replacing splines with a simple MLP in the GKAN framework), it is unclear whether the gains come from the spline itself, the additional parameters, or some other architectural choice.

- **Hyperparameter tuning asymmetry for graph classification.** For node/link tasks, both GKAN and baselines use hyperparameters tuned/designated for Cora (a symmetric protocol). However, for graph classification, GKAN's hyperparameters are tuned on MUTAG while it is unclear whether the baselines received per-dataset tuning. This asymmetry should be clarified.

### Trivial

- The paper says "averaging over 100 runs the test accuracy … of the models that achieved the highest validation accuracy during training over each run" — this is standard practice (best-epoch selection) and the wording is merely redundant, not problematic.
- Minor phrasing inconsistency: the abstract claims "state-of-the-art GNN models" while the limitations section says the paper does not claim full interpretability — these two framings are in slight tension.

## Nice-to-Haves

- A per-dataset hyperparameter tuning sweep for all baselines (or at least one additional strong baseline like GIN) would substantially strengthen the empirical evaluation.
- A synthetic experiment with a known ground-truth decision rule (e.g., "rely on edges connecting to node type A") to demonstrate that GKAN's spline weights recover that rule would provide concrete evidence for the interpretability claim.
- Reporting standard deviations for Table 2 would turn the "averaged over 100 runs" claim from a procedural statement into actionable evidence.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"Baselines not fairly tuned / asymmetric tuning"** (partially removed): The harsh critic claimed GKAN's tuning was asymmetric with baselines. For node/link tasks, the paper actually uses a symmetric protocol — both GKAN and baselines use hyperparameters for Cora applied to PubMed/CiteSeer. This point is factually incorrect for the node/link experiments and was weakened to a Minor concern limited to graph classification.
2. **"Code not yet available"**: Standard practice for anonymized submissions; not a weakness of the paper.
3. **"Unusual selection rule (best model per run)"**: The critic initially called this "unusual" but then acknowledged it IS standard practice (best-epoch selection). This is trivial and the critic's own analysis resolves the concern.
4. **"The paper should also cover Y / domain Z / additional tasks"** (scope creep): The critic's suggestion to add more datasets or domains beyond the paper's stated scope is removed as it would constitute a different paper.
5. **Strength Finder's claim of "Thorough hyperparameter tuning and fair comparison"** as a strength: This is partially accurate (the protocol is symmetric for node/link) but the baseline set is too limited to call it "thorough." Weakened to a minor note in the review rather than a core strength.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a standard pattern: a novel architecture with promising but preliminary evidence, weakened by presentation errors and missing variance reporting. The most interesting tension is between the paper's strong interpretability claims and the limitations section that disavows full interpretability — a gap the authors are aware of but do not fully address.

## Suggestions

1. **Fix the Table 1 swap** between PubMed and CiteSeer, and explicitly state in a footnote that the correct PyTorch Geometric datasets were used.
2. **Add standard deviations or confidence intervals** to Table 2 for all entries, or report them in a supplementary table.
3. **Provide at least one quantitative interpretability evaluation**: e.g., a synthetic graph with a known decision rule, or a faithfulness metric (fraction of edges with nonzero spline weight, correlation between spline weights and prediction change under perturbation).
4. **Clarify how the spline function operates on vectors** — is it element-wise with shared splines per layer? Separate splines per dimension (as in original KAN)? A simple diagram or pseudocode would suffice.
5. **Add at least one stronger baseline** (GIN is the most natural choice, especially for graph classification) and perform an ablation replacing splines with a 2-layer MLP in the same architecture.

## Score and Decision

The paper proposes an interesting architectural innovation with promising results on multiple benchmarks. However, the combination of (a) a presentation error in Table 1 that calls experimental reporting into question, (b) a complete absence of variance reporting, (c) an unsubstantiated interpretability claim that is central to the paper's narrative, and (d) a mathematically underspecified method make the current version unconvincing. The weaknesses are addressable but not trivial. The core idea has merit, but the evidence does not yet adequately support the paper's strongest claims.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>