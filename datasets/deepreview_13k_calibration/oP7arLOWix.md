# Kernel-based Optimally Weighted Conformal Time-Series Prediction

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Conformal prediction has been a popular distribution-free framework for uncertainty quantification. In this work, we present a novel conformal prediction method for time-series, which we call Kernel-based Optimally Weighted Conformal Prediction Intervals ($\texttt{KOWCPI}$). Specifically, $\texttt{KOWCPI}$ adapts the classic Reweighted Nadaraya-Watson (RNW) estimator for quantile regression on dependent data and learns optimal data-adaptive weights. Theoretically, we tackle the challenge of establishing a conditional coverage guarantee for non-exchangeable data under strong mixing conditions on the non-conformity scores. We demonstrate the superior performance of $\texttt{KOWCPI}$ on real time-series against state-of-the-art methods, where $\texttt{KOWCPI}$ achieves narrower confidence intervals without losing coverage.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors introduce KOWCPI to address the difficulties that arise from employing conformal prediction in the time series setting. In order for standard conformal prediction procedures to have valid statistical coverage guarantees the data needs to be exchangeable. However, this requirement is violated in time series data. KOWCPI uses the Reweighted Nadaraya-Watson estimator for quantile regression in the presence of dependent data to learn the distribution of residuals. Using this information, intervals can be constructed that have been theoretically shown to provide conditional coverage and empirically have been found to be narrower than other baselines while maintaining desired coverage.

### Strengths
- Authors provide a conditional coverage guarantee (much more meaningful than marginal coverage guarantee)
- Proofs are included and assumptions are clearly stated
- Strong coverage and efficiency results on intervals

### Weaknesses
 - Grammatical errors/typos scattered throughout
- Notation is rather dense. More plain language accompanying the mathematical formalism would help the reader
- Presentation of Algorithm 1 seems to be missing some pieces. In the required line should it be $(X_t, Y_t), t=1, 2, ..., T$? Variables $n, w$ are referenced but not explained earlier in the box. 
- Table 1 is a little bit confusing at first glance. Typically bold indicates "best" but in this case it only shows what the authors' method is
- See questions

### Questions
- Is quantile crossing ever an issue in $\hat Q_\beta$?
- The form of the intervals is $\hat C^\alpha_{t-1} = [\hat f(X_T) + \hat Q_{\beta^*}(\tilde X_{n+1}) , \hat f(x) + \hat Q_{1 - \alpha + \beta^*}(\tilde X_{n+1})]$. Are there cases where both quantile estimates are positive/negative and possibly leading to invalid intervals?
- Are there ever discontinuities over time? (ie the quantile estimators dramatically jump around)
- Are there any diagnostics that can be used to assess the plausibility of the assumptions? 
- How robust is this method to violation of assumptions?

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
This article studies how to use the conformal prediction framework to establish prediction intervals for time series data.
The key point of the method is: to estimate the conditional distribution of future residuals using the Reweighted Nadaraya-Watson (RNW) method. Then establish the prediction interval for the future response with mean function and estimated distribution of residual. The experiments indicate that the method produces shorter and more efficient prediction intervals while meeting coverage requirements.

### Strengths
- This article applies the conformal prediction and the RNW method to establish a prediction interval. Therefore, the proposed method is independent of specific time series models and has a broader range of applications.

- Instead of establishing prediction intervals using the quantiles $Q_{\alpha/2}$ and $Q_{1-\alpha/2}$. The method seeks a $\beta$ such that the distance between the quantiles $Q_{\alpha/2+\beta}$ and $Q_{1-\alpha/2+\beta}$ is minimized to form the prediction intervals. This approach is more effective for certain residual distributions.

- The authors consider time-series structures. In conditional coverage properties, the authors loosen the stationary condition only on strongly mixing residuals.

- The experiments indicate that the method produces shorter and more efficient prediction intervals while meeting coverage requirements.

### Weaknesses
 - The authors make a natural integration of the conformal prediction with the RNW method. However, the innovation of this approach is not particularly strong. The theoretical results primarily focus on the asymptotic accuracy of distribution estimation.

- When the dependence in the time series is strong, the dimension of $\tilde{X}$ may be large. In this case, when the data is limited, kernel estimates may not yield reliable results. Also, large $w$ leads to a low convergence rate of coverage. So it is better to include experimental results showing how coverage and interval width as $w$ increases for different sample sizes and datasets with varying degrees of temporal dependence.

-  The method establishes prediction intervals for stationary time series. Can the method be extended to handle local stationarity? Have authors considered techniques like differencing or detrending to handle non-stationarity? Additionally, please provide a more explicit discussion of the limitations of the proposed method for non-stationary data.

### Questions
-  $T$ represents the number of past residuals used to give the estimation of residual at the next time point. Can the authors give particular analyses related to $T$, such as a sensitivity analysis showing how prediction interval performance changes with different values of $T$, or a discussion of how $T$ was chosen for each dataset? 

- The method involves two important parameters: the bandwidth $h$ and the window length $w$. While the paper discusses the settings for these parameters, it is unclear whether the experimental results are sensitive to them. Additional experimental results may be needed to clarify this.

