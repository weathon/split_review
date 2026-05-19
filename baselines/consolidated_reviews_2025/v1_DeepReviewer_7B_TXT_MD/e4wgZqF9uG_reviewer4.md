### Summary

This paper explores the potential of monocular depth pre-training for semantic segmentation. The authors investigate whether pre-training on geometric tasks, specifically monocular depth estimation, can improve downstream semantic segmentation performance. They compare monocular depth pre-training with other pre-training methods, such as ImageNet pre-training, and find that depth pre-training often leads to better results. The paper also explores the impact of various factors, such as the size of the training dataset and the choice of network components, on the effectiveness of the proposed approach. The authors find that depth pre-training can be a viable alternative to human annotators for learning semantic concepts, potentially reducing the reliance on human-labeled data.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow. The authors clearly articulate the motivation, methodology, and findings of their research.
2. The paper provides a comprehensive set of experiments to validate the effectiveness of monocular depth pre-training for semantic segmentation. The authors explore various factors, such as the size of the training dataset and the choice of network components, and provide detailed analysis of the results.
3. The paper's findings suggest that monocular depth pre-training can be a viable alternative to human annotators for learning semantic concepts, potentially reducing the reliance on human-labeled data. This could have significant implications for the field of computer vision, particularly in scenarios where human annotation is expensive or time-consuming.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational cost associated with monocular depth pre-training. While the authors mention that depth pre-training can be computationally expensive, they do not provide specific details on the training time, memory requirements, or hardware used. This information is crucial for researchers who want to replicate the experiments or apply the proposed approach in real-world scenarios.
2. The paper does not explore the potential limitations of monocular depth pre-training. For example, the authors do not discuss the impact of occlusions, lighting variations, or viewpoint changes on the performance of the proposed approach. It is important to understand the limitations of the proposed approach and identify scenarios where it may not be effective.
3. The paper does not provide a comparison with other state-of-the-art methods for semantic segmentation. While the authors compare monocular depth pre-training with ImageNet pre-training, they do not compare it with other methods that have been shown to be effective for semantic segmentation. This makes it difficult to assess the relative performance of the proposed approach and identify areas for improvement.

### Suggestions

The authors should provide a more detailed analysis of the computational cost associated with monocular depth pre-training. This should include a breakdown of the training time, memory requirements, and the specific hardware used for the experiments. For example, they could report the training time in hours, the memory usage in gigabytes, and the type of GPU used (e.g., NVIDIA Tesla V100, RTX 3090). This information is crucial for researchers who want to replicate the experiments or apply the proposed approach in real-world scenarios. Furthermore, it would be beneficial to explore techniques to reduce the computational cost of monocular depth pre-training, such as using smaller models or more efficient training algorithms. This would make the proposed approach more accessible to a wider range of researchers and practitioners.

It is also important to explore the potential limitations of monocular depth pre-training. The authors should discuss the impact of occlusions, lighting variations, and viewpoint changes on the performance of the proposed approach. For example, they could conduct experiments on datasets that contain a variety of occlusions or lighting conditions and analyze how these factors affect the performance of the model. They should also discuss the potential for viewpoint changes to affect the performance of the model, and explore techniques to make the model more robust to viewpoint variations. This would provide a more comprehensive understanding of the strengths and weaknesses of the proposed approach and identify areas for future research. Additionally, the authors should consider the impact of different types of depth sensors on the performance of the proposed approach. For example, they could compare the performance of the model when trained with data from stereo cameras versus LiDAR sensors.

Finally, the authors should provide a more comprehensive comparison with other state-of-the-art methods for semantic segmentation. This should include a comparison with methods that have been shown to be effective for semantic segmentation, such as fully convolutional networks (FCNs) and other pre-training techniques. The authors should also compare their approach with other methods that use geometric information for semantic segmentation. This would provide a more comprehensive understanding of the relative performance of the proposed approach and identify areas for improvement. It would also be beneficial to include a discussion of the advantages and disadvantages of monocular depth pre-training compared to other methods. This would help researchers to make informed decisions about which approach is most suitable for their specific application.

### Questions

1. How does the choice of depth estimation algorithm affect the performance of the proposed approach? The authors mention that different depth estimation algorithms can lead to different results. It would be helpful to understand the impact of this choice on the final performance of the model.
2. How does the size of the training dataset affect the performance of the proposed approach? The authors mention that the size of the training dataset can affect the effectiveness of the proposed approach. It would be helpful to understand the relationship between the size of the training dataset and the performance of the model.
3. How does the choice of network architecture affect the performance of the proposed approach? The authors mention that the choice of network architecture can affect the performance of the proposed approach. It would be helpful to understand the impact of this choice on the final performance of the model.

### Rating

6

### Confidence

4

**********
