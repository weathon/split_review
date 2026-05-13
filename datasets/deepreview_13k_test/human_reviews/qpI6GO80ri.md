# Delving into Temperature Scaling for Adaptive Conformal Prediction

- Decision: Reject
- Scores: 3, 6, 6, 5

## Abstract
Conformal prediction, as an emerging uncertainty qualification technique, constructs prediction sets that are guaranteed to contain the true label with pre-defined probability. Previous works often employ temperature scaling to calibrate the classifier, assuming that confidence calibration can benefit conformal prediction. 
In this work, we empirically show that current confidence calibration methods (e.g., temperature scaling) normally lead to larger prediction sets in adaptive conformal prediction.
Theoretically, we prove that a prediction with higher confidence could result in a smaller prediction set on expectation. Inspired by the analysis, we propose \textbf{Conformal Temperature Scaling} (ConfTS), a variant of temperature scaling that aims to improve the efficiency of adaptive conformal prediction. Specifically, ConfTS optimizes the temperature value by minimizing the gap between the threshold and the non-conformity score of the ground truth for a held-out validation dataset. In this way, the temperature value obtained would lead to an optimal set of high efficiency without violating the marginal coverage property. Extensive experiments demonstrate that our method can effectively enhance adaptive conformal prediction methods in both efficiency and conditional coverage, reducing the average size of APS and RAPS by nearly 50$\%$ on ImageNet at error rate $\alpha=0.1$.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper is well-written and the author has conducted many experiments of ConfTS in CIFAR100 and ImageNet with various architectures. The post-processing  of conformal prediction is also interesting.

### Strengths
The paper is well-written and the author has conducted many experiments of ConfTS in CIFAR100 and ImageNet with various architectures. The post-processing  of conformal prediction is also interesting.

### Weaknesses
. In lines 25-26, the paper claims a nearly 50% reduction in the average size of APS and RAPS on ImageNet at an error rate of $\alpha$ = 0.1. This assertion requires clarification regarding the specific model architectures involved. Does this reduction apply universally across all models, or only to the specific architectures tested in the paper, such as ResNet18 and ViT-B-16?

2. **The experiments seem to be conducted improperly**. In the RAPS paper [1], Appendix E details the method for optimizing set size by choosing $k_{reg}$ and $\lambda$. However, in your paper (Page 16, line 859), these parameters are fixed $k_{reg} = 1$ and $\lambda = 0.001$, potentially inflating  the average set size of RAPS.

3. The experimental setup creates an **unfair baseline**. For instance, in the RAPS paper, the ResNet18's set size at a 0.1 error rate is 4.43 (Table 1 in [1]), while your results show inefficiency of 9.605 (base) and 5.003 (after ConfTS) at error rate 0.1. This indicates that the tuned RAPS results after ConfTS are worse than the baseline reported in [1]. Similar issues appear for other models like ResNet50 and ResNet101, where inefficiencies post-ConfTS remain higher than those reported in RAPS. Please refer to Table 1 in [1] for a comparison.

4. In line 291, you optimize the optimization of $T$ via loss in equation (8). Given that $T$ is a scalar, a grid search on a held-out validation set might be a more efficient strategy. This approach is particularly feasible for small datasets.

5. The paper compares the baseline with ConfTr [5]. Can ConfTr be employed in tuning $T$?

6.  It's essential to consider the rationale of excessive tuning of $T$. APS is designed to assure conditional coverage with an oracle classifier [2] (Section 1.1). Excessive tuning might skew the non-conformity scores of APS and RAPS towards  Least Ambiguous Set-valued Classifier (LAC) [3], potentially compromising the original intention of APS and RAPS.

7. Does tuning $T$ affect the class-stratified coverage gap (CSCG) [6], another vital adaptiveness metric alongside SSCV? Lower values of $T$ might reduce CSCG for RAPS.

8. Have you evaluated the SSCV of ConfTS for RAPS? It’s crucial to determine whether it enhances adaptiveness for more strong baseline.

9. There appears to be an error in the second column of Table 4, where APS and RAPS are listed both in the row and the column. Please correct this for clarity.

References:

[1] Anastasios Nikolas Angelopoulos, Stephen Bates, Michael I. Jordan, and Jitendra Malik. Uncertainty sets for image classifiers using conformal prediction. In 9th International Conference on Learning Representations, ICLR 2021,

