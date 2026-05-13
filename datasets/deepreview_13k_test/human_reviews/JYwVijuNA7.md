# Revisiting Large-Scale Non-convex Distributionally Robust Optimization

- Decision: Accept
- Scores: 6, 6, 6, 5

## Abstract
Distributionally robust optimization (DRO) is a powerful technique to train robust machine learning models that perform well under distribution shifts. Compared with empirical risk minimization (ERM), DRO optimizes the expected loss under the worst-case distribution in
an uncertainty set of distributions. This paper revisits the important problem of DRO with non-convex smooth loss functions. For this problem, Jin et al. (2021) showed that its dual problem is generalized $(L_0, L_1)$-smooth condition and gradient noise satisfies the affine variance condition, designed an algorithm of mini-batch normalized gradient descent with momentum, and proved its convergence and complexity.   In this paper, we show that the dual problem and the gradient noise satisfy simpler yet more precise partially generalized smoothness condition and partially affine variance condition by studying the optimization variable and dual variable separately, which further yields much simpler algorithm design and convergence analysis. We develop a double stochastic gradient descent with clipping (D-SGD-C) algorithm that converges to an $\epsilon$-stationary point with $\mathcal O(\epsilon^{-4})$ gradient complexity, which matches with results in Jin et al. (2021). Our algorithm does not need to use momentum, and the proof is much simpler, thanks to the more precise characterization of partially generalized smoothness and partially affine variance noise. We further design a variance-reduced method that achieves a lower gradient complexity of $\mathcal O(\epsilon^{-3})$. Our theoretical results and insights are further verified numerically on a number of tasks, and our algorithms outperform the existing DRO method (Jin et al., 2021).

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, the authors consider a distributionally robust optimization (DRO) problem with non-convex smooth losses. The previous work of Jin et al studied the same problem and showed that the dual problem satisfies a notion of generalized smoothness and bounded variance. They then used a normalized momentum algorithm that provably converges to stationary points under these conditions. By contrast, this paper shows that one can provide a more fine-grained analysis of the smoothness and variance. The authors that propose alternative optimization methods based on these refined properties. Finally, experimental results show that the proposed methods outperform the algorithm in Jin et al.

### Strengths
1. The authors conduct an improved analysis of the non-convex DRO problem and the analysis leads to simpler algorithms and theory. The partial generalized smoothness condition might be of interest in other settings as well.

2. Theoretical results are presented in a clear manner, and the authors provide detailed comparison with the previous work by Jin et al, thereby hightlighting the contribution of this work.

3. Besides improving over the normalized momentum method in Jin et al, the authors also provide an extension of the well-known spyder algorithm to the DRO setting. I'm not aware of such type of existing results in the literature.

### Weaknesses
1. In some paragraphs the authors seem to misuse \citet instead of \citep (e.g. the first paragraph in page 4)

2. The authors only run experiments at a relatively small scale. It would be interesting to compare different methods by running a large-scale experiments.

### Questions
I do not have questions for this work.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper studies the penalized distributionally robust optimization (DRO) problem where the loss function $\ell(x, s)$ is $G$-Lipschitz and $L$-smooth in $x$ for any given sample $s$. In particular, the authors consider $\psi$-divergence distance in the penalty term and solve the DRO problem from its dual optimization. The authors refines the generalized smoothness used in prior work [1], and proposed alternating gradient methods (in terms of the dual variables and the primal variables) by noticing that the dual problem is actually smooth with respect to the dual variables. By this refined perspective of generalized smoothness, the authors achieve the same complexities as ones in [1] by simpler algorithms. Further convergence analysis under stochastic settings and variance reduction is conducted.

[1] Jikai Jin, Bohang Zhang, Haiyang Wang, and Liwei Wang. Non-convex distributionally robust optimization: Non-asymptotic analysis. In Proceedings of Advances in Neural Information Processing Systems, volume 34, pp. 2771–2782, 2021.

### Strengths
- The write-up of this paper is good and easy to follow.
- It is interesting to see that one can refine the smoothness on the dual problem of penalized DRO and develop simpler algorithms by exploiting the refined smoothness.
- The analysis is provided under both deterministic and stochastic settings. Improved complexity is achieved by recursive variance reduction.

### Weaknesses
- The generalized smoothness on the dual side depends on the strict assumptions on the primal loss function: assuming Lipschitzness and smoothness at the same time and for any sample $s \in S$; the bounded variance of the function values.
- The deterministic setting would be restricted, as one usually cannot access the full gradient of the stochastic objective like $\mathcal{L}$.
- Although the authors propose simpler algorithms, the step size requirements are actually strict: $\beta_t$ either dependents on the initial function gap (Theorem 1) or requires full gradient evaluation (Theorem 2). 
- I would not say optimizing $x$ and $\eta$ separately; instead the algorithms are performing alternating gradient steps with respect to these two blocks of variables.

### Questions
- The paper title is quite vague. I suggest that the authors could rephrase it to make it more precise, like in terms of generalized smoothness.
- Could the authors discuss the technical challenges of this work, compared to the prior work [1]? It seems that the write-up and the analysis are mostly similar.
- It seems that generalized smoothness condition heavily relies on the Lipschitzness of the primal function. Am I understanding correctly, or it can be relaxed?
- In the stochastic settings, the step sizes $\beta_t = O(\varepsilon / L_0||v_t||)$. Could the authors discuss the dependence on $\varepsilon$?


[1] Jikai Jin, Bohang Zhang, Haiyang Wang, and Liwei Wang. Non-convex distributionally robust optimization: Non-asymptotic analysis. In Proceedings of Advances in Neural Information Processing Systems, volume 34, pp. 2771–2782, 2021.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies the Distributionally robust optimization (DRO) problem. The paper first shows an observation that the specific DRO problem satisfies a stronger smoothness and noise condition than existing work showed. Then the paper designs multiple algorithms to solve the problem making use of the stronger assumptions, together with corresponding convergence guarantees.

### Strengths
1. The paper is well written, with a clear introduction to the studied problem and well-defined notations. I enjoy reading it.

2. The theory is neat and complete, taking 3 algorithms into consideration. 

3. I appreciate the idea of finding that the problem actually satisfies stronger assumptions and designing approaches based on this observation.

### Weaknesses
1. The convergence in Theorem 3 is not strong enough, requiring a very large batch size. As a comparison, (Jin et. al.) achieved a convergence bound with a much more reasonable batch size requirement. In fact, I think this is partially why they used this more complex method, as momentum is proven to help handle noise in normalized gradient descent and enable convergence with small batch size (Cutkosky \& Mehta, 2020). 

2. All the convergence results seem to require a large batch, and I don't see benefits compared to the results in (Jin et. al.). This makes me wonder whether the observation in Sections 3.1 and 3.3 that DRO satisfies stronger conditions really helpful for designing algorithms. I will be happy to raise my score if the authors can address my concerns.

[1] Jikai Jin, Bohang Zhang, Haiyang Wang, and Liwei Wang. Non-convex Distributionally Robust Optimization: Non-Asymptotic Analysis. In NeurIPS, 2021.

[2] Ashok Cutkosky and Harsh Mehta. Momentum Improves Normalized SGD. In ICML, 2020.

### Questions
1. It seems that the citation of the original spider paper (Fang et. al.) is missing. I kindly suggest the authors to add it.

2. Definition 3 actually indicates a much stronger version of the $(L_0,L_1)$-smoothness, as the inequality only applies to $||x-y|| \le 1/L_1$ for initial $(L_0,L_1)$-smoothness. Therefore, some expressions and citations in the paper regarding the assumption may be inappropriate (e.g. citations in line 192). I suggest the authors to add some discussions on this.

3. I think possibly momentum is also helpful for convergence with smaller batch sizes in your case. Have you tried this?

[1] Cong Fang, Chris Junchi Li, Zhouchen Lin, and T. Zhang, “SPIDER: Near-optimal non-convex optimization via stochastic path-integrated differential estimator.” In NeurIPS 2018.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper studies Distributionally Robust Optimization (DRO) with non-convex smooth functions, which optimizes the expected loss under the worst-case distribution in an uncertainty set of distributions, which is different from the tradition Empirical Risk Minimization (ERM). In particular, the paper improves Jin et al (2021) which treats the same problem, working with the dual formulation. The authors show that the dual problem and the gradient noise satisfy simpler yet more precise partially generalized smoothness condition and partially affine variance condition by studying the optimization variable and dual variable separately. This also yields simpler algorithm design and convergence analysis, based on which the authors propose D-SGD-C algorithm and variance reduced SGD versions.

### Strengths
(1) Proposed an improvement of Jin et al (2021) and showed that by studying the optimization variable and the dual variable separately, one can derive the fact that the dual problem and the gradient noise satisfy simpler yet more precise partially generalized smoothness condition and partially affine variance condition;

(2) Based on this idea, they also propose new and simpler algorithms like D-SGD-C etc.

### Weaknesses
(1) This is an almost pure math paper, so a better explanation of the main mathematical ideas at the introductory part would be nice

(2) no experimental validations

### Questions
After reading the paper, I feel that the main context is a dry list of theorems referring to the proofs in the appendix. So the mathematical innovations can be lost if there is no better overview of the ideas. Can the authors provide one in a revision?

### Soundness
3

### Presentation
2

### Contribution
3
