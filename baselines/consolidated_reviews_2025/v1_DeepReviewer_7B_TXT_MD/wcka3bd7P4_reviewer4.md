### Summary

This paper proposes a novel continuous graph neural network framework, called FROND, which generalizes existing integer-order continuous GNNs by incorporating non-local fractional derivatives. The authors provide an interpretation of the node feature updating process from a non-Markovian random walk perspective and theoretically analyze the oversmoothing issue. Experiments on node classification tasks demonstrate the effectiveness of the proposed framework.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow. The authors provide a clear motivation for the proposed framework and a detailed explanation of the underlying mathematical concepts.

2. The proposed framework is novel and has the potential to generalize existing integer-order continuous GNNs. The authors provide a thorough theoretical analysis of the oversmoothing issue and demonstrate the effectiveness of the proposed framework on node classification tasks.

3. The authors provide a comprehensive set of experiments to validate the effectiveness of the proposed framework. The results show that the proposed framework outperforms existing integer-order continuous GNNs on several benchmark datasets.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed framework is a generalization of existing integer-order continuous GNNs. The authors should discuss the limitations of the proposed framework.

2. The authors should provide a more detailed analysis of the computational complexity of the proposed framework.

3. The authors should provide a more detailed analysis of the impact of the fractional order on the performance of the proposed framework.

### Suggestions

The paper introduces a novel continuous graph neural network framework, FROND, which generalizes existing integer-order continuous GNNs using non-local fractional derivatives. While the core idea of incorporating fractional derivatives is promising, the paper would benefit from a more thorough discussion of the practical implications and limitations of this approach. Specifically, the authors should delve deeper into the conditions under which the fractional-order approach might be advantageous compared to traditional integer-order methods. For instance, are there specific graph structures or node feature distributions where the fractional-order approach provides a significant performance boost, and conversely, are there scenarios where it might lead to instability or convergence issues? A more detailed analysis of these aspects would help to clarify the niche for which the proposed framework is best suited.

Furthermore, the paper lacks a detailed analysis of the computational complexity of the proposed FROND framework. While the authors mention that the framework generalizes existing integer-order methods, they do not provide a rigorous analysis of how the fractional derivatives impact the computational cost. It is crucial to understand how the computational cost scales with the size of the graph, the number of fractional orders, and the dimensionality of the node features. A theoretical analysis of the time and space complexity, along with empirical results on different graph sizes and densities, would be essential to assess the practical applicability of the proposed framework. This analysis should also consider the memory requirements for storing intermediate results, especially for large graphs. Without a clear understanding of the computational overhead, it is difficult to evaluate the trade-offs between performance gains and computational costs.

Finally, the paper should provide a more in-depth analysis of the impact of the fractional order on the performance of the proposed framework. While the authors mention that the fractional order controls the extent of memorization, they do not provide a systematic study of how different values of the fractional order affect the model's ability to capture long-range dependencies in the graph. It would be beneficial to see a more detailed analysis of the relationship between the fractional order and the model's performance on various node classification tasks. For example, are there specific ranges of fractional orders that are more suitable for certain types of graphs or node feature distributions? A more thorough exploration of this aspect would help to guide practitioners in selecting the appropriate fractional order for their specific applications. The authors should also investigate whether there are any optimal strategies for tuning the fractional order to achieve the best performance.

### Questions

Please refer to the weaknesses.

### Rating

8: accept, good paper

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
