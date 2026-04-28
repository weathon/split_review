# Beyond Stationarity: Convergence Analysis of Stochastic Softmax Policy Gradient Methods

- Decision: Accept
- Avg Score: 7.33
- Scores: 8, 8, 6

## Abstract
Markov Decision Processes (MDPs) are a formal framework for modeling and solving sequential decision-making problems. In finite-time horizons such problems are relevant for instance for optimal stopping or specific supply chain problems, but also in the training of large language models. In contrast to infinite horizon MDPs optimal policies are not stationary, policies must be learned for every single epoch. In practice all parameters are often trained simultaneously, ignoring the inherent structure suggested by dynamic programming. This paper introduces a combination of dynamic programming and policy gradient called dynamic policy gradient, where the parameters are trained backwards in time. 
   
   For the tabular softmax parametrisation we carry out the convergence analysis for simultaneous and dynamic policy gradient towards global optima, both in the exact and sampled gradient settings without regularisation. It turns out that the use of dynamic policy gradient training much better exploits the structure of finite-time problems which is reflected in improved convergence bounds.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposed a policy gradient algorithm for finite-horizon MDPs that are trained backward, for the benefit of explicit constant dependence in convergence guarantees and faster convergence behavior comparing to policy gradient methods that are trained simultaneously.

### Strengths
The idea of using dynamic programming related idea to capture the structure of finite-horizon MDPs to improve efficiency of policy gradient algorithms is interesting, and the convergence guarantees with explicit constants are established with accompanying experiments.

### Weaknesses
More comparisons with state-of-the-art policy gradient methods for tabular finite-horizon MDPs could have been presented to increase the convincingness of the example. It should be clearly stated why unregularized softmax is interesting to analyze by itself given the volume of past works on softmax PG and mirror descent methods.

- For simultaneous PG analysis of unregularized softmax, you claimed that you are the first to analyze the global convergence rate. However, there are a number of works that study convergence rate and sample complexity for stochastic policy mirror descent, which is a more general algorithmic framework that encompass softmax as a special case [1].
- Given the plethora of works on softmax policy gradient in the tabular case and discussions on its limitations [2], what would be practical benefits of using softmax aside from the fact that it gives rise an unconstrained optimization problem?
- In the unregularized MDP problem the optimal policy can be deterministic, in which case softmax parametrization does not cover all the possible policies and therefore is incomplete. Can you elaborate on the benefit of using an incomplete policy class in the tabular case here?
- Is it possible to compare with Guo et al. 2022 (appeared in original reference list of the paper) performance numerically?

### Questions
- For simultaneous PG analysis of unregularized softmax, you claimed that you are the first to analyze the global convergence rate. However, there are a number of works that study convergence rate and sample complexity for stochastic policy mirror descent, which is a more general algorithmic framework that encompass softmax as a special case [1].
- Given the plethora of works on softmax policy gradient in the tabular case and discussions on its limitations [2], what would be practical benefits of using softmax aside from the fact that it gives rise an unconstrained optimization problem?
- In the unregularized MDP problem the optimal policy can be deterministic, in which case softmax parametrization does not cover all the possible policies and therefore is incomplete. Can you elaborate on the benefit of using an incomplete policy class in the tabular case here?
- Is it possible to compare with Guo et al. 2022 (appeared in original reference list of the paper) performance numerically?


[1] Alfano, Carlo, Rui Yuan, and Patrick Rebeschini. "A novel framework for policy mirror descent with general parametrization and linear convergence." arXiv preprint arXiv:2301.13139.
[2] Li, Gen, Yuting Wei, Yuejie Chi, Yuantao Gu, and Yuxin Chen. "Softmax policy gradient methods can take exponential time to converge." In Conference on Learning Theory, pp. 3107-3110. PMLR, 2021.

-----------

