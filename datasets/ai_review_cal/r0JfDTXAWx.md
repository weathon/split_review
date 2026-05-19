- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 5, 5, 3
Now I have all the information needed. Let me compose the final consolidated review.

## Summary

This paper proposes Common Neighbor Induced Message Passing (CNMP), a framework for inductive link prediction in knowledge graphs. The core insight is that 2-hop enclosing subgraphs used by prior GNN-based methods lose key entities and relations, creating disconnected reasoning paths that hinder message passing. CNMP addresses this by updating distance labels of isolated common neighbors (enabling message passing through disconnected paths by relabeling edge features), while CNMP+ expands subgraphs via a probing/pruning strategy to preserve more complete reasoning paths without introducing excessive irrelevant nodes. The framework is combined with two GNN backbones (RCN and RGCN) and evaluated across 12 inductive benchmarks, large-scale ILPC datasets, and fully inductive settings, consistently outperforming strong baselines including NBFNet, GraIL, and RMPI.

## Strengths

- **Quantifies a concrete problem with statistical evidence**: Section 2.2 (Tables 1 and 2) provides clear statistics that over 45% of 2-hop enclosing subgraphs on WN18RR contain only the target relation, and over 75% of 3-hop subgraphs introduce irrelevant relations. This diagnostic analysis of why existing subgraph extraction fails is a contribution beyond prior work and anchors the paper's motivation in measurable data.

- **Achieves state-of-the-art results across all 12 inductive benchmarks**: Table 3 shows CNMP models achieve the best AUC-PR on every version of WN18RR, FB15k-237, and NELL-995, with average improvements over NBFNet of 1.63%, 1.41%, and 1.70% respectively. Table 4 shows consistent HITS@10 gains (e.g., 2.69% on WN18RR, 5.47% on NELL-995 over NBFNet). These gains are observed across twelve dataset versions with varying sizes, supporting robustness.

- **Demonstrates scalability on large KGs where competitors fail**: Table 5 shows that on ILPC-large, NBFNet runs out of memory while CNMP models succeed and outperform GraIL and TACT on both MRR and HITS@10. This directly supports the claim that CNMP's subgraph-based approach has practical scalability advantages over methods operating on the full KG.

- **Generalization confirmed in the fully inductive setting**: Table 6 shows CNMP models outperform RMPI, NBFNet, GraIL, and TACT on all fully inductive benchmarks (where both entities and relations are unseen during training), demonstrating that the improvements are not limited to standard inductive splits.

## Weaknesses

### Fatal
None.

### Major

- **Missing ablation isolating the CNMP contribution**: The paper reports results for CNMP-base (RCN + CNMP) and CNMP model (RGCN + CNMP), but never reports the performance of RCN or RGCN *without* the CNMP strategies. The CNMP model uses RGCN (the same backbone as GraIL), so the improvements over GraIL *are* attributable to CNMP — partially mitigating this concern. However, for the CNMP-base model (RCN + CNMP), there is no RCN-only baseline at all. Without this controlled comparison, a reader cannot fully disentangle whether the gains come from the CNMP strategies or from architectural differences in how the backbone is configured or tuned. This is the paper's most significant evidential gap. (Verified: no RCN-only or RGCN-only results appear in the paper.)

### Minor

- **CNMP+'s "path reconstruction" language is somewhat overstated**: The paper describes CNMP+ as "reconstructing the original reasoning path with precision" (line 27) and claims "each node and relation is indispensable on the reasoning path" (line 104). However, Algorithm 2 builds a computational graph from the *union* of distilled neighborhoods of *u* and *v* separately (Distilled\_k = ∪𝒩ᵢ(u) ∪ ∪𝒩ᵢ(v)), which can include nodes reachable from *u* that are not on any path to *v*. The pruning condition (node must have a neighbor in the next-hop boundary) is necessary but not sufficient to guarantee path membership. The claimed precision thus exceeds the algorithmic guarantee.

- **No standard deviations or error bars reported**: The paper states it runs each experiment five times with different random seeds and reports mean results, but no variance is shown in Tables 3–6. Without confidence intervals, the statistical significance of smaller margins (e.g., ~1% AUC-PR improvements over NBFNet on some datasets) cannot be assessed.

