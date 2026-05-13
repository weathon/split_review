# Sequential Controlled Langevin Diffusions

- Decision: Accept
- Scores: 8, 6, 6, 6

## Abstract
An effective approach for sampling from unnormalized densities is based on the idea of gradually transporting samples from an easy prior to the complicated target distribution. Two popular methods are (1) Sequential Monte Carlo (SMC), where the transport is performed through successive annealed densities via prescribed Markov chains and resampling steps, and (2) recently developed diffusion-based sampling methods, where a learned dynamical transport is used. Despite the common goal, both approaches have different, often complementary, advantages and drawbacks. The resampling steps in SMC allow focusing on promising regions of the space, often leading to robust performance. While the algorithm enjoys asymptotic guarantees, the lack of flexible, learnable transitions can lead to slow convergence. On the other hand, diffusion-based samplers are learned and can potentially better adapt themselves to the target at hand, yet often suffer from training instabilities. In this work, we present a principled framework for combining SMC with diffusion-based samplers by viewing both methods in continuous time and considering measures on path space. This culminates in the new \emph{Sequential Controlled Langevin Diffusion} (SCLD) sampling method, which is able to utilize the benefits of both methods and reaches improved performance on multiple benchmark problems, in many cases using only 10\% of the training budget of previous diffusion-based samplers.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Sequential Monte Carlo and diffusion-based samplers both intend to simulate samples from an un-normalized target distribution via a continuously-evolving sequence of distributions, yet their drawbacks are markedly different: SMC requires no learning but lacks flexibility, which might lead to slow convergence; diffusion samplers are potentially more adaptive but it requires training. 

This paper proposes sequential controlled Langevin diffusion (SCLD), a combination of the above two methods that uses diffusion-based samplers to adaptive transition between different stages of SMC. As a result from Girsanov's theorem, we can use the path measure likelihood ratio to construct a sequence of importance sampling weights, which can be used as part of resampling for the SMC procedure. The paper illustrates the results with theoretical and empirical findings that showcase SCLD as a strong alternative to SMC-based samplers.

### Strengths
The paper is well-written and I find the results to be of significant interest to the Bayesian statistics community -- SMC has become an important statistical tools for simulating samples from intractable densities, and I think merging SMC with diffusion gives useful insights in building more flexible SMC samplers. 

While some of the paper's contributions seem incremental, the resulting algorithm seems more useful in practice when compared to its predecessor work CMCD, mainly thanks to its use of SMC resampling techniques for more accurate sampling.

### Weaknesses
I have a positive assessment of this paper, and I enjoyed reading it overall.

The overall contribution of this paper seems somewhat limited. It is somewhat difficult to pinpoint exactly what is new from this paper, although I think the overall readability and SCLD's potential usefulness make up for this weakness.

I think the main weakness of this paper is that the combination of continuous and discrete time seems somewhat arbitrary. It seems to me that given enough training iterations, SCLD or CMCD will be able to learn the optimal control function eventually. In that case there would be no need for resampling and MCMC steps as a well-calibrated SDE solver would be able to simulate a sample from 0 to T directly. Therefore, the main appeal of SCLD is that it is able to correct small imperfections of the control function via resampling (as evidenced empirically by SCLD requiring fewer iterations to achieve good performance). However, when to resample depends crucially on where the discrete $t_n$s are placed. This framework has some flexibility in this regard in that it learns a smooth transition function, but the question of how many discrete steps to take remains.

### Questions
- Equation 12: the right hand side looks like the log-density ratio instead of the density ratio itself -- is this correct? 
- Figure 5 seems to suggest that the more SMC steps, the better the performance, even though the paper noted potential downsides of excessive resampling (line 521). Have you tried applying an unusually large number of resampling steps, and seen if the results would degrade overall?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper considered the task of sampling from unnormalized densities and proposed a framework that combines the sequential Monte Carlo (SMC) method with diffusion-based samplers. The main idea behind such a framework is to view both SMC and diffusion-based samplers under the continuum time limit and consider measures on path spaces. This yields the Sequential Controlled Langevin Diffusion (SCLD) method, which has achieved competitive performance on multiple real-world and synthetic examples.

