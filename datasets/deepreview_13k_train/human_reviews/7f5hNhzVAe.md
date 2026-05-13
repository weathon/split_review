# Robust Domain Generalisation with Causal Invariant Bayesian Neural Networks

- Decision: Reject
- Scores: 3, 6, 3

## Abstract
Deep neural networks can obtain impressive performance on various tasks under the assumption that their training domain is identical to their target domain. Performance can drop dramatically when this assumption does not hold. One explanation for this discrepancy is the presence of spurious domain-specific correlations in the training data that the network exploits. Causal mechanisms, in the other hand, can be made invariant under distribution changes as they allow disentangling the factors of distribution underlying the data generation. Yet, learning causal mechanisms to improve out-of-distribution 
    generalisation remains an under-explored area. We propose a Bayesian neural architecture that disentangles the learning of the the data distribution from the inference process mechanisms. We show theoretically and experimentally that our model approximates reasoning under causal interventions. 
    We demonstrate the performance of our method, outperforming point estimate-counterparts, on out-of-distribution image recognition tasks where the data distribution acts as strong adversarial confounders.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes a Bayesian neural architecture that disentangles learning of the data distribution from inference during the learning process. It outperforms its counterparts based on point estimates.

### Strengths
It outperformed the VAE on two datasets of image classification.

### Weaknesses
Overall, this paper lacks novelty, motivation is unclear, experimentation is insufficient, and there is a lack of references concerning domain generalization.

### Novelty:

1. Using causality or Bayesian for domain generalization is not novel and already investigated in [1,2,3]. Specifically, [1,2] proposed causality inspired method to domain generalization. [3] proposed Bayesian learning to extract domain invariant features.

2. The proposed only works on image classification task and only CNN based architectures.

### Motivation:

1. The motivation is unclear. Could you elaborate on your rationale for using Bayesian Neural Networks for disentanglement? What are the benefits of combining domain-invariant and specific parts during inference?

### Experiments:

1. Adding ablation studies for KL divergence term of weights to demonstrate the necessary Bayesian network. Or only use domain-invariant part in the inference time.
2. Comparison methods are insufficient. Please compare all the method in the "Missing reference", and highlight the difference.
3. Only two simple datasets CIFAR10 and Office Home. Please add more datasets. e.g., DomainBed benchmark, which including five datasets (PACS, VLCS, OfficeHome, Terra, DomainNet) and is the most widely used benchmark for domain generalization.

4. Only CNN-based architecture. Please using other widely used backbone like Visual Transformer such as Vit-B-16.

5. Only test on image classification task, please test on time series task as well.

### Missing References:

[1] Lv, Fangrui, et al. "Causality inspired representation learning for domain generalization." Proceedings of the IEEE/CVF conference on computer vision and pattern recognition. 2022.

[2] Ouyang, Cheng, et al. "Causality-inspired single-source domain generalization for medical image segmentation." IEEE Transactions on Medical Imaging 42.4 (2022): 1095-1106.

[3] Xiao, Zehao, et al. "A bit more bayesian: Domain-invariant learning with uncertainty." International conference on machine learning. PMLR, 2021.

[4] Derakhshani, Mohammad Mahdi, et al. "Bayesian prompt learning for image-language model generalization." Proceedings of the IEEE/CVF International Conference on Computer Vision. 2023.

[5] Yu, Xi, et al. "INSURE: an Information theory iNspired diSentanglement and pURification modEl for domain generalization." IEEE Transactions on Image Processing (2024).

### questions:
 1. Without a reconstruction loss, how can it ensure that no information is lost (like domain-invariant information) in achieving disentanglement?

2. Please add computation complexity in the table, since the objective function contains two KL terms.

3. How to choose the hyper-parameter in front of each terms?


### Questions
1. Without a reconstruction loss, how can it ensure that no information is lost (like domain-invariant information) in achieving disentanglement?

2. Please add computation complexity in the table, since the objective function contains two KL terms.

3. How to choose the hyper-parameter in front of each terms?

### Soundness
1

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
3

