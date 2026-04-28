# On Diffusion Modeling for Anomaly Detection

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 6, 8, 6

## Abstract
Known for their impressive performance in generative modeling, diffusion models are attractive candidates for density-based anomaly detection. This paper investigates different variations of diffusion modeling for unsupervised and semi-supervised anomaly detection. In particular, we find that Denoising Diffusion Probability Models (DDPM) are performant on anomaly detection benchmarks yet computationally expensive. 
By simplifying DDPM in application to anomaly detection, we are naturally led to 
an alternative approach called Diffusion Time Estimation (DTE). DTE estimates the distribution over diffusion time for a given input and uses the mode or mean of this distribution as the anomaly score. We derive an analytical form for this density and leverage a deep neural network to improve inference efficiency.
Through empirical evaluations on the ADBench benchmark, we demonstrate that all diffusion-based anomaly detection methods perform competitively for both semi-supervised and unsupervised settings. Notably, DTE achieves orders of magnitude faster inference time than DDPM, while outperforming it on this benchmark. These results establish diffusion-based anomaly detection as a scalable alternative to traditional methods and recent deep-learning techniques for standard unsupervised and semi-supervised anomaly detection settings.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The manuscript proposes *diffusion time estimation* (DTE) for the task of unsupervised and semi-supervised point anomaly detection. DTE assumes a data point to be produced by diffusion process and estimates the distribution of the denoising time step required to reconstruct the data point. The mean of mode of the distribution is regarded as the anomaly score of the data point. 

In addition to its effectiveness demonstrated in prior works, DTE avoids the actual denoising process redundant for anomaly detection and directly estimates the extend to which the sample appers to be anomalous. With this keen insight, the manuscript provides detailed derivation of the posterior distribution of variance of time (decided by time step) given an input image assumed to be produced by a diffusion process. Based on the derivation, the manuscript designs one non-parametric model and two parametric models (regressive and categorical respectively). 

The performances of the three models are evaluated on 57 datasets from ADBench demonstrating the capabilities of DTE for the task of anomaly detection and its advantages over DDPM in quaility and efficacy.

### Strengths
* The paper provides a new perspective for adopting diffusion modeling in the field of anomaly detection
* The paper provides one parametric and two non-parametric practical models for the task of anomaly detection 
* The methods proposed in the paper (DTE) achieve significate margins in both performance and efficacy compared with DDPM

### Weaknesses
 * The advantage of DTE methods hold should be demonstrated quantitatively. As the DTE methods perform worse than kNN in both quality and efficiency, quantitative results are recommended to demonstrate the distinctions in scalability of DTE methods
* The presentation in Figure 3 needs optimization. To demonstrate the small difference between non-parametric estimate and analytical posterior, the visualization of residual part seems more straightforward.

### Questions
See *Weaknesses*.

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The work explores the use of diffusion models for anomaly detection (AD), and proposes an AD method based on diffusion time estimation (DTE), with three models under the DTE framework introduced. The DTE models, particularly the DNN-based parametric model, can achieve desired detection performance while substantially reducing the inference time. The models are evaluated on 57 datasets and show comparable performance compared to a set of 19 baseline/SOTA methods in both semi-supervised and unsupervised settings.

### Strengths
- The work is well motivated and easy-to-follow.
- The idea of using diffusion time estimation (DTE) for AD is interesting and new. It also provides a way for learning parametric DTE models that allow efficient inference time.
- The proposed DTE models generally perform substantially better than the popular diffusion model DDPM, and show comparable performance to a large number of competing methods on 57 tabular datasets.

### Weaknesses
 - The performance of the DTE models seems to be upper bounded by the simple kNN-based AD method. There are a number of kNN-based AD methods, including some deep methods like Refs [1]. It would be helpful for the empirical evidence support if these advanced kNN variants are included in the empirical comparison. Specifically, methods that learn an embedding space optimized for kNN-based anomaly detection, as opposed to using raw feature space or embeddings from a pre-trained model, should be considered. The current comparison does not fully explore the potential of kNN-based approaches.
