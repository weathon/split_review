# On the Almost Sure Convergence of the Stochastic Three Points Algorithm

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
The stochastic three points (STP) algorithm is a derivative-free optimization technique designed for unconstrained optimization problems in $\mathbb{R}^d$. In this paper, we analyze this algorithm for three classes of functions : smooth functions that may lack convexity, smooth convex functions, and smooth functions that are strongly convex. Our work provides the first almost sure convergence results of the STP algorithm, alongside some convergence results in expectation.
For the class of smooth functions, we establish that the best gradient iterate of the STP algorithm converges almost surely to zero at a rate arbitrarily close to $o(\frac{1}{\sqrt{T}})$, where $T$ is the number of iterations. Furthermore, within the same class of functions, we establish both almost sure convergence and convergence in expectation of the final gradient iterate towards zero.
For the class of smooth convex functions, we establish that $f(\theta^T)$ converges to $\inf_{\theta \in \mathbb{R}^d} f(\theta)$ almost surely at a rate arbitrarily close to $o(\frac{1}{T})$, and in expectation at a rate of $O(\frac{d}{T})$ where $d$ is the dimension of the space.
Finally, for the class of smooth functions that are strongly convex, we establish that when step sizes are obtained by approximating the directional derivatives of the function, $f(\theta^T)$ converges to $\inf_{\theta \in \mathbb{R}^d} f(\theta)$ in expectation at a rate of $O((1-\frac{\mu}{dL})^T)$, and almost surely at a rate arbitrarily close to $o((1-\frac{\mu}{dL})^T)$,  where $\mu$ and $L$
are  the strong convexity and smoothness parameters of the function.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper analyzes almost-sure convergence for the derivative-free stochastic three points (STP) algorithm in (Bergou et al., 2020), where only the convergence in expectation was studied. The convergence in expectation does not guarantee convergence of individual instance of trajectories, which is why, for example, extensive research on almost-sure convergence has been conducted for SGD. This paper's study of STP, therefore, aligns with recent theoretical advancements in SGD. In particular, this paper provides the almost-sure convergence results for three standard classes of functions, as summarized in Table 1.

### Strengths
This paper provides the first almost-sure convergence analysis of the STP method for three standard classes of functions, a non-trivial achievement. This analysis guarantees convergence of each trajectory instance, making it valuable both theoretically and practically.

### Weaknesses
 - Motivation: The focus on STP in this paper is not well motivated in the abstract and introduction, aside from mentiong its low per-iteration complexity. Is the STP widely used in practice? Given its simplicity and strong theoretical guarantees, I cannot see why this would not be considered by practitioners. I suggest that the authors further elaborate on the theoretical and practical importance of studying the STP.

- Comparison to other existing derivative-free methods: Although this paper focuses on the STP, it would have been helpful to include comparisons or discussions of the almost-sure convergence (rate) analyses for other existing derivative-free methods, if available. Without these, it is difficult to locate this work within the broader literature.

- Experiment: What is the purpose of this experiment? It seems quite orthogonal to the paper's theoretical contributions. It looks like it was added to appeal to practitioner reviewers, but I believe it may ultimately satisfy neither theory nor practitioner reviewers. I suggest revising the experiment section to better align with the paper's main contributions.

- Lines 111-112: Although it is straightforward, please explicitly state the consequence of the result.
- Line 124: $\theta$ denotes both the iterates and the step size parameter, and I suggest using other letter for the step size parameter.
- Remark 2: This seems redundant and I suggest removing it.
- Lemma 4: This does not seem necessary here, which is only used in the proof in the Appendix. I suggest moving it to Appendix.
- Remarks 7,8 and 10: They discuss the condition that Assumption 3 can be satisfied. I believe that they can be simply discussed right after Assumption 3, or can be more clearly and briefly stated in the remarks.

### Questions
- Lines 111-112: Although it is straightforward, please explicitly state the consequence of the result.
- Line 124: $\theta$ denotes both the iterates and the step size parameter, and I suggest using other letter for the step size parameter.
- Remark 2: This seems redundant and I suggest removing it.
- Lemma 4: This does not seem necessary here, which is only used in the proof in the Appendix. I suggest moving it to Appendix.
- Remarks 7,8 and 10: They discuss the condition that Assumption 3 can be satisfied. I believe that they can be simply discussed right after Assumption 3, or can be more clearly and briefly stated in the remarks.

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
This paper establishes the almost sure (and last iterate) convergence of the stochastic three-point algorithm for zeroth-order optimization. The paper considers smooth nonconvex, convex, and strongly convex settings and gets the results under three different settings, respectively. Numerical experiments demonstrate the performance of the proposed method.

