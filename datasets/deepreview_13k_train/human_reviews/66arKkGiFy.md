# Plug-and-Play Posterior Sampling under Mismatched Measurement and Prior Models

- Decision: Accept
- Scores: 6, 5, 6, 6

## Abstract
Posterior sampling has been shown to be a powerful Bayesian approach for solving imaging inverse problems. The recent \emph{plug-and-play unadjusted Langevin algorithm (PnP-ULA)} has emerged as a promising method for Monte Carlo sampling and minimum mean squared error (MMSE) estimation by combining physical measurement models with deep-learning priors specified using image denoisers. However, the intricate relationship between the sampling distribution of PnP-ULA and the mismatched data-fidelity and denoiser has not been theoretically analyzed. We address this gap by proposing a posterior-$L_2$ pseudometric and using it to quantify an explicit error bound for PnP-ULA under mismatched posterior distribution. We numerically validate our theory on several inverse problems such as sampling from Gaussian mixture models and image deblurring. Our results suggest that the sensitivity of the sampling distribution of PnP-ULA to a mismatch in the measurement model and the denoiser can be precisely characterized.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors study the influence of model mismatch on the invariant distribution of a certain model-based posterior sampler based on the unadjusted Langevin Algorithm. The model (a forward operator in some imaging application) and the prior (incorporated via a denoiser) factor in through the drift term. The authors prove that the distribution drift is controlled by the total size of the model mismatch (in the forward model and the denoiser).

### Strengths
It is great that the paper proves a theoretical result about a relevant topic where most work is highly empirical. The setting is very clear and the derivations seem sound (although I have not checked in great detail.) The authors work under fairly general assumptions and also illustrate their bounds empirically.

### Weaknesses
 - The contribution is somewhat incremental given all the preparatory work in Laumont et al. 2022. Model mismatch is certainly a relevant topic and it is nice to have a paper about it so this is a somewhat subjective statement relative to papers I've reviewed for ICLR this year.

- The prose is waffly, with too much hyperbole. An example: "In this section, our focal point resides in the investigation of the profound impact of a drift shift on the invariant distribution of the PnP-ULA Markov chain" which could be "In this section we study the impact of drift shift on...".

- There are also numerous typos and broken sentences, especially in the appendices.

- Under "Contributions" you say that you "provide a more explicit re-evaluation of the previous convergence results...", but I am not sure what this means.

- In "we focus on the task of sampling the posterior distribution to reconstruct various solutions...", what is meant by "various solutions"?

- In "... Markov chain can be naturally obtained from an Euler-Maruyama discretisation by reformulating the process ...", what is meant by "reformulating"?

- Before equation (7), Wasserstein norm should be Wasserstein metric (or distance); before (7), TV distance should be TV norm (which is what is defined in (7)). (Also: why are Rd vectors bold in (8) and not in (7)?)

- "pseudometric between two functions in Rd" -> taking values in Rd

- In Corollary 1.3 which norm is || A^1 - A^2 ||?

### Questions
- Under "Contributions" you say that you "provide a more explicit re-evaluation of the previous convergence results...", but I am not sure what this means.

- In "we focus on the task of sampling the posterior distribution to reconstruct various solutions...", what is meant by "various solutions"?

- In "... Markov chain can be naturally obtained from an Euler-Maruyama discretisation by reformulating the process ...", what is meant by "reformulating"?

- Before equation (7), Wasserstein norm should be Wasserstein metric (or distance); before (7), TV distance should be TV norm (which is what is defined in (7)). (Also: why are Rd vectors bold in (8) and not in (7)?)

- "pseudometric between two functions in Rd" -> taking values in Rd

- In Corollary 1.3 which norm is || A^1 - A^2 ||?

### Soundness
4 excellent

### Presentation
2 fair

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
This paper considers sensitivity analysis of posterior sampling in inverse problems using diffusion models. It analyzes the effects of mismatches to the drift function on the stationary distribution of Langevin sampling.The mismatch can arise due to uncertainty in the forward operator and due to the denoiser not being exactly the MMSE denoiser.

The main result is that the stationary distributions differ proportional to a pseudometric that depends on the drift mismatch.

### Strengths
The considered problem is relevant, especially in medical imaging, where we want algorithms to be robust to mismatch in the forward model.

Inverse problems using diffusion models is also an active area of research and the proposed results could be relevant.

### Weaknesses
 - The main result in Theorem 1 shows that the TV between the stationary distributions of two Markov chains that have different drift functions can be bounded in terms of the proposed ``posterior-$L_2$ pseudometric''. This pseudometric is defined in terms of the expectation of the difference between the two drift functions when samples are drawn from the stationary distribution of one of the drifts. It's not clear at all how this pseudo metric behaves, and whether it is sufficiently small for two drifts that are close. Specifically, while the authors use an $\epsilon$ for the mollification level of the denoiser, this does not directly relate to the closeness of the drifts themselves. The bound depends on the expectation of the difference of the drifts under one of the stationary distributions, which is not a typical measure of closeness and makes it difficult to interpret the practical implications of the result. It is unclear how this pseudometric relates to more standard measures of function similarity, such as the $L_\infty$ norm of the difference between the drift functions.

