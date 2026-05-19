### Summary

The paper introduces a novel paradigm in reinforcement learning (RL) called submodular RL (SubRL), which focuses on optimizing non-additive and history-dependent rewards modeled using submodular set functions. These types of rewards are particularly relevant in applications such as coverage control, experiment design, and informative path planning, where the principle of diminishing returns applies. The authors propose an algorithm called SubPO, which is a policy gradient-based method inspired by greedy algorithms in submodular optimization. SubPO aims to maximize marginal gains and is shown to achieve optimal constant factor approximations in certain restricted settings. The paper also provides empirical evidence of the effectiveness and scalability of SubPO in various applications, including biodiversity monitoring, experiment design, and robotics tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper introduces a new paradigm in reinforcement learning (RL) by focusing on submodular reward functions, which is a novel and important contribution to the field.
2. The authors provide a comprehensive analysis of the theoretical limits of the SubRL framework, including a lower bound that establishes the hardness of approximation.
3. The proposed algorithm, SubPO, is inspired by the greedy algorithm in submodular optimization and is shown to be effective in practice, achieving optimal constant factor approximations in certain restricted settings.
4. The paper provides empirical evidence of the effectiveness and scalability of SubPO in various applications, demonstrating its practical utility.
5. The paper is well-written and clearly explains the concepts and contributions.

### Weaknesses

#### Some Related Works


#### comment

1. The paper primarily focuses on theoretical analysis and algorithm development, with limited discussion on practical implementation details and challenges. It would be beneficial to provide more insights into the practical aspects of implementing SubPO in real-world scenarios.
2. The paper could benefit from a more detailed comparison with existing RL algorithms and approaches, particularly those that also consider non-Markovian rewards or history-dependent objectives. This would help to better position the contributions of SubRL within the broader RL landscape.
3. While the paper provides empirical evidence of the effectiveness of SubPO, it would be helpful to include more detailed analysis of the results, such as comparisons with other algorithms and ablation studies to understand the impact of different components of SubPO.

### Suggestions

The paper introduces an interesting framework for submodular reinforcement learning, but it would benefit from a more thorough discussion of practical implementation challenges. For example, the paper could elaborate on how the submodular reward function is chosen and parameterized for different applications. In real-world scenarios, the reward function might not be known a priori and may need to be learned or approximated. The authors could discuss potential methods for learning or approximating submodular reward functions from data, and how these methods might affect the performance of SubPO. Furthermore, the paper could provide more details on the computational complexity of SubPO, especially in relation to the size of the state and action spaces. It would be useful to discuss how the algorithm scales with increasing problem complexity and whether there are any practical limitations to its applicability. A discussion of potential optimizations or approximations that could be used to improve the scalability of SubPO would also be valuable.

To better position the contributions of SubRL, the paper should include a more detailed comparison with existing RL algorithms that handle non-Markovian rewards or history-dependent objectives. While the paper mentions that standard RL algorithms are not directly applicable, it would be beneficial to discuss specific examples of such algorithms and explain why they are not suitable for submodular reward functions. For instance, the paper could compare SubPO with algorithms that use recurrent neural networks to model history-dependent policies, or with algorithms that use temporal difference learning to handle non-Markovian rewards. A detailed comparison would help to highlight the unique advantages of SubRL and clarify its niche within the broader RL landscape. Furthermore, the paper could discuss the limitations of SubRL and identify potential areas for future research, such as extending the framework to handle more complex reward functions or developing more efficient algorithms for submodular optimization.

Finally, the empirical evaluation of SubPO could be strengthened by including more detailed analysis of the results. The paper should provide more specific comparisons with other algorithms, including both standard RL algorithms and other submodular optimization methods. It would be useful to include ablation studies to understand the impact of different components of SubPO, such as the choice of policy parameterization or the specific submodular optimization algorithm used. The paper could also discuss the sensitivity of SubPO to different hyperparameter settings and provide guidelines for choosing appropriate values. A more thorough analysis of the empirical results would help to validate the effectiveness of SubPO and provide a more comprehensive understanding of its strengths and limitations.

### Questions

1. How does the performance of SubPO compare to other existing RL algorithms in terms of sample efficiency and scalability?
2. What are the limitations of the SubRL framework, and are there any potential extensions or modifications that could address these limitations?
3. Can the authors provide more insights into the practical implementation of SubPO in real-world scenarios, including potential challenges and solutions?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
