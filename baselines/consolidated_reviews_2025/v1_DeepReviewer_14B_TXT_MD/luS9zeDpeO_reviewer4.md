### Summary

The paper addresses the problem of safe multi-agent reinforcement learning (MARL) in a decentralized setting. The authors introduce a mathematical model called a homogeneous constrained Markov game, which extends previous work by incorporating safety constraints. They propose a decentralized primal-dual actor-critic algorithm that allows agents to learn safe policies without centralized training. The algorithm combines local gradient updates with consensus updates to ensure convergence. The authors provide theoretical proofs of asymptotic convergence under certain assumptions and develop a practical off-policy version based on deep reinforcement learning. The effectiveness of the proposed algorithm is demonstrated through experiments on three safety-aware multi-robot coordination tasks with continuous action spaces.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel mathematical model for safe MARL, extending existing work by incorporating safety constraints.
2. The proposed decentralized primal-dual actor-critic algorithm is a significant contribution, allowing agents to learn safe policies without centralized training.
3. The authors provide rigorous theoretical analysis, including proofs of asymptotic convergence under specific conditions.
4. The practical off-policy version of the algorithm, based on deep reinforcement learning, makes the approach applicable to real-world scenarios.
5. The experimental results demonstrate the effectiveness of the proposed algorithm on safety-aware multi-robot coordination tasks.

### Weaknesses

#### Some Related Works


#### comment

1. The paper assumes that agents are homogeneous, which may not hold in many real-world multi-agent systems. This assumption limits the applicability of the proposed method to scenarios where agents have identical capabilities and objectives. The theoretical analysis and algorithm design are heavily reliant on this homogeneity, and it is unclear how the approach would perform with heterogeneous agents having different state and action spaces, or different reward and cost functions. This is a significant limitation as many real-world multi-agent systems involve agents with diverse characteristics.
2. The algorithm relies on certain assumptions for convergence guarantees, such as the irreducibility and aperiodicity of the Markov chain induced by the policy. While these are standard assumptions in Markov decision process literature, their practical verification in complex multi-agent environments is not trivial. The paper does not provide sufficient discussion on how these assumptions can be ensured in practice, or what the implications would be if these assumptions are violated. This lack of practical guidance limits the applicability of the theoretical results.
3. The experimental evaluation is conducted on relatively simple multi-robot coordination tasks. While these tasks are useful for demonstrating the basic functionality of the algorithm, they do not fully capture the complexities of real-world multi-agent systems. The tasks lack the high dimensionality and stochasticity that are often present in practical applications. The paper should include more challenging environments to better demonstrate the robustness and scalability of the proposed method.

### Suggestions

The paper makes a valuable contribution to the field of safe multi-agent reinforcement learning by introducing a decentralized primal-dual actor-critic algorithm. However, several aspects could be improved to enhance its practical relevance and impact. First, the assumption of homogeneous agents is a significant limitation. Future work should explore how the proposed method can be extended to handle heterogeneous agents. This could involve designing different policy parameterizations for different agent types, or using techniques like multi-agent transfer learning to leverage knowledge across different agent populations. The paper should also investigate how the communication structure affects the performance of the algorithm in heterogeneous settings, as the consensus updates may need to be adapted to account for differences in agent capabilities. Furthermore, the paper should provide a more detailed analysis of the computational complexity of the proposed algorithm, especially in the context of heterogeneous agents, as the consensus updates may introduce additional computational overhead.

Second, the paper should provide more practical guidance on how to ensure the assumptions for convergence are met in real-world scenarios. For example, the paper could discuss how to choose appropriate policy parameterizations to ensure the Markov chain is irreducible and aperiodic. It could also explore the use of techniques like exploration bonuses to encourage sufficient exploration of the state space. Furthermore, the paper should investigate the sensitivity of the algorithm to violations of these assumptions. For example, it could analyze how the convergence rate and the quality of the learned policies are affected if the Markov chain is not strictly irreducible or aperiodic. This would provide a more robust understanding of the algorithm's performance in practical settings. The authors should also consider providing empirical analysis on the sensitivity of the algorithm to the choice of hyperparameters, such as the learning rates and the consensus update frequency.

Finally, the experimental evaluation should be expanded to include more complex and realistic multi-agent environments. This could involve using benchmark environments with higher dimensionality, more stochasticity, and more complex agent interactions. For example, the authors could consider using environments from the Multi-Agent Particle Environment (MPE) or the StarCraft Multi-Agent Challenge (SMAC). These environments would provide a more rigorous test of the algorithm's scalability and robustness. The paper should also include a more detailed analysis of the algorithm's performance in different scenarios, such as varying the number of agents, the communication topology, and the safety constraints. This would provide a more comprehensive understanding of the algorithm's strengths and limitations.

### Questions

1. How does the performance of the proposed algorithm scale with the number of agents in the multi-agent system? Are there any limitations in terms of scalability?
2. Can the proposed method be extended to handle heterogeneous agents with different state and action spaces?
3. How sensitive is the algorithm to the choice of hyperparameters, such as the learning rates and the consensus update frequency?
4. What are the computational requirements of the proposed algorithm, and how do they scale with the number of agents and the complexity of the environment?
5. How does the communication topology among agents affect the performance of the algorithm? Are there any specific network structures that are more conducive to learning safe policies?

### Rating

6

### Confidence

3

**********
