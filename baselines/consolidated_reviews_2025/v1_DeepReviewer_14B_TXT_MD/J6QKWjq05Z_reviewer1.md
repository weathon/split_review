### Summary

This paper proposes a reinforcement learning method for learning the branching heuristic in the Branch-and-Bound algorithm. The authors view the variable selection task as a tree Markov Decision Process and prove that the Bellman operator adapted for the tree Markov Decision Process is contracting in mean. They propose a modified learning objective for the reinforcement learning agent. The experimental results show that the proposed method requires less training data and produces smaller trees compared to previous reinforcement learning methods.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

1. This paper proposes a new method for learning the branching heuristic in the Branch-and-Bound algorithm using reinforcement learning.
2. The authors prove that the Bellman operator in the tree MDP is contracting in mean, which is an important property for the convergence of RL algorithms.
3. The proposed method is shown to be more sample efficient than previous RL methods for learning branching heuristics.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is only evaluated on five specific NP-hard tasks, which may not be representative of all combinatorial optimization problems. The selection of these problems, while common in the literature, lacks a strong justification for their representativeness of the broader class of combinatorial problems. The paper should include a discussion on the structural properties of these problems and how they relate to other combinatorial optimization problems. For example, are these problems primarily discrete optimization problems, or do they have continuous components? What are the typical solution space characteristics of these problems (e.g., density, convexity)? How do these properties affect the performance of the proposed method?
2. The paper does not provide a clear explanation of why the proposed method is more sample efficient than previous RL methods. While the authors claim that their method is more sample efficient, they do not provide a detailed analysis of the factors contributing to this improvement. The paper should include a more in-depth discussion of the specific mechanisms that lead to better sample efficiency. For example, how does the modified learning objective contribute to this? Is it due to a better exploration strategy, or a more effective way of using the data? A more detailed analysis is needed to understand the underlying reasons for the improved sample efficiency.
3. The paper does not address the potential for overfitting when training on a limited set of problem instances. The authors should discuss the potential for overfitting, especially given the complexity of the neural networks used and the limited number of training instances. The paper should include a discussion on the techniques used to mitigate overfitting, such as regularization, early stopping, or data augmentation. Furthermore, the paper should provide an analysis of the generalization performance of the proposed method on unseen instances, including a discussion of the factors that affect generalization.

### Suggestions

The paper would benefit from a more thorough discussion of the problem characteristics and how they relate to the proposed method. The authors should provide a detailed analysis of the structural properties of the five NP-hard problems used in the evaluation, including the type of optimization (discrete or continuous), the characteristics of the solution space, and the typical difficulty of these problems. This analysis should also discuss how these properties might affect the performance of the proposed method and whether the method is likely to generalize to other types of combinatorial optimization problems. For example, if the problems are primarily discrete optimization problems with a dense solution space, it would be important to discuss whether the method would be applicable to problems with a sparse solution space or continuous optimization problems. This discussion should be grounded in the existing literature on combinatorial optimization and should provide a clear rationale for the selection of the evaluation problems.

To address the lack of clarity regarding sample efficiency, the authors should provide a more detailed analysis of the factors contributing to the improved performance of their method. This analysis should include a discussion of the specific mechanisms that lead to better sample efficiency, such as the modified learning objective, the exploration strategy, and the way the data is used. For example, the authors could analyze the convergence behavior of the proposed method and compare it to previous RL methods. They could also provide an ablation study to evaluate the impact of different components of their method on sample efficiency. Furthermore, the authors should provide a theoretical analysis of the sample complexity of their method, if possible. This analysis should be supported by empirical evidence and should provide a clear understanding of why the proposed method is more sample efficient.

Finally, the paper should address the potential for overfitting by including a discussion of the techniques used to mitigate overfitting, such as regularization, early stopping, or data augmentation. The authors should also provide an analysis of the generalization performance of the proposed method on unseen instances, including a discussion of the factors that affect generalization. This analysis should include a comparison of the performance of the proposed method on training instances and unseen instances, and it should discuss the potential for overfitting when training on a limited set of problem instances. The authors could also explore techniques for improving generalization, such as domain adaptation or transfer learning. This discussion should be supported by empirical evidence and should provide a clear understanding of the generalization capabilities of the proposed method.

### Questions

1. What are the specific characteristics of the five NP-hard tasks that the proposed method is evaluated on? How representative are these tasks of the broader class of combinatorial optimization problems? What are the typical solution space characteristics of these problems, and how do these properties affect the performance of the proposed method?
2. Can you provide a more detailed explanation of why the proposed method is more sample efficient than previous RL methods? What are the key factors that contribute to this improvement? How does the modified learning objective contribute to this? Is it due to a better exploration strategy, or a more effective way of using the data?
3. How does the proposed method address the potential for overfitting when training on a limited set of problem instances? What techniques are used to mitigate overfitting, and how effective are they? How well does the method generalize to unseen instances, and what are the factors that affect generalization?

### Rating

3: reject, not good enough

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
