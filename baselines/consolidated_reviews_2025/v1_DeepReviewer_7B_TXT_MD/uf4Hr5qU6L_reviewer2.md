### Summary

The paper proposes a prompting framework that enhances the reasoning capabilities of LLMs by incorporating problem representation. The authors draw inspiration from human problem-solving strategies, where initial and goal states are identified and used to guide the reasoning process. The proposed framework, PreCoT, is evaluated on 15 benchmarks across arithmetic, commonsense, and symbolic reasoning tasks, demonstrating improvements over standard CoT prompting in both few-shot and zero-shot settings.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

- The paper is well-written and easy to follow.
- The motivation is clear and well-grounded in cognitive psychology.
- The experimental setup is comprehensive, covering a wide range of reasoning tasks and models.

### Weaknesses

#### Some Related Works


#### comment

 - The paper lacks a detailed analysis of the types of errors made by PreCoT compared to standard CoT, which would provide insights into the method's strengths and weaknesses.
- The improvements over standard CoT are modest, especially on more complex tasks, raising questions about the practical significance of the approach.
- The paper does not explore the sensitivity of PreCoT to different problem representations or the impact of the quality of the initial and goal states on the final reasoning performance.

### Suggestions

The paper would benefit from a more in-depth analysis of the error patterns produced by PreCoT compared to standard Chain-of-Thought (CoT) prompting. A detailed breakdown of error types, such as arithmetic errors, logical fallacies, or misinterpretations of the problem context, would provide a clearer picture of where PreCoT excels and where it falls short. For example, does PreCoT struggle more with problems requiring complex reasoning steps, or does it make more errors in specific types of arithmetic calculations? This analysis should also consider the complexity of the problem, as the benefits of PreCoT might be more pronounced in simpler tasks, while more complex tasks might show diminishing returns. Furthermore, it would be valuable to examine how the quality of the extracted initial and goal states affects the overall performance of PreCoT. For instance, how does the method perform when the extracted states are incomplete or inaccurate? This analysis could involve introducing controlled variations in the extracted states and observing the impact on the final reasoning accuracy. Such an analysis would help to understand the robustness of the method and its sensitivity to the quality of the problem representation.

To further strengthen the paper, the authors should investigate the impact of different problem representations on the performance of PreCoT. This could involve experimenting with various ways of encoding the initial and goal states, such as using different levels of abstraction or incorporating additional contextual information. For example, instead of just extracting the numerical values, the representation could include units or the context of the problem. This would help to understand which aspects of the problem representation are most important for the success of PreCoT. Additionally, the authors should explore the sensitivity of PreCoT to the quality of the initial and goal states. This could involve introducing controlled variations in the extracted states and observing the impact on the final reasoning accuracy. For example, how does the method perform when the extracted states are incomplete or inaccurate? This analysis could involve introducing controlled variations in the extracted states and observing the impact on the final reasoning accuracy. Such an analysis would help to understand the robustness of the method and its sensitivity to the quality of the problem representation.

Finally, the paper should provide a more thorough discussion of the computational overhead introduced by PreCoT. While the authors mention that the additional cost is minimal, a more detailed analysis of the time and resources required for extracting the initial and goal states, and for the subsequent reasoning process, would be beneficial. This analysis should also consider the scalability of the method to more complex problems and larger models. It would also be useful to compare the computational cost of PreCoT with other methods that aim to improve the reasoning capabilities of LLMs. This would help to contextualize the practical applicability of the proposed method and its trade-offs in terms of performance and computational cost. The authors should also discuss the potential for optimizing the extraction of initial and goal states to reduce the computational overhead.

### Questions

- How does the quality of the extracted initial and goal states affect the performance of PreCoT? Could the authors provide more details on the process of extracting these states and any potential biases or limitations?
- What are the computational costs associated with PreCoT, especially in comparison to standard CoT prompting? How does the method scale to more complex problems or larger models?
- Could the authors elaborate on the potential for extending PreCoT to other reasoning tasks or domains, such as natural language inference or planning problems?

### Rating

3

### Confidence

4

**********
