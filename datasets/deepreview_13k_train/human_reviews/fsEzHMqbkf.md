# Conditional Density Ratio Score for Post Hoc Deep Outlier Detection

- Decision: Reject
- Scores: 6, 8, 6, 3

## Abstract
The ability to accurately identify out-of-distribution (OOD) samples is essential not only as a stand-alone machine learning task but also for maintaining the reliability and safety of machine learning systems. Within this domain, post hoc density estimators like the energy score are popular ways for detecting OOD samples. However, most of the existing post hoc density estimation have mainly focused on marginalizing the conditional distributions over all possible classes. In this paper, we introduce the Conditional Density Ratio (CDR) score, a principled post hoc density estimator that leverages both a class-conditional generative model in the latent space and a discriminative classifier model, allowing us to estimate the marginal densities of the latent representation without marginalization. We demonstrate that a key component to the success of the CDR score lies in correctly calibrating the two models and propose a simple yet effective method to automatically tune the temperature parameter without the need for out-of-distribution samples. We illustrate the general compatibility of the proposed method with two popular density estimators, the kernel density estimator and the Mahalanobis estimator. Through experiments on a wide range of OOD benchmark tasks, we verify the effectiveness of the proposed method and advocate it as an easy-to-implement baseline that can achieve competitive performance in most tested scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces the Conditional Density Ratio (CDR) score, a post hoc method for deep outlier detection, which combines a class-conditional generative model with a discriminative classifier to estimate densities without marginalizing over classes. CDR enables effective detection of out-of-distribution (OOD) samples by leveraging both models and incorporating a novel temperature scaling technique that does not require OOD samples for calibration. The proposed method works with commonly used density estimators like the Mahalanobis distance and kernel density estimation, achieving competitive performance across a wide range of OOD benchmarks.

### Strengths
s1. The paper introduces a novel and practical approach to model both aleatoric and 1. The studied problem is important and practice, and the paper is well-organized with well presentation. 

2. The proposed Conditional Density Ratio (CDR) score can effectively integrate generative and discriminative models, providing a principled approach to outlier detection without the need for marginalization over classes. 

3. The paper introduces a novel temperature scaling technique that allows for automatic calibration of model parameters without requiring OOD samples.  And experiments on the high-dimensional datasets demonstrate the effectiveness of the proposed score.

### Weaknesses
w1. The proposed model is mainly tested in high-dimensional data, it would be better to test on more datasets as in [1], to see whether it can perform well in small datasets:

[1] ADBench: Anomaly Detection Benchmark, https://arxiv.org/abs/2206.09426

w2. Since the function g(x) depends on \lambda, in practice, how do we decide lambda for each dataset for better OOD detection?

### Questions
Please see the weaknesses above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes the Conditional Density Ratio (CDR) score, a new approach for post-hoc OOD detection in deep learning models. The key scenario addressed is when only pre-trained model weights and a small number of in-distribution validation samples are available, without access to OOD samples or training data.
The authors propose new principled framework for post-hoc OOD detection called the CDR score, which combines a class-conditional generative model in the latent space, a discriminative classifier model and a method to estimate marginal densities without class marginalization. The paper also introduce a novel temperature scaling technique that automatically calibrates the relative contributions of the generative and discriminative models by using in-distribution validation samples. This means that there is no need to access the OOD data. The authors show that  the CDR framework is compatible with different density estimators (CDR_KDE, CDR, Maha). 
The performed experiments on benchmark datasets (CIFAR-10, CIFAR-100, ImageNet) show the effectiveness in both supervised and self-supervised learning scenarios and competitiv/superior results compared to existing methods including the MSP, Energy score, and GEM.
The paper also provides theoretical foundations for the proposed approach.

### Strengths
First the paper addresses a practical, real-world scenario where there is only access to pre-trained model weights and limited validation data.  The theoretical foundation on presenting a mathematically grounded approach to OOD detection with clear justification for its effectiveness. The proposed CDR framework demonstrates versatility, being compatible with different density estimators like KDE and Mahalanobis, which allows for adaptation to various situations and requirements.
Another strong point is the introduction of an innovative temperature scaling technique that works without requiring OOD samples, showing a good performance across a wide range of datasets and architectures.
The paper shows effective performance in both supervised and self-supervised learning scenarios.

### Weaknesses
The most significant theoretical limitation lies in its core assumption that the marginal distribution $p(z)$ is a good approximation of the true data distribution $p(x)$. The provided theoretical justification for why this approximation should hold and under what conditions it might break down is insufficient. Specifically, the paper lacks a rigorous analysis of the potential discrepancies between the latent space distribution and the original data distribution, especially when the mapping from $x$ to $z$ is highly non-linear or when the latent space is of significantly lower dimensionality than the input space. This raises concerns about the general applicability of the method across different architectures and datasets.

The evaluations are reach in computer vision while other application domains are neglected. This focus on computer vision raises questions about the generalizability of the method to other types of data (problem spaces). Also, the authors need to discuss the computational overhead of their approach compared to baseline methods, particularly for the CDR_KDE variant which likely has higher computational requirements due to its non-parametric nature. The paper does not provide a detailed analysis of the time and memory complexity of the KDE-based approach, especially in relation to the number of validation samples used for density estimation. This is crucial for understanding the practical scalability of the method.

There is the need for more  exploration of why CDR performs poorly in scenarios where Mahalanobis distance underperforms. The paper does not delve into the specific characteristics of the data or the latent space that lead to the failure of the Mahalanobis distance, and consequently, the CDR score. This lack of analysis makes it difficult to understand the limitations of the method and when it should not be applied. The relationship between temperature scaling and model calibration needs more deeper theoretical analysis to explain why it works so well in practice. The paper lacks a formal analysis of how the proposed temperature scaling method affects the underlying probability distributions and how it relates to the calibration of the classifier. The authors use  averaging CDR scores across classes. It shows good results in practical examples, however, there is need for sufficient theoretical motivation. The practical implementation considerations, including memory requirements are not thoroughly discussed.

### Questions
1- Could authors provide a more rigorous justification for why $p(z)$ serves as a good approximation of $p(x)$? (This is a fundamental assumption of the proposed method)

2- What are the concrete computational trade-offs (memory, scaling behavior) between CDR_KDE and CDR_Maha compared to baseline methods? 

3- As indicated the CDR performs poorly when Mahalanobis distance underperforms. Could the authors provide a more detailed analysis of when and why this occurs?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposed a principled post hoc density estimator called Conditional Density Ratio (CDR) score, which is composed of a class-conditional generative model and a discriminative classifier model. The proposed method can estimate the marginal densities of the latent representation without marginalization. Besides, the authors proposed to automatically tune the temperature parameter to balance the relative contributions of the generative and discriminative models. Sufficient experiments were conducted to prove the effectiveness of the proposed CDR score and temperature adjustment method.

### Strengths
1. The paper gave a detailed theoretical introduction to the proposed CDR score and temperature tuning method.
2. The author conducted sufficient comparative experiments with benchmark methods to prove the effectiveness of the proposed CDR score, and did ablation experiments to demonstrate the importance of temperature tuning.

### Weaknesses
1. The motivation of the paper is unclear. The author did not explain clearly the advantages of the proposed CDR Score compared with existing post hoc density estimators.
2. The related work is not focused on "Post-Hoc Methods".
3. Some of the content in the method section and the experiment section is difficult to follow.
4. There are several errors in the paper. For instance, in Section 5, the statement "we show plots of AUROC vs. temperature for various datasets in Figure 3" should be corrected to "Figure 4".

Here are some further details about weakness:
1. The motivation of the paper is unclear.
In the abstract, the authors state: "the existing post hoc density estimation has mainly focused on marginalizing the conditional distributions over all possible classes." However, the CDR Score proposed in this paper enables us to "estimate the marginal densities of the latent representation without marginalization." It seems that the advantage of CDR is that it does not require marginalization. But what advantages can avoiding marginalization bring? Will it reduce costs? Or will it make the method more suitable for application scenarios? The authors should give more specific advantages.
2. The related work is not focused on "Post-Hoc Methods".
As the method proposed in this paper is a kind of post-hoc method, the related work section should focus on explaining the shortcomings of the existing post-hoc methods and the improvements that the method proposed in this paper can bring.
3. Some of the content in the method section and the experiment section is difficult to follow
(1) The authors stated that "In this work, we propose a unified approach that combines MSP and Mahalanobis distance in a principled way for OOD detection." However, in Section 3, the authors did not explain how the CDR Score combines MSP and Mahalanobis distance.
(2) Figure 2 is difficult to follow. What is the meaning of "in" and "out"?

### Questions
Here are some further details about weakness:
1. The motivation of the paper is unclear. 
In the abstract, the authors state: "the existing post hoc density estimation has mainly focused on marginalizing the conditional distributions over all possible classes." However, the CDR Score proposed in this paper enables us to "estimate the marginal densities of the latent representation without marginalization." It seems that the advantage of CDR is that it does not require marginalization. But what advantages can avoiding marginalization bring? Will it reduce costs? Or will it make the method more suitable for application scenarios? The authors should give more specific advantages.
2. The related work is not focused on "Post-Hoc Methods".
As the method proposed in this paper is a kind of post-hoc method, the related work section should focus on explaining the shortcomings of the existing post-hoc methods and the improvements that the method proposed in this paper can bring.
3. Some of the content in the method section and the experiment section is difficult to follow
(1) The authors stated that "In this work, we propose a unified approach that combines MSP and Mahalanobis distance in a principled way for OOD detection." However, in Section 3, the authors did not explain how the CDR Score combines MSP and Mahalanobis distance.
(2) Figure 2 is difficult to follow. What is the meaning of "in" and "out"?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces the Conditional Density Ratio (CDR) score, a post-hoc density estimator for out-of-distribution (OOD) detection. Unlike traditional methods that marginalize over class-conditional distributions, CDR combines a class-conditional generative model and a discriminative classifier in the latent space. A key innovation is temperature scaling, which adjusts model calibration without requiring OOD samples. CDR is compatible with estimators like the kernel density and Mahalanobis estimators. The approach is computationally efficient, requiring no additional training, and demonstrates strong performance across various OOD benchmarks. Limitations include sensitivity to poor density approximations and potential suboptimality of the temperature scaling method.

### Strengths
- Interesting direction for a new framework composed of previous approaches and marginal extensions.
- New way to set the temperature parameter, the optimization of which should be further pursued and evaluated
- Good results in the setup used

### Weaknesses
 - The approach mainly combines existing work without modification. The improvements made by setting the temperature parameter are marginal improvements.
- Lack of baselines: Numerous possible baseline methods were not included in the comparison, such as [1], [2] and [3], to name just three possible ones (latest base method from 2022).
- Lack of benchmark data sets: Instead of using established benchmarks such as [4], [5] and [6], a custom benchmark scenario is used, which, in combination with the lack of baseline methods, makes comparability extremely difficult. [5] was specially designed for this purpose, as it calls this approach into question.
- In addition, [4] and [6] are cited, and [4] is even used as a baseline method, but its benchmarks are not used anyway.

### Questions
Q1: The introduction states that it is a general framework. The method should work with any estimator. Only the two presented are evaluated. How is this statement justified?

Q2 In Related Work, Post-Hoc Methods, the overlap with Anomaly Detection is emphasised. Why, then, is KNN the only common anomaly detection method used as a baseline?

Q3  Is the statement: "However, these generative models have generally shown poor OOD detection performance" in n Related Work, Unsupervised/Self-Supervised Methods, based only on the works cited (latest 2021)? Many more recent works contradict this.

Q4 How is the statement: "In this work, we consider a setup where no OOD samples are available for training nor inference."  to be understood? Has the method not been tested with OOD samples?

Q5 Why are so few and so old baseline methods used?

Q6 Why are none of the benchmarks mentioned used to enable better comparability?

[1] Graham, Mark S., et al. "Denoising diffusion models for out-of-distribution detection." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2023.

[2] Wang, Hualiang, et al. "Clipn for zero-shot ood detection: Teaching clip to say no." Proceedings of the IEEE/CVF International Conference on Computer Vision. 2023.

[3] Jiang, Xue, et al. "Negative label guided ood detection with pretrained vision-language models." arXiv preprint arXiv:2403.20078 (2024).

[4] Rui Huang, Andrew Geng, and Yixuan Li. On the importance of gradients for detecting distributional
shifts in the wild. In NeurIPS, 2021.

[5] Guille-Escuret, Charles, et al. "Expecting The Unexpected: Towards Broad Out-Of-Distribution Detection." arXiv preprint arXiv:2308.11480 (2023).

[6] Yang, Jingkang, et al. "Openood: Benchmarking generalized out-of-distribution detection." Advances in Neural Information Processing Systems 35 (2022): 32598-32611.

### Soundness
2

### Presentation
2

### Contribution
2
