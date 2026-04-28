# Learning Object-centric Latent Dynamics for Reinforcement Learning from Pixels

- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 5, 5, 3

## Abstract
Learning a latent dynamics model provides a task-agnostic representation of an agent’s understanding of its environment. Leveraging this knowledge for model-based reinforcement learning holds the potential to improve sample efficiency over model-free methods by learning inside imagined rollouts. Furthermore, because the latent space serves as input to behavior models, the informative representations learned by the world model facilitate efficient learning of desired skills. However, most existing methods rely on holistic representations of the environment’s state. In contrast, humans reason about objects and their interactions, forecasting how actions will affect specific parts of their surroundings. Inspired by this, we propose Slot-Attention for Object-centric Latent Dynamics (SOLD), a novel algorithm that learns object-centric dynamics models in an unsupervised manner from pixel inputs. We demonstrate that the structured latent space not only improves model interpretability but also provides a valuable input space for behavior models to reason over. Our results show that SOLD outperforms DreamerV3, a state-of-the-art model-based RL algorithm, across a range of benchmark robotic environments that evaluate for both relational reasoning and low-level manipulation capabilities.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents a new model-based RL algorithm from image observations called Slot-Attention for Object-centric Latent Dynamics (SOLD). The main novelty compared to existing MBRL methods like Dreamer is a latent space structure which promotes the learning of object-centric representations. Specifically, SOLD builds on the Slot Attention mechanism used in SAVi and OCVP (video prediction only, no control) to build the world model. The rest of the MBRL pipeline is built around the Slot Attention representations similar to the settings in DreamerV3.

The authors evaluate the SOLD algorithm mainly on a custom-made multi-object environment built on the Gym Fetch simulator. The benchmark consists of reach, push and pick-and-place tasks where multiple objects are present in the scene. Aside from the basic setting to manipulate a specific color, other more challenging variants include choosing a distinct color within the collection and choosing the reddest one among similar colors. 

Visualization of open-loop predictions demonstrate that the Slot Attention architecture effectively identifies independent moving parts in the images, including both manipulatable objects and robot body links. SOLD also outperforms DreamerV3 in policy learning in terms of sample efficiency and final policy performance. Aside from the custom benchmark specifically designed for multi-object reasoning, the authors also demonstrate the applicability of SOLD in more main-stream benchmarks including DM Control and Meta-World.

### Strengths
- The idea of learning a latent world model with an object-centric representation is sound and extending the known Slot Attention mechanism to a control setting is a good move.
- The authors created a custom-made task suite to highlight the utility of object-centric reasonings in a MBRL setting. In these tasks, SOLD outperforms the state-of-the-art MBRL method DreamerV3.
- The main method is explained pretty clearly by the equations and system diagrams.
- The visualization of the slots and attentions show that the model indeed captures the moving objects in the Fetch environment as well as Meta-World and DM Control.

### Weaknesses
 - The method is showcased mainly on a custom-made environment, where the settings are a bit detachched from reality. I think this work can shine in a cluttered manipulation environment with realistic objects. The authors touches on Meta-World and DM Control tasks, but no systematic RL comparison is included.
- The core contribution of this work seems to be only adding actions to OCVP and putting it in an RL loop. If this is the case, the contribution is a bit limited, unless more systematic studies or hardware experiments are conducted.

### Questions
- What is the inference latency of SOLD's latent world model? Dreamer's RSSM is fairly light weight.
- Aside from the parameter count, as outlined in the appendix, are there any other main difference between SOLD w/o OCE and DreamerV3? I wonder where the performance gain comes from.
- Is SOLD more sample efficient in Meta-World and DM Control tasks too?
- Could there be some special treatments if more than one camera view is used?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents SOLD, a model-based RL method designed to learn object-centric representations directly from pixels. SOLD’s focus on structuring the latent space around individual objects and their interactions is a novel take that could be especially useful for tasks like robotic manipulation, where reasoning about individual objects is crucial. Experimental results show that SOLD performs strongly, particularly in object manipulation tasks that require relational reasoning between objects from Meta-World.

