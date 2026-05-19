### Summary

This paper introduces OptBatch, a novel data selection method for instruction tuning of large language models (LLMs). OptBatch focuses on the learnability of whole batch data rather than individual samples. It employs stratified sampling to ensure data distribution coverage and maximizes the relative distance between samples within a batch to enhance diversity. Additionally, it utilizes Hessian gradient optimization to guide the selection strategy for subsequent batches. The authors demonstrate the effectiveness of OptBatch through extensive experiments on three diverse downstream datasets, showing that it achieves robust generalization across various pruning rates and models, including LLaMa3 and ChatGLM3. The method reduces computational costs by 20-40% while maintaining or improving performance compared to full dataset training. The paper also includes evaluations using GPT-4 scores and other metrics for multi-turn dialogue, multilingual translation, and QA tasks, consistently demonstrating OptBatch's optimal performance.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel approach to data selection for instruction tuning of LLMs, focusing on batch-level learnability rather than individual sample importance. This is a unique perspective that has not been extensively explored in previous work.
2. The method is well-motivated and grounded in theoretical analysis, with clear explanations of the geometric set cover and Lipschitz continuity of the gradient. The authors provide a solid foundation for their approach, making it easier to understand and appreciate the underlying principles.
3. The paper is well-written and organized, with clear explanations of the methodology, experiments, and results. The figures and tables are informative and effectively support the claims made in the paper.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a thorough discussion of the limitations of the proposed method. While the authors mention some limitations in the conclusion, a more detailed analysis of potential drawbacks and failure cases would be beneficial. Specifically, the paper does not explore scenarios where the assumptions underlying the method, such as the smoothness of the loss landscape or the representativeness of the initial batches, might break down. For instance, in highly non-convex loss landscapes, the Hessian approximation might not be accurate, leading to suboptimal data selection. Furthermore, the method's reliance on batch-level diversity might not be suitable for tasks where individual samples contain critical, task-specific information that could be missed by the selection process.
2. The paper could benefit from a more detailed analysis of the computational complexity of the proposed method. While the authors mention that it reduces computational costs, a more rigorous analysis of the time and space complexity would be helpful. The paper should provide a breakdown of the computational cost associated with each step of the algorithm, including the Hessian calculation, stratified sampling, and diversity maximization. This analysis should also consider the impact of different batch sizes and dataset sizes on the overall computational cost. A comparison with the computational cost of other data selection methods would also be valuable.
3. The paper does not provide a clear explanation of how the method handles different types of data, such as text, images, and audio. While the method is presented as a general approach, the experiments are limited to text data. It is unclear how the method would be adapted to handle other data modalities, especially those with high dimensionality and complex structures. For example, how would the Hessian be approximated for image data, and how would the diversity maximization be performed in the feature space of images or audio?

### Suggestions

To address the limitations regarding the assumptions of the method, the authors should include a more detailed discussion of the scenarios where the method might fail or underperform. Specifically, they should analyze the impact of non-convex loss landscapes on the accuracy of the Hessian approximation and the effectiveness of the data selection process. It would be beneficial to include experiments on datasets with varying degrees of non-convexity to demonstrate the robustness of the method. Furthermore, the authors should explore the impact of the initial batch selection on the overall performance. If the initial batches are not representative of the entire dataset, the method might converge to a suboptimal solution. The authors could consider using a more robust initialization strategy, such as random sampling from the entire dataset, to mitigate this issue. Additionally, the authors should investigate the performance of the method on tasks where individual samples contain critical information, and compare it with methods that focus on individual sample importance.

To improve the analysis of computational complexity, the authors should provide a detailed breakdown of the time and space complexity of each step of the algorithm. This analysis should include the computational cost of calculating the Hessian, performing stratified sampling, and maximizing diversity. The authors should also consider the impact of different batch sizes and dataset sizes on the overall computational cost. A comparison with the computational cost of other data selection methods, such as random sampling or importance sampling, would be valuable. The authors could also explore techniques to reduce the computational cost of the Hessian calculation, such as using low-rank approximations or stochastic estimation methods. Furthermore, the authors should provide empirical results on the actual running time of the method on different datasets and hardware configurations.

To address the lack of clarity regarding the handling of different data types, the authors should provide a more detailed explanation of how the method can be adapted to handle image and audio data. Specifically, they should discuss how the Hessian can be approximated for these data modalities, and how the diversity maximization can be performed in their feature spaces. For image data, the authors could consider using convolutional neural networks to extract features and then apply the method in the feature space. For audio data, the authors could consider using recurrent neural networks or transformers to extract features. The authors should also provide experimental results on image and audio datasets to demonstrate the effectiveness of the method on these data modalities. This would significantly enhance the generalizability of the proposed method.

### Questions

1. How does the method handle noisy or irrelevant data in the dataset? Is there a mechanism to identify and exclude such data from the selection process?
2. Can the method be applied to other types of data, such as images or audio? If so, how would the method be adapted to handle these different data modalities?
3. How does the method perform when the dataset is highly imbalanced? Does it tend to select samples from the majority class more often than the minority class?
4. What is the impact of the batch size on the performance of the method? Is there an optimal batch size for different datasets and models?
5. How does the method compare to other state-of-the-art data selection methods in terms of performance and computational cost? Are there any specific scenarios where the proposed method outperforms or underperforms compared to other methods?

### Rating

6

### Confidence

3

**********
