# G-SPARC: SPectral ARchitectures tackling the Cold-start problem in Graphs

- Decision: Reject
- Scores: 5, 3, 3

## Abstract
Graphs play a central role in modeling complex relationships across various domains. Most graph learning methods rely heavily on neighborhood information, raising the question of how to handle \textit{cold-start nodes} — nodes with no known connections within the graph.
These models often overlook the cold-start nodes, making them ineffective for real-world scenarios. To tackle this, we propose G-SPARC, a novel framework addressing cold-start nodes, that leverages generalizable spectral embedding. This framework enables extension to state-of-the-art methods making them suitable for practical applications. By utilizing a key idea of transitioning from graph representation to spectral representation, our approach is generalizable to cold-start nodes, capturing the global structure of the graph without relying on adjacency data. Experimental results demonstrate that our method outperforms existing models on cold-start nodes across various tasks like node classification, node clustering, and link prediction. G-SPARC provides a breakthrough built-in solution to the cold-start problem in graph learning. Our code will be publicly available upon acceptance.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a spectral-based method to generalize the graph learning to handle cold start nodes. In particular, the authors propose to introduce node features into SOTA graph learning models and combine it with the abstracted graph structure, e.g., eigenvectors of the Laplacian matrix, to handle cold-start nodes. Through experiments, the authors demonstrate the effectiveness of the proposed method.

### Strengths
1. Overall, the paper is well written and easy to follow. 
2. The motivation of this work is well presented. The literature is well surveyed and discussed. 
3. The proposed method is well elaborated, and the examples of integrating this method into SOTA graph learning methods are described clearly.
4. Experiments are conducted on several datasets to showcase the effectiveness of the proposed method.

### Weaknesses
1. It's unclear how this proposed method can be used to handle directed graph, e.g. follow-relationship in social networks. Eigenvectors of the Laplacian matrix is suitable for undirected graph, how can we use it to capture the asymmetric relationship between nodes is not discussed.
2. There is no discussion or experiment to discuss how robust the proposed method is towards the sparsity of the graph. As pointed out by the authors, graphs are constantly evolving, it's unclear how the existing graph structure can better capture the underlying overall graph property and how it can capture the change dynamically.
3. There is no feature-based baseline comparison to validate the improvement of using graph structure.

### Questions
1. How will the proposed method capture the directed and asymmetric relationship between nodes, which is quite common in real world applications?
2. How is the model performance when we have different percentage of cold-start nodes? Taking Reddit dataset as an example, how does the proposed method perform when we have 10%, 20%, 30%, 50% nodes as cold-start nodes?
3. How does this proposed method compare with the pure feature-based methods for node classification and clustering? E.g. using transformer to encode the node features.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a spectral-based framework that addresses the cold-start problem in graph learning. The key is to leverage spectral embeddings to incorporate cold-start nodes (nodes without any connections to existing nodes). The authors introduce two extensions for GCN and NAGphormer: SPARC-GCN and SPARCphormer to handle cold-start nodes. The approach maps node features to spectral embeddings, enabling the identification of relevant neighbors for cold-start nodes based on the manifold structure of the graph. The authors also demonstrate the applicability of their method to other tasks like node clustering, link prediction, and mini-batching.

### Strengths
S1: good idea with spectral embedding for cold-start node in graph learning
S2: Extend Spectral-GCNs and Graph Transformers to support cold-start nodes while retaining their performance on connected nodes.
S3: multiple tasks: node classification, node clustering, link prediction, and mini-batching.

### Weaknesses
C1: How does the proposed method handle scenarios where node features are not informative, e.g., in recommendation, cold-start users are initialized with random feature or mean values of each feature?

C2: Can the spectral embedding approach be extended to handle dynamic graphs, where new edges are constantly added or removed?

C3: Computational complexity: the proposed vs existing graph learning techniques, especially for large-scale graphs. For example, in Figure 4, Metis partitioning is a classic fast method. Simply comparing convergence iteration is not convincing enough. What about running time? How about the complexity of this special-space related extension vs original algorithm GCN and NAGphomer?

C4: How can the authors cite an under-review paper in the same conference ICLR25?  "Anonymous. Grease: Generalizable spectral embedding with an application to umap. Under review ICLR 2024, attached to supplementary, 2024" In fact, by checking the sup doc, this draft is under review for ICLR25 instead of ICLR24.

C5: Lack of baselines specifically designed for cold-start nodes or dynamic graph scenarios?

### Questions
Please see weakness.

### Soundness
3

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
5

### Summary
This work studies on the cold-start problem in graph learning and proposes a new method with utilizing spectral embeddings. However, this work also has some significant limitations on motivations and experiments. As such, I give a negative point.

### Strengths
1. This work studies on an interesting problem.

2. The proposed method can be integrated into multiple existing methods.

3. Extensive experiments on real-world datasets are conducted to validate the effectiveness of the proposed method. 

4. The paper is well-writing.

### Weaknesses
1. The motivation of the proposed method is unclear. 

a) While this work addresses an interesting problem, there appear to be established techniques that can tackle it. For example, graph structure learning [a1], which refines node relations based on feature similarity and original graph topologies, can significantly enhance the performance of nodes with limited connections. Moreover, graph transformers can effectively learn cold-start node representation based on their feature similarity with other nodes. It remains unclear why these methods cannot adequately address this problem and how the proposed method is superior to them.

b) The rationale for leveraging spectral embeddings is unclear. Why map node features into spectral space rather than the conventional node representation space?

2.  While the authors claim that their method can be integrated into state-of-the-art methods, they only provide examples of Spectral-GCN and NAGphormer, which are relatively outdated. It would be more compelling to provide examples with more recent state-of-the-art methods, such as Difformer [a2].




3. There are also concerns regarding the experiments:

a) The key comparison methods are G-SAGE and C-BREW, but the authors do not provide introductions to these methods. Moreover, more state-of-the-art methods should be included.

b) From Table 6, it is evident that while the integration of SPARC improves the cold-start performance, it significantly degrades the overall performance of the model (sometimes by over 10%). This substantial performance degradation makes the proposed method less applicable in practice.




[a1] WWW24: Self-Guided Robust Graph Structure Refinement

[a2] ICLR’23: DIFFormer: Scalable (Graph) Transformers Induced by Energy Constrained Diffusion

### Questions
Please refer to weaknesses.

### Soundness
2

### Presentation
3

### Contribution
1
