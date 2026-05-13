# Variational Diffusion Posterior Sampling with Midpoint Guidance

- Decision: Accept
- Scores: 8, 8, 8, 8

## Abstract
Diffusion models have recently shown considerable potential in solving Bayesian inverse problems when used as priors. However, sampling from the resulting
denoising posterior distributions remains a challenge as it involves intractable terms. To tackle this issue, state-of-the-art approaches formulate the problem as that of sampling from a surrogate diffusion model targeting the posterior and decompose its scores into two terms: the prior score and an intractable guidance term. While the former is replaced by the pre-trained score of the considered diffusion model, the guidance term has to be estimated. In this paper, we propose a novel approach that utilises a decomposition of the transitions which, in contrast to previous methods, allows a trade-off between the complexity of the intractable guidance term and that of the prior transitions. We validate the proposed approach through extensive experiments on linear and nonlinear inverse problems, including challenging cases with latent diffusion models as priors, and demonstrate its effectiveness in reconstructing electrocardiogram (ECG) from partial measurements for accurate cardiac diagnosis.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces a novel diffusion-based posterior sampling method called Midpoint Guidance Posterior Sampling (MGPS) to address Bayesian inverse problems. In cases where denoising diffusion models (DDMs) are used as priors, MGPS aims to approximate the posterior while balancing the complexity between guidance and prior transition terms. The method leverages an intermediate midpoint state to improve posterior approximation and incorporates a Gaussian variational approximation for additional flexibility. MGPS is validated on linear and nonlinear inverse problems across various domains, including image and ECG signal reconstruction, and outperforms several state-of-the-art methods.

### Strengths
1. The approach introduces a midpoint guidance mechanism that provides a novel trade-off for guidance and complexity of the learned transition term in diffusion models. This make it different from other diffusion-based posterior sampling methods.

2. The method is well-justified with mathematical rigor. The decomposition of the backward transition and the use of Gaussian variational approximations.

3. MGPS is extensively evaluated across both synthetic and real-world tasks, such as Gaussian mixture sampling, image super-resolution, and ECG imputation. Experimental results show significant improvements in reconstruction quality over baseline methods.

4. The paper is generally well-organized, providing clear problem definitions, methodological details, and experimental results. Detailed explanations and algorithmic steps (Algorithm 1) support reproducibility.

### Weaknesses
1. More exploration of $\eta$ and the midpoint sequence's impact on different task types and data complexities would clarify MGPS's adaptability across scenarios. The authors showed the effect of $\eta$ in the Gaussian toy example. It would be interesting to see $\eta$'s influence in other tasks. Specifically, the paper lacks a systematic analysis of how the optimal $\eta$ might vary with the dimensionality of the data, the complexity of the prior, or the nature of the inverse problem (e.g., linear vs. nonlinear). This makes it difficult to assess the generalizability of the chosen $\eta$ values across diverse applications.

2. The trade-off introduced by the midpoint state could be theoretically explored further. The authors mention the need for tuning this midpoint sequence but provide limited theoretical insights on why this works well. For instance, the bounds on the approximation errors may be further derived, or the balance between the prior and guidance terms could be analyzed with the midpoint sequence. A more rigorous analysis should investigate how the choice of the midpoint sequence affects the convergence rate of the posterior sampling process and the quality of the approximation, possibly through the lens of information theory or by bounding the KL divergence between the true posterior and the approximation.

3. Concerns about the correct implementation of other compared methods remain for me, as those methods perform in Figures 13 and 15 worse than those in the original publications related to some image domain tasks. Or are those methods undertuned? The paper should provide more details on the hyperparameter tuning process for the baseline methods, including the range of values explored and the criteria used for selection. It is crucial to ensure that the baselines are implemented and tuned as fairly as possible to provide a reliable comparison.

### Questions
1. Would there be an optimal mid-point schedule for $l_k$, which allows fewer diffusion model evaluations and comparable performance? Or better technique can be used to find the optimal schedule? Or can we suggest a criteria for evaluating the trade-off between performance and computational cost?

2. What is the key reason that makes mid-point guidance perform better? When the same prior is applied, what difference does the midpoint sequence make to sample algorithm as difference stages of the posterior distributions?

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
5

### Summary
The paper proposes a novel midpoint guidance strategy for posterior sampling of diffusion models. The main idea is to first move to a mid-point state l_k that is a function of k for guidance, and then noise back to obtain X_k unconditionally. This seems to solve issues associated with other SOTA approaches that perform the guidance based on variations of Tweedie's formula. Extensive experiments are provided, along with comparison to SOTA methods. Improvements are shown in almost all inverse problems, and notably for nonlinear inverse problems. 

I think the paper has good merit, but its exposition is overly complicated and notation does not match the rest of the literature. These dampened my enthusiasm, but I'm happy to reevaluate after the authors respond.

