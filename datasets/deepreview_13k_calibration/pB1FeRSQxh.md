# Near-Optimal Quantum Algorithm for Minimizing the Maximal Loss

- Decision: Accept
- Avg Score: 6.00
- Scores: 5, 5, 8, 6

## Abstract
The problem of minimizing the maximum of $N$ convex, Lipschitz functions plays significant roles in optimization and machine learning. It has a series of results, with the most recent one requiring $O(N\epsilon^{-2/3} + \epsilon^{-8/3})$ queries to a first-order oracle to compute an $\epsilon$-suboptimal point. On the other hand, quantum algorithms for optimization are rapidly advancing with speedups shown on many important optimization problems. In this paper, we conduct a systematic study for quantum algorithms and lower bounds for minimizing the maximum of $N$ convex, Lipschitz functions. On one hand, we develop quantum algorithms with an improved complexity bound of $\tilde{O}(\sqrt{N}\epsilon^{-5/3} + \epsilon^{-8/3})$.\footnote{Throughout this paper, $\tilde{O}$ omits poly-logarithmic factors, i.e., $\tilde{O}(f)=O(f\poly(\log f))$.} On the other hand, we prove that quantum algorithms must take $\tilde{\Omega}(\sqrt{N}\epsilon^{-2/3})$ queries to a first order quantum oracle, showing that our dependence on $N$ is optimal up to poly-logarithmic factors.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents an improved quantum algorithm for minimizing the maximal loss of $N$ convex functions, the key idea is quantum Gibbs sampling subroutine that improves the classical subroutine.

The paper studies the problem of minimizing the loss of $N$ convex functions, i.e., $\min_{x} \max_{i \in [N]}f_{i}(x)$ for convex functions $f_{1}, \ldots, f_{N}$ given gradient oracle. The best classical algorithm for finding $\epsilon$-approximate solution is given by [Carmon et al. 2021] with $O(N\epsilon^{-2/3} +\epsilon^{-8/3})$ queries, which is known to be optimal in the low accuracy regime $\epsilon \geq 1/\sqrt{N}$. The idea is to approximate the maximal loss with softmax function and use the improved ball optimization oracle [Carmon et al. 2020].

The paper studies quantum algorithms and the algorithm is equipped with zero-th order quantum oracle (it can be used to obtain gradient oracle) and improve the bound to $O(\sqrt{N}\epsilon^{-5/3} +\epsilon^{-8/3})$. It also gives a lower bound saying $\Omega(\sqrt{N}\epsilon^{-2/3})$ queries are necessary for finding $\epsilon$-approximate solution.

The main idea of the algorithm is an improved estimation of the gradient, which in turns boils down to improved quantum Gibbs sampling procedure (note the gradient draws from a distribution, which requires $N$ queries, but quantum algorithm could take advantage and only needs $\sqrt{N}$ queries)

### Strengths
The paper gives improved quantum algorithm for a basic problem in convex optimization. The idea of using quantum Gibbs sampling for improve is interesting.

### Weaknesses
The major unsatisfactory point is the unmatched upper and lower bound.

The presentation is fine in general, but it could be improved (e.g. I found the English a bit awkward some time). Some detailed comments:

(1) Page 1.  "Nesterov (2018) showed ..."  I believe it is an old result, not shown recently. Probably change it to something like "it is known that .... e.g., see Nesterov (2018) ".

(2) Page 4. "named ket" I don't think you need to name it. For quantum people, they know what's the notation means; for non-quantum people, it is not informative and it does not appear twice in the paper.

(3) Line 5 in Algorithm 1. The subscription is confusing.

(4) Page 8 " given in Ref.  Carmon et al. (2021)". Remove Ref.

### Questions
I tried to understand Algorithm 2 (quantum sampling algorithm), but due to some time constraints, I did not fully understand it and I believe some better explanation should make the paper better.

I understand that you first find the $K$ largest elements of the distribution, and then you set the probability of rest element equals the probability of the $K$-th element -- this changes the distribution. Do you need some rejection sampling procedure afterwards?
(Is the answer is in figure 1? Then it would be better to move figure to the main paper).

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper designs new quantum algorithm for the problem of minimizing the maximum of $N$ convex functions with near optimal quantum query complexity. 

Given $f_1,\ldots, f_N$ convex and $L$-Lipschitz functions from $\mathbb{R}^d$ to $\mathbb{R}$. The function $F_{max}(x)$ is defined as:  $F_{max}(x)$  = ${max}_{i} \\{f_i(x)\\}$. 

The goal is to find an $x*$ so that $F_{max}(x*) - inf_{x} F_{max}(x) \leq \epsilon$. 

This is a fundamental optimization task and substantial research has gone in identifying the number of oracle queries required (say to $f_i$s and its gradients - called the first order oracle) as a function of both $N$ -- the number of functions, and $\epsilon$ -- the error parameter. Tight results have been established (matching upper and lower bounds in the number of queries) in the literature for some regimes of parameters (especially for $\epsilon \geq 1/\sqrt{N}$).  However, these prior research only focused on 'classical queries.' In this paper the authors consider 'quantum query complexity' of the problem.  It is well established that in general quantum query algorithms can get a quadratic speed up over classical query algorithm. The present paper extends that to the above described minimizing-the-maximum-loss problem.  

The paper establishes an upper bound of $\tilde{O}(\sqrt{N} \epsilon^{-5/3} + \epsilon^{-8/3})$ and a lower bound of $\tilde{\Omega}(\sqrt{N}\epsilon^{-2/3})$ on the number of quantum queries required for solving the problem. 

Thus with respect to $N$, the established results are optimal. But there is a gap in upper and lower bounds in terms of $\epsilon$. Closing this gap, the authors pose as a natural open question. The quantum oracle model they use is what is typically seen in the literature and is called the zeroth-order oracle  in the optimization terminology.

### Strengths
The strength is that the paper  reports progress on a fundamental and well-studied optimization task. It is natural to consider the question whether the speed up you get in other quantum search algorithms (such as in Grover's algorithm) can be lifted to the optimization literature also.  So in that sense, the results established are clean and informative.

### Weaknesses
A weakness is the originality. It appears that nothing very new is going on here and the results (at least with respect to $N$) are expected. Also, it is not optimal with respect to $\epsilon$. In fact, known classical algorithms do better with respect to $\epsilon$. So in that sense the picture is not complete, which the authors do not seem to address. The paper's quantum query complexity bound of $\tilde{O}(\sqrt{N} \epsilon^{-5/3} + \epsilon^{-8/3})$ is not competitive with classical methods, particularly in the dependence on $\epsilon$. For instance, classical algorithms using first-order information can achieve $\epsilon^{-2}$ dependence, which is significantly better than the $\epsilon^{-5/3}$ and $\epsilon^{-8/3}$ terms in the quantum bound. This raises questions about the practical relevance of the presented quantum algorithm, especially since the quantum speedup is only in the dependence on $N$, which is already well understood.

### Questions
It will be nice to further explain  the reason for the gap in upper and lower bounds, in particular in comparison with classical algorithms. Is the reason classical algorithm does better in $\epsilon$ is because of more powerful (first order as opposed to zeroth order) oracle? Also, I am not clear what you mean by the statement "However, as far as we know, ..." the last sentence before Contributions. Probably it is good idea to make sure it is indeed open.  It is probably fine for smaller results in the paper, but for the main question you are considering, it is better to make sure that the status of the problem.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper studies the question of minimizing the maximum of N convex Lipschitz loss functions f1, f2,...,fN. It is known that you can do so with O(N eps^{-2/3} + eps^{-8/3}) queries. The paper here studies a quantum version of the problem and achieve a complexity that is sqrt{N} eps^{-5/3} + eps^{-8/3}. While the eps-dependence is slightly worse, the dependence on N has improved by a quadratic factor. 

The main idea is to take a classical algorithm for the problem and modify one of the key-steps to exploit quantum advantage. Specifically, the authors exploit the fact that the classical algorithm uses a regularized ball optimization oracle (BROO) which is similar to a Gibbs sampling problem. The latter is known to have a quantum advantage and exploiting the better algorithms for that gives the final result.

### Strengths
The paper studies a natural problem in optimization and shows that quantum algorithms could do better.

### Weaknesses
A disadvantage is that the algorithm in a sense takes an existing classical algorithm and replaces a step in it with a suitable, known, quantum algorithm. So novelty is a bit low.

### Questions
None.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper considers a convex optimization problem where the function to be minimized is the maximum of $N$ convex Lipschitz functions. The paper presents a quantum algorithm which finds an $\epsilon$-good solution using $\tilde{O}(\sqrt{N}\epsilon^{-5/3} + \epsilon^{-8/3})$ queries. The paper complements the algorithmic result with a lower bound showing that the dependence on $N$ is optimal up to logarithmic factors.

The paper builds on the classical algorithm of Carmon et. al. which is based on the Ball optimization acceleration technique, and then identifies parts where a quadratic quantum speedup can be applied.

### Strengths
The results of the paper are novel and interesting. Furthermore, the dependence of the number of queries of the algorithm that is presented in the paper on the number of functions $N$ is shown to be optimal up to logarithmic factors.

I also find the paper to be generally well written.

### Weaknesses
There is still a gap between the query-complexity of the algorithm and the shown lower bound in terms of the dependence on $\epsilon$, but this is not a significant weakness of the paper.

### Questions
The quadratic speedup is a recurring feature of quantum algorithms and in many cases the phenomenon at the core of the speedup is the same. The techniques described in this paper can perhaps be applied to other computational/optimization problems. I wonder if one can state a general meta-theorem of the form: "For a wide class of computational/optimization problems, if we have a classical algorithm that solves it and which satisfy some properties, then we can find a corresponding quantum algorithm with a quadratic speedup".

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