### Strengths
This paper is presented clearly and in detail, making it easy for readers to follow. The proposed framework also allows the authors to design suitable loss functions compatible with off-policy training, which has greatly reduced the use of the training budget in practice. Extensive numerical experiments are provided to validate the effectiveness of the SCLD method.

### Weaknesses
1. As the SCLD algorithm relies on the diffusion bridge formulation, the reviewer thinks that it might be necessary to include a short literature review on related work [1,2,3] combining diffusion bridges/stochastic optimal control with generative models for the sake of completeness. However, this is missing in the current version of the manuscript. 

2. Though the framework based on path measures proposed in this paper leads to effective sampling methods, the idea of combining SMC with diffusion-based samplers isn't new. In fact, this has been explored in earlier work [4] for the posterior sampling problem, which the authors should have cited and discussed. Specific concerns about the comparison between the SCLD method and [4] will be further elaborated in the "Questions" section below.

### Questions
The reviewer's main concern is that a thorough comparison between the SCLD method and the method proposed in [4], whose training stage is based on score matching, needs to be included. Could the authors provide some intuition on how the training losses based on diffusion bridges compare to the score-matching loss when combined with SMC? Empirically, it would be necessary to add the algorithm in [4] as a baseline and compare it with SCLD.

References:

[1] Shi, Y., De Bortoli, V., Campbell, A. and Doucet, A., 2024. Diffusion SchrÃ¶dinger bridge matching. Advances in Neural Information Processing Systems, 36.

[2] De Bortoli, V., Thornton, J., Heng, J. and Doucet, A., 2021. Diffusion schrÃ¶dinger bridge with applications to score-based generative modeling. Advances in Neural Information Processing Systems, 34, pp.17695-17709.

[3] Domingo-Enrich, C., Han, J., Amos, B., Bruna, J. and Chen, R.T., 2023. Stochastic optimal control matching. arXiv preprint arXiv:2312.02027.

[4] Wu, L., Trippe, B., Naesseth, C., Blei, D. and Cunningham, J.P., 2024. Practical and asymptotically exact conditional sampling in diffusion models. Advances in Neural Information Processing Systems, 36.

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
This paper proposes Sequential Controlled Langevin Diffusion (SCLD), a novel sampling framework that combines the strengths of Sequential Monte Carlo (SMC) and diffusion-based sampling methods. The goal is to leverage the resampling efficiency of SMC while taking advantage of the adaptive flexibility of diffusion models. The authors further introduce a log-variance divergence loss function to address the variance issues often encountered with KL divergence estimators, aiming for more stable optimization.

### Strengths
- The integration of SMC and diffusion-based sampling represents a novel and promising approach to tackling challenges in high-dimensional sampling.
- The paper is generally well-structured, with clear segmentation between theory, algorithmic details, and experimental evaluation.
- The proposed log-variance divergence loss function could have meaningful applications in high-dimensional probabilistic modeling, particularly for tasks prone to mode collapse and instability.

