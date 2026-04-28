# Soft Robot Assisted Human Normative Walking: Real Device Control via Reinforcement Learning Without a Simulator

- Decision: Reject
- Avg Score: 6.25
- Scores: 6, 5, 8, 6

## Abstract
This study offers an innovative solution approach to soft robot-assisted human walking. The controller design of the  soft robotic exosuit aims at assisting human normative walking with reduced human physical effort. Achieving such optimal interaction between the human and robot agents presents a key challenge to the robot control design due to a lack of robust model of the soft inflatable exosuit and its interaction dynamics with the human user.  Moreover, to maximize user comfort, the robot assistance  should be personalized to individual users. Toward this goal, we propose an offline to online based approach that is referred to as AIP, which stands for online Adaptation from an offline Imitating expert Policy. Our offline learning mimics human expert actions through real human walking demonstrations without robot assistance. The resulted policy is then used to initialize online reinforcement learning, the goal of which is to optimally personalize robot assistance. In addition to being fast and robust, our online actor-critic learning method also posseses important properties such as learning convergence, system stability, and solution optimality. We have successfully demonstrated our simple and robust solution framework for safe robot control on all four tested human participants.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors present online Adaptation from an offline Imitating expert Policy (AIP) algorithm to learn a personalized and generalizable exoskeleton controller for human subjects. The knee-assist exoskeleton-suit helps reduce the effort required by the human user. The key to their approach is to first learn an offline behavior cloned policy which acts as a good starting point for online adaptation. To boost learning performance, the paper also introduces RIIV which reduces intra and inter-person variations thus improving data quality.

### Strengths
The paper is written with sufficient details. The results presented are interesting and does justify the approach as a practical solution to robot assisted locomotion. Successfully getting online reinforcement learning to work on safety-critical human-robot interaction task is commendable.

### Weaknesses
Including a supplementary video would be extremely useful for the reader to evaluate the qualitative performance of the policy. For example, noticing how gait looked like with the exoskeleton active. (I understand the privacy concerns with human subjects involved, perhaps blurring out the users could be an option?)
Adding a section on the limitations of the proposed approach would be valuable.

In section 3.5 - the following statement " Unlike traditional RL formulations that aim to
maximize the expected reward, in wearable robotics, the objective is to minimize the overall cost
over policy π" is not very clear, how are these two different. One can also reformulate a cost function to be a reward function. On a related note, the algorithm used for online adaptation direct heuristic dynamic
programming (dHDP) is not one of the more popular online RL algorithms, was any other approaches like PPO, SAC etc.. considered? If so, what are the pros and cons?

### Questions
1) If I understand correctly, the policy only controls the onset timing and duration and not the actual air pressure of the robot. Does the air pressure used in the exoskeleton vary with different users? 
2) Related to the above question, the authors mention that data from only one person was used for collecting data for the offline imitation learning phase of the algorithm. Which among the 4 users contributed to this data? or was there a different person? if so, what were the anthropometric data look like? 
3) In section 3.5 - the following statement " Unlike traditional RL formulations that aim to
maximize the expected reward, in wearable robotics, the objective is to minimize the overall cost
over policy π" is not very clear, how are these two different. One can also reformulate a cost function to be a reward function. On a related note, the algorithm used for online adaptation direct heuristic dynamic
programming (dHDP) is not one of the more popular online RL algorithms, was any other approaches like PPO, SAC etc.. considered? If so, what are the pros and cons?

### Soundness
2

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
This paper introduces a method for controlling a soft robotic exosuit to assist human walking.  The key idea is to use reinforcement learning to directly learn a control policy from real-world interactions between the human and the exosuit.  This is achieved through an offline-to-online approach called Adaptation from an offline Imitating expert Policy. In the offline phase, the robot learns to imitate human walking patterns from expert demonstrations.  This provides an initial policy for the online phase, where the robot personalizes the assistance by fine-tuning the controller through direct interaction with the user.  The method is evaluated with four participants, showing that it can effectively reduce muscle effort during walking while maintaining a normal gait.

### Strengths
1. The paper addresses the challenging problem of controlling soft exosuits for human assistance, which involves complex dynamics and human-robot interaction.
2. The method is designed to work directly in the real physical environment, without relying on a simulator, which is often difficult to construct accurately for soft robots and human-robot interaction. This makes the approach more practical and potentially more effective than sim-to-real methods.

### Weaknesses
1. The method used in this paper is naive BC and policy gradient, however, there are other related offline to online frameworks such as [1], and the authors are encouraged to perform experiments with other methods. Specifically, the paper lacks a comparison to more advanced offline-to-online RL algorithms that might offer improved sample efficiency or performance. The current approach uses basic behavioral cloning for the offline phase and a policy gradient method for online adaptation, which may not be optimal. For example, methods that incorporate uncertainty estimation or more sophisticated exploration strategies could potentially lead to better results in the online phase. 
2. The experiments are conducted with a small number of participants. It is unclear how well the method would generalize to a larger and more diverse population, including people with different walking patterns, or physical impairments. The limited number of participants makes it difficult to assess the robustness of the method across different gait patterns and individual variations. Furthermore, the paper does not address how the method would perform with individuals who have mobility impairments or other conditions that might affect their walking patterns. 
3. Missing of hardware details. The paper provides insufficient details about the hardware used in the experiments, making it difficult to reproduce the results. Specific information about the sensors, actuators, and control system is needed to fully understand the experimental setup. 
4. Missing comparison with previous methods in exosuits, does reinforcement learning really help? The paper lacks a thorough comparison to existing control methods for exosuits, making it difficult to assess the contribution of the proposed reinforcement learning approach. It is unclear whether the observed performance improvements are due to the reinforcement learning component or other factors. A comparison with traditional control methods or other machine learning-based approaches would provide a better understanding of the benefits of using reinforcement learning in this context. 
5. This article is more suitable for the robot conference or journal since it focuses on field robots rather than general methods.

