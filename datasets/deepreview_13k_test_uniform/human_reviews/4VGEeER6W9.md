# Towards Non-Asymptotic Convergence for Diffusion-Based Generative Models

- Decision: Accept
- Scores: 6, 8, 8, 8

## Abstract
Diffusion models, which convert noise into new data instances by learning to reverse a Markov diffusion process, have become a cornerstone in contemporary generative modeling. While their practical power has now been widely recognized, the theoretical underpinnings remain far from mature.  In this work, we develop a suite of non-asymptotic theory towards understanding the data generation process of diffusion models in discrete time, assuming access to $\ell_2$-accurate estimates of the (Stein) score functions. For a popular deterministic sampler (based on the probability flow ODE), we establish a convergence rate proportional to $1/T$ (with $T$ the total number of steps), improving upon past results; for another mainstream stochastic sampler (i.e., a type of the denoising diffusion probabilistic model), we derive a convergence rate proportional to $1/\sqrt{T}$, matching the state-of-the-art theory. Imposing only minimal assumptions on the target data distribution (e.g., no smoothness assumption is imposed), our results characterize how $\ell_2$ score estimation errors affect the quality of the data generation process.  In contrast to prior works, our theory is developed based on an elementary yet versatile non-asymptotic approach without resorting to toolboxes for SDEs and ODEs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper delves into the intricacies of diffusion models, a unique class of models capable of converting noise into fresh data instances through the reversal of a Markov diffusion process. While the practical applications and capabilities of these models are well-acknowledged, there remains a gap in the comprehensive theoretical understanding of their workings. Addressing this, the authors introduce a novel non-asymptotic theory, specifically tailored to grasp the data generation mechanisms of diffusion models in a discrete-time setting. A significant contribution of their research is the establishment of convergence rates for both deterministic and stochastic samplers, given a score estimation oracle. The study underscores the importance of score estimation accuracies. Notably, this research stands apart from prior works by adopting a non-asymptotic approach, eschewing the traditional reliance on toolboxes designed for SDEs and ODEs.

### Strengths
This paper offers a significant theoretical advancement by providing the convergence bounds for both stochastic and deterministic samplers of diffusion processes. I'm particularly struck by the elegance of their results, especially given the minimal assumptions required—for instance, the results for stochastic samplers rely solely on Assumption 1. These theoretical findings provide a clear understanding of the effects of score estimation inaccuracies. Furthermore, the emphasis on the estimation accuracies of Jacobian matrices for deterministic samplers sheds light on potential training strategies, suggesting the incorporation of penalties in objective functions when learning the score function for these samplers. Additionally, the proof presented is elementary, and potentially useful in a broader context.

### Weaknesses
- While this paper doesn't present any algorithmic advancements, it's understandable considering the depth of their theoretical contributions.

- The proof appears to be procedural. I was hoping for deeper insights into how the proof was constructed. It might be beneficial for the authors to include a subsection detailing the outline and insights behind their proof.

### Questions
- Eq. (14), just want to confirm: should it be $dX_t = \sqrt{1-\beta_t}X_td_t$ instead of $-\frac{1}{2}\beta(t)X_t d_t$? 
- Eq. (15), maybe I am missing something, but should it be $dY = (-f(...) + \frac{1}{2}g^2 \nabla) d_t$? The original paper was taking a reverse form. 
- Eq. (16), similar question to Eq. (15). 
- Eq. (21), I feel a bit weird about the notation: maybe remove the $R$. 
- The results for deterministic samplers may motivate a better training strategy (i.e., incorporating the requirement for Jacobian matrices accuracy). The first step is to verify that this phenomenon exists in experiments (i.e., a worse $\epsilon_{Jacobi}$ does imply a worse sampling result). It may be worth adding a numerical experiment to confirm this if time permits.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper aims to provide a systematic analysis of the convergence rate of both deterministic and stochastic samplers of the diffusion models in the context of generative modeling. The authors proves, under certain assumptions, the former has a rate of $T^{-1}$
while the latter has a rate $\sqrt{T}$ which is consistent with the previous empirical observations. The authors also proposed some improvements, leading to a rate of $T^{-2}$ in the deterministic case, and a rate of $T^{-1}$ in the stochastic case.

### Strengths
This paper provides an early systematic analysis on the convergence rate of samplers in the diffusion models. Both deterministic and stochastic cases are considered, and their results are almost optimal under the assumptions made. The presentation of the paper is good, and I really enjoyed reading it. Especially, I like Theorem 1.

### Weaknesses
As for every (good) paper, there are always plenty of things remained to be done. For instance,

(1) It is worthy to comment on the learning rate (22a)-(22b). I understand these rates are carefully chosen in order to match the rates in the theorems. The author may mention this, or provide some explanations/insights on it.

(2) The paper, like Chen et al., deals with the TV (or KL) divergence. I understand that under these metrics, one can prove "nice" theoretical results using some specific algebraic identities (flow...) On the other hand, practitioners may care more about the FID (or Wasserstein distance) -- part of the reason is that Wasserstein distance is "closer" to how humans distinguish pictures. The authors may want to add a few remarks on this.

