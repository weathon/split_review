### Summary

This paper proposes STRATEGIST, a novel framework that integrates the strengths of large language models (LLMs) with multi-agent reinforcement learning (MARL) to enhance strategic decision-making in complex, partially observable environments. The approach leverages LLMs to learn high-level strategic abstractions, which are then refined and executed by a low-level mechanism based on self-play and evolutionary strategies. The framework is evaluated in two challenging games: Game of Pure Strategy (GOPS) and Avalon, demonstrating superior performance over traditional RL methods and other LLM-based agents.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-structured and clearly written, making it easy to follow the proposed methodology and experimental results.
2. The integration of LLMs with MARL is a promising direction for enhancing strategic decision-making in complex environments. The proposed dual-level approach, which combines high-level strategic abstraction with low-level policy execution, is innovative and addresses key challenges in multi-agent reinforcement learning.
3. The paper provides a thorough evaluation of the proposed framework in two complex games, Game of Pure Strategy (GOPS) and Avalon. The results demonstrate the effectiveness of STRATEGIST in achieving higher win rates and adapting to dynamic environments compared to traditional RL methods and other LLM-based agents.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational resources required for training and execution, which is crucial for assessing the practical applicability of the framework. Specifically, the paper lacks information on the number of GPUs used, the training time per epoch, and the inference time for both the LLM and the RL components. This information is essential for understanding the scalability of the approach and its feasibility in resource-constrained environments.
2. The paper could benefit from a more in-depth discussion of the limitations of the proposed framework, particularly in terms of its generalizability to other types of strategic environments. While the paper demonstrates the effectiveness of STRATEGIST in two specific games, it does not address how well the framework would perform in environments with different characteristics, such as those with continuous action spaces or more complex state representations. The paper should also discuss the potential for overfitting to the specific games used in the evaluation.
3. The paper could explore the impact of different LLM architectures and prompting strategies on the performance of STRATEGIST. The paper does not discuss how the choice of LLM, the specific prompts used to guide the LLM, or the fine-tuning process affects the overall performance of the framework. A more detailed analysis of these factors would provide valuable insights into the robustness and adaptability of the proposed approach.

### Suggestions

The paper should include a detailed analysis of the computational resources required for training and execution. This should include the number of GPUs used, the training time per epoch, and the inference time for both the LLM and the RL components. This information is crucial for assessing the practical applicability of the framework and understanding its scalability. Furthermore, the paper should discuss the memory requirements of the framework, which can be a significant factor in resource-constrained environments. The authors should also consider providing a breakdown of the computational cost associated with each component of the framework, such as the LLM, the RL algorithm, and the self-play process. This would allow readers to better understand the bottlenecks and potential areas for optimization.

To address the limitations regarding generalizability, the paper should include a more thorough discussion of the potential challenges and adaptations required to apply STRATEGIST to other types of strategic environments. This should include a discussion of how the framework would perform in environments with continuous action spaces, more complex state representations, or different types of strategic interactions. The authors should also discuss the potential for overfitting to the specific games used in the evaluation and suggest strategies for mitigating this risk. For example, the paper could explore the use of cross-validation or other techniques for evaluating the generalization performance of the framework. Additionally, the paper should discuss the potential for the framework to be applied to other domains, such as robotics or autonomous driving, and identify the challenges and opportunities associated with these applications.

The paper should also include a more detailed analysis of the impact of different LLM architectures and prompting strategies on the performance of STRATEGIST. This should include a comparison of different LLMs, such as GPT-3.5, GPT-4, or other open-source models, and an analysis of how the choice of LLM affects the quality of the learned strategic abstractions. The paper should also explore the impact of different prompting strategies on the performance of the framework, such as chain-of-thought prompting or few-shot prompting. Furthermore, the paper should discuss the fine-tuning process for the LLM and how this process affects the overall performance of the framework. This analysis should provide valuable insights into the robustness and adaptability of the proposed approach and guide future research in this area.

### Questions

1. How does the performance of STRATEGIST scale with the complexity of the environment? Are there any limitations in terms of the size or complexity of the games that can be effectively handled by the framework?
2. How sensitive is the performance of STRATEGIST to the choice of LLM? Would using a different LLM lead to significant changes in the results?
3. How does the framework handle situations where the LLM-generated strategies are not optimal or lead to suboptimal outcomes? Are there any mechanisms in place to detect and correct such issues?

### Rating

6

### Confidence

3

**********