[2]Yaniv Romano, Matteo Sesia, and Emmanuel Candes. Classification with valid and adaptive coverage. In Advances in Neural Information Processing Systems, 33:3581–3591, 2020.

[3] Mauricio Sadinle, Jing Lei, and Larry Wasserman. Least ambiguous set-valued classifiers with bounded error levels. Journal of the American Statistical Association, 114(525):223–234, 2019.

[5]David Stutz, Krishnamurthy Dvijotham, Ali Taylan Cemgil, and Arnaud Doucet. Learning optimal conformal classifiers. In The Tenth International Conference on Learning Representations, ICLR 2022.

[6] Tiffany Ding, Anastasios Angelopoulos, Stephen Bates, Michael Jordan, and Ryan J Tibshirani. Classconditional conformal prediction with many classes. Advances in Neural Information Processing Systems, 36, 2024

### Questions
See the above.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a variant of temperature scaling ConTS to enhance adaptive conformal prediction by minimizing the gap between the threshold and the non-conformity score of the ground truth for a held-out validation dataset. Experiments in the paper show that ConfTS can effectively reduce prediction set sizes of APS and RAPS while maintaining marginal coverage. Moreover, it can provide prediction sets with better conditional coverage.

### Strengths
The paper introduces an effective improvement over existing temperature scaling, aiming for efficiency in conformal prediction by minimizing the gap between the threshold and the non-conformity score. A solid theoretical foundation for ConfTS is also provided. 

The paper is well-written and clearly structured.

### Weaknesses
1. Like the author mentioned, ConfTS does not directly address scenarios where distribution shifts occur, such as changes in data distribution over time.

2. While effective in multi-class settings, ConfTS’s performance in binary classification or non-image-based domains is less explored.

### Questions
1. How does ConfTS perform in non-image prediction tasks?

2. Would there be a way to adapt ConfTS to handle distribution shifts effectively, perhaps by dynamic temperature adjustments?

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
The submission explores the limitations of conventional temperature scaling and addresses them using the conformal prediction framework. Specifically, the authors mention that temperature scaling and other post-hoc calibration methods often lead to less efficient prediction sets in adaptive conformal prediction for classification. The authors introduce conformal temperature scaling (ConfTS). The method uses optimization to minimize an “efficiency gap”, which measures the difference between the threshold and the non-conformity score of the true label. The authors claim that ConfTS significantly improves prediction set efficiency.

### Strengths
Based on my knowledge, this is the only work that applied conformal prediction for temperature scaling. Based on the authors’ response, I would be willing to increase the score.

The strength of the submission lies in both theoretical and empirical analysis. The theoretical analysis of the upper bound (Thm. 3.3) is interesting, although there is no indication of how to choose c_1 or \gamma in practice (there is also no empirical confirmation of this thm). The strengths of ConfTS lie in 1) compatibility for many classification models, 2) low compute, 3) does not require hyperparameter tuning, and 3) maintaining coverage guarantees while reducing the size of prediction sets. ConfTS balances prediction confidence, achieving calibration, and efficiency in multiclass settings.

### Weaknesses
A major weakness of this submission is that it solely concentrates on temperature scaling without motivation as to why temperature scaling is a worthwhile problem to tackle compared to other methods.
Another weakness of the submission is the limited real-world examples/case studies.
Another weakness is that some of the claims made in the main results section were not well theoretically/empirically justified (see below).
A weakness of the method lies in the assumption of homogeneity across classes - i.e., assuming that all classes require the same level of adjustment.
A weakness is that the manuscript offers no practical recommendation on transferring Thm. 3.3 into practice - c_1 and \lambda are both arbitrary values, and there is a disconnect between theory and application.

### Questions
Please address the main weaknesses mentioned above:
1. Why was temperature scaling chosen compared to other methods? Readers may benefit from a more comprehensive comparison with alternative calibration techniques (for example: platt scaling, vector scaling, isotonic regression). It is clear from Table 1 that temperature scaling does not perform the best out of the 4 methods. An in-depth discussion of why temperature scaling is better/worse than others and was chosen would significantly enhance the motivation of this paper.
2. When is ConfTS guaranteed to be better than other methods (like different dataset characteristics)? Because there is no guarantee that ConfTS would theoretically be better than existing methods, the submission could benefit from concrete, real-world examples showing how ConfTS would be applied in practical scenarios, including edge cases (settings with numerical instability etc.). Furthermore, there is wide variability on the performance improvements across different models and datasets. A discussion/theoretical analysis of why this could be the case would significantly improve the conviction of the proposed work.
3. What is the justification for using the same temperature scaling value for all classes? This assumption could work well in simpler cases but might not capture the variability needed for more complex or imbalanced datasets. Furthermore, the efficiency could improve as well. This was not sufficiently explored. Some empirical results/discussion about this issue would improve comprehensiveness.
4. How does one use Thm 3.3? How does one pick c_1 and \gamma ?

