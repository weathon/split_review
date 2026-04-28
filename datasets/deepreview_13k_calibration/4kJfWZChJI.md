# Generalization or Specificity? Spectral Meta Estimation and Ensemble (SMEE) with Domain-specific Experts

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 5, 1, 8

## Abstract
Existing domain generalization (DG) methodologies strive to construct a unified model trained on diverse source domains, with the goal of achieving robust performance on any unseen test domain. However, in practice, not all source domains contribute equally to effective knowledge transfer for a specific test domain. Consequently, the reliability of single-model generalization often falls short of classic empirical risk minimization (ERM). This paper departs from the conventional approaches and advocates for a paradigm that prioritizes specificity over broad generalization. We propose the Spectral Meta Estimation and Ensemble (SMEE) approach, which capitalizes on domain-specific expert models and leverages unsupervised ensemble learning to construct a weighted ensemble for test samples. Our comprehensive investigation reveals three key insights: (1) The proposed meta performance estimation strategy for model selection within the sources plays a pivotal role in accommodating stochasticity; (2) The proposed spectral unsupervised ensemble method for transferability estimation excels in constructing robust learners for multi-class classification tasks, while being entirely hyperparameter-free; and (3) Multi-expert test-time transferability estimation and ensemble proves to be a promising alternative to the prevailing single-model DG paradigm. Experiments conducted on the DomainBed benchmark substantiate the superiority of our approach, consistently surpassing state-of-the-art DG techniques. Importantly, our approach offers a noteworthy performance enhancement while maintaining remarkable computational efficiency, executing in mere milliseconds per test sample during inference.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper tackles domain generalization (DG) aiming to construct a uniﬁed model trained on diverse source domains, with the goal of achieving robust performance on any unseen test domain.  This paper proposes using individual ERM models for each source and aggregating their predictions during the test phase, by a meta performance estimation technique for model selection within the sources. Furthermore, an approach based on spectral unsupervised ensemble learning to assess the transferability of each source model to test samples is proposed.

### Strengths
+ Observation and Motivation: the finding is quite important, and the motivation is quite clear by showing Figure 2 and Figure 3: the transferability of any source domain remains unpredictable without access to the speciﬁc test domain information, leading to the inherent instability witnessed in current DG approaches. The solution is to use domain-speciﬁc experts to prioritize speciﬁcity over generalization. 
+ Methodology: the introduction of a spectral ensemble for source models is both innovative and practical, effectively enhancing the robustness of the DG framework. This approach incurs the additional task of recalculating the covariance matrix with cumulative test set data, but the trade-off is well justified by the benefits.
+ Presentation: the clarity and precision of the writing, complemented by well-crafted figures, make the content not only accessible but also engaging. The overall presentation is of high quality, effectively conveying complex concepts in a coherent manner.
+ Experiments: the experimental design is thorough and multifaceted, convincingly demonstrating the efficacy of the proposed method from the following perspectives: 1) meta model selection before ensemble 2) domainbed benchmark 3) test-time ensemble 4) test-time transferability estimation. The performance is outstanding.

### Weaknesses
 - Computation Complexity: while the proposed spectral ensemble-based method offers the advantage of being applicable in online incremental settings without the need for re-training, adaptation, or iterative optimization, it still presents certain limitations. Specifically, the need to recalculate the covariance matrix and compute the Singular Value Decomposition (SVD) may result in lower computational efficiency compared to other Domain Generalization (DG) methods that do not require any post-hoc computations, such as MIRO and Fishr. This increased computational overhead could potentially slow down inference speed, posing a challenge for deploying the model in real-world scenarios. The computational cost of recalculating the covariance matrix and performing SVD scales with the number of test samples and the number of classes, which could become prohibitive for large datasets with many classes. For instance, in a scenario with a large number of classes, the size of the covariance matrix would be substantial, leading to a significant increase in computation time for each test sample. This is especially concerning in online settings where real-time inference is crucial.



### Questions
1. Refer the weakness, I am wondering the actual inference time for each target sample compared with the baselines (MIRO and Fishr). 
2. In Algorithm 1, M is the number of total models been kept after meta ranking, However, for meta estimation, “for i = 1 : S” means for each source domain, “Rank and select the best performing M models”. Does it mean each source domain will have M best performing models, so the total number of models becomes S*M. It is confusing here, because M is the predictors are available to make predictions on test samples (Sec 3.2). Could you please clarify the number of models chosen from each source domain, and explain how to get M in both Algorithm 1 and Section 3.3?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the problem of domain generalization. The proposed method employs domain-specific expert models and leverages un- supervised ensemble learning to create a combination of these experts for better predictions. Experiments are performed on the DomainBed benchmark to show the effectiveness of the proposed method in terms of accuracy and inference efficiency.

### Strengths
- The paper introduces an interesting approach to tackle the domain generalization challenge, utilizing an unsupervised ensemble learning technique that improves model selection, with an emphasis on elevating specificity over generalization

