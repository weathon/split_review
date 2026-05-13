# Almost sure convergence of stochastic Hamiltonian descent methods

- Decision: Reject
- Scores: 6, 3, 6

## Abstract
Gradient normalization and soft clipping are two popular techniques for tackling instability issues and improving convergence of stochastic gradient descent (SGD) with momentum. 
In this article, we study these types of methods through the lens of dissipative Hamiltonian systems. Gradient normalization and certain types of soft clipping algorithms can be seen as (stochastic) implicit-explicit Euler discretizations of dissipative Hamiltonian systems, where the kinetic energy function determines the type of clipping that is applied.
We make use of dynamical systems theory to show in a unified way that all of these schemes  converge to stationary points of the objective function, almost surely, in several different settings:
a) for $L-$smooth objective functions,
when the variance of the stochastic gradients is possibly infinite
b) under the $(L_0,L_1)-$smoothness assumption, for heavy-tailed noise with bounded variance and c) for $(L_0,L_1)-$smooth functions in the empirical risk minimization setting, when the variance is possibly infinite but the expectation is finite.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper studies a family of stochastic gradient methods given by equation 9 and for this family almost sure convergence to stationary points is proved under the following settings:
1. Smooth objective functions with stochastic gradients having locally bounded variance,
2. $(L_0,L_1)$-smooth objective functions with stochastic gradients having finite second moments,
3. $(L_0,L_1)$-smooth objective functions occurring in the empirical risk minimization problem with stochastic gradients having bounded expectation.

Two interesting algorithms that are part of this family are SGD with soft clipped momentum and SGD with normalized momentum.

### Strengths
The paper is written in an easy to understand way and the ideas flow smoothly between sections. On the technical side it has the following strengths:
1. Previous work has given guarantees that hold either in expectation or with high probability. These do not guarantee the convergence of every trajectory. However, the results presented in this paper can guarantee the convergence of almost all the trajectories i.e. there exists a set of initial points of measure zero whose trajectories are not guaranteed to converge.
2. The analysis done in previous work holds true only under strong assumption that the stochastic gradients are bounded. Whereas the current work’s analysis holds under much more general assumption of bounded variance.

### Weaknesses
The paper focuses primarily on proving almost sure convergence and does not provide any claims about convergence rate. The paper could benefit from showing convergence rate of the family of methods given by equation 9 under one of the settings. The analysis also seems to have a limitation in the $(L_0, L_1)$-smooth setting, as it requires a specific clipping condition (Assumption 4 iii) which excludes standard momentum, specifically when $\varphi(x) = ||x||^2/2$. This is a significant limitation as it means the analysis does not cover the standard SGD with momentum algorithm in the $(L_0, L_1)$-smooth setting, which is a widely used method. This restriction should be more clearly highlighted in the paper, as it limits the scope of the theoretical results.

### Questions
1. (Clarification for Assumption 4 iii) This assumption is not satisfied when $\varphi(x)=||x||^2/2$. For the family of algorithms under study defined by equation 9 to include SGD with momentum we need $\varphi(x)= ||x||^2/2$. So, the analysis does not hold true for SGD with momentum. Is this correct?
2. (Suggestion about numerical experiments in Appendix C) The main claim of the paper that the family of algorithms converges to a stationary point of the objective function can be better demonstrated if there are graphs showing the evolution of $||\nabla F||_2$ with the number of epochs.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper investigates the almost sure convergence of stochastic Hamiltonian descent methods in optimization, especially in the context of machine learning and statistical estimation. Key methods discussed include gradient normalization and soft clipping, which are used to stabilize stochastic gradient descent (SGD) with momentum, commonly applied in non-convex optimization settings. The authors analyze the convergence properties of these modified SGD algorithms, especially when applied to objective functions with heavy-tailed noise and potentially infinite gradient variance, by classifying these techniques into dissipative Hamiltonian systems.

 One of the main contributions of the paper is to show that gradient normalization and soft clipping can be viewed as stochastic implicit-explicit Euler discretizations of dissipative Hamiltonian systems. By utilizing Hamiltonian dynamics and dynamical systems theory, the authors provide a unified convergence framework for these methods in different objective function settings, including \(L\)-smooth and \((L_0, L_1)\)-smooth functions.

The paper introduces assumptions for the objective function and the stochastic gradient, such as coercivity and locally bounded variance, which ensure that the optimization problem satisfies the necessary conditions for convergence. Moreover, the convergence guarantee is extended to settings with heavy-tailed noise, which is common in real data. In particular, the analysis shows that the iterative updates of these modified SGD algorithms converge almost surely to the set of stationary points of the objective function under these assumptions.

