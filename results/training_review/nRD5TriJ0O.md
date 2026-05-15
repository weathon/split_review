Now I have a thorough understanding of the paper and all the reviewer claims. Let me write the consolidated review.

## Summary

The paper studies graph active learning (GAL) on heterophilic graphs, finding that prior GAL methods (designed for homophilic graphs) often underperform random sampling in this setting. The authors diagnose the cause as prior GAL methods selecting isolated nodes whose induced subgraph fails to reflect the heterophilic structure, and propose "Know Your Neighbors" (KyN) — a method that partitions the graph, represents subgraphs via Jordan-center-based ego-embeddings, and samples subgraphs using ℓ₁ Lewis weights, thereby labeling all nodes within selected subgraphs. Experiments on six heterophilic benchmarks show KyN outperforms existing GAL methods by significant margins.

## Strengths

- **Identifies an underexplored and practically important problem.** Heterophilic graph active learning is a real gap in the literature; prior GAL work has focused almost exclusively on homophilic graphs. The paper's motivating observation — that standard GAL methods are unreliable on heterophilic graphs — is supported by the empirical results.

- **Novel method design with a clear, intuitive principle.** The "Know Your Neighbors" principle (label nodes together with their neighbors) is well-motivated and directly addresses the identified issue. The "partition then sample" scheme is a pragmatic way to avoid neighbor explosion, and the use of ℓ₁ Lewis weights for subgraph selection is novel in the GAL context.

- **Strong and consistent empirical improvements.** The method outperforms baselines across multiple heterophilic datasets (up to 12.1% improvement), with different labeling budgets, with heterophilic GNN backbones (FAGCN, M2M-GNN), and on a large-scale graph (snap-patents, 2M+ nodes). Runtime is shown to be practical and often faster than several baselines.

## Weaknesses

### Fatal
None.

### Major

- **The core diagnostic analysis (Section 3.1, Figure 2) is an imperfect proxy and the claimed causal link to GNN performance is not established.** The paper measures the local homophily distribution of the *induced subgraph of labeled nodes* and argues this is what "GNNs receive." However, during training the GNN performs message passing on the *full graph* (including unlabeled neighbors' features), so the supervisory signal is not solely determined by labeled-labeled edges. The paper acknowledges this approximation ("we do not count the unlabeled neighbors") but does not empirically verify that the induced-subgraph homophily distribution causally affects downstream accuracy under full-graph message passing. While the intuition that labeling neighbors provides a richer heterophilic signal is reasonable, the specific diagnosis may be incomplete, and the paper does not rule out alternative explanations for prior methods' failure (e.g., inadequate coverage, feature-medoid selection, or simply insufficient labeled nodes in diverse neighborhoods). This weakens but does not invalidate the method — the method's empirical success stands on its own, but the motivational narrative is overclaimed.

- **The theoretical guarantee (Theorem 3.6) does not cover the actual experimental setup, and the gap is not honestly characterized.** The theorem assumes (i) a one-layer *linear* encoder, (ii) a "nice hinge function" loss (Definition 3.5, defined for scalar binary classification), and (iii) the loss is a relative-error coreset for this setting. However, the experiments use a *three-layer SAGE-Mean encoder with ReLU nonlinearities and multi-class cross-entropy loss*. The paper states "the results are similar on any multi-layer linear GNNs" — but SAGE-Mean with ReLU is not linear, and multi-layer composition with nonlinearities is not equivalent to a linear model. Furthermore, the claim that cross-entropy loss "is also a (1, ln2, ln2)-nice hinge function" is asserted without derivation or citation, and the nice hinge function definition applies to scalar inputs (binary classification) while CE operates on vector logits (multi-class). The paper provides no argument or experiment bridging this gap. This does not make the method unsound, but the theoretical contribution is significantly narrower than claimed.

- **No ablation study isolates the contribution of each component.** KyN combines METIS partitioning, Jordan-center-based subgraph representation, and ℓ₁ Lewis weight sampling. There is no comparison against simpler alternatives such as: (a) random subgraph selection within partitions, (b) uniform sampling without Lewis weights, (c) alternative central node definitions, or (d) Lewis weights on individual nodes without partitioning. Without ablations, it is unclear whether the empirical gains come from the Lewis weight sampling, the subgraph structure itself (any subgraph selection would label adjacent nodes), the Jordan center representation, or the partitioning scheme. Figure 5 only varies the number of partitions c, which is hyperparameter sensitivity, not component ablation.

### Minor

- **The claim that prior GAL methods "fail to outperform random sampling" is overstated.** The abstract and conclusion make this claim without qualification, but in Table 1 several baselines *do* outperform random sampling on some datasets/budgets (e.g., GraphPart, GreedyET, DOCTOR on Wisconsin and Texas). The body text hedges ("on some datasets... fail to *consistently* outperform"), but the framing elsewhere inflates the perceived gap. This is a rhetoric issue, not a substantive one — the core finding (no prior method is consistently reliable on heterophilic graphs) is still supported.

- **The connection between Proposition 3.1 and the paper's analysis is incomplete.** Proposition 3.1 bounds accuracy in terms of *predicted* local homophily discrepancy D(h, ĥ), but the analysis in Figure 2 and Section 3.1 concerns the *training set's induced subgraph* homophily distribution. The paper does not formally connect the two: Proposition 3.1 says nothing about how training set selection affects predicted homophily or downstream accuracy. The proposition is about a property of predictions, not about training set design.

- **The treatment of multi-class CE as a nice hinge function is unjustified.** The nice hinge function (Definition 3.5) operates on ℝ → ℝ⁺ (scalar input). Multi-class cross-entropy takes vector-valued logits. The paper states it is "reformulated" but provides no reformulation. This is a gap in the theoretical narrative.

- **Jordan center computation cost is not discussed.** Computing the Jordan center of each subgraph requires all-pairs shortest paths (O(|V_i|³) worst-case per partition). For large subgraphs or datasets with millions of nodes (like snap-patents), this could be prohibitive. The paper reports only end-to-end runtime, which may obscure this cost.

### Trivial

- The local homophily definition includes the node itself in its 1-hop neighborhood (line 48). This is a nonstandard convention; while acknowledged, it shifts homophily values upward and should be justified more explicitly or de-emphasized in the diagnostic analysis.

- The hyperparameter recommendation (c ≈ |V|/C) is not consistently followed in the experiments (e.g., Wisconsin: |V|/C ≈ 50, c = 25).

## Nice-to-Haves

- **Test KyN on homophilic graphs** (e.g., Cora, Citeseer, PubMed) to verify the method does not degrade performance when heterophily is absent. While the paper focuses on heterophilic graphs, such an experiment would strengthen generalizability claims.
- **Empirically verify the link between training set induced homophily and GNN accuracy** by constructing training sets with different induced-subgraph homophily levels and measuring downstream performance under full-graph message passing. This would substantiate the core motivation.

## Removed Points

- *"No experiment on homophilic graphs is provided to test whether KyN degrades"* — Moved to Nice-to-Haves since the paper explicitly scopes to heterophilic graphs; testing homophilic graphs is a nice addition, not a core flaw.
- *"The paper claims 'this paper is the first to explore Lewis weight sampling for graph active learning.' Given the method's reliance on partitioning and subgraph representation, this claim is narrow but fair."* — This is actually from the "strengths" section of the harsh critic. It's a minor strength and I've incorporated it.
- *"The paper includes an analysis of the local homophily distribution of training sets (Figure 2), which provides an intuitive illustration of the issue even if the interpretation is flawed."* — This conflicts with the verified weakness that the analysis is imperfect. Per instructions, when strength and weakness disagree, weakness wins. The paper's Figure 2 analysis is retained as a weakness, not a strength.
- *"The experimental evaluation covers multiple real-world heterophilic datasets and includes runtime comparisons, showing KyN is practically feasible."* — This is a valid strength (it's specific and factual) but is subsumed under the stronger "strong and consistent empirical improvements" strength above.

## Novel Insights

The most interesting observation across the reviews is the disconnect between the paper's motivational story (the induced-subgraph homophily distribution determines GNN performance) and the actual mechanism by which the method likely succeeds. A genuinely novel follow-up would be to disentangle the *label-diversity* benefit of subgraph selection (providing more contrasting labels in local neighborhoods) from the *homophily-distribution-matching* benefit claimed in the paper. The current analysis cannot distinguish these, and the latter may be a byproduct of the former. Additionally, the gap between the ℓ₁ Lewis weights theory (binary, linear, scalar loss) and the practical setting (multi-class, nonlinear, multi-layer) is large enough that connecting them would be a nontrivial theoretical contribution of its own.

## Suggestions

1. **Add a proper ablation study** that isolates: (a) METIS + random subgraph selection, (b) METIS + uniform sampling within partitions, (c) Jordan center vs. random center vs. mean-pooled representation, and (d) Lewis weights vs. uniform sampling. This is the single most impactful improvement for a camera-ready version.

2. **Honestly characterize the theoretical gap.** State clearly that Theorem 3.6 applies to a one-layer linear encoder with a scalar nice-hinge loss, and the extension to the experimental setting (multi-layer SAGE-Mean with ReLU, multi-class CE) is an empirical heuristic rather than a proven guarantee. If possible, prove the CE extension or run experiments that match the theory (e.g., a linear model with binary hinge loss).

3. **Qualify the "fail to outperform random" claim** in the abstract to match what the results actually show: e.g., "no prior GAL method consistently outperforms random sampling across heterophilic graphs."

4. **Add an experiment on homophilic graphs** (Cora, Citeseer, PubMed) to demonstrate that KyN does not harm performance when heterophily is absent.

5. **Address the Jordan center computational cost** by either providing an efficient approximation, bounding the worst-case subgraph size from the METIS parameters, or reporting per-component runtime breakdown.

6. **Clarify the reformulation** of multi-class CE as a nice hinge function, or remove the claim if it cannot be substantiated.

## Score and Decision

The paper tackles a well-motivated problem with a sensible method that achieves strong empirical results. However, the motivational analysis is imprecise, the theoretical guarantees do not cover the experimental setting, and the lack of ablation study makes it difficult to attribute the gains to specific design choices. These are significant but not fatal issues — the core empirical contribution is real and valuable. The paper would be strengthened substantially by addressing the major weaknesses, but in its current form the contribution is partially undermined by overclaimed framing and incomplete evaluation.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>