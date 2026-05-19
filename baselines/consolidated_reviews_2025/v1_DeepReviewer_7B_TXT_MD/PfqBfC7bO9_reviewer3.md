### Summary

This paper proposes a new framework, CAUSE, which leverages the concept of causal inference to improve unsupervised semantic segmentation. The authors introduce a novel approach by bridging intervention-oriented approach (frontdoor adjustment) to define suitable two-step tasks for unsupervised prediction. The first step involves constructing a concept clusterbook as a mediator, which represents possible concept prototypes at different levels of granularity in a discretized form. The second step involves enhancing the likelihood of semantic groups using concept-wise self-supervised learning. The authors demonstrate the effectiveness of CAUSE through extensive experiments and analyses on various datasets, achieving state-of-the-art performance in unsupervised semantic segmentation.

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

The paper introduces a novel framework, CAUSE, for unsupervised semantic segmentation by leveraging causal inference. While the idea of using a concept clusterbook as a mediator is interesting, the paper needs to more clearly articulate the novelty of the approach compared to existing methods. Specifically, the combination of modularity maximization and contrastive learning, while potentially effective, needs a more detailed explanation of how it differs from existing combinations of these techniques in the context of unsupervised segmentation. The authors should provide a more in-depth analysis of the specific challenges in unsupervised semantic segmentation that their approach addresses, and how it overcomes the limitations of previous methods. For example, a discussion of how the frontdoor adjustment is specifically tailored to the unsupervised setting, and how this differs from existing causal inference methods, would be beneficial. Furthermore, a more detailed explanation of the concept clusterbook construction and its role in the overall framework is needed to fully understand the contribution of this component.

Regarding the computational cost, the paper should provide a more detailed analysis of the time and space complexity of the proposed method. The authors should break down the computational cost of each step in the algorithm, including the concept clusterbook construction, the modularity maximization, and the concept-wise self-supervised learning. This analysis should consider the impact of different parameters, such as the number of concepts and the size of the feature maps, on the computational cost. A comparison of the computational cost of the proposed method with that of other state-of-the-art methods would also be valuable. This comparison should not only focus on the overall runtime but also on the memory usage and energy consumption. The authors should also discuss potential strategies for reducing the computational cost of the proposed method, such as using more efficient algorithms or parallelizing the computations. This would make the method more practical for real-world applications.

Finally, the paper should include a more comprehensive experimental evaluation of the proposed method. While the paper presents results on several datasets, a comparison with other state-of-the-art methods on the PASCAL VOC dataset is essential. The authors should consider using a wider range of evaluation metrics, such as the mean intersection over union (mIoU) and the pixel accuracy (pAcc), to provide a more complete picture of the performance of the proposed method. The paper should also include an analysis of the sensitivity of the proposed method to different hyperparameters, such as the relaxation parameters for positive and negative concepts. This would help to understand the robustness of the proposed method and provide guidance for practitioners who want to use it. The authors should also discuss the limitations of the proposed method and potential directions for future research.

### Questions

Please refer to the weaknesses.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
