# Analytic Continual Test-Time Adaptation for Multi-Modality Corruption

- Decision: Reject
- Avg Score: 5.00
- Scores: 3, 5, 6, 6

## Abstract
Test-Time Adaptation (TTA) aims to help pre-trained model bridge the gap between source and target datasets using only the pre-trained model and unlabelled test data. A key objective of TTA is to address domain shifts in test data caused by corruption, such as weather changes, noise, or sensor malfunctions. Multi-Modal Continual Test-Time Adaptation (MM-CTTA), an extension of TTA with better real-world applications, further allows pre-trained models to handle multi-modal inputs and adapt to continuously-changing target domains. MM-CTTA typically faces challenges including \textbf{error accumulation}, \textbf{catastrophic forgetting}, and \textbf{reliability bias}, with few existing approaches effectively addressing these issues in multi-modal corruption scenarios. In this paper, we propose a novel approach, Multi-modality Dynamic Analytic Adapter (MDAA), for MM-CTTA tasks. We innovatively introduce analytic learning into TTA, using the Analytic Classifiers (ACs) to prevent model forgetting. Additionally, we develop Dynamic Selection Mechanism (DSM) and Soft Pseudo-label Strategy (SPS), which enable MDAA to dynamically filter reliable samples and integrate information from different modalities. Extensive experiments demonstrate that MDAA achieves state-of-the-art performance on MM-CTTA tasks while ensuring reliable model adaptation.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a novel method, Multi-modality Dynamic Analytic Adapter (MDAA), for Multi-Modal Continual Test-Time Adaptation (MM-CTTA) tasks. MM-CTTA extends traditional Test-Time Adaptation (TTA) to handle dynamic, multi-modal data with domain shifts caused by corruptions, such as sensor issues or environmental changes. The proposed method main incorporates an additional regression term on the target data for test-time adaptation. Experiments demonstrate that MDAA achieves state-of-the-art performance on MM-CTTA tasks, outperforming existing methods.

### Strengths
- Conitnual domain shift poses real challenges to existing deep learning models. Tackling the continual domain shift could improve the robustness and generalization of deep learning models.

- Existing test-time adaptation methods have not addressed the unique challenges in multi-modality corruptions. This paper explored an important but largely dismissed problem.

### Weaknesses
 - The proposed test-time adaptation method is by simply optimizing the ridge regression problem on both source and target data, as per Eq. (12). The innovation is similar to adding a cross-entropy loss with pseudo labels on target data in regular classification tasks. It is unclear what are the main technical challenges in deploying test-time adaptation methods to multi-modality data. Specifically, the paper does not adequately address how the method handles the inherent challenges of multi-modal data, such as varying noise levels or corruption types across different modalities. The ridge regression approach, while simple, may not be sufficiently robust to handle the complex interactions and dependencies between modalities in the presence of diverse corruptions.

- Although the paper is motivated by the continual domain shift challenges, the proposed method does not specifically address the challenge of continual domain shift. The overall framework is more like applying self-training to a regression problem. The method lacks a mechanism to explicitly model the temporal dynamics of the domain shift, which is crucial for continual adaptation. The method appears to treat each adaptation step independently, without considering the cumulative effect of previous adaptations, potentially leading to catastrophic forgetting of previously learned information.

- The adptation method requires access to source domain data which does not comply with the existing definitions of test-time adaptation or test-time training. The reliance on source data for initialization, while common, still blurs the line between traditional domain adaptation and test-time adaptation. A true test-time adaptation method should ideally operate without any prior knowledge of the source domain, adapting solely based on the incoming test data.

- The dynamic selection mechanism is quite disconnected to the context. I can hardly understand how the dynamic selection mechanism is integrated to the ridge regression problem. The paper does not provide a clear explanation of how the dynamic selection mechanism interacts with the ridge regression optimization. It's unclear how the selection of modalities influences the weight update process in the regression model, and how this selection is made adaptive to the changing corruption patterns.

- The manuscript introduced too many subscripts to the notations. It makes the paper hard to follow.

- It may not be necessary to present the closed-form solution to ridge regression with a Threorem. The derivation of closed-form solution is well-known.

### Questions
- The authors should provide more discussions on how the proposed method addresses the continual domain shift challenges.

- Further evaluations of the significance of keeping the MSE term on source data is necessary.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a novel multi-modality dynamic analytic adapter (MDAA) approach for addressing the shortcomings of existing multi-modal continual test-time adaptation methods (MM-CTTA). MDAA aims to pay attention to solving the problem of domain shift caused by corruption in cross-domain data, and achieve this goal by integrating analytical classifiers (ACS), dynamic selection mechanism (DSM) and soft pseudo-labeling strategies (SPS). This method has effectively alleviated the superiority of the model by dynamically selecting reliable samples and integrating information of different modals, effectively alleviating problems such as error accumulation, catastrophic forgetting and reliability bias. Finally, the author verified the effectiveness of the proposed method through extensive experiments.

### Strengths
1. The paper has a clear motivation for the problem, clearly expresses the existing challenges in the field, and proposes innovative solutions to address them.
2. The method proposed in this article has efficient adaptability, that is, it can adapt without accessing the source data, saving computing resources and protecting data privacy.
3. This method can handle multimodal inputs and has more practical application potential compared to single modal methods.
4. The writing is coherent and logical, serving as a valuable resource for advancing the field.
5. This paper has a certain degree of originality and significance for the development of multimodal fields.

### Weaknesses
1. The analysis of the differences between the proposed method and existing methods, as well as the limitations of the analysis method is missing.
2. In the paper, the author proposed three modules (Acs, DSM, and SPS). However, in the ablation experiment, the author lacked experiments on ACs and SPS, as well as DSM and SPS. 
3. The running time of the proposed method on the model is also an important part of verifying the superiority of the method. Please supplement the running time of existing methods and all proposed methods in different models to verify whether the method can quickly fine tune and adjust the model.
4. Regarding the content of section 3.3, it still needs to be discussed whether the proposed scenario assumptions and parameter (theta) are consistent with real scenarios.
5. The complexity of the model has not been analyzed, and dynamic selection and soft pseudo labeling strategies may require high computational resources.
6. In the experimental section, only two datasets were used as experimental results to analyze whether the analysis is reliable, and whether there are other similar methods for MM-CTTA that can be compared.

### Questions
1. In the model framework of Figure 2, there are image encoders and speech encoders, indicating the existence of neural networks and learnable parameters in the paper. How did the author optimize the entire model, and is there any loss calculation in the model proposed by the author? What is the goal of optimizing the entire model?
2. In the overall model diagram of Figure 2, the information referred to by character B should be represented in the diagram for the convenience of readers' understanding.
3. Unified expression of content. For example, in section 3.4, line 316, subscript XT, t.
4. There is a regularization parameter (gamma) in formulas 6 and 12. The author stated in Appendix C.3 that gamma is within a reasonable range. Please add experiments to verify the rationality of a gamma value of 1.
5. How to fully utilize the complementary and consistent information of multimodal data to deal with corruption data.
6. What are the differences between this method and other methods that address the three core challenges of CTTA problems.
7. How to select pseudo labels and determine their reliability in section 3.4.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents a novel method called Multi-modality Dynamic Analytic Adapter (MDAA) to tackle the challenges of Multi-Modal Continual Test-Time Adaptation (MM-CTTA). In the MM-CTTA setup, pre-trained models are adapted in an online fashion to corrupted, multi-modal data (e.g., audio, video) without requiring access to original, labeled training data. The core idea in MDAA is its use of analytic classifiers - linear classifiers trained through recursive least squares that effectively store autocorrelation matrices in memory. This approach allows MDAA to retain essential knowledge from the original training data while adapting to ongoing data shifts. To further enhance adaptation, the paper introduces a Dynamic Selection Mechanism (DSM) that dynamically identifies and prioritizes reliable samples, ensuring that updates are informed by high-quality data. Additionally, a Soft Pseudo-label Strategy (SPS) refines pseudo-labels by assigning weighted probabilities across the top-k label predictions, rather than relying on one-hot labels, thus improving the model’s robustness to noisy labels.

The paper performs experiments on two datasets, Kinetics50-C and VGGSound-C, across a range of corruption types. MDAA is tested against state-of-the-art methods in both single-modality corruption and interleaved multi-modal corruption scenarios, demonstrating superior adaptability and robustness.

### Strengths
1. The majority of work in the continual test-time adaptation area focus on a single modality. While some works exist in the multi-modal space, they do not address the catastrophic forgetting issue well. MDAA introduces a recursive learning scheme which is tailored for tackling this issue. This makes MDAA highly relevant for practical applications.

2. Extensive experiment results on multiple scenarios are provided.

### Weaknesses
1. The classifiers in MDAA are fitted using a least squares loss function. It is well-known that models trained with least squares loss can lack robustness to outliers and are often outperformed by models trained with cross-entropy loss. It would be useful to see a comparison of the source model performance when trained with cross-entropy loss versus least squares loss. Specifically, if the source model classifiers were trained using cross-entropy and then frozen, would that source model perform better than the least squares version, even without adaptation? This is important to understand the baseline performance before adaptation.

