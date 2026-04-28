# Rotation Has Two Sides: Evaluating Data Augmentation for Deep One-class Classification

- Decision: Accept
- Avg Score: 5.40
- Scores: 6, 6, 6, 3, 6

## Abstract
One-class classification (OCC) involves predicting whether a new data is normal or anomalous based solely on the data from a single class during training. Various attempts have been made to learn suitable representations for OCC within a self-supervised framework. Notably, discriminative methods that use geometric visual transformations, such as rotation, to generate pseudo-anomaly samples have exhibited impressive detection performance. Although rotation is commonly viewed as a distribution-shifting transformation and is widely used in the literature, the cause of its effectiveness remains a mystery. In this study, we are the first to make a surprising observation: there exists a strong linear relationship (Pearson's Correlation, $r > 0.9$) between the accuracy of rotation prediction and the performance of OCC. This suggests that a classifier that effectively distinguishes different rotations is more likely to excel in OCC, and vice versa. The root cause of this phenomenon can be attributed to the transformation bias in the dataset, where representations learned from transformations already present in the dataset tend to be less effective, making it essential to accurately estimate the transformation distribution before utilizing pretext tasks involving these transformations for reliable self-supervised representation learning. To the end, we propose a novel two-stage method to estimate the transformation distribution within the dataset. In the first stage, we learn general representations through standard contrastive pre-training. In the second stage, we select potentially semantics-preserving samples from the entire augmented dataset, which includes all rotations, by employing density matching with the provided reference distribution. By sorting samples based on semantics-preserving versus shifting transformations, we achieve improved performance on OCC benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a novel method to improve performance on one-class classification problem. They observe a strong correlation between the accuracy of rotation prediction and one-class classification. They introduce a two-stage unsupervised framework that differentiates rotations that are semantic preserving (rotation-agnostic images) vs semantic shifting (non-rotation agnostic images) to enhance performance on the one-class classification benchmarks.

### Strengths
- The method introduced detects rotations that remain unchanged and are semantically similar to original images, ensuring their exclusion as outliers. This method demonstrates sufficient generalizability for other transformation (ex., gaussian noise), as supported by section 4.3. I feel that this contribution is of sufficient interest to the research community.
- The results on OCC presented in the paper outperform the baselines and can be added on top on existing methods. It emphasizes the significance of identifying the transformations present in the original dataset before incorporating them into the pretext task for learning.

### Weaknesses
 - Related works section of the paper is difficult to follow and seems incomplete.
    - The subheading of **One-Class Classification** is particularly confusing as it lacks comprehensive discussion on the relevant OCC literature. The authors directly diverge to self-supervised learning methods for OCC. It fails to give complete picture of OCC for non-experts. I would suggest the authors to briefly also give an introduction to OCC and existing generative methods or point readers to more detailed survey paper [1]. Specifically, the related work should discuss the nuances of different OCC approaches, such as density estimation, support vector methods, and reconstruction-based techniques, and how they relate to the proposed method. The current discussion jumps directly into self-supervised learning without establishing the broader context of OCC.
    - There exists a confusion regarding anomaly detection and OCC cited in related work, in which cases are they both considered the same? The authors need to clarify the relationship between anomaly detection and one-class classification more precisely. While both aim to identify outliers, the training paradigms differ (anomaly detection often uses both normal and anomalous data, while OCC uses only normal data). This distinction is crucial and needs to be explicitly addressed in the related work section. The current discussion does not adequately clarify when these two problems can be treated interchangeably and when they cannot.
- Missing relevant citation: the authors seem to be missing an important citation on rotation estimation [2]. I would suggest the authors to include it for completeness of related work.

### Questions
- My major suggestions are summarized in Weakenesses section
- In introduction: “While rotation has been a widely used technique in the literature for OCC…” missing citations, please add them here?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The study makes a surprising discovery: a strong linear relationship exists between the accuracy of rotation prediction and the performance of OCC and they show that representations learned from transformations already present tend to be less effective. To address this, the paper proposes a staged learning-based framework for one-class classification (OCC) that aims to identify semantics-preserving images. The framework consists of two stages: self-supervised representation learning and transformation distribution estimation.

### Strengths
- I think the authors do a great job at explaining and motivating the problem they are working on.
- The paper seems novel in its exploration of the relationship between rotation prediction and one-class classification (OCC). It highlights a surprising observation of a strong linear relationship between the performance of rotation prediction and the performance of OCC.
- The authors back up their approach on empirical observations, highlighting the importance of effective data transformations and the potential decrease in effectiveness if transformations are already present in the dataset. This empirical foundation strengthens the credibility of their proposed solution. Their approach seems to be very well-motivated
- The experiments though little are well-designed, valid, and exhaustive, with comparison to a range of baselines as well as some ablation studies.

### Weaknesses
 - A big weakness right now is the lack of extensive empirical validation. The authors currently only perform experiments on CIFAR-10 and their experiments on other kinds of transformations are also very limited. Though the authors show interesting results for another transformation, it is immensely difficult with this set of results to comment on how well their approach could work.
- One of the really interesting findings from this paper is about transformation bias, and representations learned from transformations already present tend to be less effective. I believe this would be well-shown by experiments across multiple datasets and multiple kinds of models.
- How does the analysis across other kinds of popular transformations look like and does this approach still hold, I would encourage the authors to include talking about other transforms even if they do not seems to work well.
- This shouldn't use in-text citations

> facturing defect detection (Bergmann et al., 2020; 2019) and medical diagnosis Schlegl et al. (2017).

### Questions
- How does the analysis across other kinds of popular transformations look like and does this approach still hold, I would encourage the authors to include talking about other transforms even if they do not seems to work well.
- This shouldn't use in-text citations

> facturing defect detection (Bergmann et al., 2020; 2019) and medical diagnosis Schlegl et al. (2017).

### Soundness
2 fair

### Presentation
3 good

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
This paper proposes a technique that can learn the rotation distribution of images within a dataset. The approach is motivated by the authors' study of one-class classification (OCC), which involves predicting whether data belongs to a particular class seen in training or is anomalous. Specifically, the authors are investigating the seeming strong linear relationship between rotation prediction accuracy and OCC. The authors attribute this to transformation bias, where samples that are semantic-preserving vs. semantic-shifting lead to different behavior when training OCC with contrastive learning approaches.

To this end, the authors propose a two-stage approach for learning the transformation distribution: 1) perform a standard contrastive self-supervised representation learning phase, and 2) transformation distribution estimation. For 2, the authors create a dataset consisting of the original samples in {0, 90, 180, and 270} degrees and learn a differentiable sampler with Gumbel Softmax to predict images that preserve semantics (i.e., rotating it does not necessarily change the orientation at which the picture must have been taken). Finally, MMD is used to perform density matching in the representation space to identify such semantic-preserving samples.

