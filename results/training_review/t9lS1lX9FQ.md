Now I have a thorough understanding of the paper and can verify the reviewer claims. Let me write the consolidated review.

## Summary

This paper introduces NID, a framework that learns highly compact (6–15 int4 dimensions), discrete node representations — "node identifiers" — by applying residual vector quantization (RVQ) to multi-layer GNN embeddings. The node IDs are used directly for downstream tasks (classification, clustering, link prediction, graph classification) via lightweight MLPs, achieving competitive accuracy while dramatically accelerating inference. The framework is evaluated on 34 datasets across four task families under both supervised and self-supervised paradigms, showing particular strength in clustering and codebook utilization.

## Strengths

- **Exceptional breadth of empirical evaluation.** The paper covers 34 datasets across node classification (homophilic and heterophilic, including large-scale graphs with millions of nodes), graph classification, link prediction, and attributed graph clustering — under both supervised and self-supervised settings. This breadth makes the claims about versatility well-supported.

- **Effective mitigation of codebook collapse (Table 11).** NID achieves codebook usage rates of 79–98% across datasets, compared to only 0.8–18% for VQGraph. This is a concrete, well-documented improvement over prior VQ-based graph methods, attributable to the multi-codebook RVQ design. This is one of the paper's strongest methodological contributions.

- **Strong clustering results (Table 2).** NID_DGCluster substantially outperforms the base DGCluster on 5 of 7 datasets (e.g., NMI improves 8–13 points on Cora, CiteSeer, PubMed) while also reducing clustering time. This is the clearest empirical win and suggests discretization acts as a beneficial regularizer for clustering.

