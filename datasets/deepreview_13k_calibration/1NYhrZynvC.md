# Exact linear-rate gradient descent: optimal adaptive stepsize theory and practical use

- Decision: Reject
- Avg Score: 2.50
- Scores: 3, 1, 5, 1

## Abstract
Consider gradient descent iterations $ {x}^{k+1} = {x}^k - \alpha_k \nabla f ({x}^k) $. 
Suppose gradient exists and $ \nabla f ({x}^k) \neq {0}$.
We propose the following closed-form stepsize choice:
\begin{equation}
	\alpha_k^\star =  \frac{ \Vert  {x}^\star - {x}^k  \Vert }{\left\Vert \nabla f({x}^k)  \right\Vert} \cos\eta_k , \tag{theoretical}
\end{equation}
where $ \eta_k $ is the angle between vectors $ {x}^\star - {x}^k  $ and $ -\nabla f({x}^k)  $.
It is universally applicable and admits an exact linear  convergence  rate  with factor $ \sin^2\eta_k  $.
Moreover, if $ f $ is  convex and $ L $-smooth,  then $ \alpha_k^\star \geq {1}/{L} $.

For practical use,  we approximate (can be exact) the above  via 
\begin{equation}
	\alpha_{k}^\dagger = \gamma_0 \cdot \frac{ f({x}^k) - \bar{f}_0  }{\Vert  \nabla f (	{x}^k )   \Vert^2 } ,
	\tag{practical use}
\end{equation}
where  $\gamma_0 $ is a tunable parameter; $ \bar{f}_0 $ is  a guess on the smallest objective value (can be auto. updated).
Suppose  $ f $ is convex and $ \bar{f}_0 = f ( {x}^\star )   $, then 
any choice from $\gamma_0 \in (0,2] $ guarantees an exact linear-rate convergence to the optimal point.

We consider a  few examples.
(i) An $ \mathbb{R}^2 $ quadratic program, where a well-known ill-conditioning bottleneck is  addressed, with a rate strictly better than $ O(1/2^k) $. (ii) A geometric program, where an inaccurate guess $ \bar{f}_0  $ remains powerful.
(iii) A non-convex MNIST classification problem via neural networks, where preliminary tests show that ours admits better performance than the state-of-the-art algorithms,  particularly a  tune-free version is available in some settings.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper studies some adaptive size rules for smooth functions, including some theoretical optimal ones and practical approximations. Experiments show some advantages of these rules.

### Strengths
This paper uses several examples to demonstrate the benefits of using the proposed step size rules.

### Weaknesses
 The writing could be significantly improved. There are many examples where the writing deviates from grammatical English, even from the very beginning of the paper. For instance, “due to quantity is not a priori knowledge.” — lines 75-76. In some places this does not impede the understandability of the paper, but in others the problems with the writing indeed make it hard to properly understand what the paper is about, and what its contributions are. 

The introduction is generally loose and imprecise, in areas where it should be specifying exactly what the area of contribution is, precisely because this is such a well-researched area. For example, the paper says that though there are several adaptive algorithms implemented and available, “an adaptive stepsize theory has not been established.” This is confusing, since there are many theoretical papers about AdaGrad and other adaptive step size schedules in the last few years in ML and Optimization venues (not to mention that it is also a fairly classical topic). The authors need to clearly articulate what specific gap in the theory they are addressing, and why existing theoretical results are insufficient for their purposes. The claim that no adaptive step size theory exists is simply not accurate and needs to be revised with more nuance.

Then we are told that their optimal stepwise yields a linear rate with factor sin^2 \eta_k — but we do not know what \eta_k is at this point in the paper. They then go on to say that the theory applies to non-convex functions, but we are not told what is guaranteed in this case. At least an informal statement should be made explaining what is happening, if the authors wish to talk about it directly. The lack of clarity about the meaning of \eta_k and the precise guarantees in the non-convex case makes it difficult to evaluate the significance of the theoretical results.

Proposition 2.1 says it guarantees convergence to a global optimum of GD, yet does not require in the statement that the function being optimized be convex. The proof also does not mention convexity, and indeed does not prove anything about global convergence. This is a major flaw, as global convergence for non-convex functions is generally not guaranteed for gradient descent, and the authors need to be much more precise about the conditions under which their results hold. The lack of a convexity assumption in the statement of the proposition is misleading and needs to be corrected.

