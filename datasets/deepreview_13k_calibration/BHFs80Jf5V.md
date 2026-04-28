# Constructing Confidence Intervals for Average Treatment Effects from Multiple Observational Datasets

- Decision: Accept
- Avg Score: 6.50
- Scores: 8, 6, 6, 6

## Abstract
Estimating confidence intervals (CIs) of the average treatment effects (ATE) from patient records is crucial to assess the effectiveness and safety of drugs. However, patient records typically come from different hospitals, thus raising the question of how multiple observational datasets can be effectively combined for this purpose. In our paper, we propose a new method that estimates the ATE from multiple observational datasets and provides valid CIs. Our method makes little assumptions about the observational datasets and is thus widely applicable in medical practice. The key idea of our method is that we leverage prediction-powered inferences and thereby essentially `shrink' the CIs so that we offer more precise uncertainty quantification as compared to na{\"i}ve approaches. We further prove the unbiasedness of our method and the validity of our CIs. We confirm our theoretical results through various numerical experiments. Finally, we provide an extension of our method for constructing CIs from combinations of experimental and observational datasets.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper considers the problem of estimating confidence intervals for average treatment effects when given access to a small, unconfounded observational dataset and a larger, confounded observational dataset. Specifically, the problem setting assumes that the covariates for both datasets come from the same population, but the propensity score may differ and the potential outcomes are only independent of treatment assignment in the smaller unconfounded dataset.

The paper's method builds on the prediction-powered inference (PPI) framework, which creates an estimate of the ATE via the confounded dataset and then uses the unconfounded dataset to adjust it and build the appropriate confidence intervals. The paper proves that their method asymptotically results in valid confidence intervals. The method is evaluated on both synthetic and real data, showing its gains over using only the unconfounded dataset.

### Strengths
The paper addresses an important issue that has not been covered in the literature before. The paper also does a good job of placing itself within the literature. The paper also does a good job of precisely backing up their claims with theorems.

### Weaknesses
On the theoretical side, the paper only shows the asymptotic validity of the proposed method. There are no results demonstrating the width of the resulting confidence intervals. One would like to know under what circumstances the given method will produce a confidence interval that converges on exactly 1-$α$. 

Moreover, the paper does not give any theoretical insight into when it is beneficial to use both datasets as opposed to just the unconfounded dataset. There should be some result showing that the confidence intervals are tighter for proposed method than for the naive method.

### Questions
Under what circumstances can it be proved that the proposed method is actually better than operating on just the unconfounded dataset?

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
This work presents a method for estimating average treatment effects (ATE) and constructing valid confidence intervals (CIs) from multiple observational datasets. It uses minimal assumptions and leverages prediction-powered inferences for more precise CIs. The approach is validated through theoretical proofs and numerical experiments, with extensions for mixed data sources.

### Strengths
The article is well written, and technically sound. The proposed approach is interesting, with great potential for practical application. The previous literature is well integrated, and the paper's novelty is well explicited.

### Weaknesses
1. It appears that the novelty of this work is incremental. Use the previously proposed estimator for causal effects and use it in a PPI framework to construct confidence intervals. 

2. Lemma 6.1 is a theoretical property of the inverse probability weighting (IPW) estimator and should not be considered a contribution of this paper. Furthermore, the IPW estimator can also be interpreted as an estimation method based on the influence function, while the augmented inverse probability weighting (AIPW) estimator is derived from the effective influence function. Therefore, the statements made in lines 357-360 are inaccurate.

3. The proof of Theorem 5.2 appears to depend on the asymptotic normality of $\tau_2$. However, the $\mathcal{D}_2$ does not seem to satisfy ignorability, suggesting that it is a biased estimator. I have reservations about whether it is indeed asymptotically normal about $\hat{\tau}_2$ and $\tau_2$ at this point.

### Questions
This paper is written towards an audience of applied statistics researchers, and is more suited for a statistical journal such as Biometrika. Although the reviewer acknowledges the significance of rigorously discussing the construction of confidence intervals, the methodology presented may not be highly relevant to the broader community of ICLR. For example, it does not discuss neural network or representation learning at all.

### Soundness
3

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
5

### Summary
The authors propose a new method to compute confidence intervals of the Average Treatment Effect (ATE) of the Risk Difference based on two observational data sets, the first one of small size in which all confounders are observed, the second one being larger with potential unobserved confounders. They use the largest data set to debias the estimation of the ATE computed on the first data set. The proposed confidence interval is shown to have the correct asymptotic coverage. Experiments on a toy data set and on real-world data sets show that the proposed method leads to smaller unbiased confidence intervals.

### Strengths
The paper focuses on a very important topic, which is uncertainty quantification of point estimate for the ATE, based on observational data sets. Obtaining accurate confidence intervals for the ATE helps to understand the effect of a treatment (e.g., drugs). Observational data are becoming more and more common in causal inference. The main contribution of the paper is to propose a new way of computing confidence intervals based on two observational data sets. The formula is rather simple and easy to use, while it can be applied to a wide variety of estimators (in the paper, AIPW or IPW are used depending on the context). 
Experiments tend to show that the proposed method is better in terms of coverage and IC length.

### Weaknesses
There is a potential practical interest for the confidence interval and the point estimate developed in this paper. I have two majors concerns with the paper: 
- the experimental results on the toy data set are inconclusive : the input variable is of dimension one, which does not correspond to a real-world problem. For the conclusion to hold, I would expect more experiments on more complex settings (more input variables, with or without dependence, how relaxing the assumption of all observed confounders in the first data set may impact the estimation performances). Experimenting on one single input variable does not allow us to obtain a clear comprehension of the performance of the proposed method. 
- Theorem 5.2 is the main theoretical result of the paper. It is claimed below that it does not directly result from the Prediction-powered Inference (PPI) framework. However, going in detail through the proof, I could not find an argument specific to the causal inference framework or the AIPW estimator. The proof relies on Central Limit Theorems of two independent quantities.
Thus, I find the novelty of the contribution mild from a theoretical perspective. Besides, in my opinion, more experiments should be carried out to assess the performance of the method.

- Position of the work: it is assumed that the small data set contains all confounders. The major difference with a RCT is that the propensity score is unknown and depends on the covariate (as discussed in page 4, last paragraph). This justifies the use of IPW with the true propensity score (step B, page 7). However, numerous work have shown that even in a RCT scenario where the true propensity score is known, estimating it can reduce the variance of the ATE estimate (see, e.g., references in https://arxiv.org/pdf/2303.17102). Thus, in a RCT, one would likely use an estimation of the propensity score inside the IPW estimate. This point should be discussed and may lead to qualify statements about differences between RCT and the small data set you consider. In particular, could we apply methods developed for RCT (van der Laan et al., 2024) to the first experimental setting? Paragraph l.119-121 could be modified to make explicit the differences (if any) between RCT+observational and the considered setting observational+observational. 
- Regarding the work of van der Laan et al., 2024, it is mentioned that their method is unstable due to a matrix inversion (l.509-510). I went quickly through their paper and did not find such an operation. Could you be more specific, and maybe describe with more details how this method works, as it is the main competitor?
- l.151-152 ``PP CI s smaller than the classical CI when the model $f$ is sufficiently accurate.'' Is there a specific reference for this fact?
- l.203-204: It is usually required that $0< \pi(x) < 1$.
- l.269: "The estimation needs to be both valid and unbiased to later yield valid CIs.'' What does ``valid'' mean in these contexts?
- Lemma 5.1 Assumptions are not complete/clear: there are constraints on $\alpha_{\mu}$ and $\alpha_{\pi}$, the assumption on $e(\cdot)$ is about $1/\hat{e}(\cdot)$ and not $e$ and the proof of Wager holds for crossfitted estimators. The asymptotic variance involves theoretical quantities and not their estimators. Please correct the statement. Some remarks also hold for Theorem 5.2.
- l.298  $\tilde{Y}_{\hat{\eta}}$ is built using $D_1$ and then its empirical mean (subtracted by $\hat{\tau}_2$) is computed over 
$D_1$. 

In the proof, it is argued that $\hat{\Delta}_{\tau}$ verifies a Central Limit Theorem which is not clear here, as the term inside the sum depends on the whole sample $\mathcal{D}_1$. 

I believe the proof holds for a fixed function $\tilde{Y}_{\eta}$ but not for the estimated function. Or it needs at least clarifications. 
- Equation 5, how do this new confidence interval compares to a classical one (using only $\mathcal{D}_1$). Can you show that it is stricly smaller in some specific settings (and describe them)? 
- Lemma 6.1 A factor $1/n$ is missing in the definition of $\hat{\tau}_1$, $\hat{\sigma}_1^2$ cannot depend on the sample size $n$. Its expression can be made explicit as a function of the nuisance components. In the proof, $\hat{\pi}$ should be replaced by $\pi$.  
- l488 In the real-world application, how the RMSE is computed, since we do not have access to the true ATE value? Please define ``factual outcome''. 
- l.499 ``Takeaway: Our PPI-based method is effective for medical data.'' Please qualify this statement, as you evaluate your method on two datasets only. 

Typos: 
- open parenthesis l.124
- l.162 : a for is missing
- l.177 and l.334 : $p$ is used for the number of input variables and the ratio between the data set sizes. 
- l.363 ``This steps computes analogous the above''
- l.409 ``We now evaluate our the effectiveness''
- l469 ``Hence, our method performs thus best.''

### Questions
- Position of the work: it is assumed that the small data set contains all confounders. The major difference with a RCT is that the propensity score is unknown and depends on the covariate (as discussed in page 4, last paragraph). This justifies the use of IPW with the true propensity score (step B, page 7). However, numerous work have shown that even in a RCT scenario where the true propensity score is known, estimating it can reduce the variance of the ATE estimate (see, e.g., references in https://arxiv.org/pdf/2303.17102). Thus, in a RCT, one would likely use an estimation of the propensity score inside the IPW estimate. This point should be discussed and may lead to qualify statements about differences between RCT and the small data set you consider. In particular, could we apply methods developed for RCT (van der Laan et al., 2024) to the first experimental setting? Paragraph l.119-121 could be modified to make explicit the differences (if any) between RCT+observational and the considered setting observational+observational. 
- Regarding the work of van der Laan et al., 2024, it is mentioned that their method is unstable due to a matrix inversion (l.509-510). I went quickly through their paper and did not find such an operation. Could you be more specific, and maybe describe with more details how this method works, as it is the main competitor?
- l.151-152 ``PP CI s smaller than the classical CI when the model $f$ is sufficiently accurate.'' Is there a specific reference for this fact?
- l.203-204: It is usually required that $0< \pi(x) < 1$.
- l.269: "The estimation needs to be both valid and unbiased to later yield valid CIs.'' What does ``valid'' mean in these contexts?
- Lemma 5.1 Assumptions are not complete/clear: there are constraints on $\alpha_{\mu}$ and $\alpha_{\pi}$, the assumption on $e(\cdot)$ is about $1/\hat{e}(\cdot)$ and not $e$ and the proof of Wager holds for crossfitted estimators. The asymptotic variance involves theoretical quantities and not their estimators. Please correct the statement. Some remarks also hold for Theorem 5.2.
- l.298  $\tilde{Y}_{\hat{\eta}}$ is built using $D_1$ and then its empirical mean (subtracted by $\hat{\tau}_2$) is computed over 
$D_1$. 

In the proof, it is argued that $\hat{\Delta}_{\tau}$ verifies a Central Limit Theorem which is not clear here, as the term inside the sum depends on the whole sample $\mathcal{D}_1$. 

I believe the proof holds for a fixed function $\tilde{Y}_{\eta}$ but not for the estimated function. Or it needs at least clarifications. 
- Equation 5, how do this new confidence interval compares to a classical one (using only $\mathcal{D}_1$). Can you show that it is stricly smaller in some specific settings (and describe them)? 
- Lemma 6.1 A factor $1/n$ is missing in the definition of $\hat{\tau}_1$, $\hat{\sigma}_1^2$ cannot depend on the sample size $n$. Its expression can be made explicit as a function of the nuisance components. In the proof, $\hat{\pi}$ should be replaced by $\pi$.  
- l488 In the real-world application, how the RMSE is computed, since we do not have access to the true ATE value? Please define ``factual outcome''. 
- l.499 ``Takeaway: Our PPI-based method is effective for medical data.'' Please qualify this statement, as you evaluate your method on two datasets only. 

Typos: 
- open parenthesis l.124
- l.162 : a for is missing
- l.177 and l.334 : $p$ is used for the number of input variables and the ratio between the data set sizes. 
- l.363 ``This steps computes analogous the above''
- l.409 ``We now evaluate our the effectiveness''
- l469 ``Hence, our method performs thus best.''

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
The authors present a method, based on prediction-powered inference, for estimating confidence intervals from two datasets, one with observed confounders and one with additionally hidden confounders. Theoretical and empirical results are provided.

### Strengths
- The work addresses a clear research gap with respect to existing work.
- The provided theoretical results support the method.
- The method is presented clearly, and the work is easy to follow.

### Weaknesses
 - The current empirical analysis is limited, with mostly quantitative results and only linear models.

- Due to the required assumptions, the practical relevance of the work is not entirely clear to me.

- The conclusion is an afterthought in the current version, with no discussion of limitations or directions for future work.

### Questions
1. **Empirical results:**
  - Mostly qualitative results are provided for the synthetic data. I would be interested in seeing the coverage and RMSE of each method with respect to ground truth, which should be known as the data is simulated. It seems like the proposed method has a higher bias, but lower variance.
  - In my opinion, it would be interesting to experiment with settings with more data in $\mathcal{D}_1$ to see when only using $\mathcal{D}_1$ becomes better.
  - How can the RMSE be calculated for the real data, when the true ATE is unknown? 
  - Unless I am mistaken, it seems that only simple learners are considered, based on linear and logistic regression (Appendix E3)? If so, it would be insightful to also compare with more advanced ML algorithms (e.g. gradient boosting).

2. **Practical significance:**
Although the work is interesting from a theoretical perspective, I wonder at its practical significance. How realistic are your assumptions? How can a practitioner verify them and trust your method?

3. **Conclusion:** A more detailed discussion of limitations and directions for future work would be appreciated.

___


**Minor points:**
- Brackets missing in the citations on lines 48 and 49.
- Gray text in Table 1 is not applied to all columns.

### Soundness
3

### Presentation
3

### Contribution
2
