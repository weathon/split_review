# Generalizing Stochastic Smoothing for Differentiation and Gradient Estimation

- Decision: Reject
- Avg Score: 5.00
- Scores: 3, 8, 3, 6

## Abstract
We deal with the problem of gradient estimation for stochastic differentiable relaxations of algorithms, operators, simulators, and other non-differentiable functions.
Stochastic smoothing conventionally perturbs the input of a non-differentiable function with a differentiable density distribution with full support, smoothing it and enabling gradient estimation.
Our theory starts at first principles to derive stochastic smoothing with reduced assumptions, without requiring a differentiable density nor full support, and we present a general framework for relaxation and gradient estimation of non-differentiable black-box functions $f:\mathbb{R}^n\to\mathbb{R}^m$.
We develop variance reduction for gradient estimation from 3 orthogonal perspectives.
Empirically, we benchmark 6 distributions and up to 24 variance reduction strategies for differentiable sorting and ranking, differentiable shortest-paths on graphs, differentiable rendering for pose estimation, as well as differentiable cryo-ET simulations.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This work presents methods for stochastic smoothing of non-differentiable functions, motivated by applications where there is the need to optimize non-differentiable functions. Some experiments are provided.

### Strengths
.

### Weaknesses
The novelty is insufficient. The idea of smoothing using Gaussian perturbations is a well-established technique in 0-th order optimization or non-smooth optimization. The authors present further general smoothing conditions, requiring that the density function be absolutely continuous, but these derivations are mostly standard exercises in mathematical analysis. Specifically, the core results concerning the differentiability of the smoothed function and the convergence of its gradient appear to be directly derivable from standard results in mollifier theory and the properties of absolutely continuous functions. The variance reduction techniques are also not novel. While the authors mention some techniques, a more thorough investigation into existing literature on quasi-Monte Carlo methods and their application to gradient estimation would reveal that similar approaches have been explored. Overall, my view is that there is very little theoretical novelty.

The authors provide applications and experiments, but I do not think they are strong enough to warrant publication on the basis of the experiments. The experiments, while diverse, do not convincingly demonstrate a significant advantage of the proposed methods over existing techniques in the respective application domains. The lack of comparison to more established baselines in each of these domains further weakens the impact of the experimental results.

### Questions
.

### Soundness
4

### Presentation
4

### Contribution
1

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents improved results on gradient estimation by stochastic smoothing. In particular, the density function is assumed to be absolutely continuous as opposed to being differentiable. The authors discuss three ways to reduce variance of the estimated gradients. Finally, the paper presents application of this smoothing on various problem where gradients of non-differentiable functions are required.

This paper builds on existing ideas, but it does present some strong and comprehensive results that are both insightful.

### Strengths
The paper is very well written, with ideas clearly conveyed. Mathematical descriptions are precise.

I like the fact that multiple density functions are considered and discussed.

The discussion on variance reduction is insightful.

Many different applications are presented. And at the end, some recommendations are made about the "optimal" densities, as well as on the sampling methods.

### Weaknesses
None.

### Questions
Can this method be applied to problems where the $ L^1 $ loss is minimized?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors study stochastic gradients, with applications in stochastic smoothing and variance reduction of gradient estimation. 

I recommend rejection of this paper because I feel there is a lack of novelty and impact for machine learning.

I present a more detailed summary of the paper along with my criticisms under the weakness section.

### Strengths
The experiments in Section 4 seem quite interesting, particularly the use of smoothing for relaxing discrete functions to continuous functions.

### Weaknesses
The goals of the paper are somewhat diverse, so I will go over each result and state my criticisms.

