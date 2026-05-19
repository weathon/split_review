### Summary

This paper introduces OptBatch, a data selection method that improves the instruction tuning of LLMs by considering the learnability of whole batch data instead of individual samples. The method comprises three parts: (1) An online loss-probability based stratified sampling algorithm that prioritizes batch selection methods with higher diversity. (2) Hessian gradient optimization that guides the data selection strategy for the next batch. (3) Evaluation on three diverse downstream datasets that demonstrate OptBatch's ability to maintain the same loss at a reduced computational cost.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. OptBatch introduces a unique approach to data selection by focusing on batch-level learnability rather than individual sample importance, which is rarely explored in previous methods.
2. The method integrates Hessian gradient optimization, inspired by the Adam optimization algorithm, to guide data selection, which is a novel application in the context of data curation.
3. The authors conduct extensive experiments on diverse datasets and tasks, including multi-turn dialogue, multilingual translation, and question-answering, which provide a comprehensive evaluation of the method's effectiveness.
4. The paper is well-organized and clearly written. The authors provide sufficient background information and motivation for their research. The figures and tables are clear and informative.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a clear and detailed explanation of how the Hessian gradient is calculated and used in the data selection process. The description of the Hessian gradient optimization is vague, and it is unclear how the second-moment cumulative gradient updates are integrated into the batch selection process. Specifically, the paper does not detail how the Hessian is approximated, whether it's a full Hessian, a diagonal approximation, or a block-diagonal approximation, and how this approximation impacts the computational efficiency and accuracy of the method. Furthermore, the connection between the Hessian information and the actual data selection criteria is not clearly established. For instance, it is not clear how the Hessian information is used to prioritize data samples within each stratum.
2. The paper does not provide a thorough analysis of the computational complexity of OptBatch compared to other data selection methods. While the authors claim a reduction in computational cost, there is no detailed breakdown of the time spent on different stages of the algorithm, such as the Hessian calculation, stratified sampling, and batch selection. A comparison of the computational cost of OptBatch with other data selection methods, including the time complexity of each step, is needed to fully assess the practical applicability of the method. The analysis should also consider the memory footprint of the method, especially when dealing with large language models.
3. The paper does not explore the sensitivity of OptBatch to different hyperparameters, such as the batch size, the number of strata, and the Hessian gradient optimization parameters. The choice of these hyperparameters can significantly affect the performance of the method, and a systematic analysis of their impact is needed to understand the robustness and generalizability of the method. For example, the paper does not discuss how the number of strata affects the diversity of the selected samples and the overall performance of the method. Similarly, the impact of different batch sizes on the stability of the Hessian approximation is not explored.
4. The paper does not provide a clear definition or explanation of the term "loss-based stratified sampling" in the main text. While the term may be used in other literature, it is important to provide a clear definition and explanation for the readers who are not familiar with this term. The paper should detail how the strata are formed based on the loss values, including the specific method used to determine the boundaries of each stratum. It is also unclear how the loss values are calculated (e.g., per-token loss, sequence loss) and how this affects the stratification process.

### Suggestions

To address the lack of clarity regarding the Hessian gradient calculation, the authors should provide a detailed explanation of the approximation method used, including the mathematical formulation and the computational steps involved. They should also clarify how the Hessian information is used to guide the data selection process within each stratum. For example, do they select samples with the largest Hessian eigenvalues, or is there another criterion? A concrete example illustrating how the Hessian information is used to select specific data samples would be beneficial. Furthermore, the authors should discuss the computational cost of the Hessian approximation and how it scales with the size of the model and the dataset. This discussion should include a comparison with other methods for Hessian approximation and their suitability for this specific application. The authors should also provide a sensitivity analysis of the Hessian approximation parameters, such as the learning rate and the number of samples used for the approximation, to demonstrate the robustness of the method.

To provide a more thorough analysis of the computational complexity, the authors should include a detailed breakdown of the time spent on each stage of the OptBatch algorithm, including the Hessian calculation, stratified sampling, and batch selection. This analysis should be compared with the computational cost of other data selection methods, including random selection and online hard example mining. The comparison should consider both the time complexity and the memory footprint of each method. The authors should also discuss the scalability of OptBatch to larger datasets and models, including the potential bottlenecks and limitations. A detailed analysis of the computational cost as a function of the batch size, the number of strata, and the size of the model would be valuable. The authors should also consider providing an empirical analysis of the computational cost on different hardware configurations to demonstrate the practical applicability of the method.

To address the sensitivity of OptBatch to different hyperparameters, the authors should conduct a systematic analysis of the impact of batch size, number of strata, and Hessian gradient optimization parameters on the performance of the method. This analysis should include a range of different values for each hyperparameter and a discussion of the trade-offs between performance and computational cost. For example, the authors should explore how the number of strata affects the diversity of the selected samples and the overall performance of the method. They should also investigate the impact of different batch sizes on the stability of the Hessian approximation and the convergence of the optimization process. The authors should also provide a discussion of how to choose the optimal hyperparameter values for different datasets and tasks. This discussion should include practical guidelines for users who want to apply OptBatch to their own problems.

### Questions

1. How does OptBatch handle the variability in data quality across different domains and tasks? Are there any domain-specific adaptations or considerations that need to be made when applying OptBatch to new datasets?
2. Can the authors provide more details on the implementation of the Hessian gradient optimization? How is the second-moment cumulative gradient update calculated and integrated into the batch selection process?
3. How does the performance of OptBatch scale with the size of the dataset and the model? Are there any limitations or bottlenecks that need to be addressed when applying OptBatch to larger datasets or more complex models?
4. What are the potential ethical implications of using OptBatch for data selection? Could the method inadvertently introduce biases or unfairness in the training data, and how can these issues be mitigated?

### Rating

3

### Confidence

4

**********
