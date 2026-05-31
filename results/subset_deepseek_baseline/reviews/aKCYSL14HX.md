## Summary

This paper introduces DiskHIVF, a hybrid memory-disk approximate nearest neighbor search (ANNS) algorithm that uses a two-level hierarchical inverted file structure. By storing only \(n+m\) cluster centroids and \(n \times m\) disk pointers in memory (with \(n,m \approx \sqrt{N}\)), the method achieves a memory complexity of \(O(\sqrt{N} \cdot d + N)\), yielding 10–30× memory reduction over state-of-the-art hybrid methods. Experiments on four datasets (SIFT1M, GIST, BIGANN, DEEP) show DiskHIVF is 1.2–2.3× faster at 90% recall@1 while using substantially less memory.

## Strengths

- **Novel memory-efficient design**: The two-level hierarchical clustering with shared second-level centroids is a clever way to reduce in-memory centroids from \(O(N)\) to \(O(\sqrt{N})\), directly addressing the scalability bottleneck of existing hybrid ANNS methods.
- **Strong empirical results**: On billion-scale datasets (BIGANN, DEEP), DiskHIVF achieves 27× memory savings over DiskANN/Starling and 1.2–1.9× speedup at 90% recall@1, with consistent improvements across all four datasets.
- **Well-motivated optimizations**: The centroid reordering algorithm (to improve disk locality) and query-aware dynamic pruning (to adapt search budget per query) are clearly explained and validated through ablation studies, showing tangible performance gains.
- **Practical impact**: The ability to serve billion-scale ANNS with only ~1.2 GB of memory (vs. 32 GB for baselines) makes the method highly relevant for resource-constrained deployments.

## Weaknesses

### Fatal
None.

### Major
- **Memory complexity claim is slightly overstated**: The paper states \(O(\sqrt{N} \cdot d + N)\) complexity, but the \(N\) term arises from the number of cells (\(n \times m\)), which in practice is set to \(N/100\) (not \(N\) vectors). While the constant is small, the asymptotic complexity is still linear in \(N\). The paper should clarify that the linear term is due to cell pointers, not vector storage, and that the practical savings come from the small constant factor.
- **Missing index build time and disk usage**: The paper reports only search latency and memory overhead. For billion-scale datasets, build time and total disk footprint are critical practical metrics. Without these, it is difficult to assess the full resource cost of the method.

### Minor
- **Dynamic pruning fitting procedure is underspecified**: The quadratic polynomial for budget prediction is fitted to the “99% query coverage curve,” but it is not explained how this curve is obtained (e.g., using a validation set, ground truth, or online estimation). The generalizability of this data-driven approach across different datasets is unclear.
- **Baseline selection could be broader**: The paper compares only to DiskANN, SPANN, and Starling. Other hybrid methods (e.g., FAISS with disk, HNSW with disk) or pure in-memory methods with PQ (e.g., IVFADC) are not discussed, leaving the reader to wonder how DiskHIVF compares to a wider range of approaches.
- **Figure 4 legend contains a typo**: “DiskHIVF w/o Merge-Read” appears twice with different colors, which is confusing.

### Trivial
- The method is sometimes referred to as “DiskHIVE” in the abstract and Section 1, while the rest of the paper uses “DiskHIVF.” This inconsistency should be fixed.

## Nice-to-Haves

- A sensitivity analysis of the number of cells (\(n \times m\)) vs. memory/accuracy trade-off would strengthen the design justification.
- Reporting the time to build the index (including clustering and assignment) for billion-scale datasets would be valuable for practitioners.
- An explanation of how the polynomial coefficients for dynamic pruning are computed in practice (e.g., offline on a sample of queries) would improve reproducibility.

## Novel Insights

None beyond the paper’s own contributions.

## Suggestions

- Clarify the memory complexity: explicitly state that the \(O(N)\) term comes from the number of cells (which is a fraction of \(N\)), and that the dominant savings come from avoiding storage of full vectors or PQ codes in memory.
- Add a table or paragraph reporting index build time and total disk usage for all methods on the billion-scale datasets.
- Provide more detail on the dynamic pruning fitting process, including how the 99% coverage curve is obtained and whether it requires ground truth.

## Score and Decision

**Score**: 8  
**Decision**: Accept

MY FINAL SCORE: <score>8</score>
MY FINAL DECISION: <decision>Accept</decision>