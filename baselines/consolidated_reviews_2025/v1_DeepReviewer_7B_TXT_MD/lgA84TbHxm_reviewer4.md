### Summary

This paper proposes a temperature scaling function for contrastive learning. The proposed method is based on the observation that the tolerance of hard negative samples is often overestimated in contrastive learning. The proposed method is evaluated on several datasets and shows performance improvements.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and easy to implement.
3. The experiments are conducted on multiple datasets.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is motivated by the observation that the tolerance of hard negative samples is often overestimated in contrastive learning. However, the proposed method does not seem to directly address this issue. The proposed method is motivated by the observation that the tolerance of hard negative samples is often overestimated in contrastive learning. However, the proposed method does not seem to directly address this issue. The proposed method is motivated by the observation that the tolerance of hard negative samples is often overestimated in contrastive learning. However, the proposed method does not seem to directly address this issue. The proposed method is motivated by the observation that the tolerance of hard negative samples is often overestimated in contrastive learning. However, the proposed method does not seem to directly address this issue.

2. The paper lacks a detailed analysis of how the proposed temperature scaling method affects the feature space. While the authors claim that the method leads to a more uniform distribution of samples, this claim needs to be supported by more rigorous analysis. Visualizations of the feature space, such as t-SNE plots, could provide insights into the distribution changes. Additionally, quantitative metrics, such as the average distance between samples, could be used to measure the uniformity of the distribution. The paper should also investigate the impact of the proposed method on the separability of different classes in the feature space. It is important to ensure that the method not only leads to a more uniform distribution but also maintains or improves the discriminative power of the learned representations.

3. The paper should provide a more thorough comparison with existing methods for handling hard negative samples in contrastive learning. While the authors mention that their method is different from existing approaches, a more detailed comparison is needed to understand the advantages and disadvantages of the proposed method. This comparison should include both theoretical analysis and empirical evaluation. The paper should also discuss the limitations of the proposed method and identify potential areas for future research. For example, the method might not be effective in all scenarios, and it might be sensitive to the choice of hyperparameters. A more comprehensive discussion of these limitations would strengthen the paper.

### Suggestions

The core issue with the proposed method lies in the lack of a clear, direct link between the temperature scaling and the mitigation of overestimated hard negative sample tolerance. While the authors propose a method based on the observation that hard negatives are treated as positives, the actual mechanism by which the proposed temperature scaling achieves this is not well-defined. The paper needs to provide a more detailed explanation of how the proposed temperature scaling function alters the loss landscape and specifically affects the learning dynamics of hard negatives. For example, the authors could analyze the gradient of the loss function with respect to the embeddings of hard negative samples under different temperature settings. This would provide a more concrete understanding of how the proposed method reduces the influence of hard negatives. Furthermore, visualizing the feature space before and after applying the proposed method could offer valuable insights into the method's impact on the distribution of samples and the separation of different classes. This would help to validate the claim that the method leads to a more uniform distribution of samples and improve the discriminative power of the learned representations.

To strengthen the paper, the authors should provide a more rigorous theoretical justification for their method. This could involve deriving the proposed temperature scaling function from first principles or demonstrating its equivalence to a known optimization technique. The current explanation relies heavily on empirical observations, which is not sufficient to establish the method's theoretical soundness. Additionally, the authors should explore the sensitivity of their method to different choices of the temperature scaling function. It is possible that other temperature scaling functions could achieve similar or even better performance. A comparative analysis of different scaling functions would provide a more comprehensive understanding of the proposed method's strengths and limitations. The authors should also consider the computational overhead of their method, especially when dealing with large datasets. If the method introduces significant computational costs, it may not be practical for real-world applications. A detailed analysis of the computational complexity of the proposed method is needed to assess its practicality.

Finally, the experimental evaluation should be expanded to include a wider range of datasets and model architectures. The current experiments are limited to a few specific datasets and a single model architecture. This makes it difficult to assess the generalizability of the proposed method. The authors should also consider comparing their method to other state-of-the-art contrastive learning techniques. This would provide a more comprehensive evaluation of the method's performance and its advantages over existing approaches. Furthermore, the authors should provide a more detailed analysis of the experimental results, including statistical significance tests and error bars. This would help to ensure the robustness and reliability of the reported performance improvements. The paper should also discuss the limitations of the proposed method and identify potential areas for future research. For example, the method might not be effective in all scenarios, and it might be sensitive to the choice of hyperparameters. A more comprehensive discussion of these limitations would strengthen the paper.

### Questions

Please see the weaknesses.

### Rating

5

### Confidence

3

**********
