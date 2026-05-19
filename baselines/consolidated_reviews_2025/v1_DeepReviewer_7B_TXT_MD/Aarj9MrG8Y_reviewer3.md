### Summary

This paper proposes a universal learning principle for graph neural networks (GNNs) to design infinite deep GNNs. The authors also introduce a new GNN model called Adaptive Power Graph Neural Network (APGNN) to implement this principle. The authors provide a theoretical analysis of the generalization ability of APGNN and conduct experiments to demonstrate its effectiveness.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide a theoretical analysis of the generalization ability of APGNN.
3. The authors conduct experiments to demonstrate the effectiveness of APGNN.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed APGNN model is computationally expensive, especially when the polynomial order K is large. The authors should provide a more detailed analysis of the computational complexity of APGNN and discuss potential strategies for reducing its computational cost. Specifically, the analysis should consider the time complexity of the matrix multiplications involved in the polynomial expansion, and how this scales with the size of the graph and the value of K. Furthermore, the memory requirements for storing intermediate results during the computation should also be considered, especially for large graphs.
2. The paper does not provide a clear explanation of how the proposed APGNN model can be applied to heterophilic graphs. The authors should discuss the limitations of APGNN in handling heterophilic graphs and provide potential solutions for addressing these limitations. The current analysis focuses on homophilic graphs, but many real-world graphs exhibit heterophily, where connected nodes have dissimilar features or labels. The paper should discuss how the exponentially decaying weights might behave in such scenarios, and whether they can effectively capture the complex relationships present in heterophilic graphs.

### Suggestions

The authors should provide a more thorough analysis of the computational cost of APGNN, including a breakdown of the time complexity for each step of the algorithm. This analysis should not only consider the theoretical complexity but also discuss the practical implications for different graph sizes and polynomial orders. For instance, providing empirical results on the runtime of APGNN with varying values of K and graph sizes would be beneficial. Furthermore, the authors should explore and discuss potential optimization techniques, such as sparse matrix operations or low-rank approximations, to mitigate the computational burden. A comparison of the computational cost of APGNN with other GNN models, including both shallow and deep architectures, would also be valuable to contextualize the efficiency of the proposed method. This would allow readers to better understand the trade-offs between performance and computational cost when choosing between APGNN and other GNN models.

To address the limitations of APGNN on heterophilic graphs, the authors should investigate and discuss the impact of the exponentially decaying weights on the model's ability to capture complex relationships in such graphs. Specifically, they should analyze how the decay rate parameter affects the model's performance on heterophilic graphs and provide guidelines for selecting appropriate values for this parameter. It would be beneficial to include experiments on benchmark datasets that exhibit heterophily to demonstrate the model's performance in such scenarios. Furthermore, the authors should explore potential modifications to the model architecture or training procedure that could improve its performance on heterophilic graphs. This could involve incorporating attention mechanisms or using different aggregation functions that are more suitable for capturing the complex relationships present in heterophilic graphs. The authors should also discuss the theoretical implications of using exponentially decaying weights in heterophilic graphs and whether these weights can effectively capture the complex relationships present in such graphs.

Finally, the authors should provide a more detailed discussion of the limitations of APGNN and the scenarios where it might not be the most appropriate choice. This discussion should include a clear statement of the assumptions made by the model and the conditions under which these assumptions might not hold. For example, the authors should discuss the limitations of the power series expansion used in APGNN and whether this expansion is suitable for all types of graph structures. They should also discuss the limitations of the exponentially decaying weights and whether these weights are appropriate for all types of graph data. A clear understanding of these limitations is crucial for readers to properly interpret the results and apply the model in practice. The authors should also consider providing guidelines for when to use APGNN and when to use other GNN models, based on the characteristics of the graph data and the specific task at hand.

### Questions

Please see the weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
