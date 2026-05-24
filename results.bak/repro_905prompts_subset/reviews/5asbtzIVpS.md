Now I have enough information to write the consolidated review. Let me synthesize my findings.

---

## Summary

This paper proposes Forest-based Graph Learning (FGL), a paradigm where message passing on a graph is replaced by aggregation on a forest of spanning trees. Spanning trees are the minimal subgraphs connecting all nodes, so they achieve global coverage with linear cost. The framework has four steps: (1) a pre-processing step that augments the graph by adding edges between k-nearest neighbors in pseudo-label space, (2) a homophily-estimator-based tree sampler that biases the distribution toward high-homophily trees, (3) a linear-time tree aggregator derived from two recursions (Theorem 1) that realizes quadratic node-pair interactions, and (4) a tree fuser averaging the outputs. Theorem 2 establishes that as the edge-homophily estimate improves, the induced tree distribution asymptotically approaches the maximum homophily allowed by the graph structure. Empirical results on nine benchmarks show SOTA accuracy with competitive efficiency.

## Strengths

- **Novel paradigm with clean motivation.** The framing of the trade-off as Eq. 1 (total cost = cost-per-structure × number-of-structures) is clear and insightful. The identification of spanning trees as the minimal globally-covering structure is a genuinely novel lens on graph learning, and it leads to a paradigm that breaks from both deep GNNs and global transformers.

- **Sound theoretical result (Theorem 2).** Theorem 2 establishes a rigorous asymptotic relationship between the accuracy of the edge-homophily estimator and the quality of the induced tree distribution: monotonicity for sufficiently large Δ, an upper bound tied to the number of homophilous connected components, and asymptotic tightness. This provides principled justification for the homophily-guided sampling strategy.

- **Elegant algorithmic contribution (Theorem 1, Eq. 5–8).** The tree aggregator derivation from two simple properties (Combine and Disentangle) is clever. The concrete linear-time implementation (Eq. 7–8) that propagates messages in two recursions (bottom-up then top-down) is a practical algorithmic result, and the paper convincingly demonstrates its efficiency (Table 2: e.g., 0.005 sec/epoch on Cora, 0.246 on ArXiv).

- **Strong empirical results on the augmented-graph setup.** Even within the augmented-graph context, the ablation studies (Table 3) show that the forest mechanism contributes meaningfully: dropping the global submodule drops Texas accuracy from 91.89 to 82.88, uniform tree sampling drops to 82.58, and a single homophily-guided tree drops to 84.83. These internal comparisons support the claim that the forest-based aggregation and homophily-guided sampling matter.

## Weaknesses

### Major

