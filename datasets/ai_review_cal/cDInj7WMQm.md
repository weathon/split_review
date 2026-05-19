- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 3, 6
Here is the final consolidated review:

## Summary

This paper proposes Universal Graph Coarsening (UGC), a framework that uses locality-sensitive hashing (LSH) on an augmented node representation (features + adjacency row weighted by heterophily parameter α) to assign nodes to supernodes. The key claims are: (1) UGC is the first graph coarsening method equally effective on homophilic and heterophilic datasets, (2) it achieves O(N) linear time complexity, and (3) it preserves spectral properties while enabling fast downstream GCN training. Empirical results show large runtime advantages on massive graphs (Reddit, Yelp) and substantially higher GCN accuracy on heterophilic benchmarks compared to purely structural coarsening baselines.

## Strengths

- **First coarsening method validated on heterophilic datasets with large accuracy gains**: Table 4 shows UGC (with augmented features) achieves GCN accuracies far exceeding all prior coarsening methods on heterophilic benchmarks (e.g., Squirrel 0.626, Chameleon 0.708, Texas 0.747 vs. prior best ≤0.4). This is a genuine contribution — no existing coarsening method used node features, so they were inherently limited on heterophilic graphs where structure and labels are anti-correlated.

- **Empirically fast on graphs where all baselines fail**: Table 2 shows UGC coarsens Reddit (232k nodes) in 51 s and Yelp (716k nodes) in 198 s, while every competing baseline runs out of memory (OOM). This is the strongest evidence for the method's practical scalability.

- **Principled integration of node features and structure via α-weighted augmentation**: The augmented representation F_i = (1-α)X_i ⊕ α·A_i is simple but effective. The ablation UGC(aug) vs. UGC(feat) in Table 4 demonstrates that combining structure and features provides significant benefit over features alone, especially on heterophilic datasets (e.g., Squirrel 0.626 vs. 0.363).

- **Comprehensive evaluation across metrics and baselines**: The paper compares against 5 structural coarsening methods (Variation edge/neighborhood, Algebraic Distance, Affinity, Heavy Edge, Kron) on 10 datasets using runtime, REE, HE, GCN accuracy, and ε-similarity. This is thorough relative to the literature.

## Weaknesses

### Major

- **The O(N) linear-time complexity claim is unsubstantiated**: The paper repeatedly claims "linear time complexity with respect to the number of nodes" (abstract, Section 1, Section 6) but never provides a formal complexity analysis. The augmented feature vector F_i has dimension d+N (appending the full adjacency row A_i ∈ ℝ^N). Computing LSH projections P·F_i with P ∈ ℝ^{L×(d+N)} would naively cost O(LN(d+N)) = O(N²) for large N. The paper acknowledges this only in passing ("While larger graphs may result in long vectors, efficient implementations and sparse tensor methods may alleviate this hurdle") but does not specify any sparse projection structure, analyze the actual complexity, or provide controlled scaling experiments on synthetic graphs. Since O(N) is a headline contribution, this gap undermines a central claim. The empirical runtime numbers (Table 2) are practically impressive, but they do not substitute for a rigorous complexity derivation — especially because the augmented feature dimension grows with N, which is the very factor that makes standard structural methods OOM.

- **Construction of the coarsened graph from the mapping C is never specified, breaking reproducibility**: The paper states it obtains "the coarsened graph adjacency matrix and coarsened features" (Section 3) but never defines the formulas for Ã and X̃ from the loading matrix C. Section 4 mentions L_c = C^T L C for the coarsened Laplacian, but this alone does not specify how the adjacency matrix Ã is recovered (e.g., thresholding, normalization). For the GCN experiments (which use original features X, not augmented F), the coarsened feature matrix X̃ fed to the GCN is never defined — averaging original features per supernode? Weighted by degree? The description "F_c(i) = 1/|π⁻¹(ṽ_i)| Σ F_u" (Section 4) applies only to augmented features F, not to X. Without these specifications, the experimental results are not independently reproducible, and the spectral quality metrics (REE, HE) cannot be verified.

### Minor

- **No statistical variance reported for any metric**: All tables (runtime, REE, accuracy) report single values. Since LSH involves random projections, coarsening is inherently non-deterministic. At minimum, mean and standard deviation over multiple runs should be reported.

- **Missing eigenvalue plots for heterophilic datasets**: Figure 4 shows top-100 eigenvalue preservation for three homophilic datasets (Cora, Citeseer, PubMed) but none for the heterophilic datasets where the paper claims its biggest advantages. Without these, the reader cannot visually assess whether spectral preservation on heterophilic graphs is genuine or an artifact.

- **Dangling theoretical thread (Eq. 7 minimization) never evaluated**: Section 4 introduces an optimization to bound ε-similarity (Eq. 7), but the experiments never report whether this optimization was used, how it affects the results, or what the bounded ε values are beyond the trivial ≤1 guarantee shown in Figure 6c (which is not tight — any value between 0 and 1 satisfies it).

