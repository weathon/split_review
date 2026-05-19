### Summary

This paper proposes a novel framework, CAUSE, which leverages the concept of causal inference to improve unsupervised semantic segmentation. Specifically, the authors bridge intervention-oriented approach (frontdoor adjustment) to define suitable two-step tasks for unsupervised prediction. The first step involves constructing a concept clusterbook as a mediator, which represents possible concept prototypes at different levels of granularity in a discretized form. Then, the mediator establishes an explicit link to the subsequent concept-wise self-supervised learning. Through extensive experiments and analyses on various datasets, CAUSE achieves state-of-the-art performance in unsupervised semantic segmentation.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The paper presents extensive experiments and analyses to demonstrate the effectiveness of the proposed method.
3. The proposed method achieves state-of-the-art results in unsupervised semantic segmentation.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method seems to be a combination of existing methods, such as modularity maximization and contrastive learning. The novelty of the proposed method is not clear.
2. The proposed method is complex and computationally expensive. The paper does not provide a detailed analysis of the computational cost of the proposed method.
3. The paper does not provide a comparison of the proposed method with other state-of-the-art methods on the PASCAL VOC dataset.

### Suggestions

The paper's core idea of using a concept clusterbook as a mediator for unsupervised semantic segmentation is interesting, but the novelty of the approach needs to be more clearly articulated. While the authors mention frontdoor adjustment, it's not immediately clear how this differs from existing methods that use similar concepts or techniques. A more detailed explanation of the specific challenges in unsupervised semantic segmentation that this approach addresses, and how it overcomes the limitations of previous methods, would be beneficial. For example, how does the proposed method handle the inherent ambiguity in unsupervised learning, where the ground truth is not available? A more in-depth discussion of the limitations of existing methods and how the proposed approach specifically addresses them would strengthen the paper's contribution.

Furthermore, the paper needs to provide a more thorough analysis of the computational cost of the proposed method. While the authors mention that the method is complex, they do not provide a detailed breakdown of the computational complexity of each step. This makes it difficult to assess the practical feasibility of the method. A comparison of the computational cost with other state-of-the-art methods is also needed. The authors should provide a detailed analysis of the time and memory requirements of the proposed method, including the cost of constructing the concept clusterbook, performing modularity maximization, and conducting concept-wise self-supervised learning. This analysis should also consider the impact of different parameters on the computational cost. Without this information, it is difficult to assess the practical applicability of the proposed method.

Finally, the paper should include a more comprehensive experimental evaluation of the proposed method. While the authors present results on several datasets, a comparison with other state-of-the-art methods on the PASCAL VOC dataset is essential. The authors should consider using a wider range of evaluation metrics, such as the mean intersection over union (mIoU) and the pixel accuracy (pAcc), to provide a more complete picture of the performance of the proposed method. The paper should also include an analysis of the sensitivity of the proposed method to different hyperparameters, such as the relaxation parameters for positive and negative concepts. This would help to understand the robustness of the proposed method and provide guidance for practitioners who want to use it. The authors should also discuss the limitations of the proposed method and potential directions for future research.

### Questions

Please refer to the weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
