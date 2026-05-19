# A Computation and Communication Efficient Projection-free Algorithm for Decentralized Constrained Optimization

- Decision: Reject
- Scores: 6, 3, 5

## Abstract
Decentralized constrained optimization problems arise in numerous real-world applications, where a major challenge lies in the computational complexity of projecting onto complex sets, especially in large-scale systems. 
The projection-free method, Frank-Wolfe (FW), is popular for the constrained optimization problem with complex sets due to its efficiency in tackling the projection process. 
However, when applying FW methods to decentralized constrained finite-sum optimization problems, previous studies provide suboptimal incremental first-order oracle (IFO) bounds in both convex and non-convex settings. 
In this paper, we propose a stochastic algorithm named Decentralized Variance Reduction Gradient Tracking Frank-Wolfe ($\texttt{DVRGTFW}$), which incorporates the techniques of variance reduction, gradient tracking, and multi-consensus in the FW update to obtain tight bounds. 
We present a novel convergence analysis, diverging from previous decentralized FW methods, and demonstrating $\tilde{\mathcal{O}}(n+\sqrt{\frac{n}{m}}L\varepsilon^{-1})$ and $\mathcal{O}(\sqrt{\frac{n}{m}}L^2\varepsilon^{-2})$ IFO complexity bounds in convex and non-convex settings, respectively. 
To the best of our knowledge, these bounds are the best achieved in the literature to date. Besides, in the non-convex case, $\texttt{DVRGTFW}$ achieves $\mathcal{O}(\frac{L^2\varepsilon^{-2}}{\sqrt{1-\lambda_2(W)}})$ communication complexity which is closed to the lower bound $\Omega(\frac{L\varepsilon^{-2}}{\sqrt{1-\lambda_2(W)}})$. 
Empirical results validate the convergence properties of $\texttt{DVRGTFW}$ and highlight its superior performance over other related methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper studies the decentralized constrained finite-sum optimization problem and provides a projection-free algorithm called DVRGTFW. In the convex and non-convex cases, the sample complexities $\mathcal{O}(n+\sqrt{n/m}L\varepsilon^{-1})$ and $\mathcal{O}(\sqrt{n/m}L^2\varepsilon^{-2})$ are established, respectively. Numerical experiments validate the performance of the algorithm.

### Strengths
The paper shows better theoretical convergence results compared to previous works. Specifically, by incorporating techniques such as gradient tracking and multi-consensus, it extends constrained finite-sum algorithms to the decentralized setting. The convergence of DVRGTFW is analyzed using Lyapunov functions, theoretically establishing improved sample and communication complexities, which is also validated by numerical experiments.

### Weaknesses
While improved theoretical results are established for decentralized Frank-Wolfe method, the techniques are overall similar to existing ones.

### Questions
1. Should the sample complexity in the non-convex case be $\mathcal{O}(n + \sqrt{n/m}L^2\varepsilon^{-2})$? Letting $m = 1$, the problem reduces to the centralized finite-sum setting, where the sample complexity should be $\mathcal{O}(n + \sqrt{n}\varepsilon^{-2})$ or $\mathcal{O}(n\varepsilon^{-2})$, as shown in [1].

2. In Table 1, is a direct comparison of convergence rates with [2] appropriate? Specifically, this paper addresses a finite-sum problem, whereas [2] deals with an online setting. Since DVRGTFW cannot be directly applied to the online problem, such a comparison may be inappropriate. The authors should at least point out the differences in settings when making these comparisons.

3. Finally, there are some minor issues, such as typos. 
- The Lyapunov functions defined in L.739 use the symbols  $\Phi$  and  $\Psi$ , but in several places in the following proofs, they are written as  $\phi$  and  $\psi$  (L.994, L.1069, L.1076, L.1082, and L.1085).
- L.818. ``fastMix'' should be ``FastMix''.
- The paper [1] has been accepted in ICML and the reference should be updated.

---
References

[1] Aleksandr Beznosikov, David Dobre, and Gauthier Gidel. Sarah frank-wolfe: Methods for constrained optimization with best rates and practical features. In ICML, 2024.

