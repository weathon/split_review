# Decentralized Riemannian Conjugate Gradient Method on the Stiefel Manifold

- Decision: Accept
- Avg Score: 6.33
- Scores: 5, 6, 8

## Abstract
The conjugate gradient method is a crucial first-order optimization method that generally converges faster than the steepest descent method, and its computational cost is much lower than that of second-order methods.
However, while various types of conjugate gradient methods have been studied in Euclidean spaces and on Riemannian manifolds, there is little study for those in distributed scenarios.
This paper proposes a decentralized Riemannian conjugate gradient descent (DRCGD) method that aims at minimizing a global function over the Stiefel manifold. The optimization problem is distributed among a network of agents, where each agent is associated with a local function, and the communication between agents occurs over an undirected connected graph. Since the Stiefel manifold is a non-convex set, a global function is represented as a finite sum of possibly non-convex (but smooth) local functions. 
The proposed method is free from expensive Riemannian geometric operations such as retractions, exponential maps, and vector transports, thereby reducing the computational complexity required by each agent. To the best of our knowledge, DRCGD is the first decentralized Riemannian conjugate gradient algorithm to achieve global convergence over the Stiefel manifold.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a decentralized Riemannian conjugate gradient descent (DRCGD) algorithm for distributed optimization, and proves the global convergence of the algorithm. Compared with existing state-of-the-art algorithms, DRCGD uses a projection operator that searches the direction instead of retraction and vector transport, thus reducing computational costs. Through the simulation of eigenvalue problem, the paper shows that DRCGD has better performance than state-of-the-art algorithms.

### Strengths
originality and significance: This paper has good originality and significance since it presents the first decentralized Riemannian conjugate gradient descent (DRCGD) algorithm for distributed optimization and proves the global convergence of the algorithm.

quality: The proposed algorithm is supported by solid theory and verified by simulation.

clarity: The overall narrative logic of the article is clear.

### Weaknesses
1. There is still room for improvement in the clarity of the proof. Some symbols that appear in the convergence analysis section of the text, such as $g_{i,k+1}$, $\mathcal{N}$, and $C$, are not defined in the text. For instance, $g_{i,k+1}$ should be explicitly stated as the gradient of the local objective function at agent *i* for iteration *k+1*. Similarly, $\mathcal{N}$ likely refers to the neighborhood set of an agent, which should be formally defined. The constant *C* appears in the analysis without a clear explanation of its origin or relation to other parameters in the algorithm.

2. It seems that there are some assumptions about the step size $\alpha_{k}$ that are not mentioned in Assumption 3 about $\alpha_{k}$ in the body of the proof, such as the assumption about $\alpha_{k}$ in Lemma 2. This leads to unclear assumptions about $\alpha_{k}$. Specifically, Lemma 2 implies a boundedness condition on the step size that is not explicitly stated in Assumption 3. This omission could lead to confusion about the conditions required for convergence.

3. The measures mentioned in the simulation should converge towards 0, which is not well demonstrated in the experimental results. For example, the measures in Figure 3 tend to be constant after it drops to a certain level. This does not support the theoretical results very well. The discrepancy between the theoretical requirement of a diminishing step size and the use of a fixed step size in the simulation needs further investigation. The observed plateauing behavior suggests that the algorithm might not be converging to the optimal solution as expected.

4. The definition of doubly stochastic matrix seems to be $\sum_{i} x_{ij}=\sum_{i} x_{ij}=1$, which is different from the definition in Assumption 1. Assumption 1 appears to impose additional constraints beyond the standard definition, such as symmetry and specific eigenvalue properties. This difference should be clarified, and the rationale for the stricter definition should be provided.

### Questions
1. What is the definition of $x_{x}$ in Definition 3 (ii)?

2. It seems like there are many assumptions of the parameters such as $\alpha_{k}$. Are these assumptions easy to satisfy?

3. In this paper, the decreasing step size is used in the convergence proof, while the fixed step size is used in the simulation. Does this difference affect convergence?

4. What is the significance of the eigenvalue problem used in the simulation in real life?

5. In general, since the problems solved are the same, the convergence result of the distributed algorithm should be independent of the structure of the graph if the assumptions about the graph are satisfied. In Figure 3 of the simulation, the same algorithm seems to converge to different solutions under different graphs. Why did this happen?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper suggests an extension of conjugate gradient on Stiefel manifold for distributed setting and provides convergence guarantees for this algorithms. The approach is based mainly on the Xiaojing Zhu's original papers

### Strengths
The setting of decentralized optimisation is crucial in applied optimisation, and extending one of the most practically efficient algorthms to it is topical. Riemannian generality here requires carefull trheoretical justifications and proper choice of tools to prevent big computational complexity. Paper indeed propose a good solution for solving optimisation problems on Stiefel manifold.

