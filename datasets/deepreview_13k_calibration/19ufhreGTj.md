# Understanding Dimensional Collapse in Cross-Modal Feature Distillation

- Decision: Reject
- Avg Score: 5.80
- Scores: 6, 5, 6, 6, 6

## Abstract
To overcome limited computing resources and the complexity of sensor configurations in deploying multi-modal neural networks in real-world applications, cross-modal knowledge distillation (CMKD) aims to transfer valuable information from a pretrained teacher model to a deployable student model with the target modality. Despite the successful applications of CMKD in various fields, our understanding of knowledge transfer across different modalities remains insufficient to fully explain the efficacy of feature distillation. In this work, we investigate the relationship between the distributional shifts across modalities, referred to as the modality gap, and its impact on the effectiveness of CMKD, particularly focusing on the problem of cross-modal feature distillation. We first hypothesize and empirically validate that the modality gap between the teacher and student causes dimensional collapse in the student's feature space. To prevent such inefficiency, we propose a Cross-modal Information Bottleneck Approximation (CIBA) scheme aimed at extracting and transferring modality-general features from the teacher model. Lastly, we experimentally demonstrate that our distillation strategy effectively reduces the dimensional collapse in the student model, thereby achieving improved performance for various real-world multi-modal datasets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, the author mainly propose to solve the problem of dimensional collapse caused by modality gap in cross-modal knowlegde distillation task. Firstly, the author demonstrates the impact of modality gap on cross-modal features theoretically and empirically. To combat with this issue, a Cross-modal Information Bottleneck Approximation (CIBA) framework is proposed that extracts modality-general features through a bottleneck structure, meanwhile aligning teacher and student features with an additional loss. Experiments on several datasets demonstrates the performance of CIBA.

### Strengths
1. The paper is well-written, which is quite easy to follow.
2. The author sufficiently demonstrates that modality gap can cause dimensional collapse, leading to suboptimal performance.

### Weaknesses
1. My main concern is about the generalizability of the method. As mentioned in problem statements and limitations, the theorem is established on linear extractor, which is inconsistent with practical applications where non-linear encoders are widely applied. Under such conditions, the proposed concept of modality-general and modality-specific parts could be vague since the better capacity of the encoders. I can truly understand the difficulty of theorical provement with non-linear extractors, while the direct application of CIBA seems to be accessible. Can you provide further results of CIBA compared to SOTAs with more powerful encoders on current datasets (RAVDESS and MM-IMDB) to prove the superiority?
2. In the method part, a bottleneck structure is utilized to capture mutual modality information. From my point of view, the dimension of the bottleneck feature may be a crucial parameter affecting the granularity of the extracted information. Performance seems to be fluctuant with chaning values of the param according to Fig.5(c). Can you provide more ablation on this param on more datasets? How do you choose the best bottleneck dimension?
3. The author mainly focus on the introduction and demonstration of modality gap's impact on dimensional collapse, while the introduction of method seems to be ordinary and unremarkable. Besides, since the information bottleneck structure was proposed by earlier research, and the proposed loss is a direct combination of generation loss and KL loss, the novelty of the paper is somehow limited.

### Questions
Please refer to the cons part. I will moderately raise my score if the authors can provide further experimental results and answer my questions.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper titled "Understanding Dimensional Collapse in Cross-Modal Feature Distillation" investigates the challenges of transferring knowledge across different modalities in multi-modal neural networks, specifically focusing on the problem of dimensional collapse in cross-modal feature distillation (CMFD). The authors hypothesize that the modality gap between the teacher and student models leads to dimensional collapse in the student's feature space, which degrades the quality of knowledge distillation. To address this, they propose a novel framework called Cross-modal Information Bottleneck Approximation (CIBA), which aims to extract and transfer modality-general features from the teacher model to sub-dimensions of the student model's features. The paper empirically demonstrates that CIBA effectively reduces dimensional collapse and improves performance on various real-world multi-modal datasets, including RAVDESS (Audio-Image), MM-IMDB (Image-Text), and nuScenes (LiDAR-Camera). The key contributions of the paper are the theoretical and empirical investigation of the modality gap's impact on CMKD, the proposal of the CIBA framework, and the validation of its effectiveness across different modalities.

### Strengths
The paper proposes a novel cross-modal knowledge distillation (CMKD) method by focusing on the issue of dimensional collapse in cross-modal feature distillation. The concept of modality gap and its impact on the efficacy of feature distillation is a fresh approach to understanding the limitations of CMKD. The proposal of the Cross-modal Information Bottleneck Approximation (CIBA) scheme is creative and addresses a significant problem in transferring knowledge across different modalities.

The paper is well-written. The figures and tables are clear and effectively support the textual content.

### Weaknesses
The contribution is incremental.

I feel the information bottleneck approximation idea has been used extensively.

While the proposed method is shown to outperform baseline approaches, it is unclear how it compares to the most recent and advanced techniques in the field, i.e., DML[1], DKD[2], DIST[3], C2KD[4].

### Questions
How does the performance of CIBA compare when the assumption of orthogonality between modality-general and modality-specific features is relaxed? 

How does CIBA differ from the previous CMKD approaches?

How sensitive is the CIBA framework to the choice of hyperparameters, particularly the dimension of the bottleneck feature (H)?

### Soundness
4

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
3

