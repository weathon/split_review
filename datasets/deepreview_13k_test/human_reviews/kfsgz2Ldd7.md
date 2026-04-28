# Score-Based Variational Inference for Inverse Problems

- Decision: Reject
- Scores: 3, 6, 6, 6, 6

## Abstract
Existing diffusion-based methods for inverse problems sample from the posterior using score functions and accept the generated random samples as solutions. In applications that posterior mean is preferred, we have to generate multiple samples from the posterior which is time-consuming. In this work, by analyzing the probability density evolution of the conditional reverse diffusion process, we prove that the posterior mean can be achieved by tracking the mean of each reverse diffusion step. Based on that, we establish a framework termed reverse mean propagation (RMP) that targets the posterior mean directly. We show that RMP can be implemented by solving a variational inference problem, which can be further decomposed as minimizing a reverse KL divergence at each reverse step. We further develop an algorithm that optimizes the reverse KL divergence with natural gradient descent using score functions and propagates the mean at each reverse step. Experiments demonstrate the validity of the theory of our framework and show that our algorithm outperforms state-of-the-art algorithms on reconstruction performance with lower computational complexity in various inverse problems.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors propose Reverse Mean Propagation (RMP) as a new framework that leverages score-based variational inference to solve inverse problems by tracking the posterior mean at each step of the reverse diffusion process. RMP is claimed to be more computationally efficient than traditional diffusion-based methods that rely on generating multiple samples from the posterior, as it can achieve the posterior mean directly.

### Strengths
The topic of solving inverse problems with score-based models is interesting.

### Weaknesses
* The posterior mean is not the only relevant quantity; access to
  samples from the posterior distribution also enables uncertainty
  quantification. This work provides only an approximation to the mean,
  sacrificing sample generation for computational efficiency, which may
  not even be fully realized unless unjustified approximations are made
  (see more below).

* While RMP aims to reduce complexity relative to sampling methods, it still requires nested optimization loops and numerous neural network evaluations.

* The method relies heavily on approximating the likelihood score, $\nabla_{x_k} \log p(y | x_k)$, which is acknowledged as "hard to handle in general." The chosen approximation—replacing the likelihood score with the score at the MMSE estimate of $x_0$—introduces an error quantified by Jensen's Gap.


* The performance of RMP depends on multiple hyperparameters, such as step sizes and the likelihood score balancing parameter. Sensitivity to these hyperparameters and their generalizability across datasets and inverse problems remain unclear. 

* Algorithm 2 uses a fixed-precision update to avoid computing the Hessian further introducing approximation errors.

* The authors note that the reverse conditional probability is strictly Gaussian only as $\Delta t \to 0$, an assumption that may not hold in practice, introducing further errors.

* In high-dimensional settings, computing the MMSE estimate of $x_0$ at each step, as required for likelihood score approximation, can be computationally intensive. The manuscript lacks a detailed analysis of RMP’s computational cost in high-dimensional scenarios.

### Questions
See above

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper tackles the challenge of solving inverse problems using diffusion models and introduces a framework called Reverse Mean Propagation (RMP) to recover the posterior mean of the latent variable ${\bf x} _0$ given the measurement ${\bf y}$. RMP is based on the insight that the reverse conditional distributions $p({\bf x} _k|{\bf x} _{k+1},{\bf y})$ in diffusion models are approximately Gaussian, with their mean and variance depending on the unknown quantities $\mathbb{E}({\bf x} _0|{\bf y})$ and ${\rm Cov}({\bf x} _0|{\bf y})$. The paper proposes a Gaussian variational inference approach to learn the reverse conditional mean and approximate the reverse conditional variance.

### Strengths
The paper focuses on predicting $\mathbb{E}({\bf x} _0|{\bf y})$ rather than sampling from the distribution $p({\bf x} _0|{\bf y})$, which sets it apart from most existing works. The Gaussian VI approach for learning the reverse conditional mean is innovative, and the experimental results presented are also compelling. The writing is clear, and the mathematical derivations are solid. Overall, this paper is of high quality and meets the standards of the ICLR conference.

### Weaknesses
The introduction section would benefit from a concise summary of the main contributions. Additionally, a detailed literature review of existing methods for inverse problems, particularly those related to VI, should be included to highlight the novelty of this approach.

In the experiments, the proposed method RMP is compared with DPS, MCG, DDRM, and $\Pi$GDM. While RMP demonstrates strong performance against these baselines, it is important to note that most of them (DPS, MCG, and $\Pi$GDM) do not require additional training, and can be used in a plug-and-play manner with any pretrained diffusion model and suitable measurement process ${\bf y}={\cal A}({\bf x} _0)+{\bf w} _0$. However, RMP incurs extra overhead due to the stochastic NGD update for Gaussian VI. Furthermore, in section 5.3, the comparison of NFE between RMP and DPS focuses on inference time, and does not account for training complexity, which may render the comparison a little bit unfair.

### Questions
1. I'm trying to understand proposition 1 from a continuous perspective, as it derives the continuous-time limit of the distribution $p({\bf x} _k|{\bf x} _{k+1},{\bf y})$. However, it appears that these two approaches differ significantly.

   Consider the forward process $d{\bf x} _t=\sqrt{\frac{d}{dt}(\sigma _t^2)}d{\bf B} _t$, $t\in[0,1]$, ${\bf x} _0\sim p({\bf x} _0|{\bf y})$. We know that $p({\bf x} _t|{\bf x} _0)={\cal N}({\bf x} _0,\sigma _t^2{\bf I})$, and the marginal distribution of ${\bf x} _t$ is $p _t({\bf x} _t|{\bf y})$. The backward process is $d{\bf x} _t=-\frac{d}{dt}(\sigma _t^2)\nabla\log p _t({\bf x} _t|{\bf y})dt+\sqrt{\frac{d}{dt}(\sigma _t^2)}d{\bf B}^\gets _t$, where ${\bf B}^\gets _t$ is a backward BM. If initialized at ${\bf x} _1\sim p _1({\bf x} _1|{\bf y})$, then ${\bf x} _0\sim p _0({\bf x} _0|{\bf y})$. We can express the score as $\nabla\log p _t({\bf x} _t|{\bf y})=\frac{1}{\sigma _t^2}(\mathbb{E}({\bf x} _0|{\bf x} _t,{\bf y})-{\bf x} _t)$, and thus the discretization scheme can be written as ${\bf x} _{t-\Delta t}\approx {\bf x} _t+\frac{\sigma _t^2-\sigma _{t-\Delta t}^2}{\sigma _t^2}(\mathbb{E}({\bf x} _0|{\bf x} _t,{\bf y})-{\bf x} _t)+{\cal N}(0,(\sigma^2 _t-\sigma^2 _{t-\Delta t}){\bf I})$. (I hope my calculation is correct.) 
   

   Compare this with proposition 1, the posterior variance is independent of ${\bf y}$, while the posterior mean involves $\mathbb{E}({\bf x} _0|{\bf x} _t,{\bf y})$ rather than $\mathbb{E}({\bf x} _0|{\bf y})$. Could you clarify the differences and connections between these two approaches?

2. I noticed an extra term $N\Lambda _k$ in line 2 of equations 17 and 18, which does not appear in equation 16. Is this an error? Additionally, since we are performing gradient descent, the plus and minus signs in equation 17 seem incorrect after the "=" sign.

3. Minor comments:

- Please use parenthetical citation `\citep{}` instead of `\cite{}` when the authors' names aren't part of the text. For example, the first sentence should be "Diffusion models (Sohl-Dickstein et al. 2015; Song & Ermon 2019; Ho et al. 2020; Song et al. 2020a; Rombach et al. 2022) have shown impressive performance for image generation."

