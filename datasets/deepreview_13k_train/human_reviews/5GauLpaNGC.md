# Task Characteristic and Contrastive Contexts for Improving Generalization in Offline Meta-Reinforcement Learning

- Decision: Reject
- Scores: 8, 3, 6

## Abstract
Context-based offline meta-reinforcement learning (meta-RL) methods typically extract contexts summarizing task information from historical trajectories to achieve adaptation to unseen target tasks. Nevertheless, previous methods may lack generalization and suffer from ineffective adaptation. Our key insight to counteract this issue is that they fail to capture both task characteristic and task contrastive information when generating contexts. In this work, we propose a framework called task characteristic and contrastive contexts for offline meta-RL (TCMRL), which consists of a task characteristic extractor and a task contrastive loss. More specifically, the task characteristic extractor aims at identifying transitions within a trajectory, that are characteristic of a task, when generating contexts. Meanwhile, the task contrastive loss favors the learning of task information that distinguishes tasks from one another by considering interrelations among transitions of trajectory subsequences. Contexts that include both task characteristic and task contrastive information provide a comprehensive understanding of the tasks themselves and implicit relationships among tasks. Experiments in meta-environments show the superiority of TCMRL over previous offline meta-RL methods in generating more generalizable contexts, and achieving efficient and effective adaptation to unseen target tasks.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes a framework called Task Characteristic and Contrastive Contexts for Offline Meta-Reinforcement Learning (TCMRL), which aims to enhance the generalization ability of context-based offline meta-RL methods. TCMRL introduces two key components: a task characteristic extractor and a task contrastive loss, which work together to generate more comprehensive contexts by capturing both characteristic and contrastive task information. The task characteristic extractor uses an attention mechanism to emphasize transitions that are crucial for characterizing a task, while the task contrastive loss helps to distinguish different tasks by exploring interrelations among trajectory subsequences. Experiments demonstrate that TCMRL significantly improves adaptation to unseen tasks, outperforming existing offline meta-RL methods on multiple benchmark datasets.

### Strengths
1. TCMRL brings a fresh perspective by dynamically disentangling characteristic features from the trajectories while also maximizing interrelations among tasks.

2. The paper is written clearly, with a logical structure that makes it easy for readers to follow the flow of ideas. Key concepts such as task characteristic and contrastive information are well explained, with visual aids like figures and pseudocode to help illustrate the framework.

3. TCMRL improves the generalization capability of context-based offline meta-RL.

### Weaknesses
1. Some results are reported as normalized scores, e.g. Table 1. However, there is no explanation for how normalization is processed.

2. Although context shift is highlighted as one of the primary issues that TCMRL aims to solve, there is no in-depth analysis of how TCMRL reduces context shift compared to other methods, and potential limitations.

### Questions
See above.

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
This work targets the problem of offline meta RL by learning a context of a task information from trajectories so that the learned context encoder can quickly capture characteristics of an unseen test task with limited interactions. Specifically, the authors propose to learn such context encoder by conditioning a reward neural network on a weighted aggregation of transition encodings in a trajectory. The authors also propose to train the context vector by penalising rewards prediction when conditioned on a reversed weighted version of context. This work also leverages contrastive learning to train transition encoding.

### Strengths
The motivation behind learning both task characteristic and task contrastive information for better meta generalisation is reasonable.

The proposed method is evaluated on many meta RL environments and empirical results show improved performance.

### Weaknesses
The proposed method in this work consists of many components around the context encoder training. However, It is unclear to me what is the fundamental technical reason behind these kinds of design and why these specific designs can achieve desired behaviour of the context encoder. There are many explanations in the method part in section 4 but they are not well structured in logic and look very lengthy:

(1) Line 38: “as only a few key transitions within the trajectory provide the main task characteristic information…” This is to say many other transitions do not distinguish tasks. I have concern over this statement as this is only probably correct when the tasks have some property like a hierarchical structure. In general when the dynamics of a target task has a consistent shift on the entire state space, such sparsity prior would not be beneficial.

