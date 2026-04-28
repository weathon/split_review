# Efficient Bisection Projection to Ensure NN Solution Feasibility for Optimization over General Set

- Decision: Reject
- Avg Score: 5.20
- Scores: 5, 3, 6, 6, 6

## Abstract
Neural networks (NNs) have shown promise in solving constrained optimization problems in real-time. However, ensuring that NN-generated solutions strictly adhere to constraints is challenging due to NN prediction errors. Recent methods have achieved feasibility guarantees over ball-homeomorphic sets with low complexity and bounded optimality loss, yet extending these guarantees to more general sets remains largely open. 
In this paper, we develop **Bisection Projection**, an efficient approach to ensure NN solution feasibility for optimization over general compact sets with non-empty interiors, irrespective of their ball-homeomorphic properties. 
Our method begins by identifying multiple interior points (IPs) within the constraint set, chosen based on their eccentricity modulated by the NN infeasibility region. 
We utilize another unsupervised-trained NN (called IPNN) to map inputs to these interior points, thereby reducing the complexity of computing these IPs in run-time.
For NN solutions initially deemed infeasible, we apply a bisection procedure that adjusts these solutions towards the identified interior points, ensuring feasibility with minor projection-induced optimality loss. We prove the feasibility guarantee and bound the optimality loss of our approach under mild conditions. 
Extensive simulations, including non-convex optimal power flow problems in large-scale networks, demonstrate that bisection projection outperforms existing methods in solution feasibility and computational efficiency with comparable optimality losses.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper develops bisection projection to ensure constrained neural network (NN) optimization feasibility over general compact sets with non-empty interiors, irrespective of the so-called ball-homeomorphic properties. Importantly, for NN solutions initially deemed infeasible, the authors apply a bisection procedure that adjusts these solutions towards the identified interior points and lead to feasibility eventually.  Extensive simulations in non-convex optimal power flow problems demonstrate the effectiveness of the proposed bisection projection.

### Strengths
**Originality**: This paper seems original to me. The proposed method is new.

**Quality**: The paper presents solid results and feasibility theory for the proposed bisection method.

**Clarity**: The paper is reasonably well written, and I can follow the basic idea.

**Significance**: The authors demonstrated the effectiveness of their method on a particular class of problems, namely non-convex optimal power flow problems.

### Weaknesses
 **Relevance to the ICLR community**: It is unclear whether the proposed method can be used for a wider class of problems that are of interests to the ICLR community. Non-convex optimal power flow problems do not seem to be a main interest for the ICLR community. Maybe more numerical study is needed to justify the relevance of this paper to the broad ICLR community.



### Questions
1. Bisection seems to be a quite intuitive idea. Can the authors further explain the unique novelty of their approach?

2. Bisection projection is not a true projection, right? It is "approximate projection"?

3. Can the authors further justify the relevance of the proposed method to the general ICLR community?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper presents a methodology for enforcing arbitrary constraints on the output of neural networks.
This achieved through a bisection (line search) between an initial (possibly infeasible) prediction, and an interior (i.e. strictly feasible) solution.

The concept of a line search is sound, and has been used previously in the literature.
The validity of such a line search rests on the availability of an interior point. 
**This is a very strong assumption,** especially in the non-convex setting: if one could obtain interior points for arbitrary sets, then one could perform a binary search on the objective value (similar in principle to the analytic center cutting plane method) and therefore solve the optimization problem efficiently.
In that regard, the training scheme outlined in the paper relies on interior points.

Furthermore, the paper incorrectly claims that it provides feasibility guarantees for arbitrary sets of constraints.
Instead, several assumptions are made throughout the paper (some less explicitly than others) which gradually reduce the validity of the proposed approach.

Finally, numerical experiments lack a description of the data generation procedure used to generate problem instances, as well as a principled ablation study and meaningful comparison against state-of-the-art methodologies (especially regarding the use of multiple interior points in conjuction with prior methods).

The decision to reject thus rests on those aspects:
1. incorrect claims regarding the method's scope
2. the paper's reliance on interior points (which, in general, cannot be obtained efficiently)
3. several theoretical results fail to state their intrinsic limitations
3. insufficient numerical experiments and ablation studies

### Strengths
The paper introduces two components:
* the eccentricity metric for evaluating interior points
* the use of multiple interior points for feasibility restoration

However, the paper does not satisfactorily demonstrate that _both_ components are needed to achieve good performance.
Existing methods such as RAYEN, Gauge mapping and Homeomorphic projection all assume knowledge of an interior point, and could potentially benefit from multiple interior points.
Therefore, the paper lacks a principled ablation study to corroborate its claims.

### Weaknesses
 The paper presents a methodology for enforcing arbitrary constraints on the output of neural networks. This achieved through a bisection (line search) between an initial (possibly infeasible) prediction, and an interior (i.e. strictly feasible) solution.

The concept of a line search is sound, and has been used previously in the literature. The validity of such a line search rests on the availability of an interior point. **This is a very strong assumption,** especially in the non-convex setting: if one could obtain interior points for arbitrary sets, then one could perform a binary search on the objective value (similar in principle to the analytic center cutting plane method) and therefore solve the optimization problem efficiently. In that regard, the training scheme outlined in the paper relies on interior points.

Furthermore, the paper incorrectly claims that it provides feasibility guarantees for arbitrary sets of constraints. Instead, several assumptions are made throughout the paper (some less explicitly than others) which gradually reduce the validity of the proposed approach.

Finally, numerical experiments lack a description of the data generation procedure used to generate problem instances, as well as a principled ablation study and meaningful comparison against state-of-the-art methodologies (especially regarding the use of multiple interior points in conjuction with prior methods).

The decision to reject thus rests on those aspects:
1. incorrect claims regarding the method's scope
2. the paper's reliance on interior points (which, in general, cannot be obtained efficiently)
3. several theoretical results fail to state their intrinsic limitations
3. insufficient numerical experiments and ablation studies

### soundness:
 2

### presentation:
 2

### contribution:
 2

### strengths:
 The paper introduces two components:
* the eccentricity metric for evaluating interior points
* the use of multiple interior points for feasibility restoration

However, the paper does not satisfactorily demonstrate that _both_ components are needed to achieve good performance. Existing methods such as RAYEN, Gauge mapping and Homeomorphic projection all assume knowledge of an interior point, and could potentially benefit from multiple interior points. Therefore, the paper lacks a principled ablation study to corroborate its claims.

### weaknesses:
 The paper has several limitations in its methodology and numerical experiments, as detailed below.

The most fundamental limitation of the paper is that it assumes the availability of an interior point: this is a very strong requirement that may not hold in the general nonlinear, non-convex setting.
* the bisection line search assumes a set of interior points, which are assumed to be provided by a dedicated model (denoted by IPNN in the paper)
* this IPNN is trained by maximizing the approximated eccentricity, which requires knowledge of several points on the boundary of the feasible set.
   As noted in line 314-316, the paper "derive[s] those boundary samples through projection in Alg 1 for infeasible solutions".
    **Importantly, Algorithm 1 requires knowledge of an interior point.**

### Methodology

* l. 56: the use of a bisection algorithm is not a new contribution.
	It was used, for instance, in the homeomorphic projection method of Ref. [LCL23]
