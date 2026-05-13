# Wasserstein-Regularized Conformal Prediction under General Distribution Shift

- Decision: Accept
- Scores: 8, 6, 6

## Abstract
Conformal prediction yields a prediction set with guaranteed $1-\alpha$ coverage of the true target under the i.i.d. assumption, 
which can fail and lead to a gap between $1-\alpha$ and the actual coverage. Prior studies bound the gap using total variation distance, which cannot identify the gap changes under distribution shift at different $\alpha$, thus serving as a weak indicator of prediction set validity. Besides, existing methods are mostly limited to covariate shifts, while general joint distribution shifts are more common in practice but less researched. In response, we first propose a Wasserstein distance-based upper bound of the coverage gap and analyze the bound using probability measure pushforwards between the shifted joint data and conformal score distributions, enabling a separation of the effect of covariate and concept shifts over the coverage gap. We exploit the separation to design algorithms based on importance weighting and regularized representation learning (WR-CP) to reduce the Wasserstein bound with a finite-sample error bound. WR-CP achieves a controllable balance between conformal prediction accuracy and efficiency. Experiments on six datasets prove that WR-CP can reduce coverage gaps to 3.1% across different confidence levels and outputs prediction sets 38% smaller than the worst-case approach on average.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper addresses conformal prediction under general distribution shift, including both covariate and concept shift. The authors propose using the Wasserstein distance to bound the coverage gap of conformal prediction methods in shifted distributions. Then, they decompose the Wasserstein distance between calibration and test distributions into two parts which relates to the covariate shift and concept shift separately. For scenarios where test samples are available, they use the Wassertein distance between empirical calibration and test distributions to approximate the true Wasserstein distance with concentration bound. Finally, they also consider the case without samples from the test distributions, in a multi-source conformal prediction setting. In this setting, the test distribution is an unknown mixture of training distributions. In this case, the authors introduce a Wasserstein regularizer in the training loss, which is the uniform average of the Wasserstein distance between the pushforward measure of the conformal score of the entire training data and the conformal score of each compoent over that component.

### Strengths
(1) The paper rigorously explores conformal prediction under complex distribution shifts, going beyond covariate shift to address both covariate and concept shifts. 

(2) The decomposition of the Wasserstein distance to measure and address different types of shifts is novel and provides a clearer structure for bounding the coverage gap. 

(3) The optimization method proposed in this paper by minimizing the Wasserstein distance is very practical. The application of a Wasserstein regularizer in cases where test samples are unavailable (i.e., unknown mixture of training distributions) is a practical contribution, especially for real-world applications. 

(3) The paper provides theoretical guarantees and concentration bounds. The authors validate their method across multiple datasets, showing significant improvements in coverage gap reduction and prediction set size.

### Weaknesses
(1) The Wasserstein distance upper bound on the coverage gap is decomposed into two parts. The term relates to the concepts shift, eta depends on the test distribution and is a little hard to interpret for me.

(2) In cases where some training components have smaller weights in the unknown mixture, the uniform averaging of the Wasserstein distance may potentially lead to suboptimal regularization effects.

(3) minor thing: in Line 243, there is no plot (c) in figure 1.

### Questions
(1) After decomposing the Wasserstein distance, the covariate shift component seems to be captured by the Lipschitz constant of the difference between the hypothesis and the training distribution. Is it correct to interpret that a smoother difference between the hypothesis and the training distribution would improve robustness against covariate shift, since intuitively, if this difference is smooth over x, then covariate shift will change the prediction very little? Also, this kappa doesn't depend on the test distribution, so it also means the covariate shift part is easier?

(2) Is there any geometric intuition on the term eta, which captures the concept shift? 

(3) When the test distribution is an unknown mixture of the training distribution, the Wasserstein regularizer term seems to ask the conformal prediction has a small average wasseerstein distance over all components. Would it has negative effects on the results if some component with small weights in practice?

### Soundness
3

