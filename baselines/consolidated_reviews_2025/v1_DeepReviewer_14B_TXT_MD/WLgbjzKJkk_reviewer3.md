### Summary

This paper proposes a novel coopetition label assignment strategy (COLA) and a shadow set concept to improve the performance of end-to-end Transformer-based multi-object tracking (MOT). The authors identify the limitations of existing e2e-MOT methods, which have not surpassed non-end-to-end tracking-by-detection methods, and attribute it to the label assignment strategy during training. They propose COLA to alleviate the problem of unbalanced training, where scarce positive samples are assigned to detection queries. Additionally, they introduce the shadow set concept to mitigate the sensitivity of one query for one object to prediction noises. The proposed method, CO-MOT, achieves superior performance on multiple MOT benchmarks, including DanceTrack, BDD100K, and MOT17, without extra computational costs. The paper provides extensive ablations and visualizations to demonstrate the effectiveness of the proposed components.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper proposes a novel coopetition label assignment strategy (COLA) that addresses the issue of unbalanced training in e2e-MOT methods. By adding tracked objects to the matching targets for detection queries, COLA allows for a more balanced assignment of positive samples, which improves the detection performance.
2. The paper introduces the concept of shadow sets, where each query is augmented with multiple shadow queries by adding limited disturbance to itself. This one-to-set matching strategy enhances the discriminative training by optimizing the most challenging query in the set with the maximal cost, and improves the generalization ability of the model.
3. The proposed method, CO-MOT, achieves superior performance on multiple MOT benchmarks, including DanceTrack, BDD100K, and MOT17, without extra computational costs. The paper provides extensive ablations and visualizations to demonstrate the effectiveness of the proposed components.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed explanation of the coopetition label assignment strategy (COLA) and the shadow set concept. It is not clear how these strategies are implemented in practice and how they interact with each other. For example, the description of COLA lacks specifics on how the tracked objects are incorporated into the matching targets for detection queries. It would be beneficial to include a step-by-step algorithm or pseudocode to clarify the implementation details. Similarly, the explanation of the shadow set concept is somewhat vague. The paper mentions adding 'limited disturbance' to the queries, but it does not specify the nature of this disturbance or how it is controlled. A more precise description of the disturbance mechanism and its parameters is needed.
2. The paper could provide more insights into the limitations of the proposed method and potential directions for future research. For example, it is not clear how the method performs in challenging scenarios such as occlusions, fast-moving objects, or crowded scenes. The paper should include a discussion of the failure cases and the reasons behind them. Furthermore, the paper does not explore the sensitivity of the method to hyperparameter settings, such as the number of shadow queries or the parameters of the disturbance mechanism. A more thorough analysis of these aspects would be valuable.
3. The paper could benefit from a more thorough comparison with existing methods. While the paper compares the proposed method with several baselines, it does not provide a detailed analysis of the differences between the proposed method and the state-of-the-art methods. For example, it is not clear how the proposed method compares with other transformer-based MOT methods in terms of computational complexity, memory usage, and training time. A more comprehensive comparison would help to better understand the advantages and disadvantages of the proposed method.

### Suggestions

To address the lack of clarity regarding the implementation of COLA, the authors should provide a detailed algorithm or pseudocode that outlines the steps involved in incorporating tracked objects into the matching targets for detection queries. This should include a clear definition of the data structures used, the matching criteria, and the update rules for the assignment. For instance, the algorithm should specify how the tracked objects are represented, how they are matched with detection queries, and how the matching is used to update the model parameters. Furthermore, the authors should clarify the specific mechanism used to add 'limited disturbance' to the queries in the shadow set concept. This should include a mathematical formulation of the disturbance, the parameters that control its magnitude and type, and the rationale behind the chosen disturbance strategy. For example, if Gaussian noise is added, the authors should specify the mean and variance of the noise and explain why these parameters were chosen. If a different type of disturbance is used, it should be described in detail with clear mathematical definitions.

To enhance the discussion of the method's limitations, the authors should include a qualitative analysis of the failure cases, providing specific examples of scenarios where the method performs poorly. This should include a discussion of the reasons behind these failures, such as occlusions, fast-moving objects, or crowded scenes. The authors should also conduct a sensitivity analysis of the method to hyperparameter settings, such as the number of shadow queries and the parameters of the disturbance mechanism. This analysis should include a systematic evaluation of the method's performance with different hyperparameter values, and it should provide guidelines for choosing appropriate values for these parameters. For example, the authors could show how the performance varies with different numbers of shadow queries and different magnitudes of the disturbance. This analysis would help to understand the robustness of the method and its sensitivity to hyperparameter settings.

Finally, the authors should provide a more comprehensive comparison with existing transformer-based MOT methods, including a detailed analysis of the differences in computational complexity, memory usage, and training time. This comparison should not only focus on the performance metrics but also on the practical aspects of the methods. For example, the authors could compare the number of parameters, the FLOPs, and the training time of their method with other state-of-the-art methods. This would provide a more complete picture of the advantages and disadvantages of the proposed method and help to better understand its practical applicability. Furthermore, the authors should discuss the potential limitations of the proposed method in terms of scalability and robustness to different types of data.

### Questions

1. How does the coopetition label assignment strategy (COLA) specifically address the issue of unbalanced training in e2e-MOT methods? Can you provide more details on the implementation of COLA and how it differs from existing label assignment strategies?
2. How does the shadow set concept mitigate the sensitivity of one query for one object to prediction noises? Can you provide more details on the implementation of the shadow set and how it affects the performance of the model?
3. What are the limitations of the proposed method, and what are the potential directions for future research?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
