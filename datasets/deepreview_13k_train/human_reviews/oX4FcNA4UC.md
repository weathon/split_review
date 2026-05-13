# A Simulation-Free Deep Learning Approach to Stochastic Optimal Control

- Decision: Reject
- Scores: 6, 3, 5, 3

## Abstract
We propose a simulation-free algorithm for the solution of generic problems in stochastic optimal control (SOC). Unlike existing methods, our approach does not require the solution of an adjoint problem, but rather leverages Girsanov theorem to directly calculate the gradient of the SOC objective on-policy. This allows us to speed up the optimization of control policies parameterized by neural networks since it completely avoids the expensive back-propagation step through stochastic differential equations (SDEs) used in the Neural SDE framework. In particular, it enables us to solve SOC problems in high dimension and on long time horizons. We demonstrate the efficiency of our approach in various domains of applications, including standard stochastic optimal control problems, sampling from unnormalized distributions via construction of a Schr\"odinger-F\"ollmer process, and fine-tuning of pre-trained diffusion models. In all cases our method is shown to outperform the existing methods in both the computing time and memory efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper, titled "A Simulation-Free Deep Learning Approach to Stochastic Optimal Control," proposes a novel method for solving high-dimensional Stochastic Optimal Control (SOC) problems using a deep learning-based approach. The prposed approach leverages the Girsanov theorem to compute gradients on-policy without needing adjoint-based differentiations. The method is shown to handle complex SOC scenarios more efficiently in terms of memory and computational resources. 

The method is shown to handle complex SOC scenarios more efficiently in terms of memory and computational resources. However, its reliance on simulation-free gradient estimation may introduce variance issues when applied to challenging SOC landscapes, where maintaining accuracy across high-dimensional distributions without simulations may be difficult.

### Strengths
1. The use of the Girsanov theorem for gradient estimation is theoretically sound, particularly in reducing the computational burden traditionally associated with Neural SDEs. This efficiency makes the approach suitable for high-dimensional SOC problems and applications that involve large neural networks.

2.  This formulation allows for gradient calculations without differentiating through the SOC trajectories, which is a considerable advancement over existing SOC methods.

3. Experimental results show clear computational benefits in terms of memory usage and runtime, as well as improved accuracy over baseline methods such as Neural SDEs and the Path Integral Sampler.

### Weaknesses
1. The reliance on the Girsanov theorem and assumptions related to Wiener processes and Gaussian distributions may limit the approach's applicability to more general stochastic processes or non-Gaussian noise environments. Specifically, the method's performance could degrade significantly when applied to systems with heavy-tailed noise or jump discontinuities, which are not well-approximated by Gaussian distributions. The assumption of a reference process close to the target control also raises concerns about the method's robustness in scenarios where the initial guess is poor, potentially leading to convergence issues.

2. While the method shows improvements in certain metrics, the paper does not discuss potential instability or convergence challenges in high-dimensional settings or on extended time horizons. The absence of a rigorous convergence analysis leaves open the question of whether the method can consistently find optimal or near-optimal solutions, especially as the dimensionality of the state space and the length of the time horizon increase. The method's behavior in long-horizon tasks, where error accumulation can be significant, is also not addressed.

3. While the proposed approach avoids back-propagation through stochastic differential equations, it introduces complexity in high-dimensional SOC problems. Specifically, the computation of the Girsanov density and its gradient, which involves expectations over the stochastic trajectories, can become computationally expensive and numerically unstable in high dimensions. This limitation could hinder scalability in large-scale applications, particularly when the dimension of the control space is also high.

### Questions
1. The simulation-free gradient estimation may introduce variance issues. How does the method handle situations where high variance arises in the gradient estimates?

2. The approach relies on the reference process being close to the target control. Could the authors elaborate on how to select or adapt this reference process dynamically?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper considers a likelihood ratio gradient estimator for stochastic differential equations with a controlled drift. The goal of the proposed estimator is to compute the gradient of a cost function consisting of a cumulative cost part and a terminal cost. The authors claim that the "novelty" of their approach lies in the simulation-free (but the on-policy simulation of the $X^\theta$ process is still needed) nature of their algorithm, which doesn't need to simulate the sensitivity processes of $X_t^\theta$ w.r.t. $\theta$. The authors then demonstrate that the computation time and memory cost of the likelihood ratio gradient estimator is improved over the solver back-propagation method.

### Strengths
The notation and writing are clear.

### Weaknesses
Unfortunately, I do not see any novelty in the method proposed in this paper... The likelihood ratio gradient estimator for SDEs is well-known (Yang & Kushner, 1991). I am uncomfortable with the authors' claim that this approach is their contribution.

I am open to further discussion, but in order for me to raise the score, please explain the novelty of your method or the contribution beyond implementing this estimator. I am okay with experimental/empirical validation of the effectiveness of the LR gradient estimator in complex machine learning applications, but the current version of the paper clearly isn't able to address this. 

Moreover, the LR-based methods, due to the nature of laws of SDEs, are only applicable to settings where the drift is controlled; i.e. the volatility cannot depend on $\theta$. Furthermore, I believe that it is usually the case that the LR method has a significantly larger variance in settings where the volatility is small (because you are forcing the diffusion to go to unlikely locations), and one could imagine that optimal control prefers parts of the state space where the volatility is indeed small. So, this seems to suggest that the variance performance, which is not compared in this paper, will be worse compared to back-prop or pathwise sensitivity-based methods like Li et al. 2020, Massaroli et al. 2021, and Wang et al. 2024.

