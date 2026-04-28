# Adaptive Hierarchical Certification for Semantic Segmentation using Randomized Smoothing

- Decision: Reject
- Avg Score: 3.75
- Scores: 3, 6, 3, 3

## Abstract
Certification for machine learning is proving that no adversarial sample can evade a model within a range under certain conditions, a necessity for safety-critical domains. Common certification methods for segmentation use a flat set of fine-grained classes, leading to high abstain rates due to model uncertainty across many classes. We propose a novel, more practical setting, which certifies pixels within a multi-level hierarchy, and adaptively relaxes the certification to a coarser level for unstable components classic methods would abstain from, effectively lowering the abstain rate whilst providing more certified semantically meaningful information. We mathematically formulate the problem setup, introduce an adaptive hierarchical certification algorithm and prove the correctness of its guarantees. Since certified accuracy does not take the loss of information into account for coarser classes, we introduce the Certified Information Gain ($\mathrm{CIG}$) metric, which is proportional to the class granularity level. Our extensive experiments on the datasets Cityscapes, PASCAL-Context, ACDC and COCO-Stuff demonstrate that our adaptive algorithm achieves a higher $\mathrm{CIG}$ and lower abstain rate compared to the current state-of-the-art certification method.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Tihis work presents an adaptive hierarchical certification method for semantic segmentation. To this end, the authors builds a hierarchical structure for the classes. Then, they reformulate the SegCertify with some changes for the semantic segmentation. In additon, the authors inroduce an evaluation metric. Experiments on Cityscapes and ACDC datasets partly verify the effectiveness of the proposed methods.

### Strengths
1. This work is easy to follow, since most of the techniques are based on previous works [Fischer et al.,2021][Lecuyer et al.,2019]
2. The proposed method shows better results than SegCertify [Fischer et al.,2021]

### Weaknesses
There are some key concerns:

1. Technical contributions

In fact, this work is largely based on SegCertify [Fischer et al.,2021]. The key differences are the hierarchical structure for semantic classes and the CIG metic for evaluation.  However, in my view, the proposed methods in section 4 are just a simple modification of SegCertify. There are no essential differences in theory. The new formulas are direct changes because of the different input shapes. As for the CIG, there are no insights why we should use that form. I agree that we need more robust certification methods for segmentation. However, the methods in this work is not a game-changer for this topic. 

2.Insufficeint experiments

First, there are no comparisions with other segmentation methods. As a typical vision task, should the authors provide reuslts with the mIoU, mAP, etc? I suggest the authors add more comparisions with segmentation methods. Second, from the results in Tab.1, there are no significant differences in the performance (the gaps < 2%). They are too small. It is not convicning. Third, there are no enough examples to clarify the final conclusion. In fact, the authors only present the results with 100 images (If I misunderstand, corret me). Please list the results of the whole datasets. Finally, there are no visual examples for the failure cases. And the figure 1 is not enough.

3.Unclear details

There are many unclear details. For examples, what is the meaning of IP in Eq.1? What are the type I and type II errors? How do the SAMPLEPOSTERIORS and HSAMPLE operate?  What is the effect of using different hierarchical structure for semantic classes?

### Questions
Please see the weakness part.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
1: You are unable to assess this paper and have alerted the ACs to seek an opinion from different reviewers.

### Summary
The work proposes an adaptive hierarchical certification method for segmentation. It adaptively relaxes the certification to a coarser level within the hierarchy, which helps lower the abstain rate and provides more semantic information. This problem is also mathematically formulated. Experiments also show that the proposed method beats the current state-of-the-art methods.

### Strengths
This paper is well-organized and presents a technically sound method to lower the abstain rate, which is also verified in the experiments.

### Weaknesses
I am not familiar with the area of certification for segmentation. When I read the preliminaries, the equations are not really that easy to follow. For example, in Eq.(1), what does IP means, and why do we use that. The authors should elaborate more clearly on that. Specifically, the use of $\mathbb{P}$ to denote probability is not immediately obvious within the context of the equation, especially for readers not deeply familiar with the certification literature. The notation, while standard in probability theory, requires more explicit definition in this specific context. Furthermore, the motivation for using this particular formulation of the probability within the certification framework is not sufficiently explained. It is unclear why this specific probability measure is chosen over other potential formulations, and what assumptions it makes about the underlying data distribution or the segmentation model itself. This lack of clarity makes it difficult to assess the validity and applicability of the proposed method.

