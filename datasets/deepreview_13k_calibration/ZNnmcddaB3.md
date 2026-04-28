# Robust System Identification: Finite-sample Guarantees and Connection to Regularization

- Decision: Accept
- Avg Score: 6.20
- Scores: 5, 8, 6, 6, 6

## Abstract
We address the problem of learning nonlinear dynamical systems from a single sample trajectory. While the least squares estimate (LSE) is commonly used for this task, it suffers from poor identification errors when the sample size is small or the model fails to capture the system's true dynamics. To overcome these limitations, we propose a robust LSE framework, which incorporates robust optimization techniques, and prove that it is equivalent to regularizing LSE using general Schatten $p$-norms. We provide non-asymptotic performance guarantees for linear systems, achieving an error rate of $\widetilde{\mathcal{O}}(1/\sqrt{T})$, and show that it avoids the curse of dimensionality, unlike state-of-the-art Wasserstein robust optimization models. Empirical results demonstrate substantial improvements in real-world system identification and online control tasks, outperforming existing methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Building on recent work by authors such as Simchowitz, Jedra and others, this paper
studies system identification for linear systems in the one trajectory setup,
showing that a regularized form of least-squares estimation (LSE)---with the
regularization being a Schatten $p$-norm---has favorable nonasymptotic convergence,
and (empirically) outperforms unregularized LSE on some standard benchmarks.

### Strengths
The problem is a significant one, and the theoretical results presented by the authors are nicely executed and nicely presented.

### Weaknesses
Clearly it's appropriate to regularize least-squares estimators in settings in
which there isn't much data, and for matrix estimands a standard matrix norm such
as the Schatten $p$-norm is a natural choice.  This would have seemed to be a
reasonable starting place for the paper.  But, instead of just starting with this
(statistical) perspective, the current paper starts with a robust optimization
(minimax) perspective.  In the authors' words, "seeking the best system parameter
against the worst-case realizations of the data."  But the latter motivation is
rather different from the motivation of small data sets, and it's a bit odd to
start with robustness if the focus is small samples.

The authors do show that the minimax perspective yields the Schatten $p$-norm
regularization.  Perhaps this is just a matter of taste, but this sequence of
logic doesn't make much conceptual sense to me.

A robustness perspective would seem to make sense if the issue is one of misspecification,
and indeed the authors state that "it [the LSE] suffers from poor identification
errors when the sample size is small or the model fails to capture the system's true
dynamics."  It's the latter statement that seems well aligned with the robustness
motivation.  But the paper doesn't seem to follow up on this issue, either theoretically
or empirically (e.g., by considering misspecification).

With respect to the theoretical results, they are indeed very nicely executed and presented,
but I'm not sure how much novelty there is.  My sense is that this is a redeployment of tools
from the papers of Simchowitz, Jedra and others; I'd be happy to stand corrected if that's not the case.

### Questions
My main question is regarding the extent to which there is novelty in the proof of the main theorem (Theorem 2).

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
In this paper, the authors propose a novel estimator for discrete-time, single-trajectory system-identification via Schatten-norm regularization. The authors claim that the proposed estimator combines the desiderata of rate-optimal guarantees of the standard least-squares estimator and robustness to misspecification a la Wasserstein robustness. The authors support their claims on some numerical experiments, demonstrating that in the presence of misspecification (e.g. from nonlinear dynamics), the proposed estimator has better convergence properties than the standard LSE.

### Strengths
The paper is in general well-written and straightforward to understand. The method derivation is quite clean, demonstrating that min-max robust LSE can be turned into an semi-definite program, which can then be reduced further to an unconstrained Schatten-norm-regularized least-squares problem. Something of note is that the proposed SDP only interacts with the trajectory through the empirical Gram matrix, and thus does not need to scale with the length of the trajectory. The theoretical guarantees of the estimator also demonstrate the rate-optimality of the procedure, which is otherwise not true for out-of-the-box guarantees of Wasserstein robust estimators. Numerical experiments demonstrate that not only is the estimator performant compared to LSE, it can be slotted into various online control frameworks to great effect.

I think the paper is good enough for acceptance; I have bumped my score up after the author's response.

