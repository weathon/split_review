# Hybrid Regularization Improves Diffusion-based Inverse Problem Solving

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Diffusion models, recognized for their effectiveness as generative priors, have become essential tools for addressing a wide range of visual challenges. Recently, there has been a surge of interest in leveraging Denoising processes for Regularization (DR) to solve inverse problems. However, existing methods often face issues such as mode collapse, which results in excessive smoothing and diminished diversity. In this study, we perform a comprehensive analysis to pinpoint the root causes of gradient inaccuracies inherent in DR. Drawing on insights from diffusion model distillation, we propose a novel approach called Consistency Regularization (CR), which provides stabilized gradients without the need for ODE simulations. Building on this, we introduce Hybrid Regularization (HR), a unified framework that combines the strengths of both DR and CR, harnessing their synergistic potential. Our approach proves to be effective across a broad spectrum of inverse problems, encompassing both linear and nonlinear scenarios, as well as various measurement noise statistics. Experimental evaluations on benchmark datasets, including FFHQ and ImageNet, demonstrate that our proposed framework not only achieves highly competitive results compared to state-of-the-art methods but also offers significant reductions in wall-clock time and memory consumption.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper builds on the concept of denoising regularization (DR) for solving inverse problems. Inspired by recent advancements like Red-Diff, which utilizes denoising score matching as a regularization term, the authors introduce a new approach termed consistency regularization (CR). CR adopts the central idea of consistency distillation (CD), which improves self-consistency by minimizing the difference between outputs at two consecutive reverse sampling points. However, the authors note that a direct application of CD can lead to oversaturation and artifacts due to insufficient randomness in the noise sampling process within CD. To address this, they propose a hybrid regularization (HR) framework, which incorporates hybrid noise modeling from the DDIM formulation. Experimental results suggest that HR achieves state-of-the-art performance in various inverse problem settings.

### Strengths
The use of a hybrid noise model for score distillation is a notable advance compared to DR and CR.

### Weaknesses
Despite its contributions, the paper has several notable limitations. First, to substantiate HR's advantages over DR, a comparative ablation study incorporating the hybrid noise model into the DR framework should have been conducted. The reviewer suspects that HR's benefits stem from mitigating DR's mode-collapse behavior due to the hybrid noise model rather than the use of CR, a point the current manuscript and experiments have not sufficiently addressed.

Second, although the hybrid noise model may appear novel within the Red-Diff framework, the final formulation lacks originality. Specifically, the hybrid noise model and gradient step in equation (11) represent a simplified, one-step version of the decomposed diffusion sampling (DDS) framework [1]. In DDS, the denoised image, obtained through Tweedie’s formula, is updated using a multi-step conjugate gradient (CG) approach, after which hybrid noise is introduced within the DDIM framework. The authors appear unaware of DDS, as there are no comparisons against it.

Third, the reviewer finds the authors' assertion about the growing interest in DR for inverse problems unconvincing. Posterior sampling remains predominant in achieving state-of-the-art results in inverse problems. Moreover, contrary to the authors' claims, recent approaches such as DDS bypass Jacobian computation by leveraging piecewise linear manifold structures. Therefore, this assertion appears unsupported.

Finally, the literature review and experimental comparisons with the latest approaches such as DDS,  are insufficient, lacking several significant recent works.

### Questions
- Ablation study: conduct ablation study where the DR formulation combined with hybrid noise model
- Difference: please state the difference between the one-step DDS formulation and the proposed hybrid noise model based HR approaches. Aside from the use of the adjacent sanpling time, what is the difference?
- Comparative study with DDS formulation

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a simple and effective hybrid regularization scheme for solving inverse problems using pretrained diffusion models. The authors first analyze the potential issues of existing optimization-based inverse problem solving methods, such as Denoising Regularization (DR). Based on the analysis, they propose Consistency Regularization (CR) to address the inaccurate gradient issues inspired by Consistency Distillation (CD). Then, a Hybrid Regularization (HR) method is further proposed to benefit from both the DR and CR. The proposed method is evaluated on FFHQ and ImageNet datasets, with comprehensive experiments on different distortion and inverse problems. The results show that the proposed method is efficient and can reconstruct better details than the state-of-the-art methods.

### Strengths
- The proposed Consistency Regularization (CR) and Hybrid Regularization (HR) methods are simple and effective, and can be applied to both linear and nonlinear inverse problems.
- The results look much sharper than RED-diff (e.g., Figure 1) thanks to the proposed CR and HR methods. Also, the results are overall outperforming the state-of-the-art methods.
- The reference seems comprehensive. The authors even mention score distillation sampling (SDS) introduced in text-to-3D literature, which indeed shares some similarity with RED-diff and the proposed method.
- The paper includes comprehensive results, comparisons and ablation studies that are important to understand the effect of the proposed method.
- It is nice that the authors provide pseudo code in the appendix and code in the supplemental.

