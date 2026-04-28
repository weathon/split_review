# Conformal Prediction for Deep Classifier via Label Ranking

- Decision: Reject
- Avg Score: 6.50
- Scores: 8, 5, 5, 8

## Abstract
Conformal prediction is a statistical framework that generates prediction sets containing ground-truth labels with a desired coverage guarantee. 
The predicted probabilities produced by machine learning models are generally miscalibrated, leading to large prediction sets in conformal prediction.
 To address this issue, we propose a novel algorithm named \textit{Sorted Adaptive Prediction Sets} (SAPS), which discards all the probability values except for the maximum softmax probability. 
The key idea behind SAPS is to minimize the dependence of the non-conformity score on the probability values while retaining the uncertainty information.
In this manner, SAPS can produce compact prediction sets and communicate instance-wise uncertainty. 
Extensive experiments validate that SAPS not only lessens the prediction sets but also broadly enhances the conditional coverage rate of prediction sets.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies conformal prediction as applied to classification problems. It shows that one can significantly reduce the size of the set-valued prediction by removing the miscalibrated probability values in the long tail. This is done by discarding all the probability values except for the maximum softmax probability.

### Strengths
The paper is easy to read. The idea and the solution are both clearly articulated and the results are convincing. There are theoretical justifications.

### Weaknesses
See questions.

1. On page 3, just above (4), it stated "In the APS method (Romano et al., 2019)". However, are you sure it's not Romano et al., 2020?  The 2019 paper was Conformalized quantile regression.

2. Page 13, right above equation (9), it stated "i.e., the calibrated threshold $\tau$, can be obtained by (an equation)". It is not obvious to me how this result was obtained and some clarification is appreciated. Moreover, what is the asterisk (*) at the end of that equation?

### Questions
1. On page 3, just above (4), it stated "In the APS method (Romano et al., 2019)". However, are you sure it's not Romano et al., 2020?  The 2019 paper was Conformalized quantile regression.

2. Page 13, right above equation (9), it stated "i.e., the calibrated threshold $\tau$, can be obtained by (an equation)". It is not obvious to me how this result was obtained and some clarification is appreciated. Moreover, what is the asterisk (*) at the end of that equation?

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
Conformal prediction is a widely used framework, which can outputs a confidence set with statistical guarantee. A crucial aspect of this framework is the choice of non-conformity measure. The authors modify the Adaptive Prediction Set (APS) and propose a novel non-conformity measure called Sorted Adaptive Prediction Set (SAPS). The authors theoretically demonstrate that this non-conformity measure maintains finite-sample marginal coverage and dominates APS in terms of prediction set size in some special cases. Empirically, they show the superiority of the proposed method over APS and RAPS across different datasets

### Strengths
1. The authors propose a novel non-conformity measure in classification problem, and theoretically show it always dominates APS in the size of prediction sets if $\hat{\pi} = \pi$.
2. The authors conduct the experiments on three different datasets. They propose a novel metric ESCV to evaluate the performance of methods.

### Weaknesses
1. The theoretical contribution of this paper seems limited. Proposition 1 represents a common property of any non-conformity measure. Moreover, the condition in Proposition 2, $\hat{\pi} = \pi$, is challenging to satisfy in practice. As for another condition  $\lambda \geq 1 - \frac{1}{K}$, note that $\lambda$ used in experiments is searched in the range of 0.001 to 0.5, which conflicts with this condition. Figure 4a shows that when $\lambda$ exceeds 0.2, the set size increases with $\lambda$. It is important to address these concerns.
2. In Equation (8), it is unclear why the authors use 2 instead of another constant in $o(y,\hat{\pi}(x)) - 2 + u$. The authors should provide a motivation and explanation for this choice.
3. The authors only provide theoretical analysis comparing APS and SAPS, and empirical comparisons between RAPS and SAPS. It is necessary to include a detailed comparison with RAPS theoretically, since it is also a modified version of APS.

