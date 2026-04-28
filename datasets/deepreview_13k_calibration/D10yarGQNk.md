# Efficient and Context-Aware Label Propagation for Zero-/Few-Shot Training-Free Adaptation of Vision-Language Model

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 6, 8

## Abstract
Vision-language models (VLMs) have revolutionized machine learning by leveraging large pre-trained models to tackle various downstream tasks. Despite improvements in label, training, and data efficiency, many state-of-the-art VLMs still require task-specific hyperparameter tuning and fail to fully exploit test samples. To overcome these challenges, we propose a graph-based approach for label-efficient adaptation and inference. Our method dynamically constructs a graph over text prompts, few-shot examples, and test samples, using label propagation for inference without task-specific tuning. Unlike existing zero-shot label propagation techniques, our approach requires no additional unlabeled support set and effectively leverages the test sample manifold through dynamic graph expansion. We further introduce a context-aware feature re-weighting mechanism to improve task adaptation accuracy. Additionally, our method supports efficient graph expansion, enabling real-time inductive inference. Extensive evaluations on downstream tasks, such as fine-grained categorization and out-of-distribution generalization, demonstrate the effectiveness of our approach.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes ECALP, a novel graph-based framework for training-free adaptation of vision-language models. The proposed method constructs a graph over text prototypes, optional training samples and testing samples in a simple, dynamic fashion, and adopts label propagation for inference. Furthermore, edge re-weighting is carefully designed to take into account the semantic context of different classes. Throughout training and inference, the framework introduces little augmentation and hyper-parameter search, showing its efficiency and practicality. Finally, comprehensive experimental results over a wide range of datasets on zero-shot/few-shot fine-grained classification, style-transfer and out-of-distribution detection tasks show significant improvement in performance of the proposed approach over previous methods.

### Strengths
1. Comprehensive experiments and great results:

The paper provides a comprehensive comparison of ECALP against a number of highly competitive prior works, and carried out experiments on a variety of datasets as well as visual tasks, which is sufficient to validate the approach. The empirical results clearly demonstrate that ECALP achieves significantly better performance than previous methods. The experimental design, including the main setting, comparison baselines as well as ablation studies, are well justified. Moreover, the method proves to be computationally efficient.

2. Nice presentation and clear structure

The figures in this paper are well-designed and effectively highlight the pipeline as well as advantages of the proposed framework. The formulation, presentation of the results as well as the visuals are aesthetically pleasing and easy to follow.

3. Clear motivation and good writing

The introduction and abstract are well written and lays a good foundation for the paper. It is easy to see the motivation behind the work.

### Weaknesses
1. In Figure 1, the inputs to the second image encoder and the text encoder seem to be mixed up. 

2. As is discussed in the paper, ECALP builds upon similar ideas with ZLaP (i.e. label propagation), and although I acknowledge that the proposed method achieves improvement in performance and eliminates the need for additional unlabelled datasets, the contribution seems somewhat limited.

3. In the detailed few-shot results provided in the appendix, it seems that ECALP does not always achieve the best performance. Especially on datasets like OxfordPets and Food101, the accuracy of ECALP even goes down as the number of samples per class increases. This weakens the claim of ECALP’s robustness in low-shot scenarios.

### Questions
1. As is mentioned above, I wonder if the authors could offer some explanation on ECALP’s behavior on certain datasets in low-shot settings.

2. In the ablation study, in Table 4, it’s interesting to see that without Text Reweight, the model achieves slightly better performance under the 16-shot setting on ImageNet. It would be nice if the authors could shed some light on this phenomenon.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a graph-based approach for label-efficient adaptation and inference. The method dynamically constructs a graph based on available samples to enable real-time inductive inference.

### Strengths
1. The method requires no additional unlabeled support set and effectively leverages the test sample manifold through dynamic graph expansion.
2. This paper is clear and easy to follow.
3. This paper conducts extensive evaluations on diverse downstream tasks.

### Weaknesses
1. Compared to the SOTA methods, the performance improvement seems limited. Additionally, the second-highest performance can be highlighted with an underline for clarity.
2. In the computational efficiency section, does the testing time for ECALP include the dynamic graph construction process, or does it only account for the label propagation time?

### Questions
1. It appears that ECALP requires additional storage. How does its CUDA memory compare to that of previous methods?
2. If the initial testing samples are used to create an incorrect adjacency graph, will this lead to a cumulative error?
3. In corrupted downstream tasks, is ECALP still effective when the severity is low (e.g., at level 1)?
4. Is the method sensitive to the label propagation iterations T?

### Soundness
3

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
The paper proposes a approach for adapting vision-language models (VLMs) using efficient, context-aware label propagation. It introduces dynamic graph construction to improve inference accuracy without task-specific tuning, and employs context-aware feature re-weighting for better task adaptation. The method demonstrates superior performance and efficiency across various downstream tasks, highlighting its potential in zero-/few-shot scenarios.

### Strengths
1. The introduction of dynamic graph expansion is innovative, allowing for real-time adaptation and efficient use of test samples. 
2. The method enhances feature relevance by re-weighting based on context, which is a novel approach to improving model adaptability to downstream tasks. This can potentially lead to better performance in diverse scenarios.
3. Employing an iterative solution rather than a closed-form one reduces computational costs and enhances scalability. This is particularly beneficial for handling large datasets.

### Weaknesses
1. More detailed motivation behind the model design is preferred. It is important to explain why the authors propose the method in this work.

2. The method may be complex to implement, particularly for large-scale or varied tasks. Detailed guidelines for implementation would be beneficial.

3. The approach assumes that the context-aware feature re-weighting will generalize well across different tasks, but this might not hold true for all types of data or in cases with significant domain shifts.

### Questions
Please refer to the weakness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper proposes graph-based efficient adaption and inference for vision-language models. Specifically, the paper maximizes the use of test samples through iterative label propagation without the need for task-specific tuning. Additionally, the paper introduces a novel method to mitigate biases in VLMs through context-aware re-weighting and a interesting approach for identifying KNNs within each modality. Extensive experiments on various downstream tasks demonstrate the effectiveness of the proposed graph-based method.

### Strengths
1. The proposed use of K-nearest neighbors within each modality and context-aware edge re-weighting are novel approaches that align well with the property of pre-trained VLMs.
2. The paper is well-written and easy to understand.
3. Extensive experiments were fairly conducted with recent baselines across a range of datasets and architectures. 
4. The paper improves the feasibility of the proposed method by using dynamic graph expansion, supported by a practical analysis of wall-clock time in Table 6 and time complexity in Appendix A.1.

### Weaknesses
I think the paper has no significant weaknesses.
1. Evaluating the performance degradation when using one-step label propagation instead of iterative label propagation could provide valuable insights for practitioners. This analysis would shed light on the trade-off between reduced complexity and potential accuracy decline, assisting in making informed decisions for applications where computational efficiency is crucial.
2. When utilizing an additional 16-shot training samples in Table 2, it appears that ECALP uses the training data as a component of the graph rather than for training. Wouldn’t it be possible to apply ECALP in addition to traditional prompt learning methods such as CoOp and CoCoOp?

### Questions
1. In Figure 1, it seems that the second image encoder and text encoder should be switched.
2. In Line 161, how can we obtain multiple textual prompts $z_{cm}$ for the $c$-th class? It seems that the value of $M$ can vary from class to class.

### Soundness
4

### Presentation
4

### Contribution
4
