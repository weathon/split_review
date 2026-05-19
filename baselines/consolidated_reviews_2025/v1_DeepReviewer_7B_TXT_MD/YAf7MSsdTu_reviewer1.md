### Summary

This paper studies a local-global algorithm for the shortest path problem. The algorithm works by first sampling a set of random nodes, and then computing the shortest path distances from each sampled node to all other nodes. The shortest path distance between any two nodes $u$ and $v$ can then be estimated by $\min_{s \in S} (d(u,s) + d(v,s))$. The authors show that this algorithm achieves a $(1 \pm \epsilon)$-approximation on random graphs with bounded average degree. They also show that this algorithm can be improved by replacing the BFS procedure with a GNN.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

- The paper studies an interesting problem, and the results are somewhat novel.
- The paper is well-written and easy to follow.

### Weaknesses

#### Some Related Works

[1] Sketch-based embeddings for massive graphs.
[2] Fast approximate shortest paths in a massive sparse graph.

#### comment

 - The paper lacks a comprehensive literature review. The problem studied in this paper has been studied in the past, and the algorithm studied in this paper has also been studied before. The authors should discuss the relationship between this paper and previous works, and clearly state the novelty of this work. For example, the authors should discuss the relationship between this work and the following two papers:
    - Sketch-based embeddings for massive graphs. NeurIPS 2020.
    - Fast approximate shortest paths in a massive sparse graph. ALENEX 2023.
- The theoretical results are not very strong. The authors show that the local-global algorithm achieves a $(1 \pm \epsilon)$-approximation on random graphs with bounded average degree. However, the authors do not provide any lower bounds, and it is possible that the algorithm achieves a $(1 \pm \epsilon)$-approximation on all graphs. The authors should provide lower bounds to show that the algorithm does not achieve a $(1 \pm \epsilon)$-approximation on all graphs. Additionally, the authors should provide a more detailed discussion of the limitations of their theoretical results.
- The experimental results are not very convincing. The authors only compare their algorithm with the vanilla local-global algorithm. They should compare their algorithm with other state-of-the-art algorithms for the shortest path problem. The authors should also provide a more detailed discussion of the experimental results, including the limitations of the experiments.

### Suggestions

The paper would benefit significantly from a more thorough literature review that places the proposed algorithm within the context of existing work on sketch-based embeddings and approximate shortest path algorithms. Specifically, the authors should discuss how their approach relates to methods that use random walks or other sampling techniques to generate sketches of node neighborhoods, and how these sketches are then used to estimate shortest path distances. A detailed comparison with the techniques used in Sketch-based embeddings for massive graphs (NeurIPS 2020) and Fast approximate shortest paths in a massive sparse graph (ALEX 2023) is crucial. This discussion should highlight the specific advantages and disadvantages of the proposed local-global approach compared to these existing methods, particularly in terms of computational complexity, memory requirements, and approximation guarantees. Furthermore, the authors should clearly articulate the novel aspects of their work, such as the specific GNN architecture used and the theoretical analysis performed, and how these contributions advance the field beyond existing techniques.

To strengthen the theoretical results, the authors should provide a more rigorous analysis of the algorithm's performance, including lower bounds on the approximation ratio. The current analysis only shows that the algorithm achieves a $(1 \pm \epsilon)$-approximation on random graphs with bounded average degree, but it is unclear whether this result is tight. It is important to demonstrate that the algorithm does not achieve a $(1 \pm \epsilon)$-approximation on all graphs, or to provide a theoretical justification for why this might be the case. This could involve constructing specific graph families where the algorithm's performance degrades significantly. Additionally, the authors should explore the limitations of their theoretical analysis, such as the assumptions made about the graph structure and the random sampling process. A more detailed discussion of these limitations would provide a more balanced view of the algorithm's theoretical properties.

The experimental evaluation needs to be significantly expanded to provide more convincing evidence of the algorithm's effectiveness. The authors should compare their algorithm against a wider range of state-of-the-art algorithms for the shortest path problem, including both exact and approximate methods. This comparison should include algorithms that are specifically designed for large-scale graphs, such as those based on parallel or distributed computing. The experimental results should also be analyzed in more detail, including a discussion of the algorithm's performance on different types of graphs and under different parameter settings. The authors should also provide a more thorough discussion of the experimental setup, including the hardware and software used, and the specific datasets employed. This would allow for a more objective assessment of the experimental results and their implications.

### Questions

- What is the novelty of this work compared to previous works?
- What are the lower bounds of the local-global algorithm?
- What are the experimental results of other state-of-the-art algorithms?

### Rating

3

### Confidence

4

**********
