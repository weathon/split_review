# Prompt-tuning Latent Diffusion Models for Inverse Problems

- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 6, 3, 6

## Abstract
We propose a new method for solving imaging inverse problems using text-to-image latent diffusion models as general priors. Existing methods using latent diffusion models for inverse problems typically rely on simple null text prompts, which can lead to suboptimal performance. To address this limitation, we introduce a method for prompt tuning, which jointly optimizes the text embedding on-the-fly while running the reverse diffusion process. This allows us to generate images that are more faithful to the diffusion prior. In addition, we propose a method to keep the evolution of latent variables within the range space of the encoder, by projection. This helps to reduce image artifacts, a major problem when using latent diffusion models instead of pixel-based diffusion models. Our combined method, called P2L, outperforms both image- and latent-diffusion model-based inverse problem solvers on a variety of tasks, such as super-resolution, deblurring, and inpainting.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposed a method (P2L) for prompt-tuning latent diffusion models to solve inverse problems. The method jointly optimises the latent variables/prompts on-the-fly and reconstructs the image through the inverse diffusion process. The prompt tuning step helps to tailor the model to the specific task of solving the inverse problem, while the projection step helps to ensure that the generated images are realistic and free of artefacts. The experiments on super-resolution, deblurring and inpainting demonstrate the effectiveness of P2L.

### Strengths
(1) The idea of learning prompts to guide the diffusion models for inverse problems is very interesting.

(2) The method is technically sound.

### Weaknesses
The paper lacks a theoretical analysis of, for example, convergence.

The results are not very promising.
(1) From Table 1, the performance (PSNR) gains of P2L are subtle.
(2) From the ablation experiments in Table 4, the difference between the results obtained by not using any of the three proposed modules and the results obtained by using all of them is not significant.
(3) From Table 5, the proposed proximal calibration is not that superior to the projection-based calibration, which is even cheaper and faster.

### Questions
(1) I'm curious if you have tried to figure out the text corresponding to the learned prompt. As shown in Table 1, including the methods presented in this paper and PALI's for prompt generation, what kind of textual information do they represent? I am curious about the interpretability of the prompts.

This may be important for e.g. medical image reconstruction, or at least it is unclear to me whether there are reasonable (textual) prompts to guide the reconstruction of medical images.

(2) In algorithms 1-4 there are two functions called 'OptimizeEMB', which 'OptimizeEMB' do you use in algorithm 4?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper focuses on solving inverse problems using a new method based on (latent) diffusion models. Prior works using similar generative priors only update the latent variables while keeping the text-prompt null in most cases. The authors motivate their approach by showing experiments where better text-conditioning helps achieve a significant gain in performance. Finally,  the authors propose a method that optimizes the null-embedding along with latent variables to minimize the measurement error. It extends the prior works done by Rout et al. and He et al. to optimizing the null-embeddings in addition to the latents. In addition, the authors propose a projection step to ensure that the generated image resides in the range space of the decoder. Extensive experiments on FFHQ and ImageNet are conducted to support the claims.

### Strengths
1. Optimizing the null-embeddings in addition to the latents is a strong contribution and very useful in several downstream applications.
2. The authors achieve state-of-the-art performance in several tasks.
3. The paper is well-written and the main points are clearly discussed with sufficient details to reproduce the results.

### Weaknesses
1. In Section 3.2, the authors conduct an experiment using PSLD to show that it always diverges even if it started from a clean image. I believe that this experiment does not offer any insights because of two reasons:
(i) The approximation used is not what was proposed in PSLD. In fact, the authors of PSLD show that aiming for any fixed point is not a good idea. Instead, they prove that the gluing objective helps recover the unique fixed point that exhibits contraction towards the optimal solution in a linear setting (Theorem 3.6).
(ii) The fixed point solver works only for a unique step size (Theorem 3.5). Therefore, it is hard to to get any meaningful conclusion from this experiment unless the step size is properly tuned or gluing objective is used instead.

Also, what task was considered in this experiment?

2. An important point to discuss is that the gluing objective is in fact projecting onto the measurements. But it uses the analytical solution and does one step of gradient descent to save computational time. So the trade-off between performance and speed should be discussed in the proposed projection optimization step.

3. Choice of $\tau$: It is obvious that multiple steps of gradient descent would lead to better results than a single step. To make a fair comparison, I believe the running time should be compared. In addition, there is another optimization problem being solved at every step of diffusion to get the near-optimal embeddings.

