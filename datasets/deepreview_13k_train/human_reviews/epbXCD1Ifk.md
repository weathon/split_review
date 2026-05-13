# Offline Reinforcement Learning With Combinatorial Action Spaces

- Decision: Reject
- Scores: 5, 3, 3

## Abstract
Reinforcement learning problems often involve large action spaces arising from the simultaneous execution of multiple sub-actions, resulting in combinatorial action spaces. Learning in combinatorial action spaces is difficult due to the exponential growth in action space size with the number of sub-actions and the dependencies among these sub-actions. In offline settings, this challenge is compounded by limited and suboptimal data. Current methods for offline learning in combinatorial spaces simplify the problem by assuming sub-action independence. We propose Branch Value Estimation (BVE), which effectively captures sub-action dependencies and scales to large combinatorial spaces by learning to evaluate only a small subset of actions at each timestep. Our experiments show that BVE outperforms state-of-the-art methods across a range of action space sizes

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper tackles the problem of offline RL in combinatorial action spaces, where actions are formed by combinations of sub-actions, leading to a rapid increase in possible actions. Such action spaces challenge standard offline RL methods, particularly in handling dependencies among sub-actions and limited data availability.

The authors propose a novel method, Branch Value Estimation (BVE), to address these issues by structuring the action space as a tree to capture sub-action dependencies effectively. Their approach evaluates only a subset of possible actions, making the process more computationally efficient. BVE introduces a behavior-regularized temporal difference (TD) loss designed to reduce overestimation bias in such combinatorial settings, leading to more stable value estimates.

In their experiments, BVE consistently outperforms established baselines, including methods like Factored Action Spaces and Implicit Q-Learning, demonstrating superior performance and stability across a variety of high-dimensional environments. The results suggest that BVE is particularly effective in scenarios where standard methods fail to handle sub-action dependencies within combinatorial action spaces efficiently.

This paper’s contributions include (1) introducing the BVE method with a novel value estimation strategy for structured action spaces, (2) providing theoretical insights into the impact of sub-action dependencies on offline RL performance, and (3) an extensive evaluation demonstrating BVE’s effectiveness in complex, high-dimensional environments.

### Strengths
1. Originality. The paper introduces a novel way to represent combinatorial action spaces using trees. The branch value estimation technique presents a valuable solution to action selection in large spaces. The combination of beam search with RL is innovative and hadn't been applied this way before. The approach to handling sub-action dependencies through tree traversal is original. The method provides a new angle on addressing overestimation bias in offline RL.

2. Quality. The empirical results demonstrate clear performance advantages over existing approaches. The ablation studies effectively isolate the contribution of each component. The method successfully scales to large action spaces of up to 4 million actions. The consistent performance across different environment sizes shows robustness. The experimental design directly addresses the key claims.

3. Clarity. Complex concepts are explained through effective visualizations and examples. The algorithm descriptions are precise and well-detailed with clear pseudocode. The paper follows a logical progression that builds understanding. The experimental setup and results are presented transparently. The technical content strikes a good balance between depth and accessibility.

4. Significance. The paper tackles a fundamental challenge in applying RL to real-world problems with combinatorial action spaces. The computational efficiency improvements make previously intractable problems manageable. The method has potential applications in important domains like healthcare and robotics. The approach opens new directions for handling complex action spaces in RL.

5. Technical contribution. The tree-based representation effectively reduces the search space while maintaining performance. The branch value estimation technique successfully handles dependencies between sub-actions. The beam search integration provides an efficient solution for policy extraction.

### Weaknesses
1. Limited comparative evaluation: The paper compares against only two baselines (FAS and IQL), which leaves questions about relative performance against other approaches. Particularly relevant is the recent parallel work on factorized action spaces (https://openreview.net/forum?id=STwxyUfpNV) which offers additional baselines and testing environments.

2. Theoretical analysis: While the empirical results are promising, the paper would benefit from theoretical analysis of convergence properties and formal bounds on beam search approximation error. Understanding the conditions under which BVE is guaranteed to perform well would help practitioners apply the method with confidence. This theoretical foundation would also help characterize the relationship between approximation quality and final policy performance.

3. Technical details: The paper could better explain several important implementation aspects, particularly the interaction between depth penalty and beam search during action selection. A more detailed analysis of computational overhead would help understand practical scaling properties, while clearer explanation of terminal state handling would aid reproducibility. The trade-offs between computational cost and performance deserve more thorough quantification.

4. Empirical analysis: The method's robustness to different data distributions could be more thoroughly investigated to understand its reliability in varied conditions. The ablation studies could provide deeper insights by more systematically exploring beam width's impact on performance. Additionally, a more detailed analysis of how performance scales with increasing numbers of sub-actions would help understand the method's limitations.

5. Scope of claims: The paper makes several broad claims about BVE's capabilities that could benefit from more nuanced presentation. While the claim about scaling to large action spaces is well supported empirically, the claim about "effectively capturing sub-action dependencies" needs stronger evidence from more diverse types of dependencies. The paper states BVE "outperforms state-of-the-art methods" but this is only demonstrated against two baselines. Similarly, while empirical results suggest reduced overestimation bias, the mechanism and conditions for this reduction could be better explained with theoretical analysis.

### Questions
Theory:
- Could you outline what theoretical guarantees might be possible for the tree traversal algorithm's convergence properties?
- How would you characterize the relationship between beam search approximation and policy optimality in your method?
- Could you elaborate on the specific conditions under which BVE would be expected to perform optimally?

Comparative evaluation and claims:
- Your paper addresses similar challenges as "An Investigation of Offline Reinforcement Learning in Factorisable Action Spaces" (https://openreview.net/forum?id=STwxyUfpNV) which relies on a value function decomposition. Have you considered comparing against their adaptations of BCQ, CQL, and IQL?
- Could you evaluate BVE on the DeepMind Control Suite environments with discretised actions (or other complex environments with strongly dependent sub-actions) to validate the broad claim about outperforming state-of-the-art methods?
- What evidence supports the claim about "effectively capturing sub-action dependencies" beyond the current experiments?

Technical implementation and scaling:
- Could you explain how the depth penalty and beam search interact during action selection?
-  What is the computational overhead of tree construction and traversal compared to baselines?
- How are terminal states handled in the tree structure?

Empirical analysis:
- How does the method's performance scale with increasing numbers of sub-actions?
- Could you characterize the method's robustness to different data distributions?
- Could you provide more detailed analysis of how beam width affects the trade-off between performance and computational cost?

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
3

### Summary
The paper addresses the challenge of combinatorial action spaces in offline reinforcement learning by proposing a method called Branch Value Estimation (BVE). BVE utilizes a tree structure to effectively prune the action space, organizing actions into a hierarchy where each node in the tree represents a sub-action conditioned on the values from its parent node. This structure, to some extent, captures dependencies among sub-actions and also reduces the number of actions evaluated at each timestep. As the tree is traversed, BVE estimates the highest achievable Q-value at each branch, allowing for the selection of the optimal action. The effectiveness of BVE is demonstrated through comparisons with state-of-the-art offline RL algorithms across various action space sizes, showing improved performance in environments with up to over 4 million possible actions.

### Strengths
1. The paper explains its main idea clear.
2. The paper targets an important problem.
3. The application of tree-structured action search seems new.

### Weaknesses
The critique identifies several weaknesses that should be addressed:

Clarity on Action Space Reduction: The paper states that BVE reduces the effective action space by organizing it into a tree structure, unlike traditional RL methods which often misidentify the optimal next action a^′\hat{a}’a^′ in equation 4. However, it remains unclear whether the overestimated actions are effectively excluded by this method. The tree traversal procedure appears optimistic about the estimated action values. It is not evident from the paper which design choice specifically helps to prevent overestimation in an offline setting, as the behavior cloning itself contributes to this effect. If the authors want to claim the tree-based method can mitigate overestimation, either theoretical or empirical evidence should be provided. 

Application to Online RL: Given that the tree structure concept for managing large action spaces could also be beneficial in online RL settings—which are generally less challenging than offline settings—it’s surprising that the authors chose not to begin with online RL.

Broader Applicability and Contributions: The potential for applying the tree-structure approach in other offline RL methods raises questions about the broader significance of the work. If applicable, the contribution could be more substantial.

Ablation Study and Its Implications: The message of the ablation study is ambiguous. Figure 1 only displays two deltas, with Figure (b) showing a difference only when alpha=0, while Figure (c) suggests that DQN performs poorly even in small action spaces, raising questions about its suitability as a competitor. Additionally, it’s unclear whether the DQN is used in an offline learning setting, which would be unusual.

Justification for Design Choices: Equation (4) appears abruptly, with no justification for discounting ||a' - \hat{a}‘||. The paper should clarify why this design was chosen.

Addressing Dual Challenges: The authors attempt to address both the challenges of large discrete action spaces and offline learning. This dual focus can cause confusion regarding the contributions and effects of the design choices. Two primary questions should be addressed:
Scalability: As the action space increases, can this approach maintain high computational and sample efficiency compared to other baselines? This should be the first point to verify given that the proposed idea mainly addresses scalability. Learning curves in the form of performance v.s. computation time/number of samples are expected. Overestimation in Offline Settings: How does this approach avoid the overestimation problem in offline settings, or what offline RL algorithms can be integrated if it does not?

Empirical Results and Parameter Selection: The empirical results in Figures 8 and 9 do not show statistically significant differences, raising concerns about the effectiveness. The selection process for IQL and FAS hyperparameters is also not clearly described.

Omission of Related Work: The paper fails to cite several highly relevant works, including:
“Conjugate Markov Decision Processes” by Philip Thomas et al., which deals with extremely large action spaces.
“Reinforcement Learning with Function-Valued Action Spaces for Partial Differential Equation Control” by Yangchen Pan et al., applicable to high-dimensional continuous control and potentially adaptable for discrete settings.
“Deep Reinforcement Learning in Large Discrete Action Spaces” by Gabriel Dulac-Arnold et al.
“Conditionally optimistic exploration for cooperative deep multi-agent reinforcement learning” by Xutong Zhao et al., which utilizes a tree-structured action for exploration purposes in a multi-agent, centralized setting. Note that, although it is a multi-agent setting, the subagents' actions are concatenated to a vector for execution, which can be thought of as one agent with high dimensional discrete actions.

### Questions
see above.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper addresses the challenges of reinforcement learning in combinatorial action spaces, which arise from executing multiple sub-actions simultaneously. The exponential growth in action space size and the interdependencies among sub-actions complicate learning, particularly in offline settings with limited and suboptimal data. Current methods often simplify this by assuming independence among sub-actions. The authors propose Branch Value Estimation (BVE), a method that effectively captures these dependencies and scales to large combinatorial spaces by evaluating only a small subset of actions at each timestep. Experimental results demonstrate that BVE outperforms baseline approaches across various action space sizes.

### Strengths
The motivation of this paper is clear: the issue of combinatorial action spaces in offline reinforcement learning has indeed been underexplored, making it worthy of further attention. The experiments presented are also quite persuasive and effectively demonstrate the advantages of BVE.

### Weaknesses
1. The method introduction in this paper lacks clarity, particularly regarding the process of constructing the tree and the Q-learning based on the tree, making it difficult to understand the underlying design principles. For example, in the tree shown in Figure 1, are the elements in the third and fourth layers fixed, or can their positions be swapped? Additionally, the output of \( f(s,a) \) includes \( v \), but based on the example in Figure 3, the dimensions of \( v \) corresponding to different layers of the tree are different. So what is the dimensionality of the output of \( f(s,a) \)? Is it fixed or variable? I haven't found definitive answers to these questions in the paper.

2. The paper claims that the proposed method can eliminate the assumption of action space independence from previous works; however, it does not explicitly explain why BVE can effectively consider the interdependencies among different sub-actions, merely presenting the process without clearly outlining its advantages.  So I recommend the author to provide a more explicit explanation or analysis of how BVE captures sub-action dependencies.

3. I understand that the design concept may be similar to using a binary search method to find the maximum value, thereby obtaining the maximum among exponentially many action combinations with logarithmic operations. I'm not sure if my understanding is accurate, so I suggest the authors further develop the convergence theory of Q-learning under this search paradigm, which would enhance the paper.

4. Although the paper considers the problem within an offline RL framework, it only uses an optimization objective with a behavior cloning regularization term without further addressing out-of-distribution (OOD) or distribution shift issues. This makes the offline RL setting seem unnecessary here, so the authors might consider examining the method's performance in an online setting. Additionally, I recommend the authors refer to the following paper, which, while focused on multi-agent reinforcement learning, also addresses the OOD problem in combinatorial action spaces in offline settings using a counterfactual Q-learning design, which could be relevant to this paper's problem setup.

5. Regarding the experimental section, I find the current experimental setup somewhat artificial and lacking in realistic tasks. I suggest the authors conduct experiments in more meaningful real-world scenarios.

### Questions
The same as the questions in Weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2
