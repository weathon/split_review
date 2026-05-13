# Accelerated Over-Relaxation Heavy-Ball Method: Achieving Global Accelerated Convergence with Broad Generalization

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
The heavy-ball momentum method accelerates gradient descent with a momentum term but lacks accelerated convergence for general smooth strongly convex problems. This work introduces the Accelerated Over-Relaxation Heavy-Ball (AOR-HB) method, the first variant with provable global and accelerated convergence for such problems. AOR-HB closes a long-standing theoretical gap, extends to composite convex optimization and min-max problems, and achieves optimal complexity bounds. It offers three key advantages: (1) broad generalization ability, (2) potential to reshape acceleration techniques, and (3) conceptual clarity and elegance compared to existing methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a variant of the classical heavy-ball method, where the key modification involves replacing $\nabla f(x_k)$ with its over-relaxation $2 \nabla f(x_k) - \nabla f(x_{k-1})$. It can be regarded as a discretization of the rotated gradient flow introduced by (Chen & Luo, 2021). By employing a Lyapunov function, the authors prove that the proposed method achieves the optimal linear convergence rate for smooth strongly convex minimization problems. They further extended their results to the composite setting and strongly-convex-strongly-concave saddle point problems with bilinear coupling.

### Strengths
- It is known that the classical heavy-ball method cannot achieve the accelerated rate for general smooth strongly-convex optimization problems. The contribution of this paper is to show that, with a simple modification, a heavy-ball-like method can indeed achieve acceleration. 
- The proof technique is conceptually simpler than the standard approach used in accelerated gradient methods, such as the estimate sequence. Furthermore, this technique is adaptable to more general settings, as evidenced by the extensions provided in the paper.

### Weaknesses
 - The main drawback is that other acceleration methods, such as Nesterov's accelerated gradient (NAG) and its extensions, are known to achieve similar convergence guarantees in the considered settings. As such, the advantage of the proposed algorithm over these existing methods remains unclear. This is further illustrated in the numerical experiments, where the proposed method exhibits comparable performance to NAG. Therefore, I have reservations about referring to the result as a "breakthrough." 
- Another limitation is that the paper focuses solely on the strongly convex setting. It is unclear if an accelerated rate can also be achieved in the more general convex setting.

### Questions
- It appears that the proposed method resembles the accelerated method proposed by Thekumparampil et al. (2022), albeit from a different perspective. Specifically, they presented an accelerated method for strongly convex minimization problems in equation (11). If the variable $x_k$ is eliminated, the resulting update rule resembles 
$$x_{k+1} = x_k - \gamma (\nabla f(x_k) - \theta \nabla f(x_{k-1}))+ \beta (x_k - x_{k-1}),$$
where $\gamma,\theta,\beta$ are some constants. A detailed comparison will be helpful. 

-The notation of $\mathbf{x} = (x,y)^\top$ could be confusing. I suggest the authors use a different symbol, such as $\mathbf{z}$, to represent the concatenation of $x$ and $y$.

---- 
Thekumparampil, Kiran K., Niao He, and Sewoong Oh. "Lifted primal-dual method for bilinearly coupled smooth minimax optimization." AISTATS 2022.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a variant of heavy-ball momentum acceleration that provably achieves the optimal linear convergence rate with the factor of $\sqrt{\kappa}$ for smooth strongly convex functions, amending the previous heavy-ball momentum method that does not accelerate in this setting. The proposed framework is further extended to composite optimization and saddle point optimization. Numerical results are provided to validate the theory.

### Strengths
1. The proposed method improves heavy-ball momentum, a well-known and widely applied method, to achieve acceleration for strongly convex functions.
2. Comprehensive extensions to composite optimization and saddle point optimization are also included.

### Weaknesses
1. The paper can be further improved if the authors could include some more intuitive discussion on why the over-relaxation is applied to approximate the gradient in line 110.


### Questions
1. How are the convergence rate and practical performance of AOR-HB for non-strongly convex functions? Does the proposed modification also achieve the optimal $O(1/T^2)$ rate or is the method limited to strongly convex functions?
2. In Figure 2, the HB method also achieves fast linear convergence, faster than all the other methods. Why is it the case and wouldn't this weaken the motivation of the paper? Are there more empirical evidence to demonstrate the contrast between HB and AOR-HB in terms of optimizing strongly convex functions?

### Soundness
4

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
3

### Summary
The paper introduces Accelerated Over-Relaxation Heavy-Ball method which can converge at an accelerated rate for strongly-convex objective functions.

### Strengths
The authors provide proofs for the convergence of their AOR-HB method for smooth, strongly-convex objective function. The method is also proved to achieve convergence for a class of non-smooth optimization and min-max problems.

### Weaknesses
The AOR-HB method is very similar to Nesterov Acceleration (details in questions).



### Questions
Nesterov Acceleration (NAG) can be defined as $v_k = w_k + \beta (w_k - w_{k-1})$ and $w_{k+1} = v_k - \gamma \nabla f (v_k)$. We can eliminate term $w_k$ and achieve
$$
v_{k+1} = v_k - \gamma \nabla f (v_k) + \beta (v_k - v_{k-1}) - \gamma \beta [ \nabla f (v_k) - \nabla f (v_{k-1})] 
$$
$$
v_{k+1} = v_k - \gamma \beta [ (1 + \frac{1}{\beta}) \nabla f (v_k) - \nabla f (v_{k-1})] + \beta (v_k - v_{k-1})
$$
So the only difference if 1 versus $\frac{1}{\beta}$ (where $\beta$ is close to 1) as I understand, can you elaborate more on the differences between these two methods and when will AOR-HB is more prefer compare to NAG. In fig 1 and 2 the empirical performance of AOR-HB and NAG are also very similar.

minor: line 373 typo double "that"

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
4

### Summary
This paper proposes a new momentum method AOR-HB. This method is motivated by discretizing an related ODE using over-relaxation. AOR-HB has accelerated rates compared to HB, and it is further extended to proximal and mini-max problems. Numerical results are provided.

### Strengths
1. Compared to HB, the proposed approach achieves accelerated rates. 

2. The design of ODEs and discretizing can be useful.

### Weaknesses
1. The constant $C_0$ in theorem 1.1 still depends on $\kappa$, which implies that this approach remains slower than Nesterov's momentum. The author should make this dependence clear.

2. Extensions to convex and stochastic problems are less straightforward.

3. The proposed approach only outperforms HB in numerical results. This indicates that it is not the most efficient momentum methods from a practical standpoint.

In sum, while the theoretical finding are impressive, the resultant approach occupies a ‘mid-point’ between momentum methods both theoretically and empirically.

### Questions
See above.

### Soundness
3

### Presentation
2

### Contribution
3