### Weaknesses
While the proposed method is conceptually reasonable, the writing is quite sloppy. It is hard for me to understand the contribution and advantages of the proposed SCLD.
- The authors claim that the KL divergence estimator suffers from exponential error growth (Proposition 2.4) and the authors instead use log-variance divergence (Equation (18)). However, there is no formal proof or quantitative scaling analysis of this claim using the log-variance divergence. Furthermore, the paper does not clearly show how the log-variance divergence addresses the specific issues of KL divergence in the context of the proposed method. It's unclear if the log-variance divergence is directly minimizing the same objective as the KL divergence, or if it is a proxy, and if so, what are the implications of this approximation.
- The use of "off-policy training" seems inappropriate and underexplained. This term is typically associated with reinforcement learning rather than Langevin dynamics and diffusion models. The paper does not adequately explain how the concept of off-policy training is adapted to the context of diffusion models, and how it differs from standard training procedures for these models. Specifically, the paper does not clarify what constitutes the "policy" and how it is being modified during the training process.
- Section 1.1 is loosely connected to the content presented in Table 1. For example, the Particle Denoising Diffusion Sampler (PDDS) is mentioned in the appendix without proper discussion in Section 1.1. The differences between existing methods and SCLD are not sufficiently emphasized. Furthermore, the sentence "limiting them to normalizing flows, as well as MCMC steps to keep sample diversity after resampling" (lines 125–126) is unclear and requires revision. The paper needs to more clearly articulate the limitations of existing methods and how SCLD overcomes these limitations, particularly in the context of high-dimensional sampling.
- The log-variance divergence in Equation (18) appears to be a critical component of SCLD, but it is missing from the main Algorithm 1. This omission makes it difficult to understand how the log-variance divergence is integrated into the overall sampling process. The paper should explicitly show where and how this loss function is used in the algorithm, and how it affects the sampling dynamics.

### Questions
- Could the authors elaborate on the finite-time convergence analysis of SCLD mentioned in Table 1? Unfortunately, I did not find a related analysis in the submission.
- The method claims to use a continuous-time setting inspired by Langevin diffusion, but the implementation appears to discretize time with fixed intervals (section 2.4). Could the authors clarify how the continuous-time formulation benefits the analysis or experimental results? How does it compare to related methods such as CMCD from [1]?  

[1] Transport meets Variational Inference: Controlled Monte Carlo Diffusions. ICLR 2024

### Soundness
3

### Presentation
3

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
This paper proposes a new algorithm for sampling from unnormalized distributions. The core idea is to combine the capacity of SMC to focus on relevant regions of the space with the ability of diffusion based samplers to adapt to the geometry of the target distribution by learning a control term $u$ of the reverse SDE.


The control term $u$ then parametrizes a divergence between the path space measure of the forward process and the measure of the backward process.
By minimizing this divergence the algorithm ensures that the two processes become aligned.


To learn the optimal control $u$ the optimization objective is split on N intervals $[t_n, t_{n+1}]$ over which the divergence can be estimated by running the SMC procedure.
The learned control $u$ is then used to guide the proposals in the SMC sampler.

The method is benchmarked against recent approaches on standard benchmarks.

### Strengths
The paper makes a good job at identifying the strengths and weaknesses of SMC samplers and of diffusion based samplers and how they can be combined together. The main concepts needed to understand the method are well introduced and the paper does a good job at explaining them.

### Weaknesses
A significant portion of the paper focuses on presenting the foundational concepts and prior research upon which SCLD is constructed. While this provides necessary context, very little space is used for a detailed discussion of the novel aspects of the sampler itself. As a result, the reader struggles to properly get the contributions.

A comparisons with more traditional SMC samplers to justify the need for the control term and the training procedure would be a nice thing to have. For example with the HMC kernel adaptive procedure of [1] or the adaptive tempered version of [3] (both already implemented in [2]).

In SMC, the choice of the time discretization is usually motivated by the need to have a constant effective sample size (ESS) per step. 
This is quite critical for good sampler performance and principled ways like [3] are available to achieve this. When moving to the continuous time/path space measure setting of SCLD it seems to me that we loose these principled ways to choose the time discretization. It is worth comparing if the flexibility gained in the proposal outweighs the loss of this machinery. 
Or if there is a principled way to choose the time discretization for the sampling process of SCLD.

### Questions
- Are there clear examples where the more flexible proposal is worth the added need for training over running a slightly more sophisticated SMC sampler (eg [1], [3])?

- Are there more complex and less toy examples where SCLD would be applicable ?

-  How sensitive is the procedure wrt the chosen time discretization $[t_n, t_{n+1}]$?

- When sampling, is it possible for SCLD to maintain a principled time discretization guidance similar to traditional SMC use of constant ESS? Does the flexibility in proposal distribution come at the cost of losing these methods?  If so, how does this trade-off impact the overall performance and reliability of the sampler?

### Soundness
3

### Presentation
3

### Contribution
2
