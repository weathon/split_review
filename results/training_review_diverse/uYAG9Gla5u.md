Now I have all the information I need. Let me produce the final consolidated review.

---

## Summary

This paper introduces MEGA-GNN, a message-passing framework for multigraphs that performs two-stage aggregation within each layer: first aggregating parallel edges between the same node pair (via artificial nodes), then aggregating messages from distinct neighbors at the node level. The paper proves that MEGA-GNN is permutation equivariant (without strict edge ordering) and universal (with strict edge ordering), and demonstrates strong empirical results on AML transaction edge classification and Ethereum phishing node classification tasks.

## Strengths

- **Novel two-stage aggregation that preserves individual edge features across layers.** Unlike ADAMM (which collapses parallel edges into a single super-edge before message passing), MEGA-GNN's artificial-node design enables per-edge latent feature updates across layers while maintaining the topology of the original multigraph (Equations 4–6). This clean architectural innovation is clearly motivated by the SUM-of-MAX vs. MAX-of-SUM example in Section 3.1.

- **Proof of permutation equivariance without strict total edge ordering.** Theorem 1 establishes that MEGA-GNN is permutation equivariant when using permutation-invariant aggregation functions, while Proposition 1 shows Multi-GNN is *not* permutation equivariant without such an ordering. This is a formal advantage over the primary existing multigraph GNN baseline.

- **Universality under strict total ordering, with honest characterization of the trade-off.** Theorem 2 proves universality when a strict total edge ordering is available. The paper explicitly contrasts this with Multi-GNN's position (Section 3, bullet list): without ordering, MEGA-GNN is equivariant but not universal, while Multi-GNN is universal but not equivariant. This balanced theoretical comparison is a strength.

- **Large and consistent gains on AML edge classification.** On four synthetic AML datasets (Table 1), all MEGA variants substantially outperform Multi-GNN baselines — e.g., MEGA-PNA reaches 78.26% vs. Multi-PNA's 66.48% on Medium HI. The gains hold across GIN, PNA, and GenAgg aggregation backbones, demonstrating the generality of the two-stage design.

- **Ablation study isolating contributions.** Table 2 separates bi-directional message passing and Ego-IDs, showing that MEGA-GNN without either already outperforms most prior work. This provides clear evidence about which components drive performance.

- **Throughput analysis showing modest overhead.** Figure 1 demonstrates that the multi-stage aggregation adds minimal runtime cost compared to the baselines, addressing a natural concern about efficiency.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The claim of being "the first message-passing framework explicitly designed for multigraphs" (Section 6, line 396) is factually inaccurate.** Both Multi-GNN (Egressy et al., 2024) and ADAMM are message-passing frameworks explicitly designed for multigraphs, as the paper itself discusses. The actual novelty is being the *first to perform multi-edge aggregation inside each message-passing layer while preserving individual edge features across layers*. This overstatement is easily fixable but erodes precision in an otherwise well-scoped paper.

- **The strongest empirical results are on synthetic data, with only marginal gains on the real-world benchmark.** On the AML datasets (synthetic), MEGA-GNN achieves large double-digit improvements over baselines. On the real-world ETH phishing dataset, the best result (MEGA-PNA: 64.84 ± 1.73) is within one standard deviation of the baseline (Multi-PNA: 64.61 ± 1.40). The paper is transparent about this — the abstract says "on par" — but the conclusion and abstract emphasize the 13% figure prominently without noting that it derives entirely from synthetic data. Adding "synthetic" to the abstract's description of AML datasets would improve clarity.

- **Limited analysis of *why* two-stage aggregation helps on the AML datasets.** The paper reports large gains but does not characterize the datasets by, e.g., number of parallel edges per node pair, edge-degree distribution, or how the advantage correlates with these statistics. A controlled experiment or diagnostic analysis would strengthen the evidence linking the architectural claim to the observed performance. Without it, the mechanism remains partially opaque.

- **Theoretical comparison with Multi-GNN's expressive hierarchy is incomplete.** The paper shows that MEGA-GNN is permutation equivariant while Multi-GNN is not (without ordering), and both are universal (with ordering). But when ordering is absent, the paper does not characterize whether the two architectures are expressively incomparable or whether one subsumes the other. Multi-GNN's port numbering distinguishes same-neighbor vs. different-neighbor edges in a way that is not permutation equivariant but may capture different structural information. A direct expressivity comparison (e.g., a counterexample showing where one outperforms the other in terms of function approximation) would sharpen the theoretical contribution.

