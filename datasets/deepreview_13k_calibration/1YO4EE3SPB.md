# A Variational Perspective on Solving Inverse Problems with Diffusion Models

- Decision: Accept
- Avg Score: 5.50
- Scores: 6, 6, 5, 5

## Abstract
Diffusion models have emerged as a key pillar of foundation models in visual domains. One of their critical applications is to universally solve different downstream inverse tasks via a single diffusion prior without re-training for each task. Most inverse tasks can be formulated as inferring a posterior distribution over data (e.g., a full image) given a measurement (e.g., a masked image). This is however challenging in diffusion models since the nonlinear and iterative nature of the diffusion process renders the posterior intractable. To cope with this challenge, we propose a variational approach that by design seeks to approximate the true posterior distribution. We show that our approach naturally leads to regularization by denoising diffusion process (RED-diff) where denoisers at different timesteps concurrently impose different structural constraints over the image. To gauge the contribution of denoisers from different timesteps, we propose a weighting mechanism based on signal-to-noise-ratio (SNR). Our approach provides a new variational perspective for solving inverse problems with diffusion models, allowing us to formulate sampling as stochastic optimization, where one can simply apply off-the-shelf solvers with lightweight iterates. Our experiments for various linear and nonlinear image restoration tasks demonstrate the strengths of our method compared with state-of-the-art sampling-based diffusion models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper presents a novel stochastic adaptation of regularization by denoising (RED) using the denoising diffusion model as an image prior. The study demonstrates the derivation of the score matching loss under the variational inference framework, which naturally leads to the formulation of stochastic RED. By implementing an appropriate weighting scheme, the proposed variational sampler surpasses existing diffusion-based posterior samplers in numerous inverse imaging problems, exhibiting superior reconstruction faithfulness (measured by PSNR/SSIM) and enhanced visual quality (evaluated via KID/LPIPS).

### Strengths
The paper is clearly written and comprehensible to readers. Additionally, the formulation of the proposed variational sampler, utilizing a first-order stochastic optimizer (Adam) to address the stochastic RED objective, is both innovative and straightforward, yielding effective results.

### Weaknesses
Despite the paper's clarity, several imprecise arguments and overstatements necessitate revision and clarification:

- The authors claim that a key advantage of their method is the circumvention of unimodal estimation employed in prior works. However, their variational inference approach introduces another level of approximation by using a simple unimodal Gaussian to approximate the complex multi-modal conditional posterior p(x0​∣y). This complicates the justification of the proposed framework's improvement over mitigating posterior score approximation in prior methods (Contribution 1). Specifically, while avoiding the need for a score Jacobian is beneficial, the approximation of the posterior with a unimodal Gaussian may be overly restrictive, potentially limiting the method's ability to capture the true posterior distribution, especially in cases where the posterior is highly multi-modal. The authors should provide a more thorough analysis of the impact of this approximation on the quality of the reconstructions.
- The claim that the RED framework fundamentally differs from the Plug-and-Play (PnP) framework lacks rigor. The explicit regularization term in RED only exists under certain strict assumptions, which are often not applicable to modern deep learning-based denoisers. Thus, both RED and PnP should be explained from a fixed-point iteration perspective, which provides a unified treatment with theoretical convergence guarantees [A]. The authors should acknowledge that the explicit regularization term is not always present and that both RED and PnP can be viewed as iterative algorithms converging to a fixed point. It is crucial to clarify the specific conditions under which the explicit regularization term is valid and how these conditions relate to the use of deep learning-based denoisers.
- The proposed weighting mechanism aligns with the parameter setting strategy in the PnP framework [B] (as detailed in Section 4.2). Moreover, the authors overlook discussing several related works in PnP-type literature [C, D, E], which essentially represent the deterministic counterparts of diffusion-based posterior sampling. The similarity in weighting strategies between this work and PnP methods should be explicitly discussed and justified. Furthermore, the lack of discussion of deterministic PnP methods limits the understanding of how the proposed stochastic method compares to existing alternatives. The authors should provide a more comprehensive discussion of these related works and highlight the unique contributions of their method in the context of both deterministic and stochastic approaches.
- The experimental comparison with DPS lacks sufficiency to verify the effectiveness of the proposed approach. Benchmarking against the state-of-the-art PnP approach [B] would provide a more comprehensive characterization of the method's advantages. Additionally, the performance in phase retrieval, particularly the PSNR, is too weak to be considered meaningful. To enhance credibility, it is recommended to consider adopting more realistic settings, such as coded diffraction patterns or oversampled Fourier measurements, as in [F]. The experimental section needs to be expanded to include comparisons with state-of-the-art PnP methods, and the phase retrieval experiments should be conducted with more realistic measurement models to better assess the practical applicability of the proposed method.

