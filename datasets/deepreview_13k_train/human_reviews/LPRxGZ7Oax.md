# Complementary Label Learning with Positive Label Guessing and Negative Label Enhancement

- Decision: Accept
- Scores: 6, 5, 5, 5, 5

## Abstract
Complementary label learning (CLL) is a weakly supervised learning paradigm that constructs a multi-class classifier only with complementary labels, specifying classes that the instance does not belong to. We reformulate CLL as an inverse problem that infers the full label information from the output space information. To be specific, we propose to split the inverse problem into two subtasks: positive label guessing (PLG) and negative label enhancement (NLE), collectively called PLNL. Specifically, we use well-designed criteria for evaluating the confidence of the model output, accordingly divide the training instances into three categories: highly-confident, moderately-confident and under-confident. For highly-confident instances, we perform PLG to assign them pseudo labels for supervised training. For moderately-confident and under-confident instances, we perform NLE by enhancing their negative label set with different levels and train them with the augmented negative labels iteratively. In addition, we unify PLG and NLE into a consistent framework, in which we can view all the pseudo-labeling-based methods from the perspective of negative label recovery. We prove that the error rates of both PLG and NLE are upper bounded, and based on that we can construct a classifier consistent with that learned by clean full labels. Extensive experiments demonstrate the superiority of PLNL over the state-of-the-art CLL methods, e.g., on STL-10, we increase the classification accuracy from 34.96% to 55.25%. The code has been submitted to supplementary material.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this paper, the authors address the complementary label learning problem by performing positive label guessing (PLG) and negative label enhancement (NLE). The authors prove the generalization error bound and the error rates bounds. Extensive experiments demonstrate the superiority of the proposed method.

### Strengths
1.	The authors provide theoretical generalization error bound for their proposed method.
2.	The results of the experiments verify the effectiveness of the method.
3.	This paper is well-organized and easy to understand.

### Weaknesses
1.	According to Eq.(21), the upper bound of the PLG error rate ranges from 0 to 1, which is too broad and meaningless. The bound provides no practical insight into the performance of the positive label guessing (PLG) component. Furthermore, it is not easy to estimate the interval of the error bound in Eq.(22). The authors should provide a more precise analysis, ideally demonstrating that the upper bounds for these error rates are small numbers close to zero, or at least provide a method for estimating a tighter bound. The current bounds are too loose to be useful.
2.	Most datasets used in Tables 1 and 2 are relatively easy, it would be better if data set such as 20 Newsgroups is included for comparison. The current datasets do not adequately demonstrate the robustness of the proposed method on more complex, real-world data. The lack of a challenging text dataset is a significant oversight, as the method's applicability to different data modalities is not well established.
3.	Some of the experimental results need further explanation, please refer to the questions below.

### Questions
1.	In Figure 2(b), the PLG precision decreases as the training progresses, while the NLE precision remains relatively stable, please explain this.
2.	Why do you report the method POCR in Table 4?
3.	Please give the detailed derivation of Eq.(30), especially the first inequality.
4.	There are some typos, e.g., in Eq.(32), “B” is missing, in line 134, “show” should be “shown”, in line 169, ”p” should be “f”, in line 216, “are” should be “is”, and in Figures 2(b) and 2(c), “Precison” should be “Precision”.

### Soundness
3

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
4

### Summary
This paper proposes a new Complementary Label Learning (CLL) method called PLNL (Positive Label Guessing and Negative Label Enhancement), which solves the CLL problem by decomposing the inverse problem into two subtasks, positive label guessing (PLG) and negative label enhancement (NLE). Specifically, PLNL classifies training instances into three categories based on the confidence evaluation of the model output: high confidence, medium confidence, and low confidence, and performs PLG and NNE on them respectively. This paper also proposes a unified framework that considers PLG and NLE as the process of negative label recovery, and theoretically proves that the error rates of PLG and NLE have upper bounds, thus enabling the construction of a model consistent with classifiers learned using clean and complete labels.

### Strengths
1.This paper provides a novel solution for the CLL field by transforming the CLL problem into an inverse problem that outputs spatial information and decomposing it into two subtasks, PLG and NLE.
2.This paper also provides a theoretical upper bound proof of error rate, enhancing the credibility and effectiveness of the method.

### Weaknesses
1. The performance of PLNL may be sensitive to parameter selection, such as k-NN parameter k and confidence threshold λ, which requires users to make detailed parameter adjustments when using it.
2.Although PLNL has performed well in experiments, its generalization ability on different datasets and tasks of different complexities still needs further validation.
3.The k-NN computation involved in PLNL may have high computational costs on large-scale datasets, which may limit its application in resource-constrained environments.

### Questions
Please see the weaknesses above.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces PLNL, a new method for complementary label learning that leverages positive label guessing and negative label enhancement based on a confidence-based instances selection module. Through a unified framework and theoretical analysis, it demonstrates the effectiveness of PLNL, achieving state-of-the-art results in CLL.

### Strengths
1. This paper is written clear and easy to understand.

2. This paper proposes a new method PLNL for CLL by PLG and NLE.

3. Extensive experiments demonstrate the effectiveness of PLNL over the SOTA CLL methods.

