# Following the Human Thread in Social Navigation

- Decision: Accept
- Avg Score: 7.33
- Scores: 6, 8, 8

## Abstract
The success of collaboration between humans and robots in shared environments relies on the robot's real-time adaptation to human motion. Specifically, in Social Navigation, the agent should be close enough to assist but ready to back up to let the human move freely, avoiding collisions. Human trajectories emerge as crucial cues in Social Navigation, but they are partially observable from the robot's egocentric view and computationally complex to process.

We propose the first Social Dynamics Adaptation model (SDA) based on the robot's state-action history to infer the social dynamics. We propose a two-stage Reinforcement Learning framework: the first learns to encode the human trajectories into social dynamics and learns a motion policy conditioned on this encoded information, the current status, and the previous action. Here, the trajectories are fully visible, i.e., \ assumed as privileged information. In the second stage, the trained policy operates without direct access to trajectories. Instead, the model infers the social dynamics solely from the history of previous actions and statuses in real-time.
Tested on the novel Habitat 3.0 platform, \modelname sets a novel state of the art (SoA) performance in finding and following humans.

  \keywords{Embodied AI \and Social Navigation \and Human Trajectories}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a new method enabling a robot to search for a human in a simulated indoor environment and then follow them by maintaining a distance of 1 to 2 meters for at least k steps.

The key challenge is that the robot can only see the human via its first-person egocentric camera, resulting in partial knowledge about the environment, as well as the position and velocity of the human.

To address this problem, the authors propose to rely on privileged information, e.g., human GPS data and human trajectories, that are only available during training, not deployment. Then, the authors propose to train the robot policy in 2 phases. In phase 1, the robot does RL (DD-PPO) to jointly learn an encoder that maps privileged information to the latent state and a policy that depends on the robot camera image and the latent state. In phase 2, the robot will run the learned policy while doing supervised learning to learn a decoder to map the robot's camera image to the latent state (the data for the latent state comes from the ground truth privileged information, and the learned encoder from phase 1). Then, during online deployment, the robot will first convert the camera image to the latent state using the decoder from phase 2, and then run the robot policy learned from phase 1.

The result focuses on the Habitat 3.0 simulator. The proposed method is shown to outperform 3 baseline methods. An ablation study was conducted to evaluate the usefulness of each privileged information. Latent analysis shows that the latent state refers to the robot's subtask in find, seek, lost, and follow. The authors also add more realistic components into the simulator to simulate real-world scenarios, such as making the simulated human aware of the robot's presence with reciprocal collision avoidance (ORCA), lowered planning frequency, and increased noise. In such scenarios, the proposed method still outperforms the baseline methods.

### Strengths
- The problem is well-motivated.
- The writing is clear.
- The method is sound.

### Weaknesses
 - As far as I can tell, the training and testing assume the same simulated person. In the real world, this means that to follow one person, the robot has to interact with the user to collect offline data for Phase 1 and online data for Phase 2. This can be very cumbersome. It would be great if the authors could discuss some strategies to scale this method up for different people, such as using meta-learning approaches or using more diverse training data.

- The result shown in Tab.1 shows only marginal improvement over the baseline "Baseline+Proximity Cancelli et al. (2023)". Could the authors provide an discussion about the practical implications of these improvements? Another way to demonstrate its significance is to use statistical test.

### Questions
- Regarding technical novelty, the authors discuss the comparison between the proposed work and the previous work (Cancelli et al., 2023) in Sec.2. It seems that the techniques in both works are similar, but this paper proposes to use a similar structure for the following-human problem, rather than just avoiding collisions with humans as in Cancelli et al., 2023. It would be great if the author could clarify about the difference between these work, or about the extra challenges introduced by following a person rather than just collision avoidance (e.g., perhaps the challenge is more than just changing the reward function of the RL method?).

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces the Social Dynamics Adaptation (SDA) model, a two-stage reinforcement learning approach for enhancing robot social navigation. SDA aims to improve a robot’s ability to navigate alongside humans in dynamic environments, where human trajectories serve as social cues that guide robot movement. In the first stage, the model learns a policy using privileged information about human trajectories, encoding social dynamics into a latent representation. In the second stage, this policy operates without access to these trajectories, relying on inferred social dynamics from the robot’s own state and action history.
Experiments conducted on the Habitat 3.0 platform demonstrate that SDA significantly outperforms state-of-the-art baselines in tracking, following, and maintaining appropriate distances from humans. The study includes analyses of SDA’s effectiveness under noisy conditions, different update rates, and with realistic humanoid behaviors, showcasing its potential for adapting to real-world conditions.

### Strengths
Firstly, the SDA model’s two-stage training framework effectively combines privileged information during training with adaptable inferences during deployment, allowing the model to handle real-world scenarios without needing precise human trajectory data. It outperforms several baselines, showing improved metrics for finding, following, and episode success, which is critical for effective social navigation. Testing on Habitat 3.0, with realistic human motion and environmental noise, strengthens the claim that SDA is robust and adaptable to real-world applications. Comprehensive evaluations, including noise analysis, reduced update frequencies, and alternative metrics, provide a deep understanding of the model’s strengths and weaknesses under various conditions.

