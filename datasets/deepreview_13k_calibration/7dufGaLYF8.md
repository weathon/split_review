# Sequence Denoising with Self-Augmentation for Knowledge Tracing

- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 3, 5, 3

## Abstract
Knowledge tracing (KT) aims to predict students' future knowledge levels based on their historical interaction sequences. Most KT methods rely on interaction data between students and questions to assess knowledge states and these approaches typically assume that the interaction data is reliable. In fact, on the one hand, factors such as guessing or slipping could inevitably bring in noise in sequences. On the other hand, students' interaction sequences are often sparse, which could amplify the impact of noise, further affecting the accurate assessment of knowledge states. Although data augmentation which is always adopted in KT could alleviate data sparsity, it also brings noise again during the process. Therefore, denoising strategy is urgent and it should be employed not only on the original sequences but also on the augmented sequences. To achieve this goal, we adopt a plug and play denoising framework in our method. The denoising technique is adopted not only on the  original and the enhanced sequences separately during the data augmentation process, but also we explore the hard noise through the comparison between the two streams. During the denoising process, we employ a novel strategy for selecting data samples to balance the hard and soft noise leveraging Singular Value Decomposition (SVD). This approach optimizes the ratio of explicit to implicit denoising and combines them to improve feature representation. Extensive experiments on four real-world datasets demonstrate that our method not only enhances accuracy but also maintains model interpretability.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents a Sequence Denoising with Self-Augmentation for Knowledge Tracing (SDAKT) model aimed at improving knowledge tracing by reducing the impact of noise in students' interaction sequences through explicit and implicit denoising techniques, leveraging Singular Value Decomposition (SVD) for both noise detection and feature extraction. Experimental results show significant improvements in model robustness and predictive accuracy across multiple datasets, indicating the efficacy of the proposed denoising framework.

### Strengths
- An approach to handling noise in knowledge tracing through two-stream denoising.
- Utilize SVD for explicit and implicit denoising, improving robustness and accuracy.
- Demonstrate performance gains across different standard datasets.

### Weaknesses
 - The paper overlooks some important baselines. For instance, HD-KT [1], a relevant method that also addresses denoising for guessing and slipping issues, is not discussed or compared, which limits the contextual understanding of the model's contributions. Additionally, more works in sequence denoising, as mentioned in the Related Work section, should be considered as baselines to better validate the effectiveness of the proposed method.

- The main technical contribution of the paper is the use of SVD decomposition to analyze informative signals. However, this approach is relatively simple and has been applied in other fields. Additionally, the paper lacks a thorough discussion on computational overhead, particularly the time-intensive nature of SVD calculations, which could impact real-time feasibility in large-scale applications.

- There are minor writing issues: Missing punctuation at the end of the formula; inconsistent of reference format and so on.

### Questions
- Could this paper compares the proposed method with KT methods that also perform denoising or with approaches from sequence denoising to verify the effectiveness of the proposed approach?

- In the ablation study, I noticed that the performance of CL4KT-DA and CL4KT-ID on Algebra06 is identical. Could this paper explain the reason for this?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces SDAKT that addresses noise in both original and augmented sequences using explicit and implicit denoising techniques. The main innovation is combining explicit and implicit denoising approaches during the data augmentation process, using SVD to balance between hard and soft noise reduction. The method denoises both original and augmented sequences to improve feature representation.

### Strengths
- This paper studies the important problem of noisy interactions and sparse distribution in knowledge tracing data.
- The paper structure of the solution is clear and easy to understand.

### Weaknesses
 - The motivation for noise in KT interaction sequences is poorly defined. The paper doesn't clearly quantify the extent of noise in real KT datasets or demonstrate its impact empirically.
- This article was unable to find comparison results for other baselines.
- The artificial noise injection experiments only use Gaussian noise, which may not reflect realistic noise patterns in educational data.
- There may be confusion between the model names SDAKT and CL4KT-DA.
- Limited analysis of computational overhead introduced by the denoising module.

### Questions
1 What is “unreliable knowledge states” (line 55) ？

2 Why KT datasets sparsity problems amplify noise?

3 “three errors, two correct” in (Line 65 q1) is inconsistent with Figure 1.

4 Why is the performance of the sequence model DKT-ED worse than the original DKT?

5 Why is variable Gaussian noise used in Table 2? How does variable noise affect the KT model?

### Soundness
3

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
3

### Summary
This paper studies knowledge tracing from the perspective of denoising original interaction sequences. To measure the degree of outlier, singular values from Singular Value Decomposition (SVD) are used.

### Strengths
(1) Singular values are used to measure the degree of outliers in interaction sequences.

(2) Soft and hard denoising strategies are proposed. Soft corresponds to maximize the maximum singular value. Hard corresponds to explicitly mask some nosiy examples.

(3) The experiments are conducted on three backbones to test the effectiveness of the proposed method.

### Weaknesses
(1) Explicit denosing seems to not be very effective. As shown in Table 1, DKT-ED performs much worse than DKT. Moreover, the combination of explicit denoisng and implicit denoising is not very beneficial, which is also reflected in Table 1.

(2) Some parts of this paper are questionable. For example, why is SVD performed for vectors, as shown in Eq 6 and 7? “Question q1 was answered incorrectly three times at first and correctly two times latter” is not consistent with the content in Figure 1. Why f_{den} can play a role of removing noise is not introduced. Why using data augmentation in the denoising part?

(3) Some important details are missing. What is the meaning of q_d? Figure 2 is not clear. How to calculate the influence weights in “in traditional KT methods, the influence weights” is not explained and the references are not mentioned. The effect of lambda is not very reasonable, as shown in Figure 5.

### Questions
Why maximizing the largest singular value can reduce noise.

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This study addresses the issue of noise in both original and augmented sequences within the field of knowledge tracing and proposes a self-enhanced sequence denoising knowledge tracing algorithm (SDAKT). The effectiveness of the algorithm is validated through comparison with three baseline algorithms. Further experimental results show that, compared to models without any denoising operations, SDAKT is more robust to noise.

### Strengths
1. The motivation of addressing noises in knowledge tracing is well explained.
2. The experiments have shown certain improvements especially regarding addressing noises.

### Weaknesses
1. The algorithm design has not been adequately explained. The rationale for using Equation (8) to quantify the noise in real data is not thoroughly explained. Since the singular vectors of the matrices before and after denoising differ, directly comparing the singular values seems questionable and may not provide a meaningful measure of the noise.

2. The algorithm's performance is not convincing. Although the denoising-enhanced version of the algorithm shows some improvement in AUC and RMSE metrics compared to baselines, the gains are relatively modest. Additionally, the algorithm includes both explicit and implicit denoising mechanisms. However, as seen in Table 1, the performance of the SDAKT algorithm does not significantly differ from using only one of these denoising strategies. This suggests that the combination of both denoising approaches does not substantially enhance the overall performance. One of the key innovations of this paper is the fusion of explicit and implicit denoising strategies, yet the results indicate that this fusion does not demonstrate clear advantages in practice.

3. Many writing and presentation problems: The paper suffers from inconsistencies in formatting and imprecise language. For example, in Equations (6) and (7), embedding vectors are inappropriately subjected to singular value decomposition, when matrix forms should have been used. Additionally, the citation format in line 196 is incorrect, and the reference formatting is inconsistent throughout the paper. Finally, there is a discrepancy between the description and Equation (4) in the text: while the description refers to the original sequences, the equations present denoised sequences instead.

### Questions
I would appreciate the authors to respond to weaknesses mentioned above.

### Soundness
2

### Presentation
2

### Contribution
2
