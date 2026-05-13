# COT: Consistent Optimal Transport with Applications to Visual Matching and Travelling Salesman Problems

- Decision: Reject
- Scores: 10, 6, 5, 3

## Abstract
This paper generalizes the vanilla Optimal transport (OT) to the so-called Consistent Optimal Transport (COT) accepting more than two measures as input with transport consistency. We formulate the problem as minimizing the transport costs between each pair of measures and meanwhile requiring cycle-consistency among measures. We present both the Monge and Kantorovich formulations of COT and obtain the approximate solution with added entropic and consistency regularization, for which an iterative projection (RCOT-Sinkhorn) algorithm is devised to improve the Sinkhorn algorithm. We show the superiority on the task of visual multi-point matching, in which our COT solver directly utilizes the cosine distance between learned features of points obtained from off-the-shelf graph matching neural networks as the pairwise cost. We leverage the algorithm to learn multiple matching and the experiments show a great improvement without more feature training. Furthermore, based on COT, we propose a new TSP formulation called TSP-COT and also adopt regularization to relax the optimization and use the modified RCOT-Sinkhorn algorithm to get the probability matrix of TSP routing. Then post-process search method  is adopted to get the TSP routs and the experiments show the superiority of our method. The code will be available.

## Human Reviews

## Human Reviewer 1

### Rating
10

### Rating Number
10

### Confidence
3

### Summary
The paper considers a generalized Optimal Transport (OT) problem that has pairwise transport between multiple distributions with an added constraint to ensure the formation of a closed cycle. The authors present an iterative Sinkhorn algorithm to solve the Kantorovich formulation of the above-mentioned problem.
I think the paper is well-written and well-motivated. In particular, the alternative formulation of the TSP is very interesting, especially when one takes into account the performance and computation time. The problem itself is well-motivated with multiple applications. The numerical results often outperform, or at least stay competitive, with the state-of-the-art in all the examples.

I think there is a strong case for the acceptance of this paper.

### Strengths
- The quality of writing and presentation is high. Consequently, the results are presented in a clear and concise manner.
- While I do not think there is much originality/novelty (apart from the alternative TSP problem formulation) on the theoretical side, the improvements seen in the numerical simulations make a strong case for the significance of these results.

### Weaknesses
Not weaknesses per se, but I would like to see the following information included:
- I would like to see how sensitive the results are with respect to the optimization parameters, such as $\delta$.
- Table 1 should have computation time. Line 471 says that running time is presented in Table 1, but I do not see it.

### Questions
I don't have any questions in particular. However, I did notice a couple of typos (e.g., line 307 RCOT) and random capitalizations of words while reading, so I recommend that the authors perform thorough proofreading.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper extends the scope of Optimal Transport (OT) theory to cases involving more than two probability distributions, introducing a framework called Consistent Optimal Transport (COT). The authors explore transportation among three (or more) probability measures while enforcing cycle-consistency, which ensures that the transport plan respects consistency across the measures. Unlike the traditional OT problem, the COT's Kantorovich formulation becomes a nonlinear optimization problem due to these additional constraints. To address computational challenges, the authors propose a regularized version of COT using entropic and cycle-consistency regularization, which leads them to use the Sinkhorn algorithm for approximate solutions. As a by-product, this work offers a novel formulation for the Traveling Salesman Problem, offering insights into finding the shortest route that visits each city once and returns to the starting point.

### Strengths
The paper is clear and well-written, with well-defined goals and contributions, including detailed algorithms. Additionally, the problem addressed is novel, and the authors highlight connections to other well-known problems, such as the Traveling Salesman Problem (TSP).

### Weaknesses
The authors mention a connection to the multi-marginal OT problem, noting that both multi-marginal OT and COT involve multiple distributions. They state, "However, the multi-marginal OT primarily emphasizes learning the joint coupling among more than two distributions, whereas our focus is on learning the coupling between each pair of distributions and maintaining cycle-consistency constraints among these couplings". As a point of curiosity, are there any other non-trivial connections between the multi-marginal OT problem and COT beyond the fact that both involve multiple probability measures?

The authors are motived by the algorithms proposed for approximating the computation of GW. Please provide a few references in this regard.   

