# Flow matching achieves almost minimax optimal convergence

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Flow matching (FM) has gained significant attention as a simulation-free generative model. Unlike diffusion models, which are based on stochastic differential equations, FM employs a simpler approach by solving an ordinary differential equation with an initial condition from a normal distribution, thus streamlining the sample generation process. This paper discusses the convergence properties of FM for large sample size under the $p$-Wasserstein distance, a measure of distributional discrepancy. We establish that FM can achieve an almost minimax optimal convergence rate for $1 \leq p \leq 2$, presenting the first theoretical evidence that FM can reach convergence rates comparable to those of diffusion models. Our analysis extends existing frameworks by examining a broader class of mean and variance functions for the vector fields and identifies specific conditions necessary to attain almost optimal rates.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper provides estimates for the 2-Wasserstein distance for the sample-based distribution obtained in the Flow-Matching framework relative to the exact distribution. These estimates depend on the number of samples used in training, the smoothness of the true distribution as an element of the Besov space, the asymptote of the growth of the conditional map at the initial time instant.
The paper considers the early stopping mode of the ODE, when the solution stops at time $T_0<1$, and the estimates of $T_0$ are also given.

### Strengths
- The paper is the first to present estimates for the Flow Matching framework, which shows that almost optimal minimax converges rates are achieved under several assumptions.
- The paper is well written

### Weaknesses
This paper contains many points in common with the paper cited therein [1].  In particular, using Besov space for target density, B-splines for its approximation, etc. Many estimates are based on thouse from [1], see, for example, Appendix A.4--A.5 of the presented paper, where the citation on [1] are explicit. In paper [1] diffusion models are considered, but as shown in paper [2], Flow Matching approach includes, under certain conditions, Diffusion models approach. Thus, generalization or obtaining similar results for Flow Matching is rather straightforward. Namely, in essence, the difference is to use Alekseev-Gröbner Theorem (Lemma 16 about error of a perturbed solution of ODE) instead of Girsanov’s Theorem (Proposition D.1 of [1] for error of a perturbed solution of SDE). 
One of the main differences is the presence in the estimates of the degree of growth of the parameter $\sigma_t$ at 1, but the authors come to the well-known (empirical) conclusion that the optimal asymptotics is $\sqrt t$. Does this provide the first theoretical justification for this empirically observed optimal scaling?  How can one intuitively realize that the degree of $\sigma_t$ growth near the time point $t=1$ is important if the ODE solution is considered on the interval $[0, T_0]$, where $T_0<1$?

### Questions
- How do estimates change if you take a distribution other than the Gaussian distribution as the initial distribution $P_{[0]}$?

- Can the obtained estimates be easily extended to the case of estimation error in the total variation (TV) distance?

- Would your estimates change if you use different heuristics for Flow Matching, such as OT-minibatch?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper applies the same framework as in Oko et al. (a paper on convergence rates of diffusion models as timesteps and/or sample size goes to infinity), to Flow Matching. Due to the application to a different model, some of the proofs are different but the results are of the same strength.

### Strengths
It's interesting to know that FM have the same standard guarantees as DMs.

### Weaknesses
Mathematically, the paper does not shine as to novelty, it mostly chains known estimates, and applies them to FM. 
Like in similar papers for other models, some of the setups look like toy models, this may be because the mathematical theory is unavailable in general. In particular, the regularity assumption (A1), requiring the target density to belong to a Besov space, seems particularly strong and its practical relevance is questionable. It is unclear to what extent real-world datasets satisfy such a condition, and the paper does not provide any empirical evidence or citations to support this assumption. The lack of experiments further exacerbates this issue, as there is no way to assess the practical implications of the theoretical results. The paper's analysis relies heavily on the smoothness assumptions, which may not hold in many practical scenarios, thus limiting the applicability of the theoretical findings. The paper does not discuss the limitations of these assumptions in detail, nor does it provide alternative scenarios where these assumptions might be relaxed or modified. The theoretical results, while mathematically sound, may not translate directly into practical improvements or insights for real-world applications of Flow Matching.



### Questions
1) In Theorem 1, what is a good bound for R_0?
2) Still in theorem 1, why do you chose $\sigma_{[\tau]}$ in that form? In what applications does it appear that way?
3) Can you test the sharpness of the bounds of theorem 9 for some FM famous use cases? 

at line 310 "in general we generally consider" may be rephrased

### Soundness
3

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
4

### Summary
This paper provides near-minimax convergence guarantees for the flow matching (FM) algorithm for $p$-Wasserstein distances. Distinct from diffusion models, FM use ordinary differential equations (ODEs) at inference time instead of stochastic differential equations (SDEs). Their estimator is based on time-partitioned estimators, similar to the analysis of Oko et al (2023). They adopt the estimator for more general parameters (specifically the mean and covariance parameters) to provide an estimator for flow matching.

