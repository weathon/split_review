### Summary

This paper proposes a prompt-driven mixture of experts framework for universal anomaly detection across multi-modal multi-organ medical images. The proposed method comprises encoders for vision and text, a routing network, and a mixture of hallucination-minimized expert decoders. Anomaly detection is conducted by jointly learning reconstruction and minimizing hallucinatory anomalies. The proposed method achieves state-of-the-art performance in anomaly detection.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The proposed method is technically sound and well-motivated.
2. The proposed method achieves state-of-the-art performance in anomaly detection.
3. The paper is well-written and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is evaluated on a dataset with 12,153 images from 5 modalities and 4 organs. However, the dataset is not publicly available, which makes it difficult to reproduce the results and verify the effectiveness of the proposed method.
2. The proposed method is not compared with some recent anomaly detection methods, such as UniAD, which is a relevant baseline for universal anomaly detection.

### Suggestions

The lack of a publicly available dataset significantly hinders the reproducibility and verifiability of the proposed method. While the authors mention the dataset is from a single institution, the absence of a clear protocol for data sharing and access severely limits the ability of the research community to validate the results and potentially extend the method to other datasets. To address this, the authors should consider releasing a subset of the data, or at least providing a detailed description of the data generation process, including the specific modalities, organs, and imaging protocols used. This would allow other researchers to validate the results and potentially extend the method to other datasets. Furthermore, the authors should provide clear guidelines on how to preprocess the data for their method, including any specific normalization or augmentation techniques. Without these details, the practical application of the proposed method remains challenging.

Regarding the comparison with existing methods, the absence of a comparison with UniAD is a notable omission. UniAD is a relevant baseline for universal anomaly detection, and its exclusion makes it difficult to assess the relative performance of the proposed method. The authors should include a comparison with UniAD, or at least provide a detailed justification for why such a comparison is not feasible. This comparison should include a discussion of the architectural differences, training procedures, and evaluation metrics used by both methods. Furthermore, the authors should consider comparing their method with other state-of-the-art anomaly detection methods, such as those based on generative models or contrastive learning, to provide a more comprehensive evaluation of their approach. This would help to contextualize the performance of the proposed method and highlight its strengths and weaknesses compared to existing approaches.

Finally, the authors should provide more details on the implementation of their method, including the specific hyperparameters used for training and evaluation. This would allow other researchers to reproduce the results and build upon their work. The authors should also provide a more detailed analysis of the computational cost of their method, including the training time and memory requirements. This information is crucial for assessing the practical applicability of the proposed method, especially in resource-constrained environments. Furthermore, the authors should discuss the limitations of their method and potential avenues for future research. This would provide a more balanced and comprehensive assessment of the proposed approach.

### Questions

Please see the weakness part.

### Rating

6

### Confidence

3

**********
