## Summary
The paper presents DiskHIVF, a hybrid memory-disk indexing system for billion-scale Approximate Nearest Neighbor Search (ANNS). The core contribution is a hierarchical inverted file structure that utilizes a two-level k-means clustering approach to achieve a memory complexity of $O(\sqrt{N} \cdot d + N)$, where $N$ is the number of vectors and $d$ is the dimensionality. To optimize performance on SSDs, the authors introduce a centroid reordering algorithm to improve data locality and a query-aware dynamic pruning method to adjust the search budget per query.

## Strengths
- **Superior Memory Efficiency**: The method achieves a significant reduction in memory overhead (10–30$\times$ compared to state-of-the-art methods like DiskANN and Starling). This is particularly valuable for large-scale deployments where RAM is the primary cost bottleneck.
- **Robustness to High Dimensionality**: Unlike graph-based methods like Starling, which can fail when a vertex and its neighbors exceed a disk page size (4096 bytes), DiskHIVF’s inverted list structure is more resilient to high-dimensional vectors (e.g., GIST-960).
- **Strong Empirical Results**: The paper demonstrates a 1.2–2.3$\times$ speedup over existing hybrid solutions at 90% recall across multiple standard benchmarks (SIFT1M, GIST, BIGANN, DEEP).
- **Practical Optimizations**: The inclusion of "Merge-Read" strategies via centroid reordering and dynamic pruning shows a clear understanding of the hardware constraints (SSD I/O patterns) inherent in hybrid indexing.

## Weaknesses
### Fatal
None.

### Major
- **Clarity on Memory Complexity**: The authors claim a memory complexity of $O(\sqrt{N} \cdot d + N)$. While the $O(\sqrt{N} \cdot d)$ term accounts for the cluster centers, the $O(N)$ term (likely representing the pointers to inverted lists) is not fully discussed in terms of its constant factor. At the billion scale, $N$ pointers (e.g., 8-byte offsets) still require ~8GB of RAM. While this is much smaller than storing vectors, the paper would benefit from a more explicit breakdown of what constitutes the $O(N)$ memory component.
- **Comparison with IMI/GNO-IMI**: The method is conceptually very similar to the Inverted Multi-Index (IMI) and GNO-IMI. While the authors cite these, the distinction between DiskHIVF and a disk-resident GNO-IMI implementation is not sufficiently highlighted. The primary difference seems to be the specific disk layout and pruning, but a more direct comparison of the indexing structure's novelty would strengthen the paper.

### Minor
- **Training Set Sensitivity**: The authors use 10% of the dataset for training. While they mention this is sufficient in the appendix (referenced but not provided in the main text), the impact of training set size on the quality of the hierarchical clusters for non-uniform distributions is a known challenge for IVF methods.
- **Hyperparameter Sensitivity**: The choice of $n$ and $m$ (first and second-level centers) is set using a heuristic ($\sqrt{N}/10 \times 2.5$). It is unclear how sensitive the performance is to these ratios across different data distributions.

### Trivial
- The paper uses "DiskHIVE" and "DiskHIVF" interchangeably in some sections (e.g., Section 1 and Section 3.1).

## Nice-to-Haves
- A comparison of build times. IVF-based methods often have faster build times than graph-based methods (DiskANN), which would be an additional selling point.
- Discussion on the impact of SSD types (NVMe vs. SATA) on the "Merge-Read" optimization.

## Novel Insights
The most significant insight is the application of a two-level hierarchical clustering specifically designed to minimize memory-resident centroids while maintaining a disk layout that favors sequential I/O. While hierarchical IVF is not new, the specific combination of centroid reordering to ensure spatial locality on disk and the quadratic polynomial fitting for dynamic query pruning provides a robust engineering solution to the "high-dimensional disk page overflow" problem that plagues current state-of-the-art graph-based disk indices.

## Suggestions
- Provide a more detailed breakdown of the memory usage in Table 2. Specifically, show how much memory is consumed by the centroids ($O(\sqrt{N} \cdot d)$) versus the list pointers ($O(N)$).
- Clarify the distinction between the proposed hierarchical clustering and standard GNO-IMI to better define the algorithmic novelty.

## Score and Decision
The paper presents a solid, well-motivated improvement for large-scale ANNS. The memory savings are substantial and the performance gains are consistent across diverse datasets. The method addresses a practical limitation of current graph-based disk indices regarding high-dimensional data.

MY FINAL SCORE: 8.0
MY FINAL DECISION: Accept