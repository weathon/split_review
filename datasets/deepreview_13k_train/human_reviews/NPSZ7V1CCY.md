# Zero-shot Imputation with Foundation Inference Models for Dynamical Systems

- Decision: Accept
- Scores: 5, 8, 6, 6

## Abstract
Dynamical systems governed by ordinary differential equations (ODEs) serve as models for a vast number of natural and social phenomena. In this work, we offer a fresh perspective on the classical problem of imputing missing time series data, whose underlying dynamics are assumed to be determined by ODEs. Specifically, we revisit ideas from amortized inference and neural operators, and propose a novel supervised learning framework for *zero-shot time series imputation*, through parametric functions satisfying some (hidden) ODEs. Our proposal consists of two components. First, a broad probability distribution over the space of ODE solutions, observation times and noise mechanisms, with which we generate a large, synthetic dataset of (hidden) ODE solutions, along with their noisy and sparse observations. Second, a neural recognition model that is trained *offline*, to map the generated time series onto the spaces of initial conditions and time derivatives of the (hidden) ODE solutions, which we then integrate to impute the missing data. We empirically demonstrate that *one and the same* (pretrained) recognition model can perform zero-shot imputation across 63 distinct time series with missing values, each sampled from widely different dynamical systems. Likewise, we demonstrate that it can perform zero-shot imputation of missing high-dimensional data in 10 vastly different settings, spanning human motion, air quality, traffic and electricity studies, as well as Navier-Stokes simulations — *without requiring any fine-tuning*. What is more, our proposal often outperforms state-of-the-art methods, which are trained on the target datasets.

Our pretrained model is available with the supplementary material

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a supervised learning framework for zero-shot time series imputation in dynamical systems of any dimensionality. The framework uses a synthetic data generation model based on two key assumptions: 
(1) time series with point-wise missing data have simple ODE-based interpolation solutions, and 
(2) time series with temporal missing patterns are locally simple. 
The authors introduce two neural interpolation models, FIM and FIM-l, designed for point-wise and temporal missing patterns, respectively.
The approach is evaulated over 8 datasets

### Strengths
— The proposed FIM has great zero-shot imputation performance and achieves SOTA results on multiple datasets.
— Unlike prior work, this paper proposes a zero-shot approach that can be used on processes of any dimensionality.
— The synthetic data generation model offers a general method for creating meaningful synthetic time series, which could support future research.
- The authors are honest about the limitation of the approach, especially those related to the synthetic distributions used in the analysis and setting (ODEs) as opposed to real-world data which can exhibit any (or no ) distrubution.

### Weaknesses
 - Fig 2 is difficult to read, the colors are too  similar
- The paper is too "buzzwordy", I would have  preferred more of a proper technical discussion
- The results of the proposed method are not always close to SOTA or better than SOTA

### Questions
— The FIM-l model only works for time series that follow a ‘simple’ distribution. Since existing imputation models already perform well on real-world and synthetic data, the practical value of the proposed model might be limited.
— The authors did not explain clearly how the FIM could handle processes of any dimensionality, and how the performance of the model varies with the dimensionality in practice.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces foundation model for time-series imputation, using several parametric functions of ODEs for training the model. The authors generate many synthetic noisy, irregular observations to train recognition model in offline manner.  They use combination of objective function with respect to initial value and data points to train this model. This trained model can conduct zero-shot imputation on unseen time series dataset with different dimensions. They validate their method on various different benchmarks in several domains.

### Strengths
- This paper is well written and organized. I enjoy reading this paper.
- To the best of my knowledge, this paper is novel in that this firstly introduces the zero-shot imputation of time-series with dimension free inference. 
- I think the training objective and the way they give supervision to the model is also novel.
- The experimental results are impressive, covering a wide range of datasets and scenarios enough to prove the zero-shot capability of this method. Additionally, the paper faithfully includes details for reproducing the experiments which is helpful

### Weaknesses
 - Although this model impute the data in zero-shot manner, experimental results are not that impressive in Table 2. Also, the authors use reported value from the other papers which can question whether comparison is really fair.
-  I think it would be better to include ODE based methods for the baseline considering concept of this paper.

### Questions
- I think some ablation studies for measuring the generalization capability of this model will be beneficial.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper develops a ODE-based foundation model for time series imputation. The idea is to simulate a large collection of incomplete time series including both point-wise and temporal missing patterns. A recognition model is trained to map such time series to the initial condition, and time derivatives at each time step, with both mean and log-variance prediction. The design of the recognition model is inspired by deep ONet. There is no need to fine tune the model on application-specific data. The experiments show the improvement over many sota methods specifically trained on application data.

### Strengths
1. very interesting work on time series imputation, potentially pointing out a new direction
2. design of neural recognition model is novel and interesting, albeit inspired by deepOnet. Such "borrowing" is still interesting. 
3. zero-shot performance is surprisingly good

### Weaknesses
1. as admitted by the authors, one limitation is that when the actual application does not well match the assumption of the simulation data, the performance can deteriorate. Though the paper focuses on zero-shot prediction, it will be great to discuss  possible methods for fine tuning or adaptation to specific applications. Since your training assumes the ground-truth of the initial and time derivatives of each sampled trajectories are known, and the neural recognition models directly learn to fit them, such training cannot directly apply to real dataset where these ground-truth is unknown. 
2.  The design of the neural recognition model seems not well justified, especially for the branch-net component. why do you use RNN? Why not using attention mechanism instead? Given RNN/LSTM's are replaced by attention  nearly every where, the authors should explain their rationale of such choices, either theoretically or empirically. 
3. How are the hyperparameters selected? Why using 1024 dimensional embeddings? Are this done by a rigorous validation process? If so, how?  It will be good for the authors to specify the details of hyperparmeter selection and validation process.

### Questions
see above.

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
This paper addresses the challenges of imputing missing time-series data. A framework for zero-shot time-series imputation is proposed with 1) a synthetic data generation model for sampling a set of ODE solutions and 2) a neural recognition model mapping the time series data onto parametric functions. Empirical results present improved performance of imputation compared to baseline models.

### Strengths
1. The problem of imputing time-series data is important and the idea of linking amortized inference and neural operator is interesting.
2. The methodology of the foundation inference model is well-structured.
3. Experiments were performed on the imputation of point-wise and temporal missing patterns to present the effectiveness of the proposed method.

### Weaknesses
1. I think the idea of zero-shot amortized inference framework is somewhat incremental. There have been works on amortized inference for few-shot time-series forecasting (e.g. [1] [2] [3][4]) in terms of lacking sufficient observation and learning single dynamics, where the idea of amortized inference learning the prior knowledge of dynamics is similar to the proposed method. Could the authors add a discussion about these works and the benefits of the proposed method? Also, it would be good if the authors could make a comparison of some of these methods in experiments.
2. In Equation 3, 4, and 5, do $\phi^{\theta}_i$ and $\psi^{\theta}$ share the same parameters $\theta$? Similar problem to the parameter $\psi$ in FIM model in Equation 7 and 8.

### Questions
Please find the questions in the Weaknesses section above.

### Soundness
4

### Presentation
4

### Contribution
3
