# Learning anti-classes with one-cold cross entropy loss

- Decision: Reject
- Avg Score: 5.50
- Scores: 8, 3, 5, 6

## Abstract
While softmax cross entropy loss is the standard objective for supervised classification, it primarily focuses on the ground truth classes, ignoring the relationships between the non-target, complementary classes. This leaves valuable information unexploited during optimization. In this work, we set explicit non-zero target distributions for the complementary classes, in order to address this limitation. Specifically, for each class, we define an *anti-class*, which consists of everything that is not part of the target class—this includes all complementary classes as well as out-of-distribution samples, and in general any instance that does not belong to the true class. Various distributions can be used as a target for the anti-classes. For example, by setting a uniform one-cold encoded distribution over the complementary classes as a target for each anti-class, we encourage the model to equally distribute activations across all non-target classes. This approach promotes a symmetric geometric structure of classes in the final feature space, increases the degree of neural collapse during training, addresses the independence deficit problem of neural networks and improves generalization. Our extensive evaluation demonstrates that our proposed framework consistently results in performance gains across multiple settings, including classification, open-set recognition, and out-of-distribution detection.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a new auxiliary loss function, called one-cold cross entropy (OCCE), for classification tasks. Unlike standard cross-entropy (CE), which relies on a one-hot vector representation, OCCE employs a one-cold vector, setting the true class to zero and all other classes to one. To apply this one-cold vector in OCCE, the logits of the final layer are inverted and passed through a standard softmax-cross-entropy loss. OCCE is then used as an auxiliary loss alongside CE. The proposed OCCE encourages a symmetric geometric structure among complementary classes, addressing the independence deficit problem and enhancing the degree of neural collapse. 

Brief background on “independence deficit” and “neural collapse”: independence deficit is a phenomenon caused by the rank deficiency of deep neural networks, where classification confidence of a class can be linearly reproduced by the confidences of a small number of other (sometimes irrelevant) categories. And “neural collapse” signifies maximally separated and independent class representations. 

The authors present experimental results in multiple settings for generalization in classification, open-set recognition, out of distribution recognition and transfer learning. In all reported results, OCCE improves the baseline.

### Strengths
+ Very well-written paper. 
+ Tackles a fundamental problem and brings an interesting perspective. 
+ Comprehensive set of experiments, where the proposed loss improves baseline performance.

### Weaknesses
 - Although the experiments section is comprehensive, there is not a single result from literature (other papers) -- except the transfer learning in Table 2. Almost all experiments are comparisons to baseline. There is no comparison to SOTA. For example, the methods described in Related Work are competitors but there is no direct comparison with them, such as “baseline + OCCE” versus “baseline + competitor”. And, ideally, it would be more convincing if both the baseline and “baseline + competitor” results are taken from literature. 
- Most key properties of OCCE were shown with a simple ResNet18v2 architecture. It would be more convincing to see more and larger encoders. Specifically, the analysis of neural collapse and independence deficit should be validated on more complex architectures, as these phenomena can manifest differently depending on network depth and capacity. For instance, very deep networks might exhibit different behaviors in terms of feature space geometry compared to shallower ones like ResNet18v2.
- In the abstract, robustness to “noise” is mentioned but I don’t see this in the experiments. The term “noise” is vague and could refer to various types of perturbations, such as adversarial noise, random pixel noise, or label noise. Without specific experiments, it is unclear how OCCE is robust to any of these types of noise. The claim should be either supported by experiments or removed.

Minor: 
Fig2 caption says z_0=3 but in the text you say 2.5.

### Questions
- “Relationships between non-target classes” -> this sounds ambiguous to me. Do you mean (i) the relationships between the target class and all complementary classes, or (ii) the relationships among all classes, or (iii) the relationships among complementary classes?
- Figure 1 can be made more clear. When you say “anti-class distribution for each point” and there are multiple points, do you superimpose them on top of each other and show just a single plot? This is not clear to me. 
- Isn’t “anti-class” bad nomenclature? Target or non-target, they are all classes. I don’t know, It might be better to say “anti-ground truth” or “anti-true” or “anti-positive” instead of anti-class. 
- How does squared difference (between y and y_hat) behave? It explicitly and symmetrically pulls down negative classes to zero and pushes the positive class to 1.
- How does OCCE do under class imbalance (long-tail)? 
- In the tables, what is the value after plus minus? Standard deviation, standard error or variance? 
- Does OCCE incur any kind of overhead during training?

Post-rebuttal edit: my questions above are sufficiently addressed by the authors.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
While softmax cross entropy loss is commonly used for supervised classification, it overlooks the relationships between non-target classes, leading to underutilized information. To address this, the authors introduce one-cold cross entropy (OCCE) loss, which targets the activations of complementary classes by defining an anti-class for each target class, encompassing all non-target instances. By encouraging the model to uniformly distribute activations across non-target classes, OCCE loss promotes a more structured and symmetric feature space, enhancing neural collapse and addressing the independence deficit problem. The experiments demonstrate that OCCE loss consistently improves performance across various settings.

### Strengths
1. This paper is easy to follow.

2. The effect of OCCE loss on the occurrence of neural collapse and Indepedence Deficit is explored, which is good.

### Weaknesses
1. The proposed anti-class is actually  reverse cross entropy (RCE) adopted in [1]. There is nothing new. In [1], the authors also utilized CE+\lambda RCE like Enq (8) in this paper. So the novelty of this paper is quite limited.

2. The compared baselines are quite out of date.

### Questions
Please see the Weakness.

### Soundness
2

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
4

### Summary
The paper presents "one-cold cross entropy loss" (OCCE), as opposed to the widely-adopted "one-hot cross entropy loss" (CE). The motivation is that "the typical CE loss primarily focuses on the ground-truth classes, ignoring the relationships between the non-target, complementary classes. This leaves valuable information unexploited during optimization." Therefore, the paper propose to encode all the non-target classes as label-1, so-called "anti-class", and the target as label-0. As stated in the paper, this OCCE equally treats all non-target classes,  out-of-distribution samples, noise, and in general any instance that does not belong to the true class. The OCCE loss equally distributes activations across all non-target classes. Experiments on CIFAR-100 and TinyImageNet demonstrate that OCCE performs better than CE and other CE variants, yields better performance on open-set recognition and out-of-distribution detection.

### Strengths
- It is intersting to see that the paper considers a different way to encode ground-truth information to train classification models, i.e., using the OCCE loss rather than the typical one-hot cross-entropy loss.
- The writing is good and the readability is good.
- Experiments cover multiple aspects including closed-set classification, open-set recognition, and out-of-distribution detection.

### Weaknesses
 - As the paper considers to encode the ground-truth differently from one-hot, by using the proposed one-cold encoding, it is expected to compare other losses such as Supervised Contrastive Loss (SupCon) [R1]. SupCon has supervisions from within-class positive pairs and between-class negative pairs. It can be thought of treating non-target classes equally. It is straightforward to ask whether the OCCE loss has advantages over SupCon.

- The paper combines OCCE loss and the typical CE loss in Eq. (8) to train models, and explains that "we empirically observed convergence instabilities on more complex datasets with a larger number of classes, due to the challenge of perfectly aligning the activations of all complementary classes". It suggests that it is factually unreasonable to treat non-target classes equally, make supervisions from them while ignoring the target-class 

- There are some more related works that explore hierarchical classification [R2,R3,R4], which seems to move forward beyond "treating non-target classes equally". These methods seem to satisfy the motivation of the paper "structuring the activations of these complementary classes". The paper should carry out more careful survey, discuss the importance and difference from related works.

