### Summary

The paper addresses the convergence and stability of graph filters under infinite-depth scenarios in Graph Neural Networks (GNNs). The authors propose a scalable regularized learning principle to guide the design of infinite deep GNNs. They introduce Adaptive Power GNN (APGNN), a deep GNN that uses exponentially decaying weights to aggregate graph information of different orders, allowing for the mining of deeper neighbor information. The paper also analyzes the generalization of the proposed learning framework and presents its upper bound in theory. Experimental results demonstrate that APGNN achieves superior performance compared to state-of-the-art GNNs.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper proposes a novel learning principle for developing convergent and stable GNNs, which is a significant contribution to the field of graph representation learning.
2. The introduction of APGNN, a deep GNN that can be seamlessly extended to an infinite-depth network, is a valuable contribution. The use of exponentially decaying weights to aggregate graph information of different orders is an innovative approach.
3. The theoretical analysis of the proposed learning framework, including the generalization analysis and the presentation of its upper bound, adds rigor to the paper.
4. The experimental results demonstrate the superior performance of APGNN against state-of-the-art GNNs, showcasing the effectiveness of the proposed framework.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed explanation of the practical implementation of APGNN and its scalability in real-world applications. Specifically, the paper lacks a discussion on the computational complexity of the proposed method, especially concerning the aggregation of multi-order neighbor information. It is unclear how the exponentially decaying weights are efficiently computed and applied in practice, and whether this introduces significant overhead compared to standard GNNs. Furthermore, the paper does not address the memory requirements for storing intermediate results during the aggregation process, which could be a limiting factor for large graphs.
2. While the paper presents a theoretical analysis of the proposed learning framework, it would be beneficial to provide more insights into the limitations and potential challenges of the approach. For instance, the paper does not discuss the sensitivity of the method to the choice of hyperparameters, such as the decay rate of the weights. It is also unclear how the proposed method handles noisy or incomplete graph data, which is common in real-world scenarios. A discussion of the potential failure modes and the robustness of the method would be valuable.

### Suggestions

To address the lack of clarity regarding the practical implementation of APGNN, the authors should provide a more detailed description of the computational steps involved in the aggregation process. This should include a breakdown of the time and space complexity of the algorithm, with a focus on the overhead introduced by the exponentially decaying weights. It would be beneficial to include a pseudocode representation of the algorithm, highlighting the key operations and data structures used. Furthermore, the authors should discuss the memory requirements for storing intermediate results, and how these requirements scale with the size of the graph. A comparison of the computational cost of APGNN with standard GNNs, such as GCN or GAT, would also be helpful in assessing its practical feasibility. The authors should also consider providing an analysis of the parallelizability of the proposed method, as this is crucial for scaling to large graphs.

To further strengthen the theoretical analysis, the authors should investigate the sensitivity of APGNN to the choice of hyperparameters, particularly the decay rate of the weights. This could involve conducting a sensitivity analysis to determine the optimal range of values for this parameter, and discussing the impact of different choices on the performance of the model. The authors should also explore the robustness of APGNN to noisy or incomplete graph data. This could involve conducting experiments on datasets with varying levels of noise or missing edges, and analyzing the performance of the model under these conditions. A discussion of the potential failure modes of the method, and how these can be mitigated, would also be valuable. For example, the authors could discuss the potential for over-smoothing in deep GNNs, and how APGNN addresses this issue.

Finally, the authors should consider providing a more detailed discussion of the limitations of the proposed approach. This should include a discussion of the assumptions made in the theoretical analysis, and how these assumptions might affect the applicability of the method in real-world scenarios. The authors should also discuss the potential challenges of extending APGNN to other types of graph data, such as dynamic graphs or heterogeneous graphs. A comparison of APGNN with other approaches for handling deep GNNs, such as residual connections or attention mechanisms, would also be beneficial.

### Questions

1. Can the authors provide more details on the practical implementation of APGNN and its scalability in real-world applications?
2. What are the limitations and potential challenges of the proposed learning framework, and how can they be addressed?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
