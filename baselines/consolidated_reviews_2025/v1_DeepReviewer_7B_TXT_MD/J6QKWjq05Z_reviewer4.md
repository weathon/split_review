### Summary

This paper proposes a reinforcement learning method to learn a branching rule for the Branch-and-Bound algorithm. The proposed method is based on a tree MDP formulation, and the agent is trained to minimize the geometric mean of the tree size. The proposed method is evaluated on five MILP instances and is shown to outperform the previous RL-based method.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is based on a tree MDP formulation, and the agent is trained to minimize the geometric mean of the tree size.
3. The proposed method is evaluated on five MILP instances and is shown to outperform the previous RL-based method.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is based on a tree MDP formulation, which has been previously studied in the literature. The authors should discuss the differences between the proposed method and the existing tree MDP methods in the literature.
2. The proposed method is only compared to the previous RL-based method. It would be better to compare the proposed method to other variable selection methods, such as the strong branching heuristic.

### Suggestions

The paper would benefit from a more thorough discussion of the existing literature on tree MDPs, particularly in the context of branch-and-bound algorithms. While the authors mention that their method is based on a tree MDP, they do not adequately address the nuances of how their approach differs from prior work. Specifically, they should clarify the specific tree MDP formulation they are using, and how it compares to other tree MDP formulations used in the context of branch-and-bound or similar tree-based search algorithms. A detailed comparison should include a discussion of the state space, action space, transition probabilities, and reward function, and how these differ from existing formulations. Furthermore, the authors should discuss the theoretical properties of their tree MDP, such as whether it satisfies the contraction property of the Bellman operator, and how this property is leveraged in their algorithm. This discussion should also include a comparison to other tree MDP formulations used in the literature, highlighting the unique aspects of their approach and its advantages over existing methods. This would help to better position the contribution of the paper and clarify the novelty of the proposed method.

In addition to the comparison with the previous RL-based method, the authors should also compare their method to other state-of-the-art variable selection heuristics. While the authors argue that these heuristics are not learning-based, they are still important baselines for evaluating the performance of their method. Specifically, the authors should compare their method to strong branching, which is a widely used heuristic for variable selection in branch-and-bound. The comparison should include a detailed analysis of the performance of the different methods in terms of the size of the branch-and-bound tree, the time required to find the optimal solution, and the number of nodes explored. This comparison would provide a more comprehensive evaluation of the proposed method and help to understand its strengths and weaknesses compared to existing approaches. Furthermore, the authors should also consider comparing their method to other learning-based approaches for variable selection, even if they are not directly based on tree MDP. This would help to position their method within the broader landscape of learning-based optimization techniques.

Finally, the authors should provide more details on the implementation of their method and the experimental setup. This includes details on the neural network architecture, the training procedure, and the hyperparameter settings. The authors should also provide more details on the evaluation metrics used, and how they are calculated. This would help to ensure the reproducibility of their results and allow other researchers to build upon their work. Furthermore, the authors should also discuss the limitations of their method and potential directions for future research. This includes discussing the scalability of their method to larger and more complex MILP instances, and the potential for further improvements in the performance of the method. This would help to provide a more balanced and comprehensive view of the contribution of the paper.

### Questions

See weakness.

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
