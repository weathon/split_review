# Implicit Dynamical Flow Fusion (IDFF) for Generative Modeling

- Decision: Reject
- Scores: 6, 5, 6, 6

## Abstract
Conditional Flow Matching (CFM) models can generate high-quality samples from a non-informative prior, but they can be slow, often needing hundreds of network evaluations (NFE). To address this, we propose Implicit Dynamical Flow Fusion (IDFF); IDFF learns a new vector field with an additional momentum term that enables taking longer steps during sample generation while maintaining the fidelity of the generated distribution. Consequently, IDFFs reduce the NFEs by a factor of ten (relative to CFMs) without sacrificing sample quality, enabling rapid sampling and efficient handling of image and time-series data generation tasks. We evaluate IDFF on standard benchmarks such as CIFAR-10 and CelebA for image generation, where we achieve likelihood and quality performance comparable to CFMs and diffusion-based models with fewer NFEs. IDFF also shows superior performance on time-series datasets modeling, including molecular simulation and sea surface temperature (SST) datasets, highlighting its versatility and effectiveness across different domains

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
1. The authors address two of the main challenges of prior CFMs:
a. During inference, CFMs require a large number of steps for high-quality/fidelity generation.
b. Due to a lack of stochasticity, CFMs may generate less diverse and detailed samples.
In essence, the authors present a modification to CFMs that combines the objective of CFM and score-based models, which have the benefits of CFMs for faster convergence during training while being able to use fewer NFEs during inference (an attribute of score-based models).

### Strengths
1. The authors present a new objective for training and sampling in CFMs that combines some aspects of stochasticity of score-based, making the NFEs lower at inference and improving sample generation quality.
2. The authors have provided thorough proof of the derivations for the formulation.
3. The authors have not only shown that their method performs better in image generation but also that it can be used in tasks of other domains like time series.

### Weaknesses
1. Figure 2 C) is a bit confusing by itself. Only after reading Algorithm 2 was the figure easy to understand. The authors can try to make the figure self-sufficient in understandability.
2. The authors compare image generation quality w.r.t sampling strategies like DDIM and DPM and show that their model achieves the best quality. 3. However, they have not compared against better strategies like EDM. A comparison against EDM would be even more insightful.
How does the method proposed by authors compare to objectives like Rectified Flow for diffusion models, which have shown the ability to converge faster?
4. Are there any limitations to the author's methods compared to traditional CFMs after introducing some stochasticity? Does the training convergence speed become slower compared to traditional CFMs? The authors have not discussed this in the main paper.

### Questions
Please refer to weakness section.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper derive framework for simulation free training for Schrödinger bridge. The proposed method trains a combined score matching loss and a denoiser loss, then samples by solving an SDE.

### Strengths
The paper tackles the important problem of reducing NFE in sampling process of flow/bridge models. The method is compared on number of different domians.

### Weaknesses
1. The proposed loss seems similar to the loss proposed in  [2] for simulation free training of Schrödinger bridges up to parametrizing the the velocity field with a denoiser.

2. In the CIFAR10 experiment the author chose to compare to DPM-solver [3] only, while there are already two follow up works DPM++ [4] and DPM-v3-solver [5] which in [5] are reported to perform better than the proposed IDFF method. Additionally, Uni-PC solver [6] is reported to perform better.

3. of less importance but I also note there seems to be some inconsistencies or typos in the Background section.
    1. In equation 5 of conditional flow matching loss it seems as if the network is dependent on the target point $x_1$ and the conditional target velocity is independent of the target point $x_1$.
    2. In the paragraph "Optimal Transport CFMs" the author state that the flow matching loss in equation 5 "is nearly intractable", this state is a bit unclear since flow matching has been used for many large scale application such as image, video, and audio generation. Additionally, it is un clear whether the authors refer to the conditional optimal transport (also know as linear scheduler)  with an independent coupling of $x_0$ and $x_0$ or with the optimal transport between source and target distribution. On the one hand, equation 5 is written for an independent coupling, and on the other hand the authors cite [1] and the OT-CFM path which to my understanding is referred to the optimal transport coupling.

### Questions
Follow up  weakness 2., what is the main contribution of the paper upon [2]?

[1] Tong, Alexander, et al. "Improving and generalizing flow-based generative models with minibatch optimal transport." arXiv preprint arXiv:2302.00482 (2023).

[2] Tong, Alexander, et al. "Simulation-free schr\" odinger bridges via score and flow matching." arXiv preprint arXiv:2307.03672 (2023).

[3] Lu, Cheng, et al. "Dpm-solver: A fast ode solver for diffusion probabilistic model sampling in around 10 steps." Advances in Neural Information Processing Systems 35 (2022): 5775-5787.

[4] Lu, Cheng, et al. "Dpm-solver++: Fast solver for guided sampling of diffusion probabilistic models." arXiv preprint arXiv:2211.01095 (2022).

[5] Zheng, Kaiwen, et al. "Dpm-solver-v3: Improved diffusion ode solver with empirical model statistics." Advances in Neural Information Processing Systems 36 (2023): 55502-55542.

[6] Zhao, Wenliang, et al. "Unipc: A unified predictor-corrector framework for fast sampling of diffusion models." Advances in Neural Information Processing Systems 36 (2024).

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a new method called IDFF, which facilitates rapid sampling without compromising sample quality and efficiently handles both image and time-series data generation tasks. The experimental results demonstrate the superiority of IDFF.

### Strengths
1. The idea presented is novel and effective, as demonstrated by the experiments.
2. The proofs provided in this paper are solid.
3. This paper also discusses the topic of time-series generation.

### Weaknesses
I believe the main drawback is that I cannot find an explanation for how this momentum term helps reduce the NFE. It appears that the motivation for designing this method is inspired by Hamiltonian Monte Carlo, which, by the way, is not mentioned in the background section. If I have overlooked this part, please let me know. If not, I recommend adding an explanation. If it is well justified, I will reconsider my score.

Here are some specific suggestions.
1. It would be beneficial to include a discussion in Section 3.1 that explicitly explains how the momentum term contributes to reducing the NFE without compromising sample quality, drawing parallels to Hamiltonian Monte Carlo's efficiency improvements. This discussion is crucial, as it constitutes a key claim of the paper.
2. Please include Hamiltonian Monte Carlo in the background section (Section 2) to provide context for readers and establish a clearer connection to the paper's approach.

### Questions
Please review the weaknesses.

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
4

### Summary
The paper introduces Implicit Dynamical Flow Fusion (IDFF) for generative modeling. IDFF learns a vector field with an additional momentum term, allowing for the use of larger step sizes during sampling without compromising the quality of the generated data, thereby accelerating the generation process. This method has demonstrated effectiveness across different domains, including image generation and time-series datasets modeling.

### Strengths
The paper proposes a novel approach for training Conditional Flow Matching (CFM), which adds an additional correction term to the vector field, allowing for larger step sizes during the sampling process, thereby accelerating sampling. The paper also conducts extensive experiments to validate the effectiveness of the method, including tasks in image generation and time-series datasets modeling.

### Weaknesses
1. Some parts of the paper need improvement in their descriptions. For instance, in Section 3.1, during the transition from $\tilde{\mathbf{v}}_t\left(\mathbf{x}_t\right)$ to $\mathbf{w}_t\left(\mathbf{x}_t\right)$, a stochastic differential equation (SDE) is introduced (in Appendix A.1.1), but this is not explicitly mentioned in the main text, nor is its purpose clearly explained. The authors claim that the ODE corresponding to $w_t$ is the Probability Flow ODE of the SDE corresponding to $\tilde{v}_t$, which implies that their marginal probability densities $p_t$ are consistent. However, it is not clear how the ODE corresponding to $w_t$ maintains the same marginal probability density $p_t$ as the ODE corresponding to $v_t$. The paper only uses the fact that $\tilde{v}_t$ converges to $v_t$ as $t$ approaches 0 and 1 (Lines 282-284) to address this issue, but this argument is insufficient, because the two time-varying vector fields being identical only at the initial and final points clearly does not guarantee the consistency of the marginal probability densities. The authors assume in Lemma 1 that $v_t$ is the vector field that generates the probability path $p_t$, which is a strong assumption that requires further justification. The connection between the proposed method and the continuity equation is not clearly established, and it is not clear how the proposed method ensures that the flow of probability neither creates nor destroys mass as it moves. 
2. Some experiments in the paper are insufficient. For example, in the image generation task, there is no comparison with some classic Conditional Flow Matching (CFM) methods, such as rectified flow[1]. Furthermore, the paper does not provide quantitative evidence to demonstrate that the proposed method does not suffer from mode collapse. The generated images in Figures 7–12 are insufficient to prove the absence of mode collapse. The paper also lacks a clear explanation of how IDFF leverages HMC to reduce NFE. The statement in lines 215–217 of the paper, “These properties lead to faster convergence to the target distribution with fewer function evaluations,” lacks direct evidence. The properties of HMC, such as “reducing random walk behavior and overcoming local energy barriers,” are not clear in terms of how they directly reduce the number of steps required to solve the ODE numerically.

### Questions
1. Could you provide a clearer explanation of the transition from $\tilde{\mathbf{v}}_t\left(\mathbf{x}_t\right)$ to $\mathbf{w}_t\left(\mathbf{x}_t\right)$ in Section 3.1 of the paper?

### Soundness
2

### Presentation
2

### Contribution
3
