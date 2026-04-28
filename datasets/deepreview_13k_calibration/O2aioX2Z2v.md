# Stochastic Deep Restoration Priors for Imaging Inverse Problems

- Decision: Reject
- Avg Score: 4.20
- Scores: 3, 5, 6, 1, 6

## Abstract
Deep neural networks trained as image denoisers are widely used as priors for solving imaging inverse problems. While Gaussian denoising is thought sufficient for learning image priors, we show that priors from deep models pre-trained as more general restoration operators can perform better. We introduce \emph{Stochastic deep Restoration Priors (ShaRP)}, a novel method that leverages an ensemble of such restoration models to regularize inverse problems. ShaRP improves upon methods using Gaussian denoiser priors by better handling structured artifacts and enabling self-supervised training even without fully sampled data. We prove ShaRP minimizes an objective function involving a regularizer derived from the score functions of minimum mean square error (MMSE) restoration operators, and theoretically analyze its convergence. Empirically, ShaRP achieves state-of-the-art performance on tasks such as magnetic resonance imaging reconstruction and single-image super-resolution,  surpassing both denoiser- and diffusion-model-based methods without requiring retraining.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper extends the work of [Hu et al., 2024c] for the regularization of inverse problems using a deep restoration prior trained on multiple restoration tasks. The authors theoretically analyze the induced objective function and the convergence of the proposed algorithm. Empirical results demonstrate that the framework outperforms Gaussian denoiser priors in image reconstruction tasks, including MRI and super-resolution.

### Strengths
1. The experiments show that training a deep restoration network on multiple tasks can improve its regularization capability.

2. Theoretical analysis is also provided.

### Weaknesses
1. The paper seems limited in novelty and closely resembles [Hu et al., 2024c]. The main contribution is the training of a restoration prior across the same task with varying levels of ill-posedness. The authors should clearly explain how the proposed methodology differs from [Hu et al., 2024c]. Specifically, the core idea of using a learned prior for regularization is not new, and the incremental improvement of training on multiple levels of the same task needs more justification as a significant contribution. The theoretical analysis, while present, does not seem to introduce fundamentally new concepts beyond what is already established in the literature for similar optimization problems. 

2. The authors claim that the proposed prior trained on a general restoration task outperforms Gaussian denoisers; however, there is a lack of sufficient experiments to support this claim. Gaussian denoisers can be used for solving general inverse problems, but the experiments presented here are confined to the same inverse problem and forward operator on which the prior was trained, although with different levels of ill-posedness. For example, in Section 5.1, the restoration prior is trained on MRI with an x8 acceleration and applied to the same problem with x4 and x6 acceleration factors. Although Algorithm 1 suggests that the proposed prior can be used to solve any other inverse problems, the experiments are limited to the same problem type. To validate the claimed superiority over Gaussian denoisers, the authors are requested to include experiments where the trained prior is applied to a different inverse problem from the one it was originally trained on. For example, training the prior on super-resolution and using it for solving MRI reconstruction. You can also train your prior on multiple distinct tasks as suggested by Algorithm I, for example training the prior on super-resolution and image in-painting tasks, and use it for solving a different task like MRI. This comparison is crucial as Gaussian denoisers can solve any other different inverse problems once trained.

### Questions
Please take a look at the comments under weaknesses

### Soundness
3

### Presentation
3

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
The paper proposes a new approach for learning a regularizer for linear imaging inverse problems. While Gaussian denoisers have been successfully used as effective image priors, the authors extend the idea by using more general restoration operators as image priors. In the numerical experiments, the authors show the reconstruction performance with their new “ShaRP” regularizers for two important inverse problems (compressive MRI and single-image super-resolution). The numerical experiments are performed with ShaRP regularizers trained in supervised and self-supervised manners.

### Strengths
1. Using general restoration operators instead of simple Gaussian denoisers is interesting and novel. Theorem 1 also puts this idea on a solid theoretical foundation. 

2. The experimental results are compelling. Comparison of ShaRP with different baseline methods, especially PnP algorithms that utilize Gaussian denoisers, provides evidence for the claim made by the authors in the abstract.

### Weaknesses
1. The motivation for using a general restoration prior, derived from training a deep reconstruction operator for linear inverse problems with multiple degradation operators, to solve another linear inverse problem is not entirely convincing. While learning Gaussian denoisers is fundamentally easier than solving a general inverse problem with an ill-posed operator, this distinction does not hold in the present case. The claim that a restoration operator can be trained to approximate the conditional expectation E[x|s, H] better than a Gaussian denoiser when the degradation is not simple additive white Gaussian noise needs more rigorous justification. Specifically, the paper should elaborate on why a restoration prior tailored to specific degradation types offers a significant advantage over a more general prior learned through Gaussian denoising, especially when the forward operator for the target inverse problem differs from those used in training the restoration prior.

2. The novelty in the convergence analysis, particularly in Theorem 2, is not clearly established. The assumptions and the result appear to closely follow the work presented in "A Guide Through the Zoo of Biased SGD" [1]. The paper needs to explicitly differentiate its theoretical contributions from this existing work. For instance, if Theorem 2 is a direct application of the results in [1], this should be acknowledged. If there are subtle differences in the assumptions or the derived results that offer new insights, these need to be highlighted and their implications discussed.

3. The theoretical analysis does not adequately explain the experimental results obtained with a restoration operator trained in an unsupervised manner. The training loss used in the unsupervised case (Algorithm 3) does not seem to correspond to a restoration operator that approximates the conditional expectation $E[x|s, H]$. This discrepancy between the theoretical framework, which assumes an MMSE estimator, and the practical implementation using unsupervised learning needs to be addressed. The authors should clarify whether the restoration operator learned through unsupervised training can still be interpreted as a biased SGD update and, if not, provide an alternative theoretical justification for its effectiveness.

4. Several statements in the introduction and background sections lack precision and require clarification. For instance, the claim that "ShaRP provides a richer and more flexible representation of image priors" is vague. The authors should define what constitutes "richer and more flexible" in this context. Similarly, the statement that "restoration models in ShaRP can often be directly trained in a self-supervised manner" needs to be contrasted with unsupervised training methods for Gaussian denoisers, such as those using a SURE loss. The paper should clearly articulate the advantages of ShaRP's self-supervised training in comparison to existing approaches.

5. The introduction of the regularization concept in the paper, which encourages solutions that produce degraded versions closely resembling real degraded images, needs further clarification. The paper should specify that this property holds when the degradation matches the one used to train the restoration network, not necessarily the forward operator "A" of the target inverse problem. Furthermore, it should be discussed whether a simple Gaussian denoiser, combined with a data-consistency loss, could achieve a similar outcome. The paper should also address the practical implications of the assumption in Theorem 1 that the prior density $p_x$ is non-degenerate over $\mathbb{R}^n$, which is often not true in real-world scenarios.

### Questions
1. Page 1: “...Tweedie’s formula (Robbins, 1956; Efron, 2011) seemingly implies that Gaussian denoising alone might be sufficient for learning priors,...”: That is indeed true and this work does not disprove this fact. 

2. Page 2: “...ShaRP provides a richer and more flexible representation of image priors…”: At this stage, it is rather vague as to what “richer and more flexible” means. 
3. Page 2: “Unlike Gaussian denoisers, the restoration models in ShaRP can often be directly
trained in a self-supervised manner”: Even Gaussian denoisers can be trained in an unsupervised manner using only noisy images (e.g., using a SURE loss). 

4. It might be good to put some of the math background in the intro, effectively shortening the material in the first three pages. 

5. Page 3: “We introduce a novel regularization concept for inverse problems that encourages solutions that produce degraded versions closely resembling real degraded images.”: Firstly, this would be the case if the degradation is the same for which the restoration network is trained, not the forward operator “A” for which you want to solve the inverse problem. Secondly, can one not promote this property using a simple Gaussian denoiser together with a data-consistency loss? 

6. Theorem 1: “Assume that the prior density $p_x$ is non-degenerate over $\mathbb{R}^n$”: This is almost always not true. 

7. Assumption 3: Define what “$b(x)$” is. 

Requested changes:

1. Provide a comprehensive review of the convergence analysis of biased SGD in terms of the assumptions and results to put your theoretical contributions in perspective. 

2. Clarify whether one can approximate the conditional expectation $E[x|s, H]$ using a restoration operator trained on a self-supervised loss. If not, the interpretation of ShaRP as biased SGD does not hold in this case.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces a novel concept termed ShaRP for stochastic priors for the regularization of inverse problems. At its core, a set of $b$ restoration problems is considered, for which the MMSE is minimized. In this setting, ShaRP is the expectation of the probability of the degraded version of the images given the probability density of the observations. Under certain assumptions, a closed-form solution of the gradient of the regularizer is derived and the convergence of $\nabla f$ is shown. The results are numerically tested for CS-MRI and SISR.

### Strengths
The paper introduces a novel concept for stochastic priors, which is complemented by two important theoretical assertions (see summary). The assumptions can be regarded as mild. Both results are highly relevant for numerical experiments. 
The paper remarkably advances SOTA for CS-MRI and is on par with competing methods in the case of SISR.

