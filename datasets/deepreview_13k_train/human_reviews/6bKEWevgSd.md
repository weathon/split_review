# ManiSkill-HAB: A Benchmark for Low-Level Manipulation in Home Rearrangement Tasks

- Decision: Accept
- Scores: 8, 5, 5, 5

## Abstract
High-quality benchmarks are the foundation for embodied AI research, enabling significant advancements in long-horizon navigation, manipulation and rearrangement tasks. However, as frontier tasks in robotics get more advanced, they require faster simulation speed, more intricate test environments, and larger demonstration datasets. To this end, we present MS-HAB, a holistic benchmark for low-level manipulation and in-home object rearrangement. First, we provide a GPU-accelerated implementation of the Home Assistant Benchmark (HAB). We support realistic low-level control and achieve over 3x the speed of previous magical grasp implementations at similar GPU memory usage. Second, we train extensive reinforcement learning (RL) and imitation learning (IL) baselines for future work to compare against. Finally, we develop a rule-based trajectory filtering system to sample specific demonstrations from our RL policies which match predefined criteria for robot behavior and safety. Combining demonstration filtering with our fast environments enables efficient, controlled data generation at scale.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper introduces **ManiSkill-HAB**, a comprehensive benchmark for low-level manipulation and in-home object rearrangement tasks. It aims to enhance the Home Assistant Benchmark (HAB) with a GPU-accelerated implementation for improved simulation speed and realism. The authors included extensive reinforcement learning (RL) and imitation learning (IL) baselines and developed an automated rule-based filtering system for generating demonstrations that are compliant with predefined safety and behavior rules. 

Together, this benchmark provides:
1. fast, realistic, diverse simulation tasks and environments for home scale manipulation challenges
2. support for low-level control that enables realistic grasping and interaction
3. extensive RL and IL baselines
4. vision-based robot dataset at scale

I recommend acceptance for this paper since it provides clear and important contributions to facilitate the advancement of in-home manipulation and embodied AI research.

### Strengths
Originality
- While there have been benchmarks for robotic manipulation and household-related task manipulation, this work focuses on tasks and objects prevalent in home assistant settings.
- Environments in this work are GPU-accelerated and significantly outperform prior works in terms of speed and computational costs.
- While filtering trajectories with privileged information from the simulator is not unseen, the ability to scale up the simulation and rendering at a faster speed makes sampling and filtering more trajectories feasible.

Quality:
- From the supplementary videos, the simulation environments and rollouts appear to be high quality.
- The comparisons to prior work show a clear advantage of the proposed method in simulation speed.
- The RL & IL baseline methods are extensively studied using this benchmark, providing future research good baselines.

Clarity:
- The writing, figures, and supplementary materials are well-presented and easy to follow.
- The evaluation protocols for the baseline methods are structured and presented clearly.
- The authors also included failure modes for each task in the supplementary material.

Significance:
- The benchmark attempts to address a critical need in the robotics community for more efficient and realistic simulation tools that can keep pace with the increasing expectation of robots performing complex tasks in daily environments.
- The potential impact on future research, particularly in home rearrangement tasks, is significant, providing a robust platform for developing and testing new algorithms and approaches.

### Weaknesses
1. Currently, this work consists of three long-horizon tasks: TidyHouse, PrepareGroceries, and SetTable. For future iterations, it would be beneficial to expand the tasks and manipulated objects beyond HAB and YCB datasets. Potential tasks could include cleaning dishes, laundry tasks, and tool usage.

2. The RL and IL baselines include SAC, PPO, and BC. It would be greatly beneficial to the research community to have more recent baseline methods such as TD-MPC2, ACT, Diffusion Policies, etc.

### Questions
1. Simulation limitations:
What are the limitations of simulation technologies used in this work? Would it be possible to simulate deformable objects, fluids, or more intricate rigid objects such as tools? Are there plans to expand the manipulation tasks beyond pick + place and open + close?

2. Real-World Application:
What are the anticipated challenges in transferring the learned behaviors from the simulated MS-HAB environment to real-world robots, particularly in unstructured environments like typical homes?

For future works, it would be interesting to study how methods that solve this benchmark at X% success rate would transfer to real world robotics.

### Soundness
4

### Presentation
4

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
The paper updates HAB benchmark to MS-HAB for GPU-based simulation and larger-scale evaluation. Especially, it adopts Maniskill3 (Sapien) as the backend instead of the original Habitat (Unity) backend. It is worth mentioning that the evaluation is now end-to-end in the physics engine and there is no magical grasping like in Habitat. Furthermore, it conducts more experiments on reinforcement learning / imitation learning methods for long-horizon manipulation tasks, and show the challenge of the benchmark.

