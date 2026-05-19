### Summary

The paper studies the problem of approximating shortest path distances in graphs using local-global algorithms, which first compute local distances to a set of seed nodes and then combine these distances globally to approximate shortest paths. The authors provide an average-case analysis of these algorithms on Erdős-Rényi random graphs, showing that they achieve $(1\pm\varepsilon)$ approximation with high probability using a lower embedding dimension than worst-case bounds. They also propose a modification that uses GNNs for the local computation step, demonstrating improved performance and transferability on both random and real-world graphs.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper provides an average-case analysis of local-global algorithms for shortest path approximation on Erdős-Rényi random graphs, which complements existing worst-case results.
2. The authors propose a GNN-based approach for the local computation step, which leverages the locality property of GNNs and can be more efficient than traditional methods like BFS, especially on large graphs.
3. The GNN-based approach demonstrates transferability, where GNNs trained on small random graphs can be effectively applied to larger graphs, including real-world networks.

### Weaknesses

#### Some Related Works


#### comment

1. The theoretical analysis focuses on Erdős-Rényi random graphs, which may not capture the properties of many real-world networks. The analysis does not consider other important classes of graphs, such as power-law graphs or graphs with community structure, which are commonly found in real-world applications. This limits the generalizability of the theoretical results.
2. The GNN-based approach is only applied to the local computation step, and the global step still relies on the original algorithm. This means that the complexity of the global step, which can be computationally expensive, is not addressed by the GNN. The paper does not explore the potential of using GNNs or other machine learning techniques to optimize the global step.
3. The paper lacks a thorough comparison with other existing methods for shortest path approximation, such as those based on distance oracles or spanners. This makes it difficult to assess the relative performance and efficiency of the proposed approach compared to the state-of-the-art.

### Suggestions

The paper would benefit from a more detailed exploration of the limitations of the theoretical analysis. While the analysis on Erdős-Rényi graphs is a valuable starting point, it is crucial to acknowledge that these graphs do not fully represent the complexity of real-world networks. Future work should consider extending the analysis to other graph families, such as power-law graphs, which exhibit different structural properties. Furthermore, the paper should discuss the implications of these limitations for the applicability of the proposed approach in practical scenarios. It would also be beneficial to investigate the performance of the GNN-based local computation on graphs that deviate from the Erdős-Rényi model, to better understand the robustness of the approach.

To enhance the practical impact of the work, the authors should investigate the potential of using GNNs or other machine learning techniques to optimize the global computation step. The current approach relies on the original global step algorithm, which may become a bottleneck for large graphs. Exploring alternative global steps that leverage the learned local embeddings could lead to significant performance improvements. For example, a GNN could be trained to directly predict shortest path distances based on the local embeddings, potentially bypassing the need for a separate global step. This would also allow for a more end-to-end learning approach, which could further improve the accuracy and efficiency of the method. The paper should also discuss the trade-offs between the accuracy and efficiency of different global steps.

Finally, the paper needs a more comprehensive experimental evaluation that includes a comparison with other state-of-the-art methods for shortest path approximation. This should include methods based on distance oracles, spanners, and other relevant techniques. The comparison should not only focus on the approximation accuracy but also on the computational efficiency, memory usage, and scalability of the different methods. This would provide a more complete picture of the strengths and weaknesses of the proposed approach and help to identify areas for future improvement. The experimental section should also include a more detailed analysis of the impact of different GNN architectures and hyperparameters on the performance of the proposed method.

### Questions

1. How does the proposed GNN-based approach compare with other existing methods for shortest path approximation in terms of accuracy and efficiency?
2. Can the GNN-based approach be extended to other types of graphs beyond Erdős-Rényi random graphs, such as power-law graphs or real-world networks with more complex structures?
3. Is it possible to use GNNs or other machine learning techniques to optimize the global computation step as well?
4. What are the limitations of the theoretical analysis on Erdős-Rényi graphs, and how do these limitations affect the applicability of the results to real-world scenarios?

### Rating

3

### Confidence

3

**********