- The models rely on distance in original feature space, and they would fail to work if the data lies in very high-dimensional space, e.g., datasets with hundreds of thousands of features or millions of features. While the authors mention that embeddings could help, the core method's reliance on original feature distances remains a concern for scalability to very high-dimensional data. The method's performance in such scenarios needs to be explicitly addressed and tested.
- Since the method is based on generative models, it is important to discuss and compare with other generative model-based AD methods, such as GAN-based methods, to highlight the advantages of the proposed method. The current comparison lacks a thorough analysis of the proposed method's strengths and weaknesses compared to other generative approaches for anomaly detection, particularly in terms of training stability and sample quality.
- Since the models directly work on tabular datasets, it is misleading to claim that the evaluation is performed on diverse tabular, image, and natural language datasets. The evaluation is limited to tabular data and embeddings, which does not fully represent the diversity of the claimed evaluation scope.
- The work may be improved by having more discussion on recent diffusion model-based AD studies, such as [2-4]. The discussion of related work should be more comprehensive, including a deeper analysis of the specific differences and advantages of the proposed DTE method compared to other diffusion-based approaches for anomaly detection.

### Questions
Please see the weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a non-parametric approach based on the inverse Gamma distribution of diffusion time for noisy input, achieving accurate predictions and ranking anomalies similarly to kNN. Additionally, a parametric strategy employs a deep neural network for large datasets, demonstrating competitive performance and significantly improving inference time. Pre-trained embeddings for images are found to enhance diffusion-based methods, highlighting the potential advantage of using latent space diffusion. The evaluation on ADBench, a benchmark for anomaly detection datasets, shows promising results in comparison to prior work.

### Strengths
+ The proposed approach offers a simpler alternative that avoids modeling the reverse diffusion process. Instead, it focuses on modeling the distribution over diffusion time associated with noisy input samples. The assumption is that anomalies are distant from the data manifold, leading to higher density for larger timesteps in the distribution.
+ Both non-parametric and parametric strategies are employed for DTE based anomaly detection, and the parametric strategies achieve a tradeoff between accuracy and inference time.
+ The evaluation is conducted on ADBench, as well as additional image datasets such as Visa, CIFAR-10, and MNIST.

### Weaknesses
 -The performance in the semi-supervised setting is more competitive compared to the unsupervised setting. This indicates that DTE benefits from labeled data, allowing for a more accurate modeling of the distribution of diffusion time. The observed performance difference raises a concern about the method's robustness in truly unsupervised scenarios, where labeled data is unavailable. Specifically, the reliance on normal data during training in the semi-supervised setting might lead to overfitting to the normal class, potentially hindering the detection of subtle anomalies that deviate slightly from the training distribution. This is a critical point, as the core challenge in anomaly detection lies in identifying outliers without prior knowledge of their characteristics. Therefore, the method's sensitivity to the training data composition needs further investigation.


### Questions
How does varying the ratio of labeled data in the semi-supervised setting affect the performance of DTE? Can this method be extend to more challenging tasks, such as the localization of anomaly in data?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
In this paper, the authors investigate diffusion modeling for anomaly detection and introduce an efficient approach called Diffusion Time Estimation (DTE), showing its competitive performance and improved inference times compared to traditional methods and deep learning techniques.

### Strengths
1. This paper is well-organized and easy to follow.
2. Investigating the diffusion model to facilitate anomaly detection is an interesting and promising research issue.
3. The authors conduct comprehensive experiments to demonstrate the effectiveness of the proposed method.

### Weaknesses
1. The contribution of this paper appears limited. There are several existing works on anomaly detection utilizing diffusion models, such as those mentioned below:
[1] Unsupervised Surface Anomaly Detection with Diffusion Probabilistic Model, ICCV23.
[2] Feature Prediction Diffusion Model for Video Anomaly Detection, ICCV23.
[3] DiffusionAD: Denoising Diffusion for Anomaly Detection, Arxiv.
[4] Diffusion models for medical anomaly detection, MCCAI22.
Can the authors point out the unique contributions of this paper compared with them?
2. The motivation and rationale for introducing the diffusion model into anomaly detection are somewhat unclear. The authors should emphasize it. Specifically, while the paper mentions the use of the reverse diffusion process, it does not clearly articulate why this is a suitable approach for anomaly detection compared to other generative models or even non-generative methods.
3. Authors should compare with some latest AD methods proposed in 2023. Besides, it would be more convincing to include diffusion model-based anomaly detection approaches. The current comparison is not comprehensive enough to establish the superiority of the proposed method, especially given the rapid advancements in the field.
4. The reviewer has thoroughly reviewed the experimental results presented in the appendix. The authors have done a comprehensive experiment by including the results from dozens of datasets in this paper. However, the reviewer observed that the proposed method did not consistently outperform other methods on each individual dataset. It achieved the best performance only on a subset of the datasets. This raises concerns about the generalizability of the proposed method and its practical applicability across diverse datasets.

### Questions
See weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
