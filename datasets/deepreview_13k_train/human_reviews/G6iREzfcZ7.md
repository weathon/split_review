# Hierarchical Subspaces of Policies for Continual Offline Reinforcement Learning

- Decision: Reject
- Scores: 5, 6, 6, 6

## Abstract
In dynamic domains such as autonomous robotics and video game simulations, agents must continuously adapt to new tasks while retaining previously acquired skills. This ongoing process, known as Continual Reinforcement Learning, presents significant challenges, including the risk of forgetting past knowledge and the need for scalable solutions as the number of tasks increases. To address these issues, we introduce HIerarchical LOW-rank Subspaces of Policies (HILOW), a novel framework designed for continual learning in offline navigation settings. HILOW leverages hierarchical policy subspaces to enable flexible and efficient adaptation to new tasks while preserving existing knowledge. We demonstrate, through a careful experimental study,  the effectiveness of our method in both classical MuJoCo maze environments and complex video game-like simulations, showcasing competitive performance and satisfying adaptability according to classical continual learning metrics, in particular regarding memory usage. Our work provides a promising framework for real-world applications where continuous learning from pre-collected data is essential.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper explores the use of Continual Subspace of Policies (CSP) in the context of continual offline goal-conditioned imitation learning. It introduces a low-rank subspace for both high-level and low-level policies, aiming to maintain performance while minimizing memory usage. The proposed algorithm, Hierarchical Low-Rank Subspaces of Policies (HILOW), is evaluated on newly introduced benchmarks, supporting the authors' claims about its effectiveness.

### Strengths
The paper is mostly clearly. The main results and contribution are clearly highlighted, and the conclusions are succinctly declared.

The proposed hierarchical subspace of policy is novel and is empirically validated. It is capable of capturing different levels of knowledge, enabling knowledge reuse and memory saving.

### Weaknesses
 **Limited Contribution**: Most techniques proposed in the paper are already applied in related domains. The continual subspace of policies (CSP) is proposed as a continual reinforcement learning method, adapting it to continual imitation learning is straightforward. The low-rank adaptation (LoRA) is also well-established in continual learning, and its application here does not present any distinct innovation. The only novel aspect is the hierarchical subspaces of policies.

**Limited Improvement**: The proposed algorithm, HILOW, does not demonstrate substantial improvement over basic strategies, and the limited improvement comes predominantly from existing techniques. As shown in Figure 3, the algorithm's performance is similar to that of expanding naïve strategy (SCN) and expanding finetuning strategy (FTN), with the primary advantage being reduced memory consumption. However, the ablation study indicates that most of the memory savings (approximately 75%) compared to CSP-O are due to LoRA, not the hierarchical subspace approach.
 
**Irrelevant Related Work (Addressed)**: The related work section includes extensive discussions on topics like transfer learning, multitask learning, meta-learning, and online continual reinforcement learning, which are not directly pertinent to this paper. Conversely, the core techniques employed, CSP and LoRA, are not adequately covered, leaving a gap in the context for readers.

**Unclear Usage of LoRA (Addressed)**: The paper lacks clarity regarding the implementation of LoRA. It does not specify whether the subspace of policies is applied to the factored matrices A and B or to the low-rank matrix AB. This distinction is crucial because $\sum_i\alpha_iA_iB_i\neq (\sum_i\alpha_iA_i)(\sum_i\alpha_iB_i)$. More explicit details on this aspect would help in understanding the approach better.

### Questions
Could you provide more detailed analysis or experiments that isolate the impact of the hierarchical subspaces, demonstrating their specific contribution to the overall performance and memory efficiency?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a novel framework for continual offline RL called HILOW focused on goal-conditioned offline navigation tasks. They additionally introduce a benchmark of navigation tasks along with corresponding human-authored datasets to evaluate robotics and video game scenarios to provide a testbed for future work, in which they evaluate HILOW and other continuous RL approaches. HILOW is an adaptation of Continual Subspace of Policies to offline RL, which hierarchically parameterizes the policy with a high-level path planner and low-level path-follower, each with separate parameter subspaces. HILOW shows comparable performance + adaptability to prior work with a more memory-efficient approach, thus enabling efficient continuous learning from pre-collected data.

### Strengths
- Effective Continual learning framework that slightly outperforms other prior work in the tradeoff of performance and relative memory size.
- Construction of Benchmarks with comprehensive baselines for evaluations: set of navigation maze tasks that showcase the efficacy of HILOW and other algorithms with individual task streams.

### Weaknesses
 - FTN and SCN seems to be a strong baseline as seen in Figure 3 with similar performance to memory size tradeoff. Additionally, approaches such as Polyoptron, Multitask prompt tuning and similar peft approaches have been found to help with multi-task adaptation which may additionally help with memory efficiency and would be a good standard of comparison alongside these baselines.
