## Human Reviewer 1

### Summary
With the aim of providing a more realistic and effective RL benchmark than existing ones, enabling open-ended learning of agents in reward-free contexts (unsupervised RL), the authors propose BuildBench. This environment allows for the implementation of environments, as well as providing a suite of 50 environments to force the agent to develop reasoning skills.

### Strengths
S1. Apparently, it seems that AGI could come about through open-endedness, and therefore, implementing benchmarks that enable such types of learning is obviously relevant.

S2. The document is very comprehensive and provides extensive bibliography, allowing the author to clearly identify the need for BuildBench.

### Weaknesses
W1. The paper fails to accurately determine the limitations that exist in similar proposals in the literature, and which ones are satisfactorily resolved by BuildBench.

W2. Continuing with the previous thread, one reference published in ICML 2025 was Craftium, which was also published in RLC 2025. This platform is highly developed and allows the creation of environments for open-ended learning, procedural benchmark generation, and, in addition to multi-tasking (for CRL), it also allows for multi-agent learning.
As I see it, Craftium's scope goes beyond that of BuildBench. Not including the most recent work in the comparison undermines this study.

### Questions
Q1. What are the differences between Craftium and BuildBench? Does BuildBench include the capabilities offered by Craftium? What other possibilities does it offer?

### Soundness
3

### Presentation
3

### Contribution
1

### Rating
2

### Confidence
2

---

## Human Reviewer 2

### Summary
The paper introduces BuilderBench, a new benchmark with controllable physics-based setup for evaluating reinforcement learning (RL) agents in block stacking. Two training and evaluation protocols are proposed:
I. a multi-task self-supervised protocol, where agents learn by autonomous exploration without explicit rewards;
II. a single-task supervised protocol, where agents are trained with task-specific rewards.
The benchmark is open-sourced and includes reproducible setups and a broad set of baseline evaluations. Experiments show that while current agents perform reasonably well on simple tasks, they almost all fail on more complex structures, suggesting that current RL methods lack physical reasoning and compositional planning abilities.

### Strengths
1. The paper focus on testing the ability of generalization and learning of general principle, which is an important problem in RL.
2. The environment design is clean, interpretable, scalable, and well-controlled, allowing for clear attribution of success and failure.
3. The two complementary protocols make the benchmark relevant to multiple RL paradigms.
4. The benchmark is fast-speed and reproducible, potentially useful as a standard testbed for physical reasoning research.

### Weaknesses
1. The construct validity of the benchmark could be clearer—it is not fully demonstrated that success requires genuine physical reasoning rather than geometric features.
2. The analysis of failure modes is relatively shallow; it does not fully separate challenges of exploration, long-horizon credit assignment, and physical modeling.

### Questions
1. Could the authors clarify which aspects of the benchmark truly require reasoning about stability rather than brute-force exploration?
2. The dense reward is defined primarily by geometric distance to the target structure. Would incorporating physically meaningful quantities provide a more informative learning signal and better align the benchmark with its goal of evaluating physical reasoning?

### Soundness
2

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
4

---

## Human Reviewer 3

### Summary
This work proposes BuilderBench, a benchmark designed to advance research on agent pre-training through open-ended, interactive exploration. It tasks agents with building diverse block structures in a simulator, requiring them to learn physics, math, and long-horizon planning without external supervision.

### Strengths
1. The task designs appropriately require physical understanding and spatial reasoning, demonstrating a thoughtful integration of these elements.
2. The design principles are coherent and well founded.

### Weaknesses
1. Developing a simulator using MuJoCo does not appear to be a substantial contribution, as there already exist numerous GPU-accelerated simulators with similar capabilities.
2. The problem setup is overly simplified—the flying gripper operates in 3D space but only rotates around the z-axis (i.e., performs strictly vertical). This simplification likely explains why the reinforcement learning (RL) agents achieve rapid learning.
3. Although the title claims that the benchmark targets generalist agents, the experiments primarily evaluate standard RL algorithms with different exploration strategies. In contrast, the large language model (LLM) evaluations do not involve actual interaction or feedback from the environment, thus failing to demonstrate open-ended exploration or learning through experience.

### Questions
Is there any feedback loop designed here other than merely reward functions? How can the generalist agent explore and receive experience  in the current environment?

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
3

---

## Human Reviewer 4

### Summary
This paper presents a new benchmark called BuilderBench, specifically for evaluating generalization in reinforcement learning agents. This benchmark consists of around 50 open-ended block-building tasks like T-bock, 4-cube-packing, leaning tower, etc, that test an RL agent’s capacity to physically reason with cubes. The authors also discuss some design decisions behind the benchmark like the tasks requiring distinct skills, having a curriculum of easy to difficult tasks. A few algorithms, including ChatGPT 5 and Gemini 2.5 Pro are evaluated on BuilderBench in the single-task and multi-task regime. None of the models and algorithms evaluated show signs of success beyond the simplest setup. The paper concludes by stating that better algorithm design like hypothesis driven exploration and is required to solve the introduced benchmark.