> Massaroli, Stefano, et al. "Learning stochastic optimal policies via gradient descent." IEEE Control Systems Letters 6 (2021): 1094-1099.


>Li, Xuechen, et al. "Scalable gradients for stochastic differential equations." International Conference on Artificial Intelligence and Statistics. PMLR, 2020.


>Wang, Shengbo, Jose Blanchet, and Peter Glynn. "An Efficient High-dimensional Gradient Estimator for Stochastic Differential Equations." arXiv preprint arXiv:2407.10065 (2024).

### Questions
There seems to be a typo in equation (10). 

What happened to the right one in Figure 2? Are you using different sample sizes to compute the empirical losses? You should plot a confidence interval instead of these lines: the variability in this plot does not indicate a worse variance performance of the estimator, it just suggests that you are using fewer sample paths to evaluate the empirical cost. Am I right?

How well does the estimator perform in terms of variance?

### Soundness
3

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper propose a simulation-free algorithm for the solution of generic problems in stochastic optimal control (SOC), simulating trajectories using an actual control, which is more efficient and scalable than the vanilla method commonly used recently. By applied on some examples, the paper illustrates the efficacy of the new method.

### Strengths
1. This paper solves a critical research problem about simulation-free stochastic optimal control problem.

2. This paper is clear, with a clear description of the methods and of the state of the art. And the presentation of the technical discussion is accurate and well-organized.

3. The organization of the evaluation sections is clear, and the presented results show the advance and efficiency of the proposed method.

### Weaknesses
1. This algorithm is required that the base distribution used in the generative model be a point mass distribution, which restricts the applications.

2. This article gives fewer practical examples and does not allow the reader to quickly understand the application scenarios and advantages of this method.

3. The term “simulation-free” as proposed in the title and abstract is not fully explained and may be difficult to understand for readers unfamiliar with the field and terminology.

### Questions
1. As seen in weakness 3, can you explain what “simulation-free” means, what are the advantages in practice, and what are the applications?

2. The paper presents 6 propositions, is it possible to describe the relationship between the propositions of each part? and their role in the methodological modeling of this paper?

3. The pseudo-code for the algorithm is listed in Algorithm 1, but is it possible to create a diagram of the algorithmic framework that represents in detail the operation of the network to make it easier for the reader to understand?

4. In the comparision experiment “Quadratic Ornstein-Uhlenbeck Example (easy setup, no warm-start)” in Fig. 2 right panel, the vanilla method seems not converge. Can a convergent method be compared with the proposed method?

5. The experiment in Fig. 4 shows an example of the method with heat map in a region constant with grid. Is the method able to handle with high-dimensional problems since the grids-based example?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a method to solve stochastic optimal control problems by utilizing the Girsanov theorem to change the probability measure. It claims that this reformulation makes the policy objective explicit in terms of the control input, allowing existing optimization techniques to be applied directly.

### Strengths
* This paper attempts to solve an important problem.

* The presentation is clear and easy to follow.

* The authors have made efforts to present their algorithm in a rigorous manner

### Weaknesses
There are some critical errors in the paper:

* The core foundation of the proposed algorithm is the change of probability measure using the Girsanov theorem. However, there seems to be a conceptual confusion throughout the paper. When calculating the expectation in Equation (2), the probability measure is the one under which the random noise in the system is a Brownian motion. This measure is independent of the SDE of $X^u,$ it is determined by how the random noise in the stochastic system is measured. By changing the probability measure, it implies we are considering a different way of measuring the noise (e.g., applying a transformation to it), but this is clearly not the intention of the paper. The authors seem to be confusing the change of measure with a change in the dynamics of the system itself. The Girsanov theorem is being misapplied; it does not justify rewriting the expectation in terms of a different SDE with a modified drift, while keeping the same underlying noise process. The fundamental issue is that the expectation in (2) is defined with respect to the measure under which the noise is a standard Brownian motion, and this measure is not altered by the control $u$.

* I am uncertain about the correctness of Lemma 1, as the proof is omitted. Specifically, I do not see how the Girsanov factor $G(u, v)$ is derived. The probability measure is not changed from (2) to (4). Also, the notation $\mathbb{E}_{X^u}$ is unclear to me. All expectations in this paper should be the same expectation as in (2), since it is exactly how the trajectories are sampled from the environment, as shown in Algorithm 1. The authors need to explicitly show how the Girsanov factor arises from the specific change of measure they are attempting to implement, and clarify the notation to avoid ambiguity. The expectation should be with respect to the original measure, not a measure dependent on $X^u$.

* Proposition 1 appears to be incorrect. Assuming that Equation (4) is valid, Equation (8) is obtained by directly differentiating (4) with respect to the policy parameter $\theta$. At the end of the proof, the authors claim that (8) implies (6) because (8) holds for any fixed reference control $v$, hence we can just simply let $v = u$ which yields $M(u, v) = 1$. This reasoning is not true because "(8) holds for any fixed reference control $v$" DOES NOT mean that its value is independent of $v$. The derivative in (8) is a function of $v$, and setting $v=u$ after differentiation is not a valid operation to obtain (6). The authors are incorrectly assuming that the derivative is uniform with respect to $v$, which is not generally true. The argument relies on a flawed assumption about the interchangeability of limits and function evaluation.

* The experimental results are not convincing. First, all the problems presented in the experiments can be solved using either Monte Carlo methods or analytical solutions. Second, the proposed algorithm is only compared with the vanilla method. There are various existing algorithms that might be included for comparison, such as 'Solving high-dimensional partial differential equations using deep learning' by Han et al.

### Questions
Please see the weaknesses.

### Soundness
1

### Presentation
2

### Contribution
1
