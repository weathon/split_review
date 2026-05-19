### Summary

This paper studies the shortest path problem on random graphs. The authors propose a local-global algorithm that incorporates GNNs in the local computation phase. They provide theoretical analysis on the average-case performance of the algorithm on Erdős–Rényi (ER) random graphs. The authors also provide empirical results on both ER graphs and benchmark datasets.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide a theoretical analysis of the proposed algorithm on random graphs.
3. The authors conduct experiments on both synthetic and real-world datasets.

### Weaknesses

#### Some Related Works

[1] Sketch-based embeddings for massive graphs.
[2] Fast approximate shortest paths in a massive sparse graph.

#### comment

1. The paper lacks a comprehensive literature review. The problem studied in this paper has been studied in the past, and the algorithm studied in this paper has also been studied before. The authors should discuss the relationship between this paper and previous works, and clearly state the novelty of this work. For example, the authors should discuss the relationship between this work and the following two papers:
    - Sketch-based embeddings for massive graphs. NeurIPS 2020.
    - Fast approximate shortest paths in a massive sparse graph. ALENEX 2023.
2. The theoretical results are not very strong. The authors show that the local-global algorithm achieves a $(1 \pm \epsilon)$-approximation on random graphs with bounded average degree. However, the authors do not provide any lower bounds, and it is possible that the algorithm achieves a $(1 \pm \epsilon)$-approximation on all graphs. The authors should provide lower bounds to show that the algorithm does not achieve a $(1 \pm \epsilon)$-approximation on all graphs. Additionally, the authors should provide a more detailed discussion of the limitations of their theoretical results.
3. The experimental results are not very convincing. The authors only compare their algorithm with the vanilla local-global algorithm. They should compare their algorithm with other state-of-the-art algorithms for the shortest path problem. The authors should also provide a more detailed discussion of the experimental results, including the limitations of the experiments.

### Suggestions

The paper would benefit significantly from a more thorough discussion of existing methods for shortest path computation, particularly those designed for large-scale graphs. The current literature review is insufficient, and the authors should explicitly position their work within the context of existing approaches. For instance, the paper should discuss how the proposed GNN-based local computation compares to techniques like sketch-based embeddings [1] and parallel algorithms for shortest path computation [2]. A detailed comparison would clarify the specific advantages and disadvantages of the proposed method, and highlight the unique contributions of this work. The authors should also discuss the limitations of existing methods and how their approach addresses these limitations. This would provide a stronger justification for the proposed method and its potential impact.

Furthermore, the theoretical analysis needs to be strengthened. While the authors provide a $(1 \pm \epsilon)$-approximation result on random graphs, the lack of lower bounds is a significant weakness. The authors should attempt to establish lower bounds on the approximation ratio, which would provide a more complete picture of the algorithm's performance. If proving general lower bounds is difficult, the authors should at least provide lower bounds for specific graph families or under certain assumptions. This would help to understand the limitations of the algorithm and the conditions under which it performs well. Additionally, the authors should provide a more detailed discussion of the assumptions made in the theoretical analysis and their implications for the practical applicability of the algorithm. The discussion should also include the limitations of the theoretical results and potential directions for future research.

Finally, the experimental evaluation needs to be more comprehensive. The authors should compare their algorithm against a wider range of state-of-the-art algorithms for shortest path computation, including both exact and approximate methods. This would provide a more robust evaluation of the proposed method and its performance in different scenarios. The authors should also provide a more detailed analysis of the experimental results, including a discussion of the sensitivity of the algorithm to different parameters and the computational cost of the proposed method. The experimental section should also include a discussion of the limitations of the experiments and potential directions for future research. This would help to identify the strengths and weaknesses of the proposed method and provide a more complete picture of its performance.

### Questions

1. How does the proposed algorithm compare to existing methods for shortest path computation, such as sketch-based embeddings and parallel algorithms?
2. What are the limitations of the theoretical results, and are there any lower bounds that can be established?
3. How does the performance of the proposed algorithm vary with different graph structures and parameters?

### Rating

5

### Confidence

3

**********