* The paper mentions several times that the proposed method guarantees feasibility for general sets (this claim is repeated twice at the end of Section 1). This is not a valid claim: the proposed method only produces feasible solutions on the condition that an interior point is available. The paper does not provide a guarantee that this assumption is always met in practice.
* The paper should cite the following reference: _A New Computationally Simple Approach for Implementing
Neural Networks with Output Hard Constraints_ (https://arxiv.org/pdf/2307.10459).
* The eccentricity metric in Definition 4.1 assumes the feasible set to be compact, and therefore bounded. This eliminates a large set of problems for which the feasible set may be unbounded.
* The result of Proposition 4.1 assumes the availability of a trained model with arbitrary accuracy 
* Theorem 1:
	* The sample-based condition assumes an $r_{c}$-covering dataset. In general, this requires an exponential number of data points (expoential w.r.t input dimension), and an infinite number of points if $\Theta$ has unbounded support.
	* The sample-based condition uses three constants which should be defined in the main body of the paper, as they are important for the proof and the value of the result. In particular, constant $C_{0}$ (which is only defined in the appendix) depends on the rate of variation of the constraint boundary w.r.t $\theta$. This constant may be infinite, for instance, with the following set: $C_{\theta} = ([0, 1] \cup [2, 3]) \cap ([0, \theta])$ for $0 \leq \theta \leq 3$. Note that this set is representable using the following polynominal constraints $x (x-1) (x-2) (x-3) \leq 0, 0 \leq x \leq \theta$. The boundary "jumps" when $\theta$ crosses the value $\theta = 2$.
	* The sample efficiency of the sample-based condition is not better than sampling $O(1/L^d)$ points, where $L$ is the Lipschitz constant of the ground-truth mapping from input data to ground-truth solution.
    * The verification-based condition merely re-states the definition of a feasible point. It also requires solving a neural network verification problem, which is computationally intractable in practice. While relaxing integrality in the verification problem does provide a valid bound, there is no guarantee that it will be strong enough to validate the claim of Theorem 1.
* Proposition 5.1: the proposition again assumes a compact feasible set, and the bound on eccentricity is valid only for a single $\theta$. Therefore, the number of interior-points should be denoted as $m(\theta)$, and may be unbounded w.r.t $\theta$ to obtain satisfactory accuracy. Also note that the bound on $m$ is not asymptotically better than simply splitting the space intohyperboxes that cover the set $C_{\theta}$.

### Experiments

* Convex QCQPs and SOCP are equivalent problem classes
* The data generation methodology for instances considered in the experiments is not presented. The paper should present a complete description of each problem **and** the data generation used to generate instances.
* Chance constraints of the form $P[Ax \geq \theta + \omega] \geq 1 - \delta$, where $\omega$ is Gaussian, are _convex_ and can be represented with a second-order cone constraint. This biases the results of the experiment
* Table 5 (verification-based IPNN performance) does not include AC-OPF instances.
* Instances with 200 nodes are not representative of real-life power systems. Experiments should be conducted on power grids with at least 6000 nodes.

### questions:
 * The paper should clarify how Algorithm 1 is executed during the training of the IPNN, especially regarding the availability of interior points 
* The paper should provide a complete description of the data generation procedure used for the experiments
* The paper should be more explicit about the meaning of constants $C_{0}, C_{1}, C_{2}$ in Theorem 1

Other limitations outlined above should be addressed

### flag_for_ethics_review:
 ['No ethics review needed.']

### rating:
 3

### confidence:
 5

### code_of_conduct:
 Yes

### Questions
* The paper should clarify how Algorithm 1 is executed during the training of the IPNN, especially regarding the availability of interior points 
* The paper should provide a complete description of the data generation procedure used for the experiments
* The paper should be more explicit about the meaning of constants $C_{0}, C_{1}, C_{2}$ in Theorem 1

Other limitations outlined above should be addressed

### Soundness
2

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
1

### Summary
While NNs can generate solutions for constrained optimization problems, ensuring their feasibility remains challenging. Previous methods provide feasibility guarantees only in specific cases, such as ball-homeomorphic sets. This paper presents a Bisection Projection approach that ensures NN solution feasibility across general compact sets, extending beyond the limitations of ball-homeomorphic cases. Additionally, the method offers strong performance with bounded optimality loss and low runtime complexity.

### Strengths
1). The BP framework broadens feasibility guarantees to more general settings by identifying interior points (IPs) within the constraint set with minimized eccentricity relative to the NN infeasibility region. It then employs a bisection algorithm to "project" infeasible solutions onto the constraint boundaries, ensuring minimal optimality loss.

2). This paper utilizes the IPNN to predict IPs with a substantial reduction in runtime of real-time operation.

### Weaknesses
This paper falls outside my current area of expertise.

### Questions
This paper falls outside my current area of expertise.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a novel feasibility-fixing method leveraging bisection projection between infeasible solutions and interior points. The theoretical analysis is thorough and well-developed, and numerical results demonstrate that the proposed approach significantly outperforms existing methods in terms of speed on the evaluated datasets.

### Strengths
1. The paper is well-written, with a clear and logical structure.
2. The method of addressing infeasibility through bisection operations between infeasible solutions and interior points is innovative.
3. The theoretical analysis provided is comprehensive and well-supported.