- **Extreme compression with minimal accuracy loss.** On ogbn-products, NID_SAGE achieves 81.83% accuracy (vs. SAGE's 83.27%) using only 17.5 MB storage and 0.7 ms inference vs. SAGE's 1.9 GB and 11.9 s — over 17,000× speedup. The 6-15 int4 dimensional representations compress 128–512 dimensional floating-point embeddings by orders of magnitude while retaining competitive accuracy.

- **Systematic ablation studies (Figure 5)** on codebook size (K), RVQ level (M), and MPNN layers (L) provide practical guidance and validate design choices. The finding that M=3 and K≤16 work well across datasets is informative for practitioners.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims — that compact discrete node IDs can serve as effective representations — are well-supported by the breadth of experiments. No single weakness invalidates the central contribution.

### Minor

- **The interpretability claim is overstated relative to the evidence.** The paper claims node IDs are "interpretable" and that this is a key advantage over continuous embeddings (abstract, introduction, conclusion). The supporting evidence consists of (a) codeword distribution plots showing correlation with ground-truth labels on PubMed, and (b) a graph-edit-distance (GED) analysis showing that nodes with similar IDs have structurally similar neighborhoods. These demonstrate that the codes capture label-relevant and structural information — which is a useful property — but this is not "interpretability" in the sense a practitioner would expect (e.g., being able to understand what structural role a particular code encodes, or why a specific node received its ID). The paper would benefit from either toning down the claim to "codes provide meaningful abstraction" or adding case studies on small graphs showing what specific codewords represent structurally.

- **The large improvement on the Questions dataset (96.85 vs. 77.40 ROC-AUC for GCN, a 19-point gain) lacks sufficient analysis.** The paper speculates that "node IDs may preserve information beyond that of original GNN node embeddings" due to the dataset's extreme class imbalance (98% one class). This is a plausible hypothesis, but no diagnostic analysis is provided — e.g., probing whether the quantization boundaries create a more separable representation for the minority class, comparing learned ID distributions across classes, or verifying that the baselines were properly tuned for this specific dataset. The result is consistent across two backbones (GCN and GAT both show ~19-point gains), which suggests it is not an artifact, but it remains unexplained. The paper should either provide analysis or present the finding more cautiously.

- **The inference time comparison (400×–17,000× faster) is presented without accounting for the upfront cost of generating node IDs.** Table 6 and the surrounding text compare SAGE inference time (which includes graph loading and message passing) against NID_SAGE inference time (which is just an MLP forward pass on precomputed IDs). For transductive settings where IDs are generated once and reused, this comparison is reasonable, but the paper does not explicitly state that the (significant) one-time cost of GNN forward + RVQ quantization is excluded. This should be acknowledged to avoid misleading readers, especially those considering inductive settings.

- **Selective reporting on the unsupervised node classification results (Table 1).** The text highlights that NID_MAE "surpasses all other approaches on CiteSeer" (74.2 vs. GraphMAE's 73.4) but does not acknowledge the drops on Cora (80.8 vs. GraphMAE's 84.2) and PubMed (76.4 vs. GraphMAE's 81.1). Presenting these alongside the CiteSeer win would give a more balanced picture.

- **The theoretical analysis (Theorem 1) is too simplified to meaningfully validate the full method.** The theorem assumes a one-layer GCN with identity activation, features that are exact discriminative patterns, and a weight matrix aligned with those patterns — stripping away all non-linearities, multiple layers, RVQ, and joint training that define the actual framework. The paper acknowledges this is a "simplified model," but the gap between the theorem's setting and the actual method is so large that the result (distinct IDs for different classes → zero linear classification error) provides limited insight. Moving it to the appendix with a stronger caveat would better reflect its value.

### Trivial

- The boxed summary statement could be read as promotional ("uncover hidden patterns... significantly improved performance") and would benefit from more measured language.
- The t-SNE visualization (Figure 3 in the paper, referenced as "fig:oversmoothing") is not directly tied to the NID framework — it shows MPNN embeddings at different layers, which motivates the multi-layer design but doesn't directly validate the node IDs.

## Nice-to-Haves

- **Compare node IDs to continuous embeddings of the same dimension.** A GNN compressed to output 6–15 continuous dimensions (or a GNN + PCA to the same dimensionality) would isolate whether the discretization itself adds value beyond aggressive dimensionality reduction.
- **Case study on a small graph** showing actual node IDs for a few nodes (e.g., (c11,c12,c13,c21,c22,c23)) and explaining why codes are similar/different based on neighborhood structure would concretely support the interpretability claim.
- **Include the upfront generation cost** (GNN forward + VQ time and memory) somewhere in the efficiency analysis, even if only as a footnote.

## Removed Points

These points from the reviews are flagged for removal, treated with caution:

1. **Harsh Critic's claim that the EMA replacement for codebook loss is "not explicitly stated."** The paper explicitly states this at line 126: "In practice, we can use exponential moving averages... as a substitute for the codebook loss." This criticism is factually incorrect.

2. **Harsh Critic's speculation that the Questions result is "likely an artifact" due to "different data splits, evaluation protocol, or hyperparameter search."** The paper states it maintains "all experimental settings as described in luo2024classic" (line 410), using standard evaluation protocols. The improvement is consistent across both GCN and GAT backbones (both showing ~19-point gains), making an experimental confound unlikely.

3. **Harsh Critic's claim that the theoretical analysis gives "a false sense of rigor" and "should be moved to an appendix with a clear disclaimer."** While the theory is simplified, the paper already describes it as "a simplified model" (line 174). Simplified theoretical analysis is standard practice in ML papers to provide intuition. The criticism is valid for tone but overstated in severity — I have kept the substance as a minor weakness.

4. **Strength Finder's claim of "Consistent gains on heterophilic graphs."** On Squirrel and Chameleon, NID_GCN's improvements over GCN are marginal (+0.59 and +0.18 points respectively), and NID_GAT underperforms GAT on both. Only Questions shows a large gain. "Consistent" is inaccurate; I have removed this as a standalone strength.

5. **Strength Finder's "Theoretical guarantee for classification" framing** overstates the value of Theorem 1 by not mentioning its strong simplifying assumptions. The theorem is retained as part of the paper's strengths but contextualized by the minor weakness above.

## Novel Insights

None beyond the paper's own contributions. The reviews surface useful suggestions for improvement but do not identify a limitation or insight that the paper itself misses, beyond the standard observation that discrete quantization may be particularly beneficial for imbalanced data (which the paper already hints at).

## Suggestions

1. **Tone down or better support the interpretability claim.** Either add a concrete case study (e.g., show node IDs for specific nodes on Cora and explain structural patterns corresponding to specific codewords) or replace "interpretable" with "codes capture meaningful abstractions" throughout the paper.

2. **Add diagnostic analysis for the Questions result.** At minimum, compare the learned ID distribution across classes, check if the GCN baseline was verified under identical hyperparameter tuning, and visualize the embedding space before/after quantization for this dataset.

3. **Explicitly state that the reported inference time excludes the one-time cost of generating node IDs.** Add a sentence acknowledging this and, if possible, report the total cost (training + once-per-dataset ID generation + per-query MLP inference).

4. **Balance the reporting of Table 1 results.** Acknowledge the drops on Cora and PubMed alongside the CiteSeer win.

5. **Move Theorem 1 to the appendix or add a caveat connecting it to the full framework.** The current presentation over-promises on theoretical validation.

## Score and Decision

The paper presents a well-motivated framework with a broad and generally well-executed empirical evaluation. The codebook usage analysis and clustering results are clear contributions. The weaknesses are real but addressable: the interpretability claim needs either better evidence or softer language, the Questions result needs diagnostic analysis, and the inference comparison should be more transparent. No fundamental flaw undermines the core contribution.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>