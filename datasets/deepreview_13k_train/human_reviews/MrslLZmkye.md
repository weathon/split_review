# SEE-OoD: Supervised Exploration for Enhanced Out-of-Distribution Detection

- Decision: Reject
- Scores: 3, 3, 3, 8

## Abstract
Current techniques for Out-of-Distribution (OoD) detection predominantly rely on quantifying predictive uncertainty and incorporating model regularization during the training phase, using either real or synthetic OoD samples. However, methods that utilize real OoD samples lack exploration and are prone to overfit the OoD samples at hand. Whereas synthetic samples are often generated based on features extracted from training data, rendering them less effective when the training and OoD data are highly overlapped in the feature space. In this work, we propose a Wasserstein-score-based generative adversarial training scheme to enhance OoD detection accuracy, which, for the first time, performs \textit{data augmentation} and \textit{exploration} simultaneously under the \textit{supervision} of limited OoD samples. Specifically, the generator explores OoD spaces and generates synthetic OoD samples using feedback from the discriminator, while the discriminator exploits both the observed and synthesized samples for OoD detection using a predefined Wasserstein score. We provide theoretical guarantees that the optimal solutions of our generative scheme are statistically achievable through adversarial training in empirical settings. We then demonstrate that the proposed method outperforms state-of-the-art techniques on various computer vision datasets and exhibits superior generalizability to unseen OoD data.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper studies OOD detection relying on real OOD samples in training. It proposes a method to generate more OOD samples in training based on Wasserstein-score-based generative adversarial learning. Experiments show that the proposed method can achieve good OOD detection performance, given more OOD samples in training.

### Strengths
- The method can achieve good performance on the experimented settings and datasets, which matches the assumptions that seeing real OOD samples can help OOD detection in testing. 
- The experiments studied the two settings with balanced or imbalanced OOD samples in training. 
- The paper is written clearly.

### Weaknesses
 - Some arguments and claims are the paper are impervious or unfaithful. 
    - The real OOD samples are not used in many methods because the OOD samples are unknown/unpredictable in training. Handling OOD detection without OOD samples in training is a more general and real setting, instead of a drawback. It is reasonable to use some OOD samples to perform “outlier exposure”. However, the related works are not discussed in the paper. 

- The experiments are limited.
    - The experiments only cover the simple datasets and settings as shown in Table 2. The “within-dateset” setting and the used datasets are simple. And the dataset used in “between-dataset” setting are also not complex enough the validate the methods. That’s also why the proposed method can easily achieve very high performance after seeing real OOD samples. More “between-dataset” settings should be considered as more recent OOD detection papers, such as (Liu et al., 2020).
    - The compared methods are limited and unfair. Many OOD detection methods using OOD samples in training are not discussed and compared, such as the “outlier exposure” based methods (“Deep Anomaly Detection with Outlier Exposure”).
    - Some recent strong OOD detection methods are not discussed or compared, such as
Non-Parametric Outlier Synthesis, ICLR 2023.
How to Exploit Hyperspherical Embeddings for Out-of-Distribution Detection?, ICLR 2023.
    - Many strong OOD detection do not use OOD samples in training (in the more general and real setting) but have strong modeling. But it is straightforward to introduce the known OOD samples in the training process easily. The authors should consider this case and conduct comparisons, especially considering the experimented settings and datasets are very simple.

### Questions
Please address the questions mentioned in the weakness, especially those about experiments.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper presents a generative adversarial training method leveraging a Wasserstein-score to enhance Out-of-Distribution (OoD) detection accuracy. The approach simultaneously undertakes data augmentation and exploration using a limited set of OoD samples. Additionally, the study offers theoretical assurances, confirming that the optimal solutions derived from generative model can be statistically realized through adversarial training in empirical scenarios.

### Strengths
The method employs a unique exploration strategy to identify regions where the model lacks confidence. By focusing on uncertain regions, SEE-OOD achieves superior performance in detecting OOD samples compared to existing methods. The paper presents extensive experiments and benchmarks to validate the effectiveness of SEE-OOD against other state-of-the-art techniques.

### Weaknesses
1. The paper does not provide visualizations of the generated outliers, which could offer more intuitive insights into the model's behavior and decisions. Specifically, without visual examples, it's difficult to assess the quality and diversity of the generated samples and whether they effectively cover the OOD space. The lack of visualization also makes it challenging to understand if the generated samples are semantically meaningful or simply random noise.
2. The evaluation metrics employed in the paper miss out on including the Area Under the Receiver Operating Characteristic (AUROC), which is crucial for understanding model performance in classification tasks, especially in OOD detection. AUROC provides a comprehensive view of the trade-off between true positive rate and false positive rate across different thresholds, which is essential for evaluating the robustness of OOD detection methods. Relying solely on other metrics might not capture the full picture of the model's performance.
3. While the paper presents results on certain datasets, it would benefit from testing on larger and more diverse datasets to ensure the method's generalizability and robustness. The current datasets might not fully represent the complexity and variability of real-world OOD scenarios. Testing on datasets with different characteristics (e.g., image types, data distributions) is necessary to validate the method's applicability across various domains.

