# Verifying Properties of Binary Neural Networks Using Sparse Polynomial Optimization

- Decision: Accept
- Scores: 6, 6, 5, 6

## Abstract
This paper explores methods for verifying the properties of Binary Neural Networks (BNNs), focusing on robustness against adversarial attacks. Despite their lower computational and memory needs, BNNs, like their full-precision counterparts, are also sensitive to input perturbations. Established methods for solving this problem are predominantly based on Satisfiability Modulo Theories and Mixed-Integer Linear Programming techniques, which 
 often face scalability issues.
 We introduce an alternative approach using Semidefinite Programming relaxations derived from sparse Polynomial Optimization. Our approach, compatible with continuous input space, not only mitigates numerical issues associated with floating-point calculations but also enhances verification scalability through the strategic use of tighter first-order semidefinite relaxations. We demonstrate the effectiveness of our method in verifying robustness against both $\|.\|_\infty$ and $\|.\|_2$-based adversarial attacks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents a novel approach for verifying properties of Binary Neural Networks (BNNs), particularly in the context of robustness against adversarial attacks. Traditional verification methods for BNNs, such as Satisfiability Modulo Theories (SMT) and Mixed-Integer Linear Programming (MILP), face scalability issues when applied to larger networks. To address these challenges, the authors propose using Semidefinite Programming (SDP) relaxations derived from sparse polynomial optimization. This approach is designed to verify BNN robustness efficiently and accurately, overcoming numerical challenges inherent in MILP solvers. Experimental results indicate that the SDP-based method provides significant improvements in both robustness verification against adversarial attacks and computational efficiency, with an average speedup of 4.5 to 11.4 times compared to conventional methods.

### Strengths
-  Introduces a new SDP-based approach that enhances the scalability and precsion of BNN verification.
 - Efficiently handles continuous input spaces without requiring input quantization.
 -  Theoretical contributions, including tighter SDP relaxations, improve the accuracy of robustness bounds.
  - Experimental validation across benchmarks highlights the method’s advantages in speed and robustness certification.

### Weaknesses
The paper presents an interesting approach; however, it lacks sufficient model variety in its experiments. Only two models were used to demonstrate the proposed method, which limits the generalizability and persuasiveness of the results. For a more robust evaluation, it would be beneficial to include additional models, particularly from diverse architectures, to strengthen the findings and validate the method across a broader range of scenarios.

### Questions
Could the authors provide additional experimental results on a wider variety of models? Including more model architectures would enhance the robustness of the conclusions and provide a stronger case for the method’s effectiveness across different settings.

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
The paper introduces a novel method for verifying the robustness of Binary Neural Networks (BNNs) against adversarial attacks using Semidefinite Programming (SDP) relaxations derived from Sparse Polynomial Optimization. This approach outperforms existing LP relaxation used in MILP-based verification methods without introducing much computation overhead. Specifically, the authors suggest that the SDP-based relaxations could be embedded within branch-and-bound algorithms in MILP solvers to improve bound estimation, accelerating the verification process without altering the core MILP framework. Their method achieves bounds that are up to 55% tighter than those obtained with traditional linear relaxations and demonstrates significant computational efficiency, especially under large input perturbations.

### Strengths
1. **Novel Use of SDP for BNN Verification**: Employing sparse Polynomial Optimization and SDP relaxations for BNN verification represents an innovative approach, potentially enhancing scalability and precision over existing MILP-based methods.

2. **Significantly Improved Bounds**: By using SDP relaxations, the authors achieve up to 55% tighter bounds compared to traditional linear relaxations in MILP, a notable improvement in robustness certification accuracy.

3. **Efficient Computation**: Experimental results demonstrate considerable speedups (up to 50x in severe attack scenarios), showing that the method is computationally efficient and less conservative in bounding compared to LP-based techniques, especially in high-dimensional BNNs.

4. **Broad Norm Compatibility**: The method accommodates both ∥.∥∞ and ∥.∥2 norms for adversarial attacks, expanding its applicability across different attack types, which is less common in the BNN verification field.

### Weaknesses
1. **Limited Dataset and Network Complexity**: The experiments are primarily on MNIST-based networks, which may not fully demonstrate the method’s performance on more complex datasets or larger architectures. Specifically, the reliance on MNIST, a relatively simple dataset, raises questions about the scalability of the proposed SDP relaxation approach to more challenging scenarios involving higher-resolution images and deeper network architectures. The verification of BNNs on datasets like CIFAR-10 or ImageNet, which exhibit more intricate feature dependencies, would provide a more robust evaluation of the method's practical applicability. Furthermore, the network architectures used appear to be relatively shallow; it is unclear how the method would perform with deeper BNNs, where the accumulation of approximation errors in the SDP relaxation could become more pronounced.

4. **Comparative Analysis with State-of-the-Art**: While comparisons with LP and MILP are made, a broader comparison with recent state-of-the-art BNN verification techniques could further validate the advantages and potential limitations of the SDP-based approach. The paper would benefit from a more comprehensive comparison against other methods that address the verification of BNNs with continuous input spaces. For example, a comparison with SAT/SMT-based approaches, even if those methods are not directly scalable to the same problem sizes, would help to contextualize the performance of the proposed method. Additionally, a more detailed analysis of the trade-offs between tightness of the bounds and computational cost compared to other relaxation-based methods would be beneficial.

### Questions
1. Have you tested this method on more complex datasets or architectures beyond MNIST? If so, what were the results, and if not, do you anticipate any challenges?

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
4

### Summary
This paper introduces a novel approach to verify the robustness of BNN based on sparse polynomial optimization, specifically through Semidefinite programming relaxation. The authors first encode the original verification problem as a polynomial optimization problem (POP) and then apply SDP relaxation on it to obtain lower bounds for certifying the robustness. While the verification method is sound and incomplete, experimental results show that it provides a more precise bound than LP-based methods.

### Strengths
- The problem (verification of Transformers) is important.
- A novel method based on SDP to verify the robustness of BNN.
- Compared to LP-based methods, a more precise lower bound is obtained.

### Weaknesses
 - The motivation for this approach is not intuitive. The authors claim that existing methods are either incompatible with continuous input data or are limited to $L_\infty$ input perturbations. However, expanding support to other types of input regions may not constitute a compelling contribution: i) $L_\infty$ perturbations are the primary standard in the field, and ii) most BNN verifiers support continuous input spaces. Furthermore, for methods $M$ specifically designed for discrete input region (i.e., input $x\in$ {-1,1}$^{n_0}$), one can also treat the second layer (assuming the original input region is continuous, as the setting in this work) as the new input layer and then apply these methods $M$ to verify the robustness.
- The experimental results are not convincing. The MILP-based method, which is sound and complete, solves significantly more verification tasks than the proposed SDP-based approach. While the authors introduce a "soft" encoding to avoid numerical errors, it is relatively straightforward similar to methods in previous work. The comparison with MILP is also not entirely fair, as the MILP solver is allowed to terminate as soon as a feasible solution is found, while the SDP solver is run to optimality. This makes it difficult to assess the true performance of the proposed approach.
- For $L_\infty$ experiments, it would be beneficial to include comparisons with other SOTA methods, such as the SMT-based approach (Amir et al.). 
- As Gurobi supports multi-threaded solving, presenting experimental results on multiple threads would also strengthen the evaluation. It is unclear if the reported runtimes for Gurobi are obtained using multi-threading or single-threading. This makes it difficult to compare the efficiency of the proposed method against MILP.
- Table 3 gives more results on bound computation, however, it is not clear if these bounds lead to verified results (i.e., proving the robustness). The table only shows the tightness of the bounds, not the actual verification performance. It is important to show that the tighter bounds actually translate to more instances being verified.

### Questions
See the weakness raised in **Weaknesses**.

Other minor comments:

- I failed to find the explanation for what the data in parentheses in Column $\tau_{tighter,cs}^1$ represent in Tables 1 and 2.
- MILP methods aim to verify whether a property holds or fails, offering a definitive answer rather than estimating bounds to certify robustness. Therefore, comparing the two approaches (SDP-based vs. MILP-based) should ideally focus on metrics related to verification success rates, computational efficiency, or scalability across various network sizes, rather than on bound tightness.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper considers the formal verification of binary neural networks in the classification setting.
Formal verification is necessary as (any) neural network is inherently prone to adversarial attacks.
In the paper, the robustness of binary neural networks is verified using semidefinite programming derived from polynomial optimizations.
In particular, polynomials up to order 2 are used as constraints and existing solvers (Mosek, Gurobi) are used to prove the robustness property by providing a lower bound.
The experients considers l_2 and l_inf robustness properties and shows that while achieving better bounds than simple linear programming, it also has a reduced verification time than related methods based on MILP/MINP.

