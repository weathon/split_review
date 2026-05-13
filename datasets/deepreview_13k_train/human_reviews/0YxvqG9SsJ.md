# Offline Model-Based Skill Stitching

- Decision: Reject
- Scores: 3, 3, 5

## Abstract
We study building agents capable of solving long-horizon tasks using offline model-based reinforcement learning (RL). Existing RL methods effectively learn individual skills. However, seamlessly combining these skills to tackle long-horizon tasks presents a significant challenge, as the termination state of one skill may be unsuitable for initiating the next skill, leading to cumulative distribution shifts. Previous works have studied skill stitching through online RL, which is time-consuming and raises safety concerns when learning in the real world. In this work, we propose a fully offline approach to learn skill stitching. Given that the aggregated datasets from all skills provide diverse and exploratory data, which likely includes the necessary transitions for stitching skills, we train a dynamics model designed to generalize across skills to facilitate this process. Our method employs model predictive control (MPC) to stitch adjacent skills, using an ensemble of offline dynamics models and value functions. To mitigate overestimation issues inherent in models learned offline, we introduce a conservative approach that penalizes the uncertainty in model and value predictions. Our experimental results across various benchmarks validate the effectiveness of our approach in comparison to baseline methods under offline settings.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper investigates the development of agents capable of addressing long-horizon tasks through offline model-based reinforcement learning (RL). While current RL methods excel at learning individual skills, they struggle with integrating these skills to accomplish extended tasks due to the mismatch between the termination of one skill and the initiation of another, resulting in distribution shifts. The authors propose an offline approach to skill stitching, leveraging aggregated datasets from various skills to train a dynamics model that can generalize across different skills. This model, along with an ensemble of offline dynamics models and value functions, is used to stitch adjacent skills through model predictive control (MPC). To address the overestimation issues common in offline model learning, a conservative method is introduced to penalize uncertainty in model and value predictions. The study's experimental results demonstrate the effectiveness of this approach over baseline methods in offline settings across multiple benchmarks.

### Strengths
1. This paper is written well. The method is esay to follow.
2. This work is evaluted on various domains.

### Weaknesses
1. The originality of this work is quietly limited. The idea of stitching skills based on value functions is not new; many papers have proposed similar approaches. For example, PEX [1]. Specifically, the paper does not adequately differentiate its approach from existing methods that also use value functions to guide transitions between skills or sub-tasks. The core mechanism of using a learned model to predict future states and then selecting actions based on a value function is a common paradigm, and the paper needs to more clearly articulate its novel contribution beyond simply applying this to a task-level setting.
2. A large number of baseline algorithms are missing. For example, OPAL [2] and LPD [3]. The absence of comparisons to these methods, which also address aspects of skill learning and stitching, makes it difficult to assess the true performance and novelty of the proposed approach. The paper should include a more comprehensive set of baselines, especially those that tackle similar problems, to provide a more robust evaluation.

### Questions
1. What if the model learns inaccurately in a complex environment?

2. Can you use the normalized score for the experimental results?

### Soundness
2

### Presentation
2

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
This work explores a model-based approach for offline learning of skills and their sequential stitching using only individual skill datasets, without relying on online interactions with the environment. Unlike existing skill stitching techniques based on online reinforcement learning, this approach utilizes offline data to decompose long-horizon tasks into manageable skills that can be executed sequentially. The focus is on training a dynamics model with aggregated skill datasets, enabling effective model-based planning and incorporating conservative optimization objectives to ensure robust transitions between skills during planning.

### Strengths
- The proposed offline skill stitching method is straightforward yet effective in certain environments with long-horizon tasks, enabling task completion by sequencing learned skills from offline datasets.
- Skill stitching offers a practical approach in hierarchical reinforcement learning, addressing challenges in learning tasks composed of multiple sub-tasks.

