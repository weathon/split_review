### Summary

The paper introduces STRATEGIST, a novel framework that integrates the strengths of large language models (LLMs) and traditional reinforcement learning (RL) to improve decision-making in complex, multi-agent environments. STRATEGIST leverages LLMs to generate high-level strategic abstractions, which are then refined and executed by a low-level mechanism, such as Monte Carlo Tree Search (MCTS). The framework is designed to learn and improve strategies through self-play simulations without requiring prior training data. The authors demonstrate the effectiveness of STRATEGIST in two challenging games: the Game of Pure Strategy (GOPS) and Resistance: Avalon, showing that it outperforms traditional RL methods, other LLM-based skill acquisition techniques, and pre-existing LLM agents.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper presents a novel approach by combining LLMs with a bi-level tree search framework for strategy learning in adversarial multi-agent environments. This integration is a creative solution to the limitations of LLMs in complex decision-making scenarios.
- The methodology is well-defined, with a clear distinction between high-level strategy learning and low-level policy refinement. The use of population-based self-play and a modular improvement method for high-level strategies is a significant contribution.
- The experimental results are compelling, demonstrating that STRATEGIST outperforms existing LLM-based self-improvement methods and traditional RL approaches in both GOPS and Avalon. The framework's ability to match human performance in Avalon while employing sophisticated mixed strategies is particularly noteworthy.
- The paper includes a comprehensive evaluation, comparing STRATEGIST against various baselines, including RL-based methods and other LLM agents. The results are supported by detailed analysis and visualizations, enhancing the credibility of the findings.

### Weaknesses

#### Some Related Works


#### comment

 - The paper could benefit from a more detailed discussion of the limitations of STRATEGIST, particularly in scenarios with highly dynamic or unpredictable environments. While the framework shows promise in the tested games, its performance in real-world applications with more complex and less structured environments remains unclear. Specifically, the reliance on self-play for strategy generation might lead to a lack of robustness when faced with novel strategies or unexpected behaviors from opponents not encountered during training. The paper should also address the potential for the framework to converge to suboptimal strategies due to the limited exploration of the strategy space during self-play.
- The computational cost of STRATEGIST, especially the bi-level tree search and the iterative self-improvement process, is not thoroughly analyzed. Providing insights into the scalability and efficiency of the framework would be valuable for practical applications. The paper lacks a detailed breakdown of the time complexity of the high-level strategy search and the low-level policy refinement, making it difficult to assess the feasibility of deploying STRATEGIST in resource-constrained environments. Furthermore, the memory requirements for storing the population of strategies and the computational overhead of the LLM-based strategy generation should be discussed.
- While the paper demonstrates the effectiveness of STRATEGIST in two specific games, it would be beneficial to explore its generalizability to a wider range of adversarial multi-agent environments. Testing the framework in different types of games with varying levels of complexity and information availability would strengthen the claims of its versatility. The current evaluation is limited to games with perfect information, and it is unclear how the framework would perform in games with partial observability or stochastic transitions. The paper should also consider the impact of the number of agents on the performance of STRATEGIST, as the computational cost and the complexity of the strategy space are likely to increase significantly with more agents.

### Suggestions

To address the limitations regarding dynamic environments, the authors should consider incorporating mechanisms that allow STRATEGIST to adapt to novel situations. This could involve introducing a form of online learning or meta-learning that enables the framework to adjust its strategies based on the observed behavior of opponents. For instance, the framework could be enhanced with a module that detects deviations from expected opponent behavior and triggers a re-evaluation of the current strategy. Additionally, the authors could explore the use of adversarial training techniques to generate more diverse and challenging opponent strategies during self-play, which would improve the robustness of the learned policies. The paper should also include a more detailed analysis of the exploration-exploitation trade-off in the high-level strategy search, and discuss how the framework balances the need to explore new strategies with the need to refine existing ones.

To improve the analysis of computational cost, the authors should provide a detailed breakdown of the time and space complexity of each component of STRATEGIST. This should include an analysis of the number of LLM calls, the depth of the MCTS search, and the size of the strategy population. The paper should also discuss the impact of different hyperparameter settings on the computational cost and the performance of the framework. Furthermore, the authors could explore techniques for optimizing the computational efficiency of STRATEGIST, such as using more efficient search algorithms or reducing the size of the strategy population. The paper should also include a discussion of the practical limitations of the framework in terms of the number of agents and the complexity of the environment, and suggest potential solutions for scaling the framework to more complex scenarios.

To enhance the generalizability of STRATEGIST, the authors should evaluate its performance in a wider range of adversarial multi-agent environments, including games with partial observability, stochastic transitions, and varying numbers of agents. This could involve testing the framework in benchmark environments from the multi-agent reinforcement learning literature. The paper should also discuss the challenges of applying STRATEGIST to real-world problems, such as the need for domain-specific knowledge and the difficulty of defining appropriate reward functions. The authors could also explore the use of transfer learning techniques to adapt the framework to new environments, which would reduce the need for extensive training from scratch. Finally, the paper should include a discussion of the ethical implications of using STRATEGIST in real-world applications, particularly in scenarios where the framework is used to make decisions that affect human lives.

### Questions

- How does STRATEGIST handle scenarios where the environment is highly dynamic or unpredictable? Are there mechanisms in place to adapt to such changes?
- Can the authors provide more details on the computational resources required for training and deploying STRATEGIST? How does the framework scale with the complexity of the environment and the number of agents?
- What are the potential limitations of STRATEGIST when applied to real-world problems outside of game environments? How might the framework need to be adapted for such applications?
- How does the framework ensure that the generated strategies are not only effective but also interpretable and explainable, especially in high-stakes decision-making scenarios?

### Rating

6

### Confidence

3

**********
