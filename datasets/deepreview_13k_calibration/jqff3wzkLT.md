# Variance-Covariance Regularization Improves Representation Learning

- Decision: Reject
- Avg Score: 4.33
- Scores: 5, 5, 3

## Abstract
Transfer learning plays a key role in advancing machine learning models, yet conventional supervised pretraining often undermines feature transferability by prioritizing features that minimize the pretraining loss. In this work, we adapt a self-supervised learning regularization technique from the VICReg method to supervised learning contexts, introducing Variance-Covariance Regularization (VCReg). This adaptation encourages the network to learn  high-variance, low-covariance representations, promoting learning more diverse features. We outline best practices for an efficient implementation of our framework, including applying it to the intermediate representations. Through extensive empirical evaluation, we demonstrate that our method significantly enhances transfer learning for images and videos, achieving state-of-the-art performance across numerous tasks and datasets. VCReg also improves performance in scenarios like long-tail learning and hierarchical classification. Additionally, we show its effectiveness may stem from its success in addressing challenges like gradient starvation and neural collapse. In summary, VCReg offers a universally applicable regularization framework that significantly advances transfer learning and highlights the connection between gradient starvation, neural collapse, and feature transferability.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces Variance-Covariance Regularization (VCReg), adaptation of VICReg designed for supervised learning. By focusing on high-variance, low-covariance representations, VCReg targets improved feature transferability and robustness, specifically addressing issues like gradient starvation and neural collapse which are prevalent in supervised pretraining for transfer learning. The authors apply VCReg not only to final representations but also to intermediate layers, achieving performance improvements across image and video-based transfer learning tasks, class-imbalanced datasets, and hierarchical classification.

### Strengths
1. VCReg repurpose the variance and covariance components of VICReg for supervised settings, intent to make transfer learning without dependance on invariance
2. Improvements are shown when using supervised pretraining on ImageNet and then transferring to other datasets so empirical evidence of presented task/scenarios is largely convincing.
3. presentation of this paper is well-structured with clarity.

### Weaknesses
1. VICReg's regularization easily integrates with other SSL methods like SimCLR since it operates on dimensions across the batch without interfering with contrastive losses so it should ideally can be integration with SSL and supervised losses also. So Why I see VCReg as an special case of VICReg applied on supervised setting rather than novel approach.
2. Invariance component is removed to streamline VCReg for supervised tasks however this could reduce robustness to data variations. Without the invariance regularization, I am curious about VCReg generalization capabilities in scenarios like distribution shift. To counter the question, empirical evidence should justify that.
3. Application of VCReg across intermediate layers, along with its specialized backward-pass gradient adjustments, adds substantial computational overhead and results in Appendix A does not justify it entirely.  
4. Results on combining the VCReg with SSL methods in Table 4 is interesting. Focusing on ImageNet results- How to justify that with SimCLR + VCReg doesn't help however It improves performance when VCReg added with VICReg (VICReg having invariance component). Need to understand reason.
5. Could the authors elaborate on how VCReg specifically addresses generalization in context of connection between gradient starvation and transfer learning?

### Questions
Please refer weakness section and I am waiting to get response on it.

### Soundness
2

### Presentation
3

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
This paper proposes VarianceCovariance Regularization (VCReg), a method designed to encourage learning representations with high variance and low covariance. Rather than applying VCReg only to the network’s final representation, the authors integrate it into intermediate layers, leveraging an efficient implementation to ensure minimal computational overhead and enable easy integration into existing workflows. The paper presents extensive experiments on multiple tasks, demonstrating VCReg’s effectiveness across various network architectures.

### Strengths
1.The authors perform extensive experiments across multiple tasks, showcasing the effectiveness of VCReg in diverse settings, including transfer learning for images and videos, long-tailed learning, self-supervised learning, and hierarchical classification.
2.The benefits of VCReg are explored thoroughly in Section 5 empirically, which is both interesting and convincing.

