# InfoNet: An Efficient Feed-Forward Neural Estimator for Mutual Information

- Decision: Reject
- Scores: 6, 8, 3, 6

## Abstract
Estimating mutual correlations between random variables or data streams is crucial for intelligent behavior and decision-making. As a fundamental quantity for measuring statistical relationships, mutual information has been widely studied and used for its generality and equitability. However, existing methods either lack the efficiency required for real-time applications or the differentiability necessary with end-to-end learning frameworks. In this paper, we present InfoNet, a feed-forward neural estimator for mutual information that leverages the attention mechanism and the computational efficiency of deep learning infrastructures. By training InfoNet to maximize a dual formulation of mutual information via a feed-forward prediction, our approach circumvents the time-consuming test-time optimization and comes with the capability to avoid local minima in gradient descent. We evaluate the effectiveness of our proposed scheme on various families of distributions and check its generalization to another important correlation metric, i.e., the Hirschfeld-Gebelein-Rényi Maximum Correlation Coefficient. Our results demonstrate a graceful efficiency-accuracy trade-off and order-preserving properties of InfoNet, providing a comprehensive toolbox for estimating both the Shannon Mutual Information and the HGR Correlation Coefficient. We will make the code and trained models publicly available and hope it can facilitate studies in different fields that require real-time mutual correlation estimation.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper investigates the estimation of mutual information between two random variables, primarily focusing on sequences, by leveraging a neural network-based approach for efficiency. To be specific, the authors introduce the application of an attention mechanism for feed-forward predictions, trained with the MINE-based training objective. Experimental results demonstrate the effectiveness of the proposed approach with different families of distribution, as well as its promising results on real-world applications.

### Strengths
### Originality

The paper builds on two existing works: MINE [Belghazi et al.] and attention mechanism [Jaegle et al.]. The former is used as a training objective, while the latter is used to parameterize the function in MINE. The combination of two existing ideas enables efficient computation for mutual information between two sequences.


### Significance

Estimating mutual information between two high-dimensional variables is important, yet challenging for many real-world tasks. The paper proposes one way to efficiently compute MI between two sequences.

### Weaknesses
I am confused with some parts, might be due to writing or organization. Please see the following questions.

### Introduction

- 'Specifically, we want to explore whether the estimation of mutual information can be performed by a feed-forward prediction of a neural network' -- What does a feed-forward prediction mean? For MINE, we still use NNs to parameterize a function and output a scalar via NNs. Is MINE a feed-forward prediction? Please elaborate it.

- 'Moreover, each time the joint distribution changes (different sequences), a new optimization has to be performed, thus not efficient.' -- For Figure 1, which type of sequences are you considering? I don't understand 'a new optimization has to be performed'. Could you please elaborate more? Figure 1 lacks necessary contexts.

- 'This way, we transform the optimization-based estimation into a feed-forward prediction, thus bypassing the time-consuming gradient computation and avoiding sub-optimality via large-scale training on a wide spectrum of distributions.' -- For MINE, we do need to update NNs' parameters. But InfoNet also needs gradient ascent. How to understand 'bypassing the time-consuming gradient computation'?

All in all, I think the confusion is due to the lack of enough explanations. Could you please elaborate the difference between MINE and InfoNet? The same training objective is used. Both can parameterize the function via NNs, even the same NN architecture.


### Method

- To estimate mutual information between two sequences in Eq.(2), InfoNet only considers $(x_{t}, y_{t})$ at each time step? Thus, it ignores mutual information between e.g., $x_{1}$ and $y_{2}$?

- In terms of Figure 2, the difference between MINE and InfoNet is just a look-up table? I think same NN architectures could also be used in MINE?

### Questions
### Introduction

- 'Specifically, we want to explore whether the estimation of mutual information can be performed by a feed-forward prediction of a neural network' -- What does a feed-forward prediction mean? For MINE, we still use NNs to parameterize a function and output a scalar via NNs. Is MINE a feed-forward prediction? Please elaborate it.

- 'Moreover, each time the joint distribution changes (different sequences), a new optimization has to be performed, thus not efficient.' -- For Figure 1, which type of sequences are you considering? I don't understand 'a new optimization has to be performed'. Could you please elaborate more? Figure 1 lacks necessary contexts.

