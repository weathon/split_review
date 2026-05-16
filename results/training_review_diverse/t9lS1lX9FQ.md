Now I have all the information I need. Let me construct the final consolidated review.

## Summary

This paper proposes NID, a framework that jointly trains GNNs with residual vector quantization (RVQ) to generate highly compact (6–15 int4 integers), discrete, and interpretable node representations (node IDs). Evaluated across 34 datasets spanning node classification, graph classification, link prediction, and clustering, NID demonstrates massive inference efficiency gains (400×–17,000× speedup and 100–1,000× storage reduction) while maintaining competitive accuracy. The framework integrates with multiple GNN backbones and both supervised and self-supervised paradigms.

## Strengths

- **Massive efficiency gains without sacrificing accuracy.** NID achieves 400×–17,000× inference speedups and 100–1,000× storage reductions compared to the base GNN (SAGE), while retaining near-SOTA accuracy on large-scale graphs (e.g., ogbn-products: 81.83% vs 83.27% with 0.7ms vs 11.9s inference; Computer: 93.32% vs 93.59% with 0.5ms vs 95.7ms, Table 9). These gains are the paper's strongest contribution.

- **Interpretability via structured discrete codes.** The paper provides concrete evidence that codewords in node IDs correlate with ground-truth labels (Figure 11 shows clear label alignment in PubMed) and that nodes with similar Hamming-distance node IDs retrieve structurally similar 1-hop subgraphs (lower average GED than random or VQGraph baselines, Table 10). This validates the interpretability claim — a property GNN embeddings lack.

- **Competitive or superior performance across 4 task types on 34 datasets.** Extensive experiments show that NID achieves performance matching or exceeding SOTA on attributed graph clustering (Table 2: best NMI/F1 on 5/7 datasets, e.g., Cora NMI 70.5 vs 62.1, CiteSeer F1 63.3 vs 32.2), competitive results on heterophilic node classification (Table 1: best on all 4 heterophilic graphs), and strong results on link prediction (HR@100 90.33 on Cora vs 85.73 for GCN). The breadth of evaluation directly supports the versatility claim.

- **High codebook utilization prevents collapse.** Usage rates of 79–98% for NID versus ≤18% for VQGraph (Table 11) demonstrate that the multi-codebook RVQ design effectively avoids the codebook collapse that plagues prior VQ-based methods.

- **Seamless integration with diverse GNN backbones and learning paradigms.** NID is demonstrated with GCN, GAT, SAGE, and GIN backbones, and with both supervised (cross-entropy) and self-supervised objectives (GraphMAE, GraphCL, DGCluster). The consistent results support the claim of generality.

- **Systematic ablation studies clarify design choices.** Experiments varying codebook size K, RVQ level M, and MPNN layers L (Figure 12) provide actionable guidelines (K ≤ 16, M = 3, L = 2–6 generally optimal).

## Weaknesses

### Fatal
None.

### Major
None. The paper's core contributions — massive efficiency gains, competitive performance, and interpretability — are supported by evidence. The weaknesses below are substantive but do not threaten the central claims.

### Minor

- **Overstated performance claims in the introduction.** The bullet point "lead to significantly improved performance" (line 30–31) goes beyond what the evidence supports. Across most benchmarks, NID performs competitively (slightly below on homophilic graphs, better on heterophilic ones, mixed on others) rather than "significantly" better. The raw evidence supports "competitive performance with large efficiency gains," which is what the abstract correctly states. The authors should align all high-level claims with this phrasing.

- **Weak theoretical analysis.** Theorem 1 (Section 3.3) assumes each node's feature or its neighbor is exactly an orthonormal discriminative pattern for its class, with no other class's pattern present in the neighborhood. Under this strong assumption — which essentially bakes in perfect class separability at the input level — the theorem guarantees that VQ can assign distinct IDs to different classes and a linear head can achieve zero error. This does not address the realistic regime where embeddings are noisy and classes overlap, nor does it explain *why* compressed discrete codes preserve discriminative information as well as (or better than) full continuous embeddings. The theorem provides a sanity check rather than genuine insight into the method's practical success.

- **Missing limitations discussion.** The paper does not discuss key limitations: (1) the transductive nature — if node IDs are precomputed for all nodes, unseen nodes at inference time require a GNN forward pass, which erodes the inference-speed advantage; (2) the training cost of NID (GNN + codebook learning) is never reported, yet practitioners need this context; (3) whether and how node IDs can be used inductively is not addressed. A dedicated limitations paragraph would improve honesty and reproducibility.

