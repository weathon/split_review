### Summary

This paper investigates the integration of sparse policies with offline reinforcement learning (RL) to derive a safety-aware policy entirely from a logged dataset. The authors introduce a novel algorithm, Fat-to-Thin Policy Optimization (FtTPO), which addresses the unique challenges posed by sparse policies. This method works by first establishing a fat (heavy-tailed) proposal policy that learns from the dataset and subsequently transfers its knowledge to a thin (sparse) policy. The effectiveness of FtTPO is demonstrated in a safety-critical treatment simulation as well as the standard MuJoCo suite.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The concept of "fat-to-thin" is straightforward and appears to be a reasonable approach to enforce sparsity.
3. The algorithm is simple and easy to implement.

### Weaknesses

#### Some Related Works


#### comment

1. The major concern is the motivation to use a sparse policy in offline RL. The authors claimed that "Infinite-support policies like the Gaussian or the heavy-tailed distributions… are not suitable in this regard". However, I don't think a Gaussian policy is inherently unsuitable for safety-critical tasks. (1) For example, the well-known conservative offline RL methods such as CQL can be used to learn a conservative Gaussian policy. (2) A Gaussian policy can be easily converted to a near-optimal policy in continuous games by redefining the action space (i.e., Gaussian policy under alternative action space definitions). Therefore, the claim that Gaussian policies are unsuitable for safety-critical tasks is not accurate, and the paper does not provide sufficient justification for why a sparse policy is inherently better in this context.

2. The authors claimed that "FtTPO can successfully learn one that competes favorably against popular existing methods." However, the performance of FtTPO is not as competitive as claimed. In the Mujoco benchmark, the performance of FtTPO is at most comparable to the baseline methods, not showing a significant improvement. The results presented do not demonstrate a clear advantage over existing methods, and in some cases, FtTPO performs worse than baselines such as IQL. This raises questions about the practical benefits of the proposed approach.

3. The paper lacks a thorough analysis of the proposed method. For example, in the ablation study, the authors claimed that "FtTPO-SG (Squashed Gaussian) validates the heavy-tailed proposal policy." However, the results in Table 1 show that FtTPO-SG performs worse than FtTPO only in 4 of the 9 tasks. This is not sufficient to validate the heavy-tailed proposal policy. Additionally, there is no comparison between the heavy-tailed policy and a Gaussian policy with the same action bound, making it difficult to isolate the impact of the heavy-tailed distribution. The lack of detailed analysis makes it difficult to understand the specific contributions of each component of the proposed method.

### Suggestions

The paper needs to provide a more compelling argument for the use of sparse policies in offline RL, especially when compared to well-established methods that can learn conservative Gaussian policies. The authors should provide a more detailed analysis of the specific scenarios where sparse policies offer a significant advantage over Gaussian policies, beyond simply stating that they are more suitable for safety-critical tasks. For example, they could explore environments where the optimal policy is known to be sparse and demonstrate how their method can effectively learn such policies, while Gaussian policies fail to do so. Furthermore, the authors should provide a more rigorous justification for why the proposed method is expected to outperform existing methods, especially in the context of safety-critical tasks. This could involve a theoretical analysis of the properties of the proposed method or a more detailed empirical study that highlights the specific advantages of the approach.

The experimental evaluation should be significantly strengthened to provide more convincing evidence of the effectiveness of the proposed method. The authors should include a more comprehensive set of baselines, including state-of-the-art offline RL algorithms that can learn conservative Gaussian policies, such as CQL. The comparison should be performed on a wider range of environments, including more complex and realistic safety-critical tasks. The results should be presented in a way that clearly demonstrates the advantages of the proposed method over existing methods, including a detailed analysis of the performance differences. The authors should also provide a more thorough analysis of the impact of different design choices, such as the choice of the heavy-tailed distribution and the specific method used to enforce sparsity. This could involve a more detailed ablation study that systematically varies these parameters and analyzes their impact on performance.

Finally, the paper should include a more detailed analysis of the learned policies, including visualizations of the policy's behavior in different states. This would help to provide a better understanding of how the proposed method works and why it is effective. The authors should also provide a more detailed discussion of the limitations of the proposed method and the potential directions for future research. This could include a discussion of the challenges of applying the method to more complex and realistic environments, as well as the potential for combining the method with other techniques to further improve its performance. The paper should also address the computational cost of the proposed method and compare it to existing methods.

### Questions

1. What's the motivation to use a sparse policy in offline RL? Why can't a Gaussian policy work?
2. Is the proposed FtTPO method suitable for general tasks? What's the performance of FtTPO on the D4RL AntMaze task?

### Rating

3

### Confidence

4

**********
