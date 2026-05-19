- Decision: Reject
- Avg Score: 4.33
- Scores: 3, 5, 5
Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

This paper proposes NodeDup, a simple graph augmentation method that duplicates cold-start (low-degree) nodes and connects each original to its duplicate, then trains standard GNN-based link prediction models on the augmented graph. A lightweight variant, NodeDup-light, adds self-loop edges to cold nodes instead of full duplication. The method is evaluated on 7 benchmark datasets and shows strong improvements on isolated and low-degree nodes while maintaining or improving warm-node performance, with substantially lower computational overhead than prior augmentation baselines.

## Strengths

1. **Simplicity and motivation.** The core idea — duplicating underrepresented cold nodes to give them greater visibility during training — is well-motivated by the observation that cold nodes participate minimally in standard supervised LP training. The method requires no architectural modifications, making it easy to integrate into existing GNN pipelines.

2. **Strong reported gains on cold nodes.** The paper reports 38.49% relative improvement on isolated nodes and 13.34% on low-degree nodes averaged across 7 datasets (Table 1, verified in abstract and Section 5.2). These are large and consistent improvements over the base GSage model.

3. **Simultaneous warm-node preservation.** Unlike cold-start-specific baselines (TailGNN, ColdBrew) that degrade warm-node performance, NodeDup and NodeDup-light improve warm nodes by 6–8% on average. If robust, this directly addresses the trade-off framed as the paper's core research question.

4. **Efficiency advantage.** Figure 2 (labeled `fig:aug`) demonstrates that NodeDup requires orders of magnitude less preprocessing and training time than augmentation baselines like LAGNN, DropEdge, and TuneUP (e.g., 977× faster preprocessing than LAGNN on Citeseer). This is a concrete practical advantage.

5. **Principled ablation.** Figure 1 (`fig:ablation_method`) separates the aggregation effect (Step 2) and supervision effect (Step 3), showing that each contributes independently and their combination yields the largest gain. This provides clear evidence for the claimed dual mechanism.

6. **Plug-and-play versatility.** Tables 4–5 (`tab:ablation_encoder`, `tab:ablation_decoder`) show consistent improvements with different encoders (GAT, JKNet) and decoders (MLP), demonstrating generality beyond the default GSage+inner product setup.

## Weaknesses

### Fatal
None.

### Major

1. **Inference graph structure is not specified.** The paper describes training on the augmented graph G' = {V', E', X'} (line 68) but never states whether evaluation computes node representations using G' or the original graph G. This matters fundamentally: if duplicates are present during evaluation message passing, cold nodes gain an extra neighbor (their own duplicate) at test time that baselines do not have. The comparison would then conflate representation quality with an inference-time structural advantage. If duplicates are removed during evaluation, the paper must explain how node indexing and message passing are handled. This ambiguity is the single most important missing detail — it must be resolved for the contribution to be fairly evaluated.

2. **No variance or statistical significance is reported.** All results in Table 1, Table 2, Figures 1–3 are single numbers without standard deviations, error bars, or multiple-seed reporting. Given that improvements on warm nodes are in the single-digit percentage range (6–8%), and cold-start methods are known to be variable, the absence of any uncertainty quantification makes it impossible to assess which results are robust vs. driven by random seed variation. This is a standard expectation for empirical papers in this field.

### Minor

1. **Warm-node improvement mechanism is unexplained.** The paper's core narrative is that NodeDup avoids the cold-start trade-off, yet it shows warm-node improvements of 6–8% (Table 1). Since only *cold* nodes are duplicated, why warm nodes improve is not adequately addressed. The paper offers only a brief speculation in Section 5.2 ("the impact of node duplication on the original graph structure likely affects the performance of warm nodes") without analysis or a controlled experiment (e.g., comparing against random-node duplication to test whether any augmentation would produce the same effect). This weakens the central claim that the method specifically solves the trade-off.

2. **Inductive setting protocol is underspecified.** For the inductive experiments (Table 2, Section 5.4), the paper follows prior work where "new nodes appear after the training process" but does not specify whether duplicates are created on the fly for these new cold nodes at test time. If duplicates cannot be created for unseen test nodes, the method's applicability in inductive cold-start settings is unclear.

3. **Improvement percentages are ambiguous.** The paper reports "38.49% improvement" without consistently specifying whether these are relative or absolute improvements against the base model. The context strongly suggests relative improvement (absolute Hits@10 would be implausible), but this should be stated explicitly in all results sections.

### Trivial
- The improvement percentages in the abstract (38.49%, 13.34%, 6.76%) could benefit from explicit grounding against the specific baseline (GSage).

## Nice-to-Haves
- An ablation varying the number of duplicates per cold node (k > 1) would help determine whether gains saturate and whether the primary mechanism is supervision or aggregation.
- Reporting MRR alongside Hits@10 in the main body (currently deferred to appendix) would strengthen the evidence, as MRR may better capture cold-node benefit at lower ranks.

## Removed Points
- *Time complexity assumptions (R ≤ 2, shallow GNNs).* The paper explicitly states these as experimental conditions, not general assumptions (line 71). Removed because the paper addresses this.
- *Self-distillation section is unnecessary.* This is a subjective judgment about space allocation, not a technical weakness. Removed.
- *Dataset splits vary without justification.* The paper states the split ratios per dataset (Section 4.1); varying splits for differently-sized datasets is standard practice. Removed.
- *Related work placed after experiments.* This is a formatting preference with no effect on scientific validity. Removed.
- *Multi-view explanation insufficient for low-degree nodes.* The paper's analysis (Section 3.2) explicitly states the mechanism applies to both isolated and low-degree nodes, just more dramatically for isolated ones. The criticism overstates the gap. Demoted to observation; not a retained weakness.
- *Missing memory cost discussion.* This is a minor implementation detail that does not threaten the core claims. Removed as a nitpick.
- *Baseline descriptions too brief (TailGNN/ColdBrew adaptation details).* Given page limits, this level of detail is standard for the conference format. Removed.

## Novel Insights
None beyond the paper's own contributions. The node duplication idea is itself the novelty, and the reviews surface no surprising reinterpretation of it.

## Suggestions
1. **Clarify the inference graph.** State explicitly in Section 3.1 what graph is used during evaluation. If evaluation uses the original graph (without duplicates), explain how forward passes handle node indexing for the GNN layers. If evaluation uses the augmented graph, add a controlled experiment where NodeDup is evaluated on the original graph and report the difference — this would isolate whether the gains come from better learned representations or from structural test-time advantage.
2. **Add multiple-seed results.** Report means and standard deviations over at least 3–5 random seeds for the main results (Table 1, Table 2, ablation study). This is especially important for isolated-node results (where counts are small) and warm-node results (where improvements are modest).
3. **Explain or control for warm-node improvement.** Add a small experiment comparing NodeDup against random-node duplication (duplicating random nodes instead of cold nodes). If warm nodes also improve with random duplication, the effect is a general regularizer; if not, the cold-node specificity matters. Either outcome would strengthen the paper's narrative.
4. **Specify inductive protocol.** Clarify whether duplicates are created for unseen test nodes in the inductive setting, and if not, discuss the limitation.
