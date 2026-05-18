Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper studies active learning on heterophilic graphs, identifying that previous graph active learning (GAL) methods fail because they select isolated nodes, producing training sets with homophilic bias even on heterophilic graphs. The authors propose KyN, built on the "Know Your Neighbors" principle: partition the graph via METIS, select subgraphs using ℓ₁ Lewis weight sampling, and label all nodes within selected subgraphs. Empirical results across multiple heterophilic datasets show consistent improvements over prior GAL methods.

## Strengths

- **Diagnosis of the root cause of prior GAL failure on heterophilic graphs.** Section 3.1 and Figure 2 demonstrate that prior GAL methods produce training sets whose local homophily distribution is left-skewed (homophilic) on heterophilic graphs like Roman-empire. This insight — that previous methods select isolated nodes that appear artificially homophilic — is the paper's sharpest conceptual contribution and clearly motivates why a different approach is needed.

- **Strong and consistent empirical performance.** Table 1 shows KyN achieving the best or second-best accuracy on all six datasets across multiple budget levels. Improvements are substantive (e.g., +5.2% on Roman-empire, +6.1% on Tolokers, +6.0% on Minesweeper at budget 20C). These gains hold with heterophilic GNN backbones (Table 2) and scale to snap-patents (2M+ nodes, Table 3) where several baselines time out. The runtime comparison (Figure 4) also shows KyN is practically efficient.

- **Clear and well-motivated principle.** The "know your neighbors" idea — that correct local homophily estimation requires labeling nodes alongside their neighbors (Theorem 3.2) — is simple, intuitive, and directly addresses the diagnosed problem. This conceptual framing is the paper's strongest intellectual contribution and cleanly separates it from prior node-level GAL methods.

- **Scalability demonstration.** KyN runs successfully on snap-patents (>2M nodes) where FeatProp and GraphPart exceed 24-hour limits, showing the approach is not limited to small graphs.

## Weaknesses

### Fatal
None.

### Major

- **Theory-practice gap in the claimed "solid theoretical guarantee."** Theorem 3.6 proves a relative-error coreset for approximating the sum of *subgraph-level* cross-entropy losses under a one-layer linear GNN encoder, where each subgraph is treated as a data point. However, the paper's actual evaluation trains a multi-layer GNN for *node-level* classification on the full graph. The loss L(β) = −∑ln(p(y_i)|R_{G_i}, β) is over subgraph representations, not over individual nodes in the full graph. The paper equates this coreset with V_train ("the training set V_train in experiments," line 133), but V_train is the set of *all nodes in selected subgraphs*, used for a different task. The paper never explains why a coreset for subgraph classification should yield good training data for node-level classification. While the ℓ₁ Lewis weight sampling is a reasonable heuristic for subgraph selection, framing it as a "solid theoretical guarantee" for the actual node classification problem overstates what the theory supports. This does not invalidate the empirical results, but it means the theory section is ornamental to the paper's central claims rather than foundational.

### Minor

- **The "know your neighbors" principle is only partially realized.** METIS partitions cut edges: when a subgraph is selected, nodes inside it have neighbors in *other* subgraphs that remain unlabeled. The paper does not quantify the fraction of cross-partition neighbor relationships captured within selected subgraphs, nor does it analyze how much local homophily information is lost for nodes near partition boundaries. On heterophilic graphs, cross-partition edges connecting nodes of different classes could carry important signal. Figure 2 shows KyN's induced-subgraph homophily distribution matches the ground truth, but this ignores unlabeled cross-partition neighbors — the same limitation the paper critiques in prior GAL methods. A direct measurement of "what fraction of each labeled node's neighbors are actually labeled" would strengthen the connection between principle and implementation.

- **Missing ablation: no random-subgraph baseline.** KyN involves two design choices: (a) labeling entire subgraphs rather than isolated nodes, and (b) selecting which subgraphs via ℓ₁ Lewis weights. The paper compares against methods that label individual nodes, but never against a control that also labels subgraphs but selects them randomly (e.g., METIS partitions + random subgraph selection). Without this baseline, it is difficult to attribute KyN's improvements specifically to the Lewis weight sampling as opposed to the broader strategy of labeling contiguous node groups on heterophilic graphs. The paper mentions "More detailed component analysis" (line 259) which was likely in the appendix; if it addresses this concern, it should be brought into the main paper. If it does not, this is a gap worth filling.

