# Diffusion State-Guided Projected Gradient for Inverse Problems

- Decision: Accept
- Avg Score: 6.75
- Scores: 8, 8, 8, 3

## Abstract
Recent advancements in diffusion models have been effective in learning data priors for solving inverse problems. They leverage diffusion sampling steps for inducing a data prior while using a measurement guidance gradient at each step to impose data consistency. For general inverse problems, approximations are needed when an unconditionally trained diffusion model is used since the measurement likelihood is intractable, leading to inaccurate posterior sampling. In other words, due to their approximations, these methods fail to preserve the generation process on the data manifold defined by the diffusion prior, leading to artifacts in applications such as image restoration. To enhance the performance and robustness of diffusion models in solving inverse problems, we propose \textit{Diffusion State-Guided Projected Gradient} (DiffStateGrad), which projects the measurement gradient onto a subspace that is a low-rank approximation of an intermediate state of the diffusion process. DiffStateGrad, as a module, can be added to a wide range of diffusion-based inverse solvers to improve the preservation of the diffusion process on the prior manifold and filter out artifact-inducing components. We highlight that DiffStateGrad improves the robustness of diffusion models in terms of the choice of measurement guidance step size and noise while improving the worst-case performance. Finally, we demonstrate that DiffStateGrad improves upon the state-of-the-art on linear and nonlinear image restoration inverse problems.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper present a novel method for adding an add-on of projected gradient during solving inverse problems with (latent) diffusion models. The method can be applied for an arbitrary inverse problem solver. Results show improvement over baselines such as PSLD and ReSample for solving inverse problems with LDMs.

### Strengths
1. Well written
2. Easy to Understand
3. The idea of projecting the gradient to the manifold of intermediate noise is novel and making sense to me. This method supposes to suppress artifacts that arises with hard optimization.

### Weaknesses
1. In some cases where gradient computation may incur some additional burdens (for example when PSLD takes a lot of memory), this method may not be feasible. Specifically, the need to compute and store gradients with respect to the diffusion state at each step, particularly when using large models or high-resolution images, could become a significant bottleneck. This is especially true for methods like PSLD, which already have high memory demands, and the added gradient projection step could further exacerbate this issue, limiting the practical applicability of the proposed method in resource-constrained environments.
2. There are some other works that try to project the restoration gradient onto the prior manifold (for example DreamClean [1], and MCG [2]). The paper does not sufficiently differentiate itself from these existing methods. While the authors propose projecting onto the manifold of intermediate noise, the novelty of this choice is not fully justified, especially given that other methods also leverage manifold projections for similar purposes. A more detailed analysis of how the proposed projection differs fundamentally from these prior approaches is needed.
3. The baselines with LDMs are sufficient in my view, but this paper could benefits more with pixel diffusion baselines such as DDNM [3], DDRM and so on. The lack of comparisons with pixel-based diffusion models limits the generalizability of the conclusions. It is unclear whether the proposed method would offer similar improvements when applied to pixel-based diffusion models, which have different characteristics and may respond differently to the proposed gradient projection technique.

### Questions
1. Could authors provide more baselines results especially for pixel diffusion
2. I am curious about whether the authors consider choosing a good initial noise. Like [4, 5]


[4] Chung, Hyungjin, Byeongsu Sim, and Jong Chul Ye. "Come-closer-diffuse-faster: Accelerating conditional diffusion models for inverse problems through stochastic contraction." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2022.

[5] Fabian, Zalan, Berk Tinaz, and Mahdi Soltanolkotabi. "Adapt and Diffuse: Sample-adaptive Reconstruction via Latent Diffusion Models." Proceedings of machine learning research 235 (2024): 12723.

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
Authors propose Diffusion State-Guided Projected Gradient (DiffStateGrad), a module that increases robustness of existing diffusion based inverse problem solvers to both increase the performance and the robustness against choice of hyperparameters. DiffStateGrad projects the measurement gradients onto the low-rank approximation of intermediate states of the diffusion process (noisy manifolds for each timestep). Effectiveness of DiffStateGrad is demonstrated through multiple datasets (ImageNet and FFHQ), wide range of linear and non-linear inverse problems and applied to several SOTA posterior sampling algorithms (PSLD, ReSample and DAPS).

