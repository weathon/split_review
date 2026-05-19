### Summary

This paper proposes a new RL framework, submodular RL, which seeks to optimize non-additive and history-dependent rewards modeled via submodular set functions. The authors first show that the resulting optimization problem is hard to approximate. Then they propose a policy gradient-based algorithm for submodular RL that handles non-additive rewards by greedily maximizing marginal gains. They show that the proposed algorithm recovers optimal constant factor approximations of submodular bandits under some assumptions on the underlying MDP. They also derive a natural policy gradient approach for locally optimizing submodular RL instances even in large state- and action- spaces. The authors showcase the versatility of the approach by applying it to several applications such as biodiversity monitoring, Bayesian experiment design, informative path planning, and coverage maximization.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed framework is novel and interesting. 
3. The authors provide both theoretical and empirical results to support the effectiveness of the proposed framework.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed algorithm is a straightforward extension of policy gradient to submodular rewards. The authors should discuss the challenges in adapting policy gradient to submodular rewards and highlight the technical contributions of their algorithm.
2. The theoretical guarantees of the proposed algorithm are limited to specific cases. It would be helpful to discuss the limitations of the theoretical analysis and potential directions for future research.
3. The experimental results are not very convincing. The authors should provide more details about the experimental setup and results, and discuss the limitations of their experiments.

### Suggestions

The authors should more clearly articulate the specific challenges in adapting policy gradient methods to the submodular reward setting. While the core idea of using a policy gradient approach is intuitive, the non-additive nature of submodular rewards introduces significant complexities. For instance, the standard policy gradient theorem relies on the additivity of rewards to decompose the objective into a sum of per-step rewards. With submodular rewards, this decomposition is no longer valid, and the authors need to explain how they address this issue. Specifically, they should discuss how the marginal gains of submodular functions are handled within the policy gradient framework, and how this differs from the standard approach. Furthermore, the authors should elaborate on the variance of the gradient estimates in the submodular setting, and how their algorithm mitigates this variance. A more detailed discussion of these technical challenges would significantly strengthen the contribution of the paper.

Regarding the theoretical guarantees, the authors should provide a more thorough discussion of the limitations of their analysis. While they provide approximation guarantees under certain assumptions, it is crucial to understand the scope and limitations of these assumptions. For example, the authors should discuss the types of MDPs and submodular functions for which their guarantees hold, and what happens when these assumptions are violated. It would be beneficial to explore the tightness of the approximation bounds and whether they are practically meaningful. Furthermore, the authors should discuss the computational complexity of their algorithm and whether it is scalable to large-scale problems. A more detailed analysis of these limitations would provide a more complete picture of the theoretical contributions of the paper and guide future research directions.

Finally, the experimental section needs significant improvement. The authors should provide more details about the experimental setup, including the specific environments used, the hyperparameter settings, and the training procedures. It is also important to compare the proposed algorithm with existing baselines, such as standard policy gradient methods or other algorithms designed for non-additive rewards. The authors should also discuss the limitations of their experiments and potential directions for future research. For example, they could explore the performance of their algorithm on more complex environments or with different types of submodular reward functions. A more comprehensive experimental evaluation would provide stronger evidence for the effectiveness of the proposed algorithm.

### Questions

1. Can the authors provide more details about the approximation guarantees of the proposed algorithm?
2. How does the performance of the proposed algorithm compare to existing methods for maximizing submodular rewards?
3. What are the limitations of the proposed algorithm, and what are the directions for future research?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
