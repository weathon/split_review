# FSEO: A Few-Shot Evolutionary Optimization Framework for Expensive Multi-Objective Optimization and Constrained Optimization

- Decision: Reject
- Scores: 3, 5, 6, 5

## Abstract
Meta-learning has been demonstrated to be useful to improve the sampling efficiency of Bayesian optimization (BO) and surrogate-assisted evolutionary algorithms (SAEAs) when solving expensive optimization problems (EOPs). However, existing studies focuses on only single-objective optimization, leaving other expensive optimization scenarios unconsidered. We propose a generalized few-shot evolutionary optimization (FSEO) framework and focus on its performance on two common expensive optimization scenarios: multi-objective EOPs (EMOPs) and constrained EOPs (ECOPs). We develop a novel meta-learning modeling approach to train surrogates for our FSEO framework, an accuracy-based update strategy is designed to adapt surrogates during the optimization process. The surrogates in FSEO framework combines neural network with Gaussian Processes (GPs), their network parameters and some parameters of GPs 
represent useful experience and are meta-learned across related optimization tasks, the remaining GPs parameters are task-specific parameters that represent unique features of the target task. We demonstrate that our FSEO framework is able to improve sampling efficiency on both EMOP and ECOP. Empirical conclusions are made to guide the application of our FSEO framework.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper propose a zero-shot evolutionary framework for expensive MOO and constrained optimization.

### Strengths
The studied problems such as MOO, MOEA, MOBO are very hot topics.

### Weaknesses
1. **Title**: The title feels overly lengthy and general. Consider refining it to be more concise and specific to the key contribution of the paper.

2. **Section 4.1 - Proposed Framework**: The framework in Section 4.1 appears somewhat ad hoc and lacks a rigorous mathematical foundation. It currently seems more heuristic in nature. Adding formal mathematical justification could strengthen this section.

3. **Suitability for Publication Venues**: The proposed method may be better suited for evolutionary computation venues like *IEEE Transactions on Evolutionary Computation (TEVC)* or *Genetic and Evolutionary Computation Conference (GECCO)*, given its approach and focus.

4. **Equation Formatting**: Equations 2 and 3 take up an unnecessary amount of space. Additionally, consider using `\exp` instead of `exp` to improve the visual consistency of the formulation.

5. **Algorithm 2 - Meta Learning**: The meta-learning approach in Algorithm 2 appears somewhat unconvincing in its current form. It could benefit from a clearer rationale and possibly a refinement of the underlying methodology.

6. **Language and Style**: The paper contains several instances of non-academic language. Tools like Grammarly or ChatGPT could help refine the writing style to meet academic standards.

7. **Zero-Shot Optimization Approach**: The zero-shot approach may not be ideal for handling optimization tasks. For example, if the first case optimizes \( y = x \) and the second optimizes \( y = -x \), both within the domain \([-1, 1]\), it’s unclear how learning from the first case would inform or benefit the second. Consider revisiting this approach.

### Questions
See weakness.

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
4

### Summary
This work investigates a meta-learning based few-shot evolutionary optimization (FSEO) approach to improve the performance of surrogate-assisted evolutionary algorithms (SAEA) with a special focus on multi-objective and constrained optimization. It proposes a meta deep kernel learning (MDKL) model as the surrogate model, which combines neural network with Gaussian process. Part of the MDKL model parameters are mete-learned across different tasks, while some parameters (part of GP) are fine-tuned for each specific task. Experimental results show the proposed method can achieve good performance on synthetic and real-world optimization problems.

### Strengths
+ This paper is well written and easy to follow.

+ The studied meta-learning based approach is important for real-world expensive optimization.

+ The proposed method achieves good performance on some synthetic and real-world optimization problems.

### Weaknesses
 **1. Difference between BO and SAEA**

This work claims that the existing works on few-shot optimization are mainly meta-learning based Bayesian optimization (BO) approaches, while this paper focuses on the surrogate-assisted evolutionary algorithm (SAEA). However, the difference between BO and SAEA is not clear to the reader. To my understanding, BO is a general framework for model-based optimization, of which SAEA is a subset that uses an evolutionary algorithm as the search method. For example, the covariance matrix adaptation evolution strategy (CMA-ES) is a popular search method for optimizing the acquisition function in BO.

A detailed explanation of the difference between BO and SAEA is needed.  

**2. Novelty and Connection to Related Work**

It seems that meta-learning based Bayesian optimization is already a popular research topic, and different methods have already been proposed for multi-objective optimization [1,2]. A detailed discussion and comparison with these related works are needed. 

In addition, in the related work section, this work claims "no further adaptations are made to these surrogates during optimization since they are not originally designed for optimization" for some early work on few-shot Bayesian optimization [3]. However, the surrogate model adaption is a reasonable approach for meta-learning based Bayesian optimization. Does "no further adaptation" still apply to the current meta-learning based BO method?  

[1] Speeding Up Multi-Objective Hyperparameter Optimization by Task Similarity-Based Meta-Learning for the Tree-Structured Parzen Estimator,  IJCAI 2023.

[2] BOFormer: Learning to Solve Multi-Objective Bayesian Optimization via Non-Markovian RL, AutoRL@ICML 2024.

[3] Few-shot Bayesian optimization with deep kernel surrogates, ICLR 2021.

**3. Proposed Framework**

- It seems that the proposed few-shot optimization framework is a standard combination of meta-learning and model-based optimization. Compared with existing work, what are the novelty and advantages/disadvantages of the proposed framework and the proposed methods for each step? A detailed ablation study for each algorithm step could also be very helpful for readers to truly understand the contribution of this work.  

- This work claims it "focuses on its performance on two common expensive optimization scenarios: multi-objective EOPs (EMOPs) and constrained EOPs (ECOPs)". However, no multi-objective or constrained optimization component has been shown and discussed in the proposed framework. In the experiment section, a popular decomposition-based method (MOEA/D) is used to handle the multi-objective optimization problem. However, it seems that MOEA/D can also be used with other meta-learning based approaches for multi-objective optimization. It is unclear why the proposed framework in this work is more suitable for multi-objective optimization.

**4. Expriments**

- For multi-objective optimization, the proposed framework is only tested on one synthetic test benchmark (DTLZ). More experimental results on real-world multi-objective optimization problems are needed.

- For constrained optimization, one real-world case study is provided, but the details of how the proposed framework deals with the constraints and its novelty/advantages over existing work are missing.

- The proposed framework is only compared with other SAEAs, and the comparison with BO methods is missing.

- Comparison with other meta-learning methods is missing.

### Questions
See weaknesses.

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
3

### Summary
The paper presents a novel Few-Shot Evolutionary Optimization (FSEO) framework that integrates meta-learning with surrogate-assisted evolutionary algorithms to enhance optimization efficiency in expensive multi-objective and constrained optimization scenarios. The approach is innovative and well-motivated, particularly in addressing the gap in existing research, which primarily focuses on single-objective optimization scenarios. Here are some minor suggestions:
1、	The explanation of the meta-learning process and its integration with Gaussian Processes could be further elaborated. Specific details on how the network parameters are adapted during optimization would enhance understanding of the efficacy and mechanics of the proposed method.
2、	While the experiments demonstrate improvements in sampling efficiency, the selection of benchmarks and comparison against state-of-the-art methods need to consider the latest related algorithms.
3、	The discussion section briefly mentions the limitations related to the mathematical definition of related tasks and the framework’s applicability only to regression-based SAEAs. Expanding on these points, possibly with suggestions for future research directions, would provide a more balanced view and potential pathways for advancing the framework.

### Strengths
The paper presents a novel Few-Shot Evolutionary Optimization (FSEO) framework that integrates meta-learning with surrogate-assisted evolutionary algorithms to enhance optimization efficiency in expensive multi-objective and constrained optimization scenarios. The approach is innovative and well-motivated, particularly in addressing the gap in existing research, which primarily focuses on single-objective optimization scenarios.

### Weaknesses
1）The explanation of the meta-learning process and its integration with Gaussian Processes could be further elaborated. Specific details on how the network parameters are adapted during optimization would enhance understanding of the efficacy and mechanics of the proposed method.
2）While the experiments demonstrate improvements in sampling efficiency, the selection of benchmarks and comparison against state-of-the-art methods need to consider the latest related algorithms.
3）The discussion section briefly mentions the limitations related to the mathematical definition of related tasks and the framework’s applicability only to regression-based SAEAs. Expanding on these points, possibly with suggestions for future research directions, would provide a more balanced view and potential pathways for advancing the framework.

### Questions
1）The explanation of the meta-learning process and its integration with Gaussian Processes could be further elaborated. Specific details on how the network parameters are adapted during optimization would enhance understanding of the efficacy and mechanics of the proposed method.
2）While the experiments demonstrate improvements in sampling efficiency, the selection of benchmarks and comparison against state-of-the-art methods need to consider the latest related algorithms.
3）The discussion section briefly mentions the limitations related to the mathematical definition of related tasks and the framework’s applicability only to regression-based SAEAs. Expanding on these points, possibly with suggestions for future research directions, would provide a more balanced view and potential pathways for advancing the framework.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Existing meta-learning-based surrogate models are primarily designed for single-objective expensive optimization problems. Unlike existing approaches, this paper focuses on multi-objective expensive optimization problems (EMOPs) and constrained expensive optimization problems (ECOPs). A novel meta-learning modeling approach is developed to train surrogate models within the few-shot evolutionary optimization (FSEO) framework, along with an accuracy-based update strategy for adjusting the surrogate model during optimization. Experimental results demonstrate the effectiveness of the proposed algorithm.

### Strengths
1. This paper innovatively applies meta-learning to expensive multi-objective optimization problems by designing an accuracy-based update strategy to adapt surrogates. This work has some academic value.
2. The experiments in this paper are sufficiently comprehensive, demonstrating the effectiveness of the proposed method from multiple perspectives.

### Weaknesses
1. The reasons why the paper considers addressing EMOPs and ECOPs are unclear. The paper does not adequately justify why these problem classes are more important or challenging than other expensive optimization problems, such as those with high dimensionality or non-convexity. A more detailed explanation of the specific challenges posed by EMOPs and ECOPs, and why existing meta-learning approaches are insufficient for them, is needed.
2. A key challenge in ECOPs is finding feasible solutions. This work does not incorporate constraint-handling techniques, and although it finds feasible solutions for a real-world problem with four constraints, the comparison algorithms do so as well, suggesting that the ECOP addressed here is relatively simple. The paper fails to demonstrate that the proposed method offers any advantage in constraint satisfaction over existing methods. The fact that the chosen ECOP is easily solved by other methods raises concerns about the general applicability of the proposed approach. Additionally, the title and abstract highlight ECOPs handling as a key focus, which is somewhat misleading.


### Questions
1. The paper mentions that meta-learning has already been applied to single-objective expensive optimization tasks. What are the similarities and differences between the proposed method and existing methods?
2. How does the proposed algorithm ensure that the solutions found for ECOPs are feasible?
3. The title mentions that the proposed algorithm can address ECOPs, but only a single example was tested, which is not convincing. Therefore, the title may not be appropriate, or more experiments on ECOPs should be included.
4. This paper is only tested on the DTLZ benchmark suite. The effectiveness of the algorithm should be validated on more benchmark suites.

### Soundness
2

### Presentation
3

### Contribution
2
