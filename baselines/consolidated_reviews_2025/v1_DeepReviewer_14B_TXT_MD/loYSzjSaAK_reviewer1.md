### Summary

This paper studies the problem of optimizing submodular rewards in RL. This is a novel direction to extend RL beyond the Markov assumption. The reward function is defined on trajectories, and is not necessarily additive over timesteps. Despite the NP-hardness of the problem in general, the authors propose a policy gradient-based method to tackle it. Theoretically, they show that under certain assumptions on the underlying MDP, the problem reduces to a continuous DR-submodular optimization problem. They also quantify the deviation of submodular reward functions from modular ones using curvature. Empirically, they demonstrate the effectiveness of their approach in a variety of applications.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The problem of optimizing submodular rewards in RL is novel and well-motivated. The authors have identified a broad class of interesting reward functions that go beyond the Markov assumption.
2. Both the theoretical and empirical contributions are solid. The authors provide inapproximability results, algorithmic guarantees under certain assumptions, and empirical validation across various applications.

### Weaknesses

#### Some Related Works


#### comment

1. The assumptions made in Section 5 are not clearly justified. While the authors state that these assumptions are natural and discuss some of their implications, it would be helpful to provide more insight into why these assumptions are reasonable and when they might be expected to hold in practice. Specifically, the assumption about the reward function being DR-submodular after a reparameterization seems quite strong and lacks sufficient justification. It would be beneficial to elaborate on the types of submodular reward functions that satisfy this condition, and provide examples where this assumption is likely to hold in real-world scenarios. Furthermore, the connection between this assumption and the specific parameterization of the policy is not clear, and needs further clarification.
2. The theoretical results in Section 5 rely on assumptions that are independent of the proposed algorithm. This makes it difficult to assess the algorithm's performance in settings where these assumptions may not hold. Also, the curvature-based approximation result for general MDPs is not very satisfying. The result relies on a specific choice of modular reward, and it is not clear how this choice affects the approximation guarantee. It would be helpful to explore alternative choices of modular rewards and analyze their impact on the approximation ratio. Moreover, the dependence of the approximation ratio on the curvature is quite weak, and it would be beneficial to investigate whether tighter bounds can be obtained under additional assumptions.

### Suggestions

The paper introduces an interesting and novel problem of optimizing submodular rewards in reinforcement learning, which extends beyond the standard Markov assumption. However, the theoretical analysis could be strengthened by providing more concrete examples and justifications for the assumptions made. Specifically, the assumption of DR-submodularity after reparameterization needs further elaboration. It would be beneficial to provide examples of common submodular reward functions that satisfy this condition, and explain how this assumption relates to the structure of the underlying Markov Decision Process. For instance, are there specific classes of MDPs or reward functions where this assumption is more likely to hold? Furthermore, the authors could explore the implications of violating this assumption and discuss how the performance of the proposed algorithm might be affected in such cases. This would provide a more complete understanding of the applicability of the theoretical results.

To strengthen the theoretical results, the authors should consider exploring alternative approaches that do not rely on assumptions that are independent of the proposed algorithm. For example, it might be possible to derive convergence guarantees or performance bounds that are directly related to the properties of the policy gradient algorithm. This would provide a more direct assessment of the algorithm's performance and its limitations. Additionally, the curvature-based approximation result for general MDPs could be improved by investigating tighter bounds under additional assumptions. For instance, it might be possible to explore the impact of other properties of the reward function, such as smoothness or Lipschitz continuity, on the approximation ratio. Furthermore, the authors could consider alternative choices of modular rewards and analyze their impact on the approximation guarantee. This would provide a more comprehensive understanding of the limitations of the proposed approach and potential avenues for improvement.

Finally, the empirical evaluation could be enhanced by including a more detailed analysis of the algorithm's performance under different settings. For example, it would be interesting to investigate how the performance of the algorithm varies with the curvature of the reward function, and how it compares to other existing methods for optimizing submodular functions. Furthermore, the authors could explore the sensitivity of the algorithm to different hyperparameter settings and provide guidelines for selecting appropriate values. This would provide a more practical perspective on the applicability of the proposed approach and its limitations. It would also be beneficial to include experiments on more complex and realistic environments to demonstrate the scalability and robustness of the algorithm.

### Questions

1. In the first paragraph of Section 5, you mention reparameterization and state that it is detailed in Appendix C. However, I cannot find the relevant discussion in the appendix. Could you please provide more details or point me to the correct section in the appendix?
2. In the proof of Theorem 5, you show that $J(\pi)$ is monotone DR-submodular. However, the proof only shows that $J(\pi)$ is monotone submodular. Could you please clarify this point?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
