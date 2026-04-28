# Solving Inverse Problem With Unspecified Forward Operator Using Diffusion Models

- Decision: Reject
- Avg Score: 3.75
- Scores: 3, 6, 3, 3

## Abstract
Diffusion models have excelled in addressing a variety of inverse problems. Nevertheless, their application is restricted by the requirement for specific prior knowledge of the forward operator. This paper presents a novel approach, UFODM, which circumvents this constraint by selecting the appropriate forward measurement, making the method more applicable to real-world scenarios. Specifically, our approach enables the concurrent estimation of both the reconstructed image and the characteristics of the forward operator during the inference stage. Our method effectively tackles inverse problems such as blind deconvolution, JPEG restoration, and super-resolution. Furthermore, we demonstrate the versatility of our approach in solving generic inverse problems through the automated selection of forward operators. Empirical evidence suggests that our framework has the potential to enhance the efficacy of diffusion models and extend their applicability in solving real-world inverse problems.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper develops a diffusion-based inverse problem solve designed to solve inverse problems where both the forward models form and latent parameters are unknown. E.g., don't know if solving blind deconvolution or jpeg artifact removal and don't know the blur kernel nor the compression ratio. The proposed method generally follows the approach of Song et al. 2023 to reconstruct x and then infers the unknown latent parameters and the model using MAP estimation.

The method is applied to blind deconvolution, where it performs on par with other methods. It is also applied successfully (without comparison to any other method) to jpeg restoration, superres, inpainting and other tasks.

### Strengths
Performs on par with existing methods at the bind deconvolution task.

First approach I'm aware of to tackle the, as described, unknown forward model problem.

### Weaknesses
As written, lines 7-12 of Algorithm 1 are rewriting the same values over and over.

The SSIM between x and y is not a good model for P(H|x,y,\phi). Specifically, SSIM is designed to measure perceptual similarity, not the likelihood of a forward model given observed data. This choice is particularly problematic because SSIM is highly sensitive to small spatial shifts and intensity variations, which are common in inverse problems. Using SSIM as a proxy for the conditional probability will likely lead to unstable and unreliable parameter estimation, especially when the forward model involves complex transformations or noise.

The paper doesn't motivate the problem. Without a real-world application to point to, the proposed problem setting seems somewhat contrived. While the idea of a completely unknown forward model is interesting, it lacks practical grounding. The absence of a clear use case makes it difficult to assess the relevance and potential impact of the proposed method. It's unclear why one would need to solve a problem where the forward model is completely unknown, as opposed to a blind inverse problem where the model structure is known but the parameters are not.

I don't think the two sides of equation (10) are equivalent (or at least it's nonobvious why this would be the case). The jump from a posterior probability to a product of likelihood and prior is a standard application of Bayes' theorem, but the specific formulation in equation (10) lacks sufficient justification. The paper needs to explicitly show how the posterior probability of the forward model parameters is derived from the likelihood and prior, and why the specific form of the likelihood is appropriate.

In most applications p(h) in equation (10) isn't constant. Assuming a uniform prior over all possible forward models is unrealistic. In practice, certain types of forward models are more likely than others, and this prior knowledge should be incorporated into the estimation process. Ignoring this prior information can lead to suboptimal results, particularly when the search space of possible forward models is large.

The proposed method is only compared against baselines on the blind motion deblurring task. It's unclear if other methods would also generalize to the blind setting. The lack of comparison on other tasks makes it difficult to assess the generalizability of the proposed method. It is possible that the method is only effective for deblurring and may not perform well on other inverse problems, such as super-resolution or inpainting.

### Questions
In lines 7-12 of Algorithm 1, should "i" be indexing something? H? As written, the same values are being overwritten over and over again.

"Here, we use the structural similarity index measure (SSIM) to approximate the p(H | x0, y,φ). We measure the similarity of the measurement image and the estimated image operated by the forward function to obtain the optimal H∗." Does this mean the proposed method can't handle simple operations (e..g, inversion or flipping) that cause y not to look like x?

