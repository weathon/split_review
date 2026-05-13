# CBMA: Improving Conformal Prediction through Bayesian Model Averaging

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Conformal prediction has emerged as a popular technique for facilitating valid predictive inference across a spectrum of machine learning models, under minimal assumption of exchangeability. Recently, Hoff (2023) showed that full conformal Bayes provides the most efficient prediction sets (smallest by expected volume) among all prediction sets that are valid at the  $(1 - \alpha)$ level if the model is correctly specified. However, a critical issue arises when the Bayesian model itself may be mis-specified, resulting in prediction interval that might be suboptimal, even though it still enjoys the frequentist coverage guarantee. To address this limitation, we propose an innovative solution that combines Bayesian model averaging (BMA) with conformal prediction. This hybrid not only leverages the strengths of Bayesian conformal prediction but also introduces a layer of robustness through model averaging. Theoretically, we prove that the resulting prediction interval will converge to the optimal level of efficiency, if the true model is included among the candidate models. This assurance of optimality, even under potential model uncertainty, provides a significant improvement over existing methods, ensuring more reliable and precise uncertainty quantification.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors, working in the niche of bayesian conformal prediction, propose a bayesian model averaging procedure "infused" with conformal prediction, in order to recover coverage in the case of model misspecification

### Strengths
I found the article quite well written.
Moreover, the proposal is of clear theoretical and applied interest, and developed with care and mathematical soundness.

