Now I have a complete picture. Let me produce the final consolidated review.

---

## Summary

TreeX proposes a framework for generating global, graphical (subgraph-level) explanations of Message-Passing GNNs. The key insight is to mine over *subtrees* induced by the message-passing process rather than enumerating all possible subgraphs, reducing the search space per graph from $O(N!)$ to $O(N)$. Theorem 4.2 establishes that for a maximally powerful MPGNN with injective AGG and UPDATE functions, the $L$-th layer root node embedding is a Perfect Rooted Tree Representation of the full $L$-hop subtree, enabling reuse of existing embeddings without additional subgraph encoding. Global concepts are extracted by clustering these subtree embeddings and then fitting class-specific weights to produce graphical explanations (e.g., "–NO₂" on Mutagenicity) that can also be applied to individual instances for local explanation.

## Strengths

- **Formal search-space reduction from exponential to linear.** The paper establishes that each $N$-node graph has exactly $N$ full $L$-hop subtrees (vs. up to $N!$ possible subgraphs), making global subgraph concept mining tractable. This is a concrete algorithmic innovation substantiated in Section 4.2.

- **Theoretical grounding via Theorem 4.2.** The proof that a maximally powerful MPGNN's last-layer node embedding is a Perfect Rooted Tree Representation of its corresponding full $L$-hop subtree is clean and directly supports the method's efficiency (no separate subgraph encoding needed). This distinguishes TreeX from prior work that requires auxiliary subgraph-feature computation.

- **Produces intuitive graphical global explanations.** Unlike GLGExplainer (which outputs latent prototype embeddings) or GCNeuron (human-defined language rules), TreeX directly outputs recognizable subgraph motifs (e.g., five-node cycles, "house" motifs, "–NO₂"/"–NH₂" chemical groups on Mutagenicity). This visual clarity is a genuine advantage for interpretability (Figure 3).

- **Class-specific reweighting enables diagnosis of incorrect predictions.** Table 3 shows that for most misclassified instances, reweighting the global concepts can predict the true class, providing actionable debugging insights not offered by existing global explainers.

- **Efficiency competitive with local explainers while producing global concepts.** Table 4 shows per-instance time (0.01–0.26s) comparable to EiG-Search and orders of magnitude faster than SubgraphX, despite TreeX simultaneously producing dataset-level subgraph concepts.

## Weaknesses

### Major

1. **Ambiguity about whether test data is used during concept extraction and rule generation (data leakage risk).** The method description (Section 4.1) says "across the entire dataset $\mathcal{D}$" for local concept mining and global concept extraction, and optimizes weights $\mathbf{w}_t$ (Phase 3) that are later used to compute fidelity on test instances. The paper never states that a train/test split is applied before these phases, nor clarifies whether $\mathcal{D}$ refers to the training set only. If test instances contributed to concept extraction or weight optimization, the reported fidelity numbers (Tables 1 and 2) would be invalid because the evaluation data leaked into the explanation construction. *Why this matters:* this is not a minor clarity issue — it directly affects the believability of the paper's main quantitative claims. The authors must confirm that only training data was used for all three phases of TreeX and describe how the learned concepts/rules are applied to held-out test instances.

2. **Conversion of global-rule importance weights to explanation subgraphs for fidelity computation is underspecified.** To compute AccFidelity and ProbFidelity, one must feed a concrete *explanation subgraph* $G_i^{\mathcal{X}}$ into the GNN. Section 4.3 describes producing an importance vector $I_t = K\mathbf{w}_t$ but never explains how this vector is mapped to a specific subgraph that can be masked from the input. Is it the union of all global concepts with positive weight? Only the top-weighted concept? How are overlapping edges resolved? Without this specification, the fidelity numbers in Tables 1 and 2 cannot be independently reproduced, and the comparison with local baselines (which produce explicit subgraphs) is not on equal footing. *Why this matters:* this makes the central quantitative result uninterpretable as reported.

### Minor

3. **Hyperparameter values $(k, m)$ and their selection are not reported.** The method depends on $k$ (local clusters per graph) and $m$ (initial global clusters before merging), yet the paper states neither the values used for each dataset nor how they were chosen. Clustering is central to the pipeline; its sensitivity to these parameters should be discussed or stability demonstrated. This is a standard reproducibility requirement.

