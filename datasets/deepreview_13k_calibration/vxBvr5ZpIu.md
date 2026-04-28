# Diffusion-PINN Sampler

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 8, 3, 6

## Abstract
Recent success of diffusion models has inspired a surge of interest in developing sampling techniques using reverse diffusion processes.
However, accurately estimating the drift term in the reverse stochastic differential equation (SDE) solely from the unnormalized target density poses significant challenges, hindering existing methods from achieving state-of-the-art performance.
In this paper, we introduce the \emph{Diffusion-PINN Sampler} (DPS), a novel diffusion-based sampling algorithm that estimates the drift term by solving the governing partial differential equation of the log-density of the underlying SDE marginals via physics-informed neural networks (PINN).
We prove that the error of log-density approximation can be controlled by the PINN residual loss, enabling us to establish convergence guarantees of DPS.
Experiments on a variety of sampling tasks demonstrate the effectiveness of our approach, particularly in accurately identifying mixing proportions when the target contains isolated components.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper explores diffusion-based models for unnormalized sampling and introduces the Diffusion-PINN Sampler (DPS). Using physics-informed neural networks (PINNs), DPS directly approximates the log-density of SDE marginals, enabling more precise modeling of complex distributions. The authors provide theoretical convergence analysis and validate the method on several synthetic datasets.

### Strengths
- The paper is generally easier to follow. Theoretical results in Sec 5 could be of interested for readers from other domains.

### Weaknesses
 - The proposed method is computationally expansive compared to other diffusion-based models to train—due to the Laplacian in PINN loss—and to sample from—due to the evaluation of gradient at every time step.
- Insufficient comparison to modern baselines — in addition to  MC methods like HMC or SMC, there’re many other diffusion/SDE based methods, such as [1,2], just to name a few.
- Experiments were only conducted on rather simple, synthetic, target. I’ll be more convinced to see some higher-dim experiments and/or real-world dataset. 
- Parametrize NN with log mu (12) seems like a strong inductive bias and can be infeasible for many practical applications (e.g., sample Boltzmann distribution for conformation generation) when querying energy functions are expansive. Can the authors provide ablation study without such parametrization? 
- Related works Section is rather short and should be extended.
- $\ell_\textrm{reg}$ seems ad-hoc. Why regress onto the boundary condition of the score instead of (11b), which seems more aligned with PINN loss?
- Given that x0 comes from LMC already, is the method computationally cheaper compared to standard MCMC methods?

### Questions
- $\ell_reg$ seems ad-hoc. Why regress onto the boundary condition of the score instead of (11b), which seems more aligned with PINN loss?
- Given that x0 comes from LMC already, is the method computationally cheaper compared to standard MCMC methods?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents a new approach for diffusion sampling. Inspired by existing methods that use physics-informed neural networks, they address the problem of solving the reverse diffusion process using the Fokker Plank equation which models the evolution of marginals $p_t(x)$ in the forward process. Specifically, they identify flaws of existing methods and address them. The first one is the failure of the score FPE and the second is the lack of theoretical analysis of proposed methods. They end up with a method called DPS (Diffusion-PINN sampler) that solves for log-density FPE. They show promising results and consistent improvement over other methods, providing, in addition, convergence analysis of the method.

### Strengths
The paper is very well written! It was pleasant to read and easy to follow.

- The authors provide observations of failure of score FPE and propose a motivated and illustrated solution : solving the log-density FPE and plugging it in the reverse process afterwards.

- The authors provide a good amount of experiments and parsimonious illustrations (just what is needed to illustrate their claims).

- The authors assess performances of their methods with good metrics. It could seem naive to say, but a lot of people miss the use of probabilistic measures for probabilistic problems. The choice of KL/Fisher divergence is welcomed along with the $L^2$ of the log-density.

- The use of PINN for such a problem is relevant. It bases the method on well-established (and timely) fields which is nice!

- The overall structure of the work is clean and each part is self-sufficient.

- Analysis, performed on toy problems at first, allows for good interpretation of the results.

- The proposed sampling methods show big improvement over other baselines for considered problems which further motivates it.

