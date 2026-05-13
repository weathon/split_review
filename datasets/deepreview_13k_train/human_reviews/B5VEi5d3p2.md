# SleepSMC: Ubiquitous Sleep Staging via Supervised Multimodal Coordination

- Decision: Accept
- Scores: 6, 6, 5, 6

## Abstract
Sleep staging is critical for assessing sleep quality and tracking health. Polysomnography (PSG) provides comprehensive multimodal sleep-related information, but its complexity and impracticality limit its practical use in daily and ubiquitous monitoring. Conversely, unimodal devices offer more convenience but less accuracy. Existing multimodal learning paradigms typically assume that the data types remain consistent between the training and testing phases. This makes it challenging to leverage information from other modalities in ubiquitous scenarios (e.g., at home) where only one modality is available. To address this issue, we introduce a novel framework for ubiquitous Sleep staging via Supervised Multimodal Coordination, called SleepSMC. To capture category-related consistency and complementarity across modality-level instances, we propose supervised modality-level instance contrastive coordination. Specifically, modality-level instances within the same category are considered positive pairs, while those from different categories are considered negative pairs. To explore the varying reliability of auxiliary modalities, we calculate uncertainty estimates based on the variance in confidence scores for correct predictions during multiple rounds of random masks. These uncertainty estimates are employed to assign adaptive weights to multiple auxiliary modalities during contrastive learning, ensuring that the primary modality learns from high-quality, category-related features. Experimental results on three public datasets, ISRUC-S3, MASS-SS3, and Sleep-EDF-78, show that SleepSMC achieves state-of-the-art cross-subject performance. SleepSMC significantly improves performance when only a single modality is present during testing, making it suitable for ubiquitous sleep monitoring. Our code will be released after formal publication.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents SleepSMC, a sleep stage classification framework that integrates uncertainty-based feature reweighting with modality-level contrastive learning to handle multimodal physiological data (EEG, EOG, EMG) effectively. The reweighting mechanism assigns weights to auxiliary modalities based on their uncertainty. Then, they use contrastive learning to align representations of the same sleep stage across different modalities. SleepSMC achieves modality-invariant embeddings that allow for robust performance even when only a single primary modality is available at test time. SleepSMC is evaluated on three public datasets, consistently outperforming SOTA baselines in both multimodal and unimodal settings.  They present ablation studies demonstrating that reweighting and contrastive learning are both effective individually and moreso when combined. Visualization analyses further demonstrate the model’s interpretability, showing clear, well-separated embeddings for each sleep stage.

### Strengths
This paper presents SleepSMC, a sleep stage classification framework that integrates uncertainty-based feature reweighting with modality-level contrastive learning to handle multimodal physiological data (EEG, EOG, EMG) effectively. The reweighting mechanism assigns weights to auxiliary modalities based on their uncertainty. Then, they use contrastive learning to align representations of the same sleep stage across different modalities. SleepSMC achieves modality-invariant embeddings that allow for robust performance even when only a single primary modality is available at test time. SleepSMC is evaluated on three public datasets, consistently outperforming SOTA baselines in both multimodal and unimodal settings.  They present ablation studies demonstrating that reweighting and contrastive learning are both effective individually and moreso when combined. Visualization analyses further demonstrate the model’s interpretability, showing clear, well-separated embeddings for each sleep stage. 

Originality
The uncertainty reweighting technique is clever and novel.  Most importantly, it is both empirically and theoretically effective. The contrastive learning component, combined with reweighting, enables the model to create modality-invariant embeddings, allowing SleepSMC to generalize effectively across different primary modalities.


Quality
The quality of the work is high. The evaluation is thorough, providing empirical, theoretical, and qualitative support for their approach. Reweighting consistently outperformed non-reweighted setups in both multimodal and unimodal testing, with clear gains in accuracy, Macro F1, and Kappa scores, particularly under noisy conditions. Combining reweighting with contrastive learning further boosted performance compared to contrastive learning alone, showing that these methods work well together, especially with unreliable auxiliary modalities. SleepSMC also generalized effectively across target modalities, performing robustly whether EEG, EOG, or EMG was used as the primary modality, demonstrating flexibility across configurations.
In both multimodal and unimodal testing, SleepSMC maintained high accuracy, with unimodal performance benefiting notably from reweighting. t-SNE visualizations showed clear, well-separated clusters for each sleep stage, supporting the model’s modality-invariant embedding space and interpretability. These results confirm that SleepSMC’s reweighting and contrastive learning mechanisms enhance robustness and adaptability, making it a practical solution for real-world sleep staging.


