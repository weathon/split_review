### Summary

This paper studies the shortest path problem on random graphs. The authors propose a local-global algorithm that incorporates GNNs in the local computation phase. They provide theoretical analysis on the average-case performance of the algorithm on Erdős–Rényi (ER) random graphs. The authors also provide empirical results on both ER graphs and benchmark datasets.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide a theoretical analysis of the proposed algorithm on random graphs.
3. The authors conduct experiments on both synthetic and real-world datasets.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a comprehensive literature review. The problem studied in this paper has been studied in the past, and the algorithm studied in this paper has also been studied before. The authors should discuss the relationship between this paper and previous works, and clearly state the novelty of this work. For example, the authors should discuss the relationship between this work and the following two papers:
    - Sketch-based embeddings for massive graphs. NeurIPS 2020.
    - Fast approximate shortest paths in a massive sparse graph. ALENEX 2023.
2. The theoretical results are not very strong. The authors show that the local-global algorithm achieves a $(1 \pm \epsilon)$-approximation on random graphs with bounded average degree. However, the authors do not provide any lower bounds, and it is possible that the algorithm achieves a $(1 \pm \epsilon)$-approximation on all graphs. The authors should provide lower bounds to show that the algorithm does not achieve a $(1 \pm \epsilon)$-approximation on all graphs. Additionally, the authors should provide a more detailed discussion of the limitations of their theoretical results.
3. The experimental results are not very convincing. The authors only compare their algorithm with the vanilla local-global algorithm. They should compare their algorithm with other state-of-the-art algorithms for the shortest path problem. The authors should also provide a more detailed discussion of the experimental results, including the limitations of the experiments.

### Suggestions

The paper would significantly benefit from a more thorough literature review that situates the proposed work within the existing body of research on shortest path algorithms, particularly those employing graph neural networks. The authors should explicitly compare their approach to methods like sketch-based embeddings, which have demonstrated success in handling large-scale graph data. A detailed comparison should highlight the specific advantages and disadvantages of the proposed GNN-based local computation, such as its computational cost, memory requirements, and performance on different graph structures. Furthermore, the authors should discuss how their work relates to parallel algorithms for shortest path computation, which are often used in practice for large graphs. This would help to clarify the novelty of their approach and its potential impact on the field.

To strengthen the theoretical analysis, the authors should investigate the possibility of establishing lower bounds for the approximation ratio of their algorithm. While proving general lower bounds for all graphs may be challenging, it would be valuable to demonstrate that the algorithm's performance degrades beyond a certain point as the graph size or density increases. This could involve analyzing the algorithm's behavior on specific graph families, such as sparse or dense graphs, or graphs with particular structural properties. Additionally, the authors should provide a more detailed discussion of the assumptions made in their theoretical analysis and their implications for the practical applicability of the algorithm. This discussion should include a sensitivity analysis of the algorithm's performance to variations in the graph parameters, such as the average degree and clustering coefficient.

Finally, the experimental evaluation needs to be significantly expanded to provide a more convincing assessment of the proposed algorithm's performance. The authors should compare their algorithm against a wider range of state-of-the-art shortest path algorithms, including both exact and approximate methods. This comparison should be conducted on a diverse set of benchmark datasets, including both synthetic and real-world graphs. The authors should also provide a more detailed analysis of the experimental results, including a discussion of the algorithm's performance under different parameter settings and its scalability with respect to graph size. Furthermore, the authors should investigate the impact of different GNN architectures and training strategies on the algorithm's performance. This would help to identify the optimal configuration for the proposed approach and provide a more comprehensive understanding of its strengths and limitations.

### Questions

See Weaknesses.

### Rating

5

### Confidence

3

**********
