# Prior Mismatch and Adaptation in PnP-ADMM with a Nonconvex Convergence Analysis

- Decision: Reject
- Scores: 6, 5, 6, 8

## Abstract
\noindent
Plug-and-Play (PnP) priors is a widely-used family of methods for solving imaging inverse problems by integrating physical measurement models with image priors specified using image denoisers.  PnP methods have been shown to achieve state-of-the-art performance when the prior is obtained using powerful deep denoisers. Despite extensive work on PnP, the topic of \emph{distribution mismatch} between the training and testing data has often been overlooked in the PnP literature. This paper presents a set of new theoretical and numerical results on the topic of prior distribution mismatch and domain adaptation for \emph{alternating direction method of multipliers (ADMM)} variant of PnP. Our theoretical result provides an explicit error bound for PnP-ADMM due to the mismatch between the desired denoiser and the one used for inference. Our analysis contributes to the work in the area by considering the mismatch under \emph{nonconvex} data-fidelity terms and \emph{expansive} denoisers. Our first set of numerical results quantifies the impact of the prior distribution mismatch on the performance of PnP-ADMM on the problem of image super-resolution. Our second set of numerical results considers a simple and effective domain adaption strategy that closes the performance gap due to the use of mismatched denoisers. Our results suggest the relative robustness of PnP-ADMM to prior distribution mismatch, while also showing that the performance gap can be significantly reduced with few training samples from the desired distribution.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This article proposes a theoretical analysis of PnP-ADMM algorithm under a mismatch on the prior.

### Strengths
The study of prior mismatch in inverse problems is a timely topic. This paper provides an explicit error bound on the solution of PnP-ADMM, which is challenging, and can be inspiring for the inverse problem community. The numerical experiments are well done can suggests an improvement with respect to the current literature.

### Weaknesses
The reviewer regrets the lack of contextual explanations on the result presented in Theorem 1, as well as of discussion on the significance of the performance metrics used in the analysis. The numerical simulation do not highlight the performance of the reconstruction of the proposed method with respect to the error bound proposed in Theorem 1. Specifically, the paper does not clearly articulate how the derived error bound in Theorem 1 translates into practical implications for the PnP-ADMM algorithm's performance under prior mismatch. The connection between the theoretical error bound and the observed reconstruction quality in the experiments is not made explicit, leaving the reader to infer the practical relevance of the theoretical findings. Furthermore, the choice of performance metrics (e.g., PSNR, SSIM) is not justified in the context of the specific problem being addressed, and there is no discussion on how these metrics relate to the theoretical error bound.

### Questions
N/A

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors proposed theoretical analysis of discrepancy between the desired and mismatched denoisers in PnP-ADMM and can also applicable in non-convex data-fidelity terms and non-expansive denoisers. The experiment show that using a simple domain adaptation method can addressing the problem in PnP-ADMM on several super-resolution and deblurring datasets.

--- Post-rebuttal
I read the rebuttal and would like to keep the score.

### Strengths
The authors theoretically proves the gap between the denoiser in PnP-ADMM, including limitation and application boundaries.

### Weaknesses
1. The gap of pnp denoiser is a common view for many years, a series of work aiming to solve this problem are proposed like [1,2], but the authors do not compare even a single method.
[1] Shocher, Assaf, Nadav Cohen, and Michal Irani. "“zero-shot” super-resolution using deep internal learning." Proceedings of the IEEE conference on computer vision and pattern recognition. 2018.
[2] Tirer, Tom, and Raja Giryes. "Super-resolution via image-adapted denoising CNNs: Incorporating external and internal learning." IEEE Signal Processing Letters 26.7 (2019): 1080-1084.

2. The details of domain adaptation method are not described such as loss function and training time. The computational resources of domain adaptation process are not mentioned either. Usually, the training need 2-3 times larger GPU memory than simply implement inference. Additional data and computational resources for training may not appropriate for the pnp method which is designed for non supervision.

### Questions
1. Only SR and deblurring are selected as example tasks. Some more complex inverse problem such as the compressive sensing and phase retrieval?

2. What if the there is no ground truth in a real-world test dataset? Does it mean that we have to manually label find several images which are close to the test set?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper investigates the impact of mismatched denoisers in PnP-ADMM, offering theoretical insights and empirical validation on image super-resolution while introducing a domain adaptation strategy to mitigate distribution mismatch effects, i.e. distribution alignment. The convergence analysis of this work does not require convex data-fidelity and non-expansive denoiser assumptions.


------------------------------------------post-rebuttal------------------------------------------

Thank you for your thorough responses. I've reviewed your replies to my questions and the revised paper. The changes made in the revised paper have contributed to a better understanding of your work and I'm satisfied with the changes made. I am inclined to reassess the paper positively and recommend acceptance.

