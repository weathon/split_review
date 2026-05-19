### Summary

This paper presents ACTOR, an agent that can perform high-level, long-horizon, abstract goals in 3D households. A new dataset BehaviorHub is also proposed.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

The problem studied in this paper is interesting and important. The methodology looks reasonable. The proposed dataset could be valuable to the research community.

### Weaknesses

#### Some Related Works


#### comment

The writing of the paper could be improved. It is hard to follow the paper at the first place. For example, in the abstract, the term “value” is ambiguous. It could refer to the value function in reinforcement learning or the value of objects in the scene. In line 051, “value priorities” are mentioned without clear definition. The concept of “value” needs to be rigorously defined within the context of the agent's decision-making process. The paper should clarify whether this value is a scalar reward, a vector of preferences, or something else entirely. The lack of clarity makes it difficult to understand the agent's motivation and planning process. Furthermore, the relationship between the agent's internal representation of value and the external environment is not well-established, leading to confusion about how the agent makes decisions.

It is unclear how the proposed method is better than existing MCTS methods. The paper does not provide a detailed comparison with state-of-the-art MCTS algorithms, particularly in terms of computational complexity, convergence properties, and performance on similar tasks. The novelty of the approach is not clearly articulated, and it is difficult to assess whether the proposed method offers significant improvements over existing techniques. The paper should include a more thorough analysis of the method's strengths and weaknesses compared to other MCTS variants, and provide empirical evidence to support any claims of superiority.

### Suggestions

The paper should start by clearly defining the concept of “value” as it is used in the context of the ACTOR agent. This definition should be precise and unambiguous, specifying whether it is a scalar, vector, or other mathematical object. The paper should then explain how this value is used in the agent's decision-making process, including how it is computed, updated, and used to guide the agent's actions. For example, if the value is a scalar reward, the paper should explain how it is derived from the environment and how it relates to the agent's goals. If it is a vector of preferences, the paper should explain how these preferences are represented and how they influence the agent's planning. The paper should also clarify the relationship between the agent's internal value representation and the external environment, explaining how the agent uses its perception of the environment to determine the value of different actions or states. This clarification is crucial for understanding the agent's behavior and the overall effectiveness of the proposed approach.

To address the concerns about the method's novelty and comparison to existing MCTS methods, the paper should include a detailed analysis of how the proposed method differs from traditional MCTS algorithms. This analysis should focus on the specific modifications or extensions made to the standard MCTS framework, such as the use of language-based commands or real-valued functions in the value functions. The paper should also provide a theoretical analysis of the method's computational complexity and convergence properties, comparing these properties to those of existing MCTS algorithms. Furthermore, the paper should include an empirical evaluation of the method's performance on a set of benchmark tasks, comparing its performance to that of state-of-the-art MCTS algorithms. This evaluation should include a variety of metrics, such as success rate, planning time, and computational cost, to provide a comprehensive assessment of the method's strengths and weaknesses. The paper should also discuss the limitations of the proposed method and suggest directions for future research.

Finally, the paper should provide more details on the implementation of the ACTOR agent and the BehaviorHub dataset. This includes details on the architecture of the agent, the specific algorithms used for planning and decision-making, and the structure and content of the dataset. The paper should also discuss the limitations of the dataset and potential biases that may be present. The paper should also include a discussion of the ethical implications of the research, particularly in relation to the use of human-like agents in virtual environments. By addressing these points, the paper can significantly improve its clarity, rigor, and overall contribution to the field.

### Questions

Please clarify the concept of value and the contribution of the paper compared to existing MCTS methods.

### Rating

6

### Confidence

3

**********
