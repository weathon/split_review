### Summary

This paper introduces a novel offline reinforcement learning method called Contrastive Diffuser (CDiffuser). The core idea of CDiffuser is to use contrastive learning to guide the generation of trajectories towards high-return states and away from low-return states. Specifically, CDiffuser treats states with high returns as positive samples and states with low returns as negative samples. Then, it uses a contrastive mechanism to constrain the states in the generated trajectories to be more aligned with high-return states and less aligned with low-return states. The authors evaluate CDiffuser on 14 D4RL benchmarks and show that it outperforms existing offline RL methods.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and effective. The authors provide a thorough evaluation of CDiffuser on 14 D4RL benchmarks, demonstrating its superiority over existing offline RL methods.
3. The authors provide a detailed analysis of the results, including ablation studies and further investigations. The results show that the contrastive mechanism benefits the performance of CDiffuser, and applying only the high-return samples in training diminishes benefits in some cases.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is a simple extension of the existing contrastive learning method. The core idea of using contrastive learning to guide the generation of trajectories towards high-return states is not novel. The specific implementation details, such as the choice of positive and negative samples, and the loss function, are also not significantly different from existing contrastive learning frameworks. The paper does not adequately demonstrate a substantial theoretical advancement or a novel application of contrastive learning in the context of offline RL.
2. The paper does not provide a detailed analysis of the computational cost of the proposed method. The use of contrastive learning and diffusion models can be computationally expensive, and the paper lacks a thorough discussion of the computational overhead compared to other offline RL methods. It is unclear how the method scales with the size of the dataset and the complexity of the environment. The paper should include a detailed breakdown of the computational cost, including training time, memory usage, and inference time.
3. The paper does not discuss the limitations of the proposed method. For example, the method may not perform well in environments with sparse rewards or with complex state spaces. The paper should include a discussion of the scenarios where the method is likely to fail and the potential reasons for these failures. It would also be beneficial to explore the sensitivity of the method to hyperparameter settings and the choice of positive and negative samples.

### Suggestions

The paper would benefit from a more in-depth analysis of the novelty of the proposed method. While the application of contrastive learning to offline RL is interesting, the paper needs to clearly articulate the specific challenges and adaptations required to make this approach effective in this domain. The authors should provide a more detailed comparison with existing contrastive learning methods, highlighting the unique aspects of their approach and the specific advantages it offers for offline RL. This comparison should go beyond a superficial description and delve into the theoretical underpinnings and practical implications of the proposed method. For example, the authors could analyze the convergence properties of their method and compare it with other contrastive learning approaches. Furthermore, the authors should discuss the limitations of their approach and potential avenues for future research. This could include exploring alternative contrastive learning objectives, investigating different ways of defining positive and negative samples, and analyzing the sensitivity of the method to hyperparameter settings.

To address the computational cost concerns, the paper should include a detailed analysis of the time and memory requirements of the proposed method. This analysis should include a breakdown of the computational cost associated with each step of the algorithm, such as the diffusion model training, the contrastive loss calculation, and the trajectory generation. The authors should also compare the computational cost of their method with other offline RL methods, including both model-based and model-free approaches. This comparison should be done under various conditions, such as different dataset sizes and environment complexities. Furthermore, the paper should discuss potential strategies for reducing the computational cost of the method, such as using more efficient diffusion models or optimizing the implementation of the contrastive loss function. The authors could also explore techniques for parallelizing the computation to improve the overall efficiency of the method. A thorough analysis of the computational cost is crucial for assessing the practical applicability of the proposed method.

Finally, the paper should include a more comprehensive discussion of the limitations of the proposed method. The authors should explore the performance of their method in environments with sparse rewards and complex state spaces, and discuss the potential reasons for any observed limitations. The paper should also investigate the sensitivity of the method to hyperparameter settings and the choice of positive and negative samples. For example, the authors could conduct ablation studies to analyze the impact of different hyperparameters on the performance of the method. They could also explore different strategies for selecting positive and negative samples, such as using different distance metrics or clustering algorithms. The paper should also discuss potential modifications to the method that could address these limitations and improve its robustness. A thorough discussion of the limitations is essential for providing a balanced and realistic assessment of the proposed method.

### Questions

1. How does the proposed method compare to other contrastive learning methods in terms of performance and computational cost?
2. What are the limitations of the proposed method, and how can they be addressed in future work?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