### Strengths
* The paper is written very well. The work is contextualized well among related work and I enjoyed reading the paper.
* DiffStateGrad is formulated as a module that greatly increases robustness of existing SOTA posterior sampling approaches (such as PSLD and DAPS) with respect to the choice of step siz and measurement noise. 
* The effectiveness of DiffStateGrad is demonstrated in diverse set of forward models such as box inpainting, random inpainting, Gaussian deblur, motion deblur, etc. for linear inverse problems and phase retrieval, nonlinear deblur and HDR for nonlinear inverse problems.
* Additional cost of calculating SVD and projecting gradients seems negligible based on Figure 4.

### Weaknesses
 * In line 214, there is a brief comparison between MCG and DiffStateGrad, stating that one of them enforces iterates to stay close near $\mathcal{M}_t$ and the other one enforces closeness to $\mathcal{M}_0$. The fact that these methods are similar in terms of premise (measurement gradients throwing iterates off the manifold) and intuition, I think it deserves a more in depth comparison/discussion about their similarities and differences. Specifically, a more detailed analysis of how the projection onto different manifolds affects the optimization trajectory and convergence properties would be beneficial. It would be helpful to understand the conditions under which projecting onto $\mathcal{M}_t$ is superior, and whether there are scenarios where projecting onto $\mathcal{M}_0$ might be more appropriate.
