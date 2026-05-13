# ADMM for Nonconvex Optimization under Minimal Continuity Assumption

- Decision: Accept
- Scores: 6, 6, 6

## Abstract
This paper introduces a novel approach to solving multi-block nonconvex composite optimization problems through a proximal linearized Alternating Direction Method of Multipliers (ADMM). This method incorporates an Increasing Penalization and Decreasing Smoothing (IPDS) strategy. Distinguishing itself from existing ADMM-style algorithms, our approach (denoted IPDS-ADMM) imposes a less stringent condition, specifically requiring continuity in just one block of the objective function. IPDS-ADMM requires that the penalty increases and the smoothing parameter decreases, both at a controlled pace. When the associated linear operator is bijective, IPDS-ADMM uses an over-relaxation stepsize for faster convergence; however, when the linear operator is surjective, IPDS-ADMM uses an under-relaxation stepsize for global convergence. We devise a novel potential function to facilitate our convergence analysis and prove an oracle complexity $\O(\epsilon^{-3})$ to achieve an $\epsilon$-approximate critical point. To the best of our knowledge, this is the first complexity result for using ADMM to solve this class of nonsmooth nonconvex problems. Finally, some experiments on the sparse PCA problem are conducted to demonstrate the effectiveness of our approach.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper investigates the ADMM for multi-block composite optimization problems. An adaptive penalization technique is employed to enhance convergence. The global convergence result of the proposed proximal linearized ADMM is derived under mild smoothness conditions.

### Strengths
This theoretical paper provides complete theoretical results to prove the proposed algorithms achieve competitive complexity under mild smoothness conditions. The analysis covers a broad range of problems, including those with linear constraints and problems that involve explicit proximal operators (e.g., manifold optimization). This approach encompasses a wide variety of problem categories.

### Weaknesses
The paper is written in a way that compiles all the technical material with complex notations, making it difficult for readers to follow. It would be beneficial if the author could summarize the results more effectively and provide insights and discussions.

In the numerical section on sparse PCA, it is unclear why the parameters $\dot{\rho} = 10$ and $\beta^0 = 50\dot{\rho}$ are used consistently. These values appear to be dependent on the Lipschitz constant as suggested in the theoretical section. Given that the problem scales differ in the experiments, it would be more consistent with the theoretical results to adjust the parameters accordingly.

Additionally, there are notational errors and typos that should be corrected. For example, in line 1565, the RHS should include coefficient 2. I have noticed several similar issues throughout the paper that should be rechecked.

### Questions
1. Could you provide more insight into the increasing $\beta$ update rule in (2)? I notice in line 1809 that there is a trade-off between two terms to derive the best complexity results. However, can it be shown that such type of $\beta$ update rule is optimal? A discussion or analysis regarding the optimality of this approach would be valuable.

2. In the numerical experiments section, the function used in the sparse PCA example does not appear to satisfy the smoothness assumption. It would be beneficial to conduct further analysis that incorporates the properties of the orthogonal constraints, leading to an equivalent formulation that fully aligns with the assumptions and supports the theoretical analysis.

3. Given that the algorithm involves several parameters, is it straightforward to determine their values in practice? It would be helpful if additional experiments were conducted to demonstrate the robustness of the algorithm with respect to parameter selection and to provide guidance on how to choose these parameters effectively.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a novel proximal linearized ADMM algorithm with an Increasing Penalization and Decreasing Smoothing (IPDS) strategy, termed IPDS-ADMM. The proposed method tackles multi-block nonconvex composite optimization problems under a less stringent assumptions, requiring continuity in only one block of the objective function. Additionally, this work provides the first complexity result for nonconvex, nonsmooth minimax problems.

### Strengths
* The algorithm guarantees convergence for ADMM under less stringent conditions.

* It establishes the first convergence results for solving nonconvex, nonsmooth minimax problems.

* The IPDS strategy ensures convergence for matrices $A$ that are either bijective or surjective.

### Weaknesses
 * It remains unclear whether the IPDS strategy can be extended to handle inequality or more general constraints. Specifically, while the algorithm allows for nonsmooth and non-Lipschitz functions in blocks $h_i(x_i)$ for $i \in [n-1]$, the practical implications of this for handling complex inequality constraints, beyond simple indicator functions, are not fully explored. The paper does not provide a clear methodology for how to translate a general inequality constraint into a form suitable for the proposed algorithm, nor does it discuss the potential challenges in doing so.

* In Section 4, given the compact results and dense notation, it would be helpful to emphasize the role of the IPDS strategy in the analysis, with additional explanatory comments to enhance clarity. The current presentation makes it difficult to discern the specific contributions of the IPDS strategy versus standard ADMM techniques. The analysis would benefit from a more explicit discussion of how the increasing penalization and decreasing smoothing parameters interact with the convergence proof, and how these choices impact the overall performance.

* A suggestion is to use alternative notation in Lemma 4.8 for $\epsilon_1,\epsilon_2,\epsilon_3$, as these are typically reserved for sufficiently small constants. Using these symbols for parameters that are not necessarily small can lead to confusion and misinterpretation. It would be more appropriate to use notation that clearly distinguishes these parameters from the standard use of $\epsilon$ for arbitrarily small values.

* While the sparse PCA experiments provide valuable insights, demonstrating the method’s effectiveness across a broader range of applications could further support its effictiveness in diverse problem settings. The current experimental section focuses primarily on sparse PCA, and while this is a relevant application, it does not fully showcase the versatility of the proposed method. Additional experiments on other problem instances, such as those mentioned in the introduction (e.g., Robust Sparse Regression, Dual PCP, and Robust LRA), would be beneficial.

### Questions
See weaknesses.

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
2

### Summary
This paper proposes a variety ADMM algorithm called IPDS-ADMM for multi-block nonconvex composite optimization problems, introducing an Increasing Penalization and Decreasing Smoothing strategy using Moreau envelope technique to further decrease the smoothness conditions on the objective function of previous works. The authors also conducted some experiments on sparse PCA problem to show the effectiveness of the proposed method.

### Strengths
1.	The proposed IPDS-ADMM weaken the smoothness assumption for nonconvex multi-block composite optimization that requiring continuity in only the last block of the objective function.

2.	The convergence analysis of the proposed algorithm is given for the case that the associated matrix is either bijective or surjective.

### Weaknesses
1.  The iteration complexity of the proposed algorithm seems to be not outstanding compared to previous nonconvex ADMM approaches mentioned in Table 1. Also, in section 3, the authors claim that IPDS-ADMM improve the complexity from O(ϵ^(-4)) to O(ϵ^(-3)) compared with RADMM, but it is unclear whether the comparison is fair due to RADMM focus on the manifold optimization problem and have the different assumptions with the proposed algorithm.

2. Regarding the experiments, how did the author choose the hyper-parameters of the other compared algorithms and are those hyper-parameters optimized for each algorithm? Further details are needed to ensure the fairness of the comparison. Also, the authors conduct the experiment on some small-scale datasets. Is the proposed algorithm efficient in such tasks with large-scale datasets?

3. A typo. ‘Mereau Envelope’ in Line 221 should be Moreau Envelope.

### Questions
1.  The iteration complexity of the proposed algorithm seems to be not outstanding compared to previous nonconvex ADMM approaches mentioned in Table 1. Also, in section 3, the authors claim that IPDS-ADMM improve the complexity from O(ϵ^(-4)) to O(ϵ^(-3)) compared with RADMM, but it is unclear whether the comparison is fair due to RADMM focus on the manifold optimization problem and have the different assumptions with the proposed algorithm.

2. Regarding the experiments, how did the author choose the hyper-parameters of the other compared algorithms and are those hyper-parameters optimized for each algorithm? Further details are needed to ensure the fairness of the comparison. Also, the authors conduct the experiment on some small-scale datasets. Is the proposed algorithm efficient in such tasks with large-scale datasets?

3. A typo. ‘Mereau Envelope’ in Line 221 should be Moreau Envelope.

### Soundness
3

### Presentation
3

### Contribution
2
