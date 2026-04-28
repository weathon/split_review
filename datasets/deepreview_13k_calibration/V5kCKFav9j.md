# A Sinkhorn-type Algorithm for Constrained Optimal Transport

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 6, 8, 3

## Abstract
Entropic optimal transport (OT) and the Sinkhorn algorithm have made it practical for machine learning practitioners to perform the fundamental task of calculating transport distance between statistical distributions. In this work, we focus on a general class of OT problems under a combination of equality and inequality constraints. We derive the corresponding entropy regularization formulation and introduce a Sinkhorn-type algorithm for such constrained OT problems supported by theoretical guarantees. We first bound the approximation error when solving the problem through entropic regularization, which reduces exponentially with the increase of the regularization parameter. Furthermore, we prove a sublinear first-order convergence rate of the proposed Sinkhorn-type algorithm in the dual space by characterizing the optimization procedure with a Lyapunov function. To achieve fast and higher-order convergence under weak entropy regularization, we augment the Sinkhorn-type algorithm with dynamic regularization scheduling and second-order acceleration. Overall, this work systematically combines recent theoretical and numerical advances in entropic optimal transport with the constrained case, allowing practitioners to derive approximate transport plans in complex scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper deals with constrained OT problems and the corresponding entropic regularization formulation which could potentially help researchers and practitioners of OT and Machine Learning to arrive at transport plans that have more complex structure than in the unconstrained case. Theoretically, the work is well grounded in existing literature and the authors have made use of multiple recent advancements to design a Sinkhorn-type algorithm to solve constrained OT problems and also have proposed accelerated convergence methods with corresponding bounds. The authors also provide proofs for the various theorems and propositions under certain assumptions. For methods that rely on kernel approximation, prior work do not account for dynamically evolving kernels in the constrained case such as in case of $K=exp(-C\eta)$ but with the authors approach of using a Lyapunov function to characterize the optimization in the variational formulation allows for solving transport problems with evolving kernels.

### Strengths
- This paper combines ideas from several previous works and extends them meaningfully in novel ways to solve constrained OT problems under both equality and inequality constraints.
- The novelty lies in the use of Lyapunov function to characterize the optimization procedure to perform the constraint update dual step
- Authors have presented convergence analysis of the proposed Sinkhorn-type optimization procedure with acceleration mechanisms
- Authors have provided decent survey of related literature relating to OT, ML and efficient solvers for constrained and unconstrained OT.
- Authors have provided detailed proofs for theorems and propositions wherever necessary.

### Weaknesses
 - The numerical experiments are based on (weak) assumptions such as the cost matrix entries being sampled from uniform distribution in case of random assignment problem or the Rademacher distribution in case of Ranking under constraints (appendix A). It is not clear how the proposed algorithm performs when the cost matrix may not conform to simple distributions. Specifically, the uniform distribution assumption for the random assignment problem may not reflect real-world scenarios where cost matrices often exhibit more complex structures, such as sparsity or clustering. This raises concerns about the generalizability of the empirical results. 
-  Authors could present experiments that would be more relevant to the target ML community. The current experiments, while demonstrating the algorithm's functionality, do not directly address common machine learning tasks where constrained optimal transport could be beneficial. For example, experiments involving image or text data with meaningful constraints would be more compelling.
- Solving large scale problems would help ascertain the claims made by authors about the usability and efficiency of their proposed approach. The current experiments do not provide sufficient evidence to support the claim that the proposed method can scale to large, practical problems. The absence of experiments on high-dimensional data or large-scale datasets limits the assessment of the algorithm's scalability and efficiency.

### Questions
Questions:
- For the Random assignment problem, how would the algorithm behave if cost matrix is not generated through uniform sampling and instead has some other distribution? Do you have any observations or thoughts?
- Sinkhorn supports backpropagation in neural networks owing to matrix/vector operations and hence can be used as part of the loss function or during intermediate steps in computation. Can you comment on whether your approach can be used directly in a similar fashion? Please explain your reaasoning.

Minor suggestions that won't affect the score:
- Line 166/167: “the following” repeated twice in the statement "We summarize the general form of constrained optimal transport by the following the following linear program (LP)"
- Consider citing combinatorial OT solvers that have been proposed that have successfully shown applications in ML to compute partial optimal transports

