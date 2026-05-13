# SANIA: Polyak-type Optimization Framework Leads to Scale Invariant Stochastic Algorithms

- Decision: Reject
- Scores: 6, 6, 6, 6

## Abstract
Adaptive optimization methods are widely recognized as among the most popular approaches for training Deep Neural Networks (DNNs). Techniques such as Adam, AdaGrad, and AdaHessian utilize a preconditioner that modifies the search direction by incorporating information about the curvature of the objective function. However, despite their adaptive characteristics, these methods still require manual fine-tuning of the step-size. This, in turn, impacts the time required to solve a particular problem. This paper presents an optimization framework named \textbf{SANIA} to tackle these challenges. Beyond eliminating the need for manual step-size hyperparameter settings, SANIA incorporates techniques to address poorly scaled or ill-conditioned problems. We also explore several preconditioning methods, including \textit{Hutchinson's method}, which approximates the Hessian diagonal of the loss function. We conclude with an extensive empirical examination of the proposed techniques across classification tasks, covering both convex and non-convex contexts.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a training algorithm generalizing the "Polyak step-size" to second-order algorithms, such as cubic Newton or quasi-Newton. 

Let $f$ be a function to minimize and $w\_t$ the current estimate of the argmin.
For an order-1 method, the Polyak step-size comes down to choosing the step-size such that we would attain the minimum $w^*$ in one step if $f$ was affine between $w\_t$ and $w^*$. For order-2 methods, the authors distinguish the metric used for the parameter space, denoted by $B_t$, and the metric related to the curvature of the local approximation of $f$, represented by a matrix $D_t$.

Then, the authors propose variations of existing algorithms based on their generalization of Polyak step-size.

### Strengths
# Originality

As far as I know, the work presented in this paper is original.


# Clarity

Overall, the paper is easy to follow.


# Quality

I am very grateful to the authors for providing additional experiments (Appendix E), which show not only test accuracy, but also test loss. I would have been even better to provide the training loss, since the proposed algorithms have been designed to improve the optimization process (not the generalization).

Overall, the paper seems to be correct.

# Significance

This paper provides practical uses of *SP2: A Second Order Stochastic Polyak*, Li et al., 2023. 
So the present paper is relevant for the community.

### Weaknesses
 # Originality

This paper can be seen as a practical application of *SP2: A Second Order Stochastic Polyak*, Li et al., 2023.


# Clarity

At the end of Section 2, the authors use the notations: "SANIA $I_d$", "SANIA $(V^{-1})^2$" and "SANIA $\mathrm{diag}(H^{-1})$", while writing that there is no preconditioning. Thus, I understand that "SANIA $A$" refers to Eqn. (6) with $D_t = A$. But there is no formal definition of "SANIA $A$". It should appear somewhere.

Just above Eqn. (9), one can read: $m_t = m_t$, which should be "$m_t = g_t$" (?).

Several mistakes, Figure 1, first plot: 
 * the legend is difficult to understand, since several curves have the same label;
 * some curves do not seem to correspond to their label: apparently, light green should be "SANIA $(V^{-1})^2$";
 * the purple curve is dotted, while it is not dotted in the legend.

### Questions
Could the authors provide a formal link between scale invariance and using SANIA? It seems that there is some overlap between the two, but SANIA does not ensure scale invariance by itself. It would be interesting for potential users of SANIA to provide conditions for their algorithm to be scale-invariant.

Addition to Fig. 5: how does SANIA compare to concurrent methods in terms of training loss?

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
This paper introduces cubic Newton method with adaptive Polyak step-size, enhancing robustness and efficiency in non-convex tasks. It also proposes scale-invariant variants of AdaGrad and Adam, which improve optimizer performance on poorly scaled data. Extensive experiments validate the effectiveness of these methods across diverse optimization scenarios.

### Strengths
1. Thorough theoretical analysis.
2. Clear writing

### Weaknesses
1. It would be great to have theoretical/practical comparisons with Sophia [1], which also uses Hutchinson's based method to compute their preconditioner.
2. KATE [2] removes square root to ensure scale invariance of Adagrad. It would be great to have theoretical/empirical comparison with KATE.

### Questions
What are your thoughts on how learning rate schedules such as cosine decay etc compose with $\lambda_t$ schedule defined in (19)?

How does $\lambda_t$ change during training?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The work tries to incorporate a Polyak-type optimization framework with existing optimizers for machine learning. In the new method, the optimization direction and step size are spontaneously determined by a simple local optimization for each step. The new method is not difficult in realization and appears to work. From the numerical results, the test accuracy of network trained with the new method is comparable to existing methods (but not better than them).

### Strengths
The new method can be naturally incorporated with existing methods and the realization is not difficult.

### Weaknesses
From the numerical methods, the new method does not show improvements compared to previous methods.

From the numerical results, it seems that the test accuracy of Sania is slightly worse than existing methods. The author should also compare the results with SGD, since it usually has competitive generalization ability.

In Line 209, what is the meaning of "Otherwise, we replaced step-size parameter γt to parameter fi∗?". The authors should explain more clearly.

Due to the anisotropic property of the loss landscape, the estimate f* may not be a good guess for the local optimization. How will this affect the performance of the new method?

### Questions
1. Instability of the Euler method and noises are believed to be helpful for generalization (see Ref[1]). Relatively large step size is helpful for the training process to jump out of bad local minima. In the new framework, when the steps are spontaneously obtained, the instability are also almost inhibited spontaneously. This may be a severe problem for the new frame work. 

2. From the numerical results, it seems that the test accuracy of Sania is slightly worse than existing methods. The author should also compare the results with SGD, since it usually has competitive generalization ability.

3. In Line 209, what is the meaning of "Otherwise, we replaced step-size parameter γt to parameter fi∗?". The authors should explain more clearly.

4. Due to the anisotropic property of the loss landscape, the estimate f* may not be a good guess for the local optimization. How will this affect the performance of the new method?

[1] The Implicit Regularization of Dynamical Stability in Stochastic Gradient Descent, Lei Wu, Weijie J. Su, ICML 2023;

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents SANIA, which is a method that doesn't require manual fine-tuning of the learning rate in commonly used stochastic optimization algorithms, leading to faster optimization. The authors present a framework which generalises common stochastic optimization algorithms. The authors also consider affine and scale invariance which seeks to address poorly scaled or ill-conditioned problems. The authors compare performance of SANIA with commonly used algorithms (which have had fine-tuned parameters) for training classifiers for MNIST, FashionMNIST, CIFAR10 and SVHN.

### Strengths
Provides a novel formulation of stochastic optimization algorithms and a novel method that does not require fine-tuning of the learning rate parameter. Investigation into scale invariance is novel. Theorems, equations and ideas are presented clearly. Numerical experiments show that the SANIA methodology achieves similar performance to algorithms with fine-tuned learning rates, and improved robustness as the training curves fluctuate less.

### Weaknesses
Numerical experiments lack a comparison to other options for tuning-free methods.

Minor comments:

Occasional incorrect grammar, including after equation (7): "This leads us to Stochastic Polyak step-size method." should read "This leads us to the Stochastic Polyak step-size method." Also bad grammar in the statement of Theorem 1. "Another way to derive this formulation is by solving" (4), I think it may be better to reference appendix B.2 to make it clear why this holds. "interpolation condition" isn't very clearly defined in my opinion, it may be better to be more clear. "in practice it displays better convergence to the true Hessian than other
similar methods like BFGS" - I think this needs a reference.

### Questions
In Page 2, SPS has been derived, why not just cite it? The difference between g_t and m_t is unclear to me, these seem to often mean the same thing? Why not keep the notation consistent? In (6) you have written \| w \|_{B_t} is a Euclidean norm, would it be better to say " \| \cdot \|_{B_t} is a Euclidean norm"?

### Soundness
3

### Presentation
3

### Contribution
3
