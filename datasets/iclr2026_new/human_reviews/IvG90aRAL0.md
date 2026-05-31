## Human Reviewer 1

### Summary
This paper provides a quantum version of the Frank-Wolfe algorithm for constrained convex optimization. Compared to prior work (Chen & de Wolf, 2023) which deals with regression with l1 and l2 norm constraints, the authors tackles the convex optimization in a more general setting, proposing methods for optimization on a smooth convex function with l1 norm constraints, a simplex constraint or a latent group norm constraint, as well as matrix nuclear norm constraints. Their algorithm can provide quadratic speedups in terms of the dimension of the domain.

### Strengths
1. The paper addresses an interesting problem in quantum optimization and generalizes results to a much larger set of convex optimization problems, extending the applicability of such algorithms from regression to other potential fields such as signal processing (sparsity constraints via l1 norm), game theory (zero sum games with simplex) and SDPs (nuclear norm optimization).
2. Proofs and assumptions are clearly documented, with different scenarios of gradient obtainment for the vector case discussed in detail.

### Weaknesses
1. Cost of additional qubits and gates not provided for Theorem 6 in Table I.
2. Applications of this paper can be more clearly articulated, i.e. what's been listed in strengths 1.
3. Assumption for gradient obtainment in the matrix case seems a bit strong, as the gradient has to be low rank _and_ accessible in a KP tree.

### Questions
1. Given that some previous quantum algorithms that tackle the problem of convex optimization rely on the multiplicative weight update method eg. quantum LP and SDP solvers, I am curious as to how the quantum Frank-Wolfe method proposed in this methods compares to these methods and what potential advantages/disadvantages exist for the quantum Frank-Wolfe method.
2. Why is a different assumption for gradients used for the matrix case different from the vector case? Is the gradient estimation algorithm not applicable to matrix cases? 
3. I think the strength of gradient assumption in the matrix case may be stronger than the membership and separation oracles in ariXiv:1809.00643 as you could obtain such oracles when you have both function and gradient access. How would the algorithm perform this weaker set of assumptions is provided instead of the gradient assumption?

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
4

---

## Human Reviewer 2

### Summary
This work presents a framework for Quantum Frank–Wolfe (QFW) algorithms, extending classical projection-free convex optimization to the quantum setting. The authors design quantum analogues of the Frank–Wolfe method for both vector-domain (e.g., $\ell_1$-ball, simplex constraints) and matrix-domain problems (e.g., trace-norm constraints). By leveraging quantum primitives such as Dürr–Høyer maximum finding, Jordan’s quantum gradient estimation, and quantum singular value estimation (QTSVE), they show their algorithms achieve a $\sqrt{d}$ improvement in dimensional dependence while maintaining the classical convergence rate of $O(1/\varepsilon)$.

### Strengths
1. The manuscript presents proofs and complexity analysis, which seem reasonable.

2. The proposed quantum framework attempts to address a range of convex optimization problems in both vector and matrix domains, including $\ell_1$ norm and trace norm (nuclear norm) constraints.  

3. The manuscript presents a theoretical exploration of quantum algorithms in the context of convex optimization problems.

### Weaknesses
1. The lack of simulations and qubit estimates for the core matrix algorithms (QPM/QTSVE) makes it challenging to assess the practical feasibility and actual performance of the proposed quantum speedups. 

2. The algorithm requires strong quantum oracle access (e.g., normalized row states and function value oracles), which are currently not feasible on NISQ devices.

3. The algorithmic components (quantum maximum finding, SVD estimation, gradient estimation) are not new. 

4. The use of $\tilde{O}$  notation hides constants that could have a significant impact on the practical runtime and performance of the algorithm.

### Questions
1. The QFW algorithm is designed for convex optimization, do you think its techniques could be adapted to solve non-convex problems like BQP, or provide useful insights for tackling such NP-hard problems?

2. How does the quantum acceleration of the Frank-Wolfe algorithm for sparse convex optimization  compare with the optimization methods for bi-quadratic programming over unit spheres (as discussed in [1])  in terms of computational efficiency and the ability to handle high-dimensional optimization problems?
  



[1].  Li, S., et al., Tighter bound estimation for efficient biquadratic optimization over unit spheres, Journal of Global Optimization, 2024.

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
3

---

## Human Reviewer 3

### Summary
The paper studies how quantum computing can accelerate projection-free optimization methods, particularly the Frank–Wolfe (FW) algorithm, which avoids costly projection steps by solving linear subproblems. For example, they studied for $\ell_1$-norm and simplex constraints for vector optimization problems, and nuclear norm constraints for matrix variables.

### Strengths
- Originality: the authors study quantum acceleration for projection-free convex optimization for several classes of optimization problems. They propose some ways to achieve quantum acceleration under the FW framework, like quantum gradient estimation, singular value extraction, et.c.

- Quality: They gave theoretical analysis of their methods, proving a worst case guarantee.

- Clarity: The writing of the paper is good. Their problem formulations, algorithms and theoretical results are presented in a structured way.

- Significance: Projection free methods for optimization is widely used and important in machine learning. Their results show the possibility of quantum speedups in this aspect.

### Weaknesses
The paper’s algorithmic advances rely heavily on existing quantum subroutines—such as quantum maximum finding, gradient estimation, and singular value extraction—raising questions about how much novelty lies beyond combining these tools within the Frank–Wolfe framework. The authors could better articulate what new technical challenges are overcome or what insights are unique to the projection-free setting. For example, what is the novelty of this work on vector variable problems compared with Chen & de Wolf (2023)?

Moreover, the analysis would benefit from a clearer discussion of applicability and limitations. The claimed speedups depend on assumptions like low-rank gradients and favorable spectral gaps; in dense or ill-conditioned cases, the advantage may vanish. Explicitly characterizing these regimes and their practical implications would strengthen the paper’s significance.

### Questions
- Clarification on Novelty and Technical Contributions: Beyond integrating known quantum primitives, what are the key new technical insights or analyses specific to the projection-free (Frank–Wolfe) setting? For example, are there difficulties in ensuring convergence or oracle compatibility that required new ideas?

- Regime of Quantum Advantage: The quantum speedups depend on parameters like the rank, singular value gap, and Lipschitz constants. Could you provide a more explicit characterization of the parameter regimes where your algorithms achieve practical advantage over classical FW? Also, are there examples (synthetic or theoretical) where these advantages disappear or become marginal?

- Clarification of the Matrix-Case Analysis: In the matrix domain, your algorithms assume precomputed gradients. Would including gradient computation change the overall asymptotic complexity or speedup factor? The analysis relies on rank and spectral gap assumptions—can you discuss robustness when these assumptions are only approximately satisfied?

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
4

### Confidence
4

---

## Human Reviewer 4

### Summary
This paper investigates projection-free optimization for sparse convex problems. It proposes two quantum algorithms—handling vector and matrix domains respectively—that achieve improved complexities by reducing the dependence on the dimension d.

### Strengths
The paper is well-written, featuring a clear presentation of the methods, the obtained complexity results, and comparisons with prior works.

### Weaknesses
My primary concern pertains to the paper's motivation. I find the core motivation insufficiently justified. The manuscript does not adequately establish a compelling need for specialized quantum algorithms for this particular class of problems. From my perspective, the proposed method appears somewhat ad-hoc, lacking both a clear demonstration of practical application and the provision of new, general insights for the field of quantum algorithm design.

### Questions
1.	What is the motiveitaion of this paper? Why do we need to solve this type of problem? 
2.	Why do we need to accelerate Frank-Wolfe algorithms? Is it possible to design special algorithm for these sparse learning problems?
3.	Recent advanves in non-convex optimization often solves sparse (low-rank) problem by reformulating the problem by a quadatratic parametrization problem? Why do you work on this way?

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
3

---

## Human Reviewer 5

### Summary
The paper is focused on convex optimization with convex constraints in high dimensional settings. The authors propose a quantum approach for achieving quadratic speedup, in terms of the problem dimensionality, by using quantum computing to solve the subproblems in Frank-Wolfe optimization algorithm.

### Strengths
The paper provides an original approach towards solving constraint optimization problems. The significance of the result is diminished, as noted in weaknesses, but deficiencies in complexity analysis of the method and its assumptions. The paper is clearly written, although the assumptions should be more prominently analysed.

### Weaknesses
The main weakness involves unrealistic assumptions that affect the complexity of the full algorithm. For example, step 7 in Alg. 2 involves preparing, in each Frank-Wolfe iteration, a state
$\sum_{i=0}^{d-1}|i>|x^{(t)}>|0>$, with $|x>$ defined in Assumption 3 to be $|x> = |x_1>|x_2>…|x_d>$. The state is over $d+2$ qubits. Similar qubit $O(d)$ qubit requirement is present in the rest of scenarios considered in the paper. This linear qubit requirement severely limits the applicability of the method for the stated goal of addressing high dimensional (high $d$) optimization problems. 

Preparing a $d$-dimensional arbitrary qubit state is hard in general, yet the impact of this step on the complexity of the whole method is not discussed.

Some terminology could be revised, e.g. authors mention “sparsity-constrained problems” in the introduction, but actually address L1 norm and not L0 norm constraints.

### Questions
Are there any specific properties of $|x^{(t)}>$ over the iterations that would make state preparation efficient?

### Soundness
3

### Presentation
3

### Contribution
2

### Rating
2

### Confidence
3