# Class Probability Matching with Calibrated Networks for Label Shift Adaption

- Decision: Accept
- Avg Score: 7.25
- Scores: 5, 8, 8, 8

## Abstract
We consider the domain adaptation problem in the context of label shift, where the label distributions  between source and target domain differ, but the conditional distributions of features given the label are the same. To solve the label shift adaption problem, we develop a novel matching framework named \textit{class probability matching} (\textit{CPM}). It is inspired by a new understanding of the source domain's class probability, as well as a specific relationship between class probability ratios and feature probability ratios between the source and target domains. CPM is able to maintain the same theoretical guarantee with the existing feature probability matching framework, while significantly improving the computational efficiency due to directly matching the probabilities of the label variable. Within the CPM framework, we propose an algorithm named \textit{class probability matching with calibrated networks} (\textit{CPMCN}) for target domain classification. From the theoretical perspective, we establish the generalization bound of the CPMCN method in order to explain the benefits of introducing calibrated networks. From the experimental perspective, real data comparisons show that CPMCN outperforms existing matching-based and EM-based algorithms.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a solution for the label shift adaptation problem: a matching framework called "Class Probability Matching" (CPM). CPM offers the same theoretical guarantees as the previous framework (feature probability matching framework) and addresses the issue of its low computational efficiency. Inspired by the CPM framework, the authors further develop the CPMCN algorithm, utilizing calibrated neural networks for classification in the target domain, and demonstrate the benefits of calibrated neural networks from the theoretical perspective. In experiments, CPMCN outperforms other matching methods as well as EM-based algorithms.

### Strengths
1. Paper is well written and easy to follow;
2. The authors compare, analyze, and make improvements to existing frameworks, and these improvements are well-founded; 
3. The proposed method is simple but effective.

### Weaknesses
1. The authors emphasize that the proposed algorithm has made significant improvements in terms of computational efficiency, reducing the computational complexity from O(n_p^3) to O(n_qK^2)  . However, no related experimental evidence has been provided to support this
claim;
2. While this paper is the first to estimate marginal probability ratios from a class probabilistic perspective, such methods have already been explored extensively in the long-tailed domain, especially in approaches like logit adjustment, as seen in prior works such as the one in [1]. I
believe it is essential for the authors to conduct some research and comparisons in this regard;
3. Previous studies [2] have already demonstrated that calibration can indeed enhance performance, so the calibrated network mentioned in the paper is not very novel.

### Questions
1. Could the authors provide a brief explanation of the calibrated network mentioned in the paper?
2. Why do the experiments in the 'Performance on MNIST under the tweak-one shift' have so many identical results? Even the standard deviation is the same for the accuracy metric at  \ro=0.02.

### Soundness
3 good

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents a method which addresses the label shift problem. For dealing with label shift, it rewrites the target class probability as a tractable function with unknown parameters, averaged over the target feature distribution. The parameters are optimized by the BFGS algorithm and serve as weights to construct prediction scores on a target domain. The important condition is that the underlying classifier should be calibrated.

### Strengths
While the idea somewhat resembles the probability matching framework, it considers the problem from a different angle of matching class probabilities. The paper is well written and easy to follow. It contains necessary theoretical grounding and experiments which show method’s superiority over the baselines. The method has an advantage in terms of the runtime complexity, and demonstrates better accuracy results.

### Weaknesses
1. While the computational complexity is considered as one of the main advantages of the method, the paper is missing some experimental studies on the runtime. At what point (target domain size) the method becomes computationally prohibitive? How does that compare empirically with the other methods?
2. A minor comment on writing: introducing “Calibrated networks” as a part of the method might suggest that there is some novelty in designing a proper mechanism of calibration for the label shift scenario. In fact, calibrated networks are used off the shelf as a necessary ingredient of the method to improve the estimation of p(y|x).

### Questions
The method currently doesn’t allow for a minibatch training; I’m wondering whether the authors thought about adapting the algorithm to handle minibatching?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper studies the domain adaptation problem under label shift, assuming that the domains' label priors differ while the class-conditional probabilities are the same. Existing algorithms are based on feature probability matching, where the class-conditional probability can be difficult to estimate e.g. using GAN. To cope with this problem, the authors propose a novel matching algorithm based on class probability matching. They proved that the estimated class probability ratio is consistent with previous algorithms and the estimation process enjoys wonderful theoretical guarantees. Experimentally, they show the proposed method achieves better performance than existing algorithms.

### Strengths
1. This paper is well-written and easy to follow.

2. The theoretical analysis is thorough and helpful.

3. The experimental results clearly verified the effectiveness and efficiency. 

Overall, I believe this is a solid paper and should be accepted.

### Weaknesses
1. While I vote for clear acceptance, I think the studied problem is not very significant since they simply consider the label shift problem. Notably, this problem can be regarded as an imbalanced semi-supervised learning problem where the labeled set and the unlabeled set have different classes prior. There have been many empirically strong works that study the imbalanced semi-supervised learning problem [1-4] and I suggest the authors discuss these papers properly. The core issue is that the paper focuses on a specific instance of domain adaptation (label shift) that can be reframed as a well-studied imbalanced semi-supervised learning problem, which may limit the novelty and impact of the proposed method.

2. Can the proposed method be equipped with existing imbalanced semi-supervised learning algorithms for improved performance? It won't affect my decision, but I would appreciate it if the authors could provide further extensions, which I believe will enhance the empirical significance of this paper. Specifically, it's unclear how the proposed class probability matching approach could be integrated with techniques like re-weighting, re-sampling, or pseudo-labeling strategies commonly used in imbalanced semi-supervised learning. The paper would benefit from a discussion on the potential synergies and challenges of such integration.

3. In Eq (11), the authors directly optimize the class prob ratio by searching the $R^K$ space and finally perform normalization. Can we directly obtain the class prob ratio by constraining it in the normalized space $\sum \hat{w}_k = 1$? This raises a concern about the optimization process. Constraining the search space directly to the simplex could potentially lead to more efficient and stable optimization. The current approach of optimizing in an unconstrained space followed by normalization might introduce unnecessary computational overhead or numerical instability.

4. There are some typos, e.g. there is an unexpected bracket on page 13 line 4, 'p(k))'.

### Questions
Is the network fixed and will not be fine-tuned on the target domain?

BTW, I accidentally clicked the check box of 'First Time Reviewer' while I've been an experienced reviewer in the ICLR community.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a novel method for domain adaptation in the context of label shift, where label distributions between the source and target domains differ while the conditional feature-label distribution remains the same. The proposed approach, called "class probability matching" (CPM), aims to match class probabilities and significantly improves computational efficiency compared to existing methods. Within the CPM framework, they introduce "class probability matching with calibrated networks" (CPMCN) for target domain classification, supported by a theoretical generalization bound.

### Strengths
1. This paper proposes a novel class probability matching method, which is computationally more efficient compared with existing feature distribution matching methods.

2. Theoretical analysis of the generalization bound is obtained for the proposed approach. 

3. The algorithm is simple, and the empirical results demonstrate superior performance of CPMCN over existing approaches.

### Weaknesses
The theoretical analysis is not intuitive. Maybe some proof sketches in the paper can help the readers understand the results.  For example, why assumption 5.1 is required and what does it mean.

The core of class probability matching is to derive that solving problem (11) can obtain an estimator of class probability ratio w*, which is utilized to transform the source domain classifier to the target domain classifier. However, the authors do not provide any analysis of the problem (1). Can its optimal solution be obtained by existing algorithms, e.g., BFGS. If the approximate solution is attained, how the approximation influences the generalization bound. 

In figure 1, the curves of other compared matching approaches are expected to be shown.

Please verify that the proposed approach is computational more efficient than compared matching approaches quantitatively in the experimental studies.

### Questions
1.	The core of class probability matching is to derive that solving problem (11) can obtain an estimator of class probability ratio w*, which is utilized to transform the source domain classifier to the target domain classifier. However, the authors do not provide any analysis of the problem (1). Can its optimal solution be obtained by existing algorithms, e.g., BFGS. If the approximate solution is attained, how the approximation influences the generalization bound. 
2.	In figure 1, the curves of other compared matching approaches are expected to be shown. 
3.	Please verify that the proposed approach is computational more efficient than compared matching approaches quantitatively in the experimental studies.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
