# MetaUrban: An Embodied AI Simulation Platform for Urban Micromobility

- Decision: Accept
- Scores: 8, 6, 8, 8

## Abstract
\makeatletter
\def\blfootnote{\xdef\@thefnmark{}\@footnotetext}
\makeatother
\blfootnote{$*$ Equal contribution.}

Public urban spaces like streetscapes and plazas serve residents and accommodate social life in all its vibrant variations.
Recent advances in Robotics and Embodied AI make public urban spaces no longer exclusive to humans. Food delivery bots and electric wheelchairs have started sharing sidewalks with pedestrians, while robot dogs and humanoids have recently emerged in the street.
\textbf{Micromobility} enabled by AI for short-distance travel in public urban spaces plays a crucial component in the future transportation system.
Ensuring the generalizability and safety of AI models maneuvering mobile machines is essential.
In this work, we present \textbf{MetaUrban}, a \textit{compositional} simulation platform for the AI-driven urban micromobility research.
MetaUrban can construct an \textit{infinite} number of interactive urban scenes from compositional elements, covering a vast array of ground plans, object placements, pedestrians, vulnerable road users, and other mobile agents' appearances and dynamics.
We design point navigation and social navigation tasks as the pilot study using MetaUrban for urban micromobility research and establish various baselines of Reinforcement Learning and Imitation Learning.
We conduct extensive evaluation across mobile machines, demonstrating that heterogeneous mechanical structures significantly influence the learning and execution of AI policies.
We perform a thorough ablation study, showing that the compositional nature of the simulated environments can substantially improve the generalizability and safety of the trained mobile agents.
MetaUrban will be made publicly available to provide research opportunities and foster safe and trustworthy embodied AI and micromobility in cities. The code and dataset will be released.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces MetaUrban, a simulation platform designed to support AI research for urban micromobility, focusing on autonomous systems navigating shared public spaces like streets and plazas. Unlike other platforms tailored for indoor or vehicle-based simulations, MetaUrban enables the development and testing of AI in complex urban environments. It includes diverse urban scenes, populated with obstacles, dynamic agents (like pedestrians and cyclists), and varied terrain. It has a compositional structure that allows for unbounded variations built upon its compositional elements.

The paper goes through various elements of MetaUrban:
- Hierarchical Layout Generation: This feature supports scalable scene generation, allowing the creation of realistic urban environments with complex layouts, functional zones on sidewalks, and varied terrains.
- Scalable Obstacle Retrieval: The platform uses real-world data to model the distribution of obstacles commonly found in urban settings and retrieves relevant 3D assets through vision-language models. This ensures that the simulation incorporates diverse, realistic objects to improve the generalizability of trained agents.
- Cohabitant Populating: MetaUrban models dynamic interactions by simulating various agents, including pedestrians and other vulnerable road users, with a range of movements and trajectories. This feature supports complex interaction scenarios, enhancing the safety testing of mobile AI agents.
- MetaUrban-12k, -unseen, and -finetune for training, testing, and finetuning - elements are action sequences in environments

The paper then reports the results of baseline experiments on MetaUrban. There are two primary tasks: Point Navigation (navigating to a target in static environments) and Social Navigation (reaching a destination while avoiding collisions with moving agents). Success was evaluated using metrics like Success Rate (SR), Success weighted by Path Length (SPL), Cumulative Cost (CC), and Social Navigation Score (SNS). Seven baseline models, including variations of Reinforcement Learning and Imitation Learning, demonstrated that tasks were complex, with maximum success rates of 66% for PointNav and 36% for SocialNav. Generalizability tests showed that models trained on MetaUrban-12K adapted to unseen environments with moderate success rates (41% for PointNav and 26% for SocialNav). Evaluations of different mobile machines highlighted that mechanical structures, such as speed and steering, significantly impacted performance; conservative designs improved safety but could hinder mobility. Ablation studies confirmed that increasing training data enhanced agent performance and that higher densities of static and dynamic obstacles posed greater challenges for successful navigation.

### Strengths
### Quality
- Design is robust
  - Procedural generation system clearly enables extensive domain generation 
  - Hierarchical layout generation, scalable obstacle retrieval, and cohabitant populating are convincingly argued to be crucial and effective for generating diverse scenes
- Baselines are well-considered and it's clear the benchmark is built for the current state of AI technologies, and ha put thought into the future of the field 
- Extensive evaluation and well-posed questions

### Clarity
- Paper flow is good 
- Though the paper could use more signposting, the writing is quite clear. As long as I'm able to follow along with where we are, I learn a lot from reading carefully 

### Originality
Seems to be novel, particularly the micromobility element. Combination of design factors also seems unique

### Significance 
Worthwhile to have a benchmark for alternative forms of transportation given the state of the environment. The focus on this is commendable.

### Weaknesses
### Clarity
- Paper currently has walls of text and lacks signposting - more subheadings, titled paragraphs, etc. would help 
- Figures don't seem especially well-considered - could use more thoughtful design rather than pasting various info and not much more 

### Quality 
- FMs are used creatively throughout the paper, but the paper could benefit from more material on how LLM failure modes are handled during generation

