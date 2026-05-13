# Learning-Guided Rolling Horizon Optimization for Long-Horizon Flexible Job-Shop Scheduling

- Decision: Accept
- Scores: 6, 5, 8, 8

## Abstract
Long-horizon combinatorial optimization problems (COPs), such as the Flexible Job-Shop Scheduling Problem (FJSP), often involve complex, interdependent decisions over extended time frames, posing significant challenges for existing solvers. While Rolling Horizon Optimization (RHO) addresses this by decomposing problems into overlapping shorter-horizon subproblems, such overlap often involves redundant computations. In this paper, we present L-RHO, the first learning-guided RHO framework for COPs. L-RHO employs a neural network to intelligently fix variables that in hindsight did not need to be re-optimized, resulting in smaller and thus easier-to-solve subproblems. For FJSP, this means identifying operations with unchanged machine assignments between consecutive subproblems. Applied to FJSP, L-RHO accelerates RHO by up to 54\% while significantly improving solution quality, outperforming other heuristic and learning-based baselines. We also provide in-depth discussions and verify the desirable adaptability and generalization of L-RHO across numerous FJSP variates, distributions, online scenarios and benchmark instances. Moreover, we provide a theoretical analysis to elucidate the conditions under which learning is beneficial.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a learning-augmented approach for the Flexible Job Shop Scheduling Problem (FJSP) with a long horizon. The authors consider rolling horizon optimization (RHO) where overlapping ordered subproblems are solved sequentially. The idea is to predict which decisions should remain unchanged from one subproblem to the next in order to restrict the subproblem sizes. This may have two impacts: it can accelerate the solving and/or for a fixed time budget per subproblem, improve the quality of the solutions. More precisely, the paper proposes to learn a model which predicts which of the overlapping operations should keep their previous machine assignment. The model is trained in a supervised way where the ground truth is provided by performing RHO and extracting the operations with unchanged assignments. The approach is evaluated on several variants of the FSSP, with varying objectives, distributions and additionnal noise.

### Strengths
* The paper makes an original contribution by introducing learning in RHO for the FJSP
* The paper manages to solve much longer horizon problems than existing methods
* In-depth analysis of the performance of the proposed approach in various settings
* The paper is generally clear and well organized.

### Weaknesses
* The main weakness is the focus on the FJSP which limits its scope. The idea seems quite generic, so illustrating it on more long-horizon CO problems, e.g. other scheduling variants, would strengthen the contributions and broaden the scope.

* In the theoretical analysis (Sec 6), while the intuition that "the more irregular the operations to be fixed (O∗ fix), the more advantageous LRHO can be, because of the greater potential gain from prediction" is clear, I did not understand how proposition 1 was proving this point. I found the technical part difficult to follow.

* In the experiments, I found that the comparison to DRL-450 is not so informative. While the learning task of proposed L-RHO is a classification on the subproblems, so 450x[the number of supbroblems per instance] samples seem a reasonable training set size, the "DRL" baseline is  an end-to-end constructive method, and it makes sense that its training requires more data than 450 instances.

### Questions
* The paper considers several settings as first steps towards the online setting. Why not consider the purely online setting? What kind of adaptations would be needed?
* What's the impact of the time budget per subproblem on the final performance? I imagine if the budget is large enough, standard RHO would lead to the best solutions.

Remarks:
* CP-SAT being exact solver, it would be interesting to have the optimal value as a reference to assess the quality of the other methods. Clearly restricting it to 1800 sec is not eniugh to get high qulity solutions esp for |O|=2000 in Table 1.
* "Enhancing the efficiency and scalability of Combinatorial Optimization Problems (COPs) has been a central focus.." --> missing "solving" or "methods" or such.
L151: "Each sub-problem is limited to T seconds". We understand later that T is the solving time, but It would be nice to make it explicit already here.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper proposes L-RHO, a rolling horizon optimization algorithm designed for the flexible job-shop scheduling problem (FJSP) that leverages learning to select overlapping variables in subproblems. As the first study to guide the RHO algorithm with a learning-based approach, L-RHO demonstrated performance improvements across diverse FJSP settings.

### Strengths
This paper is noteworthy as an initial study that guides the decomposition process of subproblems in the RHO algorithm using a learning-based neural network. It also stands out for conducting comprehensive experiments and analyses across diverse FJSP settings.

### Weaknesses
The specific details about making RHO learnable are mostly presented in the supplementary material rather than the main sections, making it challenging to fully grasp the proposed learning framework. Given the extensive content of the paper, focusing more on the learning aspects in the main text would improve clarity and comprehension. Additionally, it is somewhat disappointing that in Table 1, the performance of L-RHO is not markedly superior to other baseline comparisons.

### Questions
1. Could the learning guide proposed in this study potentially be adapted for use in other algorithms beyond RHO?
2. Would the ideas proposed in this paper be adaptable for subproblem decomposition in various types of long-horizon combinatorial optimization problems?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Rolling horizon optimization (RHO) [1] is a widely used approach for tackling long-horizon production planning problems in stochastic environments. RHO solves these problems by breaking them into overlapping, shorter-horizon subproblems that roll forward over time. This overlap ensures continuity between consecutive subproblems.

This paper proposes a machine learning framework to identify decision variables that should be predetermined based on the prior horizons, allowing them to be treated as fixed for the current horizon. This helps to reduce the size of the optimization problem for each horizon.
Experimental results show the proposed approach is not only fast but also result in better solutions.


1: Sethi, Suresh, and Gerhard Sorger. "A theory of rolling horizon decision making." Annals of Operations Research 29.1 (1991): 387-415.

### Strengths
**Significance**: This paper studies an important problem relevant in many production planning operations. The proposed approach seem to surpass the state of the art, a significant contribution.

**Originality**: I am not entirely familiar with the relevant literature. I searched articles published in the last five years. This work seems to take a novel direction to tackle the RHO problem.

**Quality**: Quality of the paper is good as it covers both theoretical and empirical analysis. 

**Clarity**: The overall objective and methodology of the paper are easy to understand at a high level. However, some of the introduced notations are difficult to follow, and the intuitive explanations provided are sometimes lacking
(See weakness).

### Weaknesses
- $m$ is used to denote a machine $m \in M$ as well as an assignment $m: O \rightarrow M$ (line 133 and 134).

- How can default RHO be suboptimal compared to proposed L-RHO? If I  understood correctly, default RHO solves the true problem till optimality, hence it might be computation-intensive but should have the best performance. Is it due to the fact that all algorithms have been run with a timelimit? If that's the case, can default RHO perfrom better than L-RHO if both are allowed to run for more amount of runtime?

-  It seems that the accuracy, precision, and recall of the classifier were not reported. I expect these metrics to be high for the model to demonstrate good performance. I would recommend to report this in the paper to provide a clearer picture of the ML model's performance.

### Questions
- Can you provide intuitive explanation of $q^\star$ (line 219)? Is it the assignment which has most number of overlapping assignments? What is the significance of this? I do not get the motivation for setting $y_O^\star = y_O^{q^\star}$​. Could you provide some insight/intuition into the reasoning behind this? 
- What does $w_{pos}$ represent? 
- Can you comment on what features turn out to be important in identifying decision variables that should be fixed?
- When increasing the congestion level (line 424), did you train a new model or use the one trained with low congestion?
- Have you explored the attention map? Is it possible draw a significant conclusion form that? For example, an operation is more likely to be fixed if a machine has been running for a long time!
- It is mentioned in the text that the operations are divided into subproblems of fixed duration T. How did you predetermine the value of T in your experiments? Should not it depend on the execution time of the operations?

### Soundness
4

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents L-RHO, the first learning-guided Rolling Horizon Optimization (RHO) framework for long-horizon FJSP.  Empirically, this paper shows that L-RHO accelerates RHO by up to 54% while showing significantly improved solution quality, enabling it to outperform other heuristic and learning-based baselines.

### Strengths
1. This paper claims to be the first learning-based framework to guide RHO for long-horizon Combinatorial Optimization Problems (COP).
2. In their experiments, L-RHO reduces RHO solve times by up to 54% and improves solution quality by up to 21% compared to various heuristic and learning-based baselines, across a range of FJSP settings and distributions.
3. Test on large instances, which operations are over 600, much larger than previous benchmarks.

### Weaknesses
**The novelty for learning-based RHO is limited.** L-RHO is very similar to RHO except for the customized attention based model. When compared to RHO, the experiment results (in Table 1) show only a slight improvement (less than 3% in Table 1 and also for the issue of large operations mentioned in the next item).

**The experiments are unconvincing.**
1. First, more comparisons to others are expected. For example, [1] and [2]. 
2. Second, although it seems impressive to perform well for “long-horizon” FJSP (e.g., 2000 operations in Table 1), unfortunately it is commonly agreed in this area that the more operations, the better performance. For example, in [3], the performance is nearly the optimal for large operations. 

[1] Echeverria, I., Murua, M., & Santana, R. (2023). Solving large flexible job shop scheduling instances by generating a diverse set of scheduling policies with deep reinforcement learning. arXiv preprint arXiv:2310.15706.

[2] Han, B., & Yang, J. (2021). A deep reinforcement learning based solution for flexible job shop scheduling problem. International Journal of Simulation Modelling, 20(2), 375-386.

[3] Ho, K. H., Cheng, J. Y., Wu, J. H., Chiang, F., Chen, Y. C., Wu, Y. Y., & Wu, I. C. (2024). Residual scheduling: A new reinforcement learning approach to solving job shop scheduling problem. IEEE Access.

3. Third, from the above argument, it is also interesting and important to see the performances for some traditional benchmarks, such as those mentioned in line 289 (Wang et al., 2023a; Behnke and Geiger, 2012; Dauzere-P ` er´ es and Paulli ` , 1997; Hurink et al., 1994; Brandimarte, 1993). 
4. Fourth, for CP-SAT or GA, as the problem size increases, the required time for CP-SAT and GA apparently grows a lot. It seems meaningless to compare these methods with 1800 second computation.

**Unclear theoretical analysis** 
In the section of theoretical analysis, the authors present notations and formulas of “Assump 1.” and “Prop.1” without interpretation. Some are not defined, such as $n_{fn}$, $n_{pn}$, $n_{fix}$, etc. Note that they leave partial interpretation to Appendix A.5, which readers are not obligated to read. In the main text, it still needs to be self-contained.

**Minor comments.**
1. Symbol is inconsistent: \Tau in Section 3 (e.g.: line 130) and 5 (e.g.: line 267) means jobs set, but in Section 4 (e.g.: line 235), it means machines.
2. Figure 4 should be presented in the main text. 
3. About "Machine/Operation Concatenation" (In Section LEARNING-GUIDED ROLLING HORIZON OPTIMIZATION), it needs to add " For each new operation that does not have a machine assignment, the concatenated machine feature is a dummy all-zero feature ", as mentioned in Appendix.

### Questions
1. Look-ahead oracle is unclear. An introduction and framework should be added, probably in appendix. 
2. What is the value of the weight (W_pos) of loss function?

### Soundness
2

### Presentation
2

### Contribution
2
