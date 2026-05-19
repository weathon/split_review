### Summary

This paper studies the shortest path problem on random graphs. The authors propose a local-global algorithm that uses GNNs to compute local path distances, and then uses the triangle inequality to obtain global path distances. The authors provide theoretical analysis on the performance of the algorithm on Erdos-Renyi random graphs. The authors also provide empirical results on both synthetic and real-world datasets.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The authors provide a new perspective on the local-global algorithm by incorporating GNNs to compute local path distances. This is a novel idea that has not been explored in previous works.
2. The authors provide theoretical analysis on the performance of the algorithm on Erdos-Renyi random graphs. The analysis is rigorous and well-structured.
3. The authors provide empirical results on both synthetic and real-world datasets. The results demonstrate the effectiveness of the proposed algorithm.

### Weaknesses

#### Some Related Works


#### comment

1. The authors claim that their algorithm has lower embedding dimension than previous works. However, they do not provide a comparison of the embedding dimension with existing methods. This makes it difficult to assess the true advantage of their approach.
2. The authors claim that their algorithm has lower computational complexity than previous works. However, they do not provide a comparison of the computational complexity with existing methods. This makes it difficult to assess the true advantage of their approach.
3. The authors do not provide a comparison of their algorithm with existing methods in terms of both theoretical and empirical performance. This makes it difficult to assess the true contribution of their work.
4. The authors do not provide a clear explanation of how the GNNs are used to compute local path distances. It is unclear how the GNNs are trained and how they are used to predict path distances. This makes it difficult to understand the technical details of the proposed method.
5. The authors do not provide a clear explanation of how the triangle inequality is used to obtain global path distances. It is unclear how the local path distances are combined to obtain global path distances. This makes it difficult to understand the technical details of the proposed method.
6. The authors do not provide a clear explanation of how the algorithm is implemented in practice. It is unclear how the algorithm is implemented on real-world datasets. This makes it difficult to assess the practical applicability of the proposed method.
7. The authors do not provide a clear explanation of how the algorithm is evaluated. It is unclear how the performance of the algorithm is measured. This makes it difficult to assess the effectiveness of the proposed method.

### Suggestions

The paper would benefit significantly from a more thorough comparison with existing methods, both theoretically and empirically. For the theoretical comparison, the authors should explicitly state the embedding dimension and computational complexity of their algorithm and compare them with those of existing methods. This comparison should not only focus on the worst-case scenarios but also on the average-case performance, as the authors claim that their algorithm performs better in practice. For the empirical comparison, the authors should provide a more detailed analysis of the performance of their algorithm on both synthetic and real-world datasets. This analysis should include a comparison with the performance of existing methods, as well as an analysis of the sensitivity of the algorithm to different parameters. The authors should also provide a clear explanation of how the GNNs are used to compute local path distances, including the training process and the prediction mechanism. The authors should also provide a clear explanation of how the triangle inequality is used to obtain global path distances, including the specific steps involved in combining the local path distances. The authors should also provide a clear explanation of how the algorithm is implemented in practice, including the data structures used, the implementation details, and the computational resources required. Finally, the authors should provide a clear explanation of how the algorithm is evaluated, including the metrics used, the evaluation procedure, and the statistical significance of the results.

To improve the clarity of the paper, the authors should provide more details on the implementation of their algorithm. For example, they should specify the architecture of the GNNs used, the activation functions, and the optimization algorithm used for training. They should also provide details on the hyperparameter settings used for the GNNs and the local-global algorithm. The authors should also provide details on the data preprocessing steps, including the normalization and scaling of the input data. The authors should also provide details on the evaluation metrics used, including the mean absolute error, the mean squared error, and the relative error. The authors should also provide a discussion of the limitations of their algorithm and the potential directions for future research. For example, they should discuss the scalability of their algorithm to large-scale graphs and the robustness of their algorithm to noisy data.

Finally, the authors should provide a more detailed analysis of the experimental results. For example, they should provide a breakdown of the performance of their algorithm on different types of graphs and different parameter settings. They should also provide a comparison of the performance of their algorithm with different GNN architectures and different training strategies. The authors should also provide a discussion of the statistical significance of their results and the potential sources of error. The authors should also provide a comparison of the performance of their algorithm with other state-of-the-art algorithms for shortest path computation. This comparison should include both theoretical and empirical results. The authors should also discuss the potential applications of their algorithm and the potential impact of their work.

### Questions

1. Can the authors provide a comparison of the embedding dimension and computational complexity of their algorithm with existing methods?
2. Can the authors provide a comparison of the theoretical and empirical performance of their algorithm with existing methods?
3. Can the authors provide a more detailed explanation of how the GNNs are used to compute local path distances?
4. Can the authors provide a more detailed explanation of how the triangle inequality is used to obtain global path distances?
5. Can the authors provide a more detailed explanation of how the algorithm is implemented in practice?
6. Can the authors provide a more detailed explanation of how the algorithm is evaluated?

### Rating

3

### Confidence

3

**********
