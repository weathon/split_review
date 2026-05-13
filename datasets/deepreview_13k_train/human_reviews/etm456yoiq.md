# B$^{3}$CT: Three-branch Coordinated Training for Domain Adaptive Semantic Segmentation

- Decision: Reject
- Scores: 5, 5, 5, 3

## Abstract
Unsupervised domain adaptive semantic segmentation aims to adapt a dense prediction model trained on the source domain to the target domain by transferring knowledge without further annotations. A mainstream solution for transferring knowledge is to achieve alignment between different domains and eliminate domain gaps caused by source-target distributions. However, previous work paid little attention to where and when to align. We find that different contents in images are aligned at different stages of the whole network, and the alignment should be gradually strengthened during the whole training process due to the accuracy of target pseudo labels. Given these two observations, we propose a three-branch coordinated training (B$^{3}$CT) framework. Besides two normal source and target branches, a third branch is involved specifically for the alignment. In this branch, the hybrid-attention mechanism is utilized to do the alignment, while an Adaptive Alignment Controller (AAC) is built to adjust the contents being aligned according to the stages of the whole network. Meanwhile, in B$^{3}$CT, a coordinate weight is designed to gradually strengthen the importance of the alignment based on the training accuracy in the whole training process. Extensive experiments show that our proposed methods achieve competitive performances on tasks of GTA5$\to$Cityscapes and SYNTHIA$\to$Cityscapes.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper focuses on unsupervised domain adaptation and proposes a multi-branch coordinated training method. Specifically, it designs three-branch coordinated training technique, where the final loss function is dynamically weighted by coordinate weight on the loss values of three branches. Extensive experiments show that the proposed method has achieved good unsupervised domain adaptation performance.

### Strengths
-a. It proposes a multi-branch coordinated training method for unsupervised domain adaptation.
- b. It designs three-branch coordinated training technique, where the final loss function is dynamically weighted by coordinate weight on the loss values of three branches.
- c. The experimental results show that the performance of the proposed method is promising in unsupervised domain adaptation.

### Weaknesses
Although this paper is well written with comprehensive evaluation and good results, there are still some issues.
Several parts of this paper are not very clear and need further clarification. Please check the questions.
In addition, some key related works that also address unsupervised domain adaptation are missed. Please check the questions.
1. In table 5, it seems that the proposed method performs less effectively on Synthia to Cityscapes benchmark. It would be better to provide some insights and analysis to illustrate these results.
2. As shown in the ablation studies in Tables 1-3, the performance gains seem not significant. Did the author conduct experiment with multiple random runs or random seeds? It is not clear how much the training randomness affects the performance when the gains are not significant.
3. The key related unsupervised domain adaptation papers [A, B, C, D] are missed. This paper focuses on unsupervised domain adaptation and proposes a multi-branch coordinated training method. The differences, pros and cons of the proposed multi-branch coordinated training method and the traditional UDA co-training methods [A, B, C, D] are not clear. [A] introduces multiple feature spaces and performs co-training by conducting Co-regularized Alignment among them, whereas [B] introduces multiple classifiers and performs co-training by conducting Collaborative Alignment upon them. [C] achieves co-training by introducing multiple diverse classifiers to generate class-balance weights, which are then used to weight/regularize adversarial learning or self-training, whereas [B] achieves co-training by leveraging current and historical models to generate historical consistency weights, which are then used to weight/regularize adversarial learning or self-training. It would be better to provide discussion and analysis to illustrate the differences, pros and cons of the proposed method and [A,B,C,D]. For example, the differences, pros and cons of the proposed coordinate weights, the class-balance weights in [C] and the historical consistency weights in [D], for UDA.
4. According to Table 3, it seems that HRDA (73.8) has been taken as the baseline. Did the author try to apply the proposed method on other methods/baselines and what about the performances/gains? It is very interesting to investigate the generalization ability of the proposed method by testing it on other baselines.

### Questions
Please check Weaknesses.

Conclusion
Overall, this work proposes a multi-branch coordinated training method for UDA and yields good experimental results. However, there are some details that need to be made clearer, as listed in the questions. I would like to upgrade the score if the questions could be well addressed.

### Soundness
3 good

