# Theory on Score-Mismatched Diffusion Models and Zero-Shot Conditional Samplers

- Decision: Accept
- Scores: 6, 6, 6, 8, 6

## Abstract
The denoising diffusion model has recently emerged as a powerful generative technique, capable of transforming noise into meaningful data. While theoretical convergence guarantees for diffusion models are well established when the target distribution aligns with the training distribution, practical scenarios often present mismatches. One common case is in zero-shot conditional diffusion sampling, where the target conditional distribution is different from the (unconditional) training distribution. These score-mismatched diffusion models remain largely unexplored from a theoretical perspective. In this paper, we present the first performance guarantee with explicit dimensional dependencies for general score-mismatched diffusion samplers, focusing on target distributions with finite second moments. We show that score mismatches result in an asymptotic distributional bias between the target and sampling distributions, proportional to the accumulated mismatch between the target and training distributions. This result can be directly applied to zero-shot conditional samplers for any conditional model, irrespective of measurement noise. Interestingly, the derived convergence upper bound offers useful guidance for designing a novel bias-optimal zero-shot sampler in linear conditional models that minimizes the asymptotic bias. For such bias-optimal samplers, we further establish convergence guarantees with explicit dependencies on dimension and conditioning, applied to several interesting target distributions, including those with bounded support and Gaussian mixtures. Our findings are supported by numerical studies.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies the convergence guarantees of zero-shot conditional diffusion models under certain regularity assumptions on the target distributions and assuming small score estimation errors. The authors provide distribution estimation error bounds in KL divergence for score-mismatched DDPM and establish convergence rates under several settings. They also introduce a new zero-shot conditional sampler designed to accelerate the convergence rates by reducing the asymptotic distributional bias in the obtained bounds.

### Strengths
S1. The paper is well-organized and easy to follow.

S2. The convergence results for zero-shot conditional diffusion models are new and address an area that remains largely unexplored in the literature.

S3. The authors propose a new zero-shot conditional sampler that accelerates the convergence rates of the zero-shot conditional DDPM sampler by reducing the asymptotic distributional bias in the obtained bounds.

### Weaknesses
My main concern revolves around Assumption 3, which appears to be relatively strong and may limit the applicability of the results. Specifically:

C1. **Smoothness Requirements:** The assumption requires the existence and control of higher-order derivatives of the log densities. Distributions that are not sufficiently smooth (e.g., those with discontinuities or singularities) may not satisfy this assumption.

C2. **Scaling with $(1−\alpha_t)^m$:** When $\alpha_t$ approaches 1, the factor $(1-\alpha_t)^m$  becomes very small. If the expectations do not decrease at the same rate, the assumption may not hold. This can occur in practice when $\alpha_t$ is close to 1, as in the noise schedule Equation (8) in the paper.

C3. **High Dimensionality Issues:** In high-dimensional settings (large $d$), the behavior of the derivatives can be more complex. The curse of dimensionality may make the assumption unrealistic because the number of derivatives grows exponentially with $d$.

C4. **Applicability to other distributions**: The assumption may not be valid for distributions outside certain classes, such as those with multimodal densities where modes are not well-separated, or distributions with skewness and kurtosis that affect the derivatives.

Additional concerns include:

C5. **Avoiding overstatements of contributions:** In Section 1.1, the paper claims to provide convergence bounds for general target distributions with finite second moments (e.g., Line 92-93). However, their analysis requires regular high-order derivatives for the score functions, which significantly restricts their results to smooth distributions. Adjusting the claim accordingly would provide a more accurate representation of the scope of the contributions.

C6. **Insufficient Discussion on the obtained bounds:** The paper lacks sufficient discussions on the practical implications of the bounds. For example, how do the obtained bounds compare to conventional conditional sampling methods, such as Langevin dynamics? How can the bounds explain the success of conditional diffusion models over other sampling methods?

C7. **Clarification on early stopping in Theorem 2:** The bound in Theorem 2 is given in terms of the KL divergence between the target and learned distribution at time step 1 rather than at time step 0, implying that early stopping has been imposed. Clarification on this point would be helpful.

### Questions
Q1. How does Assumption 3 relate to the standard smoothness and regularity conditions typically required for Langevin dynamics sampling, such as Lipschitz continuity and bounds on the gradient and Hessian of the log-density?

Q2. Considering high-dimensional data, how does Assumption 3 ensure that the expectations involving higher-order derivatives remain well-controlled?

Q3. Are there any connections between Assumption 3 and functional inequalities like log-Sobolev or Poincaré inequalities?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper derives KL convergence bounds for diffusion models when the model is not trained on the target distribution but on a mismatched one. Under some assumptions, the authors exhibit a bound with a term depending on the mismatch. Building on this result, the authors propose an algorithm for conditional sampling that minimizes the mismatch term.

### Strengths
This paper participates in the effort to provide theoretical characterizations of guidance and conditional sampling in diffusion models, an area which has not yet been well explored.

