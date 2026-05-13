# Stochastic Gradient Discrete Langevin Dynamics

- Decision: Reject
- Scores: 6, 5, 3

## Abstract
Sampling via Markov chain Monte Carlo can be inefficient when each evaluation of the gradient of energy function depends on a large dataset. In continuous spaces, this challenge has been addressed by extending Langevin samplers with stochastic gradient estimators. However, such an approach cannot be directly applied to discrete spaces, as a naive migration leads to biased estimation with large variance. To fill this gap, we propose a new sampling strategy, \emph{Stochastic Gradient Discrete Langevin Dynamics}, to provide the first practical method for stochastic distribution sampling in discrete spaces. Our approach mitigates the bias of naive ``gradient'' estimators via a novel caching scheme, and reduces the estimation variance by introducing a modified Polyak step size control for simulation time adaptation. We demonstrate significant efficiency improvements across various sampling problems in discrete spaces, including Bayesian learning, stochastic integer programming, and prompt tuning for text-image models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a sampling strategy, Stochastic Gradient Discrete Langevin Dynamics, for a more efficient and accurate MCMC sampling in discrete spaces. This strategy contains a cache method and a modified Polyak step size.

### Strengths
1. The authors identify the problem when sampling in a discrete space.

2. To decrease the bias, they propose a caching technique that expands the batch size with no extra computation cost.

3. To make the algorithm more stable, an adaptive step size method is introduced.

4. Many experiments are done to verify their claims.

### Weaknesses
1. Will the caching technique require a lot of memory? If yes, is there a way to make the cache more memory-efficient?

2. Could you be more precise about how $N_2$ controls the MC error in equations (9) and (10)? Specifically, how does the number of samples $N_2$ relate to the variance of the estimator of the rate matrix, and what assumptions are made about the distribution of these estimators to justify the $O(1/\sqrt{N_2})$ convergence?

### Questions
see weaknesses.

### Soundness
3 good

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
In the paper author propose a way to sample from invariant measure in discrete state space using generaliztion of SGLD to discrete spaces. Authors conduct thorough evaluation and explain how they practically made the approach work with using adaptive step-sizes, clipping and stochastic estimates. Authors also showed asymptocic results on convergence of the approach.

### Strengths
Quite an interesting approach to Monte-Carlo and a way to sample from the invariant measures. Well-detailed experimentations. And good emphasis on biasedness due to Jensen inequality when batches are sampled.

### Weaknesses
1. Main claims of the paper are asympototic, it is generally hard to follow and check whether they are correct. 
2. References to many claims are missing. 
3. Some minor typos in equations (see questions)



### Questions
1. Equation 2. The Wiener process in discrete steps is indexed with timestep and gradient looking into the future, summation over N and this is equation for $x_{t+h}$ depending on $x_{t+nh}$. I honestly can't make sense of it. I assume the authors made some honest typos there as were in a hurry with submission. Can you please explain/fix it as this is standard SGLD (and I assume that this is what authors wanted to write there).

2. Likewise entire section 2 contains a lot of statements with under "mild conditions", "easy to show", "asymptotically" (in what sense). I'd like to see some references and examples what is meant by easy, mild and asymptotic, as for applications that concern Bayesian inference one might be interested in having guarantee of convergence up to p-th moment (which is also my question to the proposed method -- convergence that is asymptotic -- it is just in probability?), while what is easy to show under mild conditions is convergence in probability that is unaplicable to practical setups. Basically, some references are needed here.

3. Appendix Equation 27. Should not there be minus sign before xWx as otherwise density is non-normalizable and henceforth this is not valid distribution?

4. Propositon A.1 seems to be unapplicable to example in Section C.2. Generally, limitations of assumptions and their applicability to the examples is not shown.

5. Out of curiosity, why this is called as SGDLD? This looks more like broader MCMC, whilst Langevin Dynamics is about stochastic differential equations (that are driven by some continious noise), while here it is justified by just showing that under certain conditions Kolmogorov equation gives invariant measure, however, this does look to me just some other form of MCMC rather than LD, as Kolmogorov equations are not about just LD. (nevertheless, this is interesting form of MCMC)

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper under review aim to sample a target distriubtion $\pi$ over a discrete sapce $\mathcal{X}$. To this end, they consider a discrete Langevin dynamics approach from (Sun et al 2023) and (Zanella 2020). This approach consists in sampling a continuous time Markov chain with transition matrix:
$$
R(x,y) = g(\pi(y)/\pi(x)) 1_{N(x)}(y) ,
$$
where $g$ is weight function satisfying $g(a) = ag(1/a)$ and $N(x)$ is a set of neighbors of $x$. 

The main challenge addressed in the paper is that in many practical scenarios, computing $g\left(\frac{\pi(y)}{\pi(x)}\right)$ can be either computationally expensive or intractable. To overcome this issue, the paper proposes a method that adapts the stochastic version of Langevin dynamics (Teh and Welling, 2011) to the discrete setting under consideration.

To achieve this adaptation, they develop a methodology for using biased estimators of the ratio $\pi(y)/\pi(x)$ through cache strategies and a discrete adaptation of the Polyak step size from optimization.

### Strengths
- The paper proposes interesting alternatives to the discrete Langevin dynamics from (Sun et al 2023) to address the problem of intractable target density ratio.
- The experiments demonstrate that the methodology is highly efficient and outperforms its competitors.

### Weaknesses
 - The writing is quite poor; although the methodology is intuitive, I am still unclear about the sampling procedure implemented by the authors (please refer to my comments).
- It would have been interesting to see the proposed methodology compared to other existing approaches on simpler examples. Currently, I have some reservations about the experiments, as the results seem almost too good to be true. Toy examples would be valuable in understanding the limitations and biases introduced by the methods compared to exact MCMC algorithms, providing insight into the various approximations made by the authors in their methodology.
- I suggest that the authors provide more details on what they mean by sampling from $I+\epsilon R$. It's not clear to me what the precise procedure they use.
- Similarly, I didn't understand how the Polyak step size procedure is implemented and why Equation (15) is valid.
- If I'm not mistaken, even if you sample exactly from DLD, the continuous Markov process doesn't exactly have the target distribution as the invariant distribution. Am I right? If so, this point should be highlighted.
- The statement of Proposition 4.1 lacks precision. I didn't understand what the authors mean by "when the step size ϵ decreases to 0, the sampling process associated with the jump rate from Equation 12 is asymptotically unbiased."

### Questions
- I suggest that the authors provide more details on what they mean by sampling from $I+\epsilon R$. It's not clear to me what the precise procedure they use.
- Similarly, I didn't understand how the Polyak step size procedure is implemented and why Equation (15) is valid.
- If I'm not mistaken, even if you sample exactly from DLD, the continuous Markov process doesn't exactly have the target distribution as the invariant distribution. Am I right? If so, this point should be highlighted.
- The statement of Proposition 4.1 lacks precision. I didn't understand what the authors mean by "when the step size ϵ decreases to 0, the sampling process associated with the jump rate from Equation 12 is asymptotically unbiased."

In conclusion, while I believe the paper presents very interesting ideas, it's not ready for publication in its current state. The presentation appears more like a draft than a properly prepared submission.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair
