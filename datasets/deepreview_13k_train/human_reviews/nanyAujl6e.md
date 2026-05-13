# Out-of-Distribution Detection with Negative Prompts

- Decision: Accept
- Scores: 6, 8, 6, 5

## Abstract
Out-of-distribution (OOD) detection is indispensable for open-world machine learning models. Inspired by recent success in large pre-trained language-vision models, e.g., CLIP, advanced works have achieved impressive OOD detection results by matching the *similarity* between image features and features of learned prompts, i.e., positive prompts. However, existing works typically struggle with OOD samples having similar features with those of known classes. One straightforward approach is to introduce negative prompts to achieve a *dissimilarity* matching, which further assesses the anomaly level of image features by introducing the absence of specific features. Unfortunately, our experimental observations show that either employing a prompt like "not a photo of a" or learning a prompt to represent "not containing" fails to capture the dissimilarity for identifying OOD samples. The failure may be contributed to the diversity of negative features, i.e., tons of features could indicate features not belonging to a known class. To this end, we propose to learn a set of negative prompts for each class. The learned positive prompt (for all classes) and negative prompts (for each class) are leveraged to measure the similarity and dissimilarity in the feature space simultaneously, enabling more accurate detection of OOD samples. Extensive experiments are conducted on diverse OOD detection benchmarks, showing the effectiveness of our proposed method.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposes how to use CLIP for OOD detection with negated prompts that include the negation word 'not'. Using the learnable prompts embeddings, the method trains the model by freezing the CLIP encoders based on a contrastive loss. The proposed method shows improvement over the baseline CLIP for OOD detection.

### Strengths
1. The paper is clearly written with descriptive visual figures.
2. Experiments have been extensively conducted across a set of diverse datasets including small ones and large ones.

### Weaknesses
1. Comparison and related works to state-of-the-arts are missing (e.g., NNGuide [1], ASH [2], CLIPN [3], [4])
2. The performance is too behind the state-of-the-art
3. The main concept of the paper is too similar to CLIPN
4. The performance improvement is very marginal

### Questions
I suggest the authors to properly address the above weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors perform OOD detection based on generic features learned from a large pre-trained language-vision model by matching the similarity between image features and features of learned positive prompts and negative prompts.
The core innovation of this paper is the proposed LSN module to learn a set of negative prompts for each ID category to help the network to comprehend the concept of "not." They mine general negative features that are not present in a category but are present in all other categories by proposing a new loss in prompt learning. In the test, the MCM scores of the cosine similarity of positive prompts and negative prompts to image features are used as OOD detection metrics. Extensive experiments on various ood detection benchmarks have been conducted to demonstrate the effectiveness of the method proposed in this work.

### Strengths
1、This work utilizes the generic feature extraction capability of CLIP and does not need to finetune the image encoder and text encoder. It only needs to learn the appropriate positive and negative prompts by LSN for OOD detection. Therefore this method has high generality and low complexity.
2、SOTA performance is achieved in different benchmark experiments.

### Weaknesses
The overall prompt learning approach is still based on CoOp without a lot of innovation.

This method is very dependent on the features learned by CLIP. If the features extracted by CLIP itself for some categories of images are not strongly discriminative, the effect of learning the prompts based on these features may be poor.

The way to learn negative prompts is to mine the general negative features that each class of samples does not have but all other classes have, i.e., the negative classifier produces low activation values for that class and high activation values for other classes. Does this result in learning what are actually generic background features rather than general features that all other classes have?

### Questions
1, This method is very dependent on the features learned by CLIP. If the features extracted by CLIP itself for some categories of images are not strongly discriminative, the effect of learning the prompts based on these features may be poor.
2, The way to learn negative prompts is to mine the general negative features that each class of samples does not have but all other classes have, i.e., the negative classifier produces low activation values for that class and high activation values for other classes. Does this result in learning what are actually generic background features rather than general features that all other classes have?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
In this paper, the authors present a negative prompt tuning method with CLIP to improve the OOD performance. Specifically, the authors learn class-specific prompts for each category. A semantic orthogonality loss is also applied to encourage diverse negative prompts. The negative prompts are also considered in the evaluation.

### Strengths
1. The proposed LSN method achieves good performance over baselines on various OOD benchmarks.
2. The authors provide sufficient ablation studies to show the effectiveness of each proposed component.
3. The proposed idea is simple and easy to understand.

### Weaknesses
1. This paper is related to negative learning or learning with complementary labels. The authors may consider adding some related discussion in the related work section.
2. The proposed method may double the training and inference time with the negative prompts.
3. I found a related work that the authors may add discussion in the related work section: " How Does Fine-Tuning Impact Out-of-Distribution Detection for Vision-Language Models? , IJCV 2023."


### Questions
1. What's the ID dataset in Table 3?
2. Why do CoOp/CoCoOp and CoOp/CoCoOp + LSN achieve the same ID results in Table 1 and Table 2?
3. The ID results of CoOp/CoCoOp appear to be significantly lower than other baselines such as NPOS in Table 2. Can the authors explain some reasons?

Some minor suggestions that do not affect my final rating:
1. It is suggested to use `\citep' rather than `\cite' in the latex code
2. Typo: 'we use we use' at the bottom of page 6

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper focuses on the out-of-distribution detection problem, which aims to precisely classify samples of known categories, and accurately discern samples of unknown categroies. To facilitate the recognition the out-of-distribution examples, a CLIP-based method is proposed, where a set of learnable negative prompts for each class are introduced. Promising results are obtained compared to existing out-of-distribution detection methods.

### Strengths
1. This paper is clearly written and easy to follow. The weakness of the hand-crafted prompts is clearly interpreted and the motivation is reasonable.
2. The proposed approach is simple and intuitive.
3. Promising experimental results are achieved compared to existing OOD detection and prompt-based methods.

### Weaknesses
1. Meta-Net in Figure 6 is not introduced in the paper.
2. The motivation and model design of this paper are similar to DualCoOp. The authors claim that the proposed method could learn negative prompts to capture negative features compared to DualCoOp, but there is no visual or quantitative evidence to verify this statement. Besides, the OOD detection performance of the DualCoOp design is not experimentally verified.
3. Some existing OOD detection methods proposed in 2022 and 2023 are not compared or discussed[2][3][4].
4. It seems that the authors have submitted this paper with an ICLR 2023 template.

### Questions
In equation(9), the positive score and the negative score are obtained independently. If the obtained positive category is different from the negative category, could this lead to mistakenly recognizing a correct positive prediction as out-of-distribution?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
