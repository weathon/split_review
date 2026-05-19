### Summary

The paper addresses the challenge of signal delay in deep reinforcement learning (DRL), where there is a lag between an agent's perception of the environment and its ability to act. The authors introduce a novel framework called Delayed Observation Markov Decision Process (DOMDP) to model this delay, extending the traditional Markov Decision Process (MDP) framework to incorporate signal delays. They demonstrate that standard DRL algorithms perform poorly in environments with delays, and propose several techniques to mitigate this issue, such as Delay-Reconciled Training for Critic, State Augmentation for Actor, and Complementary Techniques for DOMDP Resolution. The authors evaluate their approach on continuous robotic control tasks and show that their methods can achieve performance comparable to that of non-delayed cases.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

1. The paper tackles a significant and practical problem in DRL, namely the impact of signal delay on learning performance. This is a relevant issue in many real-world applications, such as robotics, autonomous driving, and finance, where delays can significantly affect the effectiveness of DRL algorithms.
2. The authors provide a comprehensive set of experiments across multiple environments and delay settings, demonstrating the effectiveness of their proposed techniques in improving DRL performance under signal delay. The results show that their approach can achieve performance comparable to non-delayed cases, which is a notable achievement.
3. The paper is well-written and organized, making it easy to follow the problem formulation, proposed methods, and experimental results. The authors provide a clear motivation for their work and a thorough explanation of their approach.

### Weaknesses

#### Some Related Works


#### comment

1. The paper's contribution is somewhat limited, as it primarily extends existing DRL algorithms to handle signal delay. While the authors propose several techniques to mitigate the issue, these techniques are not entirely novel and have been explored in other contexts. The core idea of incorporating historical information is not new, and the specific methods used, such as state augmentation and prediction networks, are also not fundamentally different from existing approaches in time-series analysis and sequence modeling. The paper lacks a strong theoretical justification for why these specific techniques are particularly well-suited for the delay problem, beyond the empirical results.
2. The paper lacks a rigorous theoretical analysis of the proposed methods. While the authors provide some theoretical insights, such as the equivalence of different delay formulations, a deeper analysis of the convergence properties and sample complexity of the proposed algorithms is missing. This makes it difficult to understand the fundamental limitations and guarantees of the approach. For example, it is unclear how the proposed methods handle different types of delays (e.g., fixed vs. variable delays) or how the performance scales with the magnitude of the delay.
3. The experimental evaluation is limited to continuous robotic control tasks, which may not fully capture the complexity and diversity of real-world applications. The paper does not explore the performance of the proposed methods in other domains, such as discrete action spaces or environments with sparse rewards. This limits the generalizability of the findings and raises questions about the applicability of the approach to a broader range of problems. Furthermore, the paper does not provide a detailed analysis of the computational overhead introduced by the proposed techniques, which is an important factor to consider in practical applications.

### Suggestions

The paper could be significantly strengthened by providing a more in-depth theoretical analysis of the proposed methods. This should include a rigorous examination of the convergence properties and sample complexity of the algorithms, particularly in the context of varying delay lengths. For instance, the authors could explore how the performance of their methods degrades as the delay increases, and whether there are specific delay ranges where the methods are more or less effective. Furthermore, a theoretical analysis of the impact of different delay formulations on the learning process would be beneficial. This could involve deriving bounds on the suboptimality of the learned policy under delayed feedback, or analyzing the conditions under which the proposed methods are guaranteed to converge to an optimal or near-optimal policy. Such analysis would provide a more solid foundation for the proposed approach and help to identify its limitations.

To address the limited experimental evaluation, the authors should extend their experiments to include a wider range of environments and tasks. This could involve testing the proposed methods in discrete action spaces, such as those found in games or puzzle games, as well as environments with sparse rewards or high-dimensional state spaces. It would also be valuable to evaluate the performance of the methods in real-world scenarios, such as robotics or autonomous driving, where signal delays are common. Additionally, the authors should provide a detailed analysis of the computational overhead introduced by their techniques, including the memory requirements and runtime. This would help to assess the practical feasibility of the approach and identify potential bottlenecks. Furthermore, the authors should explore the sensitivity of their methods to different hyperparameter settings and provide guidelines for selecting appropriate values.

Finally, the paper would benefit from a more thorough discussion of the limitations of the proposed approach and potential avenues for future research. This could include addressing the challenges of dealing with non-stationary delays, where the delay length changes over time, or exploring the use of more sophisticated prediction models. The authors should also discuss the potential impact of their work on real-world applications and identify the key challenges that need to be overcome to deploy these methods in practice. A more comprehensive discussion of these limitations would provide a more balanced perspective on the contributions of the paper and help to guide future research in this area.

### Questions

1. How does the proposed approach compare to other methods for handling delays in DRL, such as those based on recurrent neural networks or temporal difference learning? A more detailed comparison with existing approaches would help to clarify the novelty and advantages of the proposed methods.
2. The paper mentions that the proposed methods can be integrated with current or future algorithms. Could you provide more details on how this integration can be achieved and what challenges might arise in combining the proposed techniques with different types of DRL algorithms?
3. The experimental results show that the proposed methods can achieve performance comparable to non-delayed cases. However, it is not clear how the performance scales with the magnitude of the delay. Could you provide more insights into the relationship between delay length and learning performance, and whether there are specific delay ranges where the methods are more or less effective?
4. The paper focuses on continuous robotic control tasks. How do you expect the proposed methods to perform in other domains, such as discrete action spaces or environments with sparse rewards? Are there any modifications or adaptations that would be necessary to apply the methods to these different types of problems?

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
