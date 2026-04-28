# Towards Robustness of Person Search against Corruptions

- Decision: Reject
- Avg Score: 6.00
- Scores: 8, 3, 8, 3, 8

## Abstract
Person search aims to simultaneously detect and re-identify a query person within an entire scene, involving detection and re-identification as a multi-task problem.
While existing studies have made significant progress in achieving superior performance on clean datasets, the challenge of robustness under various corruptions remains largely unexplored.
To address this gap, we propose two benchmarks, CUHK-SYSU-C and PRW-C, designed to assess the robustness of person search models across diverse corruption scenarios.
Previous researches on corruption have been conducted independently for single tasks such as re-identification and detection.
However, recent advancements in person search adopt an end-to-end multi-task learning framework that processes the entire scene as input, unlike the combination of single tasks. 
This raises the question of whether independent achievements can ensure corruption robustness for person search.
Our findings reveal that merely combining independent, robust detection and re-identification models is not sufficient for achieving robust person search. 
We further investigate the vulnerability of the detection and representation stages to corruption and explore its impact on both foreground and background areas.
Based on these insights, we propose a foreground-aware augmentation and regularization method to enhance the robustness of person search models.
Supported by our comprehensive robustness analysis and evaluation framework our benchmarks provide, our proposed technique substantially improves the robustness of existing person search models.
Code will be made publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper focus on the corruptions of images in person search problems. Two benchmarks are proposed for evaluation, while the analysis is adopted on both detect and reID stages. A method with data augmentation and regularizaiton is further proposed. Good experimental resutls are achieved.

### Strengths
1. The motivaion of evaluationg the affects of image corruption for person search is useful.
2. The analysis results and discussion about the performance dropping in both detection and searching stages are acceptable.

### Weaknesses
1. It is hard to regard as a contribution via simply post-processing two exisiting datsasets. The human-designed or generated augmentation is far from the real scene. 
2. The further proposed forground-aware augmentation is not novel, which has been a common sense that the key region for accurate person search is the body region.
3. The referred methods in the experiments are most out-of-date, missing some recently proposed methods.

### Questions
See weakness.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper explores the robustness of person search models in degraded data environments. It introduces two new benchmark datasets (CUHK-SYSU-C and PRW-C) for evaluating the performance of person search models under different degraded conditions. By analyzing the sensitivity of both the detection and feature extraction stages under corruption, the authors found that existing models exhibit significant vulnerability when foreground images are damaged. Based on these findings, a foreground-aware data augmentation and regularization method was proposed to enhance model robustness.

### Strengths
This paper is the first to investigate the robustness of person search models in degraded data environments. It introduces two novel benchmark datasets (CUHK-SYSU-C and PRW-C) for evaluating the performance of person search models under various degradation scenarios.

### Weaknesses
1. The strength of this paper lies in the introduction of two new benchmark datasets for exploring person search in interference scenarios. However, overall, the dataset construction methods are largely adapted from existing approaches, and the proposed solution is relatively simple, focusing on narrowing the feature gap between corrupted and original images. From a theoretical innovation standpoint, the contributions are limited and fall short of ICLR's high standards.

2. While the foreground-aware augmentation approach is effective, it appears to be an incremental improvement rather than a fundamentally new concept. The paper could be strengthened by deeper theoretical insights into why this method improves robustness beyond empirical results.

3. The paper employs various existing data augmentation methods to simulate real-world disturbances. However, the key question is whether these augmentations can effectively benefit real-world scenarios. If their impact is limited, the constructed datasets may hold little significance.

### Questions
1. The experiments demonstrate that foreground damage has a greater impact on model performance. However, it is unclear whether this damage affects the detection performance more or the recognition performance.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Previous studies have only investigated the corruption issues in person detection or person re-identification separately, whereas this paper is the first to study the corruption robustness in the person search task (detection + re-identification). The authors meticulously constructed two benchmarks in corruption scenarios, CUHK-SYSU-C and PRW-C, and through extensively evaluating models on these two benchmarks, they obtained some meaningful findings. Subsequently, based on these findings, the authors proposed several methods to improve the model's robustness against corruption, and validated the effectiveness of these methods through extensive experiments. Overall, this is a very solid work and I like it.

### Strengths
1. The writing of this paper is smooth and easy to understand. The authors structured it by first posing the problem, then constructing the benchmarks, evaluating current models to identify areas for improvement, proposing improvement methods, and finally validating the effectiveness of the methods. I am able to follow the core ideas of this work very well.

2. According to the authors, they are the first to study the issue of corruption robustness in the person search task, a problem which I believe has significant practical relevance. In real-world applications, due to the influence of weather, lighting, and other imaging conditions, the sursurveillance videos are prone to corruption. A person search model that can withstand such corruptions is essential.

3. The contributions of this paper are substantial. The paper introduces two corrupted benchmarks CUHK-SYSU-C and PRW-C (as well as an additional manual annotated test set based on BDD100K), and proposes two modules to enhance the model's resistance to corruption, all of which have positive implications for the development of this field.

4. The paper provides rich details in its experimental procedures, offering good reproducibility.

