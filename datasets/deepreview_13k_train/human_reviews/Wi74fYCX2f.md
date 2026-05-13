# Diffusion models for Gaussian distributions: Exact solutions and Wasserstein errors

- Decision: Reject
- Scores: 3, 3, 8, 6

## Abstract
Diffusion or score-based models recently showed high performance in image generation.
They rely on a forward and a backward stochastic differential equations (SDE). The sampling of a data distribution is achieved by solving numerically the backward SDE or its associated flow ODE.
Studying the convergence of these models necessitates to control four different types of error: the initialization error, the truncation error, the discretization and the score approximation.
In this paper, we study theoretically the behavior of diffusion models and their numerical implementation when the data distribution is Gaussian.
In this restricted framework where the score function is a linear operator, we derive the analytical solutions of the backward SDE and the probability flow ODE.
We prove that these solutions and their discretizations are all Gaussian processes, which allows us to compute exact Wasserstein errors induced by each error type for any sampling scheme.
Monitoring convergence directly in the data space instead of relying on Inception features, our experiments show that the recommended numerical schemes from the diffusion models literature are also the best sampling schemes for Gaussian distributions.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors define a centered Gaussian $N(0, \Sigma)$ as the data distribution and assume that the inference SDE, or forward process, is VP-SDE. VP-SDE is a linear diffusion process and it’s transition kernel, a Gaussian distribution, can be computed in closed-form. This allows the authors to

1. Compute the exact score $\nabla \log q(x_t)$ since the process $x_t$ for all time $t$ is Gaussian
2. Having access to a closed-form for the score allows one to compute exact solutions to the backward SDE (prop 2) and the probability flow ODE (prop 3), which then allows one to analyze the effect of:
    1. impact of initialization error in the ODE and SDE generative models
    2. impact of discretization error
    3. impact of truncation error
    4. influence of the eigenvalues of the covariance matrix

Using the exact derivations, the authors then analyze a Gaussian data distribution with the covariance computed from samples from the CIFAR10 dataset. The authors analyze the $W_2$ error of different samplers on this dataset and present results in table 2. 

In their next experiment, the authors learn the score function using a U-Net and see if their findings translate to when the score function architecture is nonlinear in a setting where the exact score is available as well.

### Strengths
In section 4, particular table 2, the authors provide a thorough analysis of the impact of the:

1. initialization error 
2. truncation error
3. discretization error 

for commonly used samplers such as EM, Heun and Euler in the centered Gaussian case.

### Weaknesses
While the authors have developed a simple framework for analyzing the different sources of error while sampling, it is limited to a Gaussian data distribution. It is not made clear how these insights generalize beyond Gaussian data and fits into the wider literature. See questions.

The score function is available in closed-form when the data distribution is a mixture of Gaussians, and as the authors mention the Wasserstein error is not computable in closed form. However, empirical metrics/divergences such as MMD, kernel Stein discrepancies, etc are available.

Citations:

1. Proposition 1 has also been derived in appendix A in [Albergo 2023], where the authors derive the score for a number of different forward diffusion processes, flows, etc. Can the authors cite them in the main paper?
2. Similarly, for proposition 3, a solution to the PF-ODE has been derived in appendix B in [Khrulkov 2022]. Can the authors cite them in the main paper?

### Questions
1. Can the authors add appropriate citations for proposition 1, for instance eq 6.19 and 6.20 in [SARKKA & SOLIN 2019]. 
2. The ADSN data samples are out of distribution for the classifier used to compute FID scores. Could the authors use a different metric? for instance MMD or other metrics/divergences. 

As mentioned in the weaknesses section, the findings of this paper are not clearly situated within the wider literature, that is what this paper is adding beyond what is known already. For instance, 

1. Error due to discretization is a widely studied problem in numerical sampling. Heun’s is a second-order integration scheme leading to slower accumulation of error compared to Euler’s method. Would the Gaussian data analysis agree with the fact that  a higher order scheme such as RK4 provide a more accurate integration of the PF-ODE?
2. In line 502-503, the authors mention that “the score approximation error is by far the most impactful source of error”. However, it is already known that score estimation error can lead to an error in sampling, for instance in [Chen et al 2023], [De Bortoli et al 2021], etc. 
3. Can the Gaussian data analysi provide any theoretical justification or insight into the robustness of SDE sampling over ODE sampling besides empirical evidence?

**References**

[Chen et al 2023] Chen, Sitan, Sinho Chewi, Jerry Li, Yuanzhi Li, Adil Salim, and Anru R. Zhang. "Sampling is as easy as learning the score: theory for diffusion models with minimal data assumptions." *arXiv preprint arXiv:2209.11215* (2022).

[De Bortoli et al 2021] De Bortoli, V., Thornton, J., Heng, J. and Doucet, A., 2021. Diffusion schrödinger bridge with applications to score-based generative modeling. Advances in Neural Information Processing Systems, 34, pp.17695-17709.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
Theory:
- It is well known that the W2-distance between two gaussian distributions is exactly computable. If we consider diffusion process described by a linear drift term, it is also well known that the corresponding integral kernel is also gaussian, which means if we consider **the initial distribution as gaussian (gaussian assumption)**, the remaining all marginal distributions at diffusion time t are also gaussian distributions as commented above of eq (10). The degrees of freedom of the distribution is described by covariance matrix $\Sigma_t$.
- The authors also provide solutions of backward SDE (Proposition 2) and backward probability flow ODE (Proposition 3) under the gaussian assumption, which provide exact expressions of each covariance matrix and covariance on $t=T$ with forward time expression.
- By considering normal distribution at $t=T$ with forward time expression, the above expressions provide covariance at time t with backward SDE and ODE, which provide an inequality of W2-distance (Proposition 4).
- In addition, the authors classify errors as:
    - the initialization error, which measures discrepancy between p_T and model's latent distribution,
    - the discretization error, which measures errors caused by numerical integral of SDE or ODE,
    - the truncation error, which measures an error caused by integral truncation at t=$\epsilon>0$.

