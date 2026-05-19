### Summary

This paper studies the temperature scaling in contrastive learning. The authors propose a cosine-based temperature scaling method and conduct experiments to show the effectiveness of the method.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The proposed method is simple and easy to implement.
2. The experiments are conducted on multiple datasets.

### Weaknesses

#### Some Related Works

[1] Understanding temperature scaling in contrastive learning

#### comment

1. The novelty of the proposed method is limited. The authors simply replace the constant temperature in SimCLR with a cosine-based temperature function. The justification for using a cosine-based function, while intuitive, lacks a strong theoretical basis. The paper does not explore alternative temperature scaling functions or provide a comparative analysis to demonstrate the superiority of the chosen cosine-based approach. Furthermore, the paper does not adequately address the potential limitations of the cosine function, such as its behavior at extreme cosine values and its impact on the loss landscape.
2. The authors claim that the proposed method can be used to optimize the distribution of the samples in the feature space. However, the authors do not provide any theoretical analysis or empirical evidence to support this claim. The paper lacks a rigorous analysis of how the proposed temperature scaling affects the feature space distribution, such as changes in cluster density, separation, or dimensionality. Without such analysis, the claim remains unsubstantiated.
3. The authors claim that the proposed method can alleviate the alignment-failure dilemma. However, the authors do not provide any theoretical analysis or empirical evidence to support this claim. The paper does not clearly define what constitutes alignment-failure or how the proposed method specifically addresses this issue. The experiments do not isolate the effect of the proposed method from other factors that might contribute to alignment.

### Suggestions

The paper would benefit significantly from a more thorough investigation into the theoretical underpinnings of the proposed cosine-based temperature scaling. The authors should explore the mathematical properties of the cosine function in the context of contrastive learning and analyze how it interacts with the InfoNCE loss. This could involve examining the gradient behavior of the loss function under different temperature scaling regimes, as well as analyzing the impact of the cosine function on the feature space distribution. A more rigorous analysis of the function's behavior at extreme cosine values and its effect on the loss landscape is needed to justify the choice of the cosine function. Furthermore, the authors should consider comparing their approach with other potential temperature scaling functions, such as linear or exponential functions, and provide a comparative analysis to demonstrate the advantages of the cosine-based approach.

To support the claim that the proposed method optimizes the distribution of samples in the feature space, the authors should provide a more detailed analysis of how the temperature scaling affects the feature space. This could include visualizations of the feature space before and after applying the proposed method, as well as quantitative measures of cluster density, separation, and dimensionality. The authors should also investigate the impact of the proposed method on the alignment of positive and negative samples in the feature space. This analysis should be supported by both theoretical arguments and empirical evidence. The paper should also clarify what is meant by 'alignment' in the context of contrastive learning and how the proposed method specifically addresses this issue.

Finally, the authors need to provide a more rigorous definition of the 'alignment-failure dilemma' and explain how the proposed method alleviates it. This should be supported by both theoretical arguments and empirical evidence. The experiments should be designed to isolate the effect of the proposed method from other factors that might contribute to alignment. For example, the authors could compare the performance of the proposed method with other contrastive learning methods under different conditions, such as varying batch sizes or learning rates. The paper should also provide a clear explanation of how the proposed method affects the tolerance of hard negative samples and how this leads to improved performance.

### Questions

1. What is the difference between the proposed method and the method proposed in [1]?
2. What is the theoretical analysis of the proposed method? 
3. How does the proposed method optimize the distribution of the samples in the feature space?
4. How does the proposed method alleviate the alignment-failure dilemma?

### Rating

3

### Confidence

4

**********
