# A Reoptimization Framework for Mixed Integer Linear Programming with Dynamic Parameters

- Decision: Reject
- Avg Score: 6.00
- Scores: 6, 8, 5, 5

## Abstract
Many real-world applications, such as logistics, routing, scheduling, and production planning, involve dynamic systems that require continuous updates to solutions for new Mixed Integer Linear Programming (MILP) problems. 
These environments often require rapid responses to slight changes in parameters, with time-critical demands for solutions. While reoptimization techniques have been explored for Linear Programming (LP) and specific MILP problems, their effectiveness in general MILP is limited. In this work, we propose a two-stage reoptimization framework for efficiently identifying high-quality feasible solutions. Specifically, we first utilize the historical solving process information to predict the high confidence solving space for modified MILPs to contain high-quality solutions. Based on the prediction results, we fix a part of variables to apply the prediction intervals and use the Thompson Sampling algorithm to determine the set of variables to fix by updating the Beta distributions based on solutions obtained from the solver. Extensive experiments across nine reoptimization datasets show that our VP-OR outperforms the state-of-the-art methods, achieving higher-quality feasible solutions under strict time limits and demonstrating faster convergence with smaller primal gaps in the early stages of solving.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a re-optimization framework, VP-OR, for Mixed Integer Linear Programming (MILP) problems with dynamic parameters. The authors address real-world MILP applications, such as logistics and scheduling, where updates to parameters require quick re-optimization without starting from scratch. VP-OR combines a Graph Neural Network (GNN) model, which predicts variable probabilities, with an iterative Thompson Sampling approach to refine solutions by updating variable ranges and fixing values iteratively. The approach is tested on nine datasets, demonstrating its ability to find high-quality solutions faster than existing methods, including SCIP and other machine learning-based re-optimization techniques.

### Strengths
Originality: The paper presents an innovative approach to re-optimization for MILP problems with dynamic parameters, an area with limited solutions, especially for general MILP cases. The proposed VP-OR framework creatively combines machine learning through a Graph Neural Network (GNN) with probabilistic methods using Thompson Sampling. 

Quality: The methodology is well-founded and executed. The use of GNNs for variable prediction is appropriately adapted to handle both binary and continuous variables in the MILP context, showing a solid understanding of the unique challenges in this domain. 

Clarity: The paper is well-structured and logically progresses from problem formulation to methodology and results. Each component of the VP-OR framework, including variable prediction, Thompson Sampling, and iterative refinement, is explained in detail, making it easy for readers to follow the complex methodology. 

Significance: VP-OR addresses a significant challenge in reoptimization for dynamic MILP problems, which are prevalent in real-world applications like logistics, production planning, and scheduling. By focusing on quick, high-quality reoptimization, the paper addresses a critical need for efficient solutions in time-sensitive scenarios.

### Weaknesses
Assumptions and Limitations in Variable Fixing: The VP-OR framework relies on predictions of feasible intervals for variables, which are used to fix values iteratively. However, if predictions are inaccurate, this approach can lead to suboptimal solutions or even infeasible ones. The paper does not sufficiently address the potential for error propagation when fixing variables based on potentially flawed predictions, especially in early iterations where the model has not yet converged to a stable solution. The reliance on a fixed percentage of variables being fixed in each iteration, without a dynamic adjustment based on prediction confidence or solution quality, could also lead to premature convergence or getting stuck in local optima.

Lack of Exploration on Convergence Guarantees: The paper does not provide formal convergence guarantees for the iterative refinement process, relying instead on empirical performance. While Thompson Sampling offers a probabilistic approach, the paper lacks a theoretical analysis of how the iterative fixing and re-optimization process converges to a high-quality solution, or any guarantees on the solution quality relative to the global optimum. The absence of a convergence analysis makes it difficult to assess the robustness and reliability of the method, particularly for complex or large-scale MILP problems.

Scalability Analysis: The paper does not provide a detailed scalability analysis regarding the computational complexity of VP-OR as problem sizes increase. While the authors mention the use of GNNs, which can be computationally expensive, the paper does not explore how the runtime of the VP-OR framework scales with the number of variables, constraints, or the density of the problem instances. This lack of analysis makes it difficult to assess the applicability of the method for very large-scale real-world problems.

### Questions
Are there theoretical or empirical convergence guarantees for VP-OR?

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
4

