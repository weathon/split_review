# Accelerating Distributed Stochastic Optimization via Self-Repellent Random Walks

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 8, 6, 8

## Abstract
We study a family of distributed stochastic optimization algorithms where gradients are sampled by a token traversing a network of agents in random-walk fashion. Typically, these random-walks are chosen to be Markov chains that asymptotically sample from a desired target distribution, and play a critical role in the convergence of the optimization iterates. In this paper, we take a novel approach by replacing the standard \textit{linear} Markovian token by one which follows a \textit{non-linear} Markov chain - namely the Self-Repellent Radom Walk (SRRW). Defined for any given `base' Markov chain, the SRRW, parameterized by a positive scalar $\alpha$, is less likely to transition to states that were highly visited in the past, thus the name. In the context of MCMC sampling on a graph, a recent breakthrough in \citet{doshi2023self} shows that the SRRW achieves $O(1/\alpha)$ decrease in the asymptotic variance for sampling. We propose the use of a `generalized' version of the SRRW to drive token algorithms for distributed stochastic optimization in the form of stochastic approximation, termed SA-SRRW. We prove that the optimization iterate errors of the resulting SA-SRRW converge to zero almost surely and prove a central limit theorem, deriving the explicit form of the resulting asymptotic covariance matrix corresponding to iterate errors. This asymptotic covariance is always smaller than that of an algorithm driven by the base Markov chain and decreases at rate $O(1/\alpha^2)$ - the performance benefit of using SRRW thereby \textit{amplified} in the stochastic optimization context. Empirical results support our theoretical findings.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a new distributed stochastic optimization algorithm, where the random walk guiding the sampling of gradients across the network uses Self-Repellent Random Walk (SRRW), a recently introduced family of nonlinear Markov chain. For MCMC sampling on a graph, SRRW has been shown to achieve a $O(1/\alpha)$ decrease in the asymptotic variance [Doshi et al, ICML 2023], where $\alpha$ is a hyperparameter of the chain; roughly speaking, given any base Markov chain, SRRW works by preferring transitions to states that were less visited in the past, and the larger the $\alpha$, the stronger this preference. Building on this insight, the authors in this paper use SRRW as the "token" gradient sampler in a distributed stochastic optimization setting.

### Strengths
The main contributions are as follows. Very interestingly, the authors show that given the "right" step-size setting (i.e. when the step-size for the optimization parameter $\theta_n$, $\beta_n$, is $o(\gamma_n)$, where $\gamma_n$ is the step-size for the update of the weighted empirical distribution $x_n$), the asymptotic variance of the $\theta_n$ (defined as $\frac{\theta_n - \theta^*}{\sqrt{\beta_n}}$) actually decays with the rate $O(1/\alpha^2),$ which is better than the $ O(1/\alpha)$decay rate for the (un)weighted empirical distribution $x_n$ in [Doshi et al., 2013]. An important result the authors show is that the asymptotic step-size ratio between $\beta_n$ and $\gamma_n$ is key; when $\gamma_n = \beta_n$ or wheren $\gamma_n = o(\beta_n)$, the asymptotic variance is only $O(1/\alpha)$. The key technical tool that achieves this is a novel analysis of two-time scale SA with controlled Markov noise. The theoretical results are also well-supported by simulation results.

Overall, this is a well-written paper and the idea of adding SRRW to distributed stochastic optimization is nice. In addition, the theoretical result about the influence of step-size ratio on the asymptotical covariance decay rate is also very interesting.

### Weaknesses
There are some questions that I hope the authors can address.
1) Could the authors comment a little bit more on the stability of the iterates? This is assumed to always hold, but as the authors point out, practical tricks are required to ensure this, in which case the theoretical analysis might also need tweaks.
2) Are there any tradeoffs in picking $\alpha$? Should $\alpha$ always be as large as possible, or will that affect other aspects of the algorithm, e.g. stability?
3) While the analysis is on asymptotic covariance, could the authors comment on the likely finite-time convergence rate behavior of their SRRW-SA algorithm, and whether improvements (due to the SRRW) can be also shown in terms of finite-time convergence rates?
4) The authors suggest that $\beta_n = o(\gamma_n)$ is the best step-size choice if a $O(1/\alpha^2)$ decay rate in the asymptotic covariance is desired. However, if faster convergence is to be desired, a larger learning rate (i.e. larger $\beta_n$) should always be picked, i.e. we would want to pick the maximal possible step-size required by the assumptions in the paper, i.e. $\beta_n = O(1/n^{0.5+\epsilon})$ for some $\epsilon > 0$ as close to 0 as possible, in which case $\gamma_n$ can at best match the step-size of $\beta_n$, meaning that we can only get $O(1/\alpha)$ in the asymtotic covariance decay again. Could the authors comment on this possible issue?
5) It would be nice if the authors provided some intuition as to why the $\beta_n = o(\gamma_n)$ step-size ratio can yield the $O(1/\alpha^2)$ rate. Moreover, it would be nice if the authors spelled out precisely the dependence on the difference between the step-size exponents in their asymptotic rates (i.e. if  $\beta_n = n^{-b}$ and $\alpha_n = n^{-a}$, how the rate actually depends on the difference between $a$ and $b$). If this difference does not affect the asymptotic rate, it would be nice to provide insight into how this difference might play out in practice.

### Questions
There are some questions that I hope the authors can address.
1) Could the authors comment a little bit more on the stability of the iterates? This is assumed to always hold, but as the authors point out, practical tricks are required to ensure this, in which case the theoretical analysis might also need tweaks.
2) Are there any tradeoffs in picking $\alpha$? Should $\alpha$ always be as large as possible, or will that affect other aspects of the algorithm, e.g. stability?
3) While the analysis is on asymptotic covariance, could the authors comment on the likely finite-time convergence rate behavior of their SRRW-SA algorithm, and whether improvements (due to the SRRW) can be also shown in terms of finite-time convergence rates?
4) The authors suggest that $\beta_n = o(\gamma_n)$ is the best step-size choice if a $O(1/\alpha^2)$ decay rate in the asymptotic covariance is desired. However, if faster convergence is to be desired, a larger learning rate (i.e. larger $\beta_n$) should always be picked, i.e. we would want to pick the maximal possible step-size required by the assumptions in the paper, i.e. $\beta_n = O(1/n^{0.5+\epsilon})$ for some $\epsilon > 0$ as close to 0 as possible, in which case $\gamma_n$ can at best match the step-size of $\beta_n$, meaning that we can only get $O(1/\alpha)$ in the asymtotic covariance decay again. Could the authors comment on this possible issue?
5) It would be nice if the authors provided some intuition as to why the $\beta_n = o(\gamma_n)$ step-size ratio can yield the $O(1/\alpha^2)$ rate. Moreover, it would be nice if the authors spelled out precisely the dependence on the difference between the step-size exponents in their asymptotic rates (i.e. if  $\beta_n = n^{-b}$ and $\alpha_n = n^{-a}$, how the rate actually depends on the difference between $a$ and $b$). If this difference does not affect the asymptotic rate, it would be nice to provide insight into how this difference might play out in practice.

### Soundness
3 good

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The present paper consider a family of stochastic algorithms of the following form. There exists a finite space $\mathcal{N}$ and some kind of "random walk" $\{X_n\}_{n\in\N}$ over this set. One then takes $\theta_0\in\mathbb{R}^d$ and a function $H:\mathbb{R}^d\times \mathcal{N}\to \mathbb{R}^d$ and sets 

$$\theta_{n+1} = \theta_n + \beta_n\,H(\theta_n,X_n).$$

One particular example is when $X_n\sim \mu$ and $H(\theta,i) = -\nabla f(\theta,i)$ for some $f$. Then the above is basically a form of stochastic gradient descent for the function

$$F(\theta) :=\sum_i \mu_i\,f(\theta,i).$$

