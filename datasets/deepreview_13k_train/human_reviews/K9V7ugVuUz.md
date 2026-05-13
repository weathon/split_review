# Robust Similarity Learning with Difference Alignment Regularization

- Decision: Accept
- Scores: 6, 5, 8, 8

## Abstract
Similarity-based representation learning has shown impressive capabilities in both supervised (e.g., metric learning) and unsupervised (e.g., contrastive learning) scenarios. Existing approaches effectively constrained the representation difference (i.e., the disagreement between the embeddings of two instances) to fit the corresponding (pseudo) similarity supervision. However, most of them can hardly restrict the variation of representation difference, sometimes leading to overfitting results where the clusters are disordered by drastically changed differences. In this paper, we thus propose a novel difference alignment regularization (DAR) to encourage all representation differences between inter-class instances to be as close as possible, so that the learning algorithm can produce consistent differences to distinguish data points from each other. To this end, we construct a new cross-total-variation (CTV) norm to measure the divergence among representation differences, and we convert it into an equivalent stochastic form for easy optimization. Then, we integrate the proposed regularizer into the empirical loss for difference-aligned similarity learning (DASL), shrinking the hypothesis space and alleviating overfitting. Theoretically, we prove that our regularizer tightens the error bound of the traditional similarity learning. Experiments on multi-domain data demonstrate the superiority of DASL over existing approaches in both supervised metric learning and unsupervised contrastive learning tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This work proposed a new unified regularization technique for both supervised and unsupervised similarity learning. The proposed regularization encourages the feature difference between inter-class samples to be similar. It is claimed to help avoid learning ill-posed clustering in the feature space, which is the often case in normal metric learning.

The authors did extensive numerical experiments on many tasks and datasets. The authors also provided experiments to show the sensitivity of the proposed method to hyperparameters. Results showed that the proposed regularization is easy to tune. Numerical results on various tasks and datasets are impressive, surpassing SOTA metric learning methods by clear margins.

### Strengths
+ Interesting idea of constraining the "second-order" feature difference. The intuition of the proposed regularization is natural and the authors provided conceptual experiments to corroborate the point.

+ Impressive umerical results and extensive and informative experiments. I also appreciate the authors efforts for showing the stability of the proposed regularization technique in terms of hyperparameters. This is rare among many deep learning methods, making it much more practical to use in real world.

+ This paper is clearly written.

### Weaknesses
 - The only concern I have is about the theoretical analysis, especialy thm 3 and 4. The two theorems assumed that $x$, $z$, $\hat{x}$ and $\hat{z}$ are from the same distribution. I wonder if the assumption is so strong that makes the result meaningless in real world. The authors are clearly more interested in regularizing the differences of inter-class feature difference. In that case the samples are clearly from different distributions, as the authors assumed in the conceptual experiments in Fig. 2.

I am concerned that the math analysis is only to make the paper more "mathy" and of less practical meaning. I would love to raise the score if the authors could help to clarify or tone down the theoretical analysis. I think this work is good even as a pure empirical one.

### Questions
See the weaknesses part.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper presents a new approach to representation learning by emphasizing higher-order feature distances. It introduces Difference Alignment Regularization (DAR) to maintain consistent representation differences between inter-class instances, addressing the overfitting issue common in traditional methods. A novel cross-total-variation (CTV) norm is proposed to quantify these differences, and is simplified for optimization. DAR is integrated into Difference-Aligned Similarity Learning (DASL), reducing overfitting and enhancing performance. Theoretical and empirical analyses confirm DAR's effectiveness in tightening error bounds and improving performance in various learning tasks.

### Strengths
1.     Approach: The paper learns robust and generalized representation by focusing on reducing the the higher-order feature distances rather than the first-order differences, which is hardly explored before.
2.	Theoretical Justification: The paper not only proposes a new method but also provides theoretical evidence to support its effectiveness.
3.	Empirical Validation: The superiority of the Difference-Aligned Similarity Learning (DASL) method is backed by experiments conducted on multi-domain data (Image retrieval, face recognition, image classification and NLP classification), showing its effectiveness in both supervised metric learning and unsupervised contrastive learning tasks.

### Weaknesses
1.	Inconsistency between theoretical justification and method. Theorem 4 presents a bound on the generalization gap based on max{d'(t; t_hat)}, a metric akin to first-order measurement of feature distance. Despite the notion that smoothness of discrepancy could minimize the largest max{d'(t; t_hat)} by pulling it towards the majority, this mechanism inherently relies on first-order measurement. Consequently, the theorem does not robustly support the paper's primary claim, casting doubts on the reliability of the proposed solution. The bound relies on the maximum distance between the predicted and true feature representations, which is a first-order metric. The paper argues for the importance of higher-order feature distances, yet the theoretical analysis does not directly reflect this. The theorem essentially bounds the worst-case first-order error, while the method aims to control higher-order variations. This disconnect weakens the theoretical support for the proposed approach.

