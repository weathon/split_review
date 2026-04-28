# ANaGRAM: A Natural Gradient Relative to Adapted Model for efficient PINNs learning

- Decision: Accept
- Avg Score: 5.20
- Scores: 6, 8, 6, 3, 3

## Abstract
In the recent years, Physics Informed Neural Networks (PINNs) have received strong interest as a method to solve PDE driven systems, in particular for data assimilation purpose. This method is still in its infancy, with many shortcomings and failures that remain not properly understood.
In this paper we propose a natural gradient approach to PINNs which contributes to speed-up and improve the accuracy of the training.
Based on an  in depth analysis of the differential geometric structures of the problem, we come up with two distinct contributions:
(i) a new natural gradient algorithm that scales as $\min(P^2S, S^2P)$, where $P$ is the number of parameters, and $S$ the batch size;
(ii) a mathematically principled reformulation of the PINNs problem that allows the extension of natural gradient to it, with proved connections to Green's function theory.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper "ANaGRAM: A Natural Gradient Relative to Adapted Model for Efficient PINNs Learning" introduces an innovative natural gradient optimization algorithm tailored for Physics-Informed Neural Networks (PINNs). Named ANaGRAM, this approach leverages differential geometric perspectives to optimize PINNs, aiming to enhance computational efficiency and accuracy in solving Partial Differential Equations (PDEs) in a machine learning framework.

### Strengths
1.The paper's use of differential geometry to formulate a natural gradient specifically for PINNs counts as a theoretical contribution. By aligning gradient updates with the functional space geometry, ANaGRAM offers a alternative to gradient-based methods, potentially addressing some of the known limitations in PINN optimization.

2 NaGRAM's computational complexity, which scales favorably with parameter and batch sizes, is an improvement over traditional natural gradient methods.

3. Experimental results indicate that ANaGRAM consistently achieves lower error rates compared to baseline methods like E-NGD and standard optimizers (Adam, L-BFGS).

### Weaknesses
1. The current implementation of ANaGRAM requires manual tuning of hyperparameters, such as the cutoff factor for SVD. The selection of this cutoff, which determines the rank of the approximation to the Fisher information matrix, is critical for both performance and stability. A poorly chosen cutoff could lead to either an unstable optimization process or a significant loss of information, thus hindering the method's effectiveness. The lack of a principled method for setting this parameter is a practical limitation.

2. The choice of collocation points (batch points) is limited to heuristics in this study. The spatial distribution of these points significantly impacts the accuracy of the PINN solution. Using a uniform or random distribution, as is common practice, may not be optimal for all PDEs, especially those with highly localized features or boundary layers. An adaptive strategy that concentrates points in regions of high error or high gradient magnitude would likely improve the convergence rate and accuracy, but this is not addressed in the current work.

3. The results indicate that the efficacy of ANaGRAM may diminish for nonlinear differential operators, where the method's equivalence with traditional approaches is less certain. The theoretical justification for ANaGRAM relies on a local linearization of the problem, which may not hold for strongly nonlinear PDEs. This limitation raises questions about the general applicability of the method to a broader class of problems.

### Questions
1. Implementing an adaptive selection strategy for the SVD cutoff factor based on the eigenvalue spectrum could make the method easier to use.

2. Developing an adaptive method for selecting collocation points based on the geometry of the domain could improve convergence rates.

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
2

### Summary
The paper proposes a new algorithm -- ANaGRAM-- that is well suited for learning PDEs with boundary conditions. The algorithm makes use of a clever manipulation of natural gradient of Amari & Douglas. The natural gradient, PINN and some elements from differential geometry are introduced. The proposed algorithm can be interpreted as follows: compute the integration of the euclidean gradient using by "weighting" with the appropriate Green's function and use pseudo-inverse of the differential as a pre-conditioner (Theorem 1). Experiements show that ANaGRAM learns faster than Adam, GD, E-NGD across well-known low-dimensional PDEs.

### Strengths
The paper is very well written. The proposed method is elegant and well motivated from the theory perspective. Empirical results are well-done and show good evidence for the proposed ANaGRAM.

### Weaknesses
I quite like the paper. Even though I am not an expert of PINNs at all, I am guessing that this paper may be exciting for that community. I found the math well written, which may be not very common for an ICLR submission. 