- **The ε ≤ 1 guarantee is not useful**: Showing ε ≤ 1 is trivial; a meaningful bound would compare ε values against baselines and show that UGC actually achieves low ε (e.g., ε < 0.2), not just ≤1.

- **No hyperparameter sensitivity analysis**: The number of hash functions L and the bin width r control runtime and coarsening quality, but the paper fixes them heuristically without showing how performance degrades with suboptimal choices. Similarly, the α parameter balancing features vs. adjacency is never ablated.

- **Missing a simple feature-only baseline outside the LSH framework**: The paper includes UGC(feat) as a control, which is useful. However, the claim that combining structure and features is beneficial would be strengthened by comparison against a naive feature-clustering baseline (e.g., k-means on X to form supernodes, then aggregating adjacency). UGC(feat) shares the LSH mechanism; a non-LSH feature baseline would isolate the benefit of the augmentation specifically.

### Trivial

- **Notation inconsistency**: The LSH definition in Section 2.3 uses w for bin width, but Section 3.2 uses r for the same concept.
- **Equation 1 constraint ambiguity**: The constraint ⟨C_l, C_l⟩ = d_i mixes column index l with node index i, making it unclear which degree is intended.

## Nice-to-Haves

- A synthetic scaling experiment (varying N from 10³ to 10⁶) with wall-clock time vs. N on a log-log plot would substantiate the O(N) claim.
- An ablation of the α hyperparameter (e.g., varying α from 0 to 1) showing its effect on REE, accuracy, and coarsening ratio for both homophilic and heterophilic datasets.
- An explicit statement of the formulas for Ã and X̃ in terms of C (e.g., Ã = sign(C^T A C) or similar with appropriate normalization).

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"Figure 11 reference"** — This is a parser artifact from an appendix that was stripped. Per instructions, missing appendix content is not a valid weakness.
2. **Claim that Loukas (2019) falsifies "never applied on heterophilic graphs"** — The paper's statement refers to graph coarsening methods being evaluated/designed for heterophily, not whether a structural method could technically be applied. This is a reasonable scope claim, not a factual error.
3. **Claim that the paper says "UGC is not even able to run"** — The paper text says "for massive datasets where all methods are not even able to run, UGC is giving a coarsened graph" (all methods = baselines). The critic misread this.
4. **Specific REE numbers for Texas (25.6, 2.11, 0.26)** — These numbers come from a table image that is not machine-readable from the extracted text, and cannot be independently verified. The general concern about missing heterophilic eigenvalue plots (retained above) is the valid residue.
5. **Ambiguity of "maxOccurred" / hash computation** — The paper explains "its most frequent hash index generated across all hash functions," which is sufficiently clear for the intended readership. The formula break with w vs. r is the only real inconsistency (noted as Trivial).

## Novel Insights

The most interesting observation from this review is the tension between the two critiques. The reviewer correctly identifies that the augmented feature dimension (d+N) naively makes a per-node LSH projection O(N) — which would be O(N²) total — seemingly contradicting the O(N) claim. Yet the empirical runtime on large graphs (51s on 232k-node Reddit, 198s on 716k-node Yelp) is genuinely fast. This gap suggests one of two things: either (a) the implementation exploits sparsity in the adjacency rows and structured projections in a non-obvious way that achieves near-linear time in practice (which the paper should document), or (b) there is a temporal scaling behavior that deviates from O(N) but with small enough constants to run on these datasets. The paper's failure to clarify this is a meaningful oversight, but it does not negate the empirical speed. Similarly, the heterophilic accuracy results are large enough that even if the method is O(N log N) or O(N·deg_avg) rather than strict O(N), the practical contribution remains significant.

## Suggestions

1. **Provide the missing formulas**. Explicitly state: (a) how Ã is obtained from C (e.g., thresholded/sign(C^T A C), or directly from L_c = D_c - Ã), and (b) how X̃ for the GCN is computed from the original features X (e.g., row-wise averaging per supernode). This single change resolves the most serious reproducibility concern.

2. **Add a formal complexity analysis** that accounts for the augmented feature dimension. If sparse projections or implicit computation allows O(N · (d + deg_avg)) time, state this explicitly. If the claim is really O(N · poly(d)) for fixed d but not strict O(N), adjust the claims accordingly.

3. **Add statistical reporting** — at least mean and std over 5 runs for all tables.

4. **Include eigenvalue plots for heterophilic datasets** (Texas, Chameleon, Squirrel) analogous to Figure 4.

5. **Ablate the α parameter** across a range (0, 0.25, 0.5, 0.75, 1) on at least one homophilic and one heterophilic dataset, reporting REE and GCN accuracy.
