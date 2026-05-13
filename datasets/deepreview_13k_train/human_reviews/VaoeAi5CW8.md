# Diffusion Trajectory-guided Policy: A Novel Framework for Long-Horizon Robot Manipulation

- Decision: Reject
- Scores: 5, 3, 3, 6

## Abstract
Recently, Vision-Language Models (VLMs) have made substantial progress in robot imitation learning, benefiting from increased amounts of demonstration data. However, the high cost of data collection remains a significant bottleneck, and the scarcity of demonstrations often result in poor generalization of the imitation policy, especially in long-horizon robotic manipulation tasks. To address these challenges, we propose the Diffusion Trajectory-guided Policy (DTP) framework, which generates task-relevant trajectories through a diffusion model to guide policy learning for long-horizon tasks. Furthermore, we demonstrate that our DTP method offers a useful interface for prompt engineering, providing a novel way to connect robot manipulation skills with interactions involving LLMs or humans. Our approach employs a two-stage training process: initially, we train a generative vision-language model to create diffusion task-relevant trajectories, then refine the imitation policy using these trajectories. We validate that the DTP method achieves substantial performance improvements in extensive experiments on the CALVIN simulation benchmark, starting from scratch without any external pretraining. Our approach outperforms state-of-the-art baselines by an average of 25% in success rate across various settings.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes an imitation learning method that uses a diffusion trajectory model to guide policy learning. The diffusion trajectory model is first pre-trained on robot videos to map the robot's motion trajectory into the camera image. The policy is then trained with guidance from the output of the trajectory model. Experiments in CALVIN show that this approach can help the policy learn long-horizon tasks better than prior work.

### Strengths
The paper is well-written, and the results on the CALVIN benchmark seems to be compelling compared to the included baselines. There are also several ablations that provide insights.

### Weaknesses
1. I’m not entirely convinced why the proposed method is better than the end-to-end diffusion policy with action chunking [1, 2]. Predicting action chunks seems similar to predicting the trajectory (or gripper motion), so why is the proposed two-stage approach preferable to training a single policy to predict the long-term actions? Would it be possible to compare to these apporaches?

2. The paper conducted its evaluation on the CALVIN benchmark, but it seems the proposed method underperforms compared to SOTA methods (e.g., RoboUniView [3], MDT [4]). How does the proposed method compare to these works? Is there any reason why they were not included?

3. To train the DTM, the dataset requires the robot's global states to map the trajectory. This assumption limits the method's ability to leverage additional data, such as human / non-robot videos. It would be more interesting to explore a more general way to obtain 2D trajectories more easily, without relying on proprioceptive information.

### Questions
1. In the 10%ABCD->D task, is the Diffusion Trajectory Model also trained on the limited 10% dataset?

2. Is there a specific reason why the wrist camera is necessary? How would DTP perform if only a static camera were used?

### Soundness
3

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
4

### Summary
The authors propose an imitation learning method that additionally conditions on predicted robot gripper trajectories represented as a sequence of 2D key-points. In the first stage, given an initial observation and language instruction, a diffusion model is trained to generate a full sequence of key-points that correspond to the gripper motion that completes the task. In the second stage, a policy is trained to predict actions given the current observation, language instruction, and sequence of gripper key-points. For the policy, the authors fine-tune a VLA model from prior work, GR-1, that was pre-trained on video prediction. At test time the diffusion model is used to generate the sequence of key-points to condition the policy. Experiments on the CALVIN simulated imitation learning benchmark demonstrate that this method outperforms prior methods on long-horizon language-conditioned tasks. The method improves performance with or without the video pre-training from GR-1, though video pre-training does improve the results. Experiments also find that scaling data for only the key-point sequence predictor improves downstream performance.

### Strengths
The paper addresses an important problem, long-horizon language-conditioned imitation learning, with a combination of powerful techniques: generative modeling with diffusion and pre-training robot policies on vision-language tasks (i.e using GR-1). Generating intermediate state/action representations for policy conditioning is also an active area of research at the moment, so it's likely the community would find this interesting. 

The paper compares to relevant prior work on a well-established baseline, CALVIN, and performs a couple interesting ablations, (1) removing the GR-1 pre-training and (2) limiting data for just the policy. The method's performance on CALVIN is state-of-the-art as of when the paper was submitted.

### Weaknesses
 
**Motivation**

The motivation of the method is not entirely clear. The intro hints at trying to improve semantic and environment generalization or performance on long-horizon tasks, but does not explain how the method explicitly addresses these challenges. It's only stated that the key-point trajectories "reduce the feature disparity between the vision-language input and action spaces." After reading the full paper, my guess at the motivation is that GR-1 is pre-trained on human video prediction so one could imagine that conditioning on key-points somehow makes better use of the GR-1 initialization than directly predicting actions (since key-points on an image might map more directly to features learned for video prediction). However this reasoning is not explicitly stated anywhere in the paper. Also, the method still provides improvements without GR-1 pre-training so a different explanation/motivation would be needed in that case. Without the video prediction pre-training, I could imagine that the 2D key-point trajectories help with longer horizon behaviors by acting as a plan. If the motivation is planning, a relevant baseline would be to simply perform action chunking [9], i.e predicting multiple actions into the future. One could imagine that action chunking serves a similar purpose to predicting future gripper key-points and is much simpler to implement. 

**Novelty**

