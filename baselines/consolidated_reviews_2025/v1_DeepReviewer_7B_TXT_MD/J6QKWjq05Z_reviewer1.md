### Summary

This paper proposes a new reinforcement learning method for variable selection in the Branch-and-Bound algorithm for MILPs. The proposed method is based on a tree MDP formulation, and the agent is trained to minimize the geometric mean of the tree size. The proposed method is evaluated on five MILP instances and is shown to outperform the previous RL-based method.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

- The proposed method is shown to outperform the previous RL-based method.

### Weaknesses

#### Some Related Works


#### comment

 - The proposed method is based on a tree MDP formulation, which has been previously studied in the literature. The authors should discuss the differences between the proposed method and the existing tree MDP methods in the literature.
- The proposed method is only compared to the previous RL-based method. It would be better to compare the proposed method to other variable selection methods, such as the strong branching heuristic.

### Suggestions

The paper would benefit from a more thorough discussion of the tree MDP formulation and its relation to existing literature. While the authors mention that their method is based on a tree MDP, they do not adequately address the nuances of how their approach differs from prior work. Specifically, they should clarify the specific tree MDP formulation they are using, and how it compares to other tree MDP formulations used in the context of branch-and-bound or similar tree-based search algorithms. A detailed comparison should include a discussion of the state space, action space, transition probabilities, and reward function, and how these differ from existing formulations. Furthermore, the authors should discuss the theoretical properties of their tree MDP, such as whether it satisfies the contraction property of the Bellman operator, and how this property is leveraged in their algorithm. This discussion should also include a comparison to other tree MDP formulations used in the literature, highlighting the unique aspects of their approach and its advantages over existing methods. This would help to better position the contribution of the paper and clarify the novelty of the proposed method.

In addition to the comparison with the previous RL-based method, the authors should also compare their method to other state-of-the-art variable selection heuristics. While the authors argue that these heuristics are not learning-based, they are still important baselines for evaluating the performance of their method. Specifically, the authors should compare their method to strong branching, which is a widely used heuristic for variable selection in branch-and-bound. The comparison should include a detailed analysis of the performance of the different methods in terms of the size of the branch-and-bound tree, the time required to find the optimal solution, and the number of nodes explored. This comparison would provide a more comprehensive evaluation of the proposed method and help to understand its strengths and weaknesses compared to existing approaches. Furthermore, the authors should also consider comparing their method to other learning-based approaches for variable selection, even if they are not directly based on tree MDP. This would help to position their method within the broader landscape of learning-based optimization techniques.

Finally, the authors should provide more details on the implementation of their method and the experimental setup. This includes details on the neural network architecture, the training procedure, and the hyperparameter settings. The authors should also provide more details on the evaluation metrics used, and how they are calculated. This would help to ensure the reproducibility of their results and allow other researchers to build upon their work. Furthermore, the authors should also discuss the limitations of their method and potential directions for future research. This includes discussing the scalability of their method to larger and more complex MILP instances, and the potential for further improvements in the performance of the method. This would help to provide a more balanced and comprehensive view of the contribution of the paper.

### Questions

- Could you please discuss the differences between the proposed method and the existing tree MDP methods in the literature?
- Could you please compare the proposed method to other variable selection methods, such as the strong branching heuristic?

### Rating

3: reject, not good enough

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
