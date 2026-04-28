# Imprecise Label Learning: A Unified Framework for Learning with Various Imprecise Label Configurations

- Decision: Reject
- Avg Score: 6.00
- Scores: 5, 6, 5, 8

## Abstract
Learning with reduced labeling standards, such as noisy label, partial label, and supplementary unlabeled data, which we generically refer to as \textit{imprecise} label, is a commonplace challenge in machine learning tasks. 
Previous methods tend to propose specific designs for every emerging imprecise label configuration, which is usually unsustainable when multiple configurations of imprecision coexist. 
In this paper, we introduce imprecise label learning (ILL), a framework for the unification of learning with various imprecise label configurations.
ILL leverages expectation-maximization (EM) for modeling the imprecise label information, treating the precise labels as latent variables.
Instead of approximating the correct labels for training, it considers the entire distribution of all possible labeling entailed by the imprecise information.
We demonstrate that ILL can seamlessly adapt to partial label learning, semi-supervised learning, noisy label learning, and, more importantly, a mixture of these settings, with closed-form learning objectives derived from the unified EM modeling.
Notably, ILL surpasses the existing specified techniques for handling imprecise labels, marking the first practical and unified framework with robust and effective performance across various challenging settings.
We hope our work will inspire further research on this topic, unleashing the full potential of ILL in wider scenarios where precise labels are expensive and complicated to obtain.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The author proposes a new general framework for learning with imperfect labeling information in the multi-class classification setting, called the Imprecise Label Learning (ILL) framework. The framework works in an expectation-maximization fashion and assumes that imperfect label information I is provided among instance X, while the Y is a latent variable. The author shows how to adopt a general form of ILL framework to different previously considered settings with imperfect information: Partial label learning (PLL), Semi-supervised learning (SSL), Noisy label learning (NLL), and mixed configuration (in the appendix) and compare them against many popular baselines that focus on specific configurations on many configurations of artificial benchmarks created using CIFAR-10/100 and additional datasets (and even more experiments with different settings is provided in the appendix). The proposed framework achieves strong results, often beating all the baselines in the comparison.

### Strengths
1. The paper has strong motivation, creating a unified framework for imprecise labels in multi-class classification that can handle different settings of imperfect label information.
2. The general framework is nicely rooted in EM.
3. The proposed framework achieves strong results in empirical comparison. 
4. The empirical comparison includes many different settings, and for each setting, the proposed method is compared with a large number of SOTA baselines.

### Weaknesses
1. The work gives a general framework outline in the main paper and focuses on the loss functions used for different settings (PPL, SSL, NLL),
But I'm missing the important pieces to get a full picture of the proposed approach, it seems to me more like the outline than a concrete solution that can be implemented in different ways (what authors mention In the paper). Unfortunately, the main paper is very sparse in details about the actual implementation of many of its elements.

2. More details can be found in Appendix C and D. It is unclear to me when NFA from Appendix C.3 is used in the main paper or not. In Appendix D, all modifications to the training are mentioned without explanation and motivation.

3. NIT: Broken reference

   > However, our framework is much simpler and more concise as shown in ??

### Questions
In some experiments, the fully supervised model (with correct label information) gets worse results than the ILL framework. Actually, ILL beats the fully supervised model by a lot. At the same time, other solutions never do that, so the natural question is if there are any other differences between the supervised model and ILL, then application of EM/different loss? What is the authors' hypothesis as to why it achieves better performance?

### Soundness
3 good

### Presentation
2 fair

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
This paper proposes a unified framework for handling various learning problems with imprecise label configurations. Previous studies have achieved success in dealing with imprecise configurations of individual labels, but their methods often have significant differences. These methods are tailored to specific forms of imprecise labels, but in practical applications, annotations can be very complex and may involve multiple coexisting imprecise label configurations. Therefore, applying previous methods to situations where both noisy labels and partial labels occur simultaneously can be challenging. To address this problem, the author presents a different perspective, considering the provided imprecise label information as information that imposes deterministic or statistical constraints on the actual applicable true labels. Then, the model is trained to maximize the probability of the given imprecise information. The author demonstrates the advanced performance of their method through comparative experiments on multiple datasets, showcasing the adaptability of the ILL framework in handling a mixture of various uncertain label configurations.

### Strengths
1. The paper proposes a unified framework called imprecise label learning (ILL) for handling various configurations of imprecise labels. Compared to previous methods, this framework does not require specific designs for each imprecise label configuration. Instead, it models the imprecise label information using Expectation Maximization (EM) and treats precise labels as latent variables. This unified framework can adapt to settings involving partial label learning, semi-supervised learning, noise label learning, and their combinations, demonstrating strong adaptability and flexibility.

2. Through experiments, it has been demonstrated that ILL outperforms existing specific techniques in handling imprecise labels. It achieves robust and effective performance in various challenging settings, including partial label learning, semi-supervised learning, noise label learning, and their combinations. This indicates that the framework possesses excellent performance and wide applicability in handling imprecise labels.

3. The work presented in this paper provides insights for further research in the field of imprecise label learning, unleashing the full potential of imprecise label learning in more complex and challenging scenarios where obtaining precise labels is difficult. This has significant implications for solving real-world problems with inaccurate labels.

### Weaknesses
The author proposes a new framework for unified learning with imprecise labels, which can learn from any type of imprecise label. However, the experimental data in the current article are obtained from balanced and relatively small datasets, lacking sufficient experimental evaluation. Specifically, the datasets used do not adequately represent the complexities of real-world scenarios where class imbalances and long-tail distributions are common. The absence of experiments on larger, more challenging datasets limits the conclusions that can be drawn about the method's practical applicability. At the same time, the article does not discuss the computational complexity or scalability of this framework. Although the article mentions the limitations of some previous methods in dealing with specific forms of imprecise labels, it does not provide a detailed discussion on the scalability of this framework in large-scale datasets or complex scenarios, such as those with high dimensionality or a large number of classes. This raises concerns about its feasibility for real-world applications.

Moreover, in terms of the presentation of the paper, the author's description of existing methods is not clear enough. The paper uses a large number of formulas and tables for description, lacking visual explanations. For instance, the specific differences between the various imprecise label learning methods are not intuitively explained, making it difficult for the reader to grasp the novelty of the proposed approach. The comparison of the experimental results also appears vague and unclear. The lack of clear visualizations, such as plots showing the performance of the proposed method compared to baselines across different datasets and metrics, makes it challenging to assess the significance of the reported improvements.

### Questions
The author proposed a unified framework based on imprecise label learning, demonstrated through experiments the good performance of the unified framework in three different imprecise label scenarios, and its superiority in mixed imprecise label learning tasks compared to current methods capable of handling mixed imprecise labels. The main significance of the unified framework lies in providing a portable and scalable method for addressing various imprecise label tasks, where the use of EM to uniformly model imprecise label information can be extended to multiple scenarios. However, challenges such as potential local optima and computational complexity in the EM method still need to be addressed.

Furthermore, the author noted in the conclusion that experimental data were obtained from relatively small and balanced datasets and that designing different loss functions according to different scenarios was necessary when designing the model. This further limits the portability of this framework. In particular, the handling of probabilistic models for various imprecise label information has a significant impact on the effectiveness of the method, and we must reconsider model design solutions when dealing with different data and tasks.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The article addresses the challenge of learning with imprecise labels in machine learning tasks, such as noisy or partial labels. Traditional methods often struggle with multiple forms of label imprecision. The authors introduce a novel framework named Imprecise Label Learning (ILL) that serves as a unified approach to handle various imprecise label scenarios. ILL employs the expectation-maximization (EM) technique, viewing precise labels as latent variables and focusing on the entire potential label distribution. The framework demonstrates adaptability to different learning setups, including partial label learning and noisy label learning. Remarkably, ILL outperforms existing techniques designed for imprecise labels, establishing itself as the first integrated approach for such challenges.

### Strengths
1. The article offers a comprehensive solution to the prevalent challenge of imprecise annotations, enhancing the adaptability and applicability of machine learning models.
2. The inclusion of experimental results across multiple settings provides empirical evidence of the framework's robustness and superior performance.

