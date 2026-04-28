# Differentiable Integer Linear Programming

- Decision: Accept
- Avg Score: 7.20
- Scores: 6, 8, 8, 6, 8

## Abstract
Machine learning (ML) techniques have shown great potential in generating high-quality solutions for integer linear programs (ILPs).
However, existing methods typically rely on a *supervised learning* paradigm, leading to (1) *expensive training cost* due to repeated invocations of traditional solvers to generate training labels, and (2) *plausible yet infeasible solutions* due to the misalignment between the training objective (minimizing prediction loss) and the inference objective (generating high-quality solutions).
To tackle this challenge, we propose **DiffILO** (**Diff**erentiable **I**nteger **L**inear Programming **O**ptimization), an *unsupervised learning paradigm for learning to solve ILPs*.
Specifically, through a novel probabilistic modeling, DiffILO reformulates ILPs---discrete and constrained optimization problems---into continuous, differentiable (almost everywhere), and unconstrained optimization problems.
This reformulation enables DiffILO to simultaneously solve ILPs and train the model via straightforward gradient descent, providing two major advantages.
First, it significantly reduces the training cost, as the training process does not need the aid of traditional solvers at all.
Second, it facilitates the generation of feasible and high-quality solutions, as the model *learns to solve ILPs* in an end-to-end manner, thus aligning the training and inference objectives.
Experiments on commonly used ILP datasets demonstrate that DiffILO not only achieves an average training speedup of $13.2$ times compared to supervised methods, but also outperforms them by generating heuristic solutions with significantly higher feasibility ratios and much better solution qualities.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a new learn-to-optimize paradigm that trains a solution predictor without relying on traditional solvers to generate label data. As a result, the entire pipeline is significantly faster by avoiding solver runs. The paradigm is based on designing a Lagrangian loss for the predicted solution and iteratively updating the predictor using the gradient of the Lagrangian loss.

### Strengths
The idea of replacing solvers in the training pipeline is intriguing. Indeed, I can envision many problem classes where off-the-shelf solvers may underperform compared to simple gradient-descent-based algorithms. The proposed method could be highly effective for such problems.

### Weaknesses
When comparing their results to existing methods based on solver-generated labels, the authors overlook an important limitation of their approach: their unsupervised learning method does not learn from optimal ILP solutions and may instead be trained to only produce significantly sub-optimal solutions.

Gradient descent algorithms for MILP problems are not new (e.g., see the paper "Feasibility Jump: an LP-free Lagrangian MIP heuristic") and they generally converge to a suboptimal, heuristic solution. By performing gradient descent on the Lagrangian loss, the unsupervised learning method proposed in this paper essentially learns from heuristic solutions, which may fall far short of optimality.

To ensure a fair comparison, I believe the authors should modify the solver-based supervised learning pipelines by setting limits on (i) the solving time and (ii) the number of branch-and-bound nodes. Most off-the-shelf solvers can find a good solution in a short time, with the extended solving time largely dedicated to ensuring optimality. Since the authors are not learning from optimal solutions, they should compare their approach to existing methods without optimality requirements. Furthermore, the comparison should include a more detailed analysis of the solution quality, not just the objective value. For example, the integrality gap of the solutions found by the proposed method should be compared to the integrality gap of the solutions used to train the supervised learning baselines. This would provide a more nuanced understanding of the quality of the solutions produced by the proposed method.

### Questions
see weakness.

### Soundness
2

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors propose an interesting approach for unsupervised learning in ILP. Evaluating it in several binary programming settings, and investigating the approach itself empirically in various ways. The approach itself relies on considering that a model predicts a continuous solution where each entry represents the probability of assigning a given decision variable to 1 or 0. The model is then trained to optimize a loss that combines the expected objective value with the expected constraint violation. The expected constraint violation is estimated by sampling several solutions and computing expected constraint violation using the samples. The benefit of the unsupervised approach is that it bypasses the need to expensively collect solutions from training instances. Additionally, the authors propose that the unsupervised approach helps improve predictive performance by encouraging the predicted objects to represent feasible solutions. The authors present theoretical motivations for the approach, as well as thorough empirical evaluation on toy examples to give insights as to how the approach works.

Overall, the work is interesting while there is some room for improvement, if the authors address my comments I am eager to increase my score.

### Strengths
The strengths of the approach are that it doesn’t require expensive optimization solving for training time. Most of the literature hasn’t considered this as it is assumed that practitioners are willing to spend time upfront training a model that can be deployed on many instances, but nevertheless it can be impactful in some settings to require less training time, for instance it can be possible to train on many more problem instances given the same training time, or even larger instances given that training instances don’t need to be solved to optimality.

The approach itself is well motivated and the paper is well-written. 

The illustrative toy example is helpful for giving intuition for how the approach works in a simple setting.

### Weaknesses
The approach is proposed for general ILP; however, the approach seems to be tailored to binary programs. There is a remark stating that ILP can be reduced to binary programs; however, it would help strengthen the paper if there were experimental results validating that this approach can be used in general ILP tasks to make that claim (such as on MIPLIB instances other than the CVS dataset), or to rephrase the method as working for binary programs. Specifically, the reduction of general ILPs to binary programs often introduces a large number of additional variables, which can significantly impact the performance and scalability of the proposed method. It is unclear how the method would perform with such a large increase in dimensionality.

Theorem 2 statement 2: it seems that this direction of solvability/optimality doesn’t really apply in this setting since the predicted continuous x is always fractional as considered below in the approach. Is there any indication that the distribution being optimal for P2 has any implication about the optimality wrt P1 of the discrete solutions that the distribution represents? Is there any indication of whether the probability distribution puts weight on suboptimal solutions? The theorem implies that an optimal solution to the relaxed problem (P2) will have many components that are binary, but it does not guarantee that the discrete solutions sampled from the predicted distribution will be optimal or even feasible for the original problem (P1). The connection between the optimality of the continuous relaxation and the quality of the discrete solutions needs further clarification.

It is unclear whether the approach would outperform baselines other than the single PS baseline considered here as more recent work with available code seems to have outperformed the predict and search approach such as the two cited works. However, it would be interesting to see if the unsupervised approach could be integrated in the settings considered in previous work as well. The lack of comparison with state-of-the-art methods limits the assessment of the proposed approach's effectiveness. It is also unclear how the method would perform on more complex problem instances or in settings where the problem structure is different from the supply chain problem considered in the experiments.

Specific comments:
- Remark 2 ends in “Otherwise,” is something missing there?
- Figure 4 is missing
- Toour is missing a space

