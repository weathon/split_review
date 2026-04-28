# Enhancing Near OOD Detection in Prompt Learning: Maximum Gains, Minimal Costs

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 6, 5, 3

## Abstract
Prompt learning has shown to be an efficient and effective fine-tuning method for vision-language models like CLIP. While numerous studies have focused on the generalisation of these models in few-shot classification, their capability in near out-of-distribution (OOD) detection has been overlooked. A few recent works have highlighted the promising performance of prompt learning in far OOD detection. However, the more challenging task of few-shot near OOD detection has not yet been addressed. In this study, we investigate the near OOD detection capabilities of prompt learning models and observe that commonly used OOD scores have limited performance in near OOD detection. To enhance the performance, we propose a fast and simple post-hoc method that complements existing logit-based scores, improving near OOD detection AUROC by up to 11.67\% with minimal computational cost. Our method can be easily applied to any prompt learning model without change in architecture or re-training the models. Comprehensive empirical evaluations across 13 datasets and 8 models demonstrate the effectiveness and adaptability of our method.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper explores the few-shot near-OOD identification capabilities of various prompt-based vision-language models (VLMs), such as CLIP. To enhance the identification of near-OOD samples in these models, it introduces a set of post-hoc metrics based on existing logit-based OOD techniques, which can be applied across a wide range of prompt-based VLMs.

### Strengths
I believe the paper addresses an important and often overlooked problem. The proposed Marginal Logit Score is simple and appears effective across a wide range of models and datasets, outperforming conventional OOD metrics in near-OOD detection. The metric is intuitively appealing and supported by experimental results.

### Weaknesses
-The authors mention that the margin scale is learned from the few-shot ID examples provided. However, there is insufficient analysis of how the number of shots impacts parameter learning and, ultimately, near-OOD detection performance. Specifically, the paper lacks a detailed investigation into the sensitivity of the learned margin scale to the number of few-shot examples. It is unclear whether the learned margin scale generalizes well across different few-shot settings, or if it is prone to overfitting when the number of shots is very low. This could lead to unstable near-OOD detection performance in low-data regimes.

- Although far-OOD detection is not the focus of this work, far-OOD samples are important for a model’s overall effectiveness in identifying OOD samples, especially in real-world scenarios. From this perspective, it is crucial to compare the performance of MLE with MCM on datasets or in scenarios where both near- and far-OOD samples are present. The paper does not provide a clear picture of how the proposed method performs when faced with a mixture of both near and far OOD samples, which is a more realistic scenario in practical applications. This makes it difficult to assess the overall robustness of the method.

### Questions
- I believe the paper would benefit from an ablation study on how the number of shots impacts the learning of the margin scale hyperparameter and, subsequently, the near-OOD detection performance.

- How does MLE compare to MCM on datasets that contain both near- and far-OOD samples?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In response to the near OOD dataset and CLIP, this paper designed an OOD score based on logit, referred to as MLS. MLS computes the difference between the logit scores inferred by CLIP and a newly introduced complementary score known as the Context score. This approach effectively enhances the separation between ID samples and near OOD samples, resulting in a significant performance improvement.

### Strengths
1.	They introduced an MLS score based on the observation that the logit scores from CLIP, such as max logit, are positively correlated with their proposed context score. This MLS score reduces the overlap between ID data and near ID data compared to the max logit score.

2.	The MLS scoring method proposed in this paper requires no modifications to the model architecture and does not involve retraining. This characteristic makes it efficient and highly adaptable.

### Weaknesses
1. The authors mention that logit score and context score are proportional, but this claim is not sufficiently accurate.
a) The paper presents the case that Maxlogit is proportional to context score, but it remains unclear whether energy score and other logit-based scores follow this relationship as well. It is recommended that corresponding images be provided in the appendix. 
b) The proof that Maxlogit is proportional to the context score is based on experiments with MaPLe on the Caltech101 dataset, where we observed that ID and OOD data showed approximately linearly separable patterns in the images. It is recommended that the authors validate whether this proportionality and linear separability occur in other datasets and include those images in the appendix.
2. The paper considers the Base to new dataset as a near OOD dataset. However, it is suggested that the authors also explore more classic near OOD datasets, such as those used in the MCM(Delving into Out-of-Distribution Detection with Vision-Language Representations) paper, where Imagenet10 is used as the ID dataset and Imagenet20 as the OOD dataset. Adding experiments involving these classic near OOD datasets would be beneficial.

