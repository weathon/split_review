# Constrained Multi-Objective Optimization

- Decision: Reject
- Scores: 3, 3, 3, 1

## Abstract
There is more and more attention on constrained multi-objective optimization (CMOO) problems, however, most of them are based on gradient-free methods. This paper proposes a constraint gradient-based algorithm for multi-objective optimization (MOO) problems based on multi-gradient descent algorithms. We first establish a framework for the CMOO problem. Then, we provide a Moreau envelope-based Lagrange Multiplier (MLM-CMOO) algorithm to solve the formulated CMOO problem, and the convergence analysis shows that the proposed algorithm convergence to Pareto stationary solutions with a rate of $\mathcal{O}(\frac{1}{\sqrt{T}})$. Finally, the MLM-CMOO algorithm is tested on several CMOO problems and has shown superior results compared to some chosen state-of-the-art designs.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This work proposes a gradient-based optimization algorithm, MLM-CMOO, to solve constrained multi-objective optimization (CMOO) problems. The authors conduct a convergence analysis and several experiments to demonstrate the effectiveness of the proposed MLM-CMOO algorithm.

### Strengths
The authors conduct a convergence analysis for MLM-CMOO and provide several theoretical proofs in the supplementary materials.

### Weaknesses
1. The submission focuses on constrained multi-objective optimization (CMOO), however, no CMOO algorithms are compared in the experiments. The authors should compare several CMOO algorithms in their experiments. For example, the authors reviewed some gradient-free CMOO algorithms in the related work section, which could be included in the comparisons.
2. In Section 2, only gradient-based MOO and gradient-free CMOO are discussed in the related work. The authors should also review some constraint handling techniques (CHTs).
3. The experiments in Section 5 are all multi-task learning (MTL) problems. The authors should add explanations to clarify how these MTL problems are used to evaluate the performance of CMOO algorithms, including what the constraints are in these MTL problems.
4. The presentation of experimental results lacks detail. The authors should provide detailed explanations of Table 1 and Figure 1 to help readers understand experimental results. For example, the caption for Figure 1 is too brief, the authors should clarify the meaning of each subfigure in Figure 1.
5. The symbols in the submission are inconsistent. For instance, the $i^{th}$ objective function is denoted as $f_i(x)$ or $f^i(x)$.

### Questions
In line 132, why do the authors state that the goal of MOO is to find a Pareto optimal solution? In fact, for many real-world MOO applications, the goal is to find a set of well-distributed Pareto optimal solutions.

### Soundness
1

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes a gradient-based method for constrained multi-objective optimization, named MLM-CMOO. It is proved that the proposed method guarantees a convergence rate of $O(1/\sqrt{T})$. An empirical study demonstrates the effectiveness of the proposed method.

### Strengths
1. This paper is well-written and easy to follow.
2. The technical and mathematical details are clearly presented. The proofs are well-organized and seem correct.
3. This paper is novel and original, since constrained gradient-based MOO has not been well-studied.

### Weaknesses
There are a number of weaknesses.

1. Why do you consider gradient based approaches only in this paper to tackle multi-objective optimisation tasks? Under what conditions, gradient based methods are good? It is not clear why the authors limit their scope to gradient-based methods, especially given the wide range of evolutionary algorithms and other techniques available for multi-objective optimization (MOO). The paper should discuss the limitations of gradient-based methods, such as their potential to get stuck in local optima, sensitivity to initial conditions, and the requirement for differentiable objective functions. A more thorough justification for focusing solely on gradient-based methods is needed.

2. The number of objectives in all the datasets should be explicitly identified and described clearly. The current description lacks the necessary detail regarding the dimensionality of the objective space for each dataset used in the experiments. This information is crucial for understanding the complexity of the optimization problem and the relevance of the results.

3. In your experiments, you compared the proposed method with NSGA-II and PSL. Why didn't you consider SPEA2 and MOEA/D? The choice of baseline algorithms is limited. The paper should justify why SPEA2 and MOEA/D, which are well-established and widely used MOO algorithms, were not included in the comparison. This omission raises concerns about the comprehensiveness of the experimental evaluation.

4. The results are far from complete --- only Table 1 and Figure 1 are presented. Many interesting results such as the Pareto-fronts for each dataset, the hyper-volume or IGD comparisons are missing. It is not clear to me the comparison between those algorithms are fair. Only providing the loss and time values is not sufficient to understand the effectiveness of the proposed method. The lack of standard MOO performance metrics, such as hypervolume, generational distance, or inverted generational distance, makes it difficult to assess the quality of the obtained Pareto fronts and to compare the proposed method with the baselines fairly. Visualizations of the Pareto fronts for each dataset are also essential for a thorough evaluation.

### Questions
Please see "Weaknesses".

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper describes a constrained multi-objective optimisation approach. Instead of using ordinary gradient based algorithms, this paper proposes a constrained gradient based one based on multiple gradient descent algorithms. The new approach seems to have a good convergence to Pareto solutions, and produced good results.

