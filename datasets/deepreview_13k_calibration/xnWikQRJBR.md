# M3CoL: Harnessing Shared Relations via Multimodal Mixup Contrastive Learning for Multimodal Classification

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 6, 5, 3

## Abstract
Deep multimodal learning has shown remarkable success by leveraging contrastive learning to capture explicit one-to-one relations across modalities. However, real-world data often exhibits shared relations beyond simple pairwise associations. We propose \textbf{M3CoL}, a \textbf{M}ulti\textbf{m}odal \textbf{M}ixup \textbf{Co}ntrastive \textbf{L}earning approach to capture nuanced \textit{shared relations} inherent in multimodal data. Our key contribution is a Mixup-based contrastive loss that learns robust representations by aligning mixed samples from one modality with their corresponding samples from other modalities thereby capturing shared relations between them. For multimodal classification tasks, we introduce a framework that integrates a fusion module with unimodal prediction modules for auxiliary supervision during training, complemented by our proposed Mixup-based contrastive loss. Through extensive experiments on diverse datasets (N24News, ROSMAP, BRCA, and Food-101), we demonstrate that \textbf{M3CoL} effectively captures shared multimodal relations and generalizes across domains. It outperforms state-of-the-art methods on N24News, ROSMAP, and BRCA, while achieving comparable performance on Food-101. Our work highlights the significance of learning shared relations for robust multimodal learning, opening up promising avenues for future research.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces M3CoL, a novel multimodal learning approach that leverages mixup contrastive learning to capture nuanced shared relations across modalities, going beyond traditional pairwise associations. The key contribution is a mixup-based contrastive loss function that aligns mixed samples from one modality with corresponding samples from others. The work highlights the importance of learning shared relations for robust multimodal learning and has implications for future research.

### Strengths
1.) M3CoL's use of mixup-based contrastive learning to capture shared relations in multimodal data, offering a new perspective on multimodal representation learning.
2.) The theoretical analysis of M3CoL, including contrastive loss and the integration of unimodal and fusion modules,  contributes to the theoretical understanding of multimodal learning.
3.) The paper is well written, with clear explanations of the methodology, experiments, and results, making it accessible to readers.

### Weaknesses
1.) The paper does not deeply address how M3CoL scales with very large datasets, which could be a limitation given the increasing size of real-world datasets.
2.) There's a potential risk of overfitting with mixup, especially in early training stages. More analysis on balancing generalization and overfitting would be valuable.
3.）M3CoL's effectiveness relies heavily on the quality of mixed samples. Discussion on how data quality variations across modalities might affect performance is lacking.

### Questions
see the Weaknesses

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces M3CoL to capture complex shared relationships in multimodal data by aligning mixed samples from one modality with corresponding samples from others. This method leverages a Mixup-based contrastive loss with controlled mixup factor, extending beyond typical pairwise associations. A SoftClip-based loss is also adopted to enable many-to-many relationships between the two modalities. M3CoL also incorporates a novel multimodal learning framework that integrates unimodal prediction modules and a fusion module to improve classification. Experimental results show that M3CoL outperforms state-of-the-art methods on N24News, ROSMAP, and BRCA, and achieves comparable performance on Food-101.

### Strengths
Clarity: The paper is well-structured, with clear explanations of the methodology, including detailed descriptions of the Mixup-based contrastive loss and the unimodal and fusion modules. 

Significance: M3CoL advances multimodal classification by addressing the limitations of traditional contrastive methods, offering improved generalization across domains. Its contributions are valuable for future research in multimodal learning, especially nuanced multimodal relationships like medical datasets.

### Weaknesses
Originality: Incorporating Mixup in contrastive learning is not new [1-3], even in a multimodal setting ([4-6], see Questions.) The reviewer would truly appreciate the authors’ further discussions on [4-6].

Significance: datasets, especially the non-medical datasets, are relatively small. The effectiveness of the method is yet to be seen from larger, real-world datasets. Since this method is relatively straightforward, larger-scale experiments will improve the significance of the submission.

### Questions
Could the authors kindly discuss the following related work ([6] being concurrrent): 

[4] Wang, Teng, et al. "Vlmixer: Unpaired vision-language pre-training via cross-modal cutmix." International Conference on Machine Learning. PMLR, 2022.

[5] Georgiou, Efthymios, Yannis Avrithis, and Alexandros Potamianos. "PowMix: A Versatile Regularizer for Multimodal Sentiment Analysis." arXiv preprint arXiv:2312.12334 (2023).

[6] Bafghi, Reza Akbarian, et al. "Mixing Natural and Synthetic Images for Robust Self-Supervised Representations." arXiv preprint arXiv:2406.12368 (2024).

### Soundness
3

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
This study introduces M3CoL, a deep multimodal learning method for capturing complex relationships in real-world data. M3CoL captures shared multimodal relationships by employing a contrast loss based on mixed samples and introduces a fusion module for multimodal classification tasks for supplementary supervision.

### Strengths
1.	M3CoL uses a smart technique to find and learn common patterns across different data types. It’s like having a tool that can spot similarities in things that might not look alike, making it good at understanding complex data relationships.
2.	The experiments and analysis are extensive, involving multiple datasets with various types of data and analyses.

### Weaknesses
The reasons for the training sample selection strategy are not explained, and some experimental results are incomplete.

### Questions
1. The ACC for the Body section in N24News has not been provided.
2. Samples from modality 1 (x_i^1,x_j^1) and modality 2 (x_i^2,x_k^2), along with their respective mixed data, are fed into encoders to generate embeddings. How were samples j and k selected, and why can’t they both be j?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces M3CoL (Multimodal Mixup Contrastive Learning), a method aimed at capturing shared, non-pairwise relationships within multimodal data. The framework includes a mixup-based contrastive loss to align mixed samples across modalities, facilitating more robust representations for multimodal classification tasks.

### Strengths
- Inovative way to perform contrastive learning: The use of Mixup in a contrastive learning setting for multimodal data is quite novel and experimentally illustrate to have positive effects.
- Experiments regarding Attention map between text and image regions provide a good illustration for the effectiveness of alignment process.

### Weaknesses
 - **The motivation of the manuscript is not strong**. The process of aligning Positive couplets and Negative couplets in pairwise manner do not necessarily ignore the shared relational
information exist between samples. There are lines of contrastive learning work (e.g. [1]) which align representations of sample within the same class together. Why does the mixup can better improve the performance compared to these approaches?
- **The rationale of using MixUp technique is not well stated**. Is there any reason behind the choice of MixUp as a way to combine samples? Additional ablation studies can be provided to strengthen the choice empirically.
- Beside the idea of MixUp contrastive learning strategy, **the rationale of applying unimodal downstream loss** is also short of explanation. While it does show improvement via Ablation study, why is it the case that it can indeed help the overall system?

### Questions
Please refer to Weaknesses for related questions.

### Soundness
2

### Presentation
3

### Contribution
2
