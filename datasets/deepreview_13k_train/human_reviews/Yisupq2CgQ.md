# Deep Progressive Search for Electromagnetic Structure Design Under Limited Evaluation Budgets

- Decision: Reject
- Scores: 3, 5, 6, 3

## Abstract
Electromagnetic structure (EMS) design aims to optimize a material distribution, e.g., metals over a printed circuit board, which is crucial for antenna and meta-material. This task, however, is inherently a highly non-convex problem with no explicit objective function, making it extremely challenging to solve. The most common approach to addressing this problem relies on evolutionary algorithms (e.g., Genetic Algorithm), where candidate structures are evaluated through electromagnetic simulation using specialized software. However, these methods struggle with inefficiency, especially when dealing with large structural design space and time-consuming simulations. 
To address this, we propose a Deep Progressive Search method called DPS, which leverages a Deep Neural Network (DNN) as a surrogate model to identify a satisfactory structure within a limited simulation budget. Specifically, we develop a tree-search-based design space control strategy that models the design space as a tree and incrementally refines it through node expansions, enabling adaptive exploration of more complex regions while leveraging insights from simpler subspaces. Moreover, we introduce a consistency-based sample selection strategy to balance exploration and exploitation. Experiments on two real-world engineering tasks, i.e., Dual-layer Frequency Selective Surface and High-gain Antenna show the effectiveness of the proposed DPS in terms of efficiency under limited evaluation budgets.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper tackles simulation-based electromagnetic structure design problems and proposes a novel optimization strategy. The proposed method is composed of the deep progressive search (DPS) to improve search efficiency, the tree-search-based design space control (TSS) to expand the search space, and the consistency-based sample selection strategy (CSS) to balance the exploration and exploitation. The experimental results on real-world problems show that the proposed method outperforms several naive baseline methods.

### Strengths
- A novel method for structure design problems is introduced. Specifically, the approach to expanding the search space seems to be novel.
- The proposed method outperforms several baseline methods in the experiments of two representative structure design problems, dual-layer frequency selective surface and high-gain antenna.

### Weaknesses
 - Using the deep neural networks as a surrogate model is a common approach. The reviewer thinks that the main novelty of the proposed method is TSS.
- The compared methods in the experiment are insufficient and weak. The concrete algorithms of the baselines are unclear. As there are a lot of surrogate-assisted evolutionary algorithms, state-of-the-art or well-known surrogate-assisted evolutionary algorithms should be selected as the baseline. Also, the Bayesian optimization approach should be considered as the baseline.
- The solution representations seem to be different between the proposed method (tree) and baseline methods, which might be unfair. It would be better to consider using a similar solution representation for GA and other baseline methods.
- The presentation of the proposed algorithm is not well-written. The key novel points of the proposed method should be clarified.

### Questions
1. The reviewer thinks Bayesian optimization can be a competitor for the proposed method because the design principle of the proposed is similar to Bayesian optimization. Could you comment on why the Bayesian optimization approach is not considered?
1. The proposed method has the hyperparameters, e.g., the maximum iterations $M$ and size $K$ of top-K. What is the impact of such hyperparameters on performance?


----- After authors' response -----

Thank you for the response, which helps to understand the contribution of the paper. I do not have further questions. I would maintain my score.

Although the proposed method seems promising, I would encourage adding extensive comparison with other baselines and improving the explanation of the proposed method.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
Overall, this paper presents a promising new approach in the field of electromagnetic structure design and validates its effectiveness through experiments. However, to further enhance the quality and impact of the paper, the authors may need to conduct more in-depth research and discussion on dataset description, computational resource analysis, model interpretability, comparative experiments, robustness testing, and the feasibility of practical application.

### Strengths
1. The paper introduces a novel Deep Progressive Search (DPS) method for electromagnetic structure (EMS) design under constrained evaluation budgets, which is an inherently challenging problem. The integration of tree search and sample selection strategies represents an innovative approach within the EMS design domain
2. The paper provides detailed descriptions of the Tree-Search-based Design Space Control (TSS) and Consistency-based Sample Selection (CSS) strategies, indicating a deep level of consideration in the algorithm design by the authors.
3. The authors test their method on two real-world engineering tasks: Dual-layer Frequency Selective Surface (DualFSS) and High-gain Antenna (HGA), demonstrating the practicality and broad applicability of their approach.

### Weaknesses
1. While the paper emphasizes optimization under limited evaluation budgets, specific data and comparative analysis on computational resources and time consumption might be lacking. It would be beneficial to include a breakdown of the time spent in the optimization stage versus the simulation validation stage, as these likely have very different resource demands. Furthermore, a comparison of the computational resources (e.g., GPU/CPU hours, memory usage) required by the DPS method against other optimization techniques would strengthen the analysis.
2. Although the DPS method is described in detail, the paper discusses the interpretability of the model less, especially the logic behind the design space management and sample selection strategies. It is unclear how the tree search progresses and how specific design choices are made at each node. The paper could benefit from a more detailed explanation of the decision-making process within the TSS and CSS components, including visualizations or case studies to illustrate the evolution of the design space and the rationale behind sample selection.
3. The paper could benefit from additional robustness tests to demonstrate the performance of the DPS method across different types, scales, and complexities of EMS design problems. While the method is tested on two real-world engineering tasks, it would be valuable to see results on a wider range of problems, including those with different objective functions, constraints, and design space characteristics. This would help to establish the generalizability of the proposed approach.

### Questions
1. Could the authors provide more specific data on the computational resources required for the DPS method compared to other approaches, including details on time and memory consumption? e.g. average GPU/CPU training hours per iteration for each method across different problem sizes.
2. How do the authors address the interpretability of context of the design space management and sample selection strategies? Can they elaborate on any techniques or methods used to understand the decision-making process? Could you provide visualizations or case studies demonstrating how the tree search progresses and how sample selection decisions are made at different stages of the optimization process for a particular example. This would give concrete insight into the model's decision-making.
3. Latest research works or other emerging techniques are needed comparing with the Dps method, that might offer superior performance or efficiency. And what are the findings of such comparisons? E.g. [1] Learning gflownets from partial episodes for improved convergence and stability
4. What is the sensitivity of the DPS method to the hyperparameter tuning process? E.g. sensitivity to particular key hyperparameters, like the maximum number of tree nodes or sample selection thresholds. Please provide reporting results across a range of hyperparameter values to demonstrate robustness.
5. Please double-check the table contents, e.g. Obj2 of DPS on ''Dual-layer Frequency Selective Surface" in Table 3 should not be in bold font.

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
This paper introduces **Deep Progressive Search (DPS)**, an efficient approach for electromagnetic structure (EMS) design under limited evaluation budgets. DPS combines a **Tree-Search-based Design Space Control (TSS)**, which progressively explores from simple to complex design regions, with **Consistency-Based Sample Selection (CSS)**, which prioritizes high-consistency samples to balance exploration and exploitation effectively. Applied to high-gain antenna (HGA) and dual-layer frequency selective surface (FSS) design, DPS achieves superior performance with fewer simulations than existing methods.

### Strengths
- The paper introduces an innovative DPS framework that integrates tree search and consistency-based sample selection for cost-effective EMS design.

- Comprehensive experiments and a detailed ablation study substantiate the effectiveness of each component in improving performance.

- The methodology is clearly explained, with well-structured presentations and precise formulations enhancing reader comprehension.

- The approach addresses the critical need for budget-efficient optimization in EMS design and offers applicability to other resource-constrained fields.

### Weaknesses
 - The paper lacks a justification for the choice of grid sizes in the experimental setup. This is a key design choice that influences both the resolution of design variations and computational efficiency. It would be valuable for the authors to provide their rationale for selecting these specific grid sizes. Additionally, a discussion on how different grid sizes may affect the method's performance and efficiency would enhance the clarity of these experimental decisions.

- To evaluate the method’s scalability, an ablation study on higher-dimensional optimization problems would be insightful. Conducting experiments with progressively larger grid sizes or more intricate design problem would help demonstrate the scalability of DPS in practical, high-dimensional settings. This would offer concrete evidence of the method’s robustness and scalability under varied problem complexities.

- Given the shared focus on design optimization, comparing DPS with GenCO within the context of inverse design problems would be valuable. GenCO also proposes an optimization framework and has been evaluated on the inverse photonic design problem, which closely aligns with DPS's focus. A comparative analysis could highlight DPS’s unique strengths and limitations, providing a clearer assessment of its performance relative to GenCO.

### Questions
- Given that the balance between exploration and exploitation should ideally adjust as the remaining budget decreases, how does the proposed DPS method handle this adjustment dynamically? Is there a mechanism that gradually prioritizes exploitation over exploration as the budget runs low, or does the balance remain fixed throughout the process?

- The abstract mentions "no explicit objective function," yet the experimental results seem to address a multi-objective optimization problem. Could you clarify the intended distinction between having no explicit objective function and conducting multi-objective optimization, and explain how DPS operates within this framework?

### Soundness
3

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
4

### Summary
This submission proposes a novel Deep Progressive Search (DPS) method to solve real-world EMS design problems. EMS design problems are formulated as expensive combinatorial optimization problems. 
The proposed DPS includes a Tree-Search-based Design Space Control (TSS) strategy and a Consistency-based Sample Selection (CSS) mechanism. TSS uses a Quadtree to model the design space efficiently, making it suitable for large-scale EMS tasks with limited simulation budget. In addition, a Quadtree-based search strategy and an important assignment method are proposed. CSS employs Kendall’s tau coefficient to measure the consistency of ordering results, enabling dynamic selection of candidate designs and reducing the interference caused by inaccurate model predictions.
Two real-world design problems are considered in this work and a set of experiments is conducted to show the performance of DPS.

### Strengths
* The motivation is clear. 
* The idea of using a Quadtree to represent EMS designs is novel. 
* Sufficient ablation studies. 
* Two real-world problems are considered.

### Weaknesses
1.The description of DPS is unclear and lacks details:
* On page 7, lines 324-331, the details of Depth-wise Importance Assignment are missing. Specifically, only Equation 7 is given without further explanations, making it difficult for readers to understand how this importance assignment is implemented. Please add more details about it, such as providing a step-by-step explanation of how this assignment is implemented, including any algorithms or pseudocode if applicable. It is unclear how the partition parameters are optimized, especially given that a parameter in one leaf node could also be a parameter in another. The manuscript should clarify if this optimization is independent for each node or if there is a global optimization process and provide the specific optimization technique used.
* When compared with the traditional design matrix, although the proposed Quadtree is more efficient in representing designs, the initial states of Quadtrees are less diverse than design matrices. When using traditional matrices, the initial design matrices can be complex designs, making all candidate designs have equal probabilities to be reached in a limited number of iterations. In comparison, the initial Quadtrees are definitely very simple designs (all states =1 or all states =0). Therefore, for a Quadtree, simple designs have significantly greater chances of being searched than complex designs, especially when maximum iteration $M$ is small. Please provide a discussion or analysis to show that complex designs are adequately explored within $M$ iterations. Alternatively, please provide guidelines on setting $M$ to ensure complex designs are adequately explored.
* On page 4, Algorithm 2, the tree search of the design space is implemented by either resampling a leaf node’s state or splitting a leaf node into four child nodes. But details are not provided in the corresponding paragraph (page 6, lines 317-323). What is the probability of resampling or splitting? It is also unclear what distribution these actions follow, and under what conditions each action is taken.
* On page7, it is unclear how Equation 8 can be used to measure the consistency of ordering results. Are both $x_i$ terms in the equation from time point $t$? More explanations should be provided, specifically explaining why the sign of the difference in predicted performance is multiplied between different samples. The meaning of these terms should be explained to help readers understand how Equation 8 works.
* Some experimental setups of DPS are not explained, such as maximum iteration $M$, $K$ in top-$K$ list, and total number of samples $M$ in CSS.

2.The experiments are not solid:
* The experimental setup does not specify the number of runs conducted. Are the results reported in Table 3 obtained from only one run (As no standard deviations are reported in Table 3)? Considering the stochastic processes in DPS and the comparison algorithms, the authors should conduct many runs (e.g. 20 or more) for experiments to ensure the reliability of the results. In addition, the authors should report mean performance and standard deviations in Table 3, and perform appropriate statistical tests to demonstrate that DPS significantly outperforms the comparison algorithms. The claim that DPS's performance is robust is unconvincing with only one run, as stochastic optimization results can vary significantly.
* Bayesian optimization (BO) methods have been widely used to solve expensive optimization problems; however, the authors did not compare BO in their experiments and did not explain why it was not considered. Please consider the following options: 1). Include a comparison with a recently proposed BO method in the experiments; 2). Provide a clear explanation for why BO was not considered, discussing any potential limitations or challenges in applying BO to this specific EMS problem. The authors should also clarify why surrogate-GA is a suitable comparison, given that it is an older method, and explain how it differs from more recent surrogate-assisted evolutionary algorithms (SAEAs).
* Some comparison methods are obsolete. For example, surrogate-GA was proposed decades ago [1]. Although the authors cited a paper published in 2020, the main contribution of this publication was the application of surrogate-GA to special design problems, rather than the development of a novel optimization method. I suggest considering some newly proposed optimization algorithms as comparison methods. 
* The comparison experiment in Table 3 is not fair. Some comparison methods, such as DPS and surrogate-GA, have their predictors updated during the optimization, while the predictors in other comparison methods, such as surrogate-assisted RS and invGrad, are trained on offline datasets. Consider running additional fair experiments where all predictors in comparison methods are updated during the optimization. 

3. On page 6, Equation 3, there is no explanation about $i$ and $j$ until line 290. Please consider revising the relevant paragraphs to avoid potential confusion.  
In addition, some denotations are not consistent throughout the submission. For example, $M$ is the maximum number of iterations on page 4, Algorithm 2, but $M$ is also the number of samples on page 7, Equation 9. $t$ is the time point on page 7, Equation 8, but $t$ is also used to represent frequency in GHz on page 15, line 795 (Appendix A).

4. On page 4, line 204, the optimization problem is formulated with a predictor. However, when the predictor is fitted with limited training data, it is very likely that the optimum found by the predictor is not optimal in simulations. As mentioned in line 210, further validation with high-fidelity simulations is required. Therefore, Equation 2 could be a step in the EMS, but it is inappropriate to formulate the entire EMS problem as Equation 2.

5. Some minor issues:
* In Table 3, the agg obj results of cGAN and cVAE for High-Gain Antenna are incorrect. They should be minimum instead of maximum.
* There are some typos, such as:
    1) On page 10, line 492, 'ESS' should be ‘CSS’.
    2) On page 15, line 792, 'minimize the maximum' should be 'minimize the minimum’.
* Additionally, there are some grammatical errors, such as 'a expanded' should be 'an expanded.'

### Questions
* Why is ResNet50 employed as a predictor in the experiments? Is there any specific reason for this choice, or was it selected arbitrarily?
* Why are there four subfigures in the lower row of Fig. 4, instead of combining them into a single figure with the same y-axis scale? I believe that drawing four lines in a single figure would be clearer and easier to observe than presenting them as four separate subfigures.
* In the configuration of surrogate-assisted RS, $K$ = 10 but the simulation budget is 1000?

### Soundness
1

### Presentation
2

### Contribution
2
