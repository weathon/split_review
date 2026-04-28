# Indirect Gradient Matching for Adversarial Robust Distillation

- Decision: Accept
- Avg Score: 6.75
- Scores: 8, 8, 6, 5

## Abstract
Adversarial training significantly improves adversarial robustness, but superior performance is primarily attained with large models. 
This substantial performance gap for smaller models has spurred active research into adversarial distillation (AD) to mitigate the difference. 
Existing AD methods leverage the teacher’s logits as a guide.
In contrast to these approaches, we aim to transfer another piece of knowledge from the teacher, the input gradient.
In this paper, we propose a distillation module termed Indirect Gradient Distillation Module (IGDM) that indirectly matches the student’s input gradient with that of the teacher.
We hypothesize that students can better acquire the teacher’s knowledge by matching the input gradient. 
Leveraging the observation that adversarial training renders the model locally linear on the input space, we employ Taylor approximation to effectively align gradients without directly calculating them.
Experimental results show that IGDM seamlessly integrates with existing AD methods, significantly enhancing the performance of all AD methods.
Particularly, utilizing IGDM on the CIFAR-100 dataset improves the AutoAttack accuracy from 28.06\% to 30.32\% with the ResNet-18 model and from 26.18\% to 29.52\% with the MobileNetV2 model when integrated into the SOTA method without additional data augmentation.
The code will be made available.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper aims to improve the adversarial robustness of lightweight or small models using adversarial distillation. Unlike directly using the teacher's logits as a guide, the authors focus on distilling the input gradients of the teacher model to achieve point-wise alignment between the teacher and student. The proposed IGDM can integrate with other AD methods and has demonstrated consistent performance improvements across different datasets.

### Strengths
1. Aligning the input gradients of the teacher and student is an insightful and interesting approach.

2. IGDM is a simple and effective method that can be easily applied as a regularization term to other AD methods, achieving consistent performance improvements.

3. Comprehensive experimental results and ablation studies demonstrate the effectiveness of IGDM.

4. The paper is well-written and easy to follow.

### Weaknesses
Overall, this paper is logically coherent and well-argued. The effectiveness of IGDM is based on the assumption of the locally linear property of adversarial robust models, and preliminary experiments in Section 3.1 support this assumption. However, the data and models used in the experiments are relatively simple. Validating the effectiveness of IGDM on more general models, such as ViT or CLIP, and on more complex tasks, such as detection and segmentation, could provide more universal insights for future research.

### Questions
See Weaknesses

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper focuses on improving the adversarial robustness of DNNs through adversarial distillation. Specifically, it addresses the challenge that smaller models, which are preferred for their computational efficiency, lag behind larger models in terms of robustness against adversarial attacks. The authors propose the Indirect Gradient Distillation Module (IGDM), which aims to transfer the input gradient knowledge from a robust teacher model to a student model, indirectly matching the student’s input gradient with the teacher's.  The experimental results demonstrate the effectiveness of the proposed approach in significantly improving adversarial robustness.



Based on the detailed response by the authors, I decided to improve my rating!

### Strengths
1. The authors propose a novel distillation module called the Indirect Gradient Distillation Module (IGDM) and provide a theoretical foundation for why gradient matching through output differences works, leveraging the local linearity of adversarially trained models. But, I have some doubts about the theoretical assumptions here. The fragility of neural networks is attributed to the linear properties of neural networks[1], and the paper assumes this local linear property to solve the gradient, which is contrary to the conclusions of previous related research. So, does this method really simulate the gradient of the network?

2. Extensive experiments across different datasets, student models, and teacher models validate the effectiveness of IGDM in improving robustness against various attack scenarios.

[1] Ian J Goodfellow, Jonathon Shlens, and Christian Szegedy. Explaining and harnessing adversarial examples. ICLR, 2015.

### Weaknesses
1. The authors propose a novel distillation module called the Indirect Gradient Distillation Module (IGDM) and provide a theoretical foundation for why gradient matching through output differences works, leveraging the local linearity of adversarially trained models. But, I have some doubts about the theoretical assumptions here. The fragility of neural networks is attributed to the linear properties of neural networks[1], and the paper assumes this local linear property to solve the gradient, which is contrary to the conclusions of previous related research. So, does this method really simulate the gradient of the network?

2. Extensive experiments across different datasets, student models, and teacher models validate the effectiveness of IGDM in improving robustness against various attack scenarios.


1.  Although the paper did a lot of experiments, I think it is not fair enough. For example, the teacher model used in the paper is usually better than the teacher models of other methods. So if other methods also use the same teacher model, can they also achieve good robustness?

2. Line 160 of the paper mentions that using gradients directly is difficult, which is important for the motivation of the paper, so it needs to be reflected in the main context rather than being placed in the Appendix.

### Questions
1. I am confused about Figure 1(a) in the paper. In the distillation architecture, the teacher model is already trained, while the student model is not. In the feature space, the manifolds of the models are different. Even if the directions of the gradients are the same, the manifold spaces are inconsistent, and the paths they take should also be different. Therefore, the adversarial samples of the teacher model and the student model cannot be consistent. One way to prove this is to use the adversarial samples generated by the teacher model and the student model to attack another model to see if the attack effects are consistent.

2  In Figure 2, in adversarial training and adversarial distillation, why is it that in the early stages of training, when the student model should not be robust yet, why does the remainder proportion of the model not increase?

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
5

### Summary
This paper proposes a new method named Indirect Gradient Distillation Module (IGDM) for adversarial distillation. Different from the traditional adversarial distillation methods that mainly focus on distilling the logits of the teacher model, this method emphasizes distilling the gradient information of the teacher model. By taking advantage of the local linear characteristics of the adversarially trained model, these gradients are obtained indirectly, thereby significantly enhancing robustness.

### Strengths
1. The author obtains the gradients indirectly by taking advantage of the local linear characteristics of the adversarially trained model, thereby significantly enhancing robustness.
2. The modular design of IGDM enables it to be easily integrated with existing adversarial distillation methods.
3. Through a large number of experimental results, the author has verified that IGDM can successfully enhance the robustness of the existing adversarial distillation methods.

### Weaknesses
The loss function of the Indirect Gradient Distillation Module (IGDM) proposed in this paper is derived from the first-order Taylor function expansion, which is similar to the situation of making the training loss become low-curvature [in d - f]. In fact, the research works in [e, f] also used similar techniques, but they mainly studied the problems in traditional adversarial training. If the teacher network in this paper is changed to only input natural images, the proposed loss in the paper may degenerate into an evolutionary target of the aforementioned works. Therefore, the author needs to conduct a comparative analysis between their method and the existing works that are also based on the first-order Taylor function expansion, and analyze the differences. Moreover, what will be the result if the regularization loss of the existing works is added to the adversarial distillation target?

The authors utilize the internal loss to generate adversarial perturbations. It would be better to elaborate on its formulaic representation in the main paper. Is the cross-entropy used directly? How much impact do different internal losses have on the results? What would be the effect if the adversarial perturbations are generated using Equation 9?

Some of more recent works, that are about the adversarial distillation, are missing, such as [a-c].

### Questions
Please check the details in weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents an Indirect Gradient Distillation Module (IGDM) for adversarial training via adversarial distillation methods. 
It claims to match the input space gradient between teacher and student models with knowledge distillation. The main claim is "indirect" gradient matching/alignment compared to direct gradient alignment, which is available in the literature. Central to the paper is equation 2 (first-order Taylor expansion of adversarially trained models) and equation 8, which is the formulation of IGMD. The paper performs an exhaustive list of experiments. However, there is no indication of making code available for reproducibility is indicated in the paper.

### Strengths
The main strength of the paper is the extensive set of experiments on Indirect Gradient Distillation Modules (IGDM) for adversarial training via adversarial distillation methods. The IGDM is use used as an additive loss for adversarial knowledge distillation (Equation 9), which is claimed to be the first Indirect gradient matching compared to direct gradient matching.

### Weaknesses
The paper does not make it clear how this way gradient matching is "indirect." From Figure 1 and Figure 2 and the related explanation, it is not clear why this is "indirect" gradient distillation.  There is no comparative picture presented to clarify the comparison/contrast between  Indirect Gradient  and Direct Gradient distillation.

Except for Table 7, It is not explicitly mentioned or clear that they run the other (SOTA) algorithms themselves or that the results were taken from the reported results. If experiments were re-run, other hyperparameter setting descriptions were not given or not referred to which hyperparameter setting were used, e.g., home many epoch os training.

There are some inconsistencies in making results bold for best results in some tables and not in some tables.

### Questions
Figure 2a says that the "remainder proportion" of the adversarial robust teachers is shown in Table 1. However, One would wonder, comparing Figure 2a and Table 1, how to make sense of these two different metrics. Figure 2a y-axis is "proportion," Table 1 has clean accuracy and attacked accuracy values. How can one calculate "proportion" from Table 1 to make sense of Figure 2a?

It has not been demonstrated how preparation values 0.012 and 0.016 have arrived. It is not clear if the proposition nose value is the accuracy value. From the equation, it appeared to be a noise term, but making reference to Table 1 makes one feel it is an accuracy term.

Figure 2b also under explains as to how one can relate Equation 2 and Figure 2b. 

The paper claims to do an "input gradient" matching Figure 1 and Line 151. However, the gradient matching is done via the discrepancy between student and teacher models model outputs. It is unclear how this method differs from other methods that do gradient distillation.

### Soundness
3

### Presentation
3

### Contribution
3
