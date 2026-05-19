### Summary

The paper introduces Language Agent Tree Search (LATS), a framework that combines the reasoning, acting, and planning capabilities of language models (LMs) into a unified system. LATS leverages the in-context learning ability of LMs and integrates Monte Carlo Tree Search (MCTS) to enable LMs as agents with LM-powered value functions and self-reflections for proficient exploration and enhanced decision-making. The key feature of LATS is the incorporation of an environment for external feedback, which offers a more deliberate and adaptive problem-solving mechanism. The experimental evaluation across diverse domains, including programming, interactive question-answering (QA), web navigation, and math, validates the effectiveness and generality of LATS in decision-making while maintaining competitive or improved reasoning performance.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper proposes a novel framework, LATS, that combines reasoning, acting, and planning for language models. This is a significant contribution as it addresses the limitations of existing methods that are either reflexive or lack the incorporation of external feedback.
2. The experimental results are comprehensive and demonstrate the effectiveness of LATS across various domains. The paper shows that LATS achieves state-of-the-art performance on several benchmarks, including programming, interactive question-answering (QA), web navigation, and math.
3. The paper is well-written and provides a clear explanation of the proposed framework and its components. The figures and tables are informative and help to illustrate the key concepts and results.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed discussion of the limitations of LATS. While the authors mention that LATS has a higher computational cost compared to simpler prompting methods, they do not elaborate on the specific scenarios where this cost might be prohibitive. It would be helpful to understand the trade-offs between performance and computational resources, especially in real-world applications where resources might be limited. For instance, what is the latency of LATS compared to simpler methods, and how does this impact its usability in interactive settings? Furthermore, a more detailed analysis of the memory footprint of LATS would be beneficial, as this could also be a limiting factor in certain deployments.
2. The paper could also discuss the potential challenges in scaling LATS to more complex environments or tasks. While the authors mention that LATS assumes the ability to revert to earlier states, which may not be universally applicable, they do not provide a detailed analysis of how this assumption might affect the performance of LATS in environments where this is not possible. It would be useful to understand the specific types of environments where LATS might struggle and what modifications might be needed to address these challenges. For example, how would LATS perform in environments with stochastic transitions or partial observability, where reverting to a previous state is not straightforward?

### Suggestions

The paper would benefit from a more thorough analysis of the computational cost associated with LATS. While the authors acknowledge that LATS is more computationally expensive than simpler methods, they should provide a more detailed breakdown of the computational resources required, including latency, memory usage, and the number of tokens generated. This analysis should also consider the impact of different hyperparameter settings on computational cost, such as the number of search iterations and the size of the language model. Furthermore, it would be beneficial to compare the computational cost of LATS with other search-based methods, such as Tree of Thoughts and Reasoning via Planning, to provide a more comprehensive understanding of its efficiency. This analysis should also include a discussion of the practical implications of these computational costs, such as the feasibility of using LATS in real-time applications or on resource-constrained devices. A detailed analysis of the computational cost would allow readers to better understand the trade-offs between performance and resource usage when using LATS.

To address the limitations of LATS in environments where reverting to earlier states is not possible, the authors should explore potential modifications to the framework. One possible approach would be to incorporate a mechanism for handling stochastic transitions, such as using a probabilistic model to predict the outcome of actions. Another approach would be to explore the use of techniques for dealing with partial observability, such as maintaining a belief state or using recurrent neural networks to track the history of observations. The authors should also consider the impact of these modifications on the performance of LATS and provide empirical results to demonstrate their effectiveness. Furthermore, it would be beneficial to discuss the limitations of these modifications and identify the types of environments where LATS might still struggle. This discussion should also include a comparison of LATS with other methods that are designed to handle stochastic transitions or partial observability, such as reinforcement learning or planning with uncertainty.

Finally, the paper should include a more detailed discussion of the limitations of the value function used in LATS. While the authors mention that the value function is based on a combination of the language model's score and self-consistency, they do not provide a detailed analysis of the effectiveness of this value function in different scenarios. It would be beneficial to explore alternative value functions, such as those based on reward shaping or learned value functions, and compare their performance with the current value function. Furthermore, the authors should discuss the potential limitations of the current value function, such as its sensitivity to the choice of hyperparameters or its ability to generalize to new environments. This discussion should also include a comparison of the value function used in LATS with other value functions used in related work, such as those used in Tree of Thoughts or Reasoning via Planning.

### Questions

1. How does the performance of LATS compare to other state-of-the-art methods in terms of computational cost and efficiency?
2. What are the potential challenges in scaling LATS to more complex environments or tasks, and how can these challenges be addressed?
3. How does the value function used in LATS compare to other value functions used in related work, and what are the potential limitations of the current value function?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
