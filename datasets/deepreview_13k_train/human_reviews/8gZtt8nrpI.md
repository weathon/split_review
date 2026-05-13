# Diffusion Models With Learned Adaptive Noise Processes

- Decision: Reject
- Scores: 6, 5, 5, 6

## Abstract
Diffusion models have gained traction as powerful algorithms for synthesizing high-quality images. Central to these algorithms is the diffusion process, which maps data to noise according to equations inspired by thermodynamics, and which can significantly impact performance. In this work, we explore whether a diffusion process can be learned from data. We propose multivariate learned adaptive noise (MULAN), a learned diffusion process that applies Gaussian noise at different rates across an image. Our method consists of three components—a multivariate noise schedule, instance-conditional diffusion, and auxiliary variables—which ensure that the learning objective is no longer invariant to the choice of noise schedule as in previous works. Our work is grounded in Bayesian inference and casts the learned diffusion process as an approximate variational posterior that yields a tighter lower bound on marginal likelihood. Empirically, MULAN significantly improves likelihood estimation on CIFAR10 and ImageNet, and achieves ~2x faster convergence to state-of-the-art performance compared to classical diffusion.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper suggests a method for teaching diffusion models to adapt their noise schedules in order to increase the ELBO (Evidence Lower BOund). The authors observe that if the noise schedule is expanded to include multiple variables, the ELBO for diffusion models will change depending on the noise schedule. This variation allows for the noise schedule to be optimized at the same time as the diffusion model parameters to enhance likelihood. The authors also explore instance-conditional diffusion along with auxiliary variables. They discovered that using these multivariate noise schedules combined with auxiliary variables enables the training of diffusion models that not only surpass previous benchmarks in terms of likelihood but also converge more quickly.

### Strengths
* The paper under review brings to light that the Evidence Lower BOund (ELBO) for continuous-time diffusion models, as described in the Variational Diffusion Model (VDM) paper, remains unchanged across various noise schedules only when the noise is univariate. It presents a novel finding that for multivariate noise schedules, the ELBO transforms into a line integral and varies with different noise schedules. This is insightful and could pave the way for further research in diffusion models.

* While VDM sets a challenging benchmark in terms of log-likelihoods, the paper in question surpasses these results, which is very impressive.

* Although the use of auxiliary variables in diffusion models isn't a new concept, the approach of conditioning noise schedules on such variables, as shown in this paper, is a valuable contribution that enhances model likelihoods.

* The clarity of the writing and the effective presentation of the paper are commendable.

### Weaknesses
 * The concept of multivariate noise schedules is intriguing; however, it appears that it does not function effectively by itself and requires auxiliary variables for better performance. This raises the question of whether the combined learning of noise schedules and the diffusion model is advantageous. Specifically, it's unclear if the added complexity of learning a multivariate noise schedule is justified, given that the performance gains seem to rely heavily on the inclusion of auxiliary variables. A more thorough analysis of the individual contributions of each component (multivariate noise vs. auxiliary variables) would be beneficial.

* The potential improvements for Variational Diffusion Models (VDM) through the use of auxiliary latent variables remain unclear. It would be helpful to understand the significance of these variables in enhancing the likelihood. Although the authors have provided ablation studies for MuLAN without multivariate aspects, it's uncertain whether this is directly comparable to VDM with an auxiliary variable due to possible differences in noise schedule parameterization. The core issue is that the paper doesn't clearly isolate the effect of the auxiliary variables on VDM's performance, making it difficult to assess their true value.

* The authors justify the learning of noise schedules based on the manual adjustment of such schedules in high-resolution image diffusion models. Yet, they focus on maximizing the Evidence Lower Bound (ELBO) for their learning method, while current diffusion models tend to optimize a different objective that emphasizes perceptual quality of samples. Whether their method is applicable or beneficial when the goal is not ELBO is not clear. This discrepancy between the motivation (manual tuning for perceptual quality) and the optimization objective (ELBO) raises concerns about the practical relevance of the proposed method for real-world applications where perceptual quality is paramount.

