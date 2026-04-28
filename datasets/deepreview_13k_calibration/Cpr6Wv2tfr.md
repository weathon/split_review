# OPTAMI: Global Superlinear Convergence of High-order Methods

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 8, 6, 5

## Abstract
Second-order methods for convex optimization outperform first-order methods in terms of theoretical iteration convergence, achieving rates up to $O(k^{-5})$ for highly-smooth functions. However, their practical performance and applications are limited due to their multi-level structure and implementation complexity. In this paper, we present new results on high-order optimization methods, supported by their practical performance. First, we show that the basic high-order methods, such as the Cubic Regularized Newton Method, exhibit global superlinear convergence for $\mu$-strongly star-convex functions, a class that includes $\mu$-strongly convex functions and some non-convex functions. Theoretical convergence results are both inspired and supported by the practical performance of these methods. Secondly, we propose a practical version of the Nesterov Accelerated Tensor method, called NATA. It significantly outperforms the classical variant and other high-order acceleration techniques in practice. The convergence of NATA is also supported by theoretical results. Finally, we introduce an open-source computational library for high-order methods, called OPTAMI. This library includes various methods, acceleration techniques, and subproblem solvers, all implemented as PyTorch optimizers, thereby facilitating the practical application of high-order methods to a wide range of optimization problems. We hope this library will simplify research and practical comparison of methods beyond first-order.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper focuses on the analysis of high order methods for nearly convex functions (i.e. star-convex or convex) with additional growth properties. The authors leverage a strong star-convexity and a uniform star-convexity assumption to prove the global superlinear convergence of the Cubic Regularized Newton Method and the Basic Tensor Method. In addition, they introduce an adaptive variant of Nesterov Accelerated Tensor Method called NATA (for Nesterov Accelerated Tensor Method with $A_t$-Adaptation) which solves the problem of having too conservative parameters. Theoretical convergence guarantees are given as well as numerical experiments highlighting good performance. The authors also provide OPTAMI, a python library for high order methods.

### Strengths
Overall, I think that the contributions of the paper are valuable and the technical content would be sufficient for publishing the paper in ICLR. Moreover, I did not find any major mistake in the proofs. The library seems to be qualitative and the numerical experiments are satisfactory to me.

### Weaknesses
I am not convinced by the structure of the paper and the way it is written. It seems to me that the authors try to answer too many questions for a 10 pages paper. Also, I think that the theoretical claims are not discussed enough. Detailed comments can be found below. The main problem I have with the current version of the paper is that it lacks a clear unified story and it seems  an aggregation of results. In my opinion, this could be improved by modifying the structure of the paper.

The OPTAMI library is only mentioned but never properly introduced. I think that at least a paragraph should be dedicated to it or else, that it should be removed from the title.
About the structure:

   1) I believe that the introduction is already too technical although it is well explained. It also states too many problems and, due to a lack of structure, it can confuse the reader. This is highlighted by the fact that there are three questions at the end of the introduction. My suggestion is to keep the detailed discussions for later sections and do a way shorter and high-level introduction. Also, I would try to use as few equations as possible.

    2) It is related to the previous comment but I think that the second section "Basic methods" could be enriched with some comments from the introduction.

    3) I think that the third section is interesting with intuitive proofs. However, I regret that there is no discussion on the stated theorems: is there any similar result in the literature, was it expected, is it tight?

    4) The fourth section seems to come bit out of nowhere and lacks a proper introduction. As a reader, it can seem odd to come from superlinear convegence rates (which is in the name of the paper) to adaptive techniques and a new method without a paragraph that bridges both sections. As said before, Theorem 4.1 should be commented and I would have expected a comparison with the results ensured by vanilla NATM.

    5) I believe that the fifth section should be merged with the fourth one or defined as a subsection.

* Minor comments/typos:
    - p.3, l.140: $c_3$ is never introduced before.
    - p.4, l.188,196,201: "the function $f(x)$" should be " the function $f$"
    - p.5, l.263: $e$ is both the vector of all ones and $1e-4=10^{-4}$
    - p.6, l.283: idem
    - p.6, l.287: the bigger $\rightarrow$ the larger
    - p.6, l.288: repetition "first, the first..."
    - p.6, l.293: I think the paragraph is a bit too long especially the explanation on gradient descent.
    - p.6, l.321: I understand but I think it is not very clear.
    - p.7, l.331: " has next constant" is a bit odd to me
    - p.7, l.338: "second Theorem" $\rightarrow$ "second theorem"
    - p.7, l.338: the sentence is too long and contains two times "hence"
    - p.18, l.930: "subsolover"
    - p.24, l.1274: "Optimal" seems to be a typo.

### Questions
How do the theoretical results proved in the paper compare to the literature? Was this setting already studied?

