# Addressing Extrapolation Error in Multi-Agent Reinforcement Learning

- Decision: Reject
- Scores: 3, 6, 3

## Abstract
Cooperative Multi-Agent Reinforcement Learning (MARL) has become a critical tool for addressing complex real-world problems. 
However, scalability remains a significant challenge due to the exponentially growing joint action space. 
In our analysis, we highlight a critical but often overlooked issue: **extrapolation error**, which arises when unseen state-action pairs are inaccurately assigned unrealistic values, severely affecting performance. 
We demonstrate that the success of value factorization methods can be largely attributed to their ability to mitigate this error. 
Building on this insight, we introduce multi-step bootstrapping and ensemble techniques to further reduce extrapolation errors, showing that straightforward modifications can lead to substantial performance improvements. Our findings underscore the importance of recognizing extrapolation error in MARL and highlight the potential of exploring simpler methods to advance the field.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper addresses the challenge of extrapolation errors in multi-agent reinforcement learning (MARL), focusing on the issue caused by the large joint action space. To mitigate these issues, the authors propose the application of modified multi-step bootstrapping and ensemble TD target techniques, aiming to enhance learning stability and reduce prediction variance. These proposed solutions are supported by theoretical analysis that explains the propagation of extrapolation errors and the importance of ensuring consistent value estimation. Empirical results validate these approaches, demonstrating that they contribute to improved performance and more stable training in various MARL scenarios.

### Strengths
- Insightful Theoretical Analysis: The theoretical framework helps illustrate the propagation of extrapolation errors and lays a foundation for understanding the importance of stable value estimation in MARL.
- The proposed methods, including multi-step bootstrapping and ensemble TD targets, are backed by experiments showing improved performance and stability over baseline approaches in MARL settings, demonstrating their utility in practice.
- The paper highlights the extrapolation errors in MARL and proposes practical solutions to mitigate this challenge, contributing to a better understanding and partial resolution of this important problem.

### Weaknesses
 - Fundamental Limitations of Value Factorization: Although the paper claims that the success of value factorization methods is largely due to their ability to mitigate extrapolation errors (as noted in the abstract), this mitigation is not comprehensive. The approach simplifies the estimation by focusing on local utilities, but it may fail to capture the full complexity of joint action spaces. An agent’s action value can vary significantly when combined with other agents’ actions, leading to potential suboptimal solutions. While this method improves learning stability, as further discussed in Sections 3.1 and 3.2, it does not fully address the diverse combinations and dependencies between agents, which are critical for optimal policy learning in MARL. Specifically, the method does not account for situations where an agent's optimal action is contingent on the actions of other agents, potentially leading to a convergence to a suboptimal Nash equilibrium. The factorization assumes independence that is often not present in complex multi-agent scenarios, and the paper does not adequately address how this assumption impacts the overall solution quality.
- Incremental and Limited MARL-Specific Solutions: The proposed methods, while addressing the large joint action space, primarily adapt existing techniques like multi-step bootstrapping and ensemble TD targets. These approaches lack innovation and do not sufficiently consider agent interactions, a key aspect of MARL. This results in simplified solutions that may fall short in effectively handling complex, cooperative scenarios, limiting their overall impact and applicability. The paper does not offer a novel mechanism for handling the specific challenges of multi-agent coordination, such as communication or joint planning, which are crucial for achieving optimal performance in complex MARL environments. The modifications to existing techniques, while helpful, do not fundamentally address the core issues of agent interdependence and coordination.

### Questions
While the paper notes that value factorization mitigates extrapolation errors, how does the method address the potential suboptimality caused by not fully capturing the complexity of joint action interactions among agents? Are there plans to extend the method to better account for agent dependencies and interaction effects?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors discuss and provide an analysis on the extrapolation error in Multi-Agent Reinforcement Learning (MARL), and show that value factorisation methods, like QMIX, can help reduce this error. Furthermore, they propose two methods to reduce extrapolation error in MARL, specifically multi-step bootstrapping and using ensembled independent value functions. The authors show that these methods can improve the performance of QMIX, in SMAC, SMACv2 and Google Research Football (GRF) environments, and of on-policy MARL algorithms like MADDPG and FACMAC on SMAC.

### Strengths
- The paper is well-written, clear and easy to follow.
- Extrapolation error, especially in online MARL, is a relatively unexplored area. This paper appears to be among the first to address this issue, providing both an analysis and methods to mitigate it.
- The paper provides a relevant discussion on the propagation of extrapolation error in MARL and how value factorization methods can help reduce it. Building on this analysis, the authors introduce targeted modifications to reduce the bias and variance associated with extrapolation error, with results showing consistent performance improvements across different environments and algorithms. Additionally, ablation studies on ensemble size and the $\lambda$ annealing parameter are included.

### Weaknesses
 - The experiment section is not very detailed. The authors should provide more information on the experimental setup, including how many seeds were run, the evaluation procedure and the evaluation interval. Furthermore, the main results presented in Table 1 don't include the standard deviation, which is important to understand the significance of the results.
- Although the authors provide results in three environments, two of them are SMAC and SMACv2, which might share some similarities. It might be more informative to use a different environment to SMACv1. 
- It is unclear if parameter sharing is used in the baseline algorithms. If it is, then the proposed ensemble method would result in many more learnable parameters. This could be a potential source of the improvement in the results, especially since when using smaller ensembles ($M=1,2$) in Figure 5b, performance is worse than the QMIX baseline. It would be important to disentangle the effect of increased capacity and extrapolation error mitigation.

### Questions
1. Was parameter sharing used in the baselines?  
2. What is the comparison of the parameter counts across the baseline and proposed modifications? How does this scale as the number of agents increase?
3. Could the authors specify the experiment details as discussed in the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper discusses extrapolation error in multi-agent reinforcement learning (MARL). The authors show that extrapolation error is a critical issue in MARL, affecting performance due to propagation from unseen state-action pairs, especially when the action space is large, as is often the case in MARL. Instead of proposing a new algorithm, the authors introduce two existing techniques, annealed multi-step bootstrapping and ensembled TD targets, to mitigate extrapolation error. The proposed method is tested across three domains: SMAC, GRF and SMACv2. The results show that the two simple modifications to existing methods can lead to significant performance improvements.

### Strengths
- Extrapolation error in MARL is a natural extension of the single-agent case to the multi-agent case, which is reasonable. 
- The improved method is tested across three domains on numerous maps, which is commendable.

### Weaknesses
 - Lack of novelty. Although the paper does not introduce new techniques or methods, I would not consider this a lack of novelty. The lack of novelty in this paper lies in its discussion of extrapolation error, which does not offer anything new. Extrapolation error is a commonly discussed topic in single-agent RL and naturally extends to MARL, which is acceptable. However, the authors do not provide new insights or discussions about challenges specific to MARL. Most of the content is similar to the single-agent case. It feels more like stitching together existing works [1,2,3,4] rather than proposing a new perspective or addressing a new issue induced by the multi-agent setting.

- The writing needs improvement. The core idea is simple and natural, but the logic is messy. There are many statements that are too subjective without any evidence, making the paper less convincing. For example, line 352 states, "The behavior policy typically originates from the old policy stored in the replay buffer, which may not align closely with the current policy after convergence". Does this not hold even after convergence? Why? Additionally, some conclusions are not consistent with the results. For example, line 294 states, "While the mean and standard deviation of $\lambda$ remain small, the maximum value of $\lambda$ grows significantly as training progresses, eventually leading to performance degradation." However, Fig 2 shows that $\lambda_{max}$ decreases over time, and the performance increases when $\lambda_{max}$ increases.

- Too many results are placed in the appendix but are referenced in the main text, especially since some claims are based on the appendix (e.g., lines 355, 407, 411, and 430). This affects the readability of the paper.

- The paper claims that extrapolation error is a major issue in MARL, but the authors do not provide any evidence to support this claim. The two proposed techniques are for bias/variance reduction, which do not seem to be directly related to extrapolation error. There is no evidence that the proposed method mitigates extrapolation error, thus leading to better performance.

- There are no implementation details or parameter searches provided for the baseline methods. Only searching parameters for the proposed method is unfair and may lead to biased results.

- Minor issue. Some learning curves are missing in the last column of Appendix Figure 10.

### Questions
- Since the paper discusses extrapolation error in MARL, can you provide results demonstrating that your method mitigates extrapolation error compared to the baselines?

- Since the Target Estimation Error (TEE) can be influenced by issues such as overestimation and extrapolation errors, how can you ensure that the issue is indeed extrapolation error due to unseen state-action values backpropagating rather than overestimation due to the max operator [1]?

- Section 3 provides a detailed analysis of QPLEX to illustrate extrapolation error in MARL. However, Section 4 switches to QMIX. Is there a specific reason for this switch?

- See Weaknesses.

[1] Anschel, Oron, Nir Baram, and Nahum Shimkin. "Averaged-dqn: Variance reduction and stabilization for deep reinforcement learning." In International conference on machine learning, pp. 176-185. PMLR, 2017.

### Soundness
2

### Presentation
1

### Contribution
2
