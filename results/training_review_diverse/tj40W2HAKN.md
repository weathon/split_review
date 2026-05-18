Now I have a thorough understanding of the paper. Let me construct the final consolidated review.

## Summary

This paper proposes Node-MoE, a GNN framework that applies different spectral filters to different nodes via a mixture-of-experts architecture. The key idea is that real-world graphs contain a mix of homophilic and heterophilic patterns, so a single global filter is suboptimal. Node-MoE consists of: (1) a gating model that uses contextual features `[X, |AX-X|, |A²X-X|]` combined with a GNN to assign per-node weights to experts, and (2) multiple ChebNetII experts with differentiated initialization (low-pass, constant, high-pass). The paper provides theoretical motivation via an adapted CSBM model (Theorem 1) showing that global filters can incur significant loss on heterophilic nodes while node-wise filtering achieves linear separability. Empirical results show Node-MoE achieves the best average rank (1.29) across 7 benchmark datasets and holds the top accuracy on 5 of them.

## Strengths

1. **Strong empirical performance across both homophilic and heterophilic graphs.** Node-MoE achieves the best average rank (1.29) among all baselines, with top accuracy on Cora (89.38%), CiteSeer (77.78%), ogbn-arxiv (73.19%), Chameleon (73.64%), and Squirrel (62.31%) (Table 1). The improvements over the single-expert ChebNetII are particularly notable on heterophilic datasets: +2.50% on Chameleon and +5.19% on Squirrel, supporting the core claim that node-wise filtering benefits graphs with mixed patterns.

2. **Well-motivated theoretical framework.** Theorem 1 provides formal analysis within an adapted CSBM model: it shows a global low-pass filter incurs a loss lower bound proportional to (q₁-p₁)/(q₁+p₁) on heterophilic nodes, while node-wise filtering achieves linear separability with probability 1−o_d(1). This provides rigorous mathematical motivation that goes beyond empirical intuition.

3. **Effective and interpretable gating model design.** The gating model uses a novel composite input `[X, |AX-X|, |A²X-X|]` with GIN to leverage community structure — an important design choice since nodes with different patterns can share similar raw features. Figure 5 empirically validates that on Chameleon, nodes with low homophily receive high weight from the high-pass expert, confirming the gating model learns sensible assignments.

4. **Top-1 gating preserves performance while reducing complexity.** The ablation (Figure 6) shows Top-1 gating matches soft gating performance across all tested datasets (CiteSeer, ogbn-arxiv, Chameleon, Squirrel), demonstrating that the method can be computationally efficient without sacrificing accuracy.

## Weaknesses

### Fatal
None.

### Major

1. **Missing baseline: uniform ensemble averaging of the same experts.** The paper compares against a single ChebNetII and against MLP-based gating, but it does not compare against a simple mixture of experts with *uniform* weighting (i.e., averaging the outputs of multiple ChebNetII experts without per-node gating). This baseline is critical for isolating the source of improvement: is the gain driven by the per-node gating mechanism, or simply by having more parameters/capacity through multiple experts? The Top-1 gating ablation (Figure 6) partially addresses this concern because Top-1 activates only one expert per node yet matches soft gating, suggesting per-node selection matters. However, a direct uniform-weighting comparison across the same expert set would cleanly distinguish (a) the benefit of multiple experts from (b) the benefit of per-node gating, and this experiment is straightforward to run.

### Minor

2. **Theory–method gap in the gating model's learning problem.** Theorem 1 assumes oracle knowledge of which nodes belong to homophilic vs. heterophilic patterns (i.e., "if different filters are applied to homophilic and heterophilic sets separately"). The paper's actual method must learn this assignment without supervision. While the paper acknowledges this challenge (Section 3, paragraph 2: "without ground truth on node patterns, how can we select the appropriate filters for different nodes?"), there is no analysis — even informal — of the conditions under which the gating input `[X, |AX-X|, |A²X-X|]` is sufficient to discriminate patterns. The theory motivates *why* node-wise filtering is valuable; the empirical results show *that* the method works. Bridging these with even a synthetic experiment or informal argument would strengthen the paper.

3. **No analysis of performance as a function of number of experts.** The paper states it experiments with 2, 3, and 5 ChebNetII experts (Section 4.1) but never reports results broken down by expert count. Readers cannot tell whether more experts consistently improve performance, saturate, or even hurt. This makes it harder to assess the method's sensitivity to this important architectural choice.

4. **No discussion of limitations or failure cases.** The paper claims robust performance but does not discuss scenarios where Node-MoE underperforms. For example, on the Actor dataset, GloGNN achieves 37.35% vs. Node-MoE's 36.28% — the best heterophilic-specific baseline beats the proposed method. Acknowledging such cases would improve credibility.

5. **Top-1 gating computational cost not fully specified.** The paper claims Top-1 gating (k=1) has "complexity comparable to an individual expert model" but does not clarify whether all experts must still be forward-passed to compute gating logits, or whether only the selected expert is run. In standard MoE implementations the gating network is computed independently before expert activation, implying only one expert needs to be invoked, but this should be stated explicitly.

### Trivial
6. The behavioral analysis mentions experiments on CiteSeer (line 206) but only shows results for Chameleon in the main text. These results likely reside in the appendix stripped by the parser.

## Nice-to-Haves

- Extend the learned filter/gating weight analysis (Figures 4–5) to a homophilic dataset (e.g., CiteSeer) to confirm the gating model also correctly assigns low-pass filters to high-homophily nodes.
- Show the learned filters with and without the filter smoothing loss to directly visualize its regularization effect.
- Add a synthetic CSBM-based experiment that tests whether the gating model can recover the true pattern membership from the proposed input features, bridging the theory–method gap.
- Report performance broken down by number of experts (2, 3, 5) to show sensitivity to this hyperparameter.

## Removed Points
- **"Additional CiteSeer behavioral analysis needed"**: The paper states it conducted experiments on both CiteSeer and Chameleon (line 206). The CiteSeer figures are not present in the main text but likely reside in the stripped appendix. Evaluating based on missing appendix content is not permissible.
- **"Disconnect between theory and method" framed as a fatal issue**: While the theory–method gap is real, the reviewer overstated its severity. The paper acknowledges this gap explicitly ("without ground truth on node patterns, how can we select the appropriate filters?") and provides empirical validation. The theory serves as motivation, not as a learning algorithm. The concern is valid but minor, not critical.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add a uniform-weighting ensemble baseline (same expert set, no gating) to Table 1 or the ablation study to isolate the contribution of per-node gating from the benefit of multi-expert capacity.
2. Add a brief discussion or synthetic experiment that analyzes when the proposed gating input features are sufficient to discriminate node patterns, connecting Theorem 1's assumptions to the method's learning problem.
3. Report the ablation by number of experts (2, 3, 5) and add a brief limitations paragraph acknowledging datasets where gains are marginal or the method is outperformed (e.g., Actor).
4. Explicitly state in Section 3.4 whether Top-1 gating requires computing all experts' representations for each node, or only the selected expert's.

## Score and Decision

This paper addresses a well-motivated problem with a clean architectural solution, strong empirical results (best average rank 1.29 across 7 datasets), and a theoretical motivation that goes beyond most method papers in this space. The weaknesses are real but addressable: the missing uniform-weighting baseline is the most consequential, but the Top-1 gating ablation partially mitigates it, and the other issues are minor clarity/analysis gaps rather than structural flaws. The paper presents a genuine contribution — node-wise filtering via MoE for graphs with mixed homophilic/heterophilic patterns — and the evidence supports its main claims.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>