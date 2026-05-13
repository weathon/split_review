# Accelerated Diffusion using Closed-form Discriminator Guidance

- Decision: Reject
- Scores: 6, 5, 5

## Abstract
Diffusion models are a state-of-the-art generative modeling framework that transform noise to images via Langevin sampling, guided by the score, which is the gradient of the logarithm of the data distribution. Recent works have shown empirically that the generation quality can be improved when guided by classifier network, which is typically the discriminator trained in a generative adversarial network (GAN) setting. In this paper, we propose a theoretical framework to analyze the effect of the GAN discriminator on Langevin-based sampling, and show that in IPM GANs, the optimal generator matches {\it score-like} functions, involving the flow-field of the kernel associated with a chosen IPM constraint space. Further, we show that IPM-GAN optimization can be seen as one of smoothed score-matching, where the scores of the data and the generator distributions are convolved with the kernel associated with the constraint. The proposed approach serves to unify score-based training and optimization of IPM-GANs. Based on these insights, we demonstrate that closed-form discriminator guidance, using a kernel-based implementation, results in  improvements (in terms of CLIP-FID and KID metrics) when applied atop baseline diffusion models. We demonstrate these results by applying closed-form discriminator guidance to denoising diffusion implicit model (DDIM) and latent diffusion model (LDM) settings on the FFHQ and CelebA-HQ datasets. We also demonstrate improvements to accelerated time-step-shifted diffusion, when coupled with a wavelet-based noise estimator for latent-space image generation.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
**Summary**  
This paper seeks to extend the concept of discriminator guidance to the Integral probability metric(IPM) GAN model, with the ultimate goal of applying this framework to diffusion models.   
This paper derives a more general solution to the GAN-generator optimality using mathematical proof from the **Theorem 1**(optimal f-GAN generator). From this general solution, this paper aims to achieve the goal of **Closed-form Discriminator Guidance**. Following the mathematical approaches, this paper presents a series of comprehensive experiments.  

**Contribution**  
In addressing generative models, the concepts from GAN have been applied to diffusion model. While prior attempt focused on applying the discriminator of standard GAN to diffusion, this paper expands on that by applying the discriminator from the IPM-GAN framework to diffusion models.

### Strengths
**Originality & Significance**  
- This paper derive the more general solution to optimal GAN generator. 
- Make connection between the solution to optimal IPM-GAN generator and diffusion model.

**Quality**
- This paper demonstrates superior performance in terms of metrics and training time.

**Clarity**
- This paper employs mathematical proof to substantiate its claims.
- In **5.1 ablations** and **Appendix**, the paper rigorously designs and presents robust experiments that substantiate its claims.

### Weaknesses
1. It would be better if you could give the explanation for transition from GAN generator optimality to discriminator optimality.  
: This paper discusses GAN's alternating optimization and the optimality of the GAN generator. Subsequently, it mentions the transfer of generator optimality to discriminator optimality, but lacks sufficient explanation. Specifically, the paper needs to clarify how the optimal generator at iteration *t*, derived from minimizing the convolution between the density difference and the gradient of the optimal discriminator kernel, directly informs the update of the discriminator at iteration *t+1*. The connection between minimizing the generator's objective and the subsequent discriminator update is not explicitly detailed, leaving a gap in the theoretical justification.

2. In lines 519 (520) - 521, how can this paper assert that 'there is a stark jump initially of about ___10 or so steps___ via the ~'?  
: Further explanation or experimental results are required for those figures. The claim of a 'stark jump' needs to be supported by more rigorous analysis. It's unclear what specific metric is being used to measure this jump, and how the value of '10 or so steps' is derived. A more detailed explanation of the experimental setup and the data used to support this claim is needed. For instance, providing a plot of the time-step shift over multiple images would be beneficial.

