## Summary
The paper presents LSH-DBSCAN and LSH-HDBSCAN, two algorithms for approximate density-based clustering in high-dimensional spaces. By leveraging Locality-Sensitive Hashing (LSH), the authors achieve the first provably subquadratic runtime for approximate DBSCAN on arbitrary high-dimensional datasets without requiring restrictive assumptions on data distribution. The work also provides a SETH-based lower bound proving that subquadratic runtimes are impossible for exact DBSCAN in high dimensions, justifying the approximation approach.

## Strengths
- **Theoretical Rigor:** The paper provides the first subquadratic runtime guarantee for approximate DBSCAN in high dimensions ($\tilde{O}(dn^{1+\rho})$) that does not rely on data-dependent assumptions (like the number of points in a $c\varepsilon$ neighborhood).
- **Lower Bounds:** The reduction from the bichromatic closest pair problem to DBSCAN provides a strong theoretical justification for why approximation is necessary, showing that an exact $O(n^{2-\alpha})$ algorithm would violate SETH.
- **Algorithmic Extension:** The extension to HDBSCAN via a logarithmic number of DBSCAN calls and clustering intersections is a non-trivial and useful contribution to the hierarchical clustering literature.
- **Empirical Validation:** The experiments on standard high-dimensional benchmarks (MNIST, ALOI, GloVe) demonstrate significant practical speedups (up to 100x) with low misalignment, showing the method is not just of theoretical interest.

## Weaknesses
### Fatal
None.

### Major
None.

### Minor
- **Parameter Sensitivity:** While the paper provides theoretical values for $K$ and $T$, the experiments note that scaling these parameters (e.g., by 0.8 or 0.4) was necessary for optimal performance. A more detailed discussion on how a user should tune these parameters in practice without ground truth would be beneficial.
- **Memory Complexity:** The use of $T$ hash tables, where $T$ scales with $n^\rho$, can lead to significant memory overhead. While the paper focuses on time complexity, the space complexity is a practical bottleneck for LSH-based methods that is not explicitly discussed.

### Trivial
- The definition of $c$-approximation in Section 2.1 is slightly non-standard (sandwiching between $\varepsilon/c$ and $\varepsilon$), though the authors acknowledge this and explain the change of variables.

## Nice-to-Haves
- A comparison against other approximate nearest neighbor search (ANNS) structures beyond LSH, such as HNSW or IVF, which are often faster in practice even if they lack the same theoretical guarantees.

## Novel Insights
The most significant insight is the formalization of the "sandwiching" approximation for HDBSCAN and the proof that it can be solved efficiently by intersecting a sequence of approximate DBSCAN clusterings. Additionally, the SETH-based lower bound effectively closes the door on exact subquadratic high-dimensional DBSCAN, shifting the field's focus definitively toward approximation.

## Suggestions
- Include a brief discussion or a table in the appendix regarding the memory requirements of the $T$ hash tables compared to the $O(n)$ space of standard DBSCAN.
- Clarify the impact of the $\gamma$ parameter in LSH-HDBSCAN on the final hierarchy's granularity versus the computational cost.

## Score and Decision
The paper is a strong contribution that fills a notable gap in the literature of density-based clustering. It balances high-quality theoretical bounds with practical empirical results.

MY FINAL SCORE: 8.5
MY FINAL DECISION: Accept