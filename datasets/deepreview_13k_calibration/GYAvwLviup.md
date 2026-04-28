# Aligning brain functions boosts the decoding of videos in novel subjects

- Decision: Reject
- Avg Score: 4.25
- Scores: 5, 6, 3, 3

## Abstract
Deep learning is leading to major advances in the realm of brain decoding from functional Magnetic Resonance Imaging (fMRI). However, the large inter-subject variability in brain characteristics has limited most studies to train models on one subject at a time. Consequently, this approach hampers the training of deep learning models, which typically requires very large datasets.
Here, we propose to boost brain decoding by aligning brain responses to videos and static images across subjects.
Compared to the anatomically-aligned baseline, our method improves out-of-subject decoding performance by up to 75\%.
Moreover, it also outperforms classical single-subject approaches when fewer than 100 minutes of data is available for the tested subject.
Furthermore, we propose a new multi-subject alignment method, which obtains comparable results to that of classical single-subject approaches while improving out-of-subject generalization.
Finally, we show that this method aligns neural representations in accordance with brain anatomy.
Overall, this study lays the foundations for leveraging extensive neuroimaging datasets and enhancing the decoding of individuals with a limited amount of brain recordings.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper is aimed at improving subject video decoding from BOLD functional responses obtained during a movie watching paradigm. To this end, the authors perform brain response alignment via an optimal transport methodology, followed by a linear regression to predict latent representations of video frames (obtained by standard encoder models such as CLIP or VD-VAE).  They find that this method improves out of subject video decoding performance when compared to a purely anatomical alignment approach. They also examine multi-subject alignment in comparison to single subject approaches when limited number of paired recordings are available

### Strengths
The paper provides some interesting insights into the use of functional alignment models for studying BOLD responses in the context of naturalistic stimuli. Although the alignment methodology is not entirely a novel contribution in and of itself, the experimental setup is well deigned to examine the hypotheses being tested. The findings are clearly presented and motivated

### Weaknesses
The major weakness of this paper is the limited number of subjects that are available for testing. Given that only three different subjects are used, it is unclear whether the findings of the paper and insights will generalize for a larger population.


### Questions
1. It is not clear how sensitive the method to the choice of image latent representation/granuarity of features? How was the choice of representational models (such as CLIP or VD-VAE etc) made, is one or the other more suitable for this evaluation setup? Additionally, is there a reason the video frame decoding is restricted to a linear regression parameterization

2. How was the choice of retrieval metric made? Is there a reason standard metrics such as mean average precision, or NDCG are not appropriate for evaluating this task?

3. It would be nice to provide more context to explaining the design and modeling strategy in Eq. (1). The way it is currently presented requires the reader to flip back and forth between this manuscript and Thual et al 2022 to understand the methodology properly.

4. It would be nice if a higher resolution image for Figure 2 could be made available to understand the false retrieval cases. Additionally, it would be nice to provide more description in the appendix to help the reader interpret the extended experimental observations.

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The work deals with the decoding of high-level visual features from fMRI recordings. The authors use functional alignment to align fMRI data across subjects. The work claims that using functional alignment instead of standard structural methods boosts the decoding performance when there is limited data available for the subject in case. Further, training a model with aligned subjects can be used, whereas previous models could only decode responses specific to a subject.

### Strengths
Using functional alignment to improve decoding of visual representations across subjects is novel and noteworthy. The quantification of decoder performance with respect to data size is noteworthy.

### Weaknesses
The approach of showing the left-out subject the same video as the reference subject is a substantial weakness. This coupled with the functional alignment could theoretically act as a “leakage” mechanism for the data. The use of shared stimuli for alignment introduces a potential confound, where the alignment might be learning to map responses based on stimulus similarity rather than genuine functional correspondence. This is especially concerning given the claim that the method allows for generalization across subjects, as the shared stimulus could be driving the observed performance boost. The paper lacks a clear demonstration that the functional alignment is truly aligning brain responses based on underlying functional organization, rather than simply matching responses to the same stimuli. The current approach does not adequately address the possibility that the alignment is overfitting to the shared stimulus, leading to inflated decoding performance when tested on data from the same stimulus category.

### Questions
Does one repetition in line 268 mean the first trail or the second? 

Line 281 says the left-out subjects have to watch the same videos, while, line 265 says the subjects are shown the test stimuli for the first time. Does this mean the videos shown themselves are new to the subjects?

Where is it shown that the approach aligns brain responses in accordance with brain anatomy? ( LIne 12)

Perhaps, adding at least a single subject comparison where the subject is shown different stimuli may help have more robust results

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes to boost the decoding of videos in a single left-out subject with an alignment model and a decoder. The alignment model includes anatomical alignment and functional alignment. Finally, the pre-trained image encoder is used to obtain the video output.

### Strengths
The proposed ideas are simple and intuitive. It's quite generic and can be applied to different models.

### Weaknesses
1. The novelty needs to be further elaborated.
1. The proposed method lacks a comparison with other models. As a result, the effectiveness of the method is not convincing and requires further validation.
2. The proposed method in this paper employs one reference subject. How to deal with multiple reference subjects in practice?

### Questions
Please refer to the weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed a aligment method to boost the performance of brain decoding.

### Strengths
This paper proposed a simple method for brain decoding.

### Weaknesses
1.The loss function has three parameters. How to choose the parmeters is difficult.
2.The proposed method should be compared with the state-of-the-art methods.

### Questions
1. The dataset is very small. Hence, How is the generalization of the model？
2. The proposed method don't compared with the state-of-the-art methods.

### Soundness
1 poor

### Presentation
1 poor

### Contribution
2 fair
