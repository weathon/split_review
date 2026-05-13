# APD: Boosting Adversarial Transferability via Perturbation Dropout

- Decision: Reject
- Scores: 5, 5, 5, 5

## Abstract
The transferability of adversarial attack to deep neural networks (DNNs) accounts for the possibility that the adversarial examples crafted for a known model can also mislead other unseen models in black-box setting. Existing literature to improve the adversarial transferability often focus on spreading the adversarial perturbations towards the whole image, which can be counter-productive as the extended perturbation can hardly track the attention regions across different models. That's because although they spread the perturbation throughout the entire image but they do not consider the mutual influence of different perturbation regions. In this paper, we propose a simple yet effective perturbation-dropping scheme that can enhance the transferability of the adversarial examples by incorporating the dropout mechanism during their optimization process. Specifically, we leverage the class activation map (CAM) to locate the midpoint of the dropped regions, whereby the effective perturbation can be generated for the target models while maintaining the attack rate towards the source model even if some blocks of the perturbation noises are dropped. Extensive experiments are conducted on the ImageNet dataset, which demonstrates that the proposed method outperforms state-of-the-art methods, that achieve both high attack efficiency and transferability.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper's primary objective is to enhance the transferability of adversarial examples. To achieve this, the method introduced in the paper incorporates dropout techniques within the optimization process of adversarial attacks. The specific dropout regions are determined using Class Activation Mapping (CAM). Experimental results demonstrate that this method effectively enhances the performance compared to several baseline approaches.

### Strengths
The experimental results exhibit strong credibility. Adversarial examples are generated based on various base models (Inception-V3, Inception-V4, Inception-ResNet-V2, ResNet-101), and the proposed method, APD, is applied to several baseline attack techniques like MI-FGSM and DIM-FGSM. The results consistently demonstrate the enhancement provided by the proposed method.

I would also like to acknowledge the value of Table 3, which assesses the effectiveness of the proposed method on diverse models, including transformer-based models.

### Weaknesses
1. The motivation section requires further clarification. While it is understood that different models may emphasize different attention regions, a more explicit rationale for using Class Activation Mapping (CAM) to select dropout regions is necessary. Addressing whether random dropout region selection is a viable alternative would not only provide a valuable baseline but also shed light on the fundamental choices made in this work.

2. The paper emphasizes the distinction between traditional feature-level dropout and the proposed image-level dropout method for constructing adversarial examples. It is worth exploring the potential impact of incorporating feature-level dropout into the process and conducting a more in-depth discussion of related works such as Huang et al. (2019) and Li et al. (2020). These discussions could include experimental comparisons to better highlight the advantages and trade-offs of the proposed approach in relation to these previous works.

### Questions
See weakness.

### Soundness
2 fair

### Presentation
3 good

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
The paper proposed a novel adversarial attack named adversarial Perturbation Dropout (APD), which can enhance the transferability of adversarial examples with dropout during optimization. It is activated by the investigation that attention regions are not consistent across different models and perturbations in the neglected regions also have a significant effect on transferability due to the synergy between perturbations from different regions. Simple experiments are conducted to verify the mutual influence between perturbations. APD breaks the synergy by leveraging the class activation map (CAM) to dropout perturbations. Experiments on ImageNet show that APD can achieve high transferability and efficiency across CNNs.

### Strengths
1. The paper presents a novel finding that perturbations in attention and neglected regions have a mutual influence, creating a synergy that reduces the transferability of attack methods.

2. A major strength of APD lies in its simplicity and effectiveness, leveraging CAM to dropout perturbations.

3. Apart from APD’s performance on transferability, the paper also considers performance on defense, further highlighting the effectiveness of the method.

4. The paper's ablation study is comprehensive, including a random drop of regions and the selection of crucial hyperparameters.

### Weaknesses
1. The technical novelty of perturbation dropout is limited, as similar thoughts have been proposed in recent works [1].

2. The attention regions may shift during the attack iterations; therefore, it is unreliable to rely on the CAM from the previous iteration as guidance for the current one.

3. The experiment compares AA-TI-DIM(SOTA) and some classic transfer-based attacks with APD. It would be better if comparisons with relevant methods such as the previously mentioned PI-attack that extends the perturbation to cover the object, or other dropout methods, can be made.

4. In order to verify the mutual influence between perturbations from different regions, the paper compares random noise removal with selective noise removal. It removes perturbations in regions in which the source model focuses while the target model does not. It would be more convincing if noises in regions that both source and target models neglect were removed. 

5. In the experiments, MI and other transfer-based attacks are used as baselines but PGD attack is not presented.

6. In terms of dataset, the expression is not rigorous (the chosen images can be almost classified correctly by all models, i.e., the model has a high accuracy). Images correctly classified by all used models in this paper can be selected from ImageNet.

7. The proposed APD method can be more intuitive if the flow chart is provided. 