### Strengths
- By breaking down the environment into individual objects, the model can reason about complex interactions more intuitively, which has clear benefits for manipulation and relational tasks.

- The paper is well-organized, and the authors do a nice job of explaining SOLD’s inner workings. Visualizations of attention patterns and slot decomposition are particularly helpful, showing how SOLD parses and tracks key objects in the scene.

- The experiments show promising adaption results state distributions and performance on multi-object tasks.

### Weaknesses
 - While SOLD performs well on DM-Control and Meta-World, its robustness would be clearer if evaluated across a broader set of RL benchmarks, such as Atari, ProcGen, or Minecraft, as well as in complex robotics environments like ManiSkill2, IsaacGym, and Robosuite. Expanding the scope of environments could better showcase SOLD’s versatility.

- An ablation study on the slot attention mechanism by replacing it with another transformer-based model rather than a CNN-based encoder-decoder would help clarify its unique impact on SOLD’s object-centric understanding and performance.

- The Slot Aggregation Transformer likely plays a significant role in capturing relational dynamics. Testing alternative transformer configurations could reveal how essential this component is for tasks that require multi-object relational reasoning.

### Questions
- Have you considered ablations to evaluate the importance of specific components, such as removing slot attention, testing alternative aggregation methods for slots? This would clarify the role of each part in SOLD’s overall performance.

- Is there a plan to test SOLD on more benchmarks, like Control Suite, Atari, or more demanding robotics tasks like ManiSkill2 or IsaacGym? These benchmarks would give a clearer sense of SOLD’s versatility and adaptability.

- Could you share detailed return scores on DM-Control?

- How did you determine the slot dimension? In the visualization of the decomposition results, a small number of slots might be enough for the various tasks you presented.

### Soundness
3

### Presentation
3

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
This paper introduces SOLD, a model-based reinforcement learning approach that learns object-centric dynamics from pixel inputs without supervision. SOLD models the world as distinct objects with interactions, inspired by human reasoning. This object-focused latent space improves interpretability and supports more efficient skill learning. Results show that SOLD outperforms DreamerV3 in robotic tasks that require both understanding relationships and precise manipulation, demonstrating the benefits of object-centric learning in reinforcement learning.

### Strengths
1. This work provides an object-centric solution for world-model training based on Slot Attention, and applies it into the following behavior learning.
2. The paper is well-written and easy to follow.

### Weaknesses
1. Missing baselines from the experiment part. More model-based RL methods beyond DreamerV3 such as TD-MPC [1], TD-MPC2 [2] can be competitive and representative baselines for this work. Additionally, more related works on model-based RL can be added.
2. Limited task domain. The paper mainly focuses on reach and pick-place tasks, which has limited diversity in the task domain. Object-centric tasks with more skills can be added, such as open/close/pull/push articulations, which poses more challenge on as object-centric representation and skill learning.

### Questions
1. I'm curious about the application of the representation on multi-task, since object-centric and task-agnostic representations can be smoothly incorporated into a multi-task setting.
2. The authors have shown fine-tuned SAVi can capture unseen state distribution by visulization of masked reconstruction. Please further demonstrate whether the fine-tuned SAVi can benefit RL training.
3. The authors only demonstrate final scores of the non-object-centric baselines. More curves, comparison with baselines and visualizations can be added for clarification.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces the use of slot attention to learn object-centric latent dynamics and employs a slot-aggregated transformer as the backbone for a reward/actor/critic model. Techniques such as register tokens and ALiBi are incorporated to enhance the performance of the model-based RL algorithm, DreamerV3. The central premise is to develop structured latent world models that differentiate various objects in a scene, thereby aiding behavior learning. Experiments across 12 simulation tasks demonstrate significant performance improvements over the original DreamerV3.

