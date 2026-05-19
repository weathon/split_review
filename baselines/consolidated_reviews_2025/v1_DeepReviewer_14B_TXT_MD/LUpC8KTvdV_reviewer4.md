### Summary

This paper proposes a masked image modelling (MIM) based self-supervised neural architecture search method specifically designed for vision transformers, termed as MaskTAS. MaskTAS employs a teacher-student architecture that enables efficient training of transformer supernets. The paper also designs a novel unsupervised evaluation metric for the evolutionary search algorithm, which rates candidate architectures based on their consistency with the teacher network. The experimental results demonstrate that the searched architectures achieve state-of-the-art accuracy on various datasets without using manual labels.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper introduces a novel self-supervised learning approach for transformer architecture search, which eliminates the need for expensive data labeling.
2. The proposed MaskTAS framework employs a teacher-student architecture that enables efficient training of transformer supernets.
3. The paper designs a novel unsupervised evaluation metric for the evolutionary search algorithm, which rates candidate architectures based on their consistency with the teacher network.
4. The experimental results demonstrate that the searched architectures achieve state-of-the-art accuracy on various datasets without using manual labels.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational cost of the proposed method compared to existing approaches.
2. The paper does not discuss the potential limitations of the proposed method, such as its sensitivity to hyperparameter settings or the choice of teacher network.

### Suggestions

The paper would benefit from a more thorough analysis of the computational overhead introduced by the MaskTAS framework. While the authors claim efficiency, a detailed breakdown of the FLOPs, memory usage, and training time for each stage (teacher pre-training, student training, and architecture search) is crucial for a fair comparison with existing NAS methods. Specifically, the paper should quantify the computational cost of the evolutionary search algorithm and the masked image modeling pre-training, and compare these costs to those of other self-supervised and supervised NAS techniques. This analysis should also consider the impact of different search space sizes and the number of candidate architectures evaluated. Furthermore, the authors should discuss the practical implications of these computational costs, such as the hardware requirements and the time needed to obtain optimal architectures.

To strengthen the paper, the authors should also investigate the sensitivity of the proposed method to various hyperparameters and design choices. The performance of self-supervised learning methods is often highly dependent on hyperparameters such as the masking ratio, the learning rate, and the batch size. The paper should include a sensitivity analysis that explores how these parameters affect the final performance of the searched architectures. Additionally, the choice of the teacher network is a critical factor in the proposed framework. The authors should discuss the impact of different teacher network architectures and pre-training strategies on the performance of the student network and the overall search process. It would be beneficial to explore the trade-offs between using a larger, more accurate teacher network and a smaller, more efficient one. This analysis should also consider the potential for catastrophic forgetting during the student training phase and how to mitigate it.

Finally, the paper should address the potential limitations of the proposed method in more detail. For example, the authors should discuss the applicability of MaskTAS to different types of datasets and tasks. While the paper demonstrates strong performance on image classification tasks, it is unclear how well the method would generalize to other domains, such as object detection or segmentation. The authors should also consider the potential for bias in the searched architectures and how to mitigate it. Furthermore, the paper should discuss the limitations of the proposed unsupervised evaluation metric and how it might affect the quality of the searched architectures. A more thorough discussion of these limitations would provide a more balanced and comprehensive view of the proposed method.

### Questions

Please refer to the weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
