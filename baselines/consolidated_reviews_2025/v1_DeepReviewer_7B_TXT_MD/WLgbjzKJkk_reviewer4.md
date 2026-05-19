### Summary

This paper addresses the limitations of end-to-end multi-object tracking (e2e-MOT) methods, particularly the label assignment strategy that leads to tracking terminal without renewal or re-initialization. The authors propose a coopetition label assignment (COLA) for training tracking and detection queries, allowing tracked objects to be reassigned to detection queries in intermediate decoders. Additionally, they introduce a one-to-set matching strategy with a novel shadow concept, where each individual query is augmented with multiple shadow queries by adding limited disturbance to itself. This approach enhances the diversity of training samples and improves generalization. The proposed method achieves state-of-the-art performance on multiple benchmarks, demonstrating its effectiveness and efficiency.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow, with clear explanations of the proposed methods.
2. The experiments are thorough, covering multiple datasets and comparing the proposed method with a wide range of state-of-the-art approaches.
3. The proposed methods achieve significant performance improvements on multiple benchmarks, demonstrating their effectiveness.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed analysis of the computational cost of the proposed methods, especially the shadow set strategy, which could be computationally expensive.
2. The coopetition label assignment strategy is not thoroughly compared with other label assignment strategies, such as one-to-many assignment, and it is unclear how the coopetition strategy specifically addresses the limitations of existing methods.
3. The paper does not provide a clear explanation of how the shadow set strategy mitigates the one-to-one assignment problem, and it is not clear how the size of the shadow set affects the performance of the model.

### Suggestions

The paper would benefit from a more rigorous analysis of the computational overhead introduced by the proposed methods, particularly the shadow set strategy. While the authors mention efficiency gains, a detailed breakdown of the computational complexity of each component is needed. For instance, the paper should provide a theoretical analysis of the time complexity of the shadow set operations, comparing it to the complexity of other label assignment strategies. Furthermore, empirical results on the inference time and memory usage of the proposed method, compared to the baselines, should be included. This would provide a more comprehensive understanding of the practical implications of using the proposed methods, especially in resource-constrained environments. The analysis should also consider the impact of different shadow set sizes on the computational cost and performance trade-offs, providing a clear understanding of the trade-offs involved in using this strategy.

To strengthen the analysis of the coopetition label assignment strategy, the paper should include a more detailed comparison with other label assignment strategies, such as one-to-many assignment. The authors should explain how the coopetition strategy specifically addresses the limitations of existing methods, such as the lack of global optimization and the potential for tracking terminal issues. A more in-depth analysis of the differences between the coopetition strategy and other strategies, including a discussion of the advantages and disadvantages of each, would be beneficial. For example, the paper could include a theoretical analysis of the convergence properties of the coopetition strategy, and compare it to the convergence properties of other strategies. Additionally, the paper should provide more empirical evidence to support the claim that the coopetition strategy improves tracking accuracy, and compare it to the performance of other label assignment strategies. This would provide a more robust justification for the proposed approach.

Finally, the paper should provide a more detailed explanation of how the shadow set strategy mitigates the one-to-one assignment problem, and how the size of the shadow set affects the performance of the model. The authors should explain the specific mechanisms by which the shadow set strategy enhances the diversity and robustness of the model. For example, the paper could include a theoretical analysis of how the shadow set strategy affects the feature representation of the tracked objects, and how this affects the tracking performance. Furthermore, the paper should include an ablation study to investigate the impact of the shadow set size on the performance of the model, and provide a clear explanation of how to choose the optimal size for different datasets and scenarios. This would provide a more comprehensive understanding of the role of the shadow set strategy in the proposed method, and how it contributes to the overall performance gains.

### Questions

1. How does the coopetition label assignment strategy compare to other label assignment strategies, such as one-to-many assignment, in terms of performance and computational cost?
2. How does the shadow set strategy specifically address the one-to-one assignment problem, and what is the impact of the shadow set size on the performance of the model?

### Rating

8

### Confidence

4

**********
