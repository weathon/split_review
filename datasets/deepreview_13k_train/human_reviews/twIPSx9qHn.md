# Cross-Embodiment Dexterous Grasping with Reinforcement Learning

- Decision: Accept
- Scores: 6, 6, 3

## Abstract
Dexterous hands exhibit significant potential for complex real-world grasping tasks. While recent studies have primarily focused on learning policies for specific robotic hands, the development of a universal policy that controls diverse dexterous hands remains largely unexplored.
In this work, we study the learning of cross-embodiment dexterous grasping policies using reinforcement learning (RL). Inspired by the capability of human hands to control various dexterous hands through teleoperation, we propose a universal action space based on the human hand's eigengrasps. The policy outputs eigengrasp actions that are then converted into specific joint actions for each robot hand through a retargeting mapping. We simplify the robot hand's proprioception to include only the positions of fingertips and the palm, offering a unified observation space across different robot hands.
Our approach demonstrates an 80\% success rate in grasping objects from the YCB dataset across four distinct embodiments using a single vision-based policy. Additionally, our policy exhibits zero-shot generalization to two previously unseen embodiments and significant improvement in efficient finetuning.
For further details and videos, visit our \href{https://sites.google.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper learns a unified vision-based reinforcement learning policy via teacher-student learning to control various dexterous hands for grasping different objects. The authors propose a unified observation space across various hands, and a universal action space inspired by human hand teleoperation. The learned policy can generalize to unseen dexterous hands in a zero-shot manner.

### Strengths
- The authors conducted a comprehensive benchmark and ablation study. 
- The presentation of the paper is clear and well-structured.

### Weaknesses
 - Only LEAP Hand was tested in the real-world experiments.
- Some failure cases should be included in the video.
- Joint position of the arm is included for training policies, which might affect the generalizability to different arms.
- More design choices should be analyzed regarding the impact on generalizability. See the questions below.

### Questions
- The authors used four dexterous hands for training and would like to include more different hands in the future. It would be interesting to investigate the impact of the number of hands used for training on the learning performance, e.g., generalizability. 
- The dexterous hands for training and testing consist of either 4-fingered or 5-fingered configurations with different DoFs. What would be the impact if for example one or more 3-fingered hand is also included for training?
- The authors randomized the origin position of the joint connecting the hand and the arm to increase robustness and transferability of the policy. What would be the impact of extending this to randomize additional hand parameters?

### Soundness
3

### Presentation
4

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
This paper presents a method for learning a unified policy for dexterous grasping that can transfer to unseen hand morphologies. It achieves this by first designing an observation space that contains only fingertip positions and palm pose, which can be shared between different hands. Then, the action space is based on the eigengrasp from the MANO hand model. By using the shared observation and action space, the authors can train a reinforcement learning policy on four different hands and transfer the learned policy to new hands.

### Strengths
This paper presents a clear story on training policies with multiple embodiments. The paper is well-written and illustrates the motivation from human teleoperation well.

The design of the action space (i.e., a linear combination of eigengrasp coefficients) is interesting.

The idea of using a neural network to approximate the retargeting is also interesting.

The authors also show that the policy can successfully transfer to the real world by training a student policy with vision as the input.

### Weaknesses
From my understanding, the observation space contains four fingertip positions. It is not discussed how to deal with three or five fingers, or if the method is specifically designed for anthropomorphic hands. If this is an intrinsic assumption or limitation, it should be discussed in the main paper.

The authors design several ablation experiments to show the importance of the proposed observation and action space. However, there is still one design missing: What if we train a policy that directly predicts the fingertip positions and palm positions while keeping the observation space the same as the proposed method? The fingertip positions could then be converted to joint positions (independently for each finger) using inverse kinematics. This can also generalize to new hands as long as we have the kinematics structure of the new hand.

The retargeting mapping network needs training for each morphology, which means that when evaluating a new, unseen hand morphology, it requires extra data from the target hand. I’m concerned that this is not a fair comparison to the baselines, which does not use these data.

It is also concerning that increasing the number of eigengrasp does not significantly improve performance (Figure 4). This might indicate that the learned grasping actions are quite similar and may be limited for future applications such as functional grasping.

The real experiments are also limited; only three successful trials are demonstrated.

### Questions
For policy observation, how should different numbers of fingers be handled? From Figure 2, it seems the authors simply consider four fingers of the hand and ignore the others. If the paper only considers anthropomorphic hands with more than four fingers, this should be clearly stated.

Instead of predicting the eigengrasp and performing retargeting mapping, what is the performance of directly predicting fingertip positions?

When evaluating on unseen hands, does the retargeting mapping network use new hand data for training? If this is the case, I believe there should also be a comparison with baselines using those data.

Can you clarify how “MT-Raw-A” makes predictions on the unseen hands? From my understanding, it outputs joint positions for the unseen hands. But what if the unseen hand has a different number of joints compared to the training hands?

Minor questions and suggestions:
* The YCB dataset contains more than 70 objects. Why were only 45 YCB objects used? What was the criterion for selection?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper introduces CrossDex, a method for learning cross-embodiment dexterous grasping by defining a unified, embodiment-independent observation and action space. The action space utilizes eigengrasps of the human hand based on the MANO hand model. To enable efficient training, pre-trained neural networks replace the optimization-based retargeting process from eigengrasps to the joint angles of various embodiments. The policies are trained on grasping tasks using objects from the YCB dataset across different robot hands and evaluated for transferability to unseen embodiments. Additionally, visual policies operating on object point clouds are distilled using DAgger.

### Strengths
**Relevance of the Problem**
- The huge diversity of embodiments presents a significant challenge in embodied AI, making research on cross-embodiment learning highly relevant.

**Method**
- Leveraging pre-trained neural networks to approximate the optimization-based retargeting process across different embodiments is a intuitive approach to ensure efficient, parallelized training.

**Presentation**
- The writing is clear, and the logical flow of the paper effectively outlines studied problem and proposed solution, making it intuitive to follow.
- The visual presentation in Figures 1 and 2 is well-executed, providing a clear overview of the simulation setup and the input-output mapping from observations through policy actions to target joint positions.

### Weaknesses
 **Method and Evaluation**
- The baselines used in the evaluations are ablations of the proposed method and do not appear to be particularly strong for this task.
- Training on 4 embodiments and transferring to 2 novel ones is indeed quite limited, as acknowledged in the limitations section. However, attributing this limitation to 'restricted access to dexterous hand models' is not a compelling justification. Incorporating a simulation with a broader range of dexterous hand models and exploring how the performance of cross-embodiment policies scales with an increasing number of embodiments would add significantly value to the study. Specifically, the lack of diversity in the training set makes it difficult to assess the true generalization potential of the method. The limited number of embodiments might lead to overfitting to the specific characteristics of the training hands, rather than learning a generalizable grasping strategy.
- Details on how the vision policies are trained including camera resolution and a definition of the object point cloud are missing. The description of the point cloud generation is vague, and it is unclear how the point cloud is obtained in simulation and in the real world. The absence of details regarding the camera setup, such as the number of cameras, their positions, and resolutions, makes it difficult to reproduce the results or assess the robustness of the visual policies.


**Results and Claims**
- In section 5.3 it is stated that the cross-embodiment transferabiliy of the learned policy allows for direct deployment of the policy to new hands. This statement is not supported by the performance drop of over 50% between seen and unseen embodiments oberved for CrossDex in Table 1. The claim of direct transferability is misleading given the substantial performance degradation observed on unseen embodiments. A more nuanced discussion of the limitations of the approach is needed.
- In lines 254-255 you state that the "the dimensionality of human hand poses is significantly higher than the DoFs of most
dexterous hands, which can make RL less efficient." However, this high-dimensionality does not seem to be a challenge according to the results in Table 1, where policies using the joint-based action space outperform or perform simlarly to CrossDex in the PPO training stage. Further, related work has shown good performance with PPO in parallized simulators even with very high-dimensional action spaces (https://arxiv.org/abs/2305.12127). The argument that high dimensionality of human hand poses is a limiting factor is not supported by the experimental results, which show that joint-based control performs comparably well, suggesting that the dimensionality reduction may not be the primary driver of performance.
- The comparison to baseline methods does not convincingly support the claim that using eigengrasps is an effective approach to solving this problem. Baseline policies based on joint-level control are not expected to transfer well across embodiments with different and unknown joint limits, especially when there is no information about the function of each joint. Using a baseline that directly controls keypoints in the MANO hand model, rather than using eigengrasps, would be a more appropriate baseline to validate this claim. This approach would more naturally align with the task of positioning the fingers into stable grasping configurations on an object’s surface. Moreover, Figure 9 in the Appendix highlights substantial differences in the resulting joint configurations for the same eigengrasp across different embodiments. For instance, in the first row of the figure, the second hand shows three fingers touching at the tips, whereas in the fifth hand, there is a significant gap between the fingers. These very different grasp configurations raise questions about the reliability of grasp transfer under such variation. The lack of a baseline that directly controls the hand's keypoints makes it difficult to isolate the benefits of the eigengrasp action space. The observed variations in joint configurations across different embodiments for the same eigengrasp further undermine the claim that this action space is a robust solution for cross-embodiment transfer.
- In the ablation on 'Eigengrasp Actions,' Figure 4 examines the effect of varying the number of eigengrasps on performance it is inferred that the method is relatively insensitive to this change. However, the finding that comparable performance can be achieved with just a single eigengrasp raises important questions. This outcome may reflect a characteristic of the problem being studied, which might not require the nuanced control offered by a multi-fingered hand, rather than demonstrating a strength of the proposed method itself. The fact that a single eigengrasp performs comparably well suggests that the task may not be complex enough to fully leverage the benefits of a dexterous hand, and the method's effectiveness might be overstated.


**Minor Points on Writing**
- In line 483, "affect" should be "affects".


***

Overall, the fact that baselines not specifically designed for cross-embodiment transfer still achieve non-negligible success raises doubts about the suitability of the proposed approach. Moreover, a success rate below 40% on unseen embodiments does not justify the claim of direct transferability. This calls into question the overall feasibility of the framing. Additionally, the observation that a single eigengrasp performs comparably well on the task suggests that the task itself may not be sufficiently challenging. More complex manipulation problems are needed to meaningfully assess the impact of the proposed action space.

### Questions
- What exactly are the observations used by the visual policies, and how are they transferred to the real robot system? In lines 809-810 of the appendix, you mention that the vision policies are trained using DAgger in 16,384 parallel environments, which is double the number of environments used for state-based PPO training. Generating visual observations for such a large number of environments seems particularly challenging, especially given that prior works using student-teacher learning to distill vision policies in Isaac Gym have used two orders of magnitude fewer environments (https://arxiv.org/abs/2211.11744, https://arxiv.org/abs/2111.03043). You also state that "the object point cloud p ∈ R^(N×3), which contains N points captured by cameras." Is this captured by one camera per environment? If so, at what resolution, and how does the object point cloud differ from the point cloud obtained directly from the camera?
- Has a quantitative evaluation been conducted on real-robot deployment?
- In lines 346-347 it is stated that "The episode ends either when the task is completed or the object falls off the table". Are episodes also terminated after a certain number of time-steps?
- Is the object shape or ID represented to the state-based policies? If not, is the grouping of objects intended to reduce variability between them enough to allow learning a single grasping policy? If so, how is this grouping performed, and what are the characteristics of the resulting groups? A clearer explanation of the grouping process and its effectiveness in handling object diversity would help clarify how the policy generalizes across different objects.
- In Figure 3, the training performance of cross-embodiment learning is compared to individual training with the Shadow Hand. Is there a reason to specificallly use the Shadow Hand here, rather than the mean of the performance of all single-embodiment policies?

### Soundness
2

### Presentation
2

### Contribution
2
