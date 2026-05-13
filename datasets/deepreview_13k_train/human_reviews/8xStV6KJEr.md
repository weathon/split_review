# Constrained Diffusion Implicit Models

- Decision: Reject
- Scores: 5, 5, 5, 5

## Abstract
This paper describes an efficient algorithm for solving noisy linear inverse problems using pretrained diffusion models. Extending the paradigm of denoising diffusion implicit models (DDIM), we propose constrained diffusion implicit models (CDIM) that modify the diffusion updates to enforce a constraint upon the final output.
For noiseless inverse problems, CDIM exactly satisfies the constraints; in the noisy case, we generalize CDIM to satisfy an exact constraint on the residual distribution of the noise. Experiments across a variety of tasks and metrics show strong performance of CDIM, with analogous inference acceleration to unconstrained DDIM: $10$ to $50$ times faster than previous conditional diffusion methods.  We demonstrate the versatility of our approach on many problems including super-resolution, denoising, inpainting, deblurring, and 3D point cloud reconstruction.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper suggests a new model, Conditional Diffusion Implicit Models(CDIM) for solving linear inverse problem with pretrained diffusion models.
CDIM can address a problem whether it is noisy or not in linear cases. By imposing constraint on the prior diffusion objective, it solves a linear inverse problem efficiently in both time and utility.
Also for more efficient convergence, this paper utilizes Early Stopping and adaptive learning rate.
In experiments, it shows that it is fast, powerful and easy to use pretrained diffusion models without additional modules.

### Strengths
The authors have presented a promising approach, CDIM, that demonstrates notable improvements over existing methods. Key strengths include:

- **Efficiency**: The CDIM method shows a faster wall-clock time than other DDPM-based approaches (e.g., DPS) and achieves better performance metrics compared to DDIM-based methods (e.g., DDRM).
- **Exact Recovery for Noiseless Observations**: By incorporating the inverse relationship directly into the diffusion process as a constraint, the method can achieve exact recovery in the case of noiseless observations.
- **General Noise Model Applicability**: CDIM also addresses scenarios involving general noise models, broadening its potential use cases.

### Weaknesses
While the paper has several strengths, there are some areas where further clarification and refinement would enhance its impact and precision:

- **Early Stopping Criterion**: The paper suggests that the method handles unknown noise by utilizing early stopping based on the variance of residuals. However, the rationale for selecting the variance of residuals as an early-stopping criterion could benefit from a more detailed explanation. Specifically, the connection between minimizing KL divergence in the noiseless case and minimizing squared error via early stopping for the noise-agnostic method is not clearly established. The paper should elaborate on why monitoring the variance of residuals is an effective proxy for determining the optimal stopping point when the noise distribution is unknown, especially since the method is designed to handle general noise models, not just Gaussian noise. Furthermore, the paper lacks a discussion on how the variance of residuals relates to the actual noise level, and how this relationship might vary with different noise distributions. This makes it difficult to understand the robustness of the early stopping approach.

- **Accelerated Inference**: The paper mentions that CDIM achieves inference times 10 to 50 times faster than previous conditional diffusion methods. It is unclear whether this acceleration is solely due to the use of DDIM, or if it represents a unique contribution of the proposed method. While DDIM is known for its faster sampling, the paper needs to clarify if the constraint satisfaction within the CDIM framework also contributes to this speedup. A more detailed analysis of the computational complexity of the proposed method, compared to other constrained sampling methods, would be beneficial. This should include a breakdown of the computational costs associated with each step of the algorithm, and should also discuss the potential trade-offs between speed and accuracy.


### Questions
1. **Naming Consistency**: The model is referred to as "conditional diffusion implicit models (CDIM)" within the text, yet the title uses "Constrained Diffusion Implicit Models." Additionally, there are existing conditional diffusion models, which may cause some confusion. Consistent naming throughout the paper could help to avoid this.
2. **Typos**:
    - Page 9, line 482: missing closing parentheses.
    - Page 13, line 672: "A. CALCULATIONG" (should be "CALCULATING").
    - Page 13, line 696: "A Gaussian Kernel of size '61x61' ~".
3. **Quantitative Results for Additional Applications**: For the Additional Applications section (Time-Travel Rephotography, Sparse Point Cloud Reconstruction), providing quantitative results would add further value and demonstrate the method's effectiveness.
4. **Highlighting Advantages of Using Only Pretrained Models**: The method reportedly improves certain aspects without additional modules, relying solely on pretrained models. Emphasizing this advantage more prominently could strengthen the appeal of the method.
5. **PSNR Measurements**: Table 1 currently lacks PSNR measurements. Including these would allow for more comprehensive performance assessment.
6. **Choice of Step Size in Section 4.4**: The paper notes that the DPS method fails in this context but doesn’t provide detailed reasons. A more thorough explanation here would be appreciated to clarify the underlying issues.

### Soundness
2

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
4

### Summary
The paper proposes a new approach for solving noisy linear inverse problems with pretrained diffusion models from the perspective of optimization. By leveraging the DDIM sampling process, it is more efficient than other diffusion based posterior sampling algorithms. It is capable of dealing with arbitrary noise in the observations.

### Strengths
1. The core contribution lies in combining the DDIM sampling process with an optimization perspective to maintain alignment between the posterior mean and the observation.
2. The paper is well-written and easy to follow, comprehensive experiments have been conducted.
3. The authors conduct thorough research on the efficiency and accuracy of different diffusion-based posterior sampling algorithms.

