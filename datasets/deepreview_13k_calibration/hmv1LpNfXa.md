# Polynormer: Polynomial-Expressive Graph Transformer in Linear Time

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
Graph transformers (GTs) have emerged as a promising architecture that is theoretically more expressive than message-passing graph neural networks (GNNs). However, typical GT models have at least quadratic complexity and thus cannot scale to large graphs. While there are several linear GTs recently proposed, they still lag behind GNN counterparts on several popular graph datasets, which poses a critical concern on their practical expressivity. To balance the trade-off between expressivity and scalability of GTs, we propose \name, a polynomial-expressive GT model with linear complexity. \name is built upon a novel base model that learns a high-degree polynomial on input features. To enable the base model permutation equivariant, we integrate it with graph topology and node features separately, resulting in local and global equivariant attention models. Consequently, \name adopts a linear local-to-global attention scheme to learn high-degree equivariant polynomials whose coefficients are controlled by attention scores. \name has been evaluated on $13$ homophilic and heterophilic datasets, including large graphs with millions of nodes. Our extensive experiment results show that \name outperforms state-of-the-art GNN and GT baselines on most datasets, even without the use of nonlinear activation functions.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Summary:  
This paper proposes Polynormer, a graph transformer model architecture for node classification. 
First, the paper introduces a base attention model in Section 3.1 that explicitly represents node features as polynomials, with coefficients determined by attention scores. This is claimed to result in high polynomial expressivity (in Sec. 3.1). To make the model equivariant, the paper integrates graph topology and node features into the polynomial coefficients to derive local and global attention models. This makes the overall Polynormer architecturem which achieves linear complexity instead of quadratic. Experiments are performed on 13 datasets including both homophilic and heterephilic tasks where Polynormer improves on most datasets.

### Strengths
Strengths:
- Provides theoretical analysis of polynomial expressivity, though restricted to scalar features. It goes beyond the WL expressivity as common in graph learning literature.
- Demonstrates the performance of the architecture on 13 datasets where comparisons with baselines make the proposed model better on 11 datasets.
- Ablation study on a smaller dataset group shows benefits of global attention and local-to-global scheme.

### Weaknesses
Weaknesses and Questions:  
-The theoretical expressivity claims in Section 3.1 may be overclaiming capabilities, as proofs make simplifying assumptions about scalar features that differ from real graph data (Section 4). Can this be justified further?   
-While complexity is analyzed, runtime and memory usage are not empirically compared to baselines in Section 4.2 to demonstrate scalability.

### Questions
included with weaknesses

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The proposed Polynormer is a new graph transformer model that balances expressivity and scalability. The paper introduces a polynomial model that achieves polynomial expressiveness with linear complexity, outperforming state-of-the-art GNN and GT baselines on most datasets. The model is based on a novel polynomial attention mechanism that can capture higher-order interactions between nodes in a graph. The attention mechanism is designed to be both local and global equivariant, allowing it to capture both local and global patterns in the graph.

### Strengths
- The idea to adopt attention model in the polynomial feature mapping is novel and interesting.
- Experiments are sufficient. Many important baselines and datasets of various sizes are covered.

### Weaknesses
 - I find that the proposed approach (global) may also work in transformers in other fields, e.g. NLP. Could you provide such experiments to show its capacity in dealing with different types of data?
- Why and how could polynomial expressivity improve model performance? The point was not clear.

### Questions
- How is the degree of polynomial defined?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes Polynormer, a polynomial- expressive GT model with linear complexity. Polynormer is built upon a novel base model that learns a high-degree polynomial on input features, with model permutation equivariance. Polynormer has been evaluated on 13 homophilic and heterophilic datasets, including large graphs with millions of nodes, with results showing that Polynormer outperforms state-of-the-art GNN and GT baselines on most datasets.

### Strengths
- The idea of designing a polynomial-expressive graph Transformer model is novel and interesting. 

- The resulting Polynormer model is powerful, efficient, and theoretically expressive.

- The experiments are convincing, showing that Polynormer can outperform sota GNNs and GTs on a wide range of datasets.

### Weaknesses
 - It is inappropriate to claim that GTs and GNNs has limited polynomial expressivity (in section 3.1 and appendix C), since the non-linearity layers are not negligible. In [1] it is shown that without softmax GTs cannot represent GNNs. And in [2] Transformers are proved to be universal approximators on sequences with the softmax layer as key component. Can you discuss the polynomial expressivity of GTs and GNNs with non-linearity layers? And since [2] proves that Transformers are universal approximators, do GTs have $\infty$-polynomial expressivity?

- The concept of graph is defined by edge connections. And the definition of polynomial expressivity is completely ignorant of graph structure, comparing to WL-test expressivity. From my opinion, polynomial expressivity defined here should be used to model expressivity on sets, not graphs. What is the motivation of modeling the polynomial expressivity of graph models?

- The O(N+E) complexity claim should be supported by more experiments, like a training time (VRAM) – graph size plot on synthetic random graphs with different sizes.

### Questions
- See weakness above.

- Can authors discuss more about the relationship between WL-test expressivity and polynomial expressivity? For example, is the proposed Polynormer strictly more powerful than 1-WL-GNNs?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good
