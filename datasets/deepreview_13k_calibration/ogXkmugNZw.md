# Conflict-Averse Gradient Aggregation for Constrained Multi-Objective Reinforcement Learning

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 8, 6, 5

## Abstract
In many real-world applications, a reinforcement learning (RL) agent should consider multiple objectives and adhere to safety guidelines.
To address these considerations, we propose a constrained multi-objective RL algorithm named \textit{\textbf{Co}nstrained \textbf{M}ulti-\textbf{O}bjective \textbf{G}radient \textbf{A}ggregator (CoMOGA)}. 
In the field of multi-objective optimization, managing conflicts between the gradients of the multiple objectives is crucial to prevent policies from converging to local optima.
It is also essential to efficiently handle safety constraints for stable training and constraint satisfaction.
We address these challenges straightforwardly by treating the maximization of multiple objectives as a constrained optimization problem (COP), where the constraints are defined to improve the original objectives.
Existing safety constraints are then integrated into the COP, and the policy is updated using a linear approximation, which ensures the avoidance of gradient conflicts.
Despite its simplicity, CoMOGA guarantees optimal convergence in tabular settings.
Through various experiments, we have confirmed that preventing gradient conflicts is critical, and the proposed method achieves constraint satisfaction across all tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents an algorithm for multi objective reinforcement learning under constraints. The authors first identified that 
maximizing a specific return within the trust region is equivalent to minimizing $||\Delta \theta||^2_H$$ under a constraint that the 
return increases (if the solution exists). Therefore, the multi objective RL under constraints can be formulated as a problem that 
minimizes the induced norm of $\Delta \theta$ under a bunch of constraints that correspond to the multiple task returns and 
constraints. By using a first-order approximation of the constraints, the problem reduces to a quadratic programming problem. To avoid 
the violation of the constraint due to the inaccurate linear approximation, the authors propose to remove the return constraints once 
the violation happens. 
 
The above can be generalized to multiple objectives with preferences, and then to learn a universal policy (i.e., a policy that 
is conditioned on any given preference $w \in \R^N$), the authors propose to learn a policy that minimize the expected KL divergence 
between the learned policy conditioned on a specific preference and the updated policy that solves the above quadratic programming. In 
other word, it amortizes the optimization into a learned conditional policy. 
 
The authors conduct experiments on both synthetic toy and constrained RL problems in simulation, demonstrating that their method 
results in superior performance (in terms of optimizing the objective and satisfying constraints) compared against prior methods. The 
authors also provide a convergence guarantee for the proposed method.

### Strengths
1. The problem of interest has broad application. 
 
2. The proposed method is straightforward yet well motivated. Specifically, the transformation of objective to constraint is 
convenient. 
 
3. The presentation is clear, and the figures illustrate the main ideas well. 
 
4. The empirical results demonstrate that the proposed method consistently outperforms existing methods.

### Weaknesses
One main weakness is the computational efficiency of the proposed method, which might hinder the practical usage of the proposed method. First it requires computing/storing gradients to constraints/rewards, which can be quite large if N and M are large. Specifically, for each policy update, the method needs to compute the gradients of all the objectives and constraints with respect to the policy parameters, which scales linearly with the number of objectives and constraints. This could become a significant bottleneck in high-dimensional or complex environments where the number of objectives and constraints is large. Second, it requires estimating terms like $x^\top H x$ where x is the fisher information matrix, while this does not in general require computing $H$ explicitly, it still requires computing the inner product like $x^\top \nabla \log \pi$ (which might need extra space). The authors did not elaborate on this aspect, and there is no time complexity evaluation in the experiments or analysis sections. The computational cost of estimating the Fisher information matrix, even with approximations, can be substantial, especially when the policy network has a large number of parameters. The paper lacks a detailed analysis of how the computational cost scales with the size of the policy network and the number of samples used for estimation. Furthermore, the memory requirements for storing the gradients and intermediate computations are not discussed, which could be a practical concern for large-scale problems.

### Questions
1. I think there is a gap from (3) to (4) where the authors generalize to multiple objectives. In the multiobjective case (without 
constraints), are (2) and (3) equivalent only when a solution exists?  If so, is it the case that the norm constraint can always  
be satisfied, while the monotonic improvement constraints are not? 
 
2. The scaling of the gradient essentially adds the norm constraint back, but if this is the case, why not start with that 
constraint and use the form (2)? Like max_d d^\top g_i, s.t., b^\top d + J < d_k, ||d||_H \leq \epsilon? Is it because this form is not 
easily solvable due to the norm constraint (difficult to estimate H^{1/2})? If so, the authors could explicitly mention this. 
 
3. The authors claim that using (6) can help correct the policy when it avoids any constraint due to solving (5) which uses linear 
approximation. But isn't (6) also using linear approximation, and the solution to (5) should also satisfy constraints in (6) if there 
exists any feasible solution? Can the authors elaborate on what this means exactly? 
 
