# MoSH: Modeling Multi-Objective Tradeoffs with Soft and Hard Bounds

- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 3, 5, 3

## Abstract
Countless science and engineering applications in multi-objective optimization (MOO) necessitate that decision-makers (DMs) select a Pareto-optimal solution which aligns with their preferences. Evaluating individual solutions is often expensive, necessitating cost-sensitive optimization techniques. Due to competing objectives, the space of trade-offs is also expansive --- thus, examining the full Pareto frontier may prove overwhelming to a DM. Such real-world settings generally have loosely-defined and context-specific desirable regions for each objective function that can aid in constraining the search over the Pareto frontier. We introduce a novel conceptual framework that operationalizes these priors using \textit{soft-hard functions}, \hsfs, which allow for the DM to intuitively impose soft and hard bounds on each objective -- which has been lacking in previous MOO frameworks. 
Leveraging a novel minimax formulation for Pareto frontier sampling, we propose a two-step process for obtaining a compact set of Pareto-optimal points which respect the user-defined soft and hard bounds: (1) densely sample the Pareto frontier using Bayesian optimization, and (2) sparsify the selected set to surface to the user, using robust submodular function optimization. We prove that (2) obtains the optimal compact Pareto-optimal set of points from (1). We further show that many practical problems fit within the \hsf framework and provide extensive empirical validation on diverse domains, including brachytherapy, engineering design, and large language model personalization. Specifically, for brachytherapy, our approach returns a compact set of points with over 3\% greater \hsf-defined utility than the next best approach. Among the other diverse experiments, our approach consistently leads in utility, allowing the DM to reach $>$99\% of their maximum possible desired utility within validation of 5 points.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes incorporating real-world constraints into multi-objective optimization tasks by converting the reward function into a newly introduced soft-hard function (SHF). Existing Multi-Objective Bayesian Optimization algorithms and Greedy Submodular Partial Cover algorithms are then employed to achieve sparse coverage of the Pareto frontier with respect to the introduced SHF utility ratio.

### Strengths
a. The algorithm is motivated by real-world applications, with a careful illustration of the objective design.

b. The sample efficiency and sparsification efficiency are justified with theoretical analysis and empirical results on various tasks.

### Weaknesses
 a. Questionable Necessity of SHF Utility Ratio: The necessity of introducing the SHF utility ratio is debatable. The algorithm essentially aims to offer sparse coverage of the Pareto frontier. Existing work by Zuluaga et al. (2016), as mentioned by the authors, focuses on sample-efficient identification of the $\epsilon$-accurate Pareto set. The notion of an $\epsilon$-accurate Pareto set is a more principled and interpretable objective for sample-efficient algorithms. I respectfully disagree with the authors' claim that it resembles hypervolume-based heuristics.

b. Limited Novelty of the Proposed Algorithm: The novelty of the proposed algorithm is arguable. The algorithm essentially converts the multi-objective optimization objective using the introduced SHF utility function to incorporate constraints, and the SHF utility ratio measures the coverage of the SHF Pareto frontiers. Beyond these introduced notions, components like random scalarization, the Bayesian Optimization acquisition procedure, and submodular optimizations, along with their theoretical results, are mostly off-the-shelf. Additionally, the use of existing methods—especially the MOBO algorithm by Paria et al. (2019) and the GPC algorithm by Krause et al. (2008)—is not clearly stated in the main paper but deferred to the appendix.

c. Clarity and Readability Issues: There are clarity and readability issues in the current presentation. Key components of the algorithm, including Algorithm 3 and the acquisition function, are deferred to the appendix, which hinders understanding. Furthermore, the figures, especially those in Section 5, need to be polished for better readability.

d. Classification of Related Work: A minor point—another reference by Malkomes et al. (2021) is arguably classified as a Level Set Estimation (LSE) method. From my perspective, it also addresses identifying sparse, diversified coverage of constrained optimal candidates.

