# Lightning-Fast Image Inversion and Editing for Text-to-Image Diffusion Models

- Decision: Accept
- Avg Score: 6.75
- Scores: 6, 8, 8, 5

## Abstract
Diffusion inversion is the problem of taking an image and a text prompt that describes it and finding a noise latent that would generate the exact same image.
Most current deterministic inversion techniques operate by approximately solving an implicit equation and may converge slowly or yield poor reconstructed images.  We formulate the problem by finding the roots of an implicit equation and devlop a method to solve it efficiently. Our solution is based on Newton-Raphson (NR), a well-known technique in numerical analysis. We show that a vanilla application of NR is computationally infeasible while naively transforming it to a computationally tractable alternative tends to converge to out-of-distribution solutions, resulting in poor reconstruction and editing. We therefore derive an efficient guided formulation that fastly converges and provides high-quality reconstructions and editing. We showcase our method on real image editing with three popular open-sourced diffusion models: Stable Diffusion, SDXL-Turbo, and Flux with different deterministic schedulers. Our solution, \textbf{Guided Newton-Raphson Inversion}, inverts an image within 0.4 sec (on an A100 GPU) for few-step models (SDXL-Turbo and Flux.1),
opening the door for interactive image editing. We further show improved results in image interpolation and generation of rare objects.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses diffusion inversion for fast and accurate inversion within text-to-image diffusion models. The authors propose Guided Newton-Raphson Inversion (GNRI), which leverages the Newton-Raphson (NR) numerical root-finding technique to achieve efficient and high-quality inversion. By constructing a modified DDIM inversion function as the target for NR and adding a guiding term, GNRI ensures convergence within the distribution of the latent space, overcoming common challenges in achieving accurate reconstructions. This approach supports tasks like real-time image editing, image interpolation, and rare concept generation, achieving significant speedups. The authors show that GNRI could invert images within 0.4 seconds on an A100 GPU while maintaining high fidelity, compared with popular diffusion models.

### Strengths
Originality: This paper introduces a novel approach to the diffusion inversion problem by leveraging the Newton-Raphson (NR) root-finding method with two modifications: (1) dimensionality reduction via a scalar formulation of the Jacobian and (2) a guiding regularization term. By reframing inversion as a fixed-point iteration (FPI) problem with an $L_1$ norm relaxation, this work combines numerical optimization techniques with diffusion models, addressing limitations in accuracy and speed seen in prior methods. The addition of the regularization term prevents out-of-distribution solutions.

Quality: The methodological foundation is rigorous, with well-defined derivations and justifications for each modification to the NR method. The paper also provides extensive empirical validation across multiple tasks, including image reconstruction, editing, interpolation, and rare concept generation. The inversion time to 0.4 seconds on an A100 GPU is impressive.

Clarity: The paper is generally clearly written and accessible. 

Significance: GNRI addresses the problem of achieving efficient and accurate image inversion in text-to-image diffusion models, which is central to tasks like real-time image editing and rare concept generation. The experimental results across models (e.g., Stable Diffusion, SDXL-Turbo, Flux) demonstrate GNRI’s versatility, with the potential for broad impact in real-time generative model applications.

### Weaknesses
The concept of utilizing FPI methods in diffusion inversion is not completely new (like AIDI, ReNoise).

Figure 3 compares the performance of the method with an FPI baseline, which is not specified as the author mentioned two baseline FPI methods (AIDI, ReNoise).

There is a notational inconsistency in referencing Eq. 5 instead of Eq. 4 when describing the fixed-point function $f(z)$, which could lead to confusion regarding the intended inversion function. This typo gives the impression that the method still relies on the DDIM-inversion approximation. Please clarify these notations.

The objective function $F(Z_t)$ in Eq. 9, which combines the residual term $r(z_t)$ and the regularization $G(z_t)$ raises questions about its role in achieving exact root-finding. The two terms in Eq. 9 seem to contradict each other, because a solution to $r(z_t) = 0$ will yield a $G(z_t) > 0$, which further leads to $F(z_t) > 0$ if $r(z_t) = 0$. This suggests that the method solves an approximation of the original inversion problem rather than the exact roots.

