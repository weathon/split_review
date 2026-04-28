# Hierarchical World Models as Visual Whole-Body Humanoid Controllers

- Decision: Accept
- Avg Score: 6.50
- Scores: 8, 8, 5, 5

## Abstract
Whole-body control for humanoids is challenging due to the high-dimensional nature of the problem, coupled with the inherent instability of a bipedal morphology. Learning from visual observations further exacerbates this difficulty. In this work, we explore highly data-driven approaches to visual whole-body humanoid control based on reinforcement learning, without any simplifying assumptions, reward design, or skill primitives. Specifically, we propose a hierarchical world model in which a high-level agent generates commands based on visual observations for a low-level agent to execute, both of which are trained with rewards. Our approach produces highly performant control policies in 8 tasks with a simulated 56-DoF humanoid, while synthesizing motions that are broadly preferred by humans.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes a hierarchical world model for whole-body humanoid control based on RL. The framework separates high-level and low-level control, with a high-level puppeteering agent providing commands for a pre-trained low-level tracking agent, which executes detailed joint movements. Key contributions include a task suite for visual humanoid control, a hierarchical control model using RL without pre-defined reward designs, metrics for "naturalness" in motion, and thorough analysis through ablation studies and user preference tests.

### Strengths
1. The hierarchical world model, which integrates high-level visual guidance with low-level proprioceptive control, is novel in its simplicity and efficacy, especially in achieving natural motion without predefined rewards or skill primitives.

2. Puppeteer advances visual whole-body humanoid control by setting new standards for naturalness and efficiency in motion synthesis. The zero-shot generalization to unseen tasks demonstrates the model’s potential for practical application.

### Weaknesses
1. Lack of low-level tracking performance evaluation. There is no evaluation or metrics for the tracking accuracy of success rate. There are several works both from simulated avatars community [1,2] and real-world humanoids [3,4] that evaluate the tracking performance. I am supurised that these works are not mentioned and their metircs are not used for evaluation in this work.


[1] Luo, Z., Cao, J., Kitani, K., & Xu, W. (2023). Perpetual humanoid control for real-time simulated avatars. In Proceedings of the IEEE/CVF International Conference on Computer Vision (pp. 10895-10904).

[2] Won, J., Gopinath, D., & Hodgins, J. (2022). Physics-based character controllers using conditional vaes. ACM Transactions on Graphics (TOG), 41(4), 1-12.

[3] Cheng, X., Ji, Y., Chen, J., Yang, R., Yang, G., & Wang, X. (2024). Expressive whole-body control for humanoid robots. arXiv preprint arXiv:2402.16796.

[4] He, T., Luo, Z., Xiao, W., Zhang, C., Kitani, K., Liu, C., & Shi, G. (2024). Learning human-to-humanoid real-time whole-body teleoperation. arXiv preprint arXiv:2403.04436.


2. The lack of interface design discuss. The paper proposes to use high-level controller to generate positions of tracking keypoints. This might be one way for reuse the low-level skills for downstream tasks, but there are many existing designs in prior works [5] [6] that not are compared in this work. To me, the idea of training low-level tracking policy for skills reuse is a long-standing idea, but the interface of this hierarchy matters a lot. I'd love to see more comparison on this.

[5] Tessler, C., Kasten, Y., Guo, Y., Mannor, S., Chechik, G., & Peng, X. B. (2023, July). Calm: Conditional adversarial latent models for directable virtual characters. In ACM SIGGRAPH 2023 Conference Proceedings (pp. 1-9).

[6] Luo, Z., Cao, J., Merel, J., Winkler, A., Huang, J., Kitani, K., & Xu, W. (2023). Universal humanoid motion representations for physics-based control. arXiv preprint arXiv:2310.04582.

3. The source of naturalness is unclear. The low-level tracking policy might be conditioned on human motion pirors, but if the tracking policy is good enough, it should be able to produce what TD-MPC2 achieves. Also, if the advantage of this paper is sample-efficiency and naturalness, a key baseline here would TD-MPC2+ AMP, which is missing. That being said, all the experimental results make sense to me, but the key comparison experiments are missing somehow.

### Questions
All my questions are listed in the weakness part.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper explores the high-dimensional humanoid control from visual observations. Specifically, the proposed approach is based on two RL-trained agent models.  High-level agent generates reference trajectories from visual observations. Low-level agent focuses on tracking these trajectories using current low-dimensional state information. The proposed method demonstrated enhanced natural motion control of a 56-DoF simulated humanoid, outperforming baseline models according to experimental results and a user study.