- **Scalability claim lacks runtime or memory measurements**: The "scalability evaluation" (Table 5) reports only MRR and HITS@10. No wall-clock time, memory consumption, or inference cost data is provided. The claim of "superior scalability" is supported only by the fact that NBFNet OOMs while CNMP succeeds — which shows feasibility, not efficiency.

- **Distance computation cost is not discussed**: CNMP requires computing shortest-path distances *d(i,u)* and *d(i,v)* in the original KG for every isolated common neighbor (Algorithm 1, lines 8, 77). In large graphs with many isolated nodes, this could require per-triple BFS, which may dominate runtime. The paper does not analyze this cost.

- **Algorithm 1 has a minor underspecification**: Line 10 (and line 79 in the text) references "the relation between nodes *i* and *j*" without defining *j*. From context, *j* is a neighbor of *i* in the original graph, but this should be explicit.

- **No discussion of the choice of hop *k***: All experiments use *k=2*. The paper does not discuss whether performance is sensitive to this hyperparameter or justify why *k=2* is optimal.

- **Asymmetry between Int\_k and Distilled\_k in Algorithm 2 is unexplained**: `Int_k` uses the *k*-hop common neighbor intersection, while `Distilled_k` uses neighborhoods up to *k−1*. The reason for this asymmetry (and why the *k*-th distilled neighborhoods are excluded) is not discussed.

### Trivial

- None beyond the minor clarity issues noted above.

## Nice-to-Haves

- Analyze the CNMP+ pruning decisions on a few sample triples: how many irrelevant nodes are removed, and are any relevant nodes incorrectly pruned?
- Include a runtime/memory comparison on ILPC datasets to substantiate the scalability claim beyond feasibility.
- Add an analysis of how performance varies with the number of negative samples in ranking evaluation (currently fixed at 50).

## Removed Points

These points were flagged by reviewers but are excluded from the main weaknesses list for the following reasons:

- **"CNMP does not restore any path" (Harsh Critic, Critical Issue 1, regarding CNMP)**: The paper consistently describes CNMP as restoring *connectivity* (e.g., "restore the connectivity of the disconnected reasoning paths," line 21; "efficiently restore path connectivity," line 43), not literally returning missing entities. This is an accurate description of what the distance-label update does. The critic's reading conflates "restoring connectivity" with "reconstructing the original subgraph structure." Removed as a strawman.

- **"Comparison with more recent methods (ULTRA)"**: The paper already compares against 10 baselines including the strong NBFNet. Requesting additional methods without evidence that they are necessary to benchmark against is scope-creep. Removed per soft rules.

- **"Missing related works"**: The review cannot verify from external sources. Removed per hard rules.

- **"Formatting inconsistencies (truncated column headers, Appendix references stripped by parser)"**: These are parser artifacts, not author errors. Removed per hard rules.

- **"The 'equivalence relation' terminology is misleading"**: This is a subjective terminology preference. The paper defines what it means by the term in context (lines 23, 58–59), so no reader would be confused. Removed as a stylistic nitpick.

- **"Rule-based motivation is not operationalized"**: The rule-based discussion (Section 2.1) is used as *motivation* and *intuition*, not as the method itself. Criticizing it for not being operationalized misunderstands its role. Removed.

## Novel Insights

None beyond the paper's own contributions. The paper itself surfaces a useful diagnostic: that the prevalence of disconnected paths in 2-hop enclosing subgraphs can be measured (Tables 1, 2) and correlates with the headroom for improvement via connectivity-aware message passing. This observation is the paper's own doing, not something the reviews contribute.

## Suggestions

1. **Add the controlled ablation**: Report results for RCN alone (without CNMP) and RGCN alone (without CNMP) on a representative subset of benchmarks (e.g., WN18RR v1–v4 and NELL-995 v1–v4). This would isolate the incremental value of the CNMP strategies and directly address the paper's most significant evidential gap.

2. **Report error bars** for the main experiments (Tables 3, 4, 6), since the paper already runs five seeds — reporting mean ± std would add substantial rigor at no additional experimental cost.

3. **Soften the CNMP+ claims**: Replace "reconstructs the original reasoning path with precision" with "constructs a pruned subgraph that preserves likely path entities" and note the limitations of the pruning heuristic.

4. **Clarify Algorithm 1**: Explicitly define that *j* iterates over neighbors of *i* in the original graph (not the subgraph). Clarify the computational cost of computing *d(i,u)* and *d(i,v)*.