The authors use their model to 1) visually show a good model in learning RAIs vs. non-RAIs, 2) a correlation between the amount of RAIs in training and OCC performance, and 3) that using their approach consistently adds ~1% gain to OCC.

### Strengths
The strengths of the paper include a clear motivation, strong analysis of the correlation between rotation prediction and OCC, and its unsupervised data-driven approach. The intuition to use a predictor in conjunction with the contrastive pretrained representations and density estimation to align the dataset makes sense for extracting out the transformation distribution exhibited within the training set. Understanding this distribution is an interesting task. The visual results of selecting RAI vs. non-RAI images are compelling. The issues with existing OCC approaches are well-analyzed and the the proposed approach provides modest but consistent improvement to existing OCC approaches.

### Weaknesses
One weakness is that there is not a quantifiable way to measure the accuracy in RAI vs. non-RAI determination. One reason for this is that RAI images may be classified as 0, making it hard to separate these images from the truly non-RAI images. There is also not a discussion / inclusion of failure modes to understand where the model may succeed vs. fail. Another weakness is that the utility of the transformation distribution may be larger but is focused on OCC, and datasets used to evaluate OCC are from CIFAR-10, which may have different characteristics than some of the anomaly detection settings where labeled data of out-of-distribution samples could be limited. I also think it is odd that OCC is a common thread / motivator of the paper but the description of the technique for OCC is not in the approach section. The claim of the paper then is a bit broad, in some parts reading as if it is most concerned about OCC and other parts about the distribution being learned.

### Questions
1. In Section 4.2: it seems that images with a prediction of 0 is deemed non-RAI and anything else is deemed to be RAI. Couldn't RAI images still be predicted with an angle of 0? How many of the RAI images are classified as angle 0 and how many images classified as angle 0 are actually RAI?

2. Do you have any examples / analysis of failure modes where images like those in figure 5 are mistakenly predicted to be RAI vs. non-RAI?

3. Can you clarify the rule used in section 4.4 to determine if a sample is semantically-shifted? Which r is used?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Targeting improvement of existing OCC, this paper makes an observation of the strong linear relationship between the rotation prediction and the performance of OCC. To the end, this paper proposes a two-stage framework where in the first stage, standard contrastive learning is used, while in the second stage, semantics-preserving samples are selected from the augmented dataset. Experiments are conducted on several anomaly detection benchmarks.