### Weaknesses
1. The contribution is limited, the idea of using DDIM to accelerate the sampling process is not new.
1. More mathematical deductions in the appendix would be helpful for the readers to understand. For example, Eq.13, and Eq.14. Also, an introduction to the diffusion posterior sampling(DPS) algorithm in the related work section is also helpful.
2. DMPlug[1] proposes a similar idea. The difference will be that their method optimizes the noise space. I would suggest a comparison with their method.

### Questions
1. How much improvement does the optimization part make? Have the authors tried naive DDIM to solve inverse problems? What is the best result if we increase the number of optimization steps?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents conditional diffusion implicit models(CDIM), which modify the diffusion updates to enforce a constraint upon the final
output to solve noisy linear inverse problems. CDIM satisfies the constraints absolutely for noiseless inverse problems. For noisy case, the author use KL divergence distance to generalize CDIM to constrain the residual distribution of the noise. Compared to other solvers, the family of CDIM method achieve good quality and fast inference time for inverse problems on FFHQ and Imagenet 1k dataset.

### Strengths
1. propose a modification of the DDIM inference procedure to efficiently optimize the Tweedie estimates of $\hat{x_0}$ to satisfy $A\hat{x_0} = y$ during the diffusion process

2. propose to exactly optimize the Kullback-Leibler divergence between the empirical distribution of residuals $R(A\hat{x_0},y)$ and a known, i.i.d. noise distribution r to solve noisy inverse problems

3. give a new choice of $\eta$ to ensure the convergence for KL optimization and stable results of $L^2$ optimization

### Weaknesses
1. The results of DSG[1] on FFHQ and ImageNet datasets are not given. The DSG shows better reconstruction quality and faster inference time on FFHQ and ImageNet datasets. 

2. The KL optimization method(Algorithm 1) is proposed to solve noisy linear inverse problems with known noise distribution. However, from Table.1 and Table.2, $L^2$ optimization has better performance than KL optimization in most tasks. The KL optmization seems meaningless.

3. The calculation of Var(r) are not shown clearly. The necessity of early stopping are not clarified. I doubt that early stopping cannot perform well in noise agnostic taks. 

### Questions
1. Eq. (6), Eq. (7) have typo errors.
2. the Eq. (4) have deductive error, not $\sqrt{1-\alpha_{t}}\nabla_{x_t}\log q(x_t)$，should be ${(1-\alpha_{t})}\nabla_{x_t}\log q(x_t)$

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a linear non-blind inverse framework to solve inverse problems such as denoising, inpainting, and deblurring. The key contribution is the use of Denoising Diffusion Implicit Models (DDIM), which reformulates the diffusion process as a deterministic ODE, allowing it to bypass the full T sampling process. To ensure the denoised image aligns with the observed data, the method employs gradient projection to adjust the denoising trajectory. Additionally, a self-adaptive parameter control strategy is introduced to balance the data term and prior term dynamically. The approach significantly reduces inference time and demonstrates improved performance over Diffusion Posterior Sampling (DPS) across multiple applications.

### Strengths
+ Efficiency: 

The framework leverages DDIM, which bypasses the need for computing all 1000 denoising steps. As a result, it achieves impressive inference speeds (e.g., 2 seconds vs. 70 seconds for DPS).

+ Improved Performance: 

The method demonstrates better performance than DPS, as shown by FID scores, though it lacks evaluation through other metrics like PSNR.

### Weaknesses
I have several concerns regarding its baselines, claims, and equations.

+ Baselines:

DPS was a pioneering work that introduced diffusion priors for solving inverse problems. While this paper extends DPS by using DDIM model, the field has evolved rapidly. Recent advancements such as latentDPS (incorporating latent diffusion models), blindDPS (addressing blind inverse problems), and new methods like fastEM and other two arXiv works have shown improved performance using EM frameworks. The authors should include discussions about these recent developments and add comparisons with latentDPS or blindDPS, which have been available for over a year.

+ Claims and Contribution:

The paper's efficiency seems to primarily come from switching from DDPM to DDIM, which is a known method for speeding up inference by reducing the number of denoising steps. This makes the paper’s core contribution somewhat limited, as it largely inherits benefits from DDIM. I also question where the performance improvement over DPS originates. Does the improvement come solely from DDIM? Typically, acceleration comes with a trade-off in performance, so the authors should clarify the source of the performance gains over DPS.

+ 3D Claims:

The claim about "3D point cloud reconstruction" in the abstract is misleading. The paper focuses on 2D image completion, in the last figure, it is just projected points based 2D completion, which is far from true 3D reconstruction. The authors should rephrase this to more accurately reflect the work done. Additionally, the title could be clearer—something like "Solving Linear Inverse Problems with Constrained Diffusion Implicit Models" would better convey the focus of the paper.

+ Equations:

Some equations lack clarity. In Equations (6) and (7), it would be helpful to explicitly include $x_{t-1}$, for instance: $x_{t-1}=f_{\theta}(x_t)=...$. Additionally, the explanation between lines 195-202, which suggests that one cannot get $x_0$ from $x_t$, is confusing. In DPS, the use of Tweedie’s formula to estimate  $\hat{x_0}$ instead of $x_0$ is mentioned and widely adopted, and the authors should rewrite this section to provide a clearer explanation.

### Questions
See above.

### Soundness
3

### Presentation
3

### Contribution
2