### Questions
How different are the initial solutions compared to the solutions after one round of neighborhood search? (i.e. after solving the optimiazation problem with constraint (9) added?

Why are the Zheng 2024 and Huan 2024 baselines not included as they seemed to surpass the PS approach and provide implementations.

How many decision variables do the different settings have? It is somewhat unclear why this method would be more robust to changes in delta than baseline approaches. Is it the case that the predicted solution is already close to optimal, so a large neighborhood doesn’t need to be searched?

How does the approach generalize to different kinds of problems? Either to larger instances or out of distribution instances e.g. MIPLIB?

What are the feasibility rates for PS? They are given for DiffILO but not present for the baseline. It seems figure 4 is missing.

How is mu determined? Is it determined as a hyperparameter? Or adaptively selected to ensure feasibility?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors proposes DiffILO, a new approach that uses machine learning to solve integer linear programs (ILPs) without supervision and without traditional solvers. DiffILO transforms ILPs into continuous, differentiable, and unconstrained problems through probabilistic modeling and applied the penalty based merit function, allowing for optimization using gradient descent directly. That is, there is no need in calling solver at all. Instead, the model (which predict solution to ILP) is trained via backpropagating the merit function.

Unlike supervised methods that require labeled data typically obtained by solving ILPs, DiffILO operates in an unsupervised manner, which reduces training time. The approach has been tested on small-to-medium scaled ILP datasets, demonstrating its ability to speed up the training process and produce feasible solutions. These solutions may differ from those generated by supervised methods.

### Strengths
Overall, I think this is an interesting perspective into learning predictive models for obtaining approximation solution for combinatorial problems. Majority of previous approaches use a solver calls in some way to learn that predictive mapping, whereas here it is done by defining a differentiable (a.e.) function that serves as an objective to optimize. In this regard, I find it similar to the decision-focused learning (DFL) or predict-then-optimize framework [1,2,3] where the task is to learn a model which maps observable features into latent representation (e.g. coefficients in LP objective) used by solvers. Here, the training formulation is similar but the solution is predicted instead of latent representation. Particularly [3] draws this connection between these two domains and apply it for MINLPs. I encourage authors to add this line of research and elaborate on this. Other strengths of the paper include:

- theoretical justification of the continuous relaxation applied for this problem. Although ILP covers a lot of important class of problems, however I don't see these to be directly extended into non-linear case.
- experimental results look convincing in terms of both runtime and solution quality. Although adding larger scale experiments would be beneficial;
- the method is intuitive to understand and makes sense to me.
- can be directly applied to speed up the runtime for traditional solvers;


[1] A. N. Elmachtoub and P. Grigas. Smart “predict, then optimize”. arXiv:1710.08005

[2] A. Ferber, B. Wilder, B. Dilkina, and M. Tambe. MIPaaL: Mixed integer program as a layer. 

[3] A. Zharmagambetov, B. Amos, A. Ferber, T. Huang, B. Dilkina, and Y. Tian (2023): "Landscape Surrogate: Learning Decision Losses for Mathematical Optimization Under Partial Information".

### Weaknesses
Some are mentioned in Strengths above. Additionally, I think that the supervised approaches a bit underperforming here due to limited sample size. With enough data for supervision, I think those approaches should also improve drastically, especially for larger scale problems.

### Questions
- typo in line 198;

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces Differentiable Integer Linear Programming Optimization (DiffILO), a novel learning method for predicting high-quality Integer Linear Programming (ILP) solutions in an unsupervised manner, without the reliance on traditional solvers. The proposed prediction model is a Graph Neural Network (GNN) module followed by a multilayer perceptron (MLP). By transforming ILPs into a continuous, differentiable, and unconstrained form through probabilistic modeling and the penalty function method, the authors enable the use of gradient descent for optimization. The approach avoids reliance on traditional solvers and labeled data, reducing training time.

### Strengths
1. The paper is well-written and clear. 
2. Adequate theoretical support is provided for the key steps.
3. As one of the NeurIPS reviewers for this paper, I am pleased to see that the paper includes many of the experimental results requested during the rebuttal period.

### Weaknesses
1. Given that there are various relaxations made during the conversion of the ILP to an unconstrained problem, the experiments do not ablate the effect of the choices made at each step. For example, for the relaxation converting the constraint violation into a sampling based objective, it is not clear what the effect of the number of samples is. Specifically, how does the variance of the stochastic gradient change with different sample sizes, and what is the computational overhead of increasing the sample size? Furthermore, the impact of the specific form of the penalty function is not explored. In the Appendix, the training loss has been modified via some specific form of normalization, but it is not clear what happens to the empirical performance when such normalizations are removed. It is important to understand if the normalization is crucial for convergence or if it is simply a speedup technique. The lack of these ablation studies makes it difficult to assess the robustness of the method.
2. SC, MIS and CA are easy combinatorial optimization problems and hence identifying feasible solutions without relying on MILP solvers is not challenging. Experiment results on more realistic ILPs (such as those from MIPLIB 2017) should be included in the main paper. The current benchmarks do not adequately demonstrate the method's ability to scale to more complex problems with a larger number of variables and constraints. The absence of results on standard benchmarks like MIPLIB 2017 raises concerns about the practical applicability of the proposed approach.

### Questions
I am interested in the results and analysis of the MIPLIB experiments. Why were the “neos” datasets chosen for experiments during the NeurIPS rebuttal but not included in the current submission? Instead, the “CVS” datasets were presented. During the NeurIPS rebuttal, after the authors fixed the bugs in the Gurobi configuration, the solving time for Gurobi changed from 1000 seconds to less than 100 seconds.

The experimental results on the neos18 dataset indicate that Gurobi+DiffILO requires a longer solving time than pure Gurobi, and I am curious about the reason for this. I reviewed the problem details of neos18 and the five “CVS” datasets presented in the paper, and found that the number of variables and constraints is smaller in the five “CVS” datasets. For example, neos18 has 11,402 constraints, while the five “CVS” datasets have fewer than 5,000 constraints. Does this suggest that DiffILO may not perform well on more complex benchmarks? Could you provide the experimental results on the “neos” datasets and explain why Gurobi+DiffILO performs worse than Gurobi?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper concerns itself with integer linear programs (ILPs), a NP hard optimization problem. Previous works have trained models in a supervised manner to predict near optimal solutions as a heuristic guess to a problem instance. In this work, the authors propose a unsupervised method to train predictors: namely, by using a Bernoulli relaxation of the ILP variable, and reformulating the ILP as a unconstrained problem (via the introduction of a penalty function), a application of the Gumbel-Softmax trick (as a “relaxed Bernoulli”) enables for gradient flow suitable for back -propagation.

The mathematics corresponding to the methodology are clearly presented in detail. The methodology is evaluated empirically on three ILP benchmarks:

- Set covering 
- Maximum independent set
- Combinatorial Auctions

and compared to i) traditional solvers ii) Predict-and-search framework, as baselines. In this section the authors also provide practical results e.g. which hyper parameters are crucial, learning rate schedule, which are helpful for practitioners.

### Strengths
The paper is well written, with the methodology and experiments both presented in a clear and coherent fashion. As far as I am aware, the unsupervised learning approach is indeed completely novel. Whilst there is a wealth of literature for creating differentiable proxies of CO problems, (for which the paper calls upon multiple tools / results), I believe the overall methodology to be a significant contribution. The presentation of the mathematics underpinning the relaxation and reformulation was particularly well written.

### Weaknesses
The methodology in its current form is constrained to using a GNN as a predictor for the Bipartite graph, which seems quite excessive ; the graph structure is simple and GNNs have a high computational complexity (and poor scalability). However, the ideas presented in the work are independent of this and it is nonessential to the method. Below are two suggestions for methods to replace the GNN in the current methodology, both of which would allow for more general architectures (e.g. transformer). These may be worth mentioning as future possible work.

- Sinkhorn Knop for soft matching between nodes:  see  **[Cuturi et al 2013]** *Sinkhorn distances: Lightspeed computation of optimal transport*. (An example of such an implementation can be seen in **[Caron et al 2021]** *Emerging Properties in Self-Supervised Vision Transformers*)
- Differentiable Clustering for a soft cluster assignment (between a cluster for 0 and 1): see  **[Stewart et al 2023]**  *Differentiable Clustering with Perturbed Spanning Forests*.
- Vector Quantization (not differentiable, but commonly used in practise to assign discrete values): **[van den Oord 2017]** *Neural Discrete Representation Learning*.


As someone who is not familiar with ILPs, it would have been nicer to have further motivation on the real world applications of ILPs, and more intuition as to why DNNs are preferable to predict solutions over other established search methods (please note: I am not questioning either of these points, just pointing out that a more explicit clarification on these would be helpful to a non-expert reader).

### Questions
In Remark 5 you mention that you favour the relaxed Bernoulli over using REINFORCE, citing that it does not explicitly propagate the gradients from $\phi_j(x)$. Did you conduct experiments to verify that in practice this is indeed the case? If so this could be interesting to add to the Appendix, (appending a reference to Remark 5).

I believe the following reference would be useful for the paper (regarding smoothing COs): [Berthet 2020] *Learning with Differentiable Perturbed Optimizers*

### Soundness
4

### Presentation
4

### Contribution
3