### Questions
A follow-up work by Zhang and Golovin (2020) builds on Paria et al. (2019) and could allow for a more consistent analysis in terms of optimization performance, rather than assuming Algorithm 1 offers sufficiently dense coverage. The authors might consider incorporating methods from Zhang and Golovin (2020) to improve the completeness of their analysis.

***Reference***

Zhang, Richard, and Daniel Golovin. "Random Hypervolume Scalarizations for Provable Multi-Objective Black Box Optimization." In International Conference on Machine Learning, pp. 11096-11105. PMLR, 2020.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The authors consider sampling the Pareto frontier of a multi-objective optimization problem. They first sample the Pareto frontier by random scalarizations (which does not seem to come with any guarantees, at least for non-convex problems). Subsequently, they "sparsify" the sample. They show that for some preferences lambda, the latter problem is submodular and propose to use an algorithm of Krause for robust submodular observation selection (JMLR, 2008).

### Strengths
The problem is of considerable practical interest.

### Weaknesses
The paper is rather confusingly written. While the method does not come with any guarantees overall, the fact may be lost on the casual reader.

The empirical results are not convincing. Specifically, the comparison does not utilize any standard benchmarks, such as the one from CEC 2009 (Zhang et al. 2008).

The comparison does not extend to any methods with overall guarantees, e.g., by Christos Papadimitriou and Mihalis Yannakakis (e.g., https://dl.acm.org/doi/10.1145/375551.375560, https://link.springer.com/chapter/10.1007/3-540-44634-6_1).

The "Related work" discussion is rather biased and methods with overall guarantees are not even cited.

### Questions
How would your performance compare to the performance of the methods of Christos Papadimitriou and Mihalis Yannakakis (e.g., https://dl.acm.org/doi/10.1145/375551.375560, https://link.springer.com/chapter/10.1007/3-540-44634-6_1), or at least to the guarantees they have?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper considers when performing multi-objective optimization, for each objective $f(x)$ there is a soft lower bound $\alpha_{lS}$ that is ideally satisfied and a hard lower bound $\alpha_{lH}$   that must be satisfied. Additionally, it proposes a max-min framework for scalarization-based multi-objective optimization, aiming to find solutions that are robust against variations in the scalarization weights $\lambda$ within a bounded set $\Lambda$ to enhance solution diversity. 

The paper first proposes to leverage a pice-wise linear scalarization function to incorporate the soft and hard objective constraints. For the max-min formulation of optimization, given the computational challenges of directly solving the max-min problem, the paper introduces a two-step approximation process. The first step involves solving a max-average problem to generate a set of promising candidate solutions. The second step refines this set by removing points that do not significantly affect the worst-case utility ratio, leveraging the submodular properties of the utility function to apply the Robust Submodular Observation Selection (RSOS) framework and the submodular saturation algorithm.

The proposed algorithm is empirically tested on synthetic and real-world problems, demonstrating its practical applicability.

### Strengths
- The paper presents an interesting problem of multi-objective optimization considering soft and hard lower bounds.
- Perhaps the more interesting thing is the max-min framework to achieve robustness against user preference weights is novel, which might provide a new perspective of enhancing diversity in Pareto frontier search. 
- The practical approximation using a two-step process and leveraging submodular optimization techniques is sound, as it offers a feasible solution to an otherwise intractable problem.

### Weaknesses
 - Theoretical Analysis: The main drawback of this paper is, though heavily constructed on relaxations/approximations, does not provide adequate theoretical insights about the method itself, to elaborate:  
    - The transformation from the max-min to the max-average problem is presented as a practical approximation, but the paper lacks theoretical analysis regarding its impact on the optimization results. Specifically, there is no analysis on how the expectation over the scalarization weights affects the quality of the solution compared to the original max-min problem. Furthermore, the computational cost of calculating this expectation, especially as the number of objectives increases, is not thoroughly discussed. It is unclear how the method scales with higher dimensionality in the objective space. 
    - Similarly, the relaxation to a decomposable form to apply the RSOS framework is presented without sufficient justification. While the submodular properties are leveraged, the paper does not rigorously demonstrate that this decomposition maintains the desired properties of the original problem. The impact of this approximation on the final solution quality is not analyzed. 
     - If such analysis is non-trivial, a more pragmatic workaround could be to use some grid (or Monte Carlo) based approximation of the original min in max-min framework, such that it provides a good reference of the ground truth behavior of the original framework, but seems has not been done in the paper. This would at least provide a baseline to understand the quality of the proposed approximations.

- Clarity: 
    - All the plot quality is rather poor; please increase the size of all the image's legends and label and title font size. Also please consider avoiding snake case name style (e.g., consider avoiding using MOBO_RS_UCB_Lin)

### Questions
- It seems in experiments, it is compared with other acquisition functions with step 1 only (Sec 323), I am puzzled by such a motivation here, cause this is essentially comparing max-average with other MOBO acq instead of max-min (which is originally thought to be approximated by the combination of two steps)
- The objective constraints and the scalarization weights $\mathbf{\lambda}$ are handled almost independently, however, it is natural that they should share some dependence, why this is not considered. 
- The explainability of the utility function definition: The utility function definition is more complicated than necessary at least when originally read Eq. 1, especially because of the not well-motivated saturation points, why this is needed here, is that because of the suitableness of the submodular saturation algorithm? please state it clearly after Eq. 1.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The authors proposed a two-step framework for MOO that incorporates user defined soft and hard bounds on objectives and generates a compact set of Pareto optimal solutions for human decision makers to review. The framework consists of 

1. MoSH-Dense: a Bayesian optimization approach using random scalarizations and soft-hard functions to densely sample the Pareto frontier. 
2. MoSH-Sparse: a submodular optimization method that is robust to unknown human preference, to select a small, diverse subset of solutions from the dense set.

The authors evaluated this framework on a set of synthetic problems and real-world applications, including brachytherapy treatment planning, and showed merit of this method.

### Strengths
Originality:
1. This approach creatively incorporates the concepts of hard constraints and soft preferences into BO formulation, providing a more nuanced way to express decision-maker preferences.
2. The two-step framework is more user friendly: through sparcification of the originally found Pareto optimal solutions, it is easier for human DMs to pick the solutions to their preferences. Therefore, I would image there is fair amount of practical usage of this approach.

Quality:
1. This paper provides comprehensive theoretical analysis of the MoSH-Sparse algorithm, with provable guarantees on the near-optimality of the selected sparse set.

Clarity:
1. I think this paper is pretty well structured, and the proposed method is clearly presented.

Significance:
1. MoSH addresses a practical challenge in MOO by providing a way to generate a small but diverse set of solutions that respect user defined constraints. This has great potential impact to MOO applications.

### Weaknesses
1. The algorithmic novelty is fairly limited: for the dense sampling procedure, the primary modification is the incorporation of SHFs into the acquisition function, while the rest largely follow existing techniques from Paria et al (2019). The sparcification procedure follows standard active learning approach. While the problem formulation is novel and interesting, I do not think there is enough methodological innovation to meet the high standard of ICLR.

2. The paper lacks discussion of design choices of SHFs given it is quite important in the proposed method. Specifically, is it the case that decision-makers are always able to meaningfully specify soft and hard bounds? What if the bounds are uncertain or change over the exploration of the experiments? Any alternative utility function classes other than the piecewise-linear SHF discussed in this paper, and is the overall method robust to the choice of SHFs?

### Questions
1. The piecewise linear SHF seems somewhat arbitrary. Have you explored other functional forms, and what motivated this particular choice? The reasons need to be justified.

2. For the brachytherapy application, please add discussion about how the clinical experts use this system and their feedback. Additionally, compared with other MOO interactive solutions mentioned in this paper’s related works section, what is the advantage of using the proposed method here instead of those interactive mechanisms? The experiment section lacks comparisons against those interactive MOO methods.

### Soundness
2

### Presentation
2

### Contribution
2