8. The evaluation of APD’s performance is limited and not comprehensive due to a lack of diversity of model architectures. Only transferability across CNNs is presented in the paper but other popular models like ViTs and SNNs are not considered, which is important in terms of transferability evaluation. Such evaluations are mentioned in recent works like [2] [3]

[1] Xinquan Chen, Xitong Gao (equal)*, Juanjuan Zhao, Kejiang Ye, Chengzhong Xu. AdvDiffuser: Natural Adversarial Example Synthesis with Diffusion Models. International Conference on Computer Vision (ICCV). 2023.
[2] Muzammal Naseer, Kanchana Ranasinghe, Salman Khan, Fahad Shahbaz Khan, and Fatih Porikli. On improving adversarial transferability of vision transformers. arXiv preprint arXiv:2106.04169, 2021.
[3] Wenqian Yu, Jindong Gu, Zhijiang Li, Philip Torr.Reliable Evaluation of Adversarial Transferability. arXivpreprint arXiv:2306.08565, 2023

### Questions
1. The paper uses hotspots(i.e. the local maximum points) of the CAM as the midpoints of the dropped regions. Why not use thresholds to determine the dropped regions?

2. Will the attention regions shift during the attack iterations? Can the attention shifts be visualized?

3. The performance of APD on two classic defense methods is presented. What is the attack performance on adversarial training models?

### Soundness
2 fair

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work introduces a dropout scheme on perturbation to improve the adversarial transferability of attacks. Instead of random dropout, the authors propose to utilize CAM to discover the key points of images, which forms the dropped regions. The evaluation is conducted on ImageNet with various networks. The comparison with baselines as well as ablation studies show the effectiveness of the proposed algorithm.

### Strengths
1. The paper is well-organized and easy to follow.
2. The proposed dropout scheme seems to be an interesting way to tackle adversarial transferability since vanilla dropout in DNNs helps generalization.
3. The evaluation on ImageNet shows promising results and the ablation studies are sufficient.

### Weaknesses
1. There seems to be a gap between CAM regions and the dropped regions in Figure 3. However, the reason why the proposed algorithm utilizes midpoints with square regions instead of the CAM regions is not well-explained.
2. The complexity needs more discussion since the proposed algorithm requires more iterations, such as the time consumption comparison with other baselines in Table 1.
3. More evaluation on other advanced vision models, such as vision transformer [a, b].
4. More comparison with other adversarial transferability works on attention or regularization [c, d]. 

Minors:
1. Missing definition of $\alpha$ in Section 3.2.
2. Undefined Eq in Line 18 of Algorithm 1.

[a]. Transferable Adversarial Attack for Both Vision Transformers and Convolutional Networks via Momentum Integrated Gradients. ICCV 2023.

[b]. Transferable Adversarial Attacks on Vision Transformers with Token Gradient Regularization. CVPR 2023.

[c]. Improving Adversarial Transferability via Neuron Attribution-based Attacks. CVPR 2022.

[d]. Boosting the transferability of adversarial attacks with reverse adversarial perturbation. NeurIPS 2022.

### Questions
1.	Please clarify the gap in Figure 3.
2.	Please discuss the complexity.
3.	Please provide more evaluation on advanced vision models.
4.	Please include more comparisons.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a novel adversarial attack method called Adversarial Perturbation Dropout (APD), which enhances the transferability of adversarial examples. APD disrupts perturbations across different attention regions by applying dropout mechanisms to adversarial images, ensuring the attack effect for the target model even when perturbations are outside its attention regions. To enhance APD's effectiveness, class attention maps are incorporated to refine dropped regions. Extensive experiments demonstrate the effectiveness of APD.

### Strengths
This work's motivation is intuitive, making it overall easy to follow. The topic of this paper is valuable.

### Weaknesses
1. I don't think attention-based attack methods are innovative; in fact, this is a classic approach in the study of adversarial transferability. Unfortunately, the authors did not discuss its relevance to existing attention-based attack methods.
2. Why not consider the more challenging topic of targeted attacks instead of limiting the scope to non-targeted attack scenarios?
3. Why doesn't DBA compare or integrate with existing higher-performing methods[3][4]?

If the authors can provide reasonable explanations for these issues, I am inclined to increase the score.

[1] Wu W, Su Y, Chen X, et al. Boosting the transferability of adversarial samples via attention[C]//Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2020: 1161-1170.
[2] Wang J, Liu A, Yin Z, et al. Dual attention suppression attack: Generate adversarial camouflage in physical world[C]//Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2021: 8565-8574.
[3] Zhu Y, Chen Y, Li X, et al. Toward understanding and boosting adversarial transferability from a distribution perspective[J]. IEEE Transactions on Image Processing, 2022, 31: 6487-6501.
[4] Qin Z, Fan Y, Liu Y, et al. Boosting the transferability of adversarial attacks with reverse adversarial perturbation[J]. Advances in Neural Information Processing Systems, 2022, 35: 29845-29858.

### Questions
See above.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor
