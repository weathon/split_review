# Rethinking Graph Super-Resolution: Dual Frameworks for Topological Fidelity

- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 3, 3, 5

## Abstract
Graph super-resolution is an underexplored yet highly relevant research direction that circumvents the need for costly and time-consuming data collection, preparation, and storage. This makes it especially desirable for resource-constrained fields such as the medical domain. Existing work on graph super-resolution leverages graph neural networks (GNNs) and achieves impressive results. However, we note two major limitations in the current model design: (1) It violates the underlying graph structure when increasing the number of nodes, and (2) it relies heavily on node representation learning, which has limited capacity to accurately model edges. To address these limitations, we propose two novel frameworks: (1) Bi-SR, which performs structure-aware node super-resolution, and (2) DEFEND, which focuses on edge representation learning for enhanced edge modeling. We supplement our work with rigorous theoretical analysis and conduct extensive experiments on simulated and real-world datasets covering diverse graph topologies and low-to-high resolution relationships. The results demonstrate substantial improvements across all experiments, highlighting the potential of both frameworks for graph super-resolution tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper focuses on graph super-resolution, aiming at lifting the small graphs to large ones and preserving the distributions of graph structures and node features. The authors argue that previous methods ignore the underlying structures and fail to learn edge information. To address these issues, this paper proposes Bi-SR and DEFEND for node super-resolution and edge modeling, respectively. Experimental results demonstrate the effectiveness of the proposed method over baselines.

### Strengths
1. Graph super-resolution is a new task in the era of GNNs. It is claimed to be crucial for certain applications, such as neuroscience.

2. This paper identifies the weaknesses of previous methods and verifies them through extensive experiments.

### Weaknesses
1. There are already some GNNs that can be used for graph super-resolution, such as Graph u-nets (the authors also mentioned this paper). However, this paper does not take them into account. In contrast, this paper only uses the basic Linear Algebraic method and autoencoder as baselines, making the experiments unconvincing.

2. This paper proposes two methods, including Bi-SR and DEFEND. However, this relationship between them is not clear. Is there a principle on how to choose the algorithm? Should we use them together or should we use them separately?

3. Although graph super-resolution is a new task, the research on generating graphs with different sizes has been studied for a long time. The representative method is called graphon. Generally, graphon-based methods not only have good theoretical guarantees to preserve structural information but also model the edge distribution. In my view, current issues on graph super-resolution can be well addressed by the advanced graphon methods, such as IGNR [1].

4. The presentation of this paper needs improvement. The notation is confusing and the figures are not in pdf format.

### Questions
See weaknesses.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This work focuses on generating high-resolution (HR) graphs from low-resolution (LR) graphs. The authors propose two methods, Bi-SR and DEFEND, both using Graph Neural Networks (GNNs) as the foundational structure. Bi-SR constructs a bipartite graph that connects nodes between the LR and HR graphs. It randomly initializes the HR node features, and then uses a message-passing on the bipartite graph to refine the HR node features. These features are subsequently refined through another intra-graph message-passing on the HR graph nodes. This refinement process uses either full-graph message passing on HR nodes or a learned structure specifically for HR message passing. The DEFEND model, on the other hand, focuses on edge representation learning by performing message passing on the line graph of the original graph, treating edges as nodes. The methods are evaluated on synthetic graphs and a brain graph dataset.

### Strengths
1. The paper includes numerous illustrations that clearly demonstrate how the method works and showcases the results.
2. The authors validate their approach on both synthetic and real-world graphs and the results seem to be promising.
3. In addition to the experiments, they also provide a theoretical analysis of their method's effectiveness.

### Weaknesses
1. **Clarity and Writing Issues**
   The paper has several writing issues that make it difficult to follow. For example, Section 2.4 starts with "However, this method disrupts structural integrity..." without clarifying what "this method" refers to. This paragraph closely resembles the third paragraph in the same subsection, possibly due to editing issues. Overall, the story and motivation in each section do not flow smoothly, making it hard to understand how different parts connect.

2. **Lack of Clear Motivation for High-Resolution Graphs**
   The motivation for using high-resolution graphs, especially for general graphs, is unclear. The reviewer, unfamiliar with brain activity analysis, found it challenging to grasp the value of high-resolution graphs for general applications. Without a compelling use case in brain graph datasets, the motivation for this approach seems weak for broader graph applications.

3. **Reinventing Existing Concepts**
   The paper introduces well-known concepts as if they are novel. For instance, the "dual graph" discussed here corresponds to the line graph, which has been widely used in previous GNN research [1, 2].

4. **Inaccurate Mathematical Language**
   Propositions and corollaries should use precise mathematical language. Phrases like "this method is more effective" lack rigor, as "more effective" is not a mathematically defined term, leading to an unclear use of formal notation.

5.  **Limited Real-World Application**
   The paper only uses one real-world graph dataset, and the broader applications of this method remain unclear to the reviewer.

6. **High Computational Complexity**
   The method seems computationally expensive, requiring a full bipartite graph, a fully connected high-resolution graph, and a dual graph from the fully connected graph. However, the paper lacks an analysis of the time and memory complexity of this approach.

7. **Unclear Experimental Setup and Evaluation Metrics**
   The experimental setup and evaluation metrics are not well-defined. For instance, it's unclear how Mean Absolute Error (MAE) is measured when multiple valid permutations of the high-resolution graph could exist, making it a potential graph isomorphism problem. Calculating edge-wise MAE without addressing permutation invariance does not seem to be a valid evaluation approach.