1. In Lemma 3, the authors present a result for smoothing an objective $f$ using a distribution $\mu$ that is possibly non-differentiable. However, the non-differentiable set for $\mu$ is assumed to be $0$-measure. In any learning application I can think of, there seems to be no meaningful difference between "differentiable" and "almost everywhere differentiable". For instance, one can always convolve $\mu$ with a tiny Gaussian, of variance less than machine precision, and immediately get a differentiable density, while not affecting the outcome in any meaningful way. There are also no quantitative analysis which indicate that choosing a non-differentiable $\mu$ would offer any advantages. Specifically, the authors should clarify whether they are referring to differentiability or absolute continuity, and they should provide a concrete example demonstrating the practical implications of this distinction in a machine learning context.
2. Theorem 7 discusses smoothing with an additional rescaling matrix involved. The result appears unsurprising, and the proof appears to use just calculus. I think the authors want to apply this to finding a optimal rescaling matrix $\mathbf{L}$, but the consequences of Theorem 7 are never discussed. The proof of Theorem 7, spanning from equation (36) to (61), involves a series of relatively straightforward steps. These include change-of-variable formula for volume (36)-(37), interchanging derivative with integral (38)-(39), matrix chain rule (40), change-of-variable for volume (41), basic algebra manipulation (42)-(43), a repetition of similar tools with different order (44)-(49), matrix chain rule (50)-(52), plugging the formula for gradient of determinant (53), and basic algebra (54)-(61). Given the fundamental nature of these operations, the proof lacks novelty and could likely be derived independently by most readers familiar with basic calculus and linear algebra.
3. The authors discuss numerous variance reduction techniques in Section 2.1, but there is no attempt at any quantitative and theoretical comparison of these approaches. The authors did include some simple synthetic experiments, but it is questionable how well the observations will generalize to realistic scenarios. Specifically, what is the authors' contribution to variance reduction in this context? Have they developed novel techniques, or are they simply applying existing methods? A more rigorous comparison, potentially including theoretical bounds or guarantees, would strengthen this section.
4. In Section 2.3, the authors discuss smoothing of the algorithm vs the objective. I am not convinced by the setup of $\ell(h(y))$ where $\ell$ is the loss, $h$ is an algorithm, and $y$ is the model output. I suggest that the authors clarify that this setup is motivated by "algorithmic supervision."
5. In Section 4, the authors present a series of experiments that compare the effectiveness of different distributions and different variance reduction techniques. I am not sure how well the conclusions here generalize. The authors should address the generalizability of their experimental findings, particularly regarding the choice of distributions and variance reduction techniques across different problem domains.

### Questions
1. Can the authors comment on how their theoretical or experimental results might be applicable for discrete-to-continuous relaxations? Particularly, how would quantities such as lipschitz smoothness, convexity, or general ease of optimization be affected by different choices of distributions?

2. Can the authors comment on the run-time of their algorithms compared to the baselines in Section 4?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The work addresses gradient estimation for stochastic differentiable relaxations of non-differentiable functions. The developed theory does not require a differentiable density or full support as it was in prior works.

### Strengths
The work contains rigorous theorem statements and proofs. The work contains extensive empirical results.

### Weaknesses
The work considers the problem of estimating the gradient of the relaxation of the algorithm or of the loss function. In Section 2.3 the authors formalize the algorithm smoothing and the objective smoothing. It seems that the paper does not provide the theoretical convergence analysis of the backbone stochastic optimization algorithms, but only introduces the techniques of smoothing and variance reduction and then tests the theoretical findings in practice.

The paper's focus on gradient estimation for smoothed functions, while rigorously treated, lacks a clear demonstration of its advantage over existing methods, particularly in the context of optimization algorithm convergence. The empirical results, while extensive, do not fully address this gap. The theoretical analysis primarily focuses on the properties of the gradient estimator itself, rather than the performance of optimization algorithms when using these estimators. Furthermore, the paper does not adequately address the potential bias introduced by smoothing, especially in relation to the original non-differentiable function. While the authors mention that the original function's gradient is often zero or undefined, the practical implications of this bias on optimization convergence are not explored in depth. The comparison to AlgoVision [5] is brief and does not fully clarify the advantages of the proposed approach.

### Questions
Is it possible to demonstrate the advantage of your smoothing approach over the previous works in theory, not only in practice, in some way? For instance, by incorporating the proposed gradient estimator into the SGD or Adam optimizer and providing a better convergence result? 

There exist many general variance reduction techniques in the field of optimization (in such algorithms as SVRG, L-SVRG, Page, SAGA, Variance Reduced Adam, SPIDER etc.). Do the proposed variance reduction techniques generalize the techniques from the optimization field or orthogonal to them? Can they be combined together?

Smoothing should introduce some bias to the estimator. There are some works on the analysis of SGD with biased estimators [1, 2]. They both consider smoothing techniques. Does the proposed smoothing technique fit into the frameworks of assumptions in these papers?

[1] Ahmad Ajalloeian, Sebastian U. Stich, On the Convergence of SGD with Biased Gradients
[2] Yury Demidovich, Grigory Malinovsky, Igor Sokolov, Peter Richtárik, A Guide Through the Zoo of Biased SGD

### Soundness
3

### Presentation
4

### Contribution
3