- This paper is generally well-structured and easy to follow.

### Weaknesses
 - The novelty of this paper is somewhat limited, since both mixture-of-experts or spectral meta-learner is not new in this area.

- Some important references are missing, e.g., 
   + [1] Sparse Mixture-of-Experts are Domain Generalizable Learners, ICLR2023.
   + [2] Learning mixture of domain-specific experts via disentangled factors for autonomous driving, AAAI2022
   + [3] Generalizable person re-identification with relevance-aware mixture of experts, CVPR2021

### Questions
See weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
In contrast with the conventional single-model domain generalization framework, the paper proposes an alternative perspective that the knowledge of the unseen target domain is transferred from multiple source domains. Specifically, the prediction of unseen target data is an aggregate of the predictions from each individual source domain model, and a spectral unsupervised ensembling method is used to determine the contribution of each source model to the target. To further facilitate the selection of source models, the paper proposes a meta performance estimation technique that aims to filter out the underperformed models within the ensemble. The proposed method's effectiveness is validated across multiple benchmark datasets.

### Strengths
* The paper extends the Spectral Meta-Learner (SML) unsupervised ensemble learning approach from binary to multi-class classification as a way to aggregate the knowledge from multi-source domain models to the unseen target domain.

### Weaknesses
 * The research lacks novelty in its claim. The problem addressed in this paper, namely Test-time adaptation for Distribution shifts, was comprehensively discussed in [1]. Furthermore, the approach of aggregating knowledge from multiple source domains to an unseen target domain, often using techniques like Mixture-of-Experts or ensemble, is not a novel concept either [2, 3]

* Conceptually, the research presented in this paper bears a significant resemblance to [3]. Both works utilize a similar approach, pretraining individual models on multiple source domains using ERM and subsequently transferring the knowledge from this ensemble (akin to a mixture of experts) to the target domain. Additionally, while the authors introduce a complex method named ' multi-class SML' to determine the aggregation of predictions from the source models, [3] employs a more straightforward, learnable transformer encoder for the same purpose, with parameters learned through meta-learning. Notably, this paper omits citations and comparisons to [3].
 
* The paper lacks a comprehensive 'related work' section, leading to the omission of some pivotal prior research. For instance, meta-learning, a critical concept for addressing domain generalization, was introduced in [4]. Given that "meta" appears in the paper's title, the authors should clarify how this concept ties into their proposed method, using standard terminology such as 'support' and 'query' sets. Additionally, it would be beneficial for the authors to draw comparisons between their work and other studies that have also employed meta-learning for domain generalization.

### Questions
* Please make a comparison with [3] and identify the differences in detail. At the conceptual level, they are the same. Specifically, they both model source domain knowledge using the ensemble of models and softly determine the contribution of each source domain to the target. At the technical level, the paper proposes a different method to aggregate the source knowledge in the ensemble with an additional  "meta-performance estimation" to select the source models within the ensemble. 

* Please clarify how the concept of "meta" relates to the proposed approach. Is it the same with "meta-learning"? If yes, please explain what are the support set and query set. What is the meta-knowledge is learned during meta-training?

* Please provide more explanation of the design of "Meta model selection", especially from the perspective of intuition. It is a little bit confusing with what is described in the paper "In this way, the instability of stochastic optimization can be accommodated,"

* Please add a related work section.

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper points out limitations in existing multi-source domain generalization methods, which struggle to generalize by training a model with diverse source domains. The authors propose a new technique for effectively filtering and ensembling individual expert models. Specifically, they introduce an unsupervised spectral ensemble approach, expanding on the Spectral Meta-Learner by using a one-vs-rest paradigm for multi-class classification. This proposed method significantly outperforms traditional single model approaches and even surpasses self-ensembling and multiple model ensemble techniques.

### Strengths
- The paper boasts high-quality writing that is very readable. It provides detailed comparisons with existing methods. Especially commendable is the clarity and precision in potentially challenging statements.

- The proposed method is both intuitive and powerful, and the paper thoroughly describes the underlying assumptions and preliminaries supporting its feasibility.

- In a multi-source domain generalization setting, the proposed approach notably surpasses not only the performance of a single model but also that of self-ensembling and multi-model ensemble methods.

### Weaknesses
The paper should compare the computational overhead of the proposed spectral meta estimation with other ensemble methods. Even if a direct measurement of all test times isn't possible, including a discussion on computational complexity would be beneficial. Without such comparisons or analyses, it's hard to gauge the practicality of the proposed method. Specifically, the paper lacks a detailed analysis of how the spectral meta-learning scales with the number of experts, the size of the input data, and the number of classes. The computational cost of the SVD operation, which is central to the method, should be discussed in relation to these factors. Furthermore, the paper does not address the memory requirements of storing the covariance matrix, which could be a limiting factor for large datasets or a high number of classes. A discussion of the practical limitations of the method in terms of both computational time and memory usage is essential.

### Questions
There is no question.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent
