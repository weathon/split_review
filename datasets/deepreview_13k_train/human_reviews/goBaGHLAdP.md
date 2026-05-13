# Directional Gradient Projection for Robust Fine-tuning of Foundation Models

- Decision: Accept
- Scores: 6, 5, 6

## Abstract
Robust fine-tuning aims to adapt large foundation models to downstream tasks while preserving their robustness to distribution shifts. Existing methods primarily focus on constraining and projecting current model towards the pre-trained initialization based on the magnitudes between fine-tuned and pre-trained weights, which often require extensive hyper-parameter tuning and can sometimes result in underfitting. In this work, we propose $\textbf{Di}$rectional $\textbf{Gra}$dient $\textbf{P}$rojection (DiGraP), a novel layer-wise trainable method that incorporates directional information from gradients to bridge regularization and multi-objective optimization. Besides demonstrating our method on image classification, as another contribution we generalize this area to the multi-modal evaluation settings for robust fine-tuning. Specifically, we first bridge the uni-modal and multi-modal gap by performing analysis on Image Classification reformulated Visual Question Answering (VQA) benchmarks and further categorize ten out-of-distribution (OOD) VQA datasets by distribution shift types and degree (i.e. near versus far OOD). Experimental results show that DiGraP consistently outperforms existing baselines across Image Classfication and VQA tasks with discriminative and generative backbones, improving both in-distribution (ID) generalization and OOD robustness.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a new method for robust fine-tuning of models for robust fine-tuning that maintains model performance on out-of-distribution datasets while fine-tuning on in-domain data. The authors frame robust finetuning as a multi-objective optimization problem where the two objectives are the original loss function and the distance between the fine-tuned and pretrained weights. They propose an algorithm which projects the gradient of the original loss onto the normal plane of the regularization term’s gradient when the two gradients do not conflict. This approach is evaluated on image classification and VQA tasks, demonstrating improved performance on both in-domain and OOD datasets.

### Strengths
1. The proposed approach makes the projection strength $\omega$ as a learnable parameter, and makes it tunable by a learning rate $\mu$. This makes the approach less sensitive to hyperparameters. The authors show good experimental evidence for the claim.
2. The proposed evaluation of reformulating image classification as a VQA task allows for evaluations on foundation VLMs like PaliGemma.
3. The authors show that the proposed approach can be adapted to PEFT approaches like LoRA.

### Weaknesses
1. While the paper addresses the problem of robust fine-tuning, the proposed approach Directional Gradient Projection appears similar to PCGrad. The problem of conflicting gradients and the  idea of projecting the gradient to the normal plane have been addressed in PCGrad. I would encourage the authors to highlight the unique contributions more clearly.
2. The paper proposes a general approach for robust fine-tuning of foundation models, but the paper focuses on Image classification and VQA tasks. It would be useful to evaluate the approach by fine-tuning open-source LLMs like LLaMA on a multi-task benchmark like MMLU.



### Questions
1. In Table 1, while DiGraP performs well on OOD domains, the performance on the ID domain is poor compared to other approaches like LP-FT and TPGM. By changing the strength of ‘w’, does the approach allow a trade-off to improve performance on ID while compromising OOD performance?
2. In Table 4(b), when the learning rate is increased, which makes the projection strength larger, why does the ID performance improve?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a novel layer-wise trainable method for robust fine-tuning of foundation models, namely DiGraP, which considers the directional information of the gradients. In addition, the authors generalize the method to multi-modal evaluation settings, filling the gap in experiment. Finally, experiments on several tasks demonstrate the effectiveness and robustness of the proposed method.

### Strengths
+This work adopting multi-objective learning to alleviate the previous method's sensitivity to hyper-parameters and underfitting problems, which seems to a relatively novel attempt in the current field.

+The work expands the experimental setting from single-modal to multi-modal, filling the gap in experiments.

### Weaknesses
-Although the work attempts to utilize gradient direction information, there are still deficiencies in the innovation of the method. It looks like a combination of previous work, so the innovation needs to be explained more.

-Sec 4.1 lacks qualitative analysis of the experimental results, especially the reasons why the ID performance on the real domain is worse than LP-FT.

-The article seems to have only conducted a quantitative analysis of hyper-parameters for multi-modal tasks, and corresponding ablation experiments are still needed on singal-modal tasks.

### Questions
Please refer to the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents the Directional Gradient Projection (DiGraP) method, designed for robust fine-tuning of foundation models, particularly in the face of distribution shifts. DiGraP introduces a novel approach that leverages gradient directionality to resolve conflicts between optimization objectives, aiming to enhance model robustness across in-distribution (ID) and out-of-distribution (OOD) data. Unlike traditional approaches that primarily rely on weight projection and regularization, DiGraP utilizes directional information for gradient adjustments, bridging multi-objective optimization and regularization. The method’s effectiveness is demonstrated across image classification and multi-modal tasks (Visual Question Answering - VQA), outperforming baseline methods in both ID and OOD performance.

### Strengths
DiGraP’s gradient-based approach is innovative, incorporating directional information to handle conflicting objectives in a way that traditional regularization does not.

The expansion from uni-modal to multi-modal evaluation settings represents the contribution of robust fine-tuning.

Comprehensive ablation studies and sensitivity analyses of the hyper-parameters (e.g., projection strength) strengthen the validity of the findings, showing DiGraP’s robustness and effectiveness across different configurations.

The paper clearly explains the design choices of DiGraP, with detailed descriptions of its components.

Visualizations and tables effectively illustrate the experimental results and the model’s behavior under varying projection strengths.

### Weaknesses
There are many public unimodal and multimodal foundation models, e.g., MAE, CLIP, BEiT3, LLaVa, etc. It is unclear why ResNet50 and PaliGemma are selected as foundation models. The ResNet50 pretrained in a supervised manner on ImageNet can hardly be deemed as foundation models. The PaliGemma is pretrained on a broad mixture of large-scale vision-language tasks. Whether the conclusion of this paper holds across other, more general foundation models, e.g., CLIP or LLaVa, is questionable.

Although DiGraP demonstrates improved performance in near OOD settings, its performance on far OOD tasks remains limited compared to other methods. The authors acknowledge this trade-off between ID/near OOD and far OOD robustness, but a deeper investigation into addressing this limitation would enhance the model’s versatility.

The model’s gradient projection mechanism, while theoretically sound, lacks interpretability in how projection strength decisions impact specific instances.

The figures in Appendix have too small font.

### Questions
Could additional techniques be incorporated to enhance DiGraP’s performance on far OOD datasets without sacrificing ID and near OOD performance?

Could the authors provide more insights into how the projection strength parameter adapts dynamically across different layers and tasks, especially in multi-modal settings?

### Soundness
3

### Presentation
3

### Contribution
3
