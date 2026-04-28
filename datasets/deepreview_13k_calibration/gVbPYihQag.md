# Stochastic Diffusion: A Diffusion Based Model for Stochastic Time Series Forecasting

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 6, 6, 3

## Abstract
Recent successes in diffusion probabilistic models have demonstrated their strength in modelling and generating different types of data, paving the way for their application in generative time series forecasting. However, most existing diffusion based approaches rely on sequential models and unimodal latent variables to capture global dependencies and model entire observable data, resulting in difficulties when it comes to highly stochastic time series data. In this paper, we propose a novel **Stoch**astic **Diff**usion (StochDiff) model that integrates the diffusion process into time series modelling stage and utilizes the representational power of the stochastic latent spaces to capture the variability of the stochastic time series data. Specifically, the model applies diffusion module at each time step within the sequential framework and learns a step-wise, data-driven prior for generative diffusion process. These features enable the model to effectively capture complex temporal dynamics and the multi-modal nature of the highly stochastic time series data. Through extensive experiments on real-world datasets, we demonstrate the effectiveness of our proposed model for probabilistic time series forecasting, particularly in scenarios with high stochasticity. Additionally, with a real-world surgical use case, we highlight the model's potential in medical application.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents Stochastic Diffusion (StochDiff), a novel diffusion-based model specifically designed for stochastic time series forecasting. Unlike existing models, StochDiff incorporates the diffusion process directly into each time step during the modeling stage, rather than applying it as a post-hoc operation. This design allows StochDiff to effectively capture complex temporal dependencies and the stochastic nature of high-variability time series. The model employs a data-driven, step-wise prior, with particularly strong performance demonstrated on heterogeneous clinical data.

### Strengths
​1. **Innovative Integration of Diffusion in Sequential Modeling**: The authors embed the diffusion process into each time step within the model, enhancing its ability to capture dynamic stochastic behaviors and improving its adaptability to high-variability time series data.

​2. **Data-Driven Prior Knowledge**: The model introduces a data-driven prior, allowing it to learn detailed patterns across multiple time steps and achieve more accurate, contextually relevant predictions.

​3. **Robust Experimental Support**: Extensive testing across various datasets highlights StochDiff’s high performance, especially with clinical data, showing an approximate 15% improvement in predictive accuracy over current state-of-the-art methods.

### Weaknesses
​1. **Insufficient Explanation of Fast Sampling Performance**: While the paper claims that StochDiff achieves faster sampling than other models, it lacks sufficient explanation of the underlying mechanisms or optimizations. It’s challenging to understand why the architectural choices enable faster sampling. The use of batch sizes greater than one and the application of DDIM are standard techniques in diffusion models and do not inherently provide a novel approach to faster sampling.

​2. **Reliance on Fully Connected Networks (FCN)**: The model relies exclusively on MLPs (FCNs) for encoding, which may raise concerns about robustness and scalability in complex time series settings. The FCN-only ablation does not fully justify the architecture’s solidity; for instance, the observed performance decline when removing parts of the framework might stem from the shallow network’s reduced parameter count rather than validating the effectiveness of the design. The ablation study does not adequately control for the number of parameters, making it difficult to isolate the impact of the prior learning procedure from the effect of network capacity.

​3. **Motivation for Prior Learning**: While the paper introduces a data-driven prior, the explanation of why this approach is necessary remains insufficient. The paper does not clearly articulate the limitations of using a fixed prior, nor does it provide a compelling argument for why the proposed data-driven prior is superior, especially given the added complexity.

### Questions
​1. Why is only an MLP used for prior encoding? Given the complexity of time series data, why does the architecture rely solely on MLPs (FCNs) for prior knowledge encoding? Would a more robust structure enhance the accuracy of the prior?

​2. What specific mechanisms contribute to the claimed fast sampling times? Please clarify if there are specific optimizations or architectural choices that enable StochDiff to achieve faster sampling speeds.

​3. Are the latent variables $z_t$ in the training process derived from Equation (9) or Equation (10)? The design and practical use of Equations (9) and (10) are not clearly explained, making it challenging to understand how and why these formulations are applied.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors describe a novel model (StochDiff) for probabilistic time series forecasting. It combines a sequence-to-sequence approach consisting of an LSTM network on the input and on the output side.
The hidden LSTM states $h_t$ are also used to train two additional encoders (one taking the past state $h_{t-1}$, one taking the past state $h_{t-1}$ and the current input $x_t$) via two FCNs yielding the latent state $z_t$. Both serve as input to a standard diffusion model which aims to decode the encoded/latent state $z_t$ to $x_t$  (stochastically) by conditioning on this state and are jointly.
The aggregated hidden state at the time of the last observation $h_{t_0}$ is then used to predict $z_{t>t_0}$ utilizing the LSTM. The obtained latent state is decoded by the trained diffusion model. Optionally, the samples produced by the diffusion model are clustered and aggregated to the largest cluster center by a subsequent GMM.
In experiments, the model shows competitive or slightly better performance compared to SOTA models. The authors conclude that the performance is even better in “highly stochastic” (clinical) dataset and complete the paper with a case-study on cochlear implant data.

### Strengths
The authors describe a model which contains interesting aspects. The usage of diffusion models in the proposed way is novel, also the architecture with the two encoders. The model is applied to standard datasets and an interesting non-standard case.

### Weaknesses
The building blocks of the model, the idea of RNN/sequence-to-sequence processing and the derivation of the properties of the diffusion model are pretty standard.

p1/2: "integration of the diffusion into the modelling process" vs. "posthoc": unclear, isn't it more about recurrent prediction or some other model?

p4:  The figure does not completely fit to the text and the legend (p5: "blue dash lines", the arrow from $z_t$ to $h_t$ is not clear, the "inference" arrows are not complete, green arrows are not defined etc.)

p5, eq 11: is the complicated form needed?

p6, algorithm 1. There are two $z_t$ symbols as results from the two encoders.

p14, section C: please provide information about the Attention-Net which is crucial for the performance of the diffusion process.

### Questions
p1/2: "integration of the diffusion into the modelling process" vs. "posthoc": unclear, isn't it more about recurrent prediction or some other model?

p4:  The figure does not completely fit to the text and the legend (p5: "blue dash lines", the arrow from $z_t$ to $h_t$ is not clear, the "inference" arrows are not complete, green arrows are not defined etc.)

p5, eq 11: is the complicated form needed?

p6, algorithm 1. There are two $z_t$ symbols as results from the two encoders.

p14, section C: please provide information about the Attention-Net which is crucial for the performance of the diffusion process.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper develops a diffusion based generative model for capturing time series, using a step-wise, data-driven prior specifically dedicated for stochastic time sequences modeling. In particular, the authors demonstrate the superior performance of the studied method using highly stochastic real-world time sequence data. Moreover, the proposed StochDiff can capture individual variability and make multi-step prediction, which might be unseen properties have not been realized before.

### Strengths
- Novelty:
This is the first attempt to combine diffusion processes into capturing time series, using a step-wise, data-driven prior specifically dedicated for highly stochastic time sequences modeling.

- Quality:
Overall, the paper is well written. The main techniques are well documented.

### Weaknesses
There might be some novel technical challenges that have not thoroughly discussed for modeling time series data, using diffusion generative models. I would expect to see some further discussion such as the limitations of the work in capturing highly-stochastic time series, or any other types of sequential data. I did not find other weaknesses or flaws.

### Questions
Can the authors discuss the limitations of the work in capturing highly-stochastic time series, or any other types of sequential data?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces the StochDiff model, an approach for generative time series forecasting that leverages diffusion processes and stochastic latent spaces to capture the high variability of stochastic time series data. Unlike previous methods that rely on sequential models and unimodal latent variables, StochDiff integrates a diffusion module at each time step and learns a data-driven prior, effectively modeling complex temporal dynamics and multi-modal characteristics.

### Strengths
The introduction and background sections of the paper are well-written and easy to follow, providing a clear overview of the main ideas and approach.

### Weaknesses
The methodology part of the paper is quite confusing and even contains several errors. Please refer to the "Questions" section for details.

1. Why is a Fully Connected Network (FCN) necessary in the Prior Encoder to project the sampled random variable into $ z_t $? Wouldn't it be possible to directly match the dimensions of $\hat{\mu}$ and $\hat{\sigma}$ to $z_t$? What is the rationale behind this approach?

