## Summary

This paper proposes \frameworkname{}, a graph transformer framework for node classification on single large graphs (millions to hundreds of millions of nodes). The core technical contribution is a tokenization strategy (Algorithms 1–2) that precomputes 1-hop and 2-hop aggregated context features ($\mathbf{C}^0=\tilde{\mathbf{A}}\mathbf{H}$, $\mathbf{C}^1=\tilde{\mathbf{A}}^2\mathbf{H}$) and attaches them to each sampled neighbor's token, enabling a broad receptive field through only 2-hop operations. This local module is combined with a codebook-based global module (adapted from GOAT) that provides coarse global context. The framework is validated on three large-scale benchmarks: ogbn-products, snap-patents, and ogbn-papers100M (111M nodes).

## Strengths

1. **Clever tokenization expanding receptive field via precomputed context features**: The idea of attaching aggregated 1-hop and 2-hop context features to each sampled neighbor token (Algorithm \textsc{InputTokens}, lines 161–165) is a genuinely practical solution to the neighbor explosion problem. It allows the central node to receive information from up to 4 hops away without ever sampling beyond 2 hops, directly addressing the exponential blowup that makes 3+ hop retrieval intractable on graphs with hundreds of millions of nodes.

2. **Dramatic improvement on the non-homophilic snap-patents dataset**: On snap-patents (2.9M nodes, non-homophilic), \frameworkname{}-full achieves **70.21±0.12** — a ~10 point absolute gain over the best baseline NAGphormer-constraint (60.11±0.05). This is the strongest empirical evidence for the design principle that integrating local and global information is essential. Purely local methods (GOAT-local-constraint, GraphSAGE, GAT) all score below 50% on this dataset, demonstrating that local-only approaches fundamentally fail on non-homophilic data while \frameworkname{}'s joint local+global design succeeds.

3. **Concrete scaling to ogbn-papers100M with improved performance**: The paper validates scalability on the 111M-node ogbn-papers100M dataset within a 48-hour budget, where \frameworkname{}-full (64.73±0.05) outperforms GOAT-full-constraint (61.12±0.10) by 5.9%. This is the only model in the paper demonstrated at this scale, supporting the claim that the framework can handle graphs orders of magnitude larger than what prior graph transformers typically operate on.

4. **Empirical quantification of the D2 constraint's importance**: The paper reports that constraining GOAT-full from 3-hop neighbor sampling to 2-hop (the D2 constraint) reduces per-epoch time from 497s to 205s on ogbn-products (line 318). This concrete measurement validates the practical necessity of the 2-hop constraint for scalability and provides context for why \frameworkname{}'s 2-hop-only design is motivated.

5. **Clean ablation isolating the global module's contribution**: Comparing \frameworkname{}-local vs \frameworkname{}-full shows consistent gains from adding the global module (~1% on ogbn-products, ~2% on snap-patents). This cleanly attributes performance to the specific architectural addition rather than confounding factors.

6. **Conversion of graph learning to standard NN training**: The offline sampling stage (Algorithms 1–2) decouples graph structure from the training loop. As the paper argues (lines 178–180), this means the adjacency matrix does not need to reside on any single machine during training, enabling distributed training — a genuine architectural differentiator from MPNNs and sparse GTs that require adjacency access in every minibatch.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Only one baseline comparison on ogbn-papers100M**: On the largest dataset (111M nodes), only GOAT-full-constraint is compared (Table 3). The authors acknowledge this is "due to computational constraints" (line 295), but with a single comparison point, the 5.9% improvement, while suggestive, cannot be interpreted as a general result. Adding even computationally cheaper baselines (SIGN with precomputed features, SGC, or a simple MLP) would substantially strengthen the scaling claim for this dataset.

2. **Precomputation costs not analyzed for large graphs**: The paper states that the offline step "does not affect the computational complexity" (line 183), which is fine as a per-batch analysis. However, computing $\tilde{\mathbf{A}}^2\mathbf{H}$ for a graph with 111M nodes and 1.6B edges and running Algorithm \textsc{LocalNodes} for all 111M nodes are substantial operations. For a paper whose central claim is scalability, reporting wall-clock time, memory footprint, and infrastructure used for these offline steps would be important. The current treatment is a significant omission.

