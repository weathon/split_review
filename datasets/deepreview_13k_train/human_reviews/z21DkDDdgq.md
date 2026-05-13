# Integral Performance Approximation for Continuous-Time Reinforcement Learning Control

- Decision: Accept
- Scores: 8, 8, 5

## Abstract
We introduce integral performance approximation (IPA), a new continuous-time reinforcement learning (CT-RL) control method. It leverages an affine nonlinear dynamic model, which partially captures the dynamics of the physical environment, alongside state-action trajectory data to enable optimal control with great data efficiency and robust control performance. Utilizing Kleinman algorithm structures allows IPA to provide theoretical guarantees of learning convergence, solution optimality, and closed-loop stability. Furthermore, we demonstrate the effectiveness of IPA on three CT-RL environments including hypersonic vehicle (HSV) control, which has additional challenges caused by unstable and nonminimum phase dynamics. As a result, we demonstrate that the IPA method leads to new, SOTA control design and performance in CT-RL.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces integral performance approximation (IPA) for continuous-time model-based reinforcement learning control of control-affine nonlinear systems.

### Strengths
The paper is well-written, the contributions are clear and of significant importance for solving continuous-time optimal control problems. The simulation and ablation studies are extensive and make a compelling case for the developed controller.

### Weaknesses
My main concerns are regarding the general mathematical rigor in the theoretical results. Specifically, there are a lot of linearized approximations throughout the paper, which by itself is not necessarily problematic. However, then one would expect the unknown approximation error to be accounted for in the analysis with some appropriate bounds. Instead, there are a lot of $\approx$ relations in the paper (e.g., (14), (15), (30) etc.) without accounting for the errors.  Specifically, in Eq. (13), K_i is defined as $$\- \frac{\partial}{\partial x}\mu_i (x)|_{x=0}$$, and then it is said 
$$\mu_i \approx -K_i x.$$
This linearization is foundational to the entire paper. At that point one can also linearize the dynamic model itself, i.e., 
$$f(x)+g(x)u \approx Ax+Bu$$ and then apply the entire development accordingly. This makes me wonder if the development is appropriate for the nonlinear system in Eq. (1) like it is claimed.
Instead of writing $\mu_i \approx -K_i x,$ it would be more appropriate to write $\mu_i = -K_i x + O(||x||^2)$. The linearization error would then grow quadratically with the states, but for the region $||x||\leq r$, there exists some constant $c_1$ such that can be bounded by $ O(||x||^2) \leq c_1 r^2$. Similar analysis needs to be performed for all of the other approximations in the paper to achieve a local stability result with robustness to small perturbations. The way the paper stands now, the analysis is valid only in an infinitesimal neighborhood of the origin.

Besides, the literature review surrounding CT-RL and ADP methods is sparse. In Appendix M, the following vague comment is made about ADP methods:

 "As a result of ADP’s theoretical frameworks in adaptive and optimal control, Lyapunov arguments are available to prove qualitative properties including weight convergence and closed-loop stability results. However, the results require restrictive theoretical assumptions which are difficult to satisfy for even simple academic examples, and as a result these methods exhibit empirical issues." 

However, it is not specified what theoretical assumptions are restrictive and difficult to satisfy. Besides the literature and ablation study on ADP is mostly focused on the old result by Vamvoudakis and Lewis (2010). Besides, a lot of further development has happened after this classical work. For example, see the following works and references citing them/therein:

Kamalapurkar, R., Walters, P. and Dixon, W.E., 2016. Model-based reinforcement learning for approximate optimal regulation. Automatica, 64, pp.94-104.

Vamvoudakis, K.G., 2017. Q-learning for continuous-time linear systems: A model-free infinite horizon optimal control approach. Systems & Control Letters, 100, pp.14-20.
  
In Appendix F, the authors mention "Many SOTA ADP CT-RL algorithms require the persistence of excitation (PE) condition in proofs
of algorithm properties". There are many newer results which relax the PE condition with initial/interval/finite-time excitation conditions. See the following references for example:

Jha, S.K., Roy, S.B. and Bhasin, S., 2019. Initial excitation-based iterative algorithm for approximate optimal control of completely unknown LTI systems. IEEE Transactions on Automatic Control, 64(12), pp.5230-5237.

Yang, Y., Pan, Y., Xu, C.Z. and Wunsch, D.C., 2022. Hamiltonian-driven adaptive dynamic programming with efficient experience replay. IEEE Transactions on Neural Networks and Learning Systems.

The authors can discuss these newer results that relax the PE condition and analyze how they relate to or could potentially improve the proposed IPA method.

