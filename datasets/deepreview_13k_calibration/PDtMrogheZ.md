# Learning Robust Representations with Long-Term Information for Generalization in Visual Reinforcement Learning

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 5, 8, 6

## Abstract
Generalization in visual reinforcement learning (VRL) aims to learn agents that can adapt to test environments with unseen visual distractions. Despite advances in robust representations learning, many methods do not take into account the essential downstream task of sequential decision-making. This leads to representations that lack critical long-term information, impairing decision-making abilities in test environments. To tackle this problem, we propose a novel robust action-value representation learning (ROUSER) under the information bottleneck (IB) framework. ROUSER learns robust representations to capture long-term information from the decision-making objective (i.e., action values). Specifically, ROUSER uses IB to encode robust representations by maximizing their mutual information with action values for long-term information, while minimizing mutual information with state-action pairs to discard irrelevant features. As action values are unknown, ROUSER proposes to decompose robust representations of state-action pairs into one-step rewards and robust representations of subsequent pairs. Thus, it can use known rewards to compute the loss for robust representation learning. Moreover, we show that ROUSER accurately estimates action values using learned robust representations, making it applicable to various VRL algorithms. Experiments demonstrate that ROUSER outperforms several state-of-the-art methods in eleven out of twelve tasks, across both unseen background and color distractions.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a novel approach termed Robust Action-Value Representation Learning (ROUSER) within the Information Bottleneck (IB) framework. This paper evaluates ROUSER on VRL generalization benchmark and conducts various experiments to demonstrate the advances of ROUSER.

### Strengths
1.The method part of this paper has sufficient theoretical analysis and proof.

2.The method is evaluated on various experiments.

### Weaknesses
1.The six tasks in the DeepMind Control (DMC) suite, including "reacher_easy," are commonly used to assess the sample efficiency of VRL. However, the DMC-GB also includes tasks like "walker_stand" for evaluating generalization capabilities. To provide a more comprehensive evaluation, you should run additional experiments on "walker_stand" to better assess your method's generalization performance in alignment with this benchmark.

2.While CURL and DrQv2 have been evaluated on generalization benchmarks, they were not originally designed to address the specific challenges of generalization in VRL. To provide a more relevant comparison, you should include results for your method alongside established methods like SECANT [1] and PIE-G [2], which were specifically developed to enhance generalization in VRL.

### Questions
1.The six tasks in the DeepMind Control (DMC) suite, including "reacher_easy," are commonly used to assess the sample efficiency of VRL. However, the DMC-GB also includes tasks like "walker_stand" for evaluating generalization capabilities. To provide a more comprehensive evaluation, you should run additional experiments on "walker_stand" to better assess your method's generalization performance in alignment with this benchmark.

2.While CURL and DrQv2 have been evaluated on generalization benchmarks, they were not originally designed to address the specific challenges of generalization in VRL. To provide a more relevant comparison, you should include results for your method alongside established methods like SECANT [1] and PIE-G [2], which were specifically developed to enhance generalization in VRL. 

[1] Linxi Fan, Guanzhi Wang, De-An Huang, Zhiding Yu, Li Fei-Fei, Yuke Zhu, and Animashree Anand kumar. Secant: Self-expert cloning for zero-shot generalization of visual policies. In International Conference on Machine Learning, 2021.

[2] Zhecheng Yuan, Zhengrong Xue, Bo Yuan, Xueqian Wang, Yi Wu, Yang Gao, and Huazhe Xu. Pre trained image encoder for generalizable visual reinforcement learning. In First Workshop on Pre training: Perspectives, Pitfalls, and Paths Forward at ICML 2022, 2022.

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
This paper proposes robust action-value representation learning (ROUSER). ROUSER aims to acquire robust representation by encouraging the representation to capture Q-values while minimizing mutual information with state-action pairs to discard irrelevant features. ROUSER is applicable to different VRL algorithms and can improve performance in environments with visual distractions.

### Strengths
- ROUSER aims to keep essential information by predicting the Q-value while neglecting irrelevant features by minimizing mutual information with state-action pairs.
- ROUSER's objective is applicable to common VRL algorithms.

### Weaknesses
 - The idea of incorporating Q-values to mitigate visual distractions is a commonly adopted design choice in VRL, e.g. [1,4]. I believe the effectiveness of ROUSER needs to be evaluated in a more standard setting with VRL generalization baselines.
- To be specific:
    - The [DMC-GB](https://github.com/nicklashansen/dmcontrol-generalization-benchmark) is a commonly adopted visual generalization benchmark with `color_hard` and `video_hard` setting [1,2]. I believe the evaluation results on DMC-GB would be more persuasive.
    - For baselines, I believe comparing with generalization baselines is necessary. For example:
        - TPC [3] proposes to regularize the representation to encode temporally predictable features only.
        - [4] also proposes an information-bottleneck perspective to regularize representation.
        - TIA [5] designs structured representation so that the task-relevant representation captures long-term rewards while the task-irrelevant one captures no reward information.
        - PIEG [6] shows that representation from a pre-trained image encoder can boost the visual generalization significantly.

### Questions
NA

### Soundness
3

### Presentation
3

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
The authors propose a novel temporal difference objective (ROUSE) for learning representations that capture long-term information are robust to distractions and perturbations for visual reinforcement learning. To make the proposed method robust, the authors utilize the information bottleneck principle, and make sure the learned representations of state action pairs captures the information about the reward, while minimizing the amount of information it captures about the state itself.

ROUSE is can be integrated with a variety of critic-based methods. The authors integrated ROUSE with DrQ, SRM and QRDQN, and test on DeepMind Control, MuJoCo, ProcGen, showing improved robustness compared to the baselines.

### Strengths
- ROUSE is general can be applied to any visual RL algorithm that learns a critic;
- The proposed information-bottleneck objective is well-motivated mathematically. The authors provide detailed mathematical derivations of the objectives;
- The method shows good results on the proposed benchmarks and improves robustness to color change and background video distractors;

### Weaknesses
 - The paper is not clearly written, it took me some time to go through and understand it. I suggest improving the flow a bit. For example, something that could help is better structure. In the beginning of section 4, I would say something about the big picture of the paper, as "We propose robust reward representations, then use td learning to learn robust value representations. Throughout, we use IB-based objective make representations robust." At the end of section 4, it would also help to list the objectives, or add the figure or pseudocode from the appendix. I understand you don't have much space, maybe decreasing the size of figures 1 and 2, or aggregating results over tasks could be a way to go here.

 - 227: "one of action-value representations" : unclear wording, what does "one of" mean here?
 - 270: we support that a compressed reward representation... : 
 - 299: model a reward model -> introduce a reward model
 - 364: supports -> allows
 - Sections 5.2 and 5.3 titles are not very informative. Applicability and effectiveness? what does that mean? Something more concrete would be better, like "Extending ROUSER to tasks with discrete actions" and "Analyzing learned representations"
 - Figure 4: please put the x and y axis labels in the figure itself, at least in small font, that would make it easier to read.-
 - 466: Reword to something like "In this subsection, motivated by the result in theorem 4.4, we extend RoUSER to..."
 - 502: all methods' prediction: what does that mean?
 - 504: "use a 2 layer mlp with a learning rate of 1e4". I understand what you're saying, but the sentence is awkward. I'd say "we train a 2 layer mlp on top of frozen..., and use 1e-4 learning rate to train it."
 - 515: by searchings alpha... : reword this, this is not grammatically correct
 - 539: "sheds light" -- instead say "we believe this method is general and applicable to other problems, such as self-driving"

### Questions
Line 506: What information are you predicting in this frozen evaluation? Is it average of 300 rewards in the future? What exactly is the MSE between?


##### Writing

- 227: "one of action-value representations" : unclear wording, what does "one of" mean here?
- 270: we support that a compressed reward representation... : 
- 299: model a reward model -> introduce a reward model
- 364: supports -> allows
- Sections 5.2 and 5.3 titles are not very informative. Applicability and effectiveness? what does that mean? Something more concrete would be better, like "Extending ROUSER to tasks with discrete actions" and "Analyzing learned representations"
- Figure 4: please put the x and y axis labels in the figure itself, at least in small font, that would make it easier to read.-
- 466: Reword to something like "In this subsection, motivated by the result in theorem 4.4, we extend RoUSER to..."
- 502: all methods' prediction: what does that mean?
- 504: "use a 2 layer mlp with a learning rate of 1e4". I understand what you're saying, but the sentence is awkward. I'd say "we train a 2 layer mlp on top of frozen..., and use 1e-4 learning rate to train it."
- 515: by searchings alpha... : reword this, this is not grammatically correct
- 539: "sheds light" -- instead say "we believe this method is general and applicable to other problems, such as self-driving"

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a novel way for learning robust representations in image-based RL by learning through the proposed robust action-value representation using an information bottleneck framework. To address the challenge of unknown true action-values, this approach learns action-values indirectly through reward representations. The proposed method is validated in both continuous and discrete control domain. Experiments demonstrate improved performance over other image-based RL baselines on tasks with video background and object color changes.

### Strengths
- The paper is clearly written and easy to follow.
- The motivation and explanation for learning robust action-value representations, and learning robust action-value representations via reward representations are presented clearly.
- The experiment is conducted on both continuous and discrete control tasks.
- Applying ROUSER on top of DrQv2 and SRM shows consistent improvement.

### Weaknesses
 - Lack of training curves on Distracting DMControl benchmark for Figures 1 and 2: Including training curves would help readers understand the sample efficiency and stability of the proposed method. Specifically, it's difficult to assess the convergence rate and potential oscillations during training without these curves. The absence of these curves makes it challenging to compare the learning dynamics of ROUSER with the baselines.
- In Figures 1 and 2, the baselines include both standard methods for image-based RL (e.g., DrQv2, CURL, TACO) and methods designed to be robust against distractors (e.g., SRM, CRESP, RAP). It would be better to reorganize the results, such as grouping methods by type or using different visual indicators for a clearer comparison. The current presentation makes it hard to quickly assess the relative performance of methods designed for robustness versus standard methods, and how ROUSER compares within each group. A clearer visual separation would aid in understanding the method's contribution.

Minor: 
- Typo in line 430: Nore -> Note
- In Figure 4, axis labels should be included directly on the plots rather than in the caption.

### Questions
- In Section 5.3, the authors analyze the effectiveness of ROUSER in capturing long-term information with a fixed length of 300, It would be helpful to see how the effectiveness changes with varying lengths (e.g., 50, 100, 500).
- The recent method MIIR [1] also considers learning robust representations using the information bottleneck framework and conducts experiments on the Distracting DMControl benchmark. Could the author discuss the differences between ROUSER and MIIR, such as their theoretical motivations and empirical performance comparisons?

[1] Wang S, Wu Z, Wang J, Hu X, Lin Y, Lv K. How to Learn Domain-Invariant Representations for Visual Reinforcement Learning: An Information-Theoretical Perspective.

### Soundness
3

### Presentation
3

### Contribution
3
