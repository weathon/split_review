### Summary

This paper proposes a reinforcement learning method for learning the branching heuristic in the Branch-and-Bound algorithm. The authors view the variable selection task as a tree Markov Decision Process and prove that the Bellman operator adapted for the tree Markov Decision Process is contracting in mean. They propose a modified learning objective for the reinforcement learning agent. The experimental results show that the proposed method requires less training data and produces smaller trees compared to previous reinforcement learning methods.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. This paper proposes a new method for learning the branching heuristic in the Branch-and-Bound algorithm using reinforcement learning.
2. The authors prove that the Bellman operator in the tree MDP is contracting in mean, which is an important property for the convergence of RL algorithms.
3. The proposed method is shown to be more sample efficient than previous RL methods for learning branching heuristics.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is only evaluated on five specific NP-hard tasks, which may not be representative of all combinatorial optimization problems. 
2. The paper does not provide a clear explanation of why the proposed method is more sample efficient than previous RL methods.
3. The paper does not address the potential for overfitting when training on a limited set of problem instances.

### Suggestions

The paper would benefit from a more thorough discussion of the limitations of the chosen benchmark problems. While the five NP-hard tasks are commonly used, it is crucial to acknowledge that they might not fully capture the diversity of combinatorial optimization problems. For instance, the paper could discuss the specific structural properties of these problems, such as the density of constraints, the size of the solution space, and the presence of specific symmetries or patterns. This would provide a better understanding of the scope and applicability of the proposed method. Furthermore, it would be beneficial to include a discussion on how the performance of the proposed method might vary when applied to problems with different characteristics. This would help to identify potential areas for future research and to better understand the generalizability of the proposed approach.

To strengthen the claims regarding sample efficiency, the paper should provide a more detailed analysis of the factors contributing to the improved performance. It is not sufficient to simply state that the proposed method is more sample efficient; the authors should delve into the specific mechanisms that enable this efficiency. For example, is it due to a more effective exploration strategy, a better representation of the state space, or a more efficient learning algorithm? A detailed ablation study could help to isolate the key factors contributing to the improved sample efficiency. Furthermore, the paper should discuss the potential trade-offs between sample efficiency and solution quality. It is possible that the proposed method achieves better sample efficiency at the cost of a slightly lower solution quality, and this should be acknowledged and discussed.

Finally, the paper should address the potential for overfitting when training on a limited set of problem instances. While the authors mention that they use a set of problem instances generated from a specific distribution, it is important to acknowledge that the model might overfit to this specific distribution. The paper should discuss the potential impact of this overfitting on the generalization performance of the model. It would be beneficial to include a discussion on techniques that could be used to mitigate overfitting, such as regularization or data augmentation. Furthermore, the paper should provide an analysis of the generalization performance of the proposed method on unseen instances, including a discussion of the factors that affect generalization. This would provide a more complete picture of the strengths and limitations of the proposed approach.

### Questions

1. What are the specific characteristics of the five NP-hard tasks that the proposed method is evaluated on? How representative are these tasks of the broader class of combinatorial optimization problems? What are the typical solution space characteristics of these problems, and how do these properties affect the performance of the proposed method?
2. Can you provide a more detailed explanation of why the proposed method is more sample efficient than previous RL methods? What are the key factors that contribute to this improvement? How does the modified learning objective contribute to this? Is it due to a better exploration strategy, or a more effective way of using the data?
3. How does the proposed method address the potential for overfitting when training on a limited set of problem instances? What techniques are used to mitigate overfitting, and how effective are they? How well does the method generalize to unseen instances, and what are the factors that affect generalization?

### Rating

6: marginally above the acceptance threshold

### Confidence

2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