In line 8 of Algorithm 1, how does one know H?

Is big N in line 7 of algorithm 1 the same as little n in the definition of S_H?

### Typos:
Pg 2: "Our UFODM, simultaneous estimation of both the restored image and the
forward operator’s parameters"-->"Our UFODM, which simultaneoulsy estimates both the restored image and the forward operator’s parameters"

Pg 4: "Naturally, this setup is more challenging than the
traditional (blind) inverse problem, as it involves an unspecified forward operator and a significantly larger solution space." Should this read "(non-blind)"?

Pg 5: "the perturbed image of measurement y" "image of" seems unnecessary

Pg 9: "superior perceptual similarity and quality compared to (h) ground truth" reads as if the method is better than the ground truth.

### Soundness
1 poor

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper present a diffusion-based approach on inverse problem that explicitly estimate the unknown forward operator among a family of potential forward operators.

### Strengths
The contribution is novel and shows improved performance with respect to other approaches.

### Weaknesses
The paper presentation could be improved; for instance, the background section defining the forward operator only appears at the end of page 3. The title can be confusing as 'unspecified forward operator' could be misleading: it could correspond to solving the inverse problem while only implicitly estimating the forward operator, as is the case with task-specific methods, or it could correspond to a much wider class of forward operator that does not fall into a well-specified list of possible forward operator.

The assumptions to ensure the problem is not ill-posed could be more qualitatively explained. What is the limitation in assuming a parameter phi that is drawn independently from a known prior that is not dependent on the data? What are the limitations of assuming a known prior p(phi)? etc. The feeling is that it is not easily understandable from the paper in which situation one can implement the author's approach for solving 'real-world' inverse problems. Adding to that, there is no open-source code available, which will limit the impact of the paper.

### Questions
None

### Soundness
3 good

### Presentation
2 fair

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
This paper presents a method on using pre-trained diffusion models for inverse problem under unspecified forward operator. In the paper, three types of forward operator are considered: JPEG compression, motion blur, and downsampling. The problem studied in this paper is to develop a unifying framework to restore images degraded by any of those three operators, without knowing exactly which operator is used to degrade the image. The proposed strategy is to perform Bayesian inference over all three forward operator types, and carry out standard posterior-sampling-based image restoration under each forward operator type; at the end, the best performing forward operator is selected. The evaluations are performed on datasets including FFHQ, AFHQ, and ImageNet.

### Strengths
- The paper focuses on an intellectually intriguing problem of inverse problems with unspecified forward operator.
- The writing and overall presentation are clear and easy to follow.

### Weaknesses
 - The paper does not do a good job at justifying the practical significance of handling unspecified forward operator, and demonstrating that the proposed problem setting is not contrived. None of the degraded images used in this paper is really from the truly real-world setting where the forward operator type is completely unknown. The demonstrated results still assume that the unspecified forward model is one of three known forward operator types.
- The paper does not provide any information on the computational cost of the proposed method and how it compares to the baselines.
- Because this paper only considers a finite number (really just three) of forward operator types, the problem seem to really boil down to just running multiple reconstructions in parallel, each assuming a different forward operator type.

### Questions
- If one runs multiple separate reconstruction in parallel, each under a different forward operator assumption, how would this framework be different in terms of quality and computational cost?
- Are there any real-world examples (i.e., not controlled simulations on FFHQ) that can show exactly why this problem is meaningful?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors propose UFODM, a diffusion model-based inverse problem solver targeting for 1) blind inverse problem solving when the parameter of the forward operator is unknown (e.g. blind deblurring), and 2) blind inverse problem where one does not even know the type of forward model generated the measurement. Regarding the second part, the problem setting is simplified to the case where the authors assume a pre-defined discrete set to choose from, e.g. deblurring, JPEG decompression, SR, etc. UFODM performs favorably over prior arts such as BlindDPS and GibbsDDRM. Preliminary experiments on *unspecified forward operator* is also provided.

