# Learning in complex action spaces without policy gradients

- Decision: Reject
- Scores: 5, 5, 5

## Abstract
Conventional wisdom suggests that policy gradient methods are better suited to complex action spaces than action-value methods. However, foundational studies have shown equivalences between these paradigms in small and finite action spaces (O'Donoghue et al., 2017; Schulman et al., 2017a). This raises the question of why their computational applicability and performance diverge as the complexity of the action space increases. We hypothesize that the apparent superiority of policy gradients in such settings stems not from intrinsic qualities of the paradigm, but from universal principles that can also be applied to action-value methods to serve similar functionality. We identify three such principles and provide a framework for incorporating them into action-value methods. To support our hypothesis, we instantiate this framework in what we term QMLE, for Q-learning with maximum likelihood estimation. Our results show that QMLE can be applied to complex action spaces with a controllable computational cost that is comparable to that of policy gradient methods, all without using policy gradients. Furthermore, QMLE demonstrates strong performance on the DeepMind Control Suite, even when compared to the state-of-the-art methods such as DMPO and D4PG.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper challenges the conventional belief that policy gradient methods are superior to action-value methods for complex action spaces. The authors propose that this advantage comes from universal principles that can also be applied to action-value methods, such as using Monte Carlo approximations, amortized maximization, and scalable architectures. They introduce Q-learning with Maximum Likelihood Estimation (QMLE), a framework that adapts these principles to action-value learning. Empirical results show that QMLE performs comparably to policy gradient methods on complex action spaces, particularly on the DeepMind Control Suite. The findings suggest that the strengths of policy gradient methods are not intrinsic but can be replicated within action-value approaches.

### Strengths
- The paper presents a novel perspective by challenging the conventional wisdom that policy gradient methods are inherently superior for complex action spaces, opening up new avenues for research and exploration.
- The introduction of the Q-learning with Maximum Likelihood Estimation (QMLE) framework effectively integrates principles traditionally associated with policy gradients into action-value learning, showcasing versatility and adaptability.
- The authors provide robust empirical results demonstrating that QMLE can achieve performance comparable to policy gradient methods on complex tasks, specifically in the DeepMind Control Suite, thereby validating their theoretical claims.
- The paper emphasizes the scalability of the proposed methods, which is crucial for real-world applications involving high-dimensional action spaces, making it a practical contribution to the field of reinforcement learning.
- By revealing that the strengths of policy gradient methods can be replicated in action-value approaches, the paper encourages a reevaluation of existing strategies in reinforcement learning, potentially influencing future research directions and methodologies.

### Weaknesses
 - While the paper introduces the QMLE framework, it lacks in-depth theoretical analysis or proof of convergence properties, which could strengthen the foundational understanding of the proposed method. Specifically, the paper does not provide a rigorous analysis of how the approximate maximization impacts the convergence of the Q-learning algorithm, especially when using function approximators like neural networks. The theoretical guarantees for tabular Q-learning do not directly translate to the function approximation setting, and this gap needs to be addressed.
- The empirical evaluations are primarily conducted in the DeepMind Control Suite, which may not fully represent the challenges and complexities found in more diverse real-world environments, limiting the generalizability of the findings. The suite, while useful for benchmarking, may not capture the nuances of environments with sparse rewards, partial observability, or stochastic transitions, which are common in real-world applications. This narrow focus makes it difficult to assess the true robustness and applicability of QMLE.
- The paper could benefit from a more thorough comparison with other state-of-the-art action-value methods beyond policy gradient approaches to provide a clearer context for the advantages and limitations of the QMLE framework. For example, a comparison with methods that also use function approximation for action-value learning, such as distributional Q-learning or methods that incorporate attention mechanisms, would be beneficial. This would help to position QMLE more clearly within the existing landscape of action-value methods.
- There is little discussion on the sensitivity of the QMLE approach to hyperparameters, which can significantly impact performance in practice; this omission could hinder practitioners from effectively applying the method. The paper does not provide sufficient guidance on how to choose the sampling budgets for target and greedy actions, or the sampling ratios for uniform and local sampling. Without a clear understanding of how these parameters affect performance, it is difficult to use QMLE effectively.
- The paper does not offer concrete suggestions for future research directions or improvements to the QMLE framework, which could leave readers uncertain about the next steps for advancing this line of inquiry. While the paper introduces a novel approach, it does not delve into potential modifications or extensions that could enhance its performance or applicability, such as incorporating techniques for exploration or handling non-stationary environments.

### Questions
- What are the key theoretical assumptions underlying the QMLE framework, and how do they compare to traditional action-value methods?
- How does the QMLE framework perform in environments outside the DeepMind Control Suite? Are there specific tasks where its advantages or limitations become more pronounced?
- What guidelines can be provided for selecting hyperparameters when using the QMLE framework, and how does their choice impact performance across different environments?
- Can you elaborate on the implementation challenges encountered when applying the QMLE framework in practice? Were there any unexpected behaviors observed during training?
- How does the QMLE framework stack up against other recent approaches in reinforcement learning, particularly those utilizing action-value methods? Are there specific scenarios where it outperforms others?
- What are the authors’ thoughts on potential extensions or modifications to the QMLE framework that could enhance its applicability or efficiency in more complex scenarios?
- How robust is the QMLE approach to noise and variability in the environment? Have any experiments been conducted to assess its stability under such conditions?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper challenges the assumption that policy gradient methods are inherently superior for environments with complex/continuous action spaces. The authors identify core principles (Monte Carlo approximations, maximum likelihood estimation, and action-in architectures) in policy gradients and incorporate them into action-value methods. Their method achieves comparable performance to policy gradient methods in continuous control tasks in DMC, demonstrating that action-value methods can handle complex action spaces without the need for policy gradients​

### Strengths
1. The identification of the three core principles is noteworthy and has the potential to influence future research on policy gradient methods, even considering that the paper's goal is to provide alternatives to traditional policy gradients. 
2. The experimental setup appears sound, with comparisons against several baselines across multiple seeds, and the results generally favor the proposed method. However, I would suggest including an ablation study (see Point 3 below).

### Weaknesses
1. My major concern is with the overall goal of the paper, as its central premise is unclear to me. First, what is the issue with policy gradients that the authors are aiming to replace them? This should have been clarified to justify the need for an alternative approach. If the goal is to develop a method that is simpler (i.e., fewer components, reduced computation, fewer hyperparameters) than policy gradients, similar to the approach in [1], I would argue that the proposed method is in fact more complex than policy gradients. It introduces additional hyperparameters and design decisions. Furthermore, the method eventually requires a parametric component for predicting the argmax (Principle 2 in Section 4). In my view, this component functions as a type of policy, albeit in a somewhat convoluted and unintuitive way. Its inclusion seems to contradict the paper’s aim of eliminating the need for a policy and policy gradients. In fact, I would argue that the proposed method cannot be considered purely as an action-value method, as claimed by the authors.

2. The argument regarding the equivalence of policy gradients and MLE (Section 3.2), while likely correct, is presented in a very informal manner. A more rigorous analysis or formal proof of this equivalence would significantly strengthen the paper.

3. The paper lacks an ablation study on the different components of the proposed method (Principles 1, 2, and 3). Given the number of design choices involved, an ablation study is essential to better understand the contribution of each principle.

4. Many of the equations in the paper (Equations 3, 4, 8, 9, 10, 11, 13, 14) are written without an equal sign, making them appear as disconnected mathematical expressions. While their meaning can be inferred from the surrounding text, the lack of clarity in some cases creates an informal mathematical tone and makes it difficult to interpret the exact role of these equations.

5. The background section spans three pages and covers material likely familiar to most readers. I recommend condensing this section and moving some of the content to the appendix. This would allow for a more detailed presentation of the algorithm (currently in Appendix A) in the main body of the paper, as well as addressing the concerns I raised above.

### Questions
1. What are the limitations of policy gradients that lead to their replacement?
2. Why does the number of seeds vary across different tasks? Additionally, what do the shaded regions in the figures represent?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes three universal principles from policy gradient methods and incorporates them into action-value framework.

The method is evaluated in DMC domains with continuous action space.

However, the proposed method does not show a significant improvement in performance over DDPG or D4PG, especially in domains with high-dimensional action spaces.

### Strengths
1, The proposed principles underlying the scalability of policy gradient methods are intriguing observations, and a careful analysis of the gap between the two paradigms is insightful.

2, The presentation of the ideas proposed is clear.

3, Experiments were conducted across multiple domains, although without significant improvement.

### Weaknesses
1, There is no theoretical guarantees for computing the maximization in A_m instead of A(eq.17).    (In policy gradient methods, using an MC estimator in place of exact summation or integration has theoretical foundations.)

2, The proposed method trains all the predictors from historical argmax approximation  to construct a small action space A_m for computing an approximation of best action. The iterative dependency restricted the actions to a subset where most actions are similar, potentially leading to a suboptimal solution.

3, As illustrated in Figure.2, QMLE can transcend DPG through a uniform sampling over action space([global]). But in high-dimensional action space, uniform sampling is usually inefficient. This paper lacks an ablation study of the uniform sampling and the ensemble of argmax predictors in the domains with high-dimensional action spaces.

### Questions
1, The proposed method uses log-likelihood gradient to train the argmax predictors.  Why not use the policy gradient directly to update the the ensemble of argmax predictors?

### Soundness
2

### Presentation
3

### Contribution
2
