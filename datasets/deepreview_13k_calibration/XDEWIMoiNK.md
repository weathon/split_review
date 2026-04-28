# Mobile Object Rearrangement with Learned Localization Uncertainty

- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 3, 5, 5

## Abstract
Mobile object rearrangement (MOR) is a pivotal embodied AI task for a mobile agent to move objects to their target locations. 
While previous works rely on accurate pose information, we focus on scenarios where the agent needs to always localize both itself and the objects. This is challenging because accurate rearrangement depends on precise localization, yet localization in such a non-static environment is often disturbed by changes in the surroundings after rearrangement. To address this challenge, we first learn an effective representation for MOR only from sequential first-person view RGB images. It recurrently estimates agent and object poses, along with their associated uncertainties. With such uncertainty-aware localization as the input, we can then hierarchically train rearrangement policy networks for MOR. We develop and open source a simplified, yet challenging 3D MOR simulation environment to evaluate our method and relevant embodied AI baselines. Extensive comparisons reveal better performances of our method than baselines and the need for uncertainty estimation in our task.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes Mobile Object Rearrangement (MOR), in which the agent is tasked with recovering a goal configuration from an initial state without the use of depth maps, GPS, or ground truth positions (GT positions). The authors introduce a modular approach that begins by training an L-Net to estimate poses with uncertainty, followed by learning a rearrangement policy through Hierarchical Reinforcement Learning (RL). The proposed method demonstrates superior performance compared to the baselines in the MOR tasks.

### Strengths
1. This paper addresses an important problem in visual object rearrangement: learning a policy that does not rely on privileged information as input.
2. The introduction is well-written.

### Weaknesses
1. (Motivation) Why couldn't the agent utilize depth information and conduct simultaneous localization and mapping (SLAM)? It doesn't seem necessary to completely forgo the use of internal GPS and depth sensors.

2. (Method) The proposed method heavily relies on the localization network (L-Net). However, training the L-Net necessitates extensive pre-training (e.g., 10,000 episodes in the proposed simplified environment), raising questions about its suitability for deployment in more complex environments like Habitat, AI2Thor, or the real world.

3. (Evaluation) The evaluation of the proposed method takes place in toy-like environments, and real-world experiments assume ground-truth poses of agents and objects.

4. (Writing) I recommend that the authors enhance the clarity of the writing in Sections 3 and 4. These sections currently contain an overwhelming amount of details and lack structured and logically coherent expressions.

### Questions
How does the agent perceive the target poses of the objects? Does it estimate these poses from another unshuffled environment?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the problem of geometric goal object rearrangement in a setting where the agent does not have ground-truth GPS+Compass. Towards this end, the authors propose a simplified environment to study this problem.

They propose a policy where agent tracking is decoupled from navigation/manipulation. The task itself is broken down into a high-level controller policy that selects which object to rearrange next, a pick policy, and a drop policy. Their proposed method is shown to outperform various baselines.

### Strengths
This paper studies an important problem
Baselines and ablations for the rearrangement policy are well thought-out.
The reviewer found the landmark experiment to be quite interesting.

### Weaknesses
The environment used is not visually realistic and does not support their claim that "MOR adopts visual inputs from 3D simulations that are easier to transfer to real-world robotics systems." The environment itself is a simple convex shape with no obstacles or visual features besides a black-and-white checkerboard pattern on the walls. The reviewer is concerned that these two extreme simplifications in the environment mean that any conclusions drawn won't transfer to more realistic settings. This concern is reinforced by the result that CLIP features were not appropriate for this environment.

Additional baselines are needed for L-NET. The embodied AI literature has a large number of tracking methods that were developed for PointGoal navigation, see Partsey et al 2022 for one example. Specifically, methods that incorporate uncertainty in their pose estimation should be included as a baseline to better understand the contribution of the proposed method. The current baselines do not adequately address the specific claims made about the benefits of uncertainty estimation in the L-Net.

The name "Mobile Object Rearrangement (MOR)" is confusing as the word mobile could also be used to describe the agent being mobile and differentiate the task from table-top rearrangement.

The figure 3 caption is very long and has key method details. Method details should not be in figure captions as the reader does not know when they are supposed to read these details.

