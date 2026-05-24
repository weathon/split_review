Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

## Summary

This paper presents NID, a framework that learns highly compact (6–15 int4 values), discrete node representations ("node IDs") via multi-layer residual vector quantization (RVQ) of GNN embeddings. The node IDs can replace continuous GNN embeddings in downstream tasks (node/graph classification, link prediction, clustering), enabling orders-of-magnitude inference speedups (up to ~17,000× on ogbn-products) while maintaining competitive accuracy. The framework integrates with both supervised and self-supervised GNN paradigms across 34 datasets.

## Strengths

1. **Massive inference speedup with strong accuracy retention on large graphs.** Table 6/9: NID_SAGE achieves 81.83% on ogbn-products (vs. SAGE 83.27%) with 0.7ms inference vs. 11.9s — a ~17,000× speedup. Storage drops from 1.9 GB to 17.5 MB. This directly delivers the paper's central promise of efficient large-scale graph learning.

2. **High codebook usage that empirically solves VQ collapse.** Table 11 shows NID achieves 84.7% codebook usage on Cora vs. VQGraph's 1.3%. This is a concrete, quantitative demonstration that NID's multi-layer, multi-level RVQ design avoids a well-known failure mode of VQ-VAE-style models.

3. **Broad integration and strong empirical coverage.** NID is demonstrated with GCN, GAT, SAGE, GIN, GraphMAE, GraphCL, AutoGCL, and DGCluster across 34 datasets spanning node classification, graph classification, link prediction, and clustering — establishing generality well beyond typical GNN-to-MLP distillation methods.

4. **Interpretable structure via codeword-label correlation and subgraph retrieval.** Figure 6 shows that specific codewords correlate strongly with ground-truth labels (e.g., c₁₁=10 → label "2" in PubMed). Table 10 shows that nodes with similar Hamming-distance node IDs have structurally similar 1-hop subgraphs (lower GED than VQGraph and random), providing evidence that the discrete codes capture meaningful graph structure.

## Weaknesses

### Fatal
None.

### Major

1. **Clustering evaluation lacks methodological transparency (Table 2).** The paper applies k-means to node IDs (tuples of int4 indices) but never states what distance metric is used. Standard k-means with Euclidean distance on ordinal discrete indices is questionable. The subgraph retrieval section (line 588) explicitly uses Hamming distance — implying the authors know discrete indices need a non-Euclidean distance — but this is never extended to the clustering pipeline. The large gains (Cora F1: 54.5→73.9) could be partly an artifact of an inappropriate metric on categorical indices. This must be clarified and justified.

2. **Missing ablation: clustering on continuous GNN embeddings.** The paper attributes large clustering improvements (Table 2) to node IDs "uncovering hidden patterns" (line 30), but provides no control experiment where the same k-means clustering is run on the *original continuous GCN embeddings* from DGCluster. Without this, it is unclear whether the improvement comes from the discrete representation or from some other aspect of the NID training pipeline. Given that the improvement is framed as a key finding, this control is necessary.

### Minor

3. **No error bars reported for clustering results (Table 2).** All other result tables (1, 3, 4, 6, link prediction) report standard deviations, but Table 2 reports only point estimates. Clustering results can have high variance, and the ogbn-arxiv results (NMI 32.4 vs. 31.2, F1 35.6 vs. 32.4) appear statistically marginal. This omission weakens the evidentiary strength of the strongest advertised outcome.

4. **Theoretical analysis is conditional and adds limited insight.** Theorem 1 shows: *if* the VQ objective separates node IDs by class, *then* a linear head can achieve zero error. This is nearly tautological given the assumption. The paper does not prove that the VQ objective (minimizing reconstruction error of GNN embeddings, not class separation) actually achieves the needed separation. The assumptions (orthonormal patterns, uniform weight alignment) are strong and borrowed from binary classification settings. The theorem does not constitute a substantive theoretical justification; it is better characterized as a consistency check.

5. **"Interpretability" claim is overstated.** The evidence for interpretability is limited to codeword-label distribution plots (Figure 6, Appendix Figures 5/6), which show that some codewords correlate with class labels. This demonstrates label-correlation but not "interpretability" in the operational sense — there is no analysis of what individual code vectors semantically represent, no human-study, no demonstration that a practitioner can understand a node's role from its ID. The claim should be softened to "label-correlated" or "structured" representations, or supported with stronger analysis.

6. **Inference speed comparison omits the one-time cost of node ID generation.** Tables 6/9 compare inference-only time (MLP on precomputed IDs vs. full message-passing GNN), but the total cost of generating node IDs (GNN training + codebook learning) is not reported. For applications requiring frequent retraining, this overhead may be significant. The paper should explicitly separate one-time training cost from per-inference cost.

