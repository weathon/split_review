# Bonsai: Gradient-free Graph Distillation for Node Classification

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
\vspace{-0.1in}
Graph distillation has emerged as a promising avenue to enable scalable training of \gnns by compressing the training dataset while preserving essential graph characteristics. Our study uncovers significant shortcomings in current graph distillation techniques. First, the majority of the algorithms paradoxically require training on the full dataset to perform distillation. Second, due to their gradient-emulating approach, these methods require fresh distillation for any change in hyperparameters or \gnn architecture, limiting their flexibility and reusability. Finally, they fail to achieve substantial size reduction due to synthesizing fully-connected, edge-weighted graphs. To address these challenges, we present \name, a novel graph distillation method empowered by the observation that \textit{computation trees} form the fundamental processing units of message-passing \gnns. \name distills datasets by encoding a careful selection of \textit{exemplar} trees that maximize the representation of all computation trees in the training set. This unique approach imparts \name as the first linear-time, model-agnostic graph distillation algorithm for node classification that outperforms existing baselines across $6$ real-world datasets on accuracy, while being $22$ times faster on average. \name is grounded in rigorous mathematical guarantees on the adopted approximation strategies making it robust to \gnn architectures, datasets, and parameters. \looseness=-1

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a novel graph distillation method empowered by the observation that computation trees form the fundamental processing units of message-passing GNNs. This paper specifically addresses the issue of overly dense edges in graph distillation. Experiments on various datasets verify the effectiveness of the method.

### Strengths
1. Compared to previous works, BONSAI is novel.
2. The experimental results look very good, especially regarding the training time.
3. The theoretical analysis is solid.

### Weaknesses
1. This paper is not easy to understand.
2. In some cases, BONSAI does not perform the best, such as with citeseer.
3. Regarding table 5, can you provide experimental results for other compression rates?
4. PPR and RkNN involve many parameters, and the ablation study in Fig. 4(b) is insufficient.

### Questions
See weakness

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies critical limitations in existing graph distillation methods. It introduces a new approach that optimizes the training of GNNs by generating smaller, representative datasets without requiring full training on the original data. The proposed method leverages a computation tree-based approach to create a distilled representation that is efficient, adaptable, and capable of maintaining high accuracy across varied datasets and models. Experimental results have demonstrated its effectiveness and efficiency.

### Strengths
1. The proposed gradient-free approach bypasses the need for computationally expensive gradient calculations, resulting in a significantly faster distillation process. This efficiency makes Bonsai highly scalable even for large datasets.
2. This model-agnostic method is interesting and saves efforts in hyperparameter tuning when changing condensation models.
3. It is the first distillation method that retains the original node features and synthesizes graphs with unweighted edges, which more faithfully represent the original graph structure.

### Weaknesses
1. The idea of Bonsai is very similar to MIRAGE[1], as both methods select frequent trees. This similarity makes Bonsai appear to be a minor adaptation of MIRAGE. Furthermore, much of the theoretical analysis, such as Graph Isomorphism, is borrowed from MIRAGE. Although these two works focus on different tasks, it's strongly recommended to discuss the differences between Bonsai and MIRAGE in the related work section.
2. This paper claims that "distilling to fully-condensed graph" is a problem for previous work. However, most prior methods include a sparsification step, setting a threshold to obtain a sparse graph. Consequently, the number of edges reported in Table 2 is inaccurate. For correct edge counts, please refer to Table 5 in the GCond paper [2]. Moreover, the claim that distilled graphs are always smaller than the original graph needs more careful consideration, as sparsification techniques in other methods can result in a distilled graph that is smaller than the original.
3. Although this paper presents comprehensive deductions in the theoretical section, some hypotheses appear to be too strong and lack support. For example, Hypothesis 1 (line 201) and Logical Progression 2 (line 215) may not hold true. The connection between WL embedding similarity and training gradients needs more rigorous justification.
4. In Fig. 2, the authors empirically demonstrate the correlation between GNN embedding and WL embedding. When the threshold is large, almost all node pairs are considered, leading to a low correlation. How does this observation inform the method design? The paper should clarify how this correlation is used to guide the selection of representative trees.
5. In line 235, **Diversity** is highlighted. Which part of the method addresses this concern? The paper needs to explicitly describe how diversity is achieved in the tree selection process.
6. To select the trees with top representativeness, why do the authors choose Reverse K-NN? Would it be possible to simply adopt clustering instead? The paper should discuss the limitations of clustering and justify the choice of Reverse K-NN.
7. The experimental settings differ from commonly used ones in the following ways: (a) Different dataset split (i.e., training/validation/test set split) (b) Different metric for compression rate. The authors are suggested to clarify the reasons for choosing a different setting. The paper should provide a clear rationale for deviating from standard experimental protocols.

