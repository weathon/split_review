# Skill-based Safe Reinforcement Learning with Risk Planning

- Decision: Reject
- Avg Score: 3.75
- Scores: 3, 3, 6, 3

## Abstract
Safe Reinforcement Learning (Safe RL) aims to ensure safety when an RL agent conducts learning by interacting with real-world environments where improper actions can induce high costs or lead to severe consequences. In this paper, we propose a novel Safe Skill Planning (SSkP) approach to enhance effective safe RL by exploiting auxiliary offline demonstration data. SSkP involves a two-stage process. First, we employ PU learning to learn a skill risk predictor from the offline demonstration data. Then, based on the learned skill risk predictor, we develop a novel risk planning process to enhance online safe RL and learn a risk-averse safe policy efficiently through interactions with the online RL environment, while simultaneously adapting the skill risk predictor to the environment. We conduct experiments in several benchmark robotic simulation environments. The experimental results demonstrate that the proposed approach consistently outperforms previous state-of-the-art safe RL methods.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper presents a novel approach using learned skills to improve online exploration in CMDPs given available offline data. In the offline phase, the presented method leverages the algorithm presented in [1] to learn skills as high-level actions. To enable safe learning, the authors employ a safety classifier $P_\xi(c|s_t,z_t)$ that takes as input $s_t$ and the skill $z_t$ using a similar PU learning approach similar to [2]. In the online exploration phase, the authors use SAC to learn a skills policy $\pi_\theta(z_t | s_t)$ to maximize rewards. In each environment step, the learned skills policy $\pi_\theta(z_t | s_t)$ is used to initialize the plan for a risk planner based on CEM. The planner optimizes for safe skills by minimizing the safety classifier cost. In the experimental section, the paper is compared to recovery RL[3], CPQ[4] and SMBPO[5]. 

The contributions of the paper can be summarized in the following points
- Exploring the skill learning method from [1] in a safe RL setting.
- Learning safety classifier using PU sampling.
- Introducing a risk planner to optimize safe skills by minimizing safety classifier costs.

[1] Pertsch, Karl, Youngwoon Lee, and Joseph Lim. "Accelerating reinforcement learning with learned skill priors." Conference on robot learning. PMLR, 2021.

[2] Xu, Danfei, and Misha Denil. "Positive-unlabeled reward learning." Conference on Robot Learning. PMLR, 2021.

[3] Thananjeyan, Brijen, et al. "Recovery rl: Safe reinforcement learning with learned recovery zones." IEEE Robotics and Automation Letters 6.3 (2021): 4915-4922.

[4] Xu, Haoran, Xianyuan Zhan, and Xiangyu Zhu. "Constraints penalized q-learning for safe offline reinforcement learning." Proceedings of the AAAI Conference on Artificial Intelligence. Vol. 36. No. 8. 2022.

[5] Thomas, Garrett, Yuping Luo, and Tengyu Ma. "Safe reinforcement learning by imagining the near future." Advances in Neural Information Processing Systems 34 (2021): 13859-13869.

### Strengths
The paper investigates an interesting setting of using offline data to enable RL for online exploration in constrained settings. This topic is crucial for enabling RL to explore in constrained real-world scenarios. In this setting, the paper explores using skills in safe RL, which is a relatively unexplored combination. The paper provides a clear description of the algorithm, which aids in understanding the advantages and disadvantages of the proposed method.

### Weaknesses
 - The impact of using skills needs to be ablated. It is unclear whether using skills in this context is useful. Is it beneficial to only act on each H step in a constrained setting? The authors should ablate using the presented planning and policy learning combination on low-level actions.

- The motivation behind using PU learning to learn the safety classifier is unclear. The authors use the classifier as a cost-to-go function, which would typically be learned as a safety critic using approximate dynamic programming [1,2]. It's unclear whether PU learning can be better than approximate dynamic programming in capturing the temporal aspect of the cost. Specifically, a safety critic, trained with temporal difference learning, would provide a more direct estimate of the cumulative risk associated with a given state and action, whereas the PU learning approach, as presented, seems to focus on immediate risk without explicitly considering future consequences.