### Strengths
1. The research addresses a significant and practical challenge in generalist agents: controlling a humanoid agent from visual observations using generalizable world models.
2. The methodology involves training a low-level agent on trajectory tracking that is adaptable across a range of control tasks, showing promising generalizability.
3. A high-level agent controls the humanoid from visual observations, a task-specific but broadly applicable approach in real-world scenarios.
4. A user study validates that the proposed method enables more natural humanoid control, which is preferred by participants.

### Weaknesses
1. The evaluation heavily relies on the "naturalness" of movements, which depends on subjective human judgments of what is considered "human-like." This criterion, while important, may not fully evaluate the feasibility of such motions in actual humanoid robots, which face different kinematic and dynamic constraints than humans. Specifically, the paper lacks a clear definition of 'naturalness' beyond qualitative human perception, making it difficult to objectively assess the method's performance in terms of physical plausibility and stability. The absence of quantitative metrics that directly correlate with real-world robotic control, such as joint torques, energy consumption, or stability margins, raises concerns about the practical applicability of the approach.
2. Based on Figure 5, the episodic return of the baseline TD-MPC2 is comparable or superior to the proposed method across most tasks. It would be beneficial to evaluate other performance metrics such as survival rates or survival times on the final-trained model to provide a more comprehensive evaluation. The episodic return, while a common metric, does not capture the full picture of the agent's performance. Metrics like success rate in reaching a goal, or the consistency of performance across multiple trials, would provide a more robust understanding of the method's capabilities.
3. The paper claims "Zero-shot generalization to larger gap lengths," yet does not compare these results with baseline methods. Including comparative generalization data for the baseline TD-MPC method would strengthen claims of superior generalization. The lack of a direct comparison makes it difficult to ascertain whether the observed generalization is a unique attribute of the proposed method or a general characteristic of the training environment. A quantitative analysis of the generalization performance, such as the performance drop-off as the gap length increases, would be beneficial.
4. Minor issue:
a) Resource Efficiency: The two level agents training approach might require significantly more time and resources than single-agent baselines. Comparing memory usage, training duration, and inference times across methods would provide critical insights into the practicality of the proposed method. The paper should provide a detailed breakdown of computational costs, including training time per epoch, memory footprint of the models, and inference time for both agents.
b) Model Reusability: The low-level tracking agent is described as reusable across tasks but it is unclear if this model is applicable only to 56-DoF humanoids or if it can be adapted to different control dimensions. The paper should clarify the limitations of the low-level agent and discuss the potential for transfer learning to other humanoid models with varying degrees of freedom.
c) There is a typo in the Problem Formulation section (page 2). The environment transition function should be denoted as L, not S.

### Questions
1. How relevant is the metric of "naturalness" in real-world humanoid control, and is it sufficient to evaluate humanoid trajectory tracking effectively?
2. It would be beneficial to include a comparative study on the survival rate or survival time when using the final-trained model
3. It would be helpful to include baseline experiments focused on "zero-shot generalization."
4. Please provide details on memory usage, training time, and control (or inference) time across different methods.
5. Is the low-level tracking effectively transferred to control different humanoid models with varying degrees of freedom?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
Post rebuttal | the authors did a good job in the rebuttal phase to include some necessary baselines.

The paper improved a lot during the rebuttal phase and now includes some of the necessary baselines to validate the method. When I asked the authors about measures to ensure fairness in the new baseline experimentation, they argued that the considered MBRL algorithms are known to be robust to hyperparameter changes, which is true but not a valid argument for a simple reason: if an algo is robust to hyperparameter choice, doesn't mean that it cannot benefit from tuning. As I believe the proposed method was subject to some tuning during development time (like any ML method is), measures to ensure fairness of comparison would be necessary. Additionally, the baselines added during rebuttal just scratch the surface of hierarchical RL approaches and are themselves made up baselines combining known high-level algorithms with low-level TD-MPC. While these baselines are very important and necessary to understand the method, including standard baselines from the literature would strongly improve the paper and increase its impact. I highly encourage the authors to do that. I will be raising my score but only to a 5, as I still think the paper is not ready for publication at ICLR, despite the good improvements.

---

The paper proposes "Puppeteer" a hierarchical decision-making approach tailored for visual whole-body humanoid control. The proposed method trains two separate world models for high-level and low-level control purposes. The low-level world model is concerned with tracking reference joint-level trajectories produced by the high-level controller. The high-level controller can additionally be conditioned on visual data. Both world models are based on TD-MPC2 which is a sampling-based MPC approach with learned decoder-free world models (with deterministic-only components) and a learned value function for long-horizon value assignment. TD-MPC2 is further extended to include a termination encoder head as is common in other model-based RL methods such as dreamer. The paper claims that the proposed method achieves results that are mostly comparable to TD-MPC2's results, while the plots show significantly worse results than TD-MPC2 in terms of asymptotic performance. The main advantage of the method is that it produces more natural and human-like motion, which was quite well shown in the experiments. The paper also ablates multiple design choices.

### Strengths
- the paper is generally well-written and an enjoyable read, I also liked the figures and plots.
- the proposed approach is very interesting and promising and is a natural next step to extend the TD-MPC2 framework.
- the method is evaluated on multiple humanoid tasks including environments with only proprioception as well as others with additional visual observations.
- the ablations nicely evaluate the role of the different design choices of the method. I especially appreciate the study of the role of planning in the architecture.
- the baselines include model-free and model-based approaches.

### Weaknesses
 - the method section misses a detailed motivation for why hierarchy improves the naturalness of the motions.
- the method section misses a detailed explanation concerning the exact usage of the high-level commands (see question 2).
- the paper introduces a hierarchical version of td-mpc2, the baselines however do not include a single hierarchical RL approach, I would at least consider including a hierarchical implementation of dreamer [1].
- [main weakness] The results of the paper are weak, at least in the current way in which they are presented. While the method is interesting and makes sense, the results show that it significantly underperforms TD-MPC2 but improves the naturalness of the produced motions. That would have been an acceptable tradeoff if the paper could justify why the proposed method improves the naturalness of the motions with intuitions and ideally, some experiments that validate them.

** Minor issues:**

- line 079 end-effector joints --> end-effector links.
- punctuation is missing in the equations (but I understand that this is a matter of style, so no pressure).

Overall the paper proposes an interesting approach, but it currently fails to showcase the benefits of this approach. I am willing to raise my score if this aspect is properly addressed.

### Questions
- the main advantage of this method over TD-MPC2 is the resulting naturalness of the motions. Can the authors elaborate on why they think the proposed method improves this aspect? (here I mean further explaining the reward hacking argument made in the paper and perhaps including other arguments that could make sense)
- can the authors elaborate on how the low-level policies exactly track the high-level commands? Since the low-level receives a sequence of commands does it keep using $c_t$ until the tracking error is below a threshold, or is it only used for a single step independent of the outcome of applying the one-step action?
- on the methods side of things, the paper extends td-mpc2 to a hierarchical architecture. Can the authors compare the method to the hierarchical version of Dreamer [1]?

[1] Hafner, Danijar, et al. "Deep hierarchical planning from pixels." Advances in Neural Information Processing Systems 35 (2022)

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents a novel hierarchical world model Puppeteer designed for visual whole-body humanoid control, which operates without relying on predefined skill primitives, reward designs, or temporal abstractions. This paper also introduces a new task suite consisting of eight challenging tasks for evaluating humanoid control, demonstrating that Puppeteer produces more natural and human-like motions preferred by human evaluators in comparison with model-free and model-based RL baselines.

### Strengths
* This paper is well-organized, well-written, and includes clear figures.
* A well-designed hierarchical control framework (although the idea is not novel) is implemented to control humanoid motion in a more natural way: the high-level agent generates commands given visual observations, and the low-level agent is responsible for executing them.
* The proposed visual whole-body high-dimensional humanoid control benchmark enrich the evaluation platforms in the area.

### Weaknesses
 * The paper primarily evaluates the visio-locomotive capabilities of the humanoid model. It could be better to expand the range of tasks to include more diverse scenarios that test different aspects of humanoid capabilities.
* More baseline method should be compared, like HumanoidOlympics. This paper also uses human motion data and reinforcement learning to train natural humanoid motions in various tasks.

* The paper does not provide a compelling comparison of the generated motions with real motion capture data in the user study, instead only comparing with regular RL methods. This limits the ability to assess the true naturalness of the generated motions.

### Questions
* Although the motion produced by Puppeteer is more natural, why does the humanoid robot always lean forward while moving?
* Can the proposed method be validated in real-world experiments?
* Can this framework be generalized to manipulation tasks in HumanoidOlympics?

### Soundness
3

### Presentation
3

### Contribution
2
