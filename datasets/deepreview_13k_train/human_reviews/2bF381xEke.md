# MapSelect: Sparse & Interpretable Graph Attention Networks

- Decision: Reject
- Scores: 3, 3, 3, 3

## Abstract
Graph Attention Networks (GATs) have shown remarkable performance in capturing complex graph structures by assigning dense attention weights over all neighbours of a node. Attention weights can act as an inherent explanation for the model output, by highlighting the most important neighbours for a given input graph. However, the dense nature of the attention layer causes a lack of focus as all edges receive some probability mass. To overcome this, we introduce MapSelect, a new method providing a fully differentiable sparse attention mechanism. Through user-defined constraints, MapSelect enables precise control over the attention density, acting as a continuous relaxation of the popular top-k operator. We propose two distinct variants of MapSelect: a local approach maintaining a fixed degree per node, and a global approach preserving a percentage of the full graph. Upon conducting a comprehensive evaluation of five sparse GATs in terms of sparsity, performance, and interpretability, we provide insights on the sparsity-accuracy and sparsity-interpretability trade-offs. Our results show that MapSelect outperforms robust baselines in terms of interpretability, especially in the local context, while also leading to competitive task performance on real-world datasets.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Graph Attention Networks (GATs) can capture complex graph structures, but the dense nature of softmax functions gives non-zero probability to even irrelevant neighbors. To tackle this problem, this paper proposes MapSelect, a sparse attention mechanism as an alternative to GATs. MapSelect allows to control of the attention sparsity using a continuous relaxation of the top-k operator. The authors demonstrate the sparsity, performance, and interpretability of MapSelect on six benchmarks including one synthetic dataset.

### Strengths
This paper tackles an important problem of graph representation learning, the sparsity, and the interpretability of graph attention networks. The proposed method is easy and straightforward, and effective in terms of performance and interpretability.

### Weaknesses
- The stated strengths (Section 2: deterministic and end-to-end differentiable, and thus easier to optimize) are not fully justified. For the ‘deterministic, thus easier to optimize’ part, is it really true? Is there any reference? For the ‘end-to-end differentiable, thus easier to optimize’ part, why do authors think that existing works (NeuralSparse and SGAT) are not end-to-end differentiable? The reparameterization makes their methods end-to-end differentiable.
- This paper compares MapSelect with sparse GAT variants. However, a comparison with the original GAT is needed in terms of performance and efficiency. Since the sparse-masking procedure requires additional computations and memory, there is a need to accurately quantify the benefits gained over the original GAT. The authors should provide a detailed analysis of the trade-offs between sparsity, performance, and computational cost compared to the original GAT, as the current presentation focuses only on the benefits of sparsity without quantifying the overhead.
- The interpretability is not deeply investigated. Only one dataset (BA-Shapes) for graph-level explanation tasks is used. There is no comparison with other GNN explainers other than attention. In addition to fidelity, label-agreement for node-level tasks can be a good metric for attention quality (from How to Find Your Friendly Neighborhood: Graph Attention Design with Self-Supervision, ICLR 2021). The analysis lacks a comprehensive evaluation of interpretability, particularly in comparison to other established GNN explanation techniques. The current analysis is limited to visual inspection of attention patterns on a single dataset, which is insufficient to claim strong interpretability.
- Masking attention for sparsity is also studied in Transformers. Two missing papers below are about sparse Transformers for graph-structured data.
  - Transformers meet Stochastic Block Models: Attention with Data-Adaptive Sparsity and Cost, NeurIPS 2022
  - EXPHORMER: Sparse Transformers for Graphs, ICML 2023
- There are some missing results:
  - Top-k attention is missing in Figure 2.
  - Where can I find the results stated in “both MapSelect-G and SGAT outperform the AUC scores presented by the attention, gradient, and GNNExplainer baselines in Luo et al. (2020), with SGAT even outperforming the proposed PGExplainer itself.”
- Typos: EWe (Section 3) → We

### Questions
- Section 2.1 uses three times of parameters against the original GAT implementation: W1 (d’ x 2d) + W2 (d’ x d) = 3 *  W (d’ x d) in GAT. Is this modification applied to not only MapSelect and other baselines? We can validate this if the authors upload their codes in the supplementary material.
- The term ‘computation graph’ can be misunderstood as 'graphs where nodes are mathematical operations'. What about input graphs?

### Soundness
2 fair

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper aims to improve the explainability of attention weights of graph attention networks. In particular, the paper proposes MapSelect, which adopts SparseMap to provide fully differentiable sparse attention mechanism for better explainability. MapSelect enables precise control over the attention density. The paper proposes two variants of MapSelect, a local approach maintaining a fixed degree per node and a global approach preserving a percentage of the full graph. Experimental results show accuracy-interpretability trade-off when sparsity increases.

### Strengths
1. The proposed method is simple and makes sense
2. The proposed method enables precise control over the attention density
3. Experimental results show that MapSelect can improve the interpretability of graph attention network

### Weaknesses
1. The accuracy and interpretability of the proposed method are just comparable with SGAT on most datasets used in the paper. In other words, it doesn’t significantly outperform the baselines.
2. From experimental results, we can find that the performance drops significantly when the graph becomes sparse. It is doubtable if one would like to sacrifice the accuracy. Thus, the paper should also add one baseline, i.e., adopts GAT as a baseline for accuracy and adopts a post-hoc explainer for GAT for explainability. If such simple baseline outperforms the proposed method in terms of both accuracy and interpretability, or has comparable interpretability and better accuracy, then the proposed method is unnecessary. 
3. The scalability of the proposed MapSelect-G is questionable as one need to solve SparseMap problem in each epoch. It is better to provide time complexity analysis and real running time on the used datasets. In addition, the datasets used are very small. The authors should also conduct experiments on larger datasets.
4. Currently, the proposed method is only limited to graph attention network. The authors might consider replacing the second GAT in Figure 1(A) by other GNN models to show that the proposed method is flexible to benefit various GNNs

