# Refined Generalization Analysis of the Deep Ritz Method and Physics-Informed Neural Networks

- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 3, 5, 5

## Abstract
In this paper, we present refined generalization bounds for the Deep Ritz Method (DRM) and Physics-Informed Neural Networks (PINNs). For the DRM, we focus on two prototype elliptic PDEs: Poisson equation and static Schrödinger equation on the $d$-dimensional unit hypercube with the Neumann boundary condition. And sharper generalization bounds are derived based on the localization techniques under the assumptions that the exact solutions of the PDEs lie in the Barron spaces or the general Sobolev spaces. For the PINNs, we investigate the general linear second elliptic PDEs with Dirichlet boundary condition via the local Rademacher complexity in the multi-task learning.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Authors utilize the localized analysis to refine generalization bounds for both the Deep Ritz Method (DRM) and Physics-Informed Neural Networks (PINNs). For the DRM, authors provide theoretical results for the Poisson and Schrödinger equations. For PINN, the theoretical results obtained for the linear second order elliptic equation.

### Strengths
* The proposed theoretical results show that the function $\mathcal{B}^2$ can be well approximated in the $H^1$ norm by MLP (two hidden layers with ReLU as the activation function) network with controlled weights.  
* For the DRM, authors obtain more precise generalization bounds for the Poisson and Schrödinger equations with Neumann boundary condition, irrespective of whether the solutions are in Barron spaces or Sobolev spaces.
* For the PINNs, authors provide a generalization error for PINN loss of the linear second order elliptic equation in the $H^{1/2}$ norm. 
* Theoretical estimations for both methods with neural networks are correct for both cases if the PDE solution is in the Barron space or the Sobolev space.

### Weaknesses
 * Considering PDEs(the Poisson equation and the static Schrödinger equation with Neumann boundary condition) defined on d-dimensional cube are simple and not interested in community. Is it possible to extend the list of PDEs where proposed theory can be used?
* It will be good for understanding to add some numerical experiments.

### Questions
See the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper theoretically analyzes the generalization error of two prominent deep learning methods for solving PDEs: the Deep Ritz method and PINNs. The analysis is conducted on simple second-order linear PDEs, and under certain assumptions, they obtain tighter bounds compared to previous studies. However, the assumptions made are somewhat impractical, and the results raise questions about the significance of this research beyond its mathematical implications and what it contributes to the field of deep learning.

### Strengths
The authors have performed a mathematical analysis of the Deep Ritz method and PINNs, which continue to attract considerable interest. This mathematical analysis can aid in understanding the characteristics of the models.

### Weaknesses
A robust mathematical analysis can be more powerful than empirical observations. However, there are several areas of concern in this study:

1.	What is the intention behind studying the two methods using different mathematical tools for different PDEs? There is no connection drawn between the two methods within the paper, which leads to confusion about the main message of the study.

2.	Due to the complexity of deep learning models, it is a natural approach to start the analysis with simpler scenarios. However, the assumption that the solutions of the PDEs lie within the Barron space is too strong. The Barron space is specifically designed for functions that are best approximated by two-layer MLPs and is suitable for analyzing two-layer neural network structures, but it is too narrow to represent the space of PDE solutions. Furthermore, the paper does not adequately justify why the solutions to the specific PDEs considered would naturally reside in such a constrained space.

3.	The primary goal of Deep Ritz and PINNs is not just to minimize the loss but to find the solution to PDEs. Thus, instead of focusing on how much a minimizer of the empirical loss reduces the expectation loss, the analysis should focus on how close the empirical loss minimizer is to the true solution. It is crucial because both methods include unbounded derivative operators in their loss functions, meaning that a small difference in loss values does not necessarily imply that the functions are close. Although the paper briefly addresses this in equations (16) and (30), it does so under very restrictive assumptions, casting doubt on the implications of the results. Specifically, the analysis does not sufficiently address the impact of these unbounded operators on the stability and convergence of the methods in practical scenarios. The paper should provide a more rigorous analysis of the relationship between the loss minimization and the convergence to the true PDE solution, especially when dealing with unbounded operators.

4.	While the theoretical analysis uses the $ReLU^k$ activation function (also known as RePU) for convenience, this also has limitations. The theory is developed in the context of simple two-layer networks, but practical implementations often involve deeper networks, where the power of the RePU increases with depth, leading to floating-point precision issues. This limitation should be acknowledged in the paper. Moreover, the analysis does not discuss how the theoretical results might change with different activation functions, which is a critical aspect given the wide variety of activation functions used in practice.
5.	The PDEs considered in this study are too simple. Such simple PDEs can be solved much faster and more accurately using classical methods such as FEM, FDM, Discrete Galerkin, and FVM. Deep learning-based methods should focus on more complex PDEs or inverse problems. While it is important to start from a mathematical understanding of simpler problems, it is also important to recognize that these methods are not just mathematical objects. Research in this area must integrate PDEs, classical numerical methods, and deep learning, rather than excluding any one aspect. Furthermore, the significance of this research in the field of deep learning remains unclear beyond its mathematical implications.

