# Improving Diffusion Models for Inverse Problems Using Optimal Posterior Covariance

- Decision: Reject
- Scores: 5, 5, 8

## Abstract
Recent diffusion models provide a promising zero-shot solution to noisy linear inverse problems without retraining for specific inverse problems. In this paper, we reveal that recent methods can be uniformly interpreted as employing a Gaussian approximation with hand-crafted isotropic covariance for the intractable denoising posterior to approximate the conditional posterior mean. Inspired by this finding, we propose to improve recent methods by using more principled covariance determined by maximum likelihood estimation. To achieve posterior covariance optimization without retraining, we provide general plug-and-play solutions based on two approaches specifically designed for leveraging pre-trained models with and without reverse covariance. We further propose a scalable method for learning posterior covariance prediction based on representation with orthonormal basis. Experimental results demonstrate that the proposed methods significantly enhance reconstruction performance without requiring hyperparameter tuning.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper establish a unified framework for zero-shot inverse problem solvers based on pre-trained diffusion model. 
Especially, they unified two different approaches to approximate $\mathbb{E}[x_0|x_t, y]$ (one by likelihood estimation and the other by proximal optimization) into isotropic Gaussian approximation, which is a novel interpretation.
Based on the unified framework, the paper proposes to optimize the covariance for the approximated posterior via maximum likelihood estimation, which demonstrates effectiveness on various inverse problems.

### Strengths
- The proposed interpretation is novel. It seems to be a good try to connect different approaches.
- The paper is clearly written so easy to follow. Specifically, I like how the paper provides three possible scenarios for estimating the posterior distribution from the case without pre-trained model to the case with pre-trained model that only predicts the posterior mean.
- Underlying theories are well-aligned with prior works.

### Weaknesses
 - The approximation of posterior by the Gaussian distribution may limit performance and interpretability of the diffusion process. Especially, it inevitably leads to interpretation of diffusion model as sampling through trajectory between two Gaussian distributions.
- Leveraging diagonal covariance is easy to lose significant information in images so that the performance of the proposed method would be limited. The assumption of diagonal covariance, implying pixel independence, is particularly concerning for image data where spatial correlations are crucial. This simplification could lead to suboptimal performance, especially in tasks requiring fine-grained detail.
- The performance of the proposed method seems limited (i.e. comparable to baselines for multiple tasks)
- Section 4.3 is the most useful case where previous methods are depending on. However, the proposed method is only about optimizing $r^2_t$ which was hand-crafted in the previous method, which limits the novelty of the proposed method. The optimization of $r_t^2$ appears to be a relatively minor adjustment to existing methods, rather than a significant advancement. The core idea of using a handcrafted parameter remains, with the proposed method simply optimizing this parameter rather than introducing a fundamentally new approach.


### Questions
**Soundness**
- I would like to ask whether approximating the conditional posterior distribution using the standard normal distribution is practical. Specifically, I believe this is equivalent to assuming that the posterior distribution follows a Gaussian distribution, which inevitably implies that the diffusion model is sampling through the trajectory between two normal distributions. This seems inadequate for describing the image generation. Can authors provide their opinions on this matter? This is a crucial point for the my review because the proposed method highly relies on this aspect (section 4).
- I agree with the statement that "letting all the elements of covariance be learnable is computationally demanding" and believe that restricting it to diagonal posterior covariance could be one solution. However, this raises questions about the significance of that covariance. It may lead to the neglect of crucial information, casting doubt on whether the proposed method can achieve "optimal" variances. Additionally, the diagonal covariance assumption implies that each pixel is independent, which may not hold true for images. Note that this assumption is also for the posterior distribution of clean image $x_0$ given noisy image $x_t$. These issues raise concerns about the soundness of the proposed method.

**Experiments**
- When we see the Figure 3, we can observe that the performance of the proposed method is nearly identical to that of DiffPIR when we use $\lambda=10$. This might suggest that the effectiveness of the covariance optimization is marginal, regardless of how the covariance  is computed (i.e. Analytic or Convert). Could authors provide further explanation on this point? Specifically, I wonder that whether this lack of improvement in performance can be attributed to either non-realistic approximation of Gaussian posterior or an excessively simplified covariance structure. If not, have any experimental result been obtained to support the idea that lack of performance improvement is not due to the Gaussian approximation or diagonal covariance?
- Image quality metrics such as PSNR and FID is missing in the Figure 3. Did they show the same robustness and the performance tendency compared to the baseline?
-  I noticed that the paper also presents the results for the 'complete version' of prior works in the appendix E. I understand that the authors moved these results to the appendix for the sake of comparison within the proposed unified framework. However, the 'complete version' of $\Pi$GDM and DPS involves controlling the weight of likelihood guidance, which is orthogonal to the posterior approximation and independent to the proposed unified framework. Hence, the 'complete version' should have been reported in the main paper, as they demonstrate the effectiveness of (adaptive) likelihood guidance in solving the inverse problem without the need to optimize the covariance of approximated posterior distribution. From this perspective, when we see the Figure 4 in the appendix E, the performance of DPS and the proposed method are comparable with proper guidance. This raises the question about the effectiveness of the proposed method once again.