### Questions
See above

---
After rebuttal: I'm generally satisfied with authors' response, overall I think it's a good paper that can be accepted to ICLR.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a sampling process based on diffusion models for solving inverse problems. This approach allows to tackle very general inverse problems in images like inpainting, deblurring, super-resolution... The method itself is straightforward when using a pretrained network and the experiments show promising results.

### Strengths
The method takes the form of a sampling algorithm that can solve a large number of inverse problems with additive Gaussian noise. 
The framework is easy to setup when using pre-trained diffusion models and the theory gives access to formula for the hyperparameters. All in all the experiments show the benefit of this approach compare to similar frameworks.

### Weaknesses
The method is only for Gaussian noise while DPS, for example, can handle Poisson noise (though not in a low regime). Also the hyperparameter formula asks for the variance of the noise. Such quantity may be unknown, it would been interesting to see, experimentally, what happens with wrong or estimated values of the noise variance. Specifically, the impact of over or underestimating the noise variance on the reconstruction quality should be investigated. Finally, like all methods based on diffusion models, it asks for an appropriate model (pre-trained or not) and solving the inverse problems remains computationally heavy with thousand of iterations to produce a result. The computational cost is a significant limitation, especially for high-resolution images or real-time applications. Furthermore, the discussion on the sampling strategy is weak. The conclusion that descending sampling is best is not surprising given the time dependency in the sampler, and the lack of exploration of other descending strategies (log, exp...) is a missed opportunity. The paper should also discuss the sensitivity of the method to the choice of the diffusion model, as performance may vary significantly depending on the model architecture and training data.

### Questions
I reformulate one of my previous remarks as a question: what happens with wrong or estimated values of the noise variance?

My next question is also a remark. The authors compare different strategy for the sampling (i.e. the timestep). The conclusion is that the descending sampling leads to the best results. This is normal as there is a time dependency in the sampler since the previous mu is used for the loss. Thus, I would expect the random sampling to fail. So the discussion on this point is weak and I would expect other descending strategy (log, exp...). Would it be a way to reduce the number of timesteps?

Last point, please update the references. For example most of the paper from Chung et al are proceedings of conferences and no just papers on ArXiv.

### Soundness
3 good

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors propose a new regularization strategy for solving inverse problems with a denoising prior based on diffusion models. The regularization is reminiscent to RED but uses denoisers at different noise levels. Compared to competitive methods, DiffRED does not assume the posterior $p(x_0|x_t)$ of the diffusion model to be unimodal. Experiments on various inverse problems prove the efficiency of the algorithm.

### Strengths
Overall, the paper is well written, the motivation is clear and the method is original. The main strength of the paper is its experimental study. The authors experimented on very diverse inverse problems and perform an exhaustive ablation study. They clearly demonstrate that their algorithm performs state-of-the art performance and gives impressive visual results. Concerning the method, the proposed regularization in (8) is new and original, and the Proposition 2 makes this regularization term very promising.

### Weaknesses
My main concerns are on the theoretical side. The following aspects require further details.

