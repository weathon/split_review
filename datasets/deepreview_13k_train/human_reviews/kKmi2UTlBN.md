# Cosine Similarity Knowledge Distillation for Individual Class Information Transfer

- Decision: Reject
- Scores: 3, 5, 6

## Abstract
Previous logits-based Knowledge Distillation (KD) have utilized predictions about multiple categories within each sample (i.e., class predictions) and have employed Kullback-Leibler (KL) divergence to reduce the discrepancy between the student’s and teacher’s predictions. Despite the proliferation of KD techniques, the student model continues to fall short of achieving a similar level as teachers. In response, we introduce a novel and effective KD method capable of achieving results on par with or superior to the teacher model’s performance. We utilize teacher and student predictions about multiple samples for each category (i.e., batch predictions) and apply cosine similarity, a commonly used technique in Natural Language Processing (NLP) for measuring the resemblance between text embeddings. This metric's inherent scale-invariance property, which relies solely on vector direction and not magnitude, allows the student to dynamically learn from the teacher's knowledge, rather than being bound by a fixed distribution of the teacher's knowledge. Furthermore, we propose a method called cosine similarity weighted temperature (CSWT) to improve the performance. CSWT reduces the temperature scaling in KD when the cosine similarity between the student and teacher models is high, and conversely, it increases the temperature scaling when the cosine similarity is low. This adjustment optimizes the transfer of information from the teacher to the student model. Extensive experimental results show that our proposed method serves as a viable alternative to existing methods. We anticipate that this approach will offer valuable insights for future research on model compression.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The author proposes a method for knowledge distillation (KD) using cosine similarity, which yields favorable results on commonly used datasets such as CIFAR-100 and ImageNet. Despite its significant effectiveness, the paper still faces several issues that currently place it significantly below the acceptance threshold for ICLR.                          

Issues:
1. The author's concept of cosine distance is commendable but lacks a comparison and discussion with existing KD methods based on KL divergence, such as SHAKE [1] and DKD [2]. Incorporating relevant comparative analysis in the next version would be beneficial.
2. The paper does not adequately explore the relationship between the proposed method and existing KD techniques; it merely provides result comparisons. This leaves readers struggling to understand the unique significance of the proposed approach. A deeper discussion of the differences between these two types of KD methods is needed in the related work section.
3. The motivation behind the entire loss function is unclear. While the author introduces a temperature parameter (T) in Equation 3, its specific setting is absent in subsequent explanations. In Equation 9, where two loss functions are introduced, there is only one balancing factor, leading to reader confusion.
4. There are overall writing issues in the paper, including citation formatting and writing errors such as inconsistent tenses and mixed usage of abbreviations (e.g., Fig. vs. Figure, Table vs. Tab.). Careful proofreading and editing are required to enhance professionalism.
5. Figure 4 lacks a detailed explanation, making it challenging for readers to understand the purpose of the experiment and the impact of batch size on the results. More background information and clarification are needed.
I hope this feedback helps in further improving your research. 

[1] Shadow Knowledge Distillation: Bridging Offline and Online Knowledge Transfer. 2022. In NeurIPS.  
[2] Decoupled Knowledge Distillation. 2022. In CVPR.

### Strengths
See summary

### Weaknesses
1. The author's concept of cosine distance is commendable but lacks a comparison and discussion with existing KD methods based on KL divergence, such as SHAKE [1] and DKD [2]. Incorporating relevant comparative analysis in the next version would be beneficial. Specifically, the paper needs to clarify how the scale-invariance property of cosine similarity offers advantages over the distribution matching objective of KL divergence. The current discussion does not sufficiently explain why relaxing the strict matching constraint of KL divergence is beneficial for knowledge transfer in this context.

2. The paper does not adequately explore the relationship between the proposed method and existing KD techniques; it merely provides result comparisons. This leaves readers struggling to understand the unique significance of the proposed approach. A deeper discussion of the differences between these two types of KD methods is needed in the related work section. The paper should delve into the theoretical underpinnings of why cosine similarity might be a better metric for transferring 'dark knowledge' compared to KL divergence, beyond just empirical observations.

