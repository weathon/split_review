### Summary

This paper proposes a method called CO-MOT to boost the performance of end-to-end Transformer-based MOT. The authors investigate the issues in the existing end-to-end MOT using Transformer and find that the label assignment can not fully explore the detection queries as detection and tracking queries are exclusive to each other. Thus, the authors introduce a coopetition label assignment (COLA). Additionally, the authors develop a shadow set as units to augment the queries, mitigating the unbalanced training caused by the one-to-one matching strategy. The proposed method achieves significant performance gains on multiple datasets in an efficient manner.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The experiments are thorough, covering multiple datasets and comparing the proposed method with a wide range of state-of-the-art approaches.
3. The proposed methods achieve significant performance improvements on multiple benchmarks, demonstrating their effectiveness.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed analysis of the computational cost of the proposed methods, especially the shadow set strategy, which could be computationally expensive.
2. The coopetition label assignment strategy is not thoroughly compared with other label assignment strategies, such as one-to-many assignment, and it is unclear how the coopetition strategy specifically addresses the limitations of existing methods.
3. The paper does not provide a clear explanation of how the shadow set strategy mitigates the one-to-one assignment problem, and it is not clear how the size of the shadow set affects the performance of the model.

### Suggestions

The paper should include a more detailed analysis of the computational cost associated with the proposed methods, particularly the shadow set strategy. While the authors mention efficiency gains, a more rigorous analysis, including a breakdown of the computational complexity of each component, would be beneficial. For example, the paper could provide a theoretical analysis of the time complexity of the shadow set operations, and compare it to the complexity of other label assignment strategies. Furthermore, empirical results on the inference time and memory usage of the proposed method, compared to the baselines, should be included. This would provide a more comprehensive understanding of the practical implications of using the proposed methods. The analysis should also consider the impact of different shadow set sizes on the computational cost and performance trade-offs.

To strengthen the analysis of the coopetition label assignment strategy, the paper should include a more detailed comparison with other label assignment strategies, such as one-to-many assignment. The authors should explain how the coopetition strategy specifically addresses the limitations of existing methods, such as the lack of global optimization and the potential for tracking terminal issues. A more in-depth analysis of the differences between the coopetition strategy and other strategies, including a discussion of the advantages and disadvantages of each, would be beneficial. For example, the paper could include a theoretical analysis of the convergence properties of the coopetition strategy, and compare it to the convergence properties of other strategies. Additionally, the paper should provide more empirical evidence to support the claim that the coopetition strategy improves tracking accuracy, and compare it to the performance of other label assignment strategies.

Finally, the paper should provide a more detailed explanation of how the shadow set strategy mitigates the one-to-one assignment problem, and how the size of the shadow set affects the performance of the model. The authors should explain the specific mechanisms by which the shadow set strategy enhances the diversity and robustness of the model. For example, the paper could include a theoretical analysis of how the shadow set strategy affects the feature representation of the tracked objects, and how this affects the tracking performance. Furthermore, the paper should include an ablation study to investigate the impact of the shadow set size on the performance of the model, and provide a clear explanation of how to choose the optimal size for different datasets and scenarios. This would provide a more comprehensive understanding of the role of the shadow set strategy in the proposed method.

### Questions

See the weaknesses.

### Rating

6

### Confidence

4

**********
