# Near-Optimal Policy Identification in Robust Constrained Markov Decision Processes via Epigraph Form

- Decision: Accept
- Scores: 6, 3, 6, 8, 6

## Abstract
\looseness=-1
Designing a safe policy for uncertain environments is crucial in real-world control applications.
However, this challenge remains inadequately addressed within the Markov decision process (MDP) framework.
This paper presents the first algorithm capable of identifying a near-optimal policy in a robust constrained MDP (RCMDP), where an optimal policy minimizes cumulative cost while satisfying constraints in the worst-case scenario across a set of environments.
We first prove that the conventional Lagrangian max-min formulation with policy gradient methods can become trapped in suboptimal solutions by encountering a sum of conflicting gradients from the objective and constraint functions during its inner minimization problem.
To address this, we leverage the epigraph form of the RCMDP problem, which resolves the conflict by selecting a single gradient from either the objective or the constraints.
Building on the epigraph form, we propose a binary search algorithm with a policy gradient subroutine and prove that it identifies an $\varepsilon$-optimal policy in an RCMDP with $\tiO(\varepsilon^{-4})$ policy evaluations.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes the EpiRC-PGS algorithm for solving the robust constrained Markov Decision Process (RCMDP) problem and provides a theoretical proof for identifying an $\epsilon$-optimal policy. The paper first highlights the limitations of the traditional Lagrangian formulation in RCMDPs, introducing the epigraph form as a more effective approach for handling the policy optimization process. Finally, the authors present the EpiRC-PGS algorithm as a solution, which leverages the epigraph form to address RCMDPs effectively.

### Strengths
1. This paper identifies key limitations in traditional algorithms for robust constrained Markov Decision Processes (RCMDPs) and presents an innovative, streamlined approach to overcome these challenges. 
2. The shift to an epigraph form represents a significant advancement, simplifying the solution method and providing an effective framework for robust optimization. 
3. The empirical comparison highlights the practical effectiveness of EpiRC-PGS, showing its ability to achieve low-return, constraint-satisfying policies, making it an attractive solution in robust decision-making applications.

### Weaknesses
1. A key area for improvement is a more thorough analysis of the algorithm’s efficiency, especially in higher-dimensional state spaces. Specifically, the paper should address how the computational cost of the inner loop scales with the number of states, and whether the proposed method remains practical as the state space grows. The current analysis focuses on tabular settings, but it is unclear how the algorithm would perform when function approximation is required, which is often the case in real-world applications with high-dimensional state spaces.
2. While the $\epsilon$-optimality proof is solid, addressing any computational overhead in the inner loop for larger state spaces would enhance its applicability to real-world problems. The paper should provide a more detailed analysis of the computational complexity of the inner loop, and discuss potential strategies for mitigating its impact on the overall runtime. It would be beneficial to explore the practical implications of the double-loop structure, and whether it can be optimized for efficiency.

### Questions
Currently, experiments appear limited to low-dimensional cases. Extending tests to a more complex environment, like a two-dimensional space (e.g., velocity and distance in driving), could clarify if EpiRC-PGS maintains its time and space efficiency as complexity grows.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper reformulate robust constrained MDPs via epigraphical reformulation and propose a bisection algorithm to solve this problem.

### Strengths
- This paper addresses an important problem in the field of MDPs

- The idea of bisection search is interesting.

### Weaknesses
 - The writing is extremely confusing. For example line 205, it is not clear what does "Does pi^star \in...hold?" mean, given that the exact phrase was given in line 204. Also, there are many diamond-shape notation in the draft, and they should be typos.

- The idea, although is interesting, is very simple. The use of epigraphical reformulation is standard and not surprising and technical. The most technical part should be the evaluation of \Delta, but the proposed algorithm relies on existing methods to do this step. 

- The underlying idea of Algorithm 1 is not clear and the presentation is poor. 

- The convergence of the proposed algorithm is not fast, O(eps^-4), and there is no discuss on the complexity. 

- Experiments are not working on large-scale problems.

### Questions
See weaknesses.

- What do you mean by "is an unknown value" in Assumption 4?

- Algorithm 1, how do you set T?

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper aims to develop an algorithm to identify a near-optimal policy in Robust Constrained Markov Decision Processes (RCMDPs). RCMDPs aim to minimize cumulative costs while satisfying constraints in the worst-case scenarios. The authors note that conventional policy gradient approaches to the Lagrangian formulation for RCMDPs often get trapped in suboptimal solutions due to gradient conflicts. To address this, they propose using the epigraph form of the RCMDP problem, which circumvents these conflicts by optimizing the objective or the constraints individually. This approach allows the policy gradient to avoid local minima associated with conflicting gradients. They introduce the Epigraph Robust Constrained Policy Gradient Search (EpiRC-PGS) algorithm, a binary search-based method that iteratively refines policy selection, with theoretical guarantees to find an ε-optimal policy in RCMDPs.

### Strengths
1. Applying the epigraph form to RCMDPs is a novel solution to address gradient conflict issues that arise with traditional Lagrangian formulations. 

2. The authors offer theoretical proofs that guarantee the proposed algorithm’s convergence to an ε-optimal policy. 

3. The paper includes empirical evaluations across several RCMDP settings. The experiments show that the proposed EpiRC-PGS algorithm reliably converges to feasible and low-cost policies, significantly outperforming Lagrangian-based methods in robust settings.

### Weaknesses
1. The double-loop structure of the EpiRC-PGS algorithm, while effective, is computationally intensive. The paper mentions this as a limitation, suggesting that a single-loop alternative could improve efficiency, which is a potential area for improvement.

2. The algorithm’s effectiveness relies on the coverage of the initial distribution (Assumption 2). This assumption may not always hold, especially when the state space is large. The reliance on full coverage of the initial state distribution is a strong assumption that could limit the applicability of the algorithm in real-world scenarios where exploration is often incomplete. Furthermore, the paper does not provide a detailed analysis of how the algorithm's performance degrades with partial coverage, which is a critical aspect for practical use.

### Questions
1. How does the algorithm perform when Assumption 2 on the initial distribution is partially met but not fully satisfied? Would the relaxation of this assumption degrade the policy quality significantly?

2. Have alternative subgradient methods or other non-gradient-based approaches been considered for this epigraph-form RCMDP problem? If so, how do they compare with the EpiRC-PGS algorithm in terms of robustness and feasibility?

### Soundness
3

### Presentation
3

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
The paper present the first algorithm to solve Robust Constrained Markov Decision Process (RCMDP). The proposed algorithm achieves $\epsilon$-optimality with $\mathcal{O}(\epsilon^{-4})$ iteration complexity provided the uncertainty set is known apriori. The paper uses epigraph method which is different from the standard Lagrange approach used in the literature.

### Strengths
1. Good intuition and presentation.
2. Mathematically sound results.

### Weaknesses
 
**Minor Comments**

1. Assumption $5$ is used in Theorem $3$, however it appears later. Please correct it. 

**Major Comments**

1. To my understanding, this algorithm works if the uncertainty set is exactly characterized and known (otherwise, getting a subgradient evaluator might be difficult). However, one of the potential application of Robust MDP is to ensure that policies trained on an unknown model $P_0$ does not deviate too much if the actual model $P$ is close to the model $P_0$ in some sense. In this case, one can probably guess the shape of the uncertainty set but cannot fully characterize it since $P_0$ is unknown. For example, if $P$ lies in a ball of radius $r$ centered around $P_0$, then the shape of the uncertainty set is a high dimensional sphere but its centre, $P_0$ is unknown. Information about $P_0$ is available only through a simulator with model $P_0$. My question is: how can the proposed algorithm provide guarantees in such cases? If it cannot, then that should be highlighted in the abstract and introduction as a drawback.

### Questions
1. Please categorize the related works into two groups: one that assumes the uncertainty set is fully characterized apriori (see the weakness above) and others that do not. This will help readers put the work into context. 

2. What are the challenges in extending this result to the case where the uncertainty set is not fully known apriori?

3. Does the algorithm scale with the size of the state space? Does it scale with the size of the uncertainty set? Some comments on these should be provided in the paper.

4. What is the typical computational complexity to generate a subgradient estimate with $\mathcal{O}(\epsilon^2)$ error? Such complexities should be elaborated in the paper.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces Epigraph Robust Constrained Policy Gradient Search, an algorithm designed to identify near-optimal policies in RCMDPs. The epigraph form can address gradient conflicts and theoretical techniques of prior approaches, ensuring convergence to an 
$ϵ-optimal$ policy across uncertain environments while satisfying safety constraints.

### Strengths
This paper is well structured and written, it addresses the difficulties of applying existing CMDP algorithms in RCMDP by providing the first algorithm with theoretical performance guarantees for near-optimal policy identification. The proposed epigraph form effectively resolves gradient conflicts inherent in the Lagrangian formulation. They also include a toy example to show the challenges in RCMDP which makes the paper easy to follow and the empirical results demonstrate that EpiRC-PGS outperforms baselines in various RCMDP settings.

### Weaknesses
 The proposed algorithm’s double-loop structure may become computationally intensive in environments with high-dimensional action or state spaces, limiting real-time applicability.  The binary search within the inner loop, and the projection step in the policy update, are particularly concerning from a computational efficiency standpoint. These operations, repeated within the outer loop, could lead to significant overhead, especially as the number of iterations increases or the state/action spaces grow. Assumption 2 requires an initial distribution over all the states, which is impractical, especially in the RCMDP setting, since some states are unsafe. This assumption is particularly restrictive because it necessitates exploration of potentially unsafe regions of the state space, which is counterintuitive to the goals of robust control. Since the design of the algorithm is based on the monotonical property of $\Delta_b^*,$ it requires assumptions 3,4,5 to have accurate estimations. These assumptions, while necessary for the theoretical guarantees, may be difficult to satisfy in practice, as they require precise estimation of the robust policy evaluation and gradient, which can be challenging in complex or noisy environments. The empirical evaluation could benefit from complicated or additional real-world applications to validate the robustness in practical MDP scenarios. The current experiments, while demonstrating the algorithm's behavior, lack the complexity and realism to fully assess its performance in practical settings.

### Questions
In robust RL, sample complexity and convergence results typically depend on the gap between the transition kernels in the uncertainty set. Could the authors elaborate on how the results depend on this gap or specify which parts of the analysis are impacted by it?

### Soundness
4

### Presentation
3

### Contribution
3
