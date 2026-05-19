### Summary

The paper studies multi-agent reinforcement learning (MARL) with safety constraints under the entropy-regularized setting. The authors propose a decentralized primal-dual actor-critic algorithm for solving a class of constrained Markov games, and further extend it to the practical scenario with local observations and safety constraints. The effectiveness of the proposed algorithm is demonstrated through simulations.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The paper studies MARL with safety constraints, which is an important problem in the community of safe RL. 
2. The proposed algorithm is decentralized and thus suitable for large-scale systems. 
3. The authors provide theoretical analysis of the proposed algorithm.

### Weaknesses

#### Some Related Works

[1] Safe decentralized control for networked multi-agent systems
[2] Provably efficient multi-agent reinforcement learning with safety constraints
[3] Safe multi-agent reinforcement learning with expressive safety critics
[4] Safe multi-agent reinforcement learning with general utilities through barrier functions

#### comment

1. The proposed algorithm is only applicable to the homogeneous setting. This is a strong assumption in practice, and the authors should discuss its implications and limitations. 
2. The theoretical results are not surprising. The convergence of the proposed algorithm is essentially a direct application of the multi-time-scale stochastic approximation, which is a well-established theory. The authors should clarify the novelty of their theoretical analysis and provide a more in-depth discussion of the challenges in applying this theory to the specific problem of safe MARL. 
3. The practical algorithm is not novel. The authors use the well-known actor-critic framework, where the actor is trained via off-policy samples and the critic is trained via on-policy samples. The authors should clarify the novelty of their practical algorithm and discuss its advantages over existing methods. 
4. The simulation results are not convincing. The authors should compare their algorithm with more baselines, including both primal-based and primal-dual-based methods. The current comparison is insufficient to demonstrate the superiority of the proposed algorithm. 
5. The authors should discuss the limitations of their work and suggest future research directions. The current discussion is too brief and does not adequately address the challenges and open questions in the field.

### Suggestions

The paper's primary weakness lies in its limited scope, focusing solely on a homogeneous multi-agent system. This assumption significantly restricts the applicability of the proposed method in real-world scenarios, where agents often exhibit diverse behaviors and objectives. The authors should explicitly acknowledge this limitation and discuss potential avenues for extending their approach to heterogeneous settings. For instance, they could explore the use of personalized policy representations or investigate methods for aligning the learning processes of diverse agents. Furthermore, a more detailed analysis of the implications of this homogeneity assumption on the convergence and optimality of the proposed algorithm is needed. The current theoretical analysis does not sufficiently address the challenges posed by heterogeneous agent populations, and a more rigorous treatment is required to establish the validity of the proposed approach in such scenarios.

Regarding the theoretical analysis, the authors should provide a more in-depth discussion of the challenges in applying multi-time-scale stochastic approximation to the safe MARL problem. While the convergence results are not surprising, the authors should clarify the specific technical hurdles they overcame in adapting this theory to their setting. For example, they could discuss the difficulties in handling the safety constraints and the implications of these constraints on the convergence rate and stability of the algorithm. A more detailed analysis of the assumptions required for the convergence analysis and their practical implications would also be beneficial. The authors should also discuss the limitations of their theoretical results, such as the assumptions on the smoothness of the value functions and the boundedness of the gradients. A more thorough discussion of these limitations would provide a more balanced view of the theoretical contributions of the paper.

Finally, the practical algorithm, while based on a well-known actor-critic framework, lacks novelty. The authors should clarify the specific modifications they made to the standard framework and discuss the advantages of these modifications over existing methods. For example, they could highlight the benefits of using on-policy samples for the critic and off-policy samples for the actor in the context of safe MARL. A more detailed comparison with existing primal-based and primal-dual-based methods is needed to demonstrate the superiority of the proposed practical algorithm. The simulation results should also be expanded to include a wider range of baselines and evaluation metrics. The current comparison is insufficient to convincingly demonstrate the effectiveness of the proposed algorithm. The authors should also discuss the limitations of their practical algorithm, such as its sensitivity to hyperparameter tuning and its performance in different environments.

### Questions

1. What is the definition of $\pi_{\theta}^*$ in Theorem 2? 
2. What is the definition of $\pi_{\theta_i}^*$ in Theorem 3? 
3. In Theorem 3, the authors assume that the critic parameters converge to a fixed point. Is this assumption reasonable? 
4. In the proof of Theorem 3, the authors use the fact that $\lim_{t\to\infty} \beta_{\omega_t^z} = 0$. However, this fact is not used in the proof. Why does this fact hold? 
5. In the practical algorithm, the authors use the entropy regularization coefficient $\alpha_i$ to balance exploration and exploitation. However, this coefficient is not updated during training. How does the algorithm adapt to different environments or tasks? 
6. In the practical algorithm, the authors use the automatic entropy adjustment mechanism to balance exploration and exploitation. However, this mechanism is not used in the theoretical analysis. Why is this discrepancy necessary? 
7. In the practical algorithm, the authors use the critic to estimate the value function. However, the value function is not used in the practical algorithm. Why is this discrepancy necessary? 
8. In the practical algorithm, the authors use the entropy regularization coefficient $\alpha_i$ to balance exploration and exploitation. However, this coefficient is not updated during training. How does the algorithm adapt to different environments or tasks?

### Rating

3

### Confidence

4

**********
