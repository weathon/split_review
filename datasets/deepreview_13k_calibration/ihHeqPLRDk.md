# Sinc Kolmogorov-Arnold Network and Its Applications on Physics-informed Neural Networks

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 5, 3, 6

## Abstract
In this paper, we propose to use Sinc interpolation in the context of Kolmogorov-Arnold Networks, neural networks with learnable activation functions, which recently gained attention as alternatives to multilayer perceptron. Many different function representations have already been tried, but we show that Sinc interpolation proposes a viable alternative, since it is known in numerical analysis to represent well both smooth functions and functions with singularities. This is important not only for function approximation but also for the solutions of partial differential equations with physics-informed neural networks. Through a series of experiments, we show that SincKANs provide better results in almost all of the examples we have considered.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper presents a new model that applies sinc interpolation to the previously proposed KAN model. It discusses the advantages of the proposed model for function fitting and solving PDEs in a Physics-informed manner.

### Strengths
The study explores how the recently developed KAN model can better handle singular problems from the perspective of Physics-Informed Neural Networks (PINNs).

### Weaknesses
I believe the main goal of this paper is to improve existing PINN-based models through the development of sincKAN. However, as shown in Table 2, it's unclear if sincKAN demonstrates convincingly better performance than other existing models across various PDE problems. Clearly, as mentioned in the PI-KAN model, there are specific advantages and disadvantages to using KAN for solving PDEs, such as computational cost or training speed. If sincKAN does not consistently outperform across all datasets, as seen in Table 2, what advantages does sincKAN offer over using standard MLP or modified MLP to train Physics-informed Loss? While sincKAN appears to perform better on boundary layer problems, as shown in Table 3, the paper’s title and focus could have been more aligned with boundary layer issues if that is its primary strength. Additionally, are there recent studies related to PINNs specifically aimed at solving boundary layer problems? What would happen if epsilon increased to a larger value, such as 10^8? It might also help to include a basic explanation of KAN’s underlying mechanism for readers unfamiliar with the model, as certain concepts could be difficult to grasp without this context.

### Questions
* What exactly is f(jh) in equation (6)? Is it simply the value of f at jh? Is equation (6) interpolating f(x) using those values? If so, do we need to know those values precisely to approximate f(x) with this formulation?
* Could other problems with singularities be tested? Does the proposed method also show significant advantages and accurately approximate solutions in all cases where singular phenomena appear? Could it be applied to other boundary layer problems or higher-dimensional problems beyond two dimensions?
* For line 140, it might be better to use the \paragraph function for terms like “Convergence theorem” or “On a general interval (a, b)” to save space.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes KANs with sinc function as basis to represent univariate function, to which they refer as sincKan. They first discuss about the sinc function and its convergence properties and then extend it such that it becomes a viable and practical workhorse in the context of KANs. Equation 14 clarifies their contributions, namely, 1) choosing step size without the knowledge of function f (by using different h values, larger and smaller than the optimal one), 2) coordinate transformation (a composition of transformation from finite to infinite domain and a normalizing transformation), and 3) enforcing exponential decay (by considering g-f instead of f with a linear g). First property manifests itself in use of ci,j and hj, second one is hidden in $\gamma^{-1}$, and the third property is $c1x+c2$. They use both function approximation and solution of PDEs (similar to PINNs, which enforces the solution as soft constraint in the loss function) as numerical experiments and show lower error in most cases compared to relevant baselines.

