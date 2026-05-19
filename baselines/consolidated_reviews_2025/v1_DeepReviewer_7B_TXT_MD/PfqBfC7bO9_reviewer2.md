### Summary

This paper proposes a novel framework called CAUSE, which leverages the concept of causal inference to improve unsupervised semantic segmentation. The paper presents extensive experiments and analyses to demonstrate the effectiveness of the proposed method.

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

The paper should more clearly articulate the novelty of the proposed approach by contrasting it with existing methods. While the individual components, such as modularity maximization and contrastive learning, are known, the specific way they are combined and applied within the context of unsupervised semantic segmentation needs to be more thoroughly justified. The authors should provide a detailed explanation of how the concept clusterbook acts as a mediator and how this differs from existing approaches that directly use pre-trained features for segmentation. A more in-depth discussion of the limitations of existing methods and how the proposed approach overcomes these limitations would also strengthen the paper's contribution. For example, the paper could discuss how the proposed method addresses the issue of indeterminate clustering targets in unsupervised semantic segmentation, and how this is different from the challenges faced by methods that rely on pseudo-labeling or other forms of iterative refinement.

Furthermore, the paper needs to provide a more detailed analysis of the computational cost of the proposed method. The authors should include a breakdown of the time complexity of each step in the algorithm, including the modularity maximization, concept-wise self-supervised learning, and the overall inference process. This analysis should also consider the impact of different parameters, such as the number of concepts and the size of the feature maps, on the computational cost. It would be beneficial to compare the computational cost of the proposed method with that of other state-of-the-art methods, not just in terms of overall runtime, but also in terms of memory usage and energy consumption. This would provide a more comprehensive understanding of the practical feasibility of the proposed method. The authors should also discuss potential strategies for reducing the computational cost, such as using more efficient algorithms or parallelizing the computations.

Finally, the paper should include a more comprehensive experimental evaluation of the proposed method. While the paper presents results on several datasets, a more detailed comparison with other state-of-the-art methods on the PASCAL VOC dataset is needed. The authors should consider using a wider range of evaluation metrics, such as the mean intersection over union (mIoU) and the pixel accuracy (pAcc), to provide a more complete picture of the performance of the proposed method. The paper should also include an analysis of the sensitivity of the proposed method to different hyperparameters, such as the relaxation parameters for positive and negative concepts. This would help to understand the robustness of the proposed method and provide guidance for practitioners who want to use it.

### Questions

Please see the Weaknesses.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