### Weaknesses
1. Assumption 2 is not realistic: Assumption 2 measures how much the approximated conditional expectation deviates from the true $\mu_t$. The expectation in assumption 2 is taken with respect to $\tilde{Q}$ the target distribution, which is unknown during training. Assumption 2 can thus not be guaranteed to hold. Moreover, the authors state mistakenly, as far as I understand, that Assumption 5 is the same as Assumption 4 when is taken under different distributions. Assumption 5, under $Q_t$, is a classic assumption and, as it relates closely to the training loss, is a realistic assumption. Assumption 4 on the other hand needs more justification.
2. A minor modification of prior work with assumptions to control the additional terms: Theorem 1 is obtained through modification Liang et al 2024 by assuming the target distribution is different from the training one. The simple additional terms that appear due to the modification are controlled using a series of assumptions. This limits the technical novelty over Liang et al 2024.
3. The paper is not easy to read. This can be fixed by reducing the large number of inline equations (paragraphs line 513-523 or paragraph A in the appendix). Unnecessary factors $(1-\alpha_t)$ appear on both sides of an equation in crucial assumptions 3 and 4 which I found to be confusing.

### Questions
What does the final line in theorem 2 signify: "Here $W_2(\tilde{Q}_1, \tilde{Q}_0) < \delta d$"?  Is it an assumption or a result of the theorem ? It is unclear from the proof as well.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper mainly focuses on the convergence analysis of zero-shot samplers when training scores are based on the unconditional distribution while inference samples for a conditional distribution. Under these conditions, the inference required scores vary from the predicted one, which is considered as the score-mismatched diffusion.
Although various practical works have appeared, from a theoretical perspective, this is the first work to analyze the inference convergence under score-mismatched settings. The core step of this paper is to recognize and minimize (Theorem 3) the mismatch scores (Eq.(7)) by considering the conditional reverse process (Eq.(5)). The conditional reverse process is deduced by a known connection (e.g., linear connection) between the random variables and the conditions (Eq.(4)).

### Strengths
1. The problem setting considered in this paper is interesting, especially regarding the effectiveness of the zero-shot sampler in the score-mismatched diffusion.
2. Authors denote the gap between ground truth and generated samples lies in the accumulative mismatch between the target and training distributions. This qualitative result is useful and aligns with their sampler design.

### Weaknesses
1. I am a bit afraid that this paper overclaims the problem settings it actually solved. Specifically, this paper claims to consider a general score-mismatched setting. Although it provides a convergence analysis (Theorem 1) for such a setting, the assumption, e.g., (Assumption 4) required, is highly artificial. Besides, it can hardly find an algorithm to achieve Theorem 1, since authors do not provide any approximation for $\grad \ln \tilde{q}_t(x_t)$ under a general score-mismatched setting ($y=h(x_0)$). Instead, I think this paper more focused on the linear setting, i.e., $y=Hx_0+n$ (Eq.(4))
2. I am curious about whether the problem setting is really useful beyond the super-resolution problem. Since the conditioning (y) is usually correlated with the random variable (x) implicitly. I suggest authors provide more examples of utilizing zero-shot samplers to solve score-mismatch diffusions.
3. The establishment of Assumption 4 requires strict assumptions. It not only constrains the unconditional distribution $Q_0$ but also constrains the $H=[I_p, 0]$. I hope the authors can demonstrate whether the results can extend to a general $H$ and how.
4. The final KL divergence bound between ground truth and generated samples is unsatisfactory. Although it is an upper bound, it contains a factor O(d). Such a result will make me concern whether a zero-shot sampler is really effective for mismatch-score settings.

### Questions
1. Theorem 4 is somewhat confusing. Specifically, it claims the establishment of Theorem 2 under the specific choice of $f_{t,y}$, while Theorem 2 has additional assumptions for $\E[\|\Delta_t(X_t)\|]$. The problem is whether the upper bound of the mismatch-score, i.e., $\E[\|\Delta_t(X_t)\|]$, is required for Theorem 4 when the conditional target distribution is general.
2. The BO-DDNM is too dependent on the linear structure of $y=Hx+n$. Considering a general mismatch-score setting, i.e., $y=h(x_0)$. How can we adapt BO-DDNM to the general case except for a Taylor extension?

I am willing to raise my score if the authors solve my concerns.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This work provides the first guarantees for conditional sampling (within the inverse problems setting) via diffusion models, which approximate the guidance term via techniques that do not require additional supervision (e.g., x,y pairs such as in CG and CFG), which the authors coin zero-shot as they do not require to observe any additional data to fine-tune. 

The authors then provide a preconditioned linear-approximation-based approach to their proposed decomposition of the posterior score, which minimises the mismatch; the proposed estimator is very cheap and could be useful to the community. Furthermore, the authors provide a very modest numerical benchmark showing significant improvements to denoising diffusion null space models. In general, the strategy/sketch used in Theorem 3 can be of great use as a template to practitioners looking to derive quick yet accurate estimators.

### Strengths
1. The paper is clear and well written
2. The short summary sketches of the proofs allow us to for a high-level verification in the soundness of the results
3. The work is novel and clearly relevant to the community; with some small modifications and clarifications, this work can be impactful.

