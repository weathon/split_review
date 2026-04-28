# Learning Energy-Based Models by Cooperative Diffusion Recovery Likelihood

- Decision: Accept
- Avg Score: 6.80
- Scores: 8, 6, 6, 6, 8

## Abstract
Training energy-based models (EBMs) on high-dimensional data can be both challenging and time-consuming, and there exists a noticeable gap in sample quality between EBMs and other generative frameworks like GANs and diffusion models. To close this gap, inspired by the recent efforts of learning EBMs by maximizing diffusion recovery likelihood (DRL), we propose cooperative diffusion recovery likelihood (CDRL), an effective approach to tractably learn and sample from a series of EBMs defined on increasingly noisy versions of a dataset, paired with an initializer model for each EBM. At each noise level, the two models are jointly estimated within a cooperative training framework: samples from the initializer serve as starting points that are refined by a few MCMC sampling steps from the EBM. The EBM is then optimized by maximizing recovery likelihood, while the initializer model is optimized by learning from the difference between the refined samples and the initial samples. In addition, we made several practical designs for EBM training to further improve the sample quality. Combining these advances, our approach significantly boost the generation performance compared to existing EBM methods on CIFAR-10 and ImageNet datasets. We also demonstrate the effectiveness of our models for several downstream tasks, including classifier-free guided generation, compositional generation, image inpainting and out-of-distribution detection.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a novel training algorithm for jointly training an energy-based model (EBM) and an initializer model. The initializer has a very similar form to DDPM, so the proposed method can be viewed as a cooperation of EBM and DDPM.

### Strengths
* The overall exposition is clear to follow.
* The proposed algorithm, CDRL, shows a clear improvement over Diffusion Recovery Likelihood (DRL), an algorithm that CDRL is based on. The sample quality (in FID) is improved while the required computation (in MCMC steps) is reduced.
* CDRL demonstrates broad applicability over multiple tasks outside image generation, such as compositional generation and out-of-distribution detection.

### Weaknesses
 * The empirical performance of CDRL is good but not very strong. It is clear that CDRL is an improvement over DRL, but it still falls behind other models in multiple tasks.
    * The initializer is very similar to DDPM, but CDRL's unconditional CIFAR-10 FID is worse than DDPM (Table 1). Specifically, while DDPM achieves a FID score in the low 2s, CDRL's FID is in the mid-3s, indicating a significant gap in sample quality. This difference is notable given the conceptual similarity of the initializer to DDPM.
    * Also in Table 3, CDRL is outperformed by DDPM++. The performance gap is not marginal; DDPM++ achieves a significantly better FID score, which questions the competitiveness of CDRL in high-fidelity image generation.
* In the out-of-detection distribution (OOD) experiment (Table 4), OOD detection capability is evaluated on only three test datasets, and the number of test OOD datasets is too small. It is important to use diverse test OOD datasets in evaluation because an OOD detector needs to detect any possible outliers. The current practice typically uses at least five OOD datasets that have different visual characteristics. Also, SVHN is known to be a highly challenging OOD dataset, particularly for generative models [1], but not included in Table 4. It would be great to see CDRL is able to detect SVHN as OOD. The lack of SVHN, a well-established benchmark for OOD detection, undermines the robustness of the OOD evaluation. Additionally, the chosen datasets lack diversity, potentially leading to overly optimistic results that may not generalize to other types of outliers.
* It would be nice if the authors could comment on the consistency of the model after adding the initializer model. Would it alter the consistency?

### Questions
See weaknesses.

===
The authors have addressed my questions in detail.

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes several techniques for improved training of diffusion recovery likelihood models, such as
- learning an initializer model for MCMC,
- noise variance reduction for reducing gradient variance.

This paper shows application of the proposed model to
- conditional generation and classifier-free guidance,
- compositional generation,
- OOD detection.

### Strengths
- The paper is clearly written and easy to read.
- CDRL shows clear performance improvements over previous EBM-based generative models.
- CDRL can be applied to tasks such as unconditional generation, conditional synthesis, likelihood estimation, OOD detection, composition, etc. Such tasks were unexplored in the original DRL paper [1].

[1] Learning Energy-Based Models by Diffusion Recovery Likelihood, Gao et al., ICLR, 2021.

### Weaknesses
I am inclined to give the score "marginal accept" for the following reasons.
- The proposed method is a straightforward combination of two known techniques, DRL [1] and MCMC amortization [2,3]. While the simplicity of the idea is practically appealing, the idea lacks theoretical novelty. Moreover, the tasks demonstrated in the paper are already well-explored in the diffusion model literature, and the algorithms for the tasks are straightforward extensions of diffusion-based ones, as the score is just the gradient of the energy. For instance, classifier-free guidance is explored in [4], and compositional generation is explored in [5]. Specifically, the application of MCMC amortization to DRL, while practically beneficial, does not introduce new theoretical insights into the underlying energy-based model framework itself. The tasks, such as conditional generation and compositional synthesis, are essentially achieved by leveraging the score function, which is analogous to how diffusion models operate, thus the paper does not demonstrate a unique capability of EBMs.
- The paper lacks a comparison of inference time for CDRL and the baselines. It is crucial to understand the practical trade-offs in terms of sampling speed. The paper should include a detailed analysis of the number of function evaluations (NFEs) and wall-clock time required for CDRL compared to other EBM based methods, and diffusion models. This is critical for assessing the practical viability of the proposed method.
- The paper lacks a comparison of training cost (e.g., required VRAM) for CDRL and the baselines. I expect CDRL training is more expensive than diffusion or DRL training, as the former requires two networks while latter only one. The training cost comparison should include metrics such as GPU memory usage, training time, and the number of parameters in each network. Without these details, it is difficult to assess the computational overhead of the proposed approach.
- The paper lacks results on higher resolution (e.g., 256x256) images. The experiments are limited to relatively low-resolution images. This limits the assessment of the method's scalability and ability to generate high-fidelity images, which is a crucial aspect for practical applications.

### Questions
- I am curious about the authors' opinion on the practical benefits of CDRL vs. diffusion. Specifically, tasks that can be achieved with CDRL can also be achieved by diffusion, and vice versa, using the relation that the gradient of the energy is the score. I also observe that hyper-parameter choices in this paper are heavily influenced by those of diffusion models. Moreover, while CDRL uses fewer noise levels than diffusion models (e.g., 1000 levels), recent works on fast diffusion sampling have reduced sampling time for diffusion significantly (e.g., 2.87 FID on CIFAR10 with NFE=20 [1]). I think this naturally leads us to wonder what are the strengths of CDRL compared to diffusion.

[1] DPM-Solver: A Fast ODE Solver for Diffusion Probabilistic Model Sampling in Around 10 Steps, Lu et al., NeurIPS, 2022.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes the Cooperative Diffusion Recovery Likelihood (CDRL) for training energy-based models. Compared with the baseline DRL, CDRL introduces an extra initializer model that is jointly trained with the EBM along the diffusion process. The required MCMC steps are reduced thanks to a better initial sample.  
The experiments show that CDRL has significantly improved over the baseline DRL method. 

Besides the proposed method, the paper also discusses some other aspects of EBMs such as noise scheduler designs, classifier-free guidance, etc.

### Strengths
The paper is well-organized and easy to follow. 
I think the highlight of this paper is the strong empirical performance of CDRL. The work shows the possibility of achieving an FID on image benchmarks at least comparable to other generative models such as GANs and diffusion models. 
The ablation studies are convincing as validation of each of the components in the proposed method.

Besides, the introduced classifier-free guidance for EBM is also empirically sound, which verifies many intuitions from diffusion models.

### Weaknesses
My main concern is the lack of novelty. 
The key components are inspired by other works. The DRL is well-established in training EBMs and the idea of a trainable initializer for MCMC is also not new. The combination of them seems a bit hacky to me and the overall method is a little cumbersome.
It would be better if the motivation and necessity of introducing an initializer (because initializers bring additional costs) were explained more clearly with more new insights to DRL. 

Nonetheless, making this idea work empirically is impressive and the generative performance of EBMs has been greatly improved. 
However, the image generation experiment is on very low resolutions. I think it would be more convincing if the method could be shown to be able to handle image generation tasks for higher resolutions;

### Questions
The performance gain, regardless of efficiency, seems to come from a better initial state provided by the cooperatively trained initializer. In this case, I wonder about the limit of the baseline CRL, if we increase the MCMC sampling steps significantly, say 300, what would the performance be?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors propose a new method for learning energy-based models (EBMs) mimicking diffusion models. Specifically, within the diffusion-model framework, EBMs are modified to parameterize the denoising process; to accelerate the MCMC sampling process when training the EBM, the authors also use a simultaneously trained diffusion-like model as an ``initialzer model.'' Experimental results demonstrate the effectiveness of the proposed method.

### Strengths
The presented techniques are likely new.

### Weaknesses
The clarity should be improved. For example, consider the relationships between the proposed method and related works.

The contribution is kind of incremental. Based on the Diffusion Recovery Likelihood (DRL) (Gao et al., 2021) in Sec. 3.1, the authors proposed in Sec. 3.2 a new "initializer model" to amortize the expensive MCMC sampling.

### Questions
1. What are the main contributions of the proposed CDRL when compared with DRL (Gao et al., 2021)?

2. In the paragraph following Eq. (5), why "maximizing recovery likelihood still guarantees an unbiased estimator of the true parameters of the marginal distribution of the data?"

3. Eqs. (6) and (8) are quite like the fomula of the conventional diffusion model. Please elaborate on the relationships between them.

4. It seems that Eq. (9) indicates a deterministic noising process, right? If so, why "there’s still variance for xt given x0 and xt+1?"

