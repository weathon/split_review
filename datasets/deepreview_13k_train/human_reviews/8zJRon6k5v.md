# Amortized Control of Continuous State Space Feynman-Kac Model for Irregular Time Series

- Decision: Accept
- Scores: 8, 8, 8, 8

## Abstract
Many real-world datasets, such as healthcare, climate, and economics, are often collected as irregular time series, which poses challenges for accurate modeling. In this paper, we propose the Amortized Control of continuous State Space Model (ACSSM) for continuous dynamical modeling of time series for irregular and discrete observations. We first present a multi-marginal Doob's $h$-transform to construct a continuous dynamical system conditioned on these irregular observations. Following this, we introduce a variational inference algorithm with a tight evidence lower bound (ELBO), leveraging stochastic optimal control (SOC) theory to approximate the intractable Doob's $h$-transform and simulate the conditioned dynamics. To improve efficiency and scalability during both training and inference, ACSSM employs amortized inference to decouple representation learning from the latent dynamics. Additionally, it incorporates a simulation-free latent dynamics framework and a transformer-based data assimilation scheme, facilitating parallel inference of the latent states and ELBO computation. Through empirical evaluations across a variety of real-world datasets, ACSSM demonstrates superior performance in tasks such as classification, regression, interpolation, and extrapolation, while maintaining computational efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The authors propose ACSSM approach for modeling irregular time series which uses continuous-discrete state space models (CD-SSMs).  The authors extend doob's-h transform to multi-marginal case and solve the problem using stochastic optimal control. The formulation leads to a  evidence lower bound (ELBO) and the authors propose a VI based loss function to model the irregular time series. 

Authors make linear approximation for the SDEs, which allows them to be able to perform simulation free estimation and exploit transformers for parallel computations. Overall, the proposed approach is faster and performs better than existing simulation based approaches, neural differential equations and other RNN based approaches tailored to handle irregular time series.

### Strengths
- The paper makes significant theoretical contributions which should be relevant other researchers in this field. 
- The proposed approach has impressive empirical results showing better results with faster training while being theoretically grounded.

### Weaknesses
One of the weakness of this work that I see is that it makes several simplifying approximations to make the solution faster/tractable. Authors already acknowledge this but it would have been nice to understand if there are any practical trade-off due to these approximation.

### Questions
- How many learnable parameters are use for each method? Was each method trained with a similar paramter budget?
- Given several approximations, how does the method perform on larger datasets ?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper introduces the Amortized Control of Continuous State Space Model (ACSSM) to handle irregularly sampled time-series. ACSSM aims to model the path measure of trajectories in a latent space, conditioned on observations in the data space. By using a latent space, the model captures a flexible and structured representation of the underlying dynamics that generate observed data, which is especially useful for irregularly sampled observations. To construct this conditional path measure, the authors introduce a novel multi-marginal Doob’s h-transform. This extension of the traditional Doob’s transform induces a class of stochastic differential equations (SDEs) that define the desired path measure in the latent space. However, simulating these SDEs directly is computationally infeasible due to the need for expensive normalization constants and conditional expectations. To overcome this challenge, the authors leverage stochastic optimal control to define a variational objective that approximates the optimal control needed to produce the conditioned dynamics. To further enhance computational efficiency, they propose working with affine linear SDEs with known Gaussian perturbation kernels, allowing simulation-free estimation of the latent trajectories and significantly speeding up the inference process.

### Strengths
The diffusion and stochastic optimal control (SOC) perspective for time-series modeling offers a compelling alternative to classical recurrent network methods, as it allows for continuous, flexible representations of latent dynamics that are suited to handle irregular timesteps.

The paper demonstrates superior performance on real-world datasets. Additionally, the efficiency gains in training time make it feasible for high-dimensional data, where classical SDE-based methods might be expensive.

### Weaknesses
The absence of a Related Work section limits the reader’s ability to understand how ACSSM compares to existing time-series modeling approaches, particularly those used in irregular time-series contexts, and those compared in the experiments section (e.g., recurrent networks, attention mechanisms, and previous SDE-based models).

The paper leans heavily on measure-theoretic concepts and complex SDE formulations, which could make it difficult for readers not specialized in these areas. More accessible explanations or visual intuitions could enhance understanding. For example, the paper introduces a multi-marginal Doob's h-transform without clearly explaining why this specific extension is necessary or how it differs from the standard Doob’s transform in the context of time-series modeling. Furthermore, the connection between the h-transform and the resulting SDEs is not made intuitive, leaving the reader to grapple with the mathematical formalism without a clear conceptual understanding.

It remains to be seen how the model scales in practice with very high-dimensional or complex latent spaces, as affine SDE simplifications may reduce the expressiveness of the dynamics in these settings. The use of affine linear SDEs with known Gaussian perturbation kernels, while computationally efficient, might limit the model's capacity to capture more intricate, non-linear dependencies in the latent space. This simplification could lead to a trade-off between computational speed and the ability to model complex real-world phenomena, especially when dealing with high-dimensional data where non-linear dynamics are often present.

### Questions
- The introduction lists the contributions, but it could benefit from more intuition to guide the reader through the chain of thought. For instance, there is no explanation of what a Feynman-Kac model is or how it facilitates sequential analysis.

- The multi-marginal Doob’s  h-transform is a central component of the approach, but its presentation lacks intuitive guidance, which is reflective of the overall style in the paper. Adding more accessible explanations would enhance understanding.

- Some sentences have syntax errors or missing words. I recommend proofreading the text to improve readability.

### Soundness
4

### Presentation
2

### Contribution
4

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The authors introduce a way of amortizing the controller of a state space model (ACSSM) to make it compatible with irregular time series. To do this, they generalize the single-marginal Doob’s $h$-transform to the multi-marginal case. To simulate the resulting continuous dynamics, they use VI to get an ELBO which is then optimized. To make this tractable, they assume that the latent dynamics are locally linear, and use a neural network to get expressive latent dynamics this way. The authors provide a theoretical analysis for this work, showing that the ELBO they obtain is tight, and then offer several experiments where this method shows improved performance over comparable baselines, for both per time classification/regression as well as sequence interpolation/extrapolation.

### Strengths
-Novel method of solving Continuous State Space model which learns linear dynamics to accommodate irregular time series. 

-Theoretical analysis for the provided algorithm, including the derivation of an ELBO used to solve the dynamics.

-Demonstration of the algorithm on real time series, showing improved performance over other methods, in both Test MSE and also compute time (<5 secs).

-Addresses limitations, such as the errors accumulated from the linear approximation.

### Weaknesses
 -Some of the background was a bit hard to follow. As someone who is relatively unfamiliar with the literature in this area, I found that some of the stuff in the methods section were not explained (it’s possible that it was common knowledge). I tried looking at the appendix for a more fleshed out explanation and i still can’t say I’m confident I understand everything going on.

-The paper argues that this method is scalable, and one thing I wish I could understand better is how this would work on environments with more complex dynamics, and possibly even partially observable environments. Did you guys try anything along this route?



### Questions
-Did you guys try using the affine linear drift function for the latent dynamics? How much better does the learned NN drift function do? 

-It is sometimes unclear where you are using the full and when you are using the history attention mechanism. It is claimed that the authors perform better than CRU because they aren’t just using past information, but also future information. However, this seems like an unfair comparison, am I misunderstanding something?

-How much does the "Parallel Computation" stuff increase the speed of inference? Is this a major contributor of why the method is so fast compared the other methods.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The author models irregular time series through a latent controlled SDE. The author first showed that the problem can be solved by a conditioned SDE, and then established the link between such conditioned SDE to a controlled SDE that optimizes a specific form of cost function. Finally, solving the HJB equation for the cost function can be obtained by simulating the controlled SDE through the Feynman-Kac theorem. The simulation was then simplified by analytically solving for the first and second moments at each timestep. Overall the paper is theoretically well-motivated with good empirical results.

### Strengths
1. The paper is theoretically motivated with novel ideas and methods. 
2. The presentation of the paper is clear. 
3. The paper provides improvements on empirical results. 
4. The paper provides clear instructions on replicating the experiment.

### Weaknesses
1. The motivation for specific implementation details is not clear

### Questions
1. Can the authors elaborate on the choice of the cost function in Eq(7)? How should one interpret this cost function? Aside from the theoretical benefit, is there any intuition on the choice of this cost function? 
2. Can the author explain the usage of full attention in this scenario? If the full attention is applied to estimate the latent dynamic, does it mean the controls $\alpha_{t_i}$ for the controlled SDE is informed by the future y-observations $o_{t_j}, j > i$? Intuitively the masked attention makes sense to me, but I am unsure about the application of full attention. 
3. It seems like the main experiments are all obtained with the full attention scheme. Can the author provide the result of those experiments using masked attention as an ablation study? When is the masked attention used?

### Soundness
3

### Presentation
3

### Contribution
3