### Soundness
3

### Presentation
4

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
This paper addresses scalable solutions to the problem of optimal transport by Kantorovich relaxation, under arbitrary additional linear constraints. By introducing a set of slack variables and adopting an entropic regularization, it arrives at a dual formulation, which is then solved by a block coordinate descent algorithm with three blocks. Two of them can be exactly optimized leading to a Sinkhorn-type procedure, while the third block, corresponding to the additional inequality constraints is proposed to be solved by the Newton's method. Some discussions  about accelerating the Newton's method is provided on account of the sparsity of the Hessian.

On the theoretical side, the paper shows two main results: first the fact that entropic regularization has an exponentially decreasing effect on the solution, w.r.t. the regularization parameter and second a guarantee on a sublinear rate of convergence of the algorithm.

The results are finally verified in some numerical experiments.

### Strengths
Constrained optimal transport may have various applications. IN ML it can be used e.g. for various domain adaptation scenarios with structured data. However, OT is a difficult problem to solve at scale. The Sinkhorn-type algorithms are widely believed to be a suitable way to address the difficulties with the exact OT problem. The paper pursues such a solution and the discussion is supported by rigorous mathematical results.  The numerical results also reflect the superior convergence properties of the proposed algorithm.

### Weaknesses
I generally find the paper interesting, but have few concerns regarding the motivation of the problem, the justifications of the algorithmic choices and the implications of the theoretical results.

My main concern is that I am not sure if the choice of an entropy regularization makes sense for the additional constraints. For the standard OT problem, this choice is justified as the dual problem can be solved by exact block coordinate descent, but if one needs to employ the Newton's method, then, why should not one use e.g. a logarithmic barrier (instead of entropic regularization), which has the self-concordance property and is potentially better for the doubling strategy. The use of Newton's method suggests that the problem is not easily solved via coordinate descent, so the motivation for using entropic regularization is unclear and should be further justified.

Most of the analysis seems like a straightforward extensions of previous works Weed (2018) and Altschuler et al. (2017). A general concern about Theorem 1 is that although it is formulated as an exponential decay, it really shows the requirement that the regularization parameter grows proportionally with the inverse of the duality gap. In practice, the gap can be extremely small for large problems, leading to extremely large regularization parameters. On the other hand, the result of Theorem 2 seems to be dimension-free, but it actually depends on the dimension through the regularization parameter. As such, I think that Theorem 2 should clearly reflect the dependency on eta (which is hopefully linear as in Altschuler et al. (2017)). The practical implications of the theoretical results are not clear, especially concerning the choice of the regularization parameter and its effect on the convergence rate.

Although the authors mention some applications of their problem in their literature review, I think that the paper generally does not well motivate the study. The experiments are on toy scenarios and do not reflect scalability as they consider relatively small problems. For the MNIST case, for example, a more realistic domain adaptation scenario could be considered with at least few thousand points in each domain.

### Questions
I generally find the paper interesting, but have few concerns:

1- My main concern is that I am not sure if the choice of an entropy regularization makes sense for the additional constraints. For the standard OT problem, this choice is justified as the dual problem can be solved by exact block coordinate descent, but if one needs to employ the Newton's method, then, why should not one use e.g. a logarithmic barrier (instead of entropic regularization), which has the self-concordance property and is potentially better for the doubling strategy.

2- Most of the analysis seems like a straightforward extensions of previous works Weed (2018) and Altschuler et al. (2017). A general concern about Theorem 1 is that although it is formulated as an exponential decay, it really shows the requirement that the regularization parameter grows proportionally with the inverse of the duality gap. In practice, the gap can be extremely small for large problems, leading to extremely large regularization parameters. On the other hand, the result of Theorem 2 seems to be dimension-free, but it actually depends on the dimension through the regularization parameter. As such, I think that Theorem 2 should clearly reflect the dependency on eta (which is hopefully linear as in Altschuler et al. (2017)).

3- Although the authors mention some applications of their problem in their literature review, I think that the paper generally does not well motivate the study. The experiments are on toy scenarios and do not reflect scalability as they consider relatively small problems. For the MNIST case, for example, a more realistic domain adaptation scenario could be considered with at least few thousand points in each domain.

### Soundness
4

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents Entropy regularization formulation and a Sinkhorn algorithm to solve a more generalized class of Optimal Transport (OT) problems --- specifically, OT problems with inequality and equality constraints. 

The writing and presentation are clear and unambiguous for the most part. There is a significant theoretical contribution since the paper considers a larger class of problems than the ones typically considered in OT-related works. However, the motivation of the problem is lacking. Acceleration techniques that are presented in Section 3.1 are not necessarily original since they are an obvious extension of existing techniques. I think there is enough reason to accept the paper since it addresses an OT formulation that is rarely explored. More specifically, this solution is the first of its kind, and it will interest the ICLR audience. Having said that, I do have some reservations about giving a strong acceptance recommendation. 

One of the listed contributions (on Partial Optimal Transport) is only mentioned briefly and not included in the main paper. This seems like an attempt to bypass the page limit constraints, which, in my opinion, should not be encouraged. However, I will leave that to the discretion of the editors.

### Strengths
- The paper takes initial steps in the natural direction of OT problem research. 
- The theoretical results (such as the convergence rates and bounds) presented herein will likely be referenced in the foreseeable future. So, the results themselves are significant.

### Weaknesses
Firstly, the problem itself is not motivated well in the paper. The authors should consider working on the introduction to establish the relevance of this work better. The current introduction does not adequately convey why constrained optimal transport is a problem of interest to the machine learning community. The paper would benefit from a more compelling narrative that highlights the practical scenarios where such constraints are necessary, rather than simply stating it is a generalization of existing OT problems. For instance, the paper could discuss specific applications in areas like domain adaptation or fairness-aware machine learning where constrained OT could provide a more suitable framework than unconstrained OT. 

Secondly, the only novelty I see is in Algorithm 1. However, I consider the theoretical contribution itself significant enough to overlook this shortcoming. While the theoretical results are indeed valuable, the algorithm itself seems to be a straightforward application of existing Bregman projection techniques with the addition of an entropic barrier for inequality constraints. The paper could benefit from a more detailed discussion on how this specific combination of techniques leads to a novel algorithm, rather than just stating it as a direct extension. A more thorough analysis of the computational complexity and the practical implications of this specific algorithmic choice would also be beneficial.

### Questions
- What is $n$ in Theorem 1?
- It is not clear why $f$ is a Lyapunov function. Can the authors explain this part in more detail?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper studies the algorithm for solving the optimal transport problem under equality and inequality constraints. The authors derive a Sinkhorn-type algorithm to solve the constrained optimal transport problem.

### Strengths
The paper extends the Sinkhorn algorithm to unconstrained optimal transport problem to constrained optimal transport problem successfully.

### Weaknesses
1. The paper is hard to follow. The paper lists technical details and equations without further explanations.  For example, which is function L in Line 202? There are no further comments or interpretations of Theorem 2. Sometimes, the author refers to the equation in the appendix, for example, Line 297. The message is not direct. For example, what is Section 3.1 for? Merge some points in Section 1.1 to make the contributions clearer. It is highly recommended that the authors reorganize and polish the paper to make it accessible...

2. What is the motivation for focusing on the constrained optimal transport? Although it could be theoretically interesting to extend Sinkhorn to this kind of optimization problem, the author should make the significance of studying the problem clear.

3. What is the resulting computational complexity of the proposed Sinkhorn-type algorithm?  It seems that only polynomial time can be proved in the paper, which is not attractive enough. The complexity of the Sinkhorn-type algorithm for solving unconstrained optimal transport problems is O(n^2/\epsilon^2); it seems that a comparable complexity should be derived for constrained optimal transport problems.

### Questions
1. Line 187, what does depending only on the LP mean? It is not clear to me that a constant can depend on the linear optimization problem.

2. Line 244, parameter setting can simply your analysis instead of ensuring the efficiency of the algorithm. Can the author improve their justifications of K=O(1), K+L=O(1)?

3. Line 227, in terms of computational complexity, APDAGD can not outperform.

### Soundness
2

### Presentation
2

### Contribution
1