4. The first sentence of the abstract asserts that an RL agent needs to consider multiple objectives.  That's not necessarily the  
case - the reward hypothesis states that an agent's objective can always be summarized with a single scalar reward function.  How  
would you motivate this paper to someone who fundamentally disagrees that an agent needs to consider multiple objectives separately 
(as opposed to aggregating them to explicitly encode their tradeoffs)?

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
3

### Summary
This paper presents CoMOGA, an algorithm designed to optimize multiple objectives while satisfying constraints. CoMOGA converts objectives into constraints and combines the gradients from both objectives and constraints. Theoretical analysis provided in the paper demonstrates that CoMOGA can achieve a local Pareto optimal policy. Empirical tests show that CoMOGA surpasses competing methods in achieving better coverage of the constrained-Pareto front.

### Strengths
- The problem addressed is highly relevant and has practical real-world applications.
- The paper is well-written and easy to understand.
- The experiments are thorough, and the evaluation metrics are clearly defined and articulated.

### Weaknesses
 - The section on gradient aggregation could be improved by including comparisons with similar MORL methods like CAGrad and PCGrad.



### Questions
- Why does CoMOGA perform significantly better than the combination of CAGrad and Lagrangian in Section 6.5? Could the authors expand on this?
- Why is the combination of CAGrad and Lagrangian treated as an ablation study rather than a baseline?
- How are preferences sampled in Line 328, for example, are they uniformly sampled? How does this affect the distribution of results?
- Are the critics trained using the same targets, such as Retrace, across all methods in the experiments?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents the Constrained Multi-Objective Gradient Aggregator (CoMOGA) algorithm for constrained multi-objective reinforcement learning (CMORL). It transforms the CMORL problem into a constrained optimization framework and addresses the optimization objective within a local region, using constraints designed to enhance the original objectives in proportion to preference values. The authors also provide a convergence guarantee in the tabular setting. Experimental results across several environments demonstrate that CoMOGA achieves constraint satisfaction.

### Strengths
## Originality and Significance
1) This paper presents a constrained multi-objective optimization algorithm, CoMOGA, which transforms objectives into constraints. The idea appears to be novel.
2) Multi-objective tasks and constraint optimization are critical issues in reinforcement learning, significantly enhancing the safety of reinforcement learning and its applicability in real-world scenarios.

## Quality and Clarity
1) The paper is well-written and easy to read.
2) This paper includes both theoretical analysis and detailed empirical results.
3) Multiple figures are provided, which are helpful in understanding the main concepts presented in the paper.

### Weaknesses
## Framework
1) The core idea of this paper is to avoid gradient conflicts by converting multi-objectives into constraint terms. However, during the optimization process, due to factors such as the linear approximation of the objectives and bias in the value function estimation, it is difficult to avoid constraint violations by the constraint terms of the objective, thus causing gradient conflicts. This may undermine the authors' core contribution. Specifically, the linear approximation within a local region, while simplifying the optimization, might not accurately capture the true curvature of the objective functions, leading to inaccurate constraint boundaries and potential constraint violations. Furthermore, the bias in value function estimation, a common issue in reinforcement learning, can exacerbate this problem by providing noisy gradients that push the policy towards suboptimal regions, making it difficult to maintain constraint satisfaction.
2) Transforming multiple objectives into constraint terms can complicate the constraint boundaries, thereby increasing the difficulty of finding an optimal policy that satisfies these constraints. The original multi-objective problem might have well-defined trade-offs, but converting objectives to constraints can create complex, non-convex feasible regions. This transformation could introduce sharp corners or discontinuities in the constraint space, making it harder for gradient-based methods to navigate and converge to a satisfactory solution. The increased complexity of the constraint boundaries may also lead to the algorithm getting stuck in local optima, hindering the search for a globally optimal policy.
3) It is not clear whether this transformation yields positive gains in computational complexity and convergence rate. While the authors frame the transformation as a way to simplify the optimization, the added complexity of solving a constrained optimization problem at each step might negate any potential gains. The computational overhead of projecting the policy back into the feasible region after each update, as well as the need to solve a quadratic program, could make the algorithm computationally expensive, especially for high-dimensional problems. Furthermore, it is unclear if the convergence rate of the proposed method is better than existing multi-objective reinforcement learning algorithms, and this needs to be analyzed in detail.

