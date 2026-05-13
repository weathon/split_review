# Habitat 3.0: A Co-Habitat for Humans, Avatars, and Robots

- Decision: Accept
- Scores: 6, 6, 8

## Abstract
\makeatletter
\def\blfootnote{\xdef\@thefnmark{}\@footnotetext}
\makeatother
\blfootnote{$*$, $\dag$ indicate equal contribution. Work done at Fair, Meta.}
We present Habitat 3.0: a simulation platform for studying collaborative human-robot tasks in home environments. Habitat 3.0 offers contributions across three dimensions: (1) \textbf{Accurate humanoid\footnote{Throughout this paper, we use \emph{avatar} or \emph{humanoid} to refer to virtual people in simulation and \emph{human} to refer to real people in the world.} simulation}: addressing challenges in modeling complex deformable bodies and diversity in appearance and motion, all while ensuring high simulation speed. (2) \textbf{Human-in-the-loop infrastructure}: enabling real human interaction with simulated robots via mouse/keyboard or a VR interface, facilitating evaluation of robot policies with human input. (3) \textbf{Collaborative tasks}: studying two collaborative tasks, Social Navigation and Social Rearrangement. Social Navigation investigates a robot's ability to locate and follow humanoid avatars in unseen environments, whereas Social Rearrangement addresses collaboration between a humanoid and robot while rearranging a scene. These contributions allow us to study end-to-end learned and heuristic baselines for human-robot collaboration in-depth, as well as evaluate them with humans in the loop. Our experiments demonstrate that learned robot policies lead to efficient task completion when collaborating with unseen humanoid agents and human partners that might exhibit behaviors that the robot has not seen before. Additionally, we observe emergent behaviors during collaborative task execution, such as the robot yielding space when obstructing a humanoid agent, thereby allowing the effective completion of the task by the humanoid agent.  
Furthermore, our experiments using the human-in-the-loop tool demonstrate that our automated evaluation with humanoids can provide an indication of the relative ordering of different policies when evaluated with real human collaborators. Habitat 3.0 unlocks interesting new features in simulators for Embodied AI, and we hope it paves the way for a new frontier of embodied human-AI interaction capabilities. The following video provides an overview of the framework: \url{https://tinyurl

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
- This work introduces Habitat 3.0, a simulation platform for studying human-robot collaboration in home environments.
- The environment includes accurate humanoid simulation and a human-in-the-loop infrastructure for real-time interaction and provides a way to evaluate different robot policies with real human collaborators.
- It also allows the exploration of collaborative tasks: Social Navigation and Social Rearrangement. 
- Finally, the authors demonstrate that learned robot policies can effectively collaborate with unseen humanoid agents and human partners. Shows emergent behaviors during task execution, such as yielding space to humanoid agents.

### Strengths
1. This work complements existing works (e.g. Habitat, VirtualHome, etc.) in a human-centric way. It allows more flexible human models, human-object interactions, human-robot interactions, and human-in-the-loop evaluation, which are often ignored in previous works.
2. This work is in general well-written, providing a good survey for the field of embodied AI environments.
3. This work designs two social/collaborative tasks, navigation and rearrangement, and shows promising results.

### Weaknesses
The main limitation of this work lies in universality. While I believe this work is interesting and helpful to the field, I am wondering if it could be scaled to incorporate more elements, supporting more tasks, so that the progress wouldn't stop here at the two example tasks. While I understand that these aspects might be beyond the scope of a single work, it would be beneficial to demonstrate, or at least discuss, how future works can develop upon Habitat 3.0. For example,
- physics simulation 
- fine-grained object interactions
- sim2real deployment

### Questions
1. For social arrangement, what is the motivation for using population-based approaches? More discussions would be helpful to understand the setting.
2. Discuss relevant previous works. What is the relationship between the proposed social navigation task and visual tracking (e.g. [a])? Seems quite similar and more discussions are needed. Besides, [a] also contains humanoid simulation and end-to-end RL with Conv+LSTM.
3. For object interaction, Sec. 3.1 explains that "Once the hand reaches the object position, we kinematically attach or detach the object to or from the hand." Are all the objects simplified as a point particle? Are all the objects in the environment interactive? Is it possible to add more properties to them (e.g. geometry - shape, physics - weight, material, etc.)? It would be great to explore/discuss how to incorporate more general and complex object interactions, from pre-defined motion primitives (e.g. lie, sit) to freeform actions (e.g. grasp).
4. Currently this work focuses restricted set of motions while more motions can be potentially added with the SMPL-X representation. In demo video 2:56, it also discusses complex motions (e.g. wiping, knocking). It would be beneficial to discuss how future works can incorporate more motions with interactive objects and form meaningful tasks. 
5. Another question is, what kind of tasks can Habitat 3.0 support in addition to navigation and arrangement? Again, I understand that these two tasks are already great for this work, but more discussions on the potential of Habitat 3.0 would make this work more general and influential.
6. I wonder if the HITL tools would also be standardized and open-source.

[a] End-to-end Active Object Tracking via Reinforcement Learning, ICML 2018.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents Habitat 3.0, an Embodied AI simulator designed to facilitate research in human-robot interaction and collaboration within complex indoor environments. The proposed platform aims to address the need for efficient simulation tools to study AI agents' capabilities in realistic and diverse human-robot interaction scenarios. The main contributions of the paper are as follows:

Diverse Humanoid Simulation: Habitat 3.0 offers a framework for creating and simulating diverse humanoid avatars. These avatars encompass various appearances and motions, enhancing the realism of agent interactions within the simulated environments. By employing techniques like skeletal models and linear blend skinning, the simulator achieves a balance between efficiency and visual fidelity.

Human-in-the-Loop (HITL) Evaluation Tool: The paper introduces a HITL interface that allows real human operators to control humanoid avatars within the simulated environment. This tool enables online human-robot interaction evaluations and data collection, providing a unique platform for studying how AI agents collaborate with humans.

Social Navigation and Social Rearrangement Tasks: The paper explores two collaborative tasks—social navigation and social rearrangement—to assess AI agents' ability to interact with human or humanoid partners. These tasks require the agents to find and follow humans at a safe distance or to collaborate with a humanoid in rearranging objects within the environment.

Evaluation of AI Agents: The paper compares multiple AI agent baselines in both automated and HITL evaluation settings. These agents include heuristic experts and end-to-end reinforcement learning policies. The evaluations highlight the agents' adaptability in working with different partners to some extent and provide insights into their efficiency and success rates.

Robust HITL Assessments: By conducting HITL evaluations involving real human participants, the paper evaluates AI agents' coordination abilities in scenarios involving diverse partners. These assessments help in understanding how baseline AI agents impact human efficiency and reveal insights into the dynamics of human-robot interactions.

### Strengths
Quality:
The paper demonstrates a fair level of quality in its methodology and execution. The development of Habitat 3.0 is well-detailed and addresses a clear need in the field of HRI research. The simulator provides an effective platform for investigating human-robot interaction. The evaluation of AI agents in both automated and HITL settings enhances the paper's quality.

Clarity:
The paper is generally well-written and clear, with detailed explanations of the simulator framework and the tasks studied. 

Originality:
Habitat 3.0 introduces valuable original contributions to the field. The combination of diverse humanoid simulation, HITL control, and the study of social navigation and rearrangement tasks provide some initial steps and ideas in this domain. Furthermore, the paper explores HITL evaluations involving human participants, which adds to the originality of the work. While the components themselves are not entirely novel, their integration and application within a single framework is original and significant.

Significance:
Habitat 3.0, with its focus on embodied AI and human-robot interaction, addresses a critical aspect of AI development. The simulator has the potential to open new avenues for research, including collaborative AI, human-robot teamwork, and social embodied agents. The HITL evaluations are particularly significant, offering insights into how AI agents impact human performance and behavior. The paper's findings and methodology are likely to influence future research in these domains.

Overall, its strengths can be listed as:
- focus on human-robot interaction compared to previous platforms offering single-agent or multi-homogeneous-agent training.
- efficient simulation implementation that enables faster progress in training/evaluating developed algorithms.
- human-in-the-loop evaluation tool that can open up interesting use-cases and approaches to improve and analyze HRI methods.
- a fair amount of evaluations.

### Weaknesses
The critical weaknesses are:
- currently, the focus of simulations seem to be more on the visual realism, which is a valid concern. However, the movement of the agents lacks physical realism, which hinders the extend of how human-robot interaction can be evaluated accurately. Specifically, the humanoid agents exhibit unrealistic, jerky movements, rotating rigidly to face waypoints before moving in straight lines, failing to capture the fluidity and momentum of natural human locomotion. This oversimplification limits the transferability of learned policies to real-world scenarios and reduces the accuracy of HRI analysis.

- the focus of this work is not proposing novel learning algorithms but still the results indicate that none of the baselines achieve useful following rate (F) nor feasible collision rate (CR) in the social navigation task. Similarly, for the social rearrangement task, none of the methods seem to generalize and let the robots assist their partners effectively (checking the relative efficiency (RE) metric). Even for HITL evaluations, which would be simpler since humans adjust to robots on the fly, the results are not encouraging. This, then, makes it harder to evaluate and take some insights from these evaluations, which is a major component of the paper.

- humanoid shape diversity has been considered, however, robotic agent diversity was not addressed. The lack of diverse robotic agents limits the generalizability of the findings, as the platform currently does not reflect the variety of robots used in real-world HRI settings.

- similar to the previous point, the platform, as it is now, lacks task diversity as well. The current tasks are limited to social navigation and social rearrangement, which restricts the scope of research that can be conducted using the platform. The absence of tasks that involve more complex collaborative interactions, such as physical object manipulation or joint problem-solving, limits the platform's utility.

- it feels like (looking at the efficiency improvements (RE metric) when collaborated vs. solo cases) maybe the tasks do not offer enough opportunities for collaboration. The tasks, as currently designed, might not fully leverage the potential for collaborative interactions, as the relative efficiency metrics suggest only marginal improvements when agents work together compared to solo performance.

- personally, I find the HITL evaluations more interesting, however, the paper does not cover detailed evaluation and analysis of these experiments.

### Questions
- what are possible solutions/integrations to alleviate the unrealistic humanoid locomotion problem, i.e., the agent first rigidly rotates to face the next target waypoint and then follows a straight path. The autonomous agents trained against such human movement models will not be directly transferable to real-world settings, nor the analysis would not be informative.

- it is unclear how easy and flexible to import motion capture data. Can you elaborate on that?

- it is also unclear how trivial it is to use the AMASS dataset along with VPoser to compute humanoid poses and then to import them into the simulator. Trying to use such external tools that the benchmark providers do not support/maintain themselves frequently becomes a huge hassle and ease-of-use of such external tools is critical, so can you also provide some clarification on their integration and/or usability? 

- About reliance on VPoser: Depending on the complexity of the task, simple interpolation between poses might not be sufficient, what would be possible solutions?

- is it possible to incorporate physical collaboration scenarios, i.e., partners acting on the same object? would it require additional steps than what was explained on the paper?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper provides a simulator supporting humanoid avatars and robots for the study of collaborative human-robot tasks in home environments. Diverse and realistic human models are constructed, addressing the challenges of accurate modeling of the human body as well as the human-like appearance and motion diversity of the models. Besides, The platform supports interaction between a real person and a simulated robot via a mouse and keyboard inputs or VR interface, enabling human-in-the-loop simulation. This paper also investigates two collaborative human-robot interaction tasks, social navigation, and social reorganization, and provides insights into learned and heuristic baselines for both tasks in the simulator.

### Strengths
- This work presents a Co-Habitat for Humans, Avatars, and Robots, offering a simulation environment for humanoids and robots within a wide range of indoor settings, which can promote the development of human-robot tasks in the Embodied AI field.
- Habitat3 provides realistic human and robot simulation. In the process of realistic human modeling, this work addresses the challenges posed by efficiency realism and diversity in terms of appearance and movement.
- This work develops a Human-in-the-Loop evaluation platform within the simulator, allowing the control of humanoid robots using a mouse, keyboard, or VR devices. It provides a method for interacting and evaluating with real humans. Furthermore, it supports data collection and reproducibility during the interaction, offering a convenient tool for further research.
- This paper introduces two benchmark tasks for human-robot interaction, along with baselines for each task. This paper leverages end-to-end RL to study collaborative behaviors and examines the performance of various learning strategies. The Human-in-the-Loop evaluation in the social rearrangement task reveals potential avenues for improving social embodied agents.
- This simulator can be used for end-to-end reinforcement learning for robot agents, significantly reducing the time required for reinforcement learning. It also provides a validation environment for a broader range of robot agents, thus reducing potential risks to the environment and humans.

### Weaknesses
 - Current robots are equipped with only a depth camera, human detector, and GPS, providing a relatively limited amount of information. It is worth considering whether additional sensor types, such as LiDAR and sound sensors, can be integrated in the future to enhance obstacle avoidance and navigation capabilities. Specifically, the reliance on a depth camera alone may limit the robot's ability to perceive fine-grained geometric details of the environment, potentially hindering navigation in cluttered or complex scenes. The lack of LiDAR, which provides accurate 3D point clouds, could make it difficult for the robot to create a robust map of its surroundings. Furthermore, the absence of sound sensors limits the robot's ability to respond to auditory cues, which can be crucial in dynamic human-robot interaction scenarios.
- It has been noted that in human simulation, fixed hand movements can lead to a decrease in visual accuracy. It may be considered to address the deformability of the skin during the simulation process and create hand motion animations during activities like grasping and walking. The current fixed hand poses likely result in unrealistic interactions, especially when the simulated human is interacting with objects or other agents. The lack of skin deformation further detracts from the realism, making the simulated human appear less lifelike and potentially impacting the ecological validity of the simulation. For instance, the absence of hand motion during grasping will not allow for the study of complex manipulation tasks.
- This simulator has a wide range of potential applications and can be further explored to implement other embedded artificial intelligence tasks, such as visual-language navigation. While the current implementation focuses on social navigation and reorganization, the simulator's capabilities could be extended to include tasks that require more complex reasoning and interaction with the environment.

### Questions
See Weaknesses

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent
