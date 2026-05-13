# Gandalf: Learning label correlations in Extreme Multi-label Classification via Label Features

- Decision: Reject
- Scores: 5, 6, 5, 5

## Abstract
Extreme Multi-label Text Classification (XMC) involves learning a classifier that can assign an input with a subset of most relevant labels from millions of label choices. Recent works in this domain have increasingly focused on a symmetric problem setting where both input instances and label features are short-text in nature. Short-text XMC with label features has found numerous applications in areas such as query-to-ad-phrase matching in search ads, title-based product recommendation, prediction of related searches. In this paper, we propose \textit{Gandalf}, a novel approach which makes use of a label co-occurrence graph to leverage label features as additional data points to supplement the training distribution. By exploiting the characteristics of the short-text XMC problem, it leverages the label features to construct valid training instances, and uses the label graph for generating the corresponding soft-label targets, hence effectively capturing the label-label correlations. Surprisingly, models trained on these new training instances, although being less than half of the original dataset, can outperform models trained on the original dataset, particularly on the PSP@k metric for tail labels. With this insight, we aim to train existing XMC algorithms on both, the original and new training instances, leading to an average 5\% relative improvements for 6 state-of-the-art algorithms across 4 benchmark datasets consisting of up to 1.3M labels. \textsc{Gandalf} can be applied in a plug-and-play manner to various methods and thus forwards the state-of-the-art in the domain, without incurring any additional computational overheads.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies Extreme Multi-label Text Classification (XMC) problems, which assigns a short text input sample with a subset of most relevant labels from millions of label choices. The principal difficulty in XMC is managing the vast array of possible classes. Building upon existing research, this work incorporates the textual features of labels into the classifier's training process. Especially, given that input samples often share common tokens with the labels they're associated with, this task becomes correlating short text inputs with related sets of text.  For example, the input sample “2022 French presidential election” could be associated with “April 2022 events in France”,  “2022 French presidential election”, “2022 elections in France”, “Presidential elections in France.”

While previous research has explored various methods for aligning input and label texts, this paper proposes a straightforward technique for data augmentation, illustrated in Figure 1. It enhances the original N*L training data matrix with an additional L*L matrix, which captures the interrelationships between the L labels. The results from experiments suggest that this enrichment with the L*L matrix enables established XMC classifiers to attain better accuracy in classification tasks.

### Strengths
1)	The data augmentation concept introduced in this paper is refreshingly straightforward, offering an intuitive strategy to expand the training dataset.
2)	Empirical assessments indicate that incorporating this additional data into the training process proves beneficial.

### Weaknesses
1.	The augmented dataset introduced is considerably large, e.g., potentially consisting of a large matrix in size of millions by millions. The training time will be significantly increased.  While it's true that this does not affect the inference time, it substantially extends the duration of the training phase due to the increased volume of data. The paper does not provide a clear analysis of the computational overhead of generating and utilizing this L*L matrix, specifically regarding the time and memory requirements for both its creation and integration into the training process. This lack of detail makes it difficult to assess the practical feasibility of the proposed approach, especially for extremely large label spaces.
2.	The two-tower model “NGAME + classifier” yields the highest performance on the Amazon datasets. Even with the introduction of additional data, the base algorithms do not surpass the efficacy of the two-tower. The paper does not adequately explore why the proposed data augmentation technique fails to provide a substantial boost to the base algorithms, particularly when compared to the two-tower model. It is unclear if the issue lies in the quality of the augmented data or the limitations of the base algorithms to effectively utilize this additional information. The analysis should delve deeper into the interaction between the augmented data and the base classifiers.
3.	Some reference citations are missing: Zhang et al., 2021a; ?; Lu et al., 2022),  ANCE (?)