### Weaknesses
Since the proposed method is a regularized version of the least-squares estimator, it inherently has an additional moving part in the regularization parameter. In theory, for the robustness set to cover the population Gramian with high probability, the regularization parameter is determined by the convergence rate of the empirical Gramian to the population one, and thus can only be as good as the (typically conservative) upper bounds. Therefore, the authors propose as a heuristic to determine the best scaling of the regularization parameter via cross-validation, and demonstrate that this tuned method outperforms LSE by a large relative amount. However, this is somewhat unenlightening, as this is comparing a fine-tuned algorithm to *the* base estimation algorithm (which is technically subsumed by the proposed class of estimators). It would be more informative if the comparison were to a different class of (fine-tuned) robust estimators.

The paper also assumes strict stability. While this is likely for technical reasons in the proof, as the authors follow Jedra and Proutiere's (2020) Hanson-Wright approach, something that is left wanting in this paper is whether proposed estimator also performs better in the face of (near) marginal stability, since the authors point out in Section 5.2 that the estimator actually performs relatively better in the very-stable regime. In the same vein, it would be more enlightening to see stabilization rate of synthesized controllers from the estimated matrices $\hat A, \hat B$ as a function of data, e.g. via certainty-equivalent LQR, as this is a more practical notion of estimator robustness.

The paper also contains a few confusing parts. Most notably, the uncertainty level $\epsilon(\delta)$ in (11) is set with minimal details on the parameters therein. Since this quantity shows up in the error bound in Theorem 2, it would be good to at least show the valid upper bound on $\epsilon(\delta)$ derived in the appendix, since the main paper suggests $\epsilon(\delta) = \tilde{\mathcal O}(1/\sqrt{T})$ is the quantity up to universal constants, while in reality it contains some (rather important) system-dependent quantities.

**Minor comments**
- Should provide mathematical definition of subgaussianity in the assumptions.

- Should define what $\|\nabla_\theta \|\mathbf A(\theta^\star)\|_q\|$ is in (12). Also, this seems to differ from the quantity in the appendix proof (42).

### Questions
Please see the above Weaknesses section for areas to clarify.

Also, it would be good to expand on the comparison to the DRO literature. Notably, why is (Gao, 2023) not applicable to even the iid version of this least-squares problem? For example, if we instead pretend to draw each point of the trajectory from its marginal distribution and apply a beta-mixing blocking argument, would (Gao, 2023) be applicable to the independent process?

Rui Gao, "Finite-sample guarantees for wasserstein distributionally robust optimization: Breaking the curse of dimensionality", 2023.

Kuznetsov and Mohri, "Generalization bounds for non-stationary mixing processes", 2016.

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
4

### Summary
The authors study the problem of identifying non-linear system dynamics from a single trajectory. They introduces a robust framework for system identification and reveal the connection to regularized empirical risk minimization. They provide non-asymptotic guarantees for linear systems and demonstrate an improved error rate of $\tilde{\mathcal{O}}(1/\sqrt{T})$, which the authors claim avoids the curse of dimensionality faced by other robust methods such as Wasserstein robust optimization. Empirical results validate the effectiveness of robust LSE in system identification and online control tasks.

### Strengths
**Clarity of exposition:** The paper is well-written and identifies the limitations of the standard LSE in system identification under limited data or misspecified models, providing motivation for the proposed robust LSE.
    
**Theoretical contribution:** The paper presents non-asymptotic error bounds that establish the effectiveness of Schatten $p$-norm regularization, positioning the method as a theoretically grounded alternative to Wasserstein robust optimization.

**Empirical Validation:** Several numerical experiments are conducted, including tasks in wind speed prediction and online control, with substantial improvements over classical LSE.

### Weaknesses
 **Discussion of the theoretical results:** The authors very briefly discuss their main results and the implications of the regularization term in their bounds. In particular, it is important to note that $T$ still scales with the system dimensions, i.e., $n+m$ in Theorem 2. It is important to make clear the difference between the curse of dimensionality and the unavailable dependence of the system dimension in the burn-in.



### Questions
1) The authors mention the use of different Schatten norms but does not provide insight into the practical or theoretical consequences of varying $p$. Could the authors expand more on this?

2) Could the authors provide more intuitions on the key factors for avoiding the course of dimensionality in their results? The way the error bounds is presented in Theorem 2 it is not clear the benefit of the regularization term.

### Soundness
3

