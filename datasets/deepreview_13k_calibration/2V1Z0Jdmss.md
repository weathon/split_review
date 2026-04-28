# On the Over-Memorization During Natural, Robust and Catastrophic Overfitting

- Decision: Accept
- Avg Score: 6.25
- Scores: 8, 6, 6, 5

## Abstract
Overfitting negatively impacts the generalization ability of deep neural networks (DNNs) in both natural and adversarial training. Existing methods struggle to consistently address different types of overfitting, typically designing strategies that focus separately on either natural or adversarial patterns. In this work, we adopt a unified perspective by solely focusing on natural patterns to explore different types of overfitting. Specifically, we examine the memorization effect in DNNs and reveal a shared behaviour termed over-memorization, which impairs their generalization capacity. This behaviour manifests as DNNs suddenly becoming high-confidence in predicting certain training patterns and retaining a persistent memory for them. Furthermore, when DNNs over-memorize an adversarial pattern, they tend to simultaneously exhibit high-confidence prediction for the corresponding natural pattern. These findings motivate us to holistically mitigate different types of overfitting by hindering the DNNs from over-memorization training patterns. To this end, we propose a general framework, \emph{Distraction Over-Memorization} (DOM), which explicitly prevents over-memorization by either removing or augmenting the high-confidence natural patterns. Extensive experiments demonstrate the effectiveness of our proposed method in mitigating overfitting across various training paradigms.

\iffalse
The code to reproduce the experiments of this paper can be found at \url{http://www.google.
\fi

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper considers a unified perspective on various overfitting, including NO (natural overfitting), RO (robust overfitting), and CO (catastrophic overfitting). On top of this, the authors discover the "over-memorization" phenomenon that the overfitted model tends to exhibit high confidence in predicting certain training patterns and retaining a persistent memory for them. Unlike previous methods, this paper proposes a general framework called DOM (Distraction Over-Memorization) to alleviate the unified over-fitting issue. Experiments show that the proposed method outperforms other baselines.

### Strengths
1. The discovery of the behavior "over-memorization" unifies different types of overfittings, which is of great help when analyzing the cause of overfitting.
2. The paper is generally well-written, and the motivation is stated clearly.
3. The proposed DOM framework seems promising.

### Weaknesses
1. In the DOM framework, the loss threshold is set with a fixed value. However, with different datasets and loss functions, the optimal threshold could be different. Therefore, the given threshold may not be general on other occasions. The authors should further conduct ablation studies about this and discuss how to overcome this issue. Specifically, the paper should investigate how the performance of the DOM framework varies with different threshold values and provide a justification for choosing a specific threshold. Furthermore, the authors should consider the sensitivity of the framework to the threshold and discuss the possibility of adaptive thresholding based on the training dynamics.
2. The experiment settings are not precisely introduced in 3.1 and 3.2, making these conclusions challenging to reproduce. For example, in section 3.1, the method used to categorize original and transformed high-confidence patterns using an auxiliary model is not clearly specified. The details of the auxiliary model, including its architecture and training procedure, are missing. Similarly, in section 3.2, the criteria for grouping adversarial patterns based on their corresponding natural training loss, and the specific value of the loss threshold used, are not clearly stated. These omissions make it difficult for other researchers to replicate the experiments and verify the findings.
3. In section 3.2, the authors claim, “the AT-trained model never actually encounters natural patterns.” However, methods like TRADES do encounter natural patterns. What will happen in this case? Are the conclusions observed in this paper still applicable? The authors should clarify whether the observed over-memorization phenomenon is specific to models trained without natural patterns, or if it also occurs when natural patterns are part of the training data. If the phenomenon is applicable to TRADES, the authors should provide experimental results to support their claim and discuss the implications of the findings.
4. Why are there many 0.00 in Table 4? The authors need to give more explanation. The table lacks sufficient context and explanation. The authors should provide a detailed explanation of what the 0.00 values represent, and clarify why these values are present in the table. It is essential to provide a clear interpretation of these values to ensure the reader can understand the results and their implications.

### Questions
See above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper provides an empirical investigation into the generalization capabilities of deep neural networks (DNNs), focusing on understanding various facets of overfitting. The authors introduce the concept of over-memorization, a phenomenon where DNNs excessively retain specific training patterns, leading to diminished generalization. To mitigate this issue, the paper suggests techniques such as the removal of high-confidence natural patterns and the application of data augmentation. The effectiveness of these strategies is demonstrated through a series of experiments.

This paper makes a valuable contribution to the field by shedding light on the over-memorization behavior in DNNs and its implications for generalization. By addressing the highlighted areas for improvement, the authors have the potential to further enhance the significance and applicability of their work.

### Strengths
1. Clarity and Structure: The paper is commendable for its well-organized structure and clear exposition. The authors have provided a thorough background and review of related work, successfully setting the stage for their empirical analysis.

2. Robust Experimental Design: The experimental setup is meticulously designed, encompassing various types of overfitting and delving into the over-memorization behavior of DNNs. This comprehensive approach enhances the validity of the findings.

3. Novel Insight into Overfitting: The identification of over-memorization as a common thread linking different types of overfitting is an innovative contribution. This insight adds depth to our understanding of how overfitting impacts the generalization abilities of DNNs.

### Weaknesses
1. Limited Scope of Empirical Analysis: The paper's empirical analysis predominantly focuses on a specific network architecture and dataset. Expanding the analysis to include a wider array of cases or providing a theoretical framework to support the observed behaviors would bolster the generality and impact of the findings. Specifically, the experiments are limited to ResNet architectures and CIFAR-10/100 datasets. This raises concerns about how well the observed over-memorization phenomenon and the proposed mitigation strategies generalize to other architectures, such as transformer networks, and more complex datasets, such as ImageNet. The lack of diversity in experimental settings makes it difficult to ascertain the robustness of the conclusions.

2. Partial Improvement on Overfitting Types: According to the results presented in Tables 2-4, the proposed strategies seem to predominantly ameliorate Class Overfitting (CO), with only marginal improvements on Natural Overfitting (NO) and Random Overfitting (RO). A more detailed exploration of why these discrepancies occur would provide valuable insights. The paper does not delve into the underlying reasons why the proposed methods are more effective at combating class overfitting than other forms of overfitting. This lack of mechanistic understanding limits the potential for targeted improvements of the techniques.

3. Need for Larger-Scale Evaluation: The experiments are confined to relatively simple datasets (CIFAR-10/100) and ResNet-based architectures. Extending the evaluation to encompass larger-scale datasets and alternative architectures, such as transformers, would enhance the representativeness of the results and the applicability of the findings. The reliance on relatively small datasets and standard architectures restricts the generalizability of the findings. The field has moved towards larger datasets and more complex architectures, and the paper needs to demonstrate that the proposed methods are still effective in these more challenging scenarios.

### Questions
1. Expand Empirical Analysis: To strengthen the paper's contributions, the authors should consider conducting additional empirical analyses across diverse network architectures and datasets.

2. Deepen Analysis on Overfitting Types: A more nuanced exploration of the varying impacts on different types of overfitting would provide a richer understanding of the phenomena at play.

3. Consider Larger-Scale and Diverse Architectures: Incorporating experiments with larger datasets and a variety of neural network architectures would ensure that the findings are more widely applicable and representative of the broader deep learning landscape.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a general framework for explicitly preventing over-memorization by either removing or augmenting the high-confidence natural patterns. It is based on the observation that the model suddenly exhibits high confidence in predicting certain training patterns, which subsequently hinders the DNNs’ generalization capabilities.

### Strengths
**Strength:**

-   This paper is overall well-structured and easy to follow.
-   Extensive empirical evaluation with various training paradigms, baselines, datasets, and network architectures demonstrates its effectiveness. Results are reported with the standard deviation.
- Significant performance improvements are demonstrated.

### Weaknesses
 **Weakness**

-   According to Figure 5, the proposed method may require careful hyper-parameter (i.e. loss threshold) selection, which could be a significant drawback. The sensitivity of the method to this threshold is not fully explored, and the optimal value may vary considerably across different datasets and architectures, making it difficult to apply in practice. Specifically, the paper lacks a clear strategy for determining this threshold, and the potential impact of suboptimal values on performance is not well-quantified.
-   The proposed method might result in repeated gradient computation and extensive extra computation. It is also interesting to include a detailed analysis of the introduced extra computation. The paper does not provide a breakdown of the computational cost associated with each step of the proposed method, making it difficult to assess its practical feasibility. For example, the overhead of identifying high-confidence patterns and the subsequent augmentation or removal process should be quantified and compared to the baseline training time. Furthermore, the impact on memory consumption should also be considered.
-   The terminology "pattern" might be confusing and could be further explained. Does it refer to specific samples in datasets? The definition of a "pattern" is not precise, and it is unclear whether it refers to individual training samples, specific features within samples, or something else entirely. This lack of clarity makes it difficult to understand the core mechanism of the proposed method and how it identifies and manipulates these patterns. A more rigorous definition is needed to avoid ambiguity.
-   Lack of results on large-scale datasets. It will be convincing to have some on Tiny-ImageNet or ImageNet. The experimental evaluation is limited to relatively small datasets, and the performance of the proposed method on larger, more complex datasets is unknown. This limits the generalizability of the findings and raises concerns about the scalability of the method to real-world applications. It is crucial to demonstrate the effectiveness of the method on datasets such as Tiny-ImageNet or ImageNet to validate its practical relevance.
-   Lack of results on diverse network backbone architectures beyond ResNets. The evaluation is primarily conducted using ResNet architectures, and it is unclear whether the proposed method is effective on other types of networks, such as Transformers or other CNN architectures. This limits the scope of the findings and raises questions about the robustness of the method across different network architectures. Testing on a wider range of architectures is necessary to establish the general applicability of the method.
-   As discussed in the related works, there are various techniques for mitigating the overfitting issues. Comparisons with other techniques like dropout, ensemble, smoothing, etc. can be helpful. The paper does not adequately compare the proposed method with other established regularization techniques, such as dropout, ensemble methods, label smoothing, or weight decay. This lack of comparison makes it difficult to assess the relative advantages and disadvantages of the proposed method compared to existing approaches. A thorough comparison is needed to understand the unique contributions of the proposed method.

### Questions
Refer to the weakness section.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper analyzes three types of overfitting (natural, robust, and catastrophic) observed during the training process of deep neural networks and introduces methodologies to mitigate these phenomena. The authors are particularly motivated by the observation that, during periods of learning decay of standard training, the training loss for certain datasets sharply decreases. They designate these specific datasets as "transformed data" to differentiate them from the rest. When this transformed data is excluded from training, a reduction in the generalization gap is observed. This trend is similarly noted in settings where both robust and catastrophic overfitting are evident. Drawing from these observations, it is inferred that the transformed data might be excessively memorized, leading to overfitting. To counteract this, the authors propose the "distraction over memorization (DOM)" methodology, which emphasizes data augmentation specifically for the transformed data. Experimental results suggest that models trained using this approach exhibit a superior generalization gap compared to those trained with data augmentation applied across the entire dataset.

### Strengths
The paper demonstrates that natural overfitting can be mitigated by removing data characterized by a rapid decrease in training loss, termed "transformed data." Through this analysis, the authors highlight the occurrence of overfitting in standard settings due to such data and propose a method to distinguish data that has been excessively memorized. Furthermore, the properties of transformed data are not limited to natural overfitting; they exhibit similar trends in other types of overfitting, namely robust and catastrophic overfitting. The authors suggest a universal overfitting mitigation method by applying various data augmentation techniques to the transformed data. Experimental results are presented to validate the efficacy of this approach.

### Weaknesses
The motivation behind this paper, specifically the analysis of transformed data, has already been explored in a paper that introduced the MLCAT methodology [1]. The distinction is that the previous study limited its analysis to robust overfitting, whereas the current paper expands the analysis to three types of overfitting, demonstrating that these phenomena manifest commonly across all three. However, given that there isn't much difference in the learning algorithms or model structures between the standard, adversarial, and fast adversarial settings, one could easily anticipate that the characteristics of transformed data in the adversarial setting, as delineated in MLCAT [1], would manifest similarly in both the standard and fast adversarial settings. Therefore, the current analysis does not offer much novelty beyond the findings of the previous study. While the proposed methodology of applying data augmentation specifically to transformed data does have the advantage of being universally applicable to various types of overfitting, it only demonstrates an improved generalization gap in comparison to the baseline model. Given the inherent differences in training data for the standard, adversarial, and fast adversarial settings, one might question the necessity of a universally applicable overfitting mitigation method. To bolster this claim, the authors should compare the proposed method against methodologies in individual overfitting studies (natural, robust, catastrophic) and demonstrate that their approach offers competitive performance.

### Questions
- When compared to the analysis performed in the previously cited study (MLCAT) mentioned under weaknesses, are there notable strengths in this paper that I might have missed, aside from the observation that similar phenomena manifest across standard, adversarial, and fast adversarial settings?
- In the "distraction over memorization" methodology, is there a specific reason for applying data augmentation iteratively rather than in a straightforward manner?
- Has the study investigated whether similar phenomena occur with learning rate scheduling methods that decrease at a more gradual pace, such as cosine, as opposed to the step learning decay?
- Are there any experimental results comparing the proposed approach to traditional methodologies under the same settings?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