6.	Eq (16) combines the results of Prop 1 and Thm 3, but it appears to omit the Poincaré constant from Prop 1, which is dimension-dependent.


7.	Limitations are not addressed in the paper.

### Questions
See weakness above.

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper derived new generalization bounds for solving elliptic Partial Differential Equations (PDEs) via two deep learning based methods - the Deep Ritz Method (DRM) and Physics Informed Neural Network (PINN). For DRM, this paper obtained generalization bounds for the Poisson equation with Neuman boundary condition when the solution is in either some Barron space or some Sobolev space. For PINN, this paper considered linear second order elliptic PDEs with Dirichlet boundary condition. By utilizing results from statistical learning theory under the Multi-Task Learning (MTL) framework, the authors also obtained generalization bounds for PINN when the solution is in some Barron space or some Sobolev space. As a side product of the main results, this paper also obtained better rates of approximating functions in certain Barron spaces via two-layer neural networks.

### Strengths
1. This paper is presented in a clear way for readers to follow. Also, a thorough review of related work on variants of Rademacher complexity done by researchers from the statistical learning theory community is included. Proofs of essential lemmas are also presented to ensure the rigorousness of the entire manuscript. 

2. In terms of specific contribution, this paper obtained finer bounds for approximating certain Barron functions via two layer neural networks, which lead to better generalization bounds on solving elliptic PDEs via DRM and PINN under the circumstances when the true solution is in some Barron space compared to existing work [1].

### Weaknesses
1. The reviewer's main concern is that some contributions mentioned in this article are not described in a clear way. Specifically, the reviewer thinks that it might be worthwhile for the authors to include a separate paragraph to compare the contributions made in this manuscript and existing work [2]. For specific questions about the main contributions and novelty of this paper compared to [2], the authors may refer to the first four bulletin points in the "Questions" section below. The lack of clarity regarding the specific advantages over [2] makes it difficult to assess the true impact of this work, especially given that [2] already provides a comprehensive analysis of generalization bounds for similar problems. The current presentation does not adequately highlight the unique aspects of the proposed approach, and a more detailed comparison is needed to justify the claims of improved performance.

2. Regarding presentation of this paper, there are a few grammatic issues that can be potentially resolved. For instance, the sentence from line 40 to 41 can be possibly rephrased as "The Deep Ritz method, on the other hand, incorporates the variational formulation into training the neural networks due to the widespread use of the variational formulation in traditional methods". Furthermore, the organization of the "Related Works" section feels somewhat disjointed, making it challenging for the reader to grasp the paper's core contributions and how they relate to the existing literature. The flow of ideas could be improved by providing a more cohesive narrative that connects the different strands of research discussed.

3. Given that solving PDEs via machine learning based methods is now a popular field, the authors might consider performing a brief literature review by citing a few important work (other than DRM and PINN) [3-9] in the first part of subsection 1.1 (Related Works) for the sake of completeness. One may refer to the related works section in [2] and [10] as possible examples. The absence of a broader context limits the reader's ability to fully appreciate the significance of this work within the larger landscape of machine learning for PDEs. Including a wider range of relevant studies would help to position the paper more effectively and demonstrate a thorough understanding of the field.

### Questions
1. One thing the authors emphasized as a contribution is that this manuscript derived a generalization bound for the Poisson equation compared to [2]. However, it seems to the reviewer that Proposition 1, which provides a variational formulation of Poisson equation, actually requires extra assumption ($\int_{\Omega}f dx = 0$) compared to [2]. Hence, the review wonders whether this is a fair comparison and would appreciates it if the authors can elaborate on why they think the main reason is actually because the expectation of empirical loss is not equal to the population loss under the variational formulation (line 111-112, line 129-130). 

2. In Remark 2, the authors state that the convergence rate associated with the DRM gets improved from $n^{-\frac{2k-2}{d+2k-4}}$ to $n^{-\frac{2k-2}{d+2k-2}}$, which seems to be incorrect as the second rate is larger than the first one. Also, the same rate (up to $\log n$ factors) has also been achieved in [2] via the peeling method. Therefore, the reviewer would appreciate it if the author could specify the major novelty/contribution of this paper for the DRM. 

3. For the generalization bounds on PINN, the authors claimed that results presented in Section 4 are more general compared to [2] as this paper doesn't require strong convexity of the objective function. However, it seems to the reviewer that this cannot be claimed as a major novelty as Lemma 17 serves a similar role as Theorem B.2 in [2] (Also, here the authors still need the strict elliptic condition). Furthermore, even though the convergence rate $n^{-\frac{2k-4}{d+2k-4}}$ of PINN attained here is the same as that of [2], the norm used for measuring the error seems to be different - (30) implies that the norm used here is the $H^{\frac{1}{2}}$ norm, while [2] uses the $H^1$ norm. This will for sure influence the convergence rate and statistical optimality, so the reviewer would appreciate it if the authors could provide some intuition on the change of norms here. 