The proof strategy involves the use of a Lyapunov function based on the Hamiltonian of the system to demonstrate the finiteness and boundedness of the iterative sequences. The analysis then uses an ODE (Ordinary Differential Equation) approach to show that these sequences converge almost surely to stationary points of the objective function, and not just in expectation. This result is important because it ensures convergence along each individual optimization path and not just on average, which is crucial for the robustness of optimization algorithms.

### Strengths
- The paper is very well-written, and the authors rigorously verify the standard assumptions of the ODE approach, even if this means including assumptions that may seem idealized.

### Weaknesses
The paper doesn’t bring substantial new insights to the field; it essentially revisits classical methods, line by line, and demonstrates the applicability of standard ODE-based techniques. While it is certainly rigorous and methodical, the paper ultimately falls short of deepening our understanding of the algorithms themselves or providing fresh perspectives on their behavior. This makes it a rather conventional contribution, adhering closely to established approaches without pushing beyond them in terms of theoretical or practical insight.

The authors rely on the Kushner and Yin approach, which, although mathematically elegant, has a significant drawback: it depends on assumptions that are notably difficult to verify. For example, Theorem 5.15 includes the assumption that “there exists a compact set in the domain of attraction of \( A \) that \( \{z_k\}_{k \geq 0} \) visits infinitely often.” However, the practicality of checking this condition is questionable. For dissipative systems with Lyapunov functions, more robust and accessible conditions are typically available. For instance, Benaïm’s 2006 work on the dynamics of stochastic approximation provides an alternative perspective with less restrictive assumptions, and the work by Andrieu, Moulines, and Priouret (2005) presents stability criteria that are generally easier to validate. Both of these references suggest that a more flexible framework is possible and may have been preferable in analyzing the convergence behavior.


See Benaïm, M. (2006). Dynamics of stochastic approximation algorithms. In Seminaire de probabilites XXXIII (pp. 1-68). Berlin, Heidelberg: Springer Berlin Heidelberg.
- Andrieu, C., Moulines, É., & Priouret, P. (2005). Stability of stochastic approximation under verifiable conditions. SIAM Journal on control and optimization, 44(1), 283-312. 

### Questions
- How do you check in pratice Assumption 1-iii). Give a clear and easy to check criterion (based a.g. on Sard's theorem)
- How do you check the conditions of Theorem 5.15

### Soundness
3

### Presentation
4

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
This paper shows the almost sure convergence of a class of stochastic Hamiltonian descent methods, including gradient normalization and soft clipping algorithms, under three different set of assumptions which provide validity of the conclusions to a wide range of settings. The proof relies on the typical argument followed in dynamic systems and control theory, which is to: (1) find a suitable Lyapunov function (in this case the Hamiltonian of the system); and (2) invoke LaSalle's Invariance theorem to establish the convergence to a (isolated) stationary point the (non-convex) objective function.

Typo: Line 112 should read "term" instead of "tern"

### Strengths
The paper is well written, structured, and thus easy to follow. It contributes to the theoretical understanding of SGD with momentum under gradient normalization and soft clipping. 

Although I didn't read every proof in extreme detail, I believe the formal arguments and results are correct. 

Minor detail: Since the authors initially present the formulation of the nearly Hamiltonian system in continuous time (see eq. (8)), perhaps the choice of the Lyapunov function in the proof of Theorem 5.7 could be motivated in that context, showing that: $\dot V = -\gamma\||\nabla\varphi\||^2 \leq 0.$

### Weaknesses
The main issue I have with the paper is that, because the proof strategy closely follows the approach developed by Kushner and Yin (2003) (cf. Section 5 and Theorem 5.2.1), it is not immediately clear why their proof cannot be directly invoked after showing that the sequence of iterates is finite almost surely. For example, Lemma A.3 can in fact be found in the first part of Theorem 5.2.1 but this is not explicitly mentioned by the authors. Could the authors explicitly discuss how their proof extends or differs from Kushner and Yin (2003), for example by including a paragraph comparing their approach to Kushner and Yin's and highlighting any novel elements or modifications needed for the Hamiltonian specific setting.



### Questions
* Could the authors more clearly explain how their approach seems to extend Kushner and Yin (2003)? This would allow the reader to better evaluate the novel elements needed in the proof almost sure convergence. 
* This next question is not related to the perceived weakness of the paper but more for a deeper understanding of the results. Because the kinetic energy function is assumed to be differentiable, almost sure convergence cannot be concluded for clipping as studied by Zhang et. al. (2020) in expectation. Could the authors explain the need of the differentiability assumption, and why working with the sub-gradients of $\varphi$ is not possible?

### Soundness
3

### Presentation
3

### Contribution
2
