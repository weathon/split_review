# Quantifying Past Error Matters: Conformal Inference for Time Series

- Decision: Accept
- Avg Score: 5.50
- Scores: 8, 3, 5, 6

## Abstract
Uncertainty quantification in time series prediction is challenging due to the temporal dependence and distribution shift on sequential data. Conformal prediction provides a pivotal and flexible instrument for assessing the uncertainty of machine learning models through prediction sets. Recently, a series of online conformal inference methods updated thresholds of prediction sets by performing online gradient descent on a sequence of quantile loss functions. A drawback of such methods is that they only use the information of revealed non-conformity scores via miscoverage indicators but ignore error quantification, namely the distance between the non-conformity score and the current threshold. To accurately leverage the dynamic of miscoverage error, we propose Error-quantified Conformal Inference (ECI) by smoothing the quantile loss function. ECI introduces a continuous and adaptive feedback scale with the miscoverage error, rather than simple binary feedback in existing methods. We establish a long-term coverage guarantee for ECI under arbitrary dependence and distribution shift. The extensive experimental results show that ECI can achieve valid miscoverage control and output tighter prediction sets than other baselines.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper focuses on uncertainty quantification for time-series prediction, where exchangeability does not hold due to distribution shift and sequential dependence of data-points. Online conformal inference methods can be utilized for this task. Recent body of work on online conformal inference methods uses online gradient descent on the quantile loss function to update the thresholds of prediction sets. However, the subgradients of quantile loss function, that update the threshold at every time step, only leverage information on whether the outcome at that time-step is contained in the prediction set. The update does not include information on the magnitude of miscoverage. This paper introduces a smoothed version of quantile loss function such that the subgradient carries this information. Thus, 'Error-quantified Conformal Inference' incorporates a smooth version of feedback to update the threshold that defines prediction sets. The paper also introduces variants of smoothed ECI feedback for uncertainty quantification in time-series. Theoretical results on coverage guarantees and averaged miscoverage error are obtained without any assumptions on the data-generating distribution. Experimental results demonstrate superior performance of the ECI method in terms of reduced width of prediction sets while maintaining good coverage in comparison with other important online conformal inference baselines.

### Strengths
The idea of a smoothed version of quantile loss function to generate a more informative feedback for online gradient descent is simple and intuitive. It contributes meaningfully to improve uncertainty quantification in the online setting. 

The mathematical intuition for the idea is well-presented and contextualized within the literature on online conformal inference. 

The proposed technique produces consistent improvement in the width of prediction sets while maintaining coverage guarantees in a number of time series prediction tasks.

### Weaknesses
The authors mention difficulties in calibrating the outcomes of complex machine learning models like transformer, along with other models like deep Gaussian processes. However, the proposed techniques were evaluated on simpler time series models. It would be helpful to have some results with more complex models or discuss how the method would impact them. 

It would be helpful to discuss the tradeoffs between different ECI variants in the context of experimental results. 

For the place where the conformal PID baseline beats the proposed method, it would be helpful to explain the scorecaster term in a couple of lines so that it is more obvious why this baseline could produce a superior performance.

### Questions
For Table 3: Did the authors try to use a similar scorecaster term within the ECI update and check if that could improve over conformal PID in the Prophet model? 

Also, is there any intuition for why decay-OGD baseline beats ECI in Table 5 (Prophet model)?

### Soundness
3

### Presentation
3

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
This paper proposes Error-quantified Conformal Inference (ECI), based on the ACI approach, for online conformal inference with time series data. The key idea is to augment the online gradient descent with a smoothing term that reflects the extent of the gap between the non-conformity score and the threshold at each time step, moving beyond simple binary feedback. The main results include demonstrating coverage guarantees under a fixed learning rate, given bounded conditions for the smoothing function and non-conformity scores, and presenting a reasonable bound on the coverage gap in the case of well-designed adaptive learning rates.

### Strengths
- While the methods are relatively straightforward, they are explained clearly and precisely.
- The use of smoothing feedback to actively incorporate the degree of miscoverage during the update is a compelling idea, allowing the prediction sets to adapt well to, e.g., potential distributional shifts in time series data.
- Theoretical results are based on reasonable assumptions.

### Weaknesses
 - The authors primarily select the Sigmoid function for smoothing. However, as illustrated in Figure 2, when the extent of miscoverage exceeds a certain level, the EQ term actually decreases (which is also the case for the Gaussian error function). While the authors justify this with the goal of ensuring robustness, the rationale seems somewhat unconvincing. The decreasing EQ term for large errors could lead to instability in the adaptation process, as the feedback signal diminishes precisely when it should be most active. This behavior warrants further investigation and a more compelling justification.
- In connection with the above, if the Sigmoid function is used, the parameter $c$ can be considered a hyperparameter. Also given that Theorem 1 imposes constraints on $c$ for coverage guarantees, a more in-depth discussion on its selection, beyond the brief mention in Appendix D, would be appreciated. The impact of $c$ on the trade-off between coverage and interval width should be explored more thoroughly, including a sensitivity analysis to understand how different values of $c$ affect the performance of the method across various datasets.
- The interpretation of the miscoverage bound presented in Theorem 2 is rather ambiguous. The choice of the learning rate is a crucial aspect, yet theoretical discussion on this remains superficial. The theorem provides a bound, but it does not offer practical guidance on how to choose the learning rate to achieve the desired performance. A more detailed analysis of how the learning rate affects the tightness of the bound and the convergence properties of the algorithm is needed.
- Similarly, the experiments lack detailed discussion on how the learning rate, which is critical for the performance of each method, was chosen. The statement on Line 330, “we select the most appropriate range of learning rates $\eta$ for the respective datasets and present the best results in the tables,” is not only vague but could potentially raise concerns about data leakage. More transparency in the tuning process is needed, including the specific ranges of learning rates explored for each dataset and the criteria used to select the best one. The potential for overfitting to the validation set during hyperparameter tuning should also be addressed.
- Additionally, the choices of $h$ and $w$ in the ECI-cutoff method are not discussed. The lack of a clear rationale for these parameters makes it difficult to assess the robustness and generalizability of the method. A more detailed explanation of how these parameters influence the behavior of the ECI-cutoff method is necessary, along with guidelines for selecting appropriate values in different scenarios.

Overall, while the proposed method is straightforward and built on a solid idea, there is room for more detailed discussion regarding the rationales, interpretations of the results, and specific hyperparameter tuning.

Minor:
- Line 119: Please use \citep for Barber et al. (2021).
- Line 238: incorrect interval order
- Line 653: non-differential -> non-differentiable
- Are "coverage"s in, e.g., Figure 3, rolling averages?

### Questions
See weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work introduces Error-quantified Conformal Inference (ECI), a scheme for providing prediction intervals for time series data. Standard conformal inference requires exchangeability for statistical coverage guarantees to hold but this is generally violated in the context of time series data. Other methods to provide prediction intervals exist but many do not incorporate the magnitude of miscoverage when providing updates for future intervals. ECI utilizes this information for its updates. The authors derive a coverage guarantee for their methodology and  provide empirical results on synthetic and real-world datasets to support their claims. Compared to baselines that do not incorporate the magnitude of error they find that they are able to provide narrower intervals.

### Strengths
- General presentation of the problem is clear and this is an approach could be of interest to an active community
- Mathematical derivations are included
- Strong empirical results on synthetic and real-world datasets

### Weaknesses
 - Derivation on line 266 is difficult to read because it is inline
- Minor grammatical errors and occasional typos scattered throughout the manuscript
- See questions

### Questions
- Do the proofs for the validity of EQ-integral and EQ-cutoff need to be adjusted from the proof of EQI?
- For Assumption 1 should it also be "$\forall t$"
- Line 159: "$(1-\alpha) (1 + t^{-1})$" is not necessarily in $[0, 1]$. For instance if $t=3$ and $\alpha = 0.001$. How can this be a sample quantile?
- The EQI intervals visually are much more jagged. Could this ever result in dangerous overfitting?
- The significance of Figure 2 is unclear to me and the caption does not provide much detail. Why is this important and what is going on in this figure?
- Would error magnitude information be more useful for better or worse performing base models $f$ relative to other methods (ACI, OGD, etc)?

### Soundness
3

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
5

### Summary
The author propose an extension over the Adaptive Conformal Inference method of Gibbs and Candes, then used in the time-series realm by Zaffran et al. by incorporating in the adaptation procedure information about the magnitude of the error in the miscoverage rate.
After having stated the method and analysed its performance with some real-world applications.

### Strengths
The proposed extension is rather interesting, seems to provide reasonable results, and puts itself in a rather interesting area of conformal prediction.

### Weaknesses
- "Conformal Inference for Time Series" is an extremely broad title, which gives the impression that the authors are the first in doing something in this which is, in fact, not true.

- I found the article written in a very rough and unrefined way: I have counted at least 10 instances of missing articles (the...). Moreover, the introduction contains claims that are either too bold, or require a deeper explanation. What does it mean, for instance, that "Bayesian recurrent neural networks or deep gaussian processes are difficult to calibrate?", or, why is it meaningful to say that "quantile regression models may overfit when estimating uncertainty"

- I am seriously concerned about the "stock market" application. It seems to me that the authors aim at forecasting log stock prices, which are known to be nonstationary. In fact, the usual approach in the econometric literature is to forecast returns (i.e. log differences) which instead, tend to be a stationary time series.

- The "adaptive" CI school is only one of the possible approache to deal with the absence of indipendence between observations in Conformal Inference, in fact, https://proceedings.mlr.press/v75/chernozhukov18a.html provide a fairly interesting approach, which would be interesting to see compared to the authors proposal.

- A very recent contribution by Oliveira et al. https://jmlr.org/papers/v25/23-1553.html shows that the contribution of adaptivity procedures to be negligible. How do the authors comment about this?

### Questions
- The "adaptive" CI school is only one of the possible approache to deal with the absence of indipendence between observations in Conformal Inference, in fact, https://proceedings.mlr.press/v75/chernozhukov18a.html provide a fairly interesting approach, which would be interesting to see compared to the authors proposal.

- A very recent contribution by Oliveira et al. https://jmlr.org/papers/v25/23-1553.html shows that the contribution of adaptivity procedures to be negligible. How do the authors comment about this?

### Soundness
3

### Presentation
3

### Contribution
3
