Now let me write the final consolidated review, carefully filtering each claim from the reviewers.

## Summary

This paper proposes TopGQ, the first post-training quantization (PTQ) framework for graph neural networks (GNNs). The key idea is to group nodes based on local topological information (indegree and a localized Wiener index) so that nodes sharing similar topological structure also share quantization parameters. A fast algorithm for computing the localized Wiener index is introduced, along with a scale absorption technique that fuses node-wise scales into the adjacency matrix to enable efficient integer arithmetic. Experiments on node and graph classification tasks show that TopGQ achieves accuracy competitive with or exceeding quantization-aware training (QAT) methods while reducing quantization time by orders of magnitude (up to 358×).

## Strengths

1. **First PTQ method for GNNs with concrete speedups.** The paper is the first to demonstrate that post-training quantization can work for GNNs, eliminating the costly retraining step required by QAT methods. Table 1 (e.g., Reddit, 4-bit GraphSAGE: TopGQ 93.93% in 0.02 hours vs. Degree-Quant 89.86% in 42.27 hours) provides concrete evidence of the speed–accuracy trade-off.

2. **Topology-based grouping is validated by ablation.** Table 4 cleanly isolates the contribution of each component: on Reddit GIN 4-bit, the PTQ baseline gets 37.57%, adding scale absorption improves to 81.94%, and adding topology grouping further improves to 90.06%. This decomposition convincingly shows that both proposed components are necessary.

3. **Choice of Wiener index is supported by a comparison against alternative centrality measures.** Table 7 shows that localized Wiener index consistently outperforms betweenness, closeness, and Katz centrality for grouping, providing empirical justification for the design choice.

4. **Scale absorption is shown to improve activation quantization.** Figure 5 visualizes how scale absorption distributes activations more evenly across the integer range (−128 to 127), and Table 5 confirms that inference time with TopGQ is comparable to or faster than baselines (e.g., GCN on Reddit: TopGQ 5.62 ms vs. A²Q 35.06 ms).

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims—first PTQ for GNNs, competitive accuracy, order-of-magnitude speedups—are supported by the evidence presented. The issues below are addressable and do not invalidate the contributions.

### Minor

1. **The accelerated Wiener index algorithm (Algorithm 1) is underspecified for full reproducibility.** The derivation from Equation (10) to Equation (12) is worked out only for \(k=2\). The generalization to arbitrary \(k\) is given in pseudocode, but the mapping between the subtractive formula and the built sets \(h_l\) is opaque, and the notation (the same symbol \(k\) appears as hop count and as a multiplicative constant in line 14) is confusing. The paper does not verify that the algorithm's output matches the naive all-pairs computation for any specific subgraph. Since the large speedups in Table 6 (up to 602×) depend on this algorithm, clearer exposition and a correctness check would substantially strengthen the paper.

2. **The paper acknowledges that TopGQ sometimes exceeds FP32 accuracy but does not deeply investigate why.** The explanation ("existing QAT baselines do not consider the nature of GNN") does not directly explain why a PTQ scheme would outperform the *exact same* full-precision model. While quantization can act as regularization, and this phenomenon is known in other domains, the paper would benefit from a brief discussion (e.g., whether the FP32 models were trained to convergence, whether quantization implicitly provides regularization, or whether there is any evaluation discrepancy).

3. **No comparison against simple PTQ baselines (e.g., per-channel or per-tensor quantization) for GNNs.** The ablation includes a "PTQ baseline" but does not specify its quantization granularity. Since TopGQ is the first PTQ method for GNNs, there is no existing PTQ baseline specific to GNNs, but a comparison against a straightforward per-channel or row-wise quantization scheme applied to the same GNN architectures would help isolate the benefit of the topology-based grouping from the benefit of fine-grained quantization generally.

4. **Results are reported without variance or confidence intervals.** All accuracy numbers appear to come from a single run. Given the randomness in GNN training and QAT procedures, reporting means and standard deviations over multiple seeds is standard practice.

