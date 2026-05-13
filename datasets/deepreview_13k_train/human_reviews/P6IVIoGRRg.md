# Provable Benefit of Annealed Langevin Monte Carlo for Non-log-concave Sampling

- Decision: Accept
- Scores: 6, 8, 6, 8

## Abstract
We address the outstanding problem of sampling from an unnormalized density that may be non-log-concave and multimodal. To enhance the performance of simple Markov chain Monte Carlo (MCMC) methods, techniques of annealing type have been widely used. However, quantitative theoretical guarantees of these techniques are under-explored. This study takes a first step toward providing a non-asymptotic analysis of annealed MCMC. Specifically, we establish, for the first time, an oracle complexity of $\widetilde{O}\left(\frac{d\beta^2{\cal A}^2}{\varepsilon^6}\right)$ for simple annealed Langevin Monte Carlo algorithm to achieve $\varepsilon^2$ accuracy in Kullback-Leibler divergence to the target distribution $\pi\propto{\rm e}^{-V}$ on $\mathbb{R}^d$ with $\beta$-smooth potential $V$. Here, ${\cal A}$ represents the action of a curve of probability measures interpolating the target distribution $\pi$ and a readily sampleable distribution.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper studies the convergence of annealed Langevin algorithms for general, possibly non-log concave, target distributions. The authors propose using an argument based on Girsanov's theorem to bound the distance between a reference process and a Langevin SDE that is based on an annealing schedule of target distributions, bridging the target to a base distribution. The authors also consider a practical implementation of the continuous time SDE, based on the exponential integrator scheme.

### Strengths
The authors consider an interesting problem, which is actively researched. Most of the research has focused on obtaining convergence bounds for standard Langevin algorithms imposing strong assumptions on the target distribution, such as log-concavity or log-Sobolev inequalities. The approach in this paper seems original, since it differs from strategies that are typically used in the literature as explained by the authors. Moreover, it gives convergence bounds in KL for an annealed Langevin algorithm, for which few results are available, and under "weak" conditions. Overall, the paper is clear enough to follow what the authors are doing and has a cohesive story.

### Weaknesses
 - The authors consider a specific annealing schedule and it is not clear if their results give any kind of clarity on how the schedule affects the overall complexity of the algorithm. 

- In several occasions I would have appreciated clearer explanations. For instance, why considering the exponential integrator scheme instead of an Euler scheme? Why considering that specific annealing schedule? It is also not completely clear why one finds the topics in Section 2.4 at a first read. It would be beneficial to convince the reader that these mathematical concepts are needed, also giving an idea of how these are useful in what follows. 

- The sketch of the proof of Theorem 2 is not very clear to me and I find it should be heavily improved. It seems the authors compute the KL between two processes, neither of which is the discretisation scheme. Then the notation in the proof in the appendix seems inconsistent, denoting by \nu^{ALMC} the measure of another process. As I motivate in the Questions section below, I struggle to see how the authors use Lemma 1 in the proof of this result. This should be clarified if the paper is to be considered for acceptance.

- the contribution is in general interesting, but I would have liked to find analyses such as some (simple) numerical simulations showing that the convergence of the algorithm is for instance not exponential in the dimension.

- Table 1 gives an overview of results available in the literature, but these are for various algorithms which are denoted by corresponding  acronyms.  This is not a very clear comparison in my opinion, and it would be nice to have a short explanation at the differences between these algorithms.

- the intuitive explanations in lines 318-323 are rather obvious and are not really clarified by the results in the paper. This should be clear to the reader to avoid confusion.

### Questions
- Theorem 2 uses Lemma 1, that is a consequence of Girsanov's theorem. As far as I understand it uses it to bound the KL between the SDE in Equation (6) with the "true" SDE, that is Equation (4). However, the SDE (6) clearly does not fit into Lemma 1 of the paper, since a term in the drift depends on a past state. The authors should explain their reasoning and not just refer to Lemma 1, which is not general enough.

- in Lemma 2, in what sense do the authors say the equality is "reachable"?

- in lines 373-374 the authors state that the Euler scheme is "non-optimal", without a supporting reasoning. What are their reasons for writing that?

- In Example 1, the authors say that \rho_1 is "readily sampleable". Is it then the case that \rho_0 is a simple distribution that can be sampled? Here the notation is not clear yet. Also, in point 2. of the example, are the LSI and PI constants exponentially dependent on d for the distribution \rho_t for any t? In general, this example could be made clearer.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proves new bounds on efficacy of Annealed Langevin MC by creating an SDE which approximates the target and then analyzing the discretization error introduced by simulating it on a finite machine

### Strengths
Computational bounds are generic- a smoothness constraint for target distribution, rather than isoperimetry assumptions.

Explanations are clear and well-illustrated, suiting a broad generalist audience by mixing intuition-building and commentary.

The direct impact of this paper is unclear, but the methods it introduces are interesting contributions

### Weaknesses
The paper shares the weakness of most such oracle inequalities, which is that they reassure us of convergence of an algorithm under assumptions that are hard to verify on a particular problem

Note that I am not expert in all the components of the authors' proof, and have taken some steps on faith.

### Questions
What does $\beta$-smoothness imply about the target distribution? Can we know this in general, especially where the density arises from a posterior? It seems like this quantity would be hard to calculate for even tractable likelihoods, let alone general posterior densities.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a novel analysis of Annealed LMC which uses a specific scheduling system. The latter allows to benefit from another analysis scheme which uses the action on curves instead of isoperimetric inequalities.

### Strengths
The paper provides a concise analysis with a clever mathematical trick of using the action of the curve instead of the isoperimetry constants. Assuming gradient Lipschitzness of the potential function allows to easily (rejection-acceptance) sample from an initial distribution, which then allows to sample from the target distribution (non-convex, gradient-Lipschitz) using an annealing schedule for LMC.

### Weaknesses
 - Assumption 1 is not well discussed. One cannot verify beforehand whether the curve $\pi_{\theta}$ is AC. How should it be done? See the respective question in the section below.
- Assumption 2 is not the classic smoothness assumption. Instead it is the gradient Lipschitz continuity, which is stronger. This should be explicitly mentioned in the paper.
- The notation is slightly confusing. There are too many indices for $\pi$ and the usage is incoherent. The reading would be rather simplified, if the notation was more developed.  
- Simple experiments on sampling from a mixture of Gaussians using the proposed and existing methods would significantly boost the paper. 
- In the abstract of the paper, the authors claim that their analysis is non-asymptotic, however it is not true. Theorem 2 (main result) and related results are given with $\tilde{O}(\cdot)$. 
### Mathematical comments 

- *The equation after line 1077* in the proof of Example 2 is incorrect. The density of the sum of two independent random variables(vectors) is the convolution of their densities rather than their product. Thus, the variable $X$ is not distributed as $\hat{\pi}_{\lambda}$. This serves as the cornerstone of the remainder of the proof, which means that the proof is incorrect. 
- *The third line in the proof of Example 2* is incorrect. After recentering the Gaussians, the authors erase the terms $\exp(-\frac{2\lambda \beta}{\lambda + \beta})\|y_i\|^2$ with the $\propto$ sign. Since we have different $y_i$'s, the resulting mixture weights will be different from $p_i$. Nevertheless, this could be fixed by replacing $p_i$ by some $q_i$'s. 
- *Paragraph starting at line 364* The authors motivate the use of annealing as the schedules start at a distribution $\pi_0$, which is easy to sample from. The reason for the easy sampling according to the authors is the strong-convexity of the negative log-density $-\log\pi_0(x) = \eta(0)V(x) + \lambda_0\|x\|^2/2$. The latter is true when $\lambda_0$ is large enough.
- *Continuation of the previous point. Line 831* The strong convexity constant $(\lambda_0 - \eta_0 \beta)$ might be negative, unless $\lambda_0$ is chosen to be large. 
- *Beginning of the proof of Theorem 1* $v_t$ is chosen to satisfy the Fokker-Planck equation on line 294. However, later on line 301 it is chosen to minimize the norm $\|v_t\|_{L_2(\tilde{\pi}_t)}$  using Lemma 2. This is possible if $v_t$ also generates $\tilde{\pi}_t$. Is it possible to find such $v_t$? See the relevant question.

#### typos
- *line 956:* cure -> curve

### Questions
- Is the analysis using the action only available for annealing? Can we gain anything by applying this technique to LMC in the standard setting?
- What are the estimates of the action parameter $\mathcal{A}$ for a more general class of distributions than the mixture of Gaussians?
- Is it possible to guarantee that for certain target distributions and schedules Assumption 1 is satisfied? This is important, as it is not easy to manually check for every setting. 
- Is there always a $v_t$ such that $X_t \sim \tilde{\pi}_t$ for all $t$ in (4) and it generates $\tilde{\pi}_t$ i.e. satisfies the Fokker-Planck equation?

### Soundness
2

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
The paper consider the problem of sampling from an unnormalized density that may be non-log-concave and multimodal using annealed MCMC.  The authors present a non-asymptotic analysis of Annealed Langevin Monte Carlo, bypassing the commonly assumed log-concavity constraint in literature. The quantitative bounds derived are widely applicable and either comparable to or better than previous analyses for isoperimetry-free sampling methods.

### Strengths
The paper provides, as far as I know, the first thorough and non-asymptotic analysis of the annealed Langevin Monte Carlo algorithm.  The results obtained advance the understanding and analysis of annealed MCMC, potentially setting the stage for further research in this area. The intuition behind the algorithm and the proofs are well explained.

### Weaknesses
 The discussion on the impact of the annealing schedule on the convergence rate is not sufficiently clear in the paper. How the choice of the annealing schedule influences the derived bounds? Specifically, in the example of mixture of Gaussians,  $\lambda(\theta) \propto (1-\theta)^\gamma$ is used,   how varying $\gamma$ affects the action $\mathcal{A}$? whether there is an optimal value of $\gamma$ that could minimize the convergence rate?

### Questions
Please see the weakness part.

### Soundness
3

### Presentation
3

### Contribution
3
