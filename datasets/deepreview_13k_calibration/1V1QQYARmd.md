# Nearest neighbor-based out-of-distribution detection via label smoothing

- Decision: Reject
- Avg Score: 5.50
- Scores: 8, 5, 6, 3

## Abstract
Detecting out-of-distribution (OOD) examples is critical in many applications. We propose an unsupervised method to detect OOD samples using a $k$-NN density estimate with respect to a classification model's intermediate activations on in-distribution samples. We leverage a recent insight about label smoothing, which we call the {\it Label Smoothed Embedding Hypothesis}, and show that one of the implications is that the $k$-NN density estimator performs better as an OOD detection method both theoretically and empirically when the model is trained with label smoothing. Finally, we show that our proposal outperforms many OOD baselines and we also provide new finite-sample high-probability statistical results for $k$-NN density estimation's ability to detect OOD examples.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a new method for detecting out-of-distribution data. The method primarily relies on the k-NN radius and label smoothing to differentiate between in-distribution and out-of-distribution data. The authors provide both theoretical and experimental evidence to demonstrate the superiority of their method over many other baselines.

### Strengths
1. The application of the k-NN radius to differentiate OOD (Out-Of-Distribution) data seems like a novel idea to me.
2. In the theoretical part, I read the statements and found the results they proved to be reasonable.
3. The authors compare their method with many baselines, and improvements can be observed in most test cases.
4. The paper is clearly written and easy to understand

### Weaknesses
1. It appears that the authors' method underperforms compared to some baselines in certain test cases. Could you provide any explanation as to why this occurs with some datasets?

### Questions
1. In Proposition 1 on page 5, should there be a plus sign before x0 and proj(x) instead of a minus sign? To me, a plus sign seems more indicative of a contraction. Could you please clarify if I am misunderstanding anything?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper's main claim is that combining kNN with label smoothing training can improve OOD detection performance. The paper also proposes the usage of multiple intermediate representations. The paper is mainly theoretical, and experiments on small-scale OOD detection benchamrk datasets.

### Strengths
1. The proposed theory is well presented in rigor with well-defined notations.
2. The main point of the paper is well described.

### Weaknesses
1. The focus of the paper is not clear. The theory is focused on showing the merits of label smoothing training but the method also utilizes multiple latent representations. Is there any theory on the benefit of using multiple latent representations for kNN? Specifically, the paper lacks a clear justification for why averaging k-NN scores across multiple layers should improve OOD detection, beyond the empirical observation that it seems to work. The normalization by the average in-distribution k-NN score is also not theoretically motivated, and it is unclear if this normalization is necessary for the method to work.
2. The experiments have been conducted on only small-scale datasets.  Can this claim hold on the ImageNet-1k scale dataset as well?
3. The sufficient condition of Proposition 1 is not intuitively explained but only technical. Hence, I cannot really determine if this main theoretical result depends on a very strong assumption, in which case the theory can be quite trivial. The paper does not provide a clear explanation of how the Label Smoothed Embedding Hypothesis is related to the regularity conditions required for Proposition 1. It is not clear if the theoretical results are robust to violations of these conditions.

### Questions
1. Could the authors give a very descriptive and intuitive summary of the main theory? For me, the main theoretical point is too obvious since label smoothing makes the network learn 'better' representation [1,2,3], particularly enhancing the intra/inter-class discriminant ratio, thereby possibly improving the separation between ID and OOD in the latent space. Why is the theory not trivial?
2. Please address the above weaknesses.

[1] Xu, Yi, et al. "Towards understanding label smoothing." arXiv preprint arXiv:2006.11653 (2020).
[2] Yuan, Li, et al. "Revisiting knowledge distillation via label smoothing regularization." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2020.
[3] Jung, Yoon Gyo, et al. "Periocular recognition in the wild with generalized label smoothing regularization." IEEE Signal Processing Letters 27 (2020): 1455-1459.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a nearest neighbor-based method for out-of-distribution detection with label smoothing. The paper utilizes the k-NN based density estimation at intermediate layers to identify OOD samples. The proposed method is backed up by theoretical analysis that provides high-probability statistical results. The experiment results show that the proposed method and the proposed method without label smoothing are usually among the best performing methods.

### Strengths
The paper is well organized and clearly written.
The paper finds a good angle that combines k-NN density estimation with label smoothing and provides a theoretical analysis to support it.
The paper clearly states the assumptions for theoretical results.
The experiment results show decent performance compared to several baselines.

### Weaknesses
The comparison is not very convincing, with DeConf performing poorly, SVM and isolation forest being methods that directly build classifiers on the embedding layers, only POEM is a state-of-the-art method that adopts a different approach. It is also not clear why Control has better performance than other baselines since the paper criticizes the softmax so much.

The example in Figure 1 does not make a convincing case. The overlap does not seem too different between the no LS and 0.1 LS case. It would be better if the shrink could be quantified for better understanding.

The paper touches on a "conclusion" that distance is better than label distribution for OOD detection, but there is no further analysis to support this or about whether these two contradict each other.

### Questions
1. How does the method compare with another unsupervised method ([1] Yu, Qing, and Kiyoharu Aizawa. "Unsupervised out-of-distribution detection by maximum classifier discrepancy." Proceedings of the IEEE/CVF international conference on computer vision. 2019.) and a specific layer based method ([2] Sun, Yiyou, Chuan Guo, and Yixuan Li. "React: Out-of-distribution detection with rectified activations." Advances in Neural Information Processing Systems 34 (2021): 144-157.)?

2. Can the difference in Figure 1 be quantified?

3. Can the theoretical results be quantified in experiments, or can some kind of upper bound be calculated that can be compared with the result? I'm asking because Corollary 1 provides an interesting quantity that is the probability of falsely identifying in-distribution examples as out-of-distribution while all OOD are identified.

4.  Is there any more insight on the comparison between distance-based and label-distribution-based approaches?

### Soundness
2 fair

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a statistic based on the KNN density for OOD; when a sample is generated out of the distribution, the statistic tends to be high, and vice versa.

### Strengths
I can't fully assess the strengths of this paper, as the presentation is poor; there is no even a formal formulation of the considered OOD problem, given OOD could be framed differently depending on the applications.

### Weaknesses
This paper is not well-written, hence mainly impeding me to fully understand the proposed method. For example, the drawbacks of using the neural network’s softmax predictions for OOD is mentioned in the third paragraph in the introduction, but the description of that is hard to follow; in addition, it is unclear how the proposed method based on the KNN density can overcome the drawback. The mathematical writing is not rigorous too; for instance, there is no explanation of $\mathbf{X}$ in Def 1. The message that Theorem 1 tries to convey is also hard to follow. Furthermore, the connection between Theorem 1 and Corollary 1 is not clear. The paper claims the proposed paper is unsupervised. Does that mean the users do not have access to the information whether examples in a training set are from in- or out-of-distribution? If that is the case, then how do you compute $\hat{Q}$ that needs to access $\mathbf{X}_{in}$? On the other hand, if the unsupervised OOD implies that labels are not provided, then how do you use label smoothing to train the network?

### Questions
The paper claims the proposed paper is unsupervised. Does that mean the users do not have access to the information whether examples in a training set are from in- or out-of-distribution? If that is the case, then how do you compute $\hat{Q}$ that needs to access $\mathbf{X}_{in}$? On the other hand, if the unsupervised OOD implies that labels are not provided, then how do you use label smoothing to train the network?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair
