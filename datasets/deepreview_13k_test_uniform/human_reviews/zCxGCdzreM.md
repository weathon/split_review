# Kinetix: Investigating the Training of General Agents through Open-Ended Physics-Based Control Tasks

- Decision: Accept
- Scores: 8, 8, 8, 8

## Abstract
While large models trained with self-supervised learning on offline datasets have shown remarkable capabilities in text and image domains, achieving the same generalisation for agents that act in sequential decision problems remains an open challenge.
In this work, we take a step towards this goal by procedurally generating tens of millions of 2D physics-based tasks and using these to train a general reinforcement learning (RL) agent for physical control.
To this end, we introduce \kinetix: an open-ended space of physics-based RL environments that can represent tasks ranging from robotic locomotion and grasping to video games and classic RL environments, all within a unified framework.
\kinetix makes use of our novel hardware-accelerated physics engine \jaxtwod that allows us to cheaply simulate billions of environment steps during training.
Our trained agent exhibits strong physical reasoning capabilities, being able to zero-shot solve unseen human-designed environments.  Furthermore, fine-tuning this general agent on tasks of interest shows significantly stronger performance than training an RL agent \textit{tabula rasa}.  This includes solving some environments that standard RL training completely fails at.
We believe this demonstrates the feasibility of large scale, mixed-quality pre-training for online RL and we hope that \kinetix will serve as a useful framework to investigate this further.\footnote{We provide full code and models at \url{https://kinetix-env.io}.}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces Kinetix, a new 2D simulated benchmark designed for training generalist agents with capabilities in fine-grained motor control, navigation, planning, and physical reasoning. The benchmark is built on a novel hardware-accelerated physics engine called Jax2D. Kinetix enables the procedural generation of a vast amount of environments using simple shapes, joints, and thrusters, allowing for tasks that include robot locomotion, object manipulation, simple video games, and classic reinforcement learning scenarios. Each environment shares a unified objective: “make the green shape touch the blue shape without touching the red shape,” enabling zero-shot generalization to new environments within the same distribution. Experimental results show that policies trained across a wide range of environments generalize better to unseen tasks, and fine-tuning these generalist policies on new tasks yields improved performance over training from scratch. This work contributes to the development of generalist RL agents and open-ended physics-based control tasks.

### Strengths
- Kinetix provides 66 hand-designed levels while having the option to edit tasks with a graphical editor or to randomly generate more levels with rejection sampling. 
- The unified goal and dynamics within all environments encourage policies to have physical reasoning capabilities instead of merely memorizing the solution for some particular task, which is a valuable objective for researchers to pursue. 
- Kinetix provides a way to generate unlimited environments and tasks with a unified goal, objects, and dynamics, which could be of interest to multiple research communities like generalist RL policy learning, meta-learning, world modeling, spatial understanding and physics reasoning, and so on.

### Weaknesses
- The paper notes that as the generated environments increase in complexity, they may become unsolvable, which could contribute to the lower performance observed in the Large-level environments. If so, how does this impact the usability and interpretability of the benchmark results? To what extent does this affect the performance results reported in Figure 3?
- It is unclear whether the proposed benchmark supports visual observations, which are essential for training generalist policies and building agents that can operate in real-world settings.
- Although Kinetix can generate a vast range of environments, it is unclear how this benchmark would generalize to tasks or environments outside of its defined task distribution.

### Questions
See Weaknesses section. Additionally,
- The range of the y axis for the four plots on the right in Figure 5 are missing. Are these also from 0 to 1?
- How long does training take for training on 1B Kinetix environments? Would be good to see if training on such a large number of environments itself would be a bottleneck for learning generalist agents.

### Soundness
3

### Presentation
4

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
This paper introduces Jax2D physics engine, which is a reimplementation of Box2D but written in Jax, and introduce the Kinetix environment on top of Jax2D. Kinetix allows for procedurally generated open-ended environments with different robot morphologies. Authors create a self-attention-based policy and demonstrate performance zero-shot, with pretraining, and with finetuning on the target environments.

### Strengths
1. Introduces a physics engine that provides “almost entirely dynamically specified” scenes, where environments with different robot morphologies can be vmap-ed and run in parallel, which is not doable with prior Jax-based sim frameworks like Brax.

2. Paper is clearly written.

### Weaknesses
1. All environments in benchmark must fall under the goal of making green shape touch blue shape without touching red shape. This seems to mainly constrain the problem to single-step tasks, where the reward of minimizing the distance from green to blue always incentivizes progress. Was this unified goal constraint purposefully imposed by design, or was it a constraint of Jax implementation, where the reward function for all environments must be the same to be parallelizable?

2. Authors emphasized that parallelism and speed were big advantages of Jax2D. Since it is a reimplementation of Box2D, and this is a critical contribution of the paper, what are the performance gain metrics over Box2D?

3. Experiments were on multi-discrete action space with binary rewards. However, it would strengthen the argument of the paper to do experiments on more of the important features of Kinetix, such as pixel-based observations and continuous action space.

4. The state representation of the policy is very specific to the Kinetix environment suite and not very generalizable to other 2D RL problems. For instance, each entity is encoded separately and there is no scene-level encoding that is passed in as observation for the policy. Often, it is essential for a policy to understand the entire scene when predicting an action.

5. There were no supplementary materials submitted, which would have been a good opportunity to show video rollouts of the trained agent in action.

6. Experiments were mainly limited to the improvement of finetuned policies over pretrained and task-specific, trained-from-scratch policies. However, I would have liked to see more experiments that provide additional insights beyond “finetuning is mostly good” and “zero-shot mostly doesn’t work.” For instance, using Kinetix for lifelong learning, transfer learning, and cross-embodiment learning.

7. Abstract sentence seems like an oversell, given the results. “Our trained agent exhibits strong physical reasoning capabilities, being able to zero-shot solve unseen human-designed environments.” Most would also disagree with the 2D learned behaviors as “strong physical reasoning capabilities.”

8. Minor: I think the wrong citation was provided for MJX in Section 7 (that work seems to be Mujoco).

9. Minor: Experiments would benefit from some comparison to prior approaches/architectures, though this is less important given this is mainly a systems/framework paper.

### Questions
1. Kinetix enables a wide distribution of morphologies and initial environment scene configurations, but it doesn’t deviate beyond the single unified goal. How can it be expanded to also cover a wide distribution of goals and potentially even task specifications?

2. Does Kinetix support parallel pixel rendering, such as for vectorized image-based experiments?

3. Is SFL only choosing between the S, M, and L levels?

4. Are the inputs into the policy purely one-hots? (One-hot encoding for each of the polygons, thrusters, and shapes.)

5. Is the (x, y) 2D position of each polygon an input into the network? It would seem that positional embeddings not of the ordering of polygons, but their actual spatial positions, would matter a great deal in this problem.

6. In section 4, authors write that Kinetix is a deterministic setting (thus satisfying one of the conditions for using SFL). How is Kinetix deterministic, given that environments are randomized?

7. How many environments were used during training, and how many environments were held-out for zero-shot evaluation?

8. What was the generalist policy in Figure 5 trained on? A distribution of environments over all 4 tasks at their hard level?

9. Say we train an agent only trained on L levels. How does it perform on held-out levels of a different difficulty (M and S)?

10. Heatmaps were an interesting way to convey the agent’s performance. Why not simply graph the agent’s x distance from the goal, with x-axis being the training iterations?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper provides a framework for procedurally generated 2D physics-based tasks to learn an agent for physical control that can effectively transfer to tasks that involve physical control. They provide a hardware-accelerated physics engine that allows for cheap/efficient simulation to generate a mixed-quality pre-training dataset for online RL. The authors additionally provide human interpretable handmade levels in Kinetix to understand the type of tasks and interactions the agent must do. The authors show the efficacy of both zero-shot transfer to new tasks and the agent when fine-tuned on a new task. The authors evaluate their agent on classic RL environments such as Cartpole and video games like Pinball.

### Strengths
- Provide a highly efficient 2D rigid-body physics engine, leveraging JAX for scalable computation, with speedups of up to 30x when training an RL agent, allowing for 
- The learnt agent is highly effective at Zero-Shot transfer in the S and M levels that are held out, indicating the efficacy of pre-training on a wide set of procedural generation tasks. Additionally, show faster convergence/higher performance with this initialization
- Have interpretable/handmade levels to understand the performance on different sizes/difficulties of tasks.

### Weaknesses
- The JAX2D environment seems to be somewhat limited in its expressivities, modeling only 4 unique entities, which may not transfer to a wide set of domains/tasks outside of the ones studied.  
- The task/reward function seems to be fixed across all environments to collide the green and blue shaped objects, while avoiding red shapes. Additional reward shaping seems to be needed for effective training, leading to some limited applicability of generating this data at scale for any set of tasks.

### Questions
- For the environment generator, it is mentioned that there may exist unsolvable levels which automatic curriculum methods can filter out. Could you clarify what was done here?
- How does the choice of algorithm affect the performance in your benchmark. Do you anticipate releasing a dataset of transitions from Kinetics which can be used for offline 2 online RL?

### Soundness
3

### Presentation
3

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
This paper introduces Kinetix, a 2D physics-based RL environment aimed at enhancing generalization in RL agents. Leveraging the simulation, the agent is pre-trained for billions of steps, enabling zero-shot evaluation on novel tasks. Fine-tuning further improves performance, surpassing traditional RL methods. The approach integrates a transformer architecture with PPO as the core RL algorithm.

### Strengths
- The paper is well-written, organized, and straightforward.
- Extensive testing across various task complexities validates its robustness in diverse 2D environments.
- This paper has strong potential to serve as a valuable benchmark for future research.

### Weaknesses
- **Real World Tasks:** While this paper provides a strong foundation in 2D simulations, expanding its scope to assess the agent’s adaptability to real-world tasks, such as 3D simulations or complex dynamics as seen in [1,2], would enhance its practical relevance. Bridging this gap could amplify the study’s contributions, offering broader insights into real-world generalization and scalability.

- **Filtering out:** The authors mention that trivial and unsolvable levels are filtered out. What quantitative metrics were used to determine this filtering.

- **Generalizability:** The claims of generalizability might be overstated given that the tasks remain in controlled simulations. Could the authors clarify the expected limitations of deploying such an agent in real-world scenarios with unpredictable environmental factors?

### Questions
They are mentioned in the Weaknesses.

### Soundness
3

### Presentation
4

### Contribution
4
