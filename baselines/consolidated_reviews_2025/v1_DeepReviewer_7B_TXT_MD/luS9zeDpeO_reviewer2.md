### Summary

This paper studies the safe multi-agent reinforcement learning problem with homogeneous agents. The authors propose a primal-dual decentralized actor-critic algorithm and prove its convergence. The authors also provide a practical version of their algorithm and test it on three safety-aware continuous multi-robot tasks.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow. The authors provide a clear description of the problem setting, the proposed algorithm, and the theoretical analysis.

2. The authors provide a practical version of their algorithm and test it on three safety-aware continuous multi-robot tasks.

### Weaknesses

#### Some Related Works

[1] Safe Multi-Agent Reinforcement Learning with General Utilities through Barrier Functions
[2] Provably Efficient Safe Multi-Agent Reinforcement Learning with Linear Function Approximation

#### comment

1. The assumption of homogeneous agents is a significant limitation. In many real-world multi-agent systems, agents have different capabilities, goals, and constraints. The paper does not adequately address how the proposed algorithm would perform in such heterogeneous settings. The theoretical analysis relies on this assumption, and it is unclear how the convergence guarantees would hold when agents are not identical. Specifically, the policy consensus step, which is crucial for the convergence proof, might not be effective if agents have fundamentally different behaviors or objectives. The paper should discuss the implications of this assumption and provide some analysis or justification for its use.

2. The paper does not provide a thorough comparison with existing safe multi-agent reinforcement learning algorithms. While the authors mention some related work, they do not clearly articulate how their approach differs from and improves upon these methods. For example, the paper should discuss how the proposed algorithm compares to methods that use Lagrangian relaxation or barrier functions for safety constraints. The lack of a detailed comparison makes it difficult to assess the novelty and contribution of the proposed approach. A more comprehensive discussion of the related work is needed to contextualize the paper's contribution.

3. The theoretical analysis relies on several strong assumptions, such as the smoothness of the value functions and the boundedness of the gradients. These assumptions might not hold in many practical scenarios, and the paper does not discuss the limitations of these assumptions or their impact on the algorithm's performance. The paper should provide a more detailed analysis of the robustness of the algorithm to violations of these assumptions. For example, the paper could explore the convergence behavior under weaker assumptions or provide empirical evidence of the algorithm's performance when these assumptions are violated.

4. The practical version of the algorithm uses a fixed entropy regularization coefficient, which might not be optimal for all tasks. The paper does not provide a clear justification for this choice or discuss how the coefficient should be selected. The paper should explore adaptive methods for adjusting the entropy regularization coefficient during training and provide empirical evidence of their effectiveness. The current approach might lead to suboptimal performance in some tasks, and the paper should address this limitation.

5. The paper does not provide a detailed analysis of the computational complexity of the proposed algorithm. The authors should discuss the scalability of the algorithm to large-scale multi-agent systems and provide empirical evidence of its performance on such systems. The paper should also discuss the memory requirements of the algorithm and how they scale with the number of agents.

### Suggestions

The paper would benefit from a more thorough discussion of the limitations imposed by the assumption of homogeneous agents. While the theoretical analysis might be simplified by this assumption, it is crucial to acknowledge its potential impact on the applicability of the proposed algorithm in real-world scenarios. The authors should explore potential extensions of their approach to handle heterogeneous agents, even if these extensions are not fully developed in the current paper. For example, they could investigate the use of personalized policy representations or explore methods for aligning the learning processes of diverse agents. Furthermore, the paper should include a discussion of the trade-offs between the simplicity of the homogeneous agent assumption and the potential performance degradation in heterogeneous settings. This would provide a more balanced and realistic assessment of the proposed algorithm's capabilities.

To strengthen the paper, the authors should provide a more comprehensive comparison with existing safe multi-agent reinforcement learning algorithms. This comparison should not only focus on the theoretical aspects but also on the practical performance of the algorithms. The authors should discuss how their approach compares to methods that use Lagrangian relaxation or barrier functions for safety constraints, highlighting the advantages and disadvantages of each approach. The comparison should also include a discussion of the computational complexity and scalability of the different algorithms. This would help to contextualize the paper's contribution and provide a more complete picture of the state-of-the-art in safe multi-agent reinforcement learning. The authors should also consider including a table summarizing the key differences between their approach and existing methods, including the assumptions made, the convergence guarantees, and the practical performance.

Finally, the paper should address the limitations of the strong assumptions made in the theoretical analysis. The authors should discuss the robustness of the algorithm to violations of these assumptions and provide empirical evidence of its performance under such conditions. For example, they could explore the convergence behavior of the algorithm when the value functions are not smooth or when the gradients are not bounded. The paper should also discuss the practical implications of these assumptions and provide guidance on how to choose the algorithm's parameters in different scenarios. Furthermore, the authors should explore adaptive methods for adjusting the entropy regularization coefficient during training and provide empirical evidence of their effectiveness. This would make the algorithm more robust and applicable to a wider range of tasks. The paper should also include a discussion of the computational complexity of the algorithm and how it scales with the number of agents.

### Questions

1. How does the proposed algorithm perform in heterogeneous multi-agent systems? What are the challenges of extending the proposed algorithm to heterogeneous settings?

2. How does the proposed algorithm compare to existing safe multi-agent reinforcement learning algorithms? What are the advantages and disadvantages of the proposed approach?

3. How robust is the theoretical analysis to violations of the strong assumptions made? What are the practical implications of these assumptions?

4. How should the entropy regularization coefficient be selected in practice? What are the advantages and disadvantages of using a fixed coefficient versus an adaptive one?

5. How does the computational complexity of the proposed algorithm scale with the number of agents? What are the practical limitations of the algorithm in large-scale multi-agent systems?

### Rating

5

### Confidence

3

**********