3. The motivation behind the entire loss function is unclear. While the author introduces a temperature parameter (T) in Equation 3, its specific setting is absent in subsequent explanations. In Equation 9, where two loss functions are introduced, there is only one balancing factor, leading to reader confusion. Furthermore, the role of the temperature parameter in the cosine similarity loss needs more clarification. It is unclear how the temperature affects the learning dynamics and the transfer of knowledge.

4. There are overall writing issues in the paper, including citation formatting and writing errors such as inconsistent tenses and mixed usage of abbreviations (e.g., Fig. vs. Figure, Table vs. Tab.). Careful proofreading and editing are required to enhance professionalism.

5. Figure 4 lacks a detailed explanation, making it challenging for readers to understand the purpose of the experiment and the impact of batch size on the results. More background information and clarification are needed. The paper should explain why batch size affects the performance of the proposed method and how this relates to the underlying principles of cosine similarity-based knowledge distillation.

### Questions
See summary

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The author sims to involve a cosine similarity KD loss based on a batch-level KD signal into student model learning. A combination of fix-temp softmax and a adaptive-temp softmax is also introduced in KD process. Comprehensive experiments including entropy analyses and ablation study are conducted.

### Strengths
S1. clearly introduce the research gap between existing KD techniques and the proposed

S2. Comprehensive experiments are conducted

### Weaknesses
W1. Cosine similarity KD loss is the key but the explanation is unclear

W2. presentation structure might be reorganized

W3. experimental results are not convincing due to unclear methodology

### Questions
C1. In Eq. (2) and (3), what does ":" mean? What's the difference between "[:,j]" in (2) and "[i,:]" in (3)? Does "[:,j]" mean by concatnating all vectors from 1 to j (if so, please refer to C3)? It said that p_s, p_t \in R^{B×C} which is a matrix. How to compute the consin similarity for two matrix based on Eq (1)? 

C2. By the explanation in the below of Eq (3), it seems that the loss only focuses on one class j? I got the answer Yes from Eq (9). So it's suggested to make the definition clearer or reorganize the presentation order. It's better to explain all notations with a formal way without the assumption that audiences also understand what's presented.

C3. Though cosine similarity is scale-invariant, the significance of a cosine similarity value depends on vector length (i.e., the dimension of the vector). For a 200-d vector, 0.4 may be a relative large value. But for a 5-d vector, 0.7 does not mean two vectors are similar. For classification, the number of classes and  batch size are two factors to affect the vector length. That means, even for the same task, for difference batch size, the proposed would get different student models.

C4. The authors must take a long time to conduct extensive experiments in following sections to show the advantage of the proposed. However, concerns exist in the results due to unclear definitions and intuitions (please refer to C1 to C3)


==========

The authors response help my understanding on the methodology. I would like to raise my review score.

However, the concern is still on the batch-wise cosine similarity. Overall, I don't think it meet the acceptance bar.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a new Knowledge Distillation (KD) approach that relies on cosine similarity to effectively transfer knowledge about each specific class from the teacher model to the student model during the knowledge distillation process. By treating the predictions from student and teacher models as vectors, the method utilizes the scale-invariant property of cosine similarity to optimize student learning. The authors also introduced the "Cosine Similarity Weighted Temperature" (CSWT) technique to enhance the knowledge transfer efficiency.

### Strengths
1. This work employs cosine similarity for individual class information transfer, which is a departure from traditional KD techniques.
2. Efficient Learning from the student model. The authors of the paper leverage the scale-invariant property of cosine similarity to optimize the student's learning from the teacher.
3. With the introduction of the "Cosine Similarity Weighted Temperature" (CSWT) technique the student model refines the knowledge transfer process to obtain the most relevant information for every sample.

### Weaknesses
1. The proposed model depends on the batch size. This could be a limitation when the batch size that needs to be adjusted for reasons like memory constraints.

### Questions
1. Can this learning paradigm be used in an Out-of-distribution task or experiment?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