4. **GNN architecture used in experiments is not specified.** The paper says it "focuses on explaining the maximally powerful MPGNNs" and cites GIN as an example (Eq. 2), but the experiments section never states whether GIN is actually used, how many layers, what hidden dimensions, what training procedure, or what data splits were used to train it. These details are needed to verify that the theoretical condition (injective AGG and UPDATE) is met and to enable reproduction.

5. **L2 penalty does not align with stated sparsity intuition.** The paper writes that the L2 penalty encourages "critical concepts to occupy only a minor portion of the dataset embedding." L2 regularization shrinks weights toward zero but does not produce sparsity (weights are rarely driven to exactly zero). If the intention is to identify a compact set of critical concepts, L1 or elastic-net regularization would be more appropriate. This mismatch between intuition and the actual loss function should be clarified or corrected.

### Trivial

- None that survive filtering — the remaining presentation issues are typical of a camera-ready revision and do not warrant listing.

## Nice-to-Haves

- An ablation replacing subtree embeddings with direct subgraph encoding would strengthen the claim that the subtree reduction is both necessary and effective.
- A stability analysis of the learned global concepts across random seeds (qualitatively, not just fidelity variance) would deepen trust in the extracted motifs.
- Reporting the train vs. test fidelity for the learned global weights would help assess whether the weight optimization overfits, especially given the L2 penalty's limited sparsification.

## Removed Points

- *"Qualitative comparison with GLGExplainer and GCNeuron is thin"* — The paper states additional comparisons on BAMultiShapes and NCI1 are in the appendix (which is parser-stripped, not absent). The main text shows one representative figure, which is standard for space-limited submissions. Removed per rule about missing appendix content.
- *"L2 penalty does not encourage sparsity"* as a standalone criticism — Kept but downgraded to Minor, since the core issue is a mismatch between the stated intuition and the actual regularization, not a factual error about L2's behavior.
- *"The paper should also cover X / Y / Z additional tasks/datasets"* — Not present in the original reviews; no action needed.
- *Generic requests for more runs / larger studies* — Not present in a way that violates feasibility rules.

## Novel Insights

The most interesting tension exposed by the reviews is between the paper's clean theoretical framing (subtree isomorphism via node embeddings, search-space reduction, class-specific reweighting) and the underspecified evaluation pipeline. TreeX's core innovation — exploiting the correspondence between MPGNN message-passing subtrees and subgraph concepts — is genuinely novel among existing GNN explainability work. However, the reviewers correctly identify that the bridge from this theoretical insight to verifiable empirical claims has gaps: the data used for concept extraction is not declared, the subgraph-construction rule for fidelity is not defined, and the clustering hyperparameters are not reported. These are solvable problems (clarification, not fundamental invalidation), but they are nontrivial: a reader cannot currently tell whether the reported fidelity numbers measure faithful explanations or leakage-inflated artifacts.

## Suggestions

1. **Explicitly state in Section 4.1** that $\mathcal{D}$ refers to the *training set only* for all phases (local mining, global clustering, and weight optimization). Describe the exact split ratio and how the global rules are applied to test instances.
2. **Add a paragraph or algorithmic step in Section 4.3** detailing how $I_t = K\mathbf{w}_t$ is converted to the explanation subgraph $G_i^{\mathcal{X}}$ for fidelity computation. E.g., "we take the union of all global concepts whose weight in $\mathbf{w}_t$ exceeds a threshold $>0$" or "we select the top-$r$ concepts by absolute weight."
3. **Report the values of $k$ and $m$** used for each dataset in a table or appendix, along with a brief justification or a reference to a validation criterion.
4. **Specify the GNN architecture** (GIN, number of layers $L$, hidden dimensions, optimizer, epochs) and the data splits used for training it, ideally in a reproducibility statement.
5. **Clarify the L2 regularization motivation** — if sparsity is not actually required for the method to work, rephrase the intuition; if sparsity is desired, switch to L1 or elastic net.

## Score and Decision

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>