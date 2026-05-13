# Reinforcement Learning from Wild Animal Videos

- Decision: Reject
- Scores: 5, 5, 6

## Abstract
We propose to learn legged robot locomotion skills by watching thousands of wild animal videos from the internet, such as those featured in nature documentaries. Indeed, such videos offer a rich and diverse collection of plausible motion examples, which could inform how robots should move. To achieve this, we introduce Reinforcement Learning from Wild Animal Videos (RLWAV), a method to ground these motions into physical robots. We first train a video classifier on a large-scale animal video dataset to recognize actions from RGB clips of animals in their natural habitats. We then train a multi-skill policy to control a robot in a physics simulator, using the classification score of a third-person camera capturing videos of the robot's movements as a reward for reinforcement learning. Finally, we directly transfer the learned policy to a real quadruped Solo. Remarkably, despite the extreme gap in both domain and embodiment between animals in the wild and robots, our approach enables the policy to learn diverse skills such as walking, jumping, and keeping still, without relying on reference trajectories nor hand-designed rewards.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper trains a supervised video classification model on a dataset of wild animal videos (walking, running, standing, and jumping). It then uses the video model classifications as rewards to train a policy to control a quadroped robot in simulation. The policy is then transferred onto a quadroped robot in the real world.

### Strengths
- The paper studies an interesting problem of learning reward models from videos
- The proposed approach is interesting and in a good direction
- The paper is well written and the presentation is clear

### Weaknesses
 - Position of the paper (title, abstract, intro) is a bit misleading. It suggests that the reward function would come purely form videos. However, the approach uses a number of hand-designed reward terms such as air time, symmetry, and terminations. I think that this is ok but the positioning of the paper should be updated to reflect that. In the current version of the approach, the video model serves only as part of the overall reward function.
- The results are promising but overall limited. Looking at the supplementary materials video it looks like the learnt skills do not quite match the desired behaviors, "keeping still" seems to be moving and "running" does not seem to be running. The "keeping still" behavior, while stationary in terms of base position, exhibits significant foot movement, which is not characteristic of a truly still posture. Similarly, the "running" behavior appears more like a fast trot, lacking the aerial phase and extended stride length typically associated with running gaits.
- It would be good to ablate the impact of each of the reward terms. The current version of the manuscript includes the symmetry loss ablation which shows that the symmetry term plays a considerable role. The air time reward, while commonly used, should be ablated to understand its specific contribution in this context. Furthermore, the termination reward, which is likely crucial for shaping the behavior, should also be analyzed to determine its influence on the learned policies.

### Questions
Please see above.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces Reinforcement Learning from Wild Animal Videos (RLWAV), a novel method for training quadruped robots to perform locomotion skills by observing wild animal videos. The authors train a video classifier on a large dataset of labeled animal videos and use the classification scores to provide rewards for RL training. RLWAV avoids the need for reference trajectories or hand-designed rewards by transferring learned skills from animals to robots. The method is validated both in simulation and on a real quadruped robot (Solo-12), demonstrating the transfer of skills such as walking and jumping.

### Strengths
1. Learning quadruped robot locomotion skills from existing wild animal locomotion is a good inspiration. 
2. The task setup and experimental details are described clearly in the paper.

### Weaknesses
1. The current ablation study of the classifier training set is inadequate, making it hard to determine whether the method effectively utilizes cross-embodiment skills acquired from a diverse range of wild animal videos. The ablation should encompass factors such as the size of the training set and the number of different types of animals included in it.
2. While we anticipate gaining insights into four-legged movement skills from wild animal datasets, the only information we can provide the robot is the output of a classifier. This classifier appears to be able to achieve its task by focusing primarily on the background and the animal's torso, neglecting the movement of the four legs.

### Questions
1. If we do not use the trained classifier as a rewarder, but instead manually assign simple rewards to encourage the quadruped robot to stay still, walk forward, or jump, how effectively can the robot learn these skills?
2. How would the method perform if the output criterion of the classifier is only the movement of the robot's center of mass?

### Soundness
2

### Presentation
4

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
This paper introduces an interesting idea to learn reward function for locomotion through wild animal video. The authors curate a dataset of 8.7 wild animal videos, train a video classifier and then use it as a reward model to train RL policy to control robot for locomotion. The multi-skill policy can be trained in a physical simulator and transfer to real world.

### Strengths
1. The idea is novel.
2. The paper is well written. Easy to follow.
3. Experiments and ablation among its own algorithm shows effectiveness of the proposed method.

### Weaknesses
1. It seems the paper lacks comparison to some baseline or other works. For example, can we compare the results in sim w/ some hand crafted reward models? Then you can compare sample efficiency of the proposed method.
2. Would like to know how large the animal dataset needs to be to make it work. This work uses 8.7K videos. Do we need more or it can work w/ less? Can we add an ablation on it?
3. The paper claims that the reward model can help policy learn well in simulation and then successfully transfer to real. However, to me the "transfer to real" part seems orthogonal to the reward model itself. Could author explain why better reward model can lead to better sim-to-real transfer? For example, if we use a hand crafted reward function in the same setup and learn a policy in sim, can it also transfer to real? My impression is the answer should be yes.

### Questions
The paper claims that the reward model can help policy learn well in simulation and then successfully transfer to real. However, to me the "transfer to real" part seems orthogonal to the reward model itself. Could author explain why better reward model can lead to better sim-to-real transfer? For example, if we use a hand crafted reward function in the same setup and learn a policy in sim, can it also transfer to real? My impression is the answer should be yes.

### Soundness
2

### Presentation
3

### Contribution
3
