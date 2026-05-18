Now I have a thorough understanding of the paper and all reviewer claims. Let me construct the final consolidated review.

## Summary

This paper proposes TopGQ, the first post-training quantization (PTQ) framework for graph neural networks. TopGQ assigns group-wise quantization parameters based on local topological structure (indegree + localized Wiener index), computes the Wiener index via an accelerated algorithm that exploits bounded subgraph diameter, and absorbs group-wise scales into the adjacency matrix to enable efficient integer matrix multiplication. Experiments on node and graph classification across multiple architectures (GCN, GIN, GraphSAGE) and datasets show that TopGQ matches or exceeds QAT-based methods while achieving orders-of-magnitude faster quantization (up to 358× speedup).

## Strengths

1. **First dedicated PTQ for GNNs, with convincing efficiency gains.** The paper proposes the first post-training quantization method specifically designed for GNNs. The speed advantage over QAT methods is dramatic and clearly documented (e.g., Reddit/GraphSAGE 4-bit: 0.02 hours vs. 42.27 hours for Degree-Quant, while simultaneously improving accuracy from 89.86% to 93.93%). These improvements are large enough that single-run results still convey the message.

2. **Topology-based node grouping is well-motivated and empirically supported.** The observation that indegree alone leads to groups with large feature-magnitude spreads (Figure 2) is clearly demonstrated. The proposed use of (indegree + localized Wiener index) produces more compact groups, and the ablation (Table 4) shows that topology grouping substantially improves PTQ accuracy (e.g., GIN on PROTEINS: 72.62% → 79.93%).

3. **Accelerated Wiener index computation is practically impactful.** Algorithm 1 exploits the bounded diameter (≤2k) of k-hop subgraphs to compute the localized Wiener index efficiently. Table 6 shows speedups of up to 602× over standard algorithms (e.g., ogbn-proteins: 2.84 hours → 0.0002 hours), making topology grouping feasible on large graphs.

4. **Scale absorption is a principled engineering contribution.** The method of absorbing node-group scales into the static adjacency matrix allows node-wise quantization to be implemented with pure integer arithmetic. Figures 5–6 show that this leads to better-distributed activations across the quantization range.

5. **Evaluation breadth.** Experiments span large-scale node classification (Reddit, ogbn-proteins, ogbn-products), smaller node classification (Cora, CiteSeer, PubMed), and graph classification (PROTEINS, NCI1), using GCN, GIN, and GraphSAGE with 4-bit and 8-bit quantization.

## Weaknesses

### Fatal

None.

### Major

None. No verified weakness undermines the paper's core claims.

### Minor

1. **No statistical uncertainty reported.** Tables 1, 2, 3, 4, and 7 report single accuracy numbers without standard deviations, confidence intervals, or number of seeds. GNN quantization can be sensitive to initialization and calibration data. While the improvements are often large enough (e.g., 4+ percentage points on Reddit) that the conclusions are likely robust, the absence of any variance measure reduces confidence in the smaller margins (e.g., ogbn-proteins where some gains are ~1 pp). Including at least 3 runs with mean ± std for the main comparisons would substantially strengthen the paper.

2. **Scale absorption is not quantitatively ablated in the accuracy study.** Table 4 compares "PTQ baseline" against full TopGQ (topology grouping + scale absorption), but does not include an intermediate condition (e.g., topology grouping without scale absorption). Scale absorption is listed as a separate contribution and claimed to "preserve activation precision" (Section 5.3), yet its standalone contribution to accuracy cannot be separated from grouping. Although Section 6.7 provides qualitative distribution plots, a quantitative ablation would clarify the source of the gains.

3. **Accelerated Wiener index correctness is validated only indirectly.** Table 6 compares computation speed against standard shortest-path algorithms, but does not verify that the computed Wiener index values match ground truth from a reference implementation. The method's success in downstream tasks provides indirect evidence of correctness, but a direct comparison (e.g., on a random subset of nodes) would rule out the possibility that speed is achieved through approximations or errors.

4. **Memory overhead of scale absorption is not discussed.** Absorbing node-group scales into the adjacency matrix changes its representation (now a quantized matrix with row-wise scales embedded). For large graphs like ogbn-products (~120M edges), this overhead could be non-negligible. The paper should quantify this and place it alongside the compute savings.