### Questions
Please see the Weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Using all softmax probabilities in the non-conformity score may yield larger prediction sets. Out of this consideration, the authors proposed a method called sorted adaptive prediction sets (SAPS), which discards all the probability values except the maximum softmax probability.

### Strengths
* The authors empirically showed that using all probabilities is not necessary in APS.
* The authors empirically showed that, under different network architectures, the proposed method returns more efficient prediction sets compared to APS and RAPS on three datasets.

### Weaknesses
 * I have a reservation about the claimed contribution of higher adaption, i.e., the adaption is not that convincing: For the example of Figure 3(b), now that both SAPS and RAPS achieve the same coverage, why should we require a larger prediction set for difficult observations? In general, the smaller the better. RAPS gives more efficient predictions on those observations with higher difficulty, while the proposed SAPS only gives efficient predictions on a shorter interval of difficulty.

* Even though the proposed method has a promising performance compared to several methods, how is the proposed method far away from the ground truth? Specifically, what is the performance gap between SAPS and an ideal conformal predictor using the true underlying data distribution, and how does this gap vary with different levels of data difficulty?

* To make it clearly catch the whole scope, it would be better to explicitly outline the calibration and prediction under the frame of a pseudo-algorithm as the one in RAPS. For example, I believe "We choose the hyper-parameter that achieves the smallest set size on a validation set" fails to disclose the entire picture because the smallest set size on a validation set cannot secure the desired coverage. How did the authors handle this issue? It's crucial to detail how the hyperparameter selection interacts with the coverage guarantee, especially since the method's validity hinges on this.

* The proofs are not friendly reading (see the section on questions).

* Minor issues:
  * Do you mean $\mathcal{C}(\boldsymbol x_i, y_i, u_i)$ for the definition of coverage rate?
  * Double-check all the usage of "i.e.,"
  * 0.05 instead of 0.5 in Section 4.2.
  * In the proof of Lemma 1, did you intend to assume $p_{(k)}\geq \frac{1}{k}$? Where will be $\tilde{k}$ used in the proof?

### Questions
* Is (2) generally correct? In other words, are the prediction results always nested? Particularly in Theorem 2, Since there is a random variable $u$ introduced, why $\mathcal{C}_{1-\alpha}(\boldsymbol{x}, u)$ have the nesting property? 
* Proposition 1: How is $\mathcal{C}_{1-\alpha}(\boldsymbol x, u)$ defined as in Eq. 3? They have totally different notations.
* I didn’t get the point of the proof for Proposition 1. What is the difference between your proof of proposition 1 and Theorem 2? The conclusion of coverage is for the popped $\mathcal{C}(\boldsymbol x_{n+1},u_{n+1})$ but there is no $\mathcal{C}(\boldsymbol x_{n+1},u_{n+1})$ during your proof. I think the authors need to well-articulate the proof.
* Why $\frac{1}{\lambda}\leq1-\frac{1}{K}$ but previously you require $\lambda>1-\frac{1}{K}$?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper mainly proposes a new nonconformity score for classification task. It first identifies that the probability in APS is not that important and the rank instead is important - a rank-based version of the APS nonconformity score makes more efficient prediction sets, the size of which is also more correlated with accuracy. Then, it proposes a new nonconformity score that only keeps the top predicted probability but uses ranks for the remaining classes, and shows in the experiments that such score typically improves efficiency.

### Strengths
This is a well-motivated paper that is very easy to follow. The observation that ranking matters more than the predicted probability (or softmax output) is very interesting (and I'm surprised that it has not been discovered before). The proposed solution also makes sense. Proposition 2 about dominance is a good theoretical result on top of the finite-sample coverage.

### Weaknesses
This requires choosing a hyperparameter $\lambda$, which requires additional data and could affect efficiency in practice.

### Questions
In the experiments, choosing $\lambda$ for SAPS uses a subset of the calibration set. Do all baselines uses the (same) remaining calibration set? That is, is SAPS calibrated on a smaller set due to $\lambda$?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
