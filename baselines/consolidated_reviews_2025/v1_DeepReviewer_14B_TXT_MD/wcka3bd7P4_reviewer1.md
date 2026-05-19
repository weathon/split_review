### Summary

The paper proposes a new fractional graph neural network that uses the Caputo fractional derivative to capture long-term dependencies and mitigate oversmoothing.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The idea of using the Caputo fractional derivative to capture long-term dependencies and mitigate oversmoothing is interesting.
3. The authors provide a non-Markovian random walk interpretation of the proposed method.
4. The authors conduct comprehensive experiments.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is limited to undirected graphs.
2. The proposed method does not perform well on large graphs.
3. The proposed method is computationally expensive.
4. The proposed method requires a large number of parameters.

### Suggestions

The paper introduces an interesting approach using Caputo fractional derivatives to address oversmoothing in graph neural networks. However, the current implementation has several limitations that need to be addressed for broader applicability. The restriction to undirected graphs is a significant limitation, as many real-world networks, such as social networks with follower relationships or citation networks, are directed. Future work should explore how to extend the proposed method to handle directed graphs, potentially by incorporating separate fractional derivatives for incoming and outgoing edges or by adapting the formulation to account for the asymmetry in the adjacency matrix. Furthermore, the paper should investigate the impact of different discretization schemes on the performance and stability of the proposed method, as the choice of discretization can significantly affect the accuracy of the fractional derivative approximation, especially for large graphs.

Another key area for improvement is the scalability of the proposed method. The current implementation struggles with large graphs, which is a major drawback given the increasing size of real-world datasets. The authors should explore techniques to reduce the computational cost of the fractional derivative calculation, such as using approximations or sparse matrix operations. Additionally, the paper should provide a more detailed analysis of the memory requirements of the proposed method, as memory usage can also be a limiting factor for large graphs. The authors should also investigate the use of graph sampling techniques to reduce the computational burden on large graphs, and analyze how these techniques affect the performance of the proposed method. It is also important to provide a more detailed comparison of the computational cost of the proposed method with existing methods, including a breakdown of the time spent on different operations.

Finally, the paper should address the issue of the large number of parameters required by the proposed method. While the authors claim that the method does not introduce additional training parameters, the fractional order $\beta$ and the time horizon $T$ are hyperparameters that need to be tuned, and the tuning of these parameters can be computationally expensive. The authors should explore techniques to reduce the number of hyperparameters or to make the method less sensitive to the choice of hyperparameters. For example, they could investigate adaptive methods for selecting the time horizon $T$ or the fractional order $\beta$, or explore techniques to regularize the model and prevent overfitting. The authors should also provide a more detailed analysis of the sensitivity of the proposed method to the choice of hyperparameters, and provide guidelines for selecting appropriate values for these parameters.

### Questions

1. How does the proposed method perform on directed graphs?
2. How does the proposed method perform on large graphs, such as OGBN-arxiv, with more than 169,343 nodes and 1,166,243 edges?
3. How does the computational cost of the proposed method compare with existing methods?
4. How does the number of parameters of the proposed method compare with existing methods?
5. How does the proposed method perform when the time horizon $T$ is small?
6. How does the proposed method perform when the time horizon $T$ is large?
7. How does the proposed method perform when the fractional order $\beta$ is close to 0?
8. How does the proposed method perform when the fractional order $\beta$ is close to 1?
9. How does the proposed method perform when the graph is sparse?
10. How does the proposed method perform when the graph is dense?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
