### Summary

The paper introduces a novel cooperative mean field game model on Chung-Lu graphs, which are particularly suitable for modeling sparse networks with power law degree distributions. The authors provide a rigorous theoretical analysis of the model, including the convergence of empirical mean fields to limiting mean fields. They also develop scalable learning algorithms based on a two systems approximation, which addresses the computational complexity of the problem. The proposed approach is evaluated on synthetic and real-world networks, demonstrating its effectiveness compared to existing methods.

### Soundness

3

### Presentation

2

### Contribution

3

### Strengths

1. The paper introduces a novel approach by applying Chung-Lu graphs to model large sparse agent networks, which allows them to effectively handle networks with finite expected average degree and power law degree distributions.
2. The authors provide a rigorous theoretical analysis, proving the convergence of empirical mean fields to limiting mean fields. They also discuss the convergence of objective functions and optimality of policies.

### Weaknesses

#### Some Related Works


#### comment

1. The "extensive approximation" in Section 4 is hard to understand. The authors should provide a clearer explanation of this approximation and its derivation.
2. The paper lacks a detailed discussion of the computational complexity of the proposed learning algorithms. This information would be valuable for understanding the scalability of their approach.
3. The experimental evaluation could be improved by including more baselines and a more detailed analysis of the results.

### Suggestions

The paper would benefit from a more thorough explanation of the extensive approximation in Section 4. Currently, the derivation and intuition behind this approximation are not clear. The authors should provide a step-by-step breakdown of how this approximation is derived, including the assumptions made at each step. It would be helpful to explain the connection between the multinomial sampling of neighborhoods and the subsequent approximation of the mean field transition probabilities. Furthermore, a concrete example illustrating how this approximation works in a simple scenario would greatly enhance understanding. The authors should also discuss the limitations of this approximation and under what conditions it might fail to accurately capture the dynamics of the system. A more detailed explanation of the mathematical reasoning behind this approximation is crucial for the reader to grasp the core methodology of the paper.

Regarding the computational complexity, the authors should provide a detailed analysis of the time and space complexity of their proposed learning algorithms. This analysis should include a breakdown of the computational cost of each step in the algorithms, such as the mean field approximation, policy optimization, and evaluation. It is important to discuss how the complexity scales with the number of agents, the size of the state and action spaces, and the parameter k*. The authors should also compare the computational complexity of their algorithms with existing methods, highlighting the advantages and disadvantages of their approach. This analysis should be presented in a clear and concise manner, using standard complexity notation. Furthermore, the authors should discuss potential optimizations that could be used to reduce the computational cost of their algorithms.

Finally, the experimental evaluation needs to be significantly improved. The authors should include more baselines, such as standard mean field approximations that do not consider network structure, and other relevant algorithms from the multi-agent reinforcement learning literature. A more detailed analysis of the results is also needed. For example, the authors should investigate how the performance of their algorithms varies with different network parameters, such as the power law exponent and the average degree. The sensitivity of the algorithms to the choice of k* should be thoroughly investigated, including a discussion of how to choose an appropriate value for this parameter. The authors should also provide a more detailed analysis of the convergence behavior of their algorithms, including the number of iterations required to reach a stable solution. The experimental section should include more quantitative metrics, such as the mean and variance of the performance across multiple runs, to provide a more robust evaluation.

### Questions

1. How does the choice of k* in the two systems approximation affect the performance of the algorithms? Is there a principled way to choose this parameter?
2. What is the computational complexity of the proposed learning algorithms? How do they scale with the size of the network and the number of agents?
3. How sensitive are the results to the specific parameters of the Chung-Lu graph generation process? Have you investigated the impact of varying these parameters?

### Rating

5

### Confidence

2

**********