5. How to interpret Eq. (11), especially the $\tilde p_{\theta}$?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors study methods for training and sampling from energy-based models (EBMs). 

They propose Cooperative Diffusion Recovery Likelihood (CDRL), which is an extension of Diffusion Recovery Likelihood (DRL). The proposed CDLR aims to improve the sample quality of DLR, while also reducing the number of MCMC steps required during training and sampling. CDLR entails jointly estimating a sequence of EBMs and MCMC initializers, utilizing the cooperative training approach. Essentially, the main proposed method is a combination of DLR (Gao et al., 2021) and cooperative training (Xie et al., 2020).

The proposed method is shown to improve the sample quality of DLR in unconditional generation on CIFAR10 and ImageNet 32x32. It is also applied to some conditional generation (via classifier-free guidance), compositional generation and OOD detection experiments.

### Strengths
The paper is well written overall. I found it interesting to read. The authors definitely seem knowledgeable and familiar with previous work.

The main idea of the proposed method, combining DRL with cooperative training, makes intuitive sense and is described well overall.

The proposed method seems to improve the DLR baseline in experiments.

### Weaknesses
The related work section is placed in the Appendix, which seems quite odd. As a result, the previous work on cooperative training is sort of "hidden" in the main paper. This should be described before Section 3.3.

The similarities and differences between the proposed approach using EBMs and diffusion models could be discussed in more detail. The "Diffusion Model" paragraph in the related work section is interesting, but I think this could be expanded on a lot more.

It is not entirely clear how the resulting EBM differs from diffusion models in terms of the training objective and sampling procedure. The paper could benefit from a more detailed discussion on the specific advantages and disadvantages of using this type of EBM compared to diffusion models, particularly in the context of the reported experiments. The paper lacks a discussion on the computational cost of the proposed method compared to diffusion models, which is a crucial aspect for practical applications.

Would it be possible to compare CDLR with the DLR baseline also in the OOD detection experiment (Table 4)?

Would it perhaps be possible to illustrate / give a schematic overview of the proposed approach in some kind of figure? (a sequence of noise levels, one EBM and initializer model per level etc. I just think that this perhaps could help illustrate the general idea)

The experiment in Figure 7 is interesting. Could you report FID scores for (a) and (b)? I.e., for K=0 and K=15 steps of Langevin refinement. Could this experiment perhaps also be repeated for K=1, 2, 4, 8 steps of Langevin refinement?


Minor things:
- Section 3.1, "...constrains the conditional energy landscape to be localized around y_t": Should y_t be x_{t+1}?
- Abstract, "noisy versons": versons --> versions.
- Section 1, "The initializer model proposes initial samples by making prediction of the samples at the current noise level given": "making a prediction"? "making predictions"? "by predicting the samples..."?
- Section 3.2, "which may again requires MCMC sampling": requires --> require?
- Algorithm 1: noise level --> noise levels, sampling step --> sampling steps.
- Algorithm 2: sampling steps L --> sampling steps K? (also some inconsistency with this in the Appendix)
- 4.4: CDLR strong --> CDLR achieves strong?
- G.5: doesn't gives --> doesn't give (or, "does not give", I suppose)?

### Questions
1. I think that the proposed CDLR method makes sense, and that it seems like a promising method for improving EBM training/sampling. However, it is not entirely clear to me how the resulting EBM differs from diffusion models? What are the main pros and cons compared to diffusion models? Why should one use this type of EBM instead of a diffusion model? When / in which applications should one use this type of EBM?

2. Would it be possible to compare CDLR with the DLR baseline also in the OOD detection experiment (Table 4)?

3. Would it perhaps be possible to illustrate / give a schematic overview of the proposed approach in some kind of figure? (a sequence of noise levels, one EBM and initializer model per level etc. I just think that this perhaps could help illustrate the general idea)

4. The experiment in Figure 7 is interesting. Could you report FID scores for (a) and (b)? I.e., for K=0 and K=15 steps of Langevin refinement. Could this experiment perhaps also be repeated for K=1, 2, 4, 8 steps of Langevin refinement? 



Minor things:
- Section 3.1, "...constrains the conditional energy landscape to be localized around y_t": Should y_t be x_{t+1}?
- Abstract, "noisy versons": versons --> versions.
- Section 1, "The initializer model proposes initial samples by making prediction of the samples at the current noise level given": "making a prediction"? "making predictions"? "by predicting the samples..."?
- Section 3.2, "which may again requires MCMC sampling": requires --> require?
- Algorithm 1: noise level --> noise levels, sampling step --> sampling steps.
- Algorithm 2: sampling steps L --> sampling steps K? (also some inconsistency with this in the Appendix)
- 4.4: CDLR strong --> CDLR achieves strong?
- G.5: doesn't gives --> doesn't give (or, "does not give", I suppose)?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