### Questions
- What challenges do you expect when transferring to real world? Is transfer realistic?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposed MetaUrban, a simulator for micro-mobility in urban environments. Unlike existing simulators, MetaUrban simulates agents in urban environments while navigating along paths, sidewalks, etc. This is different from existing simulators that either focus on indoor navigation or urban driving.

Environments are procedurally generated. The procedure begins by first generating a ground plan that specifies where roads will be, sidewalks, crosswalks, etc. Then terrain and objects are added. To determine what objects to add to a given scene, the authors propose to use real-world urban object distributions and design a pipeline towards this end.

Finally, other dynamic agents are added to the scene, such as humans, vehicle, and other robots. Trajectories are created for these agents using the ORCA social forces model and the push and rotate algorithm to resolve deadlocks.

The authors then evaluate RL, IL, and Offline RL methods on two tasks, PointNav and SocialNav.

### Strengths
The proposed environments have been very carefully designed to represent real-world urban scenes.

The paper is well-written and easy to follow. Further, the simulator and choice of tasks is well-positioned and well-motivated.

There is an extensive Appendix that provides additional details, experiments, and context.

### Weaknesses
The performance of the simulator is a weakness. RGB rendering is, at best, 65 FPS, which is orders of magnitude lower than would be ideal and at least an order of magnitude lower than would be "good".

I encourage the authors to see if there are features that can be turned off for the sake of performance if researches want to make that trade-off. For instance, can visual fidelity be reduced (by disabling things like shadows), or can animations be disabled to increase performance?

I see the value of including these features for sake of full-fledged evaluation, but these may not be necessary for training and are likely not needed for initial experiments.

### Questions
See above.

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
4

### Summary
The paper presents MetaUrban, a simulation platform designed for AI-driven urban micromobility research. It generates interactive urban environments to train and test AI systems like delivery bots and electric wheelchairs. The platform supports diverse layouts, obstacles, and pedestrian interactions through procedural generation, real-world object retrieval, and dynamic agent simulation.

MetaUrban-12K, a dataset created from the platform, is used to benchmark Point Navigation and Social Navigation tasks with different AI models. The paper shows how variations in machine design impact performance and highlights the platform's potential to improve the generalizability and safety of AI agents.

### Strengths
1. The platform supports varied human and mobile agent behaviors, providing a rich set of interactions that better simulate the dynamics of crowded urban settings for long-horizon tasks.
2. The procedural generation of diverse terrains and object placements creates highly varied environments to help train robust models.
3. The paper explores the impact of different mechanical designs on mobile machines.

### Weaknesses
1. The main goal of such a large-scale simulator is to eventually transfer learned models to the real world. However, there is limited experimentation with real robots, and details on how well models trained in the simulator generalize to real-world sensor data are unclear. More real-world testing is necessary to demonstrate effective transferability.

2. The paper does not specify if robots, pedestrians, and other mobility devices can be controlled via standard interfaces like ROS. Without ROS integration, robotics users may need to modify their software pipelines, limiting the platform's usability. This lack of integration would also hinder the deployment of trained models onto real robots, making the simulator less practical for real-world robotics applications.

3. It is unclear how the simulator synchronizes with model updates during benchmarking. If the simulator runs ahead of model updates, this could lead to model decisions being applied to future time steps, potentially reducing the accuracy of training and evaluation. A more detailed explanation of time synchronization between the simulator and model updates is necessary to ensure the integrity of the training process.

4. While pedestrian behavior is simulated, there is little exploration of how AI models handle complex, unpredictable social interactions. Expanding evaluations in this area would improve the relevance of the social navigation task.

5. The paper does not fully explore the performance impact of different sensor configurations (e.g., lidar, cameras). A detailed comparison of sensor types would provide practical guidance for applying models to real-world scenarios.

6. The paper does not mention if the simulator can run in distributed systems or scale across multiple machines. Also can the simulator run in headless mode so that it can be scalably deployed on a cluster. Can the simulator run faster than real time to make model training and evaluation quicker.

7. The paper does not discuss how environmental factors like weather or lighting conditions (day/night) are handled.

8. The platform includes dynamic agents but does not explore multi-agent coordination, competition, or collaboration. More emphasis on multi-agent learning and interactions could make the simulator useful for tasks involving coordination among multiple robots or agents.

### Questions
Refer to the weaknesses section.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This is a "tech report" that introduces MetaUrban, a simulator that focuses on micromobility, consisting of low-speed moving objects such as pedestrians, bikers, small ground robots, and wheelchairs. The functionality of the simulator seems pretty strong, and it fills the gap of a simulator for applications such as low-speed robots in urban areas.

### Strengths
1. The simulator functionality is quite strong, supporting various terrain designs, static obstacles, and moving agents.
2. There are ways to easily retrieve the desired materials for building urban scenarios
3. The authors provide benchmark statistics for RL/IL agents with the simulator, demonstrating its usability
4. It fills the gap of simulating urban low-speed scenarios and is useful for many applications
5. It comes with a dataset for urban scenarios.

### Weaknesses
This is a tool that enables future research, clearly there will be feature requests to make it better and easier to use, but I don't see an clear issue with the design.

### Questions
1. Will it support easy deployment of agent policies instead of ORCA?
2. What is the runtime performance of the simulator? Is it efficient to run?

### Soundness
3

### Presentation
3

### Contribution
3
