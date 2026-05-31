## Summary
This paper introduces LSH-DBSCAN and LSH-HDBSCAN, locality-sensitive hashing based algorithms that provide the first provably subquadratic runtime for approximate density-based clustering in high dimensions without restrictive assumptions on the data. The algorithms achieve a runtime of \(\tilde{O}(dn^{1+1/(2c^2-1)+o(1)})\) for a \(c\)-approximation, and the paper also proves a SETH-based lower bound showing that near-quadratic time is necessary for sufficiently fine approximations, thus establishing a nearly tight trade-off between approximation quality and runtime.

## Strengths
- **First provably subquadratic algorithm without dataset assumptions.** Prior LSH-based work by Okkels et al. (2025) required the number of points at distance \(c\varepsilon\) from any point to be on the order of MinPts; the current paper removes that restrictive assumption, giving a rigorous guarantee for all inputs.
- **Clear theoretical framework.** The sandwiching definition of approximate DBSCAN (Definition 2.3) is well motivated, and the reduction from approximate HDBSCAN to approximate DBSCAN (Algorithm 4) is elegant and clean.
- **Lower bound complementing the algorithmic contribution.** Theorem 3.3 shows that even \((1+\gamma)\)-approximate DBSCAN requires near-quadratic time under SETH, which matches the asymptotic behavior of the algorithm as \(c\to 1\) and establishes that approximation is necessary for subquadratic time.
- **Solid experimental evidence for practical speedup.** On four diverse benchmarks (MNIST, Fashion-MNIST, ALOI, GloVe), LSH-DBSCAN achieves computation speedups of 10×–120× relative to exact DBSCAN with misalignment typically below 0.1, demonstrating the practical viability of the approach.

## Weaknesses
### Fatal
None.

### Major
- **No comparison to any other approximate DBSCAN method.** The experiments only compare LSH-DBSCAN to exact DBSCAN. Without a comparison to the prior LSH-based method of Okkels et al. (2025), to sampling-based methods, or to other approximate baselines, the empirical value of the proposed algorithm over existing alternatives is not demonstrated. The paper claims to fix a flaw in Okkels et al. (2025), but no direct runtime or accuracy comparison is provided.
- **Empirical evaluation deviates from theoretical parameter settings.** The experimental section states that the hash repetition parameter \(K\) is scaled by factors of 0.8 and 0.4 in Algorithms 2 and 3, respectively, to improve speedup. This means the experiments do not actually run the algorithm as analyzed theoretically, so it is unclear whether the theoretical guarantees (or even the empirical speedups) are preserved under these modifications.

### Minor
- **The misalignment metric is not defined in the main text.** The paper defers the precise definition to Appendix B.2, which is not included. The reader cannot fully interpret the misalignment numbers without this definition.
- **The failure probability is set to \(\delta = 0.5\)**, which is far from the “high probability” guarantee of the theory. While the paper acknowledges this is a practical choice, the large \(\delta\) weakens the connection between the experimental results and the theoretical guarantees.
- **Only one set of DBSCAN parameters is tested per dataset.** The results may be sensitive to the choice of \(\varepsilon\) and \(m\); a more thorough parameter sweep would strengthen the empirical conclusions.

### Trivial
None.

## Nice-to-Haves
- A comparison to other approximate DBSCAN implementations (e.g., sampling-based, LSH-based from prior work) would greatly strengthen the experimental section.
- Visualizing misalignment as a function of \(c\) on more datasets that have well-known ground-truth clusters (e.g., synthetic datasets with controlled density variations) would help illustrate the approximation behavior.

## Novel Insights
The key insight is that locality-sensitive hashing can be used to simultaneously certify core points and connect clusters while avoiding the quadratic bottleneck, *without* assuming low density around each point. The lower bound further reveals a fundamental barrier: even coarse approximations require near-quadratic time when the approximation factor is very close to 1, which justifies why the algorithm’s exponent approaches 2 as \(c\to 1\). None beyond the paper’s own contributions.

## Suggestions
1. Include a direct runtime comparison (both wall-clock time and computation counts) with the prior LSH-DBSCAN of Okkels et al. (2025) or another approximate method to contextualize the improvement.
2. Run experiments with the theoretically prescribed parameter \(K\) (or a fixed scaling factor) to verify that the theoretical guarantees are still empirically meaningful, and report the trade-off between accuracy and runtime when varying \(K\).
3. Provide the definition of misalignment in the main text so the reader can evaluate the results without consulting an appendix.
4. Test the algorithm on additional high-dimensional datasets (e.g., with larger \(n\)) to demonstrate scalability beyond 60k points.

## Score and Decision
The paper makes a clear theoretical contribution: it provides the first provably subquadratic algorithm for approximate DBSCAN on arbitrary high-dimensional data, together with a matching lower bound. The algorithms are well described and the experimental results, while lacking comparisons to other approximate methods, show that the approach yields meaningful speedups in practice. The missing proofs (by instruction not a weakness) and the limited experiments are the main factors preventing a higher score. The work is solid and likely to influence future research on fast density-based clustering.

MY FINAL SCORE: 8
MY FINAL DECISION: Accept