# HOGT: High-Order Graph Transformers

- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 6, 3, 6

## Abstract
Inspired by the success of transformers on natural language processing (NLP) and computer vision (CV) tasks, graph transformers (GTs) have recently been proposed to boost the performance of graph learning. 
However, the attention mechanisms used in existing GTs face certain limitations in capturing crucial topological information or scaling to large graphs, due to their quadratic complexity. 
To address these limitations, in this paper, we propose a high-order information propagation strategy within the transformer architecture to simultaneously learn the local, long-range, and higher-order relationships of the graph. 
\textcolor{blue}{We first propose a flexible sampling method to extract communities from the graph, and create new community nodes and in particular a learnable community sampling method with reinforcement learning.} We then propose a three-step message-passing strategy dubbed \emph{HOGT} to capture the local and higher-order information in the communities and propagate long-range dependency information between the community nodes to finally obtain comprehensive node representations. Note that as structural information has been flexibly integrated into our designed community-based message-passing scheme, HOGT discards the positional encoding which was thought to be important for GT.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces HOGT (High-Order Graph Transformer), a new architecture that tackles key issues in existing graph transformers, especially around capturing topology and scaling to large graphs. The authors use a three-step message-passing process: sampling communities from the graph, creating community nodes as information bridges, and enabling message flow between graph and community nodes. This design removes the need for positional encoding, embedding structure naturally through communities. HOGT shows strong performance across different types of graphs, with impressive computational efficiency.

### Strengths
1. The paper introduces a well-founded architecture with a three-step message-passing strategy that effectively captures multi-scale information in graphs, handling local, global, and higher-order details. Theoretically, it’s shown that HOGT can approximate global attention and unify existing models, while the community-based design removes the need for positional encoding.

2. HOGT also demonstrates strong versatility, performing well on various graph types (homophilic, heterophilic, and hypergraphs) and adapting to different community sampling methods, which enhances scalability across graph sizes. Efficiency is greatly improved, with computational complexity reduced from O(N²) to O(m² + N), validated by experiments that show strong results over state-of-the-art methods, especially on challenging datasets.

### Weaknesses
1. The strict hierarchy in the three-step message-passing mechanism could introduce bottlenecks in information flow. By requiring all long-range communication to route through community nodes, the model risks distorting or weakening critical direct relationships between nodes—especially in tasks where pairwise connections hold essential information. The assumption that this hierarchical structure is universally beneficial may be too broad, as the paper offers little discussion on cases where direct node-to-node communication might better capture necessary details. Specifically, the model may struggle with tasks where the precise nature of the edge between two nodes is crucial, such as in knowledge graphs or social networks where the type of relationship (e.g., 'friend', 'colleague', 'family') is as important as the connection itself. The forced compression of information through community nodes could lead to a loss of fidelity in these edge-specific details.

2. The approach to initializing community nodes also feels underdeveloped and could pose challenges. Starting with random initialization may lead to instability and slower convergence, particularly in early training stages. Additionally, there's no clear strategy for aligning community node dimensionality with original node features, which seems like a significant gap. Given that these community nodes are crucial bridges for information flow, their initial setup could substantially impact the quality of the representations learned. The lack of a principled initialization strategy could lead to the community nodes not effectively capturing the underlying structure of the graph, especially if the dimensionality of the community nodes is significantly different from the original node features, potentially causing information loss or distortion during the aggregation process.

### Questions
See weakness

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a high-order graph transformer (HOGT) for graph learning tasks. HOGT introduces a flexible sampling method to extract communities from the graph and a three-step message-passing strategy to capture local, long-range, and higher-order relationships of the graph. The paper demonstrates the effectiveness of HOGT on node classification tasks and shows its superiority over other graph models.

### Strengths
(1) The paper introduces a novel approach, HOGT, that combines community-based sampling and message-passing to capture comprehensive information in graph learning.

(2) HOGT achieves competitive results on various graph datasets, demonstrating its effectiveness in node classification tasks.

(3) The paper provides a theoretical analysis of HOGT, showing its approximation capabilities and the relationship with other graph models.

### Weaknesses
(1) Domain Limitation of Datasets. Expanding the evaluation to include diverse domains, such as those in the TEG-DB datasets, which feature rich node and edge text, would strengthen the findings. The current evaluation is limited to standard node classification datasets, which may not fully capture the model's capabilities in more complex scenarios where textual information is crucial for understanding relationships.

(2) Narrow Applicability. The model’s applicability is somewhat restricted to specific tasks within graph domains, such as node classification. The authors should consider its potential for other important tasks, like link prediction. The current formulation of HOGT appears tailored for node-centric tasks, and it is unclear how well it would generalize to tasks that require reasoning about relationships between nodes or entire graphs.

### Questions
See weakness above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper presents HOGT, a graph transformer that uses community-based processing to handle graph topology and computation complexity issues.
The method consists of three parts: Community sampling using reinforcement learning, Message-passing within communities and information propagation between community nodes. HOGT achieves highly competitive results
across node and graph classification tasks.

### Strengths
* The technical part of the paper is good -- the method is of careful design and implementation.

### Weaknesses
1. The problems of node classification and graph classification are well-studied in the past 10 years.
You can find the old baselines like GAT are very competitive.  Due to task saturation, HOGT shows relatively small improvements compared to these simple algorithms.
2. The theoretical part of the paper seems like mainly from a related work. Further analysis about HOGT is needed.
3. The method is too complex.

### Questions
N/A

### Soundness
2

### Presentation
4

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
The paper presents a unique approach to graph learning by integrating high-order information propagation within the transformer architecture. The paper empirically shows that HOGT achieves competitive results on node and graph classification tasks, especially on heterophilic datasets.

### Strengths
The idea of using a learnable community sampling method with reinforcement learning for graph representation is novel. It combines the advantages of community detection and adaptive sampling.By addressing the limitations of existing graph transformers in terms of capturing topological information and scalability, this work contributes to the advancement of the field and opens up new research directions for further exploration.

### Weaknesses
Analysis on the sensitivity of the HOGT model's performance to its hyperparameters such as walk length, hidden dimension, and dropout.

Further exploration of the sampling method's performance in graphs with irregular or sparse structures would enhance the understanding of the model's robustness.

A more detailed comparison of HOGT's computational complexity, including training time and memory usage, with other state-of-the-art models is needed.

### Questions
Could the authors provide more insights into how HOGT scales with graph size, especially in terms of memory usage and training efficiency?


Can the authors elaborate on the theoretical analysis of the model's expressiveness and how it relates to the approximation of global attention?

How sensitive is HOGT to its hyperparameters, particularly the number of communities and the reinforcement learning-based sampling method?

Could the authors discuss how HOGT captures long-term dependencies in the graph and compare this with other methods that focus on long-range interactions?

How sensitive is the performance of HOGT to changes in hyperparameters such as the hidden dimension and dropout rate? 
Have the authors experimented with different optimization algorithms for hyperparameter tuning, and if so, what were the results?

### Soundness
3

### Presentation
3

### Contribution
3