* Additionally, the discussion of related works could be more comprehensive. The paper frequently refers to continuous-time diffusion models but often overlooks citation [1], from which such models originate. The authors could provide a more thorough background for readers by acknowledging concurrent works [2] and [3], which propose the same ELBO for continuous-time diffusion models. This inclusion would add value to the context in which VDM is discussed.

### Questions
I would like to hear the authors' thoughts on the weaknesses identified above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors provided a theoretical argument that creating a noise schedule for each input dimension and conditioning it on the input yields improved likelihood estimation, which means noise with different covariance matrices can be applied to the inputs. Furthermore, the authors introduced a novel method to condition the noise schedule on the input via a latent distribution. Empirical experiments are made to demonstrate the effectiveness and efficiency of the new proposed model.

### Strengths
1. This paper is well written. The presentation is good and the reference list is complete. 
2. The experiments in this paper is quite solid.

### Weaknesses
1. I recommend the authors show some generated images as well as the comparison with other existing models, so that we can see the improvement more clearly. 
2. The theory proposed by the authors only showed us the pipeline of this model. For the reason why polynomial noise scheduling is better than the existing constant/linear/exponential noise scheduling still remains unclear. If it is difficult to obtain a solid theorem, I think it necessary to explain it more. 
3. The idea proposed is not so impressive in my opinion, but it is not a serious weakness since the authors have done solid experiments and made the polynomial noise scheduling model come true.

### Questions
1. Do you use pretrained score estimator, or you trained your own? Since the polynomial noise scheduling is originally proposed by you, there are no pretrained score estimators to use I guess. Is it right?
2.There are no more additional questions. The authors only need to answer my questions in the "weakness" section.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this work, the authors propose using an instance-dependent multivariate Gaussian noise scheduling and auxiliary latent variables to improve the likelihood estimation. Their method demonstrates strong performance in terms of negative log-likelihood (**NLL**) and convergence.

### Strengths
1. Overall, this paper is clearly written and easy to follow. The idea is simple, narrowing the gap between marginal log-likelihood and its evidence lower bound (**ELBO**) by specifying a more flexible family of approximate variational posteriors, which is a standard approach in variational inference. The relevant derivations in the paper are also straightforward.
2. The paper studies the effect of an adaptive multivariate Gaussian noise schedule on the likelihood estimation performance, which can be potentially combined with other techniques to improve the metric. The proposed method, MULAN, is also found advantageous to previous SOTA generative modeling methods in likelihood estimation and convergence. The ablation study underscores the indispensable synergy between the method's core components: the auxiliary variable and the multivariate Gaussian noise scheduling.

### Weaknesses
1. The intuition behind using a non-identical pixel-wise Gaussian noise schedule from a frequency perspective (e.g., texture and shape, which are mainly perceptual) is not convincing. It is known that likelihood generally does not correlate with sample quality and visual appearance [1]. The connection between the proposed adaptive noise schedule and the frequency domain is tenuous at best, and it's unclear how this specific parameterization of the noise schedule is theoretically justified or why it would lead to improved likelihood estimation. A more rigorous explanation of why instance-dependent noise based on pixel-wise variations would be beneficial is needed.
2. As mentioned in the paper, the proposed method itself does not contain much novelty. The use of multivariate non-isotropic Gaussian noise scheduling and the introduction of an auxiliary variable in diffusion models are not new [2,3]. The mathematical derivations presented in this paper largely mirror previous work. The combination of these techniques, while potentially effective, lacks a significant theoretical contribution that would justify its novelty. The specific parameterization of the multivariate noise using a polynomial, while claimed to be novel, is not fundamentally different from other parameterizations used in related works.
3. The introduction of an auxiliary variable does not necessarily agree with the objective of narrowing the posterior gap. In Section 3.3.2, the right-hand side of the first inequality, i.e., Equation (7), to my understanding, is the same as the ELBO of a variational autoencoder. If the actual objective of MULAN is based on the second inequality, then the ELBO w.r.t. $(x, z)$ would act as a bottleneck of the ELBO w.r.t. $(x_0, x_{1..T}, z)$. This point raises a concern about the theoretical soundness of the method, as the auxiliary variable might introduce a tighter bound but not necessarily a better approximation of the true posterior. The authors need to provide a more detailed explanation of how the introduction of the auxiliary variable does not worsen the posterior gap.
4. The experiment results are rather not impressive. As mentioned in the paper, the authors implement their method based on the VDM codebase and adopt the same settings for the most part. VDM is almost the strongest model excluding i-DODE and MULAN (this work) in the main table (Table 1). Although the improvement of the proposed method seems significant compared with other methods, it is far less impressive relative to the result by VDM (the method it is built upon), considering the extra degrees of freedom. The marginal gains in performance, especially given the increased complexity of the model, do not strongly justify the proposed method's practical value. A more substantial performance improvement would be needed to demonstrate the method's effectiveness.
5. Typos:
	Appendix C.1 prexisting -> pre-existing

