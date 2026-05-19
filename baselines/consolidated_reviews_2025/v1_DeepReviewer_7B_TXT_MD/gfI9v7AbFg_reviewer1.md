### Summary

This paper introduces STRATEGIST, a novel framework that integrates the strengths of large language models (LLMs) with traditional reinforcement learning (RL) techniques to enhance strategic decision-making in complex, multi-agent environments. The authors propose a dual-level approach that combines high-level strategic abstraction using LLMs with low-level policy execution using RL. This integration aims to address the limitations of relying solely on RL, which often requires extensive training data and computational resources, especially in environments with partial observability and hidden information. STRATEGIST employs an evolutionary process for LLM-based strategy refinement, generating and evaluating high-level strategies that are then refined and tested through self-play interactions. The framework is evaluated in two complex, multi-turn games: Game of Pure Strategy (GOPS) and Avalon, demonstrating superior performance compared to traditional RL methods and other LLM-based agents. The results highlight STRATEGIST’s ability to achieve higher win rates and adaptability in dynamic environments, showcasing the potential of combining LLMs with RL for strategic decision-making.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper introduces a novel framework, STRATEGIST, which effectively combines the strengths of large language models (LLMs) and reinforcement learning (RL) to address the challenges of strategic decision-making in complex multi-agent environments. This integration is particularly innovative in the context of partially observable and hidden information scenarios, where traditional RL methods often struggle.
2. The dual-level approach, with high-level strategy abstraction using LLMs and low-level policy execution using RL, allows for efficient learning and adaptation. The evolutionary process for LLM-based strategy refinement, coupled with self-play interactions, demonstrates a creative solution to optimizing strategies in dynamic environments.
3. The evaluation of STRATEGIST in two distinct games, Game of Pure Strategy (GOPS) and Avalon, provides a robust empirical basis for the claims made in the paper. The results show that STRATEGIST outperforms both traditional RL methods and other LLM-based agents, highlighting the framework’s superior performance and adaptability.
4. The paper is well-structured and clearly articulates the problem, methodology, and results. The use of figures and tables enhances the readability and understanding of the proposed framework and its performance.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed explanation of the specific mechanisms used for strategy refinement and how the evolutionary process ensures effective exploration of the strategy space. While the high-level strategy abstraction using LLMs is innovative, the paper lacks clarity on how these strategies are represented and evolved. For instance, it is not clear how the LLM generates new strategies, what the specific prompts are, or how the evolutionary algorithm operates on these strategies. The paper should provide more details on the mutation and crossover operations in the context of strategic abstraction, including how these operations are adapted to the specific game environments.
2. The evaluation, while comprehensive, could be strengthened by including a wider range of baseline methods, particularly those that also leverage LLMs for strategic decision-making. The current comparisons are limited to traditional RL methods and other LLM-based agents, but a more thorough comparison with state-of-the-art LLM-based strategic agents would provide a clearer picture of the framework's relative performance. It would also be beneficial to see how STRATEGIST performs against methods that use different forms of strategic abstraction, not just RL-based approaches.
3. The paper does not discuss the computational resources required for training and execution, which is crucial for assessing the practical applicability of the framework. The paper should provide details on the hardware used, the training time, and the inference time for both the LLM and the RL components. This information is essential for understanding the scalability and feasibility of the proposed approach, especially in resource-constrained environments. Furthermore, the paper should discuss the memory requirements of the framework, which can be a significant factor in practical applications.
4. The paper could provide a more in-depth analysis of the types of strategies learned by the LLM and how they contribute to the overall performance. A qualitative analysis of the learned strategies, including examples of successful and unsuccessful strategies, would provide valuable insights into the framework's decision-making process. This analysis should also discuss the limitations of the learned strategies and how they might be improved in future work.
5. The paper could benefit from a more detailed discussion of the limitations of the proposed approach and potential avenues for future research. For example, the paper should discuss the limitations of the evolutionary process, such as its potential for getting stuck in local optima, and how these limitations might be addressed. The paper should also discuss the limitations of the RL component, such as its sensitivity to hyperparameter tuning and the potential for overfitting, and how these limitations might be mitigated.

### Suggestions

The paper would benefit from a more detailed explanation of the strategy refinement process. Specifically, the authors should elaborate on how the LLM generates new strategies, including the specific prompts used and the criteria for selecting successful strategies. It would be helpful to understand the exact nature of the prompt engineering and how it influences the quality of the generated strategies. Furthermore, the paper should provide a more detailed description of the evolutionary algorithm, including the mutation and crossover operations in the context of strategic abstraction. For example, how are strategies represented internally, and how are these representations modified during the evolutionary process? A concrete example of how a strategy is encoded and evolved would greatly enhance the clarity of the paper. The authors should also discuss the limitations of the evolutionary process, such as its potential for getting stuck in local optima, and how these limitations might be addressed.

To strengthen the evaluation, the authors should include a wider range of baseline methods, particularly those that also leverage LLMs for strategic decision-making. This would provide a more comprehensive comparison and better highlight the advantages of the proposed framework. The paper should also include a more detailed analysis of the types of strategies learned by the LLM, including examples of successful and unsuccessful strategies. This analysis should discuss the limitations of the learned strategies and how they might be improved in future work. For instance, are the learned strategies overly specific to the training environment, or can they generalize to new scenarios? A qualitative analysis of the learned strategies would provide valuable insights into the framework's decision-making process. The authors should also discuss the computational resources required for training and execution, including the hardware used, the training time, and the inference time for both the LLM and the RL components. This information is crucial for understanding the scalability and feasibility of the proposed approach, especially in resource-constrained environments. Furthermore, the paper should discuss the memory requirements of the framework, which can be a significant factor in practical applications.

Finally, the paper should include a more detailed discussion of the limitations of the proposed approach and potential avenues for future research. For example, the authors should discuss the limitations of the evolutionary process, such as its potential for getting stuck in local optima, and how these limitations might be addressed. The paper should also discuss the limitations of the RL component, such as its sensitivity to hyperparameter tuning and the potential for overfitting, and how these limitations might be mitigated. The authors should also discuss the generalizability of the proposed approach to other types of strategic environments and how it might be adapted to different types of games. A more thorough discussion of the limitations and future directions would provide a more balanced and comprehensive view of the proposed framework.

### Questions

1. How does the evolutionary process for LLM-based strategy refinement ensure effective exploration of the strategy space? What mechanisms are in place to prevent the algorithm from getting stuck in local optima?
2. What specific strategies are generated by the LLM, and how are they evaluated and refined through self-play interactions? Could you provide examples of successful and unsuccessful strategies, and discuss the criteria used for their selection?
3. How does STRATEGIST compare to other state-of-the-art LLM-based strategic agents in terms of performance and computational efficiency? Are there specific scenarios where STRATEGIST outperforms or underperforms compared to these methods?
4. What are the computational resources required for training and execution of STRATEGIST? How does the framework scale with increasing complexity of the game environment?
5. How generalizable is the proposed approach to other types of strategic environments? Are there specific types of games or scenarios where STRATEGIST might face challenges in adapting?

### Rating

5

### Confidence

3

**********
