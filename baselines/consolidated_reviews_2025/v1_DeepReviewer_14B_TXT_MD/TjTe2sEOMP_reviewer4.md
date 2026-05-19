### Summary

This paper introduces a novel prompt-driven mixture of experts framework for universal anomaly detection in multi-modal, multi-organ medical images. The framework includes vision and text encoders, a routing network, and hallucination-aware expert decoders. The authors curate a dataset of 12,153 images across 5 modalities and 4 organs, demonstrating state-of-the-art anomaly detection performance. The use of natural language prompts enhances model interpretability and user interaction. The code and data will be made publicly available.

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

1. The paper does not provide a detailed analysis of the computational complexity and efficiency of the proposed framework, which is crucial for practical applications.
2. The hallucination-aware experts are a key contribution, but the paper lacks a thorough discussion of their limitations and potential failure cases.
3. The paper could benefit from a more in-depth discussion of the potential ethical implications of using such a framework in clinical settings, particularly regarding data privacy and security.

### Suggestions

To address the lack of computational analysis, the authors should include a detailed breakdown of the computational costs associated with each component of their framework, including the vision and text encoders, the routing network, and the expert decoders. This analysis should not only consider the number of parameters but also the FLOPs (floating-point operations per second) and memory bandwidth requirements during both training and inference. Furthermore, the authors should provide a comparison of their framework's computational efficiency with existing anomaly detection methods, particularly those that are also designed for multi-modal medical images. This would allow readers to better understand the trade-offs between performance and computational resources, which is crucial for practical deployment. The analysis should also consider the impact of batch size and input resolution on computational cost, providing a more comprehensive view of the framework's efficiency under different operating conditions.

Regarding the hallucination-aware experts, the authors should provide a more detailed analysis of their limitations and potential failure cases. This should include a discussion of scenarios where the hallucination scores might be unreliable, such as when the input image contains artifacts or noise that are not representative of true anatomical variations. The authors should also explore the sensitivity of the hallucination scores to different types of anomalies and provide examples of cases where the model might fail to accurately distinguish between true anomalies and normal variations. Furthermore, the authors should investigate the impact of the choice of hallucination score threshold on the overall performance of the framework, and provide guidance on how to select an appropriate threshold for different clinical applications. A more thorough analysis of the failure modes of the hallucination-aware experts would significantly enhance the robustness and reliability of the proposed framework.

Finally, the authors should expand their discussion of the ethical implications of their work, particularly regarding data privacy and security. This should include a detailed description of the measures taken to protect patient data during both training and inference, such as data anonymization and encryption. The authors should also address the potential for bias in the training data and how this might affect the performance of the framework across different patient populations. Furthermore, the authors should discuss the potential risks associated with the use of such a framework in clinical settings, such as the possibility of misdiagnosis or over-reliance on the model's output. A more comprehensive discussion of these ethical considerations would demonstrate a commitment to responsible research practices and help ensure the safe and ethical deployment of the proposed framework.

### Questions

1. Can you provide more details on the computational complexity and efficiency of the proposed framework, including FLOPs, parameters, and memory requirements?
2. How do the hallucination-aware experts perform in cases where anomalies are not well-defined or are similar to normal variations?
3. What measures are taken to ensure data privacy and security when deploying this framework in clinical settings?

### Rating

8

### Confidence

4

**********