### Questions
1. How is BPD calculated? Is it calculated by the stochastic VLB or ODE-based exact likelihood computation methods? If the reported metric of MULAN is obtained by the former one, what is the variance of it? And what effect does the choice of log-SNR parameterization have on the variance? I think the variance of stochastic VLB matters in this case when it is used to compare the proposed method with others including VDM. VDM explicitly minimizes VLB variance with a learned noise schedule whereas MULAN does not. 
2. Does the authors try to analyze the auxiliary context variables? Do they have interpretable meaning? If so, it might also be a way to do representation learning and controllable generation. In the paper, the auxiliary variables are also referred to as the context and are said to "encapsulate high-level information".

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors propose a method to learn the parametric diffusion noise schedule by jointly optimizing model parameters and diffusion parameters. In addition, the authors propose a learning method for conditional diffusion via a latent distribution.

### Strengths
1. The proposed approch that learns an adaptive diffusion noise schedule is somewhat novel.   

2.  The paper is well-written and well-organized.

### Weaknesses
1.  The authors argue a novel approch that learns conditional diffusion via auxiliary latent variables.  
 However,  the relationship and difference compared with (Wang et al. 2023) is not clearly discussed. Specifically, the paper does not delineate the precise architectural and algorithmic differences, making it difficult to assess the novelty of the proposed approach. It is unclear if the auxiliary latent variables are used in a fundamentally different way, or if the differences are merely implementation details. A more detailed comparison, highlighting the specific mathematical formulations and algorithmic steps that distinguish the proposed method from existing work, is needed.


2. The advantage of the proposed approch via auxiliary latent variables is not well supported.   In Figure 1 (a), it seems that MuLAN w/o auxiliary latent variable performs worse than the standard VDM.  This raises concerns about the necessity and effectiveness of the auxiliary latent variables. The paper should provide a more thorough analysis of why and when the auxiliary latent variables improve performance, perhaps by showing ablation studies that isolate the effect of the auxiliary variables under different conditions. The current results suggest that the auxiliary variables may not be contributing positively to the overall performance.


3. The empirical results can not support the claimed advantage of the proposed method MULAN .  In Table 1, it seems that the proposed method MULAN   performs worse than i-DODE∗ (Zheng et al., 2023). The performance of MuLAN is not competitive with the state-of-the-art, which undermines the paper's claims of advancement. The paper needs more convincing empirical evidence to demonstrate the superiority of the proposed method, especially in comparison to existing state-of-the-art methods. The current results suggest that the proposed method may not be a significant improvement over existing methods.

### Questions
Q1.  The empirical results are not convincing enough to demonstrate the advantage of the proposed method.  Could the authors provide additional empirical evidence to support the claim?

Q2.  It seems that the proposed method incurs additional time complexity. Could the authors provide additional running time comparison with baselines?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
