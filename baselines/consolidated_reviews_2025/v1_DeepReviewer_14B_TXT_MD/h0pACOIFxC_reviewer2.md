### Summary

This paper proposes a meta-learning framework to address the problem of retraining foundation models (FM) on multiple tasks, with the goal of making the model more adaptable to unseen downstream tasks. The authors propose a Meta-Adapters objective function, which incorporates parameter-efficient fine-tuning (PEFT) during the retraining phase. The paper provides theoretical results for linear models, showing that the proposed method can recover optimally adaptable parameters, while standard retraining does not. The paper also presents empirical results on the ConvAI2 dataset, demonstrating the effectiveness of the proposed method.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel meta-learning framework for retraining foundation models, which is a significant contribution to the field. The proposed Meta-Adapters objective function is a creative combination of meta-learning and parameter-efficient fine-tuning techniques.
2. The paper provides rigorous theoretical analysis for linear models, demonstrating the suboptimality of standard retraining and the advantages of the proposed method. The theoretical results are well-supported by empirical evidence on both synthetic and real-world datasets.
3. The paper is well-written and clearly explains the proposed method and its theoretical underpinnings. The experiments are well-designed and provide strong evidence for the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The paper focuses primarily on linear models in its theoretical analysis, and it is unclear how the results generalize to non-linear models. The theoretical guarantees provided for linear models may not hold for non-linear models, which are more commonly used in practice. Specifically, the analysis relies on properties of linear transformations and low-rank updates, which may not directly translate to the complex, non-convex loss landscapes of neural networks. The paper lacks a discussion on the potential challenges in extending the theoretical framework to non-linear settings, such as the impact of activation functions and the non-convexity of the loss function.
2. The experiments are conducted on a relatively small-scale model (RoBERTa-Large, 355M parameters) and a single dataset (ConvAI2). This raises concerns about the scalability of the proposed method to larger models and its generalizability to other tasks and datasets. The paper does not provide sufficient evidence to demonstrate that the observed performance gains would hold for larger models with billions of parameters, which are commonly used in state-of-the-art applications. Furthermore, the ConvAI2 dataset, while useful, may not be representative of the diversity and complexity of real-world tasks. The paper lacks experiments on more challenging datasets and tasks, such as those involving multi-modal inputs or more complex reasoning.
3. The paper does not provide a detailed analysis of the computational cost of the proposed method compared to standard retraining and fine-tuning approaches. The meta-learning framework may introduce additional computational overhead, which could be a concern for practical applications. The paper lacks a quantitative comparison of the training time and memory requirements of the proposed method with standard retraining and fine-tuning approaches. This makes it difficult to assess the practical feasibility of the proposed method, especially for resource-constrained environments.

### Suggestions

The paper would benefit from a more thorough discussion on the limitations of the theoretical analysis and its applicability to non-linear models. The authors should acknowledge that the current theoretical framework is specific to linear models and discuss the challenges in extending it to non-linear settings. This discussion should include an analysis of how the non-convexity of the loss landscape in neural networks might affect the convergence and optimality of the proposed meta-learning algorithm. Furthermore, the authors could explore potential modifications to the theoretical framework that could accommodate non-linearities, such as using techniques from non-convex optimization theory or developing approximations for the loss function. It would also be beneficial to provide some empirical analysis on the behavior of the proposed method on non-linear models, even if a full theoretical analysis is not feasible.

To address the concerns about scalability and generalizability, the authors should conduct experiments on larger models and more diverse datasets. This could include experiments on models with billions of parameters, such as large language models, and datasets that cover a wider range of tasks and domains. For example, the authors could evaluate the proposed method on tasks involving multi-modal inputs, such as image and text, or tasks that require more complex reasoning, such as question answering or summarization. Additionally, the authors should consider using a variety of evaluation metrics to assess the performance of the proposed method, including metrics that measure the adaptability of the model to unseen tasks. This would provide a more comprehensive evaluation of the proposed method and its potential for real-world applications.

Finally, the paper should include a detailed analysis of the computational cost of the proposed method. This analysis should include a comparison of the training time and memory requirements of the proposed method with standard retraining and fine-tuning approaches. The authors should also discuss potential strategies for reducing the computational cost of the proposed method, such as using more efficient optimization algorithms or parallelizing the training process. This analysis would help to assess the practical feasibility of the proposed method and its potential for use in resource-constrained environments. Furthermore, the authors should provide a clear explanation of the trade-offs between computational cost and performance, allowing readers to make informed decisions about the applicability of the proposed method.

### Questions

1. How does the proposed method perform on larger models and more diverse datasets? Can the authors provide more empirical evidence to support the generalizability of their method?
2. What is the computational cost of the proposed method compared to standard retraining and fine-tuning approaches? Is the proposed method computationally feasible for large-scale applications?
3. Can the authors discuss the potential limitations of the theoretical analysis, particularly its focus on linear models, and how it might be extended to non-linear models?

### Rating

6

### Confidence

3

**********