3. Need more ablation for ___DG*___.  
In lines 454 (455) - 457 (458), where it states, 'Motivated by the fact ~ not accurate.' the paper asserts that ___DG*___ is not always useful. Subsequently, in section 5.1, the paper presents results for the first $T_D$ = {50, 100, 200} steps using the discriminator.  
Why does the paper focus only on the first $T_D$ steps? What about the later stages of training? Could you provide some toy examples or explanations to clarify this? The paper should explore the impact of applying discriminator guidance at different stages of the diffusion process, not just the initial steps. It's unclear why the discriminator guidance is limited to the first $T_D$ steps and what the effect of applying it later would be. The lack of ablation studies on the later stages of training leaves a gap in understanding the full potential and limitations of the proposed method.


**Typos**
1. In line 199 : $\epsilon$ -> $\epsilon_t$

### Questions
1. In line 479, what is the meaning of $w_{dg, 0}$?  
Table 2 may need to be revised for clarity.  


2. In the last paragraph of section 5, it appears that the ablation study for $T_D$ is conducted with respect to WANDA.  
However, how is this approach applied to LDM-DG? What is the justification for selecting $T_D = 50 $ for LDM-DG$^*$?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
1

### Summary
**Disclaimer**: I am not familiar with the theorem of optimal GANs. While I briefly reviewed some related works referenced in this paper, I am still not confident in assessing the significance or complete accuracy of the conclusions for the GANs. My rating is primarily based on the experimental results of using this form in diffusions. I am open to discussing this further with the author or other reviewers.

This paper proves the analytical form for optimal generators in IPM GANs. The authors then connect this form to score matching. Then, the authors develop a closed-form discriminator guidance for diffusion models.

### Strengths
1. This paper extends previous conclusions on $f$-GAN and on IPM GAN discriminators to IPM GAN generators. 
2. The optimal IPM GAN generators naturally connect to diffusion models.
3. The proposed discriminator guidance is plug-and-play. Unlike previous discriminator guidance, it does not require additional training and seems compatible with different DM frameworks.

### Weaknesses
As I disclaimed, I am not confident in assessing the significance or complete accuracy of the conclusions for the GANs. Therefore, my questions and concerns will mainly be related to experiments.

1. Experimental results are not fully convincing to me. I did not see gains on CIFAR-10 and ImageNet-64 datasets using the proposed discriminator guidance. 
The authors claimed that the proposed guidance could accelerate convergence, leading to fewer time steps in image generation. However, by looking at Fig 15 and 16, it is very obvious that the results of the guidance are much worse than the baseline. It is unclear if the proposed approach is better in the Pareto sense, achieving the same quality with fewer steps, or better quality with the same number of steps. The current results suggest a trade-off where fewer steps lead to worse quality. A more compelling demonstration would show that for a fixed computational budget (e.g., number of function evaluations), the proposed method achieves superior performance. Also, visually checking the results is not enough; FID or other metrics need to be provided for a fair comparison.


2. Experimental settings are not fully clear. If I understand it correctly, the score is estimated by the MC estimators. However, I think I missed the details on the number of samples. Also, the MC estimator requires a batch of generated samples. I did not find details of how this is obtained. I guess it is only possible to draw a batch of samples (instead of 1) at each sampling time. Is this correct? In this way, we can use the samples at the last time step in this batch for the MC estimator.
If this is the case, I would be curious how the number of samples influences the performance. Especially in large-res applications like text-2-image generation, requiring a large batch for each prompt seems too much.

3. I am also a bit confused on the ablation. In Table 2, it seems that the more steps you apply discriminator guidance, the worse result you are getting. So what is the results when $T_D=0$ (w/o any discriminator guidance)? I saw there is one line saying that there is a surge around $T_D=10$. However, seeing this in plots or tables would be more convincing. Also, why Table 2 only shows different $T_D$ for WANDA. What about LDM+DG? It is unclear how the performance changes as $T_D$ increases, and if there is a trend of FID decreasing first and then increasing with $T_D$. The absence of baseline performance ($T_D=0$) in the table makes it difficult to assess the impact of the guidance.

