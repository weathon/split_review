# Convergence Analysis of Gradient Descent under Coordinate-wise Gradient Dominance

- Decision: Reject
- Scores: 5, 6, 5, 5

## Abstract
We consider the optimization problem of finding Nash Equilibrium (NE)  for a nonconvex function $f(x)=f(x_1,...,x_n)$, where $x_i\in\mathbb{R}^{d_i}$ denotes the $i$-th block of the variables. 
Our focus is on investigating first-order gradient-based algorithms and their variations such as the block coordinate descent (BCD) algorithm for tackling this problem. 
We introduce a set of conditions, termed the $n$-sided PL condition, which extends the well-established gradient dominance condition a.k.a Polyak-{\L}ojasiewicz (PL) condition and the concept of multi-convexity. This condition, satisfied by various classes of non-convex functions, allows us to analyze the convergence of various gradient descent (GD) algorithms. 
Moreover, our study delves into scenarios where the objective function only has strict saddle points, and normal gradient descent methods fail to converge to NE. In such cases, we propose adapted variants of GD that converge towards NE and analyze their convergence rates.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper focuses on solving non-convex problems and, in particular, aims to design methods for finding Nash Equilibrium. The paper proposes the n-sided PL condition and provides convergence guarantees for different block coordinate descent methods (BCD, IA-RBCS,  and A-RBCD) under this new assumption. Applications of where the assumption is satisfied and some preliminary experiments are presented.

### Strengths
The paper is well-written, and the idea is easy to follow. The authors did a very nice job in the narrative of the paper. The explanation of their new assumption, applications of where this assumption appears, and the theoretical analysis are clearly presented.

### Weaknesses
I believe there are a few issues in terms of using specific terminology that are not standard, and the author might need to revise.

1. The notion of Nash Equilibrium (NE) is very popular in min-max problems and multi-agent games. However, the paper focuses on pure minimization problems and defines NE as a standard concept, which is not typically the case. How is their NE equilibrium related to the minimizer of the function they are trying to optimize? This i believe was not clearly presented in the paper. 

2. I believe the notion G_f(x) should be more carefully presented and explain why this is a valid measure of convergence. Why is showing that f(x^t) - G_f(x^t) reduces enough to guarantee convergence to global minima (again, this is related to the notion of NE)? I would appreciate it if the authors provide more details on this. 

3. Why does Assumption 3.4 make sense? This looks like a very artificial condition to have just to make the proof work. This shows that one example (in Fig 1) satisfies, but that does not mean that this is a relaxed condition. More explanation is needed

4. The paper is clearly theoretical, but I would appreciate it if the authors compared their proposed method with state-of-the-art approaches for training Linear Residual Networks and Infinite Horizon n-player Linear-quadratic (LQR) Game. In my opinion, this is very important for the paper as then it would convey the message that through the new assumption, we not only provide new convergence guarantees but that via the new analysis and algorithms, we can more efficiently solve these practical problems.

### Questions
See Weaknesses above

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
The paper focuses on the problem of finding Nash Equilibrium for function $f(x)$ having a block form $f(x)=f(x_1, …, x_n)$. The paper introduces $n$-sided PL condition which extends the notion of PL condition to functions with block structure. Under this weaker assumption the algorithm Block Coordinate Descent is analyzed and its convergence to set of NE points is proven. Under additional assumption on the alignment of gradients of $f$ and $G_f$, linear convergence of BCD and vanilla GD is proven. Furthermore, the algorithms Adaptive randomized Block Coordinate Descent and its oracle version are proposed and their convergence rate is analyzed without the additional assumption on gradient alignment.

### Strengths
Overall, the paper is well written and uses simple examples to provide intuition for important concepts. The strengths of the paper are as follows:
1. The assumption $n$-sided PL condition introduced in the paper is a weaker notion than two-sided PL condition making the results more general. The assumption is weaker in the sense that under this the stationary points are not guaranteed to be global minimums.
2. Linear convergence guarantee is proven for BCD and GD under $n$-sided PL condition and gradient alignment assumption.

### Weaknesses
1. Insufficient empirical evidence presented for demonstrating the benefits of the proposed variant: a. Comparison with BCD method is missing for the experiments with Linear Residual Network and Infinite Horizon $n$-player LQR game. It gives empirical comparison of convergence rate of BCD and A-RBCD which would be helpful. b. The variant A-RBCD requires significantly more gradient computation than BCD. It would be beneficial to have comparison keeping the gradient computation budget constant across different methods. c. Furthermore, adding SGD and Adam as baselines would make the experiments more persuasive.

2. The theoretical convergence analysis relies on the assumption that the algorithm predominantly operates in cases 1 or 2, as defined by Assumption 3.5. While the authors argue that case 3 is rare, the analysis does not provide a concrete upper bound on the number of iterations the algorithm might spend in case 3. The provided bound on the expected value of $f(x^T) - G_f(x^T)$ is weakened by the term $(1 - \frac{(L+L')\mu\alpha^2}{4})^{T-T_3}$, where $T_3$ represents the number of iterations in case 3, and no bound on $T_3$ is given. This makes the linear convergence guarantee less robust, as a large $T_3$ could significantly degrade the convergence rate. The lack of a bound on $T_3$ makes it difficult to assess the practical implications of the theoretical results.

3. It would be helpful to highlight the differences between IA-RBCD and A-RBCD that arise due to using approximate best responses.
4. The Figure 5d is used to claim that the third case does not occur while executing the A-RBCD algorithm. I suppose the point being made is that $\rho\leq \gamma-\gamma\frac{\alpha^3}{13}$. A clarification regarding the same would be appreciated. If the graph could indicate the line $y=\gamma-\gamma\frac{\alpha^3}{13}$ that would make it much easier to understand.

### Questions
1. It would be helpful to highlight the differences between IA-RBCD and A-RBCD that arise due to using approximate best responses.
2. The Figure 5d is used to claim that the third case does not occur while executing the A-RBCD algorithm. I suppose the point being made is that $\rho\leq \gamma-\gamma\frac{\alpha^3}{13}$. A clarification regarding the same would be appreciated. If the graph could indicate the line $y=\gamma-\gamma\frac{\alpha^3}{13}$ that would make it much easier to understand.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper focuses on the convergence rates of block coordinate descent algorithms under an $n$-sided PŁ condition. Based on an adaptive, theoretical algorithm IA-RBCD that provably converges to the NE of a minimization problem of an $n$-sided PŁ objective, the paper proposes a novel algorithm A-RBCD that is implementable via computing the approximate best response and shows the same convergence speed as the ideal version. The paper also shows empirical results in various practical settings involving $n$-sided PŁ functions.

### Strengths
- I believe that extending ideas from convex/nonconvex or minimax optimization to multi-player games is a valuable direction to study and develop further. The $n$-PŁ condition might be useful in many cases, especially in handling stuff on nonconvex (and nonconcave) games.
- Experiments are well-aligned with the theorems. The results all demonstrate and support exactly what’s in the theoretical statements.
- The overall writing is clear and easy to follow.

### Weaknesses
 - **W1.** I don’t get why and when could finding an NE for a *minimization* problem be an important thing. In Figure 1, the set of stationary points (which is equal to the set of Nashes for $n$-PŁ functions) might contain saddle points. Indeed we would want to find Nashes for minimax or multi-player game settings, but for (nonconvex) minimization problems it’s usually also important to *avoid* possible saddles among stationary points (Lee et al., 2016). I get that there might be cases when we won’t care about saddles and just want to find stationary points, maybe as in the example function with only strict saddles points in Section 4, but still, I think it’s not clear in the paper about why this search for NE’s and the $n$-PŁ assumption could be a really necessary or interesting thing.
- **W2.** In the theorems, everything related to Case 3 makes the theoretical contribution of this paper quite weak. While empirical results in Figure 5 suggest that Case 3 never really happens here, there should have been a better explanation than just saying ‘rigorously verifying these cases is intractable’. There are no lower bound results, i.e., which means that there could be pathological cases that get stuck in Case 3 for a long time, and the $n$-PŁ assumption isn’t powerful enough. In fact, we already need a stronger $(\nu, \theta)$-PŁ assumption to get non-asymptotic results for Case 3, which is even sublinear.
- **W3.** Continuing from **W2**, the main results all state no more than case-specific one-step contraction inequalities. These should have been conclusively rewritten in terms of iteration complexities for a complete understanding of the convergence rate of this algorithm. This will include quantifying how rare Case 3 happens (or maybe when exactly can we make it rare), and seeing what convergence rate we get after fixing a single step size (or possibly a schedule) considering all three cases.

### Questions
- Can you explain further about what I wrote in W1? When could it be important to find Nashes in minimization problems? Or, in a slightly different perspective, could these algorithms generalize to multi-player games with adversarial components?
- Have you checked if the proposed algorithms are capable of further avoiding saddles if possible either explicitly, or in some sort of an ‘implicit-bias’ sense? We don’t have any evidence proving/disproving this since, in the experiments in the paper, for the first quadratic case the only option is a saddle, while for the rest of the cases, we can only see $f(x) - G_f(x)$ from which we cannot distinguish saddles from minima.
- Case 3 happens when the vectors $\nabla f(x_t)$ and $\nabla G_f(x_t)$ are not well-aligned (or $\| \nabla G_f(x_t) \|$ is much larger than $\| \nabla f(x_t) \|$… which probably won’t happen). While by definition of $G$ it seems intuitive that the two gradients will eventually align together near the stationary points (while both converging to zero vectors), are there any ideas to quantify or theoretically analyze this part a bit further?

TYPO. Page 6, converges sublinearly for $f_1$ (instead of $f_2$)

TYPO. Algorithm 4, $x_{-j}^t \rightarrow x_{-j}$ (while we use $x = x^t$ in Algorithm 3)

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work explores the optimization of finding a Nash Equilibrium for nonconvex functions using first-order gradient-based algorithms and their variations, such as block coordinate descent. The authors introduce the n-sided PL condition, an extension of the PL condition. Then, under this condition, they analyze the convergence of various variants of gradient descent algorithms. They provide theoretical proofs of convergence rates for these algorithms and examine conditions under which linear convergence can be guaranteed.

### Strengths
The main strengths of this work are:
-The authors extended the PL condition to the n-sided PL condition. 
-The authors proposed adapted variants of the gradient descent (GD) and block coordinate descent (BCD) algorithms and demonstrated the convergence to Nash Equilibrium of these methods.
-The authors provided theoretical proofs for the convergence rates of the proposed algorithms and established conditions under which linear convergence can be guaranteed.
-The authors provide some numerical tests to validate their claims.

### Weaknesses
 The main weaknesses of this work are:
-Dependence on Strong Assumptions: I understand that the authors gave some toy examples and linear NN that satisfy the assumptions however in general these assumptions remain strong and hard to check. Specifically, the n-sided PL condition, while a generalization of the standard PL condition, still requires a specific structure of the objective function. It is not clear how to verify this condition for general non-convex functions, and the provided examples are not sufficiently complex to demonstrate the practical applicability of this assumption. The assumption that gradients of f and G_f are well-aligned at the iterates is also a significant hurdle, as this is not guaranteed in general non-convex settings and requires further justification.
-The empirical validation is focused on simple toy examples and linear NN. The performance of the proposed algorithms on large-scale or more complex problems is not deeply explored, making it uncertain how well the algorithms scale in practice. The authors may consider including some tests on bigger problems to assess the numerical efficiency of the proposed variants, even if the conditions to converge are not necessarily satisfied. The current empirical results do not provide a strong case for the practical relevance of the proposed methods, as they only demonstrate performance on limited cases.
-The paper lacks a detailed computational complexity analysis of the proposed variants (the cost per iteration compared to the classical GD or BGD). The added steps (like approximating best responses in certain cases) introduce computational overhead, especially for high-dimensional data, and it’s unclear how these adaptations perform against standard or simpler gradient-based methods in terms of cost/runtime. The analysis should include the cost of computing the best response approximations, as this can be a significant factor in the overall runtime.
-The adaptive algorithms, particularly with the introduction of conditions for selecting step sizes and updating directions, could be challenging to implement efficiently in practice. The conditions for switching between cases in the algorithms are not straightforward to evaluate and may introduce significant overhead. Furthermore, the paper does not discuss the practical challenges of tuning the parameters involved in these adaptive steps.

### Questions
-See the previous section.
-Lines 251-252 you mentioned "The above result ensures the convergence of BCD to the NE set, but it does not necessarily indicate whether the output converges to a point within the NE set." can you give an example where this is the case? i.e. we have the convergence to the NE set but not the convergence to a point in the set. 
-Line 292: can you explain why f(x) = G_f(x) if and only if x is NE.
-Assumption 3.4. you require the condition (5) for a given set of points. But how can one know this set of points beforehand? you mentioned just after that for instance, for f_0 this assumption is valid for some domain, but the iterations of a given algorithm applied to this problem may leave this domain in the middle of the algorithm.
-Can you tell why Ass 3.4 for instance holds for strongly convex functions?
-In thm 3.6 in the linear rate of convergence, since \mu, \alpha and \kappa "do not depend" on "n" this rate can be negative for large "n"?
-Definition 3.8, do you really need the minimum to be zero?

### Soundness
2

### Presentation
3

### Contribution
2
