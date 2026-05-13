# Reward-free World Models for Online Imitation Learning

- Decision: Reject
- Scores: 3, 6, 6, 6

## Abstract
Imitation learning (IL) enables agents to acquire skills directly from expert demonstrations, providing a compelling alternative to reinforcement learning. However, prior online IL approaches struggle with complex tasks characterized by high-dimensional inputs and complex dynamics. In this work, we propose a novel approach to online imitation learning that leverages reward-free world models. Our method learns environmental dynamics entirely in latent spaces without reconstruction, enabling efficient and accurate modeling. We adopt the inverse soft-Q learning objective, reformulating the optimization process in the Q-policy space to mitigate the instability associated with traditional optimization in the reward-policy space. By employing a learned latent dynamics model and planning for control, our approach consistently achieves stable, expert-level performance in tasks with high-dimensional observation or action spaces and intricate dynamics. We evaluate our method on a diverse set of benchmarks, including DMControl, MyoSuite, and ManiSkill2, demonstrating superior empirical performance compared to existing approaches.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces an extension of the TD-MPC framework for imitation, specifically within the inverse reinforcement learning context. Rather than learning an explicit reward function, the authors propose learning implicit rewards in the Q-function space. They use the implicitly learned reward function, along with learned world models, to perform MPC in the latent space. The results demonstrate state-of-the-art performance when compared to other baselines.

### Strengths
- the idea is interesting. 
- I believe that (when done right), this is a scaleable approach.

### Weaknesses
 - the paper is written poorly. Many conclusion done lack causality and need further clarification (see below).
- mathematically there seem to be many issues (see questions)
- I believe many experiments use badly tuned baselines (see questions)



### Problematic Causality in writing:

- “By utilizing an inverse soft-Q learning objective for the critic network (Garg et al., 2021), our method derives rewards directly from Q-values and the policy, effectively rendering the world model reward-free. This novel formulation mitigates key challenges in IL, including out-of-distribution errors and bias accumulation.” → Inverse Q-learning is not the novel formulation that mitigates these problems, these are general advantange of inverse RL. 
- “ In the objective function, p0 is the initial distribution of states. In this way, we can perform imitation learning by leveraging actor-critic architecture.” → unclear why the initial state distribution should allow to leverage actor-critic architectures. Also, p0 is not mentioned anywhere in the equations. 
- “, and α is a scalar coefficient to ensure stable training and prevent overfitting.” thats a bit unspecific. More explanation is needed or add a citation. 
- Section 4, first paragraph. The storyline is not very clear. “In conventional latent world models, an explicit reward function is typically used to map latent representations and actions to observed reward data.  However, in imitation learning, the model is limited to learning from a finite set of expert state-action demonstrations, making it difficult for traditional world models to directly perform imitation learning. To address this limitation, we propose a reward-free world model that learns solely from expert demonstrations and environment interactions, without requiring explicit reward data. ” The authors first note that rewards are often learned alongside world models during training. They then argue that in imitation learning, conventional world models are typically used without rewards and only on expert data (not true), making imitation challenging. To address this, the authors propose their solution: training a world model without rewards.

### questions:
 - Equation (4): There seem to be an error in the expectation over the policy state-action distribution. What is V(s) should be Q(s, a). Or some part of the derivation is missing.
- “Compared to Eq.6, the key difference is the second term of the objective, which computes the original value difference E(st,at,s ′ t )∼Bπ [V π (zt) − γV π (z ′ t )] using only the representation of the initial state s0.” This sentence does not explain the transition from Eq. 6 to 12. And still What is V(s) should be Q(s, a).
- In Eq. 12, I think that the sum should be inside the expectation.
- In Eq. 15, the V π (zt) − γV π (z ′ t) is used for the reward. This can not be a valid reward signal, since it is just equivalent to a reward shaping term, which is policy invariant. 
- On what task was the ablation study done, high-dim or low dim? 
- I believe there is an important work missing [1]. This work provides a bridge between SQIL and IQ-Learn, showing that the underlying problems are equivalent, a provide a solution to the instability also encountered during this paper. 


Minor Things:
- Line 212: typo → Q twice

### Questions
- Equation (4): There seem to be an error in the expectation over the policy state-action distribution. What is V(s) should be Q(s, a). Or some part of the derivation is missing.
- “Compared to Eq.6, the key difference is the second term of the objective, which computes the original value difference E(st,at,s ′ t )∼Bπ [V π (zt) − γV π (z ′ t )] using only the representation of the initial state s0.” This sentence does not explain the transition from Eq. 6 to 12. And still What is V(s) should be Q(s, a).
- In Eq. 12, I think that the sum should be inside the expectation.
- In Eq. 15, the V π (zt) − γV π (z ′ t) is used for the reward. This can not be a valid reward signal, since it is just equivalent to a reward shaping term, which is policy invariant. 
- On what task was the ablation study done, high-dim or low dim? 
- I believe there is an important work missing [1]. This work provides a bridge between SQIL and IQ-Learn, showing that the underlying problems are equivalent, a provide a solution to the instability also encountered during this paper. 