### Weaknesses
Although the entire work is very solid, it relatively lacks novelty at the technical level. Through evaluation and analysis, the authors concluded that foreground corruption and robust person representation are important. Therefore, they proposed two methods: Foreground-Aware Augmentation and Regularization for Robust Person Representation. I carefully reviewed the technical details of these two methods and found them to be somewhat lacking in innovation, as they are based on existing techniques that have already been implemented. Specifically, the Foreground-Aware Augmentation seems to be a straightforward application of existing augmentation techniques like AugMix, and the Regularization for Robust Person Representation appears to be a standard regularization approach without significant modification for the person search task. The combination of these two methods, while effective, does not introduce a fundamentally new technical contribution.

### Questions
1. Will you make your entire code, model, and dataset public? I believe this would be significant for the development of the field.

2. Since you pointed out that person re-identification representation is important, have you tried to investigate the effect of some person reid pre-trained models on the robustness of the person search model against corruptions?  To my knowledge, pre-training can learn good person re-identification representations, and I would be very interested to see an experiment where you investigate the impact of pre-trained person representations on your task. For instance, you could conduct an experiment with the pre-trained ResNet50 in LUP, UPReID, LUP-NL, ISR, PLIP and CION. 

I will greatly appreciate it and **raise the score** if you could conduct the aforementioned experiment that interests me.

Reference:

LUP: Unsupervised pre-training for person re-identification (CVPR2021)

UPReID:  Unleashing potential of unsupervised pre-training with intra-identity regularization for person re-identification (CVPR2022)

LUP-NL: Large-scale pre-training for person re-identification with noisy labels (CVPR2022)

ISR: Identity-seeking self-supervised representation learning for generalizable person re-identification (ICCV2023)

PLIP: Plip: Language-image pre-training for person representation learning (NeurIPS2024)

CION: Cross-video Identity Correlating for Person Re-identification Pre-training (NeurIPS2024)

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces two benchmarks, CUHK-SYSU-C and PRW-C, evaluating the robustness of person search models under corruption scenarios. The authors propose a foreground augmentation and regularization method, improving the robustness.

### Strengths
The author examines the shortcomings of existing ReID methods based on experiments, explaining the issues in a clear and easy-to-understand manner. The authors use extensive experiments to demonstrate the drawback of existing methods.

### Weaknesses
1.	The five severity levels of the proposed benchmark are not detailed in either the main text or Fig. 1, which is quite important.
2.	The benchmark adds noise to the test sets of existing datasets without collecting additional person images for specific scenarios. I believe this does not qualify as a benchmark that makes a significant contribution. It it better to be considered as an evaluation metric.
3.	The proposed module is an existing augmentation, which I believe is quite incremental in terms of novelty.
4.	CUHK-SYSU and PRW datasets are relatively small, the proposed method has not been validated on larger-scale datasets. Therefore, the scalability of the method is doubted.
5.	Although the author claims that the augmentation method is different from the construction of the benchmark, they use a data augmentation method to solve an augmented test set of existing dataset. This is intuitive and within expectation, and I did not find anything particularly innovative in this approach.
6.	Several related works are missing, including but not limited to “SAT: Scale-Augmented Transformer for Person Search”, and “Making person search enjoy the merits of person re-identification”. Especially, the method of SAT incorporates the augmentation into transformer, whose contribution if believed to be of value.
7.	There are a lot typos in the manuscript, such as the symbols for the loss functions are inconsistent in Eq 5.

### Questions
1.	What is the five severity levels of the proposed benchmark, or can you quantatitively describe the differences between them?
2.	It is better to compare more baselines other than the five baselines in Tab. 3.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper addresses the robustness of person search under various corruption scenarios. The authors introduce two new benchmarks, CUHK-SYSU-C and PRW-C, to evaluate person search models' robustness. Unlike previous studies that focused on independent tasks such as re-identification and detection, this work highlights the inadequacy of merely combining robust detection and re-identification models for robust person search. The authors investigate the sensitivity of detection and representation stages to corruption and its impact on background regions. Based on these insights, they propose a method that significantly enhances the robustness of existing person search models.

### Strengths
Overall, this paper takes a practical approach, considering numerous details and unexplored aspects of previous work. It introduces two benchmark datasets and evaluates leading models from both detection and re-identification perspectives. By analyzing the characteristics of foreground and background in the constructed datasets, the authors propose corresponding modules and validate the model's effectiveness.

1.Originality: This paper identifies shortcomings in previous datasets and evaluation methods, proposes a novel data construction approach, and discovers the varying impact of foreground and background on person search. These contributions demonstrate a certain level of originality.

2.Quality: The paper is thorough and provides valuable insights. The introduction and validation of large-scale datasets are of high quality.

3.Clarity: The paper is easy to follow. The problem statement, in particular, is logically clear and easy to understand.

4.Significance: The proposed datasets will assist future researchers in developing more robust end-to-end person search models. Additionally, the identified interference factors and their impacts will guide improvements in detection, re-identification, and other related fields.

### Weaknesses
This article has no obvious shortcomings. The author has done a large amount of related work and relevant verification. In my opinion, the workload of this article is sufficient. It also presents visualization analysis in various aspects and in the frequency domain, which is helpful for promoting research in this field.

### Questions
1.The author can consider expanding the dataset to the multi-modal re-identification area. Because the corruption types such as darkness and strong contrast constructed in the article are similar to the harsh visual environment in RGBNT201 for the destruction of visible light images. If the corruption can be extended to near-infrared or infrared images, or if LLM is used for text annotation of images and corruption is performed on the text, these are all good expansion ideas.

### Soundness
3

### Presentation
4

### Contribution
4