The authors say that $X_n$ may be thought of as a "token", so they are considering token distributed optimization methods. 

The authors are especially interested in the case where $X_n$ is a stochastic process called "self-repellent random walk". Basically, this kind of RW have asymptotic distribution $\mu$, but they are designed to be less likely to jump to states that have already been visited many times. A recent paper by Doshi et al. showed that such random walks lead to smaller-variance Monte Carlo estimates of expectations with respect to $\mu$. In fact, the variance in this case decreases like $\alpha^{-1}$, where $\alpha>0$ measures the amount of self-repulsion. 

The present paper builds on this to show a remarkable result. Namely, under suitable conditions, $\theta_n$ converges to a fixed point $\theta_*$ (in expectation) of the iteration, and $\theta_n - \theta_*$ has variance decrease when $\alpha$ grows. In fact, the variance goes down like $1/\alpha^2$ for large $\alpha$. In particular, this implies that self-repellent walks are "even better" for optimization or fixed point computations than for Monte-Carlo integration. However, this main result requires on tuning $\beta_n$ to be smaller than a parameter describing the rate of change of the "self-repulsion measure". In fact, the authors show that, when this is not the case, it may be that a large $\alpha$ will not help at all. The paper's proofs build on Doshi et al and rely on stochastic approximation methods.

### Strengths
The paper describes a surprising phenomenon -- even considering the paper by Doshi et al. It gives precise asymptotic results. Their small simulation study observe gains in finite time. The paper is very clear and convincing.

### Weaknesses
All results are asymptotic. It is not clear (theoretically) whether there are gains for finite time, before eg. the token can visit most elements of $\mathcal{N}$. The analysis requires some *a priori* assumptions about the ODE invoked for stochastic approximation. The analysis is heavily indebted to Doshi et al.

### Questions
I only have one very open ended question: is there any hope of getting finite sample bounds?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper deals with distributed stochastic optimization, with tokens sampled by self-repelling Markov chain. The authors proved the law of large numbers and central limit theorem for the optimization iterate errors, which are refinements of recent work of Doshi et al. The proposed algorithm achieves $1/\alpha^2$-rate, and the theoretical results are corroborated by the empircal study.

### Strengths
The paper studies rigorously a distributed stochastic optimization using self-repelling random walks. The paper is well-written, and I enjoyed reading it. I have also checked most theoretical results, and they appear to be correct. The rate $1/\alpha^2$ also appears to be new.

### Weaknesses
The paper is mostly motivated by the recent progress of Dochi et al., and it is not clear what is the "main" novelty of this paper compared to the previous work (fundamentally). It seems to me that most results are refinements of Dochi et al. (while I agree that the setting is slightly different.) The authors may add a paragraph to highlight the main "technical" novelty of this paper. 

Also the parameter $\alpha$ measures the "heaviness" of the self-repelling random walk, which is basically a hyper-parameter. It seems to be a bit strange to quantify the errors using $Poly(1/\alpha)$ (provided that one sends $\alpha \to \infty$ and I do have concerns on the real application in this regime). Also the idea of using self-repelling random walk to accelerate optimization is not new, see https://arxiv.org/abs/2005.04507 (in which it was shown to outperform many existing algorithms.) The authors may think of citing the work and some references therein.

### Questions
See the Weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studied a family of distributed stochastic optimization algorithms where gradients
are sampled by a token traversing a network of agents using the Self-Repellent Radom Walk (SRRW).

This paper generalized the previous SRRW by introducing an additional iterate to update the empirical distribution so the resulting algorithm shares a similar pattern with the two-time-scale stochastic approximation (SA).

The author then provides some theoretical understanding of the proposed algorithm, including 
- (1) almost surely convergence of two iterates 
- (2) central limit theorem (CLT) of parameter $\theta_n$ 
- (3) order analysis on the asymptotic variance matrices for three different time-scales choices.

### Strengths
The paper is well-written and solid. I like reading the paper.

