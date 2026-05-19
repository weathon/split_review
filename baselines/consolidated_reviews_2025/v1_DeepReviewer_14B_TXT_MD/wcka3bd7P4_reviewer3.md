### Summary

This paper introduces the FRactional-Order graph Neural Dynamical network (FROND), a new continuous graph neural network (GNN) framework. Unlike traditional continuous GNNs that rely on integer-order differential equations, FROND employs the Caputo fractional derivative to leverage the non-local properties of fractional calculus. This approach enables the capture of long-term dependencies in feature updates, moving beyond the Markovian update mechanisms in conventional integer-order models and offering enhanced capabilities in graph representation learning. The authors demonstrate analytically that oversmoothing can be mitigated in this setting. Experimentally, they validate the FROND framework by comparing the fractional adaptations of various established integer-order continuous GNNs, demonstrating their consistently improved performance and underscoring the framework's potential as an effective extension to enhance traditional continuous GNNs.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The proposed method is novel and well-motivated. The idea of using fractional derivatives to capture long-term dependencies and mitigate oversmoothing is interesting.
2. The paper is well-written and easy to follow. The authors provide a clear explanation of the proposed method and its theoretical underpinnings.
3. The experimental results are comprehensive and convincing. The authors demonstrate the effectiveness of the proposed method on a variety of datasets and tasks.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is limited to undirected graphs. It would be interesting to see how the method performs on directed graphs.
2. The proposed method does not perform well on large graphs. The authors should provide more details on the computational cost of the proposed method and how it scales with the size of the graph.
3. The proposed method requires a large number of parameters. The authors should discuss the potential for overfitting and how to mitigate it.

### Suggestions

The paper introduces an interesting approach using fractional derivatives in graph neural networks, but several aspects could be improved to enhance its practical applicability and theoretical grounding. First, while the method's focus on undirected graphs is understandable, the lack of evaluation on directed graphs is a significant limitation. Many real-world networks, such as social networks or citation networks, are inherently directed, and the performance of FROND on these graphs is crucial for its broader adoption. The authors should explore how the fractional derivative formulation can be adapted to handle directed graphs, potentially by considering separate fractional derivatives for incoming and outgoing edges or by using a directed graph Laplacian. Furthermore, the theoretical justification for the choice of the Caputo fractional derivative should be more thoroughly discussed, especially in the context of directed graphs, where the notion of a single, global Laplacian is not as straightforward.

Second, the paper needs to address the scalability issues more directly. The authors mention that the method does not perform well on large graphs, but they do not provide a detailed analysis of the computational bottlenecks. It is essential to understand whether the limitations are due to the increased complexity of the fractional derivative calculation, the memory requirements of the method, or other factors. A more thorough analysis of the time and space complexity of the proposed method, compared to existing continuous GNNs, is needed. This analysis should include a breakdown of the computational cost of each step, such as the fractional derivative calculation, the message passing, and the parameter updates. Additionally, the authors should explore techniques to improve the scalability of the method, such as using sparse matrix representations, graph sampling, or other approximation methods. Without a clear understanding of the computational limitations and potential solutions, the practical applicability of the proposed method remains questionable.

Finally, the paper should provide more insights into the parameter sensitivity of the proposed method. The authors mention that the method requires a large number of parameters, but they do not discuss the potential for overfitting or how to mitigate it. A detailed analysis of the impact of different parameter settings on the performance of the method is needed. This analysis should include a study of the sensitivity of the method to the choice of the fractional order, the time horizon, and other hyperparameters. The authors should also explore techniques to reduce the number of parameters, such as using parameter sharing or other regularization methods. Without a clear understanding of the parameter sensitivity and potential mitigation strategies, the robustness and reliability of the proposed method cannot be fully assessed.

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

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