[2] Hoang Huy Nguyen, Yan Li, and Tuo Zhao. Stochastic constrained decentralized optimization for machine learning with fewer data oracles: a gradient sliding approach. arXiv preprint arXiv:2404.02511, 2024.

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
5

### Summary
This paper develops a decentralized stochastic Frank-Wolfe algorithm and establishes its convergence rate for both convex and nonconvex constrained problems. The experiment demonstrates the effectiveness of the proposed algorithm.

### Strengths
1. This paper is well written. It is easy to follow.

2. The literature review is good.

### Weaknesses
1. The novelty is limited. Decentralized unconstrained optimization has been well studied. This paper tries to extend those algorithms to constrained problem, where the feasible set is bounded. However, this extension is trivial. In particular, due to the bounded feasible set, it is trivial to bound the gradient variance. Actually, the proof for frank-wolfe algorithm is much easier than the unconstrained counterpart.

2. As mentioned in this paper, there are some existing decentralized Frank-wolfe algorithms for DR-submodular optimization problems. What is the difference between those algorithms and this paper? Are there any unique challenges compared to those algorithms? It would be good if the authors could discuss these critical points to show the contribution of this paper. 

3. FastMix is a not very common communication method. It would be good to provide some background for this method. For example, in standard gradient tracking method, it is well known that $\bar{v}_t=\bar{y}_t$. Does FastMix also have this property? It seems the authors directly use $\bar{v}_t=\bar{y}_t$ in the proof. 

4. It would be good to provide more details about the proof. For example, how to get the third step in Line 764? It is not very clear. 

5. How does the heterogeneity affect the convergence rate? 

6. Why does IFO not depend on the spectral gap? Any explanation?

### Questions
Please see Weakness.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
In this paper, the authors proposed to combine the Frank-Wolfe algorithm with variance reduction as well as gradient tracking in the decentralized setting, resulting in the algorithm DVRGTFW. Convergence analysis in the convex and non-convex case are provided with numerical experiments conducted to further support the theory provided.

### Strengths
1. The author manages to combine the technique of variance reduction and gradient tracking to Frank-Wolfe algorithm in the decentralized setting, convergence analysis in both convex case and non-convex case are provided, illustrating the effectiveness of the proposed algorithm DVRGTFW.

2. The proposed algorithm achieves best-known incremental first order oracle complexities both in the convex case and in the non-convex case, and near optimal communication complexity in the non-convex case.

3. The paper offers numerical experiments to validate the theory presented in the paper.

### Weaknesses
1. Though the results are interesting, the proposed method appears to be primarily a combination of established techniques, such as variance reduction, gradient tracking, and the Frank-Wolfe algorithm. As a result, the novelty of the approach may be somewhat limited.

2. If I am not mistaken, the communication complexity for DVRGTFW is not better than existing methods in the convex case given its extra dependence on $\sqrt{mn}$ as it is demonstrated in Table 1, which is a limitation of the algorithm.

3. I recommend that the authors do a thorough check of the paper as there are many typos, some of them are confusing, such examples include:
- At line 92, ''develop communication and communication efficient'';
- At line 114, $m = 0$;
- At line 222, $x_0 \in \mathbb{R}^d$,
- There are also some notations used without introduction in the paper.

4. In some of the numerical experiments, the proposed algorithm is not better than existing algorithm for an unclear reason.

### Questions
1. In table 1, when $m = 1$, we should recover the complexities in the centralized setting in the convex/non-convex setting, however, for the proposed algorithm, the reviewer does not understand why it matches the bounds given in [Beznosikov et al., 2023], for example, in the convex case the table suggests $\tilde{\mathcal{O}}(n + \frac{\sqrt{n}}{\varepsilon})$, while [Beznosikov et al., 2023] gives $\tilde{\mathcal{O}}(n + \frac{1}{\varepsilon})$.

2. What is the output of Algorithm 2 FastMix? 

3. Is it possible to further improve the communication complexity of the algorithm so that it matches the optimal bounds?

### Soundness
3

### Presentation
2

### Contribution
2
