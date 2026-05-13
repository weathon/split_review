# DUET: Decentralized Bilevel Optimization without Lower-Level Strong Convexity

- Decision: Accept
- Scores: 6, 3, 6, 6

## Abstract
Decentralized bilevel optimization (DBO) provides a powerful framework for multi-agent systems to solve local bilevel tasks in a decentralized fashion without the need for a central server. 
However, most existing DBO methods rely on lower-level strong convexity (LLSC) to guarantee unique solutions and and a well-defined hypergradient for stationarity measure, hindering their applicability in many practical scenarios not satisfying LLSC. 
To overcome this limitation, we introduce a new single-loop DBO algorithm called diminishing quadratically-regularized bilevel decentralized optimization (DUET), which eliminates the need for LLSC by introducing a diminishing quadratic regularization to the lower-level (LL) objective. 
We show that DUET achieves an iteration complexity of  $O(1/T^{1-5p-\frac{11}{4}\tau})$ for approximate KKT-stationary point convergence under relaxed assumptions, where $p$ and $\tau $ are control parameters for LL learning rate and averaging, respectively.
In addition, our DUET algorithm incorporates gradient tracking to address data heterogeneity, a key challenge in DBO settings. 
To the best of our knowledge, this is the first work to tackle DBO without LLSC under decentralized settings with data heterogeneity.
Numerical experiments validate the theoretical findings and demonstrate the practical effectiveness of our proposed algorithms.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper addresses decentralized bilevel optimization (DBO) in multi-agent systems without relying on lower-level strong convexity (LLSC), a common but limiting assumption. The authors propose DUET, a novel single-loop algorithm that introduces diminishing quadratic regularization to the lower-level objective, thus bypassing the need for LLSC. DUET achieves convergence to an approximate KKT-stationary point with a defined iteration complexity and incorporates gradient tracking to handle data heterogeneity across agents. This work is the first to address DBO without LLSC in decentralized settings with heterogeneous data, with both theoretical analysis and numerical experiments supporting DUET’s effectiveness.

### Strengths
1 The paper is well-written, providing clear explanations in the methodology section where each step addresses specific challenges, along with comparisons to existing problems and methods.

2 The authors compare the convergence rate and other results, clearly demonstrating improvements over current methods.

3 They propose using approximate KKT stationarity as the convergence measure for DBO solution quality, offering a detailed analysis of the convergence rate based on this new measure, which will aid in further research on this topic.

### Weaknesses
1 The real-world data experiments are limited to decentralized meta-learning problems on the MNIST dataset, which I believe may not be sufficiently comprehensive.

### Questions
Could you provide experimental results on other problems or datasets? This would help further demonstrate the effectiveness of the proposed method.

### Soundness
3

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
This work presents a decentralized bilevel optimization (DBO) algorithm, termed DUET, designed to solve local bilevel tasks in multi-agent systems without requiring a central server. Unlike traditional DBO methods that rely on the lower-level strong convexity (LLSC) assumption to ensure unique solutions and a well-defined hypergradient, DUET eliminates the need for LLSC by introducing diminishing quadratic regularization to the lower-level objective.

### Strengths
1. A single-loop algorithm for LLSC-less DBO is proposed in this work.

2. The proposed algorithm can be used to handle the challenges of consensus errors in DBO with data heterogeneity.

### Weaknesses
After reading this work, I have some major concerns.

1. What is the need for this algorithm in the ML community? This question arises from two main points: 1) Although this work avoids the strong convexity assumption, it still relies on the convexity assumption, whereas objectives in ML are often non-convex. Could you provide additional theoretical analyses that do not depend on convexity assumptions? 2) This work emphasizes the deterministic setting of the algorithm. While the deterministic setting is indeed important in optimization, I am curious about the challenges in analyzing convergence rates under a stochastic setting in the proposed algorithm. In ML, stochastic gradient descent is far more commonly used than deterministic approaches.

2. The relaxed stationarity (KKT-stationarity) is employed in this work without adequate justification. It is essential to provide a clear rationale for this relaxation, as it may result in significantly different solutions compared to the original problem. The stationarity measures are somewhat different from the traditional bilevel optimization works.

