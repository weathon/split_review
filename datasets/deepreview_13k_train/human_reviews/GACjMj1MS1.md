# Empirical Likelihood for Fair Classification

- Decision: Accept
- Scores: 6, 6, 5

## Abstract
Machine learning algorithms are commonly being deployed in decision-making systems that have a direct impact on human lives. However, if these algorithms are trained solely to minimize training/test errors, they may inadvertently discriminate against individuals based on their sensitive attributes, such as gender, race or age. Recently, algorithms that ensure the fairness are developed in the machine learning community. Fairness criteria are applied by these algorithms to measure the fairness, but they often use the point estimate to assess the fairness and fail to consider the uncertainty of the sample fairness criterion once the algorithms are deployed. We suggest that assessing the fairness should take the uncertainty into account. In this paper, we use the covariance as a proxy for the fairness and develop the confidence region of the covariance vector using empirical likelihood \citep{Owen1988}. Our confidence region based fairness constraints for classification take uncertainty into consideration during fairness assessment. The proposed confidence region can be used to test the fairness and impose fairness constraint using the significant level as a tool to balance the accuracy and fairness.   Simulation studies show that our method exactly covers the target Type I error rate and effectively balances the trade-off between accuracy and fairness. Finally, we conduct data analysis to demonstrate the effectiveness of our method.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a framework to ensure fairness of classifiers while handling the uncertainty from point estimates using finite samples. In particular, formulating fairness in terms of the covariance between sensitive attributes and the decision boundary (Zafar et al. 2017), the authors propose using the empirical likelihood method to derive a confidence region for the covariance vector. Empirical evaluation using simulation as well as real-world data shows that the proposed approach can balance the accuracy-fairness tradeoff and be robust to distribution shifts.

### Strengths
The consideration of uncertainty in fairness assessment is interesting, and addresses a problem that is underexplored in existing approaches.

The application of an EL-based estimator for fairness using confidence intervals is a novel contribution. The authors suggest that this approach could be applied to other fairness criteria, which could increase the impact of this method broadly.

The paper is overall well-written and technically sound as far as I can tell.

### Weaknesses
While the comparison to Zafar et al. (2017) is very thorough, no other fair learning methods are considered in the empirical evaluation. In particular, comparing group fairness metrics such as DP and EO against baselines that directly optimize those notions could serve to more strongly justify the proposed approach using covariance-based fairness constraints.

I was a bit confused about the discussion at the end about applying EL to other fairness criteria. If indeed extending to non-linear measures is straightforward, it is unclear why the current method only considers covariance as a fairness proxy.

The motivation for the covariance-based fairness constraints was not very compelling. The authors suggest that determining the threshold for accuracy-fairness tradeoff becomes easier with the proposed approach. However, it is still unclear what the appropriate confidence region is for a given group fairness notion (whether a soft constraint to bound the violation or as a hard constraint).

### Questions
1. How does the proposed method compare against Zafar et al. (2017) under distribution shifts?

2. Is the discussion about EL for general fairness measures new or known results? If it is the former, there needs to be more details and proofs. 

3. I was not sure about the significance of Figure 1. Also, should the legends ID and OOD evaluations be switched in Figures 1 and 2? Figure 2 was also extremely hard to read.

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
Based on the covariance fairness measure by Zafar et al. (2017), the authors propose a fairness constraint based on a statistical likelihood test. Specifically, they formulate a constraint that requires that a statistical test with level alpha does not reject $H_0$: the classifier is fair.

### Strengths
I think that the idea of using a likelihood statistic for enforcing fairness is novel and an interesting approach. The paper is well written and supported by the required theoretical developments.

### Weaknesses
I think the main limitation of this work is the experimental evaluation. I understand that the method is based on Zafar's covariance fairness measure, and comparing to that is very valuable. However, since this seminal work in 2017, there has been a lot of development in the community regarding fairness regularizers or constraints. Comparing the results of your approach to some of these more recent works would be of interest.

Some minor questions and comments:
- On the bottom of page 3, you state that a system of $m$ constraints and $d$ parameters with $m\geq d$ can only have the solution $\theta=0$. If I understand correctly $m$ is the number of sensitive attributes and $d$ is the number of features. Does it make sense that $m\geq d$?
- In equation (8), is $\lambda$ a decision variable of the minimization problem? 
- Am I correct in my analysis that (8) is nonconvex?
- I think Figure 1 is very hard to understand. Should we compare Figure 1 with Figure 2 and observe that the ID results are more representative of the OOD resutls than in Figure 2?

### Questions
Some minor questions and comments:
- On the bottom of page 3, you state that a system of $m$ constraints and $d$ parameters with $m\geq d$ can only have the solution $\theta=0$. If I understand correctly $m$ is the number of sensitive attributes and $d$ is the number of features. Does it make sense that $m\geq d$?
- In equation (8), is $\lambda$ a decision variable of the minimization problem? 
- Am I correct in my analysis that (8) is nonconvex?
- I think Figure 1 is very hard to understand. Should we compare Figure 1 with Figure 2 and observe that the ID results are more representative of the OOD resutls than in Figure 2?

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
This paper proposes to use the covariance as a proxy for the fairness and develop the confidence region of the covariance vector using empirical likelihood. In this way, a confidence region (with the significant level alpha being used for the fairness constraint) can be used to provide a more interpretable way to trade-off between accuracy and fairness (DP).

### Strengths
1. The proposed approach is technically sound and does seem to have the potential to replace the covariance based measure in Zafar et al., 2017 and become a more general measurement for DP.

2. Comparing results from Table 3 and 4, the proposed algorithm does have a positive impact on both DP and EO on the ACS PUMS datasets including the OOD cases.

### Weaknesses
The proposed method itself is technically sound and has good potential. Most of my concerns are regarding the evaluation of the method in the experiments.

1. The simulation results in Table 2 do not seem to be a fair comparison. I would suggest adding more granularity for Zafar et al. with 0<c<0.1.

2. In Table 3, increasing alpha from 0.05 to 0.5 does not seem to affect the performance much (both in training and testing).

3. The proposed algorithm should be tested on more commonly used fairness datasets such as [1] or the ones from UCI Machine Learning Repository (https://archive.ics.uci.edu/)--- Adult Census Income, German Credit, etc.

4. Only one baseline is compared in the experiments. I would suggest the authors to test against other baseline approaches optimizing for DP.

### Questions
1. Can you provide more simulation results in Table 2 for Zafar et al. with 0<c<0.1? E.g. c=0.01, 0.02, ... Meanwhile, can alpha take values of 1? Or what will happen when alpha is close to 1, e.g. alpha = 0.99?

2. In Table 3, increasing alpha from 0.05 to 0.5 does not seem to affect the performance much (both in training and testing). Is it still the case when alpha is increased to e.g. 0.9?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
