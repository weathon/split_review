# Second-Order Min-Max Optimization with Lazy Hessians

- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 8, 8, 6

## Abstract
This paper studies second-order methods for convex-concave minimax optimization. 
\citet{monteiro2012iteration} proposed a method to solve the problem with an optimal iteration complexity of 
$\gO(\epsilon^{-3/2})$ to find an $\epsilon$-saddle point.  
However, it is unclear whether the
computational complexity, $\gO((N+ d^2) d \epsilon^{-2/3})$, can be improved. In the above, we follow \citet{doikov2023second} and assume the complexity of obtaining a first-order oracle as
$N$ and the complexity of obtaining a second-order oracle as $dN$. In this paper, we show that the computation cost can be reduced by reusing Hessian across iterations.
Our methods take the overall computational complexity of $ \tilde{\gO}( (N+d^2)(d+ d^{2/3}\epsilon^{-2/3}))$, which improves those of previous methods by a factor of $d^{1/3}$. 
Furthermore, we generalize our method to strongly-convex-strongly-concave minimax problems and establish the complexity of $\tilde{\gO}((N+d^2) (d + d^{2/3} \kappa^{2/3}) )$ when the condition number of the problem is $\kappa$, enjoying a similar speedup upon the state-of-the-art method. 
Numerical experiments on both real and synthetic datasets also verify the efficiency of our method.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work proposed second-order algorithms LEN and LEN-restart for C-C and SC-SC min-max problems, these algorithms incorporate lazy Hessian update and Extragradient update, the computational cost analysis and numerical experiment results showed the outperformance of the proposed algorithms versus existing algorithms.

### Strengths
1. A new algorithm in min-max optimization with better computational complexity versus existing results.
2. The paper is well organized, the flow is easy to follow.

### Weaknesses
1. The main component seems to be a combination of Doikov et al. (2023) on lazy Hessian and Adil et al., (2022) on extragradient, which may restrict the novelty a bit.
2. The experiment can be further enhanced.
   - First, the $O(d^{1/3})$ improvement suggests the outperformance is valid in high-dimensional cases (while not in low-dimensional cases), now the experiment cannot exhibit such a pattern, how does the algorithm perform in low-dimensional case?
   - It is not clear how the choice of $m$ affects the performance, maybe you can follow Doikov et al. (2023) to add more experiments for clarification.
   - The theory part uses the gap function as the measurement, while the experiment uses the gradient norm or point distance, maybe you can add more clarification to rationalize your choice.

### Questions
/

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
Authors generalize the results of Nikita Doikov, El Mahdi Chayti, and Martin Jaggi. Second-order optimization with lazy hessians. In ICML, 2023. related with lazy Hessian for Cubic regularized Newton method for Saddle-point problems (SPP). The developed result was cleary presented and sufficiently technical. Moreover, requires principally new ideas. However, the the motivation to consider second-order methods are quite limited and is mainly theoretical from my point of view. Also in the paper authors doesn't observe the accuracy required to solve auxiliary problem.

### Strengths
I guess the paper is good from mathematical point of view. The results is strong, original, well presented. I agree with authors that they developed significantly new tricks to work with this class of problems. I guess the paper is good!

### Weaknesses
For me the main drawback is motivation. I do not understand why we should use second-order method with expensive iteration rather than the first-order one. I understand the motivation for convex optimization where the number of iteration significantly reduces by using optimal second-order scheme, but I do not understand it for SPP where the difference is minor. The analysis of the convergence rate focuses on the dependence on the error tolerance $\epsilon$, but does not adequately address the practical implications of the iteration cost. The computational cost of each iteration in second-order methods, which involves operations like Hessian computation and inversion, is significantly higher than first-order methods. This difference in per-iteration cost needs to be more explicitly considered when comparing the overall efficiency of the methods. Furthermore, while the asymptotic convergence rate might be better for second-order methods, the constant factors hidden in the big-O notation could be large enough to make first-order methods more practical for a reasonable range of error tolerances. Also in the paper authors doesn't observe the accuracy required to solve auxiliary problem.

### Questions
1) Is it possible to generalize the result in case strongly convex-strongly concave case with different constant of strong convexity/concavity?
2) Could you estimate the required accuracy for auxiliary problem that guarantee the desired precision for target problem? 
 I can make rating higher if you can positively answer for this questions.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
In this paper authors utilize the lazy Hessians technique inside second-order extragradient method for min-max optimization. The main idea of lazy Hessians technique is to update Hessian in second-order method only every $m$ iterations. Authors consider convex-concave and strongly-convex-strongly-concave setups. Authors claim, that if $m=\Theta(d)$ iterations, where $d$ is a dimension of the problem, their method achieves state-of-the-art computational cost.

### Strengths
Authors propose a method with the same oracle complexity, as state-of-the-art methods but with less computational complexity. This means, that their algorithm can achieve the same estimation error with the same number of iterations, but overall spending less computational resources and taking less time. The experimental results only support this point. This makes method more attractive from the practical point of view. The paper is written in a clear way, and it is easy to understand.

### Weaknesses
Overall, the paper feels like a very incremental result. Authors employ a known technique to reduce number of Hessian computations to existing second-order method to solve convex-concave min-max problem. To adapt proposed method to strongly-convex-strongly-concave problem, authors use a universal restarts framework, that works like a "wrap" around any method for convex(-concave) problems and gives better theoretical convergence for strongly-convex(-strongly-concave). Despite the fact that this paper proposes a new method with better computational complexity compared to other analogs, it lacks any novel ideas or solution of any complex problems.



### Questions
1. Could you explain please, how did you get second inequality in eq. (17)?
1. Lines 155-160. Sentence "Their methods only take a lazy CRN update (2) at each iteration..." seems to me very weird. I needed to read it couple of times to understand. Please, rewrite in in more clear way.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a second-order algorithm designed for convex-concave minimax optimization problems. The algorithm brings the Lazy Hessian (or Lazy *Jacobian* for this paper, I guess) approach by Doikov et al. (2023) to second-order minimax optimization algorithms as in Adil et al. (2022), Lin et al. (2022). The new algorithm can achieve a computational complexity smaller by an order of $d^{1/3}$ compared to previous results both for the convex-concave case. The paper also shows superlinear convergence in the strongly-convex-strongly-concave case (by adding a restarting scheme) where we also have an improvement of $d^{1/3}$.

### Strengths
- It is interesting to see that the idea of Doikov et al. (2023) can also work for minimax optimization problems.
- The paper seems to be well-written and clear, and there are empirical results supporting the theoretical arguments.

### Weaknesses
 - The results only cover convex-concave minimax optimization for now, and there are no clear ways suggested to extend to broader problem classes like nonconvex-nonconcave functions or variational inequalities. Specifically, while the paper focuses on the convex-concave setting, many real-world problems involve non-convexity or non-concavity, and the paper does not address how the proposed algorithm would perform in such scenarios. Furthermore, the extension to variational inequalities is not straightforward, as it would require a different analysis of the error terms and convergence properties, which are not discussed.
- As the main idea comes from combining two lines of previous work, it’s a bit hard to say that the ideas are highly original (except for the proof techniques of bounding the errors from lazy updates for the minimax case, particularly when there are EG steps in between). The core idea of reusing Hessian information has been explored in the past, and this paper essentially applies it to the minimax setting. The novelty lies primarily in the technical details of the analysis, particularly in handling the errors introduced by the lazy updates within the extra-gradient framework. However, the high-level approach is not fundamentally new, which limits the overall originality of the work.

### Questions
- In the proof of Theorem 4.1, what we essentially do is find an upper bound of
    $$ \begin{align*}
    \frac{1}{\sum_{i=0}^{t-1} \eta_i} \sum_{i=0}^{t-1} \eta_i \langle F(z_i),  z^{\star} - z_i\rangle
    \end{align*} $$
    which itself is an upper bound of the Gap function by Lemma A.1.
    
    My question is, can’t we just try to come up with an upper bound of the *MVI error* $\langle F(\hat{z}), z^{\star} - \hat{z} \rangle$ instead? If this works, it might be possible to extend the results to general MVIs. (I think one problem could be that we can’t use things like Jensen’s inequality if we step out of the convex-concave assumption.)
    
- Is the $\beta$ in Definition 3.4 just there for technical reasons (to ensure something like bounded iterates for the unconstrained case)?

- This might be a slightly irrelevant question, but any ideas of whether the proposed idea (or maybe the Lazy Hessian idea for minimization problems) could work for higher-order cases with $p \ge 3$?

- There seem to be complicated lower bound results in Adil et al. (2022) in terms of the *iteration* complexity. Can this naturally lead to some type of a lower bound in the *computational* complexity as well with which we can compare the new/previous upper bounds?

- Minor typo. In the middle of the inequality of Definition 3.3, I think it should be $f(x^{\star}, y^{\star})$.

**References.** \
Adil et al., 2022. Optimal methods for higher-order smooth monotone variational inequalities. \
Doikov et al., 2023. Second-order optimization with lazy Hessians. \
Lin et al., 2022. Explicit second-order min-max optimization methods with optimal convergence guarantee.

### Soundness
3

### Presentation
3

### Contribution
3