2. "With equation (9), the prior distribution at... which enables it to (1) encode more informative representations, (2) better approximate the real data distributions, and subsequently, (3) benefit the time series data modeling." This statement lacks any actual explanation. Why does using the random variable $z$ as guidance confer these advantages? Can you provide any explanation?

3. Why is equation (10) necessary? If I understand correctly, equation (10) is ultimately used in the dual objective function. However, according to equation (9), $z_t$ should represent information from times $1:t-1$ and should not include information from $x_t$. Therefore, the posterior distribution of $z_t$ given $x_t$ expressed in equation (10) should not be used.

4. Equation (11) also has significant issues. In equation (11), the mean and variance depend on $h_{t-1}$; however, according to equation (9), $h_{t-1}$ should only depend on $z_{1:t-1}$ (as per the recursive architecture) and not on $z_t$. Hence, the correct expression for equation (11) should be $p_\theta(x_t^{n-1}|x_t^n, z_{1:t-1})$ rather than one that depends on $z_t$. Similarly, the formulations $p_\theta(x_t^{n-1}|x_t^n, z_{t})$ in equation (12) and $x_\theta(x_t^n, n, z_t)$ in equation (13) are incorrect.

5. "The prior knowledge learning is associated with the variational inference that optimizes the approximate posterior $q_z(z_t|x^0_{1:t}, z_{1:t−1})$ by minimizing the KL divergence between it and the prior." This statement is also quite confusing. First, why optimize the approximate posterior? If I understand correctly, the proposed method does not use the approximate posterior; it only uses $p_z(z_t|x^0_{1:t-1}, z_{1:t-1})$. Second, according to the principles of variational inference, we should aim to minimize the KL divergence between the approximate posterior and the true posterior, not the prior.

6. Efficiency concerns. The proposed method incorporates the diffusion process at each time step, raising a natural question about its efficiency. Given that each time-step observation involves multiple steps of the diffusion process, and with many time steps requiring the same operation, wouldn't this approach be highly inefficient?

### Questions
1. Why is a Fully Connected Network (FCN) necessary in the Prior Encoder to project the sampled random variable into $ z_t $? Wouldn't it be possible to directly match the dimensions of $\hat{\mu}$ and $\hat{\sigma}$ to $z_t$? What is the rationale behind this approach?

2. "With equation (9), the prior distribution at... which enables it to (1) encode more informative representations, (2) better approximate the real data distributions, and subsequently, (3) benefit the time series data modeling." This statement lacks any actual explanation. Why does using the random variable $z$ as guidance confer these advantages? Can you provide any explanation?

3. Why is equation (10) necessary? If I understand correctly, equation (10) is ultimately used in the dual objective function. However, according to equation (9), $z_t$ should represent information from times $1:t-1$ and should not include information from $x_t$. Therefore, the posterior distribution of $z_t$ given $x_t$ expressed in equation (10) should not be used.

4. Equation (11) also has significant issues. In equation (11), the mean and variance depend on $h_{t-1}$; however, according to equation (9), $h_{t-1}$ should only depend on $z_{1:t-1}$ (as per the recursive architecture) and not on $z_t$. Hence, the correct expression for equation (11) should be $p_\theta(x_t^{n-1}|x_t^n, z_{1:t-1})$ rather than one that depends on $z_t$. Similarly, the formulations $p_\theta(x_t^{n-1}|x_t^n, z_{t})$ in equation (12) and $x_\theta(x_t^n, n, z_t)$ in equation (13) are incorrect. 

5. "The prior knowledge learning is associated with the variational inference that optimizes the approximate posterior $q_z(z_t|x^0_{1:t}, z_{1:t−1})$ by minimizing the KL divergence between it and the prior." This statement is also quite confusing. First, why optimize the approximate posterior? If I understand correctly, the proposed method does not use the approximate posterior; it only uses $p_z(z_t|x^0_{1:t-1}, z_{1:t-1})$. Second, according to the principles of variational inference, we should aim to minimize the KL divergence between the approximate posterior and the true posterior, not the prior. 

6. Efficiency concerns. The proposed method incorporates the diffusion process at each time step, raising a natural question about its efficiency. Given that each time-step observation involves multiple steps of the diffusion process, and with many time steps requiring the same operation, wouldn't this approach be highly inefficient?

### Soundness
1

### Presentation
2

### Contribution
2