2. The formulation restricts adaptation only to the classification layer. It has been shown in [1] how adapting the encoders themselves can improve performance. While [1] requires knowledge of which modality is corrupted, it would be informative to know what is the drop in performance due to this compromise. The argument that feature space adaptation is detrimental for CTTA is not definitively proven, especially considering methods like CoTTA already adapt the entire model. If the source model's feature extractor is not sufficiently robust, why would it not be beneficial to adapt it during test time?

3. The choice of leader network in DSM seems arbitrary in the absence of experiments which validate the choice. For example, how does choosing the lowest entropy network work? What other strategies have been explored, and are there any experiments to justify the current selection? Furthermore, how what is the frequency of updates using DSM? These questions need to be clarified. Also, what is the practical motivation for adapting the model every single sample, as is done in the experiments where MDAA performs best? Can a real-world scenario be provided where such a setup is necessary?

### Questions
1. What accounts for CoTTA’s significantly low performance (~5%) despite its use of a stochastic restoration mechanism? Additionally, do all baseline methods incorporate separate classifiers for each data stream?

2. How does MDAA’s training time compare to baselines that rely on backpropagation, given that MDAA requires computation of large autocorrelation matrices and their inverses?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces Multi-modality Dynamic Analytic Adapter (MDAA), a novel approach to Multi-Modal Continual Test-Time Adaptation (MM-CTTA). MDAA addresses key challenges in dynamic real-world scenarios, including error accumulation, catastrophic forgetting, and reliability bias. It leverages Analytic Classifiers (ACs) to prevent model forgetting, alongside a Dynamic Selection Mechanism (DSM) and a Soft Pseudo-label Strategy (SPS) to effectively integrate and filter multi-modal information. Extensive experiments demonstrate that MDAA outperforms current state-of-the-art methods on MM-CTTA tasks, showcasing its reliability and adaptability in handling modality corruption and dynamic changes.

### Strengths
- Effective Mitigation of Reliability Bias introduces a Dynamic Selection Mechanism (DSM) that dynamically prioritizes more reliable modalities while suppressing corrupted ones, a crucial feature for real-world scenarios where data quality and reliability may vary significantly across modalities. This reliability management enhances MDAA's robustness against data corruption, a critical improvement over existing MM-CTTA approaches.

- The use of Analytic Classifiers (ACs) within the MDAA framework enables continuous learning from new data while retaining previously acquired knowledge, ensuring effective long-term adaptability. This is particularly valuable in MM-CTTA tasks, where models must generalize from the source domain while adapting to continuously evolving target domains without catastrophic forgetting.

### Weaknesses
 - In the proposed MDAA method, how can we ensure the model does not overly rely on a single modality when dealing with highly imbalanced modal data? Is there empirical evidence of MDAA’s effectiveness in extreme cases?

- While MM-CTTA aims to handle real-world dynamic changes, can the model effectively respond to previously unseen modality corruption in practical applications? Are there relevant test results? Additionally, how effective is MDAA in rapidly changing scenarios where modality shifts occur frequently?

- The snow image in Figure 5 appears quite similar to the rain image. Could the authors check if there is a potential issue here?

- Does the MDAA method incur significant computational overhead? For practical applications, what measures can help balance model complexity with real-time adaptability?

- The motivation in the paper may benefit from further clarification. The issues of error accumulation, catastrophic forgetting, and reliability bias appear as a straightforward combination of Continual Test-Time Adaptation (CTTA) and Multi-modal Test-Time Adaptation (MM-TTA), where CTTA tackles error accumulation and forgetting, while MM-TTA focuses on reliability bias.

- In the Introduction, it is stated, “Error accumulation, stemming from incorrect pseudo-labels, can mislead models’ adaptation and potentially lead to collapse.” Does this imply that, if pseudo-labels were not used, error accumulation would not occur? If so, does this suggest that using pseudo-labels may be unnecessary?

### Questions
Another potential area for improvement in MDAA could be its robustness to label noise. While MDAA incorporates a Soft Pseudo-label Strategy (SPS) to enhance robustness against label noise, the effectiveness of this strategy in highly noisy environments remains to be fully evaluated. Future research could focus on developing more advanced mechanisms for detecting and mitigating label noise across different modalities.

### Soundness
3

### Presentation
2

### Contribution
2
