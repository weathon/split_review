Now I have a thorough understanding of the paper. Let me synthesize the final review.

## Summary

TreeX proposes a method for extracting global subgraph-level explanations from message-passing GNNs. The key insight is to leverage the existing message-passing computation: instead of explicitly enumerating subgraphs (combinatorial), it represents each node's L-hop rooted subtree by its L-th layer embedding, then clusters these embeddings to discover recurring subgraph concepts. The method operates in three phases: (1) local concept mining via clustering node embeddings within each graph, (2) global concept extraction by clustering local concepts across the dataset, and (3) class-rule generation via learning weights that predict class labels from concept counts.

## Strengths

1. **Reduction of subgraph search to tractable clustering.** The paper identifies that enumerating all subgraphs per graph is factorial, but every L-layer MPGNN naturally produces exactly N rooted L-hop subtrees (one per node). Replacing subgraph search with subtree clustering (§4.2) makes global-level graphical explanation feasible for the first time.

2. **Theoretical justification for using root node embeddings as subtree representations.** Theorem 4.2 and Definition 4.1 (§4.2) prove that for an injective MPGNN (e.g., GIN), the l-th layer node embedding is a perfect representation of the full l-hop rooted subtree. This justifies clustering directly in the GNN's embedding space without a separate subgraph encoder, and the connection to the 1-WL test is intellectually clean.

3. **Produces explicit graphical concepts rather than latent or language-based explanations.** Unlike GLGExplainer (latent prototypes) and GCNeuron (human-defined logical rules), TreeX outputs concrete subgraph motifs. The qualitative results (§5.2, Figure 3) are compelling: on BA-2Motifs it correctly recovers the 5-cycle and house motifs; on Mutagenicity it identifies -NO₂, -NH₂, and other known mutagenic/non-mutagenic chemical groups matching the biology literature.

4. **Bridges global and local explanation.** Unlike prior global methods that cannot explain individual instances, TreeX applies its global concepts to produce instance-level explanations (§4.3). The ability to both give dataset-level motifs and instance-level attributions in one unified framework is a genuine advance.

5. **Efficiency.** TreeX avoids NP-hard subgraph matching, with redundancy removal costing O(e n k) (§5.3). Table 4 shows it is orders of magnitude faster than SubgraphX and competitive with EiG-Search while additionally providing global concepts.

## Weaknesses

### Fatal
None.

### Major

1. **Global concept quality is only qualitatively validated.** The paper's central claim is producing "intuitive subgraph concepts as global explanations," yet the evaluation of these concepts rests entirely on hand-picked examples (Figure 3) and a literature-sanity-check on Mutagenicity (§5.2). On BA-2Motifs, where the ground-truth motifs (5-cycle, house) are known exactly, no quantitative metric — precision, recall, graph-edit distance, or coverage — is reported. A reviewer cannot certify the method's core output based on selected visualizations alone. The paper needs, at minimum, precision/recall of motif recovery on synthetic datasets with known ground truth.

2. **The local fidelity comparison mechanism is underspecified, raising fairness concerns.** The paper reports AccFidelity and ProbFidelity for TreeX alongside local baselines (Tables 1, 2), sometimes surpassing state-of-the-art methods. However, Section 4.3 describes the local explanation as a *weighted importance vector* I_t = K w_t, and Section 4.1 (Eq. 4) feeds the weighted concept embeddings directly to the classifier Ψ (bypassing message-passing layers). If this is how the fidelity prediction ŷ_i is computed — using a re-weighted embedding fed only to the classifier, rather than extracting a concrete subgraph from the input and running the full GNN — then the comparison is not on equal footing with local explainers. The paper never explicitly states how G_i^X (the "explanation" in the fidelity formula) is constructed as a concrete subgraph. This ambiguity undermines the main quantitative results in Tables 1 and 2.

### Minor

3. **No ablation studies isolating key design choices.** The method has several moving parts (local clustering within each graph, global clustering across graphs, isomorphism-based deduplication, learned class weights). There is no ablation — e.g., comparing against a version that uses random embeddings instead of learned ones, or skipping the deduplication step. This makes it hard to tell which components contribute what.

4. **Hyperparameter sensitivity not addressed.** The number of local clusters k and global clusters m are free parameters that could significantly affect results, yet the paper does not state how they are chosen or provide a sensitivity analysis. The regularization weight λ in the global rule loss (§4.1 Eq. 5) is also not discussed in terms of its selection or impact.

5. **Table 3 (incorrect prediction analysis) lacks a baseline comparison.** The metric — "rate of predicting the true labels using our extracted global explanations" on mispredicted instances — is presented without comparison to random-concept baselines or alternative methods. While the evaluation demonstrates something interesting, the harsh critic's point that this partially measures whether the optimization was successful is valid; a simple baseline (e.g., random weight assignment) would significantly strengthen the claim.

