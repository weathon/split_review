# Neuron-level Balance between Stability and Plasticity in Deep Reinforcement Learning

- Decision: Reject
- Scores: 3, 3, 3, 3

## Abstract
In contrast to the inherent ability of humans to continuously acquire new knowledge, modern deep reinforcement learning (DRL) agents generally encounter a significant challenge: the stability-plasticity dilemma, which refers to the trade-off between retaining existing skills (stability) and learning new knowledge (plasticity). In this study, we propose Neuron-level Balance between Stability and Plasticity (NBSP) to tackle this challenge, by taking inspiration from the observation that both stability and plasticity are integrally linked to the expressive capabilities of networks, which are primarily determined by the behavior of individual neurons. To the best of our knowledge, this is the first work that addresses both stability and plasticity loss simultaneously in DRL at the level of neurons. Specifically, NBSP first (1) defines and identifies RL skill neurons that are crucial for knowledge retention through a goal-oriented method, and then (2) introduces a stability-plasticity balancing mechanism by employing gradient masking and experience replay techniques targeting these neurons to preserve the encoded memory related to existing skills while enhancing the learning capabilities of other neurons. Experimental results on the Meta-World and Atari benchmarks demonstrate that NBSP significantly outperforms existing approaches in balancing stability and plasticity. Furthermore, our findings underscore the pivotal role of the critic within this context, providing valuable insights for future research.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper makes three main contributions: (1) it introduces the concept of RL skill neurons, a novel approach specifically tailored to deep reinforcement learning, which identifies neurons crucial for retaining task-specific knowledge; (2) it proposes the Neuron-level Balance between Stability and Plasticity (NBSP) framework, utilizing gradient masking to balance stability and plasticity at the neuron level; and (3) it provides experimental validation on the Meta-World and Atari benchmarks, demonstrating that NBSP effectively preserves prior knowledge while adapting to new tasks.

### Strengths
1. The paper is well-written, presenting complex ideas clearly and understandably.
2. It introduces a novel method for identifying "activated" neurons, contributing a fresh perspective on neuron-level balancing between stability and plasticity in deep reinforcement learning. This approach, which targets specific neurons for skill retention and adaptability, is a noteworthy advancement in handling the stability-plasticity dilemma.

### Weaknesses
1. **Limited Experimental Scope and Scalability Concerns**:
    - While the method presents a promising approach to continual learning, the experimental setup explores only two task sequences, which limits insights into scalability. As the number of tasks in a sequence grows, tracking neurons specific to each task may pose scalability issues, particularly concerning memory overhead and computational complexity. The paper does not address how the method would scale with a significantly larger number of tasks, or how the identification of skill neurons would be affected by task overlap or interference. It would be insightful to extend the experiments to a sequence of approximately 10 tasks to demonstrate the method’s scalability and robustness in long-term continual learning settings. Furthermore, the current experiments do not explore the impact of different task distributions or the potential for catastrophic forgetting when the task sequence is significantly extended.
2. **Restricted Baseline Comparisons**:
    - The paper lacks comparisons with key baselines from reinforcement learning literature. Methods like [1], [2], and [3], commonly used in reinforcement learning, could provide a stronger basis for evaluating the relative effectiveness of the proposed approach. Specifically, the paper should compare against methods that explicitly address catastrophic forgetting in continual RL, such as replay-based methods or regularization techniques. Including such baselines would help contextualize the results and address any gaps in performance evaluation against established methods. The lack of comparison with these established techniques makes it difficult to assess the true novelty and effectiveness of the proposed approach.

### Questions
Please refer to the Weakness

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
4

### Summary
This paper proposes a new continual RL framework, **Neuron-level Balance between Stability and Plasticity (NBSP)**, to address the stability-plasticity dilemma in continual deep RL. NBSP integrates three core components: (1) **RL skill neurons**, (2) **gradient masking**, and (3) **experience replay**. The authors introduce a goal-oriented method to identify and quantify RL skill neurons, using a ranking and thresholding approach similar to dormant neurons. To mitigate forgetting, NBSP applies a gradient mask to parameters connected to those  skill neurons at the output side, preserving the critical parameters learned from the first task from alteration. Additionally, NBSP periodically samples experience from previous tasks as a rehearsal strategy to reinforce memory retention. The framework is evaluated on sequential task setups from Meta-World and Atari benchmarks, each consisting of two tasks.