### Weaknesses
Empirical study is not comprehensive: there was not presented a comparison of the proposed approach with alternatives. Besides, form of convergence guarantees is not exhaustive, because the rate of the convergence is not established. Theoretical framework is mostly inherited from Zhu's original papers, but that analysis does not allow providing guarantees on convergence rate, so does not this paper, which means that there were no significant extending of that framework.

### Questions
1. Typo in "Lemma 3 In Alogrithm"
2. What about time-varying case? Conidering the case of time-varying graph would be important for all-around extending CG for decentralised setting.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The conjugate gradient method, a critical first-order optimization technique, typically exhibits faster convergence compared to the steepest descent method and demands significantly lower computational resources than second-order methods. Nevertheless, despite extensive research on various forms of conjugate gradient methods in Euclidean spaces and Riemannian manifolds, there has been limited exploration of such methods in distributed scenarios. This paper introduces a novel approach called the Decentralized Riemannian Conjugate Gradient Descent (DRCGD) method, designed to minimize a global objective function defined on the Stiefel manifold. This optimization problem is distributed among a network of agents, each associated with a local function, with communication occurring over a connected, undirected graph. Global convergence of DRCGD over the Stiefel manifold is proved. Numerical experiments demonstrate the advantages and efficacy of the DRCGD approach.

### Strengths
The paper is well written: basic definitions of optimization on Riemannian manifolds are recalled and the proposed algorithm is well explained. Furthermore, the latter is quite simple and hence has a great practical interest. Classical conjugate gradients on Riemannian manifolds have much faster convergence compared to the plain Riemannian gradient descent. Hence, proposing a decentralised Riemannian conjugate gradient descent can be well received by the community. Moreover, the global convergence of the proposed algorithm is proved whereas it is far from being trivial. Finally, numerical experiments show a practical interest to the proposed method.

The paper is overall of great quality.

### Weaknesses
The claim 2 in the introduction as well as the section 4.1 are misleading. Indeed, the authors mention they don't use retraction or vector transport to reduce the computation. However, they use the orthogonal projection onto the Stiefel manifold, which is a retraction, and the othogonal projection onto the tangent space, which is a vector transport (see "Optimization on matrix manifolds" from Absil et al. 2008). This claim should be removed.

In section 4.2, the equation (20) is not clear since $T_{\alpha_k\eta_{i,k}^R}$ is not defined. Hence, it is hard to appreciate if this hypothesis is reasonable or not. Same thing for assumption 3 (iii).

The paper lacks an overview of the poof to get the global convergence. The different proofs are long and technical and an overview would help the reader.

The numerical experiments section lacks the presentation of DRDGD and DPRGD. It would be interesting to better understand the differences with the proposed method.

Several passages in the proofs are unclear. See the questions.

- Lemma 1, eq (24): how do you get second and third inequalities. For me, there is something wrong here.
- Theorem 2 is independent from the conjugate gradient. Is it new or is it a known result from a different paper?
- Theorem 2 assumes that $\eta_{i,k}=0$. In the proposed algorithm, you jointly do a gradient descent and average the iterates of the different nodes, hence $\eta_{i,k}\neq 0$. Can you comment this?
- After eq (31), you mention that $x_{i,k_0+1} \to x_{i,k_0}$. I don't understand at all this limit. Is it a mistake?
- Second inequality in eq (36), can you explain how do you get it?

Typos:
- Definition 3: (ii) $x_x$ is $0_x$.

Notations:
- $P_{St}$ and $P_M$ are the same.
- Section 4.2: $g_{i,k+1}$ is not introduced.

Assumption 1: usually a doubly stochastic matrix is defined with positive elements and row and columns that sum to 1. Can you comment how does it relate to your definition?
- Section 4.1: "The Riemanian gradient step with a unit step size, i.e., ..." is it a unit step size or a null/zero step size?
- Assumption 3 (iii): what is $T_{\alpha_k\eta_{i,k}^R}$ ?

### Questions
- Assumption 1: usually a doubly stochastic matrix is defined with positive elements and row and columns that sum to 1. Can you comment how does it relate to your definition?
- Section 4.1: "The Riemanian gradient step with a unit step size, i.e., ..." is it a unit step size or a null/zero step size?
- Assumption 3 (iii): what is $T_{alpha_k\eta_{i,k}^R$ ?

Proofs:
- Lemma 1, eq (24): how do you get second and third inequalities. For me, there is something wrong here.
- Theorem 2 is independent from the conjugate gradient. Is it new or is it a known result from a different paper?
- Theorem 2 assumes that $\eta_{i,k}=0$. In the proposed algorithm, you jointly do a gradient descent and average the iterates of the different nodes, hence $\eta_{i,k}\neq 0$. Can you comment this?
- After eq (31), you mention that $x_{i,k_0+1} \to x_{i,k_0}$. I don't understand at all this limit. Is it a mistake?
- Second inequality in eq (36), can you explain how do you get it?

Typos:
- Definition 3: (ii) $x_x$ is $0_x$.

Notations:
- $P_{St}$ and $P_M$ are the same.
- Section 4.2: $g_{i,k+1}$ is not introduced.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
