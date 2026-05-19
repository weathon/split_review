### Summary

This paper proposes a novel framework called FROND that employs Caputo fractional derivatives to generalize existing integer-order continuous GNNs. The authors provide an interpretation of the node feature updating process in FROND from a non-Markovian random walk perspective. The experiments demonstrate the effectiveness of the proposed framework.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide a comprehensive analysis of the proposed framework, including the interpretation of the node feature updating process and the analysis of oversmoothing.
3. The experiments are extensive and demonstrate the effectiveness of the proposed framework.

### Weaknesses

#### Some Related Works


#### comment

1. The authors should provide more details on the computational complexity of the proposed framework, including the time and space complexity of the Caputo fractional derivative calculation and the overall training and inference process. Specifically, the analysis should consider the impact of the fractional order parameter on the computational cost, as this could significantly affect the practical applicability of the method. It would be beneficial to see a breakdown of the computational cost associated with each step of the proposed algorithm, such as the fractional derivative calculation, the message passing, and the aggregation of node features. This analysis should also consider the memory requirements for storing intermediate results and the impact of the graph size on the overall computational burden.
2. The authors should discuss the limitations of the proposed framework, such as the sensitivity to the choice of the fractional order parameter and the potential for overfitting. The discussion should include an analysis of how the fractional order parameter affects the model's ability to capture long-range dependencies and how it might lead to different behaviors compared to integer-order GNNs. Furthermore, the authors should address the potential for overfitting, especially when dealing with small datasets or complex graph structures. It would be useful to see experiments that explore the sensitivity of the model to different values of the fractional order parameter and the regularization techniques that can be used to mitigate overfitting.

### Suggestions

The authors should provide a more detailed analysis of the computational complexity of their proposed framework. This analysis should not only focus on the asymptotic complexity but also consider the practical implications for different graph sizes and fractional orders. For instance, the authors could provide empirical measurements of the training time and memory usage for various datasets and fractional orders. This would help readers understand the trade-offs between the performance gains and the computational costs. Furthermore, the authors should discuss the potential for optimizing the implementation of the Caputo fractional derivative calculation to reduce the computational overhead. This could involve exploring techniques such as approximation methods or parallel computing. A thorough analysis of the computational complexity would significantly enhance the practical value of the proposed framework.

To address the limitations of the proposed framework, the authors should conduct a more comprehensive sensitivity analysis of the fractional order parameter. This analysis should explore a wider range of fractional orders and their impact on the model's performance. The authors should also investigate the relationship between the fractional order and the model's ability to capture long-range dependencies. For example, they could analyze how different fractional orders affect the model's performance on tasks that require capturing long-range dependencies. Additionally, the authors should explore regularization techniques to mitigate the risk of overfitting. This could involve techniques such as dropout, weight decay, or early stopping. A thorough sensitivity analysis and regularization study would provide a more complete understanding of the proposed framework's limitations and its potential for practical applications.

Finally, the authors should provide more guidance on how to choose the appropriate fractional order for different graph structures and tasks. The current analysis lacks a clear guideline on how to select the optimal fractional order, which could be a significant challenge for practitioners. The authors could explore heuristics or adaptive methods for selecting the fractional order based on the graph properties or the task at hand. For example, they could investigate whether the fractional order should be related to the graph's diameter or the task's complexity. Providing such guidance would make the proposed framework more accessible and easier to use in practice. Furthermore, the authors should discuss the potential for extending the proposed framework to other types of fractional derivatives or other generalizations of integer-order GNNs.

### Questions

1. What is the computational complexity of the proposed framework?
2. How does the proposed framework perform on heterophilic graphs?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