- You introduce KL minimization in (5) which makes sense for sampling from $p(x_0|y)$. However, the Gaussian approximating posterior $q(x_0|y)$ is then used with $\sigma = 0$. In this case, the minimization of the KL comes back to the MAP problem $argmin_\mu p(\mu|y) = argmin_\mu p(y|\mu) - \log p(\mu) $. Therefore, the objective of this work is then to solve the MAP. This is a classical link between sampling and optimization.  From this observation, assuming Proposition 1 is true, by identification in the case $\sigma = 0$, we get that $-\log p(\mu)$ is equal to the second term in (8). Is this really true ? In general, can the authors explain why they first consider a sampling approach before taking $\sigma = 0$ ? 
- The proof of Proposition 1 uses a result from (Song et. al , 2021) that seems different (inequality and not equality). As this is the base of the theoretical analysis, I would like to see an exhaustive proof of the result. 
- The proposed regularization is defined with an expectation on $t$, but in practice $t$ is not chosen at random but with a predefined descending scheme. Therefore, the algorithm and the regularization used in practice is different from the ones originally introduced. This is for me the main weakness of the paper. 
- Proposition 2 implies that the right term in the equation is a conservative vector field, and in particular that it has symmetric Jacobian. This looks surprising to me without further assumptions on $\epsilon_\theta$. Refer to (Reehorst & Shniter, 2018) for the same observation on RED. Do you have an argument for justifying symmetry of the Jacobian ?
- The algorithm 1 is proposed without any convergence analysis. 
- Before (8) it should be made clear that you assume exact approximation of the score with $\epsilon_\theta$ to get (8).

### Questions
- The authors argue that the advantage of the paper is to avoid the assumption $p(x_0|x_t)$ unimodal. Instead, they take the assumption
$q(x_0|y)$ unimodal. Can the authors explain why this assumption would be more valid ?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors propose a novel diffusion sampling algorithm incorporating a data-fidelity term, allowing to solve inverse imaging problems with pretrained diffusion models. Interestingly, the authors claim that this novel sampling scheme can be related to a variational formulation, as opposed to traditional diffusion algorithms. This aspect is all the more interesting as it clearly relates the method to traditional, conventional variational methods for solving inverse problems. Eventually, the authors demonstrate its effectiveness on several inverse imaging problems, ranging from image inpainting to MRI imaging.

### Strengths
- The paper is overall well written and easy to follow, making it comfortable to read. The authors do not engage in unnecessary technicalities and provide the required background in a succint and clear manner.
- The proposed method is novel (to the best of my knowledge) and simple to implement.
- Relating the proposed method to the RED approach is very interesting and is a valuable contribution to the community.
- Experimental results are convincing.

### Weaknesses
Despite the many strong points raised above, this paper suffers from important drawbacks. 

- Important references from the variational [1,2,3] and PnP [4,5,6] litterature are missing. Overall, while the context within diffusion models is well set, the link with the general imaging litterature is completely absent, making it difficult for the reader to relate to other imaging techniques. Specifically, the paper lacks discussion of established variational methods and their performance on the presented tasks. This absence makes it difficult to assess the true novelty and practical relevance of the proposed approach.
- Theoretically, the fact that the Jacobian of the network is not symmetric (a priori) prevents the authors from making a link with a variational loss (see the Reehorst reference cited by the authors), questioning the full approach. The paper does not adequately address the implications of this lack of symmetry, particularly regarding the interpretation of the denoiser as a gradient of some underlying function. This point is crucial for the claimed connection to variational methods.
- Comparisons with DiffPIR [8] or RED are missing. The lack of comparison with these methods, especially DiffPIR which also combines diffusion models with inverse problems, makes it difficult to gauge the relative performance of the proposed method. A comparison with RED is also important given the strong emphasis on the RED framework in the paper.

### Questions
I've enjoyed reading this paper and I thank the authors for their interesting work. I have however some strong feelings regarding how general imaging methods are treated in the paper - and in particular how their methods relates to more general variational methods. Please find below a list of comments.

