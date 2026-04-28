# Accelerated Convergence of Stochastic Heavy Ball Method under Anisotropic Gradient Noise

- Decision: Accept
- Avg Score: 6.25
- Scores: 5, 6, 6, 8

## Abstract
Heavy-ball momentum with decaying learning rates is widely used with SGD for optimizing deep learning models. In contrast to its empirical popularity, the understanding of its theoretical property is still quite limited, especially under the standard anisotropic gradient noise condition for quadratic regression problems. Although it is widely conjectured that heavy-ball momentum method can provide accelerated convergence and should work well in large batch settings, there is no rigorous theoretical analysis. In this paper, we fill this theoretical gap by establishing a non-asymptotic convergence bound for stochastic heavy-ball methods with step decay scheduler on quadratic objectives, under the anisotropic gradient noise condition. As a direct implication, we show that heavy-ball momentum can provide $\tilde{\mathcal{O}}(\sqrt{\kappa})$ accelerated convergence of the bias term of SGD while still achieving near-optimal convergence rate with respect to the stochastic variance term. The combined effect implies an overall convergence rate within log factors from the statistical minimax rate. This means SGD with heavy-ball momentum is useful in the large-batch settings such as distributed machine learning or federated learning, where a smaller number of iterations can significantly reduce the number of communication rounds, leading to acceleration in practice.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper analyzes the performance of SGD and SHB (Stochastic Heavy Ball) in stochastic optimization with a quadratic objective. A lower bound of the convergence rate of SGD is given, which argued to be strictly worse than the upper bound of convergence rate of SHB also proved in the paper. More precisely, SGD is shown to take at least $O(\kappa)$ iterations to converge, while SHB requires only $\tilde{O}(\sqrt{\kappa})$ iterations with proper learning rate schedule.

### Strengths
The contrast between SGD and SHB does seem plausible. I checked the proof briefly and found no obvious mistakes.

### Weaknesses
1. The upper bound of SHB seems very similar (and worse by a logarithmic factor) than the quadratic setting in [Can et al. (2019)](https://arxiv.org/pdf/1901.07445.pdf). I would suggest adding a detailed comparison. Also the convergence rate is sublinear, which is not very satisfactory.
2. The batch size is required to be of order $\Omega(1/\epsilon)$, which does not seem realistic, as $\epsilon$ is usually exponentially small.

### Questions
My foremost concern is the comparison with previous literature, which I discussed in the `Weaknesses` part.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This study presents an analysis of the convergence properties of the stochastic HB method when applied to quadratic objective functions. Specifically, when we make an assumption about the presence of anisotropic noise, it demonstrates that the stochastic HB method exhibits a significantly faster rate of convergence. Earlier research has already established that this anisotropic noise model can manifest in neural networks when their parameters are in proximity to the optimal values.

### Strengths
This paper for the first time shows that in the anistorpic setting for the quadratic objective function, the stochastic HB method can achieve accelerated rate. This is a novel contribution.

### Weaknesses
The paper should delve further into the circumstances under which the anisotropic setting is applicable to machine learning models. While the authors mention that this model can appear when parameters are near optimal values, a more detailed discussion is needed. Specifically, what properties of the loss landscape or the optimization process lead to this anisotropic noise? Are there specific architectures or datasets where this is more likely to occur? The content of Theorem 1 may seem redundant as its proof is not contingent on stochasticity; it essentially establishes a lower bound for gradient descent (GD), a well-known result. Therefore, its inclusion in the paper is somewhat unclear. It would be more appropriate to allocate space to discuss the technical innovations of the main theorem's proof within the main body of the paper. The current presentation does not adequately highlight the novel aspects of the proof technique. Additionally, there are several typographical errors in the proofs, including indexing, which should be rectified. These errors, while seemingly minor, can hinder the reader's understanding and the overall credibility of the work.

### Questions
In the paper you mentioned that this rate achieved for the objective in the large enough batch regime. However the acceleration is oblivion to the mini-batch size. So I was wondering why you emphasise on this in the paper.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper investigates effect of Polyak-type momentum in SGD with large batch size. The authors show that momentum, combined with a stage-wise geometric decay stepsize schedule, improves the linear convergence part of SGD. Although the analysis is done on convex quadratic functions, it takes a step towards better understanding of SGD with momentum.

### Strengths
The paper is well-written and easy to follow. The motivation and main results are clearly presented, with enough intuition given after each result. The technical results seem solid and are supported by empirical evidence.

### Weaknesses
There is still a gap between real-life SGD applications and the analysis. Most SGD applications are for nonconvex (even nonsmooth) problems, where Hessian may even not exist and the notion of condition number is uncommon.

Assumption 3 seems to suggest "noise is small in the coordinates that result in ill-conditioning". It is unclear how this assumption can be extended to more commonly used assumptions such as bounded variance, which is a significant limitation. The paper does not adequately address the practical implications of this restrictive assumption.

In the first experiment, it appears that SGD performs worse when $M$ gets large. The range of the grid search for $\eta_t$ seems to be invariant for all batch sizes. It is unclear whether SGD would perform better with a step size scaled by $\sqrt{M}$.

Nonconvex models are used in the second experiment. While the authors claim that the strongly convex quadratic optimization model approximates the landscape near a local optimum, Figure 1 suggests that the benefits of momentum are significant at the beginning of the training procedure, which is not fully explained. The connection between the theoretical analysis and the empirical results in the nonconvex setting is weak.

Some recent researches show that even without decay of learning rate [1], momentum SGD also outperforms SGD using large batch size. The paper does not discuss this phenomenon and its implications for the analysis.

I would suggest the authors remove (or delay to the end of the appendix) proofs for auxiliary results, most of which are well-known results. Some notations should be properly defined (such as $\mathbf{X} \succeq \mathbf{Y}$ and Hessian norm $\|\cdot\|\|_{\mathbf{H}}$)

**Minor typos and stylistic issues**

1. Algorithm 1. Line 6

   $m$ => $M$

2. Experiment

   initialize $\mathbf{w}^0$ from $(-1,1) \Rightarrow (-1,1)^d$.

3. Proof of Lemma 3

   $\succ$ should be $\succeq$

4. Page 29

   genarality => generality

### Questions
1. Assumption 3 seems to suggest "noise is small in the coordinates that result in ill-conditioning". What do you think is the difficulty in extending it to commonly used assumptions (e.g., bounded variance)?
2. In your first experiment, It seems that SGD performs worse when $M$ gets large. To me it feels that it is because your range of grid search for $\eta_t$ is invariant for all batchsizes. I'm curious whether SGD performs better when you multiply the stepsize by $\sqrt{M}$.
3. Nonconvex models are actually used in the second experiment. Although the authors claim that the strongly convex quadratic optimization model approximates the landscape near local optimum, Figure 1 actually suggests that benefits of momentum are significant at the beginning of the training procedure. Could you elaborate more on this?
4. Some recent researches show that even without decay of learning rate [1], momentum SGD also outperforms SGD using large batch size. What do you think might contribute to this phenomenon?
5. I would suggest the authors remove (or delay to the end of the appendix) proofs for auxiliary results, most of which are well-known results. Some notations should be properly defined (such as $\mathbf{X} \succeq \mathbf{Y}$ and Hessian norm $\\|\cdot\\|_\mathbf{H}$)

**Minor typos and stylistic issues**

1. Algorithm 1. Line 6

   $m$ => $M$

2. Experiment

   initialize $\mathbf{w}^0$ from $(-1,1) \Rightarrow (-1,1)^d$.

3. Proof of Lemma 3 

   $\succ$ should be $\succeq$

4. Page 29

   genarality => generality

**References**

[1] Wang, R., Malladi, S., Wang, T., Lyu, K., & Li, Z. (2023). The marginal value of momentum for small learning rate sgd. *arXiv preprint arXiv:2307.15196*.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Motivated by empirical successes of stochastic heavy ball (SHB) method and the prevalence of the anisotropic gradient noise in training neural networks, the paper presented last iterate convergence rate for the SHB method on quadratic objectives under the anisotropic gradient noise assumption. The results implies SHB with polynomially decaying learning rate provides $\tilde{O}(\sqrt{\kappa})$ acceleration rate with respect to stochastic gradient descent (SGD) when batch size is large, where $\kappa$ denotes the conditional number.

### Strengths
The paper is well-written, and proofs are neat and easy to follow. 

The paper formally established a lower bound for SGD tailored for the scope of investigation, which served as a concrete comparison benchmark for SHB method.

The paper presents novel theoretical results of SHB for quadratic loss. The result implies $\tilde{O}(\sqrt{\kappa})$ acceleration in comparison to SGD when batch size is big. The results is also nearly optimal in comparison to heavy ball method in deterministic setting. 

The experiment results matches with the theoretical bound: acceleration guarantee with large batch size. The advantage of SHB with large batch size is also well-motivated in practice. 

The analysis follows the classical bias variance decomposition paradigm. The novelty is to quantifying bias and variance with some linear operator, and then analyze the property of those linear operators.

Although the scope of theoretical investigation is limited at quadratic loss with anisotropic gradient noise, the author justified the broad implication of such assumptions to real applications.

### Weaknesses
Potential minor typos:

pg5: eqn 3.11: missing - sign before $\beta$. (Same typo appears at pg 21 under the proof of Lemma 13 at two places)

pg6: Algorithm 1 line 6, batch size $M$ instead of $m$ being consistent 

pg27: the equality applies (C.18) and (C.21): the last row of the matrix $2d$.

Everything is rigorous, but the notation might be a bit overly complicated for what was actually being used in order to establish Theorem 2. For example: number of stages $n_{\ell}$, the stage lengths $\set{ k_1, \cdots,  k_{n_{\ell}} }$. Theorem 2 actually set all stages the same length, and each stage has the same learning rate.

### Questions
No

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