### Presentation
2

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
This paper investigates the effect of distribution shift between calibration and test data on conformal prediction guarantees. Theoretically, they upper bound the total distribution shift by two terms that decouple the effect of covariate and concept shifts. They are able to do so by using Wasserstein distance based upper bound of coverage gap ( which they also introduce.) Furthermore, they propose methods by which they minimize each term in the upper bound. Empirically they show that their proposed algorithm (WR-CP) can reduce coverage gaps and output smaller prediction sets.

### Strengths
1. They address an important problem in CP, namely decoupling the effect of covariate shift and concept shift on the coverage gap.
2. They upper bound the coverage gap by adopting the Wasserstein distance over the space of probability distribution of conformal scores. This allows to indicate changes across different values of mis-coverage rate $\alpha$.
3. The upper bound is then decomposed to explicitly depend on two terms where the effect of covariate/concept shift is decoupled. This is an important and novel contribution. The theory seems to extensively validate the results.

### Weaknesses
1. The minimization of the term corresponding to covariate shift, seems to just use previous contributions in the field (Tibshirani et. al 2019). Furthermore the optimization algorithm heavily depends on good density estimation, which is very difficult to do in practice.

2. The insights from the newly derived Wasserstein-based upper bound on the coverage-gap are the basis of the optimization procedure introduced in algorithm 1 (WR-CP). To this end:

2.a) There are no formal robustness/coverage guarantees on the final prediction sets. The way the problem is introduced, this becomes a major limitation.