### Strengths
- The paper addresses an important and relatively underexplored challenge in reinforcement learning by examining ways to balance stability and plasticity in a continual learning setting. The topic aligns well with the conference's core themes.

- The paper is clearly structured and well-organized, making it easy to follow and understand.

- Overall, the idea of addressing plasticity-stability trade-off at the neuron-level through identifying the RL skill neurons is interesting. The use of both neuron activation and goal-oriented behavior measures in the scoring function is somewhat novel. Neuron-level algorithms indeed present promising directions for future research in continual reinforcement learning.

### Weaknesses
1) **Comprehensive Review of Existing Approaches in Continual RL**: The paper lacks a comprehensive review of existing approaches in continual reinforcement learning. Given that stability-plasticity trade-off is a common challenge in continual RL, a survey of how it has been addressed would provide valuable context. In the fist paragraph of the related works section, the authors focus primarily on discussing continual learning without specific reference to continual RL. Additionally, for neuron-level research, a discussion of neuron-level continual RL methods, especially the **structure-based continual RL approaches** [1][2][3], would be helpful, as these methods also address the problem at the neuron level and a clear discussion is essential.  Since the experience replay is also highlighted as part of the paper's contribution, the related work also needs to discuss with **rehearsal-based continual RL methods** (e.g., [4][5]).

   [1] Using task descriptions in lifelong machine learning for improved performance and zero-shot transfer. *JAIR 2020*.

   [2] Continual Task Allocation in Meta-Policy Network via Sparse Prompting. *ICML 2023*.

   [3] Packnet: Adding multiple tasks to a single network by iterative pruning. *CVPR 2018*.

   [4] Efficient Lifelong Learning with A-GEM*. *ICLR 2021*.

   [5] Disentangling Transfer in Continual Reinforcement Learning. *Neurips 2022*.


2) **Clear Definition of the Continual Learning Problem**: The paper lacks a clear and precise definition of the continual learning problem it aims to address in the main body of the paper. Important aspects, such as whether the method is task-incremental or class-incremental, the extent of access to previous task data (and any limitations on this), and whether the continual learning model involves only the policy network or both the policy and critic networks, are not specified. Also, a clear definition to the "RL skill neuron" is required to clarify the concept.

3) **Novelty of Combining Task-Specific Skill Neurons with Gradient Masking**: The idea of combining task-specific skill neurons with gradient masking is not new. Similar approaches have been explored in previous works, such as PackNet [3] and CoTASP [2]. PackNet, prunes the policy after training each task to identify the most important neurons, which are similar to the “skill neurons” proposed here, while CoTASP combines pre-allocation and adaptive updates on "skill neuron selection masks". Both approaches use gradient masking to protect task-specific neurons and have shown strong capability to handle more complex continual RL tasks without the need of network inflation or data rehearsal from previous tasks. A thorough discussion and comparison with these closely related methods would help clarify the specific contributions and advantages of the proposed approach.

4) **Limitations in the Score Function**: The score function for identifying skill neurons is not very convincing.  It compares neuron activation  $a(N,t)$  and reward criterion $q(t)$  with some simple baselines, and then applies an indicator function to filter neurons with above-average activation and reward:

   4.1) For the activation component, the authors seem to use raw activation values instead of  **absolute** value;

   4.2) The activation baseline $\bar{a}(N)$ is calculated as a mean over multiple time steps for **a single neuron** rather than across neurons, though its meaning is to distinguish activation pattern for neurons from one to another;

   4.3) The indicator function in Eq 3 results in binary **counts of active steps**, losing precision in distinguishing the quality of activations (e.g., when two steps both meet the condition, it does not capture how much one might exceed the threshold over another);

   4.4) Since $q(t)$ is derived from some reward signal, all neurons from the networks will receive the same score over the same period, making it less effective as a **neuron-level measure**;

   4.5) The intuition behind Eq (4) is unclear. It assumes that **neurons not meeting Eq (3) still contributes positively** assigning them with a score of $1-Acc(N)$. This makes the intuition behind the scoring mechanism for RL skill neurons quite confusing. It's unclear what kind of neurons are eventually selected as skill neurons.  A statistical analysis of this scoring mechanism is needed to clearly illustrate the intuition behind this score function.

