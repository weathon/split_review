### Summary

This paper introduces Real3D, a Large Reconstruction Model (LRM) that can be trained using single-view real-world images. The authors propose a self-training framework that leverages both synthetic and real-world data. They introduce two unsupervised losses for pixel-level and semantic-level guidance, enabling the model to learn from single-view images without ground-truth 3D data. Additionally, they develop an automatic data curation method to collect high-quality examples from in-the-wild images. The experiments demonstrate that Real3D outperforms prior work in various evaluation settings, showcasing its effectiveness in leveraging real-world data for improved 3D reconstruction.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel self-training framework that enables the training of single-view large reconstruction models using real-world images, addressing a critical limitation in the field.
2. The proposed unsupervised losses for pixel-level and semantic-level guidance are innovative and effective in supervising the model without ground-truth 3D data.
3. The automatic data curation method for collecting high-quality examples from in-the-wild images is a valuable contribution, as it allows for scaling up the training data.
4. The experiments show that Real3D consistently outperforms prior work in diverse evaluation settings, demonstrating its effectiveness in leveraging real-world data for improved 3D reconstruction.

### Weaknesses

#### Some Related Works


#### comment

1. The paper mentions using a constant canonical pose for input views during self-training on real images. However, it does not provide a detailed explanation of how this canonical pose is defined or how it affects the model's performance. It is unclear how the model handles variations in object pose during training, and whether this canonical pose is learned or predefined. The lack of clarity on this aspect makes it difficult to assess the robustness of the method to different object orientations.
2. The paper states that the model is initialized on a synthetic dataset before being trained on real-world images. However, it does not provide sufficient details on the initialization process, such as the specific synthetic dataset used, the training procedure, and the impact of initialization on the final performance. The choice of the initial synthetic dataset and the training procedure could significantly impact the model's ability to generalize to real-world data. Without these details, it is hard to evaluate the effectiveness of the proposed approach.
3. The paper does not provide a detailed analysis of the computational cost and memory requirements of the proposed method. This information is crucial for understanding the practicality and scalability of the approach, especially when dealing with large-scale real-world datasets. The lack of information on training time, GPU usage, and memory footprint makes it difficult to assess the feasibility of the method for real-world applications.

### Suggestions

The paper should provide a more detailed explanation of how the constant canonical pose is defined and used during self-training. Specifically, it should clarify whether this pose is a fixed, predefined value or if it is learned during the initialization phase on the synthetic dataset. The authors should also discuss how the model handles variations in object pose during training, and whether any specific techniques are used to ensure robustness to different object orientations. For example, data augmentation techniques or pose normalization methods could be explored. A more thorough analysis of the impact of the canonical pose on the model's performance would be beneficial, including experiments with different canonical poses to demonstrate the sensitivity of the method to this parameter. This would provide a better understanding of the method's limitations and potential for improvement.

To address the lack of detail regarding the initialization process, the authors should include a comprehensive description of the synthetic dataset used for initialization, including its size, diversity, and the specific 3D representations used. The training procedure should be described in detail, including the optimization algorithm, learning rate schedule, and any regularization techniques employed. Furthermore, the authors should provide an analysis of the impact of the initialization on the final performance, including experiments with different initialization strategies. For example, they could compare the performance of the model when initialized with different synthetic datasets or with a random initialization. This would help to understand the importance of the initialization phase and its contribution to the overall performance of the model. It would also be beneficial to analyze the transferability of the learned representations from the synthetic domain to the real-world domain.

Finally, the paper should include a detailed analysis of the computational cost and memory requirements of the proposed method. This should include the training time, GPU usage, and memory footprint for different dataset sizes and model configurations. The authors should also discuss the scalability of the method, including any potential bottlenecks or limitations when dealing with large-scale real-world datasets. This analysis should be presented in a clear and concise manner, with specific numbers and comparisons to other state-of-the-art methods. This information is crucial for assessing the practicality of the method and its potential for real-world applications. The authors could also explore techniques to reduce the computational cost and memory requirements, such as model compression or distributed training.

### Questions

Please refer to the weaknesses.

### Rating

6

### Confidence

3

**********
