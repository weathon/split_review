# Gradient-free training of recurrent neural networks

- Decision: Reject
- Scores: 5, 5, 6, 8

## Abstract
Recurrent neural networks are a successful neural architecture for many time-dependent problems, including time series analysis, forecasting, and modeling of dynamical systems.
Training such networks with 
backpropagation through time is a notoriously difficult problem because their loss gradients 
tend to explode or vanish. 
In this contribution, we introduce a computational approach to construct all weights and biases of a recurrent neural network without using gradient-based methods.
The approach is based on a combination of random feature networks and Koopman operator theory for dynamical systems.
The hidden parameters of a single recurrent block are sampled at random, while the outer weights are constructed using extended dynamic mode decomposition.
This approach alleviates all problems with backpropagation commonly related to recurrent networks.
The connection to Koopman operator theory also allows us to start using results in this area to analyze recurrent neural networks.
In computational experiments on time series, forecasting for chaotic dynamical systems, and control problems, as well as on weather data,
we observe that the training time and forecasting accuracy of the recurrent neural networks we construct are improved when compared to commonly used gradient-based methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
-  The paper proposes a training method for modeling recurrent neural networks without the use of gradient-based methods, such as backpropagation through time (BPTT), which suffers from exploding and vanishing gradients, mostly occurring in a system with chaotic dynamics. Building on concepts from random feature models, such as reservoir computing (echo-state networks), the paper proposes the random sampling of weights (W­­­ and b) in the RNN from a data-driven distribution. In addition the paper employs Koopman operator theory to find the outer weights of the RNN model, which map the current state to the next state. The Koopman operator theory maps the finite nonlinear transformation matrices (outer weights) to a linear infinite-dimensional space, where the extended dynamic mode decomposition (EDMD) method is used to find a finite-dimensional approximation of the Koopman operator. 
-  For model validation, they show some computational experiments comprising simple ODEs, such as the Van Der Pol Oscillator, chaotic dynamics (Lorenz and Rossler systems), and real-world examples involving weather data.
- Paper reports results from these computational experiments in the form of training time and error (MSE/KL Divergence). When compared to other models, such as an LSTM, ESN (echo-state network), and shPLRNN (state of the art backpropagation-based RNN), the proposed model (Sampled-RNN) achieves comparable performance, in terms of MSE and KL Divergence, and a faster training time.

### Strengths
- Interesting connection to Koopman operator.
- Interesting topic of trying to circumvent gradient based training.

### Weaknesses
 - Sampling procedure not clearly explained. (E.g. 'As we stick to networks with one hidden layer in this paper, we ignore the multilayer sampling here and direct the reader to Bolager et al. (2023) for the full sample and construction procedure for an arbitrary number of hidden layers.') The paper does not provide sufficient detail on how the weights and biases are sampled from the data-driven distribution, making it difficult to reproduce the results or understand the method's nuances. Specifically, the distributions mentioned on line 183 are not fully defined, and the connection between the data and the parameters of these distributions is not clear. This lack of clarity extends to the practical implementation of the sampling process, leaving the reader with an incomplete picture of the method.
- Paper presentation generally not clear. Hard to follow. Illustrative example: equation 1 is referred to before presented. The paper suffers from a lack of clarity and organization, making it challenging to follow the authors' line of reasoning. The introduction, in particular, is difficult to understand, and the frequent forward references to equations and concepts before they are properly introduced require the reader to engage in excessive 'detective work' to piece together the method. The lack of a clear narrative flow and the frequent jumps between ideas contribute to the overall difficulty of understanding the paper.
- How sampling approach differs from ESNs seems unclear, and a minor innovation at best. The paper does not adequately distinguish its sampling approach from existing methods like Echo State Networks (ESNs). While the authors claim that their method is data-driven, the precise mechanism by which the data influences the sampling process is not clearly explained. The connection to Koopman operator theory, while interesting, does not seem to be a significant departure from the existing literature on reservoir computing, and the paper fails to demonstrate a clear advantage over ESNs in terms of performance or computational efficiency.
- Although interesting, connection to Koopman operator theory does not seem novel. The application of Koopman operator theory to recurrent neural networks, while potentially interesting, does not appear to be a novel contribution. The paper does not adequately explain how their approach differs from existing methods for approximating the Koopman operator, especially those that use random features or dictionary learning. The connection to EDMD is also not sufficiently elaborated, and the paper does not clearly articulate the specific benefits of using EDMD in the context of their proposed method.

### Questions
N/A

### Soundness
4

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents an alternative strategy to backpropagation through time (BPTT) by using a combination of Koopman operator theory and random feature networks instead of gradient-based techniques. This novel method avoids vanishing and exploding gradient problems, and outperforms BPTT in terms of training time and accuracy in a series of empirical comparisons, including time series, forecasting, control, and weather problems.

### Strengths
1. Proof seems to be sound and theoretically correct given the assumptions stated by the authors, however i am not an very well versed with koopman operator theory and thus have provided a lower confidence score.
2. Their method (called sampled RNN) takes significantly less time to train than alternative state-of-the-art models such as ESNs, shPLRNNs, and LSTMs. Predictions from this model capture patterns in toy experiments as well as real-world data (like weather forecasting), and outperform current models (especially on problems with long horizons).

### Weaknesses
1. There is little motivation for the problem in the introduction, and the paper jumps right into formalisms. 
2. The weights and biases need to be sampled from a data-dependent probability distribution, however it's unclear how feasible this is? Specifically, the method for deriving this distribution is not sufficiently detailed, making it difficult to assess the practical applicability of the approach. The description lacks clarity on how the input data's characteristics are translated into a specific probability distribution, and how this distribution is then used to sample weights and biases. This is especially concerning for high-dimensional or complex datasets.
3. This method does not converge for controlled systems.

### Questions
1. “For completeness we have added sigma_hx as an arbitrary activation function. We choose to set sigma_hx as the identity function to let us solve for the last linear layer… other activation functions such as the logit are possible as well”. However this is not shown in the paper. Can the authors provide clarification on the effect of non-linear activations here?
2. In the weather task, the sampled RNN has a similar MSE to shPLRNNs and LSTMs for 1-day forecasting, but higher than both alternative models for week-long forecasting. However, MSE is higher than ESNs for the Rosseler system task. Can the authors provide some clarification on this?
4. Can the authors provide clarifications/results on how performance for chaotic systems might change based on how many samples are drawn for the sampled RNN (and the influence on dimensionality of the hidden layer)? 
5. The authors state: “The complexity of solving this system depends cubically on the minimum number of neurons and the number of data points (respectively, time steps). This means if both the network and the number of data points grow together, the computational time and memory demands for training grow too quickly. For BPTT, the memory requirements are mostly because many gradients must be stored for one update pass”. — can the authors provide a comparison of # of neurons vs # of time steps?
6. Can the authors provide details on how they infer the “data-dependent probability distribution” (especially for the weather data)? 
5. Additionally, can the authors expand on how weights and biases are sampled from the specific, data-dependent probability distribution (again for weather data) and how other parameters are computed using a sequence of linear equations?

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
4

### Summary
The authors propose a novel way to construct recurrent neural networks. Their approach is two stepped, where they first generates hidden weights and biases according to a data-dependent distribution, and then construct read-out parameters by approximating the dimensional Koopman operator with dynamic mode decomposition.

### Strengths
Training recurrent neural networks is notoriously hard. I am partial to the authors approach of fitting an RNN to a a dynamical system by a smart sampling of hidden parameters and Koopman operator based modeling. Particularly, I am drawn to the use of Koopman operator in the context of RNNs. 

The paper is very well written and is a nice read, and the results comparing their gradient-free approach to trained models are impressive.

### Weaknesses
It is unclear how much the Koopman operator and EDMD components contributed to model performance. Since the hidden weights initialisation schema is an application of previous work (Bolager et al. (2023)), I see the Koopman related work as the main conceptual innovation. However, based on the presented results it is hard to disentangle where improvements come from and I am not fully convinced of the added value of EDMD. I suggest the authors include two additional experiments: a. setting hidden weights randomly and learning read-out with EDMD and b. setting hidden weights based on Bolager et al. (2023) and learning read-out without EDMD. 

