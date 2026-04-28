# On Accelerating Diffusion-Based Sampling Processes via Improved Integration Approximation

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
A popular approach to sample a diffusion-based generative model is to solve an ordinary differential equation (ODE). In existing samplers, the coefficients of the ODE solvers are pre-determined by the ODE formulation, the reverse discrete timesteps, and the employed ODE methods. In this paper, we consider accelerating several popular ODE-based sampling processes (including EDM, DDIM, and DPM-Solver) by optimizing certain coefficients via improved integration approximation (IIA) 
We propose to minimize, for each time step, a mean squared error (MSE) function with respect to the selected coefficients.  The MSE is constructed by applying the original ODE solver for a set of fine-grained timesteps, which in principle provides a more accurate integration approximation in predicting the next diffusion state. 
The proposed IIA technique does not require any change of a pre-trained model, and only introduces a very small computational overhead for solving a number of quadratic optimization problems. Extensive experiments show that considerably better FID scores can be achieved by using IIA-EDM, IIA-DDIM, and IIA-DPM-Solver than the original counterparts when the neural function evaluation (NFE) is small (i.e., less than 25).

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposes IIA solvers by estimating the coefficients of diffusion ODE solvers. Instead of using the previous analytical coefficients, this work use the ground truth solution (by solving with many steps) at each interval to estimate the coefficients with a MSE loss, and then further accelerate the sampling procedure of diffusion ODEs, which can be understood as "distill the coefficients".

### Strengths
- The proposed method is easy to understand and the writing is easy to follow.
- The proposed method can be used for any previous ODE solvers and further improve them.

### Weaknesses
 - Major:
  - The design for IIA solvers seem to be lack of a principle. For example:
    - In IIA-EDM, why $z_i-D_\theta$ is the "first gradient"? It is the gradient of what? Because the "2nd gradient" is the difference of two $D_\theta$, it is natural to understand the "first gradient" is $D_\theta$ itself, but not $z_i-D_\theta$. So what is the basic principle for designing it? Specifically, the choice of $z_i - D_\theta$ as a 'first gradient' is not well-motivated. It's unclear why this specific difference is chosen over, for example, just $D_\theta$ or some other related quantity. The connection to the underlying optimization problem or the ODE being solved is missing, making the design seem arbitrary.
    - Why DDIM use data-pred model and noise-pred model for IIA? As data-pred model can be equivalently rewritten to noise-pred model, it seems to be equivelent to a linear combination of $z_i$ and $\epsilon_\theta(z_i, t_i)$. The use of both data-prediction and noise-prediction models in IIA-DDIM is confusing. Given that they are mathematically interconvertible, it's not clear why both are needed. It appears that the method is essentially a linear combination of the current state $z_i$ and the noise prediction $\epsilon_\theta(z_i, t_i)$, which raises questions about its novelty and effectiveness compared to directly optimizing the coefficients of such a combination.
- Minor:
  - Table 1, Column 6, should be "IIA-DPM-Solver" instead of "IIA-PDM-Solver".
  - As far as I known, the dpm variant for SD v2 is 2nd-order multi-step DPM-Solver++, not DPM-Solver. Please clarify the detailed setting.

### Questions
Please clarify the common design principle for IIA for different solvers. Is there any common principle such that we do not need to one-by-one design them?

====================

Thanks for the authors' revisions. I think the revised version addressed my concerns to some extent, so I raise my score to 6.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposed to use the improved integration approximation(IIA) technique to numerically solve the reverse ODEs that appears in the ODE-based sampling processes, including EDM, DDIM and DPM-Solver. The authors introduced numerical algorithms based on IIA and explain the algorithms from both the theoretical and experimental perspective. 

1. Theoretically, algorithms based on IIA are designed for EDM, DDIM and DPM-Solver. In these algorithms, gradient at each step is estimated by a linear combination of several most-recent gradients, which is expected to be more accurate than to only use one or two most recent gradients. The coefficients in the linear combination are obtained by solving an optimization problem, minimizing the MSE to some highly accurate integral approximation.

2. Experimentally, they verify the effectiveness of these algorithms on EDM, DDIM and DPM-Solver. It is observed that the IIA-based algorithms improves the sampling qualities for low NFEs($\le 25$).

### Strengths
1. This paper introduces new numerical algorithms for ODE-based sampling processes based on IIA. Although this paper focuses on EDM, DDIM and DPM-Solver, same idea applied to other ODE-based sampling processes as well. 

2. The theoretical formulations of the algorithms are clear.

3. Experimental results are provided and they show the improvements of such algorithms in some cases(small NFEs).

### Weaknesses
1. The paper doesn't provide any theoretical result showing the effectiveness of the IIA-based algorithms. Specifically, while the authors propose optimizing the coefficients of the linear combination of gradients, there is no analysis of how this optimization affects the convergence rate or the stability of the numerical solution. It remains unclear if the proposed method guarantees a reduction in the error of the numerical solution compared to standard methods, or under what conditions such improvement can be expected. A theoretical analysis, even if limited to specific cases, would greatly strengthen the paper.


2. According to the experiments, the improvement of the algorithms in FID only happen when NFE is small. It is also not clear why there is no significant improvement on FID with big NFE. The paper lacks a detailed discussion on the relationship between the number of function evaluations (NFE) and the performance of the IIA-based algorithms. It is not clear if the lack of improvement at higher NFEs is due to the optimization reaching a plateau, or if the IIA method is inherently limited in its ability to improve upon existing methods when the number of steps is large. Further investigation into this behavior is needed, including an analysis of the error accumulation as NFE increases.

### Questions
Questions:

1. Comparing the integration approximation in $(9)$ and $(14)$, why do we preserve the factor $\frac{1}{2}$ in $(9)$ but ignore the two step-size in $(13)$ when we derive $(14)$? If we include the two $\frac{1}{2}$ factors into the coefficients in $(9)$, how would it affect the numerical results?

2. The MSE optimization is based on a high-accuracy integration approximation. How to choose the $M$ and fine-grained time-step in the high accuracy integration? Would the pre-trained time-step affect the parameters in the high-accuracy integration approximation?

Comment:

1. Typo in the second integral in $(10)$.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes an improvement to the diffusion model integration procedure in order to make the sampling procedure faster. In particular, in order to accelerate the numerical time integration over an interval t_i to t_{i+1}, an optimization problem is solved that optimizes the weights over gradients evaluated at a coarse grid, in order to minimize the error with  respect to the integration using a fine grid. Using the optimized weights, the inference procedure becomes faster by decreasing the number of steps, while the accuracy is kept consistent. The paper illustrates the performance of the algorithm, highlighting its computational gain, over several experiments.

### Strengths
- The paper discusses an important and timely topic.
- The contributions of the paper are clearly described 
- Extensive numerical experiments are provided to support the contributions.

### Weaknesses
 - The choice of several hyper-parameters is not clear. How does one choose the number and location of grid points for the coarse and find grids? What are the limitations? What will be the computational overhead if one has to search for suitable parameters? How does the computational gain vary as one changes these parameters? 

- There is no discussion or comparison with other numerical integration methods. Numerical integration is a classical topic. It will be helpful to include discussion about why the existing methods are not appropriate.

### Questions
Please see the comments above.

### Soundness
3 good

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes improved integration approximation (IIA) for diffusion model sampling. The core idea is to use past gradients in approximating the update term in diffusion ODEs. The parameters before past gradients are settled by minimizing MMSE to the fine-grained Euler approximation. The proposed IIA technique is only a sampling technique and does not require any modification of the pretrained model. Extensive experiments are conducted to illustrate the performance of this technique.

### Strengths
Originality: The authors studies a sampling technique in diffusion models. The key idea is to approximate ODE more precise to generate better images. This work focuses on a small task but the originality is good.

Quality: The presentation of this work is quite clear.

Significance: The technique is useful for generating high-quality images, and has potential to be integrated into SOTA diffusion realizations. However, as I'm not an expert in empirical diffusion models literature, the performance should be more carefully evaluated by other reviewers.

### Weaknesses
Some parts of the algorithm can be more clearly discussed:
 - In experiments (Table 2) the authors mostly use $r=1$, that is, only use past two gradients to estimate the integration term. It is better to discuss why to choose such a parameter, probably with some numerical illustrations. For instance, an ablation study demonstrating the FID scores for different values of $r$ could provide more insights into the choice of this parameter. In addition, only for BIIA-EDM $r=0$ is chosen, I wonder if it is because of bad performance. Choice of fine-grained timesteps $M$ is also not discussed, and it would be helpful to understand how different values of $M$ impact the performance and computational cost.
 - Personally I think the IIA idea resembles that of "Anderson Acceleration" in optimization literature, but that's not referred in the paper. The authors may gain some insights from it. Specifically, both methods attempt to leverage past information to accelerate convergence or improve approximation. Exploring potential connections or differences could further enrich the paper.
 - The authors could illustrate more about the difference between BIIA and IIA. It seems IIA only decomposes the gradient form $0.5d_i+0.5d'_{i+1|i}$ into two terms, and treat the coefficients of such two terms as optimization parameters so as to add flexibility. I wonder how the performance of IIA is compared to BIIA with larger $r$, i.e., with more previous approximations included in MMSE optimization. A comparative analysis of IIA versus BIIA with varying values of $r$ could help clarify the advantages of the proposed IIA method.

### Questions
Discussed above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