### Summary
This paper tries to address the challenges associated with deploying multi-modal neural networks in real-world applications, specifically focusing on the constraints of limited computing resources and complex sensor configurations. The authors explore Cross-Modal Knowledge Distillation (CMKD) as a solution for transferring knowledge from a pretrained teacher model to a more deployable student model tailored to a target modality. Despite the advancements in CMKD across various domains, the paper identifies a gap in understanding how distributional shifts between modalities—referred to as the modality gap—affect the efficacy of feature distillation. The study hypothesizes and empirically demonstrates that a significant modality gap leads to dimensional collapse within the student model's feature space, undermining performance. To mitigate this issue, the authors introduce the Cross-modal Information Bottleneck Approximation (CIBA) scheme, designed to extract and transfer modality-general features from the teacher model effectively. Experimental results on diverse real-world multi-modal datasets confirm that the proposed CIBA method successfully reduces dimensional collapse in the student model, resulting in enhanced performance. This work contributes a deeper understanding of the interplay between modality gaps and knowledge transfer in CMKD, offering a practical solution to improve the deployment of multi-modal neural networks under resource constraints.

### Strengths
1. The theoretical and empirical investigation of the "modality gap"—the distributional shifts between different modalities—and its detrimental effect on CMKD, specifically leading to dimensional collapse in the student model’s feature space.

2. CIBA extracts modality-general features from the teacher model and transfers them to sub-dimensions of the student’s features. This method mitigates the dimensional collapse, ensuring more robust and effective knowledge transfer.

### Weaknesses
1. Since RAVDESS is a relatively small size dataset. Do you try to work on VGGSound?

### Questions
N/A

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper investigates the relationship between distributional shifts across modalities and their impact on the effectiveness of cross-modal knowledge distillation (CMKD), specifically addressing the issue of cross-modal feature distillation. The authors hypothesize and validate that the modality gap between the teacher and student models may lead to dimensional collapse in the student’s feature space. To address this, they propose a Cross-modal Information Bottleneck Approximation (CIBA) scheme aimed at extracting and transferring modality-general features from the teacher model. Experimental results demonstrate that the proposed distillation strategy effectively mitigates dimensional collapse in the student model.

### Strengths
1.	The authors successfully propose and validate that the modality gap between the teacher and student models can lead to dimensional collapse in the student’s feature space.

2.	A novel Cross-modal Information Bottleneck Approximation (CIBA) scheme is introduced to extract and transfer modality-general features from the teacher model.

3.	Experimental results across various loss functions and tasks provide strong evidence for the effectiveness of the proposed method.

### Weaknesses
1.	The work is predicated on the assumption of linear feature extractors; however, in practical applications, most feature extractors are non-linear.

2.	In the MM-IMDB dataset, the observed improvement is marginal. Could you please provide a more detailed explanation for this finding?

### Questions
See the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper investigates the problem of dimensional collapse in cross-modal feature distillation (CMFD), where a student model trained on one modality aims to mimic the feature representations of a teacher model trained on a different modality. The authors hypothesize that the distributional shift, or "modality gap", between the teacher and student modalities leads to the student's feature space collapsing to only capture the modality-general features, resulting in suboptimal distillation performance. To address this issue, the authors provide in-depth analysis on how distributional shifts across different modalities and propose a Cross-modal Information Bottleneck Approximation (CIBA) scheme that extracts and transfers the modality-general features from the teacher to the student, allowing the student to effectively span both modality-general and modality-specific feature spaces.

### Strengths
1. Research about cross-modal knowledge distillation (CMKD) on the feature view is an important topic for multimodal learning and knowledge distillation. This paper analyses the dimensional collapse induced by modality gap and propose Cross-modal Information Bottleneck Approximation (CIBA) to disentangle the general and specific knowledge, which is novel and practical.
2. Utilizing the Mean Squared Error (MSE) loss for feature distillation (FD) is reasonable and suitable for the subsequent theoretical analysis.
3. This work is a good extension of the modality focusing hypothesis, and gives a solid analysis and detailed solutions.
4. This work is well written and organized. Extensive experiments on Audio-Image, Image-Text, and LiDAR-Camera crossmodal transfer are conducted.

### Weaknesses
1. Modality gap is widely studies in multimodal learning, and this paper does not give a review of previous modality gap analysis. Moreover, the cross-modal knowledge distillation on logit-level method [r1] is not mentioned and analysed.
[r1] Huo F, Xu W, Guo J, et al. C2KD: Bridging the Modality Gap for Cross-Modal Knowledge Distillation[C]//Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2024: 16006-16015.
2. The RAVDESS, MM-IMDB, and nuScenes have limited class categories. Large-scale experiments like conducting experiments on VGG-Sound (or subset) will make the paper more convincing.
3. Related works about the 'Cross-modal knowledge distillation' are somewhat out-of-date, only one paper published in 2023 is mentioned.
4. The proposed method is somewhat similar to online distillation [r1] and task-oriented feature distillation [r2]. How about the performance of directly employing task-oriented feature distillation [r2] on cross-modal feature distillation?
[r2]Zhang L, Shi Y, Shi Z, et al. Task-oriented feature distillation[J]. Advances in Neural Information Processing Systems, 2020, 33: 14759-14771.

### Questions
1. How is the Figure 1 formulated? The manuscript does not mention the details. I think it is important for the motivation of modality-general and modality-specific knowledge analysis.
2. How about directly apply unimodal knowledge distillation on crossmodal knowledge distillation? Could the proposed method be integrated into SOTA methds?

[r1] Zhang L, Shi Y, Shi Z, et al. Task-oriented feature distillation[J]. Advances in Neural Information Processing Systems, 2020, 33: 14759-14771. 

[r2] Huang T, You S, Wang F, et al. Knowledge distillation from a stronger teacher[J]. Advances in Neural Information Processing Systems, 2022, 35: 33716-33727.

### Soundness
3

### Presentation
3

### Contribution
2
