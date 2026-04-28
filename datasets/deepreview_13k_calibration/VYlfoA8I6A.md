# Talking Vehicles: Cooperative Driving via Natural Language

- Decision: Reject
- Avg Score: 3.75
- Scores: 6, 3, 3, 3

## Abstract
Using natural language as a vehicle-to-vehicle (V2V) communication protocol offers the potential for autonomous vehicles to drive cooperatively not only with each other but also with human drivers. Simple and effective messages for sharing critical observations or negotiating plans to achieve coordination could improve traffic safety and efficiency compared to methods without communication. In this work, we propose a suite of traffic tasks in vehicle-to-vehicle autonomous driving where vehicles in a traffic scenario need to communicate in natural language to facilitate coordination in order to avoid an imminent collision and/or support efficient traffic flow, which we model as a general-sum partially observable stochastic game. To this end, this paper introduces a novel method, LLM+Debrief, to learn a message generation and control policy for autonomous vehicles through multi-agent discussion. To evaluate our method, we developed a gym-like simulation environment that contains a range of accident-prone driving scenarios that could be alleviated by communication. Our experimental results demonstrate that our method is more effective at generating meaningful and human-understandable natural language messages to facilitate cooperation and coordination than untrained LLMs. Our anonymous code is available in supplementary materials.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors propose a method LLM+Debrief policy that deals with multi-agent interactions tailored to traffic environments. Each agent is a vehicle with a goal and communicates in natural language. This goal, along with environmental observations and previous knowledge, outputs a message to neighbors and an action. The episodes progress as each agent outputs messages and actions at every step. At the end of the episode, agents receive a summary of their performance from the environment. The agents are then involved in a debriefing session where they share reasoning and discuss strategies that provide feedback on the LLM policy. 

The method is evaluated in a CARLA simulator with multiple baselines, including a non-language baseline with and without communication. Results are presented for various levels of communication via reflection and debriefing.

### Strengths
The study provides an interesting approach to enable autonomous vehicles to interact with each other in various driving scenarios. The authors have developed a versatile TalkingVehiclesGym that uses natural language and incorporates partial observability. The framework can serve as a tool for natural language-based cooperative driving scenarios.

The work demonstrates the benefits of leveraging knowledge gained so far along with communication to improve cooperation over silent methods.

The introduction of post-episode debriefing sessions is a significant addition.

The method is tested in the CARLA simulator with a comprehensive set of baselines, including scenarios both with and without communication. The methodology is explained well. The figures aid in the understanding of the paper.

### Weaknesses
The paper is generally well-written and organized; however, there are areas where clarity could be improved. More explanation is needed on how the reward structure is utilized. 

The results could also include more evaluation details in a tabular form. For example, these could include the time to evaluate and the real-time equivalent processing time to show how this method could work in a real-world setting. Specifically, the paper lacks a breakdown of the computational cost associated with each component of the LLM+Debrief method, such as the time for message generation, reasoning, and decision-making. This makes it difficult to assess the practicality of the approach for real-time applications.

Providing more implementation details could also explain the choice of the number of episodes per scenario, which seems to be low. Could the authors justify their choice of episode number or explain how they determined this was sufficient for their experiments?

### Questions
A) Some of the supplementary materials have detailed the simulation times/elapsed times. Are these representative of a similar real-world implementation? Could the authors provide a table with columns for each method, showing evaluation time and real-time equivalent processing time for each scenario tested? Additionally, metrics could include message generation time and decision-making latency.

B) Can this LLM+Debrief include the Coopernaut method? Since this provides a relatively better performance, it would be interesting to see if combining the two would improve LLM+Debrief.

Minor comments:
1. Page 6: In line 305, “pushlish” → publish?
2. Page 6, lines 315-318 have a repeated sentence.

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
The paper proposes the use of natural language for communication between vehicles as a way to improve autonomous driving. The paper focuses on specific driving tasks (overtake, red light, left turn, highway exit, highway merge) and presents a new method, called LLM+Debrief, to learn how to generate messages to other vehicles and generate related control policies. The experimental results included have been obtained in a gym-like simulation environment built on the CARLA urban driving simulator. The experiments address in-episode communication, chain-of-thought reasoning, and post-episode debriefing. The results show that communication facilitate cooperation and that reflection and debriefing improve the performance when the vehicles negotiate with each other. The problems are modeled as "a multi-agent partially observable and general-sum game".  Each vehicle is assumed to be cooperative. The objective of each vehicle is to optimize the time to reach its destination. The main novelty is to provide autonomous vehicles with the ability to interact with each other in natural language, which facilitates the interactions with other vehicles.

### Strengths
The idea proposed is interesting and innovative. It seems premature, but it opens a new direction of work. The paper has value as a basic feasibility study.

The paper provides positive experimental results, which have been obtained in simulation, on the value of having vehicles communicate and negotiate with each other.

The writing is clear and the structure of the paper is well organized.

### Weaknesses
A question that comes to mind is why using natural language for vehicles to communicate is better that using an artificial communication language. The paper says that natural language could also allow human drivers to participate in the conversation, but it might also distract the drivers.

Each vehicle generates observation messages and decides driving plans in collaboration with the other vehicles. From the examples shown in the figures, there could be a lot of messages, sometimes too many.  The figures shown do not have many vehicles, at most 3 or 4, but there could be many more, for example in city traffic on streets with multiple lanes.

In addition to deciding what to do, each vehicle has to generate its control policy.  An issue is the time needed to share messages and what happens if there is message congestion. In the simulation experiences are collected every 0.5 seconds and kept for 2 seconds.  There is no information on what would the timing should be in real vehicles. Also no information is given about the time needed to generate the control policy.  In the simulation, are the steps for all the vehicles synchronized with the same discrete time steps?

The information sensed by the vehicle is translated into text, since it has to be used in the conversation. No indication is given about the time this will take.

The assumption of truthful information and collaborative attitude of all the vehicles is very strong and might not correspond to reality.

Minor issue: the paper says that each vehicle can express its individual preference for its objective, but does not show any examples.  All preferences are assumed to be the same. i.e., optimize the time to reach its destination.

### Questions
Please clarify some of the points listed as weaknesses, for example by providing some information on the temporal issues.  The system will have to work in real-time. 

Please also address the potential for message congestion when there are many vehicles in close proximity.

Finally, please address the issue of how to recognize untruthful information or address aggressive driving.

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
4

### Summary
This paper presents a suite of traffic coordination tasks for autonomous driving, formulated as situational communication within vehicle-to-vehicle settings. The objective is to use natural language to facilitate coordination, helping vehicles avoid imminent collisions and maintain efficient traffic flow. Authors introduced an LLM agent framework called LLM+Debrief, and developed a gym-like simulation environment featuring a range of accident-prone driving scenarios.

### Strengths
### New Angle on Vehicle-to-Vehicle Communication. 

Unlike much of the existing work that emphasizes human-vehicle communication or latent (implicit) vehicle-vehicle signaling, this paper introduces a unique angle by explicitly utilizing natural language for vehicle-to-vehicle communication. This approach advances the field by demonstrating how explicit messaging can facilitate coordination and improve safety in multi-agent driving scenarios.

### Effective LLM+Debrief Framework
The proposed LLM+Debrief framework, trained over 30 episodes and evaluated on an additional 30. This episodic structure enhances the learning process and shows promise in learning teaming strategies among autonomous LLM agents.

### Contribution of a Gym-Like Simulation Environment
The development of a gym-like simulation environment focused on accident-prone driving scenarios represents a significant contribution to the field. If made publicly available, this environment could serve as a valuable resource for testing and advancing V2V communication protocols in autonomous driving research.

### Weaknesses
### Weakness 1: The motivation.
The motivation behind this work requires clearer and more robust justification. It appears that the approach is closely related to multi-agent reinforcement learning, where, in many cases, approaching a multi-agent system often involves adopting a central agent baseline. This central agent would process all incoming information and operate within an action space equivalent to the joint action space of the individual agents. 

Explicit natural language communication could be helpful in human-vehicle settings (we cannot centralize humans in the multiagent system), but given the problem formulation in this work, as well as its potential applications in smart cities, one might question whether this specialized framework is necessary. It would be valuable for the authors to elaborate on why a decentralized approach is essential in this context. The authors suggest that a centralized control setting could effectively handle scenarios like Perception-Red-Light, where no vehicle would violate the red light. If a centralized system is capable of resolving this issue naturally, it would be helpful to clarify why the proposed decentralized approach, which introduces the additional complexity of natural language communication, is necessary for addressing such a scenario. Without a clear justification, this may create an artificial problem that may not align with practical, real-world needs.

### Weakness 2: Unclear method and training.
The so-called "training" in this work does not align with traditional machine learning training paradigms. 
> For each LLM-based learning method, we train the models for up to 30 episodes per scenario, with early stopping if the scenario is solved, indicated by 10 consecutive successful episodes. After training, we evaluate each method over 30 episodes and report the average performance across these evaluations

However, on closer examination (as detailed in the appendix), this approach appears more akin to an agentic framework where the LLM is prompted to reason, propose actions, and reflect within episodic contexts, rather than engaging in conventional gradient-based learning. The overall experiment is also not systematic as "30 episodes" provides limited information about what has been used in testing and learning. The qualitative examples only show snippets of interactions.

This approach also contrasts with more complex agent-based vision-language models [5-7], which often account for a broader range of visual context and alignment issues. The simplicity of this framework raises concerns, particularly in overlooking these ambiguities.

### Weakness 3: Related work.
The authors could consider improving the related work.

> However, training such models requires extensive data. At the time of writing this paper, only a limited number of datasets exist that provide language commentary data for single-agent driving scenarios (Kim et al., 2018; 2019; Qian et al., 2023; Sima et al., 2023). To the best of our knowledge, datasets featuring natural language data for inter-vehicle communication are not yet available.

To the best of my knowledge, language datasets featuring human-vehicle communication [1-2] and vehicle-vehicle (multi-agent) collaboration [3-4] already exist. Although these resources do not diminish the novelty of this work, the authors should provide a detailed discussion on how this paper differs from previous efforts, rather than simply stating that similar datasets “are not yet available.” The authors seem to conflate interpretability with the use of natural language messages, suggesting that V2V or multi-agent collaboration must rely on natural language for interpretability. However, interpretability does not necessarily require natural language. Many systems achieve interpretability effectively through structured formats or symbolic representations, which may be more appropriate and efficient for V2V communication.

### Questions
Question 1:  Given the problem formulation in this work, as well as its potential applications in smart cities, why do we even need a decentralized approach like the one proposed? Would authors compare to the centralized agent as a baseline?

Question 2: How would visual information be handled in this work since CARLA is used for physical simulation? 

Question 3: The action space seems to be high-level and discrete. Did the author rely on CARLA's built-in local motion planner, which has access to ground truth information about the environment? Is the focus of this work on the decision-making part rather than the actual control? (If so, I recommend changing the wording of "control policy")

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper proposed using natural language as the means of communication in traffic scenarios with V2V communication. In particular, the authors found that LLM + debrief significantly improves the performance of the cooperative planning pipeline. The proposed method is evaluated in a gym-like simulation environment equipped with LLM and Carla as the vehicle simulator and showed some signs of life. Comparing to the baseline, using language feedback leads to much smaller communication messages yet the performance seems worse than the baseline.

### Strengths
1. The idea of using natural language as feedback is interesting. Although it is probably considered by many people, the authors managed to build a simulation environment that enables communication with natural language.

### Weaknesses
1. The idea of isolating a finite set of agents called the "focal group" is not really practical in real world as the communication graph can extend to a huge size, although I understand that this is probably the common setup for V2V communication scenarios.
2. I find it very confusing as to which part of the simulation environment is automated and which part is hand-crafted/hard-coded. I think this is critical to assessing the practicality of the proposed method and a more detailed breakdown would be nice.
3. The concept of a partially observed general-sum game isn't really relevant to the proposed method. I understand that it is a nice way to describe the problem, but I don't see any game theory tools used in the actual solution.
4. The performance of the LLM agent is worse than the baseline. Although the messages were smaller, I wonder whether the benefit of smaller messages is overshadowed by the significant increase in computation. More analysis on this is needed.

### Questions
1. Please clearly state which part of the simulator is fully automated and which part is hand-crafted/hard-coded.
2. What is the role of game theory in the proposed method?

### Soundness
2

### Presentation
2

### Contribution
2
