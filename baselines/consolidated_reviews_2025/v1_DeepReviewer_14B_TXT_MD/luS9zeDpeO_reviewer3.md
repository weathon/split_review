### Summary

This paper investigates the decentralized safe multi-agent reinforcement learning (MARL) problem based on homogeneous multi-agent systems, where agents aim to maximize the team-average return and the joint policy’s entropy, while satisfying safety constraints associated to the cumulative team-average cost. A mathematical model referred to as a homogeneous constrained Markov game is formally characterized, based on which policy sharing provably preserves the optimality of our safe MARL problem. An on-policy decentralized primal-dual actor-critic algorithm is then proposed, where agents utilize both local gradient updates and consensus updates to learn local policies, without the requirement for a centralized trainer. Asymptotic convergence is proven using multi-timescale stochastic approximation theory under standard assumptions. Thereafter, a practical off-policy version of the proposed algorithm is developed based on the deep reinforcement learning training architecture. The effectiveness of our practical algorithm is demonstrated through comparisons with solid baselines on three safety-aware multi-robot coordination tasks in continuous action spaces.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. This paper is well-written and easy to follow.
2. The theoretical analysis is solid.
3. The experiments are sufficient to support the theoretical results.

### Weaknesses

#### Some Related Works


#### comment

1. The authors should provide more details about the practical algorithm. For example, how to implement the consensus update for the actor and dual variables? What is the structure of the neural networks used for the actor and critic? What are the specific optimization algorithms used for training the networks, and what are the learning rates and other hyperparameters?
2. The authors should provide more details about the experimental environment, including the specific parameters of the environment, the reward and cost functions, and the observation space for each agent. It is also important to clarify how the safety constraints are implemented and enforced in the environment.
3. The authors should provide more details about the baseline algorithms, including the specific implementation details and hyperparameter settings used for each baseline. For example, how is the centralized training performed in MASACLagrangian, and what are the specific communication protocols used in the decentralized baselines?

### Suggestions

The paper would benefit significantly from a more detailed explanation of the practical algorithm's implementation. Specifically, the consensus update mechanism for both actor and dual variables needs further clarification. The authors should describe the exact mathematical operations performed during the consensus step, including how the local gradients are aggregated and how the updates are applied to the local parameters. Furthermore, the architecture of the neural networks used for the actor and critic should be specified, including the number of layers, the type of activation functions, and the dimensionality of the hidden layers. The optimization algorithms used for training the networks, such as Adam or SGD, should be explicitly stated, along with the learning rates, batch sizes, and other relevant hyperparameters. This level of detail is crucial for reproducibility and for understanding the practical aspects of the proposed method. Without these details, it is difficult to assess the practical viability of the algorithm and compare it with other methods.

In addition to the algorithmic details, the experimental environment requires more thorough description. The authors should provide the specific parameters of the environment, such as the size of the state space, the action space, and the number of agents. The reward and cost functions should be clearly defined, including the mathematical expressions used to calculate them. The observation space for each agent should also be specified, detailing what information each agent receives from the environment. Furthermore, the implementation of the safety constraints needs to be clarified. The authors should explain how the constraints are enforced during the training process and how the algorithm ensures that the agents do not violate the safety requirements. This information is essential for understanding the experimental setup and the validity of the results. The lack of these details makes it difficult to evaluate the experimental results and to compare them with other studies.

Finally, the baseline algorithms need more detailed descriptions. For MASACLagrangian, the authors should explain how the centralized training is performed, including the architecture of the centralized critic and how the gradients are computed and applied. For the decentralized baselines, the communication protocols used should be specified, including the frequency of communication and the information exchanged between agents. The hyperparameter settings for each baseline should also be provided, such as the learning rates, batch sizes, and the discount factor. This level of detail is necessary to ensure a fair comparison between the proposed method and the baselines. Without these details, it is difficult to assess the relative performance of the proposed method and to draw meaningful conclusions from the experimental results.

### Questions

Please see the weaknesses above.

### Rating

6

### Confidence

4

**********
