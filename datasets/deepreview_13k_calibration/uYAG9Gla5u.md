# Multigraph Message Passing with Bi-Directional Multi-Edge Aggregations

- Decision: Reject
- Avg Score: 4.50
- Scores: 3, 6, 6, 3

## Abstract
Graph Neural Networks (GNNs) have seen significant advances in recent years, yet their application to multigraphs, where parallel edges exist between the same pair of nodes, remains under-explored. Standard GNNs, designed for simple graphs, compute node representations by combining all connected edges at once, without distinguishing between edges from different neighbors. There are some GNN architectures proposed specifically for multigraphs, yet these architectures perform only node-level aggregation in their message passing layers, which limits their expressive power. Furthermore, these approaches either lack permutation equivariance when a strict total edge ordering is absent, or fail to preserve the topological structure of the multigraph. To address all these shortcomings, we propose MEGA-GNN, a unified framework for message passing on multigraphs that can effectively perform diverse graph learning tasks. Our approach introduces a two-stage aggregation process in the message passing layers: first, parallel edges are aggregated, followed by a node-level aggregation of messages from distinct neighbors. We show that MEGA-GNN is not only permutation equivariant but also universal given a strict total ordering on the edges. Experiments show that MEGA-GNN significantly outperforms state-of-the-art solutions by up to 13\% on Anti-Money Laundering datasets and is on par with their accuracy on real-world phishing classification datasets in terms of minority class F1 score.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper studies neural architecture for learning on multigraphs. Existing methods either reduce to simple graphs or break properties such as permutation equivariance. A two-stage message-passing framework is proposed by introducing artificial nodes for parallel edges that preserves several desirable properties. The proposed MEGA-GNN is evaluated on synthetic and real-world financial transaction datasets and shows better or comparable performance compared to SoTA methods.

### Strengths
- The use of two-stage aggregation and artificial nodes can effectively address the limitations of existing GNN models to capture information across parallel edges while preserving certain properties.

- The MEGA-GNN framework shows good flexibility and performance in applications on financial transaction datasets.

- The authors offer in-depth analysis and jusfiication for the proposed framework regarding properties of permutation equivariance, injectivity and universality.

### Weaknesses
 - The techniques used in MEGA-GNN such as bi-directional message passing and multi-stage aggregation are already well established, and the technical challenges for multi-graph have also been largely addressed by hypergraph learning research, which limits the overall novelty.

- The model is only evaluated on financial datasets, which raise questions about wheter multi-graph learning is applicabile for broad scenarios. 

- Some choices, such as specific aggregation functions and the role of artificial nodes, lack detailed justification.

### Questions
- Q1 In practice, is permutation equivariance indeed needed for multi-graph applications? Based on results from Tables 2 amd 3, Multi-GNN without this property is a very strong baseline, especially for the node classification task.

- Q2 What aggregation functions (EdgeAgg in Eqs 4, 8, AGG in Eqs 5,9) are used for the results reported in Tables 2 and 3?

- Q3 Could the authors include ablation studies to highlight the contribution of Ego-IDs? Comparsion with other baselines without node labelling seems unfair.

You, Jiaxuan, et al. "Identity-aware graph neural networks." AAAI'21

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces MEGA-GNN, a novel message-passing framework tailored for multigraphs—graphs that include multiple parallel edges between node pairs. Unlike standard GNNs that aggregate all edges at once, MEGA-GNN introduces a two-stage aggregation strategy: Parallel Edge Aggregation and Node-Level Aggregation. The authors demonstrate the permutation equivariance and invariance of the proposed model and show that it is universal when the edges are consistently ordered.

### Strengths
- The paper is clearly written and easy to follow with various figures demonstrating the ideas in the paper.
- Novel Aggregation Mechanism: The two-stage approach addresses the limitation of traditional GNNs, enhancing expressivity by first aggregating parallel edges and then aggregating at the node level.
- The paper provides proofs for permutation equivariance, injectivity, and universality.
- Experimental Evaluation: The proposed method shows promising improvements in the included datasets.
- The code is included in the supplementary material.

### Weaknesses
1- Scalability: Although multigraphs are well-suited to some applications, real-world graphs can be vast in scale. The two-stage aggregation with artificial nodes might pose computational challenges and memory overhead for large, densely connected multigraphs. Some discussion on scalability in practical settings or optimizations for large-scale data would be appreciated.

2- The paper shows that under a consistent ordering of edges the model is universal. However, for many real work scenarios, this is not always feasible, especially in dynamic setting. Have authors considered dynamically evolving multigraph setting?

3- The experiments are limited to financial datasets and lack diversity in application areas, which might constrain the broader applicability of MEGA-GNN. I am not familiar with the multi-graph learning literature but are there other domains you can explore?

### Questions
See weaknesses.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors introduce MEGA-GNN, a message-passing framework for multigraphs—graphs where multiple parallel edges can exist between the same pair of nodes. Traditional GNNs are not well-suited for multigraphs due to their single-stage node-level aggregation. 

