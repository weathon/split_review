### Summary

This paper introduces a novel task called Real-time Learning Pattern Adjustment (RLPA) to address the dynamic nature of learners' knowledge states in Knowledge Tracing (KT). The authors propose Cuff-KT, a method that uses a controller and a generator to adapt to distribution changes in learners' patterns without the need for fine-tuning. The paper demonstrates that Cuff-KT significantly improves the performance of existing KT models under both intra- and inter-learner shifts, with an average relative increase of 7% on AUC.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel task, RLPA, which addresses a critical gap in the field of KT by focusing on the dynamic nature of learners' knowledge states.
2. The proposed Cuff-KT method is innovative, using a controller and a generator to adapt to distribution changes in learners' patterns without the need for fine-tuning.
3. The paper provides a thorough experimental evaluation, demonstrating that Cuff-KT significantly improves the performance of existing KT models under both intra- and inter-learner shifts.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational complexity of Cuff-KT, which is important for practical applications.
2. The paper does not discuss the potential limitations of Cuff-KT, such as its sensitivity to hyperparameter settings or its performance on different types of datasets.
3. The paper does not provide a detailed analysis of the impact of different components of Cuff-KT on its overall performance.

### Suggestions

The paper should include a more thorough analysis of the computational complexity of Cuff-KT. While the authors mention that the method is tuning-free, a detailed breakdown of the time and space complexity, especially in relation to the size of the input data and the number of learners, is crucial for assessing its scalability and practical applicability. For instance, providing a Big O notation analysis for both training and inference time, along with empirical measurements on datasets of varying sizes, would be beneficial. This analysis should also consider the overhead introduced by the controller and generator components, and how they scale with the number of learners and interactions. Furthermore, it would be helpful to compare the computational cost of Cuff-KT with existing KT models, including fine-tuning approaches, to provide a clear understanding of its efficiency.

To address the limitations of Cuff-KT, the paper should include a more comprehensive discussion of its sensitivity to hyperparameter settings. While the authors claim the method is tuning-free, the performance of the controller and generator might still be influenced by the choice of parameters such as the rank in low-rank decomposition. A sensitivity analysis, showing how performance varies with different hyperparameter values, is necessary. Additionally, the paper should explore the performance of Cuff-KT on a wider range of datasets, including those with different characteristics, such as varying numbers of learners, questions, and interaction patterns. This would help to identify potential biases or limitations of the method. For example, it would be useful to see how Cuff-KT performs on datasets with sparse interaction data or those with a high degree of variability in learner performance. The paper should also discuss the potential impact of data quality on the performance of Cuff-KT, such as the presence of noisy or incorrect interactions.

Finally, the paper should provide a more detailed analysis of the impact of different components of Cuff-KT on its overall performance. While the authors mention the use of a controller and a generator, a more granular analysis of their individual contributions is needed. For example, an ablation study that systematically removes or modifies each component would help to understand their importance. This analysis should also consider the impact of different design choices within each component, such as the specific architecture of the controller and generator, and the choice of low-rank decomposition method. Furthermore, the paper should explore the interaction between the controller and generator, and how they work together to adapt to distribution changes in learners' patterns. This analysis should also include a discussion of the potential limitations of each component and how they might be improved in future work.

### Questions

1. How does the computational complexity of Cuff-KT compare to existing KT models?
2. What are the potential limitations of Cuff-KT, and how can they be addressed?
3. How do different components of Cuff-KT contribute to its overall performance?

### Rating

6

### Confidence

3

**********