### Strengths
1.	The contribution is clear, and the motivation sounds reasonable.
2.	Analysis on the impact of rotation prediction on OCC is intuitive.
3.	Experiments show the effectiveness of the proposed method.

### Weaknesses
1. While the analysis is intriguing, its applicability remains limited to rotation-related datasets and methods. For instance, it may not be suitable for numerous real-world anomaly detection tasks, such as MVTec and VisA. The core idea of relying on rotation prediction as a proxy for anomaly detection is inherently constrained by the nature of the augmentation. Datasets where rotation is not a meaningful transformation, or where anomalies do not manifest as rotational deviations, will not benefit from this approach. This significantly limits the generalizability of the proposed method.

2. The improvements, as depicted in Table 1, are somewhat modest compared to existing methods. The reported gains, while present, do not demonstrate a substantial leap in performance. Given the complexity introduced by the two-stage framework and the selection of semantics-preserving samples, the marginal improvements raise questions about the practical utility of the approach. A more thorough comparison with state-of-the-art methods, especially those achieving higher performance, is needed to contextualize the significance of these results.

3. An essential evaluation is missing. This paper identifies RAI images and treats them differently from the original method. However, it is unclear whether the observed improvement stems from these RAI images alone. Assessing the performance of RAI images separately might lead to a more substantial improvement. The lack of a controlled experiment isolating the impact of RAI images makes it difficult to ascertain the true source of the performance gains. It is crucial to understand if the method is truly effective or if the improvement is merely a consequence of focusing on a specific subset of augmented data.

4. The paper's structure could be improved. There is significant overlap in the information presented in Figures 1, 2, 4, 5, 6, and 7. It may be advisable to move figures like 4-7 to the supplementary section. The current presentation leads to redundancy and makes it difficult to follow the core arguments. Consolidating the figures and streamlining the narrative would enhance the clarity and readability of the paper.

5. The rationale behind the authors' decision to use the version of UniCon without soft aggregation and hierarchical augmentation remains unclear. Since hierarchical augmentation is an integral module within UniCon, it is advisable for the authors to use the full version of UniCon as the baseline for their study. This choice raises concerns about the fairness of the comparison and whether the observed improvements are truly attributable to the proposed method or simply a consequence of using a weaker baseline.

### Questions
See the weakness.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This work targets improving OCC performance by discriminating the RAIs in the training dataset, which is inspired by a surprising observation: there exists a strong linear relationship between the accuracy of rotation prediction and the performance of OCC. The proposed distribution matching-based method is interesting and proved to be effective.

### Strengths
1. The idea is novel and interesting.
2. The proposed method is promising and well-analyzed.
3. The paper writing is good.

### Weaknesses
1. In the first stage of the proposed method, there is no reason presented for the choice of contrastive pre-training. Specifically, it's unclear why a contrastive approach is superior to other self-supervised methods for learning initial representations, especially given the goal of discriminating RAIs. The paper should justify this choice with respect to the specific properties of the learned representations that are beneficial for the subsequent distribution matching step. For example, do contrastive methods provide a more separable feature space for rotated and non-rotated images compared to other self-supervised techniques?
2. There are no large-scale dataset evaluations, such as imagenet. The experiments are limited to relatively small datasets, which raises concerns about the generalizability of the proposed method to more complex and diverse datasets. The performance on larger datasets with more classes and variations should be evaluated to demonstrate the robustness of the approach.
3. There is no direct quantitative evaluation of the RAI predictions. For instance, can the authors annotate a test set with binary labels of whether or not a sample is RAI? Without this, the evaluation of the core contribution is incomplete. The paper relies on the downstream OCC performance as a proxy for RAI identification, but it would be beneficial to directly assess the accuracy of the RAI predictions themselves. This could involve metrics such as precision, recall, and F1-score on a held-out set with ground truth RAI labels.

### Questions
1. In Page 1 "In cases where real-world outliers are lacking, one typical solution is to generate negative samples by applying geometric transformations, such as rotation, to the training samples.", why are the augmented samples negative?
2. In Sec.3.1, are other pre-trained models suitable for stage 2? Why?
3. In Sec.3.2, how to ensure there is one sample in p_i belonging to the input domain after xy-shuffling?
4. How to pick the RAI samples according to Eq. (2）？
5. There is no definition of p(R_{r}(x)) before it is been used in Eq.(2). And the end of Eq.(2) should be a period.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