(2) It is unclear to me why Eq. (7) and Eq. (8) can lead to learning a context encoder such that the task characteristic extractor q can capture task unique transitions. The neural network is probably able to capture task conditioned reward with a task-level context without learning relations in terms of tasks transitions. In my opinion, the network does not promote the correct importance score of c_i. It probably only makes c_i and c_i^neg different and that is enough to learn a conditional reward function under Eq. (7) and (8).

(3) Are r and r_reverse in Eq. (7) and Eq. (8) the same neural network with same parameters?

(4) It seems that Eq. (7) and Eq. (8) only capture the task shift in terms of reward function while the transition dynamics is ignored (no loss function in terms of next state prediction). Can authors please explain the reason?

Overall, the proposed method consists of several modified versions of previous loss functions and is also combined with existing contrastive learning technique. The technical novelty is not strong and there is no theoretical analysis on why the proposed objective function can guarantee generalisation in a meta learning setting.

### Questions
Please see the weakness part.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper addresses the limitations in generalization and adaptation of existing context-based offline meta-reinforcement learning (meta-RL) methods. The proposed framework, TCMRL, enhances context generation by incorporating both task characteristic information, which identifies key transitions within tasks, and task contrastive information, which distinguishes tasks through interrelations in trajectory subsequences. This combined approach yields a comprehensive task understanding, improving adaptability to unseen tasks. Experiments confirm TCMRL’s advantage in generating generalizable contexts and effective adaptation over previous methods.

### Strengths
•   Clarity: The paper is well-articulated, with a clear and complete structure that makes the methodology and findings accessible to readers. Additionally, the appendix provides extensive experimental details and analyses.
•   Significance: I believe the authors have targeted a valuable goal, namely addressing the challenge of context shift in context-based offline meta-reinforcement learning methods. The paper demonstrates consistent improvements over baseline methods across a wide range of experiments, showcasing the robustness of their approach in tackling this important issue.

### Weaknesses
• Quality: The paper lacks a strong motivational foundation, particularly in explaining why task characteristic information and task contrastive information are expected to enhance context generalization. While the authors introduce a novel method based on these two types of information, the construction of the approach appears somewhat arbitrary, relying on intuition rather than solid theoretical underpinnings. An improved presentation could include theoretical justifications or empirical evidence demonstrating that capturing these specific forms of task information is indeed crucial for generalization. Specifically, the paper does not clearly articulate why the proposed method of extracting task characteristic information, which involves identifying key transitions, is superior to other potential methods. The selection of transitions based on reward magnitude, while intuitive, lacks a rigorous justification. Furthermore, the paper does not adequately explain how the contrastive loss is designed to capture inter-task relationships effectively. The contrastive loss seems to rely on a somewhat arbitrary selection of positive and negative samples, and it's not clear how this choice ensures that the learned representations are truly discriminative across different tasks. The paper would benefit from a more detailed analysis of the theoretical properties of the proposed loss function and its impact on the learned context representations.
•   Originality: Although the technical implementation is undoubtedly innovative in its details, the underlying concepts are relatively familiar within the field. Techniques such as implicit attention mechanisms, context encoding, and task-based contrastive learning have been explored previously, and this paper can be seen as a new combination of these existing ideas.

### Questions
1.	As illustrated in the weaknesses, why is the lack of generalization attributed to the absence of task characteristic information and task contrastive information? Could you explain this in more detail, and how do you perceive the relationship between these two types of information?
2.	When extracting task characteristic information, why not consider using a well-established architecture like the Transformer? Given that Transformers leverage self-attention mechanisms to extract key information from sequences and create unified representations while capturing internal relationships within sequences, it seems like a viable option.
3.	Could you provide the rationale for designing the negative reward estimation as you did? What motivated this specific design?
4.	How do you determine the proportions of the various losses in the optimization process? I believe that the hyperparameters setting these ratios significantly impact the method’s performance.
5.	In the ablation study, as shown in Figures 5 and 6, I noticed that, in experiments like reacher-v2, removing an individual component within TCE results in greater performance loss than fully removing TCE. How would you explain this phenomenon?

### Soundness
3

### Presentation
3

### Contribution
3