### Strengths
1. The paper is well-written and easy to understand.
2. The updates are necessary for speed and physical fidelity.
3. The tool is widely useful, especially for long-horizon manipulation tasks like home-scale rearrangment challenge.
4. The baselines are more comprehensive in this paper comparing to previous papers, which provides a large amount of insight into the benchmark.

### Weaknesses
1. The novelty of the benchmark needs discussion. Especially when RoboCasa, Behavior-1k platforms are already published for a while (these are non-current work). In terms of the scale / scene diversity / task difficulty, why MS-HAB is comparable or is different with these existing pipelines.
2. The imitation dataset is generated with RL. Howerver, one can also generate (for pick and place) with sense-plan-act pipeline. Why not generate dataset with SPA pipeline?
3. It will be great if one provide baseline results for Senes-Plan-Act (TAMP), and with oracle information. This will provide valuable insights.

### Questions
1. Comparison with other benchmarks.
2. SPA pipeline for IL dataset.
3. More baseline comparison.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents MS-HAB, a benchmark for low-level manipulation and in-home object rearrangement aimed at supporting embodied AI research. The benchmark features a GPU-accelerated Home Assistant Benchmark (HAB), which the authors claim achieves over three times the speed of previous implementations, and provides extensive reinforcement learning (RL) and imitation learning (IL) baselines for future comparisons. Additionally, a rule-based trajectory filtering system has been developed to select demonstrations that meet specific behavior and safety criteria. Ultimately, this enhances simulation efficiency, and the authors hope their work will support scalable data generation for robotics research.

### Strengths
1. The benchmark provides a holistic framework for home-scale rearrangement, featuring a GPU-accelerated implementation of the Home Assistant Benchmark (HAB) that supports realistic low-level control, enabling more effective manipulation tasks.
2. It includes extensive RL and IL baselines, allowing researchers to compare their methods against established standards and fostering advancements in these areas.
3. The systematic evaluation approach, utilizing a trajectory labeling system, enhances the benchmark's reliability and provides detailed insights into performance.
4. The implementation of demonstration filtering allows for efficient and controlled data generation at scale, which is crucial for developing robust robotic systems.

### Weaknesses
1. There is significant room for improvement in the existing baselines, as the current performance may not meet the highest standards set by more advanced methods in the field.
2. The authors do not claim that the benchmark supports transfer to real robots, indicating that there are still challenges to be addressed in applying these methods in practical scenarios.
3. In fact, most of the ideas and techniques used in this paper have appeared in prior work, particularly the M3 framework proposed by Gu et al. [1]. Both the skill sequence partitioning for three long-horizon tasks and the training algorithms for various skills are fundamentally consistent with M3. However, the authors do not provide a detailed comparison with it in the paper.
4. The technical contribution is quite limited. The simulation environment, baseline algorithms, and even the subtask definitions used in the paper have already been proposed in previous work. This makes the draft somewhat more like a technical report.

### Questions
1. Why does the paper's baseline training algorithm not compare with the methods proposed in M3? M3 achieves a much higher task completion rate for the three tasks than the performance presented in this paper.  
2. Does the per-object policy refer to training a specific pick or place policy for each different object (e.g., bowls, cans, cups, etc.)? While this might improve completion rates for certain tasks, could it significantly limit the generalization capability for complete long-horizon tasks?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a robotic manipulation benchmark for home-scale rearrangement tasks, called ManiSkill-HAB. The authors implement the Home Assistant Benchmark (HAB) within the GPU-accelerated simulator ManiSkill3. The resulting environments achieve high simulation throughput, outperforming previous implementations by a factor of three. Additionally, the robot and object interactions are simulated with accurate rigid body physics to facilitate the learning of low-level manipulation skills. Finally, reinforcement learning (RL) and imitation learning (IL) models are trained to serve as baselines for future research. A rule-based trajectory filtering system is employed to selectively subsample demonstrations generated by RL policies.

### Strengths
**Highly Relevant Task**
- The problem of household rearrangement is highly relevant in robotics, and the research community greatly benefits from accessible, high-quality benchmarks. In this regard, the paper provides valuable foundational elements for future research to build upon.
- Furthermore, introducing accurate low-level control instead of relying on "magical" grasping is an important addition. For instance, using realistic initializations for the Place task by sampling grasp poses from the learned Pick policies is a compelling improvement.