Minor Things:
- Line 212: typo → Q twice


[1] Al-Hafez et. al. LS-IQ: Implicit Reward Regularization for Inverse Reinforcement Learning

### Soundness
1

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper looks at the problem of model-based inverse reinforcement learning. The authors propose a "reward-free" approach by combining reward-free model-free imitation learning (IQ-learn) with learned dynamics models. The proposed method, IQ-MPC, is shown to be more sample efficient in comparison to IQ-learn across a range of continuous control tasks. 

The contributions are:
1. A novel model-based, reward-free IRL algorithm
2. Empirical validation across a range of  both state-based and vision-based environments, including DMControl for locomotion, MyoSuite for dexterous hand manipulation, and ManiSkill2 for object handling
3. Ablations showing that the method is performant even as the number of expert trajectories is reduced.

### Strengths
This paper proposes a new approach to interactive imitation learning that is model-based and reward-free. This results in sample-complexity wins (from the model) and stability (from the lack of adversarial reward training). The paper also shows that the methods scale across different environments, including visual imitation learning tasks.

Originality: The work presents a unique integration of IQ-Learn’s inverse soft-Q learning with model predictive control, enabling a reward-free formulation that sidesteps adversarial reward estimation.

Quality: Empirical results support the approach’s benefits in diverse settings, achieving stable, expert-level performance on a range of tasks from DMControl and MyoSuite to ManiSkill2.

Clarity: The paper is easy to follow, and the algorithm does a good job of clearly explaining training and inference procedures. The results section is well organized. 

Significance: The proposed method is practical and the reward-free model-based learning is likely to scale well.

### Weaknesses
 **Fundamental technical concern:** The nice thing about recovering reward functions in IRL is that rewards transfer while Q doesn't. The Q function entangles reward with environment dynamics. I would imagine as the model changes across iterations, the Q function in the worst case may fail to transfer. I would love to be convinced by math that this is not the case (it may not have manifested in the limited set of experiments). Can the authors provide theoretical analysis demonstrating how their IQ-MPC handles Q-function transfer across model iterations, or to discuss potential failure modes?

**Comparison to baselines:** The paper would benefit from broader comparisons, especially with other model-based and model-free IRL approaches, to support claims of stability and efficiency. For example, how does it compare to hybrid inverse reinforcement learning (both model-free and model-based) https://arxiv.org/pdf/2402.08848v1 which have SOTA results on Mujoco and D4RL environments. Could the authors run against the baselines in https://arxiv.org/pdf/2402.08848v1?

**Computational overhead:** IQ-MPC has a more expensive inference time process than the baselines, making the comparisons unfair. Perhaps the planner can be distilled into the same policy class to have a fair comparison with model-free baselines. Additionally, including the number of interactions in the model would be helpful. One would expect IQ-MPC to have lower interactions with environment, but perhaps a larger (world + model) interactions compared to IQ-Learn. 

**Demonstrations efficiency:** The high number of expert trajectories required (100-500) contrasts with prior work, such as IQ-Learn’s ability to learn with as few as 5-10 trajectories in MuJoCo. It would be good to resolve this discrepancy, perhaps running IQ-Learn in the same mujoco setting as IQ-Learn and hybrid inverse reinforcement learning baselines. 

**Limited novelty:** IQ-MPC appears as a blend of IQ-Learn’s inverse soft-Q learning and TD-MPC’s model predictive control framework, without substantial originality beyond this combination. While the reward-free setup is interesting, the paper could be strengthened by examining distinct advantages from this integration. This could be done via an apples-to-apples comparison with reward-based model-based IRL. 

**Scope of “State-Only” data:** The mention of “state-only” data in the appraoch is misleading, as state-action pairs are needed to learn the Q-function and policy. Clarifying this would prevent confusion.

**Incomplete related work:** The paper does not cite fundamental papers like Ziebart’s max-entropy IRL framework or recent model-based IRL methods that directly relate to the current work. Including these citations would better contextualize IQ-MPC within the IRL landscape. Adding recent model-based IRL techniques to related work would help readers understand how IQ-MPC compares and advances beyond existing methods.
- Ziebart, B. D., Maas, A. L., Bagnell, J. A., & Dey, A. K. (2008, July). Maximum entropy inverse reinforcement learning. In Aaai (Vol. 8, pp. 1433-1438).
- Ren, J., Swamy, G., Wu, Z. S., Bagnell, J. A., & Choudhury, S. (2024). Hybrid inverse reinforcement learning. arXiv preprint arXiv:2402.08848.
- P. Englert, A. Paraschos, J. Peters, and M. P. Deisenroth. Model-based imitation learning by probabilistic trajectory matching. In 2013 IEEE International Conference on Robotics and Automation, pp.1922–1927. 2013. doi:10.1109/ICRA.2013.6630832.
- A. Hu, G. Corrado, N. Griffiths, Z. Murez, C. Gurau, H. Yeo, A. Kendall, R. Cipolla, and J. Shotton.
Model-based imitation learning for urban driving. arXiv preprint arXiv:2210.07729, 2022.
- R. Kidambi, J. Chang, and W. Sun. Mobile: Model-based imitation learning from observation alone, 2021.
- N. Baram, O. Anschel, and S. Mannor. Model-based adversarial imitation learning. Conference on Neural Information Processing Systems, 2016.
- M. Igl, D. Kim, A. Kuefler, P. Mougin, P. Shah, K. Shiarlis, D. Anguelov, M. Palatucci, B. White, and S. Whiteson. Symphony: Learning realistic and diverse agents for autonomous driving simulation. arXiv preprint arXiv:2205.03195, 2022.
- Z.-H. Yin, W. Ye, Q. Chen, and Y. Gao. Planning for sample efficient imitation learning. Conference on Neural Information Processing Systems, 2022.
- R. Rafailov, T. Yu, A. Rajeswaran, and C. Finn. Visual adversarial imitation learning using variational models, 2021.
- B. DeMoss, P. Duckworth, N. Hawes, and I. Posner. Ditto: Offline imitation learning with world models. 2023.
- W. Zhang, H. Xu, H. Niu, P. Cheng, M. Li, H. Zhang, G. Zhou, and X. Zhan. Discriminator-guided model-based offline imitation learning. Conference on Robot Learning, 2023.

Edit: Increased score during rebuttal period

### Questions
The "Weakness" section contains all questions I had. 

Other clarifications:
1. Line 155: there is no p_o in the equation above
2. Line 200-204: I failed to understand the argument at all. One is always free to learn dynamics models without reward?

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
3

### Summary
The manuscript presents a novel approach to online imitation learning (IL) that leverages reward-free world models, specifically focusing on latent-space representations rather than explicit rewards. The proposed model, IQ-MPC, utilizes inverse soft-Q learning in the policy space, sidestepping traditional optimization in the reward-policy space, which has previously led to instability in online IL applications. IQ-MPC aims to demonstrate robust, expert-level performance across high-dimensional and complex control tasks using a combination of latent dynamics and model predictive control (MPC) in the absence of explicit reward functions.

### Strengths
Novelty in Reward-Free Approach: The idea of removing reward dependence by operating in latent space addresses a significant challenge in imitation learning, making the model highly adaptable to complex environments with intricate dynamics.

Comprehensive Evaluation: Experiments conducted on a variety of benchmarks, such as DMControl, MyoSuite, and ManiSkill2, demonstrate the model's capabilities across tasks, including both state-based and visual IL tasks.

### Weaknesses
1. It is recommended that the author further explain the experimental results in 5.2, such as why the model restores rewards closer to the ground-truth rewards when the medium, and why the model prediction variance increases sharply when the real rewards are high; encourage the author to conduct further experiments to illustrate the extent to which the deviation of reward prediction affects the results of MPPI;

2. The author mentioned that the main advantages of the world model are sampling complexity and its future planning ability. The manuscript focuses on its excellent planning ability but lacks comparison with the baseline in sampling complexity. It is recommended to expand the experiment in 5.3 and compare IQ-MPC with the baseline in the case of a small amount of expert data;

3. Section 3 gives a general mapping of the inverse Bellman equation to recover rewards. Experiments can be added to reflect the performance of other baseline methods in reward recovery.

### Questions
Please refer to weakness.

I have made every effort to review this paper; however, I would appreciate it if the area chair could consider that its content is not closely aligned with my expertise when evaluating all the reviews.

### Soundness
3

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
This paper broadly considers problems in the regime of interactive imitation learning by learning with learned world models. It differs from previous model-based imitation learning techniques (e.g. model based inverse reinforcement learning) in that the model does not explicitly learn a reward function, and instead does optimization within the space of Q-functions. In essence, this work seems to lift the insights from IQ-Learn [1] to the space of models-based learning.

[1] Garg, Divyansh, et al. "Iq-learn: Inverse soft-q learning for imitation." Advances in Neural Information Processing Systems 34 (2021): 4028-4039.

### Strengths
* This paper is well structured, with a clearly written formulation and decent benchmarks/baselines across which empirical results are shown. The experiments are also thoughtful, covering a variety of questions such as design ablations, impact of number of expert demonstrations, and correlation with reward. The environments for such evaluations are also chosen so as to include both locomotion and manipulation tasks.
* The explanation of the proposed soft-Q learning objective within a learned model is clear and well-grounded in prior work.
* The proposed method shows compelling sample efficiency gains over selected baselines, and addresses the instability of prior interactive IL approaches. The authors also document clearly their use of various techniques to improve training stability.
* The method demonstrates good performance in both state-based and image-based environments.
* The proposed method performs reasoning entirely in latent space, and is not limited by a reconstruction objective when learning the world model, which allows it to handle high-dimensional input such as images without suffering huge computational overhead from the reconstruction objective.

### Weaknesses
### High Level Feedback:
* The paper introduces a novel framework of reward-free world model, but the main contributions seem to build heavily upon existing work such as IQ-Learn [1] and TD-MPC [2, 3]. I recommend making more explicit highlights of any new theoretical insights or mathematical contributions beyond the removal of reward modeling, or highlighting the transferrable empirical insights from the methodology section. The core idea of using a learned model to perform planning with a learned Q-function is not entirely novel, and the paper would benefit from a more detailed discussion of the specific technical contributions that differentiate it from existing methods. For instance, how does the proposed method address the challenges of compounding errors in model-based planning, and what are the theoretical guarantees associated with the learned Q-function in the context of a learned model?
* The authors claim that reward-based world models lead to training instability could be supported more strongly in the empirical results. In particular. Relatedly, it has been shown that IQ-Learn [1] is rather unstable in prior works, so it would be nice to see how this reward-free world model compares to other works focused on sample-efficiency in online IL (both model-free and model-based), such as [4]. It's crucial to demonstrate empirically that the proposed method offers a significant improvement in stability and sample efficiency compared to existing online imitation learning methods, especially in scenarios with limited expert demonstrations. The comparison should also include a discussion of the computational trade-offs between model-based and model-free approaches in this context.
* The method mentions the use of MPPI for planning in latent space, which could be potentially computationally demanding due to the large number of sampled trajectories. It would be nice to see a more detailed analysis or mentioning of the computational overhead of the proposed method compared to baselines, especially during real-time execution. It could be helpful for the authors to provide some mentioning of empirical metrics for the computational overhead, perhaps in comparison to baselines. The paper should provide a more thorough analysis of the computational cost associated with the proposed method, including the time complexity of the MPPI planning algorithm and the memory requirements for storing the learned model and Q-function. This analysis should also compare the computational overhead with other baselines, particularly in real-time execution scenarios.
* While the empirical results demonstrates efficiency comparisons with other online IL methods, it does not show the performance of offline IL methods. In the realizable setting (with 100 expert demonstrations), how does an offline IL method such as Diffusion Policy [5] perform? It is important to understand the performance of offline imitation learning methods in the same setting, especially since these methods do not suffer from the same stability issues as online methods. The paper should include a comparison with offline methods to provide a more complete picture of the proposed method's performance.

### Low Level Technical Feedback:
* In the first paragraph to Section 4, the authors claim in lines 202-204 that they propose learning "a reward-free world model... without requiring explicit reward data". But the next sentence from lines 204-206 proceed to state, "our model can decode dense rewards for the environment, allowing it to **learn a reward function** through...". This seems self-contradictory, so I recommend authors clean up the language such that it is consistent. The language used to describe the reward function learning is confusing and needs to be clarified. The authors should clearly distinguish between learning a reward function and learning a Q-function, and explain how the proposed method avoids the need for explicit reward data while still being able to estimate rewards.

### Questions
1. A number of prior works seem to observe the instability of IQ-Learn in the regime of low expert demonstrations. The proposed approach seems to handle this instability better, despite following a similar framework. I am curious to hear why the authors posit this to be the case? 
2. I am curious how adding noise to the environment dynamics will affect the performance of all methods and baselines? It seems that prior work has seen these Q-function based learning methods (IQ-Learn in particular) to suffer from stochastic transition dynamics [1].
3. I appreciate the detailing of the hyperparameters used in the appendix. How sensitive is the performance of IQ-MPC to changes in these hyperparameters?
4. As mentioned in the weaknesses section, it would be nice to see a comparison to other online IL baselines such as those in [1], as well as offline BC baselines such as those in [2]. In particular, do offline BC/other online IL methods already come close to expert performance in the case of ~100 expert demonstrations? How about in the case of image-based inputs? 


[1] Ren, Juntao, et al. "Hybrid inverse reinforcement learning." ICML (2024).

[2] Chi, Cheng, et al. "Diffusion policy: Visuomotor policy learning via action diffusion." The International Journal of Robotics Research (2023): 02783649241273668.

### Soundness
3

### Presentation
3

### Contribution
2
