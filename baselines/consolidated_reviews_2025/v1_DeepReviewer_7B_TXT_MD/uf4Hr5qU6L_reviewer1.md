### Summary

The paper introduces a prompting framework called PreCoT, which aims to enhance the reasoning capabilities of LLMs by incorporating problem representation into the Chain-of-Thought (CoT) prompting approach. The authors draw inspiration from human problem-solving strategies, where initial and goal states are identified and used to guide the reasoning process. PreCoT is evaluated on 15 benchmarks across arithmetic, commonsense, and symbolic reasoning tasks, demonstrating improvements over standard CoT prompting in both few-shot and zero-shot settings.

### Soundness

2

### Presentation

2

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

The paper would benefit from a more in-depth error analysis, comparing the specific types of errors made by PreCoT with those made by standard CoT. For example, are there specific types of reasoning steps or problem structures where PreCoT excels or struggles compared to CoT? A detailed breakdown of errors, categorized by the nature of the mistake (e.g., arithmetic, logical, or misinterpretation of the problem), would provide a more nuanced understanding of the method's strengths and weaknesses. This analysis should also consider the complexity of the problem, as the benefits of PreCoT might be more pronounced in simpler tasks, while more complex tasks might show diminishing returns. Furthermore, it would be valuable to examine how the quality of the extracted initial and goal states affects the overall performance of PreCoT. For instance, how does the method perform when the extracted states are incomplete or inaccurate? This analysis could involve introducing controlled variations in the extracted states and observing the impact on the final reasoning accuracy. Such an analysis would help to understand the robustness of the method and its sensitivity to the quality of the problem representation.

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
