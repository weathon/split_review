# Differentiation Through Black-Box Quadratic Programming Solvers

- Decision: Reject
- Scores: 5, 6, 5, 3

## Abstract
In recent years, many deep learning approaches have incorporated layers that solve optimization problems (\eg, linear, quadratic, and semidefinite programs). Integrating these optimization problems as differentiable layers requires computing the derivatives of the optimization problem's solution with respect to its objective and constraints. This has so far prevented the use of state-of-the-art black-box numerical solvers within neural networks, as they lack a differentiable interface. To address this issue for one of the most common convex optimization problems -- quadratic programming (QP) -- we introduce \textbf{dQP}, a modular framework that enables plug-and-play differentiation for any QP solver, allowing seamless integration into neural networks and bi-level optimization tasks. Our solution is based on the core theoretical insight that knowledge of the active constraint set at the QP optimum allows for \emph{explicit} differentiation. This insight reveals a unique relationship between the computation of the solution and its derivative, enabling efficient differentiation of any solver, that only requires the primal solution. Our implementation, which will be made publicly available, interfaces with an existing framework that supports over 15 state-of-the-art QP solvers, providing each with a fully differentiable backbone for immediate use as a differentiable layer in learning setups. To demonstrate the scalability and effectiveness of dQP, we evaluate it on a large benchmark dataset of QPs with varying structures. We compare dQP with existing differentiable QP methods, demonstrating its advantages across a range of problems, from challenging small and dense problems to large-scale sparse ones, including a novel bi-level geometry optimization problem.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper addresses a common issue in Quadratic Programming (QP) by proposing a decoupled algorithm for computing gradients. The core principle is to utilize the KKT (Karush-Kuhn-Tucker) conditions to recover the dual variables $\lambda$, $\mu$, given only the primal variables. Additionally, the paper employs the active set method, allowing for the reconstruction of an equivalent new problem based on the provided primal solution $z^*$, which includes only the original equality constraints and the active inequality constraints. Consequently, this work presents a generalized scheme for backpropagation in computational optimization layers, expanding the options for solvers.

### Strengths
1. The paper achieves a commendable integration and decoupling of algorithms. Previous works in differentiable quadratic optimization often entangled forward and backward algorithms, or required backward algorithms to utilize dual variables, which were only provided by a few solvers (like gurobi and cplex). By leveraging the KKT conditions to recover dual variables and offering a corresponding backpropagation method, this paper resolves the coupling issue present in earlier approaches. 

2. By addressing the coupling of forward and backward processes, the paper enables the selection of optimal solvers to enhance forward performance in the optimization layer. The extensive experiments presented demonstrate improved success rates and times in the forward process when using existing differentiable optimizers such as QPTH and SCQPTH. Thus, the findings of this paper can be applied to larger problem sizes.

### Weaknesses
1. While this work builds upon established methods effectively, there may be room for further originality in certain aspects. Though it successfully resolves the coupling issue in related works, it is limited to the specific case of QP. The recovery of KKT conditions in QP simplifies to solving a linear equation; however, in more general cases, altering the function (f) could lead to a non-linear problem, necessitating solvers that handle such complexities, which may incur additional computational costs. 

2. There are concerns regarding the fairness of the experimental comparisons. Although the paper demonstrates faster solver speeds due to the ability to select optimal solvers, it should be noted that these optimal solvers (e.g., Gurobi) are implemented in C/C++, while QPTH and SCQPTH are implemented in Python. Given the inherent speed differences between these languages, the observed performance advantage may stem from the implementation language rather than the algorithms themselves. It would be beneficial for the authors to present additional experimental data showcasing the time taken by QPTH, SCQPTH, and dQP during both the forward and backward processes. A separate demonstration using QPTH/SCQPTH for the forward process combined with dQP for the backward process would further ensure a fair comparison. 

3. The paper mentions a lack of GPU support. From the perspective of the backward process, the proposed backpropagation algorithm appears straightforward to apply to batches of data, similar to the capabilities of OptNet in this context. However, the absence of GPU support seems to arise from the external solvers utilized, which do not support GPU implementation. Given the significance of batch processing on GPU for deep learning training, it may be advantageous to develop Python versions of some solvers to enable batch mode support.

### Questions
See weakness.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes dQP, a framework for differentiation of blackbox quadratic programming solvers. The method is based on the observation that an inequality-constrained QP can be re-phrased to a locally equivalent equality-constraint QP given the active set at the solution. This eliminates the inactive inequality constraints from the differential KKT matrix, which is substantially reduced in dimension and becomes symmetric, allowing for faster derivative computation. The required factorization can also be used to compute dual variables from the primal variables, enabling support for solvers that only produce primal variables as outputs.
Experimentally, the authors test their method on a diverse benchmark of QP problems. Especially when the QPs are structured, dQP inherits the benefits of the superiority of the enabled blackbox solvers compared to the simpler dense solvers in existing differentiable QP layers, which allows dQP to be applied to much larger sparse QPs.

### Strengths
- dQP as a programming package seems very useful, the ability to choose between any state-of-the-art solver is a strong selling point.
- Re-using the matrix factorization that from the derivative computation for calculating the optimal dual variables from the primal variables is useful insight.
- The bi-level geometry optimization problem is an interesting new application of differentiable optimization methods.

### Weaknesses
 - The theoretical contribution of the paper is minor. The only insight is that the optimal dual variables can be obtained by re-using the KKT matrix factorization.
- The experiments do not sufficiently disentangle forward and backward computation time. Whenever the forward+backward time is reported, the authors should also report the the forward and backward time individually. It is clear that the solvers used in dQP can solve larger problems faster on the forward pass, but it is also important to see how the required compute for the derivative computation compare to exisitng differentiable QP layers.
- Currently, the "modularity and performance" and "scalability" experiments feel like simply benchmarking the different solvers, the gradient computation time is reported but no actual learning takes place. The Sudoku experiment does not really show any advantage over the previous OptNet method (also, here the training times are missing to jusge how big the disadvantage of not allowing GPU parallelization in dQP is). The paper would be much stronger if these results would be moved to the appendix, and more results of the kind of "Bi-Level Geometry Optimization" would be included instead.
- dQP does not allow GPU parallelization, as opposed to previous methods.
- The factorization used to solve eq (6) and (7) depends on the active set $J$, which means we cannot re-use it if we encounter a different active set by changing only the vectors $(q,b,d)$ while keeping $(P, A, C)$ constant. This is in contrast to computing a factorization of the whole KKT matrix as in OptNet, which can be re-used for any value of $(q,b,d)$. This could be a significant drawback in scenarios where $(P, A, C)$ remains constant during training, while only $(q,b,d)$ is learned, potentially requiring a full re-factorization at each step. The paper does not discuss the computational cost of this re-factorization or strategies to mitigate it, such as warm-starting the factorization based on the previous active set.

### Questions
- I am confused regarding the authors interpretation of explicit vs implicit, which is highlighted many times throughout the manuscript. If I understand correctly, the authors use the term explicit to refer to the fact that by using a factorization of the KKT matrix inverse (e.g. eq (6) and (7)) no optimization procedure has to be used to obtain the result on the left hand side. But why is this in any way fundamentally different to the (according to the authors implicit) differentiation in eq. (3) by multiplying with the inverse of the KKT matrix and solving using a factorization? After all, eq. (7) is exactly the result obtained from the *implicit* function theorem applied to an equality-constrained QP?
- The factorization used to solve eq (6) and (7) depends on the active set $J$, which means we cannot re-use it if we encounter a different active set by changing only the vectors $(q,b,d)$ while keeping $(P, A, C)$ constant. This is in contrast to computing a factorization of the whole KKT matrix as in OptNet, which can be re-used for any value of $(q,b,d)$. Have the authors thought about this potential drawback? I assume it could be especially relevant in some applications where $(P, A, C)$ is considered constant throughtout the training procedure and only $(q,b,d)$ is learned. Is it e.g. possible to re-use the factorization of the KKT matrix with $(P, A, C_J)$ to more efficiently compute the factorization of a KKT matrix for a different active set $(P, A, C_{J'})$?
- The authors write: "Furthermore, our approach not only simplifies computation but also allows for the use of fast, specialized linear solvers that exploit the problem’s structure" (line 322) Could the authors elaborate on this? Is this already used in the software package?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper belongs to the area that focuses on embedding optimization problems into neural networks. Here, optimization algorithms are integrated directly within neural networks, allowing the optimization problem to be treated as a layer with gradients that can propagate through it. This enables end-to-end learning, where neural networks learn not only representations but also parameters of embedded optimization problems.
The paper aims to integrate any quadratic programming solver in a black-box manner without specific requirements (like the availability of a dual solution), i.e., it implements the backward pass for any optimizer, using only its primal solution. The method is based on differentiating the KKT optimality conditions and solving the reduced system, where the unnecessary inactive constraints are removed.

### Strengths
- The material is presented with care, and it is easy to read and follow. The problem is clearly described in great detail, and I believe the text is accessible to a broad audience.
- The idea of an independent and universal backward pass for any QP is interesting both theoretically and practically, and this paper contains a valid contribution to this topic.
- Although the idea of solving the differentiated KKT system with removed inactive constraints already appeared in prior works, this paper systematically describes and formalizes it.
- Theorem 1 allows us to compute the backward pass efficiently solely from the forward primal solution. This seems to be a new contribution.

### Weaknesses
 - Although I personally accept the motivation that drives this work, the presented arguments should be backed by some evidence:
	- At the top of page 2, it is claimed that "many optimizers" do not provide dual solutions without mentioning any. The listed ones (Gurobi and MOSEK) provide them for QP problems.
	- There, it is also claimed that many existing methods are coupled to a tailor-made solver. Please name them.
	- At the end of related work/differentiated programming, it is claimed that the mentioned frameworks often offer limited support for solvers and may require access to a dual solution. I'm unfamiliar with all the details of these methods, and it would be beneficial if the paper could list the limitations explicitly.
- Some fragments of the theory and algorithm are missing. The overall idea is (in my opinion) clear and known. The strengths could have been in filling in the important details.
	- Computing the dual solution is said to be optional (step 4 in Algo. 1). I don't see how the derivatives (step 5) are computed if step 4 is skipped -- Eq. 7 contains both primal and dual solution.
	- Factorization (l. 320) and prefactorization (l.317, l.330) are mentioned, but never explained
- Unfortunately, any quantitative evaluation of the method is missing. All three presented experiments demonstrate and compare the performance of a selected solver. The proposed backward pass (Alg. 1) is not evaluated and I cannot confirm the proposed computational benefits of dQP.
	1. (Modularity and Performance) The "best-performing solver for each problem" with dQP backward is shown to be faster and more accurate than certain methods with their fixed solvers dedicated to certain problems. The backward pass times are not shown in separation. It it just a solver benchmark (and moreover not a fair one; OptNet was not run on GPU, which is its strength.)
	2. (Scalability) Also, OptNet was designed for lot of small dense problems and has a parallel implementation on GPU. The comparison on large sparse problems on CPU is not much valuable.
	3. (Sudoku) Loss over epoch is not informative since both methods should do the same thing (GD using analytic gradients). Training over time can tell more if dQP would prove to have more efficient backward. However (as noted) dQP suffers from infeasible solutions and OptNet is faster due to batched GPU implementation.
	4. (Bi-Level Geometry Optimization) It is just a solver comparison of forward times, not related to dQP.

Overall, the problem is well-motivated, and the approach is theoretically and practically promising. While the novelty of deriving the backward pass from the forward primal solution alone is valuable, gaps in the theoretical explanation, missing evidence to support the claims about limitations in existing methods, as well as the lack of a quantitative evaluation directly comparing the proposed backward pass with other methods, limit the paper's impact.

### Questions
- It is mentioned that gradients are obtained 'explicitly' from the primal solution. How?
- It is frequently promoted that something is 'explicit' ("Notably, our explicit perspective recasts the traditional implicit differentiation approach into an explicit method" l.87, "derivatives can be explicitly derived" l.272, "optimal point can be explicitly differentiated" l.301, "it provides an explicit expression for both the primal-dual optimal point" l.293). I don't see how the formulas are more explicit than those in the implicit function theorem -- It requires solving a linear system. I recommend avoiding this promotion.
- The paper claims that it is the first method of this kind. For instance, "LPGD: A General Framework for Backpropagation through Embedded Optimization Layers" unifies several methods and is applicable also to QP (they also do the Sudoku experiment)


- l.15 “This has so far prevented the use of state-of-the-art black-box numerical solvers within neural networks, as they lack a differentiable interface.” There are several solutions to this problem, mainly of LP, see the LPGD paper and the references therein.
- l. 244 “ensuring that a small perturbation of the _solution_ does not alter the active set” shouldn't it be 'parameters'?
- l. 250 "Implicit differentiation of these yields..." What is implicit here? It's just taking the derivatives of the equations and the chain rule.
- l.312"...the basic Sensitivity Theorem allows one to bypass the need for implicit differentiation techniques." If I understand correctly, the Theorem is based on the implicit function theorem. Hence, there is no bypass, in fact.
- l.322 I don't understand the use of 'linear solvers to exploit the problem's structure'.
- Fig 3 is not referred to in the text, and I don't understand its purpose.
- I think the overall idea of dQP is repeated too many times, and then the place for more valuable things is missing. It also feels like marketing in some places.
- Section "Approach" may be called standardly "Method."
- Related work might also mention "Unrolling methods."

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper presents dQP, a framework for differentiating QP solvers, and conducted the experiments through blackbox solvers for comparing with many existing solvers.The authors demonstrate that dQP outperforms existing models across a range of benchmark problems.

### Strengths
The authors present a solid idea aimed at improving the efficiency of the backward process, making it especially effective for large-scale problems. 

They conducted numerous experiments and provided a theoretical proof to support their methods.

### Weaknesses
I believe the authors do not clearly address their contribution. If the goal of this paper is to propose a generic framework, then it should be clarified how dQP incorporates other solvers. On the other hand, if dQP is intended as a specific method of differentiate opt layer, it should be compared to various state-of-the-art approaches to demonstrate its advantages.

From my understanding, dQP seems to be a novel method for differentiating optimization problems. In Eq (10), it seems all the inequality constraints are tightened into equality constraints. How does this approach ensure the feasibility of the problem? Wouldn’t this compromise the feasibility, potentially resulting in the optimal solution of the modified optimization problem being different from the original one? If that's the case, this framework may not be applicable to predict-then-optimize problems because the optimal solution of the optimization problem has been altered.

However, if this is not the case and a black-box solver is used to solve the problem, then essentially a new forward process is designed for backward optimization but is not actually used, there will be two forward processes, which makes this step seem redundant. Additionally, existing solvers such as OptNet don’t seem to encounter this issue. If this is the main contribution of the paper, I think this it may not be sufficient.

Besides, I’m concerned about the practical performance of dQP (maybe a inexact gradient approach?) I would like to see experimental results comparing dQP with many other existing methods, especially from the aspect of computational efficiency. In the current manuscript, only graphical results are provided, such as in Figure 5, where for around 100 nodes, the results all fall within 1 second, showing minimal differences. Including more numerical results, such as the similarity of gradients computed by different solvers, running times, and differences in the optimal solutions of the optimization problems, and so on, could make the results more convincing.

One more issue is that, in the abstract (and line 355), the authors wrote, "Our implementation, which will be made publicly available, interfaces with an existing framework that supports over 15 state-of-the-art QP solvers." Maybe I think the implementation hasn’t been fully prepared before submission, so the paper may not be fully ready for publication, as it seems there is still some unfinished work.

### Questions
1. What are the benefits of dQP over OptNet? Is it more efficient? If so, why? Intuitively, it seems that compared to existing methods, the number of computation steps hasn’t decreased—rather, additional steps related to tolerance testing have been introduced. For example, line 5 in Algorithm 1 appears more complicated.
   
2. How the tolerance $\epsilon_J$ is set? Couldn’t this lead to infeasibility? I believe the authors should analyze the impact of this parameter in the experiments.
   
3. Regarding the duality gap, why does OptNet show a larger duality gap in Figure 4, even though the forward method is the same for both OptNet and dQP?
   
4. The Bi-Level Geometry Optimization in the last part of the experiment is not a common setup. I’m curious about how it can be formulated into KKT conditions. Could you provide more details on this?
   
5. How is Sparse QP defined in the paper, and what type of problems qualify as sparse? OptNet has a "lsqr" mode that significantly accelerates performance when handling sparse optimization problems. It seems the authors did not correctly utilize the different modes of the existing methods.

6. Besides, I think the authors should elaborate more on why dQP is particularly effective for large-scale problems. What mechanism specifically helps address this challenge?

If my question are well-addressed, I'll be happy to raise my score.

### Soundness
2

### Presentation
2

### Contribution
2