### Strengths
This paper provides (to my understanding) the first estimation rates for flow matching in the context of classical statistical estimation rates. This paper is similar in spirit to the FM paper of Lipman et al (2023), where they use different combinations of mean-variance parameters to define their path. While this work leverages many ideas from Oko et al. (2023), what is especially interesting is this idea that "optimal parameter choices" lead to minimax convergence rates, whereas other choices do not enjoy the same statistical rates.

### Weaknesses
The paper could be more clearly written, and the main text is very technical. This paper would benefit substantially from a small figure explaining the construction of the estimator at a high level, and also explaining the reason why the full minimax estimation is not possible. These are overall minor points, but I do believe the paper would benefit greatly from these modifications overall.

My comments are minor (these are mostly typos I found, but this is far from exhaustive)

1. Line 188 "for probability *density* estimation"?
2. L193 (this might happen in many places): I believe grammatically it makes sense to say "i.id. sample*s*" instead of a single sample
3.  L222: *reverse* not revserve
4. L254: "respectivly" is misspelled
5. This is a question: is there a clean way to track the dependence on the diameter of the set of the support? The assumptions assume the support of the density is in the unit cube. What is the dependence if the radius was arbitrary? This might fall outside the scope of the paper, but I'm curious if the authors have the answer
6. L516: "diffrence" is misspelled

### Questions
My comments are minor (these are mostly typos I found, but this is far from exhaustive)

1. Line 188 "for probability *density* estimation"?
2. L193 (this might happen in many places): I believe grammatically it makes sense to say "i.id. sample*s*" instead of a single sample
3.  L222: *reverse* not revserve
4. L254: "respectivly" is misspelled
5. This is a question: is there a clean way to track the dependence on the diameter of the set of the support? The assumptions assume the support of the density is in the unit cube. What is the dependence if the radius was arbitrary? This might fall outside the scope of the paper, but I'm curious if the authors have the answer
6. L516: "diffrence" is misspelled

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proves an almost minimax optimality result for a class of flow models. Previously, Oko had shown that diffusion models are minimax optimal under the 1-Wasserstein distance. This paper builds on Oko to show that a class of FMs with terminal Gaussian distribution and paths of the form x_t = \sigma_t x_0 + m_t x_1 (which includes diffusion as a special case) are almost minimax optimal, with a parameter kappa determining the non-optimality. They show this under the p-Wasserstein distance for 1 <= p <= 2.

### Strengths
Provides new theoretical results for a family of flow models, showing almost minimax optimality (with 'almost' depending on a specific parameter). The paper is rigorous, clearly written, and clearly places the results in the context of prior work.

### Weaknesses
Please see Questions.

L223: Kappa = 1/2 corresponds to diffusion-FM, correct? So the result actually says that that only diffusion-FM is optimal within the family of FMs you consider? If so, L230 'FM is as strong as diffusion models' seems somewhat misleading -- it seems more like diffusion is actually stronger than FM, except when FM is equivalent to diffusion. Please correct me if I'm wrong; otherwise might want to state this differently.

L225: Can you elaborate on the ways in which your proof technique differs significantly from Oko's? (Since Oko's result is a special case of yours for diffusion-FM and 1-Wasserstein.)

L133: Can anything be said in the more general non-Gaussian case of FMs?

L177: Notation not super clear here. What is P_[1] vs p_[1]?

Theorem 1: It seems like you are further restricting sigma to have the form (1-\tau)^\kappa?

L222: Typo 'revserse'

L224: Diffusion can be expressed as an ODE so I am not sure what you mean here?

### Questions
L223: Kappa = 1/2 corresponds to diffusion-FM, correct? So the result actually says that that only diffusion-FM is optimal within the family of FMs you consider? If so, L230 'FM is as strong as diffusion models' seems somewhat misleading -- it seems more like diffusion is actually stronger than FM, except when FM is equivalent to diffusion. Please correct me if I'm wrong; otherwise might want to state this differently.

L225: Can you elaborate on the ways in which your proof technique differs significantly from Oko's? (Since Oko's result is a special case of yours for diffusion-FM and 1-Wasserstein.)

L133: Can anything be said in the more general non-Gaussian case of FMs?

L177: Notation not super clear here. What is P_[1] vs p_[1]?

Theorem 1: It seems like you are further restricting sigma to have the form (1-\tau)^\kappa?

L222: Typo 'revserse'

L224: Diffusion can be expressed as an ODE so I am not sure what you mean here?

### Soundness
3

### Presentation
3

### Contribution
3
