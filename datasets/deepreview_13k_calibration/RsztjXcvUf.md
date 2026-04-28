# A Primal-Dual Approach to Solving Variational Inequalities with General Constraints

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 8, 6, 6

## Abstract
\citet{yang2023acvi} recently showed how to use first-order gradient methods to solve general variational inequalities (VIs) under a limiting assumption that analytic solutions of specific subproblems are available.  In this paper, we circumvent this assumption via a warm-starting technique where we solve subproblems approximately and initialize variables with the approximate solution found at the previous iteration.
We prove the convergence of this method and show that the gap function of the last iterate of the method decreases at a rate of $\mathcal{O}(\frac{1}{\sqrt{K}})$ when the operator is $L$-Lipschitz and monotone.
In numerical experiments, we show that this technique can converge much faster than its exact counterpart.
Furthermore, for the cases when the inequality constraints are simple, we introduce an alternative variant of ACVI and establish its convergence under the same conditions.
Finally, we relax the smoothness assumptions in~\citeauthor{yang2023acvi}, yielding, to our knowledge, the first convergence result for VIs with general constraints that does not rely on the assumption that the operator is $L$-Lipschitz.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper studies how to use first-order methods to solve the variational inequality with general constraints. The authors first show the last iterate convergence of the ACVI method in Yang et al. (2023) without assuming the Lipschitzness of the operator. Then, the authors show similar convergence of an inexact version of ACVI if the errors of subproblem solvers decrease at proper rates. When the inequality constraints are fast to project, the authors show a simplified ACVI and its convergence. Experiments are provided to show the convergence and less computational time.

### Strengths
- The paper is well written, and all results are supported by proofs.

- The authors prove the same performance guarantee for ACVI under less restrictive conditions. A new analysis technique is developed to remove the Lipschitz assumption. 

- It is also important to consider inexact ACVI that takes warm-start technique, which provides a more practical algorithm than the original. The authors provide the same convergence rate by conditioning the quality of approximation solutions, which is a useful guide. 

-  Some experiments on standard bilinear games and GANs are provided to show convergence.

### Weaknesses
 - The last iterate convergence is characterized by the gap function and the difference of two primal iterates. This metric, while standard, is different from the optimality gap used in Yang et al. (2023), making direct comparisons challenging. The paper would benefit from a more thorough discussion of how these metrics relate and whether the convergence guarantees are directly comparable in practical scenarios.

- The algorithm design has a great similarity with ACVI in Yang et al. (2023). While the authors claim a new analysis technique, the main paper lacks a formal presentation of this technique and its novelty compared to the original ACVI analysis. The key differences in the proof strategies should be explicitly highlighted, especially given the removal of the Lipschitz assumption.

- It is less discussed why removing the Lipschitz assumption is important in theory and practice. While it is mentioned that this assumption is restrictive, the paper does not provide concrete examples where this assumption is violated and how the proposed method can handle such cases. This limits the practical impact of the theoretical contribution.

- The method is limited to monotone operators, which is a significant restriction. While monotone VIs are important, the paper does not discuss the potential limitations of this assumption and the possibility of extending the method to non-monotone settings, even if it is left for future research.

### Questions
- Since this paper focuses on improving existing analysis, can the authors more formally state new analysis techniques compared with Yang et al. (2023)? 

- How can the errors of solving subproblems be controlled in practice?

- What is the computational complexity of inexact ACVI? How can this be compared with the one for ACVI in your experiments? 

- Any examples that lack Lipschitzness? and experiments? 

- Can the authors generalize inexact ACVI to more general operators? What would be failure if not?

- Have you compared this work with last-iterate or non-ergodic convergence results in the constrained optimization literature?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Variational inequality problems are a class of numerical problems that generalize constrained optimization problems. The rough idea is to use the first-order optimality characteization, and replace the gradient $\nabla f(x)$ with some other more general function $F(x)$. These problems arise naturally when considering equilibrium computation or robust modifications of ordinary constrained optimization problems. The authors study the ACVI algorithm, an ADMM-type algorithm for this setting, and show that it converges under weaker assumptions compared to prior work, specifically under generalization of convexity to the variational inequality setting without Lipschitz-smoothness-type assumptions used previously. They also show this works even if certain steps within the respective algorithm are performed approximately rather than exactly, and use this to study how warm-start techniques affect those steps. The argument is reminiscent of Lyapunov analysis, and works by exhibiting a certain gap function which is shown to decrease at every iteration, revealing part of why ACVI behaves this way. The developed theory is illustrated on somewhat standard experiments.