Clarity
The work is mostly clearly presented. The methodology and results are well-structured, and the theoretical analysis is solid, providing strong support for the approach. However, the introduction of mathematical notation in Section 3 could be organized more effectively; starting with a table or list of symbols and definitions before diving into the equations would help clarify the notation and reduce cognitive load for the reader. The paper is otherwise transparent in discussing its limitations, and the overall clarity of the empirical findings is strong.


Significance
The work makes a meaningful contribution, adding to the literature on multimodal integration, particularly in scenarios where only unimodal data is available at test time—an approach that aligns well with many real-world applications.

### Weaknesses
 1. The introduction of mathematical notation in Section 3 is somewhat disorganized and could be clarified better. Starting this section with a concise table or list of symbols and definitions would provide readers with a quick reference point, making it easier to follow the subsequent equations. This adjustment would enhance readability, especially for readers less familiar with the specific notation conventions used.

2. The work makes a solid contribution to the field, with gains in the range of 2-3%, which are statistically significant but don’t drastically improve performance over baseline methods. While these improvements are valuable they're somewhat incremental.  Perhaps the gains are more significant in other multimodal learning problems.

### Questions
An important aspect of multimodal classification models is cross-subject generalization. Given that real-world applications often involve new subjects with varying characteristics, an evaluation on unseen subjects would provide valuable insight into the model’s robustness. If cross-subject generalization was analyzed, could the authors include these results? Otherwise, adding this analysis would strengthen the paper’s practical relevance.

Additionally, while the reported improvements are statistically significant, they appear relatively modest, with gains in the range of 2-3%. Could the authors elaborate on why these incremental gains are meaningful in the context of sleep staging? Providing additional context on the impact of these gains for real-world applications would clarify the value of these results.

Although the reweighting technique is effective within sleep staging, it would be useful to understand its potential applicability beyond this domain. Do the authors see possible applications of uncertainty-based reweighting in other multimodal learning tasks? Expanding on this would highlight the versatility and broader impact of the proposed method.

In terms of practical applications, it would be helpful to know how this model performs in real-world scenarios where data quality and availability are less controlled. Could the model handle dynamic shifts in modality reliability, and do the authors envision practical deployments for health monitoring or similar applications?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduced multimodal collaboration in sleep staging, leveraging multiple auxiliary modalities to improve the performance of primary modality-based sleep staging in an end-to-end manner. The authors utilized supervised modality-level instance contrastive coordination to capture category-related consistency and complementarity across intra-modality and inter-modality.

### Strengths
Experiments are performed using 3 different datasets. The organization of the paper is good.

### Weaknesses
The limitations are as follows:

The motivation is not clear.
How this contribution is different from the following contributions? a)CoRe-Sleep: A Multimodal Fusion Framework for Time Series Robust to Imperfect Modalities," in IEEE Transactions on Neural Systems and Rehabilitation Engineering, vol. 32, pp. 840-849, 2024, doi: 10.1109/TNSRE.2024.3354388. b) Multi-Modal Sleep Stage Classification With Two-Stream Encoder-Decoder," in IEEE Transactions on Neural Systems and Rehabilitation Engineering, vol. 32, pp. 2096-2105, 2024, doi: 10.1109/TNSRE.2024.3394738.
The motivation behind the use of Uncertainty Estimation with Frozen Gradients is not clear.
The methods mentioned in Table 2 are from before 2022. It is necessary to compare with some recent SOTA methods

### Questions
1. How the proposed method is different from SOTA?
2. What is the novel contribution that makes this paper unique?
3. What is the computational complexity?
4. How equation 10 become optimized?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
To address the issue that only one modality is available in ubiquitous scenarios, this paper introduce multimodal collaboration in sleep staging, leveraging multiple auxiliary modalities to improve the performance of primary modality-based sleep staging in an end-to-end manner. The paper utilize supervised modality-level instance contrastive coordination and uncertainty estimates to learn coordinated features. The experiment results show that the proposed method achieves SOTA performance in multimodal scenarios and unimodal scenarios.

### Strengths
The paper aims to address the issue that only one modality is available in ubiquitous scenarios, which has certain practical significance.

The paper utilizes uncertainty estimates to adaptively weight auxiliary modality features during
training, which ensures that more reliable auxiliary modality features contribute more significantly to the contrastive learning process.

