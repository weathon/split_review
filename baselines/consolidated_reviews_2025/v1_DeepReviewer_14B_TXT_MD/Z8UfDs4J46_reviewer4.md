### Summary

The paper introduces a framework for deep reinforcement learning with delayed signals. The authors formalize delayed-observation Markov decision processes (DOMDP) by extending the standard MDP framework to incorporate signal delays. The paper proposes effective strategies to overcome the challenges posed by the presence of signal delay in DRL, achieving remarkable performance in continuous robotic control tasks with large delays.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper introduces a novel approach to address the overlooked problem of signal delay in deep reinforcement learning (DRL). The authors formalize delayed-observation Markov decision processes (DOMDP) by extending the standard MDP framework to incorporate signal delays. This provides a more comprehensive understanding of DRL in the presence of signal delays and presents a novel model architecture to overcome the associated challenges.

2. The paper is well-structured and easy to follow. The authors clearly define the problem of signal delay in DRL and provide a detailed explanation of the proposed methods. The experimental results are presented in a clear and concise manner, and the figures and tables are well-designed and informative.

3. The paper addresses an important issue in DRL that has been overlooked in previous studies. Signal delay is a common problem in many real-world applications, and the proposed methods can be applied to a wide range of tasks. The paper's contributions have the potential to advance the field of DRL and improve the performance of DRL-based solutions in practical scenarios.

### Weaknesses

#### Some Related Works


#### comment

1. The paper's evaluation is limited to simulated robotic control environments, which may not be representative of real-world environments. The authors should consider evaluating their method on more diverse and challenging tasks to demonstrate its robustness and generalizability. Specifically, the simulation environments used, while standard in the field, often lack the complexities of real-world sensor noise, actuator delays, and unpredictable environmental dynamics. This raises concerns about the practical applicability of the proposed method in real-world robotic systems. The evaluation should include environments with more complex observation spaces, such as those involving visual inputs or high-dimensional sensor data, to better assess the method's ability to handle realistic scenarios.

2. The paper does not provide a detailed analysis of the computational complexity of the proposed methods. It is important to understand the computational cost of the methods, especially when applied to large-scale problems. The authors should provide a more detailed analysis of the time and space complexity of their methods and compare them to existing approaches. A thorough analysis should include not only the theoretical complexity but also the practical runtime and memory usage, especially when dealing with high-dimensional state and action spaces. Furthermore, the authors should discuss the scalability of their approach with respect to the size of the state space, action space, and delay length.

3. The paper could benefit from a more in-depth discussion of the limitations of the proposed methods. The authors should acknowledge the potential challenges and limitations of their approach and suggest directions for future research. For example, the paper should discuss the sensitivity of the method to hyperparameter settings, the potential for instability during training, and the limitations of the method when dealing with highly stochastic environments. A discussion of these limitations would provide a more balanced view of the method's capabilities and its potential for future development.

### Suggestions

To address the limitations of the evaluation, the authors should consider expanding their experiments to include more diverse and challenging environments. This could involve using more complex simulation environments that incorporate realistic sensor noise, actuator delays, and unpredictable environmental dynamics. Furthermore, the authors should evaluate their method on tasks with high-dimensional observation spaces, such as those involving visual inputs or raw sensor data. This would provide a more comprehensive assessment of the method's robustness and generalizability. Additionally, the authors could consider evaluating their method on real-world robotic platforms to demonstrate its practical applicability. This would involve addressing the challenges of transferring the method from simulation to real-world systems, such as dealing with sensor noise, actuator inaccuracies, and unexpected environmental changes. Such experiments would significantly strengthen the paper's claims and demonstrate the practical value of the proposed approach.

To provide a more thorough analysis of the computational complexity, the authors should include a detailed breakdown of the time and space complexity of their proposed methods. This analysis should consider the complexity of each component of the method, such as the neural network training, the delay handling mechanism, and the policy execution. The authors should also compare the computational cost of their method to existing approaches, both theoretically and empirically. This comparison should include not only the asymptotic complexity but also the practical runtime and memory usage, especially when dealing with high-dimensional state and action spaces. Furthermore, the authors should discuss the scalability of their approach with respect to the size of the state space, action space, and delay length. This analysis should include both theoretical considerations and empirical results, demonstrating how the method performs under different conditions. This would provide a more complete understanding of the computational trade-offs of the proposed method.

Finally, the authors should provide a more in-depth discussion of the limitations of their proposed methods. This discussion should include the potential challenges and limitations of the approach, such as the sensitivity to hyperparameter settings, the potential for instability during training, and the limitations when dealing with highly stochastic environments. The authors should also discuss the assumptions made by their method and the conditions under which these assumptions might not hold. Furthermore, the authors should suggest directions for future research that could address these limitations. This could include exploring alternative delay handling mechanisms, developing more robust training algorithms, or extending the method to more complex environments. A thorough discussion of these limitations would provide a more balanced view of the method's capabilities and its potential for future development.

### Questions

1. How does the proposed method perform in environments with high-dimensional state and action spaces? Are there any limitations or challenges in scaling the method to such environments?

2. How does the proposed method compare to other existing approaches for handling signal delay in DRL, such as those based on recurrent neural networks or attention mechanisms? What are the advantages and disadvantages of the proposed method compared to these approaches?

3. How does the performance of the proposed method vary with different delay lengths? Are there any specific delay lengths for which the method performs particularly well or poorly?

4. How does the proposed method handle noisy or incomplete observations? Are there any specific techniques used to mitigate the impact of noise or missing data on the performance of the method?

5. How does the proposed method handle non-stationary environments, where the dynamics of the environment change over time? Are there any specific techniques used to adapt to these changes?

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