### Strengths
1. The writing is excellent and the language is simple to follow.
2. The paper has a strong and relevant motivation to improve RL agents towards grounded reasoning and generalization.
3. The created tasks are intuitive and lie on a spectrum of easy to difficult w.r.t. current RL algorithms tested in the paper. This might help develop curriculum based learning methods.
4. The self-supervised protocol presented has the potential to push the field towards unsupervised RL research. Especially in developing hypothesis driven exploration and grounded reasoning methods for embodied agents.
5. I agree with the final takeaway message that the authors state - existing algorithms might lack the grounded reasoning and compositional abilities to solve difficult manipulation problems. This is definitely an area in RL that requires further attention and research work.

### Weaknesses
Also adding questions in this section:
1. While I highly appreciate the clear goal, simple presentation, and a well implemented RL environment, I would expect a benchmark paper to present more rigorous experimentation and conclusion - the current paper falls short of this expectation. From the perspective of science, implementing PPO & SAC, and stating that other algorithms are “out of scope for the paper” (Limitations & Conclusion, page 9) is simply not sufficient to conclude that existing research on generalization is weak (although I intuitively agree with the authors’ conclusions). I say this with utmost appreciation for the work by authors: Without rigorous quantitative benchmarking and ablatory analysis on scaling behavior (sample efficiency/compute cost analysis), this research contribution is just a little better than an open-source software release. The authors of a benchmark paper have the opportunity to evaluate multiple existing algorithms in a completely unbiased manner which a future work that push a particular algorithm and agenda might lack. Given the claim of simplicity and speed of this environment, I think it is essential to run experiments on other existing methods and present the results and analyses. I would like to see standard supervised RL benchmarks on other methods like TDMPC2 [1] (a model-based approach) and other approaches specifically developed for Compositional tasks and object centric behavior [2][3][4][5]. Several competent VLAs & LLM augmented models also have attempted to achieve grounded reasoning capabilities [10][11]. Unsupervised exploration is also covered by several notable prior works [6][7]. **Atleast one other algorithm that covers the breadth of research directions for each supervised and self-supervised protocol** would improve the contribution greatly. 
2. Can the authors concretely specify what sets apart their benchmark? Several existing works attempt to capture compositional and logical reasoning abilities in RL and robotics with simple-to-hard curriculum. Examples: FurnitureBench [9], BabyAI [12]. If there are significant novel changes, please specify why these new changes are essential and what prompted the need for an entirely new benchmark? For example, Maniskill [8] is a well established benchmark which already contains tasks like PickYCB, YCB Clutter, Stack cube, etc. Maniskill also provides demonstrations, RGBD & segmentation mask observations. What is the utility of a new benchmark when one could add more cubes and create these tasks on the current benchmarks. Please mention clearly.
3. Are demonstrations available for the tasks in this benchmark? Prior benchmarks like Maniskill [8] and FurnitureBench [9] also provide demonstrations and evaluations on generalizable Imitation learning methods which are additionally considered important approaches in the RL and robotics community. 
4. Similarly, can fast rendering of RGBD observations be made available? With the popularity of Vision Language Models and DINO style vision encoders, visual observations are an essential component for modern benchmarks.

### Questions
Please see above.

Overall I would consider this paper a weak reject since it lacks in experimentation and standard RL benchmark features such as RGBD observations and expert demonstrations. Authors, please answer my questions above and consider adding a few more benchmarks. I will revise my score if my assumptions are incorrect and/or the additional responses/experiments clarify my doubts and help improve the scientific contribution of this work.

**References**

*[1] Hansen, N., Su, H., & Wang, X. (2024). TD-MPC2: Scalable, robust world models for continuous control. In Proceedings of the International Conference on Learning Representations (ICLR 2024)*

*[2] Ghasemipour, et.al. (2022). Blocks Assemble! Learning to assemble with large-scale structured reinforcement learning. In Proceedings of the 39th International Conference on Machine Learning (ICML 2022) (pp. 7435–7469). PMLR*

*[3] Mishra, U. A. et.al. (2023). Generative skill chaining: Long-horizon skill planning with diffusion models. In Proceedings of the 7th Conference on Robot Learning (CoRL 2023)*

*[4] Shridhar, M., Manuelli, L., & Fox, D. (2021). CLIPort: What and where pathways for robotic manipulation. CoRL 2021*

*[5] Zeng, A., et al. (2021). Transporter networks: Rearranging the visual world for robotic manipulation. CoRL 2020*

*[6] Laskin, M., et al. (2021). URLB: Unsupervised Reinforcement Learning Benchmark. NeurIPS Datasets & Benchmarks*

*[7] Ecoffet, A., et al. (2021). First return, then explore (Go-Explore). Nature*

*[8] Gu, S., et.al. (2023). ManiSkill2: A unified benchmark for generalizable manipulation skills. arXiv preprint arXiv:2302.04659*

*[9] Nair, S., et.al. 2022). FurnitureBench: Reproducible real-world benchmark for long-horizon complex manipulation. Proceedings of Robotics: Science and Systems (RSS).*

*[10] Kalithasan, N., et al. (2024). Sketch-Plan-Generalize: Learning and planning with neuro-symbolic programmatic representations for inductive spatial concepts. arXiv preprint arXiv:2404.07774*

*[11] Ahn, M., et al. (2022). Do As I Can, Not As I Say (SayCan): Grounding language in robotic affordances. arXiv:2204.01691*

*[12] Chevalier-Boisvert, M., et al. (2019). BabyAI: A platform to study the sample efficiency of grounded language learning. International Conference on Learning Representations (ICLR)*

### Soundness
3

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
4