### Presentation
3

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
1. An equivalent SDP formulation for robust LSE with Schatten p-norm regularization 
2. finite-sample guarantees for system identification with single trajectory

### Strengths
1. very nice and solid theory
2. provide theoretical guarantees for a hard system identification problem

### Weaknesses
1. Is single trajectory a common case in real applications, although it might be an interesting theoretic topic? Could you please provide more motivate examples? Online control of linear system might be one, however the existing works most focus on learning a controller directly rather than following the conventional pipeline (i.e. system identification and then model-based control). What is the advantage of conventional pipeline in the low data region?
2. The authors claim that unlike the SOTA Wasserstein robust optimization, their approach can avoid the curse of dimensionality. However, no comparison study w.r.t. the SOTA method is provided in the paper. And the examples are of very low dimension. The largest linear model is in Sec. 5.2 with $\theta \in \mathbb{R}^{5\times 10}$.
3. Very strong theory but very weak experiments. Most of them are either synthetic or low-dimension datasets. 
4. The results in Sec.4 rely on strong assumptions. For example, if the application is online control or wind prediction, then A2 and A6 do not hold.

### Questions
1. Due to the setup (perfect state measurement and known model $\phi$), Thm. 1 holds with no significant difference for linear and nonlinear $\phi$. What if the case where only $y_t=x_t+v_t$ is available or $\phi$ has some uncertainty? For simplicity, we can assume that $\phi$ is linear.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a robust least squares estimation (LSE) framework that combines robust optimization with the LSE approach to learn nonlinear dynamical systems from a single sample trajectory, demonstrating its equivalence to regularizing LSE with a general Schatten 
p-norm. For the linear case, the authors provide non-asymptotic performance guarantees of the framework under certain conditions and show that the error rate is invariant to system dimensionality.

### Strengths
The authors propose a robust LSE framework to learn nonlinear dynamical systems and demonstrate its equivalence to the LSE problem regularized by the Schatten p-norm. They also provide theoretical performance guarantees for the framework applied to linear dynamical systems under certain conditions。

### Weaknesses
While the paper considers nonlinear dynamical systems, the theoretical results on convergence are limited to linear cases. Additionally, the paper lacks comparisons with other classical methods, such as LSE regularization with special cases of the Schatten 
p-norms mentioned in line 54 and the Wasserstein robust optimization discussed in line 59.

While the authors propose a robust LSE framework and demonstrate its equivalence to the LSE problem regularized by the Schatten p-norm, the practical implications of this equivalence are not fully explored. Specifically, the choice of the Schatten norm parameter 'p' and its impact on the performance of the proposed method are not investigated. The theoretical analysis, while providing non-asymptotic guarantees for the linear case, does not offer insights into how the choice of 'p' should be made in practice, especially when dealing with different eigenvalue distributions of the underlying system. Furthermore, the paper does not provide any empirical evidence to support the claim that the proposed method is robust to different choices of 'p'.

It seems that the definition of $\Sigma_\omega$  in equation 9 is missing. Moreover, the justification for substituting $\hat\Omega_T$ with its expectation in line 162 to obtain the 'true LSE problem' is not clearly explained. It is more conventional to define the true LSE problem by taking the expectation of the state and feature vectors in equation 2, rather than the sample covariance matrix. The paper also lacks a clear explanation of how the optimal solution to equation 5 is derived and why it is equal to $\theta^*$.

### Questions
1. In line 162, the authors state that they can express the true LSE problem by substituting $\hat\Omega_T$ in equation 3 with its expectation. Is there any literature to support this? What do you mean by "the true LSE problem"? In my opinion, it is more reasonable to obtain the true LSE problem by substituting $x$ and $\phi$ in equation 2 with their expectation. 
2. How do the authors prove that the optimal solution to equation 5 is $\theta^*$?
3. The proposed robust LSE framework is closely related to the Schatten p-norm. Hence, what is the value of p in your experiments? In particular, it is necessary to show the performance of the robust LSE across different norms.
4. In Sections 5.1 and 5.2, the authors only compare the proposed method with the LSE. Comparisons with other classical methods are highly recommended, such as LSE regularization with special cases of the Schatten p-norms mentioned in line 54 and the Wasserstein robust optimization discussed in line 59.
5. It seems that the definition of $\Sigma_\omega$  in equation 9 is missing.

### Soundness
3

### Presentation
2

### Contribution
2