### Strengths
Novelty: A theoretical error bound for PnP-ADMM under mismatched denoisers is derived, without the constraints of convex data-fidelity and non-expansive denoiser assumptions.

Significance: It shows the pivotal role of domain adaptation in mitigating the effects of distribution shifts on image priors.

### Weaknesses
Experimental Limitations: The paper's experiments primarily focus on super-resolution and deblurring with negligible measurement noise, limiting the comprehensiveness of the investigations. It lacks exploration of scenarios with nonconvex data-fidelity terms, which would enrich the analysis and diversify the paper's empirical scope. Specifically, the exclusive use of the \(\ell_2\) norm for data fidelity limits the applicability of the findings to a narrow class of problems. The absence of experiments with, for example, \(\ell_1\) norm or total variation regularization, which are common in robust recovery scenarios, leaves a gap in demonstrating the method's versatility. Furthermore, the noise level of 0.01 appears to be too low to effectively evaluate the robustness of the proposed approach in practical, noisy conditions.

Inadequate Literature Review: The related work presented in the paper lacks depth and breadth (e.g., in domain adaptation, and review of previous work). The discussion on domain adaptation is particularly shallow, failing to adequately cover the diverse range of techniques available, such as adversarial training, transfer learning, and meta-learning. The review of previous work on PnP methods also lacks a detailed comparison of the assumptions made in other theoretical analyses, making it difficult to understand the novelty and contribution of this work in the context of existing literature.

### Questions
The paper in question would benefit from addressing several issues:

    1. The paper incorrectly describes PnP as a class of deep learning algorithms (e.g., “PnP has emerged as a class of DL algorithms”, “MBDL approaches include methods such as PnP, RED, …”, “PnP is one of the most popular MBDL approaches for solving image inverse problems”). It is essential to clarify that PnP is an iterative framework in which a denoiser can be incorporated as an implicit prior model. The presence of a deep denoiser within PnP does not classify it as a class of deep learning algorithms.

    2. In the second paragraph of Page 1, it is advisable to provide a brief introduction to PnP, with more detailed information presented in the Background section.

    3. On Page 1, the sentence “Despite extensive literature on PnP, the research in the area has mainly focused on the setting where the distribution of the test or inference data is perfectly matched to that of the data used for training the image denoiser” should be rewritten to specifically refer to approaches utilizing deep learning-based denoisers within PnP.

    4. The sentence on Page 1, “Little work exists for PnP under mismatched priors” should be substantiated with appropriate references, such as (Shoushtari et al., 2022), and other relevant works. It is recommended to create a subsection or, at the very least, a paragraph discussing the similarities and differences between the present work and that of (Shoushtari et al., 2022), aside from variations in the PnP framework and applications.

    5. On Page 1, in the sentence “The success of PnP has resulted in denoising diffusion probabilistic models”, it is advisable to cite each topic individually, as appropriate.

    6. It is suggested to briefly define “domain adaptation” in the Introduction, considering that the term is used five times before its formal definition in Section 4.2. Additionally, different strategies in domain adaptation should be mentioned (e.g., see 10.1109/CVPR.2014.187 and 10.1109/ACCESS.2019.2929258) to provide context for the selected ‘distribution alignment’ strategy and to explain why it was selected. Please also explain how a limited number of data from target distribution can address the mismatched prior distribution.

    7. On Page 2, considering the provided definition of model-based deep learning (DL) as “methods that integrate the measurement model as part of the deep model”, it is necessary to clarify how employing DL-based denoisers within PnP/RED aligns with this definition. The relationship, if any, between model-based DL, model-based iterative reconstruction/recovery, and physics-informed DL should also be addressed.

    8. On Page 2, the references cited after “DL methods seek to perform a regularized inversion … by a deep convolutional neural network (CNN)” are irrelevant to the context of this sentence and can be omitted. Instead, references such as (McCann et al., 2017; Lucas et al., 2018; Ongie et al., 2020; Monga et al., 2021) are more suitable in this context.

    9. A table of assumptions for the cited references regarding the theoretical convergence analyses of PnP should be considered. Such a table would be valuable for readers to understand the differences between these works and the current study.

    10.  The experiments detailed in Section 4 raise a query: is the measurement noise level consistently set at 0.01? If so, this level of noise appears comparable to the noise-free scenario. It would significantly enhance the paper to explore the impact of more robust and varying levels of measurement noise on the obtained results, underlining the model's performance in noisier conditions.

    11.  While the experiments concentrate on convex data fidelity terms using the $\ell_2$ norm, it would be advantageous to broaden the scope by including experiments with nonconvex data-fidelities. Extending the experiments to encompass nonconvex scenarios would further corroborate the claims made in the paper. 

    12.  The paper presents Theorems 1 and 2, providing theoretical support for the proposed methodologies. It would be beneficial to provide a descriptive narrative of the results or outcomes derived from these theorems to facilitate a more comprehensive understanding for readers. 

    13.  Sections A-D of the Appendices delve into the topic of “the optimality condition for mismatched MMSE denoiser.” Further explanation is required to enhance the clarity and comprehension of this topic.

    14.  A point of inquiry arises in relation to Page 15 (above Eq.(13)) regarding the derivation of $\nabla\hat{h}(z^k)=\frac{1}{\gamma}(s^{k-1}+x^k-z^k)=\frac{1}{\gamma}s^k$. Similarly, clarity on the derivation of Eq.(16) on Page 16 would fortify the readability and comprehensibility of the paper.

    15.  An observation on the gradient of h in Eq.(16) leads to a query: shouldn't the gradient of Eq.(18) be zero? As $\nabla \frac{1}{2\gamma}\|z-(x^k+s^{k-1})\|_2^2 = \frac{1}{\gamma}(z-(x^k+s^{k-1}))$ and $\nabla h(z) = \frac{1}{\gamma} (x^k+s^{k-1}-z)$.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the behavior of plug-and-play priors with the alternating directions method of multipliers (ADMM) in case there is a mismatch in the distribution of the data the denoising prior has been trained on and the data it is applied to. The authors assume the denoisers to be perfect  minimum mean squared error (MMSE) estimators and prove convergence of the plug-and-play prior ADMM under this (as well as a few more technical) assumption. Moreover, they provide an estimate for how much the gradients of the underlying objective  function corresponding to the ideal MMSE prior differ from zero if a prior trained on a different distribution is used. Numerical experiments demonstrate (not surprisingly) that using prior trained on a different distribution can lead to suboptimal results and that (surprisingly) as few as 4 images are enough to fine-tune the denoiser to yield significantly better results.