5) **Similarity to Dormant Neurons**: The way to score RL skill neurons closely resembles the dormant neuron approach in the literature. It would be helpful to explain why dormant neurons were not directly applied and to include a comparison with a dormant-based scoring function in the experiments.

6) **Gradient Masking**: The neuron-level identification strategy is transformed to parameter-level protection strategy by blocking all gradients connected to the skill neuron, even though each parameter links two neurons from consequent layers. Why not consider blocking $\triangle W_{j,:}$ too, or blocking $\triangle W_{i,j}$ with both sides being skill neurons? The assumptions behind this needs to be clearly stated.

7) **Gradient Marking with Experience Replay**: Experience replay inherently requires access to previous task data, which may be restricted in certain continual learning scenarios. The approach would be more impactful if gradient masking could achieve effective performance without the need for experience replay.

8) **Implementation for the Skill Neurons**: The paper lacks detailed discussion on the implementation strategy and insights for the proposed score function. It appears that RL skill neurons are only identified once at the end of training the first task. For scenarios with more than two tasks, there is no comments on how the masks accumulate across tasks. The authors should not restrict to the two-task settings, and consider increasing the scalability of the proposed approach.

9) **Simple Finetuning Baseline**: The illustration of stability and plasticity challenges in Section 3.1 uses a two-task fine-tuning baseline, which lacks continual learning techniques and is outdated. The authors should provide a stronger foundation by using some decent continual RL approaches for motivating the key challenges and showcasing stability-plasticity trade-offs.

10) **Limitations of Experimental Domain**: The experimental domain, limited to two simple tasks, is overly simple. Meta-World is commonly used in continual RL, and Continual World (CW) provides a more challenging benchmark with open-source baselines, comprehensive evaluation criterias, and performance curves. The Meta-World “window-close” task adopted in this paper is also part of CW, where current methods could achieve near 100% success without replay. I recommend evaluating the on standard CW10 or CW20 benchmarks and comparing with state-of-the-art methods, such as neuron-level baseline CoTASP, PackNet and rehearsal baseline ClonEx-SAC.


11) **Ablation Study Suggestions**:  The ablation study would benefit from incorporating some of the following baselines: (1) alternative activation functions; (2) Eq 4 with Acc(N) only; (3) using dormant neuron score function. (4) some randomly selected neurons as Skill Neurons; (5) gradient-masking only, without replay; (6) gradient masking with $\triangle W_{i,j}$

### Questions
- Why the evaluation criteria $q_\theta(t)$ is made binary for Meta-World and is based on return for Atari? Meta-World provides step-wise dense rewards that offer a progressive measure of the agent’s goal accomplishment, which would make it more informative for evaluation.

- How are reasonable time steps T determined in Eq (1) and Eq (2) for different continual RL environments?

- How does the reward-based evaluation criterion relate to the identification of neuron-level RL skill neurons? More explanation and statistical insights on this relationship will be helpful.

- Why does the method use raw activation rather than absolute activation? 

- Is the proposed method specific to certain activation functions, such as ReLU, and does it perform differently with alternatives like tanh?

- The experience replay frequency is quite high. How much data must be stored from previous tasks to support rehearsal?

- A minor comment on learning curves presented: throughout the paper, training curves are shown without clear indication of whether they correspond to the result when training the first or second task. Including full training curves would make it easier for readers to interpret results.

- In practice, how do you sample data and compute q(t) from the experience replay? 

- Could you provide computational complexity for measuring the RL skill neuron?

- The algorithm 1 provided in appendix lacks the crucial steps of computing RL skill neurons. Could you reflect this procedure more precisely?

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper introduces a new method that prevents catastrophic forgetting while allowing to efficiently learning new tasks in DRL. After learning a task and during learning a second task, they propose to prevent the modification of neurons that contribute to the success of the first task. The experiments show that the proposed approach better retain the first task and better learn the second task, compared to 3 baselines on three pairs of tasks.

### Strengths
The paper is overall easy-to-follow and the approach is novel and positively simple. The approach tackles an important task (continual learning in DRL) with little overhead (no new parameters, no pseudo-rehearsal etc..).