The presentation of the paper is generally quite clear.

### Weaknesses
(1) This paper does not introduce a new concept; rather, it applies existing multimodal coordination and uncertainty estimates to the ubiquitous scenarios of sleep staging. Moreover, the proposed method for improving sleep staging does not seem to differ significantly from the multimodal coordination methods already used in areas such as vision. Some design details in the method, such as certain aspects related to uncertainty estimates, do not demonstrate a specific focus on the sleep staging task. The application of contrastive learning and uncertainty weighting, while effective, lacks novelty in the context of multimodal learning, and the paper does not adequately justify why these specific techniques are particularly well-suited for sleep staging compared to other existing methods.

(2) The authors seem to use a single-epoch sleep staging paradigm instead of a sequence-to-sequence sleep staging approach. Why is this the case? In fact, there is a strong correlation between adjacent epochs in sleep staging, and the single-epoch paradigm has already fallen behind in performance and been largely abandoned. As a paper aimed at improving sleep staging performance, it is difficult to understand the choice of using a single-epoch paradigm. Could the authors explain why this paradigm was chosen and whether the proposed method can be adapted to the sequence-to-sequence paradigm?

(3) The reviewer has some concerns about the experimental design and results. The baselines chosen by the authors appear to be relatively weak and outdated, such as the selection of SimCLR, which is a very old self-supervised learning method. The baselines in the paper perform very weakly in multimodal scenarios (shown in Table 1), making it difficult to demonstrate the advantages of the proposed method. Some very strong baselines, such as SalientSleepNet [1], BSTT [2] and XSleepNet [3] were not compared. Meanwhile, the reviewer cannot understand why the authors chose ISRUC-S3 instead of ISRUC-S1 as the primary evaluation dataset. ISRUC-S1 has more subjects and a larger data volume, making it more convincing compared to ISRUC-S3.

(4) Although the presentation of the paper is relatively clear, the content in "DETAILED ANALYSIS AND PROOFS IN SECTION 4" is difficult for readers to understand. As a supplement and proof of certain concepts in the main text, this section does not sufficiently clarify the formal definitions of each concept and the complete proof process. For example, what is the complete proposition that needs to be proven in this section? What are the assumptions underlying the proof process? What is the formal definition of "margin"? What is the formal definition of "information transfer"? The authors should provide clear explanations and complete definitions of these concepts in the appendix to ensure the readability of the paper.

### Questions
Please See Weakness

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The manuscript proposes SleepSMC, a method for detecting sleep stages leveraging contrastive learning and feature weighting based on uncertainty. The approach is specifically designed to handle scenarios where multiple data modalities are available during training, but only a single modality is accessible during testing (multimodal scenario has also been evaluated). Using three publicly available datasets, the authors demonstrate that SleepSMC achieves performance improvements over existing baselines.

### Strengths
- The paper is well-structured and clear, and easy to follow.
- Includes extensive experiments comparing the proposed method with various baselines.

### Weaknesses
 - Limited technical novelty.
- More recent & missing-modality-specific baselines could be considered as stronger baselines.

[Details]
1. Could the authors explain why "Supervised Contrastive Learning" by Khosla et al. (2020) was not considered as one of the baselines? What specific motivations underlie the use of contrastive learning here, and in what ways does the proposed technique differ (in terms of technical novelty) from the original approach in Khosla et al.? 
        - Khosla, Prannay, et al. "Supervised contrastive learning." Advances in Neural Information Processing Systems 33 (2020): 18661-18673.

2. Is there any method or technique in this work that is specifically tailored for sleep stage detection? The proposed approach appears applicable to most multimodal data; If that's the case, other recent works targeting learning/inference with missing modalities could be considered as baselines as well:
    - Wang, Hu, et al. "Multi-modal learning with missing modality via shared-specific feature modelling." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2023.
   - Yao, Wenfang, et al. "DrFuse: Learning Disentangled Representation for Clinical Multi-Modal Fusion with Missing Modality and Modal Inconsistency." Proceedings of the AAAI Conference on Artificial Intelligence. Vol. 38. No. 15. 2024.


[Problem setting & method] 
1. Could the authors clarify the rationale for assuming that only one modality is available during inference? While it is understandable that not all modalities used in training may be accessible at test time, it seems uncommon to assume the presence of only a single modality. A more practical scenario might involve each user having a unique set of available modalities at test time, rather than relying on one fixed modality. Could the authors elaborate on the motivation behind this specific setting?

