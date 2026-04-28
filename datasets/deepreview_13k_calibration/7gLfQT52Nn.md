# Proper Laplacian Representation Learning

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 6, 5, 6

## Abstract
The ability to learn good representations of states is essential for solving large reinforcement learning problems, where exploration, generalization, and transfer are particularly challenging. The \textit{Laplacian representation} is a promising approach to address these problems by inducing informative state encoding and intrinsic rewards for temporally-extended action discovery and reward shaping. To obtain the Laplacian representation one needs to compute the eigensystem of the graph Laplacian, which is often approximated through optimization objectives compatible with deep learning approaches. These approximations, however, depend on hyperparameters that are impossible to tune efficiently, converge to arbitrary rotations of the desired eigenvectors, and are unable to accurately recover the corresponding eigenvalues. In this paper we introduce a theoretically sound objective and corresponding optimization algorithm for approximating the Laplacian representation. Our approach naturally recovers both the true eigenvectors and eigenvalues while eliminating the hyperparameter dependence of previous approximations. We provide theoretical guarantees for our method and we show that those results translate empirically into robust learning~across~multiple~environments.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a method to approximate the true eigenvalues and eigenvectors of a graph Laplacian relying on an unconstrained max-min problem solved by gradient-based optimization. This can be used to learn good representations for the states in reinforcement learning problems. In the experiments, the efficiency of the method is demonstrated together with an ablation study.

### Strengths
- This is an interesting and novel approach to the challenging problem of unsupervised representation learning.
- The technical part of the paper seems to be solid and reasonable, but I have not verified the theoretical results in detail. 
- Both the theoretical results and the experiments support the claims.
- The paper is relatively well written.

### Weaknesses
I think that the proofs could have been in appendix and instead use the space for more examples, demonstrations, and clarifications.

Q1. While in the paper the approach focuses on the eigenvectors of the graph Laplacian, in the experiments it is used for finding eigenfunctions. I think that further information should be provided for the actual formulation/solution of this problem.
Q2. I find Corollary 1 and the paragraph above a bit unclear. Why does an optimum of (2) and (4) imply that the constraint must be violated?
Q3. Perhaps, an experiment to test the stability of the equilibrium with respect to permutations.
Q4. Why rotated eigenvectors do not provide a good representation?

### Questions
Q1. While in the paper the approach focuses on the eigenvectors of the graph Laplacian, in the experiments it is used for finding eigenfunctions. I think that further information should be provided for the actual formulation/solution of this problem.
Q2. I find Corollary 1 and the paragraph above a bit unclear. Why does an optimum of (2) and (4) imply that the constraint must be violated? 
Q3. Perhaps, an experiment to test the stability of the equilibrium with respect to permutations.
Q4. Why rotated eigenvectors do not provide a good representation?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
1: You are unable to assess this paper and have alerted the ACs to seek an opinion from different reviewers.

### Summary
In Graph Drawing Objective (GDO) and the generalized GDO, the optimization problem in Equation 1 and 3 are used to find the Laplacian representation, but this formulation allows symmetries, which lead to hyper-parameters that can lead to potential issues. The proposed method, Augmented Lagrangian Laplacian Objective (ALLO) in Equation 6, requires no hyper-parameters. In Theorem 1, they show a theoretical result on how there is a guarantee of the stability of the proposed objective function for finding Laplacian representations. The paper concludes with some experiments.

### Strengths
- interesting formulation and solution
- motivated problem
- having experiments

### Weaknesses
 - some parts (e.g., Section 1 and 2) are hard to follow

### Questions
- How do you compare the complexity of the proposed objective function optimization problem with previous cases?





---------------------------------------------
After the rebuttal: I appreciate the authors for their response. They fully addressed my question and I decided to keep my acceptance score.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper develops three methods for smoothing in state-space models (SSMs). The idea is to assume SSMs that are non-linear and avoid other assumptions like Gaussianity when using variational inference. The drivin gidea is to preserve the temporal structure in the variational proposal. This seems to lead to what is called exponential family dynamical systems, that it a double-looped (forward and backward) chain of markovian conditionals.

### Strengths
Having carefully checked the exponential family derivations, the parameterization, as well as the derived ELBOs, I feel that likely they are correct and well-founded on previous related work. The use of exponential families in this context, and particularly to build the factorization into markovian conditionals is definitely a strenght. The work itself is clear and concise on the details, also mentioning limitations and reasoning on why certain decisions are taken.