- The paper claims to learn a safe policy when the policy is not optimized to learn safe behavior but to maximize rewards. This is clear in the ablation studies where the policy has a much worse behavior regarding adherence to constraints without the risk planner. However, the paper mentions learning a safe policy on multiple occasions, which needs to be clarified.

- Unfair comparison with baselines. SMBPO should also be pretrained to ensure a fair comparison. Even training it from scratch, SMBPO has very similar performance in 2 environments. Additionally, the recovery RL baseline is not tuned to the benchmark used. However, recovery RL is sensitive to the $\epsilon$ parameter that triggers the recovery policy [1]. Even with an unfair comparison, recovery RL has a similar performance to the presented method in 2 environments. Also, recovery RL only uses the recovery policy (its version of the risk planner) when a trigger condition is fulfilled, unlike the presented method, where the risk planner is used in every step. It's thus hard to judge whether the use of skills is the real reason for the difference in performance or the use of planning in every environment step.

- The absence of an explanation on how the offline data was collected is a significant gap. Details such as the number of samples, the ratio of samples with constraint violations, and other relevant information are crucial for the sake of reproducibility and should be provided.

### Questions
- How would the method perform if we replaced skills with low-level actions? It's unclear whether the performance is due to using skills or a CEM planner to minimize constraint cost in every environment step.
- Why not use a safety critic similar to [1,2] instead of using PU learning for the safety classifier?
- In lines (19, 128, 307), you mention learning a safe policy $\pi_\theta$; however, as far as I understand, the policy only optimizes the policy to maximize rewards. Can you explain what makes the policy safe?
- Can you explain equation 7?
- Can you provide more details on offline data, including how it was collected and the percentages of constraint-violating samples in the data?

Additional remarks:

- The abbreviation PU in used in the abstract without prior introduction
- LfD is an abbreviation for Learning from Demonstrations, not Reinforcement Learning from Demonstrations (line 42)
- In line 218 in algorithm1, you mention you sample ($\mu_0, \Sigma_0$) from $q_\psi$, which contradicts the second paragraph in 4.2.1.
- in line 9 in algorithm, what exactly is pair $\mathcal{P}$?
- In the conclusion, you mention learning safe behavior patterns from demonstrations. However, the skill model is not optimized to teach safe skills, just skills as high-level representations of actions. I think this can be confusing.

[1] Thananjeyan, Brijen, et al. "Recovery rl: Safe reinforcement learning with learned recovery zones." IEEE Robotics and Automation Letters 6.3 (2021): 4915-4922.

[2] Srinivasan, Krishnan, et al. "Learning to be safe: Deep rl with a safety critic." arXiv preprint arXiv:2010.14603 (2020).

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper proposes a method that leverages additional offline data to train skills and a risk predictor and refines the risk predictor while collecting online data, ultimately training a skill-based policy. 
For safe exploration, the proposed method uses a risk planning strategy, similar to a cross-entropy method (CEM).

### Strengths
- The paper introduces the idea of using offline data for training skills and a risk predictor.
- The paper is well-organized and easy to read.

### Weaknesses
# Major Weaknesses
- The contributions are relatively limited.
    - Each proposed module (skills [1,2], risk predictors [3, 4, 5]) is from existing methods.
        - If there were any novel training techniques, the author should have highlighted them, but it seems there is nothing new.
    - The motivation for the proposed method is ambiguous, and in particular, it is unclear which parts of the proposed method improve upon existing methods (lines 44–48).
    - Also, there is no theoretical analysis to motivate it.
- The experimental validation is weak, with only four tasks and using just three seeds per task, which is insufficient for robust evaluation.
    - Additional experiments on safe RL benchmarks, such as Safety Gymnasium [6], are necessary for a comprehensive evaluation.
    - The baseline methods, primarily from 2021 to 2022, appear somewhat outdated, so it would be nice to include a state-of-the-art method.
- Ablation studies are not sufficient to show the roles of each module.
    - Although the current ablation study has focused on risk planning, it seems obvious that eliminating risk planning would result in unsafe outcomes, as it does not take into account costs when training the skill-based policy.
    - The training of the risk predictor and the learning of skills appear to be significantly influenced by the proportion of cost violations or the diversity of demonstrations. Therefore, a performance comparison based on different demonstrations seems essential.
    - Additionally, since using skills represents a distinct contribution, comparative experiments between employing a skill-based policy and using a direct-action policy are also necessary.

# Minor Weaknesses
- In line 178, it is essential to clarify that $\zeta$ in $P_\zeta(C|s_t,z_t)$ represents the neural network parameters to avoid confusion. 
- For reproducibility, Section 4.1 should include at least loss functions or the algorithms used for training the encoder and decoder of the skills.

### Questions
1. Given the inclusion of a planning module, this paper appears to suggest that execution time may increase as a potential drawback. Are there any results measuring execution times based on different planning parameters?

2. Is there a part of the method that improves skills online? If not, it seems that the initial skill sets the upper bound for performance.

3. When training a skill-based policy, there appears to be no component accounting for safety, which might result in a high likelihood of choosing actions far from safety during risk planning. How has this issue been addressed? According to lines 334–336, penalties are applied to encourage actions that are closer to a prior. Does this approach effectively resolve the concern?

### Soundness
2

### Presentation
2

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
The paper introduces a novel approach called Safe Skill Planning (SSkP) for safe reinforcement learning (Safe RL). SSkP enhances safe RL by leveraging offline demonstration data through a two-stage process. The first stage involves learning a skill risk predictor using Positive-Unlabeled (PU) learning from offline demonstrations. The second stage uses this predictor to develop a risk planning process that enhances online safe RL, learning a risk-averse safe policy efficiently while adapting the skill risk predictor to the environment. Experiments in various robotic simulation environments show that SSkP outperforms other state-of-the-art safe RL methods.

### Strengths
- The paper proposes a new method, SSkP, that combines skill learning with risk planning for safe RL.
- The approach uses a two-stage process that first learns from offline data and then applies it to online environments, which is efficient and reduces potential damage to physical environments.
- The risk planning process is a simple yet effective method for generating safer skill decisions, enhancing safe exploration and learning.
- The method adapts the skill risk predictor to online environments in real-time, showing the ability to learn and adjust on the fly.

### Weaknesses
 - The effectiveness of SSkP relies heavily on the quality and quantity of offline demonstration data, which may not always be available or reliable. Specifically, the performance of the risk predictor, a core component of SSkP, is directly tied to the representativeness of the offline data. If the demonstrations do not adequately cover the state space or include a sufficient variety of risky behaviors, the risk predictor may fail to generalize to unseen situations, leading to unsafe actions during online learning.
- The two-stage process and the integration of multiple components (skill model, risk predictor, risk planning) might make the approach more complex to implement and understand. The interaction between these components is not always straightforward, and the hyperparameter tuning required for each component could be challenging. Furthermore, the error propagation between the skill model and the risk predictor could lead to suboptimal performance if not carefully managed.
- The paper primarily focuses on robotic simulation environments, and it's unclear how well SSkP would generalize to other types of environments or real-world applications. The dynamics of the simulated environments may not fully capture the complexities of real-world scenarios, such as sensor noise, model inaccuracies, or unexpected disturbances. This raises concerns about the robustness and reliability of SSkP in practical applications.
- The paper does not discuss the computational cost of the risk planning process, which could be high, especially with large state and action spaces. The risk planning process involves evaluating multiple skill options based on the risk predictor, which could be computationally expensive, particularly in high-dimensional state and action spaces. This could limit the applicability of SSkP in real-time control scenarios.
-  As shown in the sensitivity analysis, the performance of SSkP decreases with smaller offline data sizes, indicating a potential weakness in scenarios with limited data. This sensitivity to data size is a significant limitation, as obtaining large, high-quality offline datasets can be difficult and costly in many real-world applications. The lack of robustness to smaller datasets makes SSkP less practical in data-scarce environments.

### Questions
- How does SSkP handle partially incorrect or noisy offline demonstration data?
- What are the computational requirements of SSkP, and how does it scale with the size of the state and action spaces?
- How does SSkP compare to other safe RL methods in terms of computational efficiency?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper considers safe reinforcement learning from demonstration problem where there is offline demonstration dataset available. The proposed method, SSkP, seeks to draw both skill encoder/policy and skill safety information from the offline data, and during online learning plan with the skill safety information to lower safety violations. The authors conduct experiments on four simulated MuJoCo environments and show SSkP can achieve higher performance in terms of performance-risk ratio, i.e., given the same amount of safety violation, SSkP’s performance outperforms. The paper is generally well-written and the experiments support the the paper’s claims, but I find important details about the method missing, and therefore wish authors to clarify.

### Strengths
1. The paper looks into an important topic of safety in RL learning process (not only the execution phase but also the training phase), and presents the novel algorithm, SSkP, with mild assumptions of offline data available (some data is labeled as unsafe while all other data is assumed unlabeled). 

2. The writing is high-quality; therefore, it is easy for me to follow the whole paper’s logic. The algorithm pseudocodes were very clear about what the procedures are.

### Weaknesses
1. [biggest question] Based on Algorithm 1 and 2, it seems the risk planning is just choosing the safest skill to activate given the current state without considering how the skill contributes to the task completion. Line 4 of algorithm2 passes in the policy and the risk predictor, but algorithm 1 does not utilize the policy at all and rather samples from the skill prior q_\psi. In this case, wouldn’t the agent just choose safe but task-irrelevant skills? For example, to avoid colliding with anyone, an autonomous vehicle would just stop and stay. This raises a significant concern about the method's ability to balance safety and task performance, as the risk planning mechanism appears to prioritize safety at the expense of progress towards the goal.

2. From my understanding, the online RL only updates the skill policy network that chooses skills based on state and keeps the skill policy that chooses actions based on state and skill fixed (this only learns from the offline dataset). Why? Do you assume the action policies learned from offline dataset are very good? How much demonstration was used in the experiments and has the authors done scale experiments with different amount of offline data? This lack of online adaptation for the action policy is a major limitation, as it restricts the agent's ability to refine its low-level control based on new experiences. The paper should provide more justification for this design choice and explore the impact of varying offline data sizes.

3. The paper seems to be lacking a “preliminary” section where the authors should show prior work that is directly utilized in the method, such as the PU learning and skill learning via skill-conditioned learning from demonstration. These are important prior knowledge to understand the whole method. More importantly, the paper currently mixes previous methods with its own, novel components, making it hard to judge the novel parts of the work. For example, it seems like the skill risk predictor is novel and all other skill learning from demonstration is using the previous work. However, the method to learn the skill risk predictor again is a prior method PU.

3.1. How is \lambda determined? It seems an essential hyperparameter for PU to work. The paper should provide a clear explanation of how this parameter is set and justify the chosen value.

3.2. In Equation 6, why don’t the authors consider allowing covariance? Covariance is an important factor for CEM to accurately represent the correct shape of the distribution. The use of a diagonal covariance matrix, while simplifying computation, may limit the expressiveness of the distribution and hinder the optimization process.

4. The experiment domains seem not diverse enough (all locomotion tasks) while there are many good safe RL benchmarks such as safety-gym and safety-gymnasium. The lack of diversity in the experimental domains limits the generalizability of the findings. The paper should include experiments on a wider range of tasks, including those with different safety constraints and dynamics.

4.1. Line 415 states “SMBPO demonstrates a similar inability as CPQ in terms of learning a good policy to maximize the expected reward”. I believe this is not true as the SMBPO final performance is very close to SSkP (much higher than CPQ), and the Table 1’s result on Ant shows that too. The claim about SMBPO's performance is inaccurate and should be revised to reflect the actual experimental results.

5. The related work is mostly comprehensive but lacks a clear description of how the current work distinguishes itself from prior work, in each of the paragraphs of the related work. I strongly recommend authors discuss this to show the uniqueness of the proposed approach. The related work section needs to be more specific in highlighting the novel aspects of the proposed method compared to existing approaches.

5.1. On line 96, the authors stated “Reinforcement Learning from Demonstration, also known as Imitation Learning” – I believe this is generally not the well-accepted definition of imitation learning. Imitation Learning generally refers to methods like behavior cloning and inverse reinforcement learning. Reinforcement Learning from Demonstration is a series of work on its own. The definition of Imitation Learning needs to be clarified to align with the established terminology in the field.

5.2. There has been work on extracting safety information from demonstrations, such as [1]. The authors could discuss the differences between their work and prior work.

### Questions
See weakness

### Soundness
4

### Presentation
3

### Contribution
2
