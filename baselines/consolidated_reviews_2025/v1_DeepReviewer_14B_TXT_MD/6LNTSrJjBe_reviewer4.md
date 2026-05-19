### Summary

The authors propose a new framework for reasoning and decision making with language models. The framework is based on Monte Carlo tree search, and incorporates both self-reflection and external feedback. The authors demonstrate the effectiveness of their approach on several tasks, including HotpotQA, HumanEval, and WebShop.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The authors propose a novel framework for reasoning and decision making with language models. The framework is based on Monte Carlo tree search, and incorporates both self-reflection and external feedback. The authors demonstrate the effectiveness of their approach on several tasks, including HotpotQA, HumanEval, and WebShop.

### Weaknesses

#### Some Related Works


#### comment

The authors do not provide a detailed analysis of the computational cost of their approach. It is not clear how the computational cost of LATS compares to other methods, and whether it is feasible to use LATS in real-world applications.

### Suggestions

The paper would benefit from a more thorough analysis of the computational demands of the proposed LATS framework. While the authors mention the use of Monte Carlo Tree Search (MCTS), which is known to be computationally intensive, they do not provide a detailed breakdown of the time and memory requirements. Specifically, it would be helpful to understand how the number of simulations, the depth of the search tree, and the size of the language model impact the overall computational cost. A comparison with other methods, such as those based on beam search or greedy decoding, would also be valuable. This analysis should include not only the time taken to generate a single solution, but also the memory footprint of the algorithm, which can be a limiting factor in practical applications. Furthermore, the authors should discuss the scalability of their approach with respect to the complexity of the task and the size of the input. For example, how does the computational cost scale with the number of reasoning steps required to solve a problem? Addressing these points would provide a more complete picture of the practical limitations of the proposed method.

In addition to the computational analysis, the paper could be strengthened by a more detailed discussion of the hyperparameter selection process. The authors mention that they use default hyperparameters for the baselines, but it is not clear how these hyperparameters were chosen and whether they are optimal for the specific tasks considered in the paper. A sensitivity analysis of the key hyperparameters, such as the number of MCTS simulations, the exploration parameter, and the reflection depth, would be beneficial. This analysis should also include a discussion of how these hyperparameters interact with each other and how they affect the performance of the algorithm. Furthermore, the authors should provide guidance on how to choose appropriate hyperparameters for new tasks or datasets. This would make the proposed method more accessible to other researchers and practitioners.

Finally, the paper could benefit from a more detailed discussion of the limitations of the proposed approach. While the authors demonstrate the effectiveness of LATS on several tasks, they do not discuss the potential failure modes or scenarios where the method might not perform well. For example, how does LATS perform on tasks that require long-range reasoning or complex planning? Are there any specific types of problems where LATS is likely to fail? A discussion of these limitations would provide a more balanced view of the proposed method and help to identify areas for future research. It would also be helpful to compare the performance of LATS with other state-of-the-art methods on a wider range of tasks, including those that are known to be challenging for language models.

### Questions

How does the computational cost of LATS compare to other methods?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
