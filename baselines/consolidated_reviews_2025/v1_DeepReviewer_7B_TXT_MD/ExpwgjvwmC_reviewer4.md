### Summary

This paper proposes a novel evaluation framework, OMNIINPUT, to assess the performance of AI/ML models across the entire input space, rather than relying on pre-defined test sets. The framework uses an efficient sampler to generate representative inputs and evaluates model performance through precision and recall metrics. The authors apply OMNIINPUT to evaluate various models on MNIST and CIFAR-10 datasets, providing new insights into model behavior and demonstrating the potential for more robust, generalizable models.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The motivation is clear, and the proposed method is reasonable.
3. The experimental results are comprehensive and convincing.

### Weaknesses

#### Some Related Works


#### comment

1. The novelty of the paper is limited. The proposed method is similar to the traditional generative model evaluation, and the proposed method is just a re-implementation of the traditional evaluation method. The paper does not adequately address how the proposed method differs fundamentally from existing evaluation techniques, particularly in terms of the underlying assumptions and the types of insights it provides. The use of a sampler to generate inputs and then evaluate model performance is not a novel concept in itself, and the paper needs to more clearly articulate the specific advantages of this approach over existing methods.
2. The paper does not provide a detailed analysis of the computational complexity of the proposed method. The paper should include a discussion of the time and memory requirements of the sampler and the evaluation process, especially when applied to larger datasets or more complex models. This is crucial for assessing the practical applicability of the method.
3. The paper does not provide a clear explanation of how the proposed method handles out-of-distribution (OOD) samples. While the method aims to evaluate models across the entire input space, it is unclear how it distinguishes between samples that are within the training distribution and those that are significantly outside. This distinction is important for understanding the model's robustness and generalization capabilities.

### Suggestions

The paper should more clearly articulate the specific advantages of the proposed method over existing evaluation techniques. While the use of a sampler to generate inputs is not novel, the paper needs to highlight the unique aspects of its approach, such as the specific sampling strategy or the way it aggregates the evaluation results. For example, the paper could discuss how the proposed method handles the exploration-exploitation trade-off in the input space, and how this affects the evaluation of model performance. A more detailed comparison with existing methods, including a discussion of the limitations of those methods, would strengthen the paper's contribution. The paper should also provide a more thorough analysis of the computational complexity of the proposed method, including the time and memory requirements for different dataset sizes and model architectures. This analysis should include a breakdown of the computational cost of each step in the method, such as the sampling process and the evaluation of model outputs. This would allow readers to better understand the practical limitations of the method and its applicability to different scenarios. 

Furthermore, the paper should provide a more detailed explanation of how the proposed method handles out-of-distribution (OOD) samples. The paper should clarify how the method distinguishes between samples that are within the training distribution and those that are significantly outside. This could involve a discussion of the sampling strategy used to generate OOD samples, and how the evaluation metrics are adapted to assess model performance on these samples. For example, the paper could discuss whether the method uses a separate OOD detection mechanism, or if it relies on the precision-recall metrics to implicitly identify OOD samples. The paper should also discuss the implications of the method's performance on OOD samples for the overall evaluation of model robustness and generalization capabilities. A more detailed analysis of the method's behavior on OOD samples would provide a more complete understanding of its strengths and limitations. 

Finally, the paper should include a more thorough discussion of the limitations of the proposed method. This should include a discussion of the assumptions made by the method, and the potential biases that could arise from these assumptions. The paper should also discuss the limitations of the method in terms of its applicability to different types of models and datasets. For example, the paper could discuss whether the method is suitable for evaluating models with complex architectures or for datasets with high dimensionality. A more thorough discussion of the limitations of the method would provide a more balanced and realistic assessment of its contribution.

### Questions

1. How does the proposed method handle the exploration-exploitation trade-off in the input space?
2. How does the proposed method handle out-of-distribution (OOD) samples?
3. What are the computational costs of the proposed method compared to traditional evaluation methods?

### Rating

5

### Confidence

4

**********
