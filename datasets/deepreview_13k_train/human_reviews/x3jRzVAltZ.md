# VR-Sampling: Accelerating Flow Generative Model Training with Variance Reduction Sampling

- Decision: Reject
- Scores: 3, 8, 5, 8

## Abstract
Recent advancements in text-to-image and text-to-video models, such as Stable Diffusion 3 (SD3), Flux and OpenSora, have adopted rectified flow over traditional diffusion models to enhance training and inference efficiency. SD3 notes increased difficulty in learning at intermediate timesteps but does not clarify the underlying cause. In this paper, we theoretically identify the root cause as a higher variance in the loss gradient estimates at these timesteps, which hinders training efficiency. Furthermore, this high-variance region is significantly influenced by the noise schedulers (i.e., how we add noises to clean images) and data (or latent space) dimensions. Building on this theoretical insight, we propose a Variance-Reduction Sampling (VR-sampling) strategy that samples the timesteps in high-variance region more frequently to enhance training efficiency in flow models. VR-sampling constructs sampling distributions based on Monte Carlo estimates of the loss gradient variance, allowing it to easily extend to different noise schedulers and data dimensions. Experiments demonstrate that VR sampling accelerates training by up to 33\% on ImageNet 256 and 50\% on ImageNet 512 datasets in rectified flow models. Furthermore, VR-sampling could simplify the hyperparameter tuning of logit-normal sampling introduced in SD3.  
The code is available anonymously in~\url{https://github.com/AnonymousProjects/VR_sampling.git}.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors theoretically identify the high variance in loss gradient estimates at intermediate training timesteps in flow-based generative models, and this variance affects influences the convergence of the optimization process during training. To address this issue, they construct an upper bound for the average total gradient variance using a function related to the signal-to-noise ratio (SNR) and propose a Variance-Reduction Sampling (VR-sampling) strategy. This strategy prioritizes sampling timesteps from high-variance regions more frequently to improve training efficiency.

### Strengths
1. The authors propose an upper bound for the variance of loss gradient estimates during training of flow-based generative models.
2. With the VR sampling strategy, the number of training iterations required to achieve similar performance is significantly reduced compared to the baseline.

### Weaknesses
1. There is no comparison with the state-of-the-art methods, and the results in Table 2 are significantly worse than the current state-of-the-art performance.
2. The paper lacks a detailed introduction to the baseline used for comparison in the results tables.
3. The paper does not provide an analysis of how the VR reduction strategy enhances the qualitative results.
4. In Section 3.3, the sampling process in the proposed strategy is not clearly explained. The current description mentions calculating normalization, followed by the PDF and the inverse CDF, but it is unclear how the probability density function π(t) is derived. Is π(t) the result of the inverse CDF? Additionally, there is no information on the final distribution from which the samples are generated.
5. In the caption of Table 2, the results are reported at 400k iterations on the ImageNet 256 dataset. The best result (17.15) is from the cosine scheduler. However, no significant improvement is observed compared to the 17.2 reported at 400k iterations as well in Table 1 of the SiT paper. I consider the Table 2 shows the main results, but the corresponding text is only one sentence in line 382. There is still no clear information on how the baseline results in Table 2 were obtained. This lack of detailed discussion raises concerns about the contribution of speedup and the reliability of all the curve results presented in the figures.

The state-of-the-art performance in SiT is 2.06, and many methods listed in Table 7 of SiT achieve results under 5. However, this paper provides no comparison with those methods. Therefore, the authors cannot guarantee that the final results at 7000k will surpass the SiT benchmark of 2.06. Although the authors said they would include these results later because of the long training time, I can only evaluate the information currently presented in the paper and cannot assume that the unavailable results will be helpful.

### Questions
What is the location parameter m in the caption of table 3?

### Soundness
1

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
3

### Summary
1. This paper first analyzes the reason for training issues in Flow models and finds the important role of high-variance regions.

2. Based on the theoretical analysis, this paper proposes a variance reduction sampling strategy to sample more timesteps with high variance to accelerate model convergence.

3. The experimental results show that the acceleration is significant.

### Strengths
1. This paper provides the theoretical analysis for the training of the flow model.

2. Based on their findings and theoretical analysis, they propose a simple but quite effective method to accelerate the training.

3. I think this method can also be applied to other models easily and the conclusion will still be valid.

### Weaknesses
1. The complexity and overhead of Monte Carlo simulations. This work heavily depends on Monte Carlo simulation, which is complex and time-consuming. Although in the paper, the time is much faster than full training, it may still cause a large overhead. I think this paper should involve more analysis of several aspects that influence the speed and performance of simulation such as the higher number of samples and higher data dimension.

### Questions
1. Based the discussion and method in the paper, during training, we will sample more high-variance regions for training. Will this cause overfitting on high-variance regions?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces a Variance Reduction-based diffusion timesteps sampling strategy to accelerate the training of DMs. The authors identify that the variance of gradient estimates in the training process is higher at intermediate timesteps, which affects training stability. They propose VR-sampling to prioritize sampling from high-variance regions, thereby accelerating training. The method is shown to significantly speed up training across various noise schedulers and data dimensions.

### Strengths
* This papers provides theoretical analysis on gradient variance for conditional flow matching loss and proves the convergence rate during training.
* The experimental results are clear and well verified the effectiveness of the VR-reduction sampling strategy.

### Weaknesses
1. The paper provides a theoretical analysis of the variance of the DSM loss and the convergence speed of DMs training in SGD. Based on this analysis, the paper proposes a method to accelerate training of DMs. While the experimental results appear promising, there is a lack of analysis explaining why the VR-Sampling strategy, specifically "sampling timesteps in high-variance regions more frequently," leads to improved convergence speed. It is not clear how prioritizing high-variance regions directly translates to faster convergence, especially given that the loss landscape is complex and non-convex. The paper needs to provide a more mechanistic explanation of how this sampling strategy interacts with the optimization process to accelerate training.

2. Building on point 1, it seems that the proposed method is anagolous to some empirical findings, such as the Log-normal and logit-normal techniques mentioned in [1] and [2]. The relationship between the theoretical insights and the proposed algorithm could be made more explicit. The paper should clarify whether the theoretical analysis provides a novel justification for these existing empirical techniques, or if the VR-sampling strategy is simply a re-parameterization of these methods. A more detailed comparison is needed to highlight the unique contributions of the proposed approach.

3. Section 4.2 is not entirely convincing. The results on the baseline models are not as strong as those reported in the original paper. For instance, in [3], the FID score (cfg=1.5) is 2.06 and 2.62 respectively on ImageNet 256 and ImageNet 512. In contrast, the best reported FID score for the baseline in this paper is 8.34, as shown in Table 2. While I understand that the experiments have controlled the number of training iterations, I believe a comparison of the convergence points is also necessary to provide a more comprehensive evaluation. It is important to demonstrate that the proposed method not only converges faster but also achieves a comparable or better final performance.

4. On line 290, the Monte Carlo approximation is somewhat confusing. Are you using samples $x_1\sim q(x_1)$ to compute both the outer expectation and inner expectation? Could the authors please provide a more detailed explanation to clarify this concept?

### Questions
* Could the authors explain more detailedly about the VR-sampling strategy (line 315~323)? 
* Could the authors offer a figure like FIgure.5(a) in [1] to show the results on how the VR-sampling strategy improve the gradient variance?

[1] Tero Karras, et al. Elucidating the design space of diffusion- based generative models.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a Variance-Reduction Sampling (VR-sampling) strategy that samples the time steps in high-variance region more frequently to enhance training efficiency in diffusion models. The method first identifies the root cause of the high variance and proposes an effective solution for importance sampling. The proposed strategy is also supported with proof of bounds and convergence analysis. The results show that the proposed method outperforms various baselines, experimented on ImageNet and CIFAR datasets and different model architectures including U-Net, DiT and SiT.

### Strengths
- How to sample time steps is indeed an important problem in traininig diffusion models, the method is with a clear motivation.
- The paper is well-written and easy to follow.
- The results including FID curves and tables clearly and consistently show the effectiveness of the proposed method on different variants of flow models and model architectures, which are widely used in generative modeling recently.
- The proposed method is also supported with necessary proof of bounds and convergence analysis.
- It is appreciated that the paper includes an anonymous code link for reproducibility.

### Weaknesses
 - The paper might lack some dicussions to related method in diffusion models. For example, in line 196, Iterative α-(de)Blending [1] also shares the same formulation as rectified flow. In Monte Carlo sampling, variance reduction can be achieved by using not just importance sampling, but also control variates and correlated sampling, which are initially explored [2,3] for diffusion models. Also, there exists similar line of work considering variance reduction in deep learning such as Deep Learning with Importance Sampling [4] (and there are more), which might also be worth mentioning. The paper could benefit from a more thorough discussion of how the proposed method relates to and differs from these existing techniques, particularly in the context of diffusion model training.
- The visual improvements of VR-sampling shown in Figure 14, 15 seem not significant to me. It will be great to have results on one of the Animal/Human faces (e.g., AFHQ, CelebA, FFHQ), or one of the LSUN datasets. As observed in Figure 13 and 14, the method seems to be working better on face images. Also, results on LSUN bedroom or church might be interesting as the images are with specific textures and patterns.



### Questions
- Is it right that the proposed VR-sampling is only performed in the training phase, not in the inference phase?
- VR-sampling can support different choice of Noise Scheduler (Diffusion, Linear, Cosine), but it seems currently only tested on deterministic ODE formulation. Is it possible to extend it to SDE formulation (as a future work)?
- Does Figure 2 show that S is highly correlated with the resolution, as both CIFAR and ImageNet 256 are using 64x64 resolution?
- Could the author provide some insights how the cfg value can affect the results? I can see with higher cfg in Figure 3, 4, 5, the FID curve for VR-sampling can converge more similar to the baseline (Fig. 3). That said, what would you expect to happen if cfg is higher like 4.0, would the method still clearly outperform the baseline?
- In line 324-331, the author mentioned VR-sampling takes extra time to find the probability density function (PDF) and construct $x_t$. To my understanding, this process requires evaluating the equation (missing equation number?) in line 290 and the term $p_t(x|x_1,i)$ using the neural network prediction. But I am not clear which state/checkpoint of the neural network is used to compute this term?
- It is briefly mentioned "Perception prioritized training of diffusion models" use heuristics to sample time steps based on signal-to-noise ratio (SNR). But I am wondering how it compares to the proposed VR-sampling method?
- The improvement seems more visible in Figure 13, than the improvement shown in Figure 14, 15. Does it give a hint that VR-sampling might work better with higher reoslution images or latents?

Some minor comments:
- I would suggest Figure 13-15 can be larger to better see more details and utilize the space.
- In table 1 "Ho et al., 2020b" is the same as "Ho et al., 2020a". It is cited twice.
- In table 6, how CFG scale is used in training? According to "Classifier-free diffusion guidance" [Ho and Salimans 2022], the training does not use the value directly, but with a random discard of the conditioning to train unconditionally.

### Soundness
3

### Presentation
3

### Contribution
3
