# A Tight Convergence Analysis of Inexact Stochastic Proximal Point Algorithm for Stochastic Composite Optimization Problems

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 6, 5, 8

## Abstract
The \textbf{i}nexact \textbf{s}tochastic \textbf{p}roximal \textbf{p}oint \textbf{a}lgorithm (isPPA) is popular for solving stochastic composite optimization problems with many applications in machine learning. While the convergence theory of the (inexact) PPA has been well established, the known convergence guarantees of isPPA require restrictive assumptions. In this paper, we establish the stability and almost sure convergence of isPPA under mild assumptions, where smoothness and (restrictive) strong convexity of the objective function are not required. Imposing a local Lipschitz condition on component functions and a quadratic growth condition on the objective function, we establish last-iterate iteration complexity bounds of isPPA regarding the distance to the solution set and the Karush–Kuhn–Tucker (KKT) residual. Moreover, we show that the established iteration complexity bounds are tight up to a constant by explicitly analyzing the bounds for the regularized Fr\'echet mean problem. We further validate the established convergence guarantees of isPPA by numerical experiments.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper considers the inexact stochastic proximal point algorithm (isPPA) for solving convex stochastic composite optimization problems.

The authors relax the convergence assumptions by removing the requirements for smoothness and strong convexity, instead imposing a local Lipschitz condition and a quadratic growth condition on the objective function.

They establish non-ergodic (last-iterate) convergence rates for the algorithm.

Finally, the authors present empirical results to show the asymptotic convergence rates for the distance to the solution set and the KKT residual.

### Strengths
**S1**. This paper proposes isPPA to solve nonsmooth convex stochastic optimization problems under weaker assumptions of **a local Lipschitz continuity condition** and **a quadratic growth condition**, broadening its applicability in nonsmooth settings.

**S2**. This paper provides a tight analysis of the last-iterate convergence rates for the distance to the optimal solution set and the KKT residual, as shown in Theorems 2.4 and 2.7.

**S3**. Using the simple regularized Frechet mean problem, the authors establish the lower bounds for the convergence rate of the distance to the optimal solution set. By comparing the lower and upper bounds, they show that the asymptotic convergence rate is tight up to constant factors.

### Weaknesses
 **W1.** Algorithm 1 is a double-loop algorithm, as it relies on another optimization algorithm to solve each subproblem. Such algorithms are rarely used; instead, single-loop algorithms, where each iteration precisely solves the subproblem, are more common. Although the algorithm specifies the required accuracy for each subproblem, these accuracy estimates tend to be conservative and are seldom used in practice, as they can significantly reduce the overall efficiency of the algorithm. The practical implications of using a double-loop structure, especially in terms of computational overhead, are not sufficiently addressed.

**W2.** For general non-smooth convex optimization problems, the paper does not provide the required iteration complexity for solving the subproblems. This lack of detail makes it difficult to assess the overall computational cost of the proposed method. The analysis should include a discussion on how the subproblem solver's complexity impacts the overall convergence rate and practical applicability.

**W3.** The authors claim that the algorithm requires weaker conditions than all existing methods. To support this claim, it would be beneficial to include a practical machine learning example where other methods fail, but the proposed method succeeds. The two examples provided in the experiments do not fully support the claim of requiring weaker assumptions. A more compelling demonstration of the method's advantage in a specific application is needed.

**W4.** The authors mention in Lines 68-69 that the Lipschitz continuity condition is violated by the elastic net regularizer. I think this statement is inaccurate; a function that is continuously differentiable on a closed compact set is indeed Lipschitz continuous. Given that the iterative sequence is assumed to be bounded (see Lines 95 and 296), the elastic net regularizer should also be globally Lipschitz. The argument regarding the local Lipschitz condition needs further clarification, especially in the context of the boundedness assumption.


**W5.** Typo. Line 440: It should be "iteration(k)".

### Questions
I would like to ask two questions regarding the nonconvex scenario, as it is more general and widely applicable.

**Q1.** Referring to Lines 84-85, why is the proposed methodology more readily extendable to nonconvex settings?

**Q2.** How does the proposed algorithm compare to the proximal point method in the cited paper *Davis, D., & Drusvyatskiy, D. (2019). Stochastic model-based minimization of weakly convex functions*, which is designed for minimizing weakly convex functions?

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
In this paper, the authors consider inexact stochastic proximal point algorithm (isPPA) for solving stochastic composite optimization problems. Under mild conditions, the authors demonstrate the stability and almost sure convergence of this method. By further assuming a local Lipschitz condition on component functions and a quadratic growth condition on the objective function, the authors establish convergence rate guarantees. Empirical validation from numerical experiments supports these theoretical analyses.

### Strengths
In this submission, the authors prove the stability of isPPA under mild conditions, extending the stability result for exact sPPA. The authors provided non-asymptotic last-iterate convergence rates for isPPA in terms of the expected squared distance to the optimal solution set. They also provide lower bounds on the convergence rates of isPPA for solving problem under the assumptions proposed in this paper, demonstrating that the derived convergence rate guarantees are tight up to constant factors. All the theoretical analysis are proved by detailed mathematical analysis and empirical results from the numerical experiments are consistent with the theoretical analysis.

### Weaknesses
The only weakness of this submission is that the authors should explain more about how the assumptions provided in this paper is "mild" or less restrictive compared with the previous results. And how exactly the results of this paper differ from the results of the previous works. How exactly the assumptions one to five are more general compared with the assumptions in the previous results and how this impact the theoretical proof and analysis.

### Questions
The authors should make more remarks about how the assumptions in this submission is weaker than the assumptions from previous papers and compared more about the theoretical analysis in this work with the previous works.

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
4

### Summary
The paper presents the convergence of an inexact stochastic proximal point algorithm for solving stochastic composite optimization problems. The main contributions lies in weakening the assumptions on the function class and illustrating the tightness of the established bounds.

### Strengths
The problem setting, assumptions, and theoretical results are clearly stated, and necessary comparisons with the existing literature are provided.

### Weaknesses
1. The applicability of the proposed proximal point algorithm is limited. It requires two loops, and the complexity of the inner loop can also be prohibitive. The complexity of solving the inner problems is not considered in the paper. Specifically, the paper does not address the practical challenges of implementing the inner loop, which involves solving a stochastic optimization problem at each iteration of the outer loop. This nested structure can lead to significant computational overhead, especially when the inner problem requires a large number of iterations to achieve sufficient accuracy. The paper should provide a more detailed analysis of the computational cost associated with the inner loop and discuss strategies for mitigating this cost, such as using efficient optimization algorithms or early stopping criteria.
2. Deriving the stability result from existing exact PPA algorithms in the literature does not seem particularly challenging. Additionally, given coercivity and the assumption that $\|x_k\|$ is bounded, it would be more natural to use local Lipschitz continuity rather than global Lipschitz continuity. It’s essential to clearly state the technical difficulties involved. The paper should clarify why global Lipschitz continuity is necessary, given the boundedness of the iterates. Furthermore, the stability analysis could be strengthened by providing a more detailed comparison with existing results for inexact PPA algorithms, highlighting the specific challenges introduced by the stochastic nature of the problem and the techniques used to overcome them.

### Questions
1. Remark 2.1: The conditions in Remark 1.1 are insufficient to ensure Assumption 2. For example, consider the indicator function of $x \geq 0$; its subgradient at $x = 0$ is a cone, and thus an unbounded set.
2. Theorem 2.3: Is there an achievable high-probability bound on the distance to the optimal set?
3. Could the assumption ${\rm sup}\\|x_k\\|_2 < \infty$ be removed to obtain a cleaner theoretical result?
4. It would be helpful comment on the impact of minibatch size $m$.
5. Numerical experiments: The applications considered are somewhat outdated, and the datasets used are synthetic. Since the theory targets a more general setting where $f$ and the regularizer are not necessarily convex, it would be valuable to see results on more general machine learning problems with this structure.
6. Numerical experiments: The current experiments resemble an ablation study. It would be helpful to include comparisons with other state-of-the-art algorithms for these problems to demonstrate practical applicability.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes an inexact stochastic proximal point algorithm. It gives conditions that the inexact subproblem solutions should satisfy, and analyzes the convergence of the algorithm based on the conditions being satisfied. Specifically, the paper shows the convergence rate of the distance of current iterate to the optimal solution set is O(k^{-\beta}), and the convergence rate of the residual of current iterate to the exact proximal solution is O(k^{-\beta/2}), where \beta \in (0,1] defines the diminishing stepsize. The experimental results align with the theoretical convergence rates for different values of \beta.

### Strengths
The contribution seems very nice and, as far as I can see, the analysis appears to be sound.

### Weaknesses
1) The paper does not present a general algorithm for solving the proximal subproblem inexactly to satisfy SCA for arbitrary problems. Although Appendix F.1 provides an algorithm, it is specifically designed for problem (4.1). 
2) There is no computation cost and convergence comparison between sPPA and isPPA.

### Questions
1) Line 219: equation (2.2). Why does Criterion SCB imply Criterion SCA?
2) \sup_k ||x_k||_2 < \infinity is a condition in Theorem 2.3 where constant stepsize is used. I’m curious what is the challenge of proving sup_k ||x_k||_2 < \infinity when using constant stepsize. 
3) In Section 2.3, why is the distance ||x - prox_\phi (x)||_2 referred to as the KKT residual?
4) In the experiment setting Line 479, for the  accuracy parameter \epsilon_k = \gamma \alpha_k^2, what is the practical rule for tuning \gamma?
5) Theorem 2.4 uses \epsilon_k = \gamma \alpha_k^{3/2}, which is different from the experiment setting. Does it make a difference? Does Theorem 2.4 specifically rely on the exponent 3/23/2?

### Soundness
4

### Presentation
3

### Contribution
4