### Weaknesses
The paper lacks sufficient experimental validation to demonstrate the generality of the proposed method. The current experiments only focus on a narrow set of tasks involving opening and closing the same object, which raises concerns about whether the observed performance gains are specific to this particular task structure. The paper should explore a wider range of task pairs with varying degrees of overlap and complexity, such as the suggested 'Push', 'Reach', 'Pick Place', 'Basketball', and 'Sweep Into' tasks in Meta-world, to establish the robustness of the method. While some additional experiments on Atari were included in the supplementary material, these should be incorporated into the main paper to provide a more comprehensive evaluation. Furthermore, the paper should not only present the best results but also include a broader range of outcomes to give a more complete picture of the method's performance.

The evaluation of the approach is limited to two sequential tasks, which does not address the critical question of its scalability to longer task sequences. It is unclear whether the method can effectively prevent catastrophic forgetting when learning multiple sequential tasks and if there are inherent limitations in its ability to scale. The paper also fails to provide a clear explanation of how the mask ratio is determined and its impact on the learning process. The number of 'RL skill neurons' is not clearly defined, and it is unclear if it is a hyperparameter and how it affects the stability-plasticity trade-off. The analysis in the appendix, which touches on this, needs to be moved to the main paper and expanded to include a more detailed study of the influence of different numbers of neurons, going beyond just '300' and '400'. The discussion of limitations in the appendix should also be incorporated into the main text.

The ablation study in Section 4.3 is incomplete and does not fully isolate the effects of the proposed masking technique and experience replay. The paper should include experiments that evaluate the method without experience replay and with masking alone to determine the individual contribution of each component. It is also unclear if the other baselines use or can benefit from a similar experience replay mechanism, which makes it difficult to assess whether the improvements are due to the masking strategy or the replay buffers. The paper also overlooks relevant literature on catastrophic forgetting, particularly methods discussed in Section 5 of [1], and fails to explain why these methods are incompatible with DRL. The authors should at least discuss the work of [2], which attempted to apply their method to DRL, and explain why it is not considered a suitable baseline. The paper's length could be improved by moving Figure 3 to the appendix and optimizing the layout of the plots to save space, allowing for the inclusion of more results and discussion.

### Questions
The experiments are not sufficient to demonstrate the generality of the method. It is currently unclear whether the results come from the specific overlap between tasks (the paper only focuses on opening/closing the same object). On Meta-world, the authors could explore new pairs of tasks based on "Push", "Reach", "pick place", "basketball", "sweep into". It was actually done for Atari in supplementary materials, but it should be added to the main paper. Best results should not be the only one showed in the main paper.

The approach is only tested on two sequential tasks. It raises the questions of how well it would perform on more sequentials tasks. Is there a limitation of the method there ? This work does not present how large is the mask ratio. It may be that they are very large such that the plasticity quickly decreases as the number of tasks increase. This should be clarified and studied. Such a clarification would start with:
"The neurons with the highest scores are identified as RL skill neurons, as they are instrumental in task-specific knowledge retention. And the number of RL skill neurons varies depending on the complexity of the task". The number of neurons is unclear. Is it a hyper-parameter ? If yes, how does it impact stability/plasticity ? A section in appendix started to investigate this question, but 1) this should be in the main paper; 2) it is unclear what the numbers "300" and "400" exactly refer to; 3) more numbers should be studied. Limitations discussed in appendix should be in the main paper.

Section 4.3 is also incomplete. The main novelty of the approach is the masking idea. But the authors do not try the method without the experience replay/with masking. It is also unclear how much of replay is dedicated to previous tasks: "Additionally, we use two separate replay buffers for experience replay: one for storing the current experiences and the other for preserving experiences from the previous task. The agent then selectively samples from these buffers to update networks". It's also unclear whether other baselines (except for the "importance" variant) use/can benefit from a similar experience replay mechanism.

The paper overlooks parts of the litterature on catastrophic forgetting, see Section 5 of [1] for instance. I understand that they did not evaluate the methods on DRL tasks, but the authors should then explain why these methods are incompatible with DRL. At least [2] tried their method with DRL and is not discussed.

Given my recommendations, the main paper seems to have a problem with the length: I would suggest: move Figure 3 to appendix. A lot of space on the left and right of plots is lost; it is likely possible to reduce the size of the plots and have 3 figures per row. Barplots could be made smaller/vertical or could be reported in a table like Table 1 (without individual success rates).

Small comments:

