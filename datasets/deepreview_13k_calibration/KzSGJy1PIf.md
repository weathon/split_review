# Selective Unlearning via Representation Erasure Using Adversarial Training

- Decision: Accept
- Avg Score: 5.67
- Scores: 5, 6, 6

## Abstract
When deploying machine learning models in the real world,  we often face the challenge of “unlearning” specific data points or subsets after training. Inspired by Domain-Adversarial Training of Neural Networks (DANN), we propose a novel algorithm, SURE, for targeted unlearning. SURE treats the process as a domain adaptation problem, where the “forget set” (data to be removed) and a validation set from the same distribution form two distinct domains. We train a domain classifier to discriminate between representations from the forget and validation sets.Using a gradient reversal strategy similar to DANN, we perform gradient updates to the representations to “fool” the domain classifier and thus obfuscate representations belonging to the forget set. Simultaneously, gradient descent is applied to the retain set (original training data minus the forget set) to preserve its classification performance.  Unlike other unlearning approaches whose training objectives are built based on model outputs, SURE directly manipulates there presentations.This is key to ensure robustness against a set of more powerful attacks than currently considered in the literature, that aim to detect which examples were unlearned through access to learned embeddings.  Our thorough experiments reveal that SURE has a better unlearning quality to utility trade-off compared to other standard unlearning techniques for deep neural networks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes a novel algorithm – SURE, for targeted unlearning. Inspired by work in domain adaptation, SURE treats a “forget set” and a validation set from the same distribution as data from two different domains, and optimizes the feature extractor to be s.t., the representations of the forget data are obfuscated from a discriminating domain classifier. Since SURE works directly on representation space, it prevents the stealing of information that may have remained in the latent space. The authors conduct experiments across a wide variety of utility metrics and compare their performance with many existing works.

### Strengths
- The paper is easy to understand. 
- SURE demonstrates impressive results over existing works on a wide variety of metrics.
- SURE provides a stable training regimen for unlearning methods that are usually sensitive to hyper-parameters.

### Weaknesses
 - The experiments are limited to CIFAR-10 and ResNet-18, albeit with a few results on CINIC-10. I believe that it’s important to observe the results on a wider variety of benchmarks, and more importantly models (like ViTs, etc) to ensure generality. The current evaluation lacks sufficient exploration of different model architectures and dataset complexities, which is crucial for establishing the robustness of the proposed method. For instance, the performance of SURE on larger datasets with more complex data distributions, or on models with different inductive biases (e.g., transformers), remains unclear.
- Access to the validation set from the same distribution as the forget data: I am unsure how practically valid this assumption might be as the kinds of data people may want to remove are also primarily scarcely available, and if you trained and now want to unlearn on all of it (which seems plausible for current foundation models), it would not sit well with your current setup. The requirement of a validation set that mirrors the distribution of the forget set is a significant limitation. In many real-world scenarios, the data to be unlearned might be rare or sensitive, making it difficult to obtain a representative validation set. This assumption needs to be more thoroughly justified, or the method's applicability will be limited.
- Novelty: The paper acknowledges that it heavily builds up on the DAN framework and applies it to the machine unlearning setup. While the application of domain adversarial training to unlearning is interesting, the core methodology is not fundamentally novel. The paper should more clearly delineate the specific adaptations and innovations that distinguish it from existing domain adaptation techniques. The contribution should be more clearly articulated beyond the application of an existing framework to a new problem.

### Questions
- I would like to see results on different architectures and possibly more benchmarks. 
- I would like to hear the authors' opinions on the practical implications of assuming access to the validation set.
- I would like to hear the authors' opinions on why SURE performs particularly (relatively) worse on RRT compared to other metrics.

### Soundness
3

### Presentation
3

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
This paper proposes an approximate unlearning method that focuses on unlearning in the representation space rather than in the output space. Experiments demonstrate that the method has superior or comparable results compared to existing techniques.

### Strengths
1. This paper introduces a novel machine unlearning method for classification tasks (CIFAR-10, CINIC-10) via domain adversarial training, which shifts the focus from the output space to the representation space.

2. The performance gain from the proposed method is convincing.

3. The presentation is clear and easy to follow.

### Weaknesses
1. The paper compared its performance with 'Towards Unbounded Machine Unlearning, NIPS 2023' by the MIA metric (User Privacy Settings). However, the proposed method should also be evaluated in removing biases (RB), Resolving Confusion (RC) settings. RB aims to achieve the highest possible error on the forgetting set, without hurting the error of the retain and the test set. It evaluates the performance of the proposed algorithm in unlearning the knowledge of the target domain while not hurting other's performance.  RC aims to resolve confusion between two classes that the original model suffers from due to a part of its training set being mislabelled. (settings from ''Towards Unbounded Machine Unlearning, NIPS 2023'')


2. Although the authors use CINIC-10 (a subset of ImageNet) to validate the effect of forgetting, the authors should still provide the effect of forgetting on the ImageNet-1K. There are many pre-trained models on ImageNet-1K and this study focuses on classification tasks, it is more convincing to test on ImageNet-1K to prove the real-world applicability of the proposed algorithm.


3. The title is ambiguous and should emphasize domain adversarial training rather than adversarial training to make it more clear, as domain adversarial training aims to improve the domain adaptation ability of the target model via an adversarial fashion, while adversarial training aims to improve the target model's robustness against adversarial attacks.

### Questions
1. The paper is mainly focused on classification tasks. I'm wondering if it can be extended to multi-modal tasks (image-text) and generation tasks (LLM, Diffusion)?

2.  Why does the reversal layer R(x)=x can helps to forget the representation & knowledge of D_f? Could the author provide more details about the optimization goal (2) on Page 6? (I see the optimization details in Appendix C, but still confused.  What is the relationship between L_d(G_d(R(G_f(x;\theta_f));\theta_d), 1(x\in D_f) ) and equation (7) (8) (9) in Page 14 & Appendix C?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes SURE (Selective Unlearning via Representation Erasure), a novel approach for targeted unlearning in neural networks, based on representation erasure rather than model output manipulation. Using concepts from Domain-Adversarial Training of Neural Networks (DANN), SURE aims to align the representation space of a model post-unlearning with that of an oracle model. This method focuses on defending against more robust attacks, particularly membership inference attacks (MIAs) in the representation space, improving the stability of unlearning while preserving model utility.

### Strengths
- The paper introduces a unique perspective by targeting the representation space instead of the output space, addressing a critical gap where unlearned models might retain information in their intermediate representations. This angle has the potential to advance understanding and methodology in the field of machine unlearning.
- The authors validate SURE’s effectiveness using extensive experiments across several unlearning scenarios, including random, partial, and full class unlearning. The results consistently demonstrate that SURE achieves a favorable trade-off between performance and unlearning efficiency.
- By specifically aiming to improve defenses against membership inference attacks within the representation space, SURE contributes to increasing the security and robustness of unlearned models.
- The technical approach, particularly the adaptation of DANN with gradient reversal and domain-adversarial training, is well-articulated.

### Weaknesses
 - Although SURE demonstrates stability across different forget set sizes, its reliance on careful hyperparameter tuning (with Bayesian optimization) may hinder ease of implementation for practitioners who cannot afford extensive hyperparameter searches.
- SURE appears to introduce additional computational complexity. While this approach enhances unlearning quality, it may limit SURE's scalability, especially for larger models or datasets where computational efficiency is crucial.
- Minor Comment on Notation Consistency: The authors should maintain consistent notations across the paper to improve readability. For example, in Figure 1, the notation for different modules should be consistent with those used in the main text ($G_f(., \theta_f)$, $G_y(., \theta_y)$, and $G_d(., \theta_d)$). This would help readers follow the mathematical formulations and understand the relationships among components more easily.

### Questions
1. Could the authors provide a breakdown of the computational cost of SURE compared to the baselines?
2. How sensitive is SURE’s performance to the choice of hyperparameters, especially those determined by Bayesian optimization? If SURE requires highly tuned hyperparameters, exploring ways to reduce this dependency could make it more accessible for practical applications.

### Soundness
4

### Presentation
3

### Contribution
3