### Strengths
- The idea of midpoint guidance is novel, and intuitively appealing to solve the issues associated with guidance issues especially at the early stages of the diffusion process.
- Very thorough evaluation.
- Results are good, showing improvement over SOTA methods, including both DDMs and LDMs (that are commonly used in these applications).
- Multiple nonlinear inverse problems are studied, an area where other posterior sampling methods have issues. A good level of improvement is shown in these applications.
- Performance also evaluated across NFEs.
- Good sample variety is shown.

### Weaknesses
 - Unfortunately, the exposition is overly complicated. The idea can be explained much more clearly, but also partly due to non-standard notation, the gist does not come across easily. Section 3 would benefit from a substantial rewrite that changes the notation (please see below), and highlights the main ideas, and potentially even including a figure to show the midpoint guidance idea.
- Similarly, the notation does not match rest of the literature on posterior diffusion sampling for inverse problems. For instance, the posterior is denoted by \pi(x), which is written as a marginal, though this should depend on the observations y. Similarly g(.) in (2.1) should be conditional on y, but this is not done either. This propagates throughout the paper, and makes it hard to appreciate the contributions. Please use standard notation to match other existing works.
- The 50 randomly selected evaluation points for FFHQ and ImageNet is a bit unconvincing. There are standard validation sets that are publicly available for both databases, and these are commonly used in other papers (e.g. DPS, PGDM). Please report your results over a larger set (& also explain how random selection was done).
- Unclear why only LPIPS is provided. PSNR/SSIM must be provided as well. I understand improvement may not be uniform for those metrics, but this should be up to the reader to figure out.
- DPS is typically run with NFE = 1000, but it was used for N = 300 in this paper for comparison. This may further close the LPIPS gap.

The following points are not really weaknesses, but I wanted to note them:
- The ECG application comes out of nowhere. Without enough motivation and knowing the difficulty of the task, the contribution here is a bit hard to appreciate.
- There are also two additional references that may be of interest:
a) arXiv:2402.02149, which is similar to Boys et al in spirit
b) arXiv:2407.11288 (ECCV 2024), which learns w_k in (2.5) and also uses a diagonal approximation to circumvent vector-Jacobian calculations

### Questions
Following up on the weaknesses:
- Why was a different notation used compared to existing works on posterior sampling for inverse problems?
- Why was only 50 randomly selected evaluation points used for FFHQ and ImageNet? How was this random selection done?
- Why was only LPIPS used for evaluation, and other standard metrics like PSNR/SSIM were not reported?
- Why was DPS run for 300 steps instead of the more standard 1000?

### Soundness
4

### Presentation
3

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
The authors propose 'midpoint guidance posterior sampling,' where the reverse diffusion process is decomposed into two steps:

1. Denoising the current diffusion measurements into a 'midpoint' state.
2. Renoising the midpoint measurements to obtain the next diffusion iterate.

The denoising approach consists of approximating a Gaussian variational approximation in conjunction with the DPS guidance proposed by Chung et al to sample an estimated image. The variational approximation is learned at each diffusion timestep.

The renoising stage appears to be the typical DDIM/DDPM computation of the next diffusion iterate.

This approach of midpoint guidance achieves very strong empirical performance on a wide variety of problems/datasets and has strong theoretical foundations.

### Strengths
S1) The approach is well-motivated and has strong theoretical backing, with a novel theoretical result included in Appendix A.3.

S2) The authors evaluate many different problems on multiple datasets, achieving relatively strong performance across the board.

S3) The paper is well-written and reasonably easy to follow (although I have some gripes with notation, outlined in the 'Weaknesses' section below.

S4) Many great visuals, especially in the appendices.

S5) The authors provide very detailed and explicit implementation details for their competitors. I think that this is of vital importance and appreciate the efforts made by the authors to share these details.

### Weaknesses
At a high level, I quite like this work. However, as described below, I feel that the experimental results are incomplete.

W1) Even though the paper is well-written, and all mathematical elements check out (at least to me), the notation makes all of the math in Section 3. In particular, the differentiation between scalar and vector quantities is not sufficient. I would suggest that the authors make vector quantities boldface (e.g., $\boldsymbol{x}$). This would make things much easier to read.

W2) While I appreciate the robust slate of experiments, using test sets of size 50 (at least for FFHQ, ImageNet) is not sufficient for two reasons:
1. I would argue that the standard test set size for any diffusion inverse solver is 1k images. This seems to be the accepted number, and large enough to truly understand model performance. A test of size 50 is just not sufficient for acceptance to a conference like ICLR. I feel that the results would be more convincing if there were fewer experiments with a larger test set. Note that I am explicitly speaking on the image datasets, where samples are plentiful. There are plenty of problems where there is not enough data to have a test set comprised of 1k samples and that is fine. To summarize: I think that fewer experiments are not a bad thing if it means more robust testing.
2. Only using 50 test samples does not enable reliable computation of FID (a metric that is noticeably absent from the paper). FID is a standard metric when evaluating diffusion inverse solvers. With it absent, the experimental results are incomplete.

