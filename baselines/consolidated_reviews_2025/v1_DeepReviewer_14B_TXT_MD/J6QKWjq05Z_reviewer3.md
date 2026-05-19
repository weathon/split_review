### Summary

The paper proposes a reinforcement learning method to learn a branching rule for the Branch-and-Bound algorithm. The synergy of the exact solving algorithm and data-driven heuristic takes advantage of both worlds: guarantees to compute the optimal solution and the ability to adapt to specific tasks. The proposed method utilizes tree MDP and contraction property of the tree Bellman operator. It maps MILP solving to an episode for our RL agent and trains the agent to optimize the final metric --- the resulting size of the B\&B tree. A modified learning objective that stabilizes the learning process in the presence of high variance returns is proposed.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper is well-written and easy to follow. The proposed method is sound and reasonable. The experimental results show the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is only evaluated on five specific NP-hard tasks, which may not be representative of all combinatorial optimization problems. It is suggested to test the proposed method on a wider range of combinatorial optimization problems to demonstrate its generalization ability.
2. The paper does not provide a clear explanation of why the proposed method is more sample efficient than previous RL methods. It is suggested to provide more details and analysis on the sample efficiency of the proposed method.
3. The paper does not address the potential for overfitting when training on a limited set of problem instances. It is suggested to discuss the potential for overfitting and how to mitigate it.

### Suggestions

The paper would benefit from a more thorough investigation into the generalization capabilities of the proposed reinforcement learning method. While the current evaluation includes five NP-hard problems, it is crucial to assess the method's performance across a broader spectrum of combinatorial optimization problems with varying characteristics. For instance, problems with different constraint structures, objective functions, and solution space sizes should be considered. This could involve incorporating benchmark datasets from diverse domains, such as graph optimization, scheduling, or resource allocation. Furthermore, it would be beneficial to analyze the performance of the method on problems with varying levels of difficulty within the same problem class. This would provide a more comprehensive understanding of the method's robustness and its ability to adapt to different problem instances. Such an analysis would also help identify potential limitations and areas for improvement.

To strengthen the claims regarding sample efficiency, the paper should provide a more detailed analysis of the factors contributing to the improved performance. This could involve comparing the proposed method with existing RL approaches in terms of the number of training episodes required to achieve a certain level of performance. It would be helpful to investigate the impact of different hyperparameters on the sample efficiency of the method. Furthermore, the paper should provide a theoretical analysis of the sample complexity of the proposed method, if possible. This would provide a more rigorous justification for the observed empirical results. Additionally, it would be beneficial to analyze the convergence behavior of the method and provide insights into why it converges faster than other methods. This could involve visualizing the learning curves and analyzing the gradients of the loss function.

Finally, the paper should address the potential for overfitting when training on a limited set of problem instances. This could involve using techniques such as regularization, early stopping, or data augmentation. The paper should also discuss the potential impact of the training data distribution on the generalization performance of the method. It would be helpful to analyze the sensitivity of the method to different training data distributions. Furthermore, the paper should provide a discussion of the limitations of the method and potential areas for future research. This would help to provide a more balanced and comprehensive view of the proposed approach.

### Questions

Please refer to the Weaknesses.

### Rating

5: marginally below the acceptance threshold

### Confidence

2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
