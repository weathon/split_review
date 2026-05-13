# Addressing Real-Time  Fragmentary Interaction Control Problems via Muti-step Representation Reinforcement Learning

- Decision: Reject
- Scores: 6, 6, 5, 5

## Abstract
Fragmentary interaction control problem is common in real-time control scenarios. For example, the delay or the loss of the network packets (caused by network obstacles, inadequate bandwidth, or switch faults) will lead to dynamic interval or fragmentary interaction. Moreover, fragmentary interaction hinders the application of reinforcement learning algorithms in real-time control tasks: when the states are not received, the reinforcement learning (RL) algorithm cannot make the decision for the agent according to the traditional MDP, which leads to the standstill of the agent, and finally leads to low efficiency or even failure in completing the task. However, such problems are not well studied in the RL community. In this paper, we propose to simultaneously generate multiple actions for future states in case some future states cannot be perceived. We present \textbf{M}ulti-step \textbf{A}ction \textbf{R}epre\textbf{S}entation (\textbf{MARS}) to learn a compact and decodable latent space for the original multi-step action space. Besides, our method enhances the environmental dynamic semantics of the action representation through unsupervised environmental dynamics prediction and action transition scale. Based on MARS, the RL algorithms optimize policies in the learned representation space and interact with the environment by decoding the latent actions to the original ones. MARS outperforms the existing state-of-the-art baselines in a variety of fragmentary interaction real-time control tasks. Further, MARS significantly improves the performance of high-frequency robot control tasks based on fragmentary interaction in the real-world.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work primarily focuses on real-time reinforcement learning for high-frequency robot control tasks, where the information transmission is not entirely reliable. The communication between the action executor and agent in reinforcement learning may be affected by packet loss and latency, potentially impacting the effectiveness of policy execution. In contrast to previous methods that directly generate multi-step action sequences, this paper proposes using sc-VAE to generate an intermediate representation in place of an action sequence. During actual execution, this intermediate representation is used to generate the corresponding action sequence. The paper introduces additional regularization for the influence of actions on the environment within the generated intermediate representation.

The proposed method's performance is tested in various Mujoco task environments and a real-world snake robot control task. The results indicate that MARS outperforms the advanced decision method that directly generates action sequences and a simple frame-skip method which makes decisions with lower frequency. Further ablation studies confirm that the proposed method can consider the influence of the environment when generating intermediate representations.

### Strengths
The strengths of this work are as follows:

1. The paper provides a detailed introduction to the background of the real-time RL problem, and the research objectives are clear.

2. The proposed method in the paper exhibits excellent generability and can work with various reinforcement learning optimization algorithms.

3. The paper offers experimental results on real robots, demonstrating the practicality of the proposed method.

### Weaknesses
The weaknesses of this work are as follows:

1. The soundness of the paper is limited. The method is based on sc-VAE, and the primary claim that "the action sequences decoded by the close points in the latent space should have a similar     influence on the environment" relies on empirical evidence and lacks theoretical explanation (refer to question 1). Specifically, the paper does not provide a rigorous justification for why clustering latent representations based on environmental impact is superior to clustering based on other metrics such as value or reward. The assumption that similar environmental changes imply similar rewards or values is not always valid, especially in complex or sparse reward environments. The paper needs a more formal analysis of the relationship between latent space proximity and the consistency of environmental effects, and how this relates to policy learning.

2. The paper lacks explanations for some critical aspects of the experiments. For more details, please refer to question 2. For instance, the paper mentions random FIMDP tasks but does not specify whether the number of decision steps is fixed or variable within a trial. This is crucial because it directly impacts the effective horizon of the policy and the difficulty of the learning problem. Furthermore, the paper does not provide sufficient details on how the action sequences are handled when the execution interval is shorter than the sequence length, which is a critical aspect of real-time control. The lack of clarity on these experimental details makes it difficult to assess the validity and generalizability of the results.

### Questions
1. Why is clustering representations of actions that have similar environmental effects better than clustering action sequences with similar values or rewards? Can you provide a more in-depth explanation and analysis?

2. In the random FIMDP tasks mentioned in the paper, is the number of decision steps fixed within one trial or randomly decided during execution? As shown in Figure 11, a larger interval leads to lower performance, how will the method perform if trained with longer action sequences but executed with a shorter interval, compared with training with shorter action sequences?

3. The paper mentions that MARS has better stationarity, but it doesn't provide relevant explanations and proofs. Additionally, in a real-time RL setting, where it's not guaranteed that the actions actually executed by the executor strictly match the policy's output, do the collected trajectory samples inherently lack stationarity? (you can regard the trajectory as being sampled from a rapidly changing environment transition probability)

4. I noticed some interesting results. Why does it appear that MARS has a more pronounced advantage over frame-skips in simpler tasks than in more complex tasks?

5. The application form of the method needs further clarification. Does the decoder need to be run on the execution device? If so, does this mean that latent representations will also be lost?

6. Should the "Musar" method in Fig.5 and 6 be referred to as "MARS"?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposed a representation learning method for reinforcement learning to handle real-time fragmentary interaction control problems. The authors proposed a novel problem formulation in the MDP, where the interaction between agents and environments might be fragmentary.The agents need to make multi-step decisions on potentially insufficient observation to handle the frame skip and package loss. The authors proposed a VAE-based approach to learn the multi-step latent representation and use the representation with RL to handle the fragmentary interaction problem. Empirical results have shown the effectiveness compared to intuition-based baselines.