I am also not keen on the name and think it over-promises. Being able to train general recurrent neural networks without gradient descent or BPTT is an extremely ambitious goal, which this paper does not fulfils. As the authors explain in the (very much appreciated) limitation section, their approach does not immediately extend to RNN tasks relating to computer vision or NLP, thus the paper results are mostly regard dimensional dynamical system. I still believe their results are impressive, but the language, and specifically the title, needs to be toned down.

The impact of exploding and vanishing gradients is not made clear in this manuscript. I understand their model outperforms LSTMs and other, gradient based models based on numerical values. Could the authors make the impact of EVGP more apparent?

Can the authors include more real-world datasets? As of now, all but 1 result is simulated, and additional examples would significantly strengthen the manuscript.

### Questions
The impact of exploding and vanishing gradients is not made clear in this manuscript. I understand their model outperforms LSTMs and other, gradient based models based on numerical values. Could the authors make the impact of EVGP more apparent?

Can the authors include more real-world datasets? As of now, all but 1 result is simulated, and additional examples would significantly strengthen the manuscript.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The MS explores an alternative method for fitting recurrent neural networks, based on Koopman operator theory.  A single-layer neural network with *random weights* is used to map the state (and possibly a control input) to a higher-dimensional space, in which the dynamics are assumed to be linear.  Since the state is assumed fully observed, the low-D state at consecutive time steps can be mapped to the high-D state, and the state matrix fit with the normal equations (and similarly for the input matrix when there is a control input).  The map back to the low-dimensional state and the output matrix can be found likewise.  The intuition from Koopman operator theory is that there exists a set, possibly infinite-dimensional, of measurement functions that evolve linearly in time.  The authors shows that this method yields computationally cheap and highly accurate models of simple nonlinear systems.

### Strengths
The proposed approach fits simple nonlinear systems with high accuracy and very little computational time compared with using BPTT in RNNs.  This makes the approach a very appealing alternative for modeling and controlling such systems.  To my knowledge, the approach is novel (but see below), and open up a new perpective on random networks.

### Weaknesses
From the point of view of implementation, the manuscript's random RNNs are a fairly minor variation on echo-state networks.  Indeed, there is a large literature on ESNs and reservoir computing, and I am surprised that this variation has not previously been explored.  Can the authors confirm this?

The introduction of Koopman operator theory does provide a nice intuition about why a linear dynamical system should exist in a higher-dimensional space.  But it seems that the trade-off it enables---linearity for higher dimension---limits the scope of application of this approach: As the authors note, the matrix inversion operation (in the normal equations) is expensive, and it is cubic precisely the dimension of the (large) measurement space. This computational cost is a significant practical limitation, especially when considering that the dimensionality of the Koopman space, $M$, is a hyperparameter that must be tuned, adding another layer of complexity to the model selection process. Furthermore, the method's reliance on a single-layer neural network for the mapping to the higher-dimensional space might not be sufficient for capturing complex nonlinear dynamics, potentially requiring a much larger $M$ than what is computationally feasible.

My understanding of the theory is that, in general, not only is this space infinite-dimensional, but also there is no way to bound the number of required dimensions.  That is, M could be arbitrarily large.  Perhaps this is addressed in the proof in Appendix B, which I did not read closely.  Can the authors provide more insight here?

Finally, I found the paper somewhat hard to read.  This could be my fault, but there seem to be notational issues.  For example, near l. 139 the authors write h_t = F(h_{t-1}), and then later in the same paragraph, h_t' = F(h_t).  Is the idea that, in the first instance, h_t is the model state; where in the second instance, h_t is the *true* state (and therefore F(h_t) need not be equal to h_{t+1})?

### Questions
The authors compare against ESNs on some problems and LSTM on others.  Is there any reason for these choices?

Can the authors provide more intuition about the weight initialization, i.e., Eq. 4 and the equation for the distribution p_H?

### Soundness
4

### Presentation
3

### Contribution
3
