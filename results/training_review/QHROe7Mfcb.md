Now I have all the information I need. Let me synthesize the final review.

---

## Summary

This paper proposes a one-shot-subgraph link prediction framework for large-scale knowledge graphs. Instead of using the full KG for prediction, the method (1) extracts a single query-dependent subgraph using Personalized PageRank (PPR) as a non-parametric sampler, then (2) runs a deep GNN predictor on this small subgraph. The authors report state-of-the-art results on five benchmarks, showing that ~10% of entities per query suffice, and achieve 94%+ training time reduction over full-graph baselines. A bi-level optimization for configuration search and a theoretical analysis of extrapolation across graph scales are also presented.

## Strengths

- **Clear formalization of the decoupled sampling+prediction paradigm (Definition 1).** The paper explicitly distinguishes its approach from full-graph structural models, per-candidate-pair subgraph methods (GraIL, CoMPILE), and layer-wise coupled sampling. The three stated advantages (low complexity, flexible propagation scope, high sampling efficiency) are concrete and well-motivated.

- **Strong empirical results across five large-scale benchmarks with clear gains.** Tables 1/2 (in the paper) report leading performance on all datasets. The most striking result is a 16.6% relative improvement in Test MRR on OGBL-WIKIKG2 over the strongest baseline, using only ~10% of entities per query. This directly supports the paper's central thesis that full-graph inference is unnecessary.

- **Large and well-documented efficiency improvements.** Table 6 shows 94.3%/94.5% reduction in per-epoch training time for NBFNet and RED-GNN on YAGO3-10 when using the subgraph framework. Table 7 demonstrates that deep (8-layer) GNNs become feasible on large graphs where they would OOM on the full graph. These are concrete, practically meaningful gains.

- **Systematic ablation isolating the effect of the PPR sampler.** Table 5 compares PPR against four other heuristics (BFS, RW, etc.) across three datasets, with PPR consistently performing best. This empirically validates the choice of PPR and shows it is not replaceable by a simpler heuristic.

- **Informative analysis of sampling ratio vs. depth trade-offs.** Figure 4 (heatmaps) and Table 4 show that using too many entities degrades performance (noise), while deeper predictors consistently help on smaller subgraphs. This provides useful practical guidance.

## Weaknesses

### Fatal

None.

### Major

- **Baseline transparency is insufficient to support the "state-of-the-art" claim.** The paper does not specify the configuration (number of layers, training protocol, hyperparameters, number of epochs) used for baseline methods like NBFNet and RED-GNN in Tables 1/2. The specific numerical discrepancy alleged by one reviewer (e.g., NBFNet on YAGO3-10 reported at 0.447 MRR vs. the original paper's 0.552) cannot be verified from the text (tables are image-only), but the absence of any discussion about baseline setup is a genuine rigor gap. Without knowing whether baselines were run with comparable depth, training budget, and tuning, the headline claim of "6.9% average effectiveness improvement" is uninterpretable. This is the paper's most serious weakness.

- **The efficiency analysis does not isolate the cost of PPR computation.** The PPR step (Eqn. 2) iterates up to 100 times over the full graph's adjacency matrix, yet Tables 6 and 7 report only combined sampling+prediction time. On a graph with 2.5M entities (OGBL-WIKIKG2), full-graph PPR is not trivially cheap. The paper calls PPR "computation-efficient" but provides no runtime or memory breakdown for the PPR step itself, nor any comparison against faster PPR approximations (e.g., local push). Without this, the reader cannot assess whether full-graph PPR cost partially offsets the predictor-side savings.

- **The source of performance gains over full-graph baselines is not decomposed.** The method bundles (a) PPR subgraph selection, (b) deeper GNN architectures enabled by smaller subgraphs, and (c) relation-adaptive sampling ratios. Table 4 shows deeper layers improve results, and Table 5 isolates (a), but the headline results in Tables 1/2 compare a subgraph+deep-GNN system against full-graph baselines that may use shallower networks. The paper does not run a controlled comparison (e.g., same-depth NBFNet with vs. without subgraph sampling) to separate the effect of increased model capacity from the effect of better sampling. The contribution is partly architectural (deep GNNs) and partly data-centric (PPR subgraphs), and these are conflated.

### Minor

- **Theorem 1 is poorly integrated with the rest of the paper.** The theorem statement (Section 4.3) is dense with unspecified constants (C₁, C₂, ‖g‖_∞, d_min, L(M^train)) and the bound is not instantiated with the paper's data or architecture. The connection to Figure 4 (which shows performance across test-time sampling ratios) is asserted but not explained — Fig. 4 varies r_V^q at test time, while the theorem addresses training vs. test distribution shift. The theoretical content feels bolted on and does not guide the method's design choices or experimental setup.

- **The link between the bi-level optimization (Section 4.2) and the main experimental results is unclear.** The paper introduces a search procedure for relation-adaptive ratios (r_V^q, r_E^q), but the main experiments report using "10% of entities on average." It is not specified whether these ratios were obtained from the search or set as a fixed heuristic, nor are the searched per-relation ratios reported. A comparison of searched vs. fixed-ratio performance is missing.

- **Novelty is incremental beyond the specific combination.** The one-shot-subgraph paradigm's distinction from per-candidate-pair methods (GraIL, CoMPILE) is valid, and using PPR as a pre-prediction sampler is a reasonable engineering choice. However, the individual components — heuristic-based importance sampling and GNN-based prediction on a sampled subgraph — are established techniques. The paper's contribution is primarily empirical (demonstrating that 10% PPR subgraphs suffice) rather than conceptual. The framing as "a new paradigm" overstates the novelty.

- **Missing empirical comparison against learnable sampling methods.** The paper cites AdaProp and AStarNet as related work but does not benchmark against them. These are directly relevant competitors that also target KG scalability through learned sampling. The paper would be strengthened by including them (or explaining why they cannot be compared).

### Trivial

None.

## Nice-to-Haves

- **Isolate PPR computation cost** from the total pipeline — report per-query PPR time and its proportion of total inference time on the largest dataset. This would strengthen the efficiency claim.
- **Evaluate a local-push PPR approximation** that avoids full-graph power iteration, which would make the efficiency story more compelling.
- **Report coverage failure rate** — how often the true answer entity is not among the sampled entities (especially for long-distance queries), and how the predictor handles these cases.
- **Compare searched vs. fixed sampling ratios** to justify the complexity of the bi-level optimization procedure.
- **Discuss limitations** for queries where the answer is many hops away and PPR may fail to concentrate scores on the relevant entities. The current datasets may have answer entities that are generally close to the query entity.

## Removed Points

*These points were flagged for removal; treat them with caution.*

- **Abstract precision nitpicks** (94.4% and 6.9% not defined at point of use). These are standard abstract-level summary figures that reference Section 5 for specifics. Removed because they are presentation preferences, not weaknesses.
- **Criticism about "joint optimization" being just hyperparameter search.** The paper's bi-level optimization of data and model configuration is a valid (if limited) form of joint optimization. Removed because it oversimplifies the paper's contribution.
- **Complaint that deep predictor advantage conflates sampling and capacity.** The paper's point *is* that subgraph sampling enables deeper architectures — this is a feature, not a bug. The controlled comparison would strengthen the analysis, but the criticism as stated misunderstands the contribution.
- **Missing appendix/proof references.** Parser artifacts; these sections exist in the original submission. Removed per instructions.
- **Various typos, formatting complaints.** Parser artifacts, not author errors. Removed per instructions.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective or connection that the paper itself does not already articulate.

## Suggestions

1. **Disclose full baseline configurations** in the main paper or appendix: number of layers, embedding sizes, training epochs, hyperparameter ranges, and how these compare with the original published settings for NBFNet, RED-GNN, etc. If discrepancies from published numbers exist, explain them.
2. **Add a controlled decomposition experiment**: compare (a) full-graph NBFNet vs. subgraph NBFNet with the *same* depth, and (b) subgraph NBFNet with PPR vs. with random subgraph of the same size. This would isolate the effect of PPR sampling from the effect of deeper propagation.
3. **Report PPR computation time separately** from predictor time in the efficiency tables. Consider comparing against a local-push approximation to show the PPR step itself can be made efficient.
4. **Improve the integration of Theorem 1**: specify the constants for the paper's setting, explain how the bound connects to Figure 4's experimental design, and state which practical design decisions the theorem informs.
5. **Benchmark against learnable sampling methods** (AdaProp, AStarNet) or provide a clear justification for omission.
6. **Clarify the status of the bi-level optimization**: were the main results (Tables 1-2) obtained using the searched ratios or a fixed 10%? Report the searched ratios for representative relations.

## Score and Decision

**Originality:** 3/5 — the formalization is clear but the components are individually established.  
**Importance of research question:** 4/5 — scaling KG link prediction is a well-motivated, practically important problem.  
**Claims supported:** 2.5/5 — the SOTA claim is weakened by baseline transparency issues and the PPR cost is not isolated.  
**Soundness of experiments:** 3/5 — good ablations but the main comparison is muddied by confounded variables.  
**Clarity of writing:** 3.5/5 — clear motivation and method description; Theorem 1 is poorly explained.  
**Value to the community:** 3.5/5 — the empirical finding that 10% PPR subgraphs suffice is practically useful, but the contribution would be stronger with fairer baselines and decomposed analysis.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>