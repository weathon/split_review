Now I have a complete picture of the paper and all the reviewer claims. Let me produce the final consolidated review.

---

## Summary

This paper proposes FedStruct, a subgraph federated learning framework that decouples node features from graph structure. The key idea is to share only structural information (rows of a combined adjacency matrix and node structure features) between clients rather than node features or embeddings, thereby avoiding the leakage of sensitive node attributes. The paper introduces Hop2Vec, a learnable task-dependent node structure embedding method, and uses a decoupled GCN to enable local computation of structure embeddings without sharing the global graph topology. Experiments on six datasets show FedStruct with Hop2Vec achieving accuracy within 2–3% of centralized GNNs and substantially outperforming prior subgraph FL methods, especially on heterophilic graphs.

## Strengths

- **Novel and clean decoupling of structure from features in subgraph FL.** The paper provides a principled framework (Propositions 3–5) showing that training requires only each client's local partition of the combined adjacency matrix $\boldsymbol{\Bar{A}}^{[i]}$ and node structure features $\mathbf{S}$, not node features or embeddings. This is a genuine algorithmic advance over prior methods (FedSage+, FedCog) that share or generate sensitive feature information.

- **Strong empirical performance across diverse settings.** On Cora (10 clients), FedStruct+H2V achieves 80.28% vs. central 82.06%; on Chameleon (20 clients), 52.76% vs. 34.33% for FedSage+; on Amazon Photo (10 clients), 91.83% vs. 90.74% for FedSGD GNN. Performance remains close to centralized across six datasets, multiple client counts, and (per the appendix) different partitionings.

- **First subgraph FL method with demonstrated effectiveness on heterophilic graphs.** Prior subgraph FL methods (FedSage+, FedCog) operate under a homophily assumption. FedStruct achieves strong results on Chameleon (edge homophily ~0.23) and Amazon Ratings (~0.13), where FedSage+ degrades significantly. The decoupled GCN with multi-hop aggregation and adjustable $\beta_l$ coefficients provides a structural basis for this capability.

- **Low online communication complexity.** The base FedStruct variant has online complexity $\mathcal{O}(E\cdot K\cdot|\theta|)$, independent of $n$, compared to $\mathcal{O}(E\cdot K^2\cdot|\theta| + E\cdot K\cdot n\cdot d)$ for FedSage+. The pruned variant reduces offline complexity from $\mathcal{O}(n^2)$ to $\mathcal{O}(p n)$ with $p=30$ while maintaining nearly the same accuracy.

- **Hop2Vec learns task-dependent structure embeddings without global graph knowledge.** Unlike Node2Vec or GDV, Hop2Vec requires no prior knowledge of the $L$-hop neighborhood and adapts to the task via gradient descent. It consistently outperforms task-agnostic NSFs (degree, FedStar) in Table 1.

## Weaknesses

### Fatal

None.

### Major

1. **Privacy claim is asserted rather than rigorously analyzed.** The paper's central privacy advantage is that FedStruct avoids sharing node features/embeddings. However, the information that *is* shared — each client's local rows of the $L$-hop combined adjacency matrix $\boldsymbol{\Bar{A}}^{[i]}$ and the node structure features $\mathbf{S}$ — can itself encode sensitive information. The paper's only defense (lines 383–385) is that "due to graph isomorphism, $\boldsymbol{\Bar{A}}^{[i]}$ cannot be used to uniquely determine the adjacency matrix of other clients." This misses the point: the relevant threat is *partial information leakage*, not unique reconstruction. In anti-money laundering, energy grid, or supply chain settings (the paper's own motivating examples), even walk-count aggregates between a client's nodes and nodes in other institutions could reveal confidential business relationships. The paper offers no analysis of what an adversary can infer from $\boldsymbol{\Bar{A}}^{[i]}$ or $\mathbf{S}$ (especially Hop2Vec's learned NSFs, which may encode label-correlated information). Without this analysis, the paper's framing as a privacy-preserving method is a claim rather than a demonstrated property. The appendix reference (App.~\ref{app:privacy}) is acknowledged but the main text should at minimum scope the privacy guarantee honestly.

2. **Offline computational cost is acknowledged but not adequately characterized.** The paper reports $\mathcal{O}(L_s n^2)$ offline complexity and notes this "may be impractical for large networks" (line 448). The pruning method reduces this to $\mathcal{O}(L_s p n)$, but the paper only evaluates $p=30$ and does not study how accuracy degrades with smaller $p$, how $p$ should be chosen relative to $n$, or what the concrete wall-clock cost of computing $\boldsymbol{\Bar{A}}^{[i]}$ is for the largest datasets used (e.g., Pubmed or Amazon Ratings). For a real-world graph with $n=10^6$, $\mathcal{O}(n^2)$ is prohibitive, and it is unclear whether the pruning computation itself requires global graph knowledge. The paper would be stronger with a clear characterization of the regime (graph size, sparsity, $p$) where FedStruct is practical.

### Minor

1. **Anomalous baseline results not discussed.** On Pubmed with 5 clients, FedSage+ (85.89%) outperforms *FedSage+ ideal* (85.40%), which uses true missing-neighbor features and should strictly dominate. The same pattern appears for Pubmed 20 clients (85.14% vs. 85.10%). While these differences are within standard deviations, the direction is unexpected and the paper does not comment on it. This raises mild concern about whether the baseline implementation or hyperparameter tuning is fair. The paper should at minimum acknowledge this.