2. Would it be expected that the auxiliary modality classifiers exhibit higher uncertainty at the beginning of training? If so, could this uncertainty indicate an opportunity for the model to learn more effectively? Did the authors experiment with dynamic tuning of weights over the course of training? Additionally, numerous metrics (such as entropy, model confidence, loss) could potentially assess sample importance. What was the rationale for selecting model confidence? Were other metrics considered, and if so, what were the comparative results?

[Related work & Baselines]  
1. In Section 2, Liu et al. (2023b) and Liu et al. (2024) are referenced as leveraging multimodal data to enhance performance, with the former employing contrastive learning to align modalities. Could the authors clarify why these methods were not considered as baselines? Additionally, it is noted that these works focus on multimodal consistency without capturing class-specific information. However, the design choices of related works should not necessarily be considered limitations. Could the authors discuss the impact of excluding class-specific information? How can we assess the relative performance without a comparison to the proposed method?

2.  In Section 2, several works related to uncertainty estimation are discussed, but the conclusion remains somewhat ambiguous. Why are these methods not applicable to the target scenario? What challenges prevent their direct application to the proposed task, especially given that multimodal data are still used during training?

[Results]
1. In most scenarios, including unimodal cases, the primary improvements appear to stem from supervised contrastive learning. However, in Section 5.5, it is stated that “uncertainty-based feature weighting has a greater impact in the unimodal testing scenario,” which may be an overstatement. Could the authors provide comparative improvement results (e.g., average ± standard deviation) for both components? If the enhancement from uncertainty-based feature weighting is minor, what justifies its inclusion?

2. Could the authors explain the observed fluctuations in EEG and EOG uncertainty weights as training progresses (as seen in Figure 3c)?

[Minor comments]:
- Font size in Figure 3 appears small.
- Class labels in Figure 4 are difficult to read; increasing the legend font size could improve readability.
- Typo in Section 4.2, first sentence: “adaptively weighted” should be “adaptively weights.”

### Questions
[Problem setting & method] 
1. Could the authors clarify the rationale for assuming that only one modality is available during inference? While it is understandable that not all modalities used in training may be accessible at test time, it seems uncommon to assume the presence of only a single modality. A more practical scenario might involve each user having a unique set of available modalities at test time, rather than relying on one fixed modality. Could the authors elaborate on the motivation behind this specific setting?

2. Would it be expected that the auxiliary modality classifiers exhibit higher uncertainty at the beginning of training? If so, could this uncertainty indicate an opportunity for the model to learn more effectively? Did the authors experiment with dynamic tuning of weights over the course of training? Additionally, numerous metrics (such as entropy, model confidence, loss) could potentially assess sample importance. What was the rationale for selecting model confidence? Were other metrics considered, and if so, what were the comparative results?

[Related work & Baselines]  
1. In Section 2, Liu et al. (2023b) and Liu et al. (2024) are referenced as leveraging multimodal data to enhance performance, with the former employing contrastive learning to align modalities. Could the authors clarify why these methods were not considered as baselines? Additionally, it is noted that these works focus on multimodal consistency without capturing class-specific information. However, the design choices of related works should not necessarily be considered limitations. Could the authors discuss the impact of excluding class-specific information? How can we assess the relative performance without a comparison to the proposed method?

2.  In Section 2, several works related to uncertainty estimation are discussed, but the conclusion remains somewhat ambiguous. Why are these methods not applicable to the target scenario? What challenges prevent their direct application to the proposed task, especially given that multimodal data are still used during training?

[Results]
1. In most scenarios, including unimodal cases, the primary improvements appear to stem from supervised contrastive learning. However, in Section 5.5, it is stated that “uncertainty-based feature weighting has a greater impact in the unimodal testing scenario,” which may be an overstatement. Could the authors provide comparative improvement results (e.g., average ± standard deviation) for both components? If the enhancement from uncertainty-based feature weighting is minor, what justifies its inclusion?

2. Could the authors explain the observed fluctuations in EEG and EOG uncertainty weights as training progresses (as seen in Figure 3c)?

[Minor comments]:
- Font size in Figure 3 appears small.
- Class labels in Figure 4 are difficult to read; increasing the legend font size could improve readability.
- Typo in Section 4.2, first sentence: “adaptively weighted” should be “adaptively weights.”

### Soundness
3

### Presentation
3

### Contribution
2
