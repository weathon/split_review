# Long-Term Fairness in Reinforcement Learning with Bisimulation Metrics

- Decision: Reject
- Scores: 5, 5, 6, 6

## Abstract
Ensuring long-term fairness is crucial when developing automated decision making systems, specifically in dynamic and sequential environments. By maximizing their reward without consideration of fairness, AI agents can introduce disparities in their treatment of groups or individuals. In this paper, we establish the connection between bisimulation metrics and group fairness in reinforcement learning. We propose a novel approach that leverages bisimulation metrics to learn reward functions and observation dynamics, ensuring that learners treat groups fairly while reflecting the original problem. We demonstrate the effectiveness of our method in addressing disparities in sequential decision making problems through empirical evaluation on a standard fairness benchmark consisting of lending and college admission scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper studies fairness in reinforcement learning. The author(s) proposed bisimulation metrics to measure long-term fairness. These metrics were further minimized to learn the reward and transition function, based on which the estimated optimal policy is derived. The author(s) further conducted two numerical experiments, including a lending example and a college admission example to investigate the finite sample performance of their proposed method.

### Strengths
I summarize the strengths of the paper as follows:

* Although fairness has been widely studied in the machine learning literature, it has been less considered in RL, to my knowledge. In that sense, the problem formulation is relatively "original".
* The approach to ensuring fairness through optimizing bisimulation metrics is "original", to my knowledge. Existing work in RL typically imposes constraints to guarantee fairness. 
* The proposed $\pi$-bisimulation-guided reward shaping algorithm is "original", to the best of my knowledge.

### Weaknesses
I summarize the weaknesses of the paper as follows:

*   One of my major concern lies in the use of the $\pi$-bisimulation-guided approach for ensuring fairness in RL. In particular, the $\pi$-bisimulation metric in (3) is intended to identify equivalent states with same rewards and transition functions. Similarly, the revised $\pi$-bisimulation metric in (7) is intended to identify equivalent state-group pairs with same rewards and transition functions. In other words, if two groups have similar rewards and transition functions, imposing such a constraint is unnecessary as they inherently would achieve similar rewards and transition functions. Conversely, if the rewards and transitions differ between two groups, enforcing such a constraint to align them might result in approximations that differ substantially from their true values. Are there scenarios where deliberately modifying the reward/transition functions could lead to fairer outcomes without significantly compromising performance.

*   Definition 5 considers a fixed s between two groups. However, the proposed metrics optimize over different state-group pairs. It makes more sense to minimize across different groups while holding the states constant. Please clarify your reasoning for optimizing over different state-group pairs rather than fixing the state across groups.

*   Theorems 1 and 2 appear to be direct extensions of existing results. Theorem 3, on the other hand, is ambiguous. Specifically, Definition 5 involves a constant $\epsilon$. Please clarify which $\epsilon$ value would be attained by minimizing the proposed metric.

*   The presentation needs to be enhanced. At several places, it remains unclear to me how the proposed methodology is indeed implemented. For instance, on Page 4, the author(s) mentioned their proposal is to minimize Equation (7). However, it remains unclear what are the parameters being optimized. Similarly, in Algorithm 1, it remains unclear what is the definition of the parameter $\omega$ being optimized on Line 12 (see the Questions Section).

*   Current theories did not fully support the validity of the proposal. For instance, it can be seen from Algorithm 1 that the proposed algorithm is iterative in nature, which alternates between estimation of the reward and transition functions and learning of the optimal policy. Please clarify whether such an iterative algorithm would converge. 

*   The numerical example, particularly the college admission, appears superficial. Can you consider more realistic examples to more effectively evaluate the various algorithms?

*   Should $j^{\pi}$ in Definition 5 be $V^{\pi}$? This seems a typo.

### Questions
1. What does the "long-term fairness" mean? Why do you want to emphasize "long-term" in the title?
2. What parameters are being optimized when minimizing Equation (7)?
3. What is the definition and role of parameter $\omega$ in Algorithm 1?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work studies the problem of enforcing long-term fairness in reinforcement learning (RL). Unlike constrained optimization approaches, the authors propose an unconstrained policy optimization algorithm. This algorithm is inspired by the connection between bisimulation metrics and long-term DP fairness in RL. The authors analyze the proposed group-conditioned bisimulation metric and propose a practical algorithm to adjust the reward and observation dynamics to achieve long-term fairness. The effectiveness of the proposed algorithm is demonstrated through extensive numerical studies on two real-world case studies, comparing it with several baselines.

### Strengths
1.	The connection between bisimulation and long-term fairness in RL is a novel and insightful approach.
2.	The authors preform thorough numerical studies on two real-world lending and college admission scenarios, comparing their method against up-to-date baselines.

### Weaknesses
1.	The clarity of the writing could be improved by providing more details and explanations for certain aspects of the proposed method. See Question section.

### Questions
1.	In Definition 5 of DP fairness in RL, the difference inexpected returns is considered for the same state $s$ and different group variables $g_i, g_j$, while in Equation (6), the difference is considered for different state-group pairs $(s_i,g_i)$ and $(s_j,g_j)$. Could you elaborate on the relationship between these two equations?
2.	Please clarify whether the proposed method is applicable to offline or online RL settings. In Algorithm 1, is the dataset $\mathcal{D}$ collected through environment interaction or by using a bisimulator?
3.	Could you explain the role of $\omega$ in Line 12 of Algorithm 1?
4.	The authors could consider mentioning potential limitations of the proposed method.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents a fairness-aware RL approach to satisfy long-term group fairness by capturing behavioral similarities across different groups. The authors show that tuning the observable MDP by minimizing a policy-dependent Bisimulation metric automatically achieves demographic parity. This modified MDP is then leveraged to learn a fair policy using standard RL algorithms.

---------------------------
**Post-rebuttal:**

The rebuttal effectively addressed some of my concerns, and I thus increased my score. However, I still find the scope of the work to be somewhat limited.

### Strengths
The paper studies the important problem of long-term fairness, and proposes a novel and somewhat straightforward approach to address it. The authors establish a connection between Bisimulation relation/metric and demographic parity, and exploit this connection for unconstrained optimization of fair policies. Empirical results show better or on par performance of the approach compared to state-of-the-arts. Moreover, the availability of the code supports the reproducibility of these findings (disclaimer: I have not checked the implementation).

### Weaknesses
The proposed approach targets a specific class of problems and it is not clear, nor discussed, how it can be generalized/adapted to other problems and settings. The framework relies on a single measure of group fairness which limits its applicability to broader contexts. Particularly that recent literature suggest that individual fairness measures are better suited for fairness-aware learning compared to group-based metrics that are more compliant with statistical analysis. 

In addition, it is implicitly assumed that the original MDP is known by the approach which may be a strong requirement (e.g., that R^original(s,a) is given or the transitions are available to sample rollouts). This assumption and how the approach extends to problems with unknown MDPs are not fully discussed in the paper.

The authors claim that modifying the observable MDP occurs outside the RL training loop, so that the problem stays stationary. However, (batch) updates of the dynamics model are still in the main loop, making the policy dependent on the changing MDP, hence, suggesting an overall non-stationary setup.

While the implementation is provided in the supplementary materials, not all parts of the framework are clear. For instance, it would be helpful to discuss how the quantile matching works or whether the expectation in Eq. 7 applies to all possible state and groups or the same state in different groups? i.e., (s,g_i) and (s,g_j)? Also some information about the architecture/etc. would improve clarity.

The main advantage mentioned for modifying the observable MDP over constrained optimization is the ability to use existing RL algorithms. However, it’s not entirely evident how this is a significant benefit, especially given the approach’s limited flexibility in terms of fairness metrics.

Minor:
There are a few references to metrics that are adapted from supervised learning, which implies that metrics are algorithm-dependent. Why this is important?

Typo (line 131):  \tau_a(s’|s,g) should be \tau_a(s’|s,a,g).

The term co-optimization seems to be over-used, e.g., co-optimization of reward function in Sec. 4.1 or co-optimizing J_rew and J_dyn that are learned separately.

line(281-282): the approach is solely based on a single fairness measure, so it is NOT regardless of fairness measure used.

### Questions
Is it possible to extend this approach to accommodate different notion of fairness, and if yes, how?

It seems that the Bisimulation metric is defined for discrete state spaces; could you explain if that's the case and how it can be generalized to continuous spaces?

Would it be more intuitive to incorporate the sensitive attribute g as part of the state representation by redefining the state as  S x G, leaving the rest of the MDP and group-conditional definitions unchanged? Would this adjustment change the technical approach?

How the choice of baselines is justified if some of them optimize a different measure of fairness (like EO)? Will the comparisons be fair then?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a novel method for learning group-fair solutions in reinforcement learning (RL), addressing a limitation of standard deep RL approaches, which prioritize reward maximization over fairness considerations. The proposed method learns group-specific reward models and observation dynamics alongside the RL policy, using bisimulation metrics without modifying the core RL optimization process. Experiments in lending and college admission scenarios are presented that show the proposed method is comparable with considered baselines.

### Strengths
The paper presents a clear and well-structured approach to incorporating group-level fairness in RL.

The connection drawn between group fairness and bisimulation is both novel and thorough.

The paper introduces a practical implementation of their framework, incorporating algorithmic innovations that enable efficient computation.

The experimental results effectively demonstrate the method's ability to learn group fair solutions in two domains.

### Weaknesses
Despite the paper's compelling core idea, the empirical evaluation appears somewhat limited in scope, with only two relatively simple domains and discrete action spaces. I believe, incorporating more complex scenarios with multiple groups with conflicting nature would greatly improve the paper. Specifically, the current experiments do not adequately explore the method's behavior under conditions of high group cardinality, which is a critical aspect for real-world applicability. The use of only two groups in the lending and college admission scenarios does not fully demonstrate the method's ability to handle complex group dynamics and potential trade-offs in fairness across multiple protected attributes.

A detailed and thorough theoretical analysis is also lacking, particularly in terms of rigorously examining the properties of the proposed reward models and observation dynamics and their relationship to bisimulation metrics. The paper does not provide sufficient theoretical justification for why learning group-specific reward models and observation dynamics using bisimulation metrics will lead to long-term fairness. A more formal analysis of the convergence properties and the stability of the learned models would be beneficial. Furthermore, the paper lacks a theoretical connection between the learned bisimulation metrics and the desired fairness metrics, which makes it difficult to assess the theoretical guarantees of the proposed method.

The paper's organization could also be improved, with a formal definition of long-term fairness and clearer connections between bisimulation and fairness metrics. The current definition of long-term fairness is vague and lacks mathematical rigor. The connection between bisimulation and fairness metrics is not explicitly defined, and the paper does not clearly explain how bisimulation is used to achieve long-term fairness. The paper would benefit from a more formal treatment of these concepts, including explicit definitions and theorems that clearly establish the relationship between bisimulation and fairness.

### Questions
1. Could you provide a clear definition of long-term fairness in the context of your work? This definition is missing and should have been defined formally. 
2. How well would the proposed method perform in environments with more groups and actions? What are the theoretical and practical limitations in scaling the approach, and how might these be addressed?
3. Current results show DQN performing comparably or better than PPO, which contradicts common findings in the field. This pattern appears in both standard implementations and when combined with bisimulation. Could you explain this unexpected behavior, and is it possibly related to hyperparameter tuning?
4. How does your approach compare to welfare-based RL methods[1-5]? Specifically, wouldn't egalitarian or lexicographic egalitarian welfare functions, which maximize the minimum group utility, achieve similar goals in reducing recall and credit gaps?
5. Regarding the implementation details, how do you handle the optimization ordering between reward and observation dynamics models (assuming they're represented by neural networks)? Does the optimization order impact performance? Could you specify which gradient-free optimization method was employed?

[1] Cousins, Cyrus, Kavosh Asadi, and Michael L. Littman. "Fair E3: Efficient welfare-centric fair reinforcement learning." 5th Multidisciplinary Conference on Reinforcement Learning and Decision Making. RLDM. 2022.

[2]Siddique, Umer, Paul Weng, and Matthieu Zimmer. "Learning fair policies in multi-objective (deep) reinforcement learning with average and discounted rewards." International Conference on Machine Learning. PMLR, 2020.

[3] Zimmer, Matthieu, et al. "Learning fair policies in decentralized cooperative multi-agent reinforcement learning." International Conference on Machine Learning. PMLR, 2021.

[4] Fan, Zimeng, et al. "Welfare and fairness in multi-objective reinforcement learning." arXiv preprint arXiv:2212.01382 (2022).

[5] Cousins, Cyrus, et al. "On Welfare-Centric Fair Reinforcement Learning."

### Soundness
3

### Presentation
3

### Contribution
2
