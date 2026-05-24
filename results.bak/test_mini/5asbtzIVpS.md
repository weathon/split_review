Confirmed: Eq. 3 defines α over the first-order neighborhood N(i), making it local. The critic's claim that "α is dense in principle" is factually incorrect. Now let me write the final consolidated review.

---

## Summary

This paper proposes Forest-based Graph Learning (FGL), a paradigm for semi-supervised node classification that reinterprets message passing as transportation over a forest of spanning trees. The core insight is that a spanning tree is the minimal subgraph achieving global coverage, so using a forest (multiple trees) enables global receptive fields at linear cost. The framework consists of: (1) a pre-processing step augmenting the graph via pseudo-label edge addition to ensure connectivity and increase homophily; (2) a homophily-estimator-guided tree sampler that biases sampling toward homophilous trees (with theoretical guarantees in Theorem 2); (3) a general tree aggregator achieving quadratic node-pair interactions in linear time (Theorem 1); and (4) a tree fuser combining local and global information. Empirically, FGL achieves the best average rank (1.22) across 9 benchmark datasets and is among the fastest methods tested.

## Strengths

1. **Novel paradigm that identifies and exploits spanning trees as the minimal globally covering substructure.** The paper articulates the cost trade-off (Eq. 1) as cost-per-structure × number-of-structures and observes that spanning trees simultaneously minimize both factors — they are the simplest subgraph connecting all nodes. This insight is directly realized: Table 2 shows FGL is the fastest among all strong baselines on 4 of 5 datasets (e.g., 0.005 sec/epoch on Cora vs. 0.010–1.453 for competitors), and the ablation in Table 3 shows that increasing the number of trees from 1 to ~6–10 consistently improves accuracy.

2. **Theorem 2 provides a non-trivial bound linking edge-score accuracy to tree quality.** Theorem 2 establishes monotonicity, an upper bound involving the number of homophilous connected components (NHCC) of the augmented graph, and asymptotic tightness — showing that as the edge-score ratio Δ = p/q grows, the expected tree homophily approaches the structural limit 1 − (NHCC−1)/(n−1). This bound depends on graph structure, not just the scoring function, and is empirically validated in Figure 5 where increasing homophily-estimator accuracy monotonically improves classification accuracy.

3. **Comprehensive experimental validation on 9 diverse benchmarks.** FGL is evaluated on homophilous (Cora, Citeseer, Pubmed, Arxiv) and heterophilous (Actor, Cornell, Texas, Wisconsin, Flickr) graphs against 26 baselines including GNNs, deep GNNs, graph transformers, and Mamba. It achieves the highest accuracy on 7 of 9 datasets with average rank 1.22, with relative gains of 11.9–16.2% against representative methods like GCNII and DIFFormer.

4. **Ablation studies systematically isolate each component's contribution.** Table 3 compares five variants (removing global submodule, removing local submodule, uniform tree sampling, single tree, full model) on all 9 datasets. This enables the reader to attribute gains: e.g., on Texas, the global (forest) submodule adds 9.01 points beyond the local-only version (91.89 vs. 82.88), and homophily-guided sampling adds 2.25 points over uniform sampling (84.83 vs. 82.58).

## Weaknesses

### Major

- **The pre-processing step confounds the evaluation of the forest paradigm on heterophilous graphs.** The method augments the graph by adding edges based on pseudo-labels (Section 4.1), which the paper states "increases the homophily ratio." On small heterophilous graphs (Texas, Wisconsin, Cornell with ~200 nodes), this can substantially alter the graph structure. The paper does not report the homophily ratio of the augmented graph, does not compare baselines on the same augmented graph, and does not include an ablation variant without pre-processing. Since the largest gaps over baselines occur on these small heterophilous datasets (e.g., Texas: Ours 91.89 vs. best baseline SGFormer 78.92), a reader cannot determine how much of the gain comes from the augmentation vs. the forest paradigm. This is the paper's most significant weakness — the evaluation design makes it difficult to attribute the reported gains to the core methodological contribution.

### Minor

- **The claimed generality of the tree aggregator is unsubstantiated by experiments.** The paper states that "many popular auto-regressive sequence models and first-order GNN aggregators can be adopted" as tree aggregators (Section 4.3), and Theorem 1 is given as a general framework. However, the implementation uses only a simple linear weighted-sum variant (Eqs. 7–8). No nonlinear aggregator, RNN, SSM, or attention variant is tested. While the paper acknowledges prioritizing a linear variant "for simplicity," the generality claim remains a speculation without empirical support.

- **The theoretical contribution (Theorem 2) is modest.** The core result — that assigning higher scores to homophilous edges biases the spanning-tree distribution toward higher-homophily trees — is a relatively straightforward property of weighted spanning-tree distributions. The NHCC-based bound provides structural insight, but the theorem does not directly connect tree homophily to classification performance, and the empirical evidence for it (Figure 5) uses synthetic control of edge scores rather than the actual learned estimator.

- **The pre-processing hyperparameter k (number of nearest neighbors for edge addition) is not stated in the main paper** and the analysis of how many edges are added to each dataset is absent. This makes it harder to assess the extent of graph modification across datasets.

