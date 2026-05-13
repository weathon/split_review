# Generative Modeling of Regular and Irregular Time Series Data via Koopman VAEs

- Decision: Accept
- Scores: 6, 6, 5, 8

## Abstract
Generating realistic time series data is important for many engineering and scientific applications. 
Existing work tackles this problem using generative adversarial networks (GANs).
However, GANs are unstable during training, and they can suffer from mode collapse. 
While variational autoencoders (VAEs) are known to be more robust to the these issues, they are (surprisingly) less considered for time series generation. 
In this work, we introduce Koopman VAE (KoVAE), a new generative framework that is based on a novel design for the model prior, and that can be optimized for either regular and irregular training data. 
Inspired by Koopman theory, we represent the latent conditional prior dynamics using a linear map. 
Our approach enhances generative modeling with two desired features: (i) incorporating domain knowledge can be achieved by leveraging spectral tools that prescribe constraints on the eigenvalues of the linear map; and (ii) studying the qualitative behavior and stability of the system can be performed using tools from dynamical systems theory. 
Our results show that KoVAE outperforms state-of-the-art GAN and VAE methods across several challenging synthetic and real-world time series generation benchmarks. 
Whether trained on regular or irregular data, KoVAE generates time series that improve both discriminative and predictive metrics. 
We also present visual evidence suggesting that KoVAE learns probability density functions that better approximate the empirical ground truth distribution.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a variational autoencoder, Koopman VAE (KVAE), for time series data based on Koopman theory. The idea is to use a linear map to represent the prior dynamics, alongside a nonlinear coordinate transformation (the encoder) that maps the data to a linear representation. The main features of KVAE is that (i) it can incorporate domain knowledge (in the prior) by placing constraints on the eigenvalues of the linear map; (ii) the behaviour of the system can be analysed using dynamical systems theory tools. The results in the paper are promising, showing that KVAE outperforms SOTA GANs and VAEs across synthetic and real world time series generation benchmarks.

### Strengths
- Experimental results indicate strong performance compared to GANs and VAEs
- The use of linear latent dynamics simplifies the learning of the latent dynamics and allows for adding physical constraints, as indicated in section 4.3

### Weaknesses
 - A large literature of sequential VAEs for time series data generation is omitted e.g. [1,2,3,4], despite a large number of baselines being used in the experiments section. Considering there is heavy development in this area, it would be useful to compare KVAE to these methods. Specifically, the omission of recurrent VAEs, which are designed to model temporal dependencies, is a significant gap. These models often incorporate recurrent neural networks (RNNs) or LSTMs within the encoder and decoder to capture sequential patterns, which is a key aspect of time series data. Without a comparison to these methods, it is difficult to assess the true novelty and performance of KVAE in the context of existing approaches.
- More discussion in the experiments section is required on the topic of analysing "the behaviour of the system...using dynamical systems theory tools" in order to claim this as an additional feature of KVAE. The current discussion lacks concrete examples of how the learned Koopman operator can be used to extract meaningful insights about the underlying dynamics. For example, it would be useful to show how spectral analysis of the Koopman operator can reveal properties such as stability, periodicity, or quasi-periodicity of the system. Without such analysis, the claim that KVAE allows for analysis using dynamical systems theory tools remains unsubstantiated.

### Questions
N/A

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
A variant of VAE for time-series data is proposed. Technically a notable point of the proposed model lies in its prior model. It first samples a sequence $\bar{y}$ based on the outputs of a GRU, thus the dynamics of $\bar{y}$ can be nonlinear. Each $\bar{y}$ is refined to be $y$ by the linear transformation with the DMD matrix computed on the sequence of $\bar{y}$. Then there appears a regularization term to minimize the discrepancy between $y$ and $\bar{y}$, which effectively imposes "soft" linearity on the dynamics of $y$, the final output of the prior model.

### Strengths
The proposed method is reasonable, and the experiments are convincing enough to see the superiority of the method especially in terms of generation. 

The literature is nicely reviewed, and the paper is adequately placed in the relevant contexts.

I cannot really assess the novelty and the significance in terms of time-series generation. On the other hand, in terms of Koopman-operator-based neural net architectures, the proposed model seems somewhat novel yet technically straightforward.

### Weaknesses
From a purely technical point of view, the contribution might look rather incremental. So the paper should be assessed rather in the context of time-series generation models, on which I am not really an expert and thus cannot provide an accurate evaluation.

There is a GRU in the decoder part, which makes it a little difficult to assess the benefit of the Koopman-based prior model. As GRU can provide a nonlinear sequence-to-sequence transformation, it is unclear if the linear structure of $y_{1:T}$ was really beneficial when generating $x_{1:T}$. The results could be more convincing if the decoder did not have the GRU; instead, it should have had a nonlinear **pointwise** (i.e., not sequence-to-sequence) transformation such as a multilayer perceptron applied to each timestep independently. An ablation study with such a change of architecture would be highly informative.

-----

Below are minor points.

- Why do you use two different letters, $y$ and $z$, for the prior part and the posterior part, respectively? Usually in VAE papers, the latent variable is always $z$, and we just say $p(\cdot)$ for prior and $q(\cdot)$ for posterior. The current notation in the paper might also be okay, but I just wondered if there could be particular intention to use the two letters.
- Although the paper focuses on the generation capability of the models, some more experiments on the reconstruction / inference capablity could also be interesting.

### Questions
(1) As stated above, the presence of GRU in the decoder makes it a little difficult to assess the real utility of the linear structure in the prior model. Do you have some observations when you did not use a nonlinear sequence-to-sequence model in the decoder?

(2) In practice, how linear the sequence of $y$ is? In my understanding, the linearity of the dynamics of $y_{1:T}$ is not a hard constraint but rather is imposed in a soft manner as regularization. I am curious to what extent the $y$ could become linear with such a soft constraint.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
In this study, the authors propose a generative model using a variational auto-encoder. The variational auto-encoder employs the neural controlled differential equations to consider irregular time series and uses a GRU to march in time. The authors proposed to use a prior distribution with a linear transition function. It is shown that the proposed model outperforms previous models in the generation task.

### Strengths
The authors proposed to use a linear operator for the prior in the training of the variational auto-encoder. The proposed method is relatively straightforward and it is shown that the method outperforms some of the existing models for generation tasks.

### Weaknesses
The novelty of the study is limited. While the authors claim their method is based on the Koopman operator, their model is, in fact, more similar to the dynamic linear model, or Kalman filter. Also, one of the claims is that the model can take care of irregular time series, the capability is simply using a pre-existing model, neural controlled differential equations. Moreover, the manuscript is not well written. The probabilistic description and the models are not clearly defined. There are a few concerns about their model. See the comments below,

1. I know trying to optimizer both the prior and posterior in a loss function has become a trend in the deep learning community. However, theoretically speaking, trying to optimize the prior and posterior jointly in the KL loss leads to a ill-posed problem, where a unique solution does not exist. Simply put, it becomes a ping-pong game between the prior and posterior. You can easily show it by computing the parameters of the distributions in a local minima. How do you deal with this ill-posedness? 

2. What is $z_t$ and what is $y_t$? Are they different random variables? Based on the paper, it looks like both $y_t$ and $z_t$ denote the latent code, meaning that they are the same variable. I understand that the authors used $y_t$ and $z_t$ to distinguish between the prior and posterior latent code. But the way it is formulated now is not correct. For example, how do you define $KL[q(z)||p(y)]$ in eq. (3)? Shouldn't It be $KL[q(z)||p(z)]$ or $KL[q(y)||p(y)]$?

3. What is the probabilistic model for $p(x_{1:t}|z_{1:t})$? Is it a parametric distribution, e.g., normal distribution? How do you compute the log likelihood function?

4. If the modulus of the eigenvalues of $A$ is not strictly 1, i.e., $|λ| =1$, the system either grows or decays exponentially fast. It should be a hard constraint, not a soft constraint. How do you guarantee this?

5. Based on Eq (6), $y_t$ becomes deterministic once $y_{t-1}$ is observed. Then the probability distribution becomes a delta function, $p(y_t|y_{1:t}) = p(y_t|y_{t-1}) = δ (y_t - Ay_{t-1})$. How do you compute the KL divergence of the Dirac delta distribution?

6. How do you find the correct initial condition $y_0$ to represent $x_{1:T}$. As discussed by the authors, $x_{1:T}$ is transformed to $y_{1:T}$. Then, since the model is linear, once $y_0$ is determined, the rest of the sequence is determined as $y_t = A^t y_0$. Hence, it is crucial to find $y_0$ that describes $x_{1:T}$ the best. How do you choose $y_0$ and how do you guarantee that the choice of $y_0$ is the optimal?

### Questions
1. I know trying to optimizer both the prior and posterior in a loss function has become a trend in the deep learning community. However, theoretically speaking, trying to optimize the prior and posterior jointly in the KL loss leads to a ill-posed problem, where a unique solution does not exist. Simply put, it becomes a ping-pong game between the prior and posterior. You can easily show it by computing the parameters of the distributions in a local minima. How do you deal with this ill-posedness? 

2. What is $z_t$ and what is $y_t$? Are they different random variables? Based on the paper, it looks like both $y_t$ and $z_t$ denote the latent code, meaning that they are the same variable. I understand that the authors used $y_t$ and $z_t$ to distinguish between the prior and posterior latent code. But the way it is formulated now is not correct. For example, how do you define $KL[q(z)\|p(y)]$ in eq. (3)? Shouldn't It be $KL[q(z)\|p(z)]$ or $KL[q(y)\|p(y)]$?

3. What is the probabilistic model for $p(x_{1:t}|z_{1:t})$? Is it a parametric distribution, e.g., normal distribution? How do you compute the log likelihood function?

4. If the modulus of the eigenvalues of $A$ is not strictly 1, i.e., $|\lambda| =1$, the system either grows or decays exponentially fast. It should be a hard constraint, not a soft constraint. How do you guarantee this?

5. Based on Eq (6), $y_t$ becomes deterministic once $y_{t-1}$ is observed. Then the probability distribution becomes a delta function, $p(y_t|y_{1:t}) = p(y_t|y_{t-1}) = \delta (y_t - Ay_{t-1})$. How do you compute the KL divergence of the Dirac delta distribution?

6. How do you find the correct initial condition $y_0$ to represent $x_{1:T}$. As discussed by the authors, $x_{1:T}$ is transformed to $y_{1:T}$. Then, since the model is linear, once $y_0$ is determined, the rest of the sequence is determined as $y_t = A^t y_0$. Hence, it is crucial to find $y_0$ that describes $x_{1:T}$ the best. How do you choose $y_0$ and how do you guarantee that the choice of $y_0$ is the optimal?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
Although the existing GAN-based time-series generation showed good performance, they proposed a Koopman-based VAE model, citing problems such as unstable training or mode collapse. In addition, KVAE is a relatively simple model but it shows better performance in regular and irregular time-series than baseline models.

### Strengths
Originality: There was an existing model that applied the VAE model to time-series generation, but its performance was lacking. This paper showed good performance in time-series generation by applying Koopman to VAE. In addition, while the existing GAN-based model had many hyperparameters due to unstable training, KVAE is very simple and shows good performance.

Quality: In addition to various experiments conducted in previous research, the effectiveness of KAVE is clearly demonstrated through additional experiments such as physics-constrained generation.

Clarity: Very well written and easy to read.

Significance: Time-series generation suffered from many problems due to complex training. However, in this paper, it shows good performance with very easy learning.

### Weaknesses
1. There is a lack of explanation about Koopman in the Background section. In the case of this paper, the main point is Koopman, and readers may also want to know more about Koopman. Therefore, an explanation of Koopman should be in the main paper.

2. There are no results for the predictive loss term in the ablation study in Section 5.5.

Minor issues
1. For Section 5, Experiments seems to be a more appropriate word than Results.
2. It seems that 0 should be excluded from the MuJoCo results in Table 10.

### Questions
I am curious about the role of the predictive loss term. In this paper, a predictive loss term was added to the object function. Therefore, I am curious about how much the predictive loss term affects the performance that is superior to existing baseline models.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent
