# MuJoCo Manipulus: A Robot Learning Benchmark for Generalizable Tool Manipulation

- Decision: Reject
- Avg Score: 3.40
- Scores: 3, 5, 3, 3, 3

## Abstract
We propose MuJoCo Manipulus, a novel open-source benchmark powered by the MuJoCo physics simulation engine, designed to accelerate advances in robot learning for tool manipulation. Our benchmark includes a diverse set of tasks for tool manipulation --- a domain where the field currently lacks a unified benchmark. Different research groups rely on custom-designed tasks or closed-source setups, limiting cross-comparability and hindering significant progress in this field. To that end, our benchmark provides 16 challenging tool manipulation tasks, including variants of Pouring, Scooping, Scraping, Stacking, Gathering, Hammering, Mini-Golf, and Ping-Pong. The benchmark supports both state-based and vision-based observation spaces, is fully integrated with the Gymnasium API, and seamlessly connects with widely used Deep Reinforcement Learning libraries, ensuring easy adoption by the community. We conduct extensive reinforcement learning experiments on our benchmark, and our results demonstrate that there is substantial progress to be made for training tool manipulation policies. Our codebase and additional videos of the learned policies can be found on our anonymous project website: https://mujoco-manipulus.github.io

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper presents a benchmark designed for robotic tool manipulation using the MuJoCo physics engine. It offers a diverse set of 14 tool manipulation tasks across categories such as pouring, stacking, scooping, gathering, hammering, and scraping. Each task features specific tools (e.g., cup, ladle, hammer) and allows for both state-based and vision-based learning. The benchmark integrates with Gymnasium API and popular reinforcement learning (RL) libraries, making it easily used by the research community.

### Strengths
1. The paper is well-written with clear images.
2. It presents convenient APIs and environments, built on the MuJoCo engine, incorporating various tools and objects.
3. Several commonly used RL algorithms were tested.

### Weaknesses
1. The benchmark lacks completeness; as a robot learning environment, it does not include any robots, and the tasks and action spaces are very simple.
2. Novelty and contribution are severely concerned - it feels more like an engineering project. Essentially, it imports objects into MuJoCo, designs tasks around them, and tests some off-the-shelf algorithms.
3. The action space appears to involve directly transforming the pose of the objects (tools) rather than applying interaction with them, which raises severe concerns about whether true physical simulation is involved.
4. Current SOTA simulation benchmarks could support the tasks presented in this paper by simply importing the relevant 3D objects.

### Questions
No additional questions.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents Mujoco Manipulus, a tool use benchmark for RL research.  This benchmark is built on top of Mujoco and gynmasium, and supports a range of tasks and tools such as scooping, stacking and gathering.  The authors evaluate PPO and SAC on these tasks using both vision and state information, demonstrating that these tasks are nontrivial to solve.

### Strengths
+ Developing new benchmarks for robotic skills and manipulation is an important contribution to the community.
+ The paper is well presented and easy to understand.
+ The authors present a clear picture of related work.

### Weaknesses
 - The size of the benchmark is relatively small.  There are only a few tasks and objects available.
- The complexity of these tasks is relatively low.  The agent has direct control over the tools (non-dexterous) and requires only a few degrees of freedom to move them.
- The realism is fairly limited, while at the same time the simulator uses Mujoco on the CPU.  Most recent robotics benchmarks are moving toward either greater realism or very-high-throughput simulation on the GPU, and so this benchmark, which lacks both, feels somewhat behind the Pareto frontier.
- It's not clear how challenging this benchmark is.  The authors run PPO and SAC on these tasks and show that they struggle to solve them out of the box.  In many robotics applications though, a large degree of reward shaping or learning from demonstrations is frequently necessary to solve real world problems, and it's not clear why those approaches wouldn't work here as well.
- A more thorough comparison against relevant tasks from Maniskill2 and Robosuite is necessary to establish the utility/necessity of this new benchmark.  Those two settings contain some tool use, are the tasks here harder than those?  More comprehensive?  Given the simplicity of the models presented here, it seems like the others should be more realistic.  What new features does this benchmark include that are not covered elsewhere?  If the only contribution here is to package together certain types of tasks that exist across many other benchmarks, that could still be useful to the community, but more work needs to be done to establish the added value of the dataset relative to what's already out there.
- Along the same lines, in a more general sense it is not clear what utility the broader community gets from this new benchmark.  Given the limited realism, this doesn't seem like it advances our practical ability to train real-world robots (sim-to-real does not seem to be much of a consideration here).  Given the small size, it doesn't add much to the already substantial physically grounded simulation benchmarks for RL.  The authors motivate this benchmark by arguing that there is not a dedicated tool-use benchmark for robot manipulation, but there are several that contain tool use as a subset, and it's not clear what this new one adds to them.

