# Subgraph-To-Node Translation for Efficient Representation Learning of Subgraphs

- Decision: Reject
- Scores: 6, 5, 5

## Abstract
Subgraph representation learning has emerged as an important problem, but it is by default approached with the graph neural networks (GNNs) on a large global graph, an approach that demands extensive memory and computational resources. We argue that resource requirements can be reduced by designing an efficient data structure to store and process subgraphs. In this paper, we propose Subgraph-To-Node (S2N) translation, a novel formulation to learn representations of subgraphs efficiently. Specifically, given a set of subgraphs in the global graph, we construct a new graph by coarsely transforming subgraphs into nodes. We theoretically and empirically show that S2N significantly reduces memory and computational costs compared to using state-of-the-art models with conventional data structures. We also suggest Coarsened S2N (CoS2N), which combines S2N with graph coarsening methods for improved results in a data-scarce setting where there are not sufficient subgraphs to cover the global graph. Our experiments on four real-world benchmarks demonstrate that fined-tuned models with S2N translation can process 183 -- 711 times more subgraph samples than state-of-the-art models at a similar or better performance level.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes S2N and CoS2N, two new methods for learning the representation of subgraphs where the subgraphs are given as input to the model as well as the original whole graph. The proposed methods are simple and effective, as evidenced by superior results on four real-world datasets.

### Strengths
1. Both theoretical analysis and experimental support are provided to show the advantages of the proposed methods.
2. The model design is quite simple yet the results are impressive, both in terms of effectiveness and efficiency.

### Weaknesses
1. There lack of ablation study of certain hyperaprameters and design choices. For example, the authors "use two well-known GNNs" but it is unclear why alternative choices are not discussed or used. Given the abundance of GNN models nowadays and the fact that GCN and GCN2 are relatively earlier (before 2021), it is unclear if the adoption of more recent GNN models could yield better results. The authors mention one baseline, SubGNN, uses pre-trained embeddings by GIN, yet there is no explanation of why GIN can or cannot be used for the proposed methods. What is more important, the number of layers is tuned between 1 and 2 layers (Section A.3), and it is unclear how much performance fluctuates with even more or less (0 layers, i.e. no message passing) layers. Similarly, it is unclear if alternative readout methods and graph coarsening methods are experimented with. Adding such additional experiments certainly require more work and resource, but would further help improve the soundness of the paper.
2. I suggest the authors provide more descriptions of existing methods, esp. SubGNN and GLASS. For example, if and what GNN models are used. There is some detail in Appendix A, but an additional section that focuses on the architectural comparison of all the methods would further enhance the clarity of the paper.
3. Writing issues, e.g. lack of citation of GIN.

### Questions
1. How is the proposed CoS2N related to DiffPool "Ying, Zhitao, et al. "Hierarchical graph representation learning with differentiable pooling." Advances in neural information processing systems 31 (2018)."? At a high level, both of them perform pooling and allow further message passing between the pooled clusters/subgraphs. DiffPool adopts a learnable/differentiable way to pool nodes, whereas the proposed method adopts Variation Edges for coarsening. Of course, the task is different, yet I would like to hear from the authors more about the model-architecture-level comparison. This would help readers better see the novelty of the proposed methods with respect to related work designed for different asks.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes Subgraph-to-node (S2N), an efficient data structure for subgraph-level prediction. The nodes of the new structure correspond to the subgraph and the edges are the relations among the subgraphs. The results shows both high efficiency and performance.

### Strengths
1. The proposed method shows high performance compared to the existing data structures and other baselines even with a simple and straightforward method.
2. The clear figures help in understanding and the presentation of the proposed work.

### Weaknesses
1. The graph coarsening process lacks novelty. It is quite straightforward and well-known to treat the subgraphs into a single node and link the nodes that share the nodes in the original graphs. The approach of representing subgraphs as nodes and connecting them based on shared nodes is not new, and has been explored in other graph-related tasks, such as graph generation. While the application to subgraph representation learning might be less common, the underlying technique is not novel.
2. Can this approach distinguish the two subgraphs that share the same number of nodes, i.e., is the proposed structure reconstructable? For instance, what if the red subgraph is connected to the right side of the blue subgraph in Figure 1? It may generate the same subgraphs and same number of shared nodes. The concern is whether the S2N structure can uniquely represent different subgraphs, especially when they have similar sizes and connectivity patterns within the original graph. The method's ability to capture the structural context of subgraphs is questionable.
3. Lack of details for the selection step of the subgraphs to be mapped into new nodes. How do you select the subgraphs and how do you prove that the selected subgraph is the optimal choice? The paper does not provide a clear explanation of how the subgraphs are chosen for mapping to new nodes in the S2N structure. The lack of a selection strategy and justification for the optimality of the chosen subgraphs is a significant weakness.
4. Lack of backbone architectures, which are limited to GCN-based. What about other GNN backbone architectures such as GIN? Is the proposed method restricted only to GCN as proved in Section 4.2? The evaluation of the proposed method is limited to GCN-based architectures. The paper needs to explore the performance of S2N with other GNN architectures, such as GIN and GAT, to demonstrate its general applicability.

### Questions
1. What is the difference between the existing works and the proposed works on super-nodes? I cannot clearly understand what the node boundaries in super-nodes are unknown is in Section 2.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper looks at the problem of supervised subgraph classification. To handle the scalability issues with the existing models, the authors propose the Subgraph-To-Node (S2N) translation, an efficient data structuring mechanism for manipulating subgraphs prior to model design. They also explore graph coarsening techniques in this context in a data-scarce setting. The authors prove that the S2N node representations approximate the subgraph representations of the original global graph. Their experiments are designed to show that S2N substantially reduces memory and time costs with little degradation in performance.

### Strengths
The exposition is quite clear. The proposed solutions are quite straighforward and easy to follow. The experimental protocol is more or less quite detailed and sufficiently tests the proposed models. The idea of using graph coarsening for subgraph classification is novel (to the best of my knowledge) and deserves further study.

### Weaknesses
1. There are not many real-world datasets for the supervised subgraph classification. The authors should definitely consider synthetic datasets, e.g. those considered by Alsenter et. al. (2020). It is not clear why the authors have not considered such synthetic datasets.

2. The authors do not clarify if the considered datasets are adequately large so that the GPU speed/memory really forms a bottleneck for learning. It would be helpful to see a comparison of the dataset sizes with other graph datasets where memory limitations are a known issue. This would better contextualize the need for the proposed method.

3. I am not sure about handpicking the Configuration Model (CM) as a justification for low computational complexity of S2N. Why has this model been picked: One could definitely study some other random graph models and ask the same questions?

4. When you coarsen a graph, how is the structure of the original subgraphs preserved? It is not clear how to use the coarsened graph to say something about the subgraphs in the original graph. Specifically, how do the node assignments in the coarsened graph relate back to the original subgraph structures, and what is the impact of this approximation on the final classification performance?

### Questions
Please comment on the enumerated points in Weaknesses above.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