### Strengths
This is a good paper. This review is going to be relatively short because the contribution is good, the paper is well-written, and everything makes sense.
* Understanding the behavior of optimization algorithms and their generalizations in cases where smoothness assumptions are relaxed is a clear and well-motivated class of research questions, and many papers in convex optimization have been written about this, which overtime have significantly improved understanding of the field and led to advances. It makes a lot of sense to also do this for more general settings.
* The paper as a whole and introduction in particular is clear, well-written, and makes sense. The authors do an excellent job at drawing attention to the aspects that distinguish variational inequalities from ordinary optimization, including limit-cycle-type behavior often found when solving for equilibria and similar problems. that monotonicity plays the role of convexity, and similar points.that someone who is familiar with optimization but not with variational inequalities - perhaps a significant fraction of readers  would want to know.
* There is not enough work on algorithms for equilibrium-solving. The fact that algorithms for doing so are underdeveloped compared to gradient-based optimization is one of the big reasons why GANs have declined in favor of diffusion models and other approaches. Having better tools could help unlock technical tools for problems like this, and for getting multi-agent reinforcement learning algorithms to work more reliably, which is an important goal for machine learning.
* The algebra in Appendix C, which is used to prove the results, is rather heavy: makes me glad that the authors have taken the effort to prove the necessary results, as it means that somebody else that wants to use the algorithm or a similar-enough variant doesn't have to. I'd imagine someone working on optimization would find it instructive to go through the appendix to see what kind of tricks are used, especially in comparison with more ordinary analysis of convex optimization algorithms.

### Weaknesses
 * Experiments are somewhat limited. The only examples are synthetic bilinear games, and GANs. It would be nice to also have an example motivated by computational game theory, or by multi-agent reinforcement learning, or applications to economics, where equilibrium-finding algorithms that are a special case of the variational inequality framework are important. The current experiments, while demonstrating convergence, do not fully showcase the practical applicability of the algorithm in diverse real-world scenarios where variational inequalities naturally arise.
* Figure 1 needs a legend, because right now it is confusing. I understand the red square is the constraint set and the yellow star is the Nash from the caption: what's the difference between the yellow and blue line? Which one is the initial point? It would save my time and improve clarity to have this labeled in full on the actual plot rather than partially explained in a manner that is buried inside the caption which has a lot more details that I may or may not be ready to delve into. The vector fields are also way too small, I can't tell on my display which direction any of the arrows are pointing. The lack of clear labeling makes it difficult to understand the dynamics of the algorithm's convergence.
* Please label all equations, not just the ones you think are important. When discussing technical papers with other people over Zoom, not labeling everything makes it needlessly difficult to communicate precise equation lines. Often, I end up saying "the 3rd equation on page 4" and then my collaborator is confused because they think I am counting by multi-line equation rather than per-line, or they think I am counting from the top rather than the bottom. This waste of time is extremely annoying and the outdated convention of "not labeling important equations to reduce clutter (actually, to reduce ink and paper costs, which no longer exist in the digital world)" needs to go away.
* Font size in figures is a bit small, making it bigger would help see what is happening.
* Notation is not always completely consistent, for instance min and argmin are sometimes italicized, sometimes not.

### Questions
Can you comment a bit further on the role of the barrier function in ACVI, and in the theory of Section 3.2? The barrier function is already a part of ACVI, and therefore not a new component of inexact ACVI - is this correct? If so, why talk about it in detail before Theorem 3.2, rather than in the background section? Does Theorem 3.2 specifically require one of these two barrier functions, and would not work with others? If so, this should be stated more explicitly - right now it's buried in the definition of Algorithm 1, and one has to unroll that definition - including the line above saying "Choosing among these is denoted with $\wp$" - to realize this, which isn't great because it puts a key part of the logic outside of both the text which defines Theorem 3.2 and the text that defines Algorithm 1.

Appendix typo: "subproblems and definitions" -> "Subproblems and definitions" (missing caps)

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The present paper considers the problem of solving a variational inequality with constraints. Recall that a solution $x_\star$ to variational inequality given by $F:\mathcal{C}\to\mathbb{R}^n$ (with $\mathcal{X}\subset \mathbb{R}^n$) satisfies
$$\forall x\in \mathcal{C}\,:\,\langle F(x_\star),x-x_\star\rangle\geq 0.$$
The paper considers monotone VIs, which include convex optimization ($F=\nabla f$ for $f$ convex) and minimal convex/concave games as special cases. The set $\mathcal{C}$ is given by linear equality and convex inequality constraints. 