2.	Inconsistency between motivation and method. Figure 2 suggests that a smoother distance between different distributions correlates with better performance. However, this conclusion appears flawed. The generalization in a mixed Gaussian scenario is predominantly governed by the distance of the distributions (a first-order attribute) rather than higher-order terms. For instance, three Gaussians with unit variance located at (0,1), (1, 0), and (1,10000) would exhibit a smaller generalization error compared to them being positioned at (0,1), (1, 0), and (1,1). The implication is that sufficient distance, regardless of higher-order distances, should invariably simplify distinguishability. The example provided highlights that the absolute distance between cluster means is a dominant factor in generalization, not the smoothness of the distance function. The paper's claim that smoother higher-order distances are crucial is not well-supported by this example, which suggests that first-order separation is more critical.

3.	Writing issues. I would suggestion the author revise the introduction, mainly on discuss the motivation and purpose of using higher order feature distance, rather than general discussion on representation learning.

### Questions
Please see above.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose to regularize ERM for similarity learning by enforcing consistency among distances between negative pairs of samples. Forcing the distances between negative pairs to be consistent leads to a more robust representation, and the authors demonstrate this theoretically using a PAC learning style upper bound on the generalization gap.

### Strengths
- Results are quite extensive and impressive.
- I found the method interesting. I like the way it was presented. However, I do have some reservations, as stated in the weaknesses and questions.
- Figures are very easy to understand.

### Weaknesses
 - Regarding the method, could you give some insight as to why it's different from the standard contrastive loss? The standard contrastive loss is: 

$L = ReLu(d^+ - \delta^+) + ReLu(\delta^- - d^-)$

where $d^+$ denotes the distance between positive pairs, $d^-$ denotes the distance between negative pairs, $\delta^+$ denotes the positive margin and $\delta^-$ denotes the native margin. This loss repels features of negative pairs until they are $\delta^-$ away from each-other. In effect, the contrastive loss ensures that all negative pairs are $\delta^-$ away from each-other. This would also satisfy your loss function. Could your loss function be doing something similar to enforcing a negative margin?

- There are some minor issues I saw with the math and the theorems that I don't think are consequential. For example, the notation is quite complicated; I think Algorithm 1 is obvious given the optimization objective in Eq. (8); Theorem 2 seems to trivially follow from the standard GD convergence result; Theorem 4 ignores the tradeoff between generalization and approximation (you say that higher lambda leads to a smaller upper-bound on the generalization gap, but a higher lambda also means $\mathcal{L}(\phi)$ is a bad approximation of what you actually want to minimize.) Obviously, it's not hard to design a loss function that generalizes well if you don't care how well it approximates the actual minimization problem; so I'm not sure how meaningful Theorem 4 is.

### Questions
See above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper addresses similarity-based representation learning, which is important to the machine learning field. In this paper, the authors propose a novel difference alignment regularization (DAR) to encourage all representation differences between inter-class instances to be as close as possible so that the learning algorithm can produce consistent differences to distinguish data points. The proposed method is sound with theoretical proof. The proposed method is extensively verified on various representation learning tasks, including supervised metric learning and unsupervised contrastive learning.

### Strengths
1. This paper addresses similarity-based representation learning, which is of great importance to the machine learning field.
2. The proposed method is sound with theoretical proof.
3. The proposed method is extensively verified on various representation learning tasks, including supervised metric learning and unsupervised contrastive learning.

### Weaknesses
1. Calculating the higher-order difference requires complex calculation complexity. It would be better to report the running time comparison of different methods with some specific dataset to show the effectiveness.
2. There are also other ways to enhance inter-class compactness in the metric learning field, e.g., [1-3]. Please discuss the differences between the current algorithm and these works.
3. It would be better to report the sensitivity with regard to the regularization parameter lambda. Does the change of it heavily influence the final performance? What is the default choice?

### Questions
Please refer to the weakness part.

Overall, this paper tackles the essential problem with a sound method. The proposed method is theoretically proven to have tight bounds, which is also evaluated with extensive experimental results in different metric learning settings. I am positive about this submission; my initial rating is “8”.

[1] Learning multiple local metrics: Global consideration helps. TPAMI 2019

[2] Deep metric learning with angular loss. ICCV 2017

[3] What Makes Objects Similar: A Unified Multi-Metric Learning Approach. TAPMI 2018

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent
