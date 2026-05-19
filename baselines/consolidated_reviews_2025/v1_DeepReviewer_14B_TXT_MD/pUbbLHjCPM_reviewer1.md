### Summary

This paper proposes Progressive Thought Refinement (PTR), a framework that enables LLMs to progressively refine their responses. The authors claim that PTR operates in two phases: (1) Thought data construction stage and (2) Thought-Mask Fine-Tuning Phase. In the first phase, the authors propose a weak and strong model collaborative selection strategy to build a high-quality progressive refinement dataset. In the second phase, the authors design a training structure to mask the "thought" and adjust loss weights to encourage LLMs to refine prior thought.

### Soundness

1

### Presentation

2

### Contribution

1

### Strengths

The research topic is promising and the authors tried to address the problem of enabling LLMs to refine responses.

### Weaknesses

#### Some Related Works


#### comment

1. The paper is not well-written and it is hard to understand. For example, in the abstract, it is unclear what is thought, why the authors propose to mask the thought, and how to adjust the loss weights. In introduction, the authors claimed that "The key limitation is that errors addressed in one domain may not apply to other tasks, since different tasks exhibit varying error types." However, I don't understand this limitation and how the proposed method can address it.
2. The proposed method is not novel or motivating enough. The method looks like a combination of existing techniques, and the authors did not provide sufficient justifications why the proposed techniques can be beneficial compared to existing techniques. The authors did not provide concrete evidence or examples to support the claim about the limitations of existing methods and how the proposed method addresses them. The novelty of the proposed method is questionable without clear differentiations and justifications.
3. The experiments are not convincing. The authors did not provide detailed experimental setup (e.g., model used, how to generate the results for baseline and the proposed method, etc.). Results for baseline methods are not provided. The authors did not provide sufficient details about the proposed method (e.g., how to determine the weights in the loss, etc.). Therefore, the experiments are not reproducible.

### Suggestions

The paper needs significant improvements in clarity and technical depth. The core concept of 'thought' needs to be explicitly defined early on, perhaps with a concrete example illustrating its role in the proposed framework. The abstract should clearly articulate the problem being addressed, the proposed solution, and the key contributions. It should explain why masking the 'thought' is necessary and how the loss weights are adjusted, providing a high-level overview of the technical details. The introduction should elaborate on the limitations of existing methods, providing specific examples of how they fail to generalize across different tasks due to varying error types. The authors should then clearly explain how their method overcomes these limitations, providing a compelling motivation for their approach. For example, if the 'thought' is an intermediate reasoning step, the authors should explain how this is different from existing methods that use chain-of-thought prompting, and why masking this 'thought' is beneficial.

To address the lack of novelty, the authors should provide a detailed comparison of their method with existing techniques, highlighting the key differences and advantages. They should justify the use of weak and strong models for data construction, explaining why this approach is superior to using a single model. The authors should also provide a clear rationale for the specific loss function and the masking strategy, explaining how these choices contribute to the overall performance of the model. For example, if the weak model is used to generate initial thoughts and the strong model is used to refine them, the authors should explain why this collaborative approach is more effective than using a single model for both tasks. The authors should also provide concrete examples of how the proposed method addresses the limitations of existing methods, demonstrating the benefits of their approach in specific scenarios. The authors should also provide a more detailed explanation of the loss function, including how the weights are determined and why this specific weighting scheme is used.

Finally, the experimental section needs to be significantly improved to ensure reproducibility. The authors should provide detailed information about the models used, including the specific architectures and hyperparameters. They should also provide a clear description of the data generation process for both the baseline methods and the proposed method, including the specific prompts and parameters used. The results for the baseline methods should be clearly presented, allowing for a direct comparison with the proposed method. The authors should also provide a detailed explanation of how the weights in the loss function are determined, including any specific formulas or algorithms used. The authors should also include an ablation study to evaluate the impact of different components of the proposed method, such as the masking strategy and the loss weights. This would help to demonstrate the effectiveness of each component and provide a more comprehensive understanding of the proposed method.

### Questions

Please address the questions in the weaknesses.

### Rating

3

### Confidence

4

**********
