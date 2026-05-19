### Summary

This paper proposes a learning principle for graph neural networks (GNNs) that ensures convergence and stability as the network grows deeper. The authors introduce Adaptive Power Graph Neural Networks (APGNN), which is designed to adhere to this principle by employing exponentially decaying weights to aggregate information from distant neighbors. The paper provides theoretical analysis of the generalization ability of APGNN and demonstrates its superior performance against state-of-the-art GNNs through experimental results.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed APGNN model is innovative and well-motivated by the theoretical analysis of the convergence and stability of graph filters. The use of exponentially decaying weights to aggregate information from distant neighbors is a novel approach that addresses the over-smoothing problem in GNNs.
3. The paper provides a theoretical analysis of the generalization ability of APGNN, which is a valuable contribution to the field of GNNs.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed APGNN model is computationally expensive, especially when the polynomial order K is large. The authors should provide a more detailed analysis of the computational complexity of APGNN and discuss potential strategies for reducing its computational cost. Specifically, the analysis should consider the time complexity of the matrix multiplications involved in the polynomial expansion, and how this scales with the size of the graph and the value of K. Furthermore, the memory requirements for storing intermediate results during the computation should also be considered, especially for large graphs.
2. The paper does not provide a clear explanation of how the proposed APGNN model can be applied to heterophilic graphs. The authors should discuss the limitations of APGNN in handling heterophilic graphs and provide potential solutions for addressing these limitations. The current analysis focuses on homophilic graphs, but many real-world graphs exhibit heterophily, where connected nodes have dissimilar features or labels. The paper should discuss how the exponentially decaying weights might behave in such scenarios, and whether they can effectively capture the complex relationships present in heterophilic graphs.

### Suggestions

The paper would benefit from a more thorough investigation into the computational aspects of the proposed APGNN model. While the theoretical analysis is valuable, the practical applicability of the model is limited by its computational cost, especially for large graphs and high polynomial orders. The authors should explore techniques such as sparse matrix operations or low-rank approximations to reduce the computational burden. Furthermore, a detailed analysis of the time and space complexity of the algorithm, including the dependence on the graph size, polynomial order, and the number of layers, would be beneficial. This analysis should also consider the practical implications of these complexities, such as the maximum graph size that can be handled with a given computational budget. It would also be useful to compare the computational cost of APGNN with other state-of-the-art GNN models, providing a clear understanding of the trade-offs involved.

To address the limitations of APGNN on heterophilic graphs, the authors should provide a more in-depth analysis of how the model's performance is affected by the degree of heterophily. It would be beneficial to include experiments on benchmark datasets that exhibit heterophily, such as social networks or knowledge graphs. The authors should also discuss the potential modifications to the model that could improve its performance on heterophilic graphs. For example, they could explore the use of adaptive weighting schemes that take into account the similarity between connected nodes, or investigate the use of different aggregation functions that are more suitable for heterophilic settings. Furthermore, the paper should discuss the theoretical implications of using exponentially decaying weights in heterophilic graphs, and whether these weights can effectively capture the complex relationships present in such graphs.

Finally, the paper should include a more detailed discussion of the limitations of the proposed APGNN model. While the theoretical analysis is comprehensive, the practical applicability of the model is limited by its computational cost and its potential inability to handle heterophilic graphs. The authors should clearly state these limitations and discuss potential directions for future research. For example, they could explore the use of more efficient implementations of the model, or investigate alternative aggregation schemes that are more suitable for heterophilic graphs. The paper should also discuss the potential impact of the model's limitations on its applicability to real-world problems, and provide guidance on when the model is most appropriate to use.

### Questions

See the weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
