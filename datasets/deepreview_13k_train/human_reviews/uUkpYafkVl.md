# Conformal Prediction for Deep Classifier via Truncating

- Decision: Reject
- Scores: 5, 3, 6, 5

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
5

### Rating Number
5

### Confidence
4

### Summary
The authors empirically demonstrate that existing conformal prediction methodologies in classification problems lead to unnecessary inefficiency by including redundant labels, resulting in large prediction sets. To address this, they introduce a novel methodology called Post-Calibration Truncated Conformal Prediction (PoT-CP), which estimates a specific rank cutoff using calibration sets and applies truncation by assuming that beyond this rank, only redundant labels would appear in the prediction sets. The authors theoretically prove that their new prediction set converges to the original prediction set as the number of calibrations increases, thus establishing asymptotic marginal validity, and further discuss asymptotic conditional validity. Finally, this work justifies the applicability of their methodology through numerical experiments across various scenarios and datasets.

### Strengths
The most impressive strength of this work lies in its novelty. PoT-CP is motivated by a simple yet insightful observation, and the approach to address it is also straightforward. Rather than introducing a new non-conformity score or overhauling the prediction framework with complexity, the authors design an easily implementable algorithm by adding an ad-hoc procedure (i.e. truncation) applicable to various existing non-conformity scores.

Moreover, they conduct extensive numerical experiments across a range of models, datasets, and the choices of the non-conformity score. In particular, they thoroughly discuss and numerically demonstrate the advantages of PoT-CP when using non-conformity scores like APS, SAPS, and RAPS. This careful execution of exhaustive numerical experiments represents another notable strength of the work.

### Weaknesses
As the authors acknowledge in the discussion, the prediction sets derived from PoT-CP achieve asymptotic validity rather than finite-sample validity, meaning that the calibration set size significantly impacts PoT-CP’s coverage. However, the paper does not carefully address differences in coverage relative to data size. While they discuss changes in prediction set size with data size (lines 375–517), they omit discussion on empirical coverage.

Furthermore, despite the originality of their idea and the rigorous numerical experiments, the theoretical analysis appears somewhat sloppy and impedes readability, there are questionable statements in the theoretical analysis in terms of rigorousity. For instance, in Theorem 2 and Corollary 2, they discuss the almost sure convergence of (marginal) probability, even though probability itself is not defined on a measure space. Additionally, since PoT-CP does not achieve finite-sample validity, convergence rates should be discussed through careful use of such as Big-O notation; however, the paper lacks adequate explanation on this aspect.

### Questions
1. This question relates to the previously mentioned points. Did you observe how (empirical) coverage changes with variations in the calibration set size? If so, what were the results?

  2. The experiments in this work discuss only cases where the nominal level \alpha is fixed at 0.1. Did you find any systematic changes in the performance of PoT-CP when this value was varied?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a modification to the construction of conformal prediction sets in classification problems. While standard CP only requires finding the critical nonconformity threshold, the authors suggest an additional requirement: identifying a second threshold based on the rank of the nonconformity scores within their corresponding predicted distributions. This added criterion for constructing the set theoretically ensures that the prediction set will not expand, and it can empirically reduce the set size, as demonstrated in experiments. Furthermore, the authors theoretically show that, asymptotically, their approach will achieve the same marginal and conditional coverage as standard CP.

### Strengths
The paper is well-written and easy to follow. Exploring alternative methods for constructing prediction sets beyond the standard thresholding approach (on nonconformity scores) is indeed an intriguing direction. The fact that the idea can be generalized to any nonconformity function adds to its strength.

### Weaknesses
1. While it is interesting to explore different ways of constructing prediction sets beyond a simple thresholding criterion, CP offers a straightforward justification rooted in statistical hypothesis testing for rejecting a label from the set. It is unclear what statistical reasoning the proposed approach uses to reject a hypothesis (i.e., a label being in the prediction set) that traditional hypothesis testing could not reject. Specifically, the p-values used in standard CP are derived from the nonconformity scores and are guaranteed to be uniformly distributed under the null hypothesis of exchangeability. This property is crucial for ensuring the validity of the coverage guarantees. The paper does not provide a clear explanation of how the proposed two-stage approach maintains this property, or if the p-values used in the second stage are also uniformly distributed. Without this, it is difficult to assess the statistical validity of the method.

2. In general, CP is a popular framework due to its ability to reason and provide finite-sample guarantees. Asymptotic results, while potentially useful when fundamental assumptions like exchangeability are violated, may not be particularly interesting. The strength of CP lies in its ability to provide guarantees with a finite number of samples, which is often more relevant in practice. The asymptotic results presented in the paper, while theoretically sound, do not address the practical concerns of finite-sample performance, which is a key aspect of CP. Furthermore, the paper does not discuss the convergence rate of the proposed method to the asymptotic regime, which is important for understanding how many samples are needed for the asymptotic results to be meaningful.