### Trivial

- The introduction's claim that the paradigm "breaks the unavoidable trade-off" is overstated — the method shifts the trade-off to a more favorable operating point (moderate number of structures, each with moderate per-structure cost) rather than eliminating it entirely.

## Nice-to-Haves

- Testing the generality of the tree aggregator by instantiating at least one nonlinear variant (e.g., a gated RNN or SSM-based aggregator) and comparing its performance to the linear variant.
- Reporting the homophily ratio of each dataset before and after the pre-processing augmentation to help readers assess the effect.
- Including a baseline comparison where existing methods (e.g., GCNII, GAT, SGFormer) are run on the same augmented graph, to isolate the forest paradigm's contribution from the augmentation's contribution.

## Removed Points

1. *"The local module (Eq. 9) is a black box that itself captures long-range information"* — REMOVED because Eq. 3 defines α over the first-order neighborhood N(i), so α is local (not dense), and K_L ≤ 2 means the module is at most 2-hop propagation. The critic's premise that α is "dense in principle" is factually incorrect.
2. *"No comparison with graph rewiring methods"* — REMOVED because the paper cites graph rewiring (Shirzad et al., 2023) in the related work and positions FGL as addressing a different fundamental paradigm question, not as a rewiring variant.
3. *"No code release verification"* — REMOVED per hard rules (all cited entities are assumed to exist).
4. *"No limitations paragraph"* — REMOVED as a formatting preference, not a substantive weakness.
5. *"Missing related works"* — REMOVED per hard rules (cannot verify existence of unmentioned works without external sources).

## Novel Insights

None beyond the paper's own contributions. The reviews surface the pre-processing confound as the central unresolved question, but this is a critique of the evaluation design rather than a novel observation about the method itself.

## Suggestions

1. **Disentangle the pre-processing contribution experimentally.** On each dataset, report: (a) the homophily ratio of the original graph, (b) the homophily ratio of the augmented graph, and (c) performance of several representative baselines (e.g., GAT, GCNII, SGFormer) when run on the *same* augmented graph. This would directly address the main confound concern.
2. **Add an ablation variant "FGL without pre-processing"** (using the original un-augmented graph, possibly with a different connectivity fix) to show whether the forest paradigm itself drives the gains or whether the augmentation is the dominant factor.
3. **Report the value of k and statistics of added edges per dataset** to improve reproducibility and transparency.
4. **Consider testing one nonlinear tree aggregator** (e.g., a gated variant) to substantiate the generality claim of Theorem 1.
5. **Add a limitations paragraph** discussing the dependence on the pseudo-label model, the risk of false connections from the augmentation, and the fact that spanning trees discard cycles by construction.

## Score and Decision

**Calibration:**

*Round 1 (bracketing):* Queried three bands on "semi-supervised node classification on heterophilous graphs" / "spanning trees forest graph" / "efficient global receptive field tree aggregation." Low band (avg < 3.5): papers scoring 2.50–3.33 (rejected). Middle band (3.5–7.5): papers scoring 4.00–6.67 (mix of accepts and rejects). High band (7.5+): papers scoring 8.00–8.50 (all accepts, but none on graph learning). Initial bracket: between 4.5 and 6.5.

*Round 2 (narrowing):* Used more targeted queries on "graph neural network node classification spanning tree forest aggregation homophily" and "node classification heterophily graph transformer efficient." Key anchors read in full:

| Paper | Avg Score | Decision | Comparison |
|-------|-----------|----------|------------|
| CTNN (yumDmlGCc9) | 5.00 | Accept (Poster) | Similar tree-cover approach but graph classification on molecular/protein benchmarks; weaker empirical results (1–2% gains), more limited benchmarks. FGL has stronger results but a more significant evaluation confound. |
| GRAPHITE (owZ6KNAtYU) | 4.50 | Accept (Poster) | Graph homophily boosting; accepted despite limited novelty concerns and discrete-features-only limitation. FGL has a more novel paradigm and more comprehensive evaluation. |
| HarmonyGNNs (mGxtoQY3GA) | 6.00 | Accept (Poster) | Self-supervised for heterophily/homophily; strong results but some theoretical assumptions are unrealistic. FGL has comparable evaluation breadth but a more concerning evaluation confound. |
| From Fields to Random Trees (5VN11Hd3uY) | 6.67 | Accept (Poster) | Spanning-tree sampling for MAP inference; cleaner theory (error bounds, concentration) but limited comparisons and different problem domain. |

FGL is stronger than CTNN (5.00) and GRAPHITE (4.50) in terms of paradigm novelty and evaluation breadth, but the pre-processing confound makes its evidence less clean than HarmonyGNNs (6.00). The paper sits between these anchors.

**Final score: 5.5**

The paper introduces a genuinely novel and well-motivated paradigm with strong empirical results. However, the evaluation confound from the pre-processing step prevents clear attribution of the reported gains to the forest paradigm, especially on small heterophilous graphs where the largest margins occur. This is a significant (but addressable) weakness rather than a fatal one — the method's transparent design and informative ablation studies provide a path toward resolution. With the disentanglement experiments suggested above, the paper would be considerably strengthened.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>