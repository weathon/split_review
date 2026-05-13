# Contrast with Aggregation: A Scalable Framework for Multi-View Representation Learning

- Decision: Reject
- Scores: 5, 6, 5, 8

## Abstract
Multi-View Representation Learning (MVRL) aims to learn the joint representation from diverse data sources by discovering complex relationships among them.
In MVRL, since the downstream task information and the view availability are often unknown a-priori, it is essential for the joint representation to be robust to the partial availability of views.
However, existing methods exhibit various limitations, such as discarding potentially valuable view-specific information, lacking
the ability to extract representation from an arbitrary subset of views, or requiring considerable computational resources that increase exponentially with the number of views.
To address these challenges, we present a scalable MVRL framework based on contrastive learning.
Our approach employs a set of encoders that is able to extract representations from arbitrary subset of views, and jointly trains them with a computation cost that scales linearly with the number of views.
We conducted comprehensive evaluations across 7 MVRL benchmark datasets ranging from 2 to 8 views, demonstrating that our method robustly handles diverse input view combinations and outperforms strong baseline methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a scalable multi-view representation learning (MVRL) framework named CwA based on contrastive learning to address the challenges in MVRL. It can effectively aggregate information from any subset of views. It optimizes each subset-view representation with a computational cost that increases linearly with the number of views, thus optimizing the computational cost. In addition, by integrating the Mahalanobis distance into the InfoNCE objective, this article reformulates their method as a contrastive learning (CL) approach for calibrating each subset-view representation. It has achieved good results on multiple datasets.

### Strengths
They introduced CwA, a scalable Multi View Representation Learning (MVRL) framework that can effectively aggregate information from any subset of views. Not only did it reduce the complexity of some models, decrease the complexity of parameter count and training time, but it also achieved better results than most related works.

### Weaknesses
1.This paper describes the reduction in the number of encoder parameters, but lacks a comparison of the number of encoder parameters in the paper. The effectiveness and necessity of the paper's method cannot be verified through poor experiments.
2.The explanation of related work in the paper is relatively simple, and it is relatively difficult for non professionals to understand the paper.  Besides, the role of the encoder and the significance of the operations performed in this article are not clear enough, and the description of the methods section is not concise enough. A large amount of space is provided to supplement the explanation, which I think is unreasonable.
3. This article proposes that the model can be modal extended, but I did not see any difference in this scalability compared to previous models in the paper. Please clarify with the submitter.

### Questions
1.Have you ever considered why the model performs relatively poorly in a single modality? Is it due to hyperparameters?
2.Are the results obtained by other methods tested by the author themselves on the server or published in other papers? Does the author think it has any reference value?
3.Has the author considered the performance of the model in subsequent tasks?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents Contrast with Aggregation (CwA) framework for multi-view representation learning that efficiently aggregates information from any subset of views using contrastive learning. CwA addresses computational and robustness challenges in multi-view learning by leveraging an information-theoretic objective and Mahalanobis distance to jointly train subset-view representations with a computation cost that scales linearly with the number of views. Extensive experiments demonstrate CwA's effectiveness and scalability, showing it outperforms baseline methods across multiple benchmark datasets source.

### Strengths
(1) The paper tackles computational challenges in multi-view learning by using an information-theoretic objective and Mahalanobis distance to train subset-view representations jointly, achieving a computation cost that scales linearly with the number of views.

(2) The paper has presented extensive experiments showing the effectiveness and scalability of CwA. The paper is clearly written and different details are well understood.

### Weaknesses
 (1) The paper lacks an explicit statement of its contributions, leaving its main claims unclear. This should definitely be clarified in the introduction. Furthermore, the related works section does not sufficiently situate the proposed approach within the existing body of research. Without these clarifications, it is challenging to fully assess the paper.

(2) The paper could be seen as an extensive application of the inverse variance weighted (IVW) average for information fusion. However, it does not investigate whether this fusion method is optimal for various downstream tasks. Additionally, it would be valuable to explore whether this fusion approach is effective when applied with other metrics as well.

(3) Table 1 indicates that, for some datasets, performance achieved with a single modality surpasses that with combined views. For instance, on the MOSI dataset, CwA attains a classification accuracy of 67.23% using only the text modality, whereas combining all three views results in a lower accuracy of 65.61%, suggesting that information fusion may actually reduce model performance. This observation and a reasoned explanation is not discussed in the paper. So, I am looking for some insightful discussion to understand the reasons behind this observation.