- **The abstract overstates the failure of prior methods.** The abstract states categorically that "previous GAL methods fail to outperform the naive random sampling on heterophilic graphs." The paper's own more careful language (line 189, "fail to *consistently* outperform") is more accurate. On some datasets (e.g., Wisconsin, Texas), certain prior methods do outperform random at some budgets. This overstatement in the abstract is minor but unnecessary — the paper's case is strong enough without it.

### Trivial
None.

## Nice-to-Haves

- A random-subgraph selection baseline as described above would cleanly isolate the contribution of Lewis weight sampling.
- An analysis of cross-partition edge statistics would directly validate whether the "know your neighbors" principle is achieved in practice.
- The theoretical section could be reframed as providing a principled heuristic for subgraph selection rather than a "guarantee" for the full node classification task, or the theorem could be more honestly scoped.
- Connecting Theorem 3.2 (homophily estimation bound) more directly to the active learning objective would strengthen the theoretical narrative.

## Removed Points
These points were flagged by reviewers but are removed or downgraded for the following reasons:

- **Criticism that the theory is "largely ornamental" and that the coreset property "does not provide a principled justification":** Kept in spirit but downgraded from the reviewer's fatal framing to Major. The theory does justify the subgraph selection step, but the overclaim about its scope is real. The reviewer's stronger language about the theory being purely ornamental is removed; the theory still provides a principled sampling mechanism even if it doesn't cover the full training pipeline.
- **Criticism about Proposition 3.1 being "not obviously insightful":** Removed as a subjective judgment that doesn't identify a concrete flaw. The proposition is a valid formal statement linking local homophily correctness to accuracy.
- **Criticism that the paper should "build a more direct link between [Theorem 3.2] and the active learning objective":** Moved to Nice-to-Haves. This is a suggestion for strengthening a specific part of the paper, not a weakness in the existing contribution.
- **Strength Finder's claim about "novel algorithm with theoretical grounding":** Weakened due to conflict with the verified theory-practice gap weakness. The algorithm is novel; the theoretical grounding is partial and overclaimed.
- **Complaint about "the paper would need to either train a classifier on the subgraph representations directly or formally relate the subgraph-level coreset to the node-level generalization error":** Removed as an infeasible demand. The paper's empirical validation is sufficient for a systems/empirical contribution; refactoring the entire evaluation to match the toy theoretical setting is not a reasonable ask.

## Novel Insights

The reviews surface a recurring pattern in graph active learning papers: the temptation to present a coreset theory from one setting (subgraph classification) as a guarantee for a different setting (node-level training on the full graph). The reviewer insightfully notes that this gap is common and often goes unremarked. The paper's actual strength — the empirical demonstration that training set homophily distribution is a *controllable* property in active learning — is more interesting and less common than the coreset theory. A version of this paper that leaned harder on the diagnostic story (Section 3.1) and treated the Lewis weights as a practical instantiation rather than a theoretical foundation would be both more honest and more impactful.

## Suggestions

1. Add a random-subgraph selection baseline (METIS + random subgraph selection) to isolate the contribution of Lewis weight sampling. If even random subgraph selection outperforms node-level GAL methods, that still validates the "know your neighbors" principle — but the paper should then be clear about what the Lewis weights add.
2. Reframe the theoretical section honestly: state that ℓ₁ Lewis weights provide a principled way to select subgraphs by importance (with known guarantees for a simplified setting), rather than claiming a solid theoretical guarantee for the full node classification pipeline.
3. Add an empirical analysis of cross-partition neighbor coverage: for labeled nodes in selected subgraphs, what fraction of their 1-hop neighbors are also labeled? How does this affect the local homophily estimates the GNN actually sees during training?
4. Soften the abstract's claim about prior methods to match the paper's own more nuanced language ("fail to *consistently* outperform random sampling").
5. Bring the component analysis from the appendix into the main paper if it addresses the random-subgraph ablation.

## Score and Decision

The paper identifies a genuine problem and provides a well-motivated, empirically effective solution. The diagnostic analysis (Section 3.1) is insightful and the empirical results are strong across diverse heterophilic graphs. The primary weaknesses are: (1) the theoretical framing overclaims what the guarantees cover, and (2) the experimental design lacks a control that isolates the key design choice. These issues are addressable and do not undermine the paper's core empirical contribution.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>