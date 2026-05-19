### Summary

This paper proposes a novel framework, Empowerment through Causal Learning (ECL), which integrates causal structure learning with empowerment-driven exploration in model-based reinforcement learning. The authors hypothesize that empowerment, when coupled with causal understanding, can improve an agent's controllability over its environment and enhance learning efficiency. ECL operates by first training a causal dynamics model from collected data, then maximizing empowerment under the causal structure for exploration. The data gathered through this exploration is used to iteratively update the causal model, making it more controllable than dense models without causal structure. In downstream task learning, an intrinsic curiosity reward is included to balance causality and mitigate overfitting. The framework is method-agnostic and can integrate various causal discovery methods. The authors evaluate ECL combined with three causal discovery methods across six environments, including pixel-based tasks, and demonstrate its superior performance compared to other causal MBRL methods in terms of causal discovery, sample efficiency, and asymptotic performance.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel framework, Empowerment through Causal Learning (ECL), which combines causal structure learning with empowerment-based exploration in model-based reinforcement learning. This approach is innovative and addresses the limitations of existing methods by actively leveraging causal structures to guide exploration and improve controllability.

2. The paper is well-organized and clearly written. The authors provide a detailed explanation of the ECL framework, including the three main steps: model learning, model optimization, and policy learning. The use of figures and examples, such as the robot manipulation task, helps to illustrate the concepts and the overall workflow of the framework.

3. The paper demonstrates the effectiveness of ECL through extensive experiments across six environments, including both simple and complex tasks, as well as pixel-based environments. The results show that ECL outperforms other causal MBRL methods in terms of causal discovery accuracy, sample efficiency, and asymptotic performance.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational complexity of the ECL framework. Understanding the computational requirements is crucial for assessing the scalability and practicality of the method, especially in more complex environments.

2. The paper could benefit from a more thorough discussion of the limitations of the ECL framework. For instance, how does the performance of ECL degrade in environments with highly stochastic transitions or when the causal structure changes over time?

3. The paper does not provide a detailed analysis of the sensitivity of the ECL framework to hyperparameters. A thorough analysis of how different hyperparameters affect the performance of ECL would be valuable for practitioners looking to implement the framework.

### Suggestions

The paper would benefit from a more rigorous analysis of the computational demands of the Empowerment through Causal Learning (ECL) framework. Specifically, a breakdown of the time complexity for each stage—model learning, model optimization, and policy learning—would be valuable. For instance, the causal discovery step, which involves constraint-based or score-based methods, can have varying computational costs depending on the chosen algorithm and the size of the state space. Similarly, the empowerment calculation, which involves entropy estimation, can be computationally intensive, especially in high-dimensional state spaces. A detailed analysis should include not only the asymptotic time complexity but also the practical runtime measurements on the environments used in the experiments. This would allow for a better understanding of the scalability of ECL and its suitability for different types of problems. Furthermore, it would be beneficial to compare the computational cost of ECL with other model-based reinforcement learning methods, both causal and non-causal, to provide a clearer picture of its relative efficiency.

In addition to computational complexity, the paper should also explore the robustness of the ECL framework under various challenging conditions. For example, the performance of causal discovery algorithms can be significantly affected by noisy or incomplete data. It would be important to analyze how ECL performs when the observed data is limited or when the environment contains stochastic transitions that are not captured by the causal model. Furthermore, the paper should investigate the sensitivity of ECL to violations of the assumption of a static causal structure. In many real-world scenarios, the underlying causal relationships may change over time, and it is important to understand how ECL would adapt to such non-stationarities. This could involve experiments in environments with time-varying causal structures or by introducing perturbations to the environment that alter the causal relationships. A thorough analysis of these limitations would provide a more complete picture of the applicability of ECL.

Finally, a more detailed hyperparameter analysis is needed to ensure the practical applicability of the ECL framework. The paper should provide a sensitivity analysis of the key hyperparameters, such as the learning rates for the different models, the regularization parameters for causal discovery, and the parameters related to the empowerment calculation. This analysis should include not only the final performance metrics but also the convergence speed and the stability of the learning process. It would be beneficial to show how the performance of ECL varies across different hyperparameter settings and to provide guidelines for selecting appropriate values for different types of environments. This would make it easier for practitioners to implement ECL and to adapt it to their specific needs. Furthermore, the paper should discuss the potential interactions between different hyperparameters and how these interactions can affect the overall performance of the framework.

### Questions

1. How does the computational complexity of the ECL framework compare to other model-based reinforcement learning methods, both causal and non-causal?

2. What are the limitations of the ECL framework, and how does its performance degrade in environments with highly stochastic transitions or changing causal structures?

3. How sensitive is the ECL framework to hyperparameters, and how do different hyperparameter settings affect the performance of the framework?

### Rating

6

### Confidence

3

**********
