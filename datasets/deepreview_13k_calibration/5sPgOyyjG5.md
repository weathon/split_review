# Feynman-Kac Operator Expectation Estimator

- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 5, 1, 3

## Abstract
The Feynman-Kac Operator Expectation Estimator (FKEE) is an innovative method for estimating the target Mathematical Expectation $\mathbb{E}_{X\sim P}[f(X)]$ without relying on a large number of samples, in contrast to the commonly used Markov Chain Monte Carlo (MCMC) Expectation Estimator. FKEE comprises diffusion bridge models and approximation of the Feynman-Kac operator. The key idea is to use the solution to the Feynmann-Kac equation at the initial time $u(x_0,0)=\mathbb{E}[f(X_T)|X_0=x_0]$. We use Physically Informed Neural Networks (PINN) to approximate the Feynman-Kac operator, which enables the incorporation of diffusion bridge models into the expectation estimator and significantly improves the efficiency of using data while substantially reducing the variance. Diffusion Bridge Model is a more general MCMC method. In order to incorporate extensive MCMC algorithms, we propose a new diffusion bridge model based on the Minimum Wasserstein distance. This diffusion bridge model is universal and reduces the training time of the PINN. FKEE also reduces the adverse impact of the curse of dimensionality and weakens the assumptions on the distribution of $X$ and performance function $f$ in the general MCMC expectation estimator. The theoretical properties of this universal diffusion bridge model are also shown. Finally, we demonstrate the advantages and potential applications of this method through various concrete experiments, including the challenging task of approximating the partition function in the random graph model such as the Ising model.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
Doing MCMC is hard (time consuming, and somewhat wasteful because of the burn-in period). The authors propose a post-processing method using the samples from some MCMC procedures, which admit an Itô decomposition, to approximate moment estimates of the desired sampling density. They use a denoising technique based on physics informed neural networks as part of the post-processing mechanism.

### Strengths
The goals stated in the introduction are bold, and quite interesting. Obtaining results in this line would prove quite useful in general for ML and statistics.

I appreciate that the authors include small introductions for the Euler-Maruyama method and physics informed neural networks in the appendix. However their existence should be indicated in the main text.

### Weaknesses
Presentation is bad throughout. There are plenty of typos. The authors do not use parenthetical citations and instead insert them in the text which makes for a less pleasant reading experience.

The notation introduced in line 232 definitely needs improvement, I do not understand which side is supposed to be the one that will be used later. Even then, it is unclear what is being defined, as there are two definitions for $\hat{\mu}_{t_i}$ .

In Assumption 2.2, it is not clear what $\mu^{\mathcal{P}_\theta}$ means.

The notation in Algorithms 1 and 3 should be introduced before the algorithms. For example, it is not clear where $Y_T$ comes from, and why it is required.

Table 1 is impossible for me to parse. I invite the authors to mimic the conciseness of their own Table 5 for summarizing the numerical results.

There is a link to GitHub page, which has been confirmed to not belong to the authors, but I do not see a good reason for why the authors would want to include a link to a GitHub that is not theirs. Usually a citation to the original article is enough.

The proofs in the main text for Theorems 2.1, 2.6 and 2.7 should either refer directly to the Appendix where they are proved, or be proved right there.

Regarding Theorem 2.8, the comment in the 'proof' space makes me think the Authors were not the first to prove it, in which case they should indicate it explicitly; otherwise it would be plagiarizing.

Currently Section 4 is quite lacking, including the aforementioned Table 1 which I cannot comprehend (by the way, it is missing a reasonable caption). 

A proposed method like this should be thoroughly tested, which in the current state of the paper it has not been. The methods the authors refer for comparison should include appropriate references. Furthermore, the numerical results lack error quantification. It is unclear if the reported results are from a single run or averaged over multiple runs, and if the latter, the standard deviations of the average MSEs are not reported in any way. At the very least they should be included as error bars, or in an appendix. This helps the reader understand how strong (if at all) the proposed method is. The labels used in the figures (MCMC-T, MCMC-R, and MCMC-C) are not intuitive, and require the reader to constantly refer back to the text to understand what they mean. The logic behind these names should be made clearer.

