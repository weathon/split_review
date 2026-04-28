# Implicit Bridge Consistency Distillation for One-Step Unpaired Image Translation

- Decision: Reject
- Avg Score: 5.33
- Scores: 3, 5, 8

## Abstract
Recently, diffusion models have been extensively studied as powerful generative tools for image translation. However, the existing diffusion model-based image translation approaches often suffer from several limitations: 1) slow inference due to iterative denoising, 2) the necessity for paired training data, or 3) constraints from learning only one-way translation paths. To mitigate these limitations, here we introduce a novel framework, called Implicit Bridge Consistency Distillation (IBCD),  that extends consistency distillation with a diffusion implicit bridge model that connects PF-ODE trajectories from any distribution to another one. Moreover, to address the challenges associated with distillation errors from consistency distillation, we introduce two unique improvements: Distribution Matching for Consistency Distillation (DMCD) and distillation-difficulty adaptive weighting method. Experimental results confirm that IBCD for bidirectional translation can achieve state-of-the-art performance on benchmark datasets in just one step generation.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
1

### Summary
Diffusion models are widely used for image translation. This paper identifies limitations in existing approaches: slow inference, need for paired data, and one-way translation constraints. It introduces Implicit Bridge Consistency Distillation (IBCD) to address these issues. IBCD extends consistency distillation with a diffusion implicit bridge model. The paper proposes two improvements: Distribution Matching for Consistency Distillation (DMCD) and a distillation-difficulty adaptive weighting method. Experimental results show IBCD achieves state-of-the-art performance in one-step generation for bidirectional translation.

### Strengths
Pro:

- The sampling speed in image-to-image translation is a critical problem in this area.
- The paper combines various techniques, including DDIB and consistency models.

### Weaknesses
Con:

- The main concern is that the method seems too incremental, appearing to be merely a combination of DDIB and consistency models.
- In Table 3, the FID improvement from adding Cycle and DMCD is marginal. Is the author aware of what a 0.1 FID change means? If you repeat the experiment twice, the variance might be even larger. This becomes a significant issue when the FID is so high. Also, most baselines in Table 2 show the variance of FID, while the author didn't. As you can see, the variance of other methods is quite large, further undermining the ablation study in Table 3.
- With only a single step, the stochasticity is significantly reduced. The authors should include several other related metrics that highlight diversity, such as the Inception Score. Additionally, more failure cases should be provided for better understanding of the method's limitations.

### Questions
as above

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a framework called Implicit Bridge Consistency Distillation (IBCD) for unpaired image to image translation. IBCD connects PF-ODE trajectories from any distribution to another one by extending consistency distillation with a diffusion implicit bridge model. It introduces Distribution Matching for Consistency Distillation (DMCD) and distillation-difficulty adaptive weighting method to deal with the distillation errors and mean prediction problems from the consistency distillation. Experiments on translation benchmarks demonstrate the effectiveness of the proposed method.

### Strengths
1) The paper is well-written and it clearly explains the proposed method.
2) The visualizations of component’s cumulative contributions on the toy dataset in Fig. (3) help appreciate the role of each part.
3) Experiments on both toy and highdimensional datasets demonstrate the effectiveness of IBCD.

### Weaknesses
1) Missing comparison of the results for bidirectional translation.
2) Missing comparison of computation cost with the existing methods to show the efficiency of the proposed method.
3) The results in Tab. 3 show the model which added DMCD loss, cycle loss and adaptive DMCD degrades the performance in terms of PSNR and SSIM compared to the method using IBCD only.
4) The zero in the first row of Eq. (6) might be \chi_A\cap\chi_B.

### Questions
see weakness

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper proposes to apply consistency distillation (CD) on previous DDIB, achieving a one-step generative model for unpaired image-to-image translation. The authors manage to extend the CD theory, which is applicable to two arbitrary distributions. The novel distribution matching and adaptive weighting techniques further stabilize and facilitate the training process. Both qualitative and quantitative experiments confirm the efficacy of the pipeline and the outperformance.

### Strengths
- The paper provides a versatile pipeline for unpaired image-to-image translation within only one step, which outperforms most previous methods even with large NFEs.

- The theory part is clear and intuitive, and the toy data showcases the instability of vanilla IBCD clearly.

- The experimental results are convincing and impressive, demonstrating directly the outperformance.

- The novel adaptive weighting is interesting and effective, encouraging further study in diffusion model distillation with insight.

### Weaknesses
 - CD highly bases on PF-ODE, i.e., it needs to follow the score function trajectory. In Eq. (6), two PF-ODEs starting from different domains are connected together at $\sigma_{max}$, how to guarantee the smoothness of score function (i.e., gradient) at this point (since one directly uses noisy $x_a$ to solver attached to domain B)? If not smooth, how will the error be like? The authors may provide analysis here similar to original CD paper.

- In L261, the authors claim one of the challenge is to employ only local consistency. However, CTM [1] refers to local consistency as the case when applying PF-ODE solver with extremely smaller step. On the contrary, when using two adjacent timesteps, CTM names it global consistency, similar to original CD. So in the paper, this should also be called a global consistency. I can hardly understand why such strategy is a challenge, given that most distillation works use such a loss.

- The authors state that vanilla IBCD faces mean prediction phenomenon, but provides no convincing analysis on it. Original CD seems not to face such challenge. Does it come from the mismatch of two PF-ODEs? The visualization in Fig. 3(a) fails to convince me. The synthesized samples are not at the mean of domain B. Besides, I cannot see the efficacy of DMCD and cycle loss.

- The ablation study is somewhat confusing. Why vanilla IBCD is only a point rather than a broken line like the others? From Tab. 3 and Fig. 6, it seems that adaptive weighting may harm the performance, which is not consistent with conclusion in toy data. Conversely, DMCD is helpful in real data but fails in toy data. The authors may need further clarification.

### Questions
- The authors propose to use one generator for two domains, which may be unreasonable or hard to achieve in practice. I think the whole pipeline is compatible with two independent pre-trained DMs, i.e., one ADM on LSUN Cat and one ADM on ImageNet with some specific class.

### Soundness
4

### Presentation
3

### Contribution
3