3. In Corollary 2, in addition to discussing the number of communication rounds required for the proposed algorithm to converge, it is also essential to analyze the number of bits needed during this process. Can you provide some comparisons about the communication complexity between the proposed method with the existing distributed bilevel optimization methods in the experiments?

4. The experimental results are not sufficiently convincing, as only a limited set of results is provided. Additionally, the experiments are conducted on a small-scale distributed system with only a few clients. I have concerns about the scalability of the proposed method, especially given its deterministic setting. Specifically: 1) Could the authors provide additional experimental results on a larger-scale distributed system? 2) The tasks addressed in the experiments are quite limited. I am curious if the proposed algorithm can be applied to more complex tasks, such as bilevel NAS (e.g., DARTS).

### Questions
Please refer to the Weaknesses. Additionally, the readability of this work is quite poor, with an excessive number of notations. Could you improve the manuscript’s readability and overall presentation?

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
3

### Summary
To address the limitations of most existing decentralized bilevel optimization (DBO) methods, which predominantly rely on lower-level strong convexity (LLSC), this paper proposes a single-loop DBO algorithm named Diminishing Quadratically-Regularized Bilevel Decentralized Optimization (DUET). This algorithm circumvents the necessity for LLSC by incorporating a diminishing quadratic regularization into the lower-level objective. DUET achieves an iteration complexity of $\mathcal{O}(1/T^{1-5p-\frac{11}{4}\tau})$ for approximating KKT-stationary point convergence under more lenient assumptions, where $p$ and $\tau$ serve as control parameters for the lower-level learning rate and averaging, respectively. Additionally, DUET integrates gradient tracking to effectively tackle data heterogeneity, a significant hurdle in DBO scenarios.

### Strengths
1. This paper proposes DUET, a single-loop algorithm that integrates gradient tracking and consensus updates to avoid the computational complexity of conventional double-loop structure in bilevel optimization while ensuring convergence in decentralized settings with data heterogeneity, which is the first algorithm with provable convergence for DBO without LLSC.

2. Without gradient heterogeneity assumptions, the proposed algorithm overcomes the challenges of consensus errors in DBO with data heterogeneity, ensuring agents can synchronize their updates effectively without relying on LLSC.

### Weaknesses
1. My primary concern is the presentation of this paper. For instance:

1-1. It is imperative to delineate the feasible region for $p$ and $	au$ in line 81;

1-2. The definitions of communication costs and communication complexity must be elucidated in lines 105 and 117;

1-3. In line 138, it is noted that several methods exist which offer enhanced complexity solutions for simple bilevel problems, as evidenced by references [1, 2, 3, 4];

1-4. The formulation of the decentralized bilevel optimization problem should be introduced earlier in the paper, ideally in the Section introduction;

1-5. A precise definition of $\nabla \mathcal{L}$ is essential and should be provided in line 231. Furthermore, given that $\nabla \mathcal{L}$ is a matrix (since $x$ may be a matrix), it is crucial to specify the type of norm to be used (F-norm or 2-norm); moreover, similarly, the definition (vector or matrix) of $\nabla \Phi$ in line 347 is also important.

1-6. The definitions of $x_{i,t}$ and $y_{i,t}$ remain ambiguous in line 242. Here, I assume that these represent the vectors $x_{i}$ and $y_{i}$ at the $t$-th iteration;

1-7. The explanation of the solution $v_{i,\mu_t}^*(x_{i,t})$ to the linear system and the multiplier $v_t$ could potentially lead to confusion among readers. The notation $\mathbf{v}$ in $\mathbf{v}_{i,\mu_t}^*$ should be replaced with a different symbol, such as $\mathbf{s}$, to prevent ambiguity, especially since the main theorems (e.g., Theorem 3 and Lemma 1) involve both notations. The use of $\|\mathbf{v}_{i,t} - \mathbf{v}_{\mu_t}^*(\mathbf{x}_{i,t})\|$ to represent the approximation error of the dual parameter also makes this part difficult to follow.

1-8. The citation format in the References section is incorrect. For example, the second reference and the reference on line 557 lack the publication location of the article, while the reference on line 574 omits the article's page numbers. The references contain some other errors that require correction.

Typo:

1. line 402, "for all $k$" should be "for all $t$".

### Questions
1. The update mode of Algorithm 1 is similar to the algorithm of [5], so I want to know the distinctions between these two algorithms. Furthermore, I am curious about whether the step of updating the optimal multiplier mirrors the step of solving the linear system within the hypergradient, given that the descent direction for the multiplier $v$, as proposed in this paper, aligns closely with the gradient descent step used for solving the linear system in the hypergradient. Considering this, I question whether the assumption of boundedness concerning the multiplier $v$ and the resolution of the linear system presented in Theorem 3 can be consolidated into a singular assumption.

2. The rationale behind the utilization of the projection parameters $r_v^t$ and $r_y^t$ remains ambiguous (line 301).

3. The definitions of $\otimes$ and $\bar{\beta}, \bar{\mu}$ are not clearly articulated (lines 347 and 362).

4. To enhance the understanding of Theorem 5, a comparative analysis with other algorithms is recommended.

5. For other questions, please see the weaknesses above.


[5] Liu, Risheng, et al. "Towards extremely fast bilevel optimization with self-governed convergence guarantees." arxiv preprint arxiv:2205.10054 (2022).

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper considers decentralized bilevel optimization (DBO) without using lower-level strong convexity (LLSC). 

To tackle this problem, the authors first propose a novel convergence metric called LLSC-less convergence. On top of this, they propose DUET that uses local updates and gradient tracking based communication updates to solve the DBO problem. The authors further provide a rigorous theoretical analysis of DUET, and obtain a finite-time convergence analysis which reveals the number of communication rounds to find an eps-stationary point is O(eps^{-3.5}) and O(eps^{-2.5}) under different settings. Besides, the authors also provide an extension of their algorithm -- DSGT, in which an additional assumption, upper-level strong convexity, is imposed. Similar results are obtained for DSGT. 

Some numerical experiments are conducted to showcase the efficiency of the proposed algorithms over existing ones.

### Strengths
1. (Weaker assumptions) The assumptions used in the paper are standard and do not impose strong convexity in the lower-level problem.

2. (Novel metric) The authors propose a novel metric to characterize the convergence of DBO problems without LLSC.

### Weaknesses
1. (Novelty of the theory) Although the proposed metric and algorithm are novel, the analysis used to obtain the final convergence is quite standard in distributed optimization and bilevel optimization literature.

2. (Simple experiments with incomplete context) The experimental settings are relatively simple -- A Pedagogical Example and MNIST dataset are so simple that they may not well represent the non-convex nature of lower-level non-convexity in many bilevel optimization problems. Some important details about the experiments setup are missing -- for example it would be better if the architecture of the neural network in the meta learning experiments is reported, otherwise the readers need to go through the code to figure it out.

3. (Unclear Table 1) Most of the algorithms in Table 1 use the eps-stationary convergence metric while this paper uses LLSC-less. However, this is not directly visible in this table. Meanwhile, the centralized settings may be moved to the appendix, as this paper mainly focuses on the distributed setting.

4. (Misleading name) The name of the extended version of DUET, DSGT, might be a little misleading -- as it refers to distributed stochastic optimization with gradient tracking in the distributed optimization literature. It would be better if the authors could use another name for the extended version of their algorithm.

### Questions
1. Can the authors provide some insights on the lower bound of this problem? For example the current O(eps^{-2.5}) seems not to be optimal, and it would be interesting to study the lower bound of DBO under the LLSC-less metric.

2. Is it correct to claim the complexity results are O(eps^{-3.5}) and O(eps^{-2.5}) in Corollary 2 and 4? Technically speaking \tau cannot be 0 and thus the logic "\tau --> 0 leads to -3.5 and -2.5" complexity seems a little bit problematic.

### Soundness
2

### Presentation
2

### Contribution
2