8. **Non-standard Definition of MPNNs**
   Section 2.3 defines MPNNs in a non-standard way. The message function could be more complex, potentially including edge features and non-linear combinations of previous layer embeddings.

----------
 **Minor Points**:
- In Equation (4), the term $\mathbf{A}_f^{ref}$ is repeated twice.
- Line 152: "violets" should be corrected to "violates."

### Questions
1. Could you explain more about the experimental setup and how your evaluation metric accounts for permutations of the nodes in the HR graph?
2. What are other potential applications of this method beyond brain analysis?
3. How can the HR graph be useful for downstream tasks? High-resolution images make sense for human visual systems, but graphs are not typically analyzed visually. For a computational system, theoretically, performing a task such as classification on the LR graph should be equivalent to first learning the HR graph and then performing the downstream task on it.

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
Graph super-resolution is an underexplored yet highly important research direction. Existing work on graph super-resolution leverages graph neural networks (GNNs), but they suffer from some limitations. In this paper, the authors propose two frameworks: Bi-SR, which performs structure-aware node super-resolution, and DEFEND, which focuses on edge representation learning for enhanced edge modeling. Experiments show the superiority of the proposed methods.

### Strengths
1. Graph super-resolution is an important problem, but underexplored in literature particularly in comparison to the image domain.
2. The proposed method shows a good empirical performance, specifically in the brain graph domain, where graph super-resolution is important.
3. The authors have well explored potential approaches to each sub-problem, not just presenting the final form of their methods, making this work beneficial to the community.

### Weaknesses
1. Writing should be definitely improved in general. (a) The organization of the paper is strange; it’s hard to separate previous works, their limitations, and what the authors propose throughout the paper. (b) Figures 1 and 2 are not mentioned in the text, and they can be located better. (c) I have other comments as well. Please see the questions below.
2. The technical novelty of the proposed methods is unclear. The methods consist of various different components, but I’m not sure what are their core improvements and what are technical details. Specifically, the Bi-SR operator seems to perform a simple upsampling of nodes, and it is not clear how it addresses the limitations of prior works. The DEFEND operator, while presented as a feature refinement step, lacks a clear explanation of why this is necessary after the initial super-resolution. The specific contributions of each component and their interactions are not well-defined.
3. I believe that the scalability and speed can be an important issue of the proposed approach, but the experiments were done on small graph datasets. It would be nice to see experiments on large graphs. The computational complexity of creating all-pair connections between $n_l$ and $n_h$ nodes in Eq. (3) is concerning, and the authors do not provide a detailed analysis of the time and memory requirements for their method, especially when compared to existing approaches. This lack of analysis makes it difficult to assess the practical applicability of the proposed method on larger datasets.

### Questions
1. I think the authors can safely remove lines 138 - 143 from the paper.
2. Do all existing approaches for graph super-resolution have the limitation described in Section 2.4? Which of them have the limitation, and which do not?
3. Is it computationally feasible to create all-pair connections between the $n_l$ and $n_h$ nodes in Eq. (3)?
4. I’m not certain why we need the refinement step in Section 3.1, since the operation seems very similar to the super-resolution, which we aim to do eventually.
5. In Section 3.2, why do the authors use graph transformers instead of more lightweight and efficient graph neural networks?
6. How can we prove Proposition 1 and Corollary 1 if the terms like “edge space” and “more effective” are not properly defined?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper investigates the graph super-resolution problem, aiming to construct a high-resolution graph from the low-resolution one. Two graph neural network (GNN)-based approaches termed Bi-SR and DEFEND are proposed in this paper, with theoretical analysis and discussions. Experiments are conducted to show the effectiveness  of the proposed methods.

### Strengths
1. The target research problem is rarely investigated by the community so far, and it is indeed a practical technique in several real-world applications, such as brain network analysis.
2. Ample discussion and theoretical analysis are provided to guarantee the effectiveness of the proposed method.
3. Experiments are conducted under diverse scenarios, from synthetic graphs to real-world brain graphs, which shows the usefulness of the proposed method.

### Weaknesses
1. The motivation and background of this paper is not clear. Specifically, in Line 064 the authors mentioned "the topological limitation". However, the specific definition of topological limitation is not clearly given in this part. It remains unclear what specific limitations of existing methods are being addressed, especially in terms of their ability to model high-resolution graph structures. The authors should clarify whether this limitation refers to an inability to capture fine-grained edge relationships, or a restriction in modeling complex graph motifs, or both.
2. In the experiments, I found that there is few baseline for comparison. Is that because this research question is too new and hence no available methods for comparison? Do there exist more heuristic methods? The lack of baselines makes it difficult to assess the true performance gain of the proposed methods. It is not clear if the performance improvements are significant compared to simpler, more heuristic approaches. The authors should explore and include more baseline methods, even if they are not directly designed for graph super-resolution, such as interpolation-based methods or simple graph upsampling techniques.
3. The presentation of this paper can be further improved. Specifically: 1. Notations in Line 102 Aij -> A_ij; 2. Figures 1 and 2 are not easy to read. The notation issue is a minor one, but the figures need significant improvement. Figure 1, in particular, is difficult to interpret, and it is not clear how the different components of the proposed methods interact with each other. Figure 2 also lacks clarity, and the axes and labels should be more descriptive.

### Questions
1. Apart from the brain graphs, are there any practical applications of graph super-resolution?
2. How is the complexity of the proposed methods? Will they run slowly when the original low-resolution graph is already large, or when the super-resolution graph is large?

### Soundness
2

### Presentation
2

### Contribution
3
