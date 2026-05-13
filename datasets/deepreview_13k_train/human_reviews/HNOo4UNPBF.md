# Scale-Aware Contrastive Reverse Distillation for Unsupervised Anomaly Detection

- Decision: Accept
- Scores: 5, 5, 8, 8

## Abstract
Unsupervised anomaly detection using deep learning has garnered significant research attention due to its broad applicability, particularly in medical imaging where labeled anomalous data are scarce. While earlier approaches leverage generative models like autoencoders and generative adversarial networks (GANs), they often fall short due to overgeneralization. Recent methods explore various strategies, including memory banks, normalizing flows, self-supervised learning, and knowledge distillation, to enhance discrimination. Among these, knowledge distillation, particularly reverse distillation, has shown promise. Following this paradigm, we propose a novel scale-aware contrastive reverse distillation model that addresses two key limitations of existing reverse distillation methods: insufficient feature discriminability and inability to handle anomaly scale variations. Specifically, we introduce a contrastive student-teacher learning approach to derive more discriminative representations by generating and exploring out-of-normal distributions. Further, we design a scale adaptation mechanism to softly weight contrastive distillation losses at different scales to account for the scale variation issue. Extensive experiments on benchmark datasets demonstrate state-of-the-art performance, validating the efficacy of the proposed method. The code will be made publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents a scale-aware contrastive reverse distillation model for unsupervised anomaly detection, focusing on improving performance in fields like medical imaging, where labeled anomalous data is often scarce. Building on this, the authors introduce a contrastive student-teacher learning approach that generates out-of-normal distributions to enhance feature discriminability. Additionally, they propose a scale adaptation mechanism that adjusts contrastive distillation losses at various scales to account for variations in anomaly size, addressing limitations in existing methods that struggle with scale variation and feature discrimination. Evaluation on benchmark datasets shows that this model achieves reasonable performance, validating its effectiveness.

### Strengths
+) Anomaly detection is an important topic

+) The paper is well-structured and easy to follow

### Weaknesses
 -) Novelty of this work seems incremental

-) The domain is limited to medical image analysis

### Questions
a) Anomaly detection is an important topic where identifying unusual patterns can have a direct impact on various applications. In this sense, this paper researches a domain-specific area in anomaly detection, i.e., medical images, using reverse-distillation. 

b) While this paper provides valuable refinements in the area of anomaly detection, particularly through its scale-aware contrastive reverse distillation model, the novelty appears somewhat incremental. Firstly, the study primarily builds on and combines well-established methods, reverse distillation and contrastive learning, rather than introducing a fundamentally new approach. Secondly, the approach to enhance feature discriminability by generating synthetic or perturbed anomaly data is not novel; similar methods have been previously explored, such as in [1]. The effectiveness of this technique can also vary significantly depending on the choice of noise or perturbation (rather than learnable in [1]), which may limit its reliability. Thirdly, fusing multi-scale features is a long-standing topic in computer vision, which further contributes to the incremental nature of the contribution. While these refinements have practical value, they represent an evolution of existing methods rather than a new innovation in anomaly detection.

[1] Cai, Jinyu, and Jicong Fan. "Perturbation learning based anomaly detection." Advances in Neural Information Processing Systems 35 (2022): 14317-14330.

c) The evaluation of the proposed method is performed on three medical datasets, it is not clear how good it can be generalized to other domains?

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
3

### Summary
This paper introduces a twofold approach: on one hand, data augmentation for unlabeled information is achieved by injecting noise, which then serves as the basis for contrastive learning. On the other hand, parameters are extracted at each layer to achieve multi-scale information fusion, enabling the model to better distinguish between positive and negative samples.

### Strengths
The methodology section of this paper is clearly written and well-presented.

### Weaknesses
1. In terms of innovation, this article presents two components that are commonly seen in other works. A straightforward suggestion would be for the authors to explore a more adaptable data augmentation method to address the issue raised in “Question 1.”

2. Regarding the writing, the **Introduction** section of this article is somewhat confusing. Firstly, the paragraphing is suboptimal. In the second paragraph of the introduction, the author discusses the shortcomings of anomaly detection models based on generation. The third paragraph explains existing work aimed at improving these models, followed by an exploration of the development of self-supervised learning. Although self-supervised learning indeed enriches unsupervised learning within deep learning, the third paragraph would be clearer if it unified these two parts, focusing on how self-supervised learning specifically addresses the issues raised in the second paragraph. Secondly, and more importantly, an excessive portion of the introduction is dedicated to discussing related work, lacking sufficient focus on the contributions of this paper. Maybe you could merging the discussion of existing work and self-supervised learning, followed by a clear transition to the paper's contributions. Additionally, you could recommend what key points about the paper's contributions should be emphasized earlier in the introduction.

### Questions
1. In the noise generation process, the intensity of each position is sampled from a uniform distribution. However, in real-world medical imaging, anomalous regions in disease cases appear in specific locations; for example, abnormalities in a chest image typically do not appear outside body regions. For instance, you could suggest incorporating prior knowledge about typical anomaly locations in different types of medical images.

2. Additionally, is each test sample measured at the image level or at the patch level? If it is at the image level, the positive-to-negative anomaly ratio in the dataset is relatively high, which does not quite align with the extremely imbalanced nature of anomaly detection tasks.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Two issues arise in reverse knowledge distillation for medical imaging, an inability to properly distinguish between different features and an inability to deal with different scales. This work proposes two methods to address these issues: a contrastive student-teacher learning approach that involves using both a “good” and a “bad” teacher, as well as a scale adaptation mechanism. Results demonstrate that on almost every dataset the proposed approach is able to outperform existing techniques.

### Strengths
The paper is well written and the ideas are easy to follow. I appreciate how the authors identify the two problems facing medical imaging in this domain and then propose solutions. The new approach outperforms all other methods that the authors compare with in table 1.

### Weaknesses
Issue 1: This paper doesn’t have any formal proofs or theorems to guarantee its effectiveness, therefore the strengths of the paper must rely on the experiments and empirical results. For the datasets I will admit as a review I am not very familiar with them. For example, on the image dataset CIFAR-10, a few years ago a jump from 93% to 98% was considered significant. Today an increase from 99% to 99.9% on CIFAR-10 would not even be considered a major contribution. Likewise, for these datasets it is hard to determine whether a jump of 3.01% and 4.38% (as the authors show) is worthy of publication. Could the authors please clarify how much other papers pushed the accuracy forward in other works, as compared to the increase their method is offering?

Issue 2: The authors say they will release their code upon publication, but I did not see any code given in the supplemental material. This might be an oversight on my part, but where is the code? I would like to see a good faith gesture of releasing an anonymous github for the code or at least a zip file of the code. Too many papers claim SOTA results and never release code. In this day and age it is simply unacceptable to continue this trend. 

Issue 3: The authors also don’t mention anything about the runtime of their algorithm. How does the student-teacher setup and training time compare to other existing methods in the field? While this is not a HUGE concern, I think it would be good to have some discussion and analysis of this. For example could you show the training time complexity of your algorithm and the next two best methods in the field? Or even an experimental runtime of the training in seconds of your algorithm and the next two best methods? Without this I feel we don’t have the complete story when comparing methods. 

Issue 4: Please see my minor comments about uncited claims in the papers. For acceptance I would like to see citations for all the claims you have made. 

Issue 5: I don’t like the terminology “good” and “bad” teacher. It is very non-technical and hard to follow. Can you please change the terminology in your paper and name the teachers more appropriately? 

Minor Comments:

=Line 36, “anomalous samples is often prohibitively expensive and time-consuming…” I believe this is correct but I want to see a citation to backup this claim?

=Line 45, “they tend to generalize too well, thereby risking the reconstruction of abnormal regions.” Citation for this claim? 

=Table 1 has many entries that are unsorted (aside from the bolded number indicating the best method). It would be better if this table was sorted in order of increasing AUC for the methods.

=Line 167 “Medical images typically exhibit a power law distribution of frequencies, with lower frequency components dominating the image content.” Please give a citation for this bold claim?

### Questions
Q1: Please address each of my issues 1-5. If they are adequately addressed I would be willing to increase my score for the paper accordingly.

EDIT: The reviewers have address my concerns adequately. I have update the score of my review accordingly.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors propose a new method for anomaly detection in medical data setting using contrastive reverse distillation. The method uses knowledge distillation as it's foundation, implementing pre-trained teachers models along with a student model trained to either minimize or maximize its distance from the teachers in a feature-map space. They additionally utilize a scale adaptive mechanism to allow for better generalizations across different sizes of anomaly.

Their method's specific construction utilizes two teacher models with the same weights, one "bad" and one "good". The good model is given benign images while the bad model is given images with synthetic anomalies. The student model is then trained to maximize its cosine similarity with the per-layer features of the good teacher while minimizing the cosine similarity with the bad teacher. At evaluation time anomaly scores are computed by comparing the scaled, per-layer feature spaces of the good teacher against those of the student. Inputs with high levels of dissimilarity between the good model and student are given high anomaly scores.

Their evaluation against prior work is very comprehensive, comparing against a total of 18 other detectors. They out perform all other detectors on all three datasets (lung, brain, and skin anomalies) in terms of their main metrics (AUC, F1, and Accuracy). The authors further perform ablations with respect to their main contributions of Contrastive Reverse Distilation and Scale Adaptive Mechanisms.

### Strengths
* Anomaly detection is somewhat outside my area of expertise, but the paper seems to frame itself well within the current body of literature. 
* The paper is well written and easy to follow. Figures are also informative and easy to understand.
* The idea of contrastive reverse distillation seems novel (to the best of my knowledge) and intuitive. I'd like to see how future works can iterate upon this framework in other settings or with improved constructions.
* Motivation is well established for the usage synthetic anomalies, and the choice of simplex noise is clever.
* Empirical analysis is very comprehensive in terms of datasets, baselines, and ablations.
* The proposed method out-performs all baselines in terms of AUC, F1, and Accuracy.
* The proposed method scales well with model architecture size, which is a good sign that the method is sensible.

### Weaknesses
In general, within my somewhat limited knowledge of this sub-field, I like this paper. In spite of that I think there are a few things the authors may want to consider to further strengthen their work.

I think when discussing detection and AUC scores it is important to give them context within the given domain. See section B of [1] for some example discussion on this topic from a different field. I'd like the authors to consider the following questions:

* Is it more important to maximize the true positive rate in spite of inducing some false positives? 
* Is it better to minimize false positives to increase confidence in the case of a positive prediction?
* How do you anticipate doctors using these tools in their analysis?

Given this, it would also be nice if the authors could plot some of the ROCs between their method and some of the baselines (maybe including all of them is too visually messy, but at least the top 5). This way people can compare their method to the baselines at different levels of false positive rate.

I think it would be good if the authors could include some extended discussion, either in the main body or the supplementary material, analyzing the more subtle features of their results. See the next section of my review "Questions" for some examples of what I think they can further analyze.

Lastly, the results of table 1 are good, but a bit overwhelming. I think it would help if the second best score in each metric is underlined and if the methods are visually grouped based on detector type (e.g. RD4AD, RD++, and ReContrast could be grouped together). Optionally it would be nice if all experiments were averaged over a few runs and given standard deviations or $\pm$ scores, at least in the supplementary material. I understand if these experiments are too extensive to replicate too many times, though.

### Questions
Here I include some questions for the authors to consider.

* Why does ISIC seem like the hardest dataset for all the detectors? Why is Brain Tumor the easiest?
* Why is SAM more impactful in the Brain Tumor dataset while it seems minimally impactful in the RSNA dataset in table 2? Is this related at all to the results of table 3 - where Gaussian noise performs similar to simplex noise on RSNA, but much worse on Brain Tumor?
* Can the method achieve better generalization by using a mixture of synthetic noise types, perhaps 10% gaussian, 90% simplex? 
* Can we improve performance by including some real world data in the training set, or will that harm generalization?

### Soundness
3

### Presentation
3

### Contribution
3
