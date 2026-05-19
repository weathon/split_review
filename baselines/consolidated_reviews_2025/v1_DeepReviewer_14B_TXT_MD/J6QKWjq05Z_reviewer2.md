### Summary

This paper proposes a reinforcement learning-based method for learning the branching heuristic for the Branch-and-Bound algorithm. The authors formulate the variable selection process as a tree MDP and prove the contraction property of the Bellman operator for the tree MDP. The proposed RL-based algorithm is evaluated on five problem instances and the results show that the proposed method outperforms the imitation learning and REINFORCE agents.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

1. The authors propose a novel RL-based method for learning the branching heuristic for the Branch-and-Bound algorithm. The proposed method is more sample efficient than previous RL methods.
2. The authors prove the contraction property of the Bellman operator for the tree MDP, which is important for the convergence of RL methods.
3. The proposed method is evaluated on five problem instances and the results show that the proposed method outperforms the imitation learning and REINFORCE agents.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is only evaluated on five problem instances, which is not enough to demonstrate the effectiveness of the proposed method. The selection of these five problems is not well-justified, and it is unclear how representative they are of the broader class of combinatorial optimization problems. The paper should include a more diverse set of problems, potentially from different application domains, to better assess the generalizability of the proposed approach. Furthermore, the size of the instances used for training and testing should be specified, as this can significantly impact the performance and scalability of the method.
2. The paper does not provide a comparison with other state-of-the-art methods for learning branching heuristics, such as the method proposed in "Learning to branch in mixed integer linear programming". A more comprehensive comparison is needed to demonstrate the advantages of the proposed method over existing approaches. This comparison should include not only the final solution quality but also the computational cost and convergence speed of the different methods. The lack of such a comparison makes it difficult to assess the true contribution of this work.
3. The paper does not provide a detailed analysis of the computational complexity of the proposed method. A more detailed analysis is needed to understand the scalability of the proposed method. Specifically, the paper should analyze the time complexity of each component of the algorithm, including the feature extraction, neural network inference, and training. This analysis should also consider the impact of the problem size and the number of training episodes on the overall computational cost.

### Suggestions

To address the limited evaluation, the authors should expand their experimental setup to include a more diverse set of combinatorial optimization problems. This could involve selecting problems from different application domains, such as logistics, scheduling, or resource allocation, to ensure that the method is not overly specialized to the current set of problems. Furthermore, the authors should clearly specify the size and characteristics of the problem instances used for both training and testing. This would allow for a more thorough assessment of the method's scalability and generalizability. It would also be beneficial to include a discussion on the limitations of the current evaluation and suggest future directions for more comprehensive testing. For example, the authors could consider using benchmark datasets that are widely used in the combinatorial optimization community to facilitate comparison with other methods.

To provide a more comprehensive comparison with existing methods, the authors should include a comparison with state-of-the-art techniques for learning branching heuristics, such as the method proposed in "Learning to branch in mixed integer linear programming". This comparison should not only focus on the final solution quality but also consider the computational cost and convergence speed of the different methods. The authors should also provide a detailed analysis of the strengths and weaknesses of their method compared to the existing approaches. This analysis should include a discussion of the trade-offs between solution quality, computational cost, and implementation complexity. Furthermore, the authors should consider using a wider range of evaluation metrics to provide a more complete picture of the performance of the different methods. For example, they could consider metrics such as the number of nodes explored during the search or the time required to reach a certain solution quality.

Finally, the authors should provide a more detailed analysis of the computational complexity of the proposed method. This analysis should include a breakdown of the time complexity of each component of the algorithm, such as feature extraction, neural network inference, and training. The authors should also consider the impact of the problem size and the number of training episodes on the overall computational cost. This analysis should be supported by empirical results that demonstrate the scalability of the method. For example, the authors could provide a plot of the training time as a function of the problem size or the number of training episodes. This would allow for a more thorough understanding of the computational limitations of the proposed method and provide guidance for future research.

### Questions

1. What is the computational complexity of the proposed method?
2. How does the proposed method compare with other state-of-the-art methods for learning branching heuristics?
3. How does the proposed method perform on a wider range of combinatorial optimization problems?

### Rating

3: reject, not good enough

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
