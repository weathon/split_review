### Summary

This paper studies the safe multi-agent reinforcement learning (MARL) problem. A mathematical model called homogeneous constrained Markov game is presented. An on-policy decentralized primal-dual actor-critic algorithm is proposed. Asymptotic convergence is proven. A practical off-policy version of the proposed algorithm is developed based on the deep reinforcement learning training architecture. Simulation results are provided to demonstrate the effectiveness of the proposed algorithm.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The problem of safe multi-agent reinforcement learning is important.
2. The writing is clear.
3. The homogeneous constrained Markov game is well-defined.

### Weaknesses

#### Some Related Works


#### comment

1. The contribution of this paper is not significant. The authors only extend the model proposed in Chen et al. (2022) under the safe MARL setting. The design of the proposed algorithm is very similar to the algorithm proposed in Qu et al. (2022). The authors should highlight the contribution and novelty of this paper.
2. The experiments are not enough. There is no comparison with other baseline algorithms. The authors should compare the proposed algorithm with other safe MARL algorithms to show the effectiveness of the proposed algorithm. The authors should also provide more details about the implementation of the proposed algorithm and the baseline algorithms.

### Suggestions

The paper's primary weakness lies in its incremental contribution over existing work. While the authors present a homogeneous constrained Markov game model and a decentralized primal-dual actor-critic algorithm, the novelty is not sufficiently highlighted. The extension of the model from Chen et al. (2022) to a safe MARL setting, while relevant, needs further justification as to why this specific extension is non-trivial. Similarly, the algorithmic design bears a strong resemblance to Qu et al. (2022), and the authors must clearly articulate the differences and advantages of their approach. For example, a detailed comparison of the mathematical formulations, assumptions, and limitations of both algorithms would be beneficial. The authors should also discuss the specific challenges in the safe MARL setting that their algorithm addresses and how it overcomes these challenges compared to existing methods. Furthermore, the theoretical analysis, while valuable, should be more clearly connected to the practical algorithm to demonstrate its relevance.

To address the lack of experimental validation, the authors should conduct a more comprehensive evaluation of their algorithm. The current experiments lack a comparison with established safe MARL baselines, making it difficult to assess the performance of the proposed algorithm. The authors should include comparisons with algorithms such as those based on constrained policy optimization or other relevant safe MARL methods. These comparisons should not only focus on the final performance but also on the learning speed, stability, and robustness of the algorithms. Furthermore, the experimental section should provide more details about the implementation, including the specific hyperparameter settings, network architectures, and training procedures used for both the proposed algorithm and the baselines. This would allow for a more thorough and reproducible evaluation of the results. The authors should also consider including ablation studies to analyze the impact of different components of their algorithm.

Finally, the authors should provide a more detailed discussion of the limitations of their approach and potential future research directions. This would help to contextualize the contribution of the paper and identify areas for further improvement. For example, the authors could discuss the scalability of their algorithm to larger multi-agent systems, the sensitivity of their algorithm to different hyperparameter settings, and the potential for extending their approach to more complex environments. By addressing these points, the authors can significantly strengthen the paper and make a more compelling case for its contribution to the field of safe multi-agent reinforcement learning.

### Questions

1. What is the contribution and novelty of this paper?
2. Can you compare the proposed algorithm with other safe MARL algorithms?

### Rating

5

### Confidence

4

**********