### Questions
1)	What is the computation cost for training the base algorithms when taking the additional L*L matrix? including the process of obtaining the L*L matrix.  It would be beneficial for the paper to detail the expected impact on the training duration.
2)	Why there is no evaluation of two-tower models on the two wiki-dataset?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposes Gandalf, which augments the training dataset in extreme classification by using label features as documents, with their corresponding “label mapping” being constructed using a label-label graph. Such a setup allows most existing extreme classifiers to now leverage label features for improved generalization, without any changes to the training pipeline and no added inference cost. Gandalf shows significant improvement in both Precision and Propensity-scored Precision metrics over four commonly used extreme classification datasets.

### Strengths
- The proposed methodology is architecture-agnostic thereby resulting in easy and widespread adoption.
- Consistently improved performance for a variety of extreme classifiers, especially for tail labels.

### Weaknesses
 - The training time will be significantly increased since the new number of training points will be number of documents + number of labels. And in typical extreme classification setups, the number of labels can be much greater than the number of available documents.
- The approach assumes (1) label features exist in the same input space as documents; and (2) the extreme classifier is NOT a two-tower approach, and embeds the labels and documents in the same space.

### Questions
- What if you use graphs other than the random-walk graph in ECLARE? For example, the co-occurrence graph?
- Why should the performance of classifiers that already use label-features (e.g., ECLARE, DECAF) improve with Gandalf?
- To combat the increased training cost, it would be interesting to understand the sample efficiency of Gandalf. To be more specific, how much performance is improved when augmenting, e.g., {0, 25, 50, 75, 100}% of random labels to the training data?
- Missing citations in multiple places in the paper.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a data augmentation method called Gandalf which leverage label correlation as additional data points against short-text extreme multi-label text classification problem. The presented experiment results show Gandalf is able to improve the performance on other extreme classifiers on several benchmark datasets.

### Strengths
1)	The proposed data augumentation idea is relatively simple and work effectively on several benchmark datasets.

2)	The empirical studies are relatively abundant.

### Weaknesses
1) The underlying idea of the main method a little bit lacks novelty and seems an extension of the existing work likes ECLARE.

2) The method does not contribute to the real-world settings as most XMC methods choose to make partial experiments on long-text benchmark datasets. Besides, the method seems to increases the overhead of training datasets which may cause limitations.

### Questions
1)	Why classical XMC problems like AttetionXML, SiameseXML++ are not experimented with Gandalf?

2)	It seems that the proposed Gandalf does not give competitative performance on PSP metrics compared to existing methods. Do you think Gandalf is an effective method dealing with the tail labels in XMC problem?

3)	Can Gandalf work on long-text XMC datasets?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Gandalf, a novel approach which makes use of a label correlation graph to leverage label features as additional data points to supplement the training distribution. Their approach can be applied in a plug-and-play manner with several existing methodologies, leading to a 30% performance improvement. The authors focus on the short-text setting where they exploit the symmetry between inputs and labels to obtain improved learning of label correlations. They propose an approach leverages the innate symmetry of short-text XMC along the LCG to construct valid data-points.

### Strengths
* The approach can be applied in a plug-and-play manner with several existing methodologies - the results of which have been demonstrated in Table 2. 
* They have used publicly available benchmark datasets to evaluate their results.
* Gandalf shows relatively large improvement of 30% over 5 state-of-the-art algorithms across 4 benchmark datasets.

### Weaknesses
 * The authors focus on short text. While it is widely used across the industry, it will be good to demonstrate why their approach is better for short text when compared to other approaches. In a sense what makes the approach more suited for short-text? At the same time, would the approach work on large text as well?

* It will be great if the authors can elaborate on the "Symmetric nature of short-text XMC". An example to illustrate the symmetric form would strengthen the reasoning for utilizing the symmetry. Especially when the paper in a way hinges on the utilizing the symmetry along with the label correlation graph; LCGs have been used in other approaches. As a result, the novelty seems limited. 

*Along the same lines, it will greatly help if the authors can detail how the approach can handle the sparse instance-to-label mapping present in the datasets.  

A minor issue: I believe there are a few missing references in the paper and the supplemental material.

### Questions
Addressed in the weakness.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