In Fig. 3(a), it is observed that GNRI achieves a lower residual than the non-guided NR inversion (NRI), which is unexpected since NRI has only one objective $r(z_t) = 0$. Why does GNRI, despite its additional regularization term, achieve a better residual than NRI? What is the residual level if you set $z_t = mu_t (G(z_t) = 0)$?

### Questions
The objective function $F(Z_t)$ in Eq. 9, which combines the residual term $r(z_t)$ and the regularization $G(z_t)$ raises questions about its role in achieving exact root-finding. The two terms in Eq. 9 seem to contradict each other, because a solution to $r(z_t) = 0$ will yield a $G(z_t) > 0$, which further leads to $F(z_t) > 0$ if $r(z_t) = 0$. This suggests that the method solves an approximation of the original inversion problem rather than the exact roots.

In Fig. 3(a), it is observed that GNRI achieves a lower residual than the non-guided NR inversion (NRI), which is unexpected since NRI has only one objective $r(z_t) = 0$. Why does GNRI, despite its additional regularization term, achieve a better residual than NRI? What is the residual level if you set $z_t = mu_t (G(z_t) = 0)$?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
To improve the accuracy of DDIM inversion approximations, previous studies, such as ReNoise, have utilized fixed-point iteration. This paper introduces a specialized fixed-point iteration known as Newton-Raphson (NR), which enables faster convergence. Because a straightforward application of the NR method is infeasible for high-dimensional points, this paper reduces dimensionality by applying the L1​-norm to the fixed-point function, transforming the Jacobian into a vector. Additionally, to prevent convergence to an off-manifold fixed point, a proximal term is added to the fixed-point function, steering the solution $z_t$ toward the mean of the forward distribution $q_t(z_t|z_{t-1})$ This complete framework is termed Guided Newton-Raphson Inversion (GNRI).

### Strengths
- The motivation and proposed method is clearly stated.
- As the NR provides faster convergence than naive fixed-point iteration method, the proposed method achieves high-efficiency compared with SOTA inversion methods.
- Combined with SDXL-turbo and Flux, it enables real-time image editing.
- Provided experimental results well demonstrate the effectiveness of the proposed method.

### Weaknesses
 - The reviewer does not find significant weaknesses
- Minor: Linebreak in Figure 2.
- Equation (10) requires one forward pass and one back-propagation through diffusion model (UNet). In fact, with the same number of fixed-point iterations, this requires additional cost for back-propagation compared to ReNoise. However, in Figure 4 and Table 1, the reported efficiency of the GNRI is almost same as the original DDIM and much better than ReNoise. Is there some points that the reviewer is missing?
- Efficiency analysis (Figure 4):  Could author provide PSNR vs NFE? It would be helpful to further understand the efficiency of inverse methods.
- Is this method also capable of multiple-object editing?

### Questions
- Equation (10) requires one forward pass and one back-propagation through diffusion model (UNet). In fact, with the same number of fixed-point iterations, this requires additional cost for back-propagation compared to ReNoise. However, in Figure 4 and Table 1, the reported efficiency of the GNRI is almost same as the original DDIM and much better than ReNoise. Is there some points that the reviewer is missing?
- Efficiency analysis (Figure 4):  Could author provide PSNR vs NFE? It would be helpful to further understand the efficiency of inverse methods.
- Is this method also capable of multiple-object editing?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces an efficient method for accelerating image inversion in diffusion models by refining the Newton-Raphson (NR) approach. While a direct application of NR is computationally intense due to the need for Jacobian computation, the authors optimize it with dimensionality reduction using the L1 norm and incorporate a regularization term to ensure the noise latent conforms to the original distribution of the diffusion model. Experiments on models like SDXL-Turbo and Flux showcase both the speed and quality of inversion, and additional tests demonstrate the method’s capabilities in image editing, interpolation, and generating rare objects.

### Strengths
1. The paper introduces an optimized approach to inversion in diffusion models, significantly accelerating the process. With inversion times as low as 0.4 seconds on an A100 GPU, this method is fast enough to enable interactive applications, a notable advancement over existing techniques.
2. By incorporating an L1 norm for dimensionality reduction and a regularization term to ensure conformity with the diffusion model's distribution, the method maintains high reconstruction quality, avoiding common issues like out-of-distribution errors in the generated latents.

### Weaknesses
1. Missing comparison with DDPM Inversion (An Edit Friendly DDPM Noise Space: Inversion and Manipulations) for the inversion performance in both quality and speed. Also, please include the DDPM-Inv result on PIE-Bench for image editing. 
2. More visualization comparison of the proposed method against other methods for editing tasks. Includes more editing results from the PIE-Benchmark.

### Questions
I suggest the authors to include the experiments for the DDPM-Inv for both reconstruction and editing. This helps to understand the difference between using one trajectory vs sample multiple trajectory and record the noise(difference) and help us to determine which method is better. 
Also please include more visualization results for the editing tasks. This helps us to understand the difference of different methods visually.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a new inversion method for image editing in T2I DMs. It uses the Newton-Raphson (NR) method to improve the speed and accuracy of the inversion process. The authors present two main contributions: applying a norm to the NR method (Sec 4.1) and using an anchoring technique (Sec 4.2). Experimental results show that they can edit real images lightning-fast.

### Strengths
1. **Innovative Approach**: The use of the Newton-Raphson method helps overcome common problems found in other iterative inversion techniques (AIDI, ReNoise, ExactDPM), making the process more efficient.
   
2. **Comprehensive Experiments**: The paper provides experiments on three practical tasks, showing that GNRI well compared to existing methods, especially in terms of speed.

### Weaknesses
1. **Questionable Contribution**: Although the idea of employing NR seems innovative, the contribution in Sec 4.1 about applying the norm seems standard and not very innovative. Optimizing norms is a common practice in optimization. For example, on page 9 of ReNoise, the convergence analysis is performed using the l2-norm, and ExactDPM also applies gradient descent to the l2-norm. Actually, anyone who tries to apply Newton method would do the same thing naturally, because calculating Jacobian is impossible while calculating the gradient of the *norm* is very easy in PyTorch. Therefore, this point does not stand out.

2. **Similarity to Other Methods**: The guiding regularizer introduced in Sec 4.2 appears similar to Pan et al.'s Anderson acceleration, which also aims to prevent large changes from previous estimates. This similarity raises questions about the originality of the approach. On the contrary, the significant drop in performance when $\lambda=0$ in Figure C2 can be seen as an indication of the instability of NRI.

3. **Memory Usage**: The Newton-Raphson method needs gradients, which can lead to high memory use. (It must be using torch.grad, I guess.) Other methods, like AIDI and the forward step method in ExactDPM, do not rely on gradients and may be more efficient, in terms of memory usage. ExactDPM actually used a smaller GPU than A100.

4. **Some writings are confusing**: The description of $\mathcal{F}$ is confusing because it is defined in two different ways: as a function from $\mathbb{R}^D \to \mathbb{R}^D$ in L203 and again as a function from $\mathbb{R}^D \to \mathbb{R}^+$ in Eq (9). This inconsistency can mislead readers. Also, in line 577, the citation for Hong et al. is duplicated. In line 637, it should be noted that EDICT was presented at CVPR *2023*, not 2022.

5. **Lack of Results for Rare Concept Generation**: The paper does not provide strong quantitative results for generating rare concepts. For example, Table 3 does not show significant improvements over existing methods.

### Questions
1. In L238, should it reference Eq. 4 instead of Eq. 5?
2. Could you provide more results for the rare concept generation?

### Soundness
3

### Presentation
2

### Contribution
3
