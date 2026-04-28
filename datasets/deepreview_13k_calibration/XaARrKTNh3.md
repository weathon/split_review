# A Catalyst Framework for the Quantum Linear System Problem via the Proximal Point Algorithm

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 5, 6

## Abstract
Solving systems of linear equations is a fundamental problem, but it can be computationally intensive for classical algorithms in high dimensions. Existing quantum algorithms can achieve exponential speedups for the quantum linear system problem (QLSP) in terms of the problem dimension, but even such a theoretical advantage is bottlenecked by the condition number of the coefficient matrix. In this work, we propose a new quantum algorithm for QLSP inspired by the classical proximal point algorithm (PPA). Our proposed method can be viewed as a meta-algorithm that allows inverting a modified matrix via an existing \texttt{QLSP\_solver}, thereby directly approximating the solution vector instead of approximating the inverse of the coefficient matrix. By carefully choosing the step size $\eta$, the proposed algorithm can effectively precondition the linear system to mitigate the dependence on condition numbers that hindered the applicability of previous approaches.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper investigates the quantum linear system problem (QLSP), which aims to produce a quantum state encoding the solution vector $x$ for a given matrix $A$ and vector $b$, such that $Ax = b$, assuming quantum query access to $A$ and $b$. The current best-known algorithm for QLSP achieves a query complexity of $O(\kappa \log \epsilon^{-1})$, where $\kappa$ is the condition number of $A$ and $\epsilon$ is the target error. While this result offers an exponential speedup in terms of $N$, the dimension of the system, the algorithm’s query complexity scales linearly with $\kappa$. Prior work has established that this linear dependence on $\kappa$ is unavoidable in the worst case, reducing the quantum advantage for poorly conditioned matrices.

This paper partially addresses this limitation by introducing a meta-algorithm for QLSP based on the proximal point algorithm (PPA)—a classical iterative optimization technique. This framework can be applied to any existing quantum linear system algorithm (QLSA) to modulate the tradeoff between solution precision and condition number. When applied to the current state-of-the-art QLSA, this meta-algorithm yields a constant-level improvement across a range of precision requirements, thereby extending the practical applicability of quantum linear system solvers.

### Strengths
This paper introduces a novel framework that enhances the dependence on the condition number $\kappa$ in quantum algorithms, while incorporating additional problem-dependent parameters. In the worst-case scenario, it achieves a significant constant-factor improvement over the existing state-of-the-art algorithm. The framework also includes a tunable parameter $\eta$, allowing users to adjust the balance between runtime and approximation error.

### Weaknesses
1. The meta algorithm itself is relatively simple, and the techniques used to analyze the problem is not extremely complicated.
2. The algorithm introduces additional problem-specific parameters, such as, $\Psi$ and $d\coloneqq ||x_0-x^*||$. Moreover, the paper did not provide a very thorough discussion on these parameters.

### Questions
1. Can the authors provide more discussions on these additionally introduced parameters?
2. Can the authors give a more detailed discussion on how the tradeoff between the runtime and the approximation error is achieved from the bound in Theorem 6?

### Soundness
4

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
4

### Summary
This paper proposes a novel meta-algorithm for solving the quantum linear system problem (QLSP) based on the proximal point algorithm (PPA). The performance of quantum linear system solvers heavily depends on the condition number of the linear system. Due to a query lower bound result, the linear dependence on condition number can not be further improved (in the asymptotic scaling sense). This paper incorporates the proximal point algorithm as a pre-conditioner of a QLSP solver. The new proximal-point QLSS can leverage the trade-offs between the approximation error (in the output solution) and the condition number of the linear system. It is proven that a finite stepsize mitigates the condition number, at the cost of making the resulting solution inexact. Numerical results show this new approach can lead to a generic (constant) speedup in solving linear systems over existing STOA.

### Strengths
- This paper exploits the proximal point algorithm to reformulate the original linear system problem as an approximate optimization problem, where the new problem is parametrized by the "step size" $\eta$. This new parameter provides a continuous interpolation from the original problem (for $\eta = +\infty$) to a pre-conditioned problem (for small $\eta$). This is an interesting point of view and also the first proposal to combine the proximal point algorithm with a quantum linear system solver (to my best knowledge).
- Numerical results show that this approach reduces the total query complexity over the STOA quantum linear system solver.

### Weaknesses
 - My main concern is that the proximal point algorithm proposed in this paper can have a **single** iteration. This feature makes this algorithm less useful in practice. The main difficulty is that the state preparation oracle (see Definition 2) is hard (or maybe impossible) to construct for subsequent steps. Specifically, the proposed method relies on efficiently implementing the operator $(I + \eta A)^{-1}$. While the paper suggests using block encoding and a polynomial approximation for matrix inversion, the practical challenge of constructing the state preparation oracle for the resulting block-encoded matrix, especially after multiple iterations, is not adequately addressed. The state preparation for $(I + \eta A)^{-1}$ is not a trivial extension of the state preparation for $A$, and the paper does not provide sufficient details on how this can be achieved efficiently.
- While it is discussed that a multi-step PPA can be realized by implementing different powers of the modified matrix, it is not clear why this would lead to asymptotic speedup because inverting $(I + \eta A)^n$ for $n \ge 2$ is likely to incur a super-linear overhead in the condition number. I would conjecture that the naive multi-step PPA will lead to a polynomial slowdown compared to the quantum STOA. The paper mentions that implementing the addition of two block-encoded matrices approximately doubles the query complexity, but it does not provide a concrete analysis of how the improvement in the condition number from a two-step PPA can compensate for this overhead. A more rigorous analysis is needed to justify the potential benefits of multi-step PPA.
- I do not understand how this PPA approach is compared to an "exact" quantum linear system solver, because this PPA approach can only perform a single iteration step so the solution is not exact. Can the authors elaborate on how a fair comparison is achieved? Is the error budget for both methods pre-fixed? The paper states that the comparison is fair because the error budget is prefixed, but it does not clarify how the error budget for the single-step PPA is determined to be comparable to the error budget of an iterative quantum linear system solver. The single-step PPA produces an approximate solution that is parameterized by $\eta$, and it is not clear how to set $\eta$ to ensure that the error is within the same budget as the iterative solver.

### Questions
Besides the questions that are raised in the "Weaknesses" part, I have the following questions:
- Is there a practical way to choose the stepsize $\eta$ in the algorithm? What if the obtained solution is still far from the exact solution to the linear system?
- Is it possible to use the PPA solution as a "warm start" in a quantum linear system solver, which might be helpful to improve the overall performance?
- Can the authors further elaborate on how the comparison is made in Figure 1? Is it fair to include a $c$ parameter in Algorithm 1?

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
This paper is a good attempt to make QLSA more practical although there is no theoretical improvement in the bigO complexity. However, the authors did not discuss how large the “constant” improvement could be if someone wants to “read out” the quantum solution. In fact, an issue would appear in that regime and limit the “constant” improvement.

### Strengths
The proposed approach is easy to plug in any quantum linear systems solver. Improving the conditional number is one of the most important tasks in QLSA.

### Weaknesses
As demonstrated in Figure 1, kappa^hat is less than kappa/2. According to lemma 1, parameter eta would be less than kappa-2 (or simply kappa). According to the eta choice in theorem 3, if we simply use eta less than kappa, then we have epsilon_2 larger than d. Recall that epsilon_2 is the accuracy for x_{t+1}-x^* as in equation 14, which is the accuracy people care about in the classical setting. This means, if someone wants to eventually read out the quantum solution, ignoring the error from the reading-out process, the accuracy of the classical solution will be very low because the accuracy is at most d and d is simply the initial accuracy. If we don’t want to read out the solutions, the applicability will be significantly limited.

A side comment: the notations of a quantum state are not consistent, i.e., some of them use the braket notation while some do not.

### Questions
See the weakness above.

### Soundness
2

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
3

### Summary
Quantum linear system problem (QLSP) is of great importance in quantum algorithms, which focuses on solving a system of linear equations, i.e., find a state $\ket{x} = x/\|x\|$ where $x$ is the solution to $Ax=b$. QLSP problem is fundamental as it is a key step in many quantum algorithms, such as quantum recommendation systems and solving differential equations. However, a major limitation of the QLSP solver is that the complexity has a linear dependence of the condition number $\kappa$ of the matrix $A$. Whether one can alleviate this issue is also of general interest.

In this paper, the authors propose a new algorithm based on proximal point algorithm (PPA) to reduce the query complexity in solving QLSP in a constant degree. To achieve this acceleration, the authors uses the technique of shifting the matrix $A$ of the problem to $I+\eta A$, leading to the change of condition number of the problem. In addition, the authors also draw some graphs to demonstrate the acceleration.

### Strengths
The authors propose a new algorithm (PPA for QLSP) to alleviate the linear dependence on condition number of the QLSP solvers, yielding a constant acceleration of previous QLSP solvers.

### Weaknesses
First, a main technical tool is the use of PPA algorithm for shifting, which might lack novelity. 
Second, the proofs of the main theorems seems straigthforward and incremental. 
Also, it looks like more numerical experiments could be conducted to demonstrate the actual performance of their proposed algorithm.
Furthermore, I am not sure whether the topic of this paper fits for the scope of ``learning represenations''.

- In Theorem 3, the parameter $\eta$ is set to $\kappa (d/\varepsilon_2 - 1)$, but $\kappa$ may be unknown. Could the authors explain what to to if $\kappa$ is not known?

- In Theorem 6, it seems that difference between the modified condition number $\hat{\kappa}$ and $\kappa$ has a linear dependence on $\Psi$, which relies on the choice of $x_0$ and $\eta$. Could the authors explain more about how to choose $x_0$ and $\eta$?

- Page 9, Line 482: proximal poin algorithm —> proximal point algorithm.

- Page 14, Line 733: the codes in algorithm 2 for Hamilonian simulation could be improved for readability.

### Questions
- In Theorem 3, the parameter $\eta$ is set to $\kappa (d/\varepsilon_2 - 1)$, but $\kappa$ may be unknown. Could the authors explain what to to if $\kappa$ is not known?

- In Theorem 6, it seems that difference between the modified condition number $\hat{\kappa}$ and $\kappa$ has a linear dependence on $\Psi$, which relies on the choice of $x_0$ and $\eta$. Could the authors explain more about how to choose $x_0$ and $\eta$?

- Page 9, Line 482: proximal poin algorithm —> proximal point algorithm.

- Page 14, Line 733: the codes in algorithm 2 for Hamilonian simulation could be improved for readability.

### Soundness
3

### Presentation
2

### Contribution
3