The paper contains rich theoretical analysis, which investigates deeply about the properties of proposed methods. The acceleration effect of the proposed method is indeed new and interesting (at least to me).

Most of the proof in the appendix seems to be correct, but I didn’t check very carefully.

The simulation validates the theoretical finding in the paper.

### Weaknesses
A concern in my mind is that the paper assumes $X$ takes values in a finite state space. 
The decentralized optimization where only a single agent is active each time is a particular example.
Are there any other examples where $X$ takes finite value?

In my opinion, for a general SA method, the randomness or the noise could be various. 
Note that the Poisson method used in the proof is not limited to discrete randomness.
Is it possible to extend the analysis to a more general setting where $X$ could be a continuous random variable?
If not, where is the main difficulty?

### Questions
1. Under the paragraph below (3), the author tries to explain why SRRW gets its name. More specifically, they said `` if node $j$ has been visited more often, so far, the entry $x_j$ becomes larger (than target value $\mu_j$ )’’. I didn’t understand the logic behind it. If node $j$ has been visited more often, I think $x_j$, as the coordinate of a distribution vector, should be close to $\mu_j$. I can’t tell whether $x_j$ is larger than $\mu_j$ or not.  However, I acknowledge that the nonlinear kernel in (3) would encourage the algorithm to visit the states that are less visited, based on its expression.

2. The newly introduced iterate in (4b) generalizes the original algorithm and allows us to treat the resulting algorithm as a two-time-scale SA. However, I didn’t see much motivation to introduce the new iterate. Could the author elaborate more on the motivation?

3. If we set $\alpha=\infty$, from (6), the variance matrix would be zero. Could I say, in this case, $x_n$ actually converges to $\mu$ at a faster rate than $\gamma_n$ so that the CLT degenerates to zero? How to explain the intuition behind it? 

4. From the simulation, it seems the larger $\alpha$, the faster convergence. Is there any suggestion for a practical choice of $\alpha$?

5. If the $\alpha$ is also updated, for example, we use $\alpha_t$ at the iterate $t$ that increases at a carefully selected rate in advance (or perhaps could be updated using a third iterate). Can we accelerate the convergence rate of $\theta_n$ so that its mean square error is faster than $\beta_n$?

I will increase my point to 8 if most of my questions are addressed.

------------------------------------ Post rebuttal --------------

Thanks for the authors' clarification.  Most of my concerns and questions are well addressed, so I increase my point to 8.
However, there are still two points I don't agree with the author.

One point I disagree with is that I think when $\alpha \to \infty$, the kernel (3) is still well defined.
In this case, I think $K_{ij}(x) = 1$ if and only if $x_j/\mu_j = \arg\min_{l} x_l/\mu_l $.
As you can see, this kernel is reduced to a deterministic transition. 
I guess this reduction makes the system no longer random so that the CLT degenerates.
One property of this generation is that the variance matrix would converge to zero.
This actually is a good property from my perspective because it means that one could get a convergence rate faster than the step size.

Let's do a simpler thought experiment. Let $X_t \sim \sqrt{\beta_t} \cdot N(0, c_t )$.
If the variance $c_t$ is non-zero (so that $c_t \to 1$ w.l.o.g.), then the MSE of $X_t$ is dominated by the variance and is of order $\beta_t$. 
If the variance is (nearly) zero (say $c_t \to 0$), then the MSE is dominated by a higher-order term and we have $E |X_t|^2$ converge faster than $\beta_t$.

Back to this paper, I guess the counterpart of $c_t$ in this paper is $1/\alpha$. So, if we let $\alpha \to \infty$, we would have $c_t \to 0$. This is the reason why I ask whether increasing $\alpha$ would fasten the convergence. The author's response works only when the optimal $\alpha^{\star}$ exists and is finite. However, the particular case I am interested in is when $\alpha^{\star} = \infty$.
I think that exploring the case where  $\alpha^{\star} = \infty$ detailedly is worth a more detailed examination. 
It is fine not to discuss this in this paper.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
