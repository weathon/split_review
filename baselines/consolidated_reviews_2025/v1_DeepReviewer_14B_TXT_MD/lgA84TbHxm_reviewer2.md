### Summary

This paper proposes a temperature scaling function for the InfoNCE loss in self-supervised contrastive learning. The motivation is to dynamically adjust the temperature based on cosine similarity to better handle hard negative samples. The authors provide theoretical analysis and experimental results demonstrating the effectiveness of their approach. The proposed method outperforms several state-of-the-art SSL algorithms on various benchmark datasets.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper introduces a novel approach to dynamically scale the temperature hyper-parameter in the InfoNCE loss function based on cosine similarity. This is a significant contribution to the field of self-supervised contrastive learning.
2. The authors provide a thorough theoretical analysis of the proposed temperature scaling function, including its derivation and properties. This adds rigor to the paper and helps in understanding the underlying mechanisms.
3. The experimental results are comprehensive and demonstrate the effectiveness of the proposed method on various benchmark datasets. The paper shows improvements over state-of-the-art SSL algorithms, which is a strong indicator of the method's potential.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed discussion on the computational overhead introduced by the proposed temperature scaling function. While the authors mention that the method is computationally efficient, a quantitative analysis of the additional computational cost would be valuable. Specifically, the paper lacks a detailed breakdown of the FLOPs or time complexity associated with calculating the dynamic temperature, making it difficult to assess the practical overhead compared to a fixed temperature approach. It would be beneficial to see a comparison of the computational cost of the proposed method against the baseline InfoNCE loss with a fixed temperature, especially when scaling to larger batch sizes and embedding dimensions.
2. The paper primarily focuses on the InfoNCE loss. It would be interesting to see how the proposed temperature scaling function can be applied to other contrastive loss functions and whether it can provide similar improvements. The paper does not explore the potential limitations or adaptations required when applying the proposed scaling function to other contrastive losses, such as those based on different similarity metrics or those that incorporate additional regularization terms. A discussion on the generalizability of the approach would strengthen the paper.
3. While the paper demonstrates improvements on benchmark datasets, it would be beneficial to see how the proposed method performs on more complex and real-world datasets. The current evaluation is limited to standard image classification datasets. It is unclear how the method would perform on datasets with more complex data distributions, such as those found in medical imaging or remote sensing, or on tasks beyond image classification, such as object detection or segmentation. The paper should also consider the impact of different data augmentations on the performance of the proposed method.

### Suggestions

The paper introduces a novel temperature scaling function for the InfoNCE loss, which is a valuable contribution. However, to further strengthen the paper, it would be beneficial to include a more detailed analysis of the computational overhead. Specifically, the authors should provide a quantitative comparison of the computational cost of their proposed method against the baseline InfoNCE loss with a fixed temperature. This could include a breakdown of the FLOPs or time complexity associated with calculating the dynamic temperature, as well as an analysis of how this cost scales with batch size and embedding dimension. Furthermore, it would be helpful to see a comparison of the training time for the proposed method versus the baseline, especially when using large batch sizes. This would provide a more concrete understanding of the practical implications of using the proposed temperature scaling function.

To enhance the generalizability of the proposed method, the authors should explore its applicability to other contrastive loss functions. This could involve experimenting with different similarity metrics, such as those based on Euclidean distance or learned metrics, and investigating how the proposed scaling function can be adapted to these different metrics. Additionally, the authors should consider the impact of different regularization terms on the performance of the proposed method. For example, it would be interesting to see how the proposed scaling function interacts with regularization techniques such as weight decay or dropout. A discussion on the limitations and potential adaptations required when applying the proposed scaling function to other contrastive losses would also be valuable. This would provide a more comprehensive understanding of the method's applicability and limitations.

Finally, to demonstrate the robustness of the proposed method, it is crucial to evaluate its performance on more complex and real-world datasets. This could include datasets with more complex data distributions, such as those found in medical imaging or remote sensing, or on tasks beyond image classification, such as object detection or segmentation. The authors should also consider the impact of different data augmentations on the performance of the proposed method. For example, it would be interesting to see how the method performs with different types of augmentations, such as those that introduce more significant changes to the input data. A more comprehensive evaluation on diverse datasets and tasks would provide a stronger validation of the proposed method's effectiveness and generalizability.

### Questions

1. Can you provide more details on the computational overhead introduced by the proposed temperature scaling function? How does it compare to the baseline methods in terms of computational cost?
2. Have you considered applying the proposed temperature scaling function to other contrastive loss functions? If so, what are the challenges and potential benefits?
3. How does the proposed method perform on more complex and real-world datasets? Are there any specific scenarios where the method might not be as effective?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
