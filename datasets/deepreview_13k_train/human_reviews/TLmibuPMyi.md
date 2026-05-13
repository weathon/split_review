# An Efficient Algorithm For Computing Optimal Wasserstein Ball Center

- Decision: Reject
- Scores: 5, 5, 3, 3, 3

## Abstract
Wasserstein Barycenter (WB) is a fundamental problem in machine learning, whose objective is to find a representative probability measure that minimizes the sum of its Wasserstein distance to given distributions. WB has a number of applications in various areas.  However, in some applications like model ensembling, where it aggregates predictions of different models on the label space, WB may lead to unfair outcome towards underrepresented groups (e.g., a "minority'' distribution may be far away from the obtained WB under Wasserstein distance). To address this issue, we propose an alternative objective called  ``Wasserstein Ball Center (WBC)''. Specifically, WBC is a distribution that encompasses all input distributions within the minimum Wasserstein distance, which can be formulated as a minmax optimization problem. We show that the WBC problem with fixed support is equivalent to solving a large-scale linear programming (LP) instance, which is quite different from the previous LP model for WB. By incorporating some novel observations on the induced normal equation, we propose an efficient algorithm that accelerates the interior point method by $O(Nm)$ times ($N$ is the number of distributions and $m$ is the support size).  Finally, we conduct a set of experiments on  both synthetic and real-world datasets. We demonstrate the computational efficiency of our algorithm, and showcase its better accuracy on model ensembling under heterogeneous data distributions.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes the WBC-problem, which is a variant of the well-known Wasserstein-ball problem. Here, given a set of discrete distributions $D_1, D_2, \dots, D_N$  the goal is to compute a distribution (with discrete support over a set of size $m$) that has minimal maximum wasserstein distance from any of these. The main modification from the typical WB-problem is that we seek to minimize the maximum distance, rather than minimize sum weighted sum of the distances. The motivation for doing so is fairness concerns, where averaging a loss may unfairly penalize distributions that correspond to underrepresented or marginalized classes. 

This problem can be relatively straightforwardly be framed as a linear program -- in particular, the wasserstein distance between two discrete distributions can be written as the dot product between 2 appropriately chosen matrices, and thus by using a slack variable we obtain a typical linear program. However, the main technical difficulty in this program is the size -- $N$ and $m$ both can be fairly large, and a naive implementation of the interior point method will achieve an $O(N^3m^4)$-running time, which is infeasible. 

Thus, the main technical innovation of this paper is a modified interior point method that achieves an $O(N^2m^3)$ running time for this problem. The high level idea is to exploit the shared structure amongst all of the constraint matrices corresponding to the $N$ distributions. Essentailly, interior point methods rely on inverting a matrix, and the matrix being inverted has a block structure that the authors exploit to significantly reduce the running time. 

Finally, this work demonstrates that their algorithm achieves better performance on the Fairfaces dataset than naively using the WB-formulation would.

### Strengths
This paper offers a fundamental optimization problem and gives a fairly elegant and non-trivial solution to it. In particular, the gains in their running time enable this algorithm to scale to relatively large sets of distributions.

### Weaknesses
I found the claim that concerns about fairness motivate this problem to be somewhat tenuous. First, while the relevance of fairness for tasks such as the fairface dataset makes sense, it is unclear to me that for downstream tasks over more complex distributions that the WBC method will significantly improve fairness. In particular, arguing for a lower maximum distance does not ensure fairness in any of the more rigorous definitions of fairness. 

Second, while it is intuitive to me that the WBC method offers a reasonable solution in ensuring no class distribution is too far from the mean, it is unclear to me why simply changing the distribution weights over WB is insufficient. In particular, if it appears as though one distribution is significantly underrepresented, we could simply apply a larger weight to that distribution and re-run the original optimization problem. While this is more computationally expensive, it could nevertheless be better suited for downstream tasks where the freedom to choose the weights of each distribution allows the practitioner to achieve some kind of objective measure of fairness.

### Questions
See weaknesses -- could you address my concerns about the connection between this problem and fairness?

### Soundness
4

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
4

### Summary
The paper proposes a method to solve the Wasserstein Ball Center problem in case of distributions with discrete support by rewriting it as a Linear Programming problem. Finally several experiments are conducted to demonstrate the efficiency of the proposed algorithm  as well as the enforced fairness of a solution.

### Strengths
The LP formulation of the WBC problem in the discrete support case as well as the proposed iterative algorithm are interesting.

### Weaknesses
$	extbf{Experiments}$:

The overall experiments were supposed to demonstrate two points: (i) the effectiveness of the proposed algorithm in solving the WBC problem, (ii) the advantage of WBC over the classical WB in fairness. Both points were not convincingly justified by the chosen experiments.

$	extbf{i}$: For the first point, it would be preferable to see the comparison to some other existing optimization algorithms to solve the problem (6), for example the IPM without preconditioning. Additionally, could you clarify if the results in Figure 2 are averaged over multiple runs, and if not, could you include error bars or standard deviations to show variability. The comparison to Gurobi is not sufficient, as it is a commercial solver that may implement various heuristics, making it difficult to isolate the performance of a specific algorithm. A more controlled comparison against a standard implementation of an Interior Point Method (IPM), without preconditioning, would provide a clearer understanding of the proposed method's efficiency. The current comparison lacks the necessary detail to assess the true performance gains.

$	extbf{ii}$:  For the second point, the fairness argument was not very well justified. The fact that a solution to the minmax probelm (2) (WBC) is more sensitive to outliers than a solution to (1) (WB) was straightforward from the fitness function. Are there any quantitative metrics that can justify this claim? The current analysis relies on an intuitive understanding of the min-max objective, but lacks concrete metrics to quantify the fairness improvement. For instance, metrics like the maximum individual loss or the variance of losses across different distributions could be used to provide a more rigorous comparison of the fairness properties of WBC and WB. Without such metrics, the fairness claim remains qualitative and not sufficiently supported by the experiments.

$	extbf{iii}$:  The conclusion was a bit sloppy, would be valuable to list some suggestions for a future work.  For example, you could propose exploring theoretical guarantees, applications to other domains, or comparisons to additional fairness metrics.

$	extbf{Small typos}$:

- Page 3 : missing reference to Woodbury’s equality
- Page 4: missing reference to "fixed-support WB"

### Questions
$\textbf{Extensions}$:
- How does the program 6 changes when we lift the assumption of the fixed support distributions ? Since all the distributions are assumed to be of a discrete support, couldn't we just define the common support as a union and lift the assumption ?

$\textbf{Experiments}$:
- How do you explain the non-monotonic behavior of the accuracy as a function of noise ratio that we observe in the table 1. 
- Same question for the results at u = 100%
- What happens in the lower noise regime (i.u for u<50%?)
- Have you experimented with the entries following other distribution than uniform.

Could you provide possible explanations or hypotheses for these observations? Additionally, reporting results for the lower noise regime (u < 50%) would provide a more complete picture of the method's performance across different noise levels.

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
The paper proposes a method for computing the centre of the _Wasserstein Ball_, that is, the minimum-radius ball in Wasserstein space that contains a given set of distributions. The aim of this Wasserstein Ball Center (WBC) is to be used as an alternative to the Wasserstein Barycentre, as it is expected that WBC will be more robust to outliers and thus be promising in fairness applications. 

Though some authors have considered the WBC in the past, the main contribution of the article seems to be the formulation of the min-max problem and the proposed solution.

### Strengths
The paper is well motivated. The WBC is certainly an attractive alternative to the Wasserstein barycentre. 

The formulation of the optimisation problem is provided in a detailed manner, and it seems to be the main contribution of the article (Thm 3.2). However, this reviewer is not an expert in optimisation and this cannot assess the correctness (other than the experimental evidence provided) or the novelty of the proposed solution

The experimental validation *for the computational complexity of the proposed method* is convincing

### Weaknesses
My main reservation with this article is that it makes a number of claims about the proposed method being suitable for *fairness*, however, the method is only either tested synthetically on data with outliers. 

Fairness in ML is much more than robustness to outliers. There are defined quantitative indicators for fairness (e.g., disparity impact) and the notion of sensitive/private variables in a learning setting. Modifying an average is *far* from a subset of distributions is not solving a fairness problem. Therefore, saying that *WBC shows better fairness than WB* is a jumping conclusion as i) no fairness problems have been presented in the paper, and ii) no fairness indicators have been measured.

Why not leave the contribution just as a gain in computational complexity? (again, this is not my area of expertise)

There are some English problems, e.g., _we uses_  or "who >> which" but nothing too important. There are also some double parenthesis in the references and missing references (?)

Caption of Fig 1: what is "t"?

There are other types of barycenters that were not considered, e.g., the weak Wasserstein barycenter, and also some unbalanced OT techniques that can help with the outlier detection problem

### Questions
see above

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
4

### Summary
The weighted Wasserstein barycenter problem seeks to find a probability distribution $\mu^*$ that minimizes the sum of Wasserstein distances to a given set of probability distributions $\mu_1,\ldots,\mu_N$ with respective weights $w_1,\ldots,w_N$, i.e., $\mu^* = \arg \min_{\mu} \sum_{i=1}^N w_k W_p(\mu, \mu_k)^p$, where $W_p(\cdot, \cdot)$ denotes the $p-Wasserstein distance. The Wasserstein barycenter problem is often used in applications such as image processing, natural language processing, machine learning, and computer graphics.

This paper notes that this formulation of the problem may lead to unfair outcomes towards specific distributions that could represent "protected" subpopulations and thus proposes an alternative formulation to minimize the objective $\min_{\mu} \max_{k=1 \in [N]} w_i W_p(\mu, \mu_k)$. They show that the problem can be formulated as a linear program when the support of the probability distributions is discrete and then describe interior point methods to improve the efficiency of solving the linear program. Finally, the paper includes a number of experiments on synthetic and real-world datasets, evaluating the algorithmic performance for model ensembling on imbalanced data distributions.

### Strengths
+ The main technical claims of the paper are supported with mathematically rigorous statements
+ Both the Wasserstein barycenter problem and the notion of fairness are important to the ML community
+ The experiments act as a small-scale demonstration that reinforces the theoretical guarantees provided in the paper

### Weaknesses
 - The variant of WBC introduced in this paper seems to be the standard socially fair objective, which has been extensively studied for the closely related problem of clustering, often using linear programming techniques, e.g., see [MV21] below
- The discussion on fairness is lacking, given that the main focus of the paper is a problem motivated by fairness
- The main techniques of the paper are for improving interior point methods on the linear program corresponding to the problem, which does not necessarily introduce insightful combinatorial properties about the problem
- The experiments on real-world datasets are not sufficiently comprehensive to convincingly demonstrate a large difference in WBC and the proposed variant (though the motivation is clear) or the practicality of the algorithm across all use cases
- There is a small number of presentation issues, e.g., broken references, extraneous equation markers, missing line breaks, missing theorem statements, substandard proof presentations, etc.

### Questions
N/A

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
Motivated by fairness applications, this paper proposed an alternative notion of the Wasserstein barycenter (WB). The new "center" for probability measures is called the Wasserstein Ball Center (WBC), which aims to minimize the farthest distance from the center to the input measures. The WBC is solved by a linear programming (LP) formulation via an accelerated interior point method tailored to the special low-rank structure of the constraint matrix. Some numeric advantages are demonstrated through an off-the-shelf commercial LP solver Gurobi.

### Strengths
Wasserstein barycenter is a timely and important research objective. Minimal distance from the farthest input measure formulation seems to be a new formulation to account for fairness. The proposed interior point method (IPM) uses an observation that the constraint matrix can be expressed as the sum of a block diagonal matrix and a low-rank matrix, which allows faster matrix inversion. The proposal IPM reduces the time complexity of a vanilla IPM from $O(N^3 m^4)$ to $O(N^2 m^3)$, where $N$ is the number of input measures and $m$ is the discretized support size. This is an acceleration of order $O(N m)$.

### Weaknesses
 ${\bf Experiment.}$ The numerical experiment scales in Section 4 are not large. For example, Fig. 2 shows up to $N=6000$ input measures supported on small size $m=50$, and $N=10$ input measures with each support up to $m=6000$ points. Either setup has limited applicability (e.g., low-resolution images, or a very small number of input point clouds). Due to the scaling $O(N^2 m^3)$, I see no reason why the algorithm can be scaled up for a reasonable experimental setup.

${\bf Convergence.}$ The paper claims super-linear convergence for the WBC objective function value (page 8, lines 427-429). However, I cannot see why the super-linear convergence rate in the objective value plot Fig. 3. A log-scale plot of objective value v.s. iteration number should be shown. Claim quadratic convergence consistent with (Ye, Guler, Tapia, Zhang, 1993) is unclear. A quadratic rate should be proved rigorous under certain assumptions in the WBC problem.

Writings of the paper seem to be rushed and many typos are present. Some examples:

-- page 3, line 108: m seems to be the support of WBC and m_i support of the i-th distribution.

-- page 3, line 117: Woodbury's equality (?) [reference link broken].

-- page 5, line 249: primal-duel -> primal-dual

-- page 5, line 258: duel -> dual

### Questions
I don't understand the equivalence between the WBC (2) and linear programming (LP) formulation (4). WBC solves an optimization problem $\min_{w, \Omega} \max_{t} \min_{\Pi^{(t)}} [...]$, where $\Pi^{(t)}$ is the coupling between the $t$-th input measure and the Wasserstein center. However, the LP solves a problem $\min_{w, \Omega} \min_{\Pi^{(t)}} \max_{t} [...]$. How was this exchange of the two inner optimization sub-problems achieved?

### Soundness
2

### Presentation
1

### Contribution
2