### Strengths
- the considered problem is highly relevant
- deep theoretical analysis that goes beyond simple linear relaxations and rather design the verification algorithm to exploit certain properties of the considered network architecture
- The theoretical results show strictly better bounds (Thm. 3.1 & 4.1), which proves the point of using the more complex verification algorithm.
- the approach allows to verify more general input perturbations. In particular, l_2, which was not considered before in binary neural network verification although it has been considered in standard neural networks.

### Weaknesses
Main points:
It is hard to follow the theoretical analysis in the paper. I tried to identify some of the key issues and give examples for each case:
- Crucial results from references are used without re-stating them or at least providing the exact equation number in the reference paper:  E.g., Sec. 4: "Firstly, notice that the semi-algebraic representation of the subgradient of the ReLU function derived in Chen et al. (2020) provides an alternative encoding of the sign(·) function." This sentence in then used without further explanation to transform (7) into (17). The paper should explicitly state the relevant equations from Chen et al. (2020) to justify this transformation, as it's not immediately obvious how the subgradient of ReLU directly translates to an alternative encoding of the sign function. The lack of a clear connection makes it difficult to verify the correctness of this step.
- Formal inconsistencies: E.g., it is unclear what the output of sign(0) is; (4) says that W can be in {-1,0,1} but later in Sec. 3 says it is in {-1,1}, which might influence how certain normalizations have to be considered, e.g., the bounds in (11). The paper needs to define the behavior of sign(0) explicitly and consistently throughout the paper. The inconsistent definition of W also introduces ambiguity in the normalization process, potentially affecting the validity of the derived bounds. The paper should clarify whether the weights are always {-1,1} or if {-1,0,1} is also considered and how this is handled in the normalization.
- try to introduce all concepts before they are used. E.g., the term "cliques" is not properly introduced. It appears to be sets of neurons but I am unable to assess how they are determined. Also, the variable "d" is used throughout Sec. 2.3 but is only later introduced as "relaxation order". Similarly, the operation "nv(A)" is introduced after its first usage in (12), making (12) unable to be understood by the reader up to this point. It is explained in the paragraph after, but I think moving such things to the notation section would be more beneficial as they are used throughout the paper and a reader can then go back to the notation section to (re-)refer to those details. The paper should define all terms and notations before their first use, including "cliques", "d", and "nv(A)". The definition of "cliques" should include how they are determined from the network structure. The variable "d" should be introduced as "relaxation order" before its first usage. The operator "nv(A)" should be defined in the notation section before it appears in equation (12).
- Steps to derive the constraints are rather quick and more explanations could help to follow along. The paper should provide more detailed explanations for each step in deriving the constraints, especially the transformations from (7) to (17), and how the input region constraints are combined with the network structure constraints. The current explanations are too brief and make it difficult to follow the derivation process.

Additionally, the experiments show only single-dimensional results without saying over how many instances the results are averaged and do not provide a standard deviation where applicable. Also, it is unclear if the compared approaches are taken from the literature or arbitrarily constructed. If the latter is true, it misses a comparison to related work altogether.

Minor points:
- It is unclear why the approach does not suffer from floating point inaccuracies. In fact, the term "floating-point" only appears twice in the paper (only in the abstract and the contribution section (Sec. 1.1)).
- the paper claims that the approach does not suffers from an exponential running time (Sec. 6) but it misses a thorough analysis of its runtime. The average speed up of 4.5 / 11.4 stated in the contribution section (Sec. 1.1) does also not support this claim.
- Make the example in Fig. 1 a running example by moving it further up in the paper and continuously refer to it when explaining all terms.
- Similarily, give an intuitive explanation why adding those tautologies are necessary
- Only the classification setting is considered. This could be stated more clearly.
- the related works section could also include more research on the verification of standard neural networks (e.g., VNN-COMP) to better place this line of research in the broader context.
- Fig 2: misses a label and ticks of the x axis.
- no repeatability package is provided

### Questions
- Can you provide the missing details about the evaluation I mentioned above?
- You mentioned in Sec. 2.3 that you use the (tractable) inner approximations of the set of polynomials that are nonnegative on S. Why is it enough to only consider that subset?
- Why can the weights take values {-1,0,1} but the bias any value in |R?
- Why does you appraoch not suffer from floating-point inaccuracies?

### Soundness
2

### Presentation
2

### Contribution
3