### Weaknesses
1. The article's innovation is limited, as the approach of considering ground-truth labels or Bayes label distribution as latent variables and using variational inference for approximation in weakly supervised learning is already a common method[1-2], which suggests that the presented techniques may not be as novel as claimed.

   [1] Xu, N., Qiao, C., Geng, X., & Zhang, M. L. (2021). Instance-dependent partial label learning. Advances in Neural Information Processing Systems, 34, 27119-27130. 

   [2] Yao, Y., Liu, T., Gong, M., Han, B., Niu, G., & Zhang, K. (2021). Instance-dependent label-noise learning under a structural causal model. Advances in Neural Information Processing Systems, 34, 4409-4420.

2. The article's treatment in section 3.2, where "P(S|X, Y ; θ) reduces to P(S|Y )," does not hold true under the instance-dependent PLL setting. When considering that the generation process of candidate labels in conjunction with S is feature-dependent[1,2], the simplification presented in the article may not be universally applicable and may overlook specific nuances associated with instance-dependent partial label learning.

   [1] Xu, N., Qiao, C., Geng, X., & Zhang, M. L. (2021). Instance-dependent partial label learning. Advances in Neural Information Processing Systems, 34, 27119-27130. 

   [2] Xu, N., Liu, B., Lv, J., Qiao, C., & Geng, X. (2023). Progressive purification for instance-dependent partial label learning. In International Conference on Machine Learning (pp. 38551-38565). PMLR.

3. Some important baselines should be compared, such as [1] in PLL and [2,3] in NLL.

   [1] Wu, Dong-Dong, et al. "Revisiting consistency regularization for deep partial label learning." International Conference on Machine Learning. PMLR, 2022.

   [2] Jiang, Lu, et al. "Mentornet: Learning data-driven curriculum for very deep neural networks on corrupted labels." International conference on machine learning. PMLR, 2018.

   [3] Han, Bo, et al. "Co-teaching: Robust training of deep neural networks with extremely noisy labels." Advances in neural information processing systems 31 (2018).

4. The article lacks detailed exposition on the derivation process of the loss functions for the three imprecise annotations configurations stemming from equation 5, potentially leaving readers without a clear understanding of the underlying methodology.

5. The article contains typographical errors in the last sentence of the 2-nd paragraph on page 6, "However, our framework is much simpler and more concise as shown in **??**."

### Questions
1. Could the authors provide a more comprehensive derivation of the loss functions for the three imprecise annotations configurations derived from equation 5 to ensure clarity and thorough understanding for the readers?

2. Given that the method of using ground-truth labels or Bayes label distribution as latent variables coupled with variational inference in weakly supervised learning is highlighted in prior works, how does the presented framework distinguish itself or advance beyond these existing approaches in terms of innovation or application?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a unified framework for multiple weakly supervised learning settings, including noisy label, partial label, and multiple label candidates. The unified framework can be described in a formulation shown in Eq5, and multiple learning problems can be solved under the framework. The proposed framework shows good performance on all those problems.

### Strengths
The exploration of multiple learning problem settings involving imprecise labels holds significant importance for researchers. It is intriguing to observe the presentation of a unified perspective on these diverse problems.

The unified framework is sound and effective. 

The proposed method shows good performance on multiple learning settings. The experiments on the performance comparison are complete and convincing. Most of recent SOTA methods are included as baselines.

### Weaknesses
1. It is good to see the proposed method can be seamlessly combined with the data augmentation techniques, but it would be helpful to examine the model's performance without data augmentation techniques. It seems that the method's performance is sensitive to the quality of data augmentation, but not all kinds of tasks can be easily benefit from data augmentation. An ablation study would be helpful.

2. There are also some other related works on unifying multiple problem settings of weakly/imprecise supervised learning. Some discussions on this topic can improve this paper. For example,
[1] Centroid Estimation With Guaranteed Efficiency: A General Framework for Weakly Supervised Learning, TPAMI
[2] Weakly Supervised AUC Optimization: A Unified Partial AUC Approach, arxiv 2305.14258


3. The presentation can be further improved. There are typos and errors in the paper, e.g., missing punctuations, broken cross references to the figures, etc.

### Questions
See above.

### Soundness
3 good

### Presentation
3 good

### Contribution
1 poor