4. The description about PSLD in the paragraph below eq. (6) is not fully correct. PSLD shows that there exists a step size for which guiding towards the fixed point is a good idea. Not for any step size.

5. Analysis of the proposed algorithm in a  simple linear model setting might be helpful to better understand the contributions in terms of convergence guarantees.

### Questions
1. How do you go from equation (11) to (12)? It is assumed that $C$ and $z_t$ are independent. However, this assumption is not properly justified?
2. Footnote 3 on page 5 is not the finding of this paper. It was shown in prior works (e.g. PSLD) that naively scaling DPS does not work. 
3. How many $C$ updates per $z_t$ update is needed? How does that affect the number of neural function evaluations? This  should be discussed properly in the main draft.
4. The use of some params like K is not clearly shown in Algorithm 2. It should be used as an argument to the optimization block.

-----------------------------------
## After discussion:
I thank the authors for their response. The idea of tuning the prompts used in SoTA inverse problem solvers is an important contribution. However, the proposed algorithm currently takes around **30 mins** to process **one single image** as opposed **5 mins for DPS** and **7 mins for PSLD/GML-DPS**. I understand that the current work is at its early stage and its runtime might improve in the near future. I believe the current score "marginally above acceptance threshold (6/10)" is a good assessment of the proposed method. Therefore, I am planning to keep my score.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes to use text prompt with iterative optimization for solving imaging inverse problems and constrains the evolution of latent variables using projection. Experimental results on high-resolution inverse problems show that the proposed method outperforms several DIS and LIDS methods on a variety of tasks.

### Strengths
1.  The motivation of using learnable prompt to improve the performance is meaningful. 
2.  Experiments on different kinds of image inverse tasks including super-resolution, deblurring, and inpainting are performed.

### Weaknesses
1.  The writing is poor and the submission is hard to follow. 

2.  Why we need iterative optimization similar to EM algorithm for optimizing text prompt and latent variable? The submission lacks necessary theoretical analysis and experimental evaluation. 

3.  The proposed projection is similar to that proposed in Chung et al. (2023b). Why the proposed approach can provide a good regularization is not clearly elaborated and why this approach is named projection is not clear. 

4.  No further analysis on why the proposed projection can target any resolution and only subjective descriptions are proposed.

5. The practicality of the proposed method is limited. The proposed P2L appears to be significantly slow. It necessitates 1000 reverse diffusion steps to achieve the results presented in the paper, each consisting of K backward propagations (BP) through the LDM for prompt tuning and 1 BP for a DPS-like step. It means that P2L could potentially be K times slower than DPS. 

6. The lack of experiments on the commonly used datasets of size 256x256 provides less evidence to support that the proposed prompt tuning is useful. The performance of the compared baselines on datasets of size 512x512 reported in this paper is unreliable. For example, there is a substantial degradation in performance for DIS methods, which may attribute to the high sensitivity to hyperparameters of these methods. I suggest the authors to add experiments on datasets of size 256x256 for fair comparison. 

7. Comparison with the DIS method termed PGDM [R1] should be included. It does not require extensive hyperparameter tuning. Additional comparison with it on datasets of size 512x512 would be beneficial to demonstrate the strength of the proposed method. 

### Questions
Please refer to the Weaknesses.

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper aims at solving image inverse problems using latent diffusion models. Two main contributions are included. The first is that the authors introduce a method for prompt tuning, i.e., a way to automatically find the right prompt to condition diffusion models when solving inverse problems. The second is that the authors propose a method to keep the evolution of latent variables within the range space of the encoder, by projection optimization. According to the presented experiment, the proposed method seems to outperform existing state-of-the-art.

### Strengths
The idea of automatic prompt-tuning is novel and effective. The overall performance achieves state-of-the-art in solving image inverse problems.

### Weaknesses
The whole pipeline is somewhat complicated, involving many pyper-parameters which may be difficult to tune, as shown in Table 6.

The proposed method seems to be expensive in computation. Reports on the inference time are necessary.

Although I believe that the proposed method can solve large-scale inverse problems, there is no experimental evidence to prove that. It is recommended that the appendix provide more experimental results with general large images.

The authors mentioned range space projection, which is highly related to DDNM [1] and should be discussed.

### Questions
Please see the Weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