### Questions
See weakness.

### Soundness
2

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
This paper tackles the key problem of how to make the robot work effectively with humans without having a computer simulation to test things first - a significant challenge since most robotics work relies heavily on simulation before real-world testing.  The paper presents a systematic investigation of the problem and shows that their method can successfully train soft robots to aid walking without relying on simulation, opening new possibilities for human-robot interaction in assistive devices.

The authors propose a two-step approach they call AIP (Adaptation from Imitating expert Policy). First, they learn from normal human walking patterns without the robot's assistance. Then, they use this as a starting point for real-time learning where the robot adapts to each individual person's walking style. Their method focuses on improving data quality through a technique called RIIV (Reducing Intra-person and Inter-person Variation) and ensures safety through careful constraint design. The researchers validate their approach with both theoretical analysis and practical experiments on four subjects, demonstrating reduction in muscle effort while maintaining natural walking patterns.

----
*Post Rebuttal*: Updated the Score.

### Strengths
- The paper presents a clear, well-structured methodology for direct learning on physical devices, with precise problem formulation and experimental validation.
    
- The data-driven approach (AIP) is simple yet effective, demonstrating successful learning without simulation through a combination of offline imitation and online adaptation.
    
- Strong empirical results with clear metrics (20% EMG reduction) and thorough ablation studies validating design choices.

### Weaknesses
 - The investigation lacks analysis of system degradation effects (e.g., soft actuator wear and tear) on the learned timing shifts discussed in Q3. This raises questions about long-term reliability. Specifically, the paper does not explore how the performance of the soft actuators degrades over time with repeated use, and how this degradation might affect the learned timing parameters. For instance, the stiffness of the actuators might change, or the response time might increase, which could lead to a mismatch between the learned policy and the actual system behavior. This is crucial for real-world deployment, where such degradation is inevitable.
    
- The paper would benefit from a baseline comparison showing human adaptation alone without robot learning, to isolate the benefits of the co-adaptation process. The current results do not clearly show how much of the improvement is due to the robot learning, and how much is due to the human adapting to the robot. A control experiment where the robot provides a fixed assistance profile, without any learning, would help to isolate the benefits of the proposed co-adaptation approach. This would allow to quantify the human learning effect in isolation.
    
- Limited discussion on the generalizability of the approach - specifically, which components are specific to soft exosuits (like RIIV data processing) versus which are generally applicable to human-robot learning systems. The paper does not clearly delineate which parts of the proposed method are specific to the soft exosuit and which are generalizable to other human-robot interaction scenarios. For example, the RIIV data processing technique might be highly specific to the type of sensor data and the biomechanics of the soft exosuit, and may not be directly applicable to other robotic systems. A more detailed discussion of the assumptions and limitations of each component would be beneficial.
    
- While the paper demonstrates successful learning without simulation, it doesn't fully address whether this approach eliminates the need for simulation in this domain. Have we achieved oracle performance? A discussion of the domain specific need of simulation and tradeoff to direct learning approaches would strengthen the contribution. The paper does not discuss the limitations of the direct learning approach and the potential benefits of using simulation for this domain. It is not clear if the proposed method achieves optimal performance, and how it compares to a hypothetical scenario where a perfect simulation model is available. A discussion of the trade-offs between the direct learning approach and a simulation-based approach would be valuable.

### Questions
NA

### Soundness
3

### Presentation
3

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
This paper presents a system to learn controllers for robot-assisted human walking. Offline learning is used from human walking data, and online adaptation is used to further fine-tune the controller. The proposed system is demonstrated to generate controllers for a soft robotics exosuit that can help reduce human walking effort.

### Strengths
A system that can generate controllers that reduce human walking effort using a soft exosuit. This can impact the wider adoption of machine learning techniques on such systems.

A comprehensive analysis of the online adaption controller that shows significant improvement and personalized adaption.

### Weaknesses
There is no video of the results.

There is a lack of comparison to existing work. What is the state of the art in the literature regarding effort reduction with an exoskeleton, either using the same robot or other exoskeletons?

There is not much innovation in terms of methodology. Are there any limitations of the current methods? What is preventing this from scaling up as mentioned in future work? Is it just simply putting more time into doing experiments?

### Questions
How necessary is the initial offline phase? Can the system work by just using the online adaptation phase with some reasonable initial guess of the policy?

What is the theoretical maximum effort reduction of the assisted walk can achieve? Is the proposed method getting close to that?

### Soundness
3

### Presentation
3

### Contribution
3