### Questions
Please see above.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces a novel method called MapSelect to address issues with dense attention layers in Graph Attention Networks (GATs). The proposed method offers a fully differentiable sparse attention mechanism that allows precise control over attention density, acting as a continuous relaxation of the top-k operator. The paper presents two versions of MapSelect: a local approach maintaining a fixed degree per node and a global approach preserving a percentage of the full graph. The approach seems to be effective but lacks rigorous analysis/proof. Finally, it tests on several widely-used datasets, however the experimental study seems not convincing.

### Strengths
1.	It tests on several widely-used datasets, and the proposed method can sometimes beat the existing methods.

### Weaknesses
1.  The core part (the proposed method in Section 3) lacks of sufficient analysis. We know that it is not difficult to put different modules together to form a paper. But we should make sure that the motivation of doing that really makes sense and we should understand what we are doing. The paper introduces a differentiable relaxation of the top-k operator, but it does not provide a clear explanation of why this specific relaxation is chosen over other possible alternatives. The theoretical properties of this relaxation, such as its convergence behavior or approximation guarantees, are not discussed. Furthermore, the connection between the proposed method and the underlying graph structure is not clearly established. It is unclear how the sparsity induced by MapSelect relates to the graph's topology and whether this sparsity is beneficial for learning on the given graph. The paper does not provide any theoretical justification for why the proposed method should be effective on graph data.
2.  The writing needs to be largely improved. The content in introduction is hard to follow. The symbol system needs to be improved. The introduction lacks a clear and concise overview of the existing challenges in GATs and how the proposed method addresses them. The motivation for using a sparse attention mechanism is not clearly articulated. The paper introduces several new symbols without proper definitions, making it difficult for the reader to follow the technical details. The notation is inconsistent and sometimes confusing, which further hinders the understanding of the proposed method. For example, the use of similar symbols for different concepts makes it hard to distinguish between them.
3.  As shown in Figures 2-5, it seems that SGAT performs better than the proposed methods? As we can see that SGAT almost always stay on the highest line. The experimental results do not clearly demonstrate the superiority of the proposed method over existing approaches. In many cases, SGAT achieves comparable or even better performance than MapSelect. The paper does not provide a detailed analysis of the cases where MapSelect performs well and the cases where it does not. The ablation study is also insufficient, and it does not provide a clear understanding of the contribution of each component of the proposed method. The paper lacks a thorough comparison with other sparse attention mechanisms, making it difficult to assess the novelty and effectiveness of the proposed approach.

### Questions
1.	See the weakness in the “*Weaknesses” part.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this article, the authors explore the limitations of Graph Attention Networks (GATs), particularly concerning their dense attention weights, which allocate probability mass to all neighbors of a node. This denseness can dilute the model's focus, as every edge is given some attention. To address this issue, the authors introduced a novel, fully differentiable sparse attention mechanism that allows for precise control over attention density. This mechanism is a continuous relaxation of the conventional top-k operator, facilitated through user-defined constraints.

The authors propose two unique variations of this sparse attention mechanism:
1. A local approach that ensures a consistent degree per node.
2. A global method that retains a specific percentage of the complete graph.

Through a comprehensive evaluation, they assess the five sparse GATs on metrics like sparsity, performance, and interpretability, offering valuable insights into the trade-offs between accuracy and both sparsity and interpretability. The findings reveal that the new sparse attention mechanism offers superior representability over baseline models, with the local approach showing promise.

### Strengths
Originality: Fair. This work combines two existing ideas, GAT and SparseMap. This work is a minor variation of a well-studied problem.

Quality: Fair. In the experiment part, this work compared two variants MapSelect-L and MapSelect-G with several baselines such as Top-k, Entmax, NerualSpare, SGAT, DropEdge, which is a good practice in empirical evaluations. 

Clarity: This work provides a lucid explanation of the proposed methodology. The appendix also contains a wealth of details.

Significance: The provided method outperforms some baselines in interpretability in some cases.

### Weaknesses
Novelty: The problem of improving differentiability by integrating some mechanisms is not unique to GATs. Mathematical novelty might seem limited. Looking forward to seeing the improvements in theory.

Technical: The tool SparseMap to sparse the graph is an open-source one, but the code has not been updated for 5 years. Looking forward to seeing the update in the code.

Presentation: Using both American English and British English, such as "neighboring" and "neighbours" in the same article, can be confusing for readers and is generally not considered good practice. Consistency in spelling, grammar, and style within a single document helps maintain clarity and professionalism.

### Questions
In the paper, a novel sparse attention mechanism was introduced to address the limitations of dense attention in Graph Attention Networks (GATs). While the approach is intriguing, I noticed that the improvements over the state-of-the-art, were not considerably very significant, especially when considering the added complexity of your proposed mechanism. Can you elaborate on the tangible benefits of adopting this new method over existing approaches, especially in real-world applications where computational efficiency might be crucial? Are there specific scenarios or types of data where your method shows distinct advantages?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