### Questions
1. Line 297-299: 
>From Lemma 3, we see that the gradient field of the kernels convolved with the density difference, and the data score $\nabla ln p_d(x)$, serve similar purposes, which is to output an arbitrarily large value at data sample location, and low values elsewhere.

I am quite confused about this: I did not see the data score in Lemma 3?

2. Line 374-376: 
>Since the proposed approach suggests the interoperability of the score and the discriminator-kernel gradient in Langevin flow, we also consider discriminator-guided Langevin sampling on the CIFAR-10 and ImageNet-64 datasets, considering EDMs as the baseline

Do you mean just adding the discriminator-kernel gradient and the score together (with some weighting for the guidance strength)? 
Also, for guidance, how do you choose the guidance strength?


3. what does the (RGB Color online) mean in the caption in figures?

### Soundness
3

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
This paper derives a closed form expression for the IPM-GAN discriminator, whose gradient is then used to perform Langevin sampling or guide diffusion generation.

### Strengths
**Originality** : this paper is original in the aspect that it uses closed-form expressions for the optimal discriminator instead of discriminators parametrized by neural nets. It is also, to the best of my knowledge, the first paper to use IPM-GAN discriminators for diffusion sampling and guidance.

**Quality** : this paper provides some theoretical grounds for using IPM-GAN discriminators over f-GAN discriminators for diffusion. Some experiments on toy and image datasets are also provided as evidence that the proposed discriminator guidance improves sample quality.

**Clarity** : motivation as well as main theoretical results are presented clearly in the main text. In particular, in Section 3.1, the authors do a good job of explaining how IPM-GAN discriminator guidance could be better than f-GAN discriminator guidance.

**Significance** : this paper provides some theoretical grounds for how diffusion and GANs could be used synergistically to enhance generative performance.

### Weaknesses
 **Missing theory** : there is no guarantee that the proposed discriminator-based generator process correctly samples from the data distribution. The paper lacks a rigorous convergence analysis for the proposed method, particularly when combined with the stochasticity of Langevin sampling. The theoretical justification relies on results from GAN literature and gradient flows, which do not directly apply to the stochastic sampling process used here. Specifically, the paper does not address how the discriminator gradient, when combined with noise, provably guides the sampling process towards the data distribution. The authors use results from Lunz et al. which are for deterministic gradient flows, not stochastic Langevin dynamics. The paper also lacks a clear explanation of how the discriminator guidance interacts with the noise term in the Langevin update, and whether this interaction preserves the convergence properties of the diffusion process. 

**Missing baselines** : while there may be other relevant baseline methods, the paper is missing comparison with the most important baseline - discriminator guidance [1]. The authors *must* compare the proposed method with [1] if they wish to support the claim that IPM-GAN discriminator guidance provides improvement over f-GAN discriminator guidance. In addition, if the authors wish to claim that the proposed method accelerates diffusion sampling, they must compare with additional relevant baselines such as [2,3]. The paper needs to show that the proposed method offers a genuine improvement over existing discriminator guidance techniques, and not just a different approach. Furthermore, the paper needs to demonstrate that the proposed method accelerates sampling compared to other methods that focus on improving the numerical integration of the diffusion process. 

**Missing ablation** : there is no ablation w.r.t. number of data samples used when approximating the optimal discriminator. Is this because a large number of samples is needed to obtain reasonable results?

### Questions
**Q1** : Why does the proposed method accelerate diffusion sampling? My understanding is that IPM-GAN discriminator guidance mitigates the mismatch between model distribution and the true data distribution at each time $t$. Sampling acceleration is related to minimizing the truncation error during numerical integration of the diffusion SDE/ODE as we reduce the number of function evaluations.

**Q2** : At lines 254-255, what do the authors mean by *the kernel $\kappa$ is the Green's function to the differential operator governing the optimal discriminator*? Please provide a concrete equation of $\kappa$ in relation to $D$.

**Q3** : Does the generative process defined by closed form discriminator gradients generalize beyond training data? In other words, how do we know whether the generative model is not simply memorizing the training dataset?

### Soundness
2

### Presentation
3

### Contribution
2
