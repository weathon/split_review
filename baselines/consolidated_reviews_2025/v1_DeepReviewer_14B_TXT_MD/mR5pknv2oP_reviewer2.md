### Summary

This paper proposes a method called SECToR (Self-Education via Chain-of-Thought Reasoning) that allows language models to teach themselves new skills without human-generated training data. The authors demonstrate that chain-of-thought reasoning can act as a policy improvement operator, similar to how Monte-Carlo Tree Search is used in AlphaZero. They train language models to solve addition problems using chain-of-thought reasoning and show that the models can improve themselves and solve harder problems over time. The results indicate that the models can teach themselves to add numbers with up to 29 digits without access to any ground truth examples beyond an initial supervised fine-tuning phase.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

1. The idea of using chain-of-thought reasoning as a policy improvement operator is novel and interesting.
2. The paper provides a clear and detailed description of the proposed method and the experimental setup.
3. The results are presented in a clear and concise manner, and the authors provide a thorough analysis of the results.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is only evaluated on the task of addition, which is a relatively simple task. It is not clear how well the method would generalize to more complex tasks. The authors should consider evaluating the method on a wider range of tasks to demonstrate its generalizability. Specifically, the current evaluation lacks tasks that require more diverse reasoning skills, such as those involving symbolic manipulation, planning, or common-sense reasoning. The method's reliance on a specific problem structure, such as the digit-by-digit nature of addition, may not translate well to problems with less rigid or more varied structures.
2. The paper does not compare the proposed method to any other existing methods. It is not clear how the proposed method compares to other methods in terms of performance and efficiency. The authors should consider comparing the proposed method to other relevant methods to demonstrate its advantages and disadvantages. A comparison to methods that use similar self-improvement techniques, or those that leverage chain-of-thought reasoning in different ways, would be particularly valuable. Without such comparisons, it is difficult to assess the true contribution of the proposed method.
3. The paper does not provide any analysis of the limitations of the proposed method. It is important to understand the limitations of a method to be able to use it effectively. The authors should provide a discussion of the potential limitations of the proposed method and suggest directions for future research. For example, the authors could discuss the computational cost of the method, its sensitivity to hyperparameter settings, or its potential failure modes. A more thorough analysis of these limitations would be beneficial.

### Suggestions

The authors should broaden the evaluation of their method to include more complex and diverse tasks. Specifically, they could consider tasks that involve symbolic manipulation, such as solving algebraic equations or proving simple theorems. Tasks that require planning, such as navigating a grid world or solving a puzzle, would also be valuable. Additionally, incorporating tasks that require common-sense reasoning, such as question answering or natural language inference, would provide a more comprehensive assessment of the method's generalizability. These tasks should be chosen to test different aspects of reasoning and problem-solving, and the authors should provide a detailed analysis of the method's performance on each task. This would help to identify the strengths and weaknesses of the method and provide a clearer understanding of its applicability to different types of problems. Furthermore, the authors should consider using established benchmark datasets for these tasks to facilitate comparisons with other methods.

To better contextualize the performance of the proposed method, the authors should compare it to existing approaches. This comparison should include methods that use similar self-improvement techniques, such as those based on reinforcement learning or iterative refinement. It should also include methods that leverage chain-of-thought reasoning in different ways, such as those that use it for few-shot learning or for generating explanations. The comparison should be performed on the same tasks as the proposed method, and the authors should provide a detailed analysis of the results. This analysis should include a discussion of the strengths and weaknesses of each method, as well as a comparison of their computational cost and efficiency. This would help to establish the novelty and contribution of the proposed method and provide a more complete understanding of its performance relative to other approaches.

Finally, the authors should provide a more thorough analysis of the limitations of their method. This analysis should include a discussion of the computational cost of the method, its sensitivity to hyperparameter settings, and its potential failure modes. The authors should also discuss the assumptions that the method makes and the conditions under which it is likely to perform well or poorly. This analysis should be supported by empirical evidence, and the authors should provide specific examples of cases where the method fails or performs poorly. This would help to identify areas for future research and provide a more complete understanding of the method's capabilities and limitations. Furthermore, the authors should discuss the potential for bias in the self-generated training data and how this might affect the method's performance.

### Questions

1. How does the proposed method compare to other existing methods in terms of performance and efficiency?
2. How well does the proposed method generalize to more complex tasks?
3. What are the limitations of the proposed method, and what are the potential directions for future research?

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