3. I don't necessarily agree that having an empty set in CP is better than having a set with multiple labels but no coverage. If CP serves as an uncertainty representation tool, we naturally expect to see relative comparisons between the set sizes for different instances. Thus, a set with three labels is more uncertain than one with two labels, even if none of them cover the ground truth. The paper seems to suggest that empty sets are preferable, but this is not necessarily the case when considering the practical use of CP as a tool for uncertainty quantification. The size of the prediction set should reflect the uncertainty of the prediction, and an empty set does not provide any information about the relative uncertainty between different instances.

### Questions
1. SSCV, though used in other papers, is not a good measure of conditional coverage, and your experiments demonstrate this. In the best-case scenario, your approach should have the same conditional coverage properties as standard CP, so any improvement in such a metric clearly indicates its uselessness. Do authors agree?

2. To me, Figures 3.c and 3.d look weird. Can authors explain why they don't behave as APS and THR?  

3. There are some typos in the proof of Lemma 1.

4. Theorem 3 is obvious and doesn’t really need to be presented as a theorem.

5. Have the authors considered comparing the efficiency by excluding the empty sets? Or have they compared the efficiency only for cases with coverage?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper aims to increase the efficiency of conformal prediction by reducing the set size. Unlike existing literature, this paper identifies the redundancy issue associated with CP in two separate scenarios: under coverage and over coverage. The inclusion of redundant labels leads CP to generate inefficient sets. To fix this problem, this paper develops a Post-Calibration Truncated Conformal Prediction (PoT-CP) procedure to eliminate class labels with high uncertainty from the prediction set for the sake of reducing the set size. Overall, this paper is well-written, and the conclusion is supported with solid evidences.

### Strengths
Extend the conformity score from one dimension to two dimensions, identify the redundancy in the class lalels included in the prediction set, develop a post-truncation conformal prediction algorithm to truncate prediction sets while maintaining coverage.

### Weaknesses
The motivation of this paper needs to be strengthend particularly the broad implications of reducing the set size of CP to the machine learning community and beyond needs to be clearly elaborated. 

On the computational study side, I suggest reporting the average set size of PoT for under coverage and over coverage separately. As the set size of the under-coverage cases is always zero, if you could report the average set size of the two scenarios separately and as a whole, this will make it more direct to assess the impact of the proposed truncation operation. 

It does not make sense when you claim "The key idea is to eliminate classes with high uncertainty in the prediction sets". What do you mean high uncertainty? Do you mean that 1 - class probability is the measure of uncertainty?

### Questions
1. Can you explain why the variation of calibration set size has a different effect on the average set size of different conformity scores as shown in Fig. 3?
2. It is also important to investigate the behavior of the conformal predictors when alpha takes other values. I am wondering what is the impact of increasing alpha value on the effect of the truncation operation in reducing the average set size.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper aims to improve the efficiency of conformal prediction sets by "truncating redundant labels," where the authors refer to this redundancy as predicted labels contained in the prediction set although these do not include the ground truth. The key idea is to find a ranking parameter r* using the calibration data that truncates the set sizes while maintaining coverage. The authors proved an asymptotic marginal coverage and asymptomatic conditional coverage (if the base conformal method achieves it). Numerical experiments show that the proposed method reduces the set sizes, maintaining adaptivity, and coverage.

### Strengths
1. A plug-in method that can be used in combination with any conformal approach to reduce the set size.
2. The authors proved a form of `no harm': when the sample size n goes to infinity the truncated set and the original conformal set would contain the test label.
3. To the best of my understanding, there are no additional hyper-parameters required to be tuned to apply the truncation; there is a procedure to tune r*.
4. Numerical experiments demonstrate the gain in performance in the sense that the constructed sets are smaller in size, adaptive, and achieve the desired coverage rate.

### Weaknesses
1. Marginal coverage is only guaranteed asymptotically, which arguably undermines the appeal of conformal prediction. See question (1) below.
2. When the sample size n goes to infinity, I expect the prediction sets constructed by the proposed method to get closer and closer to the sets constructed by the base conformal method. For an oracle model for which the conditional class probabilities are known, following Eq. (3), the rank r* is anticipated to get higher as n increases up to a point where the base and truncated methods would coincide. This behavior is somewhat demonstrated in Figure 3. As a result, it is not entirely clear to me why would one be interested in implementing this method. In the regime where it is provably valid, it almost coincides with the original score function.



### Questions
1. To address the problem of asymptotic marginal coverage, would it be possible to apply an additional calibration step to tune r*? That is, the first calibration step amounts to finding Q and r* (as happens currently), and the second calibration step aims to find a Q* (based on a fresh calibration set) as in standard conformal. 

2. Line 765: what do you mean by P[Ev|Ev] ? I believe this is a typo. 

3. As far as I understand, there are no error bars in the figures/tables. Please include standard errors.

### Soundness
2

### Presentation
3

### Contribution
2