### Weaknesses
I fear that the authors have oversold their claim. In fact, in the literature proposals of conformal model averaging can be found  (https://www.sciencedirect.com/science/article/pii/S0925231219316108, https://arxiv.org/abs/2408.06642#:~:text=Unlike%20traditional%20methods%2C%20conformal%20ensembling,%2Dto%2Dinterpret%20uncertainty%20estimates. to name a few).

I found the simulation quite lacking in terms of depth, as well and presentation of the results

I remain unconvinced that the authors have properly contextualized their contribution, as some methods do have theoretical guarantees. Moreover, the theoretical guarantees on minimal size are asymptotic, and nothing is stated on the rate of convergence nor on finite sample properties. The impact in terms of interval length does not seem statistically significant.

### Questions
-As shown in the "weaknessess", some proposals (usually in a frequentist setting) are present in the literature when it comes to model averaging/ensembling in a conformal sense. Can you comment on this, maybe providing a more thorough analysis of the outstanding literature?

- I find the cases provided by the authors of limited applicative interest, I wonder if it could be possible to provide more challenging "misspecification" cases, like for instance cases where the model misspecification causes the conditional iid assumption to break (e.g. an AR2 model with only one lag).

- The impact in terms of interval length does not seem statistically significant. Are the authors able to check this, using maybe the Scheffe' method?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors highlight that the efficiency of traditional conformal prediction can degrade in the presence of model uncertainty. To address this, they propose Conformal Bayesian Model Averaging (CBMA), which combines multiple non-conformity scores from a Bayesian perspective. This approach integrates Bayesian model averaging with Bayesian conformal prediction (full conformal Bayes; Fong & Holmes, 2021), allowing it to leverage the optimality of Bayesian model averaging from a theoretical standpoint. From a computational perspective, CBMA utilizes the add-one-in importance sampling approach of Fong & Holmes (2021), enabling it to use all available data for model training while avoiding exhaustive computation. The work demonstrates CBMA’s high efficiency through numerical justification in both correctly specified and misspecified model scenarios.

### Strengths
While several works in the field of conformal prediction have applied a Bayesian perspective, this paper is meaningful since it is the first to attempt combining “multiple models” through Bayesian model averaging, marking a novel contribution. The proposed framework is straightforward, integrating traditional Bayesian model averaging directly, yet it is powerful as it incorporates model uncertainty more fully into the framework.

### Weaknesses
This work is limited by a lack of discussion comparing its approach to existing model aggregation methods in conformal prediction including frequentist’s perspective. Although Section 2.5 touches on related works, the primary advantage highlighted is the ability to use the full data, which may be better understood as a contribution from Fong & Holmes (2021) rather than an original novelty here. To justify the method empirically, it would be more reasonable to benchmark a few of these existing methods, comparing their coverage, interval length, and execution time with suggested method. Specifically, the paper should address how the proposed Bayesian model averaging approach compares to simpler, computationally cheaper methods such as weighted averaging of conformal scores or prediction sets, which are common in the literature. The current discussion does not adequately address the trade-offs between the theoretical benefits of the Bayesian approach and the practical advantages of these more straightforward alternatives. Furthermore, the computational cost of the proposed method, particularly the MCMC sampling, is not sufficiently discussed, which is a crucial consideration for practical applications.

### Questions
1. This question relates to the previously mentioned points. What do you consider the distinguishing features of your approach compared to existing conformal set aggregation methods? Were any experiments conducted to compare them? If so, what were the results, and if not, what are your thoughts on this?

  2. In the simulations, the nominal value of $\alpha$ was set to 0.1 in the linear model scenario, but 0.2 in the nonlinear case. Is there a particular reason for these distinct choices? Also, did you observe any systematic performance changes in the model based on the value of $\alpha$?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a solution in the form of Conformal
Bayesian model averaging (CBMA) that combines Bayesian Model Averaging (BMA) with conformal prediction to address the potential issue of suboptimal prediction intervals when the Bayesian model itself is misspecified. The theoretical and empirical results show the efficiency of CBMA.

### Strengths
The results presented in the paper confirm the effectiveness of the proposed method.

### Weaknesses
1.The novelty of the work is not very significant, as it simply combines several existing methods.

2.The names of the subsections under the "Simulation" section are not entirely appropriate,  since quadratic model is a type of non-linear model. It may be more appropriate to title whether the model is polynomial.

3.The paper seems not explain why the results for model 10 and model 11 are missing when $n=50$ in Table 2.

4.The paper contains a few typographical errors. For example, the last sentence before Section 2 has a typo. Additionally, there is a missing equation reference on line 150.

### Questions
1.Is it a clear pattern in the paper for when the authors use the term "prediction set" versus "prediction interval"?

2.Is there a comparison of the time costs between CBMA and other methods?

3.Why are the values of $\alpha$ set as well as the  ratio of the size of training set to test set differently in Table 1 and Table 2? It would be better to unify them or display both values or provide a rationale for why they differ, as this would improve the clarity and comparability of the results.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper leverages Conformal Bayesian and Bayesian Model Averaging to reduce the size of Conformal Prediction sets. The Bayesian posterior of different models is used in a weighted average of Bayesian conformity scores, which produces optimal prediction sets when the average contains the exact model and the sample size is infinite. Unlike previous Conformal Bayesian methods, the proposed scheme allows possible misspecifications in the underlying Bayesian model.

### Strengths
- Conformal Bayesian can combine the advantages of frequentist and probabilistic approaches.
- Theoretical results on the optimal efficiency of the prediction sets are rare and challenging to obtain in the CP framework.   
- Model averaging and ensemble methods perform well in various setups. Studying CP in that setup may produce powerful uncertainty quantification tools.

### Weaknesses
 - The technical contribution is to combine existing techniques: the BMA and Conformal Bayes. 
- It is unclear whether using the Bayesian conformity score is needed or if the method applies to any conformity score.
- The authors should clarify why averaging the (Bayesian) conformity scores associated with different models is better than computing the conformity score of a Bayesian average of the models. 
- The main theoretical result holds in the limit of an infinite sample size. In that limit, Bayesian confidence intervals are also correct. Why would one need CP? Including the exact model in the average may look unrealistic. Does the result generalize to models that are only approximately correct?
- Combining the results of Theorem 3 with Remark 1 to have a direct result on the optimality of the prediction sets would align better with the paper's goals.
- The model has not been tested on real data. For example, the authors could show that the scheme produces smaller intervals than standard CP or any other baseline.

### Questions
- Is accessing the model parameters required?
- Is the independence of the noise from X a strict assumption for the method applicability?
- Missing reference number below Eq 1.
- In Section 2.4, you say "We propose to average conformity scores from each model to construct combined conformity score." Is this equivalent to Eq.2? Why don't you condition on X in the equations on page 3?
- What do you mean by 'valid conformity score'?  
- How expansive is computing the prediction set? 
- Does BMA converge to the true model if $n \to \infty$ because its likelihood increases?
- Is this the first work on Conformal Bayesian that does not assume the underlying Bayesian model is exact?

### Soundness
2

### Presentation
2

### Contribution
1