3. **No runtime or resource usage reported for ogbn-papers100M**: The paper reports per-epoch runtime for the smaller datasets (Figure 4) but provides no runtime information for the largest dataset where scalability matters most. This limits the ability to assess the practical efficiency of the framework at scale.

4. **No per-component runtime breakdown**: The paper claims up to 3× speedup of \frameworkname{}-full over GOAT-full-constraint on ogbn-products, but provides no component-level analysis to explain the source of this speedup. Both models share a similar two-module architecture (local transformer + codebook-based global attention), so understanding where the efficiency gain comes from would strengthen the contribution.

5. **Unconstrained baseline accuracy numbers not provided**: The paper compares all methods under the 2-hop (D2) constraint, which is fair since \frameworkname{} also operates under D2. However, the paper never reports the unconstrained accuracy of the baselines, so the reader cannot assess how much performance is sacrificed by imposing the 2-hop constraint on existing methods. This contextual information would help distinguish between "our method is genuinely better at working within the 2-hop budget" and "existing methods lose very little from the constraint." (The paper does provide one unconstrained *runtime* comparison for GOAT — 497s vs 205s — but not accuracy.)

6. **"4-hop receptive field" claim could be more precisely scoped**: The paper states the tokenization "increases the receptive field of a node up to 4 hops" (line 175). The mechanism uses $\mathbf{C}^0$ and $\mathbf{C}^1$, which are *aggregated* representations (summed over neighborhoods). The central node receives aggregated statistics from 3–4 hop neighborhoods, not individually distinguishable node-level representations at those distances. While "receptive field" in the GNN literature typically refers to which nodes can influence a representation (regardless of aggregation granularity), the paper would benefit from explicitly distinguishing aggregated statistics from true node-level receptive field expansion.

### Trivial
None.

## Nice-to-Haves
- Report unconstrained accuracy of baselines alongside constrained results to contextualize the cost of the D2 constraint.
- Provide a per-component runtime breakdown (data loading, tokenization, local attention, global attention, FFN) to explain the source of the 3× speedup.
- Add at least 1–2 computationally cheap baselines (e.g., SIGN, SGC) on ogbn-papers100M.

## Removed Points
These points were flagged for removal; treat them with caution:
- **Abstract misleading about performance claims (Harsh Critic #1)**: The abstract says "3× speedup and 16.8% performance gain on ogbn-products and snap-patents compared to their nearest baselines respectively." The word "respectively" unambiguously pairs 3× with ogbn-products (runtime speedup) and 16.8% with snap-patents (accuracy gain). This is standard English grammar; the criticism is based on a misreading.
- **Global module novelty concern (Harsh Critic)**: The paper explicitly states the global module is "adapted from [kong2023goat]" (line 32) and further acknowledges this in related work (line 50). There is no attempt to claim this as novel. The paper's novelty is correctly scoped to the local tokenization strategy.
- **K sensitivity analysis lacking baseline comparisons (Harsh Critic)**: The K analysis is a hyperparameter sensitivity study for \frameworkname{}'s own design, not a comparative experiment. Requesting baseline comparisons at varying K is beyond the stated scope.
- **Statistical significance concern for papers100M (Harsh Critic)**: With 4 runs and standard deviations of 0.05–0.10, the results exhibit high stability. This is not a meaningful concern.
- **Strength: "This paper addresses an important problem" (from Strength Finder)**: Generic and applicable to any paper in the area. Not a concrete strength specific to this paper.

## Novel Insights
None beyond the paper's own contributions. The reviews identify a gap between the confidence of the paper's presentation and the thinness of evidence on the largest dataset, but this gap is known methodology rather than a novel observation.

## Suggestions
1. Report the unconstrained accuracy of all baselines alongside the constrained results in a supplementary table. This single addition would allow readers to assess the cost of the D2 constraint and contextualize \frameworkname{}'s performance.
2. Provide a brief analysis of the offline precomputation costs (wall-clock time, memory, hardware) for all three datasets, especially ogbn-papers100M.
3. Add runtime and resource measurements for the ogbn-papers100M experiments.
4. Qualify the "4-hop receptive field" claim with a brief note that the 3–4 hop information arrives in aggregated (summed) form, distinguishing it from the node-level representations available at hops 1–2.
5. Add at least one computationally cheap baseline (e.g., SIGN or SGC) on ogbn-papers100M to contextualize the single comparison point.

MY FINAL SCORE: <score>7</score>
MY FINAL DECISION: <decision>Accept</decision>