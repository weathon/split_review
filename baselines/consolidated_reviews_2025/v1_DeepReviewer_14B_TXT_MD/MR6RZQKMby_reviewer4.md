### Summary

The paper introduces the concept of model kinship to guide the merging of large language models (LLMs). The authors demonstrate that model kinship correlates with performance gains after merging, and propose a new merging strategy called Top-k Greedy Merging with Model Kinship. This approach leverages model kinship to select models for merging, aiming to improve multitask performance and avoid local optima. The paper provides empirical analysis and experimental results to support its claims.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel concept, model kinship, which draws an analogy to biological evolution and provides a new perspective on model merging.
2. The authors conduct comprehensive empirical analysis, including correlation analysis and sequence analysis of model evolution paths, to validate the effectiveness of model kinship.
3. The proposed Top-k Greedy Merging with Model Kinship strategy is shown to improve multitask performance and efficiency in the merging process.
4. The paper is well-organized and clearly presents its methodology, experiments, and results.

### Weaknesses

#### Some Related Works


#### comment

1. The paper focuses primarily on merging models derived from the same base model. It is unclear how the concept of model kinship and the proposed merging strategy would apply to models with different initializations or architectures. This limitation restricts the generalizability of the findings.
2. The paper does not provide a detailed analysis of the computational cost associated with calculating model kinship and performing the merging process. This information is crucial for assessing the practicality of the proposed approach, especially when dealing with large language models.
3. The paper lacks a thorough discussion of potential limitations or failure cases of the proposed merging strategy. Understanding the scenarios where the approach might not be effective is important for its practical application.

### Suggestions

The authors should investigate the applicability of model kinship to models with different initializations or architectures. This could involve exploring techniques for aligning or normalizing model weights before calculating kinship, or adapting the kinship metric to account for architectural differences. For example, one could consider using a layer-wise kinship measure, where each layer is compared independently and then aggregated, which might be more robust to architectural variations. Furthermore, the authors should provide a more detailed analysis of the computational cost associated with calculating model kinship and performing the merging process. This should include a breakdown of the time and memory requirements for each step, as well as a comparison to other merging techniques. It would be beneficial to explore methods for reducing the computational overhead, such as using low-rank approximations or efficient distance metrics. This analysis should also consider the scalability of the approach to larger models and datasets.

To address the lack of discussion on limitations, the authors should conduct experiments to identify scenarios where the proposed merging strategy might fail or underperform. This could involve testing the approach on models with different levels of kinship, or on tasks that require specific expertise not captured by the kinship metric. For example, it would be useful to examine the performance of the merged models on tasks that are significantly different from the tasks used to calculate kinship. The authors should also investigate the sensitivity of the merging strategy to the choice of hyperparameters, such as the value of k in Top-k Greedy Merging. A thorough analysis of these limitations would provide a more complete understanding of the strengths and weaknesses of the proposed approach and guide its practical application.

Finally, the authors should consider exploring alternative merging strategies that could complement or improve upon the proposed Top-k Greedy Merging with Model Kinship. For instance, they could investigate the use of reinforcement learning to optimize the merging process, or explore iterative merging strategies that refine the merged model over multiple steps. It would also be beneficial to compare the performance of the proposed approach to other state-of-the-art merging techniques, such as those based on weight averaging or knowledge distillation. This would provide a more comprehensive evaluation of the proposed method and its potential advantages over existing approaches.

### Questions

1. How does the proposed model kinship metric handle models with different architectures or initializations?
2. Can the authors provide more details on the computational cost of calculating model kinship and performing the merging process?
3. Are there any specific scenarios or tasks where the proposed merging strategy might not be effective?

### Rating

6

### Confidence

3

**********