### Weaknesses
 - Lack of novelty: The proposed skill stitching method of evaluating states for stitching using the value function is not novel; it is a fundamental approach used in existing offline RL for trajectory stitching [1, 2]. A comparison with these existing offline trajectory stitching methods is required.

[1] Stitching Sub-trajectories with Conditional Diffusion Model for Goal-
Conditioned Offine RL (AAAI 2024)

[2] Model-based Trajectory Stitching for Improved Offline Reinforcement
Learning (NeurIPS 2023)

The below work also uses model-based rollouts (planning) for skill-based task planning in offline settings, similar to the proposed method.

[3] Offline Policy Learning via Skill-step Abstraction for Long-horizon Goal-Conditioned Tasks (IJCAI 2024)

- The proposed method using MPC operates by sampling possible actions and evaluating the value of the resulting states. For continuous action spaces, it requires extensive sampling and evaluation to determine the best outcome. Furthermore, in environments with stochasticity, the MPC optimization can be required at each attempt, leading to significant inefficiencies in time complexity.

- The performance gain in the Kitchen appears minimal, raising questions about whether the proposed method is effective in continuous action space settings. In the Maze Runner, the discrete action space makes the MPC method feasible. However, in complex continuous tasks like the Kitchen task, the value function evaluation may be unreliable, requiring MPC to extensively search the possible action space, which may explain the minimal performance gain observed.

- The method may not generalize well across diverse environments, especially those with dynamic or unpredictable conditions, as it relies solely on offline data without any consideration on real-time adaptability.

- The approach's effectiveness is highly dependent on the diversity of the offline datasets, as the method relies on the learned dynamics model on the aggregated offline datasets.

### Questions
- I wonder if the value function properly evaluates states that have not been visited (during stitching). As the value functions for each skill are learned distinctly, how can the value evaluation in the stitched space be accurate and reliable?
- How might the proposed method be adapted to handle low-coverage offline datasets? 
- I wonder if the authors considered any techniques to reduce the computational burden of MPC in continuous or stochastic environment?
- What potential strategies could be considered for improving generalization or adaptability to dynamic environments within the constraints of offline learning?

- Minor Typos:

line 97: over-estimate → overestimate, to match the usage elsewhere in the paper.

line 215: continous actions space → continuous action space

line 257: T(\cdot|s_t,a_t) → T_{\phi}(\codt|s_t,a_t}

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces an algorithm for skill stitching from offline data,the algorithm has two phases, an offline training phase where each skill is extracted from an offline data that contains trajectories representing the skill. And a test phase, where the dynamics model is used for MPC-based skill stitching guided by the value function. The experiments demonstrate the performance of the method in comparison with some baselines; the ablations show that the quality of the data can have a significant effect on the performance of the skill changing as well as the diversity of transitions in the training distribution.

### Strengths
1. The introduction of the offline skill stitching problem is important for real-world applications

2. The idea of using a model and planning to stitch the skills is interesting and seems a good direction for further research.

3. The method results on the maze are strong compared to the baselines.

4. The results are better than baselines in general.

### Weaknesses
1. The assumption of the availability of a dataset for each skill is a strong assumption, is there a way to relax it? For example learning diverse skills from one offline dataset? Is this possible and is there any related work that focus on this problem?

2. Training each skill separately via offline RL seems expensive and time-consuming.

3. For some hyperparameters it is not clear to me they have been chosen, for example the maximum steps of skill execution seems very problem dependent.

4. The method does not seem effective on more complicated tasks (for example in table 2 the method fails in accomplishing more than one skill regardless of the number of skills in the task), but it is still better than the baselines.

### Questions
1. For the maze experiments, can you compare to offline goal conditioned RL for example goal-conditioned IQL?

2. For the MF-stitching baseline, do you train the model-free stitching policy for each two adjacent skills?

3. How does the method perform for each skills permutation? Is it better under some permutations and worse in others?

### Soundness
2

### Presentation
3

### Contribution
2