6. **The paper does not discuss limitations.** Aspects worth acknowledging include: (a) the approach depends on a well-trained GNN that produces meaningful embeddings, (b) clustering may produce duplicate or semantically similar concepts, (c) the extracted concepts are possibly disconnected motifs rather than a single coherent subgraph, and (d) the method is designed for MPGNNs with injective aggregation.

### Trivial
None.

## Nice-to-Haves
- A quantitative comparison against global-level methods on their own terms (e.g., measuring whether GLGExplainer's latent prototypes separate classes in embedding space, or whether GCNeuron's rules achieve predictive accuracy), while acknowledging that proper fidelity comparisons cannot be made since those methods lack local explanation algorithms.
- A discussion of whether the weighted-concept-embedding → classifier prediction (Eq. 4) is being used for fidelity or whether the subgraph mask from important concepts is fed through the full GNN. If it is the latter, please clarify.

## Removed Points

- **Criticism that the paper provides "no quantitative comparison against existing global-level methods."** This is acknowledged by the paper itself (§5, line 177: "since these existing global-level approaches do not offer algorithms for employing their extracted global explanations to the data instances in the test set, we do not access the explanation fidelity of them"). The criticism is valid as a general desire for more comparison, but it's not a specific flaw — the paper cannot compute fidelity for methods that do not offer instance-level explanations.

- **Criticism that "the standard deviation over 5 runs appears but the text does not explain how these runs vary."** While this would be nice to know, this is a minor presentation detail typical of conference papers. Not elevated to a weakness.

- **Criticism about time analysis not including global rule generation phase.** The paper states (§5.3) that the reported time includes the amortized cost: "For our method, we first obtain the global explanations... then apply [local]... and finally divide the total elapsed time by the number of instances." The critic may have missed this passage.

- **Strength about "bridging global and local explanation with competitive fidelity."** Tempered — the fidelity comparison mechanism is underspecified (see Major weakness 2), so the strength is conditional.

## Novel Insights

The recognition that the root node embeddings at layer L of an injective MPGNN are already perfect representations of the full L-hop rooted subtrees — and that this equivalence converts the combinatorial problem of subgraph-level concept mining into a clustering problem in the GNN's embedding space — is the core intellectual contribution. This is not a standard observation in the GNN explainability literature, which typically treats the GNN as a black box requiring auxiliary explanation models. The paper's structural insight that message-passing naturally decomposes a graph into |V| tree structures, and that clustering these structures yields meaningful semantic concepts, is genuinely novel.

Additionally, the paper's approach of then re-weighting these concepts per class via optimizing the original classifier's predictions on concept-count vectors is a clean way to bridge global and local explanation without post-hoc fitting.

## Suggestions

1. **Quantify global concept quality on synthetic data.** Report precision, recall, and F1 of extracted motifs against ground-truth motifs on BA-2Motifs and BAMultiShapes. This directly validates the paper's central claim.

2. **Clarify the local explanation mechanism.** State explicitly whether G_i^X in the fidelity computation is (a) a concrete subgraph of the original input extracted by selecting edges/nodes belonging to important concepts (fed through the full GNN), or (b) the weighted concept embedding fed only to the classifier Ψ. If (b), the fidelity comparison with local baselines should be acknowledged as measuring a different quantity and contextualized accordingly.

3. **Add a simple ablation.** Compare the full method against a variant where global concept embeddings are replaced with random vectors of the same dimension, to isolate the contribution of the clustering. If possible, also ablate the isomorphism deduplication step.

4. **Add a baseline to Table 3.** Compare the reported "rate of predicting true labels" against a random-weight baseline (shuffling w_t) to show that the learned weights specifically contribute to the correction.

5. **Report hyperparameter choices and sensitivity.** State k (local clusters) and m (global clusters) used in experiments, and briefly discuss sensitivity or how they were chosen (e.g., via a simple heuristic or grid search).

6. **Add a limitations paragraph.** A brief discussion of scope (reliance on injective MPGNNs, potential for duplicate concepts, disconnected motif outputs) would improve completeness and reproducibility.

## Score and Decision

The paper introduces a genuinely novel approach to a difficult problem (global graphical GNN explanations) with a well-motivated technical idea, theoretical grounding, and compelling qualitative evidence. The core methodological insight — replacing factorial subgraph enumeration with linear subtree clustering via node embeddings — is a real contribution. However, the evaluation has meaningful gaps: the central claim (global concept quality) is only qualitatively supported, and the fidelity comparison that serves as the main quantitative evidence has an underspecified mechanism that raises fairness questions.

These gaps are addressable but as presented, the evidence is incomplete relative to the strength of the claims. With the suggested additions (quantitative concept metrics on synthetic data, clarification of the fidelity mechanism, ablation studies), this could be a strong paper.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Reject</decision>