- 'This way, we transform the optimization-based estimation into a feed-forward prediction, thus bypassing the time-consuming gradient computation and avoiding sub-optimality via large-scale training on a wide spectrum of distributions.' -- For MINE, we do need to update NNs' parameters. But InfoNet also needs gradient ascent. How to understand 'bypassing the time-consuming gradient computation'?

All in all, I think the confusion is due to the lack of enough explanations. Could you please elaborate the difference between MINE and InfoNet? The same training objective is used. Both can parameterize the function via NNs, even the same NN architecture.


### Method

- To estimate mutual information between two sequences in Eq.(2), InfoNet only considers $(x_{t}, y_{t})$ at each time step? Thus, it ignores mutual information between e.g., $x_{1}$ and $y_{2}$?

- In terms of Figure 2, the difference between MINE and InfoNet is just a look-up table? I think same NN architectures could also be used in MINE?

---
**Update after rebuttal**: I raised the score: 5 --> 6.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors have proposed a neural network approach using the attention-based mechanism called InfoNet for mutual information estimation. Using the Donsker & Varadhan representation of the KL divergence, the parameter of the network can be optimized by maximizing an objective function (Equation 2). Furthermore, an evaluation of the efficacy of the proposed approach on the Hirschfeld-Gebelein-R´enyi (HGR) Maximum Correlation Coefficient has been considered.

### Strengths
Speeding up the previous similar work, MINE by Belghazietal., 2018 using highly parallelizable attention modules.

### Weaknesses
Overall the paper is well written, and I don't have any specific concerns. I just wanna clarify two things:

1- Is speeding up MINE using the attention architecture the only difference between InfoNet and MINE? Fundamentally, these two algorithms are similar and the same objective function using the same Donsker & Varadhan representation of the KL divergence has been used for the MI estimation. 

2 - While the authors have mentioned some motivations for evaluating the proposed approach for MMC, there are other dependence measures with computational efficiency that also enjoy the properties of MI. For instance, Energy Distance (ED) by Gábor  Székely is one of them which is a dual form of Maximum Mean Discrepancy (MMD). In particular, ED  does not require any parametric assumption about the underlying probability distribution of the data, making it easy for many statistical inference problems. It is a good idea to compare the proposed MI estimator and MCC with ED in terms of the correlation of two random variables (similar to Figure 4 ) and computational speed given the fact that ED is quite fast to use in high dimensional data.

### Questions
Please see my above comments.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper explores mutual information estimation utilizing a feedforward neural network. Unlike most methods based on the Donsker-Varadhan formula, such as MINE, there is no need to train a critic function. The author also introduces a feedforward network designed to estimate maximal correlation. These methods forego the need for per-distribution optimization, enhancing their efficiency.

### Strengths
The paper is well-written with a clear motivation. 
The idea of replacing the optimization procedure with a feedforward neural network is intriguing.

### Weaknesses
1. The author fails to specify the dimension of the data $(x, y)$. If these are scalars, the task of mutual information estimation becomes considerably simpler. There exists an extensive body of literature on classical (non-neural network) methods addressing this, which warrants consideration.

2. Mutual information estimation methods based on the Donsker-Varadhan formula, such as MINE, are primarily designed for estimating mutual information between complex real-world data (e.g., CLIP). Comparing these to simple scalar setups seems inequitable. Should the proposed method be effective with high-dimensional data, the author is advised to validate it through experimentation.

3. Relying solely on Gaussian Mixture Models for training appears to be a limited approach, raising questions about its generalizability to other distributions. To validate training based solely on Gaussian Mixtures, the author should experiment with a variety of distributions. For further reference:
Czyz et al., "Beyond Normal: On the Evaluation of Mutual Information Estimators."

4. The core concept is to approximate the critic function $\theta$ which maximizes the Donsker-Varadhan formula using a neural network. The function that truly maximizes this is given by $\log p(x,y)/p(x)p(y)$. It seems implausible that a single pretrained neural network could accomplish this for every joint distribution $p(x, y)$.

