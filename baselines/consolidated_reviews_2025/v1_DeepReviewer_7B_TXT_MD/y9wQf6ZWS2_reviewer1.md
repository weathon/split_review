### Summary

The paper proposes a new variant of Q-learning algorithm that is guaranteed to converge when using linear function approximation. The authors show that their algorithm can be interpreted as adding a regularization term to the TD update rule. They provide a theoretical analysis of the algorithm's convergence and an upper bound on the approximation error. The authors also present experimental results demonstrating the effectiveness of their algorithm.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

- The paper addresses an important problem in reinforcement learning, namely the divergence issue of Q-learning with linear function approximation.
- The authors provide a theoretical analysis of the algorithm's convergence and an upper bound on the approximation error.
- The authors present experimental results demonstrating the effectiveness of their algorithm.

### Weaknesses

#### Some Related Works

[1] On the Convergence of Q-learning and variants with Linear Function Approximation
[2] On the Convergence of Q-learning and variants with Linear Function Approximation: A Taketa of Recent Advances

#### comment

 - The novelty of the proposed algorithm is limited. The algorithm is a simple modification of the Q-learning algorithm with a regularization term, which has been widely used in practice.
- The theoretical analysis of the algorithm's convergence and approximation error is not novel. The analysis follows the same approach as in previous works [1,2] and does not provide any new insights.
- The experimental results are not convincing. The authors only compare their algorithm with two baselines, which are not strong enough to demonstrate the effectiveness of their algorithm. The authors should compare their algorithm with more baselines, including other state-of-the-art algorithms for Q-learning with linear function approximation.
- The presentation of the paper can be improved. The authors should provide more details about the algorithm and the experimental setup. The authors should also provide a more detailed discussion of the limitations of their algorithm and potential directions for future research.

### Suggestions

The paper's primary weakness lies in the limited novelty of the proposed algorithm and the lack of a compelling experimental evaluation. While the authors frame their approach as a novel modification of Q-learning, the core idea of adding a regularization term is well-established. To strengthen the contribution, the authors should clearly articulate the specific scenarios where their algorithm offers a significant advantage over existing methods. This could involve a more detailed analysis of the regularization term's impact on convergence and stability, going beyond the existing theoretical bounds. For instance, they could investigate how the regularization parameter affects the bias-variance trade-off in the function approximation setting, and provide guidelines for selecting this parameter in practice. Furthermore, a more thorough comparison with other regularization techniques, such as L1 or elastic net regularization, would be beneficial to highlight the unique properties of the proposed approach.

To address the concerns about the experimental evaluation, the authors should significantly expand the set of baselines used for comparison. Comparing against only two weak baselines is insufficient to demonstrate the effectiveness of the proposed algorithm. The authors should include state-of-the-art algorithms for Q-learning with linear function approximation, such as those based on stochastic approximation theory or more recent variants of Q-learning with function approximation. Furthermore, the experimental setup should be more comprehensive, including a wider range of environments and hyperparameter settings. The authors should also provide a more detailed analysis of the experimental results, including a discussion of the statistical significance of the observed differences. It would be beneficial to include learning curves that show the convergence behavior of the algorithm over time, and to analyze the sensitivity of the algorithm to different hyperparameter settings. The authors should also consider using more challenging environments to test the robustness of their algorithm.

Finally, the presentation of the paper could be improved by providing more details about the algorithm and the experimental setup. The authors should include a more detailed description of the algorithm's implementation, including the specific choices of function approximation architecture and optimization parameters. The authors should also provide a more detailed discussion of the limitations of their algorithm and potential directions for future research. This could include exploring alternative regularization techniques, investigating the algorithm's performance in non-stationary environments, or extending the analysis to other reinforcement learning algorithms. The authors should also consider providing a more intuitive explanation of the theoretical results, making them more accessible to a broader audience.

### Questions

- How does the proposed algorithm compare to other state-of-the-art algorithms for Q-learning with linear function approximation?
- What are the limitations of the proposed algorithm, and what are the potential directions for future research?

### Rating

3

### Confidence

4

**********
