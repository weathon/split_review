# Towards Self-Supervised Covariance Estimation in Deep Heteroscedastic Regression

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 5, 8, 6

## Abstract
Deep heteroscedastic regression models the mean and covariance of the target distribution through neural networks. The challenge arises from heteroscedasticity, which implies that the covariance is sample dependent and is often unknown. Consequently, recent methods learn the covariance through unsupervised frameworks, which unfortunately yield a trade-off between computational complexity and accuracy. While this trade-off could be alleviated through supervision, obtaining labels for the covariance is non-trivial.
Here, we study self-supervised covariance estimation in deep heteroscedastic regression. We address two questions: (1) How should we supervise the covariance assuming ground truth is available? (2) How can we obtain pseudo labels in the absence of the ground-truth? We address (1) by analysing two popular measures: the KL Divergence and the 2-Wasserstein distance. Subsequently, we derive an upper bound on the 2-Wasserstein distance between normal distributions with non-commutative covariances that is stable to optimize. We address (2) through a simple neighborhood based heuristic algorithm which results in surprisingly effective pseudo labels for the covariance. Our experiments over a wide range of synthetic and real datasets demonstrate that the proposed 2-Wasserstein bound coupled with pseudo label annotations results in a computationally cheaper yet accurate deep heteroscedastic regression.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Deep heteroscedastic regression models provide both a mean and covariance estimate for each input (typically assuming a Gaussian likelihood). These models are difficult to fit due to overfitting, which can lead to (co)variance estimates collapsing to zero. While recent work has primarily focused on how to perform stable training of these models through adaptations to the objective or tinkering with the training process this paper suggests using pseudo labels to learn the covariance. The authors analyze fitting the covariance with the KL divergence and the 2-Wasserstein distance while using pseudo labels that come from a local heuristic algorithm. To optimize against the 2-Wasserstein distance they derive an upper bound. On synthetic and real-world datasets this method was found to perform well in comparison to recent baselines.

### Strengths
- Different approach from much of the recent literature in the space
- Good balance of theoretical and empirical support/motivation for this method
- Will provide resources to reproduce results

### Weaknesses
 - Related works is nearly identical to [Shukla 2024](https://openreview.net/pdf?id=zdNTiTs5gU)
- Missing some recent literature: [Optimal training of Mean Variance Estimation neural networks](https://www.sciencedirect.com/science/article/pii/S0925231224007008), [Understanding Pathologies of Deep Heteroskedastic Regression](https://openreview.net/pdf?id=n5faLvrsA0)
- Somewhat unclear how this methodology is implemented
- See questions

### Questions
- This method of using local information for the variance pseudo labels seems similar in spirit to the local mini-batching in Skafte 2019. Can you comment on how these differ?
- Does this relate to kernel methods?
- What sort of architectures can this be used for? Would the mean and covariance networks share some (all up to the final layer) parameters?
- Could pseudo labels also be incorporated into other existing methods for fitting heteroscedastic regression models?
- Took a few reads a little bit confused on how training works. Is there a need for any warmup period for the mean estimate (as with other methods)? Are mean and covariance learned together from the start? Is any information for the mean relevant in the presence of pseudo labels? 
- When training against the negative log likelihood, though fits may be imperfect at least the mean and covariance will be coherent together. Are the situations where the covariance conditional on the mean is nonsensical?
- Do the usage of pseudo labels still make sense/work well when the mean model does not fit well to the data (overfit/underfit)?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper deals with heteroscedastic regression, and proposes to derive a signal from the neighborhood of a given observation to supervise the covariance. The authors derive pseudo labels for the covariance by looking at the $k$-NNs to a given observation wrt the Malanobis distance. The distance is interpreted in a probabilistic sense and used to compute the expected mean and covariance over the neighboring targets. To integrate the pseudo labels for the covariance in the loss, the authors propose an upper-bound over the 2-Wasserstein distance to be optimized, where the observed target value for each observation and the pseudo label for the covariance allow supervision of both mean and covariance.

### Strengths
- The paper deals with the relevant problem of reaching accurate and efficient estimation of both the covariance and mean parameters in deep heteroscedastic regression
- The idea of relying on the neighbourhood of a given observation to obtain a signal to use as supervision for the covariance is sensible and, while this idea was already introduced in [1], the authors propose a more computationally efficient solution. 
- The empirical results show that the method improves over alternative baselines. 
- The paper is well-structured and easy to follow. 

[1] Shukla et al. TIC-TAC: A Framework For Improved Covariance Estimation In Deep Heteroscedastic Regression, ICML 2024.

### Weaknesses
 - Claim 1, how it is formulated, is confusing to me, and it does not seem like a well-posed setup. In particular, if the true covariance is assumed to be known, it does not appear to make sense to estimate it. Also, if there's a proof, I'd suggest to use "Lemma" instead of "Claim".
- The comparison on UCI regression is in my opinion not exhaustive. Why is the method from [4] not reported on the UCI benchmark despite being SOTA? Also, from the values that the authors obtain for e.g. NLL for UCI regression, which are very different from previous works (e.g. [2, 3, 4]) but much more similar to [1], it looks like they did a similar adaptation to [1], where the authors "adapt the datasets for covariance estimation". This appears to be the case, also given the authors mention that they rescale the data to have variance of ten. Can the authors report the results on the original UCI regression dataset, as used in a large number of previous works?  This allows for transparent comparisons with a large number of previous methods. 
- The authors advertise the method as computationally efficient, e.g. compared to [1]. However, do the authors grid-search hyperparameters, like weight decay? I think it would help to make this explicit and compare on overall compute time with other state-of-the-art methods like [4] , where grid-search is not needed due to automatic regularization due to Empirical Bayes.
- Do the authors try different values of $\beta$ for the $\beta$-NLL objective? Or which value is chosen? 

### Questions
- Format of citations is often wrong (missing parenthesis). see lines 152,153. 
- Why in e.g. the UCI benchmark the comparison in terms of NLL is relegated to the Appendix, while the MSE results are in the main text? Especially in heteroscedastic regression NLL can be much indicative of overall performance.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work studies the problem of estimating the covariance of a heteroscedastic random variable, i.e., a random variable $y$ whose covariance is a function of an associated covariate $x$. (in contrast to the usual homoscedastic case, where the variance of $y$ is independent of $x$). Existing approaches tackle this problem as an unsupervised problem that minimizes a KL-like loss, which tend to be unstable or slow. In this work, the authors study how to better supervise this problem, and how to obtain sensible pseudo labels to solve a self-supervised problem instead. After proposing a simple-to-optimize bound based on the 2-Wasserstein distance, and a way of collecting pseudo-labels by assuming x-continuity of the variance, the authors show that their approach is able to model heteroscedastic cases well and significantly quicker than previous methods.

### Strengths
- **S1.** Properly modelling heteroscedastic random variables is an important and often overlooked problem.
- **S2.** The paper is generally well written, and contains enough explanations and intuitions to help the reader.
- **S3.** The experiments are convincing and show the points the authors were trying to make.
- **S4.** The arguments and derivations that precede the proposed methods are clear and convincing.

### Weaknesses
 - **W1.** The particularities specific to the heteroscedastic setting should be better stressed. For example, I understand that replacing $\mu_p$ by $y_i$ in the claim 1 is done since the variance $\Sigma_y$ depends on the sample $i$ only, but this is not clear. It would be beneficial to explicitly state that the covariance matrix $\Sigma_y$ is not constant across different data points and is a function of the input $x_i$, i.e., $\Sigma_y(x_i)$. This dependence should be made more prominent in the problem formulation. I would also double-check and explicitly write the derivations of Eq. 3, as I am not sure that they are correct. Specifically, the transition from the original Wasserstein distance to the simplified form using the trace and matrix square root needs more justification. The assumption that the means are equal needs to be explicitly stated and its implications discussed.
- **W2.** The derivations are limited to the case of Gaussian predictions. A common assumption, but not clear from the abstract. This should be explicitly stated in the abstract and introduction. The limitations of this assumption should also be discussed, particularly how the method might generalize to non-Gaussian distributions. The practical implications of this limitation should be addressed, especially in contexts where non-Gaussian noise is prevalent.
- **W3.** The experiments lack standard deviations, yet they were repeated 5 times each. This makes it difficult to assess the statistical significance of the results. Reporting only the mean values without measures of variability hinders the ability to compare the proposed method with existing ones rigorously. The absence of standard deviations also raises questions about the robustness of the method.
- **W4.** It is strange that for the last experiment the authors proposed a hybrid approach that combines 3 different methods. It would be at least nice to see what happens if the TIC parametrization is dropped. And, since speed and low-memory were a selling point of the proposed method, it would be necessary to see the penalty in time/memory that the TIC parametrization incurs. It would only be fair to compare with TIC-TAC in this experiment too, as the authors are using half of their contribution. Finally, I would love to see the proposed method applied here with the pseudo-labels taken from the input images themselves. The choice of using a hybrid approach in the final experiment, without a clear justification, makes it difficult to evaluate the true performance of the proposed method in isolation. The lack of a direct comparison with the full TIC-TAC method is also a significant oversight.
- **W5.** Some figures are hard to read. I would encourage the authors to consider using a log-scale for the y-axis. Specifically, figures where the y-axis spans several orders of magnitude would benefit from a log scale to better visualize the trends and differences between the methods.

### Questions
- **Q1.** I am struggling to understand why the W2-bound is better. Are you parametrizing $\Sigma_1^{1/2}$ directly, so you do not need to compute that square root?
- **Q2.** What is that memory consumption exactly referring to? Those values look quite large.
- **Q3.** Where are the instabilities mentioned in L482? I couldn't find them in the results.
- **Q4.** What is the TIC parametrization exactly? 
- **Q5.** The claim in the lines 210-212 is not clear to me from the results. Could you clarify it?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper under review is concerned with the problem of Deep Heteroscedastic Regression in the case where the variance is known. In the classical problem, given samples from the joint distribution of $(X,Y)$, one aims to estimate the mean and covariance matrix of the conditional distribution $Y|X$ as a function of $x$ using maximum likelihood estimation. The authors consider the case where a reference distribution is known and consider two distance measures, the KL divergence and the 2-Wasserstein metric between the distribution to be optimized (given by mean and covariance) and a distribution with known covariance. The authors then also consider the problem of how to obtain pseudo-labels in the absence of a ground truth. The paper concludes with extensive experiments, suggesting that using the 2-Wasserstein distance coubpled with preudo-label generation results in a competitive performance.

### Strengths
The paper is generally well written, and apart from a few minor mistakes indicated below, the mathematical derivations are correct and sound. The graphics are informative and well readable. The results on synthetic and real datasets look convincing, though in the absence of the code (which is due to be published) I can't verify everything.

### Weaknesses
The problem formulation is not clear. The authors could start by 1) specifying the terminology they use. For example, what is the 'target'? What is the data given and what do we want to get from the data? What are the precise assumptions on the distribution? The preliminaries section in Seitzer et al. 2022 is a good example on how to set the stage (incidentally, you could call the mean $\mu$, which seems more common). There are a few typos and some minor mistakes in the mathematical derivations (see questions below). The appendix on experiments seems to have been written a bit in a hurry (there are some typos, like capitalizing 'univariate').

In the proof of Claim 1, can you check whether (2) is correct or whether the $\ln(\cdot)$ term should be outside of the square brackets? My calculation in the univariate special case indicates that the logarithmic term should not have a factor $1/2$. This also makes the factor $2$ disappear in the conclusion.

### Questions
* Could you comment on how your approach relates to the literature on normalizing flows?
* Could you specify how the KL-divernce minimization problem is formulated? Since the KL divergence is not symmetric, it makes a difference which distribution is used as first argument and which as second. You use the term "forward KL divergence" but I don't see it defined.
* Use consistent notation for the KL divernce (on page 3 you write KL, while on page 4  you write $D_{\mathrm{KL}}$)
* In the proof of Claim 1, can you check whether (2) is correct or whether the $\ln(\cdot)$ term should be outside of the square brackets? My calculation in the univariate special case indicates that the logarithmic term should not have a factor $1/2$. This also makes the factor $2$ disappear in the conclusion.

### Soundness
3

### Presentation
3

### Contribution
2
