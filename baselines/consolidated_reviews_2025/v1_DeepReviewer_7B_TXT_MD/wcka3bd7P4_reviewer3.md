### Summary

This paper proposes a novel continuous GNN framework that employs Caputo fractional derivatives to generalize existing integer-order continuous GNNs. The authors provide an interpretation of the node feature updating process from a non-Markovian random walk perspective. The authors also theoretically analyze the oversmoothing issue of the proposed framework. The experimental results show that the proposed framework can outperform existing integer-order continuous GNNs on node classification tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The proposed framework is novel and interesting. The authors provide a novel interpretation of the node feature updating process from a non-Markovian random walk perspective.
2. The authors provide a theoretical analysis of the oversmoothing issue of the proposed framework.
3. The experimental results show that the proposed framework can outperform existing integer-order continuous GNNs on node classification tasks.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed framework is a generalization of existing integer-order continuous GNNs. The authors should discuss the limitations of the proposed framework.
2. The authors should provide a more detailed analysis of the computational complexity of the proposed framework.
3. The authors should provide a more detailed analysis of the impact of the fractional order on the performance of the proposed framework.

### Suggestions

The paper introduces a novel framework using Caputo fractional derivatives to generalize integer-order continuous GNNs, which is a promising direction. However, the discussion of limitations needs to be more thorough. While the authors mention that the framework is a generalization, they should explicitly state the scenarios where the proposed method might underperform compared to existing integer-order methods. For instance, are there specific graph structures or node feature distributions where the fractional-order approach introduces instability or convergence issues? A more detailed analysis of the conditions under which the proposed method is most effective, and when it might be less suitable, would be beneficial. This should include a discussion of the potential for the fractional derivative to amplify noise or introduce artifacts in the node features, and how this might affect the overall performance of the model.

Furthermore, the computational complexity analysis should be expanded to include a more detailed breakdown of the time and memory requirements for each step of the proposed algorithm. The authors should provide a theoretical analysis of the complexity, along with empirical results on different graph sizes and densities. It would be helpful to see a comparison of the computational cost of the proposed method with existing integer-order GNNs, not just in terms of overall training time, but also in terms of memory usage and the number of operations. This analysis should also consider the impact of the fractional order parameter on the computational cost. For example, how does the computational cost scale with the fractional order, and are there specific values of the fractional order that are more computationally expensive than others? A more detailed analysis of the computational aspects would help readers understand the practical implications of using the proposed framework.

Finally, the impact of the fractional order on the performance of the proposed framework needs a more in-depth analysis. The authors should provide a more detailed explanation of how the fractional order parameter affects the model's ability to capture long-range dependencies in the graph. It would be beneficial to see a systematic study of how different values of the fractional order affect the model's performance on various node classification tasks. This analysis should include a discussion of the optimal range of fractional orders for different types of graphs and node feature distributions. The authors should also investigate whether there are any specific patterns or relationships between the fractional order and the model's performance, and provide insights into why these patterns exist. This would help readers understand how to choose the appropriate fractional order for their specific applications.

### Questions

1. What are the limitations of the proposed framework?
2. What is the computational complexity of the proposed framework?
3. How does the fractional order affect the performance of the proposed framework?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