### Questions
Actually, I am sorry that I am not really an expert on this area, and at present I do not have enough time to learn the related knowledge from scratch. So I cannot give any professional comment. That would be great for us if the authors could give more detailed explanations on the theorems.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces the concept of adaptive hierarchical certification for image semantic segmentation by mathematically formulating the problem and its adaptation to a pre-defined class hierarchy. This paper proposes ADAPTIVECERTIFY, the first adaptive hierarchical certification algorithm, which certifies the image pixels within different fine-to-coarse hierarchy levels.

### Strengths
1. The research problem is very important. 
2. The paper is overall well-structured.

### Weaknesses
1. The technical contributions are not clear. There are some components combined together. What is the contribution of each component? Specifically, the paper introduces an adaptive hierarchical certification method, but it's not clear how the adaptation mechanism contributes independently from the hierarchical certification itself. The novelty of the adaptation, in terms of both the mathematical formulation and the algorithmic implementation, needs to be more clearly delineated from existing hierarchical certification techniques. The paper should clarify the specific technical challenges addressed by the adaptive component and how it overcomes limitations of non-adaptive approaches.
2. The experiments are insufficient. The authors should compare with more baselines on more datasets. The current experiments only compare against a single baseline, SegCertify, which is insufficient to demonstrate the effectiveness and superiority of the proposed method. The experimental evaluation should include comparisons with other relevant methods, such as those that perform hierarchical classification or robust semantic segmentation, even if they are not directly designed for certification. Furthermore, the evaluation should be performed on a wider range of datasets, including those with different characteristics (e.g., varying image complexity, class distributions, and annotation quality) to assess the generalizability of the proposed approach.

### Questions
1. Highlight the contribution of each component.
2. Provide more experimental results.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper aims to present a new certification method for the semanitc segmentation task. Previous relevant works mostly aim to solve the classification task. This paper is among the first to explore a new certification method, namely adaptive hierarchical certification and design a new evaluation metric. The authors clearly explain the proposed method and conduct a series of experiments to show that the proposed adaptive hierarchical certification performs better than previous works.

### Strengths
- The novelty of this paper is clear. Introducing a hierarchical certification method is more suitable for the semantic segmentation task, which needs to predict a class for each pixel.

- The presentation of this paper is good. The authors clearly explain the background of the proposed approach and then clearly describe the method.

- Experiments show that the proposed approach receives good results in terms of the proposed CIG metric.

### Weaknesses
 - It seems that Theorem 1 is originally from (Fischer et al., 2021), not sure why put it in the main paper. 

- It is glad to see that the authors proposed to use the class hierarchy graph to do certification, which has never been proposed in previous works as far as I know. However, a problem of introducing class hierarchy is that when applied to a new dataset, for example, the ADE20k dataset, a new class hierarchy graph should be prepared. Not sure how to make the proposed method universal to different segmentation datasets.

- Fromt the paper, it seems that the proposed method only use two datasets, i.e., Cityscapes and ACDC, to evaluate the proposed method. As these two datasets, as mentioned in the paper, are composed of only 19 classes, two questions consequently come:

  - First, more datasets should be used to evaluate the performance of the proposed method.
  - Second, the Cityscapes dataset only contain 19 classes. I think the authors should do some experiments on some dataset with more classes. A proper one might be the ADE20K dataset, which has more than 100 semantic categories. This would definitely verify the effectiveness of the adaptive hierarchical certification method.

- I also think some segmentation results should be visualized to see in which cases the proposed adaptive hierarchical certification helps.

- From the paper, we can see that 7/9 space of this paper is used describe the introduction, related work, and method. Less than 2/9 of the space in the main paper are used to do experiment evaluation. Though there is some experimental analysis in the supplementary material, this is not adequate to well evaluate the proposed method and metric as posted in the weaknesses part.

### Questions
- From the paper, we can see that 7/9 space of this paper is used describe the introduction, related work, and method. Less than 2/9 of the space in the main paper are used to do experiment evaluation. Though there is some experimental analysis in the supplementary material, this is not adequate to well evaluate the proposed method and metric as posted in the weaknesses part.

I am not a researcher doing this research field but it really needs some efforts to further improve this paper.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good
