# Elucidating the Design Choice of Probability Paths in Flow Matching for Forecasting

- Decision: Reject
- Scores: 5, 6, 5

## Abstract
Flow matching has recently emerged as a powerful paradigm for generative modeling and has been extended to probabilistic time series forecasting in latent spaces. However, the impact of the specific choice of probability path model on forecasting performance remains under-explored. 
In this work, we demonstrate that forecasting spatio-temporal data with flow matching is highly sensitive to the selection of the probability path model. 
Motivated by this insight, we propose a novel probability path model designed to improve forecasting performance. 
Our empirical results across various dynamical system benchmarks show that our model achieves faster convergence during training and improved predictive performance compared to existing probability path models. 
Importantly, our approach is efficient during inference, requiring only a few sampling steps. 
This makes our proposed model practical for real-world applications and opens new avenues for probabilistic forecasting.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper addresses spatio-temporal forecasting using latent flow matching. In spatio-temporal forecasting, the performance of flow matching is highly dependent on the choice of the probability path model. To address this, the authors propose a new probability path model that accounts for the inherent continuity and correlation in spatio-temporal data, aiming to shorten the interpolating path.

### Strengths
1. The paper is well-written and accessible.

2. It presents a unified framework for probability path models in the context of flow matching and diffusion models, providing readers with a clearer overview of current generative model research.

### Weaknesses
1. The main contribution of the paper is a new probability path model for spatio-temporal data. However, the motivation behind this model is presented somewhat vaguely. A more formal and rigorous mathematical illustration would improve clarity.

2. There are numerous existing diffusion model-based methods for spatio-temporal data; a comparison with these methods would strengthen the paper.

3. The baselines all seem to use an encoder. An ablation study demonstrating the benefits of modeling in the latent space would be valuable (Please correct me if I missed this).

### Questions
If the encoder is trained separately from the flow matching model, what objective function is used to train the encoder?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this paper, the authors discussed the influence of probablity path choice in the context of spatial temporal forecasting. The authors conclude that different probability paths can significantly impact the accuracy and convergence of forecasting models and propose a new probability path model specifically designed for probabilistic forecasting of dynamical systems. Experiments show outperforming performance and faster convergence of the proposed method.

### Strengths
- The paper clearly and thoroughly discusses and compares the various kinds of probabilistic forecasting models, which are informative and insightful.
- The proposed probability path model learns to connect consecutive time series samples, leading to faster convergence and more stable training.
- The experiments are intensive, providing support for the proposed model.

### Weaknesses
 - Some notations are a little bit confusing. For example, do $v_t$ in algorithm 1 and $v_s$ in algorithm 2 mean the same vector field?
- The result for faster convergence and fewer sample steps comes empirically. It can benefit from more therotical derivations or insights for why the proposed probability path yileds better results.

### Questions
- How are those $s_n$ determined in the sampling algorithm?
- What is the reason for setting the highest variance at the middle and lowest variance at both the start and the end?
- Does the proposed probability path have equivalent form for other variants of diffusion models and bring the same benefits to them, such as the score matching and noise prediction objective?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors examine the impact of the specific choice of the probability path model on the forecasting performance. This is achieved in the context of flow matching, a well know principle which has not been properly examined in forecasting. There, the mappings are learned via stochastic processes, through random differential equations.

### Strengths
THe ability to perform spatio-temporal forecasting is a major strenght.
A novel theoretical framework for flow-based forecasting of spatio-temporal data. The probabilistic path is parametrized using a neural network, which results in the task to be solved in the form of second-order regression.
By taking into account inherent correlations in spatio-temporal data, the proposed model improves upon the existing models of the kind.
Extensive performance records, and comprehensive ablation study.

### Weaknesses
The main weakness is the choice of the framework. Stochastic processes and ODE based method are known to underperform for non-Gaussian distributions and non-stationary data. Especially, the gaussian probabiliy paths cannot deal with real-world data which exhibit fat-tailed distribution. The conditional probability paths and the  marginalization of distributions are rather standard in GenAI. The performance metrics are all second-rder (MSE, Frobenius norm, peak signal to noise ratio, etc), which are subobptimal given the  use of probabilistic models. Too many concepts are put together: encoders, neural networks (MLP),  regression using MSE, optimal mass transport, diffusion, ODEs, Gaussian models. Overall, the approach appears more of a "system-building" exercise rather than a deep new framework.

### Questions
The authors considered Gaussian probability paths, which are suboptimal fore real world data. Have the authors considered elliptical probability distributions and elliptical mixture models, to fix this issue
The authors used second-order performance metrics, yet the approach is probabilistic and requires probabilistic estimates rather than second-order measures. Which higher-order probabilistic metrics would the authors use in this context.

### Soundness
2

### Presentation
3

### Contribution
2
