### Summary

This paper proposes a temperature scaling method for contrastive learning. The proposed method is motivated by the observation that the tolerance of hard negative samples is often overestimated in contrastive learning. The proposed method is evaluated on several datasets and shows performance improvements.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

- The proposed method is motivated by the observation that the tolerance of hard negative samples is often overestimated in contrastive learning. 
- The proposed method is evaluated on several datasets and shows performance improvements.

### Weaknesses

#### Some Related Works


#### comment

 - The proposed method is motivated by the observation that the tolerance of hard negative samples is often overestimated in contrastive learning. However, the proposed method does not seem to directly address this issue. The proposed method is motivated by the observation that the tolerance of hard negative samples is often overestimated in contrastive learning. However, the proposed method does not seem to directly address this issue. The proposed method is motivated by the observation that the tolerance of hard negative samples is often overestimated in contrastive learning. However, the proposed method does not seem to directly address this issue. The proposed method is motivated by the observation that the tolerance of hard negative samples is often overestimated in contrastive learning. However, the proposed method does not seem to directly address this issue.

### Suggestions

The paper's core idea of addressing the overestimation of tolerance for hard negative samples in contrastive learning is interesting, but the proposed method doesn't directly tackle this problem. The method focuses on dynamically adjusting the temperature based on cosine similarity, which indirectly influences the learning dynamics. However, the connection between this temperature adjustment and the mitigation of hard negative sample tolerance overestimation remains unclear. A more direct approach might involve explicitly modeling or penalizing the influence of hard negatives during training. For example, the loss function could be modified to incorporate a term that reduces the impact of samples with high cosine similarity but low similarity in the embedding space. This would more directly address the identified issue of overestimating hard negative tolerance.

Furthermore, the paper lacks a detailed analysis of how the proposed temperature scaling method affects the feature space. While the authors claim that the method leads to a more uniform distribution of samples, this claim needs to be supported by more rigorous analysis. Visualizations of the feature space, such as t-SNE plots, could provide insights into the distribution changes. Additionally, quantitative metrics, such as the average distance between samples, could be used to measure the uniformity of the distribution. The paper should also investigate the impact of the proposed method on the separability of different classes in the feature space. It is important to ensure that the method not only leads to a more uniform distribution but also maintains or improves the discriminative power of the learned representations. 

Finally, the paper should provide a more thorough comparison with existing methods for handling hard negative samples in contrastive learning. While the authors mention that their method is different from existing approaches, a more detailed comparison is needed to understand the advantages and disadvantages of the proposed method. This comparison should include both theoretical analysis and empirical evaluation. The paper should also discuss the limitations of the proposed method and identify potential areas for future research. For example, the method might not be effective in all scenarios, and it might be sensitive to the choice of hyperparameters. A more comprehensive discussion of these limitations would strengthen the paper.

### Questions

- What is the difference between the proposed method and the method proposed in [1]?
- What is the theoretical analysis of the proposed method? 
- How does the proposed method optimize the distribution of the samples in the feature space?
- How does the proposed method alleviate the alignment-failure dilemma?

### Rating

5

### Confidence

3

**********