W3) I also think that the experimental results are incomplete due to the lack of a pixel-space quality metric. The authors argue against PSNR/SSIM in Section 4, but I disagree. I think that LPIPS is a great choice, but that PSNR is still a necessity when testing because similarity in the pixel-space matters too. If the samples don't respect the measurements, that is a problem and LPIPS may not catch it since it is a feature-based metric.

To summarize W2 and W3, I think that the authors need to reconsider their evaluation of problems which use the image datasets. I would suggest:
1. 1k test samples.
2. Computing PSNR and FID in addition to LPIPS.

These changes are critical to fully understanding model performance. Without this sufficient experimental evaluation, I cannot recommend this paper for acceptance.

### Questions
See weaknesses.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes MGPS, a variational inference approach to diffusion model-based inverse problem solving (DIS) in the standard guiding reverse diffusion setup. Two clever ideas are used:

1. Instead of using the DPS approx after denoising $k + 1 \rightarrow k$, denoise it up to $0 < \ell_k < k$, and use the posterior mean of $x_{\ell_k}$ instead of the posterior mean of $x_k$ to compute the DPS gradient. This way, you can control the trade-off arising in the approximation error for the denoising kernel and the likelihood computation.

2. For every reverse diffusion timestep $k$, use $j$ iterations of stochastic optimization for fitting a variational distribution for the reverse posterior kernel. The authors propose to use a Gaussian kernel but also optimize over the diagonal elements of covariance. This is different from the previous works where typically, an isotropic variance is used, probably with the exception of [1].

Overall, the paper is well-written, has a clear theory, and has great results. The reviewer especially appreciates the efforts that the authors made to make the experiments as fair as possible, carefully addressing the details that are often ignored. I do have some questions and concerns on the practical implementation of the method, and in some places, how to derive it. Nevertheless, I think the paper should be a clear accept.


**References**

[1] Peng, Xinyu, et al. "Improving Diffusion Models for Inverse Problems Using Optimal Posterior Covariance." ICML 2024.

### Strengths
1. The paper is well-written and relatively straightforward to follow.

2. When an approximation is used, the authors do a good job of explaining the rationale, by either showing it theoretically or experimentally.

3. MGPS is a good balance between a theoretically grounded solution and a practical solution, not requiring too much computation.

4. The results of image restoration tasks are clearly SOTA.

5. Experiments are complete. Numerical experiments on toy data, image restoration experiments, and ECG completion all indicate the superiority of the method.

### Weaknesses
1. Some parts of the derivation are unclear. The authors propose a variational distribution $\lambda^\varphi$ for $\hat{\pi}^\theta$ in (3.6), which, to my understanding, is already tractable. Since $\hat{g}^\theta$ is Gaussian from DPS, and $p_{\ell_k}^\theta$ is also Gaussian, then isn't $\hat{\pi}^\theta$ already a Gaussian? Why would one need an additional variational distribution to approximate this? The core issue here is that while the individual components might be Gaussian, the resulting posterior is not guaranteed to be Gaussian due to the non-linearity introduced by the measurement model within the DPS approximation, particularly when dealing with non-linear inverse problems. This non-linearity makes the analytical computation of the posterior intractable, necessitating a variational approximation.

2. Adding on 1, I don't quite understand why including the diagonal terms of the covariance for additional optimization would induce better fitting, when $\hat{\pi}^\theta$ would have istropic covariance. Both these points maybe from my misunderstanding, but it should be clarified. The concern is that the method uses a Gaussian variational approximation with a diagonal covariance, while the true posterior might have a more complex, anisotropic covariance structure, especially when $\ell_k$ is significantly smaller than $k$. The isotropic covariance assumption in the standard diffusion process is not valid for the conditional distribution $\pi_{\ell_k | k+1}(\cdot | x_{k+1})$ when $\ell_k$ is much smaller than $k$. The diagonal covariance optimization is a practical compromise to capture some of the anisotropic structure without the computational burden of a full covariance matrix.

3. Balancing the denoising and likelihood approximation errors is interesting. Is it safe to say that the mainstream previous works that use something similar to (2.5) be considered as simply taking $\ell_k = k$? Or is it not directly comparable? I believe the authors could spend some more effort on clarifying the difference between the existing methods. There is a related works section, but the connections seem a bit vague. An additional appendix section could be nice. The relationship between the proposed method and existing approaches like DPS needs further clarification. Specifically, it's unclear if setting $\ell_k = k$ in the proposed framework directly recovers a DPS-like approach, or if additional approximations are still involved. The authors should explicitly detail the differences and similarities, possibly through a more detailed analysis in an appendix.

4. The upper bound of the variational inference problem is defined and used, but it is not explained how this is derived.

### Questions
1. In Tab. 2, only the LPIPS values are reported. I understand that this is probably to save space, but I would recommend also including other standard metrics such as PSNR, SSIM, and FID.

2. MGPS is based on DDPM sampling. Would there be any way to incorporate faster solvers into this?

I am willing to further raise the score after clarification.

### Soundness
4

### Presentation
3

### Contribution
4