### Questions
In Theorem 2.1, what does "Linear growth" mean?

In Assumption 2.4, what does "D is the metric of the parameter" mean?

In Theorem 2.6, should "we exist" be "there exists a set"?

In Algorithm 1, can the authors clarify what is the main difference between $X_t$ and $X_i$? The distinction is not clear to me. 

How are the integrals in Algorithm 2 computed? Are the authors able to evaluate the integrals explicitly? If so, they should indicate how and why they are able to do so.

How does the computational cost of this approach compare to other MCMC approaches?

One of the main criticisms posed about MCMC methods is that they are not optimal since they spend quite some time in the burn-in phase (lines 56, 82). However, for the proposed method to work the authors assume that they have access to samples from a distribution that are obtained via an MCMC, that has already gone through a burn-in period (lines 188, 192). How can the authors support their claim that this method is better (line 107) than MCMC if it is still spending a similar amount of samples in burn-in?

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The authors propose the Feynman-Kac Operator Expectation Estimator (FKEE) to approximate the target distribution E[f(X)]. This estimator contains two parts: (1) A diffusion bridge model with parameters optimized to minimize the Wasserstein distance to the target distribution, and (2) a method based on the Feynman–Kac equation, formulated as a partial differential equation (PDE) and solved approximately using Physics-Informed Neural Networks (PINNs), which employ a least-squares approach. The experiments focus on approximating the partition function in a random graph model.

### Strengths
A significant strength of this work is the innovative linking of the diffusion model to high-dimensional partial differential equations (PDEs), with Physics-Informed Neural Networks (PINNs) effectively employed to overcome the curse of dimensionality in solving these PDEs.

### Weaknesses
1. The Feynman–Kac model (Algorithm 2) with the PINN solver lacks a convergence or error estimate, which would be valuable for assessing its accuracy and reliability.

2. In the experiments, the authors claim that "using fewer points on the Markov chain achieves higher accuracy in approximating expectations." However, it is unclear if this result generalizes beyond the specific example provided, as it appears quite context-dependent.

### Questions
The authors mention in the Discussion that their method requires the boundary conditions of the PDE to satisfy a smoothness condition, specifically that f is in C^2, and that this requirement broadens the scope of their approach. However, it seems that C^2 smoothness could be more restrictive than a Lipschitz assumption. Could the authors clarify how they view this requirement as less restrictive? Additionally, could they discuss any potential limitations this might introduce for functions that are not in C^2?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors proposed to leverage the Feynmann-Kac equation via Physically Informed Neural Networks (PINN) to approximate the target Mathematical Expectation efficiently and heuristically without causing a large variance.

### Strengths
the idea of using Feyman-Kac to approximate the expectation is interesting.

### Weaknesses
The scalability of the algorithm w.r.t. dimension is not verified sufficiently. d=20 is too small. There are no real-world simulations.

The authors criticize the large variance issue by the MCMC method but fail to justify theoretically why the proposed method yields a lower variance. The empirical support is limited.

NIT: Theorem 2.1: the discretization error by Growall inequality is weak and exponentially dependent on time. Girsanov can be used to fix it.

### Questions
1. I don't know why and when MCMC is required to impose complex constraints on the distribution and performance function. Some references are suggested.

2. I don't see when MCMC is not the optimal decoding method. It appears to me that burn-in is not a significant limitation and only affects the performance on a negligible scale and can be easily fixed via a large stepsize in the beginning for warm-up.

3. Discussions on the limitations would be preferred.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
The paper presents two generative models to use in the context of sampling: a diffusion bridge with $W^2$-loss and algorithm based on solving the Feynmann-Kac PDE using PINNS.

### Strengths
Developing new sampling methods using ideas from generative model is an active area with lots of promising recent advances.

### Weaknesses
 + There is no really new theoretical contributions in this paper. All the theorems mentioned in the paper are standard results. The diffusion bridge model has been used in various iterations in countless papers in the literature, for example by Doucet and collaborators.  

+ There is no indication that the algorithms presented here will scale up with dimension, especially if using the W^2 loss, so the claim that this improves on MCMC seem somewhat overblown. The curse of dimensionality is a significant concern for methods relying on approximating densities or transport maps in high dimensions, and the paper does not adequately address this. The computational cost of calculating the $W^2$ distance, which involves solving an optimal transport problem, also increases rapidly with dimension, making it impractical for high-dimensional applications.

+ Using a PINNs to solve the Feynmann-Kac equation is very unlikely to work in high dimension as PINNs are usually are no easy to to train. The training of PINNs is known to be highly sensitive to hyperparameter choices and network architecture, and convergence is not guaranteed, especially in high-dimensional settings. Furthermore, the accuracy of PINN solutions can degrade significantly as the dimensionality increases, making it an unreliable approach for high-dimensional problems.

+ Lack of experiments on high-dimensional data sets.

+ No head-to-head comparisons with state of the art algorithms.

### Questions
+ What are the limitations  of your methods regarding dimension? 

+ How does your algorithm compare with other neural ODE/SDE, diffusion models, bridges models in the literature?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The manuscript combines several DNN-based numerical techniques, associated with solving and learning SDEs and their PDE counterparts, with the aim of sampling from distributions and averaging over observables. Specifically, a type of neural-SDE is put forward and trained to converge to the desired distribution. Next averages of functions are estimated using the Feynman-Kac formula, wherein a PDE is derived from the learned SDE which “calculates” the averages for us given that one sets the boundary condition to be the function one wishes to average. This complex problem is solved using a PINN approach. Some numerical results on random graphs are reported in a table.

While the paper suggests an interesting technical path to explore in this important subdomain MC samplers— it is not clear from reading the manuscript how much of this is incremental work stringing together a series of known results or rather an original and meaningful step forward. While I am only a causal user of Monte-Carlo, my strong feeling is that the benchmarks shown are insufficient to prove that
this specific combination of techniques outperforms existing ones (including DNNs/PINN-based ones and more advanced MC techniques). Turning to the techniques themselves, it seems that neural-SDEs preceded the current work [Tzen, Ragidsky 2019], and that using Feynman-Kac formula with a combination of DNNs to estimate observables on an SDE has also been done before [Blechshmidt, Ernst 2021 and refs therein]. Reading into the latter work, it seems that DNNs have been used slightly differently than in the current work to solve the PDE associated with the SDE, but is this a conceptual change given the common use PINNs to solve PDE? Does it hold the key to any SOTA results? The related work section (which has been delegated to the appendix) and the general causal referencing to related works (such as Tzen et. al.) leave the non-expert reader with little understanding of the true novelty of the current results.

The presentation of the work also leaves a gap between conceptual claims and practical contributions. It also feels fragmented and the
common use of signposts and bold notation only worsens this in my mind. The conceptual claims, which are sometimes grand, are hard to substantiate. For instance, “Establishing a Link Between Sampling Methods and High-Dimensional Partial Differential Equations”, taken at face value, can hardly be attributed to the current work with all the knowledge on SDE, Fokker-Plank Equations, and Feynman-Kac formula. Also “Expanding the Scope of Expectation Estimators“, feels vague. Is there a current scope of expectation estimators? What results in the current work expand this scope in a way that others can't? Finally, in their introduction, the authors allude to the fact that the authors have an affirmative answer to the question “Is it possible to unify most existing MCMC algorithms into a cohesive framework to create a universal sampler for expectation estimation?“--- This is such a rich and complex problem that providing an affirmative answer would clearly violate various prevalent complexity theory assumptions. For instance, can the authors show that their sampler solves the Ising Spin-Glass problem? Can the authors even solve the much simpler case of the 2d Ising model at the phase transition and compute long-range observables? Does their technique outperform various ones used in physics to overcome sampling problems such as replica-exchange Monte Carlo?

The above issues, concerning the entanglement with previous works, evidence of going beyond SOTA, and its portrayed grand scope, prevent me from recommending it for publication in ICLR.

### Strengths
The work addresses an important fundamental topic. It provides an interesting combination of DNN-based techniques.

### Weaknesses
The manuscript combines several DNN-based numerical techniques, associated with solving and learning SDEs and their PDE counterparts, with the aim of sampling from distributions and averaging over observables. Specifically, a type of neural-SDE is put forward and trained to converge to the desired distribution. Next averages of functions are estimated using the Feynman-Kac formula, wherein a PDE is derived from the learned SDE which “calculates” the averages for us given that one sets the boundary condition to be the function one wishes to average. This complex problem is solved using a PINN approach. Some numerical results on random graphs are reported in a table.

While the paper suggests an interesting technical path to explore in this important subdomain MC samplers— it is not clear from reading the manuscript how much of this is incremental work stringing together a series of known results or rather an original and meaningful step forward. While I am only a causal user of Monte-Carlo, my strong feeling is that the benchmarks shown are insufficient to prove that
this specific combination of techniques outperforms existing ones (including DNNs/PINN-based ones and more advanced MC techniques). Turning to the techniques themselves, it seems that neural-SDEs preceded the current work [Tzen, Ragidsky 2019], and that using Feynman-Kac formula with a combination of DNNs to estimate observables on an SDE has also been done before [Blechshmidt, Ernst 2021 and refs therein]. Reading into the latter work, it seems that DNNs have been used slightly differently than in the current work to solve the PDE associated with the SDE, but is this a conceptual change given the common use PINNs to solve PDE? Does it hold the key to any SOTA results? The related work section (which has been delegated to the appendix) and the general causal referencing to related works (such as Tzen et. al.) leave the non-expert reader with little understanding of the true novelty of the current results.

The presentation of the work also leaves a gap between conceptual claims and practical contributions. It also feels fragmented and the
common use of signposts and bold notation only worsens this in my mind. The conceptual claims, which are sometimes grand, are hard to substantiate. For instance, “Establishing a Link Between Sampling Methods and High-Dimensional Partial Differential Equations”, taken at face value, can hardly be attributed to the current work with all the knowledge on SDE, Fokker-Plank Equations, and Feynman-Kac formula. Also “Expanding the Scope of Expectation Estimators“, feels vague. Is there a current scope of expectation estimators? What results in the current work expand this scope in a way that others can't? Finally, in their introduction, the authors allude to the fact that the authors have an affirmative answer to the question “Is it possible to unify most existing MCMC algorithms into a cohesive framework to create a universal sampler for expectation estimation?“--- This is such a rich and complex problem that providing an affirmative answer would clearly violate various prevalent complexity theory assumptions. For instance, can the authors show that their sampler solves the Ising Spin-Glass problem? Can the authors even solve the much simpler case of the 2d Ising model at the phase transition and compute long-range observables? Does their technique outperform various ones used in physics to overcome sampling problems such as replica-exchange Monte Carlo?

The above issues, concerning the entanglement with previous works, evidence of going beyond SOTA, and its portrayed grand scope, prevent me from recommending it for publication in ICLR.

### Questions
Can the author disentangle their works from past literature on neural SDE and Feynman-Kac's use of averaging observables?

Can the authors provide evidence that their universal sampler outperforms the existing techniques, including those in Blechshmidt
et. al.(2021)? Can they provide some canonical well-excepted benchmark at which they excel over others?

### Soundness
3

### Presentation
2

### Contribution
2
