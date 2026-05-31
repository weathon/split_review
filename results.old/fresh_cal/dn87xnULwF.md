Now I have all the information I need. Let me write the final consolidated review.

## Summary

This paper proposes CAT (Cyclic Adjacency Transform), a linear-time graph preprocessing method that provably makes the 1-WL test (and thus any sufficiently expressive MPNN) maximally expressive on outerplanar graphs — a class covering 92–97% of molecular graphs in standard benchmarks. The key idea is to decompose each biconnected outerplanar component, encode its unique Hamiltonian cycle in both directions, and annotate non-cycle edges with cycle distances, so that the full Hamiltonian adjacency list (HAL) sequence is captured in WL's unfolding trees. The paper proves Theorems 1 and 2 establishing that WL after CAT distinguishes all non-isomorphic outerplanar graphs, and provides empirical results showing that GIN+CAT and GCN+CAT improve performance on 7 of 9 molecular benchmarks.

## Strengths

- **Provable maximal expressivity on a practical graph family in linear time**: Theorem 2 establishes that WL after CAT can distinguish any two non-isomorphic outerplanar graphs, and the transformation runs in linear time by exploiting Mitchell (1979) and Tarjan (1972). This combination of a worst-case theoretical guarantee with efficient preprocessing is the paper's central contribution.

- **Strong empirical improvement for GIN and GCN**: Table 4 shows GIN+CAT outperforms GIN on 7 of 9 datasets and GCN+CAT outperforms GCN on 7 of 9 datasets. On ZINC the MAE drops from 0.139→0.092 for GIN and 0.156→0.092 for GCN — substantial gains comparable to far more expensive methods.

- **Connectivity improvements with theoretical backing**: Table 3 shows average pairwise effective resistance decreases on all 8 datasets and max resistance decreases on 7 of 8. Observations 1–2 and Proposition 1 provide worst-case bounds (diameter increases by at most 7), while in practice diameter often decreases.

- **Real-world relevance quantitatively established**: Table 1 shows 92–97% of graphs in ZINC, MOLHIV, and other benchmarks are outerplanar, justifying why focusing on this restricted class is practically valuable.

- **Graceful handling of non-outerplanar graphs**: The method degrades gracefully on non-outerplanar blocks (reverting to a single copy without expressivity guarantees) while maintaining linear-time preprocessing, since non-outerplanarity is detected during the Hamiltonian cycle computation.

## Weaknesses

### Fatal
None.

### Major

- **The proof of Theorem 1 is presented as a sketch that leaves the central reconstruction argument unjustified.** The proof asserts that "the rest of the HAL sequence and the node labels of G can be reconstructed from the unfolding tree of any node in CAT*(G)" but does not explain how the *cyclic order* of the full sequence emerges from the tree structure. It mentions that non-cycle edges carry distance annotations and that the two directed copies handle the direction ambiguity, but it never explicitly argues why the unfolding trees of *all* nodes, taken together and compared via WL's stable coloring, encode the concatenated HAL sequence in a way that resolves cyclic shifts. This is the entire basis of CAT*'s expressivity. The claim that "after at most n iterations WL will succeed" is stated without justification. Because Theorem 2 depends on Theorem 1, this gap propagates to the paper's main result. The proof exposition needs to be substantially expanded (or the missing rigorous argument signaled more clearly) for the theoretical contribution to be verifiable from the main text.

### Minor

- **No direct empirical verification of the expressivity claim.** The paper does not test whether WL after CAT can actually distinguish the canonical hard pair from Figure 5 (decalin vs. bicyclopentyl) or any other pair of non-isomorphic, 1-WL-indistinguishable outerplanar graphs. Showing that the stable colorings differ (or that a simple linear probe on MPNN+CAT embeddings can separate them) would directly confirm that the theoretical guarantee is realized in practice. While the benchmark results are consistent with increased expressivity, they do not isolate it from other factors (changed inductive bias, connectivity improvements, etc.).

- **No systematic comparison with other practical expressive GNNs.** The paper motivates CAT by arguing that existing higher-order GNNs (3-GNNs, subgraph GNNs, cycle-counting methods) are impractical, but it benchmarks against none of them. The only numerical comparison is a single MAE for CW Networks (0.079) mentioned in text without statistical variation or runtime comparison in a table. Without such comparisons, it is difficult to assess whether CAT's gains are competitive with other approaches that also enhance expressivity on the same graphs.

- **GAT results are acknowledged but not analyzed.** The paper notes "surprisingly, CAT does not work well with GAT and only improves its performance in 2/9 datasets" but offers no analysis or hypothesis about why. Since GAT is a widely used architecture, understanding whether this is a fundamental limitation (e.g., attention mechanisms cannot exploit the structured distance annotations) or an incidental tuning issue would strengthen the paper.

- **No ablation of CAT's components.** The transformation has several design elements (bidirectional cycle copies, distance annotations on non-cycle edges, pooling nodes, block nodes, global pooling node). Without ablations, it is impossible to know which components drive the performance gains and which are incidental to the theoretical argument.

### Trivial

- **Table 2 reports preprocessing runtime but without standard deviations**, which would be useful for assessing variability.

## Nice-to-Haves

- A small sanity-check experiment showing that WL colors (or MPNN embeddings) differ on decalin vs. bicyclopentyl after CAT would directly vindicate the theory.
- An ablation removing the reverse cycle copy (or the distance annotations) to isolate essential components.
- Analysis of why MOLLIPO and MOLTOX21 (both >95% outerplanar) show no improvement even for GIN/GCN.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Missing appendix may contain rigorous proof"** — Speculation about stripped appendix content; the core criticism (proof too sketchy) is retained above, but the speculation about what the appendix may or may not contain is removed.
- **"Duplicate MOLHIV in Table 4"** — Parser artifact; the original submission does not have this issue.
- **"Code availability not mentioned"** — Standard for submissions; not a weakness of the paper's scientific content.
- **"Standard deviations for runtime overhead"** — Retained as trivial above.
- **"Connects theoretical expressivity to practical GNN architectures"** (from Strength Finder) — Generic; citing Morris et al. (2019) and Xu et al. (2019) for the WL-MPNN equivalence is standard practice, not a distinctive strength.

## Novel Insights

The reviews do not surface an insight beyond what the paper itself contributes. The core observation — that the unique Hamiltonian cycle of biconnected outerplanar components can be used to encode HAL sequences into WL's unfolding trees via a linear-time transformation — is the paper's own novel contribution. No reviewer identified a hidden implication or connection that the authors missed.

## Suggestions

1. **Expand the Theorem 1 proof.** Provide a concrete argument for how the cyclic order of the HAL sequence is reconstructed from the unfolding trees at all starting points. A figure showing the unfolding trees of two adjacent nodes and how their combination resolves the cycle order would help.
2. **Add a Section 5 direct expressivity experiment.** Report WL stable colorings (or a simple probe on MPNN embeddings) for decalin vs. bicyclopentyl before and after CAT, confirming they become distinguishable.
3. **Include at least one practical expressive-GNN baseline** (e.g., GSN with cycle counts or a subgraph-based method) in Table 4 for context.
4. **Ablate the bidirectional copy:** Show performance when using only one direction of the Hamiltonian cycle to demonstrate that the reverse copy is necessary.
5. **Add brief discussion of the GAT failure** — even a hypothesis about attention mechanisms and structured edges would satisfy this.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>