MEGA-GNN addresses this limitation by implementing a two-stage aggregation process: first, it aggregates parallel edges between the same nodes, and then it performs node-level aggregation on the aggregated messages from distinct neighbors. The authors give theoretical proofs that MEGA-GNN supports permutation equivariance, injectivity, and universality under specifi conditions. 

Experimental results on synthetic and financial transaction datasets demonstrate that MEGA-GNN either outperforms or matches the accuracy of state-of-the-art models.

### Strengths
1. MEGA-GNN gives a solution to a gap of GNNs' effecitveness, by focusing on multigraphs rather than simple graphs, where multiple edges between nodes could be useful for many applications, such as financial fraud detection (as benchmarked in the paper).

2. The authors theoretically validate MEGA-GNN’s permutation equivariance, injectivity, and universality properties.

3. MEGA-GNN achieves state-of-the-art or comparable performance across various (synthetic and real-world0 datasets, particularly in edge and node classification tasks.

### Weaknesses
1. The proof for the universality property assumes that there is an ordering over the edges of the multigraph. This is not always the case for real-world setups, giving a small question-mark on what happens when the edge ordering is not consistent. Specifically, the theoretical guarantee relies on a fixed, pre-defined ordering of edges for the aggregation step, which may not be feasible or natural in many practical scenarios where edges are unordered or their ordering is dynamic. This raises concerns about the practical applicability of the universality result.

2. Although I find the utilization of financial transaction datasets quite interesting, I think it's not very diverse. I'd be very interested in seeing whether such a multigraph approach can be useful in other domains (e.g. knowledge graphs could potentially be of relevance due to the variety and number of different relations that can occur between identical pairs of nodes. For example, biomedical knwoeldge graphs could a potential use). The current evaluation is limited in scope, focusing primarily on financial transactions. This leaves open questions about the generalizability of MEGA-GNN to other graph-structured data, particularly those with different characteristics, such as varying edge densities or feature distributions.

3. The method requires the addition of artificial nodes, and the two-stage aggregation. This hints a computational overhead that is not discussed in the paper, and how it'd affect message passing in large/dense graphs. The introduction of artificial nodes and the two-stage aggregation process inherently increase the computational complexity compared to single-stage GNNs. The paper lacks a detailed analysis of the time and memory costs associated with these operations, especially when applied to large and dense multigraphs, which is a critical aspect for practical deployments.

### Questions
1. How does MEGA-GNN scale with larger, more complex multigraphs, and what are the computational costs with the two-stage aggregation process?

2. Is it possible to relax the assumption of consistent edge ordering, and if so, how would that impact the theoretic properties of MEGA-GNN?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a novel message-passing procedure on multigraphs. By first aggregating all edge states between two nodes, and using those as messages for MPNNs, a permutation equivariant method is constructed. The effectiveness of the proposed method is shown on several edge classification and one node classification task.

### Strengths
I like the proposed method. It is intuitive, simple and effective. The paper is nicely written and mostly easily to follow and sufficiently detailed described.

### Weaknesses
W1 Theorem 3.1: All MPNNs are permutation equivariant, as they do not use indices directly. I do not understand the need to specifically point this out.

W2 Corollary 3.1: This statement is false the way it is stated. First, you need f, g_v, and g_e to be injective as well. Lemma 5 of Xu et al. also only holds for functions over countable multisets, which is ignored in this statement. In fact, if you follow Lemma 5 of Xu et al., there needs to be an additional function that is applied before EdgeAgg for possible injectivity.

W3 Theorem 3.2: It should be clearly defined what the authors mean with universality. If a consistent ordering of the edges is given, permutation equivariance is lost. I find the claim that "our method is universal and capable of detecting any directed subgraph pattern in multigraphs" to be strongly misleading. How to construct a consistent ordering is not discussed and from my understanding not used for the experiments. Therefore, the point of this theoretical statement is unclear to me.

W4: Eq. 4 computes h^(l) but Eqs. 5,6 use h^(l-1). Is this intended?

W5: The introduced artificial nodes are not used in the proposed method. States are only computed for edges and nodes, but not for the artificial ones. Discarding the artificial nodes would make the framework much cleaner.

W6 Experiments: 
* The baseline results seem to be reused from previous methods. It is unclear whether the same dataset splits were used, the same number of parameters, and the same hyperparameter search space.
* There are no ablation studies. For example, to better understand this method it would be nice to see how results would change if there was a single edge state between two nodes instead of having multiple edge states.

### Questions
* l. 376: What does GIN aggregation mean? GIN uses sum aggregation + an MLP.
* MEGA-GNN seems to require a single vector of edge features, independently of the number of edges between two nodes. From my understanding all edge between two nodes would be equal if there are no initial edge features for each edge. This seems to a large constraint and it is not discussed in the experiments. Are these given for all datasets? Are baseline methods utilizing those as well?
* see weaknesses

### Soundness
2

### Presentation
2

### Contribution
2