### Weaknesses
Despite testing under realistic noise and movement in simulation, SDA’s real-world performance remains untested, raising questions about its transferability from simulated to physical environments. Specifically, the simulation environment, while incorporating noise and varied human motion, may not fully capture the complexities of real-world sensor data, such as unpredictable lighting conditions, reflections, and occlusions, which could significantly impact the performance of the vision-based system. Besides, the model assumes a certain pattern of human movement and interaction, which may limit its effectiveness in scenarios where human behaviors deviate significantly from training data. The model's reliance on a fixed set of human motion patterns during training could lead to a lack of robustness when encountering novel or unexpected human behaviors, such as sudden stops, rapid changes in direction, or interactions involving multiple people moving in complex formations.

### Questions
Are there any plans to test SDA in real-world environments to evaluate how well it transfers from simulation, particularly in handling variable lighting, unexpected obstacles, and diverse human behaviors?
How does SDA perform when humans change speed or direction quickly? Does the reliance on past state-action history allow the model to adapt in real-time, or are there latency issues?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces the Social Dynamics Adaptation model (SDA) to enhance social navigation, where robots must adapt in real-time to human movements. It proposes a two-stage reinforcement learning framework to infer social dynamics from the robot’s state-action history. In the first stage, the model trains using privileged information, like human trajectories, to learn an optimal motion policy. In the second stage, it operates without direct access to human trajectories, instead inferring social dynamics from past actions and statuses. 
The approach was tested on Habitat 3.0 and achieved state-of-the-art results in finding and following humans. The primary contributions include the SDA framework and extensive testing under realistic scenarios, which bridge the gap between privileged training data and real-world conditions.

### Strengths
1. The SDA model cleverly utilizes privileged information (e.g., human trajectories) during training to learn a social navigation policy and then shifts to infer similar dynamics from historical state-action data during deployment. 
2. By modeling human trajectories as latent dynamics, the paper addresses the challenge of partial observability, which is common in robot-centric navigation tasks. The framework effectively models and compensates for missing information, such as losing line of sight of humans, thus proposing to improve the robot's adaptive navigation behavior in dynamic environments.
3. The SDA model is designed to go beyond just avoiding collisions by recognizing and encoding social dynamics, such as keeping an appropriate distance from humans and yielding space when necessary.

### Weaknesses
1. The introduction dives too quickly into explaining the simulator, methodology, and related work without clearly stating the problem or why it is hard and important. It lacks motivating examples to contextualize the problem, making it difficult for readers to grasp the significance until section 3. 
2. The paper models sensor noise and signal drops to simulate real-world conditions, but this is not sufficient to claim robust generalization to real-world scenarios. Real-world environments involve complex interactions, unpredictability, and physical constraints that are difficult to replicate in simulation, even with added noise. Specifically, the simulation does not account for variations in lighting, surface textures, and other environmental factors that can significantly impact sensor readings and robot performance.
3. Although the authors test their model extensively in Habitat 3.0, the paper lacks real-world experiments. Simulation platforms, while powerful, cannot fully capture the complexity and unpredictability of real-world environments. Additionally, real-world computational constraints (e.g., processing speed and memory) were not sufficiently addressed. The paper does not provide any analysis of the model's performance with respect to computational resources, which is a critical factor for real-world deployment.
4. The paper does not sufficiently explore how variability in human behavior, such as different walking speeds, erratic movements, or group interactions, affects the model’s performance. The experiments seem to focus on relatively uniform human motion patterns, which do not reflect the diversity of human behavior in real-world scenarios. The model’s ability to adapt to sudden changes in human direction or speed is not thoroughly evaluated.
5. The SDA model focuses primarily on following a single human in simplified indoor environments, without considering more complex scenarios like navigating among multiple humans or handling other social situations. The model's performance in crowded environments or when interacting with multiple people simultaneously is not explored, which limits the applicability of the proposed approach to more realistic social navigation tasks.
6. Figure 4 claims that the behavior clusters are well-separated, but they appear mostly overlapping. The visualization does not clearly demonstrate the distinctiveness of the learned behavioral clusters, raising questions about the effectiveness of the latent space representation.
7. Figure 2 should explicitly define that stage 1 is offline and stage 2 is online. The lack of explicit labeling for the training and deployment stages can lead to confusion about the model's operational mode.
8. The paper’s overall presentation could use some work. Many sections of the paper have different writing styles, making the writing really inconsistent, detracting from the message of the paper.

### Questions
1. Could you clarify why the problem being solved in this work is hard and important in the introduction? Providing motivating examples early on would help the reader grasp the significance before diving into the methodology, related work or implementation details. Could you revise the introduction to include this context more explicitly?
2. While the paper models sensor noise and signal drops, this may not be enough to claim robust generalization to real-world environments. Could you explain how the model would handle the complexities of real-world social interactions, and consider testing beyond simulated noise scenarios?
3. The paper does not explore how the model adapts to varying human behavior, such as erratic movements. Have you considered testing with more diverse or unpredictable human behaviors? How do you think the model would perform under such circumstances?
4. Given the focus on simulation, could you discuss how the model could be deployed in real-world environments? What are the anticipated challenges of transferring the SDA model to physical robots, and have you considered Sim2Real experiments or alternative testing methods?
5. Could you provide more details on the computational overhead of the two-stage model, particularly during deployment? How do you anticipate the system performing on resource-constrained robots in real-time scenarios, when only stage 2 is run?
6. The current focus is on following a single human in relatively simple environments. Have you considered expanding the model to more complex social settings, such as multi-human interactions?
7. In Figure 4, the text suggests that the behavior clusters are well-separated, but visually, they appear to be overlapping. Could you clarify this discrepancy and perhaps provide a better explanation or adjust the visualization to reflect the claim more accurately?

### Soundness
3

### Presentation
2

### Contribution
3
