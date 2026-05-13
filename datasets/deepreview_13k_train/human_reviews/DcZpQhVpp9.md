# ADMM for Structured Fractional Minimization

- Decision: Accept
- Scores: 8, 6, 6

## Abstract
We consider a class of structured fractional minimization problems, where the numerator includes a differentiable function, a simple nonconvex nonsmooth function, a concave nonsmooth function, and a convex nonsmooth function composed with a linear operator, while the denominator is a continuous function that is either weakly convex or has a weakly convex square root. These problems are widespread and span numerous essential applications in machine learning and data science. Existing methods are mainly based on subgradient methods and smoothing proximal gradient methods, which may suffer from slow convergence and numerical stability issues. In this paper, we introduce {\sf FADMM}, the first Alternating Direction Method of Multipliers tailored for this class of problems. {\sf FADMM} decouples the original problem into linearized proximal subproblems, featuring two variants: one using Dinkelbach's parametric method ({\sf FADMM-D}) and the other using the quadratic transform method ({\sf FADMM-Q}). By introducing a novel Lyapunov function, we establish that {\sf FADMM} converges to $\epsilon$-approximate critical points of the problem within an oracle complexity of $\mathcal{O}(1/\epsilon^{3})$. Our experiments on synthetic and real-world data for sparse Fisher discriminant analysis, robust Sharpe ratio minimization, and robust sparse recovery demonstrate the effectiveness of our approach.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes an ADMM for solving a class of structured fractional minimization problems. The main techniques are based on smoothing methods and two well-established approaches for fractional minimization problems. The convergence rate of the proposed ADMM is established. Some numerical results are reported to show the efficiency of the proposed ADMM. Overall, the topic and results are interesting.

### Strengths
The authors discuss a class of fractional minimization problems, which seem not to be well addressed in the literature. The authors provide corresponding theoretical analysis and numerical results.

### Weaknesses
The results in Lemmas 3.9 and 3.10 are standard in the literature. The authors do not need to prove them in the appendix and should not claim the results ``represent novel contributions.'' 

After using the smoothing techniques, the hard term $h(Ax)$ will become $h_{\mu}(Ax)$. The authors could then use some standard methods from the fractional minimization community to solve this problem. The corresponding complexity will also be $\mathcal{O}(\epsilon^{-3})$. The authors might want to comment on this. It seems that Bot et al. (2023) also used this smoothing technique.

The authors do not explain Assumption 5.1 well in Remark 5.2. By the algorithm, the iterate $x^t$ is only in the domain of $\delta(\cdot)$. You cannot say that it lies in a bounded set. The same issue occurs in Lemma 5.5. It might not be safe to assume that $x^t$ is bounded.

The notation $\underline{\mathrm{Fd}}$ and $\overline{\mathrm{Fd}}$ should be $\underline{F} \, \underline{d}$ and $\overline{F} \, \overline{d}$, respectively.

If the $\epsilon$-critical point is similar to that in Bot et al. (2023b), will the same complexity results hold?

What is the method SGM mentioned in Section 7?

The authors might need to compare their method to that in Bot et al. (2023b), at least for the Robust SRM problem.

### Questions
- The authors do not explain Assumption 5.1 well in Remark 5.2. By the algorithm, the iterate $x^t$ is only in the domain of $\delta(\cdot)$. You cannot say that it lies in a bounded set. The same issue occurs in Lemma 5.5. It might not be safe to assume that $x^t$ is bounded.

- The notation $\underline{\mathrm{Fd}}$ and $\overline{\mathrm{Fd}}$ should be $\underline{F} \, \underline{d}$ and $\overline{F} \, \overline{d}$, respectively.

- If the $\epsilon$-critical point is similar to that in Bot et al. (2023b), will the same complexity results hold?

- What is the method SGM mentioned in Section 7?

- The authors might need to compare their method to that in Bot et al. (2023b), at least for the Robust SRM problem.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
In this paper, the authors introduce FADMM, the first ADMM algorithm designed to solve general structured fractional minimization problems.  FADMM decouples the original problem into linearized proximal subproblems, featuring two variants: one using Dinkelbach’s parametric method (FADMM-D) and the other using the quadratic transform method (FADMM-Q). The proposed algorithm improves the slow convergence speed and numerical stability issues of traditional subgradient methods and smoothing proximal gradient methods. The authors conduct a convergence analysis of the FADMM algorithm by introducing a novel Lyapunov function, and they validate the effectiveness of the FADMM algorithm through extensive synthetic and real-world data.

### Strengths
1.The authors provide a comprehensive analysis of the proposed FADMM algorithm, including two specific variants: FADMM-D and FADMM-Q.

2.Comprehensive theoretical analysis, with proofs on convergence.

3.The authors conduct extensive experiments on both synthetic and real-world data, effectively demonstrating the efficiency of the FADMM algorithm.

### Weaknesses
I think the writing of this paper can be further improved.

### Questions
I am not an expert in non-convex optimization, I can only give some advice on writing papers：

1.The first sentence of the abstract is too long. It is recommended to split it to improve readability.

2.Line 73, "sufficient large" should be "sufficiently large".

3.Line 138, "To the best of our knowledge......" is too long. It is better to break it into short sentences for reading.

4.Line 236,  "is a widely used to develop practical optimization algorithms ", delete ”a“.

5.Line 454, "Additioanl"  -> "Additional".

### Soundness
3

### Presentation
2

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
This paper develops and analyzes alternating direction method of multipliers (ADMM) algorithms for solving structured fractional minimization problems. Building on recent work (Bot et al., 2023a,b; Li & Zhang, 2022), the main idea is to transform the fractional minimization problem into an equivalent composite minimization problem more amenable to operator splitting. The authors consider two classical transformations following Bot et al., 2023a,b and Li & Zhang, 2022 - Dinkelbach's parametric method and the quadratic transform method. Rather than exactly solving the transformed problems at each iteration (which could be costly), they propose to linearize them and solve this majorized version (which leads to ADMM style updates). This produces two algorithms, FADMM-D and FADMM-Q, corresponding to the two transformation approaches.

A key technical contribution is the use of smoothing via the Moreau envelope to handle the nonsmooth components in the numerator of the fractional objective. The authors establish convergence rates for both D and Q variants, showing they reach eps-approximate critical points within O(1/eps^3) iterations. The theoretical analysis is rigorous and all results are precisely stated. The definition of eps-approximate critical point, however, is nonstandard.

The two methods are validated on three applications that fit loosely within their abstract framework: sparse Fisher discriminant analysis, robust Sharpe ratio maximization, and robust sparse recovery. Note that these problems do not make full use of the relaxed assumptions outlined in the paper. Numerical experiments demonstrate that both variants typically outperform existing approaches in terms of wall-clock time to convergence and seem convincing.

### Strengths
- The class of problems addressed is broader than what was previously treated in the literature. 

- The theoretical results about the convergence of the methods and their rates are strong and significant.

- The arguments made were rigorous and clearly stated. I wasn't able to review all the proofs in detail as there were many that were relegated to the appendix and the paper itself is quite long at nearly 40 pages.

- The methods appear to perform well in the numerical experiments compared to previous methods that can solve fractional minimization problems and other smoothing algorithms.

### Weaknesses
 - The technical density of the presentation harms the readability.

- The discussion after Remark 3.5, on the stationarity conditions for this problem, feels very rushed and I don't understand exactly the justifications for all the claims made. In particular there are many references but they are vague - I think it would improve a lot the clarity of the paper if you could specify a lemma or result from those papers that clearly justifies what you are claiming with the subdifferential caclulus here. This also applies to Lemma A.1.

- Definition 3.8 is the definition of the Moreau envelope - I am confused to see it called Nesterov smoothing. This comes up again in the questions section because some of these results about Moreau envelopes are already well-known, even in papers cited by the authors (i.e., Bohm and Wright).

- Many hyperparameters in the method with little guidance about how to choose them or their effect on convergence.

### Questions
- All the numerical examples given in the paper have a denominator which is convex. This leads me to question whether the generalization of the denonimator to weakly convex functions is even well-motivated; are there problems that really necessitate this assumption?

- Similarly, what is the significance of not assuming that delta is convex if later you assume that it's a simple function? When you take delta to be the indicator function of the set of orthogonal matrices, the proximal operator is not well-defined.

- In Remark 3.11 it is claimed that Lemma 3.9 and 3.10 are novel contributions but in fact many (perhaps all?) of these results are well-known results about Moreau envelopes so in what sense are they novel? The authors should either clarify this comment and be specific about what exactly is novel or to remove this remark and just cite the known references stating these results.

- Very little is said about the effect that the parameter choices have on convergence. In practice how does one go about choosing beta_0 or other hyperparameters? For instance, in the sparse FDA experiments it's written that beta_0 = 100rho which is actually quite large (1000 to 100,000).

Minor Questions:

- What is meant in line 73 when it is claimed that when rho is large, ||X||_[k] approximates ||X||_1 ?

- In line 76, shouldn't h(Ax) have a factor of rho?

- In lin 76, isn't it more clear to simply write that d and d^1/2 are convex?

- How much effort was made to tune the parameters used in all of the different methods?

### Soundness
3

### Presentation
1

### Contribution
2