### Weaknesses
While I do not identify any major weaknesses, I note a few minor points for consideration:

1. The theoretical analysis largely depends on the assumption that IPNN can accurately predict interior points. The authors provide two sufficient conditions supporting this assumption, yet, in practice, these conditions may be challenging to meet, especially in complex, non-convex problems. Specifically, the conditions rely on constants $C_0$, $C_1$, and $C_2$, which are not clearly defined in the main text, making it difficult to assess the practical implications of the theoretical results. The dependence on these constants, which relate to the constraint geometry, IPNN Lipschitz constant, and inner ball radius, respectively, suggests a sensitivity to the problem structure and the quality of the trained IPNN, which needs further discussion.

2. The proposed method focuses on inequality constraints, with no evident adaptation for equality constraints. The problems considered appear to have specific types of equalities that can be removed without impacting optimality, as outlined in Section 3. It would be beneficial to introduce these settings earlier in the paper, particularly in the introduction, to help readers quickly identify the scope and contributions. Furthermore, the method's reliance on equality completion techniques, while mentioned, lacks sufficient detail in the main text, making it hard to evaluate the practical applicability and potential limitations of this approach.

### Questions
1. What are the definitions of $C\_0$, $C\_1$ and $C\_2$ in Theorem 1? Are there any references for these terms?
2. How is the speedup metric calculated? Specifically, what do "total speedup" and "post speedup" represent, and why are total speedups larger than post speedups?
3. Could the authors clarify the meanings of WS, D-Proj, H-Proj, and B-Proj?
4. In Section 7, the heading is "Conclusions and Limitations," yet it only includes conclusions and future directions. Would it be more accurate to either update the heading or add a discussion of limitations?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper addresses the problem of the non-infeasibility of NN-generated solutions of a constrained optimization problem. Their method, termed "Bijection Projection", provides a scalable method to "project" a point onto a general compact set. In addition, they provide theoretical results on the distance between the optimal solution and the projected, feasible one obtained by their method.

### Strengths
- The proposed algorithm is scalable and very generic. It can be applied in many other contexts, especially when a projection step is involved.
- Theoretical justifications are provided adequately. The results and mathematics look sound to me (I am not checking carefully the proof though)
- The presentation is good.

### Weaknesses
Certain arguments and theorem formulations look strange to me. Here are two examples (and please correct me if I am wrong):
- In Section 3 and Appendix A.1, the authors claim that their results can cover equality constraints with constant rank property. I would argue that it is difficult to re-parameterize $x$ to $[x_1, \varphi_\theta(x_1)]$ (Line 803) because the set of variables $x_1$ is not fixed. The choice of $x_1, x_2$ generally depends on the local maps of the manifold $h(x,y) = 0$ at specific points. Except for simple cases such as Linear Equality Constraint in Assumption A.1, I feel their claim is debatable. The author might consider discuss in detail about this issue in the paper. Specifically, the implicit function theorem guarantees the existence of such a re-parameterization locally, but the authors do not address how to ensure that the chosen parameterization remains valid across the entire domain of interest, especially for non-convex constraints. The transition between different local parameterizations and the potential for discontinuities in $\varphi_\theta$ are not discussed, which raises concerns about the practical applicability of this approach for complex equality constraints.
- I find it difficult to understand Theorem 1. What are the constants $C_1$, $C_2$, and $C_3$? They are explained later but they should be explained more formally before or in Theorem 1. The lack of clear definitions for these constants directly within the theorem statement makes it hard to grasp the implications of the theorem. Furthermore, the relationship between these constants and the properties of the constraint set and the Interior Point Neural Network (IPNN) is not immediately obvious, which hinders the understanding of the theorem's practical significance. For example, how do these constants relate to the curvature of the constraint boundary or the complexity of the neural network architecture?

### Questions
- The bijection strategy uses $m$ point independently (by using bisection methods on each segment, separately). Are there better strategies that combine the information of these points? Or asymptotically, this method is already optimal (in certain criteria)?
- How to evaluate (the true)  eccentricity given a subset and a compact boundary?

### Soundness
3

### Presentation
3

### Contribution
2