**Writing**
- Overall, the writing is clear, and the logical flow of the paper effectively conveys the goals and proposed contributions. However, I noticed a few minor issues where I think the authors could improve the writing:
    - In line 213, when describing the observation space, you use the phrase "if the object/target is grasped." To enhance clarity, I suggest rephrasing it to something like "an indicator of whether the object/target is grasped".
    - In line 366, "pariwise" should be "pairwise".
    - The Open X-Embodiment reference is quite lengthy, taking up almost an entire page. To improve readability and structure, I recommend using "et al." after the first author’s name, rather than listing all the authors.

**Reproducibility**
- The code and data used in the paper are publicly available, and the experiments are described in detail.

***

Overall, the paper tackles an important problem, and making the environment code available to the research community will benefit other researchers by providing a foundation for future work.

### Weaknesses
 **Novelty**
- The primary contribution of this work is the implementation of the HAB in the ManiSkill3 simulator. While this undoubtedly makes it more efficient for researchers to work on this problem, the novelty is somewhat limited. That said, the combination of low-level manipulation and long-horizon tasks, common in household settings, is intriguing. In particular, exploring how these tasks can be integrated to mitigate hand-off issues between independent modules could add significant value. However, by studying the subtasks in isolation and replacing navigation with robot teleportation (e.g., lines 348-350), the tasks are simplified to pure manipulation problems. It’s also worth noting that ManiSkill3 already includes a drawer-opening task with the Fetch robot out-of-the-box (https://maniskill.readthedocs.io/en/latest/tasks/mobile_manipulation/index.html).

**Baseline Methods and Evaluation**
- Of the four tasks studied (Pick, Place, Open, Close), SAC and PPO are each applied to two tasks, respectively. This makes it difficult to assess the relative difficulty of the tasks or the comparative strengths of the RL methods used. While Appendix A.4.3 explains that PPO was chosen for the Open and Close tasks to enable faster wall-time training, I find this reasoning unclear, especially since SAC demonstrated superior performance in both per-object and all-object grasping tasks. Given that the Open and Close tasks are not trivially solved, with success rates still below 90%, a structured evaluation of both SAC and PPO across all tasks would likely provide more meaningful insights.
- The rationale for using imitation learning with behavior cloning (BC) as a second baseline is unclear to me. First, since the RL teacher policies can be queried for expert actions, I would expect that using DAgger, which continually aggregates the dataset during training, would lead to better performance than relying on BC with a static dataset. The rule-based filtering of trajectories before adding them to the replay buffer in DAgger could be applied similarly here. Secondly, it’s unclear what is gained from this imitation learning step. Since the RL policies already operate from visual observations, there doesn’t appear to be any knowledge distillation that would justify the need for IL policies (for example to transfer the knowledge to a deployable observation space). If the goal is to shape behavior towards specific aspects of the RL policy’s learned behaviors to boost performance, we would expect an improvement in task success rates, which, according to Table 1, does not seem to be the case.
- The reported success rate is defined as "the percentage of trajectories that achieve success at least once in an episode" (lines 343-344). However, without a clear mechanism to infer from the used visual observations whether a subtask has been successfully completed and then halt execution, this measure seems overly optimistic. The success rate should either be measured at the end of an episode after a fixed time, or the policy should be equipped with the ability to terminate an episode when it determines that the task has been successfully completed. These adjustments would provide a more accurate reflection of the performance expected on a real system.
- While I understand that the primary focus of this work is on the simulation benchmark, incorporating real-robot transfer would greatly enhance the ability to assess how realistic the simulated rigid-body physics are in enabling low-level manipulation behaviors. This is particularly important given the claim of "realistic low-level control" made in the Conclusion. One concern I have is the classification of cumulative robot collisions exceeding 5000N as "excessive collisions." In collaborative robotics, the acceptable force range is typically an order of magnitude smaller (https://pubmed.ncbi.nlm.nih.gov/12820907/). Additionally, in lines 910-912 of the Appendix, it’s mentioned that violations of the 10000N force limit are the primary performance bottleneck in the Open and Close tasks. This raises questions about the deployability and realism of the learned manipulation behaviors.

### Questions
- In Figure 7 (Appendix A.4.3), you compare the performance of training per-object policies to that of a generalist policy capable of grasping all objects. Are the per-object policies trained concurrently, and does their combined experience total 1e7 environment samples? If each per-object policy is trained on 1e7 samples individually, it seems that the RL-All variant should also be allocated num_objects * 1e7 environment steps to ensure a fair comparison.
- You mention that by using depth images, you address a partially observable variant of the MDP (line 161). However, the policies are parameterized as MLPs following a CNN encoder. Are there any mechanisms, such as history-awareness or the concatenation of consecutive frames, to handle the partial observability? Alternatively, is there an argument that partial observability has minimal impact on the tasks being considered?

### Soundness
2

### Presentation
2

### Contribution
2