### Questions
Please see Weaknesses section.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This works present a new method for real-time mutual information (MI) estimate. The core of the method is a network that maps a population of empirical samples to the optimal function r(x,y) = p(x, y)/p(x)p(y). This optimal function is represented by a look-up table where the values of x, y are quantized into several bins (e.g. 100). To train this network, the authors use an idea similar to simulation-based inference, that they first extensively simulate data from various artificial distributions, then learn the relationship between the data population and the function r(x, y) behind. It is believed that after seeing sufficiently many artificial distributions, the network can cover the case in real world. Compared to traditional methods which learns r(x, y) from scratch, this method pre-compute r(x, y) via simulation, thereby is much faster at inference time. In addition to MI estimate, the idea can also be extended to compute Renyi's maximal correlation coefficient.

### Strengths
- **Significance**: the problem of scalable estimation of mutual information and statistical dependence is very fundamental in modern data science and machine learning, and by far there is still no method that can be both accurate (like neural network-based method) and efficient (like non-parameteric method). The method does a good job in trying to take the advantage of both worlds;
- **Novelty**: the idea of this work, to my knowledge, is very novel within the context of MI and statistical dependence estimate. While many recent works have also focused on scalable computation of mutual information and statistical dependence [1, 2, 3, 4], this work presents an orthogonal possibility. The idea of learning to map the data population to the optimal neural estimator via massive simulation is so interesting, and the way to implement this idea via attention-based network is also technically sensible. In fact, the idea of simulation-based learning is not new, particularly in the field of statistics (see e.g. [5, 6]). However, the paper is the first one to apply this idea to statistical dependence modelling; 
- **Presentation**: the paper is also mostly well-written and easy to follow. I enjoy reading the paper very much.

References:

[1] The Randomized Dependence Coefficient, NeurIPS 2017

[2] Sliced mutual information: A scalable measure of statistical dependence, NeurIPS 2021

[3] Scalable Infomin Learning, NeurIPS 2022

[4] Fairness-Aware Learning for Continuous Attributes and Treatments, ICML 2019

[5] Simulation intelligence: Towards a new generation of scientific methods, arxiv 2112.03235

[6] The frontier of simulation-based inference, PNAS 2020

### Weaknesses
 - **Limitations** (major): while very interesting, the proposed method seems only work for low-dimensional data. This is due to (a) the limitation of simulation-based learning itself, where as the dimensionality grows it becomes more and more difficult to cover diverse cases of distributions; (b) the number of grids in the lookup table grows exponentially with the dimensionality of data, making the discrete representation proposed impractical. That being said, the idea can expect to work well in e.g. 1D/2D cases;
- **Experiments** (major):  the experiments in this paper are done on synthetic dataset and one (relatively simple) real-world dataset, which is a bit disappointing compared to the interesting idea. In this regard, I think the current experiments do not really show the potential of the method developed. The synthetic task regarding maximal correlation is also not so intutitive/easy-to-understand to me compared to those done in existing works [1, 3, 4]. Why not test the power of the method in the presence of different statistical association patterns (see [1, 3, 4])?;
- **Discussion on relationship to related works**: as mentioned in the strength block above, the paper presents a new method for estimating statistical dependence in a highly efficient way. It will be ideal to have a discussion between your method and these existing works, highlighting why your method is more preferable compared to these prior works. In addition, it *may* also be nice to mention the connection of your work and the field of simulation-based intelligence due to the inherent similarity between the underlying principles. This will connect your work with the broader community;
- **Presentation** (minor): while the presentation is overall good, it was only after reading Section 3.1 and Algorithm 1 I can understand your method. In fact, Section 3.1 seems to be important description of the core training algorithm of your method. I think it would be easier to understand for readers if the authors make this part a separate section (e.g. training algorithm) rather than part of the experiments. There are also some typos/errors in the text (for example `MIN-100’ in Table 1).

### Questions
- Is it really necessary to parameterize the network to be a lookup table ? Why can’t we e.g. directly output the MI/Maximal correlation value for the input data population?
- In the experiment, why study cases with known ground-truth maximal correlation? For example, you can generate data y = f(x) + eps with known f and calculate the maximal correlation with f.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
