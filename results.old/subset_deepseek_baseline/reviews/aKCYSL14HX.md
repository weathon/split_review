## Summary

This paper proposes DiskHIVF, a hybrid memory-disk ANNS index that uses a two-level hierarchical k-means clustering to partition the data space into \(n \times m\) cells. Only \(n + m\) centroids (≈ \(2\sqrt{N}\)) are kept in memory, while inverted lists are stored on disk. The authors introduce centroid reordering for disk I/O coalescing and a query-aware dynamic pruning heuristic. Experiments on four datasets (including billion-scale) show 10–30× memory reduction over state-of-the-art methods and 1.2–2.3× speedup at 90% recall.

## Strengths

- **Novel and elegant memory design.** The two-level hierarchical centroid scheme achieves memory consumption that is linear in \(N\) only through pointers (size ~\(N\)), while centroids grow only as \(O(\sqrt{N} \cdot d)\). In practice this yields drastically lower memory than PQ-based or dense-centroid competitors.
- **Consistent empirical gains.** On all four datasets, DiskHIVF outperforms DiskANN, SPANN, and Starling in both latency and memory footprint at the same recall level. The improvements are large (up to 30× memory savings, 2.3× speed).
- **Well-validated design choices.** Ablation studies confirm that both the merge-read strategy (enabled by centroid reordering) and the query-aware dynamic pruning provide real performance benefits. The paper includes experiments on billion-scale datasets, which are non-trivial.

## Weaknesses

### Fatal
None.

### Major
- **The claimed “\(O(\sqrt{N}\cdot d + N)\)” complexity is not fundamentally different from prior methods.** DiskANN and Starling also have memory linear in \(N\) (via compressed PQ vectors). The advantage is in the constant, not the asymptotic order. The paper overstates the complexity gap—this is still a linear-in-\(N\) method. The constant is much smaller, which is a genuine practical achievement, but the presentation risks misleading readers about the theoretical distinction.
- **Limited discussion of pointer storage.** The \(O(N)\) term comes from the \(n \times m ≈ N\) disk pointers required to locate each cell. For billion-scale data this is ~8 GB (if 8‑byte pointers). The paper acknowledges “only a few gigabytes” but does not analyse how this cost scales with dataset size or whether it could become a bottleneck for extremely large \(d\) or \(N\).

### Minor
- **Naming inconsistency.** The abstract and title use “DiskHIVF”, but Section 1 and later text repeatedly use “DiskHIVE”. This should be unified.
- **Query-aware pruning heuristic may be dataset-dependent.** The quadratic polynomial is fitted on SIFT1M’s 99th percentile curve. Although the ablation on BIGANN shows benefit, no cross-dataset validation of the same fitted coefficients is provided. Generalisation to arbitrary distributions is not demonstrated.
- **Hyperparameter choice for \(n\) and \(m\) is heuristic.** The formula \(n = \sqrt{N}/10 \times 2.5\), \(m = \sqrt{N}/10 / 2.5\) is given without justification or sensitivity analysis. The trade-off between deeper hierarchy and memory/recall is not explored.

### Trivial
- Some equation formatting errors (e.g., missing plus sign in cellsDistance expression) and duplicate figure labels in the PDF. These are parser artifacts or minor typos.

## Nice-to-Haves

- Provide a breakdown of memory consumption (centroids vs. pointers vs. other structures) for each dataset.
- Analyse the sensitivity of recall to the number of k‑means iterations and the fraction of data used for training.
- Compare with SPFresh or other recent hybrid methods that also reduce disk overhead.

## Novel Insights

None beyond the paper’s own contributions.

## Suggestions

- Clarify that the memory saving is due to a small constant factor on the linear \(N\) term, not a change in asymptotic complexity. Rephrase the complexity discussion accordingly.
- Add a plot or table showing how recall varies with different choices of \(n\) and \(m\) for a fixed dataset, to guide practitioners in setting these hyperparameters.
- Test the query-aware pruning polynomial on a dataset different from the one used to fit it (e.g., fit on SIFT1M, test on GIST) to demonstrate robustness.

## Score and Decision

- **Score:** 8  
- **Decision:** Accept  

MY FINAL SCORE: <score>8</score>  
MY FINAL DECISION: <decision>Accept</decision>