There are also a few questionable claims. Please comment on the following:
1. Requires no additional computational costs on temperature scaling (page 2): the optimization procedure is a computational cost. This claim may be unwarranted.
2. Improves conformal training (ConfTr): The results show that ConfTS improves ConfTR by <1 most of the time, which is extremely marginal. Please contemplate and discuss whether the average size values are significant, both statistically and in practice.
3. Improves conditional coverage: This claim is unsubstantiated because 1) there is no theoretical motivation or justification for why ConfTS produces better conditional coverage, and 2) this does not hold in all cases (see Fig 2, ViT-B-16). This would, at best, be a discussion item and not a key result.

Other minor comments:
1. t_0 and other variables need to be defined in proposition 3.1
2. Variables need defining in Thm 3.3
3. Why is the related work at the end of the manuscript?

### Soundness
3

### Presentation
2

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
This paper provides a careful study of the connection between conformal prediction and confidence calibration. They found that (i) the use of confidence calibration techniques tends to result in larger prediction sets, obtained by adaptive conformal methods; and (ii) over-confident predictions obtained by choosing a small temperature parameter results in smaller prediction sets. Building on this observation, the authors suggest tuning the temperature parameter to improve the efficiency of sets while achieving the desired coverage. Indeed, numerical experiments underscore the large gain in performance compared to baseline adaptive conformal methods.

### Strengths
1. I found the study on the effect of confidence calibration on conformal prediction set to be valuable.
2. The authors offer a novel cost function, used for temperature tuning, to reduce the size of the prediction sets.
3. The author's goal is to reduce the prediction set size and they show a significant gain in that performance metric.

### Weaknesses
My major concern is that I find it problematic to promote overly confident predictions. To me, it feels that this idea goes against the goal of uncertainty quantification. As a thought experiment, suppose you have access to the oracle classifier, in which you know the true conditional class probabilities. Suppose further that there is uncertainty in the classification, i.e., the conditional class probabilities are not close to a one-hot vector. Now, if we choose to tune the temperature to produce overconfident predictions, we may indeed obtain smaller sets, but this comes at the cost of changing the optimal conditional class probabilities, which does not make much sense. In this case, I expect that the proposed method would yield too small prediction sets that do not reflect the true uncertainty. Am I correct?

If this is the case, it would be great to discuss how the proposed method balances the trade-off between efficiency (smaller prediction sets) and accurately representing uncertainty, especially in cases where there is inherent uncertainty in the true class probabilities. 

Also, I believe the authors should better clarify when one would be interested in using their approach, e.g. perhaps when one assumes that the labels are nearly a deterministic function of the images. It will be great to conduct such a synthetic experiment and analyze what is the effect of the proposed approach on conditional coverage when the oracle classifier is available.

Please don't get me wrong, it's an interesting paper that I enjoyed reading and the results are impressive. But there are crucial points that must be clarified, especially the fact that this paper advises to make overconfident predictions (unless I misunderstood it).

### Questions
Related to the above, I don't understand definition 4.1 and eq. 8: minimizing the distance between the quantile score \tau and all other scores will push all the scores to be very close to each other. This goes against the concept of adaptivity, where one seeks large scores for images that are harder to predict and smaller scores for images that are easier to predict.

It would be great to provide more detailed explanation of how the proposed method maintains adaptivity despite minimizing the distance between scores. This can be done, for example, by building synthetic data that inherently have easy- and hard-to-predict samples.

I don't understand why the proposed method improves conditional coverage (line 414). It would be great if the authors could explain the mechanism by which the proposed method improves conditional coverage. I suspect the authors observed this behavior when using SSCV because the partitioning of the set sizes should not be fixed: the baseline methods have larger set sizes whereas the proposed method has smaller sets so each partition contains an unbalanced number of samples across the methods. Also, it would be good to report the class-conditional coverage.

### Soundness
2

### Presentation
3

### Contribution
2
