### Summary

The paper proposes a new method called D2T2, which is an extension of Decision Transformer (DT) that incorporates temporal difference (TD) learning to improve performance in stochastic environments. The authors identify that the performance degradation of DT in stochastic environments is due to the accumulation of variance in returns-to-go (RTG) signals. To address this, D2T2 uses a learned steering guidance function that provides a more stable signal for DT, reducing the variance of RTG and improving the model's ability to handle stochasticity. The authors demonstrate the effectiveness of D2T2 through experiments on various stochastic tasks and D4RL benchmarks, showing that it outperforms state-of-the-art offline reinforcement learning methods.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper provides a theoretical analysis of the performance degradation of DT in stochastic environments, identifying the variance of RTG signals as the key factor.
2. The proposed method, D2T2, is simple yet effective, incorporating TD learning to provide a more stable guidance signal for DT.
3. The authors conduct extensive experiments on various stochastic tasks and D4RL benchmarks, demonstrating the effectiveness of D2T2 compared to state-of-the-art offline reinforcement learning methods.
4. The paper is well-written and easy to follow, with clear explanations of the proposed method and experimental results.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational cost of D2T2 compared to the original DT and other baselines. This makes it difficult to assess the practical applicability of the method, especially in resource-constrained environments. Specifically, the paper lacks a breakdown of the time spent on different components of the algorithm, such as the transformer encoding, the temporal difference learning, and the policy optimization. Without this, it is hard to understand where the computational bottlenecks lie and how they might be addressed.
2. The paper does not provide a detailed analysis of the sensitivity of D2T2 to the choice of hyperparameters, such as the discount factor and the learning rate. This makes it difficult to reproduce the results and to apply the method to new tasks. The paper should include a sensitivity analysis showing how the performance of D2T2 varies with different hyperparameter settings, and provide guidance on how to choose appropriate values for these parameters.
3. The paper does not provide a detailed analysis of the limitations of D2T2, such as its performance in environments with very long time horizons or very complex state spaces. This makes it difficult to understand the scope of applicability of the method and to identify potential areas for future research. The paper should discuss the potential challenges of applying D2T2 to more complex environments, and suggest possible solutions or future research directions.

### Suggestions

The paper would benefit from a more thorough analysis of the computational cost of D2T2. The authors should provide a detailed breakdown of the time spent on each component of the algorithm, including the transformer encoding, the temporal difference learning, and the policy optimization. This analysis should be performed on different hardware configurations to understand how the computational cost scales with the size of the dataset and the complexity of the environment. Furthermore, the authors should compare the computational cost of D2T2 with that of the original DT and other state-of-the-art offline reinforcement learning methods. This would allow readers to better assess the practical applicability of the method and to identify potential areas for optimization. For example, the authors could provide a table showing the training time and memory usage of D2T2 and other methods as a function of the dataset size and the horizon length.

To improve the reproducibility of the results, the authors should conduct a sensitivity analysis of D2T2 to the choice of hyperparameters. This analysis should include a systematic evaluation of how the performance of D2T2 varies with different values of the discount factor, the learning rate, and other relevant hyperparameters. The authors should provide a clear explanation of how these hyperparameters were chosen and how they affect the performance of the method. This analysis should also include a discussion of the potential trade-offs between different hyperparameter settings. For example, the authors could show how the performance of D2T2 changes as the discount factor is increased, and how this affects the stability of the training process. The authors should also provide practical guidance on how to choose appropriate values for these hyperparameters in new tasks.

Finally, the paper should include a more detailed discussion of the limitations of D2T2. The authors should discuss the potential challenges of applying D2T2 to environments with very long time horizons or very complex state spaces. For example, the authors could discuss how the performance of D2T2 might degrade in environments with very long time horizons, due to the accumulation of errors in the learned guidance signal. The authors should also discuss the potential challenges of applying D2T2 to environments with very complex state spaces, such as those with high-dimensional observations. The authors should suggest possible solutions or future research directions to address these limitations. For example, the authors could suggest using techniques such as hierarchical reinforcement learning or model-based reinforcement learning to improve the performance of D2T2 in complex environments.

### Questions

1. How does the computational cost of D2T2 compare to the original DT and other state-of-the-art offline reinforcement learning methods?
2. How sensitive is D2T2 to the choice of hyperparameters, such as the discount factor and the learning rate?
3. What are the limitations of D2T2, and how can it be improved for environments with very long time horizons or very complex state spaces?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
