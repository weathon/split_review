### Summary

This paper proposes a prompt-driven mixture of experts framework for universal anomaly detection in multi-modal, multi-organ medical images. The framework comprises vision and text encoders, a routing network, and a mixture of hallucination-minimized expert decoders. The authors curate a dataset of 12,153 images across 5 modalities and 4 organs and demonstrate state-of-the-art anomaly detection performance. The use of natural language prompts enhances model interpretability and user interaction. The code and data will be made publicly available.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The proposed prompt-driven mixture of experts framework is a novel approach to universal anomaly detection, effectively integrating multi-modal and multi-organ data within a single model.
2. The concept of hallucination-aware experts is innovative and addresses a significant challenge in anomaly detection, leading to improved accuracy and reduced false positives.
3. The comprehensive dataset of 12,153 images across 5 modalities and 4 organs is a valuable contribution to the field, facilitating further research and development.
4. The paper is well-structured and clearly written, with detailed explanations of the methodology, experiments, and results.
5. The experimental results demonstrate state-of-the-art performance, validating the effectiveness of the proposed framework.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational complexity and efficiency of the proposed framework, which is crucial for practical applications. Specifically, the analysis should include not just FLOPs and parameters, but also memory bandwidth requirements, latency, and energy consumption, especially when deployed on resource-constrained devices. Furthermore, the breakdown of computational costs should be provided for each component (encoders, routing network, and decoders) to identify potential bottlenecks.
2. The hallucination-aware experts are a key contribution, but the paper lacks a thorough discussion of their limitations and potential failure cases. For example, it is unclear how the model performs when presented with anomalies that exhibit characteristics significantly different from those seen during training, or how the model handles complex, multi-faceted anomalies that might span multiple organ systems or modalities. The paper should also explore the sensitivity of the hallucination scores to variations in image quality and noise levels.
3. The paper could benefit from a more in-depth discussion of the potential ethical implications of using such a framework in clinical settings, particularly regarding data privacy and security. This discussion should go beyond general statements and address specific concerns related to the handling of sensitive medical data, the potential for bias in the training data leading to disparities in performance across different patient populations, and the need for robust access control mechanisms to prevent unauthorized access to patient information.

### Suggestions

To address the lack of detailed computational analysis, the authors should provide a comprehensive breakdown of the computational costs associated with each component of their framework. This should include not only FLOPs and parameter counts but also memory bandwidth requirements, latency, and energy consumption. The analysis should consider different deployment scenarios, such as cloud-based and edge-based settings, and should identify potential bottlenecks in the pipeline. Furthermore, the authors should explore techniques for optimizing the computational efficiency of their model, such as model compression, quantization, and pruning, and provide experimental results demonstrating the impact of these techniques on both performance and computational cost. This would make the framework more practical for real-world applications, especially in resource-constrained environments.

To improve the discussion of the limitations of the hallucination-aware experts, the authors should conduct a more thorough analysis of their performance under various challenging conditions. This should include evaluating the model's robustness to anomalies that are significantly different from those seen during training, as well as its ability to handle complex, multi-faceted anomalies. The authors should also investigate the sensitivity of the hallucination scores to variations in image quality and noise levels. Furthermore, the paper should include a qualitative analysis of failure cases, providing visual examples of instances where the model incorrectly identifies normal regions as anomalous or fails to detect actual anomalies. This would provide a more complete understanding of the strengths and weaknesses of the proposed approach and guide future research directions.

Finally, the authors should provide a more detailed discussion of the ethical implications of their work, focusing on specific concerns related to data privacy, security, and potential biases. This should include a discussion of the measures taken to protect patient data, such as anonymization and encryption, and the potential for bias in the training data leading to disparities in performance across different patient populations. The authors should also address the need for robust access control mechanisms to prevent unauthorized access to patient information. Furthermore, the discussion should include the potential for misuse of the technology and the need for responsible development and deployment practices. This would demonstrate a commitment to ethical considerations and help ensure that the technology is used in a safe and beneficial manner.

### Questions

1. Can you provide more details on the computational complexity and efficiency of the proposed framework, including FLOPs, parameters, and memory requirements?
2. How do the hallucination-aware experts perform in cases where anomalies are not well-defined or are similar to normal variations?
3. What measures are taken to ensure data privacy and security when deploying this framework in clinical settings?
4. How does the model handle cases where the input image and prompt do not match the actual content (e.g., using a brain CT image with a lung-related prompt)?
5. Can the framework be extended to handle more organs and modalities, and what are the potential challenges in doing so?

### Rating

8

### Confidence

4

**********