### Summary
This paper proposes an intervention mechanism that can be added to a bayesian inference pipeline to solve out of distribution tasks. The method improves in distribution and out of distribution performance in an unsupervised manner. Intervention is made by leveraging contextual information from within dataset using Mixup strategies. The inference network is a partially stochastic bayesian neural network. Theoretical result is derived for when intervention is made taking into account conditioning on the training dataset. This result is then used to show performance improvement on CIFAR10 and OFFICEHOME datasets.

### Strengths
1. The novelty of the paper is to apply causal interventions in a bayesian inference pipeline and show improvements on out of distribution data compared to point estimate based networks.
2. Another novel aspect compared to baseline used is considering datasets in the causal graph and deriving the theoretical result and its execution with partially stochastic networks.
3. The paper provides a methodology to learn causal representations in unsupervised manner.
4. The underlying concepts for bayesian networks, causality are adequately explained.
5. The authors provide an anonymized code repository for review.

### Weaknesses
1. Experiments -  The authors show improvements on dataset with translation of CIFAR10 and OFFICEHOME dataset. Results on datasets with other types of commonly seen o.o.d. variations like different backgrounds would make a more convincing point. Specifically, the paper lacks experiments that explore more complex domain shifts, such as changes in object pose, illumination, or partial occlusions, which are common in real-world scenarios. The current evaluation is limited to relatively simple transformations, which may not fully demonstrate the robustness of the proposed method.
2. Visualizations for results would be helpful to understand the domain gap and analyze improvements with proposed method. The paper would benefit from visualizations that illustrate the learned representations and how they change under different interventions. For example, t-SNE plots or similar dimensionality reduction techniques could be used to show how the proposed method clusters data points from different domains, and how these clusters are affected by the intervention mechanism. This would provide a more intuitive understanding of the method's behavior.
3. While the architecture is well described in the paper, the training and evaluation algorithm could be described with more clarity and details for how the theoretical result is used. The paper describes the theoretical framework but lacks a clear, step-by-step explanation of how this framework is translated into a practical training algorithm. Details on how the intervention is implemented during training, how the partially stochastic network is optimized, and how the theoretical results guide the training process are missing. A more detailed description of the training and evaluation process would greatly improve the reproducibility and understanding of the method.

### Questions
1. How much is the performance improvement due to proposed intervention design vs from the use of bayesian inference over point-estimate methods?
2. While other files are present, the trainer.py file in anonymized code repo is empty. Would appreciate access to understand the method better.

### Soundness
3

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
3

### Summary
This paper exploits the invariance of causal mechanisms under distribution changes to improve out-of-distribution generalisation. 
It proposes the Causal-Invariant Bayesian (CIB) neural network. The CIB architecture combines a variational encoder, an inference module, and a Bayesian neural network,
aiming to learn domain-invariant representations. Theoretically, the model is shown to approximate reasoning under causal interventions.
Experimentally, the model improves out-of-distribution generalisation in image recognition tasks.

### Strengths
1. It is interesting to exploit the causal mechanism invariance to improve out-of-distribution generalisation.
2. Both theoretical and empirical evidence are provided to validate the proposed architecture. 
3. The formulations are clearly presented and illustrated.

### Weaknesses
1. It is not a new idea to exploit the causal mechanism invariance to improve out-of-distribution generalisation.
Many works have already used this idea to improve out-of-distribution generalization, e.g., [1] [2] [3] [4].
The paper does not discuss these related works sufficiently and compare the proposed method to these approaches.
2. The experiments only compare a single method for out-of-distribution generalization, which does not even appear to outperform the vanilla baseline (Table 1).
The comparison is insufficient to prove the superiority of the proposed method.
3. The proposed architecture seems to be an integration of several existing methods.

### Questions
1. What are the novelty and the superiority of the proposed method over other methods that enhance out-of-distribution generalization through causal mechanism invariance?
2. What are the novel aspects of the proposed architecture beyond integrating existing techniques?

### Soundness
2

### Presentation
3

### Contribution
2
