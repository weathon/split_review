### Summary

This paper introduces OptBatch, a novel method for efficient instruction tuning of large language models (LLMs). The method addresses the challenge of selecting high-quality data for instruction tuning by focusing on the learnability of whole batch data rather than individual samples. OptBatch uses stratified sampling and Hessian gradient optimization to enhance data diversity and reduce computational costs. The method achieves robust generalization across various downstream tasks and models, reducing computational costs by 20-40% while maintaining optimal performance.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel approach to data selection for instruction tuning, which is a critical aspect of improving the performance of large language models (LLMs).
2. The method is well-motivated and addresses a significant challenge in the field of LLMs.
3. The paper is well-written and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational complexity of the proposed method, which is important for understanding its scalability and practical applicability.
2. The paper does not provide a detailed analysis of the sensitivity of the proposed method to different hyperparameters, which is important for understanding its robustness and generalizability.
3. The paper does not provide a detailed analysis of the limitations of the proposed method, which is important for understanding its potential impact and future research directions.

### Suggestions

The paper should include a more thorough analysis of the computational complexity of OptBatch, particularly in comparison to existing data selection methods. This analysis should consider not only the theoretical complexity but also the practical implications, such as the actual time and memory requirements for different dataset sizes and model architectures. For example, providing a breakdown of the time spent on stratified sampling, Hessian gradient optimization, and the overall data selection process would be beneficial. Furthermore, the analysis should discuss how these costs scale with the size of the dataset and the dimensionality of the model's embedding space. This would allow readers to better assess the method's suitability for different applications and resource constraints.

In addition to computational complexity, the paper should also provide a more detailed analysis of the sensitivity of OptBatch to its hyperparameters. This analysis should include a systematic exploration of how different hyperparameter settings affect the performance of the method across various datasets and models. For example, the paper could investigate the impact of the number of strata used in stratified sampling, the learning rate and batch size used in Hessian gradient optimization, and the regularization parameters. The analysis should also discuss how these hyperparameters interact with each other and how they should be tuned for optimal performance. This would provide valuable guidance for practitioners who want to use OptBatch in their own work. It would also help to understand the robustness of the method and its potential limitations.

Finally, the paper should include a more detailed discussion of the limitations of OptBatch and its potential impact on future research. This discussion should address the scenarios where the method might not perform well, such as when the data distribution is highly non-uniform or when the model is highly overparameterized. The paper should also discuss the potential biases that might be introduced by the method and how these biases could be mitigated. Furthermore, the paper should suggest future research directions that could address these limitations and further improve the method. This would provide a more balanced and comprehensive view of the method's strengths and weaknesses and help to guide future research in this area.

### Questions

1. How does OptBatch perform on datasets with highly non-uniform distributions?
2. How does OptBatch perform on models with different architectures and sizes?
3. How does OptBatch perform on tasks that require different types of reasoning or knowledge?

### Rating

6

### Confidence

3

**********