### Strengths
1. The problem formulation is novel and significant. Fragmentary interaction is indeed an important problem in real-world high-frequency control problems.
2. The presentation is excellent, the problem formulation is clear and multiple figures help clarify the problems.
3. The proposed algorithm is solid and performs well empirically.

### Weaknesses
1. The authors might need to connect more with existing problem formulations. The FIMDP looks related to partially observable MDPs and MDP with reward delays. I can get a rough sense that there are differences between FIMDP and these existing problem formulations, but not very clear. The authors should add a clear discussion to distinguish FIMDP from the existing related problem formulations.



### Questions
1. The questions are also related to weakness, what are the differences between FIMDP and POMDP, or MDP with reward delays?
2. If we have/learned a world model for the environment, can we do the model-based predictions, like model predictive control to solve the FIMDP? (this might be the most straightforward method that first came into my mind.) How does this compare to learning the multi-step representations?

It is a good paper. I will consider improving my score if the questions are appropriately addressed.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a method for solving real-time control tasks where the delay or the loss of the network packets may lead to fragmentary interaction. Specifically, this could happen when the remote controller fails to receive the observation on time and thus can not issue a new command to the robot. Without receiving correct commands at the correct timestep, the robot may standstill by doing nothing or repeating the last action. Both may induce a failure in task completion.

To address this, the paper proposes to generate an action sequence instead of a single action step when making decisions. Thus when the remote controller can not produce the new action sequence due to failing to receive the new observation, the robot can still realize what to do according to the remaining commands in the action sequence received last time. This is a bit like how traditional planning algorithms such as MPC work.

To achieve this, a modified VAE is trained to construct a latent action space, which serves as the action space for RL methods like TD3. Every time the actor-network chooses an action from the latent action space, the latent variable will be converted to a robot command sequence through the decoder. 

In the experiments, several Mujoco environments are constructed to simulate the fragment interaction situation. The results show that the proposed method can overcome this problem and compete with the agents trained and deployed in an ideal environment. Besides, a robot snake experiments are conducted to show it can be applied to real robots.

### Strengths
1. Investigating how to build a system robust to fragmentary interaction or latency is important in the robotics system.
2. The paper is easy to understand.
3. The Mujoco experiments show that the method works well and is comparable to baselines in an ideal environment. The ablation study shows the importance of different modules

### Weaknesses
The main weakness of this paper is the poor robot evaluations. As the main motivation of the method is to address a practical issue in the real-world robot learning environment, a comprehensive real-world evaluation should be conducted on a platform where the fragmentary interaction problem indeed exists and is critical to the robot's performance.

The paper only contains a short section about the snake robot experiment with simple proprioceptive observations. In this setting, the delay or the loss of the network packets rarely happens as the bandwidth should be enough for transmitting the small amount of data consisting of only 54-dimensional vectors without any high-dimensional images and lidar results. Also, if the snake fails to receive any commands, simply stopping by doing nothing and waiting for the new commands is acceptable. It is not like a legged robot, which may easily fall down if it can not receive a stable command stream.

In a word, my main concern is that it is not verified on robot platforms that indeed suffer from this problem like quadrupedal robots with multi-modal perception. Otherwise, I cannot believe the proposed method can solve the claimed problem.

### Questions
As a robotics-related submission, it is usually good to include demo videos. Sometimes, it is even more important than the paper itself. Could you please share more visualization results of the snake experiment?

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
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a method for real-time control scenarios in which interation between the execution devices and the computation node is lossy. The question here is what actions should be taken by the execution devices when the latest inference result has not arrive yet. The algorithm involves planning a sequence of future actions instead of a single action and learning a latent representation for lists of future actions in an unsupervised manner. Then an RL policy is trained to solve the task with the action space being the latent representation. Experimental results illustrate the effectiveness of using latent representations as action spaces in both simulation environments and the real world.

### Strengths
1. The paper is well-written and easy to follow.
2. The motivation is clear and the method is clean.

### Weaknesses
1. The experiemnt part may not fully match with the motivation of the paper. Generally speaking, simulation environments such as Mujoco do not require the use of framentary control. The paper does not adequately justify the use of Mujoco for evaluating methods designed for lossy communication scenarios. The simulation environments lack the characteristics of real-world systems with intermittent communication, such as variable latency and packet loss. The experiments should include a more detailed analysis of the impact of different communication patterns on the performance of the proposed method.
2. The real-world robotic control experiment lack important details, including the interaction pattern between the executor and the agent in the real-world experiment. The description of the robotic platform is insufficient, and the specific control loop details are missing. The paper should include details about the sensor suite, the actuation system, and the communication protocol used in the real-world experiment. Furthermore, the paper lacks a discussion of the challenges encountered in the real-world experiment, such as noise, delays, and model inaccuracies.

### Questions
1. Why does the method significantly outperform TD3 with advanced decision? Please explain the comparison between the baselines in more details.
2. What is the interaction pattern between the executor and the agent in the real-world experiment?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
