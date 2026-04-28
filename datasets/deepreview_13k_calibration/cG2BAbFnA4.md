# Learning with Complementary Labels Revisited: A Consistent Approach via Negative-Unlabeled Learning

- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 6, 3, 6

## Abstract
Complementary-label learning is a weakly supervised learning problem in which each training example is associated with one or multiple complementary labels indicating the classes to which it does not belong. Existing consistent approaches have relied on the uniform distribution assumption to model the generation of complementary labels, or on an ordinary-label training set to estimate the transition matrix. However, both conditions may not be satisfied in real-world scenarios. In this paper, we propose a novel complementary-label learning approach that does not rely on these conditions. We find that complementary-label learning can be expressed as a set of negative-unlabeled binary classification problems when using the one-versus-rest strategy. This observation allows us to propose a risk-consistent approach with theoretical guarantees. Furthermore, we introduce a risk correction approach to address overfitting problems when using complex models. We also prove the statistical consistency and convergence rate of the corrected risk estimator. Extensive experimental results on both synthetic and real-world benchmark datasets validate the superiority of our proposed approach over state-of-the-art methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper points out that the existing complementary-label learning approaches have relied on some assumptions about the distribution of complementary labels, or on an ordinary-label training set, which may not be satisfied in real-world scenarios. It then proposes a risk-consistent approach that express complementary-label learning as a set of negative-unlabeled binary classification problems, using the one-versus-rest strategy. Furthermore, it introduce a risk correction approach to address overfitting problems when using complex models. It also proves the statistical consistency and convergence rate of the corrected risk estimator.

### Strengths
1. The idea of expressing complementary-label learning as a set of negative-unlabeled binary classification problems is very novel and sensible.
2. The proposed approach doesn’t rely on assumptions about the distribution of complementary labels or ordinary-label training set, which makes it more suitable for real-world scenarios.
3. The result is promising.

### Weaknesses
1. The major novelty lies in the problem reformulation. The way to conduct theoretical analysis and risk correction is off-the-shelf. In this sense, the technical contribution is not very impressive.
2. In Fig2, only the impact of inaccurate class priors over the proposed method is illustrated. How about the competitors?
3. Some recent PU-learning methods should be reviewed in Sec.2.2, e.g.,
[1] Beyond Myopia: Learning from Positive and Unlabeled Data through Holistic Predictive Trends. NeurIPS 2023.

[2] Positive-Unlabeled Learning With Label Distribution Alignment. TPAMI 2023.

[3] GradPU: Positive-Unlabeled Learning via Gradient Penalty and Positive Upweighting. AAAI 2023.

[4] Dist-PU: Positive-Unlabeled Learning From a Label Distribution Perspective. CVPR 2022.

### Questions
A brief introduction for the compared methods to explain their respective characteristics will help understanding.

### Soundness
3 good

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
This paper tackles complementary label learning by regarding the problem as multiple negative-unlabeled learning problems. This novel formulation avoids explicit assumptions on the label distribution relationship between complementary and ground-truth labels, and is risk-consistent with theoretical guarantees: A risk-consistent estimator. Empirical results validate promising performance of the proposed approach.

### Strengths
1. Solid justifications on the statistical consistency and convergence rate of the corrected risk estimator have been provided with proofs.
2. Method that avoiding the assumptions on the transition matrix is a substantial contribution to the CLL community.

### Weaknesses
1. More experiments with instance-dependent CL data should be investigated, due to the practical reason mentioned in this paper.
2. The performance of prior estimation should be evaluated in the empirical study.
3. I notice some results of existing methods are much worse than the results reported in their original papers. For example, the results of NN and GA on K-MINST and F-MNIST in paper [1] are much higher than that are reported in your paper.
4. Have you tried FORWARD [2] on CLCIFAR datasets? I notice that the results of FORWAD is pretty good on these instance-dependent CL datasets and should be involved in the comparison.

### Questions
1. I notice some results of existing methods are much worse than the results reported in their original papers. For example, the results of NN and GA on K-MINST and F-MNIST in paper [1] are much higher than that are reported in your paper.
2. Have you tried FORWARD [2] on CLCIFAR datasets? I notice that the results of FORWAD is pretty good on these instance-dependent CL datasets and should be involved in the comparison.

Refs.\
[1] Chou Y T, Niu G, Lin H T, et al. Unbiased risk estimators can mislead: A case study of learning with complementary labels[C]//International Conference on Machine Learning. PMLR, 2020: 1929-1938.\
[2] Xiyu Yu, Tongliang Liu, Mingming Gong, and Dacheng Tao. Learning with biased complementary labels. In Proceedings of the 15th European Conference on Computer Vision, pp. 68–83, 2018.

### Soundness
4 excellent

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
This manuscript utilized the OVR strategy to decompose the complementary-label learning into a set of negative-unlabeled classification problems.

### Strengths
This manuscript utilized the OVR strategy to decompose the complementary-label learning into a set of negative-unlabeled classification problems.

### Weaknesses
1. ``Existing consistent approaches have relied on the uniform distribution assumption to model the generation of complementary labels, or on an ordinary-label training set to estimate the transition matrix. '' This argument is false because some cll algorithms are designed for both uniform and non-uniform distribution.

2. The methodologies compared in this research are outdated, if not obsolete. I'm afraid that most cutting-edge techniques are missing.

3. Lack of comparison. Because cll is a subset of pll, the methods comparison should include the most recent pll methods.

4. The loss proposed for complementary label learning is uncear.

5. The experiments are conducted on simple datasets, some complex dataset like cifar100, subset of webvision should be used to verify the effectness of the proposed method.

### Questions
1. Is this strategy of this paper is similar to a previous work of Ishida2017[1].

[1] Takashi Ishida, Gang Niu, Weihua Hu, and Masashi Sugiyama. Learning from complementary
labels. In Advances in Neural Information Processing Systems 30, pp. 5644–5654, 2017.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper addresses complementary-label learning, which is a weakly supervised learning problem. The proposed method does not rely on the uniform distribution assumption nor on the ordinary-label training set. More importantly, this method is risk-consistent with theoretical guarantees. Experiments on both synthetic and real-world benchmark datasets validate the effectiveness of the proposed approach.

### Strengths
1. The proposed method does not rely on the uniform distribution assumption nor an ordinary-label training set, which is more realistic.
2. The proposed method is risk-consistent with solid theoretical guarantees.
3. The introduction part is well-written and easy to follow.

### Weaknesses
1. The notations are confused, e.g., $\overline{Y}$ is a set of label vectors composed of {0,1}, and $k$ denotes the number of classes in {1,2, ..., q}, however, on page 4, line 5, the authors claim that "$k\in\overline{Y} $". The notations should be carefully checked and standardized. Specifically, the use of $\overline{Y}$ to represent both a set of labels and a set of label vectors is ambiguous. It's crucial to distinguish between the set of possible complementary labels and the specific vector representation of those labels for a given instance. The statement $k \in \overline{Y}$ is mathematically incorrect given the definitions provided.
2. Although the experimental results of the proposed method in the paper are better than the compared methods, there is a lack of experimental analysis provided. A thorough analysis of the experimental results would be helpful in understanding the factors contributing to the superior performance. For example, it would be beneficial to analyze the performance of the proposed method under different noise levels in the complementary labels or with varying dataset sizes. A more detailed breakdown of the results on different classes would also be insightful.
3. Although this paper provides nice theoretical results, it does not explain why the proposed method performs well. Which part plays an important role, the one-versus-rest (OVR) strategy, the risk correction function, or any other techniques? It is unclear how each component of the proposed method contributes to the overall performance. A more detailed ablation study would be necessary to understand the influence of each part.
4. The details of the constant $c_k$ in assumption 1 are missed. How to decide this constant? Will the choice of this constant affect the performance? The paper does not provide any guidance on how to choose this constant in practice. A discussion on the sensitivity of the method to this constant is needed.

### Questions
1. Why set the label $\bar{y}$ as a q-dimensional vector? Intuitively, adding more complementary labels would improve the performance.
2. The assumptions in Theorem 2 directly borrow from Theorem 10 of [1]. According to these assumptions, which functions can be used as the loss function $l$? Can you list some of these and write the explicit form of $l$ that can be used in practice?
3. The compared method GA[2] also adopts a risk correction approach, can you explain why your CONU outperforms GA?

[1] Tong Zhang. Statistical analysis of some multi-category large margin classification methods. JMLR, 2004.

[2] Takashi Ishida, Gang Niu, Aditya K. Menon, and Masashi Sugiyama. Complementary-label learning for arbitrary losses and models. ICML 2019.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