- In proposition 1, the reverse conditional should be *approximately* Gaussian when $\Delta t\to0$. $k=0\cdots T-1$ should be $k=0,\cdots,T-1$.

- In line 234: $p({\bf x} _k|{\bf x} _{k+1:T},{\bf y})$ should be $p({\bf x} _k|{\bf x} _{k+1},{\bf y})$.

- Throughout the paper, $KL$ should be ${\rm KL}$, and $Cov$ should be ${\rm Cov}$.

- In equation 15, $\nabla _{{\bm\Lambda} _k}$ should be $\nabla _{{\Lambda} _k}$.

- In line 287, there is no need to mention $\Lambda _k=v _k^{-1}$.

- In algorithm 2, the roles of $T _s$ and $T _{in}$ need to be stated.

- I suggest the author(s) replace figures 1 and 2 with higher resolution versions, especially the bottom-right in figure 2.

- The title of section 6 has a spelling error.

### Soundness
3

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
This paper introduces a novel framework called Reverse Mean Propagation (RMP) for estimating the posterior mean. The framework involves tracking the mean and covariance in the evolution of the conditional reverse diffusion process.
This is achieved by minimizing the reverse KL divergence at each step through a variational inference with stochastic natural gradient descent.
In experiments, the authors validate their method on image reconstruction tasks. The results show that RMP outperforms than the existing baselines, including DPS and MCG methods.

### Strengths
S1: The paper proposes a novel framework, Reverse Mean Propagation, which significantly reduces the complexity of estimating the posterior mean compared to other methods that rely on generating samples from the posterior distribution.

S2: The details of each component of the RMP algorithm are well presented, including the reverse mean updates and estimation using stochastic natural gradient descent. The discussion on estimating the trace of the Hessian matrix $\nabla^2_{x_k} \log p_k$ is also clear and informative.

### Weaknesses
W1: In line 148, the authors discuss the variance preserving (VP) diffusion model and the variance exploding (VE) diffusion model, mentioning their different training approaches. It would be helpful to explain that the VP scheme, like the VE scheme, is also equivalent to learning the score functions of perturbed data distributions[1]. Clarifying this point could provide more comprehensive background information.

W2: In Table 2, the FID results appear inconsistent with the previously reported results of the DPS method in Table 4 of [2].

W3: The comparison methods in the paper are relatively limited. Including additional baselines, such as PnP-ADMM [3], would be beneficial. 

W4: As a specific type of VI method, there is limited discussion on previous works that directly estimate the posterior mean. 

[1] Song, Yang, et al. "Score-based generative modeling through stochastic differential equations." ICLR 2021.

[2] Chung, Hyungjin, et al. "Diffusion posterior sampling for general noisy inverse problems." ICLR 2023.

[3] Chan, Stanley H., Xiran Wang, and Omar A. Elgendy. "Plug-and-play ADMM for image restoration: Fixed-point convergence and applications." IEEE Transactions on Computational Imaging 3.1 (2016): 84-98.

### Questions
Q1: In line 703, the authors present the estimated form $p(x_k|y) \approx \mathcal{N}(x_k; \mathbb{E}\_{p(x_0|y)}[x_0], (\sigma_k^2 I + C_{x_0}))$. 
However, $x_k|y$ is not generally an asymptotically Gaussian distribution when $\Delta t \rightarrow 0$. Could the authors provide further clarification on this estimation?

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
This paper presents a score-based variational inference method for inverse problems. The key ingredient is a framework called reverse mean propogation (RMP) that targets the posterior mean directly. The authors show that RMP can be implemented by solving a variational problem which decomposes into independent sub variational problems at each reverse step. Natural gradient descent is used for learning variational parameters. The authors show that the proposed algorithm outperforms state-of-the-art algorithms in various inverse problems.