**Major comments**
1. Pure variational methods are simply completely absent of this paper. Not only is this problematic with respect to the conveyed message ("the proposed method links with variational methods") but it is also detrimental to the experiments - for instance top row of Figure 11, a standard TV method would certainly reach very high PSNR. In the current form, I disagree that the paper links with variational methods; the paper links with RED approaches (which are very specific). Here are some more general references that may be of interest: [1,2,3].
2. The RED approach plays an important role in this paper, but the authors do not mention an important aspect of RED: the loss that it derives is incorrect. This is explicitely stated in the Reehorst and Schnitter reference cited by the authors. An important point raised there is that without symmetry of the Jacobian, there is no hope that the denoiser approximates a gradient. This is well known in the PnP community which has led to significant works [4,5,6].
3. Talking about fixed point after (9) is very misleading. In general, a fixed point is derived from the 0 of a subdifferential (or equivalently in the convex case, of the minimum of a convex function). In the case proposed by the authors, the loss varies with each iterate. How can there be a fixed point? (by the way, "the fixed point" strongly suggests a relationship to a convex function, switching to "a fixed point" would be more appropriate).
4. While the context on diffusion models is clear and the literature review is appropriate, this cannot be said on more general inverse imaging techniques. The authors do not seem to be aware of state-of-the-art PnP algorithms such as DPIR [7], and more importantly, to methods mixing PnP and diffusion techniques, such as DiffPIR [8]. I think comparing with at least one PnP would be interesting (e.g. DPIR, or since a strong emphasis is put on it, RED).
5. In my opinion, a key contribution of the paper is equation (8). An interesting point there is that the loss function is on $\mu$, which relates to Minimum Mean Square Error (MMSE) approaches in imaging. This is an important point as most traditional methods in imaging follow a Maximum a Posteriori (MAP) approach. In fact, it is often believed that MMSE approaches are better than MAP approaches, but unfortuntely too costly and/or difficult to implement. A comment on that would be very necessary and interesting to the imaging community readers.
6. The presence of $\epsilon$ in the equation of Proposition 2 is surprising given the remark made at the end of the proof in the appendix (just before A.3). Why keep it in the equation?
7. Maybe the authors could merge the results from A.2 and A.3 in Proposition 2 with additional notations regrouping the different constants. In fact, A.3 is an interesting result that is a bit hidden in the paper at the moment.

**Minor comments**
1. Small typos are remaining here and there. For instance: "stropped", "bellows up", "approaches to zero; ." (point after ;)...
2. "An inverse problem is often formulated as" --> "Inverse problems can be formulated as"

**References**

[1] Knoll F, Bredies K, Pock T, Stollberger R. Second order total generalized variation (TGV) for MRI. Magn Reson Med. 2011

[2] Portilla J, Strela V, Wainwright MJ, Simoncelli EP. Image denoising using scale mixtures of Gaussians in the wavelet domain. IEEE Transactions on Image processing. 2003

[3] Kobler E, Klatzer T, Hammernik K, Pock T. Variational networks: connecting variational methods and deep learning. InPattern Recognition: 39th German Conference, GCPR 2017, Basel, Switzerland, September 12–15, 2017.

[4] Hurault, Samuel, Arthur Leclaire, and Nicolas Papadakis. "Gradient Step Denoiser for convergent Plug-and-Play." International Conference on Learning Representations. 2021.

[5] Xu X, Sun Y, Liu J, Wohlberg B, Kamilov US. Provable convergence of plug-and-play priors with MMSE denoisers. IEEE Signal Processing Letters. 2020

[6] Pesquet JC, Repetti A, Terris M, Wiaux Y. Learning maximally monotone operators for image recovery. SIAM Journal on Imaging Sciences. 2021

[7] Zhang K, Li Y, Zuo W, Zhang L, Van Gool L, Timofte R. Plug-and-play image restoration with deep denoiser prior. IEEE Transactions on Pattern Analysis and Machine Intelligence. 2021

[8] Zhu Y, Zhang K, Liang J, Cao J, Wen B, Timofte R, Van Gool L. Denoising Diffusion Models for Plug-and-Play Image Restoration. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition 2023

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good