### Questions
The authors mention Maniskill2 and Robosuite, but say that only a portion of those tasks cover tool use/manipulation.  How would the current benchmark compare in size/complexity/realism with a subset of the Maniskill2 and Robosuite tasks that only cover tool use/manipulation?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduced a MuJoCo-based simulation framework named "MuJoCo Manipulus," which features tool-use tasks such as pouring, stacking, scooping, gathering, etc. In these benchmarking tasks, an "idealized" agent manipulates a free-floating tool to physically interact with objects and accomplish manipulation goals. Specifically, the initial release of this benchmark includes 12 tools spanning two categories: Kitchen Tools and Home Tools, which were either hand-designed or drawn from existing asset libraries (e.g., TACO and MuJoCo). The authors highlighted several engineering features offered by their framework, including support for end-to-end RL with the MuJoCo physics engine, integration with the Gymnasium interface, and state/vision-based observations. As an initial attempt toward solving these tasks, they evaluated two popular deep RL algorithms, PPO (on-policy) and SAC (off-policy), with both state-based and vision-based observations. These baseline methods achieved mixed results in these tasks, suggesting room for future development.

### Strengths
- **Problem motivation.** Tool use is an important family of robot manipulation problems to study, as it represents a high level of physical intelligence manifested in intelligent species and requires multi-step, contact-rich interactions with multiple objects. Building systematic benchmarks for robotic tool manipulation would facilitate reproducible research in this problem domain.
- **User-friendly design.** The proposed benchmark was built on the MuJoCo simulation engine. Its designs prioritized flexibility and ease of use, with the standardized Gymnasium APIs and support for state-based/vision-based observations for end-to-end reinforcement learning. These designs could reduce the barrier of entry for researchers to leverage this simulator for research.
- **Baseline evaluations.** Experiments with standard RL algorithms, including PPO and SAC, presented a baseline view of existing RL methods' strengths and limitations. These preliminary results provide insight into the major challenges and motivate potential avenues for future work.

### Weaknesses
While the benchmark is well-motivated and carefully designed, its current version bears major weaknesses:

- Although the authors motivated this benchmark for robot learning and manipulation research, this paper did not use realistic robot models or controllers. Instead, it used an idealized "point mass" robot with simple Cartesian action spaces. This design severely abstracts away the challenges of contact-rich robot manipulation problems in the real world. Compared to existing manipulation benchmarks, such as ManiSkill2 (Gu et al., 2023) and Robosuite (Zhu et al., 2020), which aimed to model robot dynamics faithfully, the simplified robot model could hinder the ability to deploy the learned models on physical robots and thus limit its impact in advancing robot learning research.

- The authors motivated the benchmark as a "wider-scale tool manipulation benchmark with substantially more tasks." However, the current offering of the tasks is fairly limiting compared to several existing simulation frameworks for robot navigation and manipulation (Nasiriany et al., 2024; Szot et al., 2021; Li et al., 2022), which provides 100-1000 tasks in large-scale home environments. In contrast, the proposed benchmark only provides 14 simplified tasks in a restricted tabletop workspace.

- The authors highlighted the "Unified API for Reinforcement Learning with MuJoCo" as the main feature of the benchmark and spent a great amount of text in Sec 3 explaining these design choices. However, these features seem to be directly inherited from MuJoCo and its derived open-source tools/software, such as Gymsium. MuJoCo provides native support for state-based/vision-based observations, which has been commonly used in existing frameworks such as Robosuite (Zhu et al., 2020). Therefore, it remains unclear what technical challenges the authors have tackled to construct this benchmark and what are unique designs of this benchmark that have not been done in prior work.

- The experiments of this paper focus on evaluating off-the-shelf RL methods instead of innovating new ones. More qualitative analyses and ablative studies should be done to understand the limitations of these methods and provide insight into how these algorithms could be improved to better tackle these tasks. The mixed success rates also indicate the challenges of defining informative (dense) reward functions without extensive reward engineering. More reward design techniques could be explored to improve the quality of these tasks for RL purposes.

### Questions
In addition to addressing my comments in the Weaknesses section above, I have the following questions:
- I would like to hear the authors' explanation of the technical contributions of this work in comparison to existing MuJoCo-based simulations and tools. The APIs, simulation speed, and environments do not seem particularly novel. Can you please clarify how this effort differentiates (improves upon) robot learning simulations, especially the ones built with MuJoCo?
- Why would different tasks come with different action spaces, from three to five DoFs? For example, the Pouring tasks have 4D action spaces, while the Stacking tasks have 3D ones. Would it be beneficial to unify the actions across these tasks to enable multi-task RL research with the benchmark?
- Could you comment on the potential of transferring the model trained on MuJoCo Manipulus to a real robot? How could you bridge the embodiment gap between the idealized robot used in this work and the kinematic designs of real robots?
- The RL results reported that "the PPO+RGB and SAC+RGB methods were often better than PPO+State and SAC+State." This result is interesting and a bit counterintuitive, as visual RL is usually more expensive to train due to the high-dimensional visual observations as input to the policy. Could you provide more insight why we see this result?

### Soundness
2

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
4

### Summary
a Mujoco benchmark for policy learning including pouring, stacking, scooping, and various miscellaneous tasks, each with multiple tool options

### Strengths
This work introduces a MuJoCo simulator featuring a range of tasks, including pouring, stacking, scooping, and various miscellaneous tasks, each with multiple tool options.

The benchmark supports both state-based and image-based representations, compatible with standard reinforcement learning algorithms such as PPO and SAC.

### Weaknesses
The novelty of this benchmark appears limited. Many tasks resemble simplified, toy examples, with objects floating in the air rather than being manipulated by robotic arms. This raises concerns about the practical value of the benchmark for advancing robot learning.

The content is incomplete, with multiple paragraphs repeating similar ideas. While the state space for different tasks is described, there is no mention of the action space, reward function, or terminal states. The lack of detail regarding the action space makes it difficult to assess the complexity and feasibility of the tasks. For instance, are actions parameterized in joint space or Cartesian space? What are the bounds on the action space, and how do these bounds affect the learning process? Similarly, the absence of a clearly defined reward function makes it impossible to understand the learning objective and how it is achieved. Without knowing the reward structure, it is difficult to evaluate the effectiveness of the benchmark for training agents.

There is no comprehensive comparison with previous benchmarks, leaving the unique contributions of this benchmark unclear. The number of objects or tools available for each task is limited, which restricts the potential for in-category object manipulation learning. For example, the pouring task might only include a single type of container and liquid, which limits the generalizability of any learned policy. The lack of object variation prevents the benchmark from being useful for studying generalization across object categories.

### Questions
1. Could different robot manipulators be added to the simulator? Most robotic arms are limited by their mechanical design and current motion planning algorithms, making it challenging to follow the trajectory of floating objects.

2. Could this benchmark support in-category object variations for each task? Adding this feature would greatly benefit the robot learning community.

3. A comparison table highlighting the differences and contributions of this benchmark compared to others would be very helpful.

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces MuJoCo Manipulus, a new benchmark for robotic tool manipulation. Built on the MuJoCo simulation platform, the benchmark includes 14 tasks and offers a user-friendly gym interface. The paper also provides baseline evaluations using SAC and PPO algorithms on the proposed tasks.

### Strengths
1. The paper is well-structured and presents its contributions clearly.
2. Tool manipulation is an important and timely topic in robotics, and the introduction of a new benchmark in this area is a valuable contribution.

### Weaknesses
1. A significant limitation of the benchmark is that the tasks are based on floating control points, rather than simulating direct interaction between the robot and the tool. This abstraction, while simplifying the simulation, bypasses the complexities of tool-object contact dynamics and force interactions which are crucial for realistic manipulation. The absence of a physical robot arm and direct tool interaction makes it difficult to evaluate the performance of manipulation policies in scenarios with real-world constraints such as joint limits, torque limits, and contact forces. This approach also neglects the challenges of grasping and maintaining a stable hold on the tool, which are fundamental aspects of tool manipulation. The floating control point abstraction reduces the realism of the tasks and poses significant challenges for sim-to-real transfer, which is critical in robotic manipulation.
2. Despite the claim of offering a "diverse set of challenging tool manipulation tasks," the benchmark consists of only 14 tasks, with a significant portion focused on pouring. This narrow focus, with multiple variations of pouring tasks, limits the utility of the benchmark for evaluating a broader range of tool manipulation skills. The benchmark lacks tasks that involve more complex tool use such as cutting, hammering, or screwing, which are common in real-world scenarios. The limited diversity in task types restricts the ability to assess the generalization capabilities of learned policies to different manipulation primitives.

### Questions
I have no major technical questions, as the paper is relatively straightforward. However, I am unsure whether ICLR is the most appropriate venue for this work. While the benchmark provides meaningful contributions to the field of robotics, it lacks substantial algorithmic innovation or methodological novelty that would typically align with the scope of ICLR. A robotics-focused conference may offer a more fitting platform for this type of work.

### Soundness
2

### Presentation
3

### Contribution
2
