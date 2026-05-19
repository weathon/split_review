### Summary

This paper proposes a new framework, Progressive Thought Refinement (PTR), to enhance the performance of large language models (LLMs) across various tasks. PTR consists of two main phases: (1) Thought data construction, where a weak-strong model collaborative selection strategy is used to build a high-quality progressive refinement dataset, and (2) Thought-Mask Fine-Tuning, where a training structure is designed to mask the "thought" and adjust loss weights to encourage LLMs to refine prior thoughts. The experimental results show that PTR significantly improves LLM performance across ten diverse tasks without task-specific fine-tuning.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The proposed PTR framework is a novel approach to improving LLM performance by stimulating the model's intrinsic refinement ability.
2. The weak-strong model collaborative selection strategy is an efficient way to construct high-quality PTR datasets without the need for extra feedback.
3. The weighted thought-mask fine-tuning method is a creative solution to instill general PR capabilities in LLMs.
4. The experimental results show that PTR significantly improves LLM performance across ten diverse tasks without task-specific fine-tuning.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a clear explanation of how the weak and strong models are selected and how their collaboration leads to improved performance. Specifically, the criteria for choosing these models and the mechanism by which their interaction refines the initial thoughts are not well-defined. It is unclear what specific model architectures or sizes constitute 'weak' and 'strong' in this context, and how their relative capabilities impact the quality of the generated data. For instance, are 'weak' models significantly smaller or trained on less diverse datasets, and how does this difference contribute to the progressive refinement process?
2. The paper does not provide a detailed analysis of the impact of the proposed method on different types of tasks and domains. The performance gains of the proposed method are not consistently significant across all tasks, and the paper does not provide a thorough analysis of why the method works well on some tasks but not on others. The lack of task-specific analysis makes it difficult to understand the generalizability of the approach. For example, are there specific task characteristics that make them more amenable to the PTR framework, and what are the limitations when applied to tasks with different requirements?
3. The paper does not address the potential limitations and challenges of the proposed method, such as the computational cost of the two-stage training process and the potential for bias in the generated data. The computational overhead of the iterative refinement process is not quantified, and the paper does not discuss how the method scales with larger models or datasets. Furthermore, the potential for the weak-strong model collaboration to introduce biases or reinforce existing biases in the training data is not explored. This is a critical oversight, as the quality of the generated data directly impacts the performance of the fine-tuned model.
4. The paper lacks a comprehensive comparison with existing methods for improving LLMs' reasoning capabilities. The paper does not clearly articulate how the proposed method differs from and improves upon existing approaches, such as self-improvement or other iterative refinement techniques. A more detailed comparison with state-of-the-art methods is needed to establish the novelty and effectiveness of the proposed approach. Without this, it is difficult to assess the true contribution of the PTR framework.

### Suggestions

To address the lack of clarity regarding the weak and strong model selection, the authors should provide a detailed explanation of the criteria used for choosing these models. This should include specific information about the model architectures, sizes, and training data used for both the weak and strong models. Furthermore, the authors should elaborate on the mechanism by which the collaboration between these models leads to improved performance. For example, do the weak models generate initial thoughts that are then refined by the strong models, or is there a more complex interaction? A concrete example of how this collaboration works in practice would be beneficial. The authors should also discuss the potential limitations of this approach, such as the risk of introducing biases from the strong model or the computational cost of using multiple models. It would be useful to see an ablation study that examines the impact of different model combinations on the final performance.

To improve the analysis of the impact of the proposed method on different types of tasks and domains, the authors should provide a more detailed breakdown of the performance gains across different task types. This should include an analysis of the characteristics of the tasks where the method performs well and compare them to the tasks where the method does not show significant improvements. For example, are the tasks with significant gains primarily reasoning-based, or are there other common factors? The authors should also investigate the reasons for the varying performance across tasks. Is it due to the nature of the task, the quality of the training data, or the inherent limitations of the proposed method? A more in-depth analysis of the error patterns on different tasks would also be helpful. Furthermore, the authors should consider conducting ablation studies to understand the contribution of each component of the proposed method to the overall performance. This would help to identify the key factors that drive the improvements and to understand the limitations of the approach.

Finally, the paper needs a more comprehensive comparison with existing methods for improving LLMs' reasoning capabilities. The authors should clearly articulate how their method differs from and improves upon existing approaches, such as self-improvement or other iterative refinement techniques. This should include a detailed comparison of the proposed method with state-of-the-art methods, highlighting the advantages and disadvantages of each approach. The authors should also discuss the potential limitations of their method, such as the computational cost of the two-stage training process and the potential for bias in the generated data. The computational overhead of the iterative refinement process should be quantified, and the paper should discuss how the method scales with larger models or datasets. The potential for the weak-strong model collaboration to introduce biases or reinforce existing biases in the training data should also be addressed. The authors should also consider comparing their method with other iterative refinement techniques that do not rely on a weak-strong model collaboration.

### Questions

1. How does the proposed method compare to existing methods for improving LLMs' reasoning capabilities in terms of performance, computational cost, and generalization ability?
2. What are the potential limitations and challenges of the proposed method, and how can they be addressed?
3. How does the weak-strong model collaborative selection strategy ensure the quality of the generated thoughts and answers, and what are the criteria for selecting the weak and strong models?
4. How does the weighted thought-mask fine-tuning method encourage LLMs to refine their responses, and what are the key factors that contribute to the effectiveness of this approach?
5. How does the proposed method perform on tasks that require common sense reasoning, and how does it compare to other methods that are specifically designed for common sense reasoning tasks?

### Rating

6

### Confidence

3

**********