Post-rebuttal: I thank the authors for their clarification and agree that unregularized softmax would be of interest for theoretical analysis. I personally disagreed with the statement in the paper "...very little is known about convergence to global optima even in the discounted case" per the discussion before. I have increased my score.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This manuscript delves into the convergence characteristics of policy gradient (PG) methodologies utilizing softmax policies within the context of MDPs that have a finite horizon, denoted as $H$. A prevalent approach to implementing PG methods in finite horizon scenarios involves augmenting the state space with a temporal coordinate, subsequently training across all epochs in a simultaneous fashion. The authors have extended the convergence analysis techniques from [Agarwal et al., 2021; Mei et al., 2020], originally applied to gradient ascent algorithms with exact gradients in infinite MDPs, to the domain of simultaneous PG with exact gradients for finite horizon MDPs. This adaptation has yielded a global convergence rate of $O(H^5)$. Building upon this, the paper introduces an innovative algorithm that synergizes PG with dynamic programming, termed as dynamic PG, which notably enhances the global convergence rate of simultaneous PG to $O(H^3)$. Finally, the authors extended their findings to encompass scenarios where a stochastic gradient is utilized instead of an exact gradient.

### Strengths
I believe this paper is comprehensively developed and presents a balanced view on the topic at hand. Despite the intricate nature of the subject, the paper is articulately written, ensuring clarity and ease of understanding for the readers. While I have not had the opportunity to delve into Appendix C, I feel reasonably assured about the soundness of the proofs presented in the rest of the document. To me, the concept of backward updating stands out as the most intriguing aspect of this paper, marking a novel application of this technique in proving global convergence, something I have not encountered in previous papers proving global convergence result for MDPs.

### Weaknesses
The only limitation I can think of is the limited experimental results; however, this is understandable given its theoretical nature.

### Questions
Correct me if I'm wrong, my intuition is that since dynamic PG is fixing policy from $h+1$ onward, it can be viewed as a specific coordinate ascent algorithm. Do you see any way to use the backward update idea for infinite horizon non-stationary MDPs?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a thorough investigation of policy gradient (PG) methods applied to finite-horizon Markov Decision Processes (MDPs). The authors introduce two PG methods: the conventional simultaneous PG and a novel dynamic PG. The convergence of these methods is mathematically proven by leveraging two key factors: (1) the smoothness property inherent in finite-horizon MDPs, and (2) the gradient dominance condition. Furthermore, the authors extend their analysis to the model-free setting, proposing two stochastic PG methods with proven convergence analysis.

### Strengths
This paper is easy to follow. The dynamic gradient method proposed is new to finite-horizon MDP, and it is complimented by strong theoretical guarantees, while the smoothness property and the gradient dominance condition existing in infinite-horizon MDPs' literature are adopted into the finite-horizon case. Meanwhile, the paper also considers the character of the coefficient $\inf_{n}\min_{s\in\mathcal{S}}\pi^{\theta}(a^{\star}(s)|s)$ and further shows how to determine its lower bound, which is a new insight. 

To address the model-free setting, the authors introduce two related stochastic PG methods with proven convergence results. In their comparison, both dynamic PG and stochastic dynamic PG take less steps than their counterparts.

### Weaknesses
One reason for not giving a higher score at this point is that the global convergence results and their analysis are actually not that surprising. As mentioned in the paper, all proofs of convergence behaviors follow the idea of the smoothness property and the gradient dominance condition, which are well used especially in [1]. While they are adopted in the finite-horizon MDP, it would surely help if the authors could discuss more about the technical challenges of the analysis. Specifically, the paper could benefit from a deeper discussion on how the finite-horizon setting necessitates modifications to the smoothness and gradient dominance arguments, and what specific challenges arise when applying these concepts in a non-stationary environment. The paper should also clarify the specific differences in the analysis compared to the infinite-horizon case, beyond just stating it's an adaptation.

Furthermore, the discussion on motivation in the paper appears to be somewhat weak. It would be beneficial to include a more comprehensive review of relevant literature to emphasize the significance and importance of studying finite-horizon MDPs. For example, the paper could discuss the practical relevance of finite-horizon MDPs in real-world scenarios, such as robotics or resource management, where the planning horizon is inherently limited. The current introduction does not adequately highlight the unique challenges and benefits of focusing on the finite-horizon setting, especially compared to the more commonly studied infinite-horizon case.

### Questions
The proofs make sense to me. I have the following minor questions:

1. As mentioned above, it would be nice if the authors could further describe the technical challenges of establishing the convergence results.

2. Why does the term '$\exists s \in\mathcal{S}$' exist in the equation of Theorem 4.2? It seems the result of Theorem 4.2 is weaker.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
