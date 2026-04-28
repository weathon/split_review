# Supermodular Rank: Set Function Decomposition and Optimization

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 3, 6, 5

## Abstract
We define the supermodular rank of a function on a lattice. This is the smallest number of terms needed to decompose it into a sum of supermodular functions. The supermodular summands are defined with respect to different partial orders. We characterize the maximum possible value of the supermodular rank and describe the functions with fixed supermodular rank. We analogously define the submodular rank. We use submodular decompositions to optimize set functions. Given a bound on the submodular rank of a set function, we formulate an algorithm that splits an optimization problem into submodular subproblems. We show that this method improves the approximation ratio guarantees of several algorithms for monotone set function maximization and ratio of set functions minimization, at a computation overhead that depends on the submodular rank.
\smallskip 
\newline 
\emph{Keywords:} supermodular cone, imset inequality, 
set function optimization, greedy algorithm, approximation ratio

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors introduce the concept of supermodular rank for functions defined on partially ordered sets. Supermodular rank characterizes how a function can be decomposed into a sum of functions that exhibit a "supermodular" property. This concept allows for a more refined understanding of the structure of set functions. The authors propose optimization algorithms, namely R-SPLIT and R-SPLIT RATIO, for optimizing monotone set functions and the ratio of set functions. These algorithms provide a trade-off between computational cost and accuracy, offering theoretical guarantees for their performance.

### Strengths
1. Introduction of Supermodular Rank: The concept of supermodular rank is considered interesting and valuable for understanding the structure of set functions.

2. Optimization Algorithms: The proposed optimization algorithms, R-SPLIT and R-SPLIT RATIO, are seen as valuable contributions. They provide a trade-off between computational cost and accuracy while offering theoretical guarantees for their performance.

### Weaknesses
1. Complex and Notation-Heavy: The paper is noted as being quite complex and filled with notation, making it challenging to follow. Simplifying the presentation or providing additional explanations could enhance the accessibility of the material.

2. Lack of Clarity on Performance Improvement: The paper's comparison to existing solutions, particularly in Table 2, is mentioned as lacking clarity. It is not immediately clear how the proposed algorithm outperforms existing solutions. The authors should elaborate on the additional benefit brought by the proposed algorithm's computational overhead.

### Questions
See Weakness 2 above.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This work measures how far a function $F$ from being submodular or supermodular. The main idea is the decomposition of $F$ into the sum of the smallest number $r$ of submodular function with a different total order on individual variables. The number $r$ is the submodular rank of $F$. The less interesting part of this work is the elementary submodular rank where the order can be reversed in one variable at most for each function. The paper proposes a simple R-SPLIT algorithm using the proposed notion, which splits up a function $f$ of rank $r+1$ into $2^r$ pieces and runs a simple algorithm e.g. greedy on each piece returning the best solution.

### Strengths
It is clear that this work is novel in terms of the definitions of supermodular/submodular rank and elementary rank. This work also provides both theoretical results and empirical evaluation.

### Weaknesses
The theoretical contribution of this work seems to be very weak. In particular, the elementary rank $r$ basically says that the function becomes submodular for all assignments to a subset of the variables, which leads to an exhaustive search for this subset. The core issue is that the elementary rank, while novel, appears to simply reframe the problem of identifying a subset of variables that, when fixed, result in a submodular function. This rephrasing doesn't inherently offer a computationally tractable method for finding this subset; the proposed R-SPLIT algorithm essentially performs a brute-force search over the $2^r$ possible variable subsets. This makes the theoretical contribution somewhat incremental, as it doesn't provide a more efficient way to handle non-submodularity; it merely quantifies it in terms of the size of the variable subset that needs to be fixed. Hence, demonstrated by the complexity of the algorithmic part, the contribution of this work does not meet the bar of top-tier conferences such as ICLR. I have two additional comments:

1. The current paper is very tough to read.
2. The empirical evaluation is not convincing.

### Questions
1) Seems like when the submodular rank $r$ is high, the algorithms are impractical.
2) Empirical evaluation is not convincing.

### Soundness
3 good

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper considers the supermodular and submodular optimization problem. In these problems, we are given a supermodular/submodular or a related function defined over a ground set. The goal is to select a certain subset of the ground elements such that (1) the selected subset satisfies some properties; (2) the value of the selected subset is optimized. If a function is not submodular/supermodular, one can describe it into several parameters, and the approximation ratio shall also be related to these parameters.

The main contribution of this work is a new approach to grading the space of set function. They propose a new concept called supermodular/submodular rank, which is defined over a partial order set. Based on such a concept, they show that a function can be decomposed into a summation of several \p-supermodular/submodular functions. Then, one can improve the approximation by such a splitting.

### Strengths
1. The high-level idea of this paper is clear. The main technical idea is to decompose a function into a sum of functions that are \pi-supermodular/submodular. And then split the problem into several submodular pieces. This improves the approximation when the submodular/supermodular rank is bounded.

2. This paper is technically involved. To my knowledge, there is no such definition and decomposition in the literature. Probably the most related one is that a submodular function can be decomposed into n! additive functions, but the definition used in this paper is quite different from this.

### Weaknesses
1. The presentation of this work is poor. It seems that the authors ran out of space and moved a lot of background knowledge to the appendix. Without this knowledge, it's hard to get the definition of \pi-supermodular. After moving, it seems that the authors didn't do careful proofreading. For example, R(alpha, gamma) in Theorem 25 is not defined. This significantly impairs readability. I appreciate that the authors also try to explain their ideas with some examples, and I also understand that the space issue is not the authors' fault, but it is a fact that the paper does need a better presentation.

2. To my understanding of Table 2, the proposed algorithm improves the previous ratio only in the case where the elementary submodular rank is a constant. If this is true, it’s not clear how important this improvement is. Because the paper didn't include a discussion about whether there exists some famous functions with a constant submodular rank. Besides this, the paper only includes an upper bound on the rank of a function but excludes the way to compute the rank of a function. Maybe I missed something, and such a computation is trivial, but this should be stated explicitly.

### Questions
See my second comment in Weaknesses.

### Soundness
3 good

### Presentation
1 poor

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper studies the set function optimization problem, where there is a ground element set and the goal is to pick an element subset such that some certain objective is maximized. The authors mainly consider two concrete models: matroid-constrained maximization and set function ratio minimization. In the first model, we are given a monotone, non-negative function $f$ with generalized curvature $\alpha$ and submodularity ratio $\gamma$, and a matroid system $M$. The goal is to pick an element subset $S\in M$ such that $f(S)$ is maximized. The authors prove that there exists a framework such that by applying it to any approximation algorithm with $O(q(m))$ queries ($q(\cdot)$ is a polynomial function), a better approximation ratio can be obtained in time $O(2^{r-1}n^{r-1} q(n))$, where $r$ is the elementary submodular rank. In the second model, we are given two set functions $f, g$ and the goal is to pick a subset $S$ such that $f(S)/g(S)$ is minimized. The authors prove that when $f,g$ are normalized positive monotone functions and $f$ has a bounded elementary submodular rank, they obtain an approximation ratio polynomially that was previously only available when function $f$ was submodular. Finally, the authors conduct experiments to investigate the empirical performance of the algorithms.

### Strengths
- The paper considers two classical and important models in set function optimization. The main contribution of the paper is introducing the concept of elementary submodular rank and building on it to extend the previous results to a more general function class. 

- Both theoretical analyses and experimental evaluations for the proposed algorithms are provided in the paper.

### Weaknesses
A main weakness is that the paper is not well-written. The structure is quite confusing. The formal definitions of the considered models are not provided until section 4. Several new definitions, such as the generalized curvature and submodularity ratio, are introduced before Section 4 without sufficient context. The absence of any intuitive explanations or motivating examples for these definitions, especially the elementary submodular rank, renders the paper less accessible to readers. The connection between these definitions and the optimization problems is not clear until later in the paper, making it difficult to understand the significance of the early sections.

### Questions
(1) Could you give some intuition about the elementary-submodular-rank-based trick used in the paper?

### Soundness
3 good

### Presentation
1 poor

### Contribution
3 good
