# Scaling for Training Time and Post-hoc Out-of-distribution Detection Enhancement

- Decision: Accept
- Scores: 6, 6, 8, 5

## Abstract
The capacity of a modern deep learning system to determine if a sample falls within its realm of knowledge is fundamental and important.
In this paper, we offer insights and analyses of recent state-of-the-art out-of-distribution (OOD) detection methods - extremely simple activation shaping (ASH). We demonstrate that activation pruning has a detrimental effect on OOD detection, while activation scaling enhances it.
Moreover, we propose SCALE, a simple yet effective post-hoc network enhancement method for OOD detection, which attains state-of-the-art OOD detection performance without compromising in-distribution (ID) accuracy. By integrating scaling concepts into the training process to capture a sample's ID characteristics, we propose \textbf{I}ntermediate Tensor \textbf{SH}aping (ISH), a lightweight method for training time OOD detection enhancement. We achieve AUROC scores of +1.85\% for near-OOD and +0.74\% for far-OOD datasets on the OpenOOD v1.5 ImageNet-1K benchmark.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors first analyze the OOD detection method ASH and then propose a post-hoc network enhancement method for OOD detection, namely SCALE. Besides, they propose a Intermediate Tensor Shaping method for training time OOD detection enhancement.

### Strengths
1.	The proposed method is simple and easy to implement.
2.	The results of the proposed method are better than the SOTA method ASH.

### Weaknesses
1.	Could the authors provide an algorithm to demonstrate the overall pipeline of the proposed method? I am confused about when we should invoke the method in Section 3.4.
2.	Recently, Transformer-based models become more and more popular. Could the proposed method be applied to these models?

### Questions
I am not familiar with this OOD detection field. However I think the proposed method is simple and effective based on the current manuscript.

### Soundness
3 good

### Presentation
3 good

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
The authors present Intermediate Tensor SHaping (ISH) method for efficient OOD detection.

### Strengths
The method presented in this work is interesting and innovative. I appreciate the idea and encourage authors to further the work along this domain.

### Weaknesses
The method is tested only in Imagenet. The authors should use it for OOD detection in other kinds of datasets to ensure that the method is applicable in various domains.

### Questions
How does the method generalize to other types of data e.g. tabular, time-series etc.?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This work studies the problem of OOD detection. It starts by analyzing a recent SOTA method, ASH, where the analysis successfully disentangles the effect of ASH's two building components, namely pruning and scaling. Surprisingly, it is found that while scaling benefits the separation of ID and OOD score, pruning actually adversely hurts it. Based on this analysis, a new post-hoc method named SCALE is proposed. Furthermore, a training-time regularization that echoes the working mechanism of SCALE is also proposed (ISH). Both SCALE and ISH achieves improvements over closely-related and competitive baselines on multiple benchmarks.

### Strengths
1. The written and presentation quality of this manuscript is good. Easy to follow, and the logic is smooth and sound.
2. The analysis of ASH and the insights originate from the analysis are valuable for two reasons. First, ASH indeed leads to superior performance (a recent SOTA), and thus understanding why it works is of course important. Second, the finding that scaling actually benefits OOD detection the most is surprising. In a bigger picture, I think this finding contradicts the common belief that pruning / rectifying is the (only) right direction (this can be evidenced by that many methods, e.g., ReAct, DICE, ASH, adopt such general design idea).
3. The analysis is backed up by both theoretical investigation (Proposition 3.1) and empirical evidences (Table 1 and Figure 2 - 4).
4. The developed method is motivated by the analysis, making it sound and valid.
5. The empirical improvement on OpenOOD ImageNet-1K benchmark is convincing. In the first place, I also like it that the authors consider a unified benchmark for evaluation, which many works failed to do. This will definitely encourage follow-up works to continue making fair and straight comparison, which would benefits the whole OOD detection community.

### Weaknesses
I have two minor comments.

1. For CIFAR experiments, I strongly encourage the authors to refrain from using LSUN-Crop and LSUN-Resize as OOD datasets, if they are directly taken from the ODIN paper. LSUN-Resize has been shown to exhibit obvious resizing artifacts [1], which make the detection trivially easy. LSUN-Crop is 32x32 crops from images with larger resolution, and arguably the resulting samples will have unnaturally different distribution compared to CIFAR's 32x32 natural images, which again makes the evaluation less meaningful.

2. The "Comparison with OOD traning methods." subtitle in Sec. 4.3 has a typo ("traning" -> "training"), and should be placed in the same line as the leading sentence of the next paragraph. There also should be a blank space in "LogitNorm(Wei et al., 2022)". I would suggest a proof-reading to further improve the quality.
 
[1] CSI: Novelty Detection via Contrastive Learning on Distributionally Shifted Instances

### Questions
I was wondering if the analysis provided in this work can also help explain ReAct's effect. Some elaboration or discussion on this can help provide even a more complete picture.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper investigates modern deep learning systems' ability to identify out-of-distribution (OOD) samples. It critically analyzes the extremely simple activation shaping (ASH) method, finding that activation pruning hinders, while activation scaling improves OOD detection. The authors propose two methods: SCALE, a post-training enhancement that boosts OOD detection without affecting in-distribution accuracy, and Intermediate Tensor SHaping (ISH), a training-time method for enhancing OOD detection. These methods show significant performance improvements on the OpenOOD v1.5 ImageNet-1K benchmark.

### Strengths
1. The analysis of ASH looks reasonable.
2. SCLAE and ISH are easy to reproduce and use.
3. It is commendable that similar ideas can be applied simultaneously to post-hoc and training time OOD detection.

### Weaknesses
1. Incorrect Motivation: The author seems to have not conducted sufficient research in the field of OOD detection. Generally, OOD detection requires the model to identify OOD data without affecting the accuracy of ID classification. Hence, there should not be a trade-off between ID classification accuracy and OOD detection performance. Post-hoc OOD detection refers to performing OOD detection through post-processing algorithms without altering the model parameters. Consequently, React, Dice, and ASH  utilize the original classifier for ID classification tasks and a modified classifier for OOD detection tasks, introducing a very minimal computational overhead. Therefore, I believe there is a problem with the motivation presented in the introduction section of the paper.
2. Limited Novelty: SCALE and ISH are incremental works of ASH. Thus, I attribute the commendable performance of ISH and SCALE mainly to the superior performance of ASH. The performance improvement over ASH is quite minimal.
3. Unsubstantiated Claim on React: The author claims that React “hinders the OOD detection process.” However, this analysis is solely theoretical and lacks experimental validation. I think the results from SCALE+React or ISH+React could potentially validate this point.
4. Minimal Performance Gain: As observed from Table 5, the performance improvement brought by combining ISH and SCALE compared to using SCALE alone is extremely minimal. I am curious to know if combining ISH with other OOD detectors (e.g., ISH+MSP/ODIN/Energy/React/ASH) could yield any performance improvement.
5. Lack of Ablation Study: The paper is missing an ablation study related to the placement of SCALE, specifically, how its performance varies when placed after different stages of ResNet50.

### Questions
see Weakness

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
