Now I have a thorough understanding of the paper and all reviewer claims. Let me produce the consolidated review.

## Summary

The paper introduces FedStruct, a subgraph federated learning framework that decouples graph structure from node features, enabling clients to share only structural information (not node features/embeddings) while training GNNs on interconnected subgraphs. The framework uses a decoupled GCN architecture and introduces Hop2Vec, a method for learning task-dependent node structure embeddings without requiring global graph knowledge. Experiments on six datasets show strong performance close to centralized training, particularly on heterophilic graphs where existing subgraph FL methods struggle.

## Strengths

1. **Privacy-preserving design relative to existing subgraph FL methods**: Unlike prior work (FedSage+, FedNI, FedCog, FedPub) that requires sharing or generating node features/embeddings among clients, FedStruct eliminates this need entirely, sharing only structural information (the local partition of the combined adjacency matrix). This is a genuine architectural innovation and a clear improvement over the status quo (abstract, lines 86-89, 95-96, 577).

2. **Strong empirical performance across challenging settings**: On six datasets with random partitioning and only 10% labeled nodes, FedStruct with Hop2Vec achieves accuracy within 2–3% of the centralized GNN on Cora, Pubmed, and Amazon Photo, and significantly outperforms baselines on the heterophilic Chameleon dataset (52.76% with 20 clients vs. 34.33% for FedSage+). Results are consistent across 10 independent runs (Table 1).

3. **First systematic handling of heterophilic graphs in subgraph FL**: The paper explicitly addresses the homophily assumption that limits existing methods. The decoupled GCN with learnable hop weights $\beta_l$ and non-local neighbor-extension provides a principled mechanism for handling heterophilic graphs, and this is validated on Chameleon (edge homophily ratio ~0.23) and Amazon Ratings (heterophilic) datasets (lines 101-102, Table 1).

4. **Theoretical grounding for local computation**: Propositions 1–3 rigorously show that training (forward pass and gradients) requires only the local partition $\boldsymbol{\Bar{A}}^{[i]}$ of the global combined adjacency matrix and the structure features $\bS$, not the full global adjacency. This formal analysis is a genuine contribution that supports the feasibility and privacy claims (lines 350-380).

5. **Lower online communication complexity**: FedStruct (without Hop2Vec) has online cost $\mathcal{O}(E \cdot K \cdot |\theta|)$, independent of $n$, whereas FedSage+ costs $\mathcal{O}(E \cdot K^2 \cdot |\theta| + E \cdot K \cdot n \cdot d)$. The pruning variant maintains this advantage while achieving near-original performance (Section 5.4, Table).

## Weaknesses

### Fatal
None.

### Major

1. **Unequal GNN architectures in empirical comparisons confound the reported advantages.** The paper's experimental setup (line 491) states: "For the GNN, we rely on GraphSage with two or three layers." However, FedStruct's fGNN is explicitly defined as a *decoupled* GCN (Eq. 10: $\bH_i^{(L)} = \BarA^{(i)} \boldsymbol{F}_{\btheta_{\msf}}(\bX_i)$), which is architecturally different from standard GraphSage used by baselines (FedSGD GNN, FedSage+, FedPub). Decoupled GCNs are known to handle heterophilic graphs better than standard coupled GNNs. The paper's reference to "DGCN performs similarly" (Table in appendix) addresses the *centralized* setting only and does not control for interaction effects in the federated setting. This means the substantial performance gap on Chameleon (52.76% vs. 34.33%) could be partly attributable to the decoupled architecture rather than the structural information sharing — the very mechanism the paper argues is responsible for the improvement. An ablation where FedStruct uses a standard (non-decoupled) GNN for the fGNN component, holding everything else equal, is needed to isolate the benefit of structural sharing from the benefit of the decoupled architecture.

2. **Hop2Vec's strong performance lacks robustness checks against overfitting.** Hop2Vec treats NSFs as $n \times d_s$ learnable parameters optimized jointly during training. With only 10% labeled nodes (as few as ~200–300 labeled examples on datasets like Cora or Citeseer), this adds a large number of free parameters that could memorize patterns in the small labeled set rather than capturing genuine structural dependencies. The paper demonstrates that Hop2Vec outperforms fixed NSFs (Degree, FedStar), but does not control for parameter count: Hop2Vec has far more degrees of freedom. While the consistent performance across 10 runs and the pruning variant's similar results partially mitigate this concern, the paper provides no training-vs-validation loss curves, no analysis of how performance varies with NSF dimensionality $d_s$, and no ablation with randomly initialized but frozen NSFs to test whether the learning step is the key driver. This undercuts the paper's narrative that Hop2Vec "captures deep structural dependencies" rather than benefiting from additional capacity.

### Minor

1. **Privacy claims are informally argued and lack a clear threat model.** The paper motivates FedStruct by the privacy risks of sharing node features/embeddings, and argues that structural information is "less sensitive" (line 88) and that $\boldsymbol{\Bar{A}}^{[i]}$ "cannot be used to uniquely determine the adjacency matrix of other clients" due to graph isomorphism (lines 383-385). However, this is a weak privacy notion: it does not preclude leaking information about node degrees, local subgraph density, or the existence of interconnections between clients — which in many applications (e.g., anti-money laundering, energy grids) is itself sensitive. The paper references an appendix on privacy (App.~\ref{app:privacy}) but provides no formal analysis (no differential privacy, no adversary model) in the main text. This does not invalidate the core contribution — the paper's design achievement is avoiding feature/embedding sharing, which is a real improvement — but the argument that structural information is inherently less sensitive is asserted without justification and would benefit from a more precise characterization.

