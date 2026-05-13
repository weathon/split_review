# Action Mapping for Reinforcement Learning in Continuous Environments with Constraints

- Decision: Reject
- Scores: 5, 6, 3, 3

## Abstract
Deep reinforcement learning (DRL) has had success across various domains, but applying it to environments with constraints remains challenging due to poor sample efficiency and slow convergence. Recent literature explored incorporating model knowledge to mitigate these problems, particularly through the use of models that assess the feasibility of proposed actions. However, integrating feasibility models efficiently into DRL pipelines in environments with continuous action spaces is non-trivial. We propose \new{a novel DRL training strategy utilizing  \textit{action mapping}} that leverages feasibility models to streamline the learning process. By decoupling the learning of feasible actions from policy optimization, action mapping allows DRL agents to focus on selecting the optimal action from a reduced feasible action set. We demonstrate through experiments that action mapping significantly improves training performance in constrained environments with continuous action spaces, especially with imperfect feasibility models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors introduce a novel approach known as action mapping (AM) within the context of deep reinforcement learning (DRL), showcasing its effectiveness, particularly when utilizing approximate feasibility models. Their results suggest that the integration of approximate model knowledge can improve training performance and enable agents to represent multi-modal action distributions, thus enhancing exploration strategies. By applying AM to both PPO and SAC, which represent on-policy and off-policy RL algorithms respectively, the authors provide comparative experimental results. These findings demonstrate that the AM method can transform state-wise constrained Markov Decision Processes (SCMDP) into Markov Decision Processes (MDP), thereby enhancing the sample efficiency of the original algorithms.

### Strengths
1. The motivation for this work is clear: it addresses the SCMDP problem by utilizing a model to learn a feasible action space, effectively converting SCMDP into an MDP and improving the algorithm’s sample efficiency.
2. The paper provides a step-by-step explanation of related concepts, making it very accessible to readers who may not be familiar with the field.
3. The description of the action and state spaces for the tasks in the experiments is clear, and the importance of the AM algorithm is effectively illustrated through visualizations at the end of the experimental section.

### Weaknesses
1. The absence of accompanying code makes it difficult to replicate the experimental results.
2. The experimental section appears somewhat limited, as it only tests the method in two environments. This reduces the persuasive power and credibility of the results.
3. The action mapping approach is not end-to-end, requiring pre-training with trajectory data before its application. This introduces additional costs, which are not adequately discussed in the paper.

### Questions
1. The paper's theme is closely related to Safe RL, as mentioned. However, many Safe RL algorithms are not included as baselines for comparison. What is the rationale behind this omission?
2. While PPO+Replacement has slower learning efficiency, it strictly ensures the satisfaction of constraints. This property is valuable in some online environments, but AM lacks this capability. Are there any proposed methods to address this limitation?
3. In Figure 4(c), the performance of AM-SAC suddenly increases at 7500 steps. How can this phenomenon be explained?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper tackles the problem of how to efficiently train agents in environments with constraints (like a robotic arm avoiding obstacles or an aircraft maintaining non-holonomic constraints). Traditional DRL approaches struggle with poor sample efficiency and slow convergence in such constrained environments. The authors propose "action mapping," which decouples the learning process into two parts: first training a feasibility policy that learns to generate all feasible actions for any state, then training an objective policy to select optimal actions from this feasible set, effectively transforming a state-wise constrained Markov Decision Process (SCMDP) into an unconstrained MDP. They validate their approach through two experiments - a robotic arm end-effector pose task with perfect feasibility models and a path planning problem with approximate feasibility models - demonstrating superior performance compared to common approaches like action replacement, resampling, and projection.

### Strengths
- The most significant contribution is how action mapping allows agents to express multi-modal action distributions through a simple Gaussian in latent space, improving exploration. Ability to plan with approximate feasibility models is a notable advantage since perfect models are rarely available in practical applications.

### Weaknesses
 - The paper omits constraint violation plots for the path planning task, making it impossible to verify claims about performance with approximate feasibility models.
    
- The feasibility model is a critical component of the proposed architecture, yet the paper lacks essential analysis and ablations of this component. Key questions remain unanswered: How is state space sampling performed during training? What metrics determine sufficient training of the feasibility model? How does the quality/approximation level of the feasibility model impact overall performance? Without these analyses, it's difficult to understand the method's robustness and its applicability to scenarios where perfect or near-perfect feasibility models aren't available.

Minor Comments:

- Typo on line 406, “actiosn”

### Questions
NA

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
This paper proposes an action mapping method that distinguishes between feasibility and objective policies during training. By pretraining the feasibility policy first and then training the objective policy, the approach enables more efficient learning within a reduced action set. Experimental results demonstrate that the proposed method results in fewer constraint violations and achieves higher returns compared to previous action replacement, resampling, and projection methods.

### Strengths
1. The method for training the feasibility policy is novel, allowing for fewer constraint violations and higher returns compared to other methods.
2. Experiments were conducted in environments requiring constraints, such as a robotic arm task and a spline-based path planning.
3. The approach is straightforward and can be combined with any RL algorithm.

### Weaknesses
1. The assumption that the feasible policy can be pretrained seems overly strict. Pretraining requires prior knowledge of the cost function $C^\tau(s;\pi)$ and the feasibility model $G(s,a)$, which may be difficult to assume in general. Specifically, the requirement for a known cost function $C^\tau(s;\pi)$ is a significant limitation. In many real-world scenarios, the cost function is not explicitly known and must be learned through interaction with the environment, similar to how rewards are learned in standard RL. The feasibility model $G(s,a)$ also presents a challenge, as it necessitates a model of the environment's constraints, which may not be readily available or easily approximated. This reliance on prior knowledge restricts the applicability of the method to environments where such information can be obtained or derived, which is a strong assumption.
2. The experimental environments appear limited. It would be beneficial to include comparisons in environments like Safety Gym or other constrained RL environments. The current experiments, while demonstrating the method's effectiveness in specific tasks, lack the breadth needed to establish its general applicability. The robotic arm task and spline-based path planning, while relevant, do not fully capture the diversity of challenges encountered in constrained RL problems. A more comprehensive evaluation should include environments with varying constraint types, complexities, and state-action spaces, such as those found in Safety Gym, to better assess the robustness and versatility of the proposed approach.
3. There is a lack of baseline algorithms. Currently, the comparisons are limited to variants of action mapping, such as action resampling and projection. Direct comparisons with a wider range of methods, including Lagrangian approaches, would strengthen the evaluation. The absence of comparisons with established constrained RL algorithms, such as Lagrangian-based methods, makes it difficult to assess the relative performance of the proposed approach. While action mapping variants provide a useful internal comparison, they do not offer a complete picture of the method's performance compared to state-of-the-art constrained RL techniques. A more comprehensive evaluation should include comparisons with methods that directly address constraint satisfaction during learning, even if they are primarily designed for standard CMDPs, by adjusting the constraint thresholds to be more strict.

### Questions
1. **[About Weakness 1]** Isn’t the required setup for the proposed method too strict? Other constrained RL methods estimate the cost function without prior knowledge, obtaining cost information similarly to rewards. In such cases, would the proposed action mapping approach still be applicable?

2. **[About Weakness 2]** Could you provide experimental results in a wider variety of environments?

3. **[About Weakness 3]** Could you also show performance comparisons with other constrained RL methods?

### Soundness
1

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a strategy called action mapping for RL in continuous environments with state-wise constraints. The idea is to learn a latent action space and an action mapping model, with which the policy samples a latent action and the latent action is further mapped to a feasible action. The proposed method is evaluated in a robotic arm end-effector pose positioning task and a path planning environment, showing better performance than several existing methods in terms of higher returns and lower constraint violations.

### Strengths
- The target problem to solve in this work is of great significance to many real-world applications.
- The related works are introduced and discussed satisfactorily.

### Weaknesses
 - Although the authors mentioned the reference [Theile et al., 2024], I found the content in Section 4 overlaps largely with the content in Section 3 and Section 4 of [Theile et al., 2024]. For example, Equation 16 in this paper is almost the same as the JS loss in Table 2 of [Theile et al., 2024]. Therefore, the novelty and contribution of this paper are questionable.
- The whole training process is not clear. Adding a pseudocode of the proposed algorithm will help. Especially, the training of the feasibility model is not clear enough. In addition, many technical details are missing. Please see my questions below.
- The idea of action mapping is closely related to the research on action representation learning [1-4]. The illustration in Figure 1 is very similar to the concept presented by Figure 1 in [1]. These related works should be included in the related work section for a detailed discussion.

### Minors

- The symbol $J$ in Equation 1,2 and Equation 3,4 are inconsistent.
- The legends in Figure 4 are too small.

### Questions
1. For the training in Section 4.1, does it require a ground-truth $g(s,a)$?
2. What is the bound of the output of $\pi_f$ and $\pi_o$?
3. What are the implementation details of the proposed method, e.g., network structure, hyperparameters?
4. For Figure 4, why is SAC+Replacement not included in Figure 4c? And where is the constraint violation plot for SAC?
5. Throughout the paper, it seems that the definitions in Equation 5-7 are not necessary, as in Section 4 and the experiments only the function $g$ is assumed. Can the authors provide more explanation on this point?
6. How many seeds/trials are used in Figure 4?

### Soundness
2

### Presentation
2

### Contribution
1
