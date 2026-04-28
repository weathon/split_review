# Graph layouts and graph contrastive learning via neighbour embeddings

- Decision: Reject
- Avg Score: 5.33
- Scores: 5, 5, 6

## Abstract
In node-level graph representation learning, there are two distinct paradigms. One is known as graph layouts, where nodes are embedded into 2D space for visualization purposes. Another is graph contrastive learning, where nodes are parametrically embedded into a high-dimensional vector space based on node features. In this work, we show that these two paradigms are intimately related, and that both can be successfully approached via neighbour embedding methods. First, we introduce graph t-SNE for two-dimensional graph drawing, and show that the resulting layouts outperform all existing algorithms in terms of local structure preservation, as measured by kNN classification accuracy. Second, we introduce graph contrastive neighbor embedding (graph CNE)}, which uses a fully-connected neural network to transform graph node features into an embedding space by optimizing the contrastive InfoNCE objective. We show that graph CNE, while being conceptually simpler than most existing graph contrastive learning methods, produces competitive node representations, with state-of-the-art linear classification accuracy.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a new algorithm for graph layouts, graph t-SNE, and a new algorithm for contrastive learning algorithm, graph
CNE, and draw a connection between the two algorithms.

### Strengths
1. The paper uses several real-world graph datasets to demonstrate the superiority of the proposed methods.
2. The exploration of the connection between graph layouts and graph contrastive learning is a relatively under-explored yet important topic given the abundance of graph data nowadays and the need to visualize and process graph data.

### Weaknesses
1. Paper writing can be made better. For example, for Equation 3, there is no description of the meaning of y. The definitions of parametric and non-parametric embeddings should be clearly described earlier in the paper.
2. As the authors mention, it is suspected that "in GCL algorithms employing GCNs, it is the GCN that does the heavy lifting, and not the specifics of the GCL algorithm." However, there is no experimental setup where the authors verify this hypothesis, which is a pity. The lack of this experiment makes it difficult to assess the true contribution of the proposed contrastive learning method, as it is unclear how much of the performance gain comes from the GCN backbone versus the contrastive objective itself.

### Questions
1. Does graph t-SNE use the graph node features? This is asked because for Graph CNE, the paper mentions the reduction of dimensionality from D (input feature dimension) to d (2 or 128), and to my understanding, all the methods for graph layouts use only the structure/topology of the graph. If this is the case, I am still unsure if kNN classification accuracy is the right metric, since the metric quantifies local class separation, yet the class label for each node is unobserved by the layout methods. If this is the case, please justify the adoption of such a metric for comparing different graph layout algorithms. The concern is, what if for a real-world dataset, the class labels of nodes are less related or unrelated to the structure/topology of the graph? Then wouldn't all the layout methods show low accuracy? Fundamentally, the question is about the justification of using this metric to evaluate layout algorithms.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors aim to achieve both graph layout and node-level graph contrastive learning by neighbor embedding methods. They simplify $t$-SNE and CNE by using graph adjacency matrix as their proposed neighbor embedding methods. Experiments with 3 metrics on 6 public datasets are conducted to demonstrate the effectiveness of the proposed method.

### Strengths
1. The results on graph layouts look promising.

2. The proposed graph CNE does not rely on the entire graph as input.

### Weaknesses
Please kindly correct me if I misunderstood something.

**Majors:**

1. In Section 4, the authors say "we split all nodes into a training (2/3 of all nodes) and a test set (1/3 of all nodes)." Is this setting applied to all datasets? How to choose nodes for training? Why not use $K$-fold splits?

2. In Section 6, Paragraph 2, the authors say "we used the cosine distance and the Gaussian similarity kernel for $d$=128." Does it make sense to evaluate the models by $k$NN recall/accuracy, which is based on Euclidean distance?

3. In Section 6, Paragraph 3, the authors say "The number of epochs was set to 100." I think the number of epochs should be decided by the convergence of a model. The authors also say "running CNE for more epochs and/or with higher $m$ could likely yield better results" and "be due to insufficient optimization length and/or $m$ value" in the following paragraphs. Does this mean the models are not well-trained?

4. In Section 3.2, the authors use CNE to denote the framework of [1], and the proposed contrastive learning model is named graph CNE. However, the CNE in Figure 4 and Table 2 seems to denote the proposed method, which is confusing.

        [1] Damrich, Sebastian, et al. "From t-SNE to UMAP with contrastive learning." The Eleventh International Conference on Learning Representations. 2022.

5. In Table 2, are the baseline methods using the same experiment settings (for example, train/val/test split) as the proposed method?

6. The authors claim that "graph CNE performed comparably to the state-of-the-art graph contrastive learning algorithms." However, in Table 2, Local-GCL looks better. Please provide more evidence (for example, $t$-test) to support this sentence.

7. Why not try GNN architecture if the authors want to compare the proposed graph CNE with other GCL methods?

**Minors:**

8. Why is Figure 1 shown on Page 1 but cited on Page 7?

9. How are the hyperparameters decided?

10. ".. where running CNE for more epochs and/or with higher $m$ could likely yield better results." Is the $m$ explained somewhere in this paper?

### Questions
Please see the weaknesses part.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
First, this paper introduces graph t-SNE for two-dimensional graph drawing, and shows that the resulting layouts outperform all existing algorithms in terms of local structure preservation, as measured by kNN classification accuracy. Second, the work introduces graph contrastive neighbor embedding (graph CNE), which uses a fully connected neural network to transform graph node features into an embedding space by optimizing the contrastive InfoNCE objective.

### Strengths
1. The experimental performance is good.

2. This method is easy to implement and experimentally efficient.

### Weaknesses
1. This work uses MLP to transform node features and gives reasons for not using GCN. If possible, I think it would be helpful to include experiments that use GCN to transform node features. It's not entirely clear that the justification for avoiding GCNs is sufficient, especially given their prevalence in graph representation learning. The argument that GCNs cannot process one node at a time seems to overlook the fact that GCNs operate on the entire graph structure, and the node representations are derived from this global operation. Therefore, it would be beneficial to see a comparison with GCN-based node feature transformation to empirically validate the design choice.

2. This work seems to apply only at the node level but not at the graph level. While the paper focuses on node-level tasks, the lack of exploration into graph-level representation learning is a limitation. Many real-world applications require graph-level embeddings, and it's unclear how the proposed method could be adapted or extended to address such tasks. The paper should at least acknowledge this limitation and discuss potential avenues for future work in this direction.

### Questions
Is the proposed method applicable at the graph level?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
