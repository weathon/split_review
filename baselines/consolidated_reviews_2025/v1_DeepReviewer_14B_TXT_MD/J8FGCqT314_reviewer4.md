### Summary

This paper proposes a new method called D2T2 (Decision Transformer with Temporal Difference via Steering Guidance) to improve the performance of Decision Transformers (DT) in stochastic environments. The authors first analyze the limitations of DT in stochastic environments and show that the performance of DT can be significantly degraded due to the growing variance of returns-to-go (RTGs) accumulated over the horizon. To address this issue, they propose D2T2, which integrates DT with approximated TD learning. D2T2 maps the current state to a guiding vector that steers DT towards high-reward regions where the expected returns are approximated by TD learning. The authors demonstrate the superior performance of D2T2 compared to state-of-the-art offline reinforcement learning methods on various stochastic tasks and D4RL environments.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper provides a novel perspective on the limitations of Decision Transformers in stochastic environments and proposes a new method to address this issue.
2. The proposed method, D2T2, is well-motivated and theoretically grounded.
3. The authors conduct extensive experiments on various stochastic tasks and D4RL environments to demonstrate the effectiveness of D2T2.
4. The paper is well-written and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational complexity of D2T2. It would be helpful to understand how the computational cost of D2T2 compares to that of other methods, especially in terms of training time and memory requirements.
2. The paper does not discuss the sensitivity of D2T2 to hyperparameters. It would be helpful to understand how the performance of D2T2 is affected by different hyperparameter settings.

### Suggestions

The paper would benefit from a more thorough analysis of the computational complexity of the proposed D2T2 method. Specifically, the authors should provide a detailed breakdown of the computational cost associated with each component of the algorithm, including the temporal difference learning and the decision transformer. This analysis should consider how the computational cost scales with the size of the state and action spaces, the length of the trajectories, and the dimension of the guiding vector. Furthermore, it would be helpful to compare the computational cost of D2T2 with that of other state-of-the-art offline reinforcement learning methods. This comparison should include both training time and memory requirements. For example, the authors could provide a table that compares the number of parameters, the training time per epoch, and the memory usage for D2T2 and other methods on a specific benchmark dataset. This would allow readers to better understand the practical implications of using D2T2 in different settings.

In addition to the computational complexity analysis, the paper should also include a more detailed analysis of the sensitivity of D2T2 to hyperparameters. The authors should investigate how the performance of D2T2 is affected by different learning rates for the temporal difference learning component and the decision transformer component. It would be beneficial to provide a sensitivity analysis that shows how the performance varies with different learning rates, and to identify the optimal learning rate for each component. Furthermore, the authors should investigate the impact of the discount factor on the performance of D2T2. It would be helpful to provide a plot that shows how the performance varies with different discount factors, and to identify the optimal discount factor for the method. This analysis should also consider the impact of other hyperparameters, such as the batch size and the number of training epochs. A more thorough analysis of the sensitivity to hyperparameters would help readers to better understand the robustness of the method and to apply it effectively in different settings.

Finally, the paper could be improved by providing more details on the implementation of the D2T2 method. For example, the authors could provide more details on the architecture of the decision transformer, the choice of the temporal difference learning algorithm, and the method used to generate the guiding vector. It would also be helpful to provide more details on the training procedure, such as the optimization algorithm used, the loss function, and the regularization techniques. Providing these details would make it easier for other researchers to reproduce the results and to build upon the proposed method.

### Questions

1. Could the authors provide more details on the computational complexity of D2T2 and how it compares to other methods?
2. Could the authors discuss the sensitivity of D2T2 to hyperparameters and provide guidelines for selecting appropriate hyperparameter values?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
