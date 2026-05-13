# Pre-Training Robo-Centric World Models For Efficient Visual Control

- Decision: Reject
- Scores: 6, 3, 5, 8

## Abstract
Humans can accurately anticipate their movements to behave as expected in various manipulation tasks. We are inspired to propose that integrating prior knowledge of robot dynamics into world models can effectively improve the sample efficiency of model-based reinforcement learning (MBRL) in visual robot control tasks. In this paper, we introduce the Robo-Centric World Model (RCWM), which explicitly decouples the robot dynamics from the environment and enables pre-training to learn generalized and robust robot dynamics as prior knowledge to accelerate learning new tasks. Specifically, we construct respective dynamics models for the robot and the environment and learn their interactions through cross-attention mechanism. With the mask-guided reconfiguration mechanism, we only need a few prior robot segmentation masks to guide the RCWM to disentangle the robot and environment features and learn their respective dynamics. Our approach enables independent inference of robot dynamics from the environment, allowing accurate prediction of robot movement across various unseen tasks without being distracted by environmental variations. Our results in Meta-world demonstrate that RCWM is able to efficiently learn robot dynamics, improving sample efficiency for downstream tasks and enhancing policy robustness against environmental disturbances compared to the vanilla world model in DreamerV3. Code and visualizations are available on the project website: https://robo-centric-wm.github.io.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper considers the problem of world model pre-training in robotics applications. Different from previous approaches that use a single model to train the scene evolution, the key idea of this paper is to decouple world dynamics into robot dynamics and environment dynamics. The proposed model uses a dedicated robot branch to predict the future images of the robot, an environment branch to predict the future images of the environment, and an interaction module to inject the information from the robot branch to the environment branch.

### Strengths
This paper is well-written and the logic is clear. The idea of decupling robot dynamics and environment dynamics is interesting. The claim is supported by promising experiment results.

### Weaknesses
It is unclear if the gains are from the additional capacity introduced by the additional branch. (2x model capacity?) To verify this, the authors could expand the dreamer model capacity and compare the results.

It is strange that the robot branch can learn effects of the environment on the robot, even there is no information exchange from environment branch to the robot branch.
This makes me wonder if the true technical idea is simply using two models to predict the evolution of the robot and the rest of the scenes separately. This can be validated by disabling the interaction part and compare with the proposed model in terms of dynamics prediction and policy learning.

### Questions
See my questions above

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper presents robot-centric world models that distinctively model robot and environmental dynamics to enhance visual model-based reinforcement learning. Results from eight MetaWorld tasks demonstrate improved learning efficiency compared to the vanilla baseline, DreamerV3.

### Strengths
- The paper is well-organized, featuring visualizations that aid in understanding the proposed robot-centric world models.
- The approach appears to effectively learn robot-centric dynamics, though I have some questions about it.
- Experimental results show performance gains over the state-of-the-art DreamerV3 across 8 MetaWorld tasks.

### Weaknesses
 - A primary concern is that the performance improvement may not solely be attributed to the proposed idea. Several additional implementations, such as the transformer in the interaction model, mask-guided encoder, and predictor head, confuse the attribution of improvements. The use of a transformer for interaction modeling, while potentially beneficial, introduces architectural complexity that makes it difficult to isolate the impact of the core robot-centric world model. The mask-guided encoder, though intended to focus on robot features, may also contribute to performance gains independently of the core idea. Similarly, the predictor head's specific design could be a confounding factor. Without careful ablation studies, it's impossible to determine if the observed improvements stem from the robot-centric modeling itself or from these additional architectural choices.
- The generalization ability of the proposed model seems limited. Significant performance drops occur under environmental disturbances, particularly in the Sweep-Into task (Figure 8(b)). Additionally, the focus on disturbance testing should extend to other variables like robot arm appearance, base position, and camera view. The experiments only consider a limited set of environmental disturbances, such as changes in background texture. The model's robustness to variations in robot appearance (e.g., different colors or textures), base position (e.g., slightly shifted or rotated), and camera viewpoint (e.g., different angles or distances) remains untested. These factors are crucial for real-world deployment and should be investigated to assess the true generalization capability of the proposed approach.
- The selected tasks appear relatively simple. It would be beneficial to evaluate the modeling effectiveness on more complex embodiments, such as dexterous hands or humanoids, as evaluated in [1]. The MetaWorld tasks, while useful for initial evaluation, do not fully capture the complexities of real-world manipulation. Evaluating the model on tasks involving more complex embodiments, such as dexterous hands (e.g., those in the Adroit or MyoSuite benchmarks) or humanoid robots, would provide a more comprehensive assessment of its modeling capabilities. These more complex systems involve higher degrees of freedom, intricate dynamics, and more challenging visual perception problems.
- The absence of ablation studies. An analysis of each design's impact—such as the warm-up stage, warm-up data choice, or removal of components—would assist the understanding. The lack of ablation studies makes it difficult to understand the contribution of each component. For example, the warm-up stage, which is crucial for pre-training the robot dynamics model, should be evaluated with different amounts of data and different data collection strategies. Furthermore, the impact of the mask-guided decoder, the interaction model, and the specific design of the predictor head should be analyzed by removing them individually or replacing them with simpler alternatives.
- Construction error may not be a good metric to measure the ability to model robot dynamics, because the error may mainly caused by the environmental dynamics error. As an extreme case, the vanilla world model may be good at robot dynamics but very poor at environmental modeling. The authors should address this concern. The reconstruction error, while commonly used, is not a direct measure of the quality of the robot dynamics model. The error could be dominated by inaccuracies in modeling the environment, making it difficult to isolate the performance of the robot dynamics model. A vanilla world model, for example, might be very accurate in modeling robot dynamics but perform poorly in modeling environmental dynamics, leading to a high overall reconstruction error. A more direct metric, such as predicting the robot's future state given its current state and action, would be more appropriate.
- Testing the extension capability of the proposed method on other state-of-the-art algorithms, like TD-MPC2 [1], would significantly strengthen this paper. The current evaluation focuses on comparing the proposed method with a vanilla DreamerV3 baseline. However, it would be beneficial to evaluate the proposed method in conjunction with other state-of-the-art model-based reinforcement learning algorithms, such as TD-MPC2. This would provide a more comprehensive assessment of its performance and potential for integration into existing frameworks.

### Questions
- What is the performance in a multi-task setup, following [1]?
- What do the attention maps signify in all figures? The highlighted regions seem meaningless.
- The gripper reconstruction in Figure 5 appears inadequate. Could the authors clarify this?

[1] Hansen, N., Su, H., & Wang, X. TD-MPC2: Scalable, Robust World Models for Continuous Control. In *The Twelfth International Conference on Learning Representations*.

[2] Sferrazza, C., Huang, D. M., Lin, X., Lee, Y., & Abbeel, P. (2024). Humanoidbench: Simulated humanoid benchmark for whole-body locomotion and manipulation. *arXiv preprint arXiv:2403.10506*.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces the Robo-Centric World Model (RCWM), designed to improve sample efficiency and robustness in model-based reinforcement learning (MBRL) for visual robot control. RCWM achieves this by decoupling robot dynamics from environment dynamics, allowing each component to be modeled independently while an interaction model, based on cross-attention, captures the effect of robot actions on the environment. The model’s training pipeline includes a mask-guided warmup using robot segmentation masks, followed by mask-free pre-training and fine-tuning, ensuring RCWM can robustly handle novel tasks and disturbances.

### Strengths
* The paper is well-written and well-organized.
* The idea of decoupling robot and environment dynamics is very novel and holds potential value for improving the efficiency and robustness of learning algorithms.
* The proposed method demonstrates resilience against visual disturbances and changing backgrounds.

### Weaknesses
 * More baselines should be included, such as a leading model-based RL algorithm TD-MPC2 (https://arxiv.org/abs/2310.16828). Meanwhile, it is important to report the sample-efficiency comparison with leading model-free algorithms like DrM (https://arxiv.org/pdf/2310.19668). The lack of comparison with TD-MPC2, a state-of-the-art model-based RL method, makes it difficult to assess the relative performance of the proposed approach. Furthermore, while the paper focuses on sample efficiency, a comparison with a leading model-free algorithm like DrM is necessary to understand the trade-offs between the two approaches.
* More experiments should be conducted in more challenging tasks such as dexterous manipulations in Adroit (https://arxiv.org/pdf/1709.10087) to validate the effectiveness of the proposed method. The current experiments are limited to relatively simple manipulation tasks. Evaluating the method on more complex tasks, such as those found in the Adroit benchmark, would provide a more comprehensive assessment of its capabilities, particularly in handling high-dimensional action spaces and intricate object interactions.
* It is also essential to validate the proposed method in real-world experiment (such as Box Close task). The absence of real-world validation limits the practical applicability of the proposed method. While simulation results are promising, real-world experiments are crucial to demonstrate the robustness of the approach to sensor noise, model inaccuracies, and other real-world challenges.

### Questions
* How might RCWM handle scenarios where prior robot segmentation masks are unavailable or difficult to obtain? Could an alternative approach to disentangling robot and environment dynamics be feasible in these cases?
* Given RCWM's reliance on cross-attention for modeling interactions, how well would it handle environments with more unpredictable or dynamic elements, such as deformable objects or non-static obstacles?
* What will happen if we only use the replay buffer from 1 task trained by DreamerV3 as the dataset?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces the Robo-Centric World Model (RCWM), which decouples robot dynamics from environmental dynamics, and employs an interaction model to evaluate the impact of the robot's actions on the environment. The authors use SAM2 to create segment masks for the robot, which are then used to warmup the mask reconstruction process. The subsequent pre-training is conducted without mask usage. Experiments are conducted in the Meta-world domain, demonstrating through quantitative and visual results that RCWM can learn distinct dynamics and show robustness against disturbances.

### Strengths
- The decomposition of robot and environmental dynamics is a straightforward method that enables transfer of shared knowledge.
- The distillation of SAM into world models that enables the agent to distinguish robot and background is an interesting practice.
- The experimental results show improvement over the base model, with the rich visualization results offering valuable insights.

### Weaknesses
 - Discussion and comparison to related works are missing. The authors state that action-free pre-training methods "are of limited help when confronted with robot manipulation tasks that require accurate predictions". However, the paper only carries out experiments in the Meta-world domain, where other action-free pre-training methods also demonstrate good performance. Specifically, the paper lacks a comparison to methods that leverage similar ideas of decoupling or disentanglement in world model learning, which could provide a more comprehensive understanding of the advantages and disadvantages of the proposed approach.
- Limitations are not addressed adequately. RCWM limits the interaction between the robot and the environment from two-way to one-way, which is acceptable for Meta-world since pre-training and fine-tuning are carried out on the same platform. However, RCWM may encounter difficulties when applied to certain types of real-world visual robotics tasks, such as dealing with a different friction coefficient or a different tilting angle for the table. The paper does not discuss how the model would handle scenarios where the robot's dynamics are significantly altered by external factors or unexpected interactions, which is a critical aspect for real-world deployment.


### Questions
- In Figure 7(a), do RCWM and vanilla WM use the same set of trajectories for evaluation, or are the trajectories sampled independently for each model? If the models share the same trajectories, how are they sampled?
- In Figure 7(b), a sharp turn can be observed between 10 and 20 rollout steps for the stick-push task. Why would this happen?
- A discussion section comparing RCWM to previous action-free pre-training methods should be added. The authors should compare RCWM to previous action-free pre-training methods specifically on robot manipulation tasks that requires accurate predictions.
- A limitation section about the applicability and generality scope of RCWM should be added. The authors should explicitly discuss the potential limitations in applying RCWM to real-world scenarios with varying physical properties.

Minor comments:
- The notation for the baseline method is a bit inconsistent. I suggest changing all "vanilla WM" notations to "DreamerV3" or vice versa for better readability.
- Typo: "dynamic model" should be "dynamics model"

### Soundness
3

### Presentation
3

### Contribution
2