### Summary
This paper proposes a two-stage learning-based framework for reoptimization of mixed-integer linear programs (MILPs), that is for solving MILP instances which do not differ in structure, but only with respect to parameter values (cost  coefficients, variable bounds, constraint coefficients and constraint RHS values). In the first stage, using instance features as well as features obtained from solving a base instance to optimality, GNNs are used to predict variable values (for binary variables) or ranges for variable values (for integer and continuous variables). In the second stage, these predictions are used to fix a sampled subset of the variables, and using Thompson sampling, the sampling is improved to obtain better feasible solutions.

In a set of computational experiments with a public reoptimization benchmark data set, the approach is compared against other reoptimization approaches as well as against other state-of-the art learning-based and learning-augmented approaches for solving MILPs. For a strict time limit of 10 seconds, the new approach mostly outperforms the other approaches, and for longer computation times, it shows a good convergence, in particular compared to other learning-based approaches.

### Strengths
1. Probably the closest approach to the presented paper is the predict-and-search (PS) approach by Han et al. (2023), which also can be viewed as a two-stage approach. Compared to that approach, this paper introduces two advancements: First, while the PS approach only predicts binary variable values, this approach also predicts ranges for general integer variables and continuous variables. Second, while PS uses a neighborhood search in the second stage, this approach cleverly combines variable fixing with Thompson sampling.

2. I find that both ideas (predicting ranges and using Thompson sampling for selecting variables (and bounds) to fix) form original contributions that nicely complement each other in this work, but that will be also useful for future works going beyond this paper.

3. The computational results in general are fairly strong; they show that in the reoptimization setting under very strict time limits (10 seconds) the approach outperforms the baseline approaches.

3. As far as I can see, the baselines are mostly reasonably chosen (with one exception).

### Weaknesses
1. When used in a reoptimization setting, it seems natural to warm-start SCIP with the base solution; this is apparently not performed in the paper. Neglecting this natural approach lets me think that maybe the results are a bit too favorable for the proposed approach, in particular given that SCIP is often the strongest contender in the experiments. It is standard practice in reoptimization to leverage the previous solution as a starting point, and the absence of this in the baseline comparison makes it difficult to assess the true advantage of the proposed method.

2.  On page 9, the authors write  "We observe that VP-OR consistently outperforms other methods, achieving the fastest convergence across datasets and rapidly closing the primal gap." Looking at Fig. 2, this statement is a bit optimistic, since e.g. in the middle plot, VP-OR never closes the gap, and other approaches close the gap at some point.


3. From the paper (Han et al 2023), it becomes clear that the PS approach only deals with binary variables. It does not become clear in the paper how that approach is adapted in the experiment to deal with instances also involing general integer variables and continuous variables. The paper lacks a clear explanation of how the predict-and-search (PS) approach, which is designed for binary variables, is modified to handle general integer and continuous variables in the experimental setup. This raises concerns about the validity of the comparison, as the PS method might not be directly applicable without significant adaptation.

4. The authors often use the term "x%", e.g. when referring to the fraction of variables to be fixed. As x is also used for decision variables, a different symbol would be better.

5. Fig. 2 is much too small, in particular w.r.t. the font sizes of the legends and axis labels.

6. The text mentions appendix D3 which is empty.

### Questions
1. I find that using plain SCIP in the reoptimization setting is a bit unfair. In general, in a reoptimization settign it would be reasonable to provide the base solution as a warm-start solution. I suggest you to include that as an additional baseline as well and report the results.

2. How is the PS approach adapted to deal with non-binary decision variables for the experiments?

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
5

### Summary
In this manuscript, the authors introduce a two-stage reoptimization framework designed to efficiently identify high-quality feasible solutions. This framework comprises an initial stage of variable prediction followed by an iterative online refinement process. The proposed methodology has been rigorously evaluated through extensive experimentation across nine diverse datasets, demonstrating its superiority over state-of-the-art methods and open-source solvers. These comprehensive evaluations highlight the framework's effectiveness and robustness across various scenarios.

### Strengths
The paper presents an interesting idea. Replacing LNS with the Thompson Sampling algorithm is an intriguing and valuable exploration. This approach effectively leverages real-time solution information and promotes greater exploration through sampling, enhancing the overall search process.

1.	Interesting Observations in Section 4.1: The observations presented in Section 4.1 are particularly intriguing. The detailed discussion of the mispredicted variables provides strong support for the design of the subsequent iterative online refinement process.

2.	Comprehensive Evaluation Datasets and convincing results: The selection of experimental datasets is commendably broad, incorporating a diverse array of modifications and updates to the initial problem. This breadth lends a significant degree of credibility to the reported outcomes. However, to further solidify the robustness and reliability of the findings, it is suggested that future work include experiments with more complex instances and comparisons against additional state-of-the-art (SOTA) baselines.

### Weaknesses
1.	The novelty appears somewhat limited. Moreover, the manuscript lacks a clear summary of its contributions and does not sufficiently differentiate itself from existing literature.

  e.g., in Section 3, it seems that the solution prediction framework closely resembles the approach proposed in ND (also proposed a method for handling general integer variables). The authors should provide a detailed comparison highlighting the distinctions between their method and ND.

2.	The experimental comparisons presented in the manuscript are insufficient. Notably, some of the latest works in the field have not been included for comparison, such as [1], [2], and [3].

  [1] Ye H, Xu H, Wang H, et al. GNN&GBDT-guided fast optimizing framework for large-scale integer programming[C]//International Conference on Machine Learning. PMLR, 2023: 39864-39878.

  [2] Ye H, Xu H, Wang H. Light-MILPopt: Solving Large-scale Mixed Integer Linear Programs with Lightweight Optimizer and Small-scale Training Dataset[C]//The Twelfth International Conference on Learning Representations.

  [3] Nair V, Alizadeh M. Neural large neighborhood search[C]//Learning Meets Combinatorial Algorithms at NeurIPS2020. 2020.

3.	ND and PS appear to perform significantly worse in terms of generating feasible solutions (Table 3). Is this due to suboptimal hyperparameter settings, such as the appropriate radius in PS? Could the authors clarify why their proposed method succeeds in finding feasible solutions in more instances?
4.	The rationale behind choosing Thompson Sampling in the "Iterative Online Refinement" section is not clearly articulated. What is the necessity of introducing Thompson Sampling?

  a)	Could the authors include additional ablation studies comparing the application of Thompson Sampling against traditional LNS strategies (e.g., those presented in [1, 2, 3] and PS)? This would help illustrate the contributions in this phase.

  b)	Important algorithm descriptions, such as Algorithm 1, should be moved to the main body of the paper since they are crucial for understanding the implementation of Thompson Sampling.

### Questions
1.	In Section 3.1, the rationale for distinguishing between base instances and modified instances should be clarified. Is this a common approach in reoptimization problems? Additionally, it would be beneficial to discuss the impact of this setting on the final results.
2.	Can the relaxation mechanism ensure the identification of feasible solutions? It would be beneficial to include a discussion or proof regarding the feasibility guarantees provided by the relaxation approach.
3.	On line 79, the author states that "LNS does not actually decrease the problem’s variable size." This assertion might not be entirely accurate, as specific variants of LNS can indeed significantly reduce the variable size at each iteration by fixing some variables, as seen in reference [4]. A similar concern applies to Table 2. The author should clearly indicate which particular LNS method is being discussed and explain the distinction between this method and the process of variable fixation.

  [4] Wu, Yaoxin, et al. "Learning large neighborhood search policy for integer programming." Advances in Neural Information Processing Systems 34 (2021): 30075-30087.

4.	It appears that only five test cases were utilized for each dataset. Given this limited sample size, it raises concerns about whether the results can adequately substantiate the effectiveness of the proposed method.

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
4

### Summary
This paper provide a learning method for solving MILP instances that change slightly from previous solved instances (base instances). The paper leverage features from the solving process of the base instances to improve solving the modified instances. It uses a GNN to predict the solution values or the solution ranges. It also employs an iterative refinement process to refine the predictions by solving a multi-arm bandit problem. Evaluations are done on a sets of instances from the MIP 2023 computation competition. The runtime, solution quality are the main metrics for evaluation against other baselines.

### Strengths
1. The paper provides a novel ML method for MILP reoptimization. The innovation comes from leveraging the features from the solving process for the base instances and introducing the refinement methods for prediction confidence. 
2. The paper handles MILP with not just binary variables, but also those with general integer and continuous variables. Engineering details are included in the methods to handle the those variables. 
3. The paper is in general easy to follow.

### Weaknesses
1. My main criticism for the paper is that the instances used for evaluation are easy. It looks like the instances could be solved to close optimal in about 1 minute even with SCIP. The paper didn’t justify why easy instances are considered. In previous work, such as [1] (ND), [2] (PS) and [3] (a follow-up work of PS), much harder and larger instances are used in evaluation. 
2. I am not sure if the main competitor Re_Tuning is properly implemented. It performs the worst in many case but it is the main competitor of the proposed methods in this paper.
3. While I understand the definition of the problem well, the paper doesn’t motivate the problem of reoptimization well. For example, why is this problem important? What are the main difference from the settings of [1,2,3]? Why do we consider instances that are easy that can be solved by SCIP to close-optimal within 60-80 seconds?

### Questions
Please see the weaknessses.

### Soundness
3

### Presentation
3

### Contribution
2
