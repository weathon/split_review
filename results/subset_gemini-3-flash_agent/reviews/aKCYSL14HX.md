The paper presents **DiskHIVF**, a hybrid memory-disk indexing scheme designed for billion-scale Approximate Nearest Neighbor Search (ANNS). To address the memory limitations of existing hybrid indices (like DiskANN or SPANN) which scale linearly with the dataset size, DiskHIVF utilizes a hierarchical two-level $k$-means clustering approach with shared second-level centers, achieving a memory space complexity of $O(\sqrt{N} \cdot d + N)$. The method further optimizes query speed and I/O efficiency through a centroid reordering algorithm for spatial locality on disk and a query-aware dynamic pruning strategy.

## Strengths
- **Significant Reduction in Memory Overhead**: The hierarchical clustering architecture achieves a memory space complexity of $O(\sqrt{N} \cdot d + N)$. Empirical results on 1B-scale datasets (BIGANN, DEEP) show $10\text{--}30\times$ less memory usage than competitive baselines (e.g., ~1.2GB for DiskHIVF vs ~32GB for DiskANN).
- **Improved Pareto Efficiency**: The method demonstrates a $1.2\text{--}2.3\times$ speedup over state-of-the-art hybrid indices (DiskANN, SPANN, Starling) when achieving a 90% Recall@1 target across multiple datasets.
- **Robustness to High-Dimensional Data**: By avoiding the fixed disk-page-size constraints of graph-on-disk methods like Starling (which struggles when vertex size exceeds 4KB), DiskHIVF successfully handles clusters of high-dimensional vectors (e.g., the 960d GIST dataset).
- **Effective Disk I/O Optimization**: The Centroid Reordering Algorithm (Alg 2) and "Merge-Read" strategy effectively improve spatial locality. Ablation studies in Table 3 show that this reduces the discrete disk access count by significantly (e.g., ~3.7x reduction at $L=5000$).

## Weaknesses

### Fatal
None.

### Major
- **Sustainability of Linear Memory Scaling** — The paper claims a complexity of $O(\sqrt{N} \cdot d + N)$ and emphasizes the square root term. However, the $O(N)$ term (representing pointers/offsets to lists) remains a linear scaling factor. For $N=10^9$, even 4-8 bytes per vector results in 4-8 GB. While this is a massive saving compared to current SOTA (which stores PQ vectors or large centroid sets), the paper should explicitly discuss the transition where the linear pointer overhead $N$ starts to dominate the $O(\sqrt{N} \cdot d)$ term, as this is the ultimate bottleneck for scaling to the trillion-scale.

### Minor
- **Generalizability of Dynamic Pruning Coefficients** — The dynamic pruning method (Section 3.5) relies on a quadratic fit of the "99% query coverage curve." While it works well for SIFT1M, there is little discussion on how robust these coefficients ($a, b, c$) are across different data distributions (e.g., highly clustered vs. uniform). A more stable analysis across datasets would strengthen the claim of "minimal manual tuning."
- **Lack of Build Time and Disk Footprint Details** — While memory efficiency is well-documented, the paper does not explicitly report the total index build time or the storage overhead on disk compared to baselines. Since SPANN is criticized for $8\times$ data duplication, clarifying if DiskHIVF uses $1\times$ storage would be a significant selling point regarding resource total cost of ownership.

### Trivial
None.

## Nice-to-Haves
- **High-Dimensional Stress Test**: While GIST (960d) is tested, evaluation on modern 1536d+ or 3072d+ embeddings would further highlight the robust handling of high-dimensional vectors compared to graph-based methods.
- **Cache Analysis**: Clarity on whether latencies were measured with a cleared OS page cache or a warm cache would help contextualize the Disk I/O bound results.

## Removed Points
- *Starling's Failure on GIST*: A concern was raised that this comparison might be unfair because Starling could theoretically be configured with larger page sizes. This is removed as the paper correctly highlights a real structural limitation of Starling's default architecture, and DiskHIVF's architectural avoidance of this is a valid contribution.
- *Reproducibility/Hyperparameters*: Minor nitpicks about training time and specific implementation details were removed or addressed in suggestions, as they do not threaten the core empirical claims.

## Novel Insights
DiskHIVF’s primary insight is that hierarchical clustering can be engineered specifically for disk-resident inverted files by sharing second-level centers. This shifts the memory bottleneck from storing a large percentage of centroids (as in SPANN) or compressed vectors (as in DiskANN) to a much smaller set of shared centers and a linear array of list pointers. The integration of a TSP-style centroid reordering algorithm to match spatial proximity to disk layout is a particularly effective application of classic heuristics to modern SSD-based retrieval.

## Suggestions
- Report the total index build time for the 1B-scale datasets to compare with DiskANN's famously long build times.
- Explicitly state the disk footprint (e.g., total GB on disk) for DiskHIVF to confirm there is no heavy data duplication like in SPANN.
- Provide sensitivity analysis for the $\delta$ and quadratic coefficients across the different datasets (BIGANN vs DEEP) to demonstrate the robustness of the dynamic pruning.

## Calibration and Score Explanation
The initial bracket was set between 5.5 and 7.5 based on the strong empirical results for a billion-scale systems problem, but balanced by the fact that the algorithmic components (hierarchical k-means, TSP reordering, dynamic pruning) are individually well-known.

**Round 1 Anchors:** 
- `iQtz3UJGRz` (Avg 4.0): A rejection for a bi-metric framework. DiskHIVF is significantly stronger as it provides a complete, high-performance system for billion-scale search with massive memory gains.
- `ESq3U7z6FD` (Avg 6.0): Learned hierarchical indexing. This is a good baseline; DiskHIVF’s 10-30x reduction in memory for *billion-scale* data is more practically impactful and clearly demonstrated than the novelty in EHI.
- `l0fn10vSyM` (Avg 7.0): A well-received paper on semi-parametric retrieval. DiskHIVF sits near this range due to its high practical utility and strong experimental evidence on 1B-scale public benchmarks.

**Round 2 Anchors:**
- `2zMHHZ569S` (Avg 6.4): Improvements to vector compression/quantization. DiskHIVF is more fundamental to the "system" architecture of memory-disk indices.
- `lgsyLSsDRe` (Avg 7.5): A strong embedding model paper. While different in domain, both show strong empirical gains over SOTA.

DiskHIVF is a solid contribution to the systems side of ANNS. Its memory reductions are significant enough to be considered a major improvement over the standard DiskANN/SPANN approaches used in industry. The complexity analysis is clear, and the ablation studies (especially the merge-read impact) are convincing.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>