# Lipschitz Singularities in Diffusion Models

- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 8, 8, 6

## Abstract
Diffusion models, which employ stochastic differential equations to sample images through integrals, have emerged as a dominant class of generative models. However, the rationality of the diffusion process itself receives limited attention, leaving the question of whether the problem is well-posed and well-conditioned. In this paper, we uncover a vexing propensity of diffusion models: they frequently exhibit the infinite Lipschitz near the zero point of timesteps. We provide theoretical proofs to illustrate the presence of infinite Lipschitz constants and empirical results to confirm it. The Lipschitz singularities pose a threat to the stability and accuracy during both the training and inference processes of diffusion models. Therefore, the mitigation of Lipschitz singularities holds great potential for enhancing the performance of diffusion models. To address this challenge, we propose a novel approach, dubbed E-TSDM, which alleviates the Lipschitz singularities of the diffusion model near the zero point. Remarkably, our technique yields a substantial improvement in performance. Moreover, as a byproduct of our method, we achieve a dramatic reduction in the Fréchet Inception Distance of acceleration methods relying on network Lipschitz, including DDIM and DPM-Solver, by over 33\%. Extensive experiments on diverse datasets validate our theory and method. Our work may advance the understanding of the general diffusion process, and also provide insights for the design of diffusion models.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Diffusion models, utilizing stochastic differential equations to generate images, have become a leading type of generative model. However, their underlying diffusion process hasn't been thoroughly examined. This paper reveals a concerning tendency in diffusion models: they often display infinite Lipschitz (for $\sigma_{t} \cdot \text{score function}$) near the initial timesteps. Through theoretical and empirical evidence, the presence of these infinite Lipschitz constants is confirmed, which can jeopardize the stability and precision of the models during training and inference. To combat this, the paper introduces a new method, E-TSDM, that uses quantization to reduce these Lipschitz issues. Tests on various datasets support the presented theory and approach, potentially offering a deeper understanding of diffusion processes and guiding future diffusion model design.

### Strengths
This paper highlights a unique and previously unexplored challenge with DDPM: the instability encountered when learning $\epsilon_{\theta} = \sigma_{t} \cdot \nabla \log q_{t}(x)$ during the time steps where $\sigma_{t}$ is minimal. One might naturally question why DDPM doesn't directly learn $\nabla \log q_{t}(x)$. I conjecture that the optimization process for learning $\nabla \log q_{t}(x)$, which involves solving $E\|\nabla \log q_{t}(x) - \frac{1}{\sigma_{t}} \|^2$, becomes problematic with a small $\sigma_{t}$. As a workaround, DDPM employs a transformation to learn $\sigma_{t}\cdot \nabla \log q_{t}(x)$ directly. However, this paper reveals the inherent price of such an approach (no free lunch indeed).

The paper validates the infinite Lipschitz problem with $\epsilon_{\theta}$ both theoretically and empirically. Moreover, it introduces E-TSDM, an innovative solution that essentially employs a quantization strategy when $\sigma_{t}$ is minimal, particularly during the initial t=100 steps. Comprehensive experiments demonstrate E-TSDM's enhanced stability and performance, even setting a new benchmark for FFHQ 256×256.

The paper's novelty is commendable, presenting a compelling and succinct argument with an impressive practical performance. Its insights could significantly influence the diffusion model community. I'm inclined to strongly endorse its acceptance.

### Weaknesses
- One minor suggestion is to avoid saying $t$ being small (rather, it is about $\sigma_{t}$ being small). Since $t$ is in fact $0, 1, 2, 3, .. 100.$ 
- May add more discussions to the alternative approaches (see Questions below).
- It may be worth showing that directly learning $\nabla \log q_{x}(t)$ with the least square is prohibitve.

### Questions
I am looking for comments from the authors on a few alternative methods:
1. Learning $\nabla \log q_{x}(t)$ directly with weighted least square: can we reduce the weight of the least square when $\sigma_t$ is small, e.g., learn $E \sigma_{t}^2\|\nabla \log q_{x}(t) - \frac{1}{\sigma_{t}}I\|^2$?
2. For Eq (9), what if we only learn $\epsilon_{\theta}(\alpha_{f_T(t)}x_0 + \sigma_{f_T(t)}\epsilon, f_{T}(t))$, i.e., only learn the score function for time $f_{T}(t)$ and only use those time steps to do sampling? 
3. Is that $\sigma_{t}$ an input of the neural network: what if we learn $\epsilon_{\theta}(x, \sigma_{t})$ (the intuition is that $\sigma_{t}$ will help adjust the network Lipschize automatically). 

Minor comments:
- Eq 10, are $\beta_{t}$ and $\eta_{t}$ defined?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper demonstrates theoretically (and confirms empirically) that the limit of the Lipschitz constant of the noise prediction network for a timestep of zero is infinite. Such a result is a source of instability for using diffusion models in many generative tasks, and the authors propose a technical solution to alleviate this issue and confirm the superiority of the approach with extensive numerical simulations.

### Strengths
This is an excellent paper, and the presentation is very well carried out. The authors point out a very interesting theoretical property that could explain some practical instabilities encountered in DDPM samples. They then present a practical solution to the problem. The authors' contribution is excellent for the community, as reducing the instabilities in the generative process, such as diffusion models, has important practical consequences.

### Weaknesses
This paper as it is impeccable in terms of presentation and contribution, both theoretically and practically. The only drawback is that no open-source code is available to experiment with their approach.

### Questions
None

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper deals with an exploding Lipschitz constant in the function a neural network is asked to learn in a DDPM model, and the negative effects of trying to learn a function with such.

The authors present an argument based on taking time derivative of the quantity $-\sigma_t \nabla \log q_t(x)$, where the $\sigma_t$ are the standard deviations of the forward noising process in the time-discrete forward noising process in the DDPM formulation and $q_t$ is the density of the data distribution diffused to discrete time step $t$.

They demonstrate that the Lipshitz constant in time explodes to infinity for a most parameter settings of common noising schedules under the DDPM/VPSDE setting.

The authors propose a method for fixing this issue by applying a transform to the time input of the score network, tying together multiple timestep near t=0 to have the same score.

They demonstrate significant empirical benefit over a range of diffusion modelling tasks.

The authors also discuss a number of other possible methods to alleviate the issue of learning high lipshitz constants in diffusion models, but show that these methods despite being theoretically attractive, do not perform as well in practise.

### Strengths
1) The method proposed is simple to implement.
2) The method clearly demonstrates significant empirical benefit.
3) The authors discuss alternative proposals and show these are less effective

### Weaknesses
1) The only weakness I would like to highlight is the discussion of the alternative methods presented.
 - I believe 1 of the methods from the appendix is not mentioned in the main text - namely the Remp method (D.3.3).
 - It would be nice to see an expanded discussion of these with some small experiment to show the quantitative difference between the proposed method and these other methods. I appreciate the space limitation, but I think this is really an interesting point.

2) Could the authors highlight better which lipshitz constant is is that is important, and why we care about it? While I understand I believe which and why it is cared about, it is perhaps not the clearest from reading the paper. The sentence in the abstract "they frequently exhibit the infinite Lipschitz near the zero point of timesteps" is a good example of this - it does not specify _what_ function has high lipshitz constant, or why indeed that matters. From reading the paper in depth, the authors care about the lisphitz constant of the quantity $-\sigma_t \nabla \log q_t(x)$ as a) neural networks find it difficult to learn high lipshitz constant functions, and this is the function we are asking the score net to learn, and b) because this quantity is involved in the reverse rollouts, having a term with high lipshitz constant makes discretising the SDE challenging to do accurately, but this should be apparent from the abstract/introduction.

### Questions
1. Could the authors highlight better which lipshitz constant is is that is important, and why we care about it? While I understand I believe which and why it is cared about, it is perhaps not the clearest from reading the paper. The sentence in the abstract "they frequently exhibit the infinite Lipschitz near the zero point of timesteps" is a good example of this - it does not specify _what_ function has high lipshitz constant, or why indeed that matters. From reading the paper in depth, the authors care about the lisphitz constant of the quantity $-\sigma_t \nabla \log q_t(x)$ as a) neural networks find it difficult to learn high lipshitz constant functions, and this is the function we are asking the score net to learn, and b) because this quantity is involved in the reverse rollouts, having a term with high lipshitz constant makes discretising the SDE challenging to do accurately, but this should be apparent from the abstract/introduction.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper elaborates upon an important observation concerning the presence of infinite-Lipschitz constants in the diffusion process, made earlier by (Song et al., 2021a; Vahdat et al., 2021). It also proposes a simple yet effective approach to address this challenge.

### Strengths
Theorem 3.1 is a nice piece of rigorous analysis of diffusion models, albeit indebted to Song et al.

The proposed approach to address this infinite-Lipschitz challenge, which is based on improving the resolution of the discretisation, does indeed seem to be effective. 

Numerical results in Figures 3 and 4 seem quite impressive.

### Weaknesses
The observation concerning the presence of infinite-Lipschitz constants in the diffusion process is not original (Song et al., 2021a; Vahdat et al., 2021). Concerning it has been observed before, the authors should like to tone down their claims of having observed it first. 

Some of the English is stilted ("vexing propensity of diffusion models" in the abstract, "Recently, there have been massive variants that significantly promote the development of diffusion models" on page 3).

### Questions
How would you describe the differences in your observation and those of (Song et al., 2021a; Vahdat et al., 2021)? 

You could make your observation more original by noting that the infinite Lipchitz constants mean the SDE need not have a unique strong solution (Øksendal, 2003). Exhibiting multiple solutions would indeed be of interest.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good