### Strengths
The paper and idea are well-written. It is clear what authors try to implement and they are also rigor in deriving equation 14, which is a foundation for their sincKAN network. 
The choice of boundary layer example is smart and shows the good performance of sincKAN in the presence of singularities (specially pronounced in large epsilon (lower width of boundary layer or larger Reynolds, which is more complicated).

### Weaknesses
The contribution of this paper seems limited to me and I hope authors clarify this in the rebuttal period. 
Using more advanced basis functions for KANs is a meaningful research direction but currently it seems to me no single method can be seen as the best solution for all PDEs. In fact sincKAN may have better performance in the presence of singularities but may not be the best option otherwise. In the current version, I can't derive a concrete conclusion as which version of KANs to use for what type of problems (within PDE domain or even beyond). In fact, in Table 2, sincKAN is not the best option in some cases.
In an analogy to more conventional deep learning papers, the use of Relu activation functions with CNN enable them to achieve very good performance: it helped with vanishing gradient problem, it helped with efficiency of implementations, and also empirical success (for instance AlexNet). sincKAN does not seem to be such an abrupt idea. The theorems provided do not really guarantee the performance (specially considering the fact that authors use a range of step sizes instead of the optimal value due to practical reasons). 
In this vein, authors discuss how sincKAN can help with spectral bias, but not much discussion is done on other issues for PINNs e.g. issue for causality (which makes them problematic in chaotic PDEs--which by the way is good to add to examples), and many other issues (like plateauing loss, etc.).
Finally, in "vanilla" KANs paper there are some arguments on the advantage of using B-splines, which enable them the use of grid related tricks including grid extension and grid update tricks. In other variants also there are some interesting merits; it's hard to say sincKAN still has all this merits and in addition to them provide more robustness in the case of singularities.

### Questions
Can sincKAN help with some pathological issues of PINNs? Would be interesting to explore; see for example Wang, S., Teng, Y., and Perdikaris, P. Understanding and Mitigating Gradient Flow Pathologies in Physics- Informed Neural Networks. SIAM Journal on Scientific Computing, 43(5):A3055–A3081, 2021a. or Wang, S., Sankaran, S., and Perdikaris, P. Respecting causal- ity is all you need for training physics-informed neural networks. arXiv preprint arXiv:2203.07404, 2022a. or the more recent paper Challenges in Training PINNs: A Loss Landscape Perspective by Rathore et al.

I still don't see the real advantages of theorems 1 and 2, since the optimal value of step is not uses in sincKAN. Also, I advise authors formally add another theorem to Coordinate transformation section to prove for the composition, the theory still holds (it should be straightforward). Also, if a function needs to be Hardy, does that mean the guarantees are only valid for differentiable functions f? It would be good to discuss the implementations.

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
The paper builds upon recently proposed architecture KANs that are meant to be more parameter efficient than MLPs and provide additional benefits like interpretability. The authors replace the splines in KANs with sinc to propose SincKAN. Furthermore, the paper presents experiments in PINNs (using KANs) to demonstrate potential benefits of SincKAN.

### Strengths
1. Applying sinc to replace splines in KAN is a novel approach. Additionally, the authors address the practical challenges of selecting step sizes using multiple step sizes.

### Weaknesses
1. The PDEs selected for the experiments are generally unsuitable to demonstrate the benefits of PIKANs. The chosen problems are extremely small and these problems can be solved using any numerical PDE solver. Since PINNs / PIKANs don't provide any practical advantage in small problems, it would be interesting to see if the benefits proposed here can be demonstrated in real problems.



### Questions
1. For MLP architectures, how were the architectures chosen? Since the problems are small and toy-ish, over-parameterization may cause a higher final loss.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The work proposes using Sinc interpolations replace the splines used within recently popularised Kolomogorov Arnold Networks (KANs). The work outlines foundational background required of Sinc interpolation and demonstrates some nice properties of Sinc interpolation on some specific benchmarks. It then outlines certain properties that must hold for effective Sinc interpolation and incorporates these within its KAN framework. Benchmarks are performed against against baselines comprising of two different multilayer perceptron architectures, and two other KAN architectures. These experiments encompass a range of function approximation tasks for manufactured functions, and physics-informed tasks.

### Strengths
1. KANs are recent and might have much scope for optimisation. The interpolation scheme in KANs seems to be an important point to consider in practical use, so it is good that the authors draw attention to this.
2. Given the recency of KANs, the study provides more independent comparisons between KANs and MLPs which might be of interest to the wider community.
3. The authors do not straightforwardly substitute Sinc interpolants into the KAN architecture, but properly consider its principled application in terms of optimal step sizes, required exponential decay of the approximated function and how to circumvent this etc.

### Weaknesses
1. The manufactured solutions used in the learning for approximation secion (3.1) are arbitrary and seemingly not very relevant to real world applications. They are both manufactured, and all are one dimensional.
2. While the performance of SincKANs is good in physics-informed settings, it feels like some scrutiny of the results is missing. There are many reasons why a physics-informed problem might fail to converge. It might not be that the reason for better performance in a physics-informed problem is a better architecture. The benchmarks used for function approximation, while now including higher dimensional cases, still consist of functions with closed-form solutions that are easily approximated by Sinc functions. This limits the scope of the analysis and does not adequately demonstrate the practical advantages of SincKANs over other methods for more complex, real-world functions.

### Questions
Question:
1. Can't one use a Sinc interpolator directly for all the function approximation tasks?

Sugestions:
1. The experiments of section 3.1 do not seem so relevant for practical applications. It seems that what might be most interesting would be to take a selection of complicated PDE/ODE data (using any off the shelf differential equation solver) and use these instead. This would demonstrate the value of SincKANs in practical circumstances, and in situations of more than 1 dimension. As it stands, these benchmarks feel artificial and irrelevant for real world application.
2. More scrutiny of the physics-informed losses would be beneficial. Some plots of solutions and errors across the poorer performing methods might help understand why they are performing badly. Is it that boundary conditions are not being adhered to? Maybe there are regions of high PDE loss in the resulting solution? Perhaps small changes (e.g. weighing boundary conditions effectively) might lead to improved performance.

### Soundness
3

### Presentation
2

### Contribution
2