### Questions
Please refer to the weakness.

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
This paper introduces a novel post-hoc method to improve the near Out-Of-Distribution (OOD) detection capabilities of prompt learning models for vision-language tasks, without requiring architectural changes or retraining. The proposed method, named Marginal Logit Score (MLS), leverages the Context Score computed based on a variant of existing prompts to enhance near OOD detection performance . Experiments on 13 datasets demonstrate that MLS significantly boosts the near OOD detection performance, while maintaining the same classification accuracy.

### Strengths
1. The finding is interesting.

2. The experimental results have validated the effectiveness of the proposed method.

### Weaknesses
1. The cause of the phenomenon is not clearly explained.

The author find: Compared to ID images, OOD images have a smaller gap between the original score and the Context Score. Based on this phenomenon, the author proposes combining Energy (or MaxLogit) and Context Score to identify OOD. However, the author does not deeply analyze this phenomenon and explain its cause. I speculate that the cause might be because when CLASS is present, CLASS plays the main role in the Prompt, and at this time, regardless of whether it is an ID image or an OOD image, the attention is on CLASS, so the scores are similar. When CLASS is removed, the attention of ID images and OOD images to the remaining vectors in the Prompt will differ, thus producing different scores. However, this is just a speculation, and the paper lacks a rigorous analysis of why the context score behaves differently for ID and OOD samples, particularly in relation to the attention mechanisms within the prompt learning model. The paper needs to provide a more detailed explanation of how the removal of the class token from the prompt affects the attention weights and feature representations, leading to the observed differences in context scores.

2. The discussion is not thorough enough.

Why combine Energy (or MaxLogit) with Context Score? I see that there is already a significant difference in Context Score between ID images and OOD images. Can't we directly use the Context Score to distinguish between the two types of images? The paper presents the context score as a crucial component, yet it doesn't fully explore its limitations when used in isolation. While the authors show that combining it with the logit score improves performance, they don't provide a clear explanation of why the context score alone is insufficient. A more thorough discussion should include examples or scenarios where using only the context score fails to effectively separate ID and OOD samples, and why the logit score is necessary to complement it. The paper needs to clarify the specific limitations of the context score, such as its potential for high variance or overlap between ID and OOD distributions, and how the combination with the logit score mitigates these issues.

This work discovers a phenomenon in prompt-based learning and designs an OOD detection algorithm based on this phenomenon, but it does not delve into the cause for the occurrence of this phenomenon, so I am somewhat concerned that this may not be a universal phenomenon. If the authors could provide more analysis on it, the article could be further improved.

### Questions
Please refer to the Weaknesses.

### Soundness
3

### Presentation
3

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
The paper introduces a new logit-based score named Marginal Logit Score (MLS) based on existing logit scores and a new complementary score named Context score.

### Strengths
1. The proposed method boosts existing prompt learning methods' near OOD detection performance in AUROC by up to 11.67% with minimal computational

2. The method can be easily applied to any prompt learning model without change in architecture or model re-training.

### Weaknesses
1. Lack of novelty: The contribution of the paper is limited. All I could discover is a post-hoc OOD score. More description and deeper analyses are needed to certify its usefulness.

2. Incomplete comparison with current methods: The paper mainly compares with few-shot based methods but not OOD-based methods for VLM [1, 2, 3], which should be addressed.

3. Marginal improvements: The performance gains in the main tables are marginal, even when compared with the basic MaxLogit.

4. The writing of the paper should be improved and standardized, including but not limited to the usage of quotation marks in Sec. 2.1 and the usage of superscripts and subscripts in Sec. 3.1, which may confuse readers.

### Questions
1. The OOD score is a measure of OOD detection performance. There have been numerous methods for calculating OOD scores in CLIP-based out-of-distribution detection, including, but not limited to, the papers mentioned [1, 2, 3, 4]. The comparison is too narrow, and I suggest that the authors compare with more methods to analyze the effectiveness of the proposed approach.

2. The comparison is not fair. In Table 2, the paper merely compares with prompt-based methods and achieves seemingly significant improvements. However, as shown in Table 3, the improvement becomes marginal when assessed using different metrics and OOD-based methods.

3. The writing may be somewhat confusing. For example, in the near OOD setting, which dataset is the ID dataset? I did my best but could not find any description.

4. Based on the results shown for the given datasets, the effectiveness of the method is not convincing. I suggest that the authors provide more visualizations and additional results to demonstrate its effectiveness and generalization.


[1] Learning Transferable Negative Prompts for Out-of-Distribution Detection.

[2] Negative Label Guided OOD Detection with Pretrained Vision-Language Models.

[3] Enhancing Outlier Knowledge for Few-Shot Out-of-Distribution Detection with Extensible Local Prompts.

[4] CLIPN for Zero-Shot OOD Detection: Teaching CLIP to Say No.

### Soundness
2

### Presentation
3

### Contribution
2