### Weaknesses
The presentation of the paper could be improved in some places. In particular, Section 4 lacks a concise introduction to the motivation behind the concept of ShaRP. The core idea, maximizing the probability of degraded versions of x in the distribution p(s|H) where H is sampled from p(H), needs further elaboration. A more intuitive explanation of this concept would significantly enhance the reader's understanding. Furthermore, the parameter $b$, representing the number of restoration problems, is essential for numerical performance. However, the paper lacks a substantial discussion of the role of this parameter. The interplay between $b$ and the restoration problems needs to be clarified. Specifically, how does varying $b$ affect the results? Additionally, no details about the role of $\alpha$ (see Section 5.1) and its impact on the results were provided. The influence of $\alpha$ on the overall performance should be thoroughly investigated. Finally, the results in Table 4 do not show a clear tendency for DiffPIR, DRP, or ShaRP. A more in-depth analysis is required to understand the conditions under which each method performs best and why there isn't a clear winner.

### Questions
1. Can you please provide more details about the impact of the choice of $b$ on the numerical results? An ablation study might help here. Likewise, you could numerically evaluate the impact of $\alpha$.
2. What happens if you modify the number of restoration priors in B.1.1?
3. Please rewrite the motivation in Section 4. In particular, I am missing a good motivation and reasoning for the actual definition in equation (6), which might help the reader to better understand ShaRP. In addition, the object $G_\sigma(s-Hx)$ could be better motivated from a mathematical point of view.
4. The results in Table 4 do not show a clear tendency for DiffPIR, DRP, or ShaRP. Is there a reason for this available? Are there specific conditions under which each method performs best?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
This paper extends the "deep restoration priors" approach from Hu et al 2024c from one degradation operator to multiple ones.

### Strengths
The paper is clearly written, for the most part.

### Weaknesses
This paper is a trivial extension of Hu et al 2024c.  In this paper, the degradation operator is randomly chosen from a set, whereas in Hu et al 2024c there was a single operator.  But this change led to no new challenges or questions.  For example, the "ShaRP" regularizer in (6) is a trivial extension of (9) in Hu et al 2024c that now takes an expectation over H.  Figure 2 in this paper is a direct copy of Figure 1 from Hu et al 2024c.  The experiments are conducted on different linear inverse problems, but there is no intellectual contribution there.

While the authors use multiple degradation operators, this extension is not significant. The core idea of using a learned prior remains the same, and the extension to multiple operators does not introduce any new theoretical or practical challenges. The regularizer, while now involving an expectation over multiple operators, is a straightforward application of the same principle used in Hu et al 2024c. The change is merely a notational adjustment to accommodate multiple operators, rather than a fundamental shift in the approach. The experimental results, while demonstrating the method's applicability to different inverse problems, do not provide any novel insights or address any new challenges that arise from the use of multiple operators. The choice of different linear inverse problems is not a contribution in itself, as the method is designed to be applicable to any such problem.

### Questions
I don't have any questions for the authors.

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces Stochastic deep Restoration Priors (ShaRP), a method that leverages an ensemble of deep restoration models to regularize imaging inverse problems. ShaRP improves upon Gaussian denoiser-based methods by handling structured artifacts more effectively, enabling self-supervised training without fully sampled data.

### Strengths
- The paper is well-written and easy to follow.
- The theoretical analysis of the convergence is thorough and well-explained.

### Weaknesses
1.  **Comparison to Diffusion-Based Methods:**
   The paper lacks a comprehensive comparison to diffusion-based methods, such as DiffIR [1] and DDRM [2]. Including these comparisons would strengthen the results and provide clarity on how ShaRP performs relative to other leading methods in the field.

2.  **Supervised vs. Self-Supervised ShaRP:**
   In line 154, the authors mention a key contribution: "We implement ShaRP with both supervised and self-supervised restoration models as priors and test it on two inverse problems: CS-MRI and SISR." However, the experimental section does not provide a direct comparison between the self-supervised and supervised versions of ShaRP for the same task. This comparison is necessary to assess the benefits of the self-supervised approach.

3.  **Self-Supervised Nature:**
   For a restoration network to be trained on a set of tasks, such as a set of blur kernels \(H_i\), access to ground truth data is still required. This approach, which involves sampling multiple times from the ground truth, raises questions about whether the method can truly be considered self-supervised. Clarification is needed regarding the self-supervised claim.

4.  **Use of Multiple Degradation Operators:**
   The rationale for using a set of degradation operators \(H_1, H_2, \ldots, H_k\) in cases where the target problem involves only a single fixed operator (e.g., \(H_1\)) is unclear. It would be helpful if the authors could explain why introducing multiple degradation operators is necessary or beneficial when solving a fixed-task problem.

### Questions
What is the practical inference time of the proposed method in comparison to state-of-the-art (SOTA) methods? Additionally, the visual comparisons presented do not clearly demonstrate significant improvements. It would be beneficial to include more compelling visual examples to better illustrate the advantages of the proposed approach.

### Soundness
3

### Presentation
3

### Contribution
2