Numerical experiments:
- They conducted some experiments to measure these errors in W2-sense (Table 2) and reported (each $\Sigma_t$'s) eigenvalue dependencies of each error with "gaussianized" CIFAR-10 data (Figure 2).
- They studied effects of score approximations by models (section 5).

### Strengths
- clarity(+)
    - The paper is well written and easy to follow. The theory part is easy to understand.
    - The numerical experiments are somewhat informative.

### Weaknesses
 - significance (-?)
    - Thanks to the gaussian assumption, everything is very clear. However, at the same time, it makes the all results a little weak. I am not sure about how these exact results help in understanding the errors in actual learning outcomes. I summarized some questions about it below.



### Questions
I know that considering non-gaussian case is out of scope of this paper, but I would like to know the followings.
1. In the ablation study, the authors reported some influences based on the classified error categories (initialization/discretization/truncation errors), but it is not clear where the gaussian assumption is being used in the consideration of this error.
2. In Figure 2, as the authors commented, all errors around $\lambda=1$ drop suddenly. Why does it happen? In addition, similar sudden drops happen some other $\lambda$s. Are there any explanations on why it happens?
3. In the same page, the authors leave a comment "... for any Gaussian distribution Heun's method introduces nearly no additional discretization error, ..." Is this significantly influenced by the gaussian assumption, or can this be stated regardless of the gaussian distribution?
4. In page 9, to my understanding, the authors approximate W2 between $p_\theta$ and $p_{data}$ by replacing $p^{emp} \to p_\theta$ in eq (26). If so, how do you get $\lambda^{\xi, emp} = \lambda^{\xi, \theta}$ ? It would be related to Appendix F.3, but I'm not sure how to get $\Gamma$ in this case.
5. Besides these questions, if the authors have any insights indicating that the current results can be commonly applied outside the gaussian assumption, please make it clear.

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper presents a theoretical investigation of the different sources of errors in diffusion models in the case of Gaussian distributions. I.e., the setting is on purpose limited to this simple case in order to be able to derive closed form solutions to the forward and backwards diffusions and to provide a direct error investigation.

### Strengths
- the paper presents an interesting description and investigation of the sources of errors in diffusion models
- though restricted to specific cases, I found the discussions and results interesting. I believe the findings can be useful for practical application of diffusion models
- the paper is well written and nicely presented

### Weaknesses
 - one can of course criticize the Gaussian assumption as being limited and not reflecting the complexity of real world data. I still believe the paper was an interesting read, even though it covers a specific case

### Questions
- I was a bit surprised that closed form solutions for the forward and backwards SDEs in the Gaussian case have not been presented in the literature earlier on. My guess would have been that they could be found in SDE textbooks. The authors provide some newer references to related results at the end of section 3. My question would be if you have thoroughly checked earlier SDE literature (before diffusion models became popular in the ML world) if these results have been covered previously?

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
5

### Summary
This paper studies theoretically the behavior of diffusion models and their numerical implementation when the data distribution is Gaussian. In this restricted framework where the score function is a linear operator, we derive the analytical solutions of the backward SDE and the probability flow ODE. We prove that these solutions and their discretizations are all Gaussian processes, which allows us to compute
exact Wasserstein errors induced by each error type for any sampling scheme.

### Strengths
1.The paper derives exact analytical solutions for the forward and inverse stochastic differential equations (SDEs), as well as the probabilistic flow ordinary differential equations (ODEs), within the framework of Gaussian distributions. 
2.The initialization error, truncation error, discretization error, and  score approximation error  are systematically analyzed. 
3.Different numerical sampling schemes are compared through numerical experiments, and in particular, the effectiveness of Heun's method for Gaussian distributions is demonstrated.

### Weaknesses
1.While the paper provides an in-depth theoretical analysis, it may lack validation on diverse real-world datasets. Specifically, the analysis is limited to Gaussian distributions, which are rarely encountered in their pure form in practical applications. The paper does not address how the theoretical results would translate to non-Gaussian data, where the score function is no longer a simple linear operator. This raises concerns about the practical relevance of the derived analytical solutions.

2.Although it is possible to derive exact solutions under the assumption of a Gaussian distribution, obtaining such analytical solutions for more complex data distributions may be challenging, which could limit the generalization of the theory. The paper does not discuss potential approximations or alternative methods for handling non-Gaussian distributions. This limitation is significant because real-world data often exhibits complex, non-Gaussian characteristics, such as multi-modality or heavy tails.

3.The paper points out that score approximation errors may be significant in practical applications but does not propose an effective solution for minimizing these errors. The analysis focuses on the error introduced by discretization and truncation, but does not delve into the impact of inaccurate score estimation, which is a crucial factor in the performance of diffusion models. The paper should explore methods for improving score estimation, such as using more advanced neural network architectures or training techniques.

### Questions
1.The paper compares several numerical sampling schemes, but has it covered all the optimal possible schemes?
2.For complex data distributions, analytic solutions may be difficult to obtain, which may affect the computational efficiency of the model. Does the paper consider the issue of computational efficiency in practical applications?

### Soundness
3

### Presentation
3

### Contribution
3