### Strengths
MOO is a good topic and approach to processing multiple potentially conflicting objectives. This paper develops a new method toward this direction, which is good.

The paper also provides an convergence analysis, which seems to be theoretically demonstrating the the proposed algorithm can be converged.

### Weaknesses
There are a number of weaknesses. 

1. Why do you consider gradient based approaches only in this paper to tackle multi-objective optimisation tasks? Under what conditions, gradient based methods are good? 

2. The number of objectives in all the datasets should be explicitly identified and described clearly. 

3. In your experiments, you compared the proposed method with NSGA-II and PSL. Why didn't you consider SPEA2 and MOEA/D?

4. The results are far from complete --- only Table 1 and Figure 1 are presented. Many interesting results such as the Pareto-fronts for each dataset, the hyper-volume or IGD comparisons are missing. It is not clear to me the comparison between those algorithms are fair. Only providing the loss and time values is not sufficient to understand the effectiveness of the proposed method.

### Questions
1. How many independent runs have you carried our for each of the comparison algorithm? All those methods including those gradient based methods and NSGA-II are stochastic ones, different runs with the same parameter setup will produce different results. 

2. Have you considered other performance evaluation measures, such as HV and IGD, comparison of Pareto-fronts?

3. Ablation studies: your proposed method has several components. Which one plays more important roles than others? Are all of them useful? 

It seems that you submitted this paper in a hurry without completing it.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
In this paper, the authors propose a gradient-based algorithm for solving multi-objective optimization problems: MLM-CMOO. Moreover, under the assumption that both the individual objectives as well as the constraints are convex, the authors provide a proof in which they show the convergence rate of their algorithm to reach a Pareto stationary solution. At last, they conduct an experimental study, in which they evaluate their approach in comparison to two competitors, NSGA-II and PSL.

### Strengths
- The paper proposes a novel gradient-based algorithm for constraint MOO.
- The authors provide a proof sketch for the algorithm's convergence rate.

### Weaknesses
First of all, the paper title is entirely misleading. "Constrained Multi-Objective Optimization" sounds like a book title, or at least a PhD thesis, in which the entire research field is investigated from various perspectives, such as diverse benchmark problems, algorithmic approaches, visualization methods, performance measures, etc. However, this paper is limited to the gradient-based part of that research field and essentially focusses on the introduction of a new algorithm. 
Within this work it is stated that the goal of MOO is to find a Pareto stationary solution. However, as the optima of MOO problems usually consist of entire solution sets, the goal of algorithms usually is to find a good approximation of the solution set. Claiming that MOO focusses on finding a single solution would downplay the complexity of this research area.
The proposed approach has been designed for MOO problems that are (strongly) convex. Yet, it is not clear whether this property relates to the search or objective space. 
The usefulness of MLM-CMOO remains unclear, as real-world problems likely aren't compositions of purely (strongly) convex single-objective functions. As has been shown in various publications, concatenations of convex problems are a very special case, failing to capture the complexity of most MOO problems. By integrating a single multimodal (single-objective) function, the resulting MOO problem will have several local optima, which serve as traps for gradient-based approaches.
In the benchmark study, the proposed algorithm is compared to NSGA-II and PSL. However, NSGA-II is a population-based approach that evaluates multiple solutions per iteration. In consequence, it will likely take more time to converge. Also, population-based approaches such as NSGA-II are designed to find optima in complex black-box problems. If the problem is convex, gradient-based approaches will usually win such a comparison. Therefore, fair benchmark studies should consider state-of-the-art gradient-based approaches.
The convergence rate is indicated in relation to T, however, T is not specified/defined within the paper.
For citing, in multiple cases the wrong citing command has been used. For instance, it should be "The NSGA-II (Deb et al., 2002)" instead of "The NSGA-II Deb et al. (2002)".
The experimental analysis is kept extremely brief, providing hardly any insights.

### Questions
Does the assumption of a convex problem refer to the objective or search space?
According to Assumption 4.1, the individual objectives f_i need to be convex. Isn't this a very extreme assumption, which severely limits the contribution of this work as hardly any MOO problems will consist exclusively of convex components?
Within the experiments, MLM-CMOO has been benchmarked agains NSGA-II and PSL. How does MLM-CMOO perform in comparison to algorithms utilizing similar concepts or other gradient-based approaches? For instance, gradient ascend and gradient sliding methods could provide a fairer comparison.
Is T referring to the number of function evaluations, generations, runtime, ...?
In the literature, you find various works that investigate multimodality in MOO and also define various properties. Is the term "Pareto criticality" identical to a multi-objective "local optimum"? If so, why would you give it a different name?
The work emphasizes its focus on constrained MOO. However, why are constraints necessary in this context? Wouldn't this work look similar, if the problems would be unconstrained?
Table 1 measures the performance until a Pareto stationary point is reached. Again, this looks like a very special case, as one of the main challenges of MOO usually is to find a good approximation of the entire Pareto set (or front, respectively).
How often is each of the three algorithms executed per test problem?

### Soundness
2

### Presentation
2

### Contribution
1