### Weaknesses
The contribution of this paper is incremental and using a commonly used confidence based instance selection strategy. Moreover,  only one SOTA method (published in 2023 or 2024) is used and it is too weak to validate the effectiveness of the proposed method.

### Questions
1. In the ablation study, it appears that the weak-strong data augmentation strategy is more effective than the proposed confidence-based instance selection strategy.

2. The settings outlined in Table 1 are lacking experimental results for the CIFAR100 dataset.

3.  The number of SOTA methods employed in the experiments is insufficient: only one SOTA method (published in 2023 or 2024) is used, which is inadequate and too weak to validate the effectiveness of the proposed method.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper solved the complementary label learning problem by dividing the training instances into three categories: highly-confident, moderately-confident and under-confident. Then, it performed positive label guessing (PLG) and negative label enhancement (NLE) according to the categories of the instances. In addition, it unified PLG and NLE into a consistent framework. It also studied the bounds of the error rates of both PLG and NLE.

### Strengths
1. The study of generalization error bound is useful for algorithm evaluation.
2. The improvement in empirical study is significant.

### Weaknesses
1. There is no performance reported under biased complementary label learning settings.
2. There is no performance reported under manually annotated datasets, such as CLCIFAR10，CLCIFAR20. In addition, the results on these manually annotated data indicates the performance under instance-depedent CLL.
3. The semi-supervised learning methods used in this paper is not the SoTA ones.
4. There is no deviation reported in Table 3 and Table 4. It is suggested to add standard deviations or confidence intervals for the results, which would help readers better assess the statistical significance and reliability of the reported performance.
5. The study of the separation of moderately-confident and under-confident is not reported in the ablation. It will be helpful for evaluate the idea by comparing the performance when treating these two categories the same versus separately.

### Questions
1. Please consider the point 1 and 2 in the weaknesses.
2. How to evaluate the contribution of the separation of moderately-confident and under-confident instances?
3. Assumption 1 should be reconsidered and carefully checked. It assume that the variety of negative labels is large enough in the KNN instances. However, I think this assumption is too strict.
4. Is there any difference between the supervised and complementary learning losses for the high-confident instances? Maybe there are different from the loss gradient perspective.
5. The negative label set size in eq.(15) is fixed at $\tau_i$. However, when the top-$\tau_i$ and the complementary label is largely overlapped in the multiple complementary label setting, the benefit from the complementary label sharing mechanism is largely weakened.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes to decompose the CLL problem into multi-class classification problems. The one is to infer the positive label by a positive label guessing method, and another is to infer the negative labels by enhancing the negative labels of the moderately-confident and under-confident instances. Besides, this paper provides the upper bounds for the error rate of positive label guessing method and negative label enhancement method, and the effectiveness of the proposal is demonstrated by several experiments.

### Strengths
This paper proposes a new method for CLL, which divides the CLL into two subtasks: PLG and NLE to deal with the high-confident and low-confident instances separately. The authors also verify the effectiveness of the proposal by several experiments and theorems.

### Weaknesses
1. This paper attempts to learn a multi-label classifier from CL. However, the difference between CL and partial labels is not clarified. Initially, Ishida proposed complementary label learning, and noted that complementary label y can be regarded as an extreme case of partial labels given to all K −1 classes other than class y. However, in lines 48 and 121 of this paper, the authors claim that CL can be multiple classes that the instance does not belong to, which seems to fundamentally eliminate the difference between partial label and CL. This conflation of CL with partial labels undermines the motivation for a novel approach, as it is unclear if the problem being addressed is distinct from existing partial label learning scenarios. Specifically, the paper does not address how the proposed method handles the inherent ambiguity in partial labels, which is a core challenge in partial label learning.

2. This paper does not well-motivate the proposed method, so that its advantages over existing methods are not clear. It is also not clear what conditions make the proposed method work or fail. Besides, given the strong relevance of this paper and partial label learning, it is not yet clear what advantages the algorithms in this paper have over existing partial label learning algorithms, either motivationally or experimentally. The paper lacks a clear explanation of why the proposed decomposition into Positive Label Guessing (PLG) and Negative Label Enhancement (NLE) is superior to existing disambiguation strategies in partial label learning. The paper should provide a detailed analysis of the specific scenarios where the proposed method outperforms existing approaches, and conversely, when it might fail.

3. Theorem 2 and Theorem 3 do not give valuable information. For example, the theorem presented in Equation (21) seems to say one thing that a probability value does not exceed 1. Furthermore, the author's discussion of Theorems 2 and 3 is very shallow; they just tell readers that there is an upper bound on the error rate, which is meaningless because any error rate has an upper bound of 1. The theoretical analysis lacks depth and does not provide meaningful insights into the performance of the proposed method. The bounds derived are not tight and do not offer practical guidance on how to improve the algorithm's performance. The paper should provide a more rigorous analysis that demonstrates the practical implications of the theoretical results.

### Questions
1. What is the difference between partial label learning and the problem addressed in this paper?
2. What are the advantages of the proposed algorithm over other existing algorithms (including CLL and partial label learning)?
3. What are the conditions for the proposed algorithm?
4. What do Theorem 2 and Theorem 3 reveal?

### Soundness
3

### Presentation
3

### Contribution
2