2. **Heterophily handling mechanism underspecified in the main text.** The paper claims to be the first subgraph FL framework capable of handling heterophilic graphs, citing "non-local neighbor-extension and inter-layer combination" and the ability to adjust/learn $\beta_l$ coefficients. However, it never states what $\beta_l$ values were used in the experiments, whether they were learned or fixed, or how they were chosen for each dataset. Given that this is a first-to-claim novelty, the main text should provide explicit evidence (e.g., an ablation with different $\beta_l$ choices or a comparison on datasets with varying homophily ratios) rather than deferring entirely to the appendix.

3. **Main experiments use GraphSAGE backbone rather than decoupled GCN.** Since the theoretical development of FedStruct fundamentally relies on the decoupled GCN (Eqs. 2–4, Propositions 1–3), the choice of GraphSAGE for the GNN backbone creates a disconnect between theory and the primary experiments. The paper states DGCN "performs similarly" (line 491) and references an appendix table, but a head-to-head comparison in the main text would strengthen the connection between the theoretical framework and empirical validation.

### Trivial

None.

## Nice-to-Haves

- A differential privacy discussion or baseline. Given the paper's privacy emphasis, the paper should at least acknowledge that DP can be applied to any shared information and discuss how FedStruct's structural information interacts with DP mechanisms.
- Results with varying label rates in the main text (currently in appendix).
- A study of how performance varies with the pruning parameter $p$.
- A clearer distinction in Table 1 that "FedSGD GNN" uses gradient averaging (FedSGD) rather than model averaging (FedAvg), and a note that FedAvg results are in the appendix.

## Removed Points

- **"The method for collaboratively computing $\boldsymbol{\Bar{A}}^{[i]}$ before training is described in the appendix, which is not available"** — This is a complaint about missing appendix content. The parser strips appendix sections from all papers; they exist in the original submission. Removed per hard rules.
- **"Results with varying label rates are promised in the appendix but are not available for this review"** — Same as above. Removed per hard rules.
- **"FedSage+ ideal never reaches within 1% of centralized performance" on Amazon Ratings** — Factually incorrect for the 5-client case (40.44% vs. 41.32% = 0.88pp difference, within 1pp). Removed this specific claim, though the more general observation about FedSage+ ideal not reaching centralized performance on Amazon Ratings is retained as context.
- **"Missing appendix, missing proofs in appendix, or absent references"** — All such criticisms removed per hard rules; proofs and appendices are stripped by the parser and exist in the original submission.

## Novel Insights

The most interesting tension revealed by this set of reviews is between the paper's clean theoretical framework (which elegantly shows that decoupled GCN training requires only structural aggregates, not features) and the practical privacy implications of those very aggregates. The graph-isomorphism defense (uniqueness is impossible) is formally correct but pragmatically weak — a pattern common in graph privacy work where worst-case guarantees (perfect reconstruction) are confused with meaningful privacy (partial attribute inference). This suggests a broader community need for a formal threat model in subgraph FL that specifies what "privacy" means when the shared information is structural rather than feature-based. The paper's technical contribution (decoupling) is solid regardless; the privacy framing simply needs to match the actual protection level.

## Suggestions

- **(Required for privacy claim to be credible)** Add a dedicated subsection analyzing what information $\boldsymbol{\Bar{A}}^{[i]}$ and $\mathbf{S}$ (especially Hop2Vec's learned NSFs) leak about other clients' subgraphs. Compare the leakage channel to what prior methods leak via shared features. Be explicit about the threat model (honest-but-curious server? malicious clients?) and scope the privacy advantage as *relative reduction* rather than an absolute property.
- **(Recommended)** Report the $\beta_l$ values used in experiments or clearly state whether they were learned. Add a small ablation showing performance on a heterophilic dataset with different $\beta_l$ choices.
- **(Recommended)** Acknowledge and explain the anomalous FedSage+ ideal results on Pubmed (e.g., "within standard deviations, the ideal variant performs similarly or better on most datasets, but on Pubmed the noise in the 10-run average occasionally reverses the expected ordering").
- **(Nice-to-have)** Add a table showing accuracy vs. pruning parameter $p$ for at least one dataset, to characterize the trade-off concretely.
- **(Nice-to-have)** Add a sentence explaining that the baseline "FedSGD GNN" uses gradient averaging (as opposed to FedAvg, which is studied in the appendix).

## Score and Decision

The paper presents a genuinely novel algorithmic contribution — decoupling structure from features in subgraph FL — with strong and thorough empirical validation. The theoretical development is sound, and the empirical results convincingly show that FedStruct+Hop2Vec approaches centralized performance and significantly outperforms prior methods on heterophilic graphs. The low online communication complexity is a practical advantage.

However, the paper's framing overstates its privacy contribution. The central claim of "privacy-preserving" learning is incomplete without an analysis of what the shared structural information reveals. This is not a fatal flaw (the algorithmic contribution stands on its own, the paper refers to a privacy appendix, and the claim is qualified as "less sensitive" rather than "non-sensitive") but it is a significant gap that prevents the paper from fully delivering on its stated selling point. The offline $\mathcal{O}(n^2)$ cost is a practical concern that is only partially addressed.

With a strengthened privacy discussion (even a brief one in the main text) and acknowledgment of the anomalous baseline points, the paper would be a solid contribution. In its current form, the paper's strengths substantially outweigh its weaknesses.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>