### Weaknesses
To me the paper has two main weaknesses:

[w1] — the paper is in general concise and thorough, but written in a way that the smoothing idea is kind of lost. Particularly, technical details jump in for solving issues of previous technical details (derivations begin at the beginning of pp. 2 and finish at the end of pp. 7). In that way, the paper loses quite a lot of space, and story on the general smoothing idea that authors want to solve (and in which way they want to solve it). The core motivation behind using exponential families to achieve a specific factorization is not immediately clear, and the reader is left to piece together the connection between the technical derivations and the high-level goal of smoothing. The paper dives into the mathematical details before fully establishing the need for this specific approach, making it difficult to appreciate the significance of the technical contributions. The narrative flow could be improved by first clearly articulating the challenges in smoothing for non-linear, non-Gaussian state-space models, and then demonstrating how the proposed exponential family approach addresses these challenges.

[w2] — the second concern to me is the limited results. Having derived long technical details, the manuscript should at least provide results proportional to the technical development. In my opinion, the evaluation of the model is somehow short (learning of two synthetic systems (pendulum and chaotic scenario) plus analysis on convergence). While the pendulum and chaotic system are reasonable starting points, the evaluation lacks depth and breadth. The paper does not explore the performance of the proposed methods on more complex, high-dimensional systems, or real-world datasets. Furthermore, the analysis of convergence is limited to a single plot, and does not provide a thorough investigation of the convergence properties of the proposed algorithms. A more comprehensive evaluation would include a wider range of datasets, a more detailed analysis of convergence rates, and a comparison with existing state-of-the-art smoothing techniques.

### Questions
Not technical questions

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a new method for approximating the graph Laplacian (and namely its eigenvectors) over a discrete state space. This paper builds off of the "graph drawing objective" (and "generalized graph drawing objective"), with the goal to eliminate hyperparameters in its optimization that have been shown to sensitively effect the output approximation of the graph Laplacian's eigenvectors. It achieves this goal with a reformulated minimax objective, and provides both theory and experiments to justify this novel objective.

### Strengths
- This is a very mathematically clear and concise paper. The objective of the paper is clear and well-presented (re-formulate the graph drawing objective with a smaller hyperparameter space), the solution is clearly presented (convert into a max-min game, in spirit as a replacement to these hyperparameters), and the theory is both mathematically sound and interpretable to understand why the max-min game here achieves the desired objective.
- While the proposed solution appears "simple" on paper, the theory and justification behind the method is both theoretically rich and clever, combining both a nice environment for theoreticians and a direct benefit for practitioners (less hyperparameters to tune alongside the rest of the system).

### Weaknesses
 - The primary limitation is my view is the lack of justification in the practical context. Experiments are only provided in very simple maze scenarios, and it is not demonstrated here (or in primary related work I saw) why, in practice, one would chose a Laplacian representation over a standard representation. Specifically, while the paper mentions applications like exploration and reward shaping, it does not provide concrete examples or experiments that show how this specific Laplacian representation outperforms other methods in these tasks. The experiments are limited to grid-world environments, which are useful for theoretical analysis but do not reflect the complexity of real-world RL problems. A more thorough justification would include experiments on more challenging environments and a comparison against standard state representations in practical RL tasks.
  - On a similar note, there lacks more thorough discussion on the stability of the now-induced minimax game. This likewise seems like something necessary in order to demonstrate practical utility of this framework, at least theoretically. While the paper establishes a stable equilibrium point, it does not analyze the convergence properties of the minimax optimization process. For example, it would be useful to understand the condition number of the Hessian of the objective function at the critical point, as this is directly related to the convergence rate and stability of the optimization. Furthermore, it would be beneficial to discuss how the choice of optimization algorithm (e.g., gradient descent, Adam) affects the practical stability of the minimax game, and how often one can expect to reach the stable equilibria in practice. This is crucial for understanding the practical trade-offs of casting the optimization as a minimax game, as such formulations can sometimes lead to unstable training dynamics.

### Questions
- As there are natural continuous analogs to the graph Laplacion in Euclidean spaces, I am curious how, at least in theory, this framework is extendible into continuous state and action spaces? What are the limitations in extending this theory to continuous settings?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good
