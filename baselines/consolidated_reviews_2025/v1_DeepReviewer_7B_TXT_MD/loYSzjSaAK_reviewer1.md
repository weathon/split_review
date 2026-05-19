### Summary

The paper studies the problem of RL with non-additive (specifically, submodular) rewards. The authors show that this problem is inapproximable and design a policy gradient-based method, called submodular policy optimization (SubPO), for solving it. The authors also show that SubPO recovers the standard PG method in the case of additive rewards. The proposed method is tested on a number of applications, such as coverage, informative path planning, and Bayesian experimental design.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

The paper is well-written and easy to follow. The problem of RL with non-additive rewards is interesting, and the proposed method is simple and intuitive. The experimental results are promising.

### Weaknesses

#### Some Related Works


#### comment

The main weakness of the paper is the lack of novelty. The proposed method is a straightforward adaptation of the standard PG method to the case of submodular rewards. While the authors acknowledge the inapproximability result, they do not sufficiently explore the implications for practical algorithm design. The theoretical analysis, while providing a lower bound on the approximation ratio, does not offer much insight into the behavior of the proposed algorithm in the context of submodular rewards. Specifically, the analysis does not address how the curvature of the submodular reward function affects the convergence or sample complexity of the algorithm. Furthermore, the paper does not provide a clear comparison to existing methods for optimizing submodular functions in other contexts, such as offline RL or combinatorial optimization. The experimental section, while demonstrating promising results, lacks a thorough analysis of the algorithm's sensitivity to hyperparameters and the impact of different submodular reward structures. The paper also does not discuss the limitations of the proposed approach, such as the potential for poor performance in scenarios with highly complex or non-smooth submodular reward functions.

### Suggestions

The paper would benefit significantly from a more in-depth exploration of the theoretical properties of the proposed SubPO algorithm, particularly in relation to the specific characteristics of submodular reward functions. Instead of focusing solely on the inapproximability result, the authors should investigate how the curvature of the submodular reward influences the convergence rate and sample complexity of the algorithm. For instance, it would be valuable to analyze how different curvature parameters (e.g., the minimum curvature) affect the performance of SubPO. This could involve deriving tighter bounds on the approximation ratio or providing a more detailed analysis of the algorithm's behavior under different curvature regimes. Furthermore, the authors should provide a more comprehensive comparison to existing methods for optimizing submodular functions in other contexts. This would help to clarify the novelty and contribution of the proposed approach and highlight its advantages and disadvantages compared to alternative techniques. For example, a comparison to algorithms used in offline RL or combinatorial optimization could provide valuable insights into the strengths and weaknesses of SubPO.

To strengthen the experimental evaluation, the authors should conduct a more thorough analysis of the algorithm's sensitivity to hyperparameters and the impact of different submodular reward structures. This could involve performing a hyperparameter search to identify optimal settings for different environments and analyzing how the performance of SubPO varies with different choices of submodular functions. It would also be beneficial to include a wider range of experimental scenarios, including more complex and challenging environments, to better assess the robustness and generalizability of the proposed method. Additionally, the authors should discuss the limitations of the proposed approach in more detail, particularly in scenarios where the submodular reward function is highly complex or non-smooth. This could involve analyzing the performance of SubPO under different types of submodular functions and identifying potential failure modes or scenarios where the algorithm is likely to perform poorly. A more thorough discussion of these limitations would help to provide a more balanced and realistic assessment of the proposed method.

Finally, the authors should consider exploring alternative algorithmic approaches for solving the RL problem with submodular rewards. While the proposed SubPO method is simple and intuitive, it may not be the most effective approach for all types of submodular reward functions. Investigating alternative algorithms, such as those based on Lagrangian relaxation or submodular maximization techniques, could potentially lead to more efficient and robust solutions. The authors could also explore the use of techniques from online learning or reinforcement learning to develop adaptive algorithms that can adjust to changing reward structures. A more thorough exploration of these alternative approaches would help to broaden the scope of the paper and provide a more comprehensive understanding of the challenges and opportunities in RL with submodular rewards.

### Questions

1. In the proof of Theorem 1, why is the case $V_h(s) = V_h(s')$ possible?
2. In the proof of Theorem 1, the authors write that $V_{h-1}(s) \geq V_{h-1}(s') + 1$. Why is this the case? If I understand correctly, the authors use the fact that $V_{h-1}(s)$ and $V_{h-1}(s')$ are integers. Is it possible to relax this assumption?

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