### Strengths
The paper is well-written, with technical results clearly presented and explained. Also, different settings are considered in the paper.

### Weaknesses
My major concern is the technical novelty of the paper.

1. Insufficient technical contribution.

   Although the paper considers multiple settings and gets almost-sure convergence results, the techniques seem to be a combination of [1] and other papers that establish almost-sure convergence of SGD in different settings. Especially the results in section 3 and 4 look less surprising, since most of them are obtained by verifying some conditions and invoking an existing almost-sure convergence result from the SGD literature. The core of the analysis relies on adapting existing proof techniques rather than introducing novel analytical tools or insights. The paper does not sufficiently highlight the specific challenges in extending these techniques to the stochastic three-point algorithm, nor does it offer a detailed comparison with the existing literature to showcase the unique aspects of the contribution.

2. Presentation issues.

   The paper contains many technical results, either proven in this paper or cited from other papers. However, there is not sufficient explanation after each main result. This may make the results less accessible to the readers. For example, the implications of the convergence rates derived in each setting are not thoroughly discussed, and the practical relevance of the theoretical findings is not clearly articulated. The paper would benefit from more intuitive explanations of the technical steps and a more detailed discussion of the significance of each theorem.

### Questions
1. In the nonconvex case (Theorem 1), lower-boundedness (A2) is not assumed. But on line 624 in the appendix, the authors use the assumption that $f$ is bounded from below. 
2. A7 seems to be an artifact of analysis. Could you provide more intuitions behind it?
3. Results in section 4 require the initial point to lie in the sublevel set. Here the cost of finding such an initial point is not discussed. Could you elaborate more on this?

**Minor issues**

1. Line 139

   There seems to be an additional 2 in the complexity.

2. Line 146

   The Assump column does not match all the results in the paper (e.g., Theorem 7 in section 5 mentions "Assumption 1 and 4 to 7"). Also, assumption 7 does not appear in the table.

3. Line 146, 533

   Please put the caption of the table at the top.

4. Line 204

   The statement of the examples seems incorrect and inconsistent with [1]. The covariance matrix in [1] is $I_d / d$  instead of $I_d$.

   For any arbitrary => For any.

5. Line 318, 372

   $\ast$ and $^\star$ are inconsistent.

6. Line 890

   $m$ is undefined.

**References**

[1] Bergou, E. H., Gorbunov, E., & Richtarik, P. (2020). Stochastic three points method for unconstrained smooth minimization. *SIAM Journal on Optimization*, *30*(4), 2726-2749.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Convergence analysis of the stochastic three points (STP) algorithm is studied. The rates for different classes of functions are shown. A almost sure convergence rate arbitrarily close to $O(1/\sqrt{T})$ is shown for smooth functions.
And almost sure convergence rate arbitrarily close to $o(1/T)$ and in expectation a rate of $O(d/T)$ is shown for smooth convex functions. For the class of strong convex functions, a rate of $O((1-\mu/dL)^T)$ in expectation and a rate arbitrarily close to $o((1-\mu/dL)^T)$ for almost sure convergence is shown.

### Strengths
Paper is well-written. Convergence rates of the STP algorithm for smooth, smooth convex and smooth strongly convex functions are shown.

### Weaknesses
The results are incremental. How does the convergence rate of STP compare with other methods both in expectation and almost sure. For example with RGF or GLD which is compared in the experiments ? This could be discussed or given as a table. What about the optimal convergence rate in each case ?  A brief discussion about the advantages of STP algorithm in the introduction would be helpful.

### Questions
1. Please add a table comparing the convergence rates (both in expectation and almost sure) of STP, RGF, and GLD for each function class studied. Also please discuss how STP's rates compare to known optimal rates for each case. This is important as it would provide valuable context for the significance of the STP results.

2. Please add a paragraph or two in the introduction highlighting the key advantages of STP over other zeroth-order methods, such as its linear dependence on dimension compared to quadratic dependence for deterministic direct search methods. This would help readers better understand the importance of studying STP's convergence properties.

### Soundness
4

### Presentation
4

### Contribution
3