### Questions
See the weaknesses.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the deterministic probability flow ODE-based sampler often used in practice for score-based diffusion. It shows that the ODE-based sampler gets a $1/T$ convergence rate, improving upon the SDE-based sampling rate of $1/\sqrt{T}$. The techniques are elementary, and do not rely on Girsanov's theorem and other techniques from the SDE/ODE toolboxes. While there was prior work (Chen et. al. 2023b) that obtains an improved guarantee for the ODE-based sampler, their analysis required the use of stochastic "corrector steps", while in practice, even just the ODE-based sampler without corrector steps seems to perform well. This is the first work that provides theoretical evidence that the vanilla ODE-based sampler can outperform the SDE-based sampler in practice.

### Strengths
- Provides the first analysis of the (vanilla) ODE-based sampler for score-based diffusion models that gives some theoretical evidence for why it outperforms the SDE-based sampler in practice ($1/T$ convergence instead of $1/\sqrt{T}$)
- New analysis that doesn't make use of Girsanov's theorem/other results from the ODE/SDE literature.
- Doesn't require Lipschitzness of score unlike (Chen et al 2023b), but pays in d dependence

### Weaknesses
- $d$ dependence is worse than (Chen et al 2023b). In particular, Chen gets a $\sqrt{d}$ dependence for the ODE-based sampler when using stochastic corrector steps, which is better than the previous bound of $d$ for the SDE-based sampler. This paper on the other hand gets a $d^3$ dependence, which is significantly worse than both these bounds. 
- Requires Jacobian of score to be estimated accurately, rather than just the score
- Requires the distribution $q_0$ to be bounded, and bound is stated in terms of this bound. In contrast, some of the prior works only required the second moment of $q_0$ to be bounded.
- While new analysis is "elementary" in that it doesn't require SDE/ODE machinery, it seems much longer/more complicated than the previous analyses. Would really appreciate a condensation/proof overview in the main paper.

### Questions
- Is it clear that $1/\sqrt{T}$ is tight for the SDE-based sampler, and $1/T$ is impossible?
- What are the barriers to getting a $d$ or $\sqrt{d}$ dependence? Can you write something about this in the main paper?
- Can you include a proof overview in the main paper?
- Why is the proof so long? Can it be condensed?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper develops theoretical analyses for two variants of score-based generative models, those with deterministic (known as the probability flow ODE) and stochastic (known as denoising diffusion probabilistic models) reverse time processes, respectively. The deterministic variant is of particular interest because it has been difficult to analyze with existing techniques, despite being successful in practice. The main contribution of this work is to derive convergence guarantees for each of these processes under mild assumptions on the data distribution and the score function. Briefly, they provide an analysis of the deterministic algorithm which is the first to provide explicit rates of convergence, when the data distribution has bounded support (with only logarithmic dependence on the diameter) and when the score function and its Jacobian have been estimated. For the stochastic algorithm they recover similar results to the state-of-the-art, albeit with worse dimension dependence and stronger assumptions on the data distribution (compact support vs finite second moment).

### Strengths
This work studies an important problem, that of developing theoretical understanding of the efficacy of score-based methods, and focuses in particular on deterministic methods, which are not well understood theoretically. They develop the first analysis to achieve explicit rates of convergence for these methods in the literature, and achieve a strong bound under assumptions which are quite mild (except for the Jacobian assumption). For the stochastic method, they gain results which are close to the best known. Their analysis is necessarily novel and avoids technical difficulties that have forced previous works [1] to study (stochastic) modifications of the fully deterministic methods.

[1] The Probability Flow ODE Is Provably Fast, by Chen et al 2023

### Weaknesses
From my point of view, the main weakness of the results is that they involve the error of the differential of the score function, and it is not clear why this would be well-controlled in general (since the score-matching objective doesn't involve the Jacobian). The prior work [2] didn't use such conditions, but then again achieved far weaker guarantees. It would be good to comment on the importance and plausibility of this condition. Less significant but nonetheless important is the authors' use of very specific step-size schemes, a remark on this would also be helpful. Finally, their convergence results are proved in TV (weaker than KL) and are not for the true data distribution, but for the distribution of the first step of the forward diffusion process.

With regard to correctness of their arguments, I was not able to carefully check this point due to the long and involved natured of their proofs but everything that I did read in the supplementary material seems correct.

[2] "Restoration-degradation beyond linear diffusions: A non-asymptotic analysis for DDIM-type samplers" by Chen, Daras, and Dimakis 2023

### Questions
- Please add a remark about the fact that you prove your guarantees for convergence to the first step of the forward process (rather than the true data distribution). Of course, this is what allows for guarantees in TV with minimal assumptions on the data distribution since otherwise the data distribution could be singular, but I wonder how much this changes your results.
- Are the step-size schemes you consider similar to those used in practice? How robust are your results to variations in the step-sizes?
- Please discuss the utility and plausibility of the bound on the difference of Jacobians
- Could you please clarify the meaning of "continuous" in the assumption on the data distribution when it is says "$X_0$ is a continuous random vector, and". In particular, are you assuming the data distribution has a density wrt Lebesgue here?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