- When the dimension of $\tilde{X}$ is large, the results from kernel estimation may not be robust. In this case, is it possible to train a function to compress $\tilde{X}$, aiming to extract effective information and reduce dimensionality for $\tilde{X}$?

- In classic time series models like the ARMA-GARCH model, can the choice of $w$ or $h$ be discussed more precisely in theoretical parts as a corollary?

- Can the authors provide some experimental results on non-stationary time series?

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
3

### Summary
This paper proposes a conformal prediction method for time-series data using the Reweighted Nadaraya-Watson estimator. The authors provide non-asymptotic marginal coverage gap in Proposition 4.1 and conditional coverage guarantees under strong mixing conditions in Theorem 4.9. Its efficiency is demonstrated through experiments on three real-world datasets.

### Strengths
1. The paper is well-written and easy-to-follow.
2. The considered problem is important and well-motivated.
3. The proposed KOWCPI is efficient in various real datasets.

### Weaknesses
1. Regarding the experiments, the author only provides real datasets to demonstrate the efficiency of marginal and conditional coverage without offering information about dependency. However, I believe it would be beneficial to include additional synthetic experiments to explore different dependency structures and more comprehensively assess the scope and validity of the methods. Specifically, the experiments should include synthetic data with known and varying degrees of autocorrelation, heteroscedasticity, and non-stationarity to evaluate the robustness of the proposed method under diverse conditions. This would allow for a more granular understanding of the method's strengths and limitations.

2. While a theoretical guarantee is provided, the bound heavily depends on the estimation of weights and the strong mixing assumptions. The practical implications of these assumptions should be further explored. Specifically, the paper should discuss how sensitive the method is to violations of the strong mixing condition and how the estimation error of the weights impacts the coverage guarantees. It would be beneficial to provide a sensitivity analysis of the theoretical bounds with respect to the parameters of the mixing condition and the weight estimation process.



### Questions
1. Regarding the theoretical results, one of my concerns is could the author provide theoretical guarantees for other types of dependent time-series beyond strong mixing assumption or explain the difficulties under other dependent conditions?  

2. Related works and experiments: 
- Could the author provide more details about the benchmarks and related works to help readers unfamiliar with online conformal prediction understand why KOWCPI outperforms other methods? For example, providing a brief summary of the key differences between KOWCPI and each baseline method, highlighting why these differences might lead to improved performance may be helpful.  You can also include a table to compare the main features of each method if possible.
- Besides, the comparison methods in experiments seem to be incomplete. For example, the conformal PID in [1], the BCI in [2] and the decay-OGD in [3] should be considered. 

4. Optimal choice of window length $\omega$: 
 - Is it possible to design some strategy to determine optimal $\omega$ values that adapt to real-time changes in data volatility or distribution patterns, thereby further enhancing the KOWCPI? For example, using change point detection algorithms or online learning techniques to dynamically adjust the window length.

References:

[1] Angelopoulos A, Candes E, Tibshirani R J. Conformal PID control for time series prediction[J]. NeurIPS, 2023, 36.

[2] Yang Z, Candès E, Lei L. Bellman Conformal Inference: Calibrating Prediction Intervals For Time Series[J]. arXiv, 2024.

[3] Angelopoulos A, Barber R F, Bates S. Online conformal prediction with decaying step sizes. ICML, 2024

### Soundness
2

### Presentation
3

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
The paper presents a method to construct prediction intervals for time-series data, its main contribution being using RNW estimators for quantile regression. The paper builds upon a large body of work on the topic and offers a new algorithm under mild assumptions.

### Strengths
- The paper is very well-written and easy to follow. 
- The algorithm that leverages the RNW estimator is innovative. 
- Theory section (as far as I have understood) is correct and well-argued.
- The experiment comparison is comprehensive (includes almost all the baselines in the space. thanks for doing all this work).

### Weaknesses
 **1. Differentiation from SPCI.**

One concern I have is that this approach feels very similar to SPCI both in terms of algorithm (using an estimator to model residuals) and guarantee / proof technique (relies on the convergence property of the estimator). In terms of experiment results, KOWCPI also does not significantly outperform SPCI (in figure 2(c), there is a significant chunk of time where SPCI is more valid).

Can you add some more explanation on how your method is different from SPCI, in terms of theoretical guarantees, assumptions on data, and performance? It will not only improve clarity, but also help readers in practice know which method to choose for their specific applications.

**2. Experiment results & analysis**

I would strongly encourage the authors to add more details to their experiment results, including: 

- Add standard deviations to table 1. 
- Explain the results in table 1. What are the rationale of highlighting the first row? You should also highlight other methods that achieve the same coverage, and explain  why lower width was not highlighted. 
- Add experiments for one or more values of $\alpha$ to demonstrate consistent performance.
- Provide some qualitative examples to show why/how the KOWCPI confidence bands are better. 
- Elaborate on figure 2(d), perhaps adding a further study/analysis on weights. The remark in line 494-496 is not very convincing when only one example is provided. 

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2