The authors include a section on the Numerical Convergence Analysis. Can the authors say anything about the analytic convengence of their methods? 

Minor details:

- Line 94: "The Monge problem is exactly not easy to calculate [...]" Add: "and an optimal T might not exists" (as is pointed out later in section 3.1)
- Line 188, eq (7): replace T_k by T_K, that is, capitalize the subindex 
- Use either "travelling" or "traveling" consistently through the paper, that is, pick one option.

### Questions
The authoirs are motived by the algorithms proposed for approximating the computation of GW. Please provide a few references in this regard.   

The authors include a section on the Numerical Convergence Analysis. Can the authors say anything about the analytic convengence of their methods? 

Minor details:

- Line 94: "The Monge problem is exactly not easy to calculate [...]" Add: "and an optimal T might not exists" (as is pointed out later in section 3.1)
- Line 188, eq (7): replace T_k by T_K, that is, capitalize the subindex 
- Use either "travelling" or "traveling" consistently through the paper, that is, pick one option.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper addresses the challenge of computing consistent optimal transport across multiple measures. The authors propose a cycle-consistent version of the Monge formulation, which is then relaxed to the Kantorovich formulation. Finally, it is further relaxed into an optimization problem regularized by cycle consistency and entropy, solved using an iterative Sinkhorn-like algorithm. The approach is demonstrated on several problems, including consistent point matching in computer vision and approximating solutions for the combinatorial traveling salesman problem.

### Strengths
- The problem of consistent multiway optimal transport is compelling, and the authors effectively demonstrate its relevance through several potential applications. To my knowledge, both the formulation and approach are new.
- The authors present a comprehensive approach that includes Monge and Kantorovich formulations, entropic relaxation, and optimization algorithms.
- The connection to the Traveling Salesman Problem (TSP) is a valuable addition.
- The experimental results, particularly in the point matching experiment, underscore the motivation for computing cycle-consistent optimal transport.

### Weaknesses
### strengths:
 - The problem of consistent multiway optimal transport is compelling, and the authors effectively demonstrate its relevance through several potential applications. To my knowledge, both the formulation and approach are new.
- The authors present a comprehensive approach that includes Monge and Kantorovich formulations, entropic relaxation, and optimization algorithms.
- The connection to the Traveling Salesman Problem (TSP) is a valuable addition.
- The experimental results, particularly in the point matching experiment, underscore the motivation for computing cycle-consistent optimal transport.

### weaknesses:
 - The exposition could be improved. Parts of the paper are challenging to read, especially for readers without prior familiarity with the subject. For instance, the transition between sections 3.1 and 3.2 feels abrupt and lacks a clear explanation of the underlying motivations for the proposed relaxations. Providing a more intuitive explanation of the conceptual steps would improve the readability.
- The authors define "COT's Monge Formulation," "COT's Kantorovich," and then introduce relaxations in Section 3.2. While these formulations appear similar to the traditional Monge-Kantorovich formulations with entropic relaxation, it's unclear if similar properties apply. For instance, the existence of a solution to the Monge formulation in Eq. (6) is not explicitly addressed. A rigorous proof or a detailed discussion on the conditions guaranteeing the existence of a solution would strengthen the theoretical foundation. Furthermore, the relaxation from the Monge formulation in Eq. (6) to the Kantorovich formulation in Eq. (8) needs further clarification. What specific properties are being relaxed, and what are the trade-offs involved? A more thorough discussion of these formulations and any necessary conditions is needed.
- The author's definition of cycle-consistency seems to be order-dependent, relying on the order of the probability measures \( \alpha_k \). It only accounts for consecutive pairs. Although this is briefly mentioned for applications in point matching, it is not discussed in more detail. A more comprehensive analysis of this order-dependency is crucial. How does this dependency affect the theoretical guarantees of the method? Are there specific scenarios where this dependency might lead to suboptimal solutions? Exploring potential ways to mitigate this dependency, perhaps by considering all possible orderings or by introducing a more robust definition of cycle-consistency, would be valuable.
- The connection to the Traveling Salesman Problem (TSP), while intriguing, requires a more detailed explanation. Specifically, how are the nodes and edges of the TSP graph represented within the COT framework? What are the specific cost matrices used in this context? Furthermore, what can be said about the quality of the approximate solution obtained through the COT formulation compared to existing TSP solvers? Providing a more concrete mapping between the COT formulation and the TSP problem, along with a theoretical analysis of the approximation quality, would significantly enhance this section.
- It’s difficult to assess whether cycle-consistency is achieved exactly or approximately, in theory and in experiments, and at what rate. A more rigorous analysis of the cycle-consistency properties of the proposed method is needed. Does the iterative algorithm guarantee convergence to an exactly cycle-consistent solution? If not, what is the theoretical bound on the deviation from cycle-consistency? Providing empirical results on the rate of convergence and the degree of cycle-consistency achieved in different scenarios would strengthen the experimental evaluation.
- The ablation study in Section 4.3 is unclear. What are the "certain factors"? The setup and conclusions of this study need to be clarified. Providing a detailed description of the experimental setup, including the specific factors being ablated and the metrics used for evaluation, is essential. Furthermore, a more thorough discussion of the results and their implications for the proposed method is needed. For example, how does the performance vary with different choices of these factors, and what are the optimal settings?