- **Some baseline comparisons not fully controlled.** Tables 1 and 2 compare NID variants against baselines whose numbers are taken directly from other papers (Polynormer, S3GRL, etc.). While the paper re-runs the direct base GNN (GCN/GAT/SAGE) comparisons under controlled settings following Luo et al. (2024), the cross-paper comparisons may not reflect identical tuning budgets, train/val splits, or hardware. The paper should at minimum disclose this caveat more prominently.

- **Mixed graph classification results under-acknowledged.** In unsupervised graph classification (Table 3), NID_CL outperforms GraphCL on 5/8 datasets and NID_AutoGCL outperforms AutoGCL on 4/8 datasets — results are mixed, not strongly supportive. The paper states NID "outperforms all baselines on 3 out of 8 datasets," which is accurate but could benefit from fuller context. Additionally, the 20% gain on the Questions dataset (node classification) is striking but the paper offers only a brief speculation about label imbalance — a deeper analysis would strengthen the claim that "node IDs may preserve information beyond that of original GNN node embeddings."

### Trivial

- The qualitative interpretability analysis (Figures 3, 4, 5) shows that codewords correlate with labels but remains anecdotal. Computing a concrete metric (e.g., purity of codeword clusters with respect to ground-truth labels) would strengthen the claim.

## Nice-to-Haves

- Evaluate the sensitivity of graph-level NID performance to the choice of readout function (mean pooling vs. histogram of codewords vs. sum pooling).
- Provide a rule-of-thumb for selecting codebook size K (e.g., proportional to number of classes or dataset size) to improve reproducibility.
- Report training time overhead of NID vs. the base GNN so practitioners can assess total cost.

## Removed Points

These points were flagged for removal; treat them with caution.

1. **"NID_GCN beats GCN on Cora HR@100 by 4.6 points. The paper attributes this to node IDs 'preserving more information'."** — Factually incorrect. The paper's discussion of "preserving information beyond that of original GNN embeddings" (line 412) refers to the Questions dataset (node classification), not to link prediction. For link prediction, the paper simply states "competitive performance" without attribution.

2. **"NID rarely outperforms the base SSL method (GraphCL or AutoGCL) on graph classification."** — Factually incorrect. NID_CL outperforms GraphCL on 5/8 datasets; NID_AutoGCL outperforms AutoGCL on 4/8 datasets. The results are mixed, not "rarely outperforming."

3. **"The paper should also cover Y / additional tasks."** — These are scope-creep demands; the paper already covers 34 datasets across 4 task types, which is thorough.

4. **Formatting/style nitpicks from the Section-by-Section Notes.** — These reflect parser artifacts or subjective preferences, not paper errors.

## Novel Insights

The most interesting cross-cutting observation from the reviews is that the multi-level RVQ design solves a practical problem (codebook collapse) that has limited prior VQ-based graph methods. Combining this with the finding that 6–15 discrete int4 codes suffice to match the representational power of 128–512 dimensional continuous embeddings suggests a fundamental redundancy in GNN embeddings that the paper only begins to explore. The 20% gain on the imbalanced Questions dataset hints that discretization may act as a regularizer that is especially beneficial in low-signal regimes — a hypothesis worth investigating further.

## Suggestions

1. **Align claims with evidence** — Replace "significantly improved performance" (line 30–31) with "competitive or improved performance" throughout. The paper's main selling point is massive efficiency gains with competitive accuracy; let that stand without overreach.

2. **Add a limitations paragraph** — Discuss the transductive nature of precomputed node IDs, the training cost overhead, and the inductive setting.

3. **Either restructure or remove the theoretical section** — The current Theorem 1 adds little. Either replace it with an analysis that addresses the realistic (noisy, overlapping) regime, or acknowledge its limitations and reposition it as a sanity check.

4. **Add a quantitative interpretability metric** — Compute the purity of codeword clusters or the fraction of nodes whose node ID uniquely identifies their class.

5. **Analyze the Questions gain** — Provide a brief analysis of why NID yields a 20% improvement on this dataset (e.g., codebook assignment patterns, degree distribution).

## Score and Decision

This paper makes a solid empirical contribution: it demonstrates that highly compact discrete node representations learned via joint GNN+VQ training can achieve massive efficiency gains (up to 17,000×) while maintaining competitive accuracy across a broad range of tasks. The evaluation is thorough (34 datasets, 4 task families, multiple backbones), the codebook collapse problem is meaningfully addressed, and the interpretability analysis is a genuine differentiator from prior work. The main weaknesses — overstated claims in a few sentences, a weak theoretical section, and a missing limitations discussion — are presentation issues that can be fixed without changing the core results. No fatal or major flaws are present.

**Score:** 6.5 / 10

**Decision:** Accept

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>