4. Given that [2] provides not only upper bounds but also informational theoretical lower bounds on the expected estimation error, which certifies statistical optimality under certain regimes, would it be possible for the authors to provide some intuition on the lower bounds for the cases when the true solution is in some Barron spaces? Essentially speaking, are the bounds presented in (13) and (27) statistically optimal? 

5. In the abstract and introduction (line 15-16 and line 125-127), the authors claimed that sharper generalization bounds are derived for solving both the Poisson equation and the Schrödinger equation via the DRM. However, it seems that Theorem 3 in Section 2 only contains results for the Poisson equation?

References: 

[1] Lu, Y., Lu, J. and Wang, M., 2021, July. A priori generalization analysis of the deep Ritz method for solving high dimensional elliptic partial differential equations. In Conference on learning theory (pp. 3196-3241). PMLR.

[2] Lu, Y., Chen, H., Lu, J., Ying, L. and Blanchet, J., 2021. Machine learning for elliptic pdes: Fast rate generalization bound, neural scaling law and minimax optimality. In International Conference on Learning Representations, 2022. URL https://openreview.net/forum?id=mhYUBYNoGz.

[3] Sirignano, J. and Spiliopoulos, K., 2018. DGM: A deep learning algorithm for solving partial differential equations. Journal of computational physics, 375, pp.1339-1364.

[4] Han, J., Jentzen, A. and E, W., 2018. Solving high-dimensional partial differential equations using deep learning. Proceedings of the National Academy of Sciences, 115(34), pp.8505-8510.

[5] Khoo, Y., Lu, J. and Ying, L., 2021. Solving parametric PDE problems with artificial neural networks. European Journal of Applied Mathematics, 32(3), pp.421-435.

[6] Zang, Y., Bao, G., Ye, X. and Zhou, H., 2020. Weak adversarial networks for high-dimensional partial differential equations. Journal of Computational Physics, 411, p.109409.

[7] Chen, Y., Hosseini, B., Owhadi, H. and Stuart, A.M., 2021. Solving and learning nonlinear PDEs with Gaussian processes. Journal of Computational Physics, 447, p.110668.

[8] Li, Z., Kovachki, N., Azizzadenesheli, K., Liu, B., Bhattacharya, K., Stuart, A. and Anandkumar, A., 2020. Fourier neural operator for parametric partial differential equations. arXiv preprint arXiv:2010.08895.

[9] Lu, L., Jin, P., Pang, G., Zhang, Z. and Karniadakis, G.E., 2021. Learning nonlinear operators via DeepONet based on the universal approximation theorem of operators. Nature machine intelligence, 3(3), pp.218-229.

[10] Lu, Y., Blanchet, J. and Ying, L., 2022. Sobolev acceleration and statistical optimality for learning elliptic equations via gradient descent. Advances in Neural Information Processing Systems, 35, pp.33233-33247.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this paper, the authors derive refined generalization bounds for the Deep Ritz Method (DRM) and Physics-Informed Neural Networks (PINNs), building on the work of Lu et al. (2021c in the manuscript).  The authors derive sharper bounds for the Poisson and Scrodinger's equations, and then present their modified framework within a multi-task learning perspective.

### Strengths
The strength of the paper is that the authors present mathematical analysis of physics-informed neural networks and similar (related) methods. The author's work fits within the current push for developing and growing the mathematical foundations of PINNs and related ideas.

### Weaknesses
The reviewer did not find any mathematical errors in the work, but was surprised that the authors did not point to the other mathematical works that exist (in the field).  The most well-known on the mathematical side would be Weinan E and collaborators:

https://link.springer.com/article/10.1007/s00365-021-09549-y

Weinan and others (some of which the authors reference part of their work, like: 
https://arxiv.org/abs/2106.07539).

People have since built on Weinan's ideas:  A Deep Double Ritz Method (D
RM) for solving Partial Differential Equations using Neural Networks by Uriiarte et al., CMAME 2023.





### Questions
+ How does the analysis differ (substantially) from the work of Weinan E (paper above) and subsequent papers? In particular, when comparing the author's theoretical framework or results to Weinan's section 2 or the CMAME Section 3, can you highlight how your results/conclusions are different and what changes your work makes in terms of the results.

+ Clarify how the author's work is distinct from the CMAME paper, as an 'extension' of the Lu and Weinan E ideas?  Although not identical, can the authorrs provide details on how their work is novel and how it leads to improved or different results over those of Weinan E and/or the CMAME paper.

+ Please compare the framework with the multi-head (multitask) work of Karniadakis :  https://www.semanticscholar.org/paper/L-HYDRA%3A-Multi-Head-Physics-Informed-Neural-Zou-Karniadakis/ec7289f0cb03f0987a0f84391de278f83654bb09   (either argue how they are different or show numerical results).

### Soundness
3

### Presentation
3

### Contribution
2
