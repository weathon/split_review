# GPUDrive: Data-driven, multi-agent driving simulation at 1 million FPS

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 8, 8, 3

## Abstract
Multi-agent learning algorithms have been successful at generating superhuman planning in various games but have had limited impact on the design of deployed multi-agent planners. A key bottleneck in applying these techniques to multi-agent planning is that they require billions of steps of experience. To enable the study of multi-agent planning at scale, we present GPUDrive, a GPU-accelerated, multi-agent simulator built on top of the Madrona Game Engine that can generate over a million simulation steps per second. Observation, reward, and dynamics functions are written directly in C++, allowing users to define complex, heterogeneous agent behaviors that are lowered to high-performance CUDA. We show that using GPUDrive we can effectively train reinforcement learning agents over many scenes in the Waymo Open Motion Dataset, yielding highly effective goal-reaching agents in minutes for individual scenes and enabling agents to navigate thousands of scenarios within hours.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents a GPU accelerated simulator that can generate millions of simulation steps samples per second that can be used to train multi-agent reinforcement learning (RL) algorithms. The simulator is claimed to simulate hundreds to thousands of scenarios/scenes in parallel with each scene containing thousands of agents.

The simulator is built on top of the Madrona Game Engine and is written in C++. The C++ simulator engine can also be interfaced with learning environments written in JAX and Torch.
The authors have released implementations of RL algorithms capable of processing millions of agent steps per second and some baseline agents trained on these algorithms that achieve 95% of their goals. The simulator claims to provide both recorded logs and RL agents for the environment.

The authors introduced certain metrics to evaluate the simulation speed of GPUDrive in terms of agent steps per second (ASPS), controllable agent steps per second (CASPS) and scene completion time. Compared against other sim engines like Nocturne GPUDrive achieved 25-40x training speedup solving 10 scenarios in less than 15 minutes.

### Strengths
- The proposed simulator has the flexibility to handle multiple modalities of sensor data. 

- The authors have implemented ways to reduce the memory footprint due to the large number of agents and observation space using algorithms like Bounding Volume Hierarchy (to exclude certain agent pairs for collision checking) and polyline decimation to approximate the straight polylines.

- The trained agents are claimed to be useful for out-of-distribution tests for the driving agents.

- The authors presented the different simulator features in a comprehensive way.

- The paper shows that the simulator gets the scaling benefits in terms of increased amortized sample efficiency with increasing dataset size. This can be beneficial when dealing with large scale datasets with limited compute.

### Weaknesses
 - The paper does not provide simple IDM (intelligent driving models) agents that can be sometimes practical to have basic reactivity to the ego-agent.
- The authors mention that the current work is limited in properly utilizing the generated samples for optimal training.

- Just a thought: The implementation is in C++ and it provides a binding interface with Python environments. It would have been nice to have a mono-language (primarily Python based) tool as the model training and other related pipelines are mostly in Python.

### Questions
- Were other agents in the scenes like pedestrians and cyclists also controlled? If so, what were the dynamics used to model their behavior if they were not logged?
- Nit: Ethical statement was missing?
- Nit: Can the x-axis in the center plot in Fig 5 be made to a log scale?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
GPU drive introduces a fast multi agent simulator build using C++ that helps you run complex scenarios especially related to self driving cars at scale built on top of the Waymo Open Motion dataset. This allows iterating on these scenarios quicker reaching greater than a million FPS thus allowing more experimentation runs and iterating/trying out different scenarios even on desktop grade GPU's.

### Strengths
1. A multi agent simulator accelerated on the GPU iteration of over a million steps per second.
2. Very well written and structured code to run any experiment easily with a lot of easy experimentation code readily available. 
3. Extensive results analyzing the sampling frequency of the simulation.

### Weaknesses
1. Figure 2 needs a better caption and an explanation
2. Designed to fit one exact dataset. A section explaining the effort required to integrate other datasets is desirable.

### Questions
1. Benchmarks consist of limitations because of the dataset. Can it be addressed by using another dataset ?
2. Stable baselines is not known that well for speed. Could other implementations of PPO have been used ?
3. Is there support for multi GPUs ? And if they do exist, an ablation or benchmark would be great for that

### Soundness
4

### Presentation
3

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
This paper proposes GPUDrive, a GPU-accelerated multi-agent driving simulator designed to increase efficiency of learning-based systems. The simulator allows for loading expert trajectories from real-world driving datasets, can support multiple observation spaces (including e.g. LiDAR), and displays favorable throughput compared to other openly accessible simulators. The simulator, together with pre-trained goal-conditioned policies, is made openly available with accessible pythonic interfaces.

