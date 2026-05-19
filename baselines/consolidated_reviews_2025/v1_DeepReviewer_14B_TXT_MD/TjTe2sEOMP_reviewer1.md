### Summary

This work presents a prompt-guided multi-organ, multi-modal anomaly detection framework. The authors collect a dataset spanning 12,153 images across 5 imaging modalities and 4 anatomical structures. They propose a mixture of experts framework, capable of routing images to suitable hallucination-minimized expert decoders based on text prompts. The experimental results demonstrate the superiority of the proposed method.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The authors collect and publicly release a dataset, which is valuable for the development and evaluation of universal anomaly detection methods.
2. The proposed method is relatively easy to understand.
3. The manuscript is well-written.

### Weaknesses

#### Some Related Works


#### comment

1. The concept of using MoE for universal anomaly detection has been explored in the industry anomaly detection field. The authors are encouraged to review and discuss the differences between their proposed method and existing industry methods, such as the following papers:
MoCoE: Saving Inference Costs in Outlier Detection by Using Mixture of Experts with Sparse Routing
Sparse Mixture-of-Experts are Predictive Anomaly Detectors
Quantile Regression with Mixture of Experts for Prognostic Uncertainty Modeling in Hematology-Oncology
2. How can the proposed method be applied to the anomaly detection of new types of data (e.g., new modalities or organs)?
3. The authors are encouraged to discuss the computational complexity of the proposed method.
4. In Figure 6, the authors should provide a more detailed explanation of the relationship between experts and tasks.
5. In the experiments, the authors are encouraged to include results for the following methods:
SSD: Supervised Sparse Domain Adaptation for Unsupervised Anomaly Detection
3DCNN: Anomaly Detection with Three-Dimensional Convolutional Neural Networks
6. The authors are encouraged to compare their method with existing industrial anomaly detection methods.

### Suggestions

The paper introduces a prompt-guided multi-organ, multi-modal anomaly detection framework using a mixture of experts (MoE) approach. While the concept of using MoE for anomaly detection is not entirely novel, the authors should more clearly articulate the specific differences between their approach and existing methods, particularly in the context of medical image analysis. For instance, the cited papers on MoE for anomaly detection in industrial settings highlight the potential for MoE to handle diverse data types and tasks. The authors should discuss how their method builds upon or diverges from these approaches, focusing on the unique challenges and requirements of medical anomaly detection, such as the need for high sensitivity and specificity, and the interpretability of results. A more detailed comparison of the architectural choices, training procedures, and performance trade-offs would be beneficial to establish the novelty and contribution of this work.

Furthermore, the paper needs to address the practical limitations of the proposed method, especially regarding its applicability to new data types. The current framework appears to be designed for a fixed set of modalities and organs, and the authors should provide a clear strategy for extending the method to new scenarios. This could involve discussing the process of adding new experts, retraining the routing network, and ensuring that the model can generalize to unseen data. The authors should also discuss the computational cost associated with adding new experts and how this impacts the overall scalability of the method. A detailed analysis of the computational complexity, including the number of parameters, training time, and inference time, is crucial for assessing the practical feasibility of the proposed approach. This analysis should also consider the impact of the number of experts on the computational burden.

Finally, the experimental evaluation should be strengthened by including comparisons with more relevant baselines. While the authors include some anomaly detection methods, the selection of baselines could be improved. Specifically, the inclusion of methods like SSD and 3DCNN is important, as they represent different approaches to anomaly detection. SSD, with its focus on domain adaptation, could provide a valuable comparison for the proposed method's ability to generalize to new data. Similarly, 3DCNN, which leverages volumetric information, could highlight the limitations of the proposed method when dealing with 3D medical images. A more comprehensive comparison with these methods, along with a discussion of the results, would provide a more robust evaluation of the proposed framework. Additionally, a comparison with existing industrial anomaly detection methods would be beneficial to contextualize the performance of the proposed method in a broader landscape.

### Questions

Please see the weaknesses.

### Rating

6

### Confidence

4

**********