- **Missing basic architectural details in the main text.** The paper does not state hidden dimensions, number of layers, learning rate, or optimizer settings. While the code is open-source, providing a one-sentence summary (e.g., "3 layers, hidden dim 64, Adam lr=1e-3") would aid reproducibility assessment without reading external code.

### Trivial

- The phrase "first message-passing framework" in the conclusion should be rephrased to reflect the actual scope of the novelty (see Minor weakness #1). This is the only place where the overstatement occurs; the rest of the paper is appropriately scoped.

## Nice-to-Haves

- Add a discussion of memory/compute complexity for the artificial nodes. The number of artificial nodes equals |E^supp|, which could be large in dense multigraphs. A brief complexity analysis would help practitioners.
- Run node classification on AML datasets (Table 2 only shows ETH for node tasks). The paper's framing as a "unified framework" would be better supported, though this is not necessary for the core contribution.
- A controlled experiment varying the number of parallel edges per node pair to directly test when two-stage aggregation provides the most benefit.

## Removed Points

These points were identified by the reviewers but are removed or downgraded after verification:

- **"Abstract gives equal weight to synthetic and real-world results."** Removed. The abstract explicitly says "up to 13% on Anti-Money Laundering datasets" (synthetic) and "is on par with their accuracy on real-world phishing classification datasets." The paper separates these claims clearly.
- **"Missing node classification on AML datasets is a weakness."** Removed. This is scope creep — the paper already evaluates edge classification on AML (the primary edge-level task for those datasets) and node classification on ETH. Doing node classification on AML would add breadth but is not required for the paper's claims.
- **"Scalability and memory concerns about artificial nodes are a serious weakness."** Downgraded to Nice-to-Have. The throughput analysis already shows practical efficiency, and the number of artificial nodes is bounded by |E^supp|, which is at most the number of edges.

## Novel Insights

Beyond the paper's own contributions, integrating the reviews yields one genuinely synthetic observation: the key architectural tension in multigraph GNNs is between *permutation equivariance* and *edge distinction*, and the paper demonstrates these are not fundamentally in conflict — via artificial nodes, permutation-equivariant multi-edge aggregation is achievable. This decouples a trade-off that prior work (Multi-GNN vs. ADAMM) had implicitly treated as binary. The empirical finding that bi-directional MP helps much more on the real-world ETH data than on synthetic AML data (Table 2, ablation) suggests that the practical benefit of the two-stage design may be task-dependent in ways the current analysis does not yet explain — this is a promising direction for future work.

## Suggestions

- **Fix the overstatement in the conclusion.** Replace "the first message-passing framework explicitly designed for multigraphs" with "the first framework to perform multi-edge aggregation inside each message-passing layer while preserving individual edge features" (or similar).
- **Add a diagnostic experiment.** On the AML datasets, report the distribution of parallel edge counts per node pair and show how MEGA-GNN's gain correlates with this statistic.
- **Include basic architectural hyperparameters in the experimental section** (hidden dims, layers, optimizer, learning rate).
- **Add a direct expressivity comparison with Multi-GNN** in the absence of strict total ordering — specifically address whether the two schemes are expressively incomparable or whether one subsumes the other on the function-approximation hierarchy.

## Score and Decision

**Originality**: 7/10 — The two-stage aggregation via artificial nodes is a clean and genuinely new architectural idea for multigraphs, though it builds on existing concepts (hypergraph GNNs, Multi-GNN).

**Importance**: 7/10 — Multigraphs are ubiquitous in financial, communication, and transportation networks, and principled GNN architectures for them are scarce. The paper addresses a real gap.

**Claims support**: 7/10 — The theoretical claims are appropriately conditioned and proven. The empirical claims are well-supported on synthetic data but only marginally confirmed on the real-world benchmark.

**Soundness**: 7/10 — The theory is sound, the experiments are properly designed (5 seeds, ablation, throughput analysis), and limitations are mostly acknowledged.

**Clarity**: 7/10 — The paper is well-structured and the motivating example is excellent. The "first" overstatement in the conclusion is the main clarity issue.

**Value**: 7/10 — The architecture, theoretical analysis, and code release will be useful to researchers working on multigraphs and financial crime detection.

**Overall**: The paper makes a solid contribution — a novel, theoretically grounded message-passing architecture for multigraphs with strong empirical results. The weaknesses are fixable and do not undermine the core contribution. 

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>