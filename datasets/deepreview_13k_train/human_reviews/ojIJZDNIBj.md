# Copula Conformal prediction for multi-step time series prediction

- Decision: Accept
- Scores: 6, 6, 8, 5

## Abstract
Accurate uncertainty measurement is a key step in building robust and reliable machine learning systems. Conformal prediction is a distribution-free uncertainty quantification framework popular for its ease of implementation, finite-sample coverage guarantees, and generality for underlying prediction algorithms. However, existing conformal prediction approaches for time series are limited to single-step prediction without considering the temporal dependency. In this paper, we propose the Copula Conformal Prediction algorithm for multivariate, multi-step Time Series forecasting, CopulaCPTS. We prove that CopulaCPTS has finite-sample validity guarantee. On four synthetic and real-world multivariate time series datasets, we show that CopulaCPTS produces more calibrated and efficient confidence intervals for multi-step prediction tasks than existing techniques. Our code is open-sourced at https://github.com/Rose-STL-Lab/CopulaCPTS.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors have proposed an extension of classical conformal prediction for multi-step, multivariate time series forecasting. Their work builds upon the foundations laid by Messoudi et al. without implying a significant improvement.

### Strengths
(1) The authors employ copulas to capture the relationships between different time steps in their time series analysis.

(2) Based on the experimental results, their method demonstrates a narrower predicted region compared to other approaches, suggesting enhanced efficiency.

### Weaknesses
 (1) The primary weakness of this paper lies in its novelty. The use of copulas to capture uncertainty for multi-output scenarios is not a new concept. Notably, Messoudi et al. have previously proposed a similar approach, even employing the same empirical copula. While the authors assert that their contribution is the multivariate nature of every entry, it's important to note that the nonconformity score remains scalar. Therefore, the process of conformal prediction remains largely the same as in the univariate case. The core idea of applying conformal prediction to each time step independently and then combining the results using a copula is not a significant departure from existing methods. The paper lacks a clear explanation of how the multivariate nature of the input truly differentiates it from existing approaches, especially given the scalar nonconformity score.

(2) Another notable issue pertains to data type. While this paper primarily focuses on time series, upon closer examination, it becomes apparent that the temporal aspect of the data may not be as critical as initially assumed. The dataset comprises numerous time series, and each data point within these series appears to be exchangeable with one another. This exchangeability is what enables the application of conformal prediction. Furthermore, it's crucial to differentiate this work from other studies that delve into conformal prediction methods that extend beyond exchangeability. The paper does not adequately address the limitations of assuming exchangeability, especially in the context of time series data where temporal dependencies are often crucial. The lack of discussion on how the method would perform with non-exchangeable data is a significant oversight.

### Questions
Q1: What distinguishes the proposed method from Messoudi's work, apart from the introduction of multivariate entries?

Q2: In comparison to another work[1] focusing on the multi-output version of conformal prediction that uses quantiles and can be extended to the multivariate case with the same score function, what distinguishes and contributes to this paper? I also recommend adding [1] as another baseline in the experimental part to prove the efficiency improvement.

Q3: In Equation 8, when aiming to enhance efficiency by minimizing the L1 norm of u, what is the rationale for choosing this particular norm?

Q4: Is there any typo in the loss function in the B.2 part? The loss function appears to be incorrect. Additionally, in the appendix, both equation (16) and equation (19) contain typos. The proof details regarding the validity (appendix A) are crucial; it would be beneficial to double-check this part.

[1] Feldman, S., Bates, S., & Romano, Y. (2023). Calibrated multiple-output quantile regression with representation learning. Journal of Machine Learning Research, 24(24), 1-48.

Following a thorough review of the authors' response and considering the feedback from other reviewers, I have decided to adjust the score to 6.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a method called CopulaCPTS which allows to perform conformal prediction to any multivariate multi-step forecaster, with statistical guarantees of validity. Based on the notion of copula to model the dependency between forecasted time steps, the authors prove that CopulaCPTS has finite sample validity guarantee. On both synthetic and real multivariate time series, they show that CopulaCPTS produces more efficient confidence intervals than existing techniques.

