# NaVILA: Legged Robot Vision-Language-Action Model for Navigation

- Decision: Reject
- Scores: 3, 6, 8, 5

## Abstract
\vspace{-1em}
This paper proposes to solve the problem of Vision-and-Language Navigation with legged robots, which not only provides a flexible way for humans to command but also allows the robot to navigate through more challenging and cluttered scenes. However, it is non-trivial to translate human language instructions all the way to low-level leg joint actions. We propose \method, a 2-level framework that unifies a Vision-Language-Action model (VLA) with locomotion skills. Instead of directly predicting low-level actions from VLA, \method first generates mid-level actions with spatial information in the form of language, (e.g., ``moving forward 75cm''), which serves as an input for a visual locomotion RL policy for execution. \method substantially improves previous approaches on existing benchmarks. The same advantages are demonstrated in our newly developed benchmarks with IsaacLab, featuring more realistic scenes, low-level controls, and real-world robot experiments. \url{https://navila-bot.io/}

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents a method to perform navigation tasks with legged robots. To do so, they train a VLM to translate high-level language instructions into low-level navigation commands, such as "move forward 75 cm" or "turn left 30 degrees," based on current and past single-view RGB image observations. These commands are then executed by a legged robot using a locomotion policy that is trained beforehand in a physics simulator through reinforcement learning to follow velocity commands and avoid obstacles. 
The performance of the VLM is evaluated on standard benchmarks for navigation in continuous environments, and a benchmark designed to evaluate navigation and obstacle avoidance is introduced. Finally, the system is deployed on a real Go2 robot.

### Strengths
- Real-World Deployment: The authors have successfully implemented their navigation policy on a real legged robot, proving its capability to execute complex navigational tasks in diverse real-world scenarios, including both indoor and outdoor settings.
- Good experimental results in simulated navigation environments: The proposed method outperforms previous approaches for navigation in continuous environments when using only a single RGB camera.

### Weaknesses
A significant issue with the paper is that, despite its emphasis on legged locomotion, the navigation skills demonstrated do not inherently require this form of mobility. All the navigation tasks demonstrated could likely be accomplished by wheeled robots without altering the proposed framework. In contrast, prior works on VLA models for legged robots have incorporated capabilities unique to legged robots, such as climbing and crawling under obstacles [1, 2, 3, 4]. The action space of the proposed VLA model is limited to basic navigation commands: “move forward X cm”, “'turn left/right X degrees”, and “'stop”, which abstracts away skills unique to legged robots. The real-world deployment is evaluated in environments where wheeled robots could also navigate effectively. Low-level obstacle avoidance is not exclusive to legged robots. Additionally, it is unclear if the proposed framework for the VLA, which involves supervised fine-tuning from navigation datasets, can handle these kinds of actions only legged robots can perform. The proposed benchmark in simulation, focusing mostly on navigation and collision avoidance, also does not address challenges specific to legged robots.

### Questions
Could the proposed approach be extended to navigation tasks that demand more advanced locomotion skills?

### Soundness
2

### Presentation
3

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
This paper present NaVILA, a framework that integrates vision-language models with locomotion skills for navigation tasks. It uses high-level language commands and a real-time policy for obstacle avoidance. NaVILA maintains reasoning through language actions, avoiding overfitting and allowing broader task training.

### Strengths
1. This paper extends NaVid to legged robot scenarios and demonstrates strong performance in real-world applications.
2. The framework effectively integrates 3D scenes into the policy, enhancing robustness, particularly in real scenarios. This is a commendable attempt.

### Weaknesses
1. One issue that remains is the inference time, particularly in the demo where the quadruped robot must wait for the large model to complete inference before executing tasks. This waiting period for model inference can lead to instability in motion, which is a point worth considering for resolution.

2. It is unclear whether the model's performance has been tested in an open environment. Currently, the demos presented are tests conducted in a semi-open environment. The authors could consider introducing environments with greater variance from the dataset to test the model's generalizability in real-world scenarios.

### Questions
Please refer to the weakness.

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
4

### Summary
This paper introduces a large vision-language-action model for enabling vision-language navigation for a legged robot. Instead of inferring joint states from image context, authors follow a two step process: (i) predicting the mid-level actions in textual form and (ii) providing these actions to a low-level policy for synthesizing joint action commands. Authors observe the limitations of video-language models (due to lack of large scale data set for the task) and hence take the approach of adapting a VLM to predict actions based on sampled frames from a video. The authors modify prior work VILA to the VLN task by (i) pretraining on generic data sets, (ii) SFT using  VLN data sets and (iii) incorporating auxiliary tasks such as summarization and QA in the associated navigation data. The low-level policy architecture operates on a specific set of skills such as moving forward, turning left etc. and is trained by taking in low-level point cloud maps. Experiments show effectiveness across several benchmarks. Notably performance gain is higher on complex instructions. Finally, the authors also release a new benchmark for the research community.

### Strengths
- The paper contributes insights into how to adapt a VLM to predict actions conditioned on present and past visual context. The paper shows how to factor the navigation task as predicting the mid-level actions described in a text form followed by learning a low-level policy. The paper describes the training strategy and SFT data blend and as well as inclusion of auxiliary tasks during training.  

- Authors demonstrate their results on common benchmarks, extensively comparing their results to other approaches. Further, a new benchmark is proposed, specifically suited to the problem setting. 

- Results indicate higher performance gains on complex instructions. Strong results on legged platforms. Indicative results on the humanoid.

### Weaknesses
A key motivation for NaVILA is the ability to generalise using the separation between high-level action prediction and the presence of a low-level policy. The experiments demonstrated are impressive in their sequentiality but do not fully highlight the generalization capacity. Specifically, where the low-level plan changes with high-level inputs and visa versa.


### Questions
- The authors emphasize the need for including both the current view and a random sample of past frames (a memory) for predicting actions. In this regard, how much memory (number of samples) is needed for the tasks considered. Presumably, the length would depend on the horizon of the underlying navigation task. 

- How does NaVILA respond to action failures. Consider asking a robot to move forward by a distance but the path is either blocked half way or the robot develops a fault. In this case, does the VLA component monitor action execution and replan? More generally, do the low-level actions inform adapation of the high-level plan?

- The core contribution of NaVILA is one of factoring the navigation action generation into predicting mid-level actions in textual form, followed by a low-level join control policy opens doors for behaviour adapation via reasoning. To what extent can the robot perform semantic queries on the world while deciding high-level actions. For example, consider a modification of the action sequence show in top row of figure 1. If one modifies the second phrase to “if you see the stair bar then turn left else go right”, would NaVILA be able to adapt?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes NaViLA, a hierarchical framework for vision-language-based legged robot navigation tasks. The framework consists of a high-level vision-language model (VLM) and a vision-based locomotion policy. The high-level VLM converts historical camera observations and user instructions into commands for the low-level locomotion policy to follow. It takes current and previous observations as input and outputs language-based planning instructions. The VLM is fine-tuned from an existing model using an augmented online dataset. The locomotion policy is trained with reinforcement learning (RL) in a physics-based simulation. The proposed method is compared with various benchmarks, and the results show that it outperforms baseline methods. Additionally, a new benchmark for evaluating vision-language navigation (VLN) in a physics-based simulation is introduced. Finally, the proposed method is successfully implemented on a real-world robot.

### Strengths
- The proposed method looks reliable and easy to be reproduced.
- Baselines are compared extensively.
- The real world demonstration look good.
- Paper structure is clear and easy to follow.

### Weaknesses
 - The motivation for using a legged robot is unclear to me. Since the VLN model is trained separately, the low-level control policy should not impact the high-level model, as long as the low-level policy can achieve the desired goal. 

 - The experimental analysis could be improved. For example, in the 'High-fidelity VLN-CE-Isaac Benchmark' section, the robot with vision outperforms the blind policy. But why is this the case? Are there obstacles that need to be avoided? Should the VLN handle obstacle avoidance? Are there any examples that illustrate the different behaviors of these two policies?

 - The overall contribution is limited. From my perspective, the main contribution is fine-tuning a VLM that processes vision input and outputs several predefined intermediate actions.

### Questions
Please review the weaknesses section. For the overall contribution, I would appreciate a more detailed summary during the rebuttal.

### Soundness
4

### Presentation
3

### Contribution
2
