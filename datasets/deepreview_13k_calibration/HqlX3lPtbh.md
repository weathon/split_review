# OT-Attack: Enhancing Adversarial Transferability of Vision-Language Models via Optimal Transport Optimization

- Decision: Reject
- Avg Score: 6.00
- Scores: 5, 8, 5, 6

## Abstract
Vision-language pre-training (VLP) models demonstrate impressive abilities in processing both images and text. However, they are vulnerable to multi-modal adversarial examples (AEs). Investigating the generation of high-transferability adversarial examples is crucial for uncovering VLP models' vulnerabilities in practical scenarios.
Recent works have indicated that leveraging data augmentation and image-text modal interactions can enhance the transferability of adversarial examples for VLP models significantly. However, they do not consider the optimal alignment problem between data-augmented image-text pairs. This oversight leads to adversarial examples that are overly tailored to the source model, thus limiting improvements in transferability.
In our research, we first explore the interplay between image sets produced through data augmentation and their corresponding text sets. We find that augmented image samples can align optimally with certain texts while exhibiting less relevance to others. Motivated by this, we propose an Optimal Transport-based Adversarial Attack, \emph{dubbed} OT-Attack. The proposed method formulates the features of image and text sets as two distinct distributions and employs optimal transport theory to determine the most efficient mapping between them. This optimal mapping informs our generation of adversarial examples to effectively counteract the overfitting issues. Extensive experiments across various network architectures and datasets in image-text matching tasks reveal that our OT-Attack outperforms existing state-of-the-art methods in terms of adversarial transferability.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper focuses on the task of conducting adversarial attacks on vision-language models. The focus of the attack is transferability. The paper introduces the optimal transport perspective for finding more transferable attacks by considering the optimal alignment between augmented image-text pairs. In experiments, the paper compares the proposed method with single-modality attacks, separate attacks by two single-modality attacks, and two multi-modal attacks.

### Strengths
This paper introduces a new perspective on an existing problem. The paper considers optimal alignment between augmented image-text pairs for more transferable adversarial attack patterns. This idea makes sense and is original to the best of my knowledge.

### Weaknesses
1. The evaluation baselines are not comprehensive in experimental design. The use of single-modality attacks PGD/Bert-Attack as baselines is weak in proving the effectiveness of the proposed method. There are certain representative multi-modal adversarial attacks not included for comparison. E.g., VLATTACK by Yin et al. in NeurIPS 2023, which focuses on the transferability of attacking pretrained vision-language models. These representative multi-modal attacks are not discussed in the paper either.
2. Although the perspective is new, the proposed solution is proposed to solve an existing problem, which makes the contribution trivial. Meanwhile, the paper lacks technical depth for discussing the applications of optimal transport in this problem. First, the paper lacks a discussion on the computational overhead caused by optimal transport. This paper introduces the application of it in vision-language models. However, the computation of optimal transport needs a certain time. The paper hasn't discussed it in the paper. Second, the paper didn't discuss the convergence of optimal transport for vision-language model attack either. Such algorithms need careful selection of hyperparameters. Thus, although the designed method sounds reasonable, this paper lacks technical depth for discussing the tradeoff and convergence.
3. Formatting problem exists in the current manuscript: e.g., L251, 'transport'. L411, '1 3 5 7' is not centered in table 4.

### Questions
1. What's the convergence condition for solving the optimal transport problem in this proposed setting?
2. What's the time cost is like for solving the optimal transport problem in this proposed setting?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a new adversarial attack for vision-language models called OT-Attack, pointing out that the existing SGA attack has a limitation in considering correct image-text matching after augmentations.

OT-Attack utilizes Optimal Transport to capture valid image-text matching between augmented images and captions (calculate transportation matrix $T_{ij}$). Then, adversarial attack optimization maximizes the $loss_{OT}$ ($\sum T_{ij} C_{ij}$) to update an adversarial image. 

The method improves the transferability of the SGA attack in three tasks: image-text retrieval, image captioning, and visual grounding.

