# Towards Reliable Evaluation and Fast Training of Robust Semantic Segmentation Models

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 6, 5

## Abstract
Adversarial robustness has been studied  extensively in image classification, especially for the $\ell_\infty$-threat model, but significantly less so for related tasks such as object detection and semantic segmentation, where attacks turn out to be a much harder optimization problem than for image classification. We propose several problem-specific novel attacks minimizing different metrics in 
accuracy and mIoU. The ensemble of our attacks, \multiloss, shows that existing attacks severely overestimate the robustness of semantic segmentation models.
Surprisingly, existing attempts of adversarial training for semantic segmentation models turn out to be weak or even completely non-robust. We investigate why previous adaptations of adversarial training to semantic segmentation failed and  show how recently proposed robust \imagenet backbones can be used to obtain adversarially robust semantic segmentation models with up to six times less training time for \voc and the more challenging \ade.
  \keywords{Semantic segmentation \and Adversarial attacks \and Robust models}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors propose an ensemble of adversarial attacks,  like in the AutoAttack framework, containing attacks with different loss functions for the task of semantic segmentation. In particular, they empirically show that existing loss functions for the task of semantic segmentation overestimate the confidence of robust models. Furthermore, they also train a robust model by utilizing the robust backbones from image classification literature, which significantly boosts performance while saving computing power

### Strengths
- The presentation of the paper is good 
- The empirical boost in performance is consistent across the board for different models
- It is interesting to see the benefit that comes with the robust initialization using pre-trained Imagnet models

### Weaknesses
 - My major concern is the limited novelty, as the explored loss functions are not new. Although JS divergence, masked CE loss, and masked spherical loss have not been commonly used in the context of segmentation attacks, in my view, this appears to be a simple 'plug and play' of loss functions


- The conducted attacks are white-box, and the absence of black-box evaluation is a significant limitation

- The paper only considers untargeted attacks, and it would be useful to extend the analysis to targeted attacks to showcase the strength of the proposed attack method.


- The authors could conduct experiments to evaluate the transferability of the proposed attack to other models and compare it against the baseline PGD/CosPGD/SegPGD attacks.

### Questions
- Please see my comments in the Weakness section.

- Why is AT in Section 3 performed with the PGD attack baseline?  It would be interesting to use stronger attacks during the AT to develop even stronger robust models

- How did you choose the budget scheme of 3:3:4 in the progressive reduction of epsilon approach?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper focus on making robust evaluation of semantic segmentation models against L-inf adversarial attacks and show a straightforward approach to train robust segmentation models faster. Authors review existing measures like Jensen-Shannnon divergence, Masked cross-entropy and Masked spherical loss for their applicability as adversarial objectives for semantic segmentation task. They show that these objectives serve as better robustness evaluators than previously utilized objectives in the literature. They make three optimization related decisions: 1) replacing PGD with APGD, 2) progressively reduce attack radius and, 3) train for more iterations. Finally, they propose Segmentation Ensemble Attack (SEA) to evaluate models with different losses utilizing APGD and optimize for more iterations. Furthermore, to improve speed and efficiency of adversarial training, they initialize backbone of semantic segmentation models with ImageNet Robust Models and show a significant improvement on the adversarial robustness.

### Strengths
-	Paper is well written and easy to understand.

-	Motivation is clearly delivered.

-	Discussed and reviewed different measures for their suitability for adversarial loss.

-	Results show that the candidate losses mentioned in the paper attack the model better.

-	Backbones initialized with ImageNet Robust Models provide higher adversarial training robust accuracy than using standard ImageNet model.

### Weaknesses
My major concern is the lack of originality and novelty in the paper. All the losses, optimizations tricks, and robust models utilized in the paper are obtained from the existing literature (authors have cited the prior works sufficiently). There are no novel methodological contributions presented in the paper. Paper detail as different existing components collectively utilized to obtain better results. The findings shown in the paper are interesting. However, I believe that they alone do not support to meet the standards for accepting at a conference. Novel methodological contribution regarding losses or obtained robust models would be appreciated.

### Questions
My concern mainly targets the core essence of the paper i.e. lack of originality and technical novelty. I appreciate the authors for conducting this study. I believe this paper would fit for a workshop submission.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the l_{\limit} white-box adversarial attacks for semantic segmentation model. By discussing the loss functions used in semantic segmentation, i.e., pixel-level cross entropy loss, this paper shows the difficulty of adversarial attacks for semantic segmentation, than image classification model. Besides, this paper also proposes and compares 4 loss functions for semantic segmentation. As a result, to achieve higher attack performance, the proposed method combines 4 loss functions as SEA attack. Finally, this paper also studies the defense techniques for the above attacks. Comparing the proposed method with SegPGD and CosPGD, this work shows stronger attack performance won ADE20K and Pascal VOC. Finally, this paper also presents the comparison between the proposed defense PIR-AT with AT on several network architectures.

### Strengths
+ The overall work is solid, that the proposed method starts from the analysis of loss functions for semantic segmentation. Besides, 4 different loss functions are compared, and then Semantic Ensemble Attack (SEA) is proposed, which is interesting.

+ The evaluation is conducted under different attack strengths and network architectures.

+ Different optimization methods are discussed for adversarial attacks, that fewer computation costs are needed.

### Weaknesses
 - This paper needs to discuss more about PIR-AT. It is only mentioned that this paper proposes Pre-trained ImageNet Robust Models. What is this method in detail? 

- What is the motivation to limit this paper to focus on l_{\limit} threat model?

### Questions
See weakness section.

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes several losses for attacking the semantic segmentation models with adversarial training and an evaluation protocol for benchmarking the adversarial robustness of the segmentation models. This paper also proposes to adopt adversarially pretrained models for segmentation models' initialization. Extensive experiments with various segmentation networks present the effectiveness of the proposed  methods.

### Strengths
1. The motivation of this paper for the proposed method is clear and the proposed method is consistent to the motivations.
2. The paper proposes new losses for attacking, evaluating and training semantic segmentation models. The proposed loss and the evaluation protocol could become great baselines for the further works.
3. The proposed method is verified on two popular segmentation networks and two datasets and it presents great insights in this field.

### Weaknesses
1. The advantages of the proposed three losses are not well depicted. It would be better if the author could discuss under different scenarios which proposed loss is the best for attacking. Some visual examples would be better.
2. The organization of this paper is confusing. The introduction of some existing works like APGD should be put in the related works. An overview of the method's structure could be added to the beginning of section 2. As section 2 mentions PIR-AT s many times, a short description about PIR-AT model is also necessary.
3. As many related works and ablation studies are mixed in the method part, it is difficult to distinguish the contributions of this work from previous works.
4. The SEA is not presented clearly. Why four losses perform worse than all six losses is not analyzed. How the current four losses are selected is not mentioned. And SEA doesn't discuss how to balance different losses.
5. Previous works[1] have proven that using a better robust initialization model could improve the task model's robustness. How PIR-AT is different from the existing practices is not well presented.

### Questions
1. Will AT obtain the same performance as PIR-AT if sufficient training time is given?
2. PIR-AT suggests using $L_{\infty}$-robust ImageNet model for initialization. How much computational resources are required to train this model compared to the normal ImageNet model with the same parameters?
3. How the image-wise worst case over all losses in Table 2 is calculated? A short description is expected.
4. Does the conclusion in Figure 2 also generalize to clean models?
5. What is the result of AT with 32 epoch in Figure 5?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