## Experiments
1) There is a lack of sensitivity analysis concerning hyperparameters. The paper introduces new hyperparameters such as the local region size and the number of preference samples, but there is no discussion on how these parameters affect the performance of the algorithm. Without a sensitivity analysis, it is difficult to determine the optimal hyperparameter settings for different environments, and the reported results might be specific to the chosen settings. This lack of analysis limits the practical applicability of the proposed method, as users would need to perform extensive hyperparameter tuning for each new task.
2) The fairness of the ablation experiments is questionable. The constraint optimization algorithm employed for the CAGrad algorithm in the ablation experiments is the Lagrangian method, which is inconsistent with the optimization algorithm used in CoMOGA. This inconsistency makes it difficult to isolate the effect of the core components of CoMOGA. The performance difference between CoMOGA and CAGrad could be due to the different optimization algorithms rather than the core ideas of the proposed method. A fair ablation study should compare CoMOGA with a version of CAGrad that uses the same optimization method, or at least provide a justification for the use of different methods.

### Questions
1) Can the authors analyze the computational complexity and the rate of convergence of the algorithm after converting multiple objectives into constraints?

2) Does the algorithm converge in continuous space?

### Soundness
2

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
3

### Summary
This paper introduces a novel multi-objective reinforcement learning (RL) approach that incorporates safety constraints. The authors present a gradient conflict management technique, which formulates multi-objective RL as a constrained optimization problem. This formulation effectively prevents policies from getting trapped in local optima, particularly in tabular settings. Additionally, it enables the seamless integration of safety constraints and facilitates an efficient policy update mechanism.

### Strengths
1.***Theoretical Contribution:***

The paper presents an interesting theoretical contribution, providing a comprehensive convergence analysis.

2.***Experimental Coverage:***

The study includes a wide range of experiments within the MORL domain, offering an extensive evaluation of the proposed method.

### Weaknesses
1.***Constrained Multi-Objective RL as a Constrained Optimization Problem:***

The authors propose addressing constrained multi-objective reinforcement learning (CMORL) by formulating it as a constrained optimization problem (COP). While COP offers robust theoretical guarantees for convergence, the paper provides limited insights into its practical implementation, specifically regarding the transformation of the theoretical framework into a concrete algorithm. The paper lacks details on how the gradients of the objective and constraint functions are computed in practice, and how the inverse Fisher information matrix is approximated, which are crucial for the method's real-world application and reproducibility.

2.***Inconsistencies in Hypervolume (HV) Scale and Reporting:***
Figure 8 presents hypervolume (HV) results on a significantly smaller scale compared to previous work. For example, in PD-MORL, HV values are reported across training steps up to 10 $e^6$, while in this study, the results are shown only from 1$e^6$ up to 3$e^6$ steps, Which may not reach the convergency. Furthermore, the lack of clarity on the normalization process for the objectives before computing the hypervolume makes it difficult to compare the results with other studies, and raises concerns about the validity of the comparison.

3.***Different unit to benchmark in HV:***
 With PD-MORL reporting HV values in the unit of 1$e^6$ , whereas this paper uses a unit of 0.1 for HV. These inconsistencies create confusion and lead to the perception that PD-MORL performs worse in this comparison than reported in the original study.

4.***Practical Implementation Challenge: High Dimensionality and Computational Expense:***
In the theoretical work, Equation (9) utilizes the inverse Fisher information matrix over the policy parameter theta, potentially resulting in high dimensionality and significant computational expense in practical applications. The paper does not adequately address how the method handles the computational burden associated with inverting the Fisher information matrix, especially in high-dimensional policy spaces, which is a critical aspect for the scalability of the proposed approach.

### Questions
1. **Limited Practical Implementation Details in Constrained Optimization Problem (COP)**: The authors propose solving constrained multi-objective reinforcement learning (CMORL) as a constrained optimization problem (COP), which theoretically offers strong convergence guarantees. However, the paper lacks detailed insights into the practical implementation of this approach. In contrast, methods like TRPO provide clear derivations of practical algorithms from theoretical foundations, taking into account finite sample sizes and arbitrary parameterizations in deep reinforcement learning. Can you include a similarly detailed derivation to bridge the theoretical framework with practical implementation?

2. **Inclusion of Pareto-Dominated Points in Figure 7**: In Figure 7, numerous points are shown that are Pareto-dominated by others. This raises questions about the relevance of including these dominated points, as they do not contribute to optimal trade-offs and may complicate the interpretation of the results. What is the rationale behind the inclusion of these Pareto-dominated points, and how do they add value to the analysis presented in this figure?

3. **Inconsistencies in Hypervolume (HV) Reporting in Figure 8**: In Section 6.4, Why do the results for Hopper and HalfCheetah in Figure 8 differ significantly from the original results reported in PD-MORL?

4.***Practical Implementation Challenge: High Dimensionality and Computational Expense:***
In the theoretical work, Equation (9) utilizes the inverse Fisher information matrix over the policy parameter theta, potentially resulting in high dimensionality and significant computational expense in practical applications. How does CoMOGA handle this challenge in its practical implementation?

### Soundness
3

### Presentation
2

### Contribution
2