### Questions
1. Is the agent always initialized in the center of the environment?
2. What is the advantage of using a distribution for agent/object pose instead of using regression?
3. Why is it necessary to predict object position? Since the object position is given relative the agent position at the start of the episode, the object's location with respect to the agent's position can always be computed given the agent's pose.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a variation of the Embodied AI rearrangement task, that drops the assumption of ground-truth agent pose and perfect localization of the objects during the task. The proposed approach first learns to localize jointly both the agent and the objects in the environment and employs a hierarchical pick and drop policy for executing the task.

### Strengths
The paper is easy to follow with the proposed task and methodology are clearly explained. The separate training of the pick and drop policies makes sense, I would be curious to see the performance improvement compared to a single training stage of the proposed hierarchical policy network.

### Weaknesses
My main issue with this work are the chosen simulation environments which are visually and structurally trivial with primitive objects. The paper mentions that the main challenge of the object rearrangement task is precise localization, but I fail to see how the localization of either the agent or the objects is a challenge in these environments. Have the authors tried classical visual odometry or monocular slam with object detection to register the objects in a map? The proposed L-Net seems kind of an overkill in this setup. The authors also mention that partial observability and their choice of using a single first-person RGB view makes the problem harder. The environment is small enough without obstacles that it can be fully observed in very few views, while including an RGB-D sensor is a fair assumption in robotic settings.

Even in cases where the localization is a challenge, it is an orthogonal problem to the re-arrangement task. I am expecting that the planning is more of a bottleneck here due to the non-trivial sequence of actions that need to be decided (i.e., moving a certain object first might lead to a state where an optimal solution is not possible anymore). This is also recognized as the main challenge of this problem by Batra et al. (2020a).

### Questions
--

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper focuses on mobile object rearrangement (MoR) and the scenarios where the localization is imperfect. To this end, the authors propose to use a recurrent network (L-Net) to estimate agent and object poses with uncertainties (following Gaussian distributions), and train a policy network (P-Net) based on estimated poses. The authors compare the proposed method with baselines on a simulation benchmark, and show some qualitative results in the real world.

### Strengths
1. The paper studies the scenarios where the localization is imperfect, which is an under-explored aspect of prior works (e.g., Habitat 2.0, Multi-skill Mobile Manipulation for Object Rearrangement).

### Weaknesses
1. Missing baselines or explanations about related works. Can the authors explain why Neural SLAM [1] is not included as a baseline? In NeuralSLAM, the NeuralSLAM module estimates the 2D map and relative pose as what the L-Net does in this paper, and a global policy is trained to explore the map but can be adapted to achieve arrangement tasks as what the P-Net does in this paper. Besides, [2] showcases that using explicitly estimated poses can be helpful for learning mobile manipulation.

2. The paper lacks clarity on the specific implementation of the "ResNet + $\Delta$Pose" baseline. It's unclear how the relative pose is acquired, especially given that ground truth poses are not typically available in real-world scenarios. Furthermore, the absence of results for this baseline in the "Pick" task raises questions about its general applicability and the consistency of the experimental setup.

3. The use of a recurrent network is not consistently applied across all baselines. Specifically, it is unclear why baselines like ResNet + Img and ResNet + Landmark do not utilize a recurrent network, especially when the proposed method does. This inconsistency makes it difficult to fairly compare the performance gains of the proposed method with the baselines. The authors should clarify the reasoning behind this design choice.

4. The paper does not provide sufficient quantitative or qualitative analysis of the estimated poses and uncertainties. While the method proposes to estimate pose uncertainties, there is no clear evaluation of the quality of these estimations. It is important to demonstrate how well the L-Net can estimate both the poses and their associated uncertainties, beyond just the performance on downstream tasks.

### Questions
1. Does the "global coordinate" in Sec 4.1 mean "episodic coordinate"? For example, the initial agent position is considered (0, 0).
2. How do the authors acquire "relative pose" for the baseline "ResNet + $\Delta$Pose"? And why are results for these baselines missing for "Pick"?
3. Is the recurrent network used for baselines like ResNet + Img and ResNet + Landmark?
4. Can the authors qualitatively and quantitatively show how well the estimated poses are?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