### Weaknesses
1.The paper lacks a theoretical explanation for how VCReg improves generalization. For instance, can the authors provide a theoretical analysis of VCReg’s impact on the decision boundary or expected risk? A theoretical grounding would clarify VCReg’s influence on generalization and strengthen the methodology. Relevant references for further grounding could include:
- Empirical Bernstein Bounds and Sample Variance Penalization by Maurer et al., 2009
- Variance-based Regularization with Convex Objectives by Namkoong et al., 2017
- Feature Variance Regularization: A Simple Way to Improve the Generalizability of Neural Networks by Ranran et al., 2020
- PAC-Bayes-Empirical-Bernstein Inequality by Tolstikhin et al., 2013

2. The description in Section 3.2 could be clearer, particularly regarding spatial dimensions and covariance calculations. Is covariance calculated for each feature dimension, and if so, why do spatial dimensions influence the results? Providing explicit equations would enhance clarity and improve the understanding.

2. Minor typos: in line 076, suppresses -> surpasses.

### Questions
Please refer to the weakness.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes to adapt regularization components (variance, covariance) from the VICReg to supervised learning contexts, which aims to encourages the network to learn high-variance, low covariance representations, promoting learning more diverse features. The authors focus on an efficient implementation of VCReg and conduct experiments to show its effectiveness in transfer learning.

### Strengths
1. Writing and motivation are generally clear.
2. The proposed VCReg makes sense as whitening technique has been proved to enhance feature diversity in SL.
3. Extensive experiments are conducted to verify VCReg’s performance in transfer Learning.

### Weaknesses
1. **Lack of novelty and practicality.**
- Firstly, most SSL methods, such as VICReg, DINO and so on, have been verified to significantly outperform supervised learning on downstream transfer learning tasks. No matter what components are added, SL consistently focuses on matching label information. Therefore, in contemporary machine learning, SL is more commonly used for fine-tuning specific tasks rather than serving as a pretraining method for obtaining general-purpose representations. If the proposed SL+VCReg can outperform current self-supervised learning methods on downstream tasks, in my view, that would truly represent both novelty and practicality. I suggest that the authors conduct direct comparisons between their SL+VCReg method and leading SSL approaches on downstream transfer learning tasks. This would provide a clearer picture of where the proposed method stands in relation to current best practices.

- Secondly, the author proposes adding regularization components to multiple intermediate layers of the neural network. Although the runtime of each component is similar to that of batch normalization (BN), it still introduces additional computational overhead. Moreover, based on the experimental setup, selecting the coefficients $\alpha$ and $\beta$ for the two regularization components across different network architectures is challenging and requires significant cost. However, despite these additional burdens, the performance improvement is not particularly remarkable. These issues make it difficult for this method to have strong prospects in practical applications. The authors should discuss potential strategies for efficiently selecting the $\alpha$ and $\beta$ coefficients, such as automated hyperparameter optimization techniques. This would help readers better understand the practical implications of implementing VCReg.

2. **Some aspects of the method's setup are unclear and lack intuitive analysis.** Specifically, how VCReg uses spatial dimensions in its calculations is not well explained—I suggest that the authors provide explicit formulas. Additionally, it is unclear how the method determines which intermediate layers to add the regularization components. The lack of clarification on these critical settings raises concerns about the reproducibility of the method. The authors should provide a step-by-step algorithm or pseudocode for how VCReg is applied, including details on handling spatial dimensions and selecting intermediate layers. This would significantly enhance the reproducibility of the method and clarify its implementation.

3. **Some of the experimental results raise concerns.** CDNV measures the degree of clustering of the features, but the authors applied it to "two unlabeled sets of samples." It is unclear how the authors obtained and processed this data, and the significance of using unlabeled data in a supervised learning context is questionable. In Table 6, the results show that ConvNeXt (VCReg) demonstrates significantly weaker clustering ability compared to the standard ConvNeXt, which does not support the claim that this method prevents neural collapse. Furthermore, in Table 4, the reproduced performance of VICReg is even worse than SimCLR, which contradicts the prior knowledge of self-supervised learning. As a result, I find it difficult to be convinced by the experimental outcomes presented in the paper.

### Questions
See weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2