### Strengths
- The paper conducts an interesting theoretical analysis on a problem that has received comparably little attention in the literature so far. 
- It demonstrates numerically that even a small number of images can help to fine-tune (domain-adapt) a denoiser such that it performs significantly better within the plug-and-play framework in case of domain shifts.

### Weaknesses
 - At first, I just wanted to state that the theorems are impossible: As $(x^0, z^0, s^0)$ is the (arbitrary) starting point of the ADMM algorithm, it is impossible to ensure that $\phi(x^0, z^0, s^0) - \phi^* \geq 0$, which immediately contradicts the inequality in Theorem 2. Yet, I think this is just a typo, i.e., one needs to start with the first iteration of the ADMM algorithm to make the theorem work. I'd like to ask the authors to briefly confirm this as I have not checked any proof.
- I cannot judge the contribution on the theoretical side very well yet. I phrased a question on this below.
- The practical implications of the paper are not large (= it is good to know that a setting similar to what everyone does in practice converges, but the assumptions are of course never verifiable exactly; knowing a constant by which the gradient of the objective differs from zero still makes it hard to say something about the point one converges to).

Yet, the third point is not uncommon for theory-inspired papers and would not keep me from recommending the acceptance of this work.

### Questions
- Even after realizing that the theorems' starting points might just have been a typo, the results still appeared to be a little surprising (as the augmented Lagrangian is not monotone in the usual convex ADMM setting). Then, I, however, remembered the paper "Global Convergence of ADMM in Nonconvex Nonsmooth Optimization", where the augmented Lagrangian was also used as a Lyapunov function (which might therefore be worth citing). How similar/different is the conducted convergence analysis from taking existing literature on the analysis of nonconvex ADMM (the one I cited, versions that make smoothness assumptions, and those that have possibly considered an inaccurate evaluation of the prox) and just making assumptions that allow you to return to such a known analysis?  Things like 'summable errors' in substeps of such algorithms are also very common in the general optimization literature. 
- The paragraph below Theorem 2 speaks of convergence to a stationary point. Convergence is, however, not what the theorems state. Is this something that comes out of the actual proof in the supplement? If so, it would be worth stating in the main paper. If not, please rephrase. 
- In assumption 6, one needs the inequality to be satisfied for all stationary points of the augmented Lagrangian, and the theorems are to be interpreted as "there exists $(x^*, z^*, s^*)$ such that ...", correct? Does the existence of a stationary point have to be assumed or do the assumptions guarantee that?
- Can you please comment on assumption 1: Isn't it common to assume that "realistic" images lie in some set (e.g. a union of subspaces) much smaller than the dimension of the space? Would that cause a problem for assumption 1?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