2. **Key claim about label efficiency is not demonstrated in the main body.** The abstract and introduction claim strong performance "in scenarios with limited number of labeled training nodes" (line 101), and the paper states results for "varying levels of label availability" (line 480). However, the main results table (Table 1) shows only a single split (10% train, 10% val, 80% test). While additional label-rate ablations may exist in the appendix, the main paper body does not support this headline claim with any figure or table showing accuracy vs. label fraction. Readers cannot verify the robustness to label scarcity from the main results alone.

3. **The offline computation of $\boldsymbol{\Bar{A}}^{[i]}$ is deferred entirely to the appendix.** This computation is critical for both feasibility and privacy: clients must collaboratively compute their local partition of the global combined adjacency matrix without exposing the global graph. The paper mentions "In App.~\ref{app:schemes}, we provide an algorithm to obtain $\boldsymbol{\Bar{A}}^{[i]}$ before the training begins without gaining any additional information about the global graph" (line 382) but provides no sketch in the main text. A brief, self-contained description of how this is done (even a few sentences with a small example) would significantly strengthen the paper's credibility.

4. **No ablation on the number of hops $L$ or pruning parameter $p$.** The paper uses a decoupled GCN with $L$ hops for both fGNN and sGNN, and uses $p=30$ for the pruning variant. Neither $L$ nor $p$ is varied or justified; it is unclear how sensitive performance is to these hyperparameters. For heterophilic graphs, a large $L$ could be harmful without appropriate $\beta_l$ weighting, and different values of $p$ would affect the communication-privacy-accuracy tradeoff.

5. **No runtime/wall-clock comparison.** Communication complexity is analyzed theoretically, but the offline computation of $\boldsymbol{\Bar{A}}^{[i]}$ ($\mathcal{O}(L_s \cdot n^2)$) could be expensive in practice. A wall-clock comparison (even approximate) would help assess practical feasibility.

### Trivial
- The claim "first subgraph FL framework capable of handling heterophilic graphs" (line 102) is slightly overstrong: FedSage+ could in principle operate on heterophilic graphs (it just performs poorly). "First to explicitly address" or "first to demonstrate strong performance on" would be more precise.
- The communication complexity table includes only FedSage+ as a baseline; FedPub is also used in experiments but not included for completeness.

## Nice-to-Haves
- Provide accuracy vs. label fraction curves for at least one dataset in the main text to substantiate the label-efficiency claim.
- Include an ablation where Hop2Vec NSFs are randomly initialized and frozen (not updated during training) while keeping the decoupled GCN architecture, to isolate the benefit of learning NSFs from the benefit of added capacity.
- Show training vs. validation curves for Hop2Vec to check for overfitting.
- Add a brief sketch (2–3 sentences) in the main text of how $\boldsymbol{\Bar{A}}^{[i]}$ is computed collaboratively.

## Removed Points
- **Criticism that the paper provides "no formal privacy analysis" as a fatal flaw**: Removed because the paper's contribution is not a formal privacy framework — it is a method that avoids sharing features/embeddings, which is a genuine and verifiable privacy improvement. The paper notes it discusses privacy in the appendix. The critic's framing as a critical issue overstates its severity relative to the paper's actual claims.
- **Criticism about "missing appendix proofs" or "appendix stripped"**: Removed per instructions — parser artifacts should not be treated as author errors.
- **Criticism about "should include FedPub and FedCog in complexity table"**: Removed as a nice-to-have; the table focuses on the main comparison, and including all baselines is secondary.

## Novel Insights
The reviewers' critiques collectively highlight a recurring tension in subgraph FL papers: architectural innovation (decoupled GCN) is confounded with data-sharing innovation (structural information exchange). The paper would benefit from a cleaner experimental decomposition that isolates these two axes. Additionally, the privacy argument would be more persuasive if it precisely characterized the *information asymmetry* — what an adversary with access to structural information alone can infer compared to an adversary with access to feature information — rather than appealing to graph isomorphism, which is an overly broad guarantee.

## Suggestions
1. **Conduct architecture-controlled experiments**: Run FedStruct with a standard (coupled) GNN for fGNN to separate the benefit of structural sharing from the benefit of the decoupled architecture. Similarly, run the best baseline (e.g., FedSGD GNN) with a decoupled GCN to see if its performance on heterophilic graphs improves.
2. **Add a dedicated privacy discussion subsection** in the main text that clarifies: (a) exactly what information is shared ($\boldsymbol{\Bar{A}}^{[i]}$ rows and learned $\bS$), (b) what an adversary could potentially infer from each, and (c) why this is still an improvement over sharing node features.
3. **Include Hop2Vec overfitting analysis**: report training vs. validation loss, vary $d_s$, and add an ablation with frozen random NSFs.
4. **Include main-text results for varying label fractions** (at least one figure, e.g., for Cora and Chameleon) to support the label-efficiency claim.
5. **Add a brief main-text description** of how $\boldsymbol{\Bar{A}}^{[i]}$ is computed collaboratively offline.
6. **Vary $L$ and $p$** to show hyperparameter sensitivity.

## Score and Decision

This paper makes a solid contribution: a novel framework for subgraph FL that avoids sharing node features, with strong empirical results and theoretical grounding for local computation. The main weaknesses — the uncontrolled GNN architecture comparison and the insufficiently analyzed Hop2Vec overparameterization — are addressable in revision and do not invalidate the core contribution. The privacy motivation is slightly oversold but the design itself is genuinely privacy-improving relative to prior art.

**Score**: 6.5 (Marginally above the acceptance threshold; would be stronger with the suggested ablations and architecture-controlled experiments)

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>