### Strengths
1. The paper is clearly written and estimating the posterior mean directly seems new for score-based inverse problems.
2. The authors show that in the limit of continous time, the end point of reverse mean propogation would recover the exact posterior mean, with different conditions for VP and VE diffusions respectively.
3. Natural gradient descent is employed for optimization.
4. The authors have evaluated their algorithms thoroughly, and also conducted an ablation study on the complexity vs performance.

### Weaknesses
1. Although the derivation of the proposed algorithm seems right, there are lots of approximations that would damage the validity of the methods. For example, proposition 1 and theorem 1 only hold in the continuous limit, not sure how accurate it would be, especially when the step size is large (or equivalently, $T$ is small). Can the authors provide an empirical analysis or theoretical bounds on the approximation error for finite T? For example, can the authors show how the algorithm's performance changes as T varies, to demonstrate how closely it approaches the continuous limit in practice?

2. It seems that the proposed method also uses the same approximation as in DPS for the likelihood score (section 4.3). As this is the main reason that DPS would perform poorly, can the author explain why your algorithm would perform better than DPS? any intuition? Can the authors provide a detailed comparison or ablation study isolating the impact of the likelihood score approximation versus other aspects of their approach?

3. There are some hyperparameters (i.e., $\gamma_k$ in equation (22) and the stepsize $s_1$) that would be crucial for the performance. The paper lacks ablation studies on it. Can the authors conduct and report sensitivity analyses for $\gamma_k$ and $s_1$, showing how performance metrics change across reasonable ranges for these parameters?

### Questions
1. It seems that the overall complexity is the product of the number of the outer loops $T$ and the number of the inner loops $T_{in}$. Would different choices of these numbers affect the performance? For example, one can make $T$ larger, in the hope that the correspondng posterior $p(x_k|x_{k+1},y)$ would become easier to approximate so that the convergence would be faster for VI and $T_{in}$ can therefore be smaller.

2. It seems that VE-RMP tends to require smaller $T$, can the author explain it?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper targets the estimating the posterior mean in the inverse problems.
To do this, the authors first argument the intractable posterior distribution with a diffusion process, and derive the mean and variance propagation rule in the backward diffusion process.
To estimate the intractable transitions incorporated in the above propagation rule, variational inference objectives as well as the natural gradient update are developed.
The above estimation relies on a pretrained score model on the clean data.
The experiments on toy examples and high-resolution images both demonstrate the effectiveness of the proposed method compared to baselines.

### Strengths
- This paper is well written and easy to follow.
- Although diffusion-based approaches for solving inverse problems are extensively investigated, the estimating strategy for the posterior mean in equation (7) is novel.
- The gradient estimation in equation (22) with a pre-trained score model is non-trivial. It proves that this method can provide reliable posterior mean estimation in the experiments.
- Figure 2 clearly illustrates how RMP propagates the mean through the diffusion process, which highlights the difference from the models targeting the distributional information.

### Weaknesses
- The citation formats, \citep and \citet, need to be more carefully distinguished.
- RMP requires an additional pre-trained score network to estimate the posterior mean. The evaluation in the experiments does not count the time consumption for training the score network. Moreover, the difficulty of obtaining such a score model can depend on the modeling objects, where images are only a special instance. If this is not possible, the authors should discuss this in their limitations. 
- For each fixed measurement $y$, RMP requires two loops to obtain a posterior mean estimation. The outer loop iterates the timesteps in the diffusion process, and the  inner loop optimizes transition means by variational inference. Adding more computational cost comparison in experiments would help better evaluate the proposed method.
- For a different $y$, we need to re-run the expensive RMP to establish a posterior mean estimation. Especially, the $\mu$ and $\Lambda$ need to be re-estimated. Is an amortized inference approach possible here?

### Questions
- Is such an expensive two-loop circulation common in this field? If not, the authors should discuss this in their limitations. If so, a comparison with related works is recommended.

### Soundness
3

### Presentation
3

### Contribution
3
