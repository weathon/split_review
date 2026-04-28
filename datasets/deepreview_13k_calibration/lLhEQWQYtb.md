# Parameter Estimation of Long Memory Stochastic Processes with Deep Neural Networks

- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 3, 5

## Abstract
We present a purely deep neural network-based approach for estimating long memory parameters of time series models that incorporate the phenomenon of long-range dependence.
    Parameters, such as the Hurst exponent, are critical in characterizing the long-range dependence, roughness, and self-similarity of stochastic processes.
    The accurate and fast estimation of these parameters holds significant importance across various scientific disciplines, including finance, physics, and engineering.
    We harnessed efficient process generators to provide high-quality synthetic training data, enabling the training of scale-invariant 1D Convolutional Neural Networks (CNNs) and Long Short-Term Memory (LSTM) models.
    Our neural models outperform conventional statistical methods, even those augmented with neural networks. %extensions.
    The precision, speed, consistency, and robustness of our estimators are demonstrated through experiments involving fractional Brownian motion (fBm), the Autoregressive Fractionally Integrated Moving Average (ARFIMA) process, and the fractional Ornstein-Uhlenbeck (fOU) process.
    We believe that our work will inspire further research in the field of stochastic process modeling and parameter estimation using deep learning techniques.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces the use of efficient process generators to estimate the long range parameters of stochastic process models via a purely deep neural network approach that does not use conventional statistical methods. Background information on these time series that exhibit long range dependence is provided and some experimental results are supplied to validate the approach.

### Strengths
The main strengths of this paper are quite limited and therefore, I have spent more time in highlighting the weaknesses and shortcomings of this paper.

### Weaknesses
The major novel contribution of this work is not clearly specified at all. The paper has the following weaknesses:

1) This work seems to be an application of available process generators to generate high quality synthetic data for the fBm and other long range stochastic processes to train standard neural network models and evaluate their performance. This contribution is not sufficient for an ICLR paper. The paper does not clearly articulate why a deep learning approach is superior to existing statistical methods for parameter estimation, especially given the computational overhead associated with training deep networks. The use of synthetic data, while practical, raises questions about the generalizability of the findings to real-world time series data which may exhibit different characteristics not captured by the generators.

2) The paper reads like a background on stochastic processes exhibiting long range dependence and a small section devoted to the actual tasks implemented by the authors. It does not make for good reading. The experimental section lacks sufficient detail regarding the specific neural network architectures used, the training procedures, and the hyperparameter selection process. Without this information, it is difficult to reproduce the results or assess the robustness of the proposed approach. Furthermore, the paper does not adequately compare the performance of the deep learning approach with established statistical methods, making it hard to evaluate the practical significance of the work.

### Questions
The line of work is interesting, and I urge the authors to undertake more detailed theoretical analysis and possibly even some guarantees on estimating these long range memory parameters using recurrent neural networks and other architectures.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Fractional Brownian motion, Autoregressive Fractionally Integrated Moving Average and the fractional Ornstein-Uhlenbeck process are often used in real world. They are governed by the Hurst or differencing parameter which this paper estimates using neural networks. Having generated many different samples the network learns to output the true underlying parameter.

### Strengths
The paper is easy to follow. The baselines established in 2.4 are reasonable. The approach is simple but it is well motivated.

### Weaknesses
The scope of the problem is very limited. The paper focuses on estimating the Hurst parameter for specific fractional processes (fBm, ARFIMA, and fractional OU), but does not explore the generalizability of the approach to other stochastic processes or more complex models. The lack of a broader perspective limits the impact of the work. Perhaps showing that this approach scales to different equations at once, or having a *foundation* model for symbolic regression would significantly increase the contribution. 

The results in Figure 1 (right) are not that impressive, showing only modest accuracy in parameter estimation. The paper does not address the limitations of the model when dealing with shorter time series, which is a crucial aspect in practical applications where data is often limited. An interesting contribution would be to have a model that scales from short sequences to large ones, demonstrating robustness across different data lengths.

I believe that the novelty, significance and the results are not enough for this conference.

### Questions
.

### Soundness
3 good

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a method for fitting fractional Brownian motion using neural network sequence models. They test the method by creating many simulated datasets of varying lengths and assessing the each model's quality of fit with MSE on the observation, analysis of bias and deviation, recovery of the Hurst parameter.

### Strengths
The results seem to suggest that this method does in fact work better than traditional alternatives to model fitting on fBms and by a significant margin.

### Weaknesses
I'm not an expert in this domain, but it was very challenging to tell what was actually being proposed in this paper.

My first interpretation was that the parameters of the fBm were parameterized and then a differentiable integration method was applied to the fBM to get sample paths which were compared with ground truth paths using MSE. Then the parameters could be found by backpropagating through the integration to the parameters. But naively this would not require a sequence model, which is describe to take in a sequence and output a single scalar through mean aggregation. It's not obvious to me what the neural network is actually being used for. Is it also being used to integrate the process in some way? The presentation could be improved significantly with appropriate explanatory figures or at least a description of the actual training loss and simulation procedure.

Is it possible the baselines are too weak? They seem to be *significantly* worse than a straightforward application of sequence models. It's a little hard to believe there aren't other deep learning methods that could be used as baselines here. There is has been substantial work on learning SDEs (e.g. Patrick Kidger's work) and other stochastic processes with neural networks (e.g. neural diffusion processes) and those methods might be applicable here. 

What is the intended use case for this model? In the paper it states that the setup implies there is infinite data. I see how this is true when fitting models to synthetically generated data, but it's almost certainly not true when attempting to fit real world data. If this is meant to be used in the types of financial or scientific applications described in the introduction to the paper, why not apply it directly to those applications and evaluate how fell it performs in terms of MSE?

### Questions
Is it possible the baselines are too weak? They seem to be *significantly* worse than a straightforward application of sequence models. It's a little hard to believe there aren't other deep learning methods that could be used as baselines here. There is has been substantial work on learning SDEs (e.g. Patrick Kidger's work) and other stochastic processes with neural networks (e.g. neural diffusion processes) and those methods might be applicable here. 

What is the intended use case for this model? In the paper it states that the setup implies there is infinite data. I see how this is true when fitting models to synthetically generated data, but it's almost certainly not true when attempting to fit real world data. If this is meant to be used in the types of financial or scientific applications described in the introduction to the paper, why not apply it directly to those applications and evaluate how fell it performs in terms of MSE?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper studies the problem of estimating parameters of long stochastic processes with long-range dependencies. The proposed method generates high-quality synthetic training data to train neural networks that are able to capture the long-range dependencies in the data. The paper experimentally demonstrates the benefits of their method compared to a set of baselines.

### Strengths
The paper studies a very relevant problem of learning long-range dependencies and estimating involved parameters. The key novelty I see in this work is the relation of the dependency in the data and the estimation of parameters to capture it.

### Weaknesses
 - The paper misses significant breakthroughs in the domain of learning long-term dependencies using neural networks. In particular, [1,2,3,4] pushed the boundary on the sequence length of data that can be learned by an ML model. It is important to see how the proposed methods work compared to and in conjunction with these approaches.
- The writing of the paper can be improved. In particular, it is unclear what is new and what is just standard training methods. I think the paper would be much stronger if the contributions and relations to existing methods were stated more clearly.

### Questions
Can't the stochastic process parameters in the paper much better be characterized using the log-signature? (e.g. see Morrill et al. 2021)

### Soundness
3 good

### Presentation
1 poor

### Contribution
3 good
