### Summary

This paper addresses the challenge of learning from long-tailed and noisily labeled data, which often occur in real-world applications. The authors observed that existing solutions fail to consistently improve learning when the dataset exhibits both of these issues. They introduce a novel approach called the Fairness Regularizer (FR), which aims to reduce the performance gap between different sub-populations. The FR improves the performance of sub-populations on the tail end and enhances overall learning performance. The paper provides extensive experiments to demonstrate the effectiveness of the proposed solution when combined with existing popular robust or class-balanced methods.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

1. This paper addresses the problem of learning with long-tailed and noisily labeled data, which is a common challenge in real-world applications. The authors provide an empirical analysis of the disparate impacts of sub-populations and propose a novel approach called the Fairness Regularizer (FR). The FR aims to reduce the performance gap between head and tail sub-populations and improve overall learning performance.

2. The authors conduct extensive experiments on various datasets, including CIFAR-10, CIFAR-100, and Clothing1M, to demonstrate the effectiveness of the FR. The results show that the FR improves the performance of sub-populations on the tail end and enhances overall learning performance when combined with existing popular robust or class-balanced methods.

3. The paper provides a comprehensive analysis of the proposed approach, including theoretical justifications and empirical evaluations. The authors also discuss the limitations of their approach and suggest directions for future research.

4. The problem of learning with long-tailed and noisily labeled data is an important challenge in machine learning, and the proposed approach has the potential to improve the performance of various applications, including image classification, natural language processing, and recommender systems.

### Weaknesses

#### Some Related Works


#### comment

1. The paper introduces the Fairness Regularizer (FR) as a solution to the problem of learning from noisily labeled long-tailed data. However, the motivation behind this approach is not entirely clear. The authors argue that existing methods fail to consistently improve learning when the dataset is long-tailed with label noise, and that these methods do not observe universal improvements across different sub-populations. While this observation is valid, it is not immediately obvious why fairness regularization is the appropriate solution to address this issue. The connection between reducing performance disparities and mitigating the effects of label noise in long-tailed distributions needs further clarification. Specifically, it's unclear how minimizing the performance gap between head and tail classes directly addresses the problem of noisy labels, which could be randomly distributed or disproportionately affect certain classes.

2. The proposed FR approach relies on the availability of sub-population information during training. However, in many real-world scenarios, this information may not be readily available or easy to obtain. The authors do not discuss the challenges of identifying sub-populations in practice and how this might impact the applicability of their approach. The method's reliance on pre-defined sub-populations, without addressing the practical difficulties of obtaining these groupings, limits its real-world applicability. The paper should discuss the sensitivity of the method to different sub-population definitions and the potential for performance degradation if the sub-populations are not well-defined or accurately identified.

3. The experimental evaluation of the FR approach is limited to a few datasets, including CIFAR-10, CIFAR-100, and Clothing1M. While these datasets are commonly used in the literature, they may not be representative of all real-world scenarios. The authors should consider evaluating their approach on a wider range of datasets with varying characteristics, such as different levels of noise, imbalance, and data complexity. The current evaluation lacks a thorough analysis of the method's robustness to different types of noise and imbalance, and it is unclear how the method would perform on more complex datasets with higher dimensionality or more intricate class structures.

### Suggestions

The paper would benefit from a more detailed explanation of the theoretical underpinnings of the Fairness Regularizer (FR) in the context of noisy, long-tailed data. While the empirical results demonstrate the effectiveness of the approach, a deeper theoretical analysis is needed to clarify why minimizing performance disparities between sub-populations helps to mitigate the effects of label noise. Specifically, the authors should provide a more rigorous justification for how the FR term interacts with the loss function to improve the model's robustness to noisy labels. This could involve analyzing the gradient behavior of the FR term and its impact on the model's learning dynamics. Furthermore, the authors should explore the relationship between the FR and existing methods for handling noisy labels and long-tailed data, providing a more comprehensive understanding of how the proposed approach complements or differs from these methods. A more detailed theoretical analysis would strengthen the paper's contribution and provide a more solid foundation for future research.

To address the practical limitations of relying on pre-defined sub-populations, the authors should investigate methods for automatically identifying or learning sub-populations from the data. This could involve exploring clustering techniques or other unsupervised learning methods to group similar instances into sub-populations. The paper should also discuss the sensitivity of the FR approach to different sub-population definitions and provide guidelines for selecting appropriate sub-population groupings. Furthermore, the authors should consider the computational cost of identifying sub-populations and how this might impact the scalability of the approach. A more thorough discussion of these practical considerations would enhance the paper's relevance and applicability to real-world scenarios. The authors could also explore the use of adaptive sub-population strategies, where the sub-populations are dynamically adjusted during training based on the model's performance.

The experimental evaluation should be expanded to include a wider range of datasets with varying characteristics, such as different levels of noise, imbalance, and data complexity. This would provide a more comprehensive assessment of the FR approach's robustness and generalizability. The authors should also conduct a more detailed analysis of the method's performance under different noise conditions, including varying noise rates and noise distributions. Furthermore, the paper should include a comparison with more recent state-of-the-art methods for handling noisy, long-tailed data, providing a more thorough evaluation of the proposed approach's effectiveness. The authors should also consider including ablation studies to analyze the impact of different components of the FR approach and to identify the key factors contributing to its performance.

### Questions

1. Can you provide more insights into the motivation behind using fairness regularization to address the problem of learning from noisily labeled long-tailed data? How does reducing the performance gap between head and tail sub-populations help to mitigate the effects of label noise?

2. How do you obtain sub-population information during training in real-world scenarios where this information may not be readily available? What are the challenges of identifying sub-populations, and how do you address them?

3. Can you evaluate the FR approach on a wider range of datasets with varying characteristics, such as different levels of noise, imbalance, and data complexity? This would help to demonstrate the robustness and generalizability of the proposed approach.

4. How does the FR approach compare to more recent state-of-the-art methods for handling noisy, long-tailed data? A comparison with these methods would provide a more comprehensive evaluation of the proposed approach's effectiveness.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
