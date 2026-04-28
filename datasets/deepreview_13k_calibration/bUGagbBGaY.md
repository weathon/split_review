# Momentum-accelerated Diffusion Process for Faster Training and Sampling

- Decision: Reject
- Avg Score: 6.00
- Scores: 6, 5, 8, 5

## Abstract
Diffusion models (DMs) have been adopted across diverse fields with its remarkable abilities in capturing intricate data distributions. In this paper, we propose a Fast Diffusion Model (FDM) to significantly speed up DMs from a stochastic optimization perspective for both faster training and sampling. We first find that the diffusion process of DMs accords with the stochastic optimization process of stochastic gradient descent (SGD) on a stochastic time-variant problem.  
Then, inspired by momentum SGD that uses both gradient and an extra momentum to achieve faster and more stable convergence than SGD, we integrate momentum into the diffusion process of DMs. This comes with a unique challenge of deriving the noise perturbation kernel from the momentum-based diffusion process. To this end, we frame the process as a Damped Oscillation system whose critically damped state---the kernel solution---avoids oscillation and yields a faster convergence speed of the diffusion process. Empirical results show that our FDM can be applied to several popular DM frameworks, e.g., VP, VE, and EDM, and reduces their training cost by about 50% with comparable image synthesis performance on CIFAR-10, FFHQ, and AFHQv2 datasets. Moreover, FDM  decreases their sampling steps by about 3x to achieve similar performance under the same samplers. The codes are in the attached supplementary material and will be released online.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper is trying to reduce the high computational cost of training diffusion models. The authors propose a new method called the Fast Diffusion Models (FDM), which are intuitively similar to doing momentum on SGD in stochastic optimization. FDM significantly reduces the training cost, as well as the sampling cost of DMs, while maintaining or improving their image synthesis performace. Moreover, the FDM framework is general and flexible, can be adapted to several DM frameworks including VP/VE SDE, EDM. The authors verify by experiments that the performance of FDM outperforms the corresponding baseline models under most settings.

### Strengths
The algorithm framework presented in this paper is both elegantly designed and robust in terms of performance. In its comparison of the score network of different diffusion models in Table 1, their method can be summarized as modifying the expectation of the perturbation kernel to incorporate a momentum related term $e^{-\int_0^{t^{\prime}} \beta(s) \mathrm{d} s}\left(1+\int_0^{t^{\prime}} \beta(s) \mathrm{d} s\right)$. The modification is simple, possibly adaptive to more diffusion models. Additionally, it has demonstrated superior performance in benchmark tests.

### Weaknesses
The idea of aligning diffusion process with stochastic gradient descent, and adopt acceleration techniques in SGD is not entirely new.

In [1], they first proposed the critically-damped Langevin diffusion, in which they mentioned that "the velocity in CLD accelerates mixing in the diffusion process, and is equivalent to momentum in gradient descent", where they refer to [2] for the equivalence.

I understand that removing the velocity term stabilizes training and might result in better performance compared with CLD, but I wonder how to compare the understanding in [2] that critically damped Langevin = gradient descent on probability space, with the viewpoint proposed in this paper.

### Questions
- The formulation of acceleration seems to be closely related to that in the critically damped Langevin diffusion. Specifically, (15) and (19) in this paper, which corresponds to the update equation of $x$ and its velocity, corresponds to (28) in Dockhorn et al. (2021) (with $v_0 = 0$). It seems that the techniques employed in EDM, particularly the conversion of the discrete process into a continuous one, play a significant role in enhancing the efficiency of the proposed method. Can the authors elaborate more on what is most critical in the superiority of their experimental results?

- Why does the mixing speed of the forward diffusion process, transitioning from the data distribution to a Gaussian distribution, relate to the training cost?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper investigate to incorporate the momentum SGD into the diffusion process and propose a method named Fast Diffusion Model (FDM) to speed up diffusion models. Several experiments are conducted, and the results were compared against existing models to validate the effectiveness of the proposed method.

### Strengths
1. The authors not only analyze the proposed method from the theoretical apsect but also validate it empirically. The experimental results seems solid. Also, accelaration of diffusion process is a meaningful problem to investigate.
2. The paper is well-organized, and it is quite easy for readers to follow.

### Weaknesses
1. Using momentum to accelerate the optimation seems not a new idea, and the contribution is somewhat limited.
2. The theoritical analyses seem not very rigorous. See Questions part.

### Questions
In Theorem 1, the author argues that the momentum SGD is faster by comparing the errors in expectation. However, does the upper bound of SGD tight? It is not safe to draw the conclusion that SGD is slower by simply showing that the upper bound is higher than momentum SGD, epsically when we are not aware whether this upper bound is tight.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work incorporates heavy-ball momentum into the diffusion process of a diffusion model to speed up its training and inference. Specifically,  it first shows that the forward diffusion process can be viewed as an iterative scheme of stochastic gradient descent (SGD) applied to minimize a time-varying quadratic function. Motivated by this, it adds a heavy-ball-type momentum term to the forward diffusion process. To derive a concrete algorithm, it translates the discrete-time forward process into a (deterministic) critically damped ODE (noise term treated as a constant following EDM (Karras et al. [1])). By solving the ODE, it obtains a perturbation kernel, which is incorporated with other diffusion models and used in the reverse sampling process. The numerical experiments demonstrate that the proposed approach can speed up both training and inference given a certain budget.

[1] Elucidating the Design Space of Diffusion-Based Generative Models

### Strengths
- This paper is well-organized and can be easily followed. The idea of introducing momentum into the forward diffusion process seems to be novel and the contributions are made clear. 

- The experiments are promising, showing that the integration of the modified forward diffusion process (including momentum) with other models seem to work well, and the improvement in terms of training and inference speed is consistent over the baselines.

### Weaknesses
 - Some claims are not fully supported. Theorem 1 is mainly a convergence result of SGD with momentum on a quadratic function. It is unclear how this rate would imply a faster convergence speed of the modified forward diffusion process (eqn 2) despite some similarities in the iterates. Specifically, the analysis in Theorem 1 focuses on the convergence of the expected value of the iterates, while the diffusion process involves stochastic updates. The connection between the convergence rate of the expected value in the optimization setting and the convergence rate of the stochastic diffusion process is not rigorously established. This is further complicated by the fact that the noise term in eqn 2 is treated as a constant in eqn 9. The derivation leading to equation 9 appears to ignore the stochastic nature of the noise term, which is a crucial component of the diffusion process. Theorem 2 shows the convergence of the proposed diffusion process to a Gaussian distribution. However, it does not really quantify the rate of convergence, and its implications on the reverse sampling process is largely a heuristic.

- The actual algorithm (and its implementation) differs from the iterates considered in Theorem 2. Thus, the theory does not really capture the training dynamics. The theoretical analysis simplifies the diffusion process by assuming a constant beta, while the actual implementation uses a time-varying beta schedule. This discrepancy between the theoretical model and the practical implementation raises concerns about the applicability of the theoretical results to the actual training dynamics.

### Questions
Despite some weakness in the theory justifications. The proposed approach seems to open up some new directions in speeding up diffusion process by drawing ideas from the optimization perspectives.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work presents a momentum-accelerated diffusion model for faster training and sampling. Empirical results are reported by applying the proposed FDM into several diffusion models (VP, VE, EDM). Three datasets (CIFAR-10, FFHQ, and AFHQv2) are used for evaluation.

### Strengths
- It is good to evaluate the proposal under different diffusion models.

- Detailed theoretical analysis is provided.

### Weaknesses
 - The idea to connect SGD with forward process of diffusion process is interesting. However, there's a main difference between them: the gradient $g_t$ in SGD has unique relation to $x_t$ but $\epsilon_t$ is only a random variable, and is independent with $x_t$. They only share the formulation of the formula but has few connection in their meaning. I doubt under this situation, the momentum in the forward process still makes sense.

- 'following EDM, we remove the stochastic gradient noise in Eq. (2)'. Could you point out where EDM has stated this? Discarding stochasticity during forward process seems strange. If there's no stochasticity in forward process, then the equation makes no sense but only $x_T = \prod_{i=1}^{T} \alpha_t x_0$ and there's nothing for the model to learn.

- All the three datasets are somewhat small. It is necessary to evaluate FDM on large-scale dataset with higher resolution (like ImageNet 256x256).

- It is better to show more results by applying FDM into state-of-the-art diffusion model (Stable Diffusion).

### Questions
Please check the details in Weaknesses section

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