### Questions
Please see the weaknesses

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents Bonsai, a gradient-free graph distillation method for node classification that overcomes limitations in existing approaches. By selecting exemplar computation trees rather than synthesizing fully connected graphs, Bonsai efficiently distills graphs without needing full dataset training or specific GNN architectures. This approach achieves higher accuracy and faster distillation across various datasets and GNN models.

### Strengths
1. The performance of bonsai is impressive, including the cross-arch results.
2. The proof of maximizing the representative power of exemplars is NP-hard is simple but attracting.

### Weaknesses
See questions.

### Questions
1. Could the authors clarify their specific contributions to Mirage [A]? While Mirage highlights the importance of the computation tree in graph dataset condensation, their primary focus is on the graph level (with node-level experiments included in the appendix). Thus, extending their approach to the node level by following the 1-WL test may not represent a substantial novelty.
2. Regarding Fig. 4(b), although the authors emphasize the significance of the RkNN and PPR components, the random exemplar selection still yields considerable results. How do the authors interpret this outcome? Could they also provide a performance comparison for $\mathbf{S_r}$ using different exemplars on datasets like Cora, Ogbn-arxiv, and Reddit? Including results for random selection would further clarify the comparison.
3. From my perspective, selecting datasets using a sampling strategy seems more akin to traditional graph reduction, sparsification, or coarsening methods, rather than directly aligning with the field of graph condensation. Therefore, it’s challenging to accept the significant improvements claimed over random or herding baselines. Could the authors provide an intuitive example to support their approach?

[A] Mridul Gupta, Sahil Manchanda, HARIPRASAD KODAMANA, and Sayan Ranu. Mirage: Model
agnostic graph distillation for graph classification. ICLR 2024.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes Bonsai, a linear-time, model-agnostic graph distillation algorithm for node classification. It observe three limitations of previous works, Full Gnn training, Distilling to a fully-connected graph and Model-specific. To address these limitations, Bonsai  aims to identify a set of b exemplar computation trees that optimally represent the full training set.

### Strengths
S1: The problem is important in this field.

S2: Presentation is good. Good model name.

S3: The solution looks novel to me.

### Weaknesses
W1: The experiments are not very standard. 

W2: Some recent works are not included as baseline.

### Questions
Q1: Why the authors choose 0.5%, 1% and 3% as $S_r$? This setting does not align with previous works.

Q2: Recently, a lot of works have studied the efficiency of graph condensation, e.g., Exgc [1] and GC-SNTK [2]. These two methods should be included as baselines when comparing condensation time. By the way, it would be better to present time comparison via table than figure.

Q3: Other graph condensation methods should be included for accuracy comparison, e.g., SGDD [3], SFGC [4], GEOM [5].

[1] Exgc: Bridging efficiency and explainability in graph condensation

[2] Fast Graph Condensation with Structure-based Neural Tangent

[3] Does graph distillation see like vision dataset counterpart

[4] Structure-free graph condensation: From large-scale graphs to condensed graph-free data

[5] Navigating Complexity: Toward Lossless Graph Condensation via Expanding Window Matching

### Soundness
3

### Presentation
3

### Contribution
2