### Strengths
- The paper is well-written and organized, featuring numerous visualizations that facilitate understanding of the proposed object-centric world models.
- Experimental results indicate notable performance gains over the state-of-the-art DreamerV3 across a diverse array of robotics tasks (e.g., DM-Control, Meta-World).
- The concept of utilizing slot attention to learn structured world models is both intuitive and effectively illustrated, though I have some questions about it.

### Weaknesses
One major concern is the justification for the necessity of object-centric latent dynamics in model-based RL:

- The objectives of employing latent dynamics include (1) reducing rollout time and (2) maintaining accurate world modeling. However, the paper lacks quantitative comparisons regarding time efficiency and accuracy against DreamerV3. Specifically, there is no analysis of the computational cost associated with the slot attention mechanism and the slot-aggregated transformer, which could potentially increase rollout time despite any benefits in sample efficiency. Furthermore, the paper does not provide metrics such as prediction error or reconstruction loss to demonstrate improved world modeling accuracy compared to DreamerV3.
- The ability of the world model to handle more complex scenes remains unclear. The current tasks appear too simplistic; it is recommended to utilize more realistic simulators and diverse object tasks to assess whether the proposed method surpasses earlier models like DreamerV3. For example, the manipulation tasks involve only a few simple geometric shapes. It is unclear how the proposed method would perform in environments with more complex object geometries, textures, and lighting conditions, or with a larger number of interacting objects.
- The discussion on the additional properties of the proposed world model is insufficient. For instance, will the learned model demonstrate greater robustness to scene disturbances, such as sudden changes in background, object textures, or the number of objects? Additionally, will it model interactions between objects and manipulators more accurately? The paper does not provide any analysis of the model's behavior under such perturbations, which is crucial for assessing its practical applicability. For example, how would the model perform if the color or texture of the target object changes during the task?
- The benefits for behavior learning are not clear as well. While performance improvements in simulation tasks are shown, more insights into how object-centric dynamics contribute to this enhancement—such as increased accuracy of value estimation by critic—are suggested. The paper lacks a detailed analysis of the learned value function and how it benefits from the object-centric representation. It would be beneficial to show, for instance, that the critic's value estimates are more accurate for individual objects, leading to better policy learning.

### Questions
- What distinguishes "Ours w/o OCE" from DreamerV3? If the differences stem solely from the proposed tricks, does this imply that these tricks may be detrimental? This raises concerns about the practical implementation of all methods.
- Are tricks like EMA, spatial bins, and imagination also utilized in DreamerV3? This raises issues regarding the fairness of comparisons and, consequently, the true benefits of the proposed components.
- What is the effect of removing pre-training stage of world model? What’s the performance of DreamerV3 if pre-training its world model instead of learning from scratch?
- In Figure 6, the authors claim that SOLD discovers objects relevant to tasks. However, at the initial timesteps (e.g., t=2), the object is not discovered until the manipulator begins to interact with it (after t=3). This raises the chicken-and-egg dilemma: does object discovery drive manipulation, or vice versa? Could the authors clarify this?
- Still, regarding object discovery, can DreamerV3 or SOLD w/ CNN already discover target objects? Visualizing their attention maps using techniques like Grad-CAM could help address this concern.
- It is good to visualize slot representations in Figure 3. But it seems that SAVi could achieve similar results using videos alone, without action/reward labels. How do action/reward labels influence the representational capacity of SAVi in this context?

[1] Hansen, N., Su, H., & Wang, X. TD-MPC2: Scalable, Robust World Models for Continuous Control. In *The Twelfth International Conference on Learning Representations*.

[2] Sferrazza, C., Huang, D. M., Lin, X., Lee, Y., & Abbeel, P. (2024). Humanoidbench: Simulated humanoid benchmark for whole-body locomotion and manipulation. *arXiv preprint arXiv:2403.10506*.

### Soundness
3

### Presentation
3

### Contribution
2