- line 216: The "evaluation criterion function" is unclear. Is that the reward ? How do you measure "the degree to
which the agent approaches the goal" ?
- line 60: "However, stability and plasticity attribute to the expressive capabilitie" is unclear.
- Paragraph 2, Section 3.2  is mostly redundant with the related works section
- Figure 7: why not showing the average return on the x-axis ? It would help comparing with results from a) and c).
- There are two "Fengshuo Bai, Hongming Zhang, Tianyang Tao, Zhiheng Wu, Yanna Wang, and Bo Xu. Picor:
Multi-task deep reinforcement learning with policy correction. In Proceedings of the AAAI Con-
ference on Artificial Intelligence, volume 37, pp. 6728–6736, 2023b" in the bibliography.

[1] Khetarpal, K., Riemer, M., Rish, I., & Precup, D. (2022). Towards continual reinforcement learning: A review and perspectives. Journal of Artificial Intelligence Research, 75, 1401-1476.
[2] Rusu, A. A., Rabinowitz, N. C., Desjardins, G., Soyer, H., Kirkpatrick, J., Kavukcuoglu, K., ... & Hadsell, R. (2016). Progressive neural networks. arXiv preprint arXiv:1606.04671.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a method from the neuron level for mitigating plasticity loss issue while maintaining the performance in Deep RL domain.  Their method outperforms several related baselines on several simulation tasks. 

About the method part, I think the total algorithm design is novel and makes sense. However, The experimental part is too brief to support the effectiveness of the algorithm.

### Strengths
1. This paper is well-written, and has clear figures.
2. The method is introduced in a reasonable and theatrical way.
3. The results show that their method performs well practically.

### Weaknesses
1.  The selected scenarios in the experimental part are too simple and rare, involving only four small tasks in metaworld, to provide a strong validity verification, which makes me doubt the performance of the method in practical applications. Please show the effectiveness of the algorithm on more benchmark tasks such as DeepMind Control Siult\Gym-Mujoco\Baby AI [1] and the famous continuous learning manipulator benchmark-- LIBERO[2]. The current experiments do not adequately demonstrate the method's ability to scale to more complex environments or tasks with higher dimensionality, which is crucial for real-world applicability. The limited scope of the experimental setup raises concerns about the generalizability of the findings.

2. The existing continuous deployment papers all build well over two sequential training tasks. Please test all methods according to the mainstream experimental design. Refer to the paper [3]. The current evaluation lacks a rigorous assessment of the method's performance in a truly continual learning setting. Testing on only a few tasks does not sufficiently demonstrate the method's ability to mitigate catastrophic forgetting or maintain performance over extended sequences of tasks. The absence of a clear evaluation protocol aligned with mainstream continual learning practices makes it difficult to compare the method with existing approaches.

3. The selected baselines are few and simple. Please compare with the latest method of addressing plasticity loss,e.g. [4] [5] [9]. It also suggests a contrast with recent approaches to lifelong learning [8](which do not explicitly focus on plasticity loss or primacy bias, but also test an agent's performance in changing scenarios). The lack of comparison against state-of-the-art methods specifically designed to address plasticity loss and continual learning makes it difficult to assess the novelty and effectiveness of the proposed approach. The current baseline selection does not provide a sufficient benchmark to demonstrate the method's superiority or even its competitiveness with existing techniques. A more comprehensive comparison is needed to validate the contribution of the proposed method.

4. This paper claims that the proposed method can alleviate plasticity loss, but does not show the performance of the methods on plasticity evaluation metrics, such as covariance metric [6], FAU [7]. The absence of quantitative evaluation using established plasticity metrics weakens the claim that the proposed method effectively mitigates plasticity loss. Without these metrics, it is difficult to ascertain whether the method truly addresses the underlying issue or simply achieves better performance through other means. The lack of direct measurement of plasticity makes it challenging to validate the core contribution of the paper.

### Questions
As for the skill neuron identification part,  I think the first half is too similar to the design of $\tau$-dormant neuron [1], but it is not referenced in the method part. This kind of makes me wonder. Could you please explain this point?

[1 ]Sokar, Ghada, et al. "The dormant neuron phenomenon in deep reinforcement learning." International Conference on Machine Learning. PMLR, 2023.

### Soundness
2

### Presentation
3

### Contribution
2