In line 146, the paper says that they assume that the gradient is non-zero unless GD has already converged; but then they say that this means that it has converged to x*, but which I understand that the assumption is that they assume they are minimizing a function that has no stationary points other than the unique global optimum. This assumption is not clearly stated, and the connection between a non-zero gradient and convergence to the global optimum is not well explained. The authors need to clarify their assumptions and provide a more rigorous justification for their claims.

The experiments are also not particularly convincing. They need to better point to where the weaknesses are of other related methods, where this approach succeeds. The experiments should include comparisons with state-of-the-art adaptive methods, and the authors should provide a clear explanation of why their proposed method is superior in specific scenarios. The current experimental results do not provide sufficient evidence to support the claims made in the paper.

### Questions
1. Does Theorem 2.1 and Corollary 2.2 assumes $L$-smoothness?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
The paper considers selecting a stepsize for gradient descent, in particular when we cannot compute global quantities like smoothness parameters. Though there has been considerable work, including recently, on adaptive step size selection methods such as Adagrad, this paper takes a different view. The idea is to approximate the a step size that looks a lot like the Polyak step size, by quantities that can be estimated (the Polyak step size requires knowing f(x*)). 

They use this step size on various experiments, including on the non-convex problem of training a 2 layer MLP.

### Strengths
The paper considers a significant and important problem.
The problem is of current interest -- there are papers appearing about related topics every year.
The proposal of a new step size is related to well studied step sizes like Polyak step size, but it seems to have some novel aspects.

### Weaknesses
**W1.** The theoretical analysis relies on strong assumptions, namely that the objective function is convex and the optimal objective value $f(x^*)$ is known. In practice, $f(x^*)$ is rarely known beforehand. While the authors propose an adaptive estimation in Algorithm 1, the reliance on this estimate, particularly its accuracy, could significantly impact the algorithm's performance in general settings.

**W2.** The only practical solution proposed in this paper is Algorithm 1. However, the authors do not provide a theoretical analysis for it. In particular, does Algorithm 1 converge in convex settings? What is its iteration complexity in an ergodic sense when the objective function is convex and non-convex? These theoretical guarantees are crucial for understanding the algorithm's practical applicability and limitations.

**W3.** Additional detailed discussion and analysis are necessary and would be beneficial to further clarify and present Algorithm 1.
1. For example, the auto-correction mechanism in Algorithm 1 explicitly requires $g(x) \geq 0$; otherwise, $\overline{f}_0$ may not serve as a reliable estimate of $f(x^*)$. This condition might not always hold, especially during the initial iterations or in non-convex settings. A more robust mechanism for estimating $f(x^*)$ or adapting the stepsize when $g(x) < 0$ is needed.
2. Taking the least squares problem in Problem (3.16) as an example, when $\alpha >0$ and $\alpha \approx 0$, Algorithm 1 could get stuck at a point that is neither a local nor a global minimum, as the second correction in Line 322 is never invoked. This can result in a less accurate estimation of $f(x^*)$. Specifically, if the algorithm gets stuck in a region where the gradient is close to zero but the function value is far from the optimum, the update rule might not be able to escape this region due to the small stepsize. A more rigorous analysis of the conditions under which the algorithm can escape such regions is needed.

**W4.** Other issues:

1) The proposed algorithm is only suitable for deterministic optimization problems, as it requires calculating the objective function value, making it incompatible with stochastic optimization models. Comparing it with stochastic optimizers like ADAM may be unfair, as ADAM is designed for stochastic settings while the proposed method is deterministic. The authors should clarify the intended application domain of their method and compare it with appropriate baselines.

2) It would be beneficial for the authors to include comparisons with other leading deterministic algorithms, such as AdaGrad-Norm [1], APGM [2], and AdaBB [3]. These comparisons would provide a more comprehensive evaluation of the proposed method's performance in the deterministic setting.



### Questions
What are the weakest assumptions that are required about the function f, in order for you to guarantee your results hold? 

What is the relationship to the Polyak step size (e.g., paper by Hazan and Kakade)?

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
This paper proposes a new adaptive stepsize for gradient descent that achieves exact linear convergence rates for convex optimization.

