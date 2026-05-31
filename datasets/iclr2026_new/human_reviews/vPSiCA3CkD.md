## Human Reviewer 1

### Summary
This paper proposes an accelerated adaptive method that can estimate the local Lipschitz constant of the gradients adaptively. It is based on a series of recent papers that use the difference of gradients or other empirical quantities to estimate the Lipschitzness of gradients. This work isn't the first to introduce an accelerated adaptive method like that, but it is the first one where the stepsize estimate can change by a constant non-decreasing factor. The authors prove convergence guarantees for $L$-smooth as well as $(L_0, L_1)$-smooth problems, claiming complexity improvements. The paper features strong theoretical results, but it doesn't present any numerical validation of the proposed method's performance.

### Strengths
The work is undeniably strong theoretically. The authors propose a method that is more adaptive than other accelerated methods, which is an important consideration for its practical performance. It is also clear that deriving the method and its convergence guarantees was no easy task. The algorithmic design can be insightful for future developments of other adaptive methods.

I also think the proposed method can be quite useful for deterministic convex optimization on its own. While convex optimization is a less popular area of applications these days, I still find it a valuable contribution since such problems arise in a lot of applications.

### Weaknesses
1. The method unfortunately requires the ability to compute functional values, unlike the prior work on GRAAL and AdGD.

2. In terms of complexity, there is no realy improvement upon the work of Li & Lan (2025). As the authors mention, the approach of Li & Lan (2025) is to use a line-search at the first iteration, which introduces only an additive term in the complexity, while guaranteeing that $\eta_0 L \ge 1$, so it doesn't affect the complexity in a multiplicative way. I don't see any limitation of this approach since both works require the use of functional values anyway. That being said, the proposed new method still may benefit a lot from updating the stepsize more adaptively in practice.

3. It's a bit unfortunate there is no numerical insights in this paper.

4. I found the discussion in Section 4.1 to be extremely hard to follow, especially Lemma 7. The four sets of indices are introduced without being properly explained, not to mention the third and the fourth sets use $l(k)$, whose meaning is even less obvious. It's completely unclear why these sets are introduced and what we should expect them to be. Moreover, it would be useful to remind the reader of the definition of $m$ around Lemma 8 as it's not used anywhere prior to that except for Theorem 2. It's also very confusing that the authors redefine $m$ in Theorem 3. To summarize, this section is extremely technical and would benefit from a rewrite that makes it more intuitive.

5. The way the proofs are structured in the appendix makes reading them a tedious and a strongly challenging endeavour. I wish the authors chopped it into pieces with intuitive steps, rather than just giving the bounds all as a single huge inequality. I just couldn't make myself go through all the steps to check them even though I wanted to understand the proof.

## Minor typos
"$f(x) \colon \mathbb{R}^d \to \mathbb{R}$" should be "$f \colon \mathbb{R}^d \to \mathbb{R}$"  
"Hence, it is rarely used in practice." I don't think this statement is true, many convex problems are still solved with line-search based methods  
"It is well known that AdaGrad has the complexity of GD in eq. (3) for L-smooth functions (Levy et al., 2018)". I think it needs a clarification here that the results of Levy are only for bounded domains. It is also worth mentioning that the update in (5) misses the $G^2$ constant inside the square root, which is important for non-smooth convergence results.  
I think when introducing (6) and (7) it would be educational for the reader if the authors provided values of $\gamma$ and $\nu$ that have theoretical guarantees.  
"Suh & Ma (2025) uses a stepsize" -> "Suh & Ma (2025) use a stepsize"  
Some small issues in the citations: "Jonathan M Borwein" -> "Jonathan M. Borwein", "in banach spaces" -> "in Banach spaces", "barzilai and borwein gradient" -> "Barzilai and Borwein gradient", etc.

### Questions
1. The authors wrote that $\theta$, $\gamma$, and $\nu$ should satisfy equation (19), but it's not obvious from looking at the equation what possible values we can select from. Could you please provide at least explicit example in the paper?
2. The complexities in Table 1 for Algorithm 1 and for the method of Tyurin (2025) are different in the power of $L_1 \mathcal{D}$. Is the optimal complexity known for this term? Is the result of Vankv et al. (2024) optimal? Do the authors believe their complexity is worse because it's a limiation of the analysis or of the method itself?
3. When discussing AdGD for $(L\_0, L\_1)$ functions, the authors wrote "In fact, $\mathcal{D}$ also contains the initial objective function gap $f(x\_0) − f(x^\*)$, and hence, it may have an exponential dependency on the initial distance $\Vert x\_0 − x^\*\Vert$." However, it seems that the proof of Corollary 3 actually also shows an exponential dependency on $\Vert x_0 − x^*\Vert$, which is then removed by assuming $\eta\_0 L\_0 \le \exp(-L\_1 \Vert x\_0 - x^\* \Vert)$. Isn't it an unfair comparison?

### Soundness
4

### Presentation
3

### Contribution
3

### Rating
8

### Confidence
4

---

## Human Reviewer 2

### Summary
The paper allows exponential growth of the stepsize for adaptive accelerated gradient method. The results show true adaptivity of the method under the generalized smoothness.

### Strengths
The paper solves the issue with explicit (no backtracking) adaptive accelerated methods  -- they cannot increase the stepsize fast.

Detailed comparison with related works.

### Weaknesses
Despite experiments would be quite predictable it would be interesting to see a comparison with adproxgd and optimizers with backtracking beyond the standard smoothness. Not a real weakness, for the sake of comprehensiveness, the theoretical contribution is solid enough.

### Questions
-

### Soundness
4

### Presentation
4

### Contribution
4

### Rating
10

### Confidence
5

---

## Human Reviewer 3

### Summary
This paper develops an accelerated variant of the GRAAL algorithm that achieves near-optimal iteration complexity for convex optimization while maintaining adaptive stepsize capabilities. The main contribution is Algorithm 1 (Accelerated GRAAL), which incorporates Nesterov acceleration while adapting stepsizes to local curvature at a geometric rate. The authors conduct convergence analysis of the proposed algorithm for $L$-smooth and $(L_0, L_1)$-smooth functions. The key technical innovation is an "additional coupling step" that allows adaptive choice of acceleration parameters $\alpha_k$ without requiring predefined sequences or restricting stepsize growth.

### Strengths
1. The additional coupling step is a novel technique that elegantly enabling acceleration and adaptive step-size growth in one framework.

2. The analysis is layered and rigorous: a general potential-descent framework for convex $C^1$ objectives, followed by rate results for $L$-smooth and $(L_0,L_1)$-smooth settings. The bounds are near-optimal and adapt to unknown curvature, with only logarithmic dependence on the initial stepsize guess in the $L$-smooth case.

3. The paper clearly states its target question, the design obstacles, and how each algorithmic components (extrapolation, coupling, curvature estimation) addresses them.

### Weaknesses
1.  Lack of empirical validation. The paper presents no experiments. Small-scale benchmarks (logistic regression, least-squares, GLMs, robust convex losses) would verify geometric step-size growth in practice, overhead of computing $\Lambda$, and wall-clock speedups versus other algorithms.

2. The theory requires universal constants $(\theta, \gamma, \nu)>0$ satisfying equation (19), but the paper does not provide guidance on how to choose these parameters in practice. This is a significant practical limitation. The paper should provide at least one explicit set of valid parameters and discuss how parameter choices affect the hidden constants in the O(·) notation.

3. Results cover smooth convex minimization only; there is no composite/prox extension, constraint handling, or analysis with stochastic/inexact oracles.

### Questions
1. How does the algorithm perform empirically compared to AC-FGM, AdaNAG, and non-accelerated GRAAL? 

2. Could you provide explicit $(\theta,\gamma,\nu)$ values that satisfy the required inequalities, and a recommended default $\eta_0$?

3. Because the method introduces several iterates ($x_k, \bar{x}_k, \hat{x}_k, \tilde{x}_k$) and requires multiple gradients for curvature estimation, the peak memory can exceed that of standard AGD. Have you considered memory-efficient implementation of the proposed algorithm?

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
3

---

## Human Reviewer 4

### Summary
This paper studies a GRAAL-based adaptive variant of Nesterov’s accelerated gradient method for smooth convex minimization. Unlike other recent adaptive methods, this approach allows the step size to grow linearly, which is particularly useful when the algorithm is initialized with a very small step size. This feature becomes even more important under the more general $(L_0,L_1)$-smoothness condition, where the local curvature may change at an exponential rate.

### Strengths
- As clearly summarized in Table 1, this paper proposes the first adaptive accelerated method that achieves the optimal rate under convexity and $(L_0,L_1)$-smoothness.

- Even under the standard smoothness assumption, the proposed adaptive accelerated method allows the step size to grow linearly, unlike existing methods, which is particularly beneficial when the initial step size is small.

### Weaknesses
- Although this is primarily a theoretical paper, including a simple toy experiment would make the contribution more informative. (This is not a requirement for acceptance, but a suggestion to strengthen the paper.)

- I would appreciate it if Section 4.1 provided a higher-level sketch of the main idea.

### Questions
- (10): The definition of $D_f$ is missing.
- L181: It seems that Option II can better exploit the properties of the objective function, but I recommend providing a more precise statement.
- L207: Could the authors clarify how the extrapolation enables adaptive capabilities?
- L226: The definition of $\Lambda$ is missing.
- L322: Wouldn't a small $\eta_0$ slow down the empirical performance?
- L461-462: The initial step size is required to satisfy $\eta_0 \le \frac{1}{L_0\exp(L_1||x_0-x^*||)}$, and the authors suggest choosing a very small value, which effectively makes the method free from hyperparameter tuning. The authors also note that a concurrent work by Tyurin (2025) provides a similar result but requires additional hyperparameter tuning. However, if one apply the same principle (choosing an extremely small or large constant), couldn't Tyurin's method also be regarded as tuning-free? This is what I inferred after reading Section 4 of Tyurin (2025). I would appreciate clarification on this point.

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
3