### Trivial

7. **Clustering time reduction is modest despite large dimensionality reduction.** Table 2 shows NID_DGCluster clustering times are only 10–35% faster than DGCluster (e.g., Cora: 78.3ms vs. 93.6ms), despite reducing 128/256-dim continuous embeddings to 6–15 int4 values. An explanation would be helpful.

## Nice-to-Haves

- A comparison against VQ-VAE applied to the same GNN embeddings (to isolate the effect of the reconstruction-free loss) would strengthen the methodological claims.
- Reporting node ID collision rates on large graphs would help practitioners understand when the codebook capacity is sufficient.
- An analysis of what information is preserved by the codebooks (e.g., mutual information between node IDs and labels/embeddings) would provide more direct support than the current theoretical section.

## Removed Points

- **"NID_CL winning on only 1 dataset (RDT-B)"**: Factually incorrect. Verified from Table 3: NID_CL outperforms GraphCL on 5 out of 8 datasets (PROTEINS, MUTAG, COLLAB, RDT-B, IMDB-B) when considering point estimates. The harsh critic's assertion is not supported by the data.
- **"Node ID collision concern"**: With K ∈ {4,6,8,16,32} and ID lengths of 6–15, the total number of possible IDs ranges from 4⁶=4,096 to 32¹⁵ ≈ 3.8×10²². For the graph sizes tested (max 2.4M nodes for ogbn-products), collisions are not a practical concern. This is a speculative point not grounded in the paper's actual configurations.
- **"Table 3 shows no standard deviations"**: Table 3 (lines 498–510) clearly reports ± standard deviations for all entries. This claim is factually wrong.
- **"Missing VQ-VAE baseline is a critical omission"**: The paper explicitly distinguishes NID from VQ-VAE (line 143: "does not involve using the code vectors... for a reconstruction task"). While a comparison would be nice-to-have, the framework is different by design, so this is not a weakness in the paper's own framing.
- **"Missing related works"**: I cannot verify the existence of omitted works without external sources. Removed per instructions.
- **Formatting/typo nitpicks**: Removed per instructions (parser artifacts).
- **Missing appendix content complaints**: Removed per instructions (appendices exist in the original submission).

## Novel Insights

The reviews surface that the paper's most impressive empirical result — large clustering gains from discrete codes — is simultaneously its weakest evidentiary link due to missing methodological detail (distance metric, no continuous-embedding control, no error bars). This tension highlights a broader pattern in the paper: the discrete codes clearly work well for classification tasks where an MLP is trained on top, but the *unsupervised* utility (clustering, interpretability) is less rigorously supported. The gap between the strong, verifiable core (inference speed, competitive accuracy, codebook usage) and the softer, less-verified claims (clustering improvements, interpretability) is the key axis along which the paper could be strengthened. Neither reviewer identified a fatal flaw, but both correctly flagged that the clustering results, as presented, are not reproducible from the information given.

## Suggestions

1. **Specify the distance metric used for k-means clustering on node IDs** (Table 2). If Hamming distance was used (consistent with the subgraph retrieval methodology in line 588), state this. If Euclidean or another metric was used, justify why it is appropriate for discrete index tuples.
2. **Add the missing control experiment**: run the same k-means clustering pipeline on the continuous GCN embeddings from DGCluster (same dimension reduction, same algorithm) and report the results alongside Table 2. This will either validate the "hidden patterns" claim or contextualize it.
3. **Add standard deviations to Table 2** to match the rigor of the other experimental tables.
4. **Either strengthen or compress the theoretical section (Section 3.3).** Either provide a non-conditional proof that the VQ objective provably induces class separation under realistic assumptions, or honestly downgrade it to a consistency observation and replace it with empirical analysis (e.g., mutual information between node IDs and labels).
5. **Soften the "interpretability" claim** to "label-correlated" or add more substantive analysis (e.g., retrieving nodes with the same codeword and analyzing their neighborhoods qualitatively).
6. **Report the total training cost** (GNN training + codebook learning time) alongside inference time so practitioners can assess the full deployment trade-off.

## Score and Decision

The paper presents a novel, well-motivated framework with extensive experimental support (34 datasets) and delivers on its central promise of massive inference speedups with competitive accuracy. The core contributions — discrete node ID learning via multi-layer RVQ, demonstration of codebook collapse avoidance, and integration across GNN paradigms — are substantiated by concrete evidence. The weaknesses are addressable in revision and do not undermine the paper's main claims.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>