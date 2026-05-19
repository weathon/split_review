### Summary

This paper presents a framework called Strategist, which combines large language models (LLMs) and traditional planning methods to improve decision-making in complex environments. Strategist leverages LLMs to generate high-level strategies, which are then refined and executed using techniques like Monte Carlo Tree Search (MCTS). The framework is designed to operate without extensive prior training data, using self-play and population-based methods for self-improvement. The authors evaluate Strategist in competitive, multi-turn games, including the Game of Pure Strategy (GOPS) and Avalon, a hidden-identity social deduction game. Results show that Strategist outperforms traditional reinforcement learning (RL) approaches, other LLM-based agents, and even human players in certain aspects, particularly in strategic randomization and policy refinement.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow, with clear explanations of the methodology and experimental setup.
2. The Strategist framework effectively combines LLMs with traditional planning techniques, leveraging the strengths of both approaches.
3. The authors conduct extensive experiments across multiple game environments, providing a thorough evaluation of Strategist’s performance.
4. The framework demonstrates impressive results, outperforming both human players and existing AI approaches in certain aspects, particularly in strategic randomization and policy refinement.

### Weaknesses

#### Some Related Works


#### comment

1. The Strategist framework is tested primarily on two games, GOPS and Avalon. While these games provide a good starting point, they may not fully represent the diversity of real-world decision-making scenarios. It would be beneficial to evaluate the framework in more varied environments, including those with continuous action spaces, stochastic transitions, and more complex state representations, to better assess its generalizability and robustness. For example, testing on environments with partial observability or those requiring long-term planning beyond the scope of the current games would be valuable.
2. Although the paper compares Strategist to traditional RL methods, it does not provide a detailed analysis of its computational efficiency. Including such an analysis would help readers understand the trade-offs involved in using Strategist, particularly in terms of training time, memory usage, and inference speed. For instance, the paper could compare the number of LLM calls, the depth of the MCTS search, and the overall wall-clock time required for training and evaluation, relative to the RL baselines.
3. The paper does not discuss the scalability of the Strategist framework in detail. As the complexity of the environment increases, it is unclear how well the framework will perform, especially in terms of computational resources and the ability to maintain effective strategies. Specifically, it is unclear how the framework would perform with a larger number of agents, more complex state spaces, or longer game horizons. A discussion of the limitations and potential bottlenecks would be valuable.
4. The paper does not address how Strategist handles ethical considerations, particularly in adversarial settings where deception and manipulation might be advantageous. It would be beneficial to discuss the ethical implications of using such a framework in real-world applications and how these concerns could be mitigated. For example, in a negotiation scenario, the framework might learn to exploit biases or use misleading tactics, which raises ethical questions about its deployment.

### Suggestions

To strengthen the evaluation of the Strategist framework, it is crucial to test it in a wider range of environments that better reflect the complexities of real-world decision-making. This should include environments with continuous action spaces, such as those found in robotics or control systems, and environments with stochastic transitions, which are common in many real-world scenarios. Furthermore, the framework should be evaluated in environments with partial observability, where agents must make decisions based on incomplete information, and in environments that require long-term planning, where the consequences of actions are not immediately apparent. This would provide a more comprehensive understanding of the framework's generalizability and robustness. For example, the authors could consider using benchmark environments from the OpenAI Gym or similar platforms, which offer a diverse set of challenges.

In addition to expanding the range of environments, a more detailed analysis of the computational efficiency of the Strategist framework is needed. This analysis should include a comparison of the training time, memory usage, and inference speed of Strategist with those of the RL baselines. The authors should provide a breakdown of the computational costs associated with different components of the framework, such as the number of LLM calls, the depth of the MCTS search, and the time required for self-play simulations. This would allow readers to better understand the trade-offs involved in using Strategist and to assess its practicality for different applications. Furthermore, the authors should investigate the impact of different hyperparameter settings on the computational efficiency of the framework, such as the number of MCTS simulations or the size of the LLM used.

Finally, the paper should address the scalability of the Strategist framework and its ethical implications. The authors should discuss how the framework would perform in environments with a larger number of agents, more complex state spaces, or longer game horizons. They should also consider the potential for the framework to be used in malicious ways, such as in adversarial settings where deception and manipulation might be advantageous. The authors should discuss the ethical implications of using such a framework in real-world applications and how these concerns could be mitigated. This could involve incorporating ethical guidelines into the training process or developing mechanisms to detect and prevent malicious behavior. A thorough discussion of these issues would enhance the paper's overall impact and relevance.

### Questions

1. How does Strategist perform in environments that are not game-based, such as real-world decision-making scenarios? Can the framework be adapted to handle such environments effectively?
2. How does the framework scale with the complexity of the environment? Are there any limitations in terms of computational resources or the ability to maintain effective strategies as the environment becomes more complex?
3. How does Strategist handle ethical considerations, particularly in adversarial settings where deception and manipulation might be advantageous? Are there any safeguards in place to prevent malicious use of the framework?

### Rating

5

### Confidence

3

**********