1. **Uncontrolled confound between graph augmentation and the forest paradigm.** The pre-processing step (Section 4.1) adds edges to the graph based on pseudo-labels derived from the training labels, which "increases the *homophily ratio*" (paper's own words). The baselines in Table 1 operate on the *original* graph without this augmentation. There is no ablation that runs FGL on the original graph (without augmentation) to separate the effect of the added edges from the effect of the forest-based aggregation. Without this control, the extraordinary margins on heterophilous datasets (Cornell: 83.24 vs. next-best 76.76; Texas: 91.89 vs. next-best 78.92) cannot be cleanly attributed to the forest paradigm. The ablation studies (Table 3) all operate on the augmented graph, so they do not address this gap. The paper should either (a) demonstrate FGL's performance on the original graph or (b) compare against baselines that also receive the same augmentation.

2. **Missing baseline: simple models with the same augmentation.** Since the augmentation injects homophilous edges based on pseudo-labels, it would be informative to run a standard GCN or label propagation on the augmented graph. The comparison of row (1) in Table 3 (w.o. Global Submodule, which keeps the augmentation and local module) with the best baselines already suggests that the augmentation alone lifts performance (e.g., Texas: 82.88 with augmented graph + local module vs. 78.92 for SGFormer on the original graph), but we need to know whether a simple method on the augmented graph could match or exceed full FGL. Without this baseline, the specific advantage of the forest-based aggregation over simpler alternatives on the same graph remains unproven.

### Minor

3. **Ambiguous notation for the local submodule's graph.** Equation 9 uses $\hat{A}_G$ without a clear definition of whether this refers to the original adjacency or the augmented adjacency. The paper defines $\hat{A}$ (normalized adjacency of $A+I$) in Section 3, and $\hat{G}$ (augmented graph) in Section 4.1, but the subscripted $\hat{A}_G$ is never explicitly specified. Since the local submodule's graph could affect the interpretation of the ablation studies (Table 3, row (2)), this should be clarified.

4. **The value of *k* in the pre-processing step is not reported in the main text.** The number of nearest neighbors used for graph augmentation is never stated in the parsed paper. Given how central this step is — it determines how many edges are added and how much the homophily ratio is increased — the main text should specify *k* and the resulting change in edge count per dataset.

5. **Average rank in Table 1 is misleading.** The "Avg. Rank" column is computed across all 9 datasets, but several baselines have OOM entries (GT, SAN, Graphormer, TDGNN on Arxiv/Flickr). The rank presumably treats OOM as the worst rank, which inflates the gap (our method at 1.22 vs. next-best SGFormer at 7.22). Moreover, on datasets where FGL leads by only decimal points (e.g., Cora: 85.46 vs. GCNII: 85.34, within statistical noise), rank-based aggregation overstates the practical advantage.

### Trivial

6. The running time comparison (Table 2) reports only per-epoch training time of the student model, not including the pre-processing time (pseudo-label training, attention estimator training, Wilson sampling). Total time to solution would be a more complete picture, but the per-epoch figures are still informative for the core efficiency claim.

## Nice-to-Haves

- An ablation that removes only the augmentation while keeping the forest paradigm (e.g., by ensuring connectivity through some other mechanism or using a uniform distribution over spanning trees on the original graph).
- Comparison with label propagation or graph Laplacian regularization methods, which are natural competitors for the transductive setting.
- A brief proof sketch of Theorem 2 in the main text to help readers assess it without consulting the appendix.

## Removed Points

- *Criticism about independence of tree samples potentially leading to overfitting*: The paper's ablation explicitly compares single-tree vs. multi-tree variants, showing multi-tree helps, so the concern about overfitting to specific trees is partially addressed.
- *Claim that Theorem 2's novelty is "modest"*: While the bound is intuitive, the formal asymptotic tightness result is a genuine theoretical contribution that goes beyond what prior spanning-tree literature provides. This criticism undervalues the theoretical result.
- *Request for confidence intervals or standard deviations in Table 1*: Standard deviations are reported in Table 10 of the appendix, which is standard practice for papers with many baselines.
- *Criticism about pseudo-labels using the same training labels (transductive label propagation)*: This is true but not a flaw per se; the paper acknowledges the pre-processing step; the real issue is the lack of controlled comparison, not the transductive nature itself.
- *Several generic strength-finder points*: Removed claims about the problem being "important" (generic) and about the framework being "competitive" without specific evidence citation.

## Novel Insights

The paper's key conceptual insight — that spanning trees are the minimal globally-covering subgraph and thus strike an optimal balance in the "cost per structure × number of structures" equation — is genuinely novel and reframes the efficiency-coverage trade-off in a productive way. This insight could inspire follow-up work on other minimal-structure decompositions for graph learning. The theoretical framework linking the quality of a local homophily estimator to a global property of the tree distribution (Theorem 2) is also a useful bridge between local edge-level signals and global structural properties.

## Suggestions

1. **Run FGL on the original graph (without augmentation) to isolate the forest effect.** If the graph is not connected, use a different mechanism to ensure connectivity (e.g., connecting disconnected components via minimal edges) that does not inject label information.

2. **Include baselines that also receive the same graph augmentation.** For instance, run GCN, GAT, and label propagation on the augmented graph $\hat{G}$. If these simple methods match or approach FGL's performance, the contribution should be repositioned as a graph-augmentation + tree-aggregation pipeline rather than a pure forest paradigm.

3. **Report the value of *k* and the number of added edges per dataset in the main paper.**

4. **Clarify whether $\hat{A}_G$ in Eq. 9 refers to the original or augmented adjacency**, and state explicitly which graph each component operates on.

5. **Include a brief proof sketch of Theorem 2 in the main text** (even 3-4 sentences of intuition would help).

## Score and Decision

**Calibration report:**

*Round 1 (bracketing):* Queried for papers on graph neural networks with spanning trees or forest-based architectures. Weak-band anchors (avg 2.60–3.00, sim 0.69–0.71) were clearly below FGL in novelty and rigor. Middle-band anchors (avg 4.75–6.50, sim 0.71–0.72) included a range of papers with mixed quality. Strong-band anchors (avg 8.00, sim 0.67–0.68) were substantially more rigorous theoretically and empirically. Initial bracket: [5, 7].

*Round 2 (narrowing):* Examined anchors more closely:
- Posterior Label Smoothing (5.50, sim 0.76): simpler contribution, marginal gains, but clean experimental design without the confound issue. FGL has stronger novelty but a more significant empirical gap.
- Graph Parsing Networks (6.00, sim 0.68): novel pooling architecture with solid experiments. Comparable novelty level; FGL is architecturally more innovative but has a weaker empirical case.
- Neural Spacetimes for DAGs (6.80, sim 0.69): strong theory but missing downstream task validation. FGL has more complete task evaluation.

FGL's core idea (spanning-tree paradigm) is more novel than any of these anchors. However, the uncontrolled augmentation confound in the empirical evaluation is a real weakness that these comparison papers do not share. The paper sits between Graph Parsing Networks (6.00) and Neural Spacetimes (6.80) in terms of contribution strength but below both in experimental rigor. Final score: **6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>