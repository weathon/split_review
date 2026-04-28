# SINGER: Stochastic Network Graph Evolving Operator for High Dimensional PDEs

- Decision: Accept
- Avg Score: 6.33
- Scores: 8, 6, 5

## Abstract
We present a novel framework, StochastIc Network Graph Evolving operatoR (SINGER), for learning the evolution operator of high-dimensional partial differential equations (PDEs). The framework uses a sub-network to approximate the solution at the initial time step and stochastically evolves the sub-network parameters over time by a graph neural network to approximate the solution at later time steps. The framework is designed to inherit the desirable properties of the parametric solution operator, including graph topology, semigroup, and stability, with a theoretical guarantee. Numerical experiments on 8 evolution PDEs of 5,10,15,20-dimensions show that our method outperforms existing baselines in almost all cases (31 out of 32), and that our method generalizes well to unseen initial conditions, equation dimensions, sub-network width, and time steps.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
In this work the authors propose a stochastic graph neural network based framework for solving high dimension partial differential equations (PDE).  Neural PDE solvers that perform well in low-dimensional settings do not generalize to high-dimensional settings and hence require special attention. However, existing methods in the high dimension regime suffer from instability and do not generalize to different types of PDEs. To overcome these drawback, the authors propose the SINGER framework.

The SINGER model uses a GNN to approximate the solution of the PDE at the initial time step and then stochastically evolves the network parameters over time according to a GNN-driven ODE. This network is then used to approximate the solution at later time steps. The structure enables permutability of neurons within a layer, this enhances the models capability to generalize. To combat the issue of instability in the evolution process, SINGER introduces noise during the training step.  Further more, SINGER is designed to satisfy three key assumptions: graph topology, semigroup property and stability. The authors theoretically and empirically verify that their proposed framework satisfies these assumptions. Finally, SINGER is validated on 8 benchmark PDEs and its performance is compared with state-of-the-art methods.

### Strengths
1) The authors identify gaps in current literature and do a good job in motivating their research.

2) The contributions of their framework are explained clearly.

3) Theoretical analysis of stability, graph topology and semigroup property of SINGER

4) Computational results are positive

### Weaknesses
Section 3: The authors could do a better job in explaining what the 3 assumptions signify and why They are important for solving PDEs.

### Questions
(page 1) The 3 contributions of the paper can be rewritten clearly and explained in more detail. 

The authors can consider briefly explaining their theoretical contributions earlier in the paper.

(Table 3) Why not replace 'ours' with SINGER

### Soundness
3

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
3

### Summary
The paper proposes to solve time-dependent PDEs with a neural network model $U$that approximates the PDE solutions, where the neural network parameters are solutions to a system of stochastic differential equations with a drift term modeled by a Graph Neural Network on a graph induced by the architecture of $U$. 

While I am unfamiliar with the literature, I think the idea is interesting, especially with the mathematical reasons discussed in the paper. Upon careful inspection, it seems that this work extends NODE with stochastic noise and GNN architecture for the control vector $V$, where they used tools from Liu et al. 2019 (which is a paper that was rejected in ICLR 2020). My slight reservation with this work is due to my confusion as to why the paper Liu et al. 2019 paper has not been published and the work NODE also seems to be under review. However, these facts should not be the basis for rejecting this work. Based on my reading, the math part of this work is rather trivial and I am not against the paper for publication after the authors satisfactorily answer my following questions.

### Strengths
The central idea of using GNN for modeling the control seems to be novel.

### Weaknesses
This writing needs more clarifications.

Looking at Eq. (4), I assumed that the PDE that is to be solved is $u_t = F(U)$? Is there any restriction on $F$ (e.g., class of PDEs) for this approach to work well or to fail?

Can the authors clarify or give a detailed explanation on a sub-network of $U$? At this point, I am just reading the paper as if the entire architecture of $U$ forms a graph, and the parameters in the neural networks are denoted by $\theta_t$. How do you set $V,E$ a priori? If it is a fully connected network, does it mean $E$ is always 1 between any pair of vertices? How do you choose a sub-network of $U$? How critical is the performance under variations of sub-networks (what if you use the entire full network)?

How do you specify $N$ in (3)? I suspect you need to set it to $N^2>2L$ based on Theorem 1, where $L$ is the Lipschitz constant of $V$, which needs to be estimated in the optimization procedure?