### Weaknesses
 - The proposed CR method can lead to over-sharpened or noisy images, but it is not clear to me why this happens. To my understanding, this is not the case for image generation from noise based on the original consistency distillation paper [Song et al. 2023]. As shown in Figure 2 and Figure 3, the Consistency Regularization (CR) results do get better structures but also introduce artifacts and noise. Also in Figure 1 middle column, the images look a bit noisy even under the Hybrid Regularization (HR) method. In Figure 10 the problem seems more visible ($\beta=0$). I would like to hear more insights on this if this is a potential issue.


### Questions
- Would the idea of Consistency Regularization (CR) lead to less diversity in the inversed image? As shown in the original consistency distillation paper [Song et al. 2023], the amount of variations in the generated images  (measured by recall [Kynka¨anniemi et al. 2019]) can be reduced due to consistency distillation.
- As discussed in the "Weakness" section above, could the authors provide more insight on why the proposed method can lead to over-sharpened or noisy images?
- The equation of consistency distillation has a moving average (EMA) term in the original paper [Song et al. 2023], denoted by $\theta^{-}$. Is it also the case in Equation 12 or the same network is applied for two different time steps?
- Equation 14 shows that the regularization requires 2x network inference denoted by epsilon_theta, but this does not slow down the optimization process. Is it because the effect of reducing the number of iterations is more significant than the extra computation cost?
- I am a bit confused about what should I expect in Figure 6, since I am not familiar with compressed sensing and phase retrievel. Given such highly distorted images, is it possible to recover the results that can match the reference so well? The same question applies to Figure 7 on the nonlinear deblurring results.

Some minor comments:
- In line 421-422, "FFHD" should be "FFHQ".

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper is an improvement over previous work called RED-diff, which is variational method for diffusion posterior estimation.   

By analyzing the weakness of RED-diff and drawing inspiration from consistency model, this paper proposes consistency regularization to replace the denoising regularization in RED-diff. 

By analyzing the limitation of consistency regularization and drawing inspiration from DDIM, this paper further proposes hybrid regularization which combines denosing and consistency.  

Experiments show the proposed method achieve great improvement regarding image quality and sampling speed.

### Strengths
The writing follows a problem analysis and problem soving manner, which is very logical and frendly to readers.   

The improvement over previous works regarding image quality and speed is significant. The experiments are thorough, especially, different previous works are analyzed in detail regarding their image quality.  

The Consistency Regularization (CR)  and Hybrid Regularization (HR) are all well motivated by previous works on diffusion sampling, i.e., consistency model and DDIM etc.

### Weaknesses
eq. 10 is already derived in the previous work Mardani et al. (2024) in section 4.3, it might be better to clarify this.  

There exists a previous work which uses consistency model for diffusion posterior sampling ('Consistency Models Improve Diffusion Inverse Solvers') and should be discussed. What if we follow this paper to use consistency model directly in the original RED-diff framework?  Can this, to some extent, play the same role as Consistency Regularization (CR)?  

[main concern] The consistency to the measurement is not evaluated and compared. This line of works solve inverse problems, shoud the consistency to the measurement also be a important metric in addition to the image reconstruction quality? For example, In DPS and RED-diff, PSNR between reconstruction and ground truth is reported, which can represent the consistency to measurement to some extent. I am not requiring achieving SOTA PSNR and SOTA FID at the same time. But it helps to have some fidelity evaluation.

### Questions
It is interesting that beta=0.2 is a common sweet spot for across different tasks, is there any insight on this?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a novel approach called Consistency Regularization (CR), which provides stabilized gradients without the need for ODE simulations. Building on this, we introduce Hybrid Regularization (HR), a unified framework that combines the strengths of both DR and CR, harnessing their synergistic potential. The approach proves to be effective across a broad spectrum of inverse problems, encompassing both linear and nonlinear scenarios, as well as various measurement noise statistics. The experiment is clear and convincing.

### Strengths
1. The method combines the strength of both Consistency Regularization and Denoising processes with Regularization. 
2. The experimental results are promising, including non-linear problems.
3. The writing quality is strong.

### Weaknesses
1. The method lacks comparisons with recent works such as DDNM [a] and GDP [b].
2. Although the method addresses non-linear problems, it has not been evaluated on blind problems. The performance on real-world samples should be demonstrated to validate its practical effectiveness.

### Questions
1. It would be interesting to explore whether the method proposed in this paper can be extended to other inversion problems, such as image editing.

### Soundness
3

### Presentation
3

### Contribution
3
