### Summary

This paper proposes LATS, a framework that synergizes LM reasoning, acting, and planning. LATS extends ReAct and ToT by incorporating external feedback and self-reflection. LATS is evaluated across diverse domains, including programming, interactive question-answering (QA), web navigation, and math.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

- LATS combines the strengths of ReAct and ToT, integrating external feedback and self-reflection to enhance LM performance.
- The framework is evaluated across diverse domains, including programming, interactive QA, web navigation, and math, demonstrating its versatility.

### Weaknesses

#### Some Related Works

[1] Chain of Thought Prompting Elicits Reasoning in Large Language Models
[2] ReAct: Synergizing Reasoning and Acting in Language Models
[3] Tree of Thoughts: Deliberate Problem Solving with Large Language Models
[4] Reflexion: Language Agents with Verbal Reinforcement Learning
[5] Training language agents with online preference optimization
[6] Large language models as programs: Aligning and scaling llms through compi language
[7] Reasoning and planning with large language models
[8] Reflexion: Improving long-form reasoning capability of language models through self-reflection

#### comment

 - The paper does not provide sufficient technical novelty. It primarily combines existing techniques like MCTS, self-reflection, and value functions, which have been previously explored in works such as CoT [1], ReAct [2], ToT [3], Reflexion [4], and Comi [5]. The integration of these techniques, while potentially useful, does not represent a significant conceptual leap. The paper lacks a clear explanation of how the specific combination and adaptation of these methods lead to a fundamentally new approach, rather than just an incremental improvement.
- The paper lacks a detailed analysis of the computational overhead introduced by the tree-based search and the value function. The practical implications of this overhead, especially in resource-constrained environments, are not thoroughly discussed. The paper should provide a more rigorous analysis of the time and memory complexity of LATS, including a breakdown of the costs associated with each component of the framework.
- The paper does not adequately address the limitations of the proposed approach. For example, how does LATS handle situations where the external feedback is noisy or inconsistent? The paper should include a discussion of the robustness of LATS to imperfect feedback and explore potential strategies for mitigating the impact of noisy feedback. Furthermore, the paper does not discuss the potential for bias in the feedback and how this might affect the performance of LATS.

### Suggestions

The paper should provide a more detailed explanation of the specific mechanisms by which LATS integrates external feedback and self-reflection. It is not sufficient to simply state that these techniques are incorporated; the paper needs to articulate the precise algorithms and data structures used to manage the tree of possible actions, track the agent's state, and incorporate feedback into the search process. For example, the paper should describe how the value function is trained and how it is used to guide the search. A more detailed explanation of the self-reflection mechanism is also needed, including how the agent generates and evaluates its own reflections. The paper should also include a discussion of the limitations of the current approach and potential avenues for future research. For example, the paper could explore how LATS could be extended to handle more complex tasks or more diverse types of feedback.

The paper needs to provide a more thorough analysis of the computational cost of LATS. This analysis should include a detailed breakdown of the time and memory complexity of each component of the framework, including the tree search, the value function, and the self-reflection mechanism. The paper should also discuss the practical implications of these costs, including the potential for LATS to be computationally expensive in resource-constrained environments. The paper should also explore potential strategies for reducing the computational cost of LATS, such as pruning the search tree or using more efficient algorithms for value function estimation. A comparison of the computational cost of LATS with other related methods would also be beneficial.

The paper should also address the limitations of the proposed approach, particularly its robustness to noisy or inconsistent feedback. The paper should include a discussion of how LATS could be made more robust to such feedback, including the use of techniques such as filtering or weighting. The paper should also explore the potential for bias in the feedback and how this might affect the performance of LATS. Furthermore, the paper should discuss the potential for the agent to get stuck in a local optimum due to the tree-based search and how this could be mitigated. The paper should also explore the potential for the agent to generate infeasible actions due to the lack of constraints on the action space and how this could be addressed.

### Questions

- How does LATS handle situations where the external feedback is noisy or inconsistent? Does the framework have any mechanisms to filter or correct inaccurate feedback?
- How does the performance of LATS scale with the complexity of the task? Are there any limitations on the types of tasks that LATS can effectively handle?
- How does LATS compare to other state-of-the-art methods in terms of computational efficiency and resource requirements?

### Rating

3

### Confidence

4

**********