* How would DiffStateGrad interact with diffusion-based solvers that adopt earlier initialization strategies such as (CCDF [1] or it's adaptive version Adapt-and-Diffuse [2])? I would expect bigger step sizes are more detrimental in the "chaotic" regimes of reverse diffusion process where SNR is low. Would DiffStateGrad + CCDF combination should perform similar or better (albeit with less margin) than vanilla CCDF? A more detailed discussion on how the proposed method interacts with different initialization strategies and how it affects the overall convergence behavior of the diffusion process would be valuable. It would be interesting to see if DiffStateGrad can mitigate the need for more complex initialization strategies, or if it is best used in conjunction with them.
* Except for the robustness experiments, measurement noise level is not specified for the experiments (Table 2, 3, etc.). If noise was present, what was the variance and based on line 365 was it added to the images in the range [0,1] (this information is very useful for reproducibility in the future)? Does the presense/absense of measurement noise have any effect on the performance of DiffStateGrad? It is crucial to specify the noise model and parameters used in the experiments to ensure reproducibility. The impact of different noise levels on the performance of DiffStateGrad should be analyzed more thoroughly. A clear understanding of how DiffStateGrad behaves under varying noise conditions is essential for its practical application. 
  * On a related note, how does the measurement noise robustness experiment figures look when noise level is $<0.05$?

### Questions
* In line 214, there is a brief comparison between MCG and DiffStateGrad, stating that one of them enforces iterates to stay close near $\mathcal{M}_t$ and the other one enforces closeness to $\mathcal{M}_0$. The fact that these methods are similar in terms of premise (measurement gradients throwing iterates off the manifold) and intuition, I think it deserves a more in depth comparison/discussion about their similarities and differences.
* How would DiffStateGrad interact with diffusion-based solvers that adopt earlier initialization strategies such as (CCDF [1] or it's adaptive version Adapt-and-Diffuse [2])? I would expect bigger step sizes are more detrimental in the "chaotic" regimes of reverse diffusion process where SNR is low. Would DiffStateGrad + CCDF combination should perform similar or better (albeit with less margin) than vanilla CCDF?
* Except for the robustness experiments, measurement noise level is not specified for the experiments (Table 2, 3, etc.). If noise was present, what was the variance and based on line 365 was it added to the images in the range [0,1] (this information is very useful for reproducibility in the future)? Does the presense/absense of measurement noise have any effect on the performance of DiffStateGrad?
  * On a related note, how does the measurement noise robustness experiment figures look when noise level is $<0.05$? 

***

[1] Chung, Hyungjin, Byeongsu Sim, and Jong Chul Ye. "Come-closer-diffuse-faster: Accelerating conditional diffusion models for inverse problems through stochastic contraction." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2022.

[2] Fabian, Zalan, Berk Tinaz, and Mahdi Soltanolkotabi. "Adapt and Diffuse: Sample-adaptive Reconstruction via Latent Diffusion Models." Proceedings of machine learning research 235 (2024): 12723.

### Soundness
4

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
This paper tackles the problem of solving from a posterior distribution defined with a diffusion-based prior. The authors assume that a diffusion model has been pre-trained and then use it to solve various inverse problems while not requiring anymore training. The method proposed can be thought of as enhancement for existing solvers; it can applied on top of any existing diffusion-based posterior sampling algorithm. It basically consists in adding a projection step, where the projection operator is computed based on the current diffusion state.

### Strengths
- The paper is well written and the methodology is clearly presented. The fact that the proposed algorithm can be plugged on top of existing methods is a significant feat. The theoretical justification for the method is loose but the explanations provided are intuitive. 
- The experiments are convincing are well thought and rather extensive.

### Weaknesses
 - While the additional computational cost is marginal for latent diffusion models, isn't it prohibitive for pixel space diffusion models? Having to compute the SVD at each iteration is certainly a significant drawback. 
- The methodology is based on having at some point a sample on the manifold of "artifact free images" (this is loosely defined). It is unclear how this arises in practice. 
- There are some inconsistencies in the experiments which I believe are explained nowhere in the paper. First, the authors compare to DAPS in pixel space but not in latent space, although in the original paper DAPS is applied in latent space too. Second, in the only example involving imagenet, the authors compare to PSLD only and not ReSample nor PSLD. Also, no experiment on pixel space imagenet is provided. Is there any reason for this?

- While it is claimed that you test the robustness of the method to measurement noise, I am failing where this is done in the paper. 
- How would the method apply to more general methods, e.g. to methods that do not use the approximate guidance term, for example [1]. Would you then simply project the updated $x_t$ and reconstruct it, then move on to the next step?

### Questions
- While it is claimed that you test the robustness of the method to measurement noise, I am failing where this is done in the paper. 
- How would the method apply to more general methods, e.g. to methods that do not use the approximate guidance term, for example [1]. Would you then simply project the updated $x_t$ and reconstruct it, then move on to the next step? 

[1] Lugmayr, Andreas, Martin Danelljan, Andres Romero, Fisher Yu, Radu Timofte, and Luc Van Gool. "Repaint: Inpainting using denoising diffusion probabilistic models." In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pp. 11461-11471. 2022.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors propose DiffStateGrad, a method for projecting the gradients to a low-rank subspace through SVD, where the gradients are those arising from the diffusion models for inverse problem-solving (DIS) framework. The authors propose an adaptive thresholding value, where it is automatically calculated for every timestep $t$. It is shown that DiffStateGrad improves the performance compared to when it is not used. DiffStateGrad is shown to be especially useful for latent diffusion-based methods, which is understandable as gradients are noisier due to the existence of the decoder.

### Strengths
1. The method is straightforward to understand and easy to implement.

2. The proposed framework can be used regardless of the base framework. In the three frameworks that the authors tested DiffStateGrad, it always shows improved performance.

### Weaknesses
1. I believe DiffStateGrad should mainly be compared to approaches like MPGD [1] or DDS [2], which are highly related to this work. The authors do mention [1] as a related work, but says that DiffStateGrad is different to [1], as it considers a projection on $\mathcal{M}_t$ and not $\mathcal{M}$. However, care should be taken because applying gradient guidance to the posterior mean or $x_t$ are equivalent up to a constant. Hence, projecting the gradient guidance on MPGD has about the same effect. The same goes for [2], which does not explicitly project the gradient but uses a Krylov subspace method. I believe DiffStateGrad should be directly compared to MPGD, and ideally also to DDS, with a focus on how the specific projection mechanisms differ and their practical implications, not just the theoretical motivation.

2. The fact that guidance on the posterior mean and the guidance on $x_t$ only differs by a scale factor questions if the theory presented in the paper is actually useful. The paper needs to provide a more compelling argument for why projecting onto $\mathcal{M}_t$ is beneficial, especially if the underlying gradient is essentially the same up to a constant. The practical differences in performance should be more thoroughly analyzed and explained, rather than relying solely on the theoretical justification.

3. Most of the experiments are conduced with latent diffusion based methods. More experiments should be conducted on other widely used pixel domain methods such as DPS and $\Pi$GDM. It is crucial to demonstrate the effectiveness of DiffStateGrad across a broader range of diffusion models, including those that operate directly in the pixel space, to ensure the generalizability of the proposed method.

### Questions
Please see weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2
