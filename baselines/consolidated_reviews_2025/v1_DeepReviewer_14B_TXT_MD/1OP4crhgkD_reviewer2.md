### Summary

The paper introduces SAMA, a novel method for multi-agent reinforcement learning (MARL) that uses pre-trained language models (PLMs) to generate semantically aligned subgoals. SAMA addresses the credit assignment problem in MARL by prompting PLMs with chain-of-thought to suggest goals, decompose them, and allocate subgoals. It also incorporates language-grounded RL to train policies conditioned on natural language subgoals. The method is evaluated on two challenging sparse-reward tasks, Overcooked and MiniRTS, where it demonstrates significant advantages in sample efficiency over state-of-the-art automatic subgoal generation (ASG) methods.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is interesting and leverages the power of PLMs to address the credit assignment problem in MARL.
- The experimental results show that SAMA significantly improves sample efficiency compared to state-of-the-art ASG methods on two challenging tasks.

### Weaknesses

#### Some Related Works


#### comment

 - The proposed method relies heavily on the quality of the PLMs and the prompts used to generate subgoals. The paper does not provide a detailed analysis of how sensitive the method is to the choice of PLMs and prompts.
- The paper does not compare SAMA to other non-PLM-based methods for addressing the credit assignment problem in MARL. It is unclear how SAMA compares to these methods in terms of performance and computational cost.
- The paper does not provide a detailed analysis of the computational cost of SAMA. The use of PLMs can be computationally expensive, and it is important to understand the trade-offs between performance and computational cost.
- The paper does not provide a detailed analysis of the limitations of the proposed method. It is important to understand the scenarios where SAMA may not perform well or may be computationally infeasible.
- The paper does not provide a detailed analysis of the impact of the self-reflection mechanism on the performance of SAMA. It is unclear how the self-reflection mechanism affects the quality of the generated subgoals and the overall performance of the method.

### Suggestions

The paper should include a more thorough investigation into the sensitivity of SAMA to the choice of pre-trained language models (PLMs) and the specific prompts used to generate subgoals. This should involve testing SAMA with a range of different PLMs, including those with varying sizes and architectures, and analyzing how the performance of the method changes. Furthermore, the prompts used to elicit subgoals from the PLMs should be systematically varied, and the impact of these variations on the quality of the generated subgoals and the overall performance of SAMA should be carefully examined. This analysis should include not only the final performance metrics but also the semantic coherence and relevance of the generated subgoals. It would be beneficial to explore the use of techniques such as prompt ensembling or prompt tuning to improve the robustness of the subgoal generation process.

In addition to comparing SAMA to other PLM-based methods, the paper should also include a comparison to non-PLM-based approaches for addressing the credit assignment problem in multi-agent reinforcement learning (MARL). This comparison should include methods that rely on intrinsic motivation, reward shaping, or other techniques for guiding agent behavior. The comparison should not only focus on final performance metrics but also consider the computational cost and sample efficiency of the different methods. It would be valuable to analyze the strengths and weaknesses of SAMA in comparison to these alternative approaches, highlighting the specific scenarios where SAMA is most effective and where it may be less suitable. This analysis should also consider the computational resources required by each method, providing a more complete picture of the trade-offs involved.

Finally, the paper should provide a more detailed analysis of the computational cost of SAMA, including the time and memory requirements for both training and inference. This analysis should consider the impact of the size of the PLMs used, the number of agents, and the complexity of the environment on the computational cost of the method. The paper should also discuss the limitations of SAMA, including the scenarios where it may not perform well or may be computationally infeasible. This discussion should include an analysis of the factors that contribute to these limitations, such as the complexity of the environment, the number of agents, and the quality of the PLMs used. Furthermore, the paper should provide a more detailed analysis of the impact of the self-reflection mechanism on the performance of SAMA, including how it affects the quality of the generated subgoals and the overall performance of the method.

### Questions

- How sensitive is SAMA to the choice of PLMs and prompts used to generate subgoals? Have you tested SAMA with different PLMs and prompts, and how does the performance vary?
- How does SAMA compare to other non-PLM-based methods for addressing the credit assignment problem in MARL? What are the advantages and disadvantages of SAMA compared to these methods?
- What is the computational cost of SAMA? How does it compare to the computational cost of other MARL methods?
- What are the limitations of SAMA? In what scenarios does SAMA not perform well or is computationally infeasible?
- How does the self-reflection mechanism affect the performance of SAMA? What is the impact of the self-reflection mechanism on the quality of the generated subgoals and the overall performance of the method?

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