I am not familiar with NODE or PINO, so it is hard for me to say that the comparison in numerical experiments is fair. How does this work compared to any other methods to solve such a high-dimensional PDEs that are cited in the references (such as DeepRitz, PINN).

As noted in p.6, the semigroup property depends on the random seed in the solution of SDEs. I think stating that the method satisfies the semigroup property in Table 1 is overselling. Upon inspecting the setup for the stability (Eq (6)) in the manuscript, the analysis is performed under the assumption that the same path of Brownian noise is used. I think one can avoid this assumption by stating a weaker result (convergence in distribution instead of almost surely convergence). If my conjecture is correct, there is more theoretical work to satisfy the semigroup property in a weaker sense instead of stating "approximately satisfied". Table 5 also suggests that the semigroup is weakened after training (unless I misunderstood the reported values in this table)?

Minor: Should $u_{\theta_t}$ below Eq. (4) be $U_{\theta_t}$?

### Questions
1. Looking at Eq. (4), I assumed that the PDE that is to be solved is $u_t = F(U)$? Is there any restriction on $F$ (e.g., class of PDEs) for this approach to work well or to fail? 
2. Can the authors clarify or give a detailed explanation on a sub-network of $U$? At this point, I am just reading the paper as if the entire architecture of $U$ forms a graph, and the parameters in the neural networks are denoted by $\theta_t$. How do you set $V,E$ a priori? If it is a fully connected network, does it mean $E$ is always 1 between any pair of vertices? How do you choose a sub-network of $U$? How critical is the performance under variations of sub-networks (what if you use the entire full network)?
3. How do you specify $N$ in (3)? I suspect you need to set it to $N^2>2L$ based on Theorem 1, where $L$ is the Lipschitz constant of $V$, which needs to be estimated in the optimization procedure?
4. I am not familiar with NODE or PINO, so it is hard for me to say that the comparison in numerical experiments is fair. How does this work compared to any other methods to solve such a high-dimensional PDEs that are cited in the references (such as DeepRitz, PINN).
5. As noted in p.6, the semigroup property depends on the random seed in the solution of SDEs. I think stating that the method satisfies the semigroup property in Table 1 is overselling. Upon inspecting the setup for the stability (Eq (6)) in the manuscript, the analysis is performed under the assumption that the same path of Brownian noise is used. I think one can avoid this assumption by stating a weaker result (convergence in distribution instead of almost surely convergence). If my conjecture is correct, there is more theoretical work to satisfy the semigroup property in a weaker sense instead of stating "approximately satisfied". Table 5 also suggests that the semigroup is weakened after training (unless I misunderstood the reported values in this table)?
6. Minor: Should $u_{\theta_t}$ below Eq. (4) be $U_{\theta_t}$?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors introduce StochastIc Network Graph Evolving operatoR (SINGER), a novel framework for learning the evolution operator of high-dimensional partial differential equations (PDEs). SINGER employs a sub-network to approximate the initial solution and stochastically evolves its parameters over time using a graph neural network to approximate later solutions. Designed to inherit key properties such as graph topology, semigroup properties, and stability, SINGER comes with theoretical guarantees of performance. Numerical experiments on eight PDEs across various dimensions show that SINGER outperforms existing methods in most cases and generalizes effectively to new conditions and parameters.

### Strengths
1. The presentation is clear and concise, and the problem is clearly illustrated. Although if I am correct, the network solves the PDEs at fixed collocation points, it would be great to point that out somewhere.
2. The empirical results are clear.
3. The theory of the method are sound and extensive.

### Weaknesses
1. While the empirical results cover most important PDE solvers, it does not compare with the SOTA methods, and merely compare to the vanilla ones. What's more, methods such as neural ordinary differential equations (NODEs) are not meant for solving partial differential equations, it seems a bit unfair to compare to them.
2. For instance, the proposed method resides in the realm of hypernetworks, it would be nice to see a hypernetwork of PINN or DeepONet.

### Questions
1. Why is it beneficial to have the stochasticity? Usually they hurts the surrogate performances, is there an ablation on the noise level to illustrate this issue?
2. The test cases are all very smooth PDEs, any reason why this is the case? Is it possible to either prove the ability on non-smooth PDEs or show with empirical results?

### Soundness
3

### Presentation
4

### Contribution
2
