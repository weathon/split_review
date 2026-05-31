## Summary

This paper introduces LSH-DBSCAN and LSH-HDBSCAN, the first provably subquadratic algorithms for approximate density-based clustering in arbitrary high-dimensional spaces without restrictive data assumptions. The algorithms use locality-sensitive hashing to achieve runtime \(\tilde{O}(dn^{1+1/(2c^2-1)+o(1)})\) for \(c\)-approximate DBSCAN and HDBSCAN. The paper also proves a quadratic lower bound under SETH, showing that subquadratic time inherently requires approximation. Experiments on four benchmarks demonstrate significant computational speedups with moderate misalignment.

## Strengths

- **First provably subquadratic algorithm for approximate DBSCAN in high dimensions without restrictive assumptions.** Prior work (Okkels et al., 2025) required a strong assumption about cluster density; this paper removes that condition entirely while maintaining rigorous guarantees.
- **Clean extension to HDBSCAN** via a simple reduction that makes logarithmically many calls to LSH-DBSCAN and uses clustering intersection to maintain the hierarchy.
- **Lower bound (Theorem 3.3)** establishes that near-quadratic time is necessary for sufficiently accurate approximation, assuming SETH. This justifies the polynomial exponent in the upper bound and shows that approximation is essential for subquadratic speed.
- **Theoretical analysis is rigorous and well-structured.** The algorithms are clearly presented, and the proof sketches (deferred to appendix) follow from LSH guarantees.
- **Empirical validation on four diverse real-world datasets** (MNIST, Fashion-MNIST, ALOI, GloVe) demonstrates speedups up to two orders of magnitude, with misalignment typically below 0.1 for moderate approximation factors.

## Weaknesses

### Fatal
None.

### Major
1. **Experimental implementation deviates from the theoretically guaranteed algorithm.** The authors report scaling the hash repetition parameter \(K\) by factors of 0.8 and 0.4 for Algorithms 2 and 3, respectively, to improve computational speedups. This modification breaks the theoretical guarantees (Theorem 3.1) that rely on specific \(K\) values to control failure probability. Without analysis of this trade-off, the empirical results do not directly validate the provable subquadratic claims; they validate an ad-hoc variant.

2. **Empirical evaluation uses non-standard metrics that are not directly comparable to prior work.** Computational efficiency is measured by the number of heavy operations (hash + distance computations) rather than wall-clock time. While hardware independence is a fair motivation, raw runtime results are relegated to the appendix, and the main table (Table 2) does not include wall-clock speedups. The misalignment metric is defined in the appendix but not widely used; its interpretation (e.g., whether 0.1 misalignment is “small”) is not calibrated against standard clustering metrics (e.g., adjusted Rand index).

3. **The practical trade-off between speed and accuracy is not fully characterized.** For Fashion-MNIST, misalignment exceeds 0.11 for \(c \geq 4\); for ALOI, misalignment jumps to 0.53 at \(c=7\). The paper claims “small error” broadly, but the deterioration for larger approximation factors is not discussed critically. The choice of approximation factor in practice remains unclear from the experiments.

### Minor
- The lower bound (Theorem 3.3) is a relatively direct application of known reductions from bichromatic closest pair to DBSCAN. While it is a valuable addition, the core hardness result is not novel and could be given less emphasis.

### Trivial
None.

## Nice-to-Haves
- A comparison with the prior method of Okkels et al. (2025) on the same benchmarks (if their code were available) would directly demonstrate the improvement from removing their assumption.
- An ablation study showing the effect of the \(K\) scaling factors on both speedup and misalignment would clarify the gap between theory and practice.

## Novel Insights
The key insight is that LSH-based core point identification and BFS-based cluster formation can both be made robust without the dense-cluster assumption of Okkels et al. (2025). The authors achieve this by carefully amplifying the number of hash tables so that, with high probability, every pair of points within distance \(\varepsilon/c\) collides in at least one table, while far pairs rarely cause false collisions. The hierarchical extension to HDBSCAN via clustering intersection is technically simple but effective: it avoids recomputing a full MST and instead leverages the logarithmic-scale DBSCAN calls.

## Suggestions
1. **Reconcile theory and experiments:** Either run experiments with the theoretically prescribed \(K\) values and report the resulting (likely lower) speedups, or provide a rigorous analysis that justifies the heuristic scaling and shows it still yields a guaranteed approximation (possibly with higher failure probability).
2. **Include wall-clock runtime in the main table** alongside the custom metric, and consider reporting standard clustering quality metrics (e.g., ARI, NMI) in addition to misalignment.
3. **Discuss the choice of approximation factor** more practically: for a given application, how should one select \(c\) to balance speed and fidelity? The experiments show that even \(c=2\) yields small speedups on some datasets (ALOI, GloVe); a guidance statement would strengthen the paper.

## Score and Decision

MY FINAL SCORE: 6.5score</score>
MY FINAL DECISION: Acceptdecision</decision>