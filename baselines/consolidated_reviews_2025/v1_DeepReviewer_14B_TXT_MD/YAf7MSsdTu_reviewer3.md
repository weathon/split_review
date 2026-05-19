### Summary

This paper investigates the use of local-global algorithms for approximating shortest distances in graphs, particularly focusing on Erdős-Rényi (ER) random graphs. The authors provide a theoretical analysis showing that these algorithms can achieve $(1-\epsilon)$-factor lower bounds and $(1+\epsilon)$-factor upper bounds for shortest distances with high probability on ER graphs, requiring a lower embedding dimension than in the worst-case scenario. Additionally, they propose a modification to these algorithms by incorporating Graph Neural Networks (GNNs) in the local computation phase to automate and improve computational efficiency. Empirical results demonstrate that the GNN-augmented algorithm performs better than traditional approaches on both ER graphs and benchmark graph datasets.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper provides a theoretical analysis of local-global algorithms on ER random graphs, showing that these algorithms can achieve $(1-\epsilon)$-factor lower bounds and $(1+\epsilon)$-factor upper bounds for shortest distances with high probability, while requiring a lower embedding dimension than in the worst-case scenario. This analysis is a valuable contribution to the understanding of the performance of these algorithms on random graphs.
2. The authors propose a modification to the local-global shortest distance algorithm by incorporating GNNs in the local computation phase. This modification aims to automate local computations and improve computational efficiency in practical scenarios. The use of GNNs in this context is a novel approach that has the potential to significantly improve the performance of these algorithms.
3. The paper is well-written and easy to follow. The authors clearly explain the theoretical results and the proposed modification to the algorithm. The empirical results are also presented in a clear and concise manner.

### Weaknesses

#### Some Related Works


#### comment

1. The paper's analysis is limited to Erdős-Rényi (ER) random graphs, which may not fully represent the complexity and diversity of real-world networks. While ER graphs are a foundational model in random graph theory, they often lack the structural properties found in many real-world networks, such as community structure, power-law degree distributions, and small-world phenomena. This limitation raises concerns about the generalizability of the theoretical results and the practical applicability of the proposed GNN-augmented algorithm to more complex network topologies. The analysis should be extended to other graph families to validate the robustness of the findings.
2. The paper does not provide a detailed analysis of the computational complexity of the proposed GNN-based algorithm, particularly in comparison to the original local-global algorithm. While the authors mention that the GNN aims to improve computational efficiency, a rigorous analysis of the time and space complexity, including the number of parameters and the computational cost of each layer, is missing. This makes it difficult to assess the practical scalability of the proposed approach, especially for large-scale graphs. A comparison with the complexity of Dijkstra's algorithm or other shortest path algorithms would also be beneficial.
3. The paper lacks a comprehensive comparison of the proposed GNN-based algorithm with other state-of-the-art methods for approximating shortest distances in graphs. While the authors compare their approach to traditional methods, a more thorough evaluation against other GNN-based approaches or other machine learning techniques for graph analysis is needed. This comparison should include not only accuracy but also computational efficiency and scalability. Furthermore, the evaluation should consider a wider range of datasets with varying sizes and structural properties to provide a more complete picture of the algorithm's performance.

### Suggestions

To address the limitations of the current analysis, the authors should extend their theoretical results to other families of graphs beyond Erdős-Rényi (ER) random graphs. Specifically, they should consider graphs with power-law degree distributions, community structures, or small-world properties, which are commonly observed in real-world networks. This would involve adapting the existing proofs or developing new theoretical frameworks to analyze the performance of local-global algorithms on these more complex graph structures. Furthermore, the authors should investigate the impact of different graph parameters, such as average degree and clustering coefficient, on the approximation guarantees of their algorithm. This would provide a more comprehensive understanding of the algorithm's behavior under various network conditions and enhance the practical relevance of their findings. The analysis should also explore the limitations of the proposed approach on graphs that deviate significantly from the ER model, identifying potential failure cases and suggesting possible remedies.

To improve the practical applicability of the proposed GNN-augmented algorithm, the authors should provide a detailed analysis of its computational complexity. This analysis should include a breakdown of the time and space complexity of each component of the algorithm, including the GNN training and inference phases. The authors should also compare the computational cost of their approach with that of traditional shortest path algorithms, such as Dijkstra's algorithm and Bellman-Ford, as well as other GNN-based methods for shortest path approximation. This comparison should consider both the theoretical complexity and the empirical runtime on different graph sizes and densities. Furthermore, the authors should investigate the scalability of their approach to large-scale graphs, identifying potential bottlenecks and suggesting optimization techniques to improve performance. This analysis should also include a discussion of the memory requirements of the GNN model and its impact on the overall computational efficiency.

Finally, the authors should conduct a more comprehensive evaluation of their proposed GNN-based algorithm by comparing it with other state-of-the-art methods for approximating shortest distances in graphs. This comparison should include not only traditional methods but also other GNN-based approaches and machine learning techniques for graph analysis. The evaluation should consider a wide range of datasets with varying sizes, densities, and structural properties to provide a more complete picture of the algorithm's performance. The authors should also report the accuracy of the approximations, as well as the computational efficiency and scalability of the different methods. This comparison should also include a discussion of the strengths and weaknesses of each approach, highlighting the specific scenarios where the proposed algorithm performs best. The evaluation should also consider the impact of different GNN architectures and hyperparameters on the performance of the proposed approach.

### Questions

1. How does the performance of the GNN-augmented algorithm vary across different types of real-world networks with varying structural properties?
2. Can the theoretical analysis be extended to other families of graphs beyond ER random graphs?
3. How does the computational complexity of the proposed GNN-based algorithm compare to the original local-global algorithm, especially for large-scale graphs?
4. How does the proposed GNN-based algorithm compare to other state-of-the-art methods for approximating shortest distances in graphs, in terms of both accuracy and computational efficiency?

### Rating

5

### Confidence

2

**********