The key contribution is a novel stepsize formula based on the gradient and objective function.

The authors provide two versions of the stepsize: a theoretical version and a practical version.

They demonstrate the efficacy of this approach through some preliminary examples.

### Strengths
**S1:** The paper is well-written and easy to follow, with a clear presentation of the introduction and background on line-search-free first-order methods.

**S2:** This paper proves a simple line-search-free variant of gradient descent to minimize smooth convex functions. The proposed stepsize can be dynamically adjusted to capture the curvature information of the problem, allowing for faster convergence.

**S3:** The paper provides a rigorous proof of the linear convergence rate under the convex settings.

**S4:** The paper includes empirical comparisons with other popular optimizers, such as Adam and N-AGD.

### Weaknesses
 - The definition of the theoretical stepsize proposed depends on x* but it's not clear that x* is unique or that this stepsize is well-defined if x* is not unique. No further assumptions on the objective function f are ever stated to ensure uniqueness of x*. No discussion of what will happen if x* is not unique is given.

- The practical use stepsize given is just a Polyak stepsize approximating inf f by \bar{f}_0. Yet, no reference to Polyak is made nor to any papers studying the Polyak stepsize and related variants, which are quite numerous. In this way the discussion of related work is severely lacking.

- The quality of writing is far below a level that is acceptable for publication. Many statements are mathematically incomplete (e.g., line 155 and many others) or outright incorrect (e.g., the Baillon-Hadad theorem on line 650). Many statements have implicit assumptions that are never stated and not always satisfied or verifiable (e.g., line 146 and many others). None of the convergence results make sense mathematically as there is no reason for x* to be unique - how can \|x_k-x*\|^2 go to 0 for two different x*?

- There is no comparison of the tuning-free algorithm to other tuning-free gradient descent algorithms, of which there is a significant body of work.

### Questions
**Q1.** Could the authors provide theoretical analysis (e.g., oracle or iteration complexity) for the proposed adaptive stepsize strategy in the case where $f(x)$ is non-convex?

**Q2.** The authors mention using a commonly adopted mini-batch size of 128. Is this setting specific to ADAM? The proposed method may not directly extend to stochastic settings if it requires a dynamic estimation of $f(x^*)$.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
The paper proposes an adaptive stepsize selection scheme for gradient descent (GD). The main theoretical contribution is providing an expression for what is claimed to be an optimal stepsize choice, which depends on the (implicitly assumed to be unique) solution to the problem. For practical implementation, they propose approximating this with a Polyak-like stepsize estimating inf_x f(x). The authors provide convergence analysis and some numerical experiments on MNIST and quadratic optimization.

### Strengths
- Numerical experiments are performed and their plots are reported

### Weaknesses
- The definition of the theoretical stepsize proposed depends on x* but it's not clear that x* is unique or that this stepsize is well-defined if x* is not unique. No further assumptions on the objective function f are ever stated to ensure uniqueness of x*. No discussion of what will happen if x* is not unique is given.

- The practical use stepsize given is just a Polyak stepsize approximating inf f by \bar{f}_0. Yet, no reference to Polyak is made nor to any papers studying the Polyak stepsize and related variants, which are quite numerous. In this way the discussion of related work is severely lacking.

- The quality of writing is far below a level that is acceptable for publication. Many statements are mathematically incomplete (e.g., line 155 and many others) or outright incorrect (e.g., the Baillon-Hadad theorem on line 650). Many statements have implicit assumptions that are never stated and not always satisfied or verifiable (e.g., line 146 and many others). None of the convergence results make sense mathematically as there is no reason for x* to be unique - how can \|x_k-x*\|^2 go to 0 for two different x*?

- There is no comparison of the tuning-free algorithm to other tuning-free gradient descent algorithms, of which there is a significant body of work.

### Questions
- Why are there no citations to relevant works on Polyak stepsize and tuning-free methods?
- What are the assumptions made on f for each of the results, and do they depend on x* being unique?
- Can you actually verify the assumptions you make on alpha_k in any way if you know in advance f or at least properties that it satisfies, e.g., Lipschitz-smoothness or gradient domination?

### Soundness
1

### Presentation
1

### Contribution
1
