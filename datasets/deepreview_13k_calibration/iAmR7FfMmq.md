# Improving Graph Neural Networks by Learning Continuous Edge Directions

- Decision: Accept
- Avg Score: 5.50
- Scores: 6, 3, 5, 8

## Abstract
Graph Neural Networks (GNNs) traditionally employ a message-passing mechanism that resembles diffusion over undirected graphs, which often leads to homogenization of node features and reduced discriminative power in tasks such as node classification. Our key insight for addressing this limitation is to assign fuzzy edge directions---that can vary continuously from node $i$ pointing to node $j$ to vice versa---to the edges of a graph so that features can preferentially flow in one direction between nodes to enable long-range information transmission across the graph. We also introduce a novel complex-valued Laplacian for directed graphs with fuzzy edges where the real and imaginary parts represent information flow in opposite directions. Using this Laplacian, we propose a general framework, called Continuous Edge Direction (CoED) GNN, for learning on graphs with fuzzy edges and prove its expressivity limits using a generalization of the Weisfeiler-Leman (WL) graph isomorphism test for directed graphs with fuzzy edges. Our architecture aggregates neighbor features scaled by the learned edge directions and processes the aggregated messages from in-neighbors and out-neighbors separately alongside the self-features of the nodes. Since continuous edge directions are differentiable, they can be learned jointly with the GNN weights via gradient-based optimization. CoED GNN is particularly well-suited for graph ensemble data where the graph structure remains fixed but multiple realizations of node features are available, such as in gene regulatory networks, web connectivity graphs, and power grids. We demonstrate through extensive experiments on both synthetic and real datasets that learning continuous edge directions significantly improves performance both for undirected and directed graphs compared with existing methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Traditional GNNs often suffer from feature oversmoothing due to their diffusion-like message-passing mechanism over undirected graphs. To address this, the authors propose the Continuous Edge Direction (CoED) GNN framework that assigns differentiable fuzzy edge directions to graph edges, allowing features to preferentially flow in one direction and introducing a complex-valued Laplacian for directed graphs with fuzzy edges.

### Strengths
The paper is well-written and offers an intriguing evaluation on graph ensemble data, where the graph structure remains fixed but multiple realizations of node features and targets exist—an important task that demands attention. Additionally, the authors demonstrate that their method is more expressive than the Magnet Laplacian.

### Weaknesses
1. The paper omits important baselines and related work, such as [3], which share similar concepts and should be included for a comprehensive comparison.
2. If the theorem is highlighted in the abstract and introduction, it should be mentioned explicitly in the main paper for consistency and emphasis.
3. The evaluation on node classification tasks is unconvincing:
   - Only one homophilous dataset is included in the study.
   - The Chameleon and Squirrel datasets used are known to be problematic [1], and it is advisable to use filtered versions for more reliable results.
   - The heterophilous datasets used for evaluation are all quite small, and the results do not approach the current state-of-the-art. To more robustly validate the claims, experiments on larger-scale heterophilous datasets [1][2] are necessary.

### Questions
1. What is the runtime of the proposed methods, and how does it compare to the baselines? Providing a detailed runtime analysis would enhance the evaluation.
2. For the node classification task, how does the performance change if the edge direction is made learnable? Prior work, such as [3], suggests that it will likely improve performance.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper presents a novel graph neural network architecture named Continuous Edge Direction (CoED) GNN, which improves upon traditional GNNs by introducing the concept of fuzzy edge directions. These directions allow for more effective feature propagation by varying continuously, enabling more controlled information flow between nodes. CoED GNN utilizes a complex-valued Laplacian that represents these fuzzy directions, where the real and imaginary parts correspond to opposite directions of information flow. The architecture is especially effective in graph ensemble settings, where the structure is static but node features vary, such as in gene regulatory networks and power grids.

### Strengths
1. The paper is well-written, and the motivation of the model is reasonable.
2. The idea of learning optimal edge directions, and using phase angles to scale the direction-aware information flow is intuitive and interesting.
3. Theoretical Analysis appears to be rigorous and formally describes the expressive power of the proposed model

### Weaknesses
1. Directed graph Laplacians have been extensively explored in previous studies, including seminal works like those by F. Chung [1] and on Hermitian Laplacian [2]. The introduction of the fuzzy graph Laplacian is a significant contribution of this work. However, while comparisons have been made with the magnetic Laplacian, it would be beneficial to extend these comparisons to include contemporary directed graph Laplacians, such as those derived from the normalized adjacency matrix or the random walk Laplacian, to fully contextualize its advancements and differences.

2. From my perspective, employing phase angles to dictate continuous edge directions is designed to adaptively modulate the weights from in-neighbors and out-neighbors. However, could we alternatively employ a shared learnable function $f$, , such as, $\mathrm{Sigmoid}(f(u_i, u_j))$ and $1- \mathrm{Sigmoid}(f(u_i, u_j))$ , to scale the information flow? This approach might offer a simpler alternative to using complex values. Furthermore, related work such as superGAT [3] enhances GAT by identifying important neighbors, a concept that could potentially be extended to directed graphs. By incorporating the separate message-passing strategy of DirGNN—which independently considers in-edges and out-edges—we could apply superGAT to each direction separately. Subsequently, the two representations could be combined to produce the final node representation. It's also worth exploring if the proposed method can be adapted to handle edge features, which are often present in real-world directed graphs.

3. While the concept of learning optimal edge directions is intriguing, I find the experimental results presented in the paper unconvincing. Firstly, as illustrated in Table 1, the CoED model achieves the best results in only one out of the five datasets examined. Secondly, the paper omits experiments on several pertinent datasets commonly used in related works, notably those employed by DirGNN, which is frequently referenced in this study. Specifically, there are no results included for datasets such as SNAP-PATENTS, ROMAN-EMPIRE, and ARXIV-YEAR, despite DirGNN reporting significant findings on these along with various other baselines. Incorporating these datasets could enhance the persuasiveness of the results. Thirdly, I view SAGE as a specific instantiation of DirGNN, implying that the performance of DirGNN should be at least as good, if not better, than that of SAGE. To enhance DirGNN's performance, particularly on the Texas and Wisconsin datasets, I experimented with incorporating an MLP layer following the final layer of DirGNN. This modification has significantly improved its performance. Additionally, the Texas and Wisconsin datasets are relatively small, and the Chameleon and Squirrel datasets reportedly contain significant amounts of duplicate data [4]. Therefore, I believe these datasets may not be the most suitable for evaluating the model's performance. The authors might consider using the AM-Photo, AM-Computer, or Citeseer datasets, as employed in [5], to provide a more robust assessment.

### Questions
See Weaknesses

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper leverages "fuzzy edges" to improve the flow of information across a graph. CoED GNN learns directions (coefficients) for each edge. This is achieved through a complex-valued fuzzy Laplacian. Experiments on both synthetic and real-world datasets demonstrate CoED GNN's good performance in node classification and regression tasks, attributed to its ability to optimize long-range feature propagation.

### Strengths
1. The fuzzy Laplacian enables CoED GNN to handle directional message passing, preserving the discriminative features over longer distances.
2. CoED GNN shows performance gains in diverse datasets, highlighting its adaptability to both synthetic and real-world applications.

### Weaknesses
1. The edge directions are essentially edge weights. GAT can also learn edge weights, and it even leverages node features while doing so, unlike CoED GNN. Since GAT utilizes more information, it should perform better. At the very least, the weights learned by GAT should not be worse than those learned by CoED GNN. It is puzzling that GAT performs worse than CoED GNN in the experimental results provided by the authors. The authors should provide theoretical provements to show that CoED GNN is superior. Furthermore, the mechanism by which CoED GNN's learned edge directions lead to better performance compared to GAT's learned edge weights needs more rigorous justification. The current explanation lacks a detailed analysis of how the complex-valued fuzzy Laplacian and the resulting edge directions specifically contribute to improved information flow, especially when GAT also learns edge weights based on node features.
2. The authors should explain why CoED GNN can alleviate the problem of homogenization of information across the graph. Also, the authors should  provide experimental validations. The explanation should include a discussion of how the complex-valued edge directions prevent the averaging of node features that leads to homogenization. It is not clear how the fuzzy Laplacian and its complex-valued edge directions directly address the oversmoothing problem. The authors need to provide a more detailed analysis of the spectral properties of the fuzzy Laplacian and how they differ from standard graph Laplacians in the context of information propagation.

### Questions
1. Could the authors provide theoretical analysis of the superiority of CoED GNN over GAT?
2. In Equation (1), why $(L_F)_{ij}=\text{exp}(i\theta_{ij})$? Is the first $i$ the imaginary unit? If so, the authors should use different letter to denote the $i$th node.
3. Could the authors provide explanation and experimental results to show that CoED GNN can alleviate the problem of homogenization of information across the graph?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a novel framework for undirected and directed graphs called Continuous Edge Direction (CoED) GNN, based on the insight to assign fuzzy edge directions in a novel complex-valued Laplacian matrix. The paper includes empirical comparison to various GNNs on both synthetic and real-world datasets, and theoretically shows the expressive power of CoED.

### Strengths
- The paper is generally well-written and well-motivated.
- The topics of expressive power, directed GNNs, and oversmoothing in GNNs are significant.
- The proposal of fuzzy edge directions is novel and effective.
- The statements are theoretically and empirically grounded.

### Weaknesses
 - No source code is provided.
- It would be better to show the runtime comparison explicitly, e.g. via a table, when comparing CoDE with MagNet etc.
- The paper uses the idea of separate aggregation of in- and out- information in addition to self. [1] does something similar and is based on flow imbalance in its objective. It would be better to add some discussion and comparison in experiments.
- In line 315, it is not clear where $\alpha$ should appear in the formula.
- Table 1 compares a CoED version without edge direction learning, how about with edge direction learning for node classification?
- (bonus) It would be better to show the ultimate directions (visualized) for some directed or undirected graphs to show more insights.

### Questions
- What is the runtime comparison explicitly, e.g. via a table, when comparing CoDE with MagNet etc.?
- The paper uses the idea of separate aggregation of in- and out- information in addition to self. [1] does something similar and is based on flow imbalance in its objective. How are they compared empirically?
- In line 315, where should $\alpha$ appear in the formula?
- Table 1 compares a CoED version without edge direction learning, how about with edge direction learning for node classification?

Reference:

[1] He, Y., Reinert, G., & Cucuringu, M. (2022, December). DIGRAC: digraph clustering based on flow imbalance. In Learning on Graphs Conference (pp. 21-1). PMLR.

### Soundness
3

### Presentation
3

### Contribution
3