### Presentation
2 fair

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
This paper introduces an unsupervised domain adaptive segmentation method named B$^3$CT. In addition to the traditional UDA learning approach, which involves supervised training on the source domain and re-training on the target domain, the key idea lies in the introduction of a third branch that facilitates the alignment of the source and target domains through cross-attention mechanisms.

When addressing the question of "where to align," the paper introduces an Adaptive Alignment Controller (AAC) at each layer to determine varying degrees of alignment. As for the question of "when to align," the paper defines a coordinate weight that controls the loss value within the hybrid branch, where the coordinate weight is derived from the pseudo-accuracy of target predictions generated by the student model compared to the target pseudo-labels provided by the teacher model. The experiments are conducted on two public benchmarks: GTA5-to-CityScapes and Synthia-to-CityScapes, showing the effectiveness of the method.

### Strengths
- The paper is well-written and easy to follow.
- The concept of using cross-attention to align source and target features is elegant and logically sound.
- The design of the coordinate weight, which operates smoothly, is well-founded.

### Weaknesses
 - The paper claims to achieve state-of-the-art performance on GTAV→Cityscapes (74.8), which is not entirely accurate. A previously published paper, MIC (CVPR2023) [1], has achieved a higher performance of 75.9. I noticed the authors did not cite and compare it. Therefore, the claimed contribution should be reconsidered.
- The proposed B$^3$CT is only applicable to transformer-based architectures and cannot be employed with CNN-based models. This significantly limits its applicability, as many existing segmentation models are based on CNNs. The paper does not discuss potential adaptations or modifications that would enable the method to work with CNN backbones, which is a major drawback for broader adoption.
- B$^3$CT introduces additional computation during the inference stage, which raises concerns about computational efficiency for both training and testing. The paper lacks a thorough analysis of the computational overhead introduced by the cross-attention mechanism and the Adaptive Alignment Controller (AAC). It would be valuable to include a comparison of computational efficiency in the paper's evaluation, specifically reporting the increase in FLOPs, parameter count, and inference time, and discuss the practical implications of these increases.

### Questions
Will authors release code?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper primarily focuses on the domain-adaptive semantic segmentation task. The authors introduce a so-called "Three-Branch Coordinated Training" (B^3CT) framework. This framework encompasses distinct source and target domain branches, along with a mixed attention branch equipped with an Alignment Controller (AAC) to transfer knowledge from the source to the target domain gradually. Additionally, the authors propose a "coordinate weight" strategy to emphasize when to execute the knowledge transfer. The authors have effectively evaluated their approach to major public benchmarks.

### Strengths
1. The problem of unsupervised domain adaptation is important and pertinent to the community.

2. The exposition on related techniques is quite comprehensive.

3. The ablation studies are thorough, and the experimental configurations are clearly presented.

### Weaknesses
1. While the authors' motivation offers some insight, the experimental results presented are not entirely convincing. Despite the inclusion of three carefully designed components, the model's performance only improves by 1% mIoU on the GTA to Cityscapes transfer. Moreover, the performance on the Synthia to Cityscapes transfer is even lower than the baseline (HRDA).

2. The authors only conducted experiments in the relatively simple and ideal scenario of transferring from synthetic datasets to real datasets, neglecting the more convincing Cityscapes to ACDC experiments. I believe that adding this experiment would make the authors' work more robust.

3. I have some reservations to the extent that the introduced three-branch and AAC modules may add additional parameters and computational load, potentially boosting the model's Oracle performance. The performance gains claimed by the authors could very well stem from this.

### Questions
See weaknesses above.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This work aims to address the problem of domain adaptive semantic segmentation, mainly focusing on "where and when to align". At first, a hybrid-attention mechanism is proposed to achieve feature fusion and alignment. Then, an adaptive alignment controller (AAC) is designed to determine the alignment feature at each stage. Next, a coordinate weight is proposed to adjust the alignment time through the training process. In summary, the main contributions of this work are somehow novel, however, the performance gains are limited, and the comparison results are insufficient.

### Strengths
**Originality**: The paper proposes three ideas, hybrid branch, adaptive alignment controller (AAC), and coordinate weight, which are generally applicable and work for feature alignment and fusion.