### Weaknesses
I'm really sorry, but I think you will have to change the name (at least the reduced name) of your method! DPS is already a well known and well established sampling method for posterior problems [1]. I think it would be beneficial to avoid being shadowed by existing method. Moreover, it's more than just a sampling method that you present. It's a conjugate training and sampling algorithm. Your main change is about what your network is trained for (the log density) and not about the FPE which is not new in itself (Although the training and the sampling make a whole). 

Otherwise, I point below a few questions and small concerns.

**Small details**

- Line 60: *to ensure convergence guarantee*, it's nitpicking but isn't it a bit redundant?

**Performance concerns**

- I'm a little bit concerned about the performances of the method both in time and resources. It would be nice to, at least discuss them and at best provide some measures in Appendix for example. I detail below my concerns.

- You model the log-density, then you have to take its gradient in order to compute the score that you plug into the reverse process, right? What is the cost of this compared to direct score matching? Indeed, I presume that taking the grad at every step is not without cost. 

- The PINN loss involves gradient and Laplacian operators. What is the cost of computing such a loss compared to simple denoising score matching (which, at the end, is not more complex than an mse)? Does it slow down training? Do you use optimized tricks like jvp/vjp when possible? Could you comment a bit on that please?

- In table 1, isn't it misleading to report KL only on first dimensions for Funnel and Double-well? Can't you report either on several sub-combinations of dimensions or use another measure? Is it due to the cost of the KL in higher dimension? What about more tractable divergence metrics such as the Sinkhorn divergence?

**Sampling method**

- From your text and as the first requirement in **Algorithm 1** you speak about access to the initial condition which derives from the unnormalized density. It is still not clear to me how you access to such density? 

- You present a sampling method, and even more, for diffusion models. It would be nice to have a higher dimensional problem (I agree that it is not necessary to cover your claims here). This method should be studied in more realistic settings also (with images, high dimensional data, ...) and I'm worried about the cost of computing explicitly the score from the log-density or the cost of the loss in such settings. At least comment on that in the main paper.

- Echoing with the previous comment: What about conditional sampling? Posterior problems. Technically your method can extend easily. You compute the prior score as for now and plug the likelihood to guide the sampling. It would be nice (and I think easy) to show, in Appendix if you lack space, the conditional generation for one toy problem. For example, generating only on one mode in the 9-Gaussians or Rings problem. I'm curious to see the benefit of more accurate prior score to such problems. I'm also curious to see if you still perform much better than other considered methods. Indeed, the likelihood guiding score can sometimes help and simplify a bit the problem.

- Nitpick: In figure 3 you say "Sampling performance". Those figures do not show any performances. Maybe change it to "Samples from different methods ...".


**Additional suggestion**

Figure 5 (center and right) are not really revealing. I know that it's hard to display samples in high dim. Could you put corner plots instead? Even if it's on a subset of dimension of the problem. It would be easier to see the differences with and without regularization if you display marginals along this 2-dimensional joint.

### Questions
See weaknesses.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper studies sampling via time-reversing a diffusion process that starts in the target distribution, i.e. it considers diffusion-based generative modeling, where, however, no data samples from the target distribution are available, but the (unnormalized) target density can be evaluated. The authors suggest to learn the score function that is necessary to sample accurately by approximating the underlying Fokker-Planck PDE (in log-space) with Physics-informed neural networks (PINNs). In particular, it is argued that solving the Fokker-Planck PDE and taking derivatives afterwards is advantageous over solving a corresponding PDE for the score directly. The paper presents theoretical analyses that bound the error of the approximations of the log-density and the score, respectively, by the (weighted) PINN objective. Leveraging previous work, this in consequence allows to bound the sampling error by the PINN objective. Some numerical evaluation on synthetic sampling problems in moderate dimensions is provided, demonstrating a proof of concept of the method.

### Strengths
Sampling via learned diffusion processes is an interesting and active field of research, which is arguably more challenging than the typical generative modeling task since no samples from the target are available. The connection to the underlying PDEs is interesting, however, not novel (see weaknesses). Still, the presentation is sound and offers a detailed and interesting theoretical analysis.

The paper is mathematically well written, however, some (practical) implications and motivations could be made clearer for the convenience of the reader.

### Weaknesses
In my opinion, the paper has the following main weaknesses.

1. **Novelty.** The idea of employing PINNs for diffusion-based sampling has already been suggested in [1], [2], [3] and [4]. While [1] and [2] have been cited, only a preliminary version of [3] seems to be mentioned. In fact, in [3] (almost) the same algorithm has been presented (without relying on sampling from an MCMC algorithm) and multiple numerical experiments (including also variants of the suggested method, such as e.g. deterministic evolutions, general evolutions, annealed/prescribed evolutions) have been conducted.

2. **Numerical evaluation.** While the numerical evaluation in the paper showcases good performance of the suggested algorithm, the considered examples are rather synthetic and of moderate dimension. The question of how the algorithm scales to real-world problems and higher-dimensional examples (say, $d > 100$, which might be challenging for PINNs due to computation of higher-order derivatives) remains open.

3. **Practical relevance of theoretical results.** While the theoretical analyses look sound and are nice from a mathematical perspective, I am not certain about their practical relevance. It is clear that in principle a zero PINN loss implies zero score error and (up to discretization and up to the prior error) perfect sampling. At the same time, the provided bound seems to not allow for quantitative statements since constants cannot be computed and it is (due to the Grönwall inequality) probably far from being tight. Furthermore, it seems that the theoretical results heavily rely on earlier works by [5] and [6].

Some additional comments are the following:

4. It is unclear to me how generating collocation points with MCMC-like algorithms (e.g. LMC) is sufficient. It is known that those algorithms converge exponentially slowly for multimodal targets where the modes are sufficiently separated. Therefore, some exploration strategy seems to be necessary in order to get collocation points that cover regions containing distant modes.
5. You write that trajectory-based alternatives lead to "computational complexity associated with differentiating through SDE solvers". However, this is not necessarily true since off-policy training can be chosen also for trajectory-based methods, e.g. by using divergences other than the KL-divergence, see, e.g., [7], [8].
6. The related work section barely lists any of the many alternative methods for diffusion-based sampling that have been suggested in the last 1-2 years.
7. Concurrently to the work of [9], [1] has also derived the PDE for the log-density (and in fact, also approached it via PINNs, see above).
8. You write about "a linear interpolation (i.e., annealing) path between the target distribution and a simple prior", however it’s linear only in log-space.
9. It would be helpful to define the Fisher divergence in the main text (and not only in Appendix A.2).
10. Sampling quality can usually not be measured well by only one metric and therefore it would be even better to have more metrics (e.g. Wasserstein, ELBO, ESS, comparison to expectation reference values etc.).

I apologize in case I misunderstood certain aspects of your paper and am looking forward to potential corrections.

### Questions
1. If I understand it correctly, you claim that Example 1 shows that the Fisher divergence can be arbitrarily small, while the KL divergence stays large at the same time. However, clearly, if the Fisher divergence goes to zero, so does the KL divergence (by the definition of a divergence). Therefore, your statement seems to mean that "the KL divergence can be (much) larger than the Fisher divergence", is this correct? This implies the following questions:
    - a) Since the "scale" of any divergence is rather arbitrary, why should the scale of the KL divergence be better suited than the scale of the Fisher divergence? (That said, I think it could be helpful to consider log-scales in Figure 1.)
    - b) Does your observation generalize to distributions that are not Gaussian?
    - c) Are you aware of any bounds that directly relate the KL divergence to the Fisher divergence? (I’m thinking of something similar to the Poincare inequality.)