### Strengths
- This paper highlights an interesting point: the SGA attack overlooks true image-text matching when using input augmentations. The motivation is clear.
- The method is simple.
- OT-Attack consistently improves SGA's attack success rate in three tasks: image-text retrieval, image captioning, and visual grounding.

### Weaknesses
 - [W1] The presentation is not optimal.
    - [W1.1] The citation style is wrong: Authors should correctly use \citet and \citep. Please refer to the guideline carefully and modify them. 
    - [W1.2] While the authors highlight OT-Attack’s successful attack against GPT-4 and Bing Chat at the end of the Introduction, there is no result in the main text.  Even in the Appendix, there is only one example without a comparison between attack methods, which makes it unreasonable to highlight this in the introduction. I suggest adding quantitative results or remove the claim.
- [W2] OT optimization introduces additional computational cost. How much does the computational cost differ between SGA and OT-Attack? 
- [W3] Sensitivity to the regularization hyperparameter is unclear. How does the hyperparameter $\lambda$ affect the attack success rate (ASR) and computational cost? Does more accurate OT optimization lead to better ASR? I suggest adding an ablation study table.

### Questions
Please refer to the weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this paper, the authors propose a transfer-based adversarial attack method for vision-language pre-training (VLP) models that leverages image-text augmentations and optimal transport theory to enhance adversarial example transferability. Experiments are conducted across various vision-language tasks and VLP models.

### Strengths
1. This paper aims to enhance the transferability of adversarial examples for vision-language pre-training models, addressing a practical and increasingly relevant issue as these models gain importance in real-world applications.  
2.  Adversarial examples generated by OT-Attack are tested on commercial models like GPT-4 and BingChat.

### Weaknesses
1. Overall, the manuscript presents valuable insights; however, enhancing the clarity and coherence of the writing, particularly in the methods section, would significantly improve its readability and impact.
2. The titles of Tables 1 and 2 are identical, which may easily confuse readers and hinder their understanding of the experiments. Differentiating the titles would improve clarity and facilitate comprehension of the authors' work.

### Questions
1. Co-attack and SGA were proposed prior to 2023, and since then, many new vision-language models have emerged. To further validate the effectiveness of the proposed method, the authors should evaluate additional vision-language models, such as Eva-CLIP and BLIP2 for image-text retrieval tasks, and MiniGPT4 and Qwen2-VL for image generation tasks in a transfer-based setting.  
2. I did not find any ablation experiments addressing the role of image-text augmentation and optimal transport theory in OT-attack.  
3. The authors claim that optimal transport can enhance adversarial example transferability; I recommend providing a theoretical explanation and further experimental analysis to support this assertion.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper investigates data augmentations in the context of transferable attacks on Vision-Language Processing (VLP) models. Compared to existing methods, the proposed approach achieves improved alignment between augmented images and text. Specifically, the authors leverage optimal transport theory to derive the most efficient mapping between augmented image distributions and text distributions. They conduct experiments on image-text retrieval, image captioning, and visual grounding tasks to demonstrate their improved transferability.

### Strengths
1. This paper identifies a key issue in existing attacks: a mismatch in augmentations applied to images versus text. To address this, the authors utilize optimal transport theory, enhancing transferability. The motivation and proposed solutions are logical and well-founded.
2. The authors conduct extensive experiments across four VLP models and multiple tasks, effectively demonstrating the superior performance of their approach.

### Weaknesses
My primary concern is the focus on attacking VLP models solely through adversarial image generation, while neglecting the equally crucial role of text in these models. Since texts play an integral part in VLP models, a comprehensive approach should consider adversarial perturbations for both modalities. For example, incorporating a text-to-image generation component could be beneficial to observe how adversarial texts lead to variations in generated images.

### Questions
1. What is the time cost associated with using optimal transport theory?
2. How are augmented texts generated?

### Soundness
3

### Presentation
3

### Contribution
3