- The datasets (CIFAR100 and TinyImageNet) and network architectures (ResNet18v2) used in the experiments are too small. Related works consider larger-scale datasets (e.g., ImageNet) and more diverse larger networks (e.g., ResNet-200) in experiments to demonstrate the effectiveness of proposed methods in nowadays' standards. The paper should enrich experiments.

### Questions
Authors are encouraged to address the weaknesses in rebuttal/responses. Please refer to the weaknesses for details.

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
The paper proposes to complement the standard cross-entropy loss with the idea of better controlling the behavior of predictions for negative classes, i.e., different from the target groundtruth (other classes or out-of-distribution data).

The complementary loss is expressed as the entropy of an inverse-coded problem formulation (the "one-cold" loss), where the targets are the negative classes with equal priors. The loss is claimed to favor three desirable properties: neural collapse, reduced independence deficit, and generalization.

The evaluation is carried out on problems of basic and transfer learning for classification, open set detection, and out-of-distribution detection on small to medium-sized datasets.

### Strengths
- The writing is clear and easy to read.

- The proposed OCCE complementary loss is simple.

- The impact of the loss on neural collapse and independence deficit is well argued and justified by experiments on some convolutional and transformer architectures.

- The positive impact on almost all experiments is consistent, although marginal for some problems (transfer learning).

### Weaknesses
 - The impact of OCCE on generalization, while empirically effective, is less justified. It is stated that it should avoid distribution shifts (which cannot be reduced to out-of-distribution detection), but this is not really proven or demonstrated by experiments.

- The limitations of the approach are not clearly identified or summarized: the only discussion I found is about learning instabilities (l.252).

- No discussion or presentation of other known approaches for dealing with negative or hard data, e.g., contrastive or focal losses (see few references in the "Questions" section).

- Evaluation only on small or medium-sized datasets: should at least be evaluated on ImageNet.

### Questions
- My feeling is that favoring neural collapse and reducing the independence deficit is not always desirable for classification problems where the classes have a structure or hierarchy. Can you elaborate on this?

- Can you compare your approach with contrastive [1-4] or focal [5-7] losses?

- Some of the concurrent losses have been used for calibration [8], which is also an issue for OOD or open set recognition: what is the calibration level of the proposed approach? (can be evaluated with ECE).

[1] Khosla, P., Teterwak, P., Wang, C., Sarna, A., Tian, Y., Isola, P., ... & Krishnan, D. (2020). Supervised contrastive learning. Advances in neural information processing systems, 33, 18661-18673.

[2] Kalantidis, Y., Sariyildiz, M. B., Pion, N., Weinzaepfel, P., & Larlus, D. (2020). Hard negative mixing for contrastive learning. Advances in neural information processing systems, 33, 21798-21809.

[3] Li, S., Xia, X., Ge, S., & Liu, T. (2022). Selective-supervised contrastive learning with noisy labels. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition (pp. 316-325).

[4] J. Mukhoti, V. Kulharia, A. Sanyal, S. Golodetz, P. Torr, et P. Dokania, « Calibrating deep neural networks using focal loss », Advances in Neural Information Processing Systems, vol. 33, p. 15288‑15299, 2020.

[5] Neo, D., Winkler, S., & Chen, T. (2024). MaxEnt Loss: Constrained Maximum Entropy for Calibration under Out-of-Distribution Shift. In Proceedings of the AAAI Conference on Artificial Intelligence.

[6] X. Li et al., « Generalized Focal Loss: Learning Qualified and Distributed Bounding Boxes for Dense Object Detection », 8 juin 2020, arXiv: arXiv:2006.04388.

[7] A. Ghosh, T. Schaaf, et M. Gormley, « AdaFocal: Calibration-aware Adaptive Focal Loss », Advances in Neural Information Processing Systems, vol. 35, p. 1583‑1595, déc. 2022.

[8] C. Wang, « Calibration in Deep Learning: A Survey of the State-of-the-Art », 10 mai 2024, arXiv: arXiv:2308.01222.

### Soundness
3

### Presentation
3

### Contribution
2