Typos:
- Eq 2: $h_i \to h_p $
- line 147: "his" comp. cost $ \to $ "its" comp. cost
- line 199: maybe add what $\Delta_{\theta_r}$ means here (singular values) 

The performance of ANaGRAM is quite similar to E-NGD for Heat eqn and 5D Laplace eqn. ANaGRAM is faster by a tiny margin. I did not find a discussion of this in the paper. Can the authors comment on this? In particular, what would be the expected advantage of  ANaGRAM over E-NGS in words?

### Questions
I find the empirical investigations sufficient for this paper. It might be even better to have a high dimensional example. For example, would ANaGRAM still perform better than E-NGD when tested on 100 D Laplace eqn?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposed a natural gradient based optimizer called ANaGRAM for PINNs. The key algorithmic contribution of the paper includes a novel approach to discretize the natural gradient by connecting the natural gradient with a linear regression in L2 space, which is then combined with the fact that PINNs can be regarded as a least square regression to adapt the method for PINNs. A major theoretical contribution of this is showing that the natural gradient for PINNs is actually Green’s function under some conditions. 

In summary, this paper proposed a novel optimization approach which can be used to help improve the convergence of the usually ill-condition problems in PINNs.

### Strengths
This paper has an interesting and supportive theoretical results for their results.

### Weaknesses
1. There are many typos 126 il conditioned -> ill condition 186 hapens -> happens 201: writes -> write 274 quadraic....
2. The flow of the paper may be better by revisiting some parts. For example, at the end of the section 2, authors illustrate the relationship between the natural gradient and the linear regression problem. However, the section 3.1 has the title indicating the same thing. Maybe the end of section 2 can be moved to section 3.1, otherwise, I don't see the reason why section 3.1 has the current titles.
3. The experiments are not enough. Usually people also include Burgers, Schrodinge, etc.
4. The paper's main theoretical result is the equivalence of Green's function and natural gradient. It would be helpful to include some toy examples to justify this finding. The current presentation lacks concrete examples to demonstrate the practical implications of this equivalence, particularly in the context of PINN optimization. A more thorough exploration of this theoretical finding is needed to solidify its contribution.

### Questions
1. It's interesting that ANaGRAM usually has the largest variance among all methods, is there a reason for that? I was thinking it should have small variance since it's more well conditioned.

2. For some experiments, it seems the difference between different methods is more stark for L2 loss compared to test Loss. Any explanation for this?

3. Could you explain more about the relationship between NTK and equation 19 (line 223)?

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
This paper studies the natural gradient descent, which is theoretically and empirically believed to improve the convergence of training PINNs. Theoretical analysis on the natural gradient and training PINNs bridges connections on Green function theory.

### Strengths
(1) The natural gradient descent approach is theoretically sound, offering a promising solution for improving the convergence of regression problems and PINNs. Notably, while gradient descent may struggle with PINNs involving nonlinear PDEs, natural gradient descent effectively addresses this limitation.


(2) The paper's presentation is clear and well-structured.

### Weaknesses
 (1) The algorithm in the paper is not novel. The general natural GD method requires O(P^3) computational costs, due to the inversion of the Gram matrix of \hat{\phi} (G = \hat{\phi} \hat{\phi}^{T} is in size of P \times P). This paper applies SVD directly on \hat{\phi}. Moreover, the line 6 of the algorithm is exactly equivalent to the vanilla natural GD algorithm (rewriting the pseudo-inverse with the SVD). Therefore, I do not find the novelty of the algorithm. The authors claim a reduction in computational complexity by using SVD, but this is a standard technique for computing the pseudo-inverse and does not represent a novel algorithmic contribution. The core operation remains the computation of the pseudo-inverse of a matrix related to the feature map, which is inherent to natural gradient descent. The paper does not introduce any new approximation or optimization technique that would differentiate it from standard implementations of natural gradient descent using SVD for the pseudo-inverse.


