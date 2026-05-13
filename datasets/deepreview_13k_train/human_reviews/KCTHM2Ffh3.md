# Runtime Learning Machine

- Decision: Reject
- Scores: 6, 5, 8

## Abstract
This paper proposes the **Runtime Learning Machine** for safety-critical autonomous systems. The learning machine has three interactive components: a high-performance (HP)-Student, a high-assurance (HA)-Teacher, and a Coordinator. The HP-Student is a high-performance but not fully verified Phy-DRL (physics-regulated deep reinforcement learning) agent that performs safe runtime learning in **real** plants, using **real**-time sensor data from **real**-time physical environments. On the other hand, HA-Teacher is a verified but simplified design, focusing on safety-critical functions. As a complementary, HA-Teacher's novelty lies in real-time patch for two missions: i) correcting unsafe learning of HP-Student, and ii) backing up safety. The Coordinator manages the interaction between HP-Student and HA-Teacher. Powered by the three interactive components, the runtime learning machine notably features i) assuring lifetime safety (i.e., safety guarantee in any runtime learning stage), ii) tolerating unknown unknowns, iii) addressing Sim2Real gap, and iv) automatic hierarchy learning (i.e., safety-first learning, and then high-performance learning). Experiments involving a cart-pole system, two quadruped robots, and a 2D quadrotor, as well as comparisons with state-of-the-art safe DRL, fault-tolerant DRL, and approaches for addressing Sim2Real gap, demonstrate the machine's effectiveness and unique features.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a "Runtime Learning Machine" designed for autonomous systems operating in safety-critical environments. The machine combines three main components: an HP-Student (high-performance learner), an HA-Teacher (high-assurance safety monitor), and a Coordinator. The HP-Student learns in real-time from physical environments, with the HA-Teacher correcting unsafe actions and enforcing safety. This design aims to address critical challenges in deep reinforcement learning, including tolerating unknown unknowns and bridging the Sim2Real gap.

### Strengths
The paper presents an innovative hierarchical safety mechanism where the HA-Teacher manages safety while the HP-Student prioritizes performance optimization within safety constraints. This interactive approach is practical and well-suited to the paper’s focus on real-world, safety-critical applications. The experimental setup, involving both a cart-pole system and a quadruped robot, is comprehensive and shows the method’s robustness across different unknowns. The results suggest that the system can maintain stability through real-time patching by the HA-Teacher, showing practical value in environments where safety and performance trade-offs are essential. Additionally, the framework addresses the Sim2Real gap, which remains a significant challenge in deploying DRL systems in physical settings.

### Weaknesses
The design details for the teacher, a core element of this framework, could be expanded, particularly in scenarios where unknowns extend beyond simple disturbances to include hardware or sensor faults. Additionally, the theoretical justification for the teacher’s resilience against unknown unknowns could be strengthened, as the current analysis lacks formal rigor or quantitative measures. While the selected experimental domains are relevant, further discussion on generalizability to applications like autonomous driving or complex industrial robots would broaden the framework’s impact. Although comparisons with other DRL methods are made, the analysis could be enhanced by discussing specific scenarios where other methods may outperform this framework or identifying potential limitations.

### Questions
Could you provide more insights into the teacher's handling of complex unknowns, such as hardware failures or significant sensor errors?

What theoretical guarantees exist for the teacher's performance in completely unanticipated scenarios?

How might this system perform in applications outside of the tested environments, such as in higher dimensional or more complex environments?

### Soundness
3

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
3

### Summary
The paper presents a novel approach to runtime learning for agents, guided by a verified teacher during runtime to ensure safe operation. This teacher-student framework leverages physics-regulated deep reinforcement learning (PhyRL) and aims to address safety concerns arising from unknown variables and Sim2Real gaps. The validation of the approach is conducted on two benchmarks, including a real quadruped robot, which adds to the practical value of this research.

### Strengths
1. The paper addresses a important safety issue in learning-based systems, particularly focusing on challenges like unknown unknowns and Sim2Real gap.
2. The paper presents solid theorem.
3. The evalution is performed on a real robot, which exhibits the practicality of this work.

### Weaknesses
Though the results look impressive, I found some parts of the paper needs further clarification and a few more discussion about related works are expected.
1. The paper lacks details on the verifiability of the PhyRL structure, especially regarding how the teacher's safety is guaranteed in unknown environments. In Equation 2, the system safety is only related to its state. Does this mean that this paper assumes such simple constraint and not consider how the environment change impacts on the states?
2. The paper should discuss whether switching back to the teacher affects operational performance, as such switches may potentially degrade it. Additionally, the evaluation would benefit from presenting metrics on how frequently the teacher’s guidance is triggered.
3. The work currently assumes a single-step safety model, where each action ensures safety only for the immediate next state. However, a broader perspective on end-to-end safety—considering the effects over several steps or even entire trajectories—is the cases that usually happen in reality.
4. There are lots of verified learning works that are not cited/discussed by this paper.  For example, Neurosymbolic reinforcement learning with formally verified exploration. Neurips 2020.
5. There are only two benchmarks presented. Though one of them is the real robot, it would be necessary to evaluate on a more diverse set of benchmarks.

### Questions
1. How often does the teacher’s intervention occur during runtime, and is there an impact on the agent's performance with frequent switches?
2. If the teacher is adjusted or modified during runtime, how is its performance or reliability guaranteed in changing conditions?

### Soundness
3

### Presentation
2

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
This paper introduces a runtime learning machine for safety-critical autonomous systems, featuring an interactive HP-Student, HA-Teacher, and Coordinator. It ensures lifetime safety by addressing unknowns and the Sim2Real gap, enabling real-time learning for safe, high-performance policies. Experimental results validate its effectiveness on cart-pole and quadruped robot systems.

### Strengths
- The proposed method combines a High Assurance Teacher with a Performance optimizing student to yield strong real word robustness results on a challenging quadruped robot.
- The experiments show scalable computation that can work fast enough for real-time learning using matrix toolboxes and related libraries.

### Weaknesses
 - The setting considered assumes knowledge of the environment dynamics by the HA-Teacher. System identification is proposed but does not appear to have been experimented with.
- The presentation is cluttered at times and causes some difficulty in parsing. For example, some of the numerous assumptions, remarks, characteristics, and definitions should be consolidated if possible. Section 1.3 is almost entirely italicized.

### Questions
1. How is this approach placed in the context of other shielding approaches [1,2]?
2. The triggering condition in Eq 7 is entirely causal (i.e., depends only on the current time and prior to the current time). Why is this better than using the environment model to predict for a future failure from the current state and input?
3. How does the approach generalize to different safety sets (e.g., velocity < 1.5 vs velocity < 3)? Will the entire training process be needed for each change? How long would the training time be for each minor change?
4. Are there any experiments or examples with System Identification as mentioned in Remark 6.5 or Appendix C?

### References:
[1] Safe Reinforcement Learning with Nonlinear Dynamics via Model Predictive Shielding, Bastani, ACC 2020

[2] Dynamic Model Predictive Shielding for Provably Safe Reinforcement Learning, Banerjee et al, arXiv 2024

### Soundness
3

### Presentation
2

### Contribution
3