2. I find the numerical experiments in Figure 4 more enlightening than the statement in Example 1. Do those observations carry over to other (more complicated, high-dimensional) examples? It seems to me that Lai et al. (2023) have found that using the score FPE (as a regularizer) seems to work well. Can you comment on this finding, given your argument against the score FPE? Also, what happens if you use more gradient steps in the example from Figure 4 (both losses seem to not have converged yet)? Does the score FPE eventually converge sufficiently? (Actually, how do you define "score error"? Is it some kind of $L^2$ error?)
3. If one approximates the log-density as you do, one later must take gradients to get a score approximation, which might incur errors. Can you comment on potential numerical implications?
4. Did you use Hutchinson’s gradient estimator that you introduce in lines 262 and following? While it removes a derivative, it is known to increase the variance of gradient estimators. 
5. In (20) one considers $L_\mathrm{PINN}(t_k; C_1(\varepsilon))$ for multiple $t_k$, however, the integral in $L_\mathrm{PINN}$ always starts at $t=0$. Does this mean that the larger $N$ the larger is the sum? (I would not have expected the term to increase with finer time discretization.)

Some comments on notation and typos:
1. The notation seems to be not consistent all the time, e.g. regarding the time index: $g(t), f(x,t)$, but $p_t(x)$ and not $p(x, t)$; also: $u_t(x)$ vs. $u_\theta(x, t)$.
2. Why do you write $\nabla_x$, but not $\Delta_x$ or $\nabla_x \cdot f$? Also, you write $\nabla_x u_\theta(z, T)$ (e.g. in l. 254). Shouldn’t it be $\nabla_z u_\theta(z, T)$? (Alternatively, you should explain your notation. Suggestion: Writing $\nabla$ instead of $\nabla_x$ solves the issue.)
3. Some citations are not correctly formatted (e.g. "monte carlo" instead of "Monte Carlo"), some versions are old.
4. Inconsistent writing: Fokker-Planck vs. Fokker Planck.
5. 83: Definition of norm: "+" is missing.
6. 83: "Let ν denotes".
7. 199: "until the every end".
8. 320: Assumption -> Assumptions (this typo appear multiple times throughout the paper).
9. 326: After (17) replace "." with ",".
10. 333: (Arjovsky et al. (2017)).
11. 355: "Let $\hat{\pi}_T$ denotes".
12. In the appendix, there are often commas or periods missing after equations, see, e.g. (22), (23) etc.
13. 750: "Let $p(x)$ denotes".

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a novel diffusion-based sampling algorithm called the Diffusion-PINN Sampler (DPS). The DPS estimates the drift term in the reverse diffusion process by solving the governing partial differential equation of the log-density of the underlying stochastic differential equation (SDE) marginals using physics-informed neural networks (PINN). The authors prove that the error of log-density approximation can be controlled by the PINN residual loss, which allows them to establish convergence guarantees for the DPS. Experiments on sampling tasks demonstrate the effectiveness of this method.

### Strengths
1. The paper is well-composed and the concepts are clearly articulated, making it easy to comprehend. 
2. The innovative approach of learning a diffused log-density via the log-density-PF equation is novel.
3. The math derivation is rigorous.

### Weaknesses
1. When the score of the target distribution is accessible, we can perform sampling using MCMC[1] and ParVI[2][3][4]. Renowned algorithms such as HMC and SVGD should be considered for comparison. It would be interesting to see if PINN-Sampling can surpass these methods.

2. The training objective in equation 14 requires gradients of the neural network. This could potentially be time-intensive as the dimension increases. I am skeptical about the scalability of this method. Could you provide a complexity analysis of the training process in relation to dimensionality?

3. Assumption 1 is not plausible, as the suggested scenario is unlikely to occur. Consequently, it's not feasible to bound the error within a constrained domain. It's probable that the subsequent theorems will also hold when $\Omega = \mathbb{R}^d$ and $\nu_t$ are light-tailed distributions.

4. In Example 1, as $\tau$ approaches zero, the variance of $\pi^M$ and $\hat{\pi}^M$ becomes unbounded. However, in real-world applications, the variance of our data distribution is always bounded. Could you give an example where the data distribution has a bounded variance but still has an arbitrarily small $\tau$?

5. The scope of the experiments appears to be rather limited, being mostly synthetic and low-dimensional. It would be beneficial to see applications to higher-dimensional cases, Gaussian processes, Bayesian Neural Networks, and real-world data experiments.

### Questions
see Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2
