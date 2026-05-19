### Summary

This paper proposes a novel framework for addressing the challenge of signal delay in deep reinforcement learning (DRL). The authors introduce the Delayed Observation Markov Decision Process (DOMDP) to model the problem, where the agent's perception of the environment is delayed. They provide theoretical insights into the impact of delay on DRL performance and propose effective strategies to mitigate the issue. The paper evaluates the proposed methods on continuous robotic control tasks with varying delay steps and demonstrates that their approach can achieve performance comparable to non-delayed cases. The contributions of this work include a formalization of the delay problem in DRL, novel algorithms for handling signal delay, and empirical validation in continuous control tasks.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

1. The paper addresses a critical issue in DRL, namely the impact of signal delay on learning performance, which is particularly relevant in real-world applications such as robotics and autonomous systems.
2. The authors provide a comprehensive set of experiments across multiple environments and delay settings, demonstrating the effectiveness of their proposed techniques in improving DRL performance under signal delay.
3. The paper is well-written and organized, making it easy to follow the problem formulation, proposed methods, and experimental results.

### Weaknesses

#### Some Related Works


#### comment

1. The paper's contribution is somewhat limited, as it primarily extends existing DRL algorithms to handle signal delay. While the authors propose several techniques to mitigate the issue, these techniques are not entirely novel and have been explored in other contexts. The core idea of incorporating historical information is not new, and the specific methods used, such as state augmentation and prediction networks, are also not fundamentally different from existing approaches in time-series analysis and sequence modeling. The paper lacks a strong theoretical justification for why these specific techniques are particularly well-suited for the delay problem, beyond the empirical results.
2. The paper lacks a rigorous theoretical analysis of the proposed methods. While the authors provide some theoretical insights, such as the equivalence of different delay formulations, a deeper analysis of the convergence properties and sample complexity of the proposed algorithms is missing. This makes it difficult to understand the fundamental limitations and guarantees of the approach. For example, it is unclear how the proposed methods handle different types of delays (e.g., fixed vs. variable delays) or how the performance scales with the magnitude of the delay.
3. The experimental evaluation is limited to continuous robotic control tasks, which may not fully capture the complexity and diversity of real-world applications. The paper does not explore the performance of the proposed methods in other domains, such as discrete action spaces or environments with sparse rewards. This limits the generalizability of the findings and raises questions about the applicability of the approach to a broader range of problems. Furthermore, the paper does not provide a detailed analysis of the computational overhead introduced by the proposed techniques, which is an important factor to consider in practical applications.

### Suggestions

The paper would benefit significantly from a more in-depth theoretical analysis of the proposed methods. Specifically, the authors should investigate the convergence properties of their algorithms under different delay conditions. This could involve deriving bounds on the suboptimality of the learned policy as a function of the delay magnitude. Furthermore, a more rigorous analysis of the sample complexity of the proposed algorithms is needed to understand how the amount of data required for effective learning is affected by the presence of delays. The authors should also explore the limitations of their approach, such as the types of delays it can effectively handle and the conditions under which it might fail. This would provide a more complete understanding of the theoretical underpinnings of the proposed methods and their practical applicability.

To address the limited experimental evaluation, the authors should extend their experiments to include a wider range of environments and tasks. This could involve testing the proposed methods in discrete action spaces, such as those found in game playing or puzzle games, as well as environments with sparse rewards or high-dimensional state spaces. It would also be beneficial to evaluate the performance of the methods in real-world scenarios, such as robotics or autonomous driving, where signal delays are common. Additionally, the authors should provide a detailed analysis of the computational overhead introduced by their techniques, including the memory requirements and runtime. This would help to assess the practical feasibility of the approach and identify potential bottlenecks. The authors should also consider comparing their methods with other existing approaches for handling delays in DRL, to better contextualize their contributions.

Finally, the paper should provide more clarity on the specific implementation details of the proposed techniques. For example, the authors should specify the exact architecture of the prediction networks and the state augmentation modules, as well as the hyperparameter settings used in their experiments. This would allow other researchers to reproduce their results and build upon their work. Furthermore, the authors should provide a more detailed discussion of the limitations of their approach and potential avenues for future research. This would help to guide future work in this area and contribute to a deeper understanding of the challenges of delayed reinforcement learning.

### Questions

1. How does the proposed approach compare to other methods for handling delays in DRL, such as those based on recurrent neural networks or temporal difference learning? A more detailed comparison with existing approaches would help to clarify the novelty and advantages of the proposed methods.
2. The paper mentions that the proposed methods can be integrated with current or future algorithms. Could you provide more details on how this integration can be achieved and what challenges might arise in combining the proposed techniques with different types of DRL algorithms?
3. The experimental results show that the proposed methods can achieve performance comparable to non-delayed cases. However, it is not clear how the performance scales with the magnitude of the delay. Could you provide more insights into the relationship between delay length and learning performance, and whether there are specific delay ranges where the methods are more or less effective?
4. The paper focuses on continuous robotic control tasks. How do you expect the proposed methods to perform in other domains, such as discrete action spaces or environments with sparse rewards? Are there any modifications or adaptations that would be necessary to apply the methods to these different types of problems?

### Rating

3: reject, not good enough

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
