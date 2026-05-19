### Summary

The paper proposes a Progressive Thought Refinement (PTR) framework to improve the reasoning ability of LLMs. The framework includes two stages: (1) Thought data construction stage, where a weak-strong model collaborative selection strategy is used to build a high-quality progressive refinement dataset; (2) Thought-Mask Fine-Tuning Phase, where a training structure is designed to mask the "thought" and adjust loss weights to encourage LLMs to refine prior thought. The authors claim that PTR enhances LLM performance across ten diverse tasks without task-specific fine-tuning.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The proposed PTR framework is designed to stimulate the model's intrinsic refinement ability, which is a novel approach to improving LLMs' reasoning capabilities.
2. The weak-strong model collaborative selection strategy eliminates the need for accurate labels, which is a significant advantage over traditional methods that rely heavily on supervision signals.
3. The weighted thought-mask fine-tuning method instills general PR capabilities in LLMs, allowing them to improve their responses over multiple iterations.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a clear explanation of how the weak and strong models are selected and how their collaboration leads to improved performance. Specifically, the criteria for choosing these models and the mechanism by which their interaction refines the initial thoughts are not well-defined. It is unclear what specific model architectures or sizes constitute 'weak' and 'strong' in this context, and how their relative capabilities impact the quality of the generated data.
2. The paper does not provide a detailed analysis of the impact of the proposed method on different types of tasks and domains. The performance gains of the proposed method are not consistently significant across all tasks, and the paper does not provide a thorough analysis of why the method works well on some tasks but not on others. The lack of task-specific analysis makes it difficult to understand the generalizability of the approach.
3. The paper does not address the potential limitations and challenges of the proposed method, such as the computational cost of the two-stage training process and the potential for bias in the generated data. The computational overhead of the iterative refinement process is not quantified, and the paper does not discuss how the method scales with larger models or datasets. Furthermore, the potential for the weak-strong model collaboration to introduce biases or reinforce existing biases in the training data is not explored.
4. The paper lacks a comprehensive comparison with existing methods for improving LLMs' reasoning capabilities. The paper does not clearly articulate how the proposed method differs from and improves upon existing approaches, such as self-improvement or other iterative refinement techniques. A more detailed comparison with state-of-the-art methods is needed to establish the novelty and effectiveness of the proposed approach.

### Suggestions

The paper would benefit from a more detailed explanation of the weak-strong model collaboration strategy. Specifically, the authors should provide a clear definition of what constitutes a 'weak' and a 'strong' model in their context, including specific model architectures and sizes. They should also elaborate on the criteria used to select these models and how their relative capabilities influence the quality of the generated data. For example, do they use models with different numbers of parameters, or models trained on different datasets? Furthermore, the authors should provide a more detailed explanation of the collaborative selection process itself. How do the models interact during the data generation phase? Is it an iterative process, or do the models contribute to different parts of the data generation pipeline? A concrete example of how this collaboration works in practice would be beneficial. The authors should also discuss the potential limitations of this approach, such as the risk of introducing biases from the strong model or the computational cost of using multiple models.

To address the lack of task-specific analysis, the authors should provide a more detailed breakdown of the performance gains across different task types. They should analyze the characteristics of the tasks where the method performs well and compare them to the tasks where the method does not show significant improvements. For example, are the tasks with significant gains primarily reasoning-based, or are there other common factors? The authors should also investigate the reasons for the varying performance across tasks. Is it due to the nature of the task, the quality of the training data, or the inherent limitations of the proposed method? A more in-depth analysis of the error patterns on different tasks would also be helpful. Furthermore, the authors should consider conducting ablation studies to understand the contribution of each component of the proposed method to the overall performance. This would help to identify the key factors that drive the improvements and to understand the limitations of the approach.

Finally, the paper needs a more comprehensive comparison with existing methods for improving LLM reasoning capabilities. The authors should clearly articulate how their method differs from and improves upon existing approaches, such as self-improvement or other iterative refinement techniques. A detailed comparison with state-of-the-art methods is needed to establish the novelty and effectiveness of the proposed approach. The authors should also discuss the potential limitations of their method, such as the computational cost of the two-stage training process and the potential for bias in the generated data. The computational overhead of the iterative refinement process should be quantified, and the paper should discuss how the method scales with larger models or datasets. The potential for the weak-strong model collaboration to introduce biases or reinforce existing biases in the training data should also be addressed. The authors should also consider comparing their method with other iterative refinement techniques that do not rely on a weak-strong model collaboration.

### Questions

1. How does the proposed method compare to existing methods for improving LLMs' reasoning capabilities in terms of performance, computational cost, and generalization ability?
2. What are the potential limitations and challenges of the proposed method, and how can they be addressed?
3. How does the weak-strong model collaborative selection strategy ensure the quality of the generated thoughts and answers, and what are the criteria for selecting the weak and strong models?
4. How does the weighted thought-mask fine-tuning method encourage LLMs to refine their responses, and what are the key factors that contribute to the effectiveness of this approach?
5. How does the proposed method perform on tasks that require common sense reasoning, and how does it compare to other methods that are specifically designed for common sense reasoning tasks?

### Rating

5

### Confidence

3

**********
