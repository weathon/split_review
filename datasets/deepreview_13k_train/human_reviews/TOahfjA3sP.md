# Noise Separation guided Candidate Label Reconstruction for Noisy Partial Label Learning

- Decision: Accept
- Scores: 6, 6, 6, 5, 6

## Abstract
Partial label learning is a weakly supervised learning problem in which an instance is annotated with a set of candidate labels, among which only one is the correct label. However, in practice the correct label is not always in the candidate label set, leading to the noisy partial label learning (NPLL) problem. In this paper, we theoretically prove that the generalization error of the classifier constructed under NPLL paradigm is bounded by the noise rate and the average length of the candidate label set. Motivated by the theoretical guide, we propose a novel NPLL framework that can separate the noisy samples from the normal samples to reduce the noise rate and reconstruct the shorter candidate label sets for both of them. Extensive experiments on multiple benchmark datasets confirm the efficacy of the proposed method in addressing NPLL. For example, on CIFAR100 dataset with severe noise, our method improves the classification accuracy of the state-of-the-art one by 11.57%. The code has been submitted to the supplementary material.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies the noisy partial label learning (NPLL) problem, where the correct label is not always in the candidate label set (CLS). This setting is more practice in real world. To address this problem, firstly, the authors theoretically prove the generalization error bound of the classifier constructed under NPLL paradigm and reveal that the error bound depends on the noise rate and the average length of the candidate label set. Secondly, the authors propose a method to reduce the noise rate and reconstruct shorter candidate label sets. Finally, experiments on benchmark datasets are conducted to confirm the efficacy of the proposed method in addressing NPLL.

### Strengths
1.	This paper provides a theoretical generalization analysis of the NPLL, highlighting the noise rate and the length of the candidate label sets are two key factors, which is insightful.
2.	The proposed method is grounded in theoretical findings, making it reasonable and intuitive.
3.	Extensive experiments have been conducted and the reported results verify the effectiveness of the proposed method.

### Weaknesses
1.	Since the whole label space is very large, then the size of non-CLS may also be very large, which will bring challenges to find the ground truth label. Specifically, the method relies on identifying discrepancies between CLS-based and KNN-based pseudo-labels, but with a large non-CLS, the probability of a noisy sample having a high KNN-based pseudo-label within the non-CLS increases, potentially misleading the noise detection mechanism. This issue is particularly relevant when the true label is far from the candidate set in the feature space, making the KNN-based pseudo-label unreliable.
2.	Some parts of this paper is unclear, see the questions below for details. For example, the exact mechanism by which the ECK metric effectively distinguishes noisy samples needs more rigorous justification. The paper claims that a larger ECK value indicates a noisy sample, but the theoretical basis for this claim is not fully established. Furthermore, the sensitivity of ECK to different noise levels and dataset characteristics is not explored.
3.	Sensitivity analyses of the hyperparameters are absent. The method introduces several hyperparameters, such as the warm-up epoch, the rate of percentile change, the trade-off parameter for CLS reconstruction, and the KNN parameter. The impact of these parameters on the final performance is not clear, and the paper lacks a systematic analysis to determine the optimal values and their robustness across different datasets and noise conditions. This absence makes it difficult to reproduce the results and assess the practical applicability of the proposed method.

### Questions
1.	According to Eq.(2), do you need to know the CLS of the normal samples in prior?
2.	Since the computation of Eq.(3) relies on the KNN-based pseudo-label, how to decide the parameter of K when applying KNN?
3.	In lines 192-195, the authors claim that “when the ground-truth label of a sample locates at the non-candidate labels, there will be a significant discrepancy between the CLS-based pseudo-label and KNN-based pseudo-label, leading to a larger value of ECK”, could you provide some experimental results to support this?
4.	In lines 272-274, the authors claim that “add the label with the highest pseudo-label probability from the non-CLS to the CLS, and remove the label with the lowest pseudo-label probability from the CLS”, this operation may destroy the diversity of CLS. Is it beneficial to the performance? And please explain Eq.(10).
5.	Please give the detailed derivation of second inequality of Eq.(18).
6.	In lines 648-654, there are two repeated references.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses the problem of noisy partial label learning (NPLL), where the true label may not be included in the candidate label set (CLS). The authors provide a generalization bound on the empirical risk and, based on this, propose an NPLL method that progressively separates samples and reconstructs the CLS, reducing the noise rate while shrinking the CLS size. Experiments are conducted on both synthetic and real-world noisy datasets.

### Strengths
1. Building on the generalization error bound, the authors propose a method of progressive sample separation and CLS reconstruction, which reduces the noise rate while simultaneously shrinking the CLS size.
2. The performance of the proposed method is promising in the experiments.
3. The writing is very clear and easy to understand.

### Weaknesses
1. Theoretical part.
   * "$f_y(x)$" (Line 125) is not defined in the paper. I assume this represents the predicted probability of the $y$-th class for $x$, following the notation in Xie et al. (2023), as cited by the authors in Appendix 1?
   * The authors state, "Theorem 1 shows that the empirical risk minimizer $\hat{f}$ converges to the true risk minimizer $f^*$ as $n \rightarrow \infty$, $\epsilon \rightarrow 0$, and $\alpha \rightarrow 1" (Line 138). However, even under these conditions, the Rademacher complexity will not necessarily converge to zero, which implies that $R(\hat{f})$ does not necessarily converge to $R(f^*)$. Furthermore, even if $R(\hat{f})$ does converge to $R(f^*)$, this does not guarantee that the minimizer $\hat{f}$ itself converges to $f^*$. The statement about convergence is not precise and needs further clarification. The conditions under which the empirical risk minimizer converges to the true risk minimizer are not fully established.
2. Proposed Method and Experimental Part
   * Could you clarify the rationale behind the statement, "When the ground-truth label of a sample is included in the candidate labels, the CLS-based pseudo-labels and KNN-based pseudo-labels tend to be similar... however, when the ground-truth label of a sample is in the non-candidate labels, there will be a significant discrepancy between the CLS-based pseudo-label and KNN-based pseudo-label" (Lines 190-195)? The intuition behind this claim is not immediately clear and requires more detailed explanation. Specifically, how does the model's training state influence the similarity of pseudo-labels, and what specific properties of the KNN-based pseudo-labels cause them to be more reliable when the ground truth is outside the candidate set?
   * In constructing the KNN-based pseudo-label and CLS-based pseudo-label for $x_i$, model probability prediction vectors and features are used. How does the warm-up stage affect this process? What if the warm up stage that relies on noisy labels is not good enough to produce meaningful features, especially when the noise ratio is high? The paper should provide a more detailed analysis of the warm-up phase and its impact on feature quality, particularly under high noise conditions. It is not clear how the method ensures that the warm-up phase does not introduce biases that propagate through the rest of the training process.

### Questions
See above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors provide the generalization error bound of the classifier constructed under NPLL, which depends on the noise rate and the mean size of candidate label sets for normal samples. Empirically, they propose a novel NPLL method which includes two components: progressive sample separation and CLS reconstruction. Their method can serve as a plug-in for existing PLL methods to enhance their performance on NPLL datasets.

### Strengths
1. From generalization error bounds in NPLL problem, they find that the lower noise rate and smaller candidate label are two key
factors to solve the NPLL problem.

2. By iterative learning, their method can effectively reduce the noise rate while simultaneously decreasing the size of CLS.

3. Extensive experimental results validate that our method outperforms the current state-of-the-art (SOTA) methods by a large margin

### Weaknesses
The authors did not compare with the recent work (Lv et al., 2024).


### Questions
1. Can we use the prediction from the network $p_j$ instead of the KNN-based $q_j$ in Equ. (6)? Are there any difference in performance? In other words, can you empirically show that the KNN-based pseudo-label is better than probability prediction vector from the network?
2. Can you compare the performance with (Lv et al., 2024)?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper addresses the problem of Noisy Partial Label Learning (NPLL), a challenging subset of weakly supervised learning where instances are annotated with a set of candidate labels, only one of which is correct. The authors theoretically demonstrate that the generalization error of a classifier constructed under the NPLL paradigm is constrained by the noise rate and the average length of the candidate label set. Building on this theoretical foundation, they propose a novel NPLL framework designed to distinguish noisy samples from normal ones, thereby reducing the noise rate and reconstructing shorter candidate label sets for both categories.

### Strengths
1. The paper presents a groundbreaking contribution to the field of weakly supervised learning, specifically addressing the Noisy Partial Label Learning (NPLL) problem. The authors’ novel approach to bounding the generalization error of classifiers under NPLL is a significant theoretical advancement. The proposed method, which integrates progressive sample separation and CLS reconstruction, demonstrates a clear and innovative approach to solving NPLL. This originality in problem formulation and theoretical analysis is commendable.
2. The article's structure is well-organized and easy to comprehend.
3. The experiments are generally comprehensive.
4. Theoretical analysis contributes to establishing the effectiveness of the proposed model.

### Weaknesses
1.The computational efficiency of the proposed model is a concern.  The requirement to train the classifier on the entire dataset at every epoch introduces a high time complexity, which may limit the practical applicability of the method, especially for large datasets.

2.The computational efficiency of the proposed model is a concern.  The requirement to train the classifier on the entire dataset at every epoch introduces a high time complexity, which may limit the practical applicability of the method, especially for large datasets.

3.When there are many noisy samples, for the calculation of KNN, if the neighboring samples are also noisy, is this method reliable?

### Questions
Could the authors provide a more detailed explanation or theoretical justification for the assumption that reliable samples become increasingly reliable, while unreliable samples become increasingly unreliable as training progresses?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper introduces a new framework for noisy partial label learning (NPLL) that combines progressive sample separation and candidate label reconstruction to reduce noise rates and improve classification accuracy, achieving a good  performance enhancement on the CIFAR10 dataset compared to state-of-the-art methods.

### Strengths
1. This paper is clearly written and easy to understand.

2. The paper provides the generalization error bound for the classifier constructed under NPLL.

3. Extensive experimental results demonstrate that our method significantly outperforms the current state-of-the-art (SOTA) methods.

### Weaknesses
 1. For ablation study,  $v_2$ seems ineffective in separating normal samples and noisy samples in CIFAR10.

2. For Eq.(3), the author calculates the ECK of each sample $x_i$ by CE and uses $\widetilde q$ as target. What about using a KNN-based pseudo-label as the target instead?

3. The sentence below Eq.(10), $c^\prime$ can be  $c^\prime = \mathrm{arg min}_{j \in Y_i}$ instead of   arg max

4. The datasets adopt in the experiment are few and small. It would be more effective to utilize larger datasets to further validate the effectiveness of the proposed method.

### Questions
Please refer to the weakness

### Soundness
3

### Presentation
3

### Contribution
3