- The domains seem somewhat narrow and similar to each other (all being maze-like), which meets the offline navigation claims you shared in the paper, but the method is agnostic to the environments in which it is evaluated with. It could be helpful to evaluate how this approach performs on alternate domains such as long horizon manipulation (such as tasks seen in OG bench) or other navigation tasks (e.g driving domains like Carla), to see if the method is general and widely applicable.
- Given the framework has origins from Continual Subspace of Policies (CSP), it would be helpful to clarify the contribution of your offline approach concerning the prior work, which entails many of the components described such as subspace extension/pruning.

### Questions
- It is mentioned that hierarchical imitation learning is used to learn both the anchor weights and new low-rank parameters, given that the anchor weights are shared across tasks, do you see degradation for prior tasks?
- [Related] Could you share an ablation/scaling law of how the performance of the policy changes as the number of tasks increases. Metrics to consider would be performance on the new/old tasks with respect to efficiency in memory.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a method for continual offline reinforcement learning to specifically solve navigational problems in video games or video game like scenarios such as mazes. The method, "hierarchical low-rank subscpaces of policies (HILOW)" is based on the soft actor-critic method and the similarly named "continual subspace of policies" from the online learning domain. The idea of this method is to extend or prune a subspace of parameters in a neural network with new parameters and new weights during training to avoid forgetting previously learned behaviours.
To evaluate the method a comparison to state-of-the art CRL methods with newly created offline, goal-oriented navigational tasks is done. There is a heavy focus memory size as an evaluation metric.

### Strengths
The adaptation of an existing method such as "continual subspace of policies" to a slightly differnt flavor of reinforcement learning makes sense and should be studied. The proposed new method from said adaptation is explained well and clear. With the given information the experiments should be quite easily reproducable. The metrics and method used to evaluate the baseline and proposed algorithms are chosen well and make sense in the given context.
With this in mind this study could be a small but valuable addition in the continual reinforcement learning domain.

### Weaknesses
The greatest weaknesses of the paper are the baseline comparisons. There is a chapter for preliminaries that is referenced when describing what the proposed method is compared to, but only describes categories of different methodologies in a broad way.
The actual description of the baselines and why they were chosen instead of others is too short or even missing making them hard to comprehend. Is is especially unclear what part of the preliminary chapter is relevent for which baseline method, unless you are already familliar with them. Also i think the newly introduced environments such as the Godot Maze and Godot Agent are either to close to the already existing ones or the differences are not explained well enough. The Godot Agent comes across as a simpler version of the Ant or Point agent, while the Godot Maze and MuJoCo Maze in figure 2 seems to be identical but with differnt colors.

### Questions
Why is a generative replay approach not considered and brushed aside because of data storage constraints? From my understanding that is exactly the strength of generative replay vs. the memory heavy experience replay with their buffers.
What about exsisting offline RL methods such as Behavior Regularized Offline Reinforcement Learning or Conservative Q-Learning?
Could they be used to achieve something similar or are they not as good for this specific szenario meaning navigational problems.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper tackles the challenge of continual offline reinforcement learning for goal-conditioned navigation, where agents must adapt to new tasks using only pre-collected data, without forgetting previous skills. The authors introduce Hierarchical LOW-Rank Subspaces of Policies (HILOW), a hierarchical framework that uses low-rank subspaces for scalable, memory-efficient policy adaptation. Experiments demonstrate HILOW’s superior scalability and adaptability compared to existing continual reinforcement learning methods on standard benchmarks.

### Strengths
1. HILOW provides an solution for goal-conditioned offline continual reinforcement learning, excelling in knowledge retention and data efficiency.

### Weaknesses
1. This paper focuses on continual offline reinforcement learning with an emphasis on goal-conditioned navigation tasks, but this specific problem is not adequately highlighted throughout. The title, as well as the related work and preliminaries sections, do not mention goal-conditioned learning explicitly. Additionally, the paper does not clearly define the continual offline reinforcement learning problem with goal-conditioned navigation tasks or explain its importance, which weakens the motivation behind this work.
2. Each section of the paper reads as a list of points, with minimal cohesion or natural progression between parts. For example, there is no clear logical connection between sections 4.3 and 4.4. It is unclear why subspace exploration is needed immediately after subspace extension. This disjointed organization makes the overall flow of the paper difficult to follow and requires significant revision to improve coherence.
3. The choice to sample anchor weights from a Dirichlet distribution lacks adequate explanation. While Dirichlet distributions are commonly used for weight sampling, relying solely on this approach may not be sufficient for finding the optimal weight combination in complex tasks. A stronger justification or alternative exploration method could improve this aspect.
4.  The propose method is complex and may bring additional implementation and computational costs.

### Questions
1. The baselines used in the experiments are designed for continual reinforcement learning. Is it fair to compare these with the proposed method in goal-conditioned offline continual reinforcement learning? Could you explain why these baselines were chosen and how well they address the challenges specific to goal-conditioned offline continual reinforcement learning tasks?
2. Could you provide details on the run-time and computational efficiency of the proposed algorithm? Given the added complexity from subspace extension, anchor sampling, and hierarchical imitation learning, how does HILOW’s efficiency compare to that of the baselines?

### Soundness
2

### Presentation
2

### Contribution
2
