### Summary

The paper introduces a prompt-driven mixture of experts framework for universal anomaly detection in medical images, which detects anomalies across multiple organs and modalities using natural language prompts. The framework comprises encoders for vision and text, a routing network, and expert decoders that produce pixel-wise hallucination estimates. The authors benchmark their method against state-of-the-art universal and single-task anomaly detection models, demonstrating superior performance across multiple datasets.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The authors have conducted extensive experiments across multiple datasets and compared their method with a wide range of state-of-the-art anomaly detection models.
3. The proposed method achieves state-of-the-art performance in anomaly detection, outperforming existing approaches.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed discussion of the limitations of the proposed method and potential areas for improvement.
2. The authors could have provided a more in-depth analysis of the computational complexity and efficiency of the proposed method, especially when scaling to larger datasets or higher-resolution images.
3. The paper could benefit from a more thorough discussion of the interpretability of the results and how the method could be used to gain insights into the anomaly detection process.

### Suggestions

The paper would benefit from a more thorough discussion of the limitations of the proposed approach. Specifically, the authors should address the potential for the model to be fooled by subtle variations in normal images, a common issue in anomaly detection. It would be valuable to explore how the model performs under adversarial attacks, where an attacker might introduce small perturbations to normal images to cause misclassification as anomalies. Furthermore, the authors should discuss the sensitivity of the model to different types of prompts and how the choice of prompt might affect the results. A more detailed analysis of these limitations would provide a more balanced view of the method's capabilities and potential vulnerabilities. The authors should also consider the potential for the model to be biased towards certain types of anomalies or certain types of images, and how this bias could be mitigated.

To improve the analysis of computational complexity, the authors should provide a more detailed breakdown of the computational cost of each component of the model, including the encoders, routing network, and expert decoders. This analysis should consider both training and inference time, as well as memory usage. It would be beneficial to compare the computational cost of the proposed method with that of other state-of-the-art anomaly detection models, especially when scaling to larger datasets or higher-resolution images. The authors should also discuss the potential for optimizing the model for efficiency, such as through model pruning or quantization. A more thorough analysis of computational complexity would help readers understand the practical limitations of the method and how it might be deployed in real-world applications.

Finally, the paper should include a more in-depth discussion of the interpretability of the results. While the authors mention that the method produces pixel-wise anomaly maps, they should provide more details on how these maps can be used to gain insights into the anomaly detection process. For example, they could discuss how the pixel-wise anomaly maps can be used to identify specific regions of an image that are contributing to the anomaly score. The authors should also explore the potential for visualizing the expert decoders' outputs to understand which experts are most active for different types of anomalies. A more detailed analysis of the interpretability of the results would help readers understand the underlying mechanisms of the method and how it can be used to gain insights into the anomaly detection process.

### Questions

1. How does the proposed method handle cases where the input image contains multiple types of anomalies?
2. How does the method perform on datasets with more complex and diverse medical images?
3. How does the method handle cases where the input image is noisy or has artifacts?

### Rating

5

### Confidence

3

**********