- It is also not clear how different the two stationary distributions are when compared to the continuous stationary distribution. This can be very different due to discretization error, and the paper does not provide sufficient analysis of this aspect. The theoretical results focus on the discrete-time Markov chain, but the connection to the underlying continuous-time process and its stationary distribution is not well established. This makes it difficult to assess the practical relevance of the bounds, as the discretization error could dominate the observed differences.

- There is very little comparison to existing results in the literature. Other than saying that their results are backwards compatible with Laumont et al 2022, the authors do not state what benefits / drawbacks their results face. The paper would benefit from a more thorough discussion of how its findings relate to and improve upon existing theoretical analyses of diffusion models and Langevin sampling. A more detailed comparison with other sensitivity analysis techniques would also be beneficial.

- The paper considers Langevin sampling, which is known to not mix very well -- most theoretical results in the literature consider ODE / SDE solvers for an Ornstein–Uhlenbeck process. The slow mixing of Langevin sampling could limit the practical applicability of the results, and the paper should discuss this limitation more explicitly. The theoretical analysis should also consider the impact of this slow mixing on the derived bounds.

- The upper bounds in Theorem 1 are specified in terms of $A_0, A_1, B_0, B_1$, without any mention on the dimension dependence of these quantities. This makes it difficult to assess the practical relevance of the bounds, especially in high-dimensional settings. The paper should provide more insight into how these constants scale with the dimensionality of the problem.

- Some statements are unsubstantiated. In the contributions section, the authors claim "This paper stresses that in the case of mismatched operators, there are no error accumulations." I don't see why this would we be true. This statement requires more justification and should be clarified or removed if not sufficiently supported by the theoretical results.

### Questions
Listed in the weaknesses section

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper studies the error bound of the plug-and-play unadjusted Langevin algorithm (PnP-ULA) under mismatched posterior distribution owing to mismatched data fidelity and/or denoiser. After rigorously deriving their main theoretical results, they provide some numerical experiments with simple settings to further support their theory.

### Strengths
- Sections 1–4 are generally clearly written. The readers can get what the authors try to convey without diving into the mathematical details.
- The quantification of the error bound for PnP-ULA under a mismatched posterior distribution is of theoretical importance.

### Weaknesses
 - The section associated with the numerical experiment is hard to dig out. Particularly, it's not easy to understand how and why the proposed setting can be adopted to validate the theoretical corollary.
- As claimed by the authors, "our results can be seen as a PnP counterpart of existing results on diffusion models.", which therefore weakens the novelty of this paper.
- It seems like the theoretical results drawn rely on "oracle" information that is unavailable in practice. So the practical use of this theoretical tool is largely unclear for me.

### Questions
See above

____
After rebuttal: the authors addressed my concerns, thus I raise my score.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a theory of the plug-and-play unadjusted Langevin algorithm (PnP-ULA) to solve inverse problems, that builds and improves upon a prior work [1]. Specifically, the main theorem quantifies the distributional error of PnP-ULA under prior shift and the likelihood shift, which are both practical questions in the field of inverse imaging. Numerical experiments including the analytical GMM experiment and the image deblurring experiment solidify the correctness of the theorem.

### Strengths
1. The paper is well-written, concise, and clear.

2. The theory given in the paper is solid, with numerical experiments building support for the proposed theorem. The theory is practical and non-vacuous, as mismatch in the prior or in the likelihood happens (at least to a minimal amount) on virtually every application that you can think of.

3. The subject of the paper is well-suited for the conference, given the popularity of diffusion models on solving inverse problems.

### Weaknesses
1. The prior mismatch model, and the likelihood mismatch model, are not too realistic.

1-1. For the prior mismatch, it would be more interesting if one could see the effect when the underlying training distributions are different. For example, in the context of medical imaging, [5,6] demonstrated that diffusion models are particularly robust under prior distribution shifts. A discussion would be useful.

Note that I understand why the authors opted for the number of parameters for a DNN when they assumed a mismatch from the perfect MMSE estimator. However, given the current landscape of ML/generative AI, this situation would be easily solvable by more compute, whereas solving the data distribution shift is a much harder and realistic problem.

2. The authors cite [1] as an example of a mismatched imaging forward model. Correct me if I am wrong, but as far as I understand, when using unconditional denoisers as in PnP-ULA, [1] uses the exact forward operator that were used to generate the measurement. I believe references such as [2-4] would be more relevant.

### Questions
1. In the forward model shift experiment on color image deblurring, what happens if one takes $\sigma > 3$, and taking to the extreme, when one uses a uniform blur kernel?

2. For image deblurring, what happens when you have an anisotropic blur kernel, but you use an isotropic kernel for inference?

3. Two different versions of references are given for [1]

4. It is probably better to cite [2] rather than [3] for score-matching (pg. 2)





**References**

[1] Chung, Hyungjin, et al. "Diffusion posterior sampling for general noisy inverse problems." ICLR 2023.

[2] Vincent, Pascal. "A connection between score matching and denoising autoencoders." Neural computation 23.7 (2011): 1661-1674.

[3] Dhariwal, Prafulla, and Alexander Nichol. "Diffusion models beat gans on image synthesis." NeurIPS 2022

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