2.b) The problem is considered within the context of "regression" tasks. However, when exploring the literature including classification tasks, we can see a clear distinction between training phase (where the predictor model parameters are changed in order to optimize a conformal-based loss ( e.g (Stutz et. al 2022, Yan et. al 2024)) , and the calibration procedure where the model is treated as a black-box and formal coverage guarantees are the main point. The same pipeline seamlessly extends to the regression setting as well. I do not believe the authors have made a clear distinction where their contribution lies in this context. 

2.c) The experiments compare the proposed algorithm WR-CP to Worst-Case-CP ( WC-CP) to indicate a reduction in length-inefficiency of the prediction sets. I do not believe the experiments are a fair comparison, as the model parameters are "changed". The fair comparison would apply a fixed calibration procedure, with guarantees to both models ( one baseline trained without any insights from the Wasserstein upper bound, one trained according to WR-CP) in order to measure the gains in terms of coverage gap or the length-inefficiency. To indicate this point further, (https://lilywenglab.github.io/Provably-Robust-Conformal-Prediction/) applied "Conformal Training" (Stutz. et. al) where the model parameters are changed similar to WR-CP, on top of an algorithm that certifies robustness in case of adversarial noise, and reduce the inefficiency of the prediction sets. Then when applying a CP method with guarantees on top of the new model, we obtain smaller sets. This procedure seems sound as it does not break the main point of CP ( coverage guarantees) and yet reduces inefficiency. The current experimental set-up of this paper does not support their claim ( (-38%) reduction in the prediction set sizes than the worst-case approach on average), and are insufficient. Based on this, I don't believe the experiments fairly and constructively asses performance of WR-CP compared to the SOTA or the prior works. 

5. very very Minor typos ~ there is no fig 1(c) , line 153 "adaption"

### Questions
1. With respect to point 1 in the "Weaknesses",  I am concerned about the practicality of the algorithm 1 ( WR-CP), and computational overhead. Further, could you elaborate on how alternate solutions in the existing literature can potentially solve the density-estimation problem - or be integrated within your pipeline ( if any according to your literature-review ). I believe this is a major over-head that can be addressed if the algorithm allows for alternate solutions. 

2. With respect to points 2a, 2b, could you elaborate where your contributions stand with respect to the CP pipeline ( as described ).  I believe the paper can benefit from an alternative narrative where the contributions are more on the conformal-based training procedure, and formal gaurantees are provided. Providing formal gaurantees during the trainning phase might be difficult, however applying a calibration procedure with the gaurantees to the "changed" model could mitigate this issue.

3. with regard to point 2c above, I am concerned about "the fairness" in the comparison with the baselines in which coverage is gauranteed. 

4. I believe the related works should include conformal training based procedures where the model parameters are explicitly changed in order to optimize a conformal-based efficiency, in order to clearly place your contributions with respect to the literature. Further, the application to Multi-source conformal prediction calls for a more thorough literature review in this context. there are works that use a similar framework and address distribution shift in a multi-agent CP framework, or use a similar global distribution to introduce distributed/federated conformal procedures. None of those were addressed in this work.

### Soundness
2

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
Conformal Prediction (CP) sets may not have the guaranteed lower-bounded coverage if calibration and test samples are not exchangeable. The authors derive bounds for and optimize the gap between nominal and empirical coverage in such a distribution-shift setup. Unlike existing work, the bounds and the optimization loss are given in terms of the Wasserstein Distance.

### Strengths
- Improving CP under distribution shifts is timely and challenging. The provided bounds and algorithm may increase CP applicability to new kinds of data.
- Optimizing the uncertainty estimation of a CP algorithm is an increasingly popular topic. It is interesting to focus on reducing a model's uncertainty instead of improving the accuracy of its point predictions.
- Looking at CP-aware optimization as the joint optimization of a standard objective and a CP-aware regularization term.
- The proposed penalty term does not seem to involve the (non-differentiable) sample quantiles of the conformity score distribution.

### Weaknesses
 - Using WD to optimize the prediction intervals is justified by saying that the Total Variation Distance (TVD) *ignores where two conformal score distributions differ* by focusing on the worst-case discrepancy and is location independent. The authors should clarify the difference between the integral and the infimum in the WD definition, Eq.5, and the sup appearing in the definition of TVD. Specifically, the infimum in the Wasserstein distance is taken over all joint distributions with the correct marginals, representing the minimum cost of mass transport. The integral represents the cost of a specific transport plan, and it would be helpful to elaborate on how this relates to the sup in the TVD, which considers the maximum difference in probability assigned to any measurable set, and how this difference impacts the optimization.
- The authors may justify better their idea of separating covariate and concept shift. In practice, such separation requires making strong assumptions on the data-generating distribution. The advantages are less clear. It's not immediately obvious why separating these shifts is beneficial for optimizing prediction interval size, especially given the potential for complex interactions between covariate and concept shifts in real-world scenarios. The authors should provide a more detailed explanation of the specific conditions under which this separation is advantageous and how it simplifies the optimization problem.
- The optimization scheme assumes the availability of samples from the base and the shifted distributions. This is not the case in the standard distribution-shift setup. Access to the test samples at training time would allow a more straightforward approach where the CP algorithm is trained on all samples and hence not affected by distribution shift. The authors should clarify how their approach differs from simply training a CP model on the combined training and test data, and why this is not a viable alternative. The assumption that samples from the shifted distribution are available during training needs to be better justified in the context of typical distribution shift problems.
- The authors should discuss the exchangeability of the samples in the proposed application of Section 5. It is unclear whether the calibration and test sets are truly non-exchangeable, and this needs to be explicitly addressed. If the test distribution is a mixture of the training distributions, it is not clear why sampling from the test distribution is not equivalent to sampling from the training set, and this point needs further clarification.

### Questions
- If the goal is to optimize the size of the prediction intervals, why is it important to distinguish between covariate and concept shift? And why should one avoid the worst-case approach of an analogous TVD minimization? 
- Why does the TVD fail *to indicate coverage gap changes thoroughly" and  *is agnostic about where two distributions diverge*? The WD integrates over local divergences and does not explicitly depend on $\alpha$. Can one prove that the TVD fails to summarize the distance between the quantiles of two distributions?
- Are the test and calibration samples of Section 5 non-exchangeable?
- Is the loss in Eq.19 tractable in practice? Doesn't the KDE cause numerical instabilities for bad kernel choices?  
- Have you compared the proposed optimization with a naive CP baseline trained on all available original and shifted samples?
- Do the proofs of Theorems 1 and 2 depend on the specific conformity measure?

### Soundness
3

### Presentation
2

### Contribution
2
