- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 3, 5, 5
Now I have all the information needed. Let me produce the consolidated review.

## Summary

ReHub introduces a graph transformer architecture that achieves linear complexity by dynamically reassigning graph nodes ("spokes") to a small constant number of virtual nodes ("hubs") per layer. The key insight is that each spoke only needs to interact with a small subset of hubs (k=3), and a cheap hub-hub similarity heuristic enables reassignment without expensive spoke-hub computation. The paper demonstrates that sparse spoke-hub connectivity with this dynamic reassignment closely matches the performance of fully-connected variants, while reducing memory consumption from O(n^{3/2}) (Neural Atoms) to O(n), and uses 36% less peak memory than Exphormer on large graphs with competitive accuracy.

## Strengths

- **Sparse reassignment matches dense performance across multiple backbones.** Tables 1 and 2 show ReHub (sparse, k=3) achieves results nearly identical to ReHub-FC (fully connected to all hubs) across five MPNN backbones (GCN, GCN2, GINE, GatedGCN, GatedGCN+RWSE). For example, on Peptides-func with GatedGCN: 0.6685 ± 0.0074 (sparse) vs 0.6732 ± 0.0107 (FC); on Peptides-struct: 0.2512 vs 0.2501. This directly validates the core claim that dynamic reassignment eliminates the need for expensive full connectivity.

- **Empirical demonstration of linear memory complexity.** The memory experiment (Figure 2) uses random regular graphs from 10K to 700K nodes and shows ReHub's peak memory scales linearly — using less than half the memory of Neural Atoms and Exphormer. On real large graphs (Table 4), ReHub uses 1.13 GB vs 1.77 GB on Coauthor Physics (36% reduction) and 2.45 GB vs 2.83 GB on OGBN-Arxiv (13% reduction).

- **Consistent improvement over Neural Atoms with strict lower complexity.** Across all five MPNN backbones (Table 1), ReHub outperforms Neural Atoms on every dataset while reducing complexity from O(n^{3/2}) to O(n). For instance, GatedGCN+RWSE on PCQM-Contact: 0.3528 vs 0.3262; on Peptides-struct: 0.2488 vs 0.2568.

- **Clean ablation study isolating contributions.** Table 3 progressively adds components (dynamic hub count, cluster-based initialization, reassignment, spoke encoding) with clear performance increments on PascalVOC-SP, from 0.3152 (GNN baseline) to 0.3860 (full model). The learned-hub baseline (0.3084) performing worse than the GNN baseline demonstrates that the initialization scheme is non-trivial.

- **Modularity across diverse MPNN backbones.** Table 1 tests ReHub with GCN, GCN2, GINE, GatedGCN, and GatedGCN+RWSE, showing consistent improvements across all backbones, establishing the method's generality.

## Weaknesses

### Fatal
None.

### Major
None. No verified weakness threatens the paper's core claims.

### Minor

- **The accuracy–memory trade-off on OGBN-Arxiv is under-characterized.** The paper describes the results on OGBN-Arxiv as "comparable accuracy" to Exphormer (Table 4), but the gap is 71.06 ± 0.40 vs 72.44 ± 0.28 — a 1.38 percentage-point drop that is roughly 3 standard deviations from the Exphormer mean. This is a non-trivial degradation, and the paper should candidly frame it as a trade-off (moderate accuracy drop for substantial memory savings) rather than as "comparable." It is also not stated whether the Exphormer numbers come from re-running under the same hardware/hyperparameter conditions or from the original paper.

- **COCO-SP results are not reported.** The paper says it evaluates on LRGB (five datasets) and lists COCO-SP in the datasets section, but Table 2 only reports results on Peptides-func, Peptides-struct, PCQM-Contact, and PascalVOC-SP. The omission of COCO-SP is not explained, which weakens the otherwise thorough evaluation.

- **Neural Atoms results on PascalVOC-SP are marked n/a without explanation.** In Table 2, Neural Atoms shows "n/a" for PascalVOC-SP. The paper should clarify whether this is due to out-of-memory, the method not being applicable, or results not being reported in the original paper.

- **The reassignment heuristic lacks direct validation against an exact nearest-hub oracle.** Algorithm 1 replaces each spoke's farthest hubs with the k-1 nearest hubs of the hub most similar to that spoke — a heuristic that assumes the closest hub is a good proxy. The ablation (Table 3) shows reassignment helps, but the paper does not compare against exact per-spoke nearest-hub selection (at O(n√n) cost) on a small dataset to quantify the approximation loss. This would directly bound how much performance the heuristic leaves on the table.

### Trivial
- **METIS initialization cost not discussed.** The paper uses METIS clustering (O(|E|) time) for initialization but does not mention its runtime relative to a forward pass. This is a one-time cost, but should be acknowledged for completeness.

## Nice-to-Haves
- **Hub utilization analysis could be deepened.** Figure 3 shows ~10% of hubs remain unused regardless of r and k. The paper could discuss whether unused hubs are harmful or beneficial (e.g., reserve capacity) and potentially run a simple experiment forcing all hubs to have at least one spoke.
- **Wall-clock training time** alongside memory would help practitioners assess throughput.
- **Positional encoding for geometric graphs** is acknowledged as a limitation in the conclusion; incorporating simple positional information for hubs (e.g., averaged spoke coordinates) could be explored.

## Removed Points

- **Hub-hub attention memory blowup concern (Harsh Critic's first Critical Issue).** The critic claimed that for n=700K, the √n×√n hub-hub attention matrix would be "840M entries (3.4GB in fp32)." This is factually incorrect: √700K ≈ 837, so the hub-hub matrix is ~837×837 ≈ 700K entries (~2.8 MB). There is no memory blowup, and no special implementation is needed. The paper's complexity analysis (Section 3, paragraph "Complexity") and empirical memory curve (Figure 2) are consistent. **Reason for removal: arithmetic error in the review.**
- **Missing appendix/proofs/hyperparameters.** Removed per hard rules: the PDF extraction strips appendix content that exists in the original submission. Hyperparameters may be detailed in the stripped appendix.
- **Missing related works.** Removed per hard rules: the reviewer cannot confirm the existence or absence of works not cited.
- **Formatting nitpicks.** Removed per hard rules as parser artifacts.

## Novel Insights

The most interesting observation from the reviewer cross-analysis is the asymmetry in how the paper's strengths and weaknesses interact: the sparse-vs-FC comparison (Tables 1, 2) is remarkably tight — the gap is typically <0.01 in AP/MAE — which is far stronger evidence for the reassignment heuristic than any theoretical bound could provide. Yet the paper's largest accuracy gap against a baseline (OGBN-Arxiv: -1.38% vs Exphormer) occurs in the very setting where the memory savings are largest. This suggests that the cost of the heuristic may be dataset-dependent (citation networks vs. molecular graphs), and understanding this dependence would be a valuable future direction.

## Suggestions

1. Clarify whether Exphormer results on Coauthor Physics and OGBN-Arxiv were obtained by re-running under the same conditions or taken from the original paper. If re-run, report whether the same hyperparameter tuning budget was used. If cited from the original paper, acknowledge that memory measurements may differ due to hardware and framework differences.
2. Report or explain the omission of COCO-SP from Table 2.
3. Add a brief explanation for Neural Atoms' n/a entry on PascalVOC-SP.
4. On a small dataset (e.g., Peptides-func), compare the heuristic reassignment against exact per-spoke nearest-hub selection to bound approximation loss.
5. Qualify the OGBN-Arxiv claim from "comparable accuracy" to something like "competitive accuracy with moderate degradation in exchange for substantial memory savings."
