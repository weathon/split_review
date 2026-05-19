### Summary

This paper introduces a novel approach to offline reinforcement learning (RL) with sparse policies, addressing the challenge of learning safe, sparse actions from logged datasets. The proposed method, Fat-to-Thin Policy Optimization (FtTPO), maintains a heavy-tailed proposal policy that learns from offline data and transfers knowledge to a sparse policy. The authors demonstrate the effectiveness of FtTPO in a safety-critical treatment simulation and the MuJoCo benchmark, showing that FtTPO can learn a sparse policy that outperforms popular baselines.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel approach to offline RL by combining sparse policies with offline learning, which is particularly relevant for safety-critical applications.
2. The proposed FtTPO algorithm is the first to address the challenge of out-of-support actions in sparse policy learning, which is a significant contribution to the field.
3. The paper provides a thorough analysis of the proposed method, including ablation studies and comparisons with existing baselines. The empirical results demonstrate the effectiveness of FtTPO in learning sparse policies.
4. The paper is well-written and easy to follow. The authors provide a clear explanation of the problem, the proposed solution, and the experimental results.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed discussion of the limitations of the proposed method and potential directions for future research. For instance, the paper does not thoroughly explore the sensitivity of the method to the choice of the heavy-tailed distribution's parameters, specifically the entropic index q. The performance implications of different q values, and how they interact with the sparsity of the learned policy, are not fully analyzed. Furthermore, the paper lacks a discussion on how the method might perform in environments with higher dimensional action spaces, where the benefits of sparse policies might be more pronounced, or conversely, where the optimization landscape might be more challenging.
2. The paper could include more detailed ablation studies to analyze the impact of different design choices on the performance of the proposed method. For example, the paper does not provide a detailed analysis of the impact of the weighting coefficient w(s, a) on the learning process. It is unclear how different weighting schemes affect the convergence and stability of the algorithm. Additionally, the paper could benefit from a more thorough investigation of the trade-off between the sparsity of the policy and the performance, and how this trade-off is affected by the choice of the q-Gaussian distribution's parameters.

### Suggestions

The paper should include a more detailed analysis of the sensitivity of the proposed method to the choice of the heavy-tailed distribution's parameters, specifically the entropic index q. This analysis should include a systematic exploration of how different q values affect the sparsity of the learned policy and its performance. For example, the authors could conduct experiments where they vary q across a range of values and plot the resulting policy sparsity and performance metrics. This would provide a clearer understanding of the trade-offs involved in selecting q and help practitioners choose appropriate values for their specific applications. Furthermore, the authors should discuss how the choice of q might interact with the dimensionality of the action space, as higher dimensional spaces might require different parameter settings to achieve optimal performance. This discussion should also include a theoretical analysis of the impact of q on the optimization landscape and the convergence properties of the algorithm.

To strengthen the ablation studies, the paper should include a more detailed analysis of the impact of the weighting coefficient w(s, a) on the learning process. This analysis should explore different weighting schemes and their effects on the convergence and stability of the algorithm. For instance, the authors could compare the performance of the algorithm when using different weighting functions, such as exponential or uniform weighting, and analyze how these choices affect the learning dynamics. This would provide a more comprehensive understanding of the role of the weighting coefficient and help practitioners choose appropriate weighting schemes for their specific applications. Additionally, the authors should investigate the trade-off between the sparsity of the policy and the performance, and how this trade-off is affected by the choice of the q-Gaussian distribution's parameters. This could involve plotting the performance of the algorithm as a function of the sparsity level, which could be controlled by the q parameter, and analyzing the resulting trade-off curve.

Finally, the paper should include a more thorough discussion of the limitations of the proposed method and potential directions for future research. This discussion should include an analysis of how the method might perform in environments with higher dimensional action spaces, where the benefits of sparse policies might be more pronounced, or conversely, where the optimization landscape might be more challenging. The authors should also discuss the computational cost of the proposed method and how it scales with the dimensionality of the action space. Furthermore, the paper should explore the potential for extending the proposed method to other types of sparse policies, such as those based on categorical or discrete distributions. This would broaden the applicability of the method and make it more relevant to a wider range of applications.

### Questions

1. How does the choice of the heavy-tailed distribution affect the performance of the proposed method? Are there any specific distributions that work better than others?
2. How does the proposed method perform in environments with higher dimensional action spaces? Are there any specific challenges that arise in such environments?
3. How does the proposed method compare to other approaches for learning sparse policies in offline RL? Are there any specific advantages or disadvantages of the proposed method compared to these approaches?

### Rating

6

### Confidence

3

**********