### Strengths
-- The analysis of time series is a very interesting problem in conformal prediction.

-- The experience shows that the method performs quite well.

-- The paper is clear and easy to follow.

### Weaknesses
 -- It seems that the algorithm needs a large amount of data as the calibration dataset is split a second time.

-- In the experiment, computational times are not given.

-- The standard deviations of the experiments are made with only 3 runs of the algorithm. Maybe the algorithm is very time-consuming (this should be more discuss).


Minor:

-- 'the the green'

-- Lemma ?? (eq 18)

-- In the right-hand side of equation 12, there should be a $v$ and not a $u^*$ (?).

### Questions
-- The paper uses a particular definition for the multivariate empirical quantile function (Eq. 13). Is this the only possible definition? If not, why use this one and not another?

-- In Lemma A.2, how is it possible to have an equality? (Do scores not need to be continuous?).

-- Isn't the definition of "exchangeability" in the paper rather a consequence of the "true" definition?

-- Is the "$\forall j$" in the probabilty or outside ? In the proof, Eq. (20), this is inside but in Theorem 4.1, this is outside.

-- In the experiments, the score is chosen to be an L2 norm (see, for example, step 9 of Algorithm 1). What are the implications of this choice on the results? For example, are the results very different if we use another norm?

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper studies a special setting of multi-step time series forecasting with the focus on predicting confidence intervals when a traning dataset of similar time series is available.  The authors combine conformal prediction with copula modelling in a two-step algorithm that uses a part of the training dataset for calibration of confidence intervals and can be based on any other time series forecasting model. They prove the validity of the introduced algorithm and evaluate its performance on two synthetic and two real-world datasets.

### Strengths
## Originality 
The paper presents a novel application of copula based conformal prediction explored in multi-target regression to time series setting
## Quality 
* The presented method is both theoretically grounded and practically applicable
* Authors discuss the limitations of the algorithm
* Authors showcase the performance of their algorithm from different angles including exemplar visualizations
## Clarity 
The paper is well-written and the presentation is very clear
## Significance
The paper is a continuation of an existing line of work on copula based conformal prediction into time series domain. Due to method limitations, in particular the requirements for vast calibration set size for non-parametric modelling, I would expect the paper to be of limited significance.

### Weaknesses
The paper doesn't have major weaknesses. The main downside of the presented method is its relience on large calibration dataset, which is a luxury in practical problems.

### Questions
* Equation (4) presents validity in terms of marginal distributions, while the prior work, e.g. Stankeviciute et al. (2021) uses a joint distribution. The proof of your theorem also uses the definition based on the joint distribution. Which one is correct? 
* In experiments, did you use the same training dataset for all methods or did you adapt it depending on whether the method need a calibration set? I assume you used the same one for all baselines, but it seems fair to give methods that don't rely on calibration more data.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work considers conformal prediction for multi-step time-series prediction using copula, demonstrating improved performance than existing baselines.

### Strengths
* The idea of multi-step time-series forecasting using copula CP is novel.
* Strong empirical performance on various tasks.

### Weaknesses
1. Theoretical analyses: the i.i.d. assumption is imposed on $z^i=(x^i_{1:t}, y^i_{1:t})$ for $i=1,...,n$. However, this eliminates the dependency of data over time, which is typical and expected for time-series. Hence, this seems very restrictive for the purpose of theoretical analyses, and it is important to discuss what this assumption actually imposes on the data collection process.

2. The simulation performance of CopulaCPTS seems very similar to Copula [Messoudi et al. 2021], which notably was not developed for this setting. I think this goes back to the assumption on $z^i$ being i.i.d., where the use of CopulaCPTS is not essential under the absence of temporal dependency.

3. Performance of Copula on real-data examples is not reported.

4. Given that Copula does not seem to under-perform much, I think additional comparison is needed. For example, the locally ellipsoid CP in [Ellipsoidal conformal inference for Multi-Target Regression](https://copa-conference.com/papers/COPA2022_paper_7.pdf) by [Messoudi et al. 2022]

### Questions
No additional questions are raised.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
