### Summary

The paper proposes a framework called Progressive Thought Refinement (PTR) to enable large language models to progressively refine their responses. The framework consists of two stages: (1) Thought-Answer Preparation, where the model generates a sequence of thoughts and an improved answer based on an initial query, and (2) Progressive Weighted Thought-Mask Fine-tuning, where the model is fine-tuned to focus on refining its thoughts and answer. The authors claim that PTR can improve the performance of LLMs across various tasks without requiring task-specific fine-tuning.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

- The paper is well-organized and easy to follow.
- The authors provide a comprehensive evaluation of PTR across various tasks, including knowledge reasoning, code generation, and mathematical reasoning, demonstrating the effectiveness of the proposed approach.

### Weaknesses

#### Some Related Works


#### comment

 - The authors claim that the proposed method is annotation-free, but the thought generation and answer refinement processes require a strong model and a weak model, which implies the need for some form of supervision or pre-existing models. This undermines the claim of being annotation-free, as the models used for thought generation and refinement are not generated without any human input or supervision. The reliance on a strong model for thought generation and refinement introduces a dependency on its quality and potential biases, which is not addressed by the authors' claim of annotation-free learning.
- The paper lacks a detailed analysis of the computational cost associated with the proposed method. The iterative refinement process, involving multiple calls to a strong model and fine-tuning, could be computationally expensive, especially for large language models. The authors should provide a more thorough analysis of the time and resources required for training and inference, comparing it to existing methods. This analysis should include the number of parameters, training time, and inference time, as well as the memory requirements for training and inference.
- The paper does not provide a clear explanation of how the weak and strong models are selected and how their performance affects the overall performance of the proposed method. The authors should provide a more detailed analysis of the impact of different weak and strong models on the performance of the proposed method. Specifically, they should investigate how the performance gap between the weak and strong models affects the quality of the generated thoughts and the final answer. The authors should also discuss the criteria used to select the weak and strong models and how these criteria relate to the performance of the proposed method.

### Suggestions

The authors should clarify the claim of being annotation-free by explicitly stating that they are referring to the absence of human annotation on the final output, rather than the absence of any form of supervision or pre-existing models. They should also acknowledge the potential limitations of relying on strong models for thought generation and refinement, and discuss how these limitations might affect the overall performance of the proposed method. Furthermore, the authors should provide a more detailed analysis of the computational cost associated with the proposed method, including the time and resources required for training and inference. This analysis should compare the computational cost of the proposed method to existing methods, and should include a discussion of the trade-offs between computational cost and performance. The authors should also provide a more detailed explanation of how the weak and strong models are selected and how their performance affects the overall performance of the proposed method. Specifically, they should investigate how the performance gap between the weak and strong models affects the quality of the generated thoughts and the final answer. The authors should also discuss the criteria used to select the weak and strong models and how these criteria relate to the performance of the proposed method. This analysis should include a discussion of the potential limitations of using specific weak and strong models, and how these limitations might affect the generalizability of the proposed method.

To improve the evaluation of the proposed method, the authors should include a more detailed analysis of the impact of different weak and strong models on the performance of the proposed method. This analysis should include a comparison of the performance of the proposed method using different combinations of weak and strong models, and should investigate how the performance gap between the weak and strong models affects the quality of the generated thoughts and the final answer. The authors should also discuss the criteria used to select the weak and strong models and how these criteria relate to the performance of the proposed method. This analysis should include a discussion of the potential limitations of using specific weak and strong models, and how these limitations might affect the generalizability of the proposed method. Furthermore, the authors should provide a more detailed analysis of the computational cost associated with the proposed method, including the time and resources required for training and inference. This analysis should compare the computational cost of the proposed method to existing methods, and should include a discussion of the trade-offs between computational cost and performance. The authors should also provide a more detailed explanation of how the weak and strong models are selected and how their performance affects the overall performance of the proposed method. Specifically, they should investigate how the performance gap between the weak and strong models affects the quality of the generated thoughts and the final answer. The authors should also discuss the criteria used to select the weak strong models and how these criteria relate to the performance of the proposed method.

### Questions

- How does the proposed method compare to existing approaches in terms of computational cost and efficiency?
- How does the performance of the proposed method vary with different weak and strong models?
- How does the proposed method handle cases where the strong model makes incorrect predictions?

### Rating

5

### Confidence

4

**********
