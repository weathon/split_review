### Summary

This paper introduces a novel approach to imitation learning (IL) using behavior foundation models (BFMs). The authors leverage recent advances in BFMs, based on successor measures, to enable fast and efficient IL from few expert demonstrations. They demonstrate that their method achieves state-of-the-art performance on several imitation learning tasks from the DeepMind Control Suite, outperforming existing offline IL algorithms while requiring significantly less time for policy learning.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper introduces a novel approach to imitation learning using behavior foundation models (BFMs) based on successor measures. This is a creative combination of existing techniques that allows for fast and efficient IL from few expert demonstrations.
- The authors provide a thorough theoretical analysis of their method, demonstrating that it satisfies the three properties required for effective IL: when pre-trained on unsupervised data, it can imitate any expert policy, it can implement different IL principles, and it can do so in a few seconds without solving any complex RL problem.
- The paper is well-written and easy to follow, with clear explanations of the proposed method and its theoretical foundations.
- The authors conduct extensive experiments on several imitation learning tasks from the DeepMind Control Suite, demonstrating that their method achieves state-of-the-art performance while requiring significantly less time for policy learning compared to existing offline IL algorithms.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a detailed analysis of the limitations of the proposed method. For example, it would be helpful to discuss the types of tasks or environments where FB-IL may not perform well.
- The paper does not discuss the sensitivity of the proposed method to the choice of hyperparameters. It would be helpful to provide guidelines for selecting the optimal hyperparameters for different tasks.
- The paper does not provide a comparison of the computational cost of FB-IL with other imitation learning methods. It would be helpful to provide a more detailed analysis of the computational complexity of the proposed method and compare it with other methods.

### Suggestions

The paper would benefit from a more thorough discussion of the limitations of the proposed FB-IL method. Specifically, the authors should explore scenarios where the forward-backward (FB) framework might struggle, such as tasks with highly stochastic dynamics or environments where the expert demonstrations are not sufficiently informative. For example, in environments with sparse rewards, the pre-trained FB model might not effectively capture the underlying dynamics, leading to suboptimal imitation policies. Furthermore, the paper should investigate the impact of the quality and diversity of the expert demonstrations on the performance of FB-IL. A detailed analysis of these factors would provide a more complete understanding of the applicability and robustness of the proposed method. It would also be beneficial to discuss the potential failure modes of the method, such as when the expert demonstrations are noisy or contain errors.

In addition to the limitations, the paper should include a more detailed analysis of the hyperparameter sensitivity of the FB-IL method. The authors should provide a systematic study of how different hyperparameters, such as the learning rate, the number of training iterations, and the architecture of the pre-trained model, affect the performance of the method. This analysis should include a discussion of the trade-offs between different hyperparameter settings and provide guidelines for selecting the optimal hyperparameters for different tasks. For example, the authors could investigate how the learning rate affects the convergence speed and the final performance of the method, or how the size of the pre-trained model affects the generalization ability of the imitation policy. Furthermore, the authors should provide a discussion of the computational cost of the proposed method, including the time required for pre-training the FB model and the time required for imitation learning. A comparison of the computational cost with other imitation learning methods would be helpful to assess the practical applicability of the proposed method.

Finally, the paper should provide a more detailed analysis of the computational complexity of the proposed method. The authors should provide a theoretical analysis of the time and space complexity of the FB-IL method, and compare it with the complexity of other imitation learning methods. This analysis should include a discussion of the factors that affect the computational cost, such as the size of the state and action spaces, the number of expert demonstrations, and the complexity of the pre-trained model. Furthermore, the authors should provide a practical analysis of the computational cost of the method, including the time required for pre-training the FB model and the time required for imitation learning. This analysis should be performed on different hardware platforms to provide a more comprehensive understanding of the computational requirements of the method.

### Questions

- How does the proposed method handle tasks with sparse rewards or environments with high levels of stochasticity?
- What are the limitations of the proposed method in terms of the quality and diversity of the expert demonstrations?
- How sensitive is the proposed method to the choice of hyperparameters?
- What is the computational cost of the proposed method compared to other imitation learning methods?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
