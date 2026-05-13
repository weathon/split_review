# Exploring the Impact of Information Entropy Change in Learning Systems

- Decision: Reject
- Scores: 5, 8, 3

## Abstract
We investigate the impact of entropy change in deep learning systems by noise injection at different levels, including the embedding space and the image. The series of models that employ our methodology are collectively known as Noisy Neural Networks (NoisyNN), with examples such as NoisyViT and NoisyCNN discussed in the paper. Noise is conventionally viewed as a harmful perturbation in various deep learning architectures, such as convolutional neural networks (CNNs) and vision transformers (ViTs), as well as different learning tasks like image classification and transfer learning. However, this work shows noise can be an effective way to change the entropy of the learning system. We demonstrate that specific noise can boost the performance of various deep models under certain conditions. We theoretically prove the enhancement gained from positive noise by reducing the task complexity defined by information entropy and experimentally show the significant performance gain in large image datasets, such as the ImageNet. Herein, we use the information entropy to define the complexity of the task. We categorize the noise into two types, positive noise (PN) and harmful noise (HN), based on whether the noise can help reduce the complexity of the task. Extensive experiments of CNNs and ViTs have shown performance improvements by proactively injecting positive noise, where we achieved an unprecedented top 1 accuracy of 95$\%$ on ImageNet. Both theoretical analysis and empirical evidence have confirmed that the presence of positive noise, can benefit the learning process, while the traditionally perceived harmful noise indeed impairs deep learning models. The different roles of noise offer new explanations for deep models on specific tasks and provide a new paradigm for improving model performance. Moreover, it reminds us that we can influence the performance of learning systems via information entropy change.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This research investigates the impact of noise-induced entropy changes in deep learning systems, focusing on computer vision tasks. While noise is traditionally seen as detrimental, this study demonstrates that specific noise, termed positive noise (PN), can enhance deep learning model performance by reducing task complexity defined by information entropy. The study introduces a distinction between positive noise (beneficial) and harmful noise (detrimental) and shows that proactive injection of positive noise significantly improves accuracy, achieving over 95% on ImageNet. Besides, this paper explores three types of noises. But the difference of positive noises on different kinds of noise types lacks discussion.

### Strengths
Strengths:
- This paper challenges the notion that noise always hampers deep learning models, showcasing its potential as a positive influence.
- It offers theoretical insights, distinguishing noise impact at different levels, aiding in optimizing task complexity.
- Experiments on both CNNs and Vision Transformers are conducted.

### Weaknesses
- The range of tasks tackled remains relatively limited, lacking diversity and complexity in comparison to broader applications. To be specific, this paper only conducts experiments on classification tasks. More results on other tasks (e.g., regression tasks like Object Detection or generative tasks like language understanding)  are lacking to validate its generalization ability.

### Questions
For each type of noise, there will exist positive noises. What are their difference and influences?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper examines the impact of task entropy change in deep neural networks by introducing noise at different levels in a network, and demonstrates that certain kinds of noise can actually help with learning by reducing the task entropy. The paper differentiates between "positive noise" (PN) that can enhance system performance by reducing task complexity and "harmful noise" (HN) that deteriorates it. The concept of "positive noise" is introduced in [1] which this work cites. By using information entropy as a measure of task complexity, the research shows that intentionally adding positive noise can substantially improve performance. The empirical findings challenge traditional views on noise in deep learning, suggesting that positive noise can be beneficial. Results are demonstrated using networks from the ResNet and ViT family for classification on ImageNet and using ViT-B for unsupervised domain adaptation on Office-Home and Visda2017 datasets.

[1] Xuelong Li. Positive-incentive noise. IEEE Transactions on Neural Networks and Learning Systems,
2022.

### Strengths
The paper is well written. The supplementary section provides further details on the derivations, which is very helpful.

The technique is well motivated and the empirical results are quite impressive.

This work provides an interesting new perspective on positive noise injection which can help training.

### Weaknesses
No error bars in any tables - did the authors run multiple seeds for their experiments? Even though the improvements are generally large, it is nice to see these in the tables/figures.

The technique is only evaluated on classification using ImageNet and domain adaptation. It would be good to see results on other tasks like object detection perhaps, and specially domains like Natural Language Processing, which differ from vision based tasks.

### Questions
Given that the improvement is so large on ResNet-18, do the authors have an explanation for why ViT-T does not improve similarly?

Can the authors elaborate on this statement? "Besides, when the models are corrupted under brute force attack, the positive noise also can not work." Why is this the case?

This point also requires more detailed explanation - "Second, injection to shallow layers obtain less entropy change gain because of trendy replacing Equation 8 with Equation 7." The explanation for why shallower layers don't provide as high accuracy gains as deeper layers can be improved. 

Have the authors tried combinations of later layers for noise injection?

Given that this is a new perspective and the results are strong, will code be released for reproducibility?

Can the authors give other examples of positive noise that they considered?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper aims to explore the influence of the information entropy change, and specifically analyzes the impact of various types of noise, i.e., Gaussian noise, linear transform noise, and salt-and-pepper noise, on the performance of deep learning models for image classification and domain adaptation tasks. The authors verify their method on different network architectures, i.e., CNNs and ViTs, and show that the positive noise injection can improve the accuracy of image classification.

### Strengths
1. The proposed method of using noise injection to improve the performance of CNNs and ViTs, which has not been extensively explored before.

2. The article is well-written and easy to understand, with clear explanations of the proposed method and the experimental results.

### Weaknesses
1.Limited analysis between data augmentation and the proposed noise injection. It seems more like a feature augmentation method for different layers. The article claims that the positive noise is benefit of the classification network, but it is hard to measure the noise level for the positive/negative influence. It is encouraged to compare the difference between the data augmentation with noise and the proposed method.

2.Noise definition confusion. Unlike Gaussian noise and salt-and-pepper noise with the specific probability distribution, the linear transform is not a kind of noise, but a simple operation. 

3.Limited analysis of the tasks. The authors leverage the proposed method in image classification tasks, including domain adaptation. It is encouraged to conduct the noise injection in image object detection/segmentation tasks, or some NLP tasks, to verify the effectiveness of the proposed method.

### Questions
See weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor
