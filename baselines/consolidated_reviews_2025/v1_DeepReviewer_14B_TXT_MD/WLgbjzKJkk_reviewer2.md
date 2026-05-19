### Summary

This paper proposes a coopetition label assignment for training tracking and detection queries for e2e-MOT with high efficiency and develops a one-to-set matching strategy with a novel shadow concept to address the hungry for positive training samples and enhance generalization ability. The approach achieves superior performance on multiple benchmarks, while it functions as an efficient tool to boosting the performance of end-toend Transformer-based MOT.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well written and easy to follow.
- The proposed coopetition label assignment is simple and effective.
- The proposed one-to-set matching strategy is novel and interesting.
- The approach achieves state-of-the-art performance on multiple benchmarks.

### Weaknesses

#### Some Related Works


#### comment

 - The authors should provide more analysis and visualization results on the effectiveness of the proposed coopetition label assignment and one-to-set matching strategy.
- The authors should provide more analysis on the choice of hyper-parameters, such as the number of shadows.

### Suggestions

The paper introduces a coopetition label assignment and a one-to-set matching strategy, which are interesting concepts. However, the evaluation of these components needs to be more thorough. Specifically, the analysis of the coopetition label assignment should include a more detailed breakdown of how it impacts the training process, such as the convergence speed and the final performance of both detection and tracking queries. It would be beneficial to see visualizations that show the matching process between detection and tracking queries under different label assignments, highlighting the advantages of the proposed coopetition approach. Furthermore, the analysis should explore the sensitivity of the method to different levels of coopetition, perhaps by varying the number of detection queries that are allowed to compete for the same tracking target. This would provide a more comprehensive understanding of the method's behavior and limitations.

Regarding the one-to-set matching strategy, the paper should provide more insights into how the shadow sets are constructed and how the size of the shadow set affects the performance. The current analysis lacks a detailed exploration of the trade-offs between the size of the shadow set and the computational cost, as well as the impact on the final tracking performance. It would be helpful to see a more granular analysis of how different sizes of shadow sets affect the precision and recall of the tracking results. For example, the authors could analyze the performance of the method with different shadow set sizes on different datasets, which may have varying levels of object density and occlusion. This would help to determine the optimal shadow set size for different scenarios and provide a more robust evaluation of the proposed method.

Finally, the paper should include a more detailed discussion on the choice of hyper-parameters, particularly the number of shadows. While the authors mention that this parameter is determined through ablation studies, they should provide more details on the specific ablation experiments that were conducted. For example, they could show a plot of the performance of the method as a function of the number of shadows, which would help to visualize the trade-offs involved. Furthermore, the authors should discuss the potential impact of the number of shadows on the computational cost of the method. It would also be beneficial to explore the sensitivity of the method to other hyper-parameters, such as the learning rate and the batch size, and provide guidelines for choosing appropriate values for these parameters.

### Questions

Please see the Weaknesses.

### Rating

5: marginally below the acceptance threshold

### Confidence

5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

**********