### Weaknesses
1. The reviewer found the presentation of the paper a bit confusing. Calling methodologies such as reconstruction guidance (Chung 2023 in the paper) zero-shot (whilst potentially accurate) can be confusing and misleading for the following reasons: 


      *  Whilst many of these methodologies do not require additional supervision (e.g. observing x,y pairs such as in CFG or classifier guidance) they do often still approximate the same quantity e.g. the h-transform / guidance term [1], ultimately with the goal of approximating the posterior score.

     *  Many of these zero shot approximations induce costs that are comparable to training when one considers (see wallclock times in [1]) , furthermore with methods like DPS / reconstruction guidance we can see that they are effectively fine-tuning/minimising a reconstruction loss across timesteps, whilst there's no extra data (thus arguably zero shot) , there is certainly a significant extra cost arising from this "online-finetuning". 

In short, I think the paper would improve its reach/impact if it revised its presentation of what it considers to be zero-shot, or make it much more precise from earlier in the manuscript. 


2. Assumption 4 seems quite strong and rather non-practical for some of these zero-shot methodologies, which make Gaussian approximations on the reverse process and thus do not induce a mismatch that can be controlled. 


[1] Denker, A., Vargas, F., Padhy, S., Didi, K., Mathis, S., Dutordoir, V., Barbano, R., Mathieu, E., Komorowska, U.J. and Lio, P., 2024. DEFT: Efficient Finetuning of Conditional Diffusion Models by Learning the Generalised $ h $-transform. arXiv preprint arXiv:2406.01781.

### Questions
1. I am slightly confused by theorem 2 following from theorem 1 (more specifically, Corollary 1 following from theorem 1).  Theorem 2 bounds the KL between Q_1 (the marginal distribution of the zero-shot sampler at time 1) and P_1 (e.g. the time 1 marginal of the VP-SDE at time 1 where P_0 is the conditional distribution). Typically for all practical purposes in diffusion models Q_1 is simply a Gaussian and this bound can be obtained from exploring the ergodicity of the OU-process and prior work on the convergence of diffusion models. So two questions 

     * Why is this bound for a general Q_1 relevant? We typically fix/choose Q_1 , so Im a bit confused about what specific aspect of the zero-shot diffusion models considered in this work induces/requires a particular Q_1 which needs to be analysed 
     * How does corollary 1 follow from theorem 2 , do you simply just preform the same analysis in reverse time ?  (e.g. flip the time indices) more detail here would be useful 

2. How realistic is assumption 4 for zero-shot models such as Chung 2022a-b, Chung 2023 where the score mismatch cant really be controlled as it makes rather unrealistic Gaussian approximations of the transition density in the backwards process.  Assumption 4 is a rather specific bound on the mismatch it seems its form is required to make everything else work so discussion on its relevance outside of a Gaussian setting for the prior (data distribution) would be extremely helpful.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper provides a non-asymptotic convergence theory for diffusion models with a mismatched score function. The results can be applied to zero-shot conditional samplers, especially linear conditional models. The authors also propose the Bias-Optimal (BO) DDNM sampler and provide a comparison with the previous algorithms.

### Strengths
- The convergence bound of DDPM under score mismatch applies to a variety of target distributions without restrictive assumptions. 
- A bias-optimal zero-shot sampler is proposed, and its convergence rate is analyzed.

### Weaknesses
- Assumption 2 requires an upper bound on the score estimation error $\epsilon^2 = \tilde{\mathcal{O}}(T^{-2})$, which could be restrictive compared to the previous literature (e.g., Li et al. 2024b) which applies to any $\epsilon$. 
- The in-line equations in Section 2.1 and Section 5 are hard to follow. I suggest the authors re-organize the equations for better readability, especially by highlighting the definitions and differences of $q$, $p$, and $\hat{p}$.

### Questions
- The big-O notation in this work is confusing. To name a few, in Assumptions 3 and 4, should $(1-\alpha_t)^m \mathbb{E}[\cdot] = O((1-\alpha_t)^m)$ be equivalent to $\mathbb{E}[\cdot] = O(1)$? Or do the hidden constants in these assumptions implicitly depend on $(1-\alpha_t)^m$? In Definition 1, the noise schedule needs to satisfy $\bar{\alpha}\_T = o (1/T)$ which is defined as an asymptotic bound $\lim\sup_{T\to\infty} |\bar{\alpha}_T / (1/T)| \to 0$, while Theorem 1 presents a non-asymptotic analysis. How does the asymptotic assumption apply to the non-asymptotic analysis? I suggest the authors clarify the notations or even explicitly write the constants' dependency on the hyperparameters if possible. 
- Does $1-\alpha_1=\delta$ in equation (8) contradict with $1-\alpha_1 \lesssim \frac{\log T}{T}$ in Definition 1? What can we obtain from Theorem 1 if $\alpha_t$ is chosen as (8)?

### Soundness
2

### Presentation
2

### Contribution
3
