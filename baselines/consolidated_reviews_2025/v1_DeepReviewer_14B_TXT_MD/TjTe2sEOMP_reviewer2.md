### Summary

This paper proposes a prompt-driven mixture of experts framework for universal anomaly detection in multi-modal, multi-organ medical images. The model uses vision and text encoders, a routing network, and hallucination-aware expert decoders to improve anomaly detection accuracy and reduce false positives. The authors create a dataset of over 12,000 images across five modalities and four organs, showing that their approach outperforms existing methods. The framework also allows for interpretability and user interaction through natural language prompts.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The proposed hallucination-aware expert decoder is a novel component that addresses a key issue in anomaly detection models, where normal regions are often misidentified as anomalous. This innovation improves the accuracy of anomaly detection.
2. The paper introduces a large-scale dataset spanning 12,153 images across 5 imaging modalities (X-ray, MRI, OCT, ultrasound, and CT) and 4 anatomical structures (lung, brain/head, retina, and breast). This dataset provides a comprehensive resource for evaluating and advancing universal anomaly detection models.
3. The proposed method outperforms both single-task and universal anomaly detection models across multiple datasets, achieving higher AUC, F1 score, and accuracy. This demonstrates the effectiveness of the prompt-driven mixture of experts framework.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is only evaluated on a single dataset, which may not fully represent the diversity of medical images. The generalizability of the model to other datasets or clinical settings is not extensively discussed. Specifically, the dataset, while large, is limited to four anatomical structures and five imaging modalities. The performance of the model on datasets with different pathologies, image acquisition parameters, or patient populations is unknown. This raises concerns about the robustness of the model in real-world clinical scenarios.
2. The mixture of experts framework, while effective, may add complexity to the model, potentially making it more challenging to implement or deploy in practical settings. The routing network and multiple expert decoders increase the number of parameters and computational cost, which could be a barrier to adoption in resource-constrained environments. Furthermore, the training process for such a complex model may be more difficult to stabilize and optimize compared to simpler architectures.
3. The hallucination-aware expert decoder is designed to minimize false positives in anomaly detection. However, in medical images, some anomalous regions may be subtle and closely resemble normal regions, potentially leading to false negatives. The model's ability to distinguish between truly anomalous subtle findings and normal variations needs further investigation, especially given the high stakes of medical diagnosis.

### Suggestions

To address the limitations in dataset diversity, the authors should evaluate their model on additional, publicly available medical imaging datasets that cover a broader range of anatomical regions, imaging modalities, and pathologies. This would provide a more comprehensive assessment of the model's generalizability and robustness. For example, datasets focusing on different organs, such as the heart or kidneys, or those using different imaging techniques like PET or SPECT, could be included. Furthermore, the authors should analyze the performance of the model on datasets with varying image quality and noise levels to understand its sensitivity to these factors. A detailed analysis of the model's performance across different patient demographics would also be beneficial to ensure its applicability across diverse populations. This would provide a more thorough understanding of the model's strengths and weaknesses and its potential for real-world clinical application.

To mitigate the complexity of the mixture of experts framework, the authors should explore methods to reduce the computational overhead and simplify the model architecture without sacrificing performance. This could involve techniques such as pruning less important experts, using more efficient routing mechanisms, or employing knowledge distillation to transfer the knowledge of the complex model to a simpler one. The authors should also provide a detailed analysis of the computational cost of their model, including the number of parameters, training time, and inference time, and compare it to other state-of-the-art methods. This would help to assess the practical feasibility of deploying the model in resource-constrained environments. Additionally, the authors should investigate the sensitivity of the model to hyperparameter settings and provide guidelines for selecting optimal values for different datasets and applications.

To improve the model's ability to detect subtle anomalies, the authors should explore techniques to enhance the sensitivity of the hallucination-aware expert decoder. This could involve incorporating attention mechanisms to focus on regions of interest, using more sophisticated loss functions that penalize false negatives more heavily, or employing data augmentation techniques to increase the representation of subtle anomalies in the training data. The authors should also conduct a detailed analysis of the model's performance on different types of anomalies, including subtle and obvious ones, and provide metrics such as precision, recall, and F1-score for each category. This would provide a more nuanced understanding of the model's strengths and weaknesses and guide future research directions.

### Questions

1. How does the model perform on datasets with different characteristics or from different domains? Have you considered evaluating the model on additional datasets to assess its generalizability?
2. The proposed method introduces a routing network and multiple expert decoders, which may increase the computational cost and complexity of the model. Can you provide more details on the computational efficiency of the model and how it compares to other anomaly detection methods?
3. The hallucination-aware expert decoder is designed to minimize false positives. However, in medical images, some anomalous regions may be subtle and closely resemble normal regions. How does the model handle such cases, and what is the risk of false negatives?

### Rating

6

### Confidence

4

**********