### Strengths
1. The paper is, for the most part, easy to follow. The method is intuitive.

2. UFODM is the first method to tackle the case where one does not even know the class of forward operator (i.e. whether it is deblurring, SR, or JPEG decompression). This is definitely an interesting and practical question, which, when solved, will have a high impact in the field.

### Weaknesses
1. Focusing on blind deblurring, UFODM becomes similar to FastDiffusionEM, which also uses $\Pi$GDM update step for x, and uses MAP to update the kernels. The difference is that [1] uses the plug-and-play denoiser prior augmented with expectation-maximization (EM) approach, which is usually superior to standard gradient descent. Given that the UFODM does not compare directly with [1], I can only guess that it will be inferior to FastDiffusionEM.

2. Extending 1, I think the authors must compare against FastDiffusionEM. One might complain that it is only an arxiv paper yet, but considering the highly fast-growing and competitive nature of the field, and also given that the code is already open-sourced, it wouldn't take too long to run a head-to-head comparison against it.

3. Even when comparing against BlindDPS [2] and GibbsDDRM [3], it does not seem that UFODM consistently outperforms the prior arts. Yes, it does outperform [2,3] when time-travel trick is utilized, but time-travel is a standard trick that can easily be incorporated into all of the solvers, which makes the comparison unfair. Given that UFODM is an ad-hoc mix of Gibbs sampling and MAP optimization, it is important to show the empirical strength, which, in my opinion, is insufficient.

4. The problem setting for unknown $\mathcal{H}$ is unrealistic. Considering even the canonical degradations that arise in computational photography, the number of classes in the set exponentially grows. This is especially true if we start to consider a mixture of degradations, which usually happen in the real-world. The current approach of selecting from a small, discrete set of forward operators does not adequately address the complexity of real-world scenarios where degradations are often a combination of multiple factors.

5. Even if the algorithm is not theoretically grounded, it is intuitive when one does not consider sampling from $\mathcal{H}$. However, the part of inferring $\mathcal{H}$ seems quite odd, or at least unrealistic. In order to choose $\mathcal{H}^*$, one has to run all the diffusion process for each candidate $\mathcal{H}$, which will be painfully slow as the number of possible class increases. Moreover, the criterion is the distance from the measurement, which does not seem to be a particularly *good* metric. My concern is corroborated from seeing that the accuracy of $\mathcal{H}$ for ImageNet is 61.3% even when there are only 3 classes to choose from. This indicates a fundamental weakness in the method's ability to reliably identify the correct forward operator, especially as the set of possible operators expands.

### Questions
1. What is UFODM short for? Unknown forward operator diffusion model?

2. I would strongly suggest to include a comparison against FastDiffusionEM [1]

3. When considering unknown forward operators, is the quality factor of JPEG compression inferred as a by-product of the blind inverse problem solver? For SR, is the blur kernel also inferred here?

4. It is said that $T'$ = 65 was chosen, which seems a bit ad-hoc. Do you use a strategy like CCDF [2] for initialization?

5. In the inner for loop of Algorithm 1, Line 8 and Line 10 iteratively samples for $\mathbf{x}_t$ and $\varphi$. When sampling for $\mathbf{x}_t$, a $\Pi$GDM step will be involved, and an NFE will be needed. When taking $T' = 65$ and $N = 100$ as stated in the paper, this would be inducing 6500 NFE, which is probably not the case. Is there a typo in the algorithm?


**References**

[1] Laroche, Charles, Andrés Almansa, and Eva Coupete. "Fast Diffusion EM: a diffusion model for blind inverse problems with application to deconvolution." arxiv 2023.

[2] Chung, Hyungjin, Byeongsu Sim, and Jong Chul Ye. "Come-closer-diffuse-faster: Accelerating conditional diffusion models for inverse problems through stochastic contraction." CVPR 2022.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good