### Questions
Please address the weaknesses I've highlighted above.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In the presented research, the authors introduce a novel generative adversarial training approach rooted in the Wasserstein-score-based
framework. This method facilitates the generator in traversing Out-of-Distribution (OoD) spaces to produce virtual outliers, guided by feedback from the discriminator. Concurrently, the discriminator harnesses these outliers to distinguish between In-Distribution (InD) and OoD data within the designated Wasserstein score space. The study furnishes theoretical validations confirming the method's robustness, highlighting its capacity to seamlessly segregate InD and OoD data, including the synthesized virtual OoD samples. A unique experimental paradigm is unveiled, termed Within-Dataset OoD detection, which offers a more rigorous test for Deep Neural Networks (DNNs) compared to the conventional Between-Dataset OoD differentiation tasks. The efficacy of the proposed technique is further validated through extensive benchmark tests across varied image datasets.

### Strengths
1. The paper introduces a novel generative adversarial training scheme that allows the generator to explore Out-of-Distribution (OoD) spaces and generate virtual outliers. This innovative approach enhances the traditional methods of OoD detection by leveraging the power of generative models.

2. A standout feature of this paper is the provision of several theoretical results that back the proposed method. By demonstrating that the
discriminator can achieve perfect separation between In-Distribution (InD) and OoD samples in the Wasserstein score space, the authors solidify the the credibility of their approach.

### Weaknesses
1. Evaluation Metrics: The paper seems to overlook certain prevalent evaluation metrics. For instance, the Area Under the Curve (AUC) is a widely accepted metric in many domains, including OoD detection. It would be beneficial to understand the performance of the proposed method under such widely recognized metrics. Furthermore, the reliance on outlier exposure raises questions. Specifically, OoD detection typically aims to identify data points that deviate from the expected distribution, rather than simply identifying outliers. The distinction between these two is subtle but crucial. The paper does not sufficiently clarify how the generated 'virtual outliers' truly represent the broader concept of OoD data, which is not necessarily composed of extreme outliers, but rather data from a different distribution.

2. Generality of Proposed Setting: The proposition of the Within-Dataset OoD detection is undoubtedly a fresh perspective. However, its universal applicability remains a concern. This setting, which treats different classes within the same dataset as OoD with respect to one another, might not capture the diverse and multifaceted nature of real-world OoD scenarios. To many, this approach might appear as an analysis of variations within a single domain rather than a genuine OoD situation. The paper needs to better justify the practical relevance of this within-dataset setting, especially given that real-world OoD often involves more substantial distributional shifts.

3. Scalability Concerns: The scalability of the proposed method, especially when confronted with vast and diverse datasets , remains ambiguous. The paper lacks a thorough analysis of the computational cost associated with the generative adversarial training, particularly as the dimensionality and size of the datasets increase. This is a critical consideration for practical deployment, and the paper should provide more insights into the computational demands of the proposed approach.

### Questions
Please refer to the above weakness part.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper is concerned with the robust out-of-distribution (OOD) detection, while maintaing the same level of performance of in-distribution (IND) data. In order to overcome the case when the number of OOD samples is too smalll (which could lead to overfitting), the authors propose a generative adversarial approach that uses real OOD data for supervised generation of synthetic OOD samples and thus could better represent the OOD space. More concretely, they propose a Wasserstein-score-based generative adversarial training
framework where the generator explores OOD space and synthesis virtual outliers with the feedback provided by the discriminator, while the discriminator exploits the generated outliers to separate IND and OOD data distributions. Extensive experiments demonstrates the superiority of the proposed approach in OOD detection when compared with other state-of-the-art approaches.

### Strengths
The paper is well-documented, clearly written and easy to follow. The paper provides a theoretical insight in order to demonstrate the effectiveness of the proposed method. The related work section covers the most relevant papers in the field. Experimental validation is convincing and demonstrates the superiority of the proposed approach.

### Weaknesses
The idea is not totally new, i.e. the usage of Wasserstein-based-score for OOD detection has been used before (see the WOOD method).



### Questions
- I understand that your approach is suitable for low-data regime (especially when the number of OOD samples is low). It would be interesting to visualize the curves in figures 2 and 3 also as a number of several ratios (IND/OOD). How many number of OOD samples do you need to generate in each case? 
- Why do you distinguish between two experimental scenarios (balanced vs imbalanced OOD classes)? It is assumed that OOD data is unlabeled. So, it does not matter how many data is in each class. Please clarify this aspect.
- Another aspect which is not clear to me is how do you define the imbalanced regime for OOD, i.e. you mention 'only a few classes are observed'). I thought imbalance refers to different ratios between the samples of OOD classes or with respect to the samples in the IND classes. What is in each case the ratio between majority classes and minority classes?
- If the generative adversarial approach is unconditional, why the case of imbalanced scenario is relevant? OOD data is unlabeled anyway.
- How do you evaluate the quality of the synthetic OOD samples? Some quantitative and qualitative analysis is indicated.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