5. **The centrality-measure comparison (Table 7) is limited scope.** The paper compares localized Wiener index against other centrality measures (betweenness, closeness, Katz), but appears to do so on a single dataset. Running this analysis on at least one additional dataset would strengthen the claim that Wiener index is superior for this task.

### Trivial

- The paper mentions continuous graph updates (e.g., social media, traffic networks) as motivation but does not discuss how TopGQ handles dynamic topologies. Group assignment depends on the current topology; recomputing Wiener indices on a changed graph has a cost that is not analyzed.
- The nearest-neighbor group assignment rule for unseen test vertices (first compare I, then W) is stated but not evaluated against alternatives (e.g., k-NN over the (I,W) space).
- Section 5.3 says "Scale Absorption preserves both the benefits of fixedpoint operations" — small typo ("fixedpoint" → "fixed-point").

## Nice-to-Haves

- A toy-graph walkthrough showing how (I(u), W_k(u)) maps to groups and why this reduces within-group feature variance would make the intuition behind the method more concrete.
- An ablation separating the contribution of indegree vs. Wiener index (i.e., group by indegree alone, Wiener index alone, and both) would clarify the role of each topological feature.
- A sensitivity analysis for the hop-count hyperparameter k would help users understand the accuracy–compute trade-off.
- Including SMP (Wang et al., 2023) and Eliasof et al. (2023) as baselines — or explicitly justifying why the comparison would be apples-to-oranges due to different target problems (oversmoothing mitigation, wavelet-based compression, different depth regimes) — would preempt concerns about baseline completeness.
- Inference latency on resource-constrained hardware (e.g., mobile CPU) would strengthen the deployment motivation.

## Removed Points

These points from the reviewer are flagged for removal; they are kept here for reference but should be treated with caution:

- **Criticism about "first PTQ" claim being unqualified because general CNN/transformer PTQ methods could be applied to GNNs.** This is speculative — the reviewer provides no evidence that general PTQ methods would work for GNNs without modification. The paper's claim of "first PTQ for GNNs" refers to a method designed specifically for the GNN setting (addressing node-wise feature magnitude diversity via topology grouping), which is not addressed by general PTQ methods.
- **Criticism about missing SMP and Eliasof et al. baselines.** The paper's Related Work correctly identifies these as QAT methods. SMP targets oversmoothing in deep GNNs specifically, and Eliasof et al. uses wavelet-based compression. Comparison against general-purpose QAT methods (Degree-Quant, SGQuant, A²Q) is already provided and is appropriate for the paper's scope.
- **"Outperforms FP32 without analysis" sub-point.** The paper addresses this briefly (Section 6.2: "hints that existing QAT baselines do not consider the nature of GNN"). The explanation is brief but not absent.
- **Strength Finder's claim about "comprehensive evaluation demonstrates robustness"** — retained but de-emphasized as somewhat generic.

## Novel Insights

None beyond the paper's own contributions. The reviews surface no structural flaw or missed connection that the paper itself does not already address or acknowledge.

## Suggestions

1. **Add error bars.** Run the main experiments (Tables 1–3) with at least 3 random seeds and report mean ± std. This is the single most impactful change for credibility.
2. **Ablate scale absorption quantitatively.** Add an intermediate column to the ablation study: topology grouping with naive per-node scales (floating-point aggregation) vs. topology grouping with absorbed scales.
3. **Verify accelerated Wiener index correctness.** Compare values from Algorithm 1 against a brute-force all-pairs shortest-path computation on a random subset of subgraphs across all datasets, reporting both exact match rate and speedup.
4. **Quantify the memory overhead** of the scale-absorbed adjacency matrix versus a plain quantized adjacency matrix.
5. **Expand the centrality comparison** (Table 7) to at least one additional dataset to demonstrate that the superiority of Wiener index is not dataset-specific.

## Score and Decision

This paper proposes a genuinely novel and practical approach — the first PTQ framework designed for GNNs — with strong empirical results showing order-of-magnitude speedups over QAT baselines while maintaining competitive accuracy. The four contributions (topology grouping, accelerated Wiener index, scale absorption, and the overall PTQ framework) are clearly articulated and individually supported. The verified weaknesses (no error bars, incomplete ablation of scale absorption, indirect correctness validation of Wiener index algorithm, and a few unaddressed overhead/scope questions) are real but minor — they reduce polish and completeness but do not undermine the core claims. All are addressable in a revision.

**Overall assessment:** Solid paper with clear contributions and addressable methodological gaps. Recommend acceptance.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>