5. **The choice of \(k\) (hop count) is not analyzed.** The paper uses \(k=2\) or \(k=3\) depending on the dataset but provides no ablation or sensitivity study. Since \(k\) determines subgraph size and grouping granularity, it affects both accuracy and computation time; a sweep would be informative.

6. **Inductive setting (unseen nodes) receives limited analysis.** The paper describes a nearest-neighbor fallback for unseen \((I,W)\) pairs at inference time (Section 5.1) but does not evaluate how often the fallback is triggered or its effect on accuracy.

### Trivial

- The pseudocode in Algorithm 1 has formatting issues (line 13 appears garbled in the extracted text) that should be cleaned up.
- The text and Figure 1 describe quantization times in days/hours, but the paper would benefit from ensuring all reported times use consistent units for easy comparison.

## Nice-to-Haves

- A quantitative metric (e.g., feature magnitude variance per group, KL divergence from uniform for quantized activations) would strengthen the qualitative visual evidence in Figure 2 and Figure 5.
- For the scale absorption method, a brief discussion of memory overhead (absorbing \(S_X\) into \(\tilde{A}\) produces a denser or real-valued matrix) and its implications for sparse adjacency representations would be useful.
- A comparison of the accelerated Wiener index output against naive computation on a subset of nodes would confirm correctness.

## Removed Points

*The following points raised by reviewers were removed with justification:*

- **"Inconsistency between Figure 1 (4.9 days) and Table 1 (4.28 hours)"**: The reviewer claimed Table 1 reports 4.28 hours for Degree-Quant on ogbn-products. Since Table 1 is an image in the parsed text, this claim cannot be verified from the available content. The text's 4.9-day claim for ogbn-products (a larger dataset than Reddit, where 42.27 hours is reported) is internally consistent. Removed as unverifiable.

- **"The speed comparison against QAT conflates PTQ vs QAT paradigm"**: The paper's claim is that *TopGQ as a whole* (PTQ + topology grouping + scale absorption) is faster and better than existing QAT methods. Comparing against QAT baselines is the natural comparison since no GNN-specific PTQ baselines exist. This is not a weakness; it is how new methods in a category are evaluated.

- **"Section 5.3 scale absorption memory and sparsity implications"**: The paper explicitly states that \(\tilde{A}_X\) is pre-calculated and row-wisely quantized. In many GNN architectures (e.g., GCN), \(\tilde{A}\) is already a real-valued normalized matrix, so the sparsity concern is architecture-dependent. This is a reasonable point for discussion but not a weakness of the paper's claims.

- **"Section 6.7 scale absorption analysis is qualitative"**: The visual evidence (Figure 5) is accompanied by a clear explanation of why even distribution across quantization bins reduces error. A quantitative metric would be nice-to-have but the qualitative analysis is sufficient.

- **Various formatting/style nitpicks and complaints about missing appendix content**: Removed per instructions (parser artifacts, not author errors).

## Novel Insights

None beyond the paper's own contributions. The two reviews largely converge on the same picture: a novel and well-motivated method with solid empirical results, but with some presentation and verification gaps that are addressable in revision.

## Suggestions

1. Provide a correctness verification of the accelerated Wiener index algorithm: compare its output against naive all-pairs computation on a subset of nodes across datasets and confirm exact match.
2. Add a sensitivity study varying \(k\) (hop count) to show the accuracy–speed trade-off.
3. Report mean and standard deviation over multiple runs (at least 3 seeds) for the main results.
4. Include a simple per-channel PTQ baseline to further isolate the benefit of topology-based grouping.
5. Investigate and discuss the cases where TopGQ exceeds FP32 accuracy — is the FP32 model fully converged? Does quantization provide a regularization benefit?
6. Clarify the Algorithm 1 pseudocode: use distinct symbols for the hop count parameter and any multiplicative constants, and show the general formula for arbitrary \(k\) more explicitly.

## Score and Decision

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>