### Questions
Please see the weaknesses section

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces Contrast with Aggregation (CwA), a scalable Multi-View Representation Learning (MVRL) framework designed to efficiently learn joint representations from diverse views. By leveraging contrastive learning with the InfoNCE objective and encoding subsets of views through Weighted Mixture of Experts (WMoE), CwA enables linear computational scaling relative to the number of views, allowing it to extract robust representations from any subset of views.

### Strengths
1. Compared to traditional methods, this approach demonstrates greater adaptability and scalability across different combinations of views.
2. By simplifying multiple terms that maximize mutual information (MI) into a single term, this strategy reduces computational costs, making it more effective in multi-view scenarios.
3. The paper includes open-source code, which enhances reproducibility.

### Weaknesses
1. The paper lacks sufficient theoretical justification for the choice of mutual information estimators and the use of specific distance metrics (Mahalanobis distance). More detailed theoretical explanation for this selection should be provided. Specifically, the paper should elaborate on why the chosen estimator is optimal or at least well-suited for the specific characteristics of the data and the learning task. The use of Mahalanobis distance, while accounting for variance, needs a more rigorous explanation, especially when compared to other common metrics like cosine similarity or Euclidean distance, which have different underlying assumptions and may be more appropriate in certain scenarios. A deeper analysis of the implications of these choices on the learned representations is needed.
2. In the experiments, the paper notes that the method performs slightly worse than other baseline methods in single-view scenarios. While this issue improves with multiple view combinations, a thorough exploration of why CwA fails to surpass other methods in single-view cases and the implications for practical applications is necessary. The paper should investigate whether this is due to the architecture, the training procedure, or the inherent limitations of the approach when only a single view is available. Furthermore, the paper should discuss the trade-offs between performance in single-view and multi-view scenarios, and how this impacts the applicability of the method in real-world scenarios where some views might be missing or unreliable.
3. Although the paper conducts extensive experiments across various tasks, the selected datasets and task types are relatively narrow, primarily focusing on sarcasm and emotion recognition. Validation on more diverse datasets (e.g., ImageNet and NYU-Depth-V2) and tasks (e.g., action recognition on videos) should be explored to verify the method's effectiveness. The current evaluation does not fully demonstrate the generalizability of the method to different data modalities and task complexities. The paper should also consider evaluating the method on datasets with a larger number of views to assess its scalability in more challenging scenarios.
4. For the used datasets, the current advanced pretrained deep backbones should be employed to perform feature extraction for different data views instead of the somewhat handcrafted preprocessed features. More thorough studies are necessary to show its superiority. The paper should clarify the specific pretrained models used, and explain why these models were chosen over other alternatives. A comparison of the proposed method's performance using different backbone architectures would also be beneficial to understand the robustness of the approach.

### Questions
Please refer to the weaknesses part.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper studies an innovative multi-view representation learning framework：Contrast with Aggregation: A scalable Framework for Multi-view Representation Learning. Existing multi-view representation learning methods have three main limitations: (1) discarding potentially valuable view-specific information; (2) inability to extract representations from arbitrary subsets of views; (3) computational costs exponentially increasing with the number of views. To address these issues, this paper proposes a scalable subset view representation learning framework based on contrastive learning. This framework reduces the number of encoder parameters by simplifying the existing encoder structure, thus lowering computational costs. It is capable of learning each subset view representation through a single objective function, making the computational cost grow linearly with the number of views. Finally, this paper introduces an operational lower bound to effectively calibrate the subset view representations based on contrastive learning. Experimental results demonstrate that this method can effectively handle various combinations of views across multiple benchmark datasets and outperforms other strong baseline methods.

### Strengths
1.This paper is well-structured, with clear explanations of the problems with existing methods, the proposed solutions, and the experimental results. 

2.The motivation  to extract representation from an arbitrary subset of views  is commendable.

3.CwA proposes a scalable subset view representation learning framework based on contrastive learning. This framework serves as a new paradigm for multi-view representation learning, offering new insights into how different data views can enhance the model's learning capabilities.

### Weaknesses
1.Please provide a detailed explanation of the relationship between the analysis method presented in this paper and the one in [1], and if possible, offer a comparison with [1].

2.This paper mainly addresses two issues: scalability and calibration. However, the experimental section does not perform calibration verification.

### Questions
See the above weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3