**Quality**: The paper provides a thorough experimental evaluation of B$^3$CT on two simulation-to-real domain adaptive semantic segmentation bechmarks. The paper also conducts ablation studies to analyze the impact of different components of B$^3$CT, such as data flow in the hybrid branch, qualitative experiments on AAC, and the hyperparameter of coordinate weight. The paper demonstrates that B$^3$CT can achieve superior performance when combined with the HRDA baseline.

**Clarity**: The paper also provides sufficient background information and related work to situate the contribution of B$^3$CT in the context of existing literature on domain adaptive semantic segmentation and self- and cross-attention.

**Significance**: The paper addresses an important and challenging problem of domain adaptive semantic segmentation, which has many applications in autonomous driving, robotics, and scene understanding.

### Weaknesses
 **Major Issues**:

**Insufficient novelty and contribution**: The newly proposed B$^3$CT framework lacks justification for its design. The pipelines of hybrid-attention and adaptive alignment controller seem natural and basic. The core issue is that the paper doesn't adequately explain why this specific combination of hybrid attention, adaptive control, and coordinate weighting is particularly effective or novel compared to existing methods. The hybrid attention mechanism, while seemingly applicable, lacks a strong theoretical or empirical basis for its specific design choices. The adaptive alignment controller (AAC) appears to be a straightforward application of attention, and the paper does not sufficiently justify its specific architecture or control mechanism. The coordinate weight, while providing some dynamic adjustment, does not demonstrate a significant advantage over simpler methods. The overall framework lacks a compelling rationale that justifies its complexity and differentiates it from existing domain adaptation techniques.

**Insufficient results for experiments**: 

- Although the authors state in the main text, "the third branch of which facilitates learning domain-invariant features for alignment", they provide no experimental results. 

- In Tab. 1, the result of only ablating "coor. weight" also should be reported.

- In Sec. 4.4, the authors should differentiate the comparison results according to different network architectures, such as deeplab and segformer. The current presentation of results does not allow for a clear understanding of how the proposed method performs across different network architectures. Specifically, it is unclear whether the method's effectiveness is consistent across different backbone networks or if it is highly dependent on a specific architecture. This is crucial for assessing the generalizability of the proposed approach.

- Recent works not only conduct experiments on two standard simulation-to-real benchmarks, i.e., GTA5-to-Cityscapes and SYNTHIA-to-Cityscapes but also extend to adverse conditions. To name a few, SePiCo [a] and MIC [b] have extended to more challenging daytime-to-nighttime semantic segmentation task and CoTTA [c] has also investigated clear-to-adverse conditions using online adaptation. I would like to see the potential of B$^3$CT on more challenging scenarios.

**Insufficient justifications**: For example, about training accuracy or pseudo-accuracy, some justifications are missing in this paper. Any advantages and limitations of pseudo-accuracy? The paper does not provide a clear explanation of how pseudo-labels are used, their potential limitations, and how these limitations are addressed within the proposed framework. Specifically, the paper should discuss the potential for error propagation from inaccurate pseudo-labels and how the proposed method mitigates this issue.

**Insufficient details**: From Tab. 3, the only thing we can see is that there will be one hybrid attention with AAC in each stage. However, where should we exactly insert hybrid branch into a feature encoder? And what is the consumption of resources, such as GPU memory? The paper lacks specific details regarding the implementation of the hybrid branch within the feature encoder. The exact location of insertion and the impact on the overall network architecture are not clearly defined. Furthermore, the paper lacks a discussion of the computational resources required by the proposed method, such as GPU memory usage and inference time. This information is crucial for assessing the practical applicability of the method.

**Minor Issues**:

- In Eq. 2 and Eq. 5, $p_t^{i,j,c}$ (target predictions from student model) should be $\hat{y}_t^{i,j}$ (target pseudo-label from teacher model)? Also, in Eq. 7 and Eq. 8 $p_t^i, \hat{y}_t^i$ should be $p_t^{i,j}, \hat{y}_t^{i,j}$, respectively?

- The results of the experiments throughout the text are in two retained decimals, except for Table 5, where the authors should be consistent.

- Typos: "hybrid-attention different stages." -> "Hybrid-attention different stages." in Sec. 4.1.

### Questions
The authors should discuss the limitations and potential negative societal impact in the Conclusion.

Please also refer to Weaknesses.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