My larger concern is novelty. The paper is very similar to several papers that predict and condition on gripper key-point trajectories [1, 2, 3, 4, 5, 6]. In particular Any-Point Trajectory Modeling (ATM) [1] and RT-Trajectory [2] are quite similar. These papers are addressed in the related work, but the stated differences don't seem meaningful. The related work says that RT-Trajectory generates linear trajectories rather than particle trajectories, but I'm not sure what that means or why it's a relevant difference. It's also said that ATM predicts trajectories for multiple points in the image rather than just the gripper. However, I'm not sure why predicting only the gripper movement is beneficial (in fact it seems like it could be useful to predict the movements of objects as well). Additionally, tracking just the gripper introduces the additional assumption of a calibrated camera. ATM does not have this assumption. ATM also performs more thorough evaluation by performing experiments on a real robot, and additionally demonstrates improvements from training the point trajectory predictor on human videos and other robot morphologies. 

Other relevant papers to discuss in the related work include chain-of-thought with VLAs [7] and visual prompting with VLMs [8, among many others].

**Evaluation**

The evaluation of the proposed method is limited to the simulated CALVIN benchmark, which makes it difficult to determine if the method would generalize to real robot applications. Papers proposing similar methods typically evaluate over a much broader range of simulated and real robot tasks (see cited papers below).

**Presentation/Writing**

Along with the lack of clear motivation in the intro as mentioned above, there are several other issues with the presentation:

- The intro doesn't state that the method predicts 2D key-point trajectories so it's easy for the reader to assume the method is doing video prediction.
- It's not clear whether the video prediction loss is used when fine-tuning GR-1.
- It's not clear from the method section whether the method uses just the architecture from GR-1 or the pre-trained model itself (though it becomes clear in the experiments). 
- I would replace the term "diffusion trajectory" with "key-point trajectory" since diffusion describes the generation process and not the type of trajectory.
- The inference (evaluation time) procedure is never described in the method section. I'm assuming that at evaluation time the diffusion trajectory model is used to generate a key-point trajectory which is then used to condition the policy, whereas during training the ground truth key-point trajectories are used to train the policy.
- In section 4.4, the subsection title "Diffusion Trajectory Prompt" should be called "Re-planning" or something similar. This section should also cite model predictive control or receding horizon control work since it seems like that's the technique that is being used here. 
- In section 4.4, I could not understand what was meant by "Strategic Prompting" 

### Questions
- What are the differences between this work and ATM and RT-trajectory?
- Is the video prediction loss used when fine-tuning GR-1?
- What is "strategic prompting" (section 4.4)?

### Soundness
3

### Presentation
2

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
This paper introduces a novel imitation learning framework, the Diffusion Trajectory-guided Policy (DTP), designed to address challenges in long-horizon robot manipulation tasks. The core contribution of the paper is the use of diffusion models to generate task-relevant 2D-particle trajectories that guide the learning of a robot’s manipulation policy. The framework operates in two stages: the first stage involves training a diffusion trajectory model (DTM) using language and vision inputs to generate trajectories, and the second stage uses these trajectories to refine the robot's policy. The authors validate their approach on the CALVIN benchmark, demonstrating significant improvements in performance over baseline methods in various long-horizon manipulation tasks.

### Strengths
1. The paper presents an innovative use of diffusion models to generate task-relevant trajectories.
2. The method achieves substantial performance gains, with a 25% higher success rate over baselines.

### Weaknesses
1. Lack of real-world robot experiments.
2. Lack of novelty. There seems to be no too much takeaway from the designed method, as a lot of works have try to incorporate the diffusion process into long-horizon robotic manipulation.

### Questions
See weakness.

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
5

### Summary
This paper introduces a diffusion trajectory-guided framework that utilizes diffusion trajectories, generated in the RGB domain, to enhance policy learning in long-horizon robot manipulation tasks.

### Strengths
The core idea is compelling, as it utilizes a diffusion-based method to generate trajectories. Additionally, the method's intricate design enables the model to effectively produce particle trajectories.

### Weaknesses
-The paper specifically highlights that the generated trajectory can enhance the performance of long-horizon tasks. However, as tasks grow longer, trajectories may overlap. It is unclear how the proposed approach addresses this scenario, particularly if the atomic-level skills themselves involve complex, multi-stage movements that could lead to self-intersections or collisions within the generated trajectory. The lack of discussion on how the method handles such overlapping or self-intersecting trajectories is a significant concern.

-The paper lacks real-world experiments, making it difficult to assess its practical effectiveness. While real-world execution experiments may be complex, at the very least, visualizations of real-world generated trajectories should be included to provide some insight. The absence of any real-world validation, even in a qualitative form, limits the confidence in the method's applicability beyond simulation.

-The introduction mentions that robot data is sparse, yet the diffusion-based trajectory model relies on robot data for training. This inconsistency should be addressed, and claims in the background section should be made more carefully to avoid confusion. The reliance on robot data for training the diffusion model, while claiming data scarcity, raises questions about the practical feasibility of the approach in truly data-scarce environments.

-How effective are the generated trajectories? The authors should design experiments to evaluate this, such as measuring the similarity between generated trajectories and their corresponding ground-truth. Additionally, if the generated trajectory contains noise, it’s important to assess how well the subsequent policy model can handle such inaccuracies. It's crucial to understand the robustness of the policy model to variations and noise in the generated trajectories, as this directly impacts the reliability of the overall system.

### Questions
Please refer to weakness section

### Soundness
3

### Presentation
3

### Contribution
3
