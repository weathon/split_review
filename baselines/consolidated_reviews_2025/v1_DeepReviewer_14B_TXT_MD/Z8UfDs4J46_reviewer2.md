### Summary

This paper introduces a novel approach to address the challenge of signal delay in deep reinforcement learning (DRL). The authors formalize delayed-observation Markov decision processes (DOMDP) by extending the standard MDP framework to incorporate signal delays. They highlight the significant impact of signal delay on DRL performance and demonstrate that trivial DRL algorithms and generic methods for partially observable tasks suffer greatly from delays. The proposed methods achieve remarkable performance in continuous robotic control tasks with large delays, yielding results comparable to those in non-delayed cases.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1.	The paper formalizes delayed-observation Markov decision processes (DOMDP) by extending the standard MDP framework to incorporate signal delays.
2.	The authors elucidate the challenges posed by the presence of signal delay in DRL, showing that trivial DRL algorithms and generic methods for partially observable tasks suffer greatly from delays.
3.	The proposed methods achieve remarkable performance in continuous robotic control tasks with large delays, yielding results comparable to those in non-delayed cases.

### Weaknesses

#### Some Related Works


#### comment

1.	The paper primarily focuses on simulated robotic control environments, which may not fully capture the complexities and uncertainties present in real-world applications. The simulation environments, while useful for initial testing, often lack the nuances of sensor noise, imperfect actuation, and dynamic environmental conditions that are inherent in real-world robotic systems. This discrepancy could lead to a significant performance drop when the proposed methods are deployed on physical robots. The paper should include a more detailed discussion of the limitations of the simulated environments and how these limitations might affect the generalizability of the results.
2.	The paper could benefit from a more detailed discussion of the computational complexity and scalability of the proposed methods, especially when applied to large-scale or real-world problems. The analysis should include not only the theoretical complexity but also the practical implications of the proposed methods, such as memory usage and training time. For example, the paper should discuss how the computational cost scales with the size of the state and action spaces, and the length of the delay. Furthermore, the paper should provide a more detailed analysis of the computational bottlenecks of the proposed methods and suggest potential optimizations.
3.	The paper could provide more insights into the practical challenges and considerations when deploying the proposed methods in real-world scenarios. The paper should discuss the sensitivity of the proposed methods to hyperparameter settings and the potential for overfitting to the training environment. Additionally, the paper should address the challenges of adapting the proposed methods to different robotic platforms and tasks, and the potential for domain adaptation techniques to improve the generalizability of the results. The paper should also discuss the robustness of the proposed methods to noisy sensor data and unexpected environmental changes.

### Suggestions

To address the limitations of relying solely on simulated environments, the authors should consider incorporating more realistic simulation scenarios that include sensor noise, actuator inaccuracies, and dynamic environmental conditions. This could involve using more sophisticated simulation tools or incorporating noise models that mimic real-world sensor data. Furthermore, the authors should explore the use of domain adaptation techniques to bridge the gap between simulated and real-world environments. This could involve training the agents in a simulated environment and then fine-tuning them in a real-world environment, or using techniques such as domain randomization to improve the generalizability of the learned policies. The paper should also include a discussion of the potential challenges and limitations of deploying the proposed methods in real-world scenarios, and suggest potential solutions to these challenges.

To provide a more comprehensive analysis of the computational complexity and scalability of the proposed methods, the authors should include a detailed breakdown of the computational cost of each component of the proposed methods. This should include the cost of the neural network training, the cost of the delay reconciliation process, and the cost of the policy execution. The authors should also discuss how the computational cost scales with the size of the state and action spaces, the length of the delay, and the number of training samples. Furthermore, the authors should provide a more detailed analysis of the memory usage of the proposed methods, and discuss potential optimizations to reduce the memory footprint. The paper should also include a comparison of the computational cost of the proposed methods with existing methods for handling delayed observations in reinforcement learning.

To provide more insights into the practical challenges and considerations when deploying the proposed methods in real-world scenarios, the authors should include a more detailed discussion of the sensitivity of the proposed methods to hyperparameter settings. The paper should also discuss the potential for overfitting to the training environment and suggest techniques to mitigate this issue, such as regularization and early stopping. Additionally, the authors should explore the use of transfer learning techniques to adapt the proposed methods to different robotic platforms and tasks. The paper should also include a discussion of the robustness of the proposed methods to noisy sensor data and unexpected environmental changes, and suggest techniques to improve the robustness of the learned policies. The authors should also consider including a case study of deploying the proposed methods on a physical robot to demonstrate the practical feasibility of the approach.

### Questions

1.	How do the proposed methods perform in real-world robotic applications, and what are the challenges and considerations when deploying them in such scenarios?
2.	What is the computational complexity of the proposed methods, and how do they scale with the size of the environment and the complexity of the tasks?
3.	How do the proposed methods compare to other existing approaches for handling signal delay in DRL, and what are their advantages and disadvantages?

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