**minors**
- In the last sentence of the section 5.1, why the equation 22 becomes 0/0 when $v^{*2}(x_t)-\tilde{\beta}_t \approx 0$? According to the equation 22, it should be 0 rather than 0/0.  If I overlooked anything, it would be appreciated pointing it out.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper provides a unified view of the existing linear inverse samplers with diffusion models. Motivated by this, they proposed an improved approach by calculating the optimal covariance in the Gaussian approximation. Experimental results show that the proposed approach outperforms previous methods in most cases.

### Strengths
1. The unified view of various existing methods to solve linear inverse problems with diffusion models is interesting and useful. 
2. The proposed improved approach (both convert and analytic) by optimal covariance estimation performs well.

### Weaknesses
1. There is a lack of analysis or experimental results on the inference speed of the proposed method. 
2. As mentioned by the authors, the proposed approach performs badly if it is implemented purely with the optimal variance, which is wired and unreasonable, even contradicting the starting point of this paper.  From a practical implementation side, how to decide where we should switch to the optimal variance value for a specific problem?
3.  How does the proposed approach perform on linear tasks like colorization and denoising, compared with other methods like DPS and other variants?

### Questions
Please see the above

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper is constructed into two parts. In the first part, a framework that unifies prior diffusion model-based inverse problem solvers (excluding the DDRM family) is proposed. It is shown that even the approaches that did not explicitly aimed for a Gaussian approximation of the posterior $p(\mathbf{x}_0|\mathbf{x}_t)$ implicitly makes this assumption, and the only difference is in the computation of the conditional posterior mean $\mathbb{E}[\mathbf{x}_0|\mathbf{x}_t,\mathbf{y}]$. In the second part, several methods on computing the optimal diagonal covariance of the variational Gaussian posterior $q(\mathbf{x}_0|\mathbf{x}_t)$ are proposed. Numerical experiments validate that using these optimal covariance to derive the step sizes of the gradient improves the performance of the heuristically-chosen step sizes.

### Strengths
1. Overall, the paper is well-written, clear, concise, with solid experiments.

2. This is the first work that shows that [3,4] can also be interpreted as approximating the posterior $p(\mathbf{x}_0|\mathbf{x}_t)$ with a Gaussian, similar to [1,2]. Such connection was non-trivial, and it is useful that one can understand [1-4] in a unified framework.

3. Theorem 1 is useful as many of the previous works leverage a pre-trained model that can estimate the reverse diagonal covariance, but simply discards it during inference. It is good that one can leverage such un-used information to acquire the optimal posterior covariance through variational inference. Moreover, the proof obtained from variational calculus is clean.

4. Previous approaches [1,2,4] have hyper-parameters that are hard to decipher and choose from. The proposed method partially alleviates this issue. (It is partially alleviated since it still resorts to the pre-configured hyperparameters of [2,4] when $\sigma_t \geq 0.2$.

5. On the practical side, it is the first time that I see a diffusion model-based inverse problem solver that is based on a 2nd order solver. All previous works that I am aware of utilize DDIM/DDPM sampling.



**References**

[1] Chung, Hyungjin, et al. "Diffusion posterior sampling for general noisy inverse problems." ICLR 2023
[2] Song, Jiaming, et al. "Pseudoinverse-guided diffusion models for inverse problems." ICLR 2023
[3] Wang, Yinhuai, Jiwen Yu, and Jian Zhang. "Zero-shot image restoration using denoising diffusion null-space model." ICLR 2023
[4] Zhu, Yuanzhi, et al. "Denoising Diffusion Models for Plug-and-Play Image Restoration." CVPRW 2023.

### Weaknesses
1. The construction of the theory mostly follows [2] (except that the proof is simpler), and hence the contribution could be limited.

2. Proposition 1 was also proposed in [1] for estimating $\mathbb{E}[\mathbf{x}_0|\mathbf{x}_t,\mathbf{y}]$ through DPS approximation. It should be worth citing and discussing.

3. For readers' convenience, it is worth highlighting that Type II circumvents the computation of $\nabla_{\mathbf{x}_t}$ that requires expensive backpropagation as a closed-form solution for deriving $\mathbb{E}[\mathbf{x}_0|\mathbf{x}_t,\mathbf{y}]$ exists, which is the key difference for the two types.

4. It is unclear what the authors mean by the first sentence of 5.1. paragraph **Posterior variances prediction**. By *ground-truth* square errors, do they mean that they computed the pixel-wise variance from multiple posterior mean that was obtained through the denoiser? Clarification is needed. If so, should this really be called *ground truth*?

5. There is a discrepancy between theory and practice. For one, the authors use a stochastic sampler for Type II, which would not be sampling from (4). How bad are the samples if one simply uses Type II with a deterministic sampler? Any reasons why a deterministic sampler would under-perform in this case?

6. How bad are the samples if one uses the predicted optimal posterior covariance for all the timesteps?

### Questions
1. For estimating the optimal posterior variance with (24), how long does this computation take? Is it a bottleneck for inference?

2. The authors state that they only use the proposed variance when $\sigma_t < 0.2$. Out of 50 steps, how many steps does this correspond to?

3. DPS is known to excel with 1000 NFE, $\Pi$GDM with 100 NFE, etc. Is there any specific reason why the authors chose 50 NFE?

4. (12pg A.1. first sentence) here we proof --> here we prove

5. Is $\tilde\beta_t$ defined somewhere in the paper?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