A standard first-order approach to this problem, such as Korpelevich's extragradient method, would require lots of projection steps to $\mathcal{C}$. Since these may be quite expensive, Yang, Jordan and Chavdarova (ICLR 2023) considered a first-order interior point method. Their approach is based on a rewriting of the constrained VI problem using Lagrangian duality, which leads to an alternating direction method of multipliers (ADMM). Those authors show that their method works (with $O(1/\sqrt{K})$ last-iterate error after $K$ iterations) only under assumptions that are significantly stronger than mere monotonicity (for instance, $F$ is assumed t be Lipschitz).

The present paper strengthens Yang et al's analysis in different ways. First, the algorithm by Yang et al. is shown to converge at the same rate previously shown under the sole assumption of monotonicity (plus strict monotonicity *or* strict convexity of one of the constraints). They also show that, if $F$ is Lipschitz, one may use *approximate* solvers for the optimization problems in each inner loop of the interior point method, while keeping the same convergence rate. Finally, when the constraints are "simple", a projection based method for the inner loop may also be used, with similar assumptions and results. The paper also presents a short empirical study suggesting that the methods given are accurate and faster than the "competition".

### Strengths
The paper greatly increases the scope of application of first order methods in the solution of constrained VIs. In particular, it shows that such methods can be fast, while achieving similar or better theoretical guarantees than the "competition"

### Weaknesses
The main issue I had in reading the paper was the comparison with Yang et al. I tried to follow the long proofs in that paper and to compare them with the present proofs. Many of the steps were similar, but I was still left wondering where the main improvements took place.  

Given this, I have been somewhat conservative in my "contribution" score, but I am perfectly willing to reconsider it in the light of the answer to my question (see below).

___

A small typo: in the first two displays of page 23, the norms in the RHS are missing their squares (the mistake is fixed in the next display).

### Questions
In the proof of Theorem 3.1 (including the preceding Lemmas), can you pinpoint exactly where you manage to circumvent the strict/strong monotonicity assumption of Yang et al? It seems to me that equation (14) is one of the crucial steps: it avoids Lemma 1 in Yang et al, where the gap is bounded as a function of the distance to the optimal VI solution. However, I struggle to see where/how exactly the improvements were achieved.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Previous research has shown that first-order methods can be used to solve general variational inequality (VI) problems under the assumption that analytic solutions for the subproblems are available. This paper circumvents this assumption by using a warm-starting technique. The authors prove the convergence rate of the gap function for the last iteration of both the proposed exact ACVI and inexact ACVI methods. Additionally, the authors discuss scenarios where the inequality constraints are quick to project onto and introduce an alternative version of ACVI, confirming its convergence under identical conditions.

### Strengths
S1: The authors prove that the gap function of the last iterate of ACVI decreases at a rate of $O(1/\sqrt{K})$ for monotone VIs, without depending on the assumption that the operator is L-Lipschitz.

S2: The authors establish the convergence rate for both the exact ACVI and the inexact ACVI methods.

S3: The authors discuss the special case of inequality constraints that are quick to project onto.

S4: Experiments have been conducted to demonstrate that inexact ACVI can outperform other methods, such as the lookahead-Minmax algorithm, by advantageously solving linear systems implicitly beforehand (as shown in Steps 3 and 4 of Algorithm 1).

### Weaknesses
W1. The assumption that F(x) is monotone or strictly monotone may be overly stringent. This condition is not met in applications involving Generative Adversarial Networks. The practical implications of this assumption should be discussed more thoroughly, especially considering the wide range of applications that do not satisfy monotonicity.

W2. The actual efficiency of the algorithm heavily depends on the solution approach for the x-subproblem, which is challenging to solve. The authors do not address the resolution of this general nonlinear system, and the computational cost of solving this subproblem is a critical factor that needs to be analyzed in more detail. The convergence rate of the overall algorithm is highly dependent on the efficiency of solving the x-subproblem, and this dependency should be made explicit.

W3. It is preferred to provide an explanation for assuming the "monotonicity" of $F$ on $\mathcal{C}_{=}$ and the "strictly monotonicity" of $F$ on $\mathcal{C}$. The specific implications of these assumptions on the convergence and stability of the algorithm need to be clarified. The conditions under which these assumptions hold in practical scenarios should also be discussed.

W4. The barrier map is undefined when it first appears in Algorithm 1. This lack of definition makes the algorithm difficult to understand and implement. The barrier map should be defined before it is used in the algorithm.

### Questions
See above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