### Questions
1. Does the state-dependent part of the cost need to be quadratic? Specifically, can the $x^T Q x$ term be generalized to some positive semi-definite function Q(x). I can understand the challenges generalizing so for the $u^T R u$, but $x^T Q x$  must be easy if linearizations are being used in the integral approximation anyway.

2. Does the linearization in (13) need to be necessarily around x=0? What would be difficult about constructing a function $K_i(x)=-\frac{\partial}{\partial x}\mu_i (x)$? across a range of values of x, similar to gain scheduling methods?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces Integral Performance Approximation (IPA), a new method for continuous-time reinforcement learning (CT-RL) control. IPA utilizes an affine nonlinear dynamic model that partially captures the environment's dynamics, alongside state-action trajectory data, to enable highly data-efficient and robust control. The approach incorporates structures from the Kleinman algorithm to ensure theoretical guarantees for learning convergence, solution optimality, and closed-loop stability. The effectiveness of IPA is demonstrated across three CT-RL environments, including hypersonic vehicle (HSV) control, which presents additional challenges due to unstable and non-minimum phase dynamics.

### Strengths
The paper introduces a CT-RL method, IPA CT-RL, which leverages an affine nonlinear dynamic model and quadratic cost structure for data-efficient, robust control. It provides theoretical guarantees for convergence, optimality, and stability, validated through extensive evaluations. Finally, it demonstrates IPA CT-RL's successful application to HSV control.

### Weaknesses
However, there are still some aspects of this paper that require clarification:

1. The paper mentions several SOTA methods that are not restricted to control-affine systems, such as Yildiz et al. (2021). However, the authors did not include these methods in their simulations for comparison. Could the authors explain the reasoning behind this choice?

2. The authors briefly mention the discretization of continuous-time environments in Yildiz et al. (2021), suggesting that this process could lead to significant numerical issues for real-world systems. However, their proposed method also relies on discrete data points when performing integration, which could introduce discretization errors. A previous study [1] has analyzed this issue in detail. I believe the authors should at least discuss the impact of discretization error in their approach.

3. The authors suggest that HSV represents a SOTA environment, but it still appears to be relatively low-dimensional. It’s unclear why their approach cannot scale to higher dimensions, especially since the method in Yildiz et al. (2021) seems capable of handling more complex systems. The authors should discuss the limitations that might prevent their approach from scaling up.

4. I am unclear about the theoretical advantage of the IPA method. Is this benefit primarily due to a linearization structure or another feature? I recommend that the authors provide a clear explanation of this through a example. Additionally, it’s unclear if IPA applies effectively to all control-affine systems or only to those with high linearity. The systems simulated by the authors do not exhibit a high degree of nonlinearity, so clarification here would be helpful.

### Questions
All the questions are listed in the weakness part.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a continuous-time reinforcement learning control method. The critic network design is novel. However, the theoretical analysis is questionable, which is difficult to follow. Simulation results on three optimal control tasks show that the proposed method outperforms SOTA methods.

### Strengths
(1) Extensive simulations are conducted.

(2) The proposed method is robust to model uncertainty empirically.

### Weaknesses
(1) The proposed method is model-based, which only considers affine nonlinear systems.

(2) There are some theoretical issues in the paper.

(3) The advantage of the proposed method in improving learning robustness is not analyzed theoretically.

### Questions
(1) It is suggested to introduce the value function $V$ (formula (7)) before Section 2.1. In addition, please use different notations to represent the value function (e.g. $V$) and the critic network (e.g. $\hat V$). In this paper, the authors sometimes replace the value function with the critic network in their theoretical analysis.

(2) In (5), the notation $V$ in the function $H$ should be $V^*$.

(3) In Fig. 1, the HJB equation is unrelated to the CT temporal difference equation. 

(4) In (13), why do you linearize the controller $\mu (x)$ at $x=0$? For states which are far away from the origin, the linearized function could not approximate $\mu (x)$ accurately.

(5) The reviewers are confused with the content in Appendix C, as formulas (16) and (17) can be obtained directly based on the Bellman equation (8), the critic network (9), and linearized controller (13).

(6) The proof of Theorem 3.1 is hard to follow. It seems the authors overlook that the system considered in this paper is affine nonlinear.

(7) In appendix F, the authors should explain clearly that how the reference command input and the error influence the control policy, which could be an important trick in improving the learning performance of the proposed method.

(8) Since the system is known, the authors are encouraged to further compare their method with some classic control methods which do not consider optimality. In addition, could the authors explain why the SOTA baselines are significantly sample-inefficient?

(9) Is it possible to discuss the learning robustness of the proposed method from a theoretical perspective?

### Soundness
2

### Presentation
3

### Contribution
2
