## Summary

The paper proposes **Forest-based Graph Learning (FGL)**, a novel paradigm for semi-supervised node classification that decomposes graph-level message passing into propagation over a *forest* of spanning trees. The core insight is that spanning trees represent the minimal subgraph connecting all nodes, providing global coverage at lower cost than dense attention while avoiding the scalability bottleneck of stacked local layers. The framework consists of four components: graph pre-processing (connectivity augmentation via pseudo-label-guided k-NN edges), a homophily-guided tree sampler based on Wilson's algorithm, a general linear-time tree aggregator achieving all-pairs interactions via two-pass tree DP, and a mean tree fuser. The paper provides a theoretical result (Theorem 2) showing that as the estimated edge-homophily score ratio Δ = p/q increases, the induced spanning-tree distribution concentrates on high-homophily trees.

---

## Strengths

- **Genuinely novel paradigm with clean conceptual grounding.** The decomposition of total cost as (cost per structure) × (number of structures) cleanly identifies why both deep local models and shallow global models fail, and motivates the spanning tree as the right intermediate structure. This framing is lucid and compelling.

- **Strong theoretical contribution.** Theorem 2 establishes monotonicity, an upper bound, and asymptotic tightness of the expected homophily ratio under the induced distribution. The upper bound in terms of the number of homophilous connected components is informative and non-trivial.

- **General and expressive tree aggregator.** Theorem 1 provides a two-pass recursion framework (bottom-up S-collection + top-down H′-computation) that achieves O(n²) node-pair coverage in O(n) time. The characterization through Properties (I)/(II) (Combine/Disentangle) abstracts away the specific aggregator, making it compatible with linear attention, RNNs, and SSMs—a meaningful generality claim backed by concrete examples.

- **Impressive and broad empirical results.** FGL ranks first overall (Avg. Rank 1.22 vs. 7.22 for the second-best SGFormer) across 9 benchmarks and 26 baselines. Gains on heterophilous graphs are large: +13 pp on Texas (91.89 vs. 78.92), +5.9 pp on Wisconsin (86.27 vs. 80.39), +6.5 pp on Cornell (83.24 vs. 76.76). Large-scale benchmarks (ArXiv, Flickr) also improve over all prior methods.

- **Efficiency demonstrated concretely.** Table 2 shows 2–10× speedup over competitive baselines (DIFFormer, GCNII, GOAT) while simultaneously achieving higher accuracy, grounding the theoretical linear-complexity claims in measured wall-clock time.

- **Thorough ablation.** The ablation study cleanly isolates the contributions of the global submodule (tree aggregator), local submodule, homophily-guided vs. uniform sampling, and single vs. multiple trees, with results consistent across all 9 datasets.

---

## Weaknesses

### Fatal
None. The core claims are internally consistent and supported by theory and experiments.

### Major

1. **Pre-processing augmentation is exclusive to FGL, creating a potentially unfair comparison.** The k-NN edge-insertion step (Sec. 4.1) modifies the graph in a way that no baseline benefits from. Table 3 row (1) (without global submodule = local-only with augmentation) already reaches 83.92 on Wisconsin, beating the best baseline (GraphMamba at 80.39) before any tree propagation. The gains on heterophilous graphs could be largely attributable to the augmentation rather than the forest paradigm. A fair evaluation would require applying the same augmentation to top baselines (e.g., SGFormer + k-NN augmentation) to isolate the contribution of the FGL mechanism. This is absent from the paper.

2. **Multi-stage training complexity and total cost are not reported.** Table 2 reports per-epoch training times, but FGL requires at least three stages: (a) pre-training a GCN/MLP for pseudo-labels, (b) training the local attention homophily estimator, and (c) training the full model. Total wall-clock time including all stages is not compared. This is a significant omission given that efficiency is a central claim.

3. **Wilson's algorithm complexity claims are imprecise.** The paper states "nearly O(n) time per-tree" for Wilson's algorithm. In expectation, Wilson's algorithm runs in O(cover time), which is O(n log n) for expanders but O(n²) or worse for sparse or poorly-connected graphs. The "nearly O(n)" claim is optimistic for general graphs and lacks qualification. For heterophilous real-world graphs that require pre-processing to become connected, this is particularly relevant.

### Minor

1. **The "quadratic node-pair interactions" claim needs clarification.** The abstract and introduction prominently state that the tree aggregator "realizes quadratic node-pair interactions." This is technically accurate (every node receives aggregated messages from all others), but the interaction is mediated through a tree path, not a direct pairwise function. This should be stated more precisely to avoid overstating expressiveness relative to full attention.

2. **Effect of number of k-NN neighbors (k) in pre-processing is not ablated.** This hyperparameter controls how much the graph is structurally modified, and its sensitivity is not reported.

3. **Abstract undersells the empirical gains.** The abstract says "comparable results against state-of-the-art," but the method achieves the best Avg. Rank of 1.22 and improves Texas by 13 pp—these are clearly *better*, not merely comparable results.

### Trivial
None worth listing.

---

## Nice-to-Haves

- An experiment where the same k-NN augmentation is applied to a strong baseline (e.g., SGFormer) would sharpen the attribution of gains to the FGL mechanism vs. the pre-processing.
- A reported total training time (all stages combined) in Table 2 would make the efficiency claim more complete.
- Qualification of Wilson's algorithm complexity with appropriate assumptions (e.g., spectral gap, mixing time) would strengthen the theoretical claims.
- Extending experiments to at least one graph-level or link-prediction task would demonstrate the paradigm's broader applicability beyond the specific benchmark suite.

---

## Novel Insights

The paper's genuinely novel observation is that spanning trees—as the minimal connected subgraphs—occupy a "Goldilocks" position in the cost-coverage trade-off space of graph learning structures: they achieve global coverage (O(n²) node-pair reachability) at O(n) structural cost. The two-pass recursion on trees for aggregating all-pairs information in linear time (Theorem 1) is an elegant instantiation of this insight, and the theoretical connection between homophily estimator quality and induced distribution quality (Theorem 2) provides principled direction for model improvement. The empirical confirmation that improving the homophily estimator monotonically improves classification accuracy—including an approximate oracle study—is also a useful diagnostic tool for future work on structure-aware sampling.

---

## Suggestions

- Add a single ablation row to Table 3: a strong baseline (e.g., SGFormer) trained on the k-NN-augmented graph without the tree framework. This would establish the baseline's contribution cleanly.
- Report total training time across all stages (not just per-epoch inference time) in Table 2 or a supplement.
- State Wilson's algorithm complexity as "O(cover time)" and note that for the benchmark graphs empirically observed to have near-linear cover times, this is effectively O(n).
- Clarify the "quadratic node-pair interactions" claim with a brief note that interactions are global (all pairs reachable) but mediated through tree paths.

---

## Score and Decision

The paper makes a coherent, theoretically grounded, and empirically strong contribution to the problem of efficient global message passing on graphs. The spanning-tree paradigm is novel, the theoretical results are substantive, and the performance gains are large and consistent. The main concern—the potential confound from graph augmentation exclusive to FGL—is a legitimate methodological issue but does not invalidate the core contribution, especially given that ablation results show the tree aggregator component contributes meaningfully independent of augmentation. The efficiency story is compelling and well-documented at the per-epoch level. The work advances the field in a meaningful direction and belongs at a top venue.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>