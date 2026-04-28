# Block Coordinate Descent Methods for Optimization under J-Orthogonality Constraints with Applications

- Decision: Reject
- Avg Score: 4.25
- Scores: 5, 3, 3, 6

## Abstract
The J-orthogonal matrix, also referred to as the hyperbolic orthogonal matrix, is a class of special orthogonal matrix in hyperbolic space, notable for its advantageous properties. These matrices are integral to optimization under J-orthogonal constraints, which have widespread applications in statistical learning and data science. However, addressing these problems is generally challenging due to their non-convex nature and the computational intensity of the constraints. Currently, algorithms for tackling these challenges are limited. This paper introduces \textbf{JOBCD}, a novel Block Coordinate Descent method designed to address optimizations with J-orthogonality constraints. We explore two specific variants of \textbf{JOBCD}: one based on a Gauss-Seidel strategy (\textbf{GS-JOBCD}), the other on a variance-reduced and Jacobi strategy (\textbf{VR-J-JOBCD}). Notably, leveraging the parallel framework of a Jacobi strategy, \textbf{VR-J-JOBCD} integrates variance reduction techniques to decrease oracle complexity in the minimization of finite-sum functions. For both \textbf{GS-JOBCD} and \textbf{VR-J-JOBCD}, we establish the oracle complexity under mild conditions and strong limit-point convergence results under the Kurdyka-Lojasiewicz inequality. To demonstrate the effectiveness of our method, we conduct experiments on hyperbolic eigenvalue problems, hyperbolic structural probe problems, and the ultrahyperbolic knowledge graph embedding problem. Extensive experiments using both real-world and synthetic data demonstrate that \textbf{JOBCD} consistently outperforms state-of-the-art solutions, by large margins.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper focuses on one special optimization problem with J-orthogonal constraints, a generalized version of orthogonality into signature matrix $J= X^TJX$. They provide a method based on the Block Coordinate Descent (BCD) with two variants: the Gauss-Seidel strategy (GS-JOBCD) and variance-reduced and Jacobi strategy (VR-J-JOBCD). They showed complexity and convergence analyses for both variants. They numerically tested their method on real-world and synthetic datasets.

### Strengths
Pros:

1. They provide a BCD algorithm that is specially designed for J-orthogonal constraints.

2. They offered complete optimality and convergence analyses.

3. The experiment result is interesting, but the baselines are slightly debatable. (Is there any other STOA in these certain applications?)

### Weaknesses
Cons:

1. The main concern is the significance of their applications where the reviewer does not find a special significance for a more general area.

2. When they claimed stronger stationary points than the baselines method due to their special design on the J-orthogonal constraints. They are using the standard ADMM and Unconstrained Multiplier Correction Method (UMCM), which are not necessarily tailored to their problem. Especially as far as the reviewer has known, it's wired to see that BCD significantly outperformed ADMM, since they can both guarantee convergence to a stationary point. In general, BCD is not a lightweight algorithm, the experience is ADMM usually more stable and maybe faster. Could the author further clarify the following questions:

a. Could the authors please provide a more detailed theoretical comparison of the convergence properties of their BCD method vs ADMM specifically for problems with J-orthogonal constraints?

b. Could the author please provide more empirical convergence plots comparing BCD and ADMM across different problem instances to better understand when/why BCD outperforms ADMM?

c. Could the authors please implement a version of ADMM that is more tailored to J-orthogonal constraints as a stronger baseline? Or any other SOTA methods can be applied.

d. Could the authors please discuss potential reasons why BCD may be better suited for J-orthogonality constraints compared to general ADMM? For example, provide the theoretical comparison of the complexity bounds between their methods and the baselines.

3. For the complexity part, it would be suggested to add an analysis for baselines to explain why it outperforms the baselines so much in certain settings.

a. Is there any detailed complexity analysis for the baseline methods (ADMM and UMCM) in addition to their proposed methods?

b. Could the author please discuss specific problem characteristics or settings where their methods are expected to have lower complexity and verify these expectations empirically?

### Questions
Please address the questions in the weakness part.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper considers solving an optimization problem over the set of J-orthogonal matrices (the set of $X^T J X = J$ where $J$ is an $n\times n$ diagonal matrix with $\pm 1$s), where the objective might consist of a finite sum of losses (i.e. empirical risk minimization) or a single loss. The paper proposes two methods for solving this problem: ** GS-JOBCD ** based on Gauss-Seidel strategy and its extension: **VR-J-JOBCD** based on variance reduction with Jacobi strategy. 

The main technical innovation of the paper is based on the observation, that when only two rows are updated at once, it is possible to provide a closed form solution for the optimal update. The second algorithm, VR-J-JOBCD, can then apply this strategy on randomly chosen pairs of row indices in parallel.

### Strengths
The idea of using (block) coordinate descent for hyperbolic J-orthogonal manifold is novel as far as I know. Also the concept of an update that does pair-wise rotations coordinates is new. The paper also provides many numerical experiments.

### Weaknesses
 * It is not clear if JOBCD represents a fundamentally new algorithmic framework or if it is a modification of existing block coordinate descent methods or Riem. coordinate descent tailored for J-orthogonal constraints. In particular, the work is very similiar to the work of (Ganzhao; A block coordinate descent method for nonsmooth composite optimization under orthogonality constraints). Although there is a comparison with this work, the main idea in both of these (pairwise index update) is the same.
* The convergence results are stated without enough detail, e.g., without discussing the individual constants.
* The algorithm needs the knowledge of the probability $p$ for the VR to work, this might not be realistic.

### Questions
* What is the impact of choosing suboptimal $p$ in the VR strategy?

### Soundness
2

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
5

### Summary
The paper introduces a block coordinate descent framework named JOBCD to address optimization problems subject to J-orthogonality constraints. The authors propose two variants of JOBCD: GS-JOBCD, based on a Gauss-Seidel strategy, and VR-J-JOBCD, which incorporates variance reduction and a Jacobi strategy. The paper establishes the oracle complexity and strong limit-point convergence results for both algorithms. Extensive experiments demonstrate the effectiveness and efficiency of JOBCD.

### Strengths
The framework tailored for the specific structure of the J-orthogonality constraint is interesting, which updates on a low-dimensional space in each iteration. The proposed algorithms also exhibit good scalability. Additionally, the paper is theoretically grounded, and numerical experiments validate the effectiveness and efficiency of the framework.

### Weaknesses
1. The paper does not specify the motivations of the study, leaving the reader unclear about the overall impact. Specifically, it is noted in line 95 that "all the aforementioned methods solely identify critical points". However, the theory developed in this work only guarantees convergence to first-order stationary points as well. Additionally, the authors state the unconstrained multiplier correction Methods are "efficient", and the ADMM-based methods are "widely adopted". The discussion suggests that existing work appears to be good enough, and thus weakens the motivation of the authors' study. It would be beneficial to point out the disadvantages of the mentioned work, which are addressed by the proposed JOBCD.
2. The novelty of this work seems limited. An array of work has generalized the coordinate descent framework to Stiefel manifolds, e.g., [1,2,3,4], among which [4] also allows to update two rows per iteration. Additionally, the optimization problems on the symplectic Stiefel manifold have also been well-studied, e.g., [5]. To alleviate the concerns, the authors should clarify the challenges of generalizing the BCD method from the orthogonality constraint to the J-orthogonality constraint, and essentially, identify the difference between the symplecticity constraint [5] and the J-orthogonality constraint.
3. The readability should be significantly improved. For instance, all the algorithm names and matrix notation are formatted in bold throughout the manuscript, which makes the text overwhelming and departs from the article's main points. In addition, there are some typos (see Questions).

### Questions
1. The complexity developed in Theorem 4.6 hides the dependency on the problem dimension $n$. The proposed GS-JOBCD updates two rows per iteration (only $2/n$ of the variables), which will result in a trade-off between efficiency and convergence rate. Could the authors provide the dependency on $n$ explicitly in the main text?
2. The inequality (10) serves as an $n/2$-step extension of the inequality (3), and accordingly, the VR-J-JOBCD collects $n/2$ steps of JOBCD as one iteration. As stated by line 298, the inequality (3) is not adopted as the surrogate in stochastic settings, for which the presentation of (10) seems tedious.
3. Typos. In equality (6), the "$\in$" should be "$\subseteq$"; in line 420, the "Proposition 4.8" is not formulated.



If the response addresses the concerns, I would like to change the grade.


[1] Coordinate descent without coordinates: Tangent subspace descent on Riemannian manifolds. MOR, 2023

[2] A block coordinate descent method for nonsmooth composite optimization under orthogonality constraints. 2023

[3] Riemannian coordinate descent algorithms on matrix manifolds. ICML, 2024

[4] Randomized submanifold subgradient method for optimization over Stiefel manifolds. 2024

[5] Riemannian optimization on the symplectic Stiefel manifold. 2021

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper extends the findings in [52] to the J-orthogonal (hyperbolic orthogonal) case. A new algorithm, JOBCD, is introduced along with a convergence analysis. The authors further develop two JOBCD variants: GS-JOBCD and VR-J-JOBCD which enhance robustness in convergence and efficiency, respectively. Finally, numerical simulations are provided to support the theoretical insights of their study. I would be open to raising my score if the authors can address certain issues I’ve mentioned.

### Strengths
The idea makes sense and the problem is of interest to the community. The technical contribution is solid: the authors employed the majorization-minimization method to develop a majorization function for the original forms under hyperbolic orthogonal constraints. They then analyzed the optimal solution of this majorization function, simplifying the hyperbolic orthogonal constraints to the standard orthogonal case as detailed in Proposition 2.2.

### Weaknesses
A detailed comparison with [52] would be valuable to better understand the technical challenges posed by the gap between hyperbolic orthogonal and standard orthogonal constraints. I’m also curious about whether the hyperbolic orthogonal constraints will impact the convergence rate compared to [52]. Specifically, the paper would benefit from a more in-depth discussion on how the indefinite metric in the J-orthogonal constraint affects the optimization landscape, potentially leading to saddle points or local minima that are not present in standard orthogonal optimization. Furthermore, it is unclear how the block coordinate descent approach handles the non-compact nature of the hyperbolic orthogonal group, which could lead to numerical instability or slower convergence. The analysis should also explore the impact of different choices of the matrix J on the performance of the proposed algorithms, as the structure of J directly influences the geometry of the constraint set.

### Questions
See weakness.

### Soundness
3

### Presentation
3

### Contribution
2
