### Summary

This paper considers the problem of reinforcement learning with submodular rewards. The authors show that the problem is NP-hard to approximate. They propose a submodular policy gradient-based algorithm for the problem. They also show that the algorithm recovers the standard policy gradient algorithm in the case of additive rewards. The authors conduct experiments to demonstrate the effectiveness of the proposed algorithm.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well-written and easy to follow. The problem of reinforcement learning with submodular rewards is interesting and important. The proposed algorithm is simple and intuitive. The authors conduct experiments to demonstrate the effectiveness of the proposed algorithm.

### Weaknesses

#### Some Related Works


#### comment

The proposed algorithm is a straightforward adaptation of the standard policy gradient algorithm to the case of submodular rewards. The theoretical analysis does not provide much insight into the behavior of the proposed algorithm in the context of submodular rewards. Specifically, the analysis does not address how the curvature of the submodular reward function affects the convergence or sample complexity of the algorithm. The paper lacks a detailed discussion on how the proposed algorithm handles the non-additive nature of the reward, which is a key aspect of submodular optimization. The analysis should consider the specific properties of submodular functions, such as diminishing returns, and how these properties interact with the gradient-based optimization process. Furthermore, the paper does not explore the potential limitations of the proposed algorithm when dealing with highly complex or non-smooth submodular reward functions.

### Suggestions

The paper would benefit from a more in-depth analysis of the proposed algorithm's behavior with respect to the curvature of the submodular reward function. This could involve deriving theoretical bounds on the convergence rate or sample complexity as a function of the curvature parameter. The analysis should also investigate how the algorithm's performance is affected by different types of submodular functions, such as those with varying degrees of submodularity. For example, it would be valuable to analyze the algorithm's behavior on functions that exhibit strong diminishing returns versus those that do not. This analysis should include a discussion of the algorithm's limitations and potential failure modes in scenarios with highly complex or non-smooth submodular reward functions. It would be beneficial to explore alternative algorithmic approaches that are specifically designed for submodular optimization and compare their performance with the proposed method. 

To strengthen the experimental evaluation, the authors should conduct a more comprehensive analysis of the algorithm's sensitivity to hyperparameters and the impact of different submodular reward structures. This could involve performing a hyperparameter search to identify optimal settings for different environments and analyzing how the performance of the algorithm varies with different choices of submodular functions. The experiments should also include a comparison of the proposed algorithm with existing methods for submodular optimization, if any, to provide a more comprehensive evaluation of its performance. It would be valuable to explore the algorithm's performance in more complex and challenging environments, and to investigate its robustness to noise and uncertainty in the reward signal. The experimental section should also include a discussion of the computational cost of the proposed algorithm and how it scales with the size of the state and action spaces.

Finally, the paper should provide a more detailed discussion of the limitations of the proposed approach and potential directions for future research. This could include exploring alternative algorithmic approaches that are specifically designed for submodular optimization, or investigating the use of techniques from online learning or reinforcement learning to develop adaptive algorithms that can adjust to changing reward structures. The authors should also discuss the potential impact of the proposed algorithm on real-world applications and identify areas where further research is needed to address the challenges of reinforcement learning with submodular rewards. The discussion should also address the practical implications of the theoretical results, such as the inapproximability result, and how these results affect the design and analysis of algorithms for this problem.

### Questions

Please see the weakness section.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
