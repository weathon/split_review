# OGBench: Benchmarking Offline Goal-Conditioned RL

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 8, 6, 6

## Abstract
Offline goal-conditioned reinforcement learning (GCRL) is a major problem in reinforcement learning (RL)
because it provides a simple, unsupervised, and domain-agnostic way to acquire diverse behaviors and representations from unlabeled data without rewards.
Despite the importance of this setting, we lack a standard benchmark that can systematically evaluate the capabilities of offline GCRL algorithms.
In this work, we propose OGBench, a new, high-quality benchmark for algorithms research in offline goal-conditioned RL.
OGBench consists of $8$ types of environments, $85$ datasets,
and reference implementations of $6$ representative offline GCRL algorithms.
We have designed these challenging and realistic environments and datasets to directly probe different capabilities of algorithms,
such as stitching, long-horizon reasoning, and the ability to handle high-dimensional inputs and stochasticity.
While representative algorithms may rank similarly on prior benchmarks,
our experiments reveal stark strengths and weaknesses in these different capabilities,
providing a strong foundation for building new algorithms.

Project page: \ogbenchwebsite

Repository: \ogbenchrepo

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
In this work the authors present OGBench, a novel benchmark for offline goal-conditioned reinforcement learning (GCRL). The authors motivate the need for such benchmark, due to the lack of a standardized evaluation suite for works in offline GCRL and the increasing interest from the research community on the topic. The authors describe the main challenges tackled with OGBench: learning from sub-optimal data, goal stitching, long-horizon reasoning and stochastic environments. To tackle these challenges, the authors describe the design principles of the benchmark and consider a wide range tasks (locomotion, manipulation and drawing) across multiple environments. Additionally, the authors collect several different datasets per environment, considering different sub-optimality conditions of the behavior policy. Finally, the authors evaluate several literature-standard algorithms in OGBench, contributing their implementation as well, and discuss their performance and other findings.

### Strengths
- **Originality**:
  - Recently, there has been an extensive push towards the development of benchmarks that focus on different aspects of reinforcement learning (e.g., for offline RL [1], [2]). However, as noted by the authors, there existed no centralized evaluation suite for algorithms in offline GCRL and the community often resorted to different set of tasks (not tailored for, making difficult to access the true performance of the proposed methods. As such, the development of a benchmark that tackles specific research issues in offline GCRL is most welcomed and, to the best of my knowledge, novel.

- **Quality**:
   - The work presented here is of high quality: the proposed benchmark contains a set of diverse tasks that address specific problems in offline GCRL research and high-quality, fine-tuned implementations of recently proposed algorithms for offline GCRL (that often surpass the performance of the original versions). Furthermore, the authors collect a wide range of datasets for each task, with different levels of sub-optimality.

- **Clarity**:
   - The current version of the work is well-written, with no major typos (that I could detect). Furthermore, the document is easy to read, with self-explanatory figures and tables. I would, however, recommend some refrain when using adjectives such as "cool" (Section 6, page 4) or "exciting" (Section 6, page 4), due to their intrinsic subjectivity.

- **Significance**:
   - This work proposes a novel benchmark for offline GCRL. Given the relevance of the topic for RL research, the work can have substantial impact by providing a standardized suite for evaluation of novel algorithms.


**References**: 

- [1] Seno, Takuma, and Michita Imai. "d3rlpy: An offline deep reinforcement learning library." Journal of Machine Learning Research 23.315 (2022): 1-20.
- [2] Fu, Justin, et al. "D4rl: Datasets for deep data-driven reinforcement learning." arXiv preprint arXiv:2004.07219 (2020).

### Weaknesses
My concerns with the current version of the work are the following (none of them particularly major):
- Currently, it is challenging to assess the varying levels of novelty present in the environments available in OGBench. Throughout Section 7, I found myself questioning whether each environment was accessible elsewhere (in another benchmark or repository) or if it was unique to this benchmark. I do understand that some tasks (e.g., AntMaze) are heavily inspired by/available in other benchmarks. It would strengthen the originality of the benchmark if the authors clarified the level of novelty in each environment.
- Currently the paper lacks any discussion about the limitations of the current benchmark and plans for future extension (for example, one potential extension could tackle robustness to data corruption as explored in [1], or integrating scenarios with multiple modalities).
- Is not clear how the five evaluation goals per task were defined or what criteria was used for their selection. Additionally, why only 5 goals? Since GC policies should be able to reach any (viable) state from any state, it is unclear why the authors selected such a set of small goals.

### Questions
Please, also refer to the questions brought up in the "Weaknesses" section.

- **1** - Why not also collect an "exploratory" dataset for the AntSoccer task? Is it due to the lack of coverage of states where the agent is dribbling the ball?
- **2** - In the locomotion and manipulation tasks, how exactly is the goal state provided to the agent? Does it also include the final pose of the agent/robot? In that case, the task goal becomes a convolution of an environmental change (for example, a set of objects in a specific location in the Scene task) and a final pose of the agent?
- **3** - I found it quite interesting the comment at the end of Section 8.2 ("this suggests that we may need to prioritize coverage much more than optimality when collecting datasets for offline GCRL in the real world") as this seems to go against the current trends in large scale collection of interaction data in robotics, where the data are collected across multiple environments/embodiments but always by expert-level demonstrators (e.g., [1]). Can the authors make any parallelism between the case of offline GCRL and other large-scale data collection efforts?


**Reference**:
- [1] Collaboration, Open-X. Embodiment, et al. "Open X-Embodiment: Robotic learning datasets and RT-X models." arXiv preprint arXiv:2310.08864 1.2 (2023).

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes a new suite of tasks for benchmarking goal-conditioned offline RL algorithms. The proposed benchmarks are built with consideration specific to the goal-conditioned navigation tasks, with an emphasis on evaluating relevant task capabilities such as stitching, long-horizon reasoning, dealing with stochastic and visual input. The tasks cover a range of difficulty levels and types, including ant and humanoid locomotion, multi-step manipulation and a painting task with an high-dimension state space entailing combinatorial search. Offline policy data are also collected with various policies to emulate the data sub optimality. The benchmark is shown to be challenging for state-of-the-art and helpful in analysing strengths and limitations on investigated task capabilities. Code and policy scripted are provided and with a minimum dependencies on open-sourced mujoco and PyTorch libraries.

### Strengths
* Well-motivated research efforts and a solid execution with many considerations customised to goal-conditioned offline RL.

* A good coverage of task variations and challenges to state-of-the-art algorithms based on different principles.

* Proper task difficulties demonstrated from the results. Could be promising to spur new algorithmic research.

* Decent writing with clear presentation and well organised flow of narratives.

### Weaknesses
 * The benchmark is motivated for the generality of goal-conditioned navigation tasks, aiming at learning transferrable representations for down-stream tasks. However, this is not reflected in the task design and experimental results. It would be better to include some functionalities to facilitate analysing and transferring the learned latent representations, with a report on a few SotA algorithms' performance on this aspect.

* The tasks seem to only challenge policies with different initial states but not the shift of transition dynamics.

### Questions
* The expert data are collected from policies trained by RL. How can we assume the policies provide sufficient optimality? Since the all the tasks are essentially planning towards a goal, would running motion planning/search algorithms with certain guarantees give better data quality?

* Can the benchmark add a study on the representation and the transferability to assess the idea of using goal-conditioned tasks as a general-purpose representation learning?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces OGBench, a comprehensive benchmark for the standardized evaluation of offline GCRL. OGBench provides a diverse range of environments and datasets, covering areas such as locomotion, manipulation, and drawing, to assess key capabilities like trajectory stitching, long-horizon reasoning, image-input handling, and managing stochasticity. The authors evaluate six offline GCRL algorithms using this benchmark, designed to highlight each algorithm's unique strengths and weaknesses across different tasks. OGBench is optimized for computational efficiency and user-friendliness, allowing researchers to easily test and refine their ideas, thereby advancing the field of offline GCRL.

### Strengths
* Offline GCRL is an important research direction, and this work addresses the current lack of a challenging and comprehensive benchmark.

* This benchmark evaluates GCRL algorithms across diverse aspects, including stitching, stochastic environments, high-dimensional control, and long-horizon control.

* The benchmark includes popular baseline results, highlighting some unsolved tasks and areas for improvement.

### Weaknesses
Some benchmark designs need further discussion or improvement.

* The evaluation seems limited to five tasks. Does this mean there are only five evaluation goals? If so, this number is restricted compared to several prior goal-conditioned tasks such as the Fetch environments.

* The design of the transparent arm in pixel-based manipulation tasks seems unrealistic. It would be better to let users choose between a transparent or solid option. Additionally, demonstrating how transparency affects performance could be helpful.

* The goal information is missing in Table 6. Is the goal in image-based tasks another image provided to the agent, or is it just a transparent bot as shown in the manipulation task figures?

* Can the benchmark support language instructions as a special type of "goal"? This would be interesting given the current research focus on LLMs.

* The stochastic task appears confined to the teleport domain. More stochastic settings that might be relevant to real-world scenarios should be explored, such as random observation perturbation during both data collection and evaluation.

* Current baselines still use MLP networks as backbones. Could the authors consider implementing more advanced architectures, such as transformers? Are there any limitations in the current tasks that more sophisticated network architectures might address?

### Questions
See the weakness part.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper contributes to offline GCRL by introducing a suite of high-quality benchmarks. These benchmarks systematically assess offline GCRL algorithms' performance in learning from suboptimal data, goal stitching, long-horizon reasoning, and handling stochasticity, providing a useful tool for advancing offline GCRL research.

### Strengths
1. They are very useful benchmarks to evaluate offline GCRL methods. 
2. The authors evaluate $6$ standard offline GCRL methods on the proposed benchmarks, establishing a solid baseline for comparison and further development.

### Weaknesses
The positioning of this paper is very similar to a previous paper - D4RL (Fu et al., 2021), which was well-known but rejected by ICLR 2021 (https://openreview.net/forum?id=px0-N3_KjA). 

This paper makes a clear contribution by providing valuable benchmarks, but it does not introduce novel ideas. However, given its potential importance to the field, I lean towards assigning a slightly positive score.

### Questions
1. It would be better to retain one or two decimal places in Table 2. In benchmarks such as D4RL (Fu et al., 2021) and offline robotics (Yang et al., 2022), the success rate/score provided by decimal places is sometimes critical for comparisons. 
2. Could the authors clarify in the paper whether a rollout is considered successful if the goal is achieved at the last state, or if any state within the rollout reaches the goal? 
3. The authors should include a mention of GOPlan (Wang et al., 2024), which applies model-based planning with a generative adversarial network as the prior policy, in the related work. Additionally, GOPlan and GoFar (Ma et al., 2022) evaluate algorithm robustness in stochastic offline GCRL settings and should be discussed in Section 5.4.


**References**

Fu, J., Kumar, A., Nachum, O., Tucker, G., \& Levine, S. (2021). D4RL: Datasets for Deep Data-Driven Reinforcement Learning. 

Ma, J. Y., Yan, J., Jayaraman, D., \& Bastani, O. (2022). Offline Goal-Conditioned Reinforcement Learning via f-Advantage Regression. NeurIPS.

Wang, M., Yang, R., Chen, X., Sun, H., Fang, M., \& Montana, G. (2024). GOPlan: Goal-conditioned Offline Reinforcement Learning by Planning with Learned Models. TMLR.

Yang, R., Lu, Y., Li, W., Sun, H., Fang, M., Du, Y., … Zhang, C. (2022). Rethinking Goal-conditioned Supervised Learning and Its Connection to Offline RL. ICLR.

### Soundness
3

### Presentation
3

### Contribution
3