Additional issues and comments:
- Abstract: Challenging to read.
- The first sentence of the introduction is incomplete.
- "introduce the entropic regularization transforming the hard cycle-consistency": the regularized version seems to seperately include an entropy term and a cycle-consistency term, so this statement may be inaccurate.
- "matrix-vector iterative method": unclear.
- Line 69: What is "MCTS"?
- "We generalize OT to the marginal consistent case": This is confusing since "multi-marginal" is later described as something related but different.
- "The Monge problem is exactly not easy to calculate and a popular improvement is the Kantorovich relaxation": please revise.
- "C is the cost matrix defined by the divergence": is it limited to this C?
- Line 138: What is "LAP"?
- "In contrast, our method employs a training-free approach that assumes consistency is satisfied on the test set, using this prior information to improve performance during inference." please clarify.
- Line 246: RCOT-PGD is mentioned but is not defined or explained (except in the Appendix).
- Line 248: What is "GW"?
- "RCOT-Sinkhorn achieves cycle-consistency results": Approximately or exactly cycle-consistent? Are there any guarantees?
- Figure 3: Somewhat unclear.
- "The setting of Hyper-parameter \(\delta'\)": What about the entropic regularization parameter \(\epsilon\)?
- Algorithms 1-5 are not included in the main text.

Typos:
- Line 47: "there calls"
- Line 52: "cost of three trasnsportation"
- Line 69: "we contribute"
- "is one of the simple but efficient methods"
- Eq (6): Summation should be over k.
- Line 345: "k<0" => "k<K"

### questions:
 - What is the connection to multimarginal OT? The authors mention briefly in Section 2 but do not elaborate.

### Questions
- What is the connection to multimarginal OT? The authors mention briefly in Section 2 but do not elaborate.

============
post-rebuttal: Increasing my rating from 3->5

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a "cycle-consistent" optimal transport (COT) formulation : given a sequence of (say, discrete) measures $\alpha_1,\dots,\alpha_K$, the goal is to minimize 
$$ (P_1,\dots,P_k) \mapsto \sum_{k=1}^K \braket{C_k, P_k}$$
where $C_k$ is a cost matrix, $P_k$ should be a transportation plan between $\alpha_k$ and $\alpha_{k+1}$ (with the convention that $\alpha_{K+1} = \alpha_1$, and the $(P_k)_k$ are related through the _cycle-consistency constraint_ $\prod_{k=1}^K P_k = I$.

Because the cycle consistency constraint is non-linear, solving the COT problem is harder than solving standard OT problems, and thus the authors propose to resort on two layers of regularization: relaxing the constraint $\prod_{k=1}^K P_k = I$ using a divergence term (here, a Froebenius norm) and add an entropic regularization term (a common idea in computational OT for the last decade). They derive an mirror descent like scheme to minimize their regularized problem. 

Eventually, they observe that their formulation may be adapted to resemble the celebrated Traveler Salesman Problem (TSP).

### Strengths
The formulation of the COT problem is somewhat intriguing and I do believe that it may be of interest in some situations. 

The relation with the TSP is interesting. I appreciate that the authors acknowledge the limitations of their approach and do not "oversell" it.

### Weaknesses
## 1. Clarity

Overall, the paper lacks clarity in its writing. Key issues include the following:

**Unclear or Misleading Statements:** Numerous sentences are either unclear or misleading. For example, in the abstract, it’s stated that the COT problem considers each pair of measures, which implies that one must compute the optimal transportation cost between all pairs, i.e., between each $\alpha_i$ and $\alpha_j$, for $1 \leq i, j \leq K$. However, the paper actually focuses only on transportation between adjacent measures, $\alpha_k$ and $\alpha_{k+1}$.

**Inconsistent and Incorrect Notation:** Mathematical notation is inconsistently and sometimes incorrectly applied. For instance, the scalar product is denoted by < x, y >, which should be written as \langle x, y \rangle or using the braket package for $\braket{x, y}$. Additionally, notations should be standardized—sometimes measures contain $N$ points, while other times they contain $n$. Such issues, though minor in isolation, collectively impede readability.

**Formatting of Proofs:** The proofs in the appendix are poorly formatted, with equations split across multiple lines without necessity (for example, $d P_k$ at the end of Eq. (25) and in Eq. (26)). This formatting makes it difficult to review the proofs accurately.

**Placement of Algorithms:** The algorithms are all placed in the appendix but are referenced in the main paper as if they were essential. While it’s acceptable to include optional material in the appendix, the main text should be self-contained. Therefore, the algorithms should either be included in the main paper if they are necessary or clearly marked as optional if they’re not.

**Lack of Informative Content in Some Sentences:** Some sentences add little information. For instance, the introductory sentence, "Optimal transport (...) is a tool to learn the optimal transportation between the source and target probability measures," requires prior knowledge of what optimal transportation means, offering minimal insight. Additionally, comparisons with the Gromov--Wasserstein (GW) problem are not particularly useful here, as the GW problem is fundamentally different and is not introduced in this work. Relaxing the cycling constraint to a penalty seems natural and doesn’t require extensive justification.

## 2. Motivation of the method, comparison with multi-marginal OT, soundness, and mathematical grasp on the problem. 

The motivation for introducing the COT problem is limited, and the authors seem to lack critical distance from their work. For example:

**Motivation of the approach and Comparison with multi-marginal OT (MMOT):** It is regularly said that the contribution of this paper is to "generalize the OT problem to more than two marginals " (abstract, contributions section, etc.), but this is precisely what multi-marginal OT is about. The paper mentions multi-maginal OT and, while I understand the formal difference between the two approach (they are different problems, for sure), I fail to see the practical difference: when should one use MMOT or COT? The paper does not give a proper answer to this central question in my opinion. 

**Dependence on the Order of Measures:** The formulation of the COT problem depends on the order of $\alpha_1, \dots, \alpha_K$, yet this is not discussed. This could be crucial; for example, if a user has a set of measures from an experiment, how should they be ordered? Is the solution permutation-equivariant? (in which case I would agree that the ordering does not matter)

**Applicability of Birkhoff’s Theorem:** The authors assume discrete uniform measures with $N$ points each, but it’s unclear whether Birkhoff’s theorem applies here. Specifically, is it generally true that the optimal $P_1, \dots, P_K$ are permutation matrices if we only assume that $P_k \in U(a_k, a_{k+1})$ in Eq. (8) rather than $P_k \in {0,1}^{N \times N}$? Understanding this is essential for motivating the adaptation to the Traveling Salesman Problem (TSP), the behavior of entropic regularization as $\epsilon \to 0$, and related points.

**1D Case in Figure 2:** In Figure 2, the measures are depicted in 1D. In this case, it’s known that the standard OT plan is monotone, involving matching quantiles. Unless something is overlooked, this suggests that cycle-consistency is automatically satisfied without enforcement, making this experiment barely supporting the proposed approach. Could this be confirmed?

### Questions
See Section 2. in the Weaknesses block.

Note : rating updated after rebuttal.

### Soundness
1

### Presentation
1

### Contribution
2
