# Positive-Unlabeled Diffusion Models for Preventing Sensitive Data Generation

- Decision: Accept
- Scores: 8, 5, 5, 6

## Abstract
Diffusion models are powerful generative models but often generate sensitive data that are unwanted by users,
mainly because the unlabeled training data frequently contain such sensitive data.
Since labeling all sensitive data in the large-scale unlabeled training data is impractical,
we address this problem by using a small amount of labeled sensitive data.
In this paper,
we propose positive-unlabeled diffusion models,
which prevent the generation of sensitive data using unlabeled and sensitive data.
Our approach can approximate the evidence lower bound (ELBO) for normal (negative) data using only unlabeled and sensitive (positive) data.
Therefore, even without labeled normal data,
we can maximize the ELBO for normal data and minimize it for labeled sensitive data,
ensuring the generation of only normal data.
Through experiments across various datasets and settings,
we demonstrated that our approach can prevent the generation of sensitive images without compromising image quality.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work proposes positive-unlabeled diffusion models that prevent the generation of sensitive data using unlabeled and sensitive data. To address the issue that labeling all sensitive data in the large-scale unlabeled training data is impractical, the authors propose to use a small amount of labeled sensitive data and then propose an approach based on PU learning to train a binary classifier to distinguish between positive and negative data. Simulation results show that the proposed method does effectively prevent generation of sensitive data. Interesting work.

### Strengths
See above summary.

### Weaknesses
I wouldn't count it as a weakness, but more like a further discussion.

### Questions
I assume that for this method to work, the small amount of labeled sensitive data should well represent the characteristics/properties of all sensitive data. I am just wondering what will happen if there is a mismatch? For example, in the MNIST example that the authors show in the paper, what if the labeled sensitive dataset includes some but not all odd numbers?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents positive-unlabeled diffusion models to address the challenge of generating sensitive data by diffusion models. Traditional training methods often lead to the inclusion of unwanted sensitive data, prompting the authors to propose a novel approach that utilizes a small amount of labeled sensitive data alongside unlabeled data, which may contain both normal and sensitive instances. The core idea is to maximize the evidence lower bound (ELBO) for normal data using only unlabeled and sensitive data, enabling the generation of only normal content. By treating the unlabeled data distribution as a mixture of normal and sensitive distributions, the approach allows effective model training without needing extensive labeled normal data.

The overall logic of the paper is coherent, providing a detailed introduction to the relevant technologies and concepts. In particular, the work appears to be well-motivated and the methodology is reasonable. However, the rationale for the proposed method and the challenges associated with it, as well as comparisons with other methods, are not thoroughly explained. For instance, the paper does not clarify why prior methods cannot be directly adapted to diffusion models. The underlying reasons for the unique characteristics of the diffusion model or the challenges inherent in the adaptation process remain unaddressed.

### Strengths
- Paper studies an important topic that is highly related to diffusion model and privacy protection.
- Paper is easy to follow.

### Weaknesses
 - The methodological details, and the rationale for adopting the methods, are rather confusing.
- limited contribution and novelty.
- The selection of datasets for the experiments and the design of the experimental methods seem to be unreasonable.


### Questions
1. In Section 4, the disadvantages of previous work and the advantages of the proposed method seem to be inadequately explained and presented. For instance, in Section 4.1, the statement "Moreover, it cannot work well in the PU setting because it assumes all unlabeled data are normal" raises the question of what specific issues arise from assuming that all unlabeled data are normal, yet this point is not well articulated.
2. In Section 4.2, a work related to "semi-supervised anomaly detection" is mentioned, which appears to be highly relevant to the proposed method. However, the paper does not clarify why this work cannot be directly adapted to diffusion models. What are the challenges and difficulties associated with this transition?
3. The experiments involve selecting several classic datasets and categorizing them into two classes. However, the rationale for these datasets being sufficiently representative of sensitive and non-sensitive data is unclear. Although these are binary classification tasks, the boundaries between sensitive and non-sensitive data do not seem to be so distinct. Additionally, in Section 5.4.1 on page 9, it states, "since the ratio of normal data to sensitive data in the unlabeled data U is 10:1." Please clarify the reasoning behind this choice of ratio.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes a novel method to prevent the generation of sensitive images from Diffusion Models. It can estimate the evidence lower bound for normal images without using labeled normal images. Experiments show that the proposed method can alleviate the generation of sensitive images while maintaining high image quality.

### Strengths
This paper has the following strengths:
- It is helpful for estimating the evidence lower bound for normal images without relying on labeled examples.
- The writing of the method part is clear which makes the method easy to understand.

### Weaknesses
This paper has the following weaknesses:
- The presentation of qualitative examples is not very good. The images in Figure 2 and Figure 3 are small and blurry. Besides, as mentioned by the authors, "Since the same random seed was used for both training and generation, the generated images are largely similar". It is harder to see the difference clearly.
- This paper only tests the performance of the proposed method. It does not have a comparison of previous closely related works.
- The setting/scenario is not very close to real-world **sensitive** images. For example, it treats even numbers as normal while odd numbers as sensitive. It would be better to consider more real-world common scenarios/settings as in previous works [1, 2].
- It does not conduct experiments using popular SD such as SD v 1.4, SD v2.0, and SD XL.

### Questions
The questions/suggestions are mainly based on weaknesses.
- Could authors compare the performance of the proposed method with the works in the related work section? 
- Could authors conduct experiments using SD v1.4 and SD v2.0?
- It would be better to contain more clear images in the Appendix.
- Some sentences in the abstract are not very clear. For example, 'Our approach can approximate the evidence lower bound
(ELBO) for normal (negative) data using only unlabeled and sensitive (positive) data.' Does this mean the sensitive data are unlabeled? But the abstract also says 'we address this problem by using a small amount of labeled sensitive data.'

### Soundness
2

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
4

### Summary
The paper proposes a new scenario in sensitive generation prevention for DMs, where only an unlabeled dataset and a sensitive dataset are available, rather than a fully labeled training dataset. The authors integrate positive-unlabeled learning methods into DMs, and experimental results demonstrate superior performance across multiple datasets.

### Strengths
1. The writing is clear and easy to follow.
2. The scenario is new and intriguing in the context of DM's sensitive generation prevention.
3. The experimental results are strong in most cases.

### Weaknesses
The weakness lies in the theory part. There is no guarantee of why the proposed method works, making it seem like positive-unlabeled learning methods are directly applied to DMs. Specifically:

In Eq(7), the $L_{DM}$ comes from analyzing the lower bound for $\log p_{\theta}(x_0)$. However, in Eq(13), there is a linear combination of two distributions, and following Eq(7), it is unclear whether this could be decomposed into terms relating to $l_{BCE}$ for the two given distributions (such as finding a lower bound $\log (\beta p_{u}(x) + (1-\beta) p_{N}(x))$). More insights within the theoretical analysis would help validate whether the proposed positive-unlabeled learning methods can indeed be directly implemented as described in the paper.

Besides, there seems to be a few typos, such as it should be \citet in L 253.

### Questions
Question:

See weakness. Could the authors provide either proof or assumptions that help explain the proposed methods from the perspective of DM's learning process? I believe the results look promising, and with a solid theoretical analysis, I would consider increasing my score.

### Soundness
3

### Presentation
3

### Contribution
2