(2) In Equations (18) and (19), it seems that the paper tries to explain the consistency by approximating the integral by finite sum of some observations. However, the results of Corollary 1 are relatively weak. The existence of certain points, as stated, follows naturally from standard regularity conditions (e.g., smoothness) of functions. The result is therefore not surprising and lacks substantial implications. It is better if the paper can alternatively prove that if we randomly pick P training samples as observations and with high probability, the difference between du and \hat{\phi} \hat{f} is upper bounded, e.g., O(1/P^{\alpha}), where \alpha is a constant depending on function’s conditions and dimensionality. Such findings would be more meaningful for machine learning. The current analysis provides no insight into the convergence rate or the generalization properties of the method. A more rigorous statistical analysis is needed to justify the empirical success of the method, especially in the context of high-dimensional problems.


(3) The ANaGRAM for PINNs closely resembles existing natural GD for training PINNs (https://arxiv.org/abs/2408.00573). For example, in Equation (31) of the paper, the pseudo-inverse of (J J^{T}) is equivalent to the SVD of \hat{\phi} in this paper. The paper fails to adequately distinguish its approach from existing applications of natural gradient descent to PINNs. The core idea of using the Fisher information matrix or its approximation via the Jacobian is a common practice, and the paper does not introduce a novel way of computing or utilizing this information. The use of SVD is merely an implementation detail and does not constitute a significant methodological advancement.


(4) The natural GD requires the full-batch training, which limits its adaptability to stochastic algorithms. We know that the SGD-like algorithms are widely used in deep learning due to their benefits, such as improving the generalization and bypassing spurious local minima. A more practical approach would be one that can adapt effectively to a stochastic setting. The reliance on full-batch training is a significant limitation, especially for large-scale problems. The paper does not address the challenges of adapting the method to mini-batch settings, which are crucial for practical applications. The lack of stochasticity can also hinder the method's ability to escape sharp local minima, a common issue in deep learning.

### Questions
Please see the weakness part.

One typo: Lines 126-127: ill conditioned

### Soundness
2

### Presentation
4

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The manuscript proposes a natural gradient method related to the ENGD optimizer proposed by (Müller and Zeinhofer). The main contributions are:

- In the context of PINNs, the authors view the ansatz/parametric model as a neural network followed by the application of the PDE and boundary operator. This means that the model is defined on some parameter space $\Theta$, taking values in the product space $L^2(\Omega) \times L^2(\partial\Omega)$ via the intermediate space $\mathcal H$ which is related to the PDE and boundary operators of the specific problem. This mathematical trick of changing what is the model and what is the loss function allows to view PINNs as a standard regression problem. This viewpoint motivates the authors to use an $L^2(\Omega)\times L^2(\partial\Omega)$ based natural gradient method, which agrees with ENGD for linear PDEs but performs better than ENGD for nonlinear PDEs

- The second contribution is on the numerical linear algebra level. Instead of solving the normal equations of the regression, the authors propose to use an SVD directly for the Jacobian of the model. Here, when I write Jacobian I mean the discretized differential of the parametrization, which is denoted by $\hat \phi_{\theta(t)}$ in the manuscript. This gives an improvement in computational complexity from $\mathcal O(P^3)$ for solving the normal equations, to $\mathcal O (\min(N^2P, P^2N) )$, as the Jacobian is of shape $(N, P)$, where $P$ is the dimension of the parameter space $\Theta$ and $N$ is the number of sampling points.

### Strengths
- The viewpoint outlined above leads to a performant method, that works better than ENGD for nonlinear PDEs.

- The improvement in complexity for the linear solve is helpful.

### Weaknesses
 - The viewpoint of absorbing the differential operators into the model can also be understood as a Gauss-Newton method in function space compare to (Jnini et al, arXiv:2402.10680). Moreover, it leads to the standard Gauss-Newton algorithm in parameter space. The manuscript thus does not provide a novel algorithm, but a novel derivation of a known algorithm. While I like this idea and it is certainly a contribution, I think it is not significant enough for an exceptional venue such as ICLR.

 - I am still considering the improved scaling through the rectangular SVD solve as the main contribution of the paper. While the SVD realization is of course useful,  I reiterate that in my opinion it is not significant enough for an exceptional venue such as ICLR.

### Questions
- Can the authors add a reference for the computational complexity of the SVD for the rectangular solve?

- Why is the proposed method performing better than ENGD for the linear equations? I would expect similar performance as it is the same algorithm (up to numerical linear algebra).

- it is very common to include damping into natural gradient methods (adding a scaled identity term to the square Gramian). Can this be realized in this setting?

### Soundness
3

### Presentation
2

### Contribution
2