* Minor comments/typos:
    - p.3, l.140: $c_3$ is never introduced before.
    - p.4, l.188,196,201: "the function $f(x)$" should be " the function $f$"
    - p.5, l.263: $e$ is both the vector of all ones and $1e-4=10^{-4}$
    - p.6, l.283: idem
    - p.6, l.287: the bigger $\rightarrow$ the larger
    - p.6, l.288: repetition "first, the first..."
    - p.6, l.293: I think the paragraph is a bit too long especially the explanation on gradient descent.
    - p.6, l.321: I understand but I think it is not very clear.
    - p.7, l.331: " has next constant" is a bit odd to me
    - p.7, l.338: "second Theorem" $\rightarrow$ "second theorem"
    - p.7, l.338: the sentence is too long and contains two times "hence"
    - p.18, l.930: "subsolover"
    - p.24, l.1274: "Optimal" seems to be a typo.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper first establishes the global superlinear convergence rate for second-order methods in optimizing strongly star-convex functions, and its higher-order extension for optimizing uniformly star-convex functions, then proposes a variant of Nesterov accelerated tensor method which demonstrates superior performance in numerical experiments consistent with the theoretical faster convergence rate, and finally presents a systematical numerical comparison across mainstream second-order methods.

### Strengths
1. The proposed acceleration variant of tensor method achieves better empirical performance than the existing (near)-optimal accelerated second-order methods.
2. All methods are systematically implemented and released as a library.

### Weaknesses
1. The global linear rate is established by relaxing the required accuracy to exceed the radius of the quadratic convergence region.
2. Some typos: 
- line 143 "$\epsilon \leq c_3 r$" --> $\epsilon > c_3 r$ 
- Eq (20) $t \rightarrow 0$ --> $t \rightarrow \infty$?
3. The practical significance of achieving superlinear convergence only when the required accuracy is relatively low is not fully justified. The paper does not adequately address scenarios where higher accuracy is needed, which is often the case in practical optimization problems. The theoretical result seems to prioritize a faster convergence rate in a less practically relevant regime, potentially limiting its impact.

### Questions
1. How do the authors interpret this trade-off between accuracy and rate of convergence? If the requirement on accuracy is relaxed and the conditions are different, how can the superlinear convergence rate be seen as an improvement compared to previous results?
2. In addition to the first question, Song et. al. 2021 proposed an acceleration framework that matches the lower bound established by Arjevani et al. 2019. Shouldn't that be seen as the optimal rate for this setting of optimizing strongly convex functions with second-order methods?

Chaobing Song, Yong Jiang, and Yi Ma. Unified acceleration of high-order algorithms under general holder
continuity. SIAM Journal on Optimization, 31(3):1797–1826, 2021.

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
In this work, the authors studied the convergence rate of high-order methods, e.g., the cubic regularized Newton method and the basic tensor method. The authors proved the global superlinear convergence of both methods for $\mu$-strongly star-convex functions and $\mu_q$-uniformly star-convex functions, respectively. In addition, a variant of accelerated high-order method, named NATA, was proposed and compared with other accelerated high-order methods.

### Strengths
The paper is well-organized and easy to follow. The results are novel and should be interesting to the audience from machine learning and optimization fields. The problems studied in this work are important and applicable to certain practical problems where the computational time is not a critical constraint. The proof in the main manuscript should be correct, while I do not have time to check the proofs in the appendix due to the time limit.

### Weaknesses
The main problem with the paper is that the first part (superlinear convergence rate of high-order methods) and the second part (NATA algorithm) seem to be independent and can be separated into two papers. I feel that these two parts considered two different topics. The first one is mostly theoretical and is about non-accelerated methods, while the second one is about accelerated methods and their empirical performance. I would suggest the authors split the paper into two and include more details to the content. For example, the intuition behind the design of NATA. 

In addition, I think the current introduction section is too lengthy. Considering the page limit of the conference, the background knowledge can be simplified and moved to the appendix, since it can be easily found in textbooks and literature. 

Finally, I think the authors could include more details to the experiments. For example, in Figure 3, I wonder if the Tensor NATA converges faster with a carefully chosen $v_t$? This is not discussed. Also, it would be better if the authors could provide more intuition behind the current design of searching $v_t$ in sub-iterations instead of fixing $v_t$ to be a constant. Since the performance of a fixed $v_t$ is better than that of a adaptive $v_t$, I wonder if this design is unnecessary. Furthermore, I think it will be helpful if the authors could provide the running time comparison. This is because the solving time of the sub-problem in each iteration may be non-negligible and comparable to the computation time of the Hessian matrix. Especially, for the NATA method, the sub-problem needs to be solved several times in each iteration.

### Questions
I have a few other minor comments for the authors to consider:

- Line 143: I think it should be $\epsilon > c_3 r$?

- Line 295: "where the sublinear rate outperforms the linear rate" is a little confusing. Maybe the authors meant the high-order methods have not entered the linear convergence region and the convergence rate is sublinear at the beginning?

- For the CRN method, did the authors prove the superlinear convergence for $\mu_q$-uniformly star-convex functions? If so, it may be better to state the results in Theorem 3.2. Currently, I cannot find the results for $\mu_q$-uniformly star-convex functions and the CRN method.

### Soundness
3

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
4

### Summary
The paper presents two main results: the first shows that the basic high-order methods (the Cubic Regularized Newton Method and Basic Tensor Method) achieve global superlinear convergence for μ-strongly star-convex functions. 
Second, it proposes a technique for choosing the parameters of an existing method (Nesterov Accelerated Tensor Method), evaluates its convergence speed, and shows its usefulness in numerical experiments. 
Furthermore, the paper introduces an open-source computational library called OPTAMI for high-order methods.

### Strengths
It is great to show that cubic Newton and Basic Tensor methods can achieve superlinear convergence for strongly convex functions.
This paper also includes the necessary equations and propositions for following the proof of superlinear convergence in the main text, and explains the proof strategy leading to the most important theorem, Theorem 3.4, in an easy-to-understand manner. 

 I also think that providing an open-source computational library for high-order methods would be very helpful to subsequent researchers.

### Weaknesses
[Structure of the paper]
Section 3 and Section 4 are not well connected, and the paper seems to contain two disparate contents; it would be better to divide the paper into two papers, and strengthen the contents of each, for example, in the following ways. The algorithms and classes of functions are different between Sections 3 and 4.

For example, for the contents of Section 3, if the cost of solving the subproblem in each iteration can be evaluated, what is the total computational complexity? How attractive is it compared to the total computational complexities of other algorithms? Even if the number of iterations (i.e., the worst-case iteration complexity) is reduced, on the other hand, if the computational complexity at each iteration explodes, it will not be attractive as an algorithm, so it would be better to provide the total computational complexity. If the subproblem is to be solved iteratively, can't we allow it to be solved inexactly and include the error in the iteration complexity and total computational cost?

For example, for the contents of Section 4, if we consider strongly star-convex, how can the theoretical guarantee given in Theorem 4.1 be changed? As future work, the authors wrote this type of question, but what trends do you see, at least in numerical experiments? More precisely, what would Figure 3(b) look like in the case of strongly convex (21) with positive $\mu$ (perhaps the horizontal axis might need to be the iteration number)?

----------

[Various unclear descriptions]
There are unclear descriptions and various minor errors, giving the impression that this paper was written in haste.

For example, lines 62-74 introduce the existing studies and describe their global convergence rates, but the assumption of the function $f$ is not clearly stated. Before that, there is a definition of star-convex, etc., but I do not think that those existing studies assume star-convex. This is because the Hessian matrix in (7) is not necessarily positive definite when the function is nonconvex.
The others are line 80: upperbound --> upper bound, NPE in line 109 should be written as Newton Proximal Extragradient (NPE), in line 123 the methods performs --> the method performs, etc. Line 193 defines the norm $||x||$ using a matrix B, but which kind of matrices are specifically used in your claims? If we always assume $B=I$, why use $B$ to define the norm? I won't point out any more, but I would like the authors to review the paper again and and reduce this type of typo.

----------

[Insufficient reference]
The survey of existing studies does not seem to be sufficient. For example, in line 97, the authors write “poor global convergence” for the quasi-Newton method, but I do not think they are aware of the following paper. The paper also shows “Global Non-Asymptotic Superlinear Convergence” as well as this paper.

Qiujiang Jin, Ruichen Jiang, Aryan Mokhtari, "Non-asymptotic Global Convergence Rates of BFGS with Exact Line Search",
arXiv:2404.01267, 2024.

 Although the authors mention the Jiang, Jin, and Mokhtari paper (COLT 2023) in Appendix A, I think the global convergence rates of quasi-Newton methods should be mentioned around lines 97-98, including the above-mentioned papers. Can it no longer be called “poor global convergence”?

### Questions
1) What are the total computational complexities for the Cubic Regularized Newton Method and Basic Tensor Method if the costs of solving the subproblems in each iteration can be evaluated? How attractive are they compared to the total computational complexities of other algorithms? 

2) If the subproblems of the Cubic Regularized Newton Method and Basic Tensor Method are to be solved iteratively, can't we allow them to be solved inexactly and include the errors in total computational costs?

3) About the proposed algorithm, Newterov Accelerated Tensor Method with At-Adaptation (NATA). Can the authors show anything about the iteration complexities for the strongly (star-)convex case? If it is difficult, show us the best iteration complexity for the classical Nesterov accelerated tensor method when the function $f$ is strongly convex, and tell us why it is difficult to derive the complexity for NATA. 

4) For the strongly (star-)convex case, how does NATA perform in numerical experiments? More precisely, what would Figure 3(b) look like in the case of strongly convex (21) with positive $\mu$ (perhaps the horizontal axis might need to be the iteration number)?

### Soundness
3

### Presentation
2

### Contribution
2
