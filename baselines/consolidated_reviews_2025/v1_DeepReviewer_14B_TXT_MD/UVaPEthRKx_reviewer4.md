### Summary

The paper introduces Cuff-KT, a novel approach to enhance the adaptability of Knowledge Tracing (KT) models in Intelligent Tutoring Systems (ITS) by addressing the challenges of intra- and inter-learner shifts. These shifts refer to the dynamic changes in learners' knowledge states over time and the differences in learning patterns among various groups of learners, respectively. Cuff-KT employs a controller and a generator to adaptively update model parameters in real-time without the need for retraining, thereby improving the model's ability to generalize across different distributions. The proposed method demonstrates significant improvements in performance, with an average relative increase of 7% on AUC across multiple datasets.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a new task, Real-time Learning Pattern Adjustment (RLPA), which is a significant contribution to the field of personalized learning and Knowledge Tracing.
2. The proposed Cuff-KT method is innovative and addresses a critical gap in existing KT models by providing a tuning-free, fast, and flexible approach to adapt to distribution changes.
3. The paper provides a comprehensive experimental evaluation, demonstrating the effectiveness of Cuff-KT across multiple datasets and baseline models.
4. The authors have made their code and datasets publicly available, which enhances the reproducibility and transparency of their research.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational complexity of Cuff-KT compared to fine-tuning-based methods. While the authors mention that Cuff-KT is faster and more efficient, a quantitative comparison of the time and resource costs would strengthen this claim.
2. The paper does not explore the potential limitations of Cuff-KT in scenarios with highly dynamic or rapidly changing distributions. It would be beneficial to discuss how the method performs under such conditions and whether there are any trade-offs between adaptability and stability.
3. The paper could benefit from a more detailed discussion of the practical implications of Cuff-KT in real-world educational settings. For instance, how would the method handle the integration with existing ITS platforms, and what are the potential challenges in deploying it in a live environment?

### Suggestions

The paper would benefit from a more rigorous analysis of the computational overhead introduced by Cuff-KT. While the authors claim efficiency gains over fine-tuning, a detailed breakdown of the time complexity for both training and inference is needed. Specifically, the analysis should consider the number of parameters updated by Cuff-KT compared to full fine-tuning, and how this impacts the overall computational cost. Furthermore, a comparison of the memory footprint of Cuff-KT versus fine-tuning methods would be valuable, especially when dealing with large-scale datasets. This analysis should also include a discussion of the potential impact of the generator's complexity on the overall runtime, as this component is responsible for adapting the model parameters. A quantitative comparison, perhaps in the form of a table or graph, would provide a clearer picture of the practical advantages of Cuff-KT in terms of computational resources.

To further strengthen the paper, the authors should investigate the performance of Cuff-KT under more extreme distribution shifts. The current evaluation focuses on relatively stable shifts, but real-world educational data can exhibit rapid and unpredictable changes in learner behavior. It would be beneficial to test Cuff-KT on datasets with more abrupt changes in learner performance or knowledge states, such as those caused by external factors or sudden changes in curriculum. This could involve simulating scenarios where learners experience significant knowledge gains or losses over short periods, or where the distribution of learner abilities changes drastically. The analysis should also explore the trade-offs between adaptability and stability, as a highly adaptive model might overfit to recent data and lose its ability to generalize to future distributions. A discussion of how the controller and generator parameters affect this trade-off would be valuable.

Finally, the paper should provide a more detailed discussion of the practical challenges of deploying Cuff-KT in real-world educational settings. This should include a discussion of how the method would integrate with existing ITS platforms, and what modifications might be necessary. For example, how would the system handle the continuous stream of data from multiple learners, and how would it ensure that the model updates do not interfere with the normal operation of the ITS? The authors should also address the potential challenges of deploying Cuff-KT in a live environment, such as the need for real-time processing and the potential for unexpected errors. A discussion of the ethical considerations of using such a system, such as the potential for bias or unfairness, would also be valuable.

### Questions

1. How does the performance of Cuff-KT vary with different frequencies of parameter updates? Is there an optimal frequency for different types of learners or datasets?
2. Can the authors provide more insights into the choice of the rank in low-rank decomposition? How does the rank affect the performance and computational cost of Cuff-KT?
3. How does Cuff-KT handle the cold-start problem for new learners or questions? Are there any specific strategies or modifications to address this issue?

### Rating

6

### Confidence

3

**********