### Strengths
- The proposed simulator improves over alternatives in terms of sample efficiency. All of the design choices appear reasonable, while the underlying source code with pre-trained driving baselines will be released.
- The ability to load real-world driving datasets is extremely useful, while providing a variety of observation spaces is a great feature.
- Transparency about current limitation of the benchmark are very helpful for user adaptation.

### Weaknesses
 - While the focus of this paper is on providing a novel simulator, it would be very interesting to see some more complex behavior over longer time-horizons to fully capture the capabilities unlocked by the simulator (e.g. training a single agent policy with higher velocity limit to weave through a simulated traffic scene, etc.)
- Showcasing such behavior would likely require addressing the “Absence of a map” limitation raised in the paper, in order to formulate more sophisticated reward function. An important question would then be how easily this could be integrated, and how much the absence of such a feature could hurt adaptation of the simulator. Specifically, the lack of a map makes it difficult to implement lane-keeping behavior or more complex navigation tasks that require global planning. The current goal-reaching task, while useful, does not fully demonstrate the potential of a high-throughput simulator for more complex driving scenarios.
- The discussion of batched simulators could be extended to include references [1-3], where [1] has driven many results in single-agent robot learning, while [3] considers heterogenous multi-agent settings
- Figure 3 mentions performance on an RTX 4080, while line 711 states RTX 8000
- Line 308: “number valid number”

### Questions
- How easily can the simulator be updated to efficiently provide map-like utilities that allow for lane-keeping rewards (re mentioned limitations)?
- Do you support loading multiple different polices for individual agents? Could they have different sampling rates? How would these aspects affect efficiency?
- How do traffic jams affect throughput (re BVH)? This could be an interesting experiment to add.
- In video scene_53.mp4, agent 4 displays rather jerky behavior when moving towards its goal - could you elaborate on the underlying reasons?
- In video scene_43.mp4, agents 1 and 10 seemingly disappear without reaching their goals - could you elaborate on this behavior?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents GPUDrive, a GPU-based simulator for autonomous driving. The simulator is compatible with existing datasets and allows parallel simulations. The experiments show that it can train a policy with 25-40x training speedup against the baseline.

### Strengths
1. The GPU-based simulation is important in facilitating the training for complex real-world applications, highlighted by recent advances in robotics.
2. The experiment result shows significant wall-clock time speedup again baselines.

### Weaknesses
1. The paper claims compatibility with existing datasets but only demonstrates map loading, leaving other functionalities unclear. For example, the imitation learning experiment or mixing agent behaviors—some from datasets and others from RL agents during training. The lack of experiments demonstrating these functionalities raises concerns about the practical utility of the simulator beyond basic map loading. Specifically, it is unclear how the simulator handles different data formats or if it supports the necessary data structures for complex agent behavior mixing.
2. I believe one major advantage of parallel environments is that it allows you to do randomization across different environments (worlds). However, the paper lacks detail on whether GPUDrive supports this capability. The absence of explicit support for domain randomization limits the simulator's ability to generalize to unseen scenarios, which is a critical aspect for real-world deployment. For example, randomizing weather conditions, road textures, or vehicle models is not discussed, which are common techniques in autonomous driving simulation.
3. While GPUDrive offers a Python interface, I am curious how easy to customize those key elements in the environment given that the observation, reward, dynamic functions are written in C++. The reliance on C++ for core functionalities might create a barrier for users who are not proficient in C++, potentially hindering rapid prototyping and experimentation. The paper does not provide sufficient detail on the API design and how users can modify these functions without recompiling the entire simulator. 
4. Experiments only evaluate IPPO, despite the paper claims that it targets at mixed motive setting. The choice of IPPO, a basic independent learning algorithm, does not fully validate the simulator's capabilities in handling complex multi-agent interactions. The paper lacks experiments that demonstrate the simulator's ability to facilitate research in cooperative or competitive scenarios, which are essential for mixed-motive settings.

### Questions
1. In Figure 3, the speedup appears nearly linear. However, it would be helpful to examine scaling performance by adding more environments to identify saturation points and gain insights into system limitations.. 
2. What is the scaling of speedup with respect to the number of agents in the environment? e.g., fix the number of environments and scales the number of agents?
3. In Figure 5, do you use the CPU-parallel version of Nocturne?

### Soundness
3

### Presentation
2

### Contribution
2
