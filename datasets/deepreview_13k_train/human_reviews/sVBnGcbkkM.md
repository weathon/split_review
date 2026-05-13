# RILe: Reinforced Imitation Learning

- Decision: Reject
- Scores: 8, 3, 8, 5

## Abstract
Reinforcement Learning has achieved significant success in generating complex behavior but often requires extensive reward function engineering. Adversarial variants of Imitation Learning and Inverse Reinforcement Learning offer an alternative by learning policies from expert demonstrations via a discriminator. However, these methods struggle in complex tasks where randomly sampling expert-like behaviors is challenging. This limitation stems from their reliance on policy-agnostic discriminators, which provide insufficient guidance for agent improvement, especially as task complexity increases and expert behavior becomes more distinct. We introduce RILe (Reinforced Imitation Learning environment), a novel trainer-student system that learns a dynamic reward function based on the student's performance and alignment with expert demonstrations. In RILe, the student learns an action policy while the trainer, using reinforcement learning, continuously updates itself via the discriminator's feedback to optimize the alignment between the student and the expert. The trainer optimizes for long-term cumulative rewards from the discriminator, enabling it to provide nuanced feedback that accounts for the complexity of the task and the student's current capabilities. This approach allows for greater exploration of agent actions by providing graduated feedback rather than binary expert/non-expert classifications. By reducing dependence on policy-agnostic discriminators, RILe enables better performance in complex settings where traditional methods falter, outperforming existing methods by 2x in complex simulated robot-locomotion tasks.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces ‘Reinforced Imitation Learning’, a new trainer-student framework. In this framework, the trainer receives feedback from a discriminator and continuously adjusts the output reward in response to the student's behavior. The student is then trained using reinforcement learning based on the reward signal from the trainer. This approach may enable increased exploration behavior in students and more detailed feedback from the trainer. The proposed approach is evaluated in a maze setting, LocoMujoco, and humanoid MuJoCo. Experimental results indicate that the proposed approach outperforms competitive baselines significantly.

### Strengths
**Originality & Significance** 

1. The reviewer found the concepts of a custom reward function and the decoupling of reward function learning from the student and discriminator to be quite innovative. The experimental results suggest that this approach effectively addresses the issue of insufficient guidance, a common challenge in early-stage training for adversarial imitation and reinforcement learning methods. This improvement in guidance appears to be particularly beneficial during the initial phases of the learning process.

2. The background section is well-organized and effectively introduces the key concepts. The authors provide a concise overview of reinforcement learning (RL), inverse reinforcement learning (IRL), adversarial imitation learning (AIL), and adversarial reinforcement learning (AIRL). These explanations establish a solid foundation for understanding the proposed approach and its position within the broader literature. Additionally, the authors clearly articulate the distinctions between existing methods and their proposed approach, further highlighting the motivation and novelty of their work. 


**Quality** 

The claims are supported by experimental results. Particularly, table 1 shows that the proposed approach is able to handle complex tasks that baselines didn’t perform well. 
The reviewer appreciated the presentation of figure 3. It clearly illustrates the dynamics of the reward function of the proposed approach and its difference to existing methods. 

**Clarity** 

While some clarification of  the technical contents is needed,  the paper is overall well organized and easy to follow. Please see the weakness section for details.

### Weaknesses
1. The reviewer found the reward function for the trainer agent needs further clarification. Specifically, L 241 reads ‘the trainer’s RL-based approach optimizes for long-term performance rather than immediate feedback’, but it is unclear to the reader how the formulation of the reward function (Eq. 8) could achieve it. The reward function appears to be a combination of the discriminator's output and the trainer's action, but it is not clear how this combination encourages long-term planning. The discriminator's output provides a measure of how well the student is imitating the expert, but it is not clear how this translates into a reward that encourages the trainer to provide better feedback over time. The connection between the reward function's components and the stated goal of long-term performance optimization is not sufficiently explained.

2. It is unclear to the reviewer the role of $a^T$ in the reward function of the trainer (Eq. 8). With $a^T$ in the objective, would it encourage the trainer to generate $a^T=1$ without further constraint? Also, L 314 reads ‘by incorporating $a^T$ into the reward function, the trainer learns to adjust its policy based on the effectiveness of its previous actions’. It is unclear to the reviewer how this is achieved. Specifically, if $a^T$ is a binary variable, it is not clear how it can represent the effectiveness of the trainer's previous actions. The reward function seems to incentivize the trainer to simply set $a^T$ to 1, which would maximize the reward, without any consideration for the quality of the feedback being provided to the student. The explanation of how $a^T$ enables the trainer to learn to adjust its policy based on the effectiveness of its previous actions is not clear and requires further elaboration.

### Questions
1. The reviewer's primary concern is how the trainer's reward function contributes to optimizing long-term feedback. Additionally, the reviewer questions the rationale for incorporating the trainer's action into the reward function. Please refer to the "Weaknesses" section for a detailed explanation.  
2. L313, how is the constant determined in $v(x) = 2x - 1$?  
3. How many training environment steps are used for each task?   
4. Why are confidence intervals not included in Table 1?

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
This paper proposes a novel method for adversarial imitation learning. Unlike established methods such as GAIL and AIRL, which learn a policy using reinforcement learning (RL) under a reward function derived directly from the discriminator, the proposed method, RILe, introduces an additional RL component called the trainer agent. This trainer agent generates the reward function for policy learning, effectively serving as an intermediary layer between the discriminator and the policy learning component (referred to as the student agent). The paper claims that this additional trainer component, as an RL agent, is able to dynamically provide an adaptive reward function throughout the student agent's policy learning process, resulting in superior imitation learning performance in complex settings.

### Strengths
1. This paper aims to address some of the challenges faced by existing imitation learning methods in complex settings, a valuable problem to study with a wide range of potential practical applications.

2. The introduction of an additional trainer agent in the proposed method, RILe, is a novel design.

3. The discussion of related literature is clear and effectively situates the proposed method within the context of existing research.

### Weaknesses
1. My major concern with the paper is that several major claims regarding the capabilities of the proposed method, RILe, are not sufficiently supported by rigorous analysis or adequate experimental evidence.
* Claim of RILe's adaptability: For instance, in Section 5.1, it is stated that "RILe demonstrates a more adaptive reward function that evolves with the student's progress ...". However, this claim is inadequately supported by the limited results in Figure 3, which only includes a single, simple setting and is open to subjective interpretation. A more comprehensive analysis involving multiple, diverse environments and a quantitative measure of adaptability would significantly strengthen this claim. Similar claims in the Introduction and Discussion suggest that RILe’s adaptability leads to more efficient policy learning for the student agent, but there is insufficient experimental evidence to validate this connection. A direct comparison of the learning curves of the student agent under RILe versus baseline methods, while controlling for other factors, would provide more convincing evidence.
* Claim of RILe outperforming state-of-the-art adversarial IL methods: Although the main results in Section 5.2 show that RILe outperforms the baseline methods, GAIL and AIRL, on several LocoMujuco tasks, these results lack sufficient details on the experimental setup, such as the settings of tasks used for evaluation and the hyperparameter values of the compared methods. Without this information, it is difficult to assess the validity and reproducibility of the results. Furthermore, reporting the standard deviation or confidence intervals of the performance metrics would provide a better understanding of the statistical significance of the observed differences.
* Additionally, the proof of the theoretical argument, Lemma 1, is neither rigorously presented nor complete. Specifically, the connection between the assumptions made and the final result is not clearly established, and several intermediate steps are missing.

2. Another concern I have with the proposed RILe method is that it stacks one RL agent (the trainer agent) on top of another (the student agent). The trainer agent's state transition depends on the student agent's policy since its states are represented by the state-action pairs generated by the student agent. Meanwhile, the student agent's policy is influenced by the trainer agent's policy through the reward function generation. This structure creates a dependency in the trainer's RL environment (i.e. the state transition of the RL environment faced by the trainer agent is not exogonous to its policy), making the MDP ill-defined and potentially introducing extra instability to the training framework. This interdependency could lead to complex and unpredictable dynamics, making it difficult to guarantee convergence or stability. 
* In fact, the paper briefly addresses training instability in the Discussion section and mentions a workaround of freezing the trainer midway through training. However, this workaround seems ad-hoc and may not fully address the underlying issue of the ill-defined MDP.

3. The proposed optimization objective of the trainer agent, Equation 8, lacks a clear explanation of the rationale behind this particular choice. Specifically, the use of the term  $v(D_{\phi}(s, a)) a^T$ is not well-motivated. While the paper mentions that "By incorporating $a^T$ into the reward function, the trainer learns to adjust its policy based on the effectiveness of its previous actions", this explanation is somewhat unclear. A more detailed explanation of how this term relates to the overall objective of imitation learning and how it helps the trainer agent guide the student agent would be beneficial. It would also be helpful to discuss alternative formulations and why this particular one was chosen.

4. Overall, the paper is not well-organized and includes errors or inaccuracies in some parts.
* In Section 3.2, entropy regularization is introduced as part of the RL problem formulation in this work, defined in Equation 1. However, in Section 3.3, the RL formulation is presented without entropy regularization, which is then added again in Equation 2. This inconsistency creates confusion about the actual RL formulation being used.
* In Section 4, the first term on the right-hand side of Equation 14 should be $v(D_{\phi}(s_t))a_t$ instead of $D_{\phi}(s_t)$ to remain consistent with the reward definition in Equation 11. This appears to be a typographical error that needs to be corrected.
* The workaround for the training instability (freezing the trainer after meeting certain criteria) is only mentioned in the Discussion section, with no mention of it in the discussion of experimental settings and results. This makes it difficult to understand how this workaround was implemented in the experiments and how it might have affected the results.

### Questions
1. What is the rationale behind the specific definition of the optimization objective of the trainer agent, $v(D_{\phi}(s, a)) a^T$ (Equation 8)? It is mentioned that "By incorporating $a^T$ into the reward function, the trainer learns to adjust its policy based on the effectiveness of its previous actions", but this explanation is somewhat unclear. Could you clarify why $a^T$ is specifically multiplied with $v(D_{\phi}(s, a))$?

2. In Figure 4, the performance of RILe remains relatively good when the trainer's replay buffer is 100\% expert data, provided that the proportion of expert data in the student's replay buffer is not too large. This outcome is somewhat puzzling, as I would expect that with 100\% expert data in the trainer's replay buffer, neither the trainer nor the discriminator would be trained on any trajectories generated by the student policy, based on the framework illustrated in Figure 2. Am I misunderstanding something here?

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
RILe (Reinforced Imitation Learning environment) is a framework that enhances reinforcement and imitation learning by introducing a dynamic, adaptive reward function responsive to agent performance. Addressing limitations of traditional IL methods like GAIL and AIRL, RILe’s trainer-student model continuously optimizes rewards through reinforcement learning, effectively guiding the student agent to mimic expert demonstrations in complex tasks. Experiments in maze and humanoid locomotion tasks demonstrate RILe's advantages in scalability, robustness, and adaptability, highlighting its effectiveness for high-dimensional control environments.

### Strengths
1. **Motivation and Intuition**: The motivation for reducing reliance on static discriminators is compelling, as complex tasks often necessitate adaptive guidance.

2. **Novelty**: The framework’s use of a trainer agent that dynamically learns a reward function to align with student policy is an innovative approach that enhances traditional adversarial learning strategies.

3. **Technical Contribution**: RILe’s decoupling of the reward function learning from the student’s policy learning shows clear benefit, especially in tasks requiring extensive exploration, as the framework enables more progressive feedback than binary classifications.

4. **Clarity**: The paper is well-structured, with clear theoretical explanations and effective visualizations. Figures, such as Figure 3, successfully illustrate the evolution of reward functions across training stages.

### Weaknesses
 - The connection between motivation and the proposed method is weak. More intuition or theoretical proofs are needed.
- While the paper highlights some issues with existing methods, it lacks detailed references and experiments to convincingly demonstrate how RILe addresses these issues. More ablation studies or theoretical analysis could strengthen the argument.
- The scope of the experiment is limited to comparing only GAIL and AIRL on one benchmark. More baselines [1,2,3,4] and tasks should be evaluated.

- In line 241, the authors mention "the trainer’s RL-based approach optimizes for long-term performance rather than immediate feedback".  If the benefit comes from RL, all AIL methods also share it since they all use RL for policy learning. How does the RILe handle this?

- In Section 5.1 and Figure 3, it’s stated that RILe offers better rewards for guiding student policies, but in the second and third columns, GAIL appears to learn faster. The reward contours for GAIL and AIRL also seem closer to the ground truth. Moreover, learning with a fixed reward function is the most common approach in typical RL. Could the authors elaborate more on how the evolving feature benefits policy learning?

- Why did the authors choose LocoMujoco, which lacks action labels, rather than more widely used Mujoco tasks for Learning from Demonstration (LfD)? I would recommend limiting the scope to Learning from Demonstration (LfD), where action labels are available. Besides, IQLearn did provide learning with state-only rewards version in the paper. If the authors want to demonstrate the application on Learning from Observation (LfO), I think it will be better to conduct experiments separately with a different set of baselines [5,6,7,8].

- In Figure 4, how are normalized scores and steps defined? The result seems to be applicable to many online imitation learning methods. Could the authors provide more details on the purpose of these metrics in the context of RILe?

- The authors mentioned RILe improves the computational efficiency compared to other IRL works. However, RILe needs to train an extra trainer network compared to GAIL. Is there a quantitative analysis on this?

### Questions
1. The experimental setup relies primarily on older baselines (e.g., BC from 2010, GAIL from 2016, and AIRL from 2018). Including comparisons with more recent adversarial imitation learning (AIL) methods, such as DRAIL [1], would provide a more comprehensive assessment of RILe’s performance, especially given that DRAIL also address challenges related to learning efficiency in complex, high-dimensional environments. The paper needs to include DRAIL [1]. Doing so would significantly enhance the paper’s impact. I would be willing to score it higher with this addition.

2. How does the dynamic reward adjustment by the trainer agent handle rapidly changing or highly stochastic environments, where optimal behavior may vary significantly within episodes?

3. RILe involves multiple components with different objectives (trainer, student, and discriminator). How sensitive is RILe to hyperparameter choices across these agents, and are there any recommended tuning strategies?

4.  The paper shows RILe’s ability to perform well with noisy expert data, but how robust is this approach if the noise distribution changes dynamically during training, or if the expert data is sparse?

[1] Lai, Chun-Mao, et al. "Diffusion-Reward Adversarial Imitation Learning." arXiv preprint arXiv:2405.16194 (2024).

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposed Reinforced Imitation Learning (RILe) to learn the reward function for policy learning with AIL and teacher-student framework. The method is evaluated on LocoMujoco benchmark and it outperforms GAIL and AIRL.

### Strengths
- The idea of Decoupled Reward-function Learning with AIL is novel.

- RILe demonstrates better performance on the LocoMujoco benchmark than baselines (GAIL and AIRL).

### Weaknesses
- The connection between motivation and the proposed method is weak. More intuition or theoretical proofs are needed.
- While the paper highlights some issues with existing methods, it lacks detailed references and experiments to convincingly demonstrate how RILe addresses these issues. More ablation studies or theoretical analysis could strengthen the argument.
- The scope of the experiment is limited to comparing only GAIL and AIRL on one benchmark. More baselines [1,2,3,4] and tasks should be evaluated.

### Questions
- In line 241, the authors mention "the trainer’s RL-based approach optimizes for long-term performance rather than immediate feedback".  If the benefit comes from RL, all AIL methods also share it since they all use RL for policy learning. How does the RILe handle this?

- In Section 5.1 and Figure 3, it’s stated that RILe offers better rewards for guiding student policies, but in the second and third columns, GAIL appears to learn faster. The reward contours for GAIL and AIRL also seem closer to the ground truth. Moreover, learning with a fixed reward function is the most common approach in typical RL. Could the authors elaborate more on how the evolving feature benefits policy learning?

- Why did the authors choose LocoMujoco, which lacks action labels, rather than more widely used Mujoco tasks for Learning from Demonstration (LfD)? I would recommend limiting the scope to Learning from Demonstration (LfD), where action labels are available. Besides, IQLearn did provide learning with state-only rewards version in the paper. If the authors want to demonstrate the application on Learning from Observation (LfO), I think it will be better to conduct experiments separately with a different set of baselines [5,6,7,8].

- In Figure 4, how are normalized scores and steps defined? The result seems to be applicable to many online imitation learning methods. Could the authors provide more details on the purpose of these metrics in the context of RILe?

- The authors mentioned RILe improves the computational efficiency compared to other IRL works. However, RILe needs to train an extra trainer network compared to GAIL. Is there a quantitative analysis on this?

References:

[1] Pomerleau, D. A. (1991). Efficient training of artificial neural networks for autonomous navigation. Neural computation, 3(1), 88-97.

[2] Papagiannis, G., & Li, Y. (2022, September). Imitation learning with sinkhorn distances. In Joint European Conference on Machine Learning and Knowledge Discovery in Databases (pp. 116-131). Cham: Springer Nature Switzerland.

[3] Chi, C., Xu, Z., Feng, S., Cousineau, E., Du, Y., Burchfiel, B., ... & Song, S. (2023). Diffusion policy: Visuomotor policy learning via action diffusion. The International Journal of Robotics Research, 02783649241273668.

[4] Lai, C. M., Wang, H. C., Hsieh, P. C., Wang, Y. C. F., Chen, M. H., & Sun, S. H. (2024). Diffusion-Reward Adversarial Imitation Learning. arXiv preprint arXiv:2405.16194.

[5] Torabi, F., Warnell, G., & Stone, P. (2018). Behavioral cloning from observation. arXiv preprint arXiv:1805.01954.

[6] Liu, M., Zhu, Z., Zhuang, Y., Zhang, W., Hao, J., Yu, Y., & Wang, J. (2022). Plan your target and learn your skills: Transferable state-only imitation learning via decoupled policy optimization. arXiv preprint arXiv:2203.02214.

[7] Torabi, F., Warnell, G., & Stone, P. (2018). Generative adversarial imitation from observation. arXiv preprint arXiv:1807.06158.

[8] Huang, B. R., Yang, C. K., Lai, C. M., Wu, D. J., & Sun, S. H. (2024). Diffusion Imitation from Observation. arXiv preprint arXiv:2410.05429.

### Soundness
2

### Presentation
